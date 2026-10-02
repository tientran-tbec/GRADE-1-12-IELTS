// Giả lập Google Apps Script (SpreadsheetApp, Utilities, ...) để kiểm thử code.gs bằng Node.
const crypto = require('crypto'), fs = require('fs'), vm = require('vm'), path = require('path');
function loadGas(file, opts) {
  opts = opts || {};
  const sheets = {};
  const props = {}, cache = {};
  let offset = 0, fetchImpl = null;
  const FDate = class extends Date { constructor(...a) { if (a.length) super(...a); else super(Date.now() + offset); } static now() { return Date.now() + offset; } };
  const nowMs = () => Date.now() + offset;
  class Range {
    constructor(sh, r, c, nr, nc) { Object.assign(this, { sh, r, c, nr: nr || 1, nc: nc || 1 }); }
    getValue() { return (this.sh.rows[this.r - 1] || [])[this.c - 1] === undefined ? '' : this.sh.rows[this.r - 1][this.c - 1]; }
    setNumberFormat() { return this; }
    clearContent() { for (let i = 0; i < this.nr; i++) for (let j = 0; j < (this.nc || 1); j++) { const row = this.sh.rows[this.r - 1 + i]; if (row) row[this.c - 1 + j] = ''; } while (this.sh.rows.length && this.sh.rows[this.sh.rows.length - 1].every(x => x === '' || x === undefined)) this.sh.rows.pop(); return this; }
    setValue(v) { while (this.sh.rows.length < this.r) this.sh.rows.push([]); this.sh.rows[this.r - 1][this.c - 1] = v; return this; }
    setValues(vs) { vs.forEach((row, i) => row.forEach((v, j) => new Range(this.sh, this.r + i, this.c + j).setValue(v))); return this; }
    getValues() { const w = this.sh.getLastColumn(); const o = []; for (let i = 0; i < this.nr; i++) { const row = []; for (let j = 0; j < (this.nc || w); j++) { const x = (this.sh.rows[this.r - 1 + i] || [])[this.c - 1 + j]; row.push(x === undefined ? '' : x); } o.push(row); } return o; }
  }
  class Sheet {
    constructor(name) { this.name = name; this.rows = []; }
    getLastRow() { return this.rows.length; }
    getLastColumn() { return this.rows.reduce((m, r) => Math.max(m, r.length), 0); }
    appendRow(a) { this.rows.push(a.slice()); }
    setFrozenRows() {}
    getRange(r, c, nr, nc) { return new Range(this, r, c, nr, nc); }
    getDataRange() { return new Range(this, 1, 1, this.rows.length, this.getLastColumn()); }
    deleteRow(n) { this.rows.splice(n - 1, 1); }
    setName(n) { this.name = n; }
  }
  const ss = {
    getSpreadsheetTimeZone: () => 'Asia/Ho_Chi_Minh',
    getSheetByName: n => sheets[n] || null,
    insertSheet: n => (sheets[n] = new Sheet(n)),
  };
  const bytes = x => typeof x === 'string' ? Buffer.from(x, 'utf8') : Buffer.from(x.map(b => (b + 256) % 256));
  const toArr = b => Array.from(b).map(v => v > 127 ? v - 256 : v);
  const ctx = {
    console, Date: FDate, Math, JSON, String, Number, Array, Object, RegExp, Error, isNaN, parseInt,
    Logger: { log: m => { if (opts.verbose) console.log('[Logger]', m); } },
    SpreadsheetApp: { openById: () => ss },
    PropertiesService: { getScriptProperties: () => ({ getProperty: k => props[k] || null, setProperty: (k, v) => { props[k] = v; } }) },
    CacheService: { getScriptCache: () => ({ get: k => (cache[k] && cache[k].exp > nowMs()) ? cache[k].v : null, put: (k, v, ttl) => { cache[k] = { v: String(v), exp: nowMs() + (ttl || 600) * 1000 }; }, remove: k => { delete cache[k]; } }) },
    UrlFetchApp: { fetch: (url, o) => fetchImpl ? fetchImpl(url, o) : { getResponseCode: () => 500, getContentText: () => '{}' } },
    LockService: { getScriptLock: () => ({ waitLock() {}, releaseLock() {} }) },
    ContentService: { MimeType: { JSON: 'json' }, createTextOutput: t => ({ text: t, mime: 'text', setMimeType(m) { this.mime = m; return this; }, getContent() { return this.text; } }) },
    Utilities: {
      DigestAlgorithm: { SHA_256: 'sha256' }, Charset: { UTF_8: 'utf8' },
      computeDigest: (alg, s) => toArr(crypto.createHash('sha256').update(bytes(s)).digest()),
      computeHmacSha256Signature: (v, k) => toArr(crypto.createHmac('sha256', k).update(bytes(v)).digest()),
      base64Encode: x => bytes(x).toString('base64'),
      base64EncodeWebSafe: x => bytes(x).toString('base64').replace(/\+/g, '-').replace(/\//g, '_'),
      base64DecodeWebSafe: s => toArr(Buffer.from(s.replace(/-/g, '+').replace(/_/g, '/'), 'base64')),
      getUuid: () => crypto.randomUUID(),
      newBlob: s => ({ getBytes: () => toArr(Buffer.from(typeof s === 'string' ? s : String(s), 'utf8')) }),
      formatDate: (d, tz, pat) => { const o = {}; new Intl.DateTimeFormat('en-GB', { timeZone: tz, hourCycle: 'h23', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' }).formatToParts(new Date(d.getTime())).forEach(p => o[p.type] = p.value);
        return String(pat).replace('yyyy', o.year).replace('MM', o.month).replace('dd', o.day).replace('HH', o.hour).replace('mm', o.minute).replace('ss', o.second); },
    },
  };
  // Blob từ byte array → getDataAsString
  ctx.Utilities.newBlob = s => {
    const buf = typeof s === 'string' ? Buffer.from(s, 'utf8') : Buffer.from(s.map(b => (b + 256) % 256));
    return { getBytes: () => toArr(buf), getDataAsString: () => buf.toString('utf8') };
  };
  vm.createContext(ctx);
  vm.runInContext(fs.readFileSync(file, 'utf8'), ctx, { filename: file });
  return {
    ctx, sheets, props, advance(ms) { offset += ms; }, setFetch(f) { fetchImpl = f; },
    post(obj) { const r = ctx.doPost({ postData: { contents: JSON.stringify(obj) } }); return r.text; },
    api(obj) { return JSON.parse(this.post(obj)); },
    run(code) { return vm.runInContext(code, ctx); },
  };
}
module.exports = { loadGas };
