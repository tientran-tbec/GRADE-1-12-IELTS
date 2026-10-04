'use strict';
/* Bộ chạy code.gs (Apps Script) trên Node + kho dữ liệu bất kỳ (Firestore / bộ nhớ).
 * Ý tưởng: code.gs chạy NGUYÊN VĂN trong sandbox; "Sheet" là bảng nằm trong bộ nhớ, nạp lười từ kho.
 * Khi code cần dữ liệu chưa nạp (sheet, ô cache, URL ngoài) → ném Need → ta nạp bất đồng bộ rồi CHẠY LẠI từ đầu
 * (chưa ghi gì nên chạy lại an toàn). Cuối cùng ghi một lần (transaction) với kiểm tra phiên bản (optimistic). */
const crypto = require('crypto'), vm = require('vm'), fs = require('fs');

const ROWS_PER_CHUNK = 500, BYTES_PER_CHUNK = 600000;
const VOLATILE_CACHE = /^(u_|uv$|asg2_|fbu_|ttf_|ttc$|ttp_|tta$|ttr_|eky_)/;   // chỉ là bộ nhớ đệm kết quả → bỏ được; các khoá còn lại (giới hạn đăng nhập, online, hạn mức AI, nhắc bài...) phải bền vững
const PERSIST_CACHE = { test: k => !VOLATILE_CACHE.test(k) };
const keyOf = n => String(n).replace(/[^A-Za-z0-9_-]/g, '_');

/* ---------- (de)serialize hàng ---------- */
function enc(rows) {
  return JSON.stringify(rows, function (k, v) {
    const raw = this[k];
    if (Object.prototype.toString.call(raw) === '[object Date]') return {$d: raw.getTime()};
    return v;
  });
}
function dec(s) { return JSON.parse(s, (k, v) => (v && typeof v === 'object' && !Array.isArray(v) && '$d' in v) ? new Date(v.$d) : v); }
function chunkify(rows) {
  const strs = [], counts = [];
  let cur = [], bytes = 0;
  const flush = () => { strs.push(enc(cur)); counts.push(cur.length); cur = []; bytes = 0; };
  for (const r of rows) {
    const b = Buffer.byteLength(enc([r]));
    if (cur.length && (cur.length >= ROWS_PER_CHUNK || bytes + b > BYTES_PER_CHUNK)) flush();
    cur.push(r); bytes += b;
  }
  if (cur.length) flush();
  return {strs, counts};
}
const maxCols = rows => rows.reduce((m, r) => Math.max(m, r.length), 0);
function planFull(rows, oldStrs, meta) {
  const {strs, counts} = chunkify(rows), writes = {}, deletes = [];
  strs.forEach((s, i) => { if (s !== oldStrs[i]) writes[i] = s; });
  for (let i = strs.length; i < Math.max(meta.nchunks || 0, oldStrs.length); i++) deletes.push(i);
  return {writes, deletes, meta: {ver: (meta.ver || 0) + 1, n: rows.length, cols: maxCols(rows), c0: counts[0] || 0, nchunks: strs.length}};
}
function planAppend(lastRows, newRows, meta) {
  const nch = meta.nchunks || 0, lastIdx = Math.max(nch - 1, 0);
  const {strs, counts} = chunkify(lastRows.concat(newRows)), writes = {};
  strs.forEach((s, i) => { writes[lastIdx + i] = s; });
  return {writes, deletes: [], meta: {ver: (meta.ver || 0) + 1, n: (meta.n || 0) + newRows.length, cols: Math.max(meta.cols || 0, maxCols(newRows)),
    c0: lastIdx === 0 ? counts[0] : meta.c0, nchunks: lastIdx + strs.length}};
}

