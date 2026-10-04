// Giao diện giống gas_mock.loadGas nhưng chạy bằng bộ chạy Firebase (firebase/functions/gasrt.js) + MemStore.
const path = require('path');
const { Runtime, MemStore, dec, enc, planFull, chunkify } = require('../firebase/functions/gasrt');
function loadGas(file, opts) {
  opts = opts || {};
  let offset = 0, fetchImpl = null;
  const FDate = class extends Date { constructor(...a) { if (a.length) super(...a); else super(Date.now() + offset); } static now() { return Date.now() + offset; } static [Symbol.hasInstance](x) { return Object.prototype.toString.call(x) === '[object Date]'; } };
  const store = new MemStore(() => Date.now() + offset);
  const rt = new Runtime(store, file, { Date: FDate, now: () => Date.now() + offset,
    fetchImpl: (url, o) => { const r = fetchImpl ? fetchImpl(url, o) : { getResponseCode: () => 500, getContentText: () => '{}' }; return { code: r.getResponseCode(), text: r.getContentText() }; } });
  const mat = {};   // bản "vật chất hoá" để test sửa trực tiếp sheets[...].rows
  const flushMat = () => { Object.keys(mat).forEach(k => { const cur = JSON.stringify(mat[k].rows, (kk, v) => v); const fresh = [].concat(...(store.chunks[k] || []).map(dec)); if (enc(fresh) !== enc(mat[k].rows)) { const m = store.meta[k]; const p = planFull(mat[k].rows, store.chunks[k] || [], m); store.chunks[k] = chunkify(mat[k].rows).strs; store.meta[k] = p.meta; } }); };
  const reloadMat = () => { Object.keys(mat).forEach(k => { const fresh = [].concat(...(store.chunks[k] || []).map(dec)), cur = mat[k].rows; fresh.forEach((r, i) => { if (cur[i]) { cur[i].length = 0; cur[i].push(...r); } else cur[i] = r; }); cur.length = fresh.length; }); };
  const sheets = new Proxy({}, {
    get(_, name) { const k = String(name).replace(/[^A-Za-z0-9_-]/g, '_'); if (!store.meta[k]) return undefined; return mat[k] || (mat[k] = { name, rows: [].concat(...(store.chunks[k] || []).map(dec)) }); },
    ownKeys() { return Object.keys(store.meta); }, getOwnPropertyDescriptor(t, k) { return store.meta[k] ? { enumerable: true, configurable: true } : undefined; }, has(_, k) { return !!store.meta[k]; },
  });
  return {
    store, rt, sheets, props: store.props, advance(ms) { offset += ms; }, setFetch(f) { fetchImpl = f; },
    post(obj) { flushMat(); const r = rt.handleSync(JSON.stringify(obj)); reloadMat(); return r; },
    api(obj) { return JSON.parse(this.post(obj)); },
    run(code) { flushMat(); if (/^\s*[A-Za-z_$][\w$]*\s*=[^=]/.test(code)) (rt.preludes = rt.preludes || []).push(code); const r = rt.runCodeSync(code); reloadMat(); return r; },
  };
}
module.exports = { loadGas };
