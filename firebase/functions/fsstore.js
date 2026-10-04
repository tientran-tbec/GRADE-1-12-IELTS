'use strict';
/* Kho dữ liệu Firestore cho bộ chạy gasrt.js.
 *  gn_meta/<sheet>      {ver,n,cols,c0,nchunks}
 *  gn_data/<sheet>~<i>  {k,i,rows:"<json>"}  (≤ ~600KB/chunk)
 *  gn_meta/_props       {v:{GN_SECRET:...}}
 *  gn_cache/<key>       {v,exp,expAt}   (đặt TTL policy trên trường expAt để tự dọn) */
const {dec, planFull, planAppend, chunkify} = require('./gasrt');

class FsStore {
  constructor(db) { this.db = db; }
  mref(k) { return this.db.collection('gn_meta').doc(k); }
  cref(k, i) { return this.db.collection('gn_data').doc(k + '~' + i); }
  pref() { return this.db.collection('gn_meta').doc('_props'); }
  kref(k) { return this.db.collection('gn_cache').doc(encodeURIComponent(k).slice(0, 700)); }

  async getProps() { const s = await this.pref().get(); return s.exists ? (s.data().v || {}) : {}; }
  async setPropIfAbsent(k, v) {
    return this.db.runTransaction(async tx => {
      const s = await tx.get(this.pref()), cur = s.exists ? (s.data().v || {}) : {};
      if (cur[k]) return cur[k];
      tx.set(this.pref(), {v: {[k]: v}}, {merge: true}); return v;
    });
  }
  async getMeta(key) { const s = await this.mref(key).get(); return s.exists ? s.data() : null; }
  async getChunks(key, head) {
    if (head) { const s = await this.cref(key, 0).get(); return s.exists ? [s.data().rows] : []; }
    const q = await this.db.collection('gn_data').where('k', '==', key).get();
    return q.docs.map(d => d.data()).sort((a, b) => a.i - b.i).map(d => d.rows);
  }
  async cacheGet(k) { const s = await this.kref(k).get(); if (!s.exists) return null; const d = s.data(); return d.exp > Date.now() ? d.v : null; }
  async cachePut(k, v, ttlSec) { const exp = Date.now() + ttlSec * 1000; await this.kref(k).set({v, exp, expAt: new Date(exp + 86400000)}); }
  async cacheDel(k) { await this.kref(k).delete(); }

  async commit(plan) {
    for (let i = 0; ; i++) {
      try { return await this._commit(plan); } catch (e) {
        const abort = e && (e.code === 10 || e.code === 4 || /ABORTED|contention|DEADLINE/i.test(String(e.message || e)));
        if (!abort || i >= 9) throw e;
        await new Promise(r => setTimeout(r, 20 + Math.random() * 80 * (i + 1)));
      }
    }
  }
  async _commit(plan) {
    return this.db.runTransaction(async tx => {
      const metaSnaps = await Promise.all(plan.sheets.map(s => tx.get(this.mref(s.key))));
      const metas = metaSnaps.map(s => s.exists ? s.data() : {ver: 0, n: 0, cols: 0, c0: 0, nchunks: 0});
      const lasts = await Promise.all(plan.sheets.map((s, i) => {
        if (s.mode !== 'append' || !metas[i].nchunks) return null;
        return tx.get(this.cref(s.key, metas[i].nchunks - 1));
      }));
      for (let i = 0; i < plan.sheets.length; i++) {
        const s = plan.sheets[i];
        if (s.mode === 'full' && (metas[i].ver || 0) !== s.baseVer) return 'conflict';
      }
      for (let i = 0; i < plan.sheets.length; i++) {
        const s = plan.sheets[i], m = metas[i];
        const p = s.mode === 'full' ? planFull(s.rows, s.oldStrs || [], m) : planAppend(lasts[i] ? dec(lasts[i].data().rows) : [], s.rows, m);
        Object.keys(p.writes).forEach(idx => tx.set(this.cref(s.key, +idx), {k: s.key, i: +idx, rows: p.writes[idx]}));
        p.deletes.forEach(idx => tx.delete(this.cref(s.key, idx)));
        tx.set(this.mref(s.key), p.meta);
      }
      if (plan.props) tx.set(this.pref(), {v: plan.props}, {merge: true});
      return 'ok';
    });
  }

  /* Nhập nguyên sheet (công cụ di chuyển dữ liệu). */
  async replaceSheet(key, rows) {
    const m = (await this.getMeta(key)) || {ver: 0, nchunks: 0};
    const {strs, counts} = chunkify(rows), batch = this.db.batch();
    strs.forEach((s, i) => batch.set(this.cref(key, i), {k: key, i, rows: s}));
    for (let i = strs.length; i < (m.nchunks || 0); i++) batch.delete(this.cref(key, i));
    const cols = rows.reduce((a, r) => Math.max(a, r.length), 0);
    batch.set(this.mref(key), {ver: (m.ver || 0) + 1, n: rows.length, cols, c0: counts[0] || 0, nchunks: strs.length});
    await batch.commit();
  }
  async setProps(obj) { await this.pref().set({v: obj}, {merge: true}); }
}
module.exports = {FsStore};