/* ---------- kho trong bộ nhớ (dùng cho test) ---------- */
class MemStore {
  constructor(now) { this.now = now || Date.now; this.meta = {}; this.chunks = {}; this.props = {}; this.cache = {}; this.reads = 0; this.writes = 0; }
  getProps() { return JSON.parse(JSON.stringify(this.props)); }
  setPropIfAbsent(k, v) { if (!(k in this.props)) this.props[k] = v; return this.props[k]; }
  getMeta(key) { this.reads++; return this.meta[key] ? {...this.meta[key]} : null; }
  getChunks(key, head) { const a = this.chunks[key] || []; this.reads += head ? 1 : a.length; return head ? a.slice(0, 1) : a.slice(); }
  cacheGet(k) { const c = this.cache[k]; return c && c.exp > this.now() ? c.v : null; }
  cachePut(k, v, ttlSec) { this.cache[k] = {v, exp: this.now() + ttlSec * 1000}; }
  cacheDel(k) { delete this.cache[k]; }
  commit(plan) {
    for (const s of plan.sheets) { const m = this.meta[s.key]; if (s.mode === 'full' && ((m && m.ver) || 0) !== s.baseVer) return 'conflict'; }
    for (const s of plan.sheets) {
      const m = this.meta[s.key] || {ver: 0, n: 0, cols: 0, c0: 0, nchunks: 0}, arr = this.chunks[s.key] = this.chunks[s.key] || [];
      let p;
      if (s.mode === 'full') p = planFull(s.rows, s.oldStrs || [], m);
      else { const li = Math.max((m.nchunks || 0) - 1, 0); p = planAppend(m.nchunks ? dec(arr[li]) : [], s.rows, m); }
      Object.keys(p.writes).forEach(i => { arr[+i] = p.writes[i]; this.writes++; });
      p.deletes.sort((a, b) => b - a).forEach(i => arr.splice(i, 1));
      this.meta[s.key] = p.meta;
    }
    if (plan.props) Object.assign(this.props, plan.props);
    return 'ok';
  }
}

/* ---------- Need ---------- */
class Need extends Error { constructor(n) { super('NEED ' + JSON.stringify(n)); this.need = n; } }

/* ---------- trạng thái 1 request ---------- */
class Req {
  constructor(rt, props) { this.rt = rt; this.props = props; this.propsDirty = null; this.meta = {}; this.data = {}; this.ckeys = {}; this.fetchMemo = {}; this.needs = []; this.reset(); }
  reset() { this.sheets = {}; this.volatile = {}; this.cops = []; this.used = {}; this.cused = []; }
  need(n) { this.needs.push(n); throw new Need(n); }
}

/* ---------- Sheet / Range lười ---------- */
class Range {
  constructor(sh, r, c, nr, nc) { Object.assign(this, {sh, r, c, nr: nr || 1, nc: nc || 0}); }
  _w() { return this.nc || this.sh.getLastColumn(); }
  getValue() { this.sh.rd(this.r, 1); const row = this.sh.rows[this.r - 1] || []; return row[this.c - 1] === undefined ? '' : row[this.c - 1]; }
  getValues() {
    this.sh.rd(this.r, this.nr); const w = this._w(), o = [];
    for (let i = 0; i < this.nr; i++) { const row = [], src = this.sh.rows[this.r - 1 + i] || []; for (let j = 0; j < w; j++) { const x = src[this.c - 1 + j]; row.push(x === undefined ? '' : x); } o.push(row); }
    return o;
  }
  setNumberFormat() { return this; }
  setValue(v) { this.sh.wr(); const rows = this.sh.rows; while (rows.length < this.r) rows.push([]); const row = rows[this.r - 1]; while (row.length < this.c - 1) row.push(''); row[this.c - 1] = v; return this; }
  setValues(vs) { vs.forEach((row, i) => row.forEach((v, j) => new Range(this.sh, this.r + i, this.c + j, 1, 1).setValue(v))); return this; }
  clearContent() {
    this.sh.wr();
    for (let i = 0; i < this.nr; i++) for (let j = 0; j < (this.nc || 1); j++) { const row = this.sh.rows[this.r - 1 + i]; if (row) row[this.c - 1 + j] = ''; }
    const rows = this.sh.rows; while (rows.length && rows[rows.length - 1].every(x => x === '' || x === undefined)) rows.pop();
    return this;
  }
}
class Sheet {
  constructor(st, key, name, meta, created) {
    this.st = st; this.key = key; this.name = name; this.m = meta; this.created = !!created;
    this.mode = created ? 'full' : 'meta'; this.rows = []; this.appends = []; this.dirty = !!created; this.orig = 0; this.baseVer = meta.ver || 0; this.oldStrs = [];
    st.used[key] = Math.max(st.used[key] || 0, 1);
  }
  _lvl(l) { this.st.used[this.key] = Math.max(this.st.used[this.key] || 0, l); }
  _load(level) {   // 'head' | 'full'
    const d = this.st.data[this.key], src = d && (level === 'full' ? d.full : (d.head || d.full));
    if (!src || d.ver !== this.m.ver) this.st.need({kind: level, key: this.key});
    const clone = structuredClone(src.rows);
    if (level === 'full' || d.full) { this.mode = 'full'; this.rows = d.full ? structuredClone(d.full.rows) : clone; this.oldStrs = d.full ? d.full.strs : []; this.orig = this.rows.length;
      if (this.appends.length) { this.rows.push(...this.appends); this.appends = []; } this._lvl(3); }
    else { this.mode = 'head'; this.rows = clone; this._lvl(2); }
  }
  needFull() { if (this.mode !== 'full') this._load('full'); }
  rd(r, nr) {
    if (this.mode === 'full') return;
    const end = r + (nr || 1) - 1, hr = Math.min(this.m.n, this.m.c0 || 0);
    if (end <= hr || (this.m.n === (this.m.c0 || 0) && end <= this.m.n)) { if (this.mode !== 'head') this._load('head'); } else this._load('full');
  }
  wr() { this.needFull(); this.dirty = true; }
  getLastRow() { return this.mode === 'full' ? this.rows.length : this.m.n + this.appends.length; }
  getLastColumn() { return this.mode === 'full' ? maxCols(this.rows) : Math.max(this.m.cols || 0, maxCols(this.appends)); }
  appendRow(a) { if (this.mode === 'full') this.rows.push(a.slice()); else this.appends.push(a.slice()); }
  setFrozenRows() {}
  setName() {}
  getRange(r, c, nr, nc) { return new Range(this, r, c, nr, nc); }
  getDataRange() { this.needFull(); return new Range(this, 1, 1, this.rows.length, maxCols(this.rows)); }
  deleteRow(n) { this.wr(); this.rows.splice(n - 1, 1); }
}

