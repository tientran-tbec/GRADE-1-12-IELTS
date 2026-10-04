// Bản giả tối thiểu của Firestore Admin SDK (đủ cho firebase/functions/fsstore.js) để kiểm thử khi không có emulator.
class Snap { constructor(id, data) { this.id = id; this._d = data; this.exists = data !== undefined; } data() { return this._d === undefined ? undefined : structuredClone(this._d); } }
class Ref { constructor(db, col, id) { this.db = db; this.col = col; this.id = id; } get path() { return this.col + '/' + this.id; }
  async get() { await tick(); return new Snap(this.id, this.db.data[this.path]); }
  async set(d, o) { await tick(); this.db._set(this.path, d, o); this.db.writes++; }
  async delete() { await tick(); delete this.db.data[this.path]; } }
const tick = () => new Promise(r => setImmediate(r));
function merge(a, b) { const o = Object.assign({}, a); for (const k of Object.keys(b)) o[k] = (b[k] && typeof b[k] === 'object' && !(b[k] instanceof Date) && !Array.isArray(b[k]) && o[k] && typeof o[k] === 'object') ? merge(o[k], b[k]) : b[k]; return o; }
class Fake {
  constructor() { this.data = {}; this.ver = {}; this.writes = 0; this.txRetries = 0; }
  _set(p, d, o) { this.data[p] = (o && o.merge) ? merge(this.data[p] || {}, structuredClone(d)) : structuredClone(d); this.ver[p] = (this.ver[p] || 0) + 1; }
  collection(c) { const self = this; return { doc: id => new Ref(self, c, id), where: (f, op, v) => ({ get: async () => { await tick(); return { docs: Object.keys(self.data).filter(p => p.startsWith(c + '/') && self.data[p][f] === v).map(p => new Snap(p.split('/')[1], self.data[p])) }; } }) }; }
  batch() { const ops = [], self = this; return { set: (r, d) => ops.push(() => self._set(r.path, d)), delete: r => ops.push(() => { delete self.data[r.path]; }), commit: async () => { await tick(); ops.forEach(f => f()); } }; }
  async runTransaction(fn) {
    for (let tries = 0; tries < 3; tries++) {
      const readVer = {}, writes = [], self = this;
      const tx = { get: async r => { await tick(); readVer[r.path] = self.ver[r.path] || 0; return new Snap(r.id, self.data[r.path]); },
        set: (r, d, o) => writes.push(() => self._set(r.path, d, o)), delete: r => writes.push(() => { delete self.data[r.path]; self.ver[r.path] = (self.ver[r.path] || 0) + 1; }) };
      const res = await fn(tx);
      if (Object.keys(readVer).some(p => (self.ver[p] || 0) !== readVer[p])) { this.txRetries++; continue; }   // xung đột → thử lại như Firestore thật
      writes.forEach(f => f()); this.writes += writes.length; return res;
    }
    throw new Error('tx contention');
  }
}
module.exports = { Fake };