/* ---------- Bộ chạy ---------- */
class Runtime {
  constructor(store, codePath, opts) {
    this.store = store; this.opts = opts || {};
    this.script = new vm.Script(fs.readFileSync(codePath, 'utf8'), {filename: codePath});
    this.fetchImpl = this.opts.fetchImpl || (async (url, o) => {
      const h = Object.assign({}, o.headers || {}); if (o.contentType) h['Content-Type'] = o.contentType;
      const r = await fetch(url, {method: (o.method || 'get').toUpperCase(), headers: h, body: o.payload});
      return {code: r.status, text: await r.text()};
    });
    this.hints = {};      // action → {key: level}
    this.cache = {};      // key → {ver, head, full} (bộ nhớ instance)
    this.now = this.opts.now || (() => Date.now());
    if (this.opts.Date) this.D = this.opts.Date;
  }

  buildCtx(st) {
    const rt = this;
    const bytes = x => typeof x === 'string' ? Buffer.from(x, 'utf8') : Buffer.from(x.map(b => (b + 256) % 256));
    const toArr = b => Array.from(b).map(v => v > 127 ? v - 256 : v);
    const ss = {
      getSpreadsheetTimeZone: () => 'Asia/Ho_Chi_Minh',
      getSheetByName: n => {
        const key = keyOf(n);
        if (st.sheets[key]) return st.sheets[key];
        if (!(key in st.meta)) st.need({kind: 'meta', key});
        const m = st.meta[key]; if (!m) return null;
        return (st.sheets[key] = new Sheet(st, key, n, m, false));
      },
      insertSheet: n => {
        const ex = ss.getSheetByName(n); if (ex) return ex;
        return (st.sheets[keyOf(n)] = new Sheet(st, keyOf(n), n, {ver: 0, n: 0, cols: 0, c0: 0, nchunks: 0}, true));
      },
    };
    const cacheSvc = {
      get: k => {
        k = String(k);
        if (!PERSIST_CACHE.test(k)) return (st.volatile && st.volatile[k] && st.volatile[k].exp > rt.now()) ? st.volatile[k].v : null;
        const ov = st.cops.filter(o => o.k === k).pop();
        if (ov) return ov.op === 'put' ? ov.v : null;
        if (!(k in st.ckeys)) st.need({kind: 'ckey', key: k});
        st.cused.push(k); return st.ckeys[k];
      },
      put: (k, v, ttl) => { k = String(k); v = String(v); if (PERSIST_CACHE.test(k)) st.cops.push({op: 'put', k, v, ttl: ttl || 600}); else { (st.volatile = st.volatile || {})[k] = {v, exp: rt.now() + (ttl || 600) * 1000}; } },
      remove: k => { k = String(k); if (PERSIST_CACHE.test(k)) st.cops.push({op: 'del', k}); else if (st.volatile) delete st.volatile[k]; },
    };
    const ctx = {
      console, Date: rt.D || Date, Math, JSON, String, Number, Array, Object, RegExp, Error, isNaN, parseInt, parseFloat, Boolean,
      Logger: {log: () => {}},
      SpreadsheetApp: {openById: () => ss},
      PropertiesService: {getScriptProperties: () => ({
        getProperty: k => (k in st.props ? st.props[k] : null),
        setProperty: (k, v) => { st.props[k] = String(v); (st.propsDirty = st.propsDirty || {})[k] = String(v); },
      })},
      CacheService: {getScriptCache: () => cacheSvc},
      LockService: {getScriptLock: () => ({waitLock() {}, releaseLock() {}})},
      UrlFetchApp: {fetch: (url, o) => {
        o = o || {}; const k = url + '|' + JSON.stringify(o);
        if (!(k in st.fetchMemo)) st.need({kind: 'fetch', k, url, o});
        const r = st.fetchMemo[k];
        return {getResponseCode: () => r.code, getContentText: () => r.text};
      }},
      ContentService: {MimeType: {JSON: 'json'}, createTextOutput: t => ({text: t, mime: 'text', setMimeType(m) { this.mime = m; return this; }, getContent() { return this.text; }})},
      Utilities: {
        DigestAlgorithm: {SHA_256: 'sha256'}, Charset: {UTF_8: 'utf8'},
        computeDigest: (alg, s) => toArr(crypto.createHash('sha256').update(bytes(s)).digest()),
        computeHmacSha256Signature: (v, k) => toArr(crypto.createHmac('sha256', k).update(bytes(v)).digest()),
        base64Encode: x => bytes(x).toString('base64'),
        base64EncodeWebSafe: x => bytes(x).toString('base64').replace(/\+/g, '-').replace(/\//g, '_'),
        base64DecodeWebSafe: s => toArr(Buffer.from(String(s).replace(/-/g, '+').replace(/_/g, '/'), 'base64')),
        getUuid: () => crypto.randomUUID(),
        newBlob: s => { const buf = typeof s === 'string' ? Buffer.from(s, 'utf8') : Buffer.from(s.map(b => (b + 256) % 256)); return {getBytes: () => toArr(buf), getDataAsString: () => buf.toString('utf8')}; },
        formatDate: (d, tz, pat) => {
          if (pat === 'u') { const wd = new Intl.DateTimeFormat('en-US', {timeZone: tz, weekday: 'short'}).format(new Date(d.getTime())); return String(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].indexOf(wd) + 1); }
          const p = new Intl.DateTimeFormat('en-GB', {timeZone: tz, hourCycle: 'h23', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit'}).formatToParts(new Date(d.getTime()));
          const o = {}; p.forEach(x => { o[x.type] = x.value; });
          return String(pat).replace('yyyy', o.year).replace('MM', o.month).replace('dd', o.day).replace('HH', o.hour).replace('mm', o.minute).replace('ss', o.second);
        },
      },
    };
    vm.createContext(ctx);
    this.script.runInContext(ctx);
    (this.preludes || []).forEach(c => vm.runInContext(c, ctx));
    return ctx;
  }

  * satisfy(st, needs) {
    const rt = this, seen = new Set(), list = [];
    needs.forEach(n => { const id = JSON.stringify([n.kind, n.key || n.k]); if (!seen.has(id)) { seen.add(id); list.push(n); } });
    // vòng 1: meta + ckey + fetch + meta cho head/full (song song)
    const r1 = list.map(n => {
      if (n.kind === 'ckey') return rt.store.cacheGet(n.key);
      if (n.kind === 'fetch') { try { const p = rt.fetchImpl(n.url, n.o); return (p && p.then) ? p.then(x => x, e => ({code: 599, text: String(e)})) : p; } catch (e) { return {code: 599, text: String(e)}; } }
      if (n.key in st.meta) return st.meta[n.key];
      return rt.store.getMeta(n.key);
    });
    const v1 = yield r1;
    const todo = [];
    list.forEach((n, i) => {
      if (n.kind === 'ckey') st.ckeys[n.key] = v1[i];
      else if (n.kind === 'fetch') st.fetchMemo[n.k] = v1[i];
      else { st.meta[n.key] = v1[i]; if (v1[i]) todo.push(n); }
    });
    // vòng 2: nạp dữ liệu (nếu bộ nhớ đệm của instance chưa có)
    const calls = [], plan = [];
    todo.forEach(n => {
      const m = st.meta[n.key]; let c = rt.cache[n.key]; if (c && c.ver !== m.ver) c = rt.cache[n.key] = null;
      c = c || (rt.cache[n.key] = {ver: m.ver});
      const d = st.data[n.key] = st.data[n.key] || {ver: m.ver};
      if (n.kind === 'full') { if (c.full) d.full = c.full; else { calls.push(rt.store.getChunks(n.key, false)); plan.push({n, c, d}); } }
      else if (c.head || c.full) d.head = c.head || c.full;
      else { calls.push(rt.store.getChunks(n.key, true)); plan.push({n, c, d}); }
    });
    const v2 = yield calls;
    plan.forEach((p, i) => {
      const strs = v2[i], o = {strs, rows: [].concat(...strs.map(dec))};
      if (p.n.kind === 'full') { p.c.full = o; p.d.full = o; } else { p.c.head = o; p.d.head = o; }
    });
  }

  * handleG(text) {
    let action = ''; try { action = String(JSON.parse(text).action || ''); } catch (e) { return 'error: ' + e; }
    return yield* this.execG(action, ctx => ctx.doPost({postData: {contents: text}}).text);
  }

  * execG(action, fn) {
    const store = this.store;
    for (let attempt = 0; attempt < 6; attempt++) {
      const props = yield store.getProps();
      if (!props.GN_SECRET) props.GN_SECRET = yield store.setPropIfAbsent('GN_SECRET', crypto.randomUUID() + crypto.randomUUID());
      const st = new Req(this, props);
      const hint = this.hints[action];
      if (hint) {
        yield* this.satisfy(st, Object.keys(hint).filter(k => hint[k] > 0).map(k => ({kind: 'meta', key: k})));
        yield* this.satisfy(st, Object.keys(hint).filter(k => hint[k] >= 2 && st.meta[k]).map(k => ({kind: hint[k] >= 3 ? 'full' : 'head', key: k})));
      }
      let out = null;
      for (let replay = 0; replay < 60; replay++) {
        st.reset(); st.needs = []; const ctx = this.buildCtx(st);
        try { out = fn(ctx); } catch (e) { if (!(e instanceof Need)) out = 'error: ' + e; }
        if (st.needs.length) { yield* this.satisfy(st, st.needs); continue; }
        break;
      }
      const plan = {sheets: [], props: st.propsDirty};
      for (const sh of Object.values(st.sheets)) {
        if (sh.mode === 'full' && (sh.dirty || sh.created)) plan.sheets.push({key: sh.key, name: sh.name, mode: 'full', baseVer: sh.baseVer, rows: sh.rows, oldStrs: sh.oldStrs});
        else if (sh.mode === 'full' && sh.rows.length > sh.orig) plan.sheets.push({key: sh.key, name: sh.name, mode: 'append', rows: sh.rows.slice(sh.orig)});
        else if (sh.mode !== 'full' && sh.appends.length) plan.sheets.push({key: sh.key, name: sh.name, mode: 'append', rows: sh.appends});
      }
      if (plan.sheets.length || plan.props) {
        const r = yield store.commit(plan);
        for (const s of plan.sheets) delete this.cache[s.key];
        if (r === 'conflict') continue;
      }
      for (const o of st.cops) { if (o.op === 'put') yield store.cachePut(o.k, o.v, o.ttl); else yield store.cacheDel(o.k); }
      const h = this.hints[action] = this.hints[action] || {};
      Object.keys(st.used).forEach(k => { h[k] = Math.max(h[k] || 0, st.used[k]); });
      return out;
    }
    return JSON.stringify({ok: false, error: 'Hệ thống đang bận, hãy thử lại sau ít giây.'});
  }

  handleSync(text) { return runSync(this.handleG(text)); }
  handle(text) { return runAsync(this.handleG(text)); }
  runCodeSync(code) { return runSync(this.execG('#run', ctx => vm.runInContext(code, ctx))); }
}

function runSync(gen) { let r = gen.next(); while (!r.done) r = gen.next(r.value); return r.value; }
async function runAsync(gen) {
  let r = gen.next();
  while (!r.done) {
    let v;
    try { v = await (Array.isArray(r.value) ? Promise.all(r.value) : r.value); } catch (e) { r = gen.throw(e); continue; }
    r = gen.next(v);
  }
  return r.value;
}

module.exports = {runSync, runAsync, Runtime, MemStore, Need, chunkify, planFull, planAppend, enc, dec, keyOf, PERSIST_CACHE, ROWS_PER_CHUNK};
