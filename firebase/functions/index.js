'use strict';
// Điểm vào Cloud Functions. POST /api (text/plain JSON {action,...}) — cùng giao thức với Apps Script cũ.
const path = require('path');
const {onRequest} = require('firebase-functions/v2/https');
const {initializeApp} = require('firebase-admin/app');
const {getFirestore} = require('firebase-admin/firestore');
const {Runtime} = require('./gasrt');
const {FsStore} = require('./fsstore');

let rt = null, fs_ = null;
function runtime() {
  if (!rt) { initializeApp(); fs_ = new FsStore(getFirestore()); rt = new Runtime(fs_, path.join(__dirname, 'code.gs')); }
  return rt;
}
const bodyText = req => (req.rawBody ? req.rawBody.toString('utf8') : (typeof req.body === 'string' ? req.body : JSON.stringify(req.body || {})));
const OPTS = {region: 'asia-southeast1', cors: true, timeoutSeconds: 60, memory: '512MiB', maxInstances: 20};

exports.api = onRequest(OPTS, async (req, res) => {
  res.set('Cache-Control', 'no-store');
  if (req.method !== 'POST') { res.type('text/plain').send('GRADE script OK'); return; }
  try {
    const t = bodyText(req);
    res.type('text/plain').send(await runtime().handle(t));
  } catch (e) { console.error(e); res.type('text/plain').send('error: ' + e); }
});

// Công cụ nhập dữ liệu từ Google Sheets (chỉ dùng lúc chuyển; khoá IMPORT_KEY đặt bằng biến môi trường, xoá sau khi xong).
exports.importer = onRequest({...OPTS, memory: '1GiB', timeoutSeconds: 300}, async (req, res) => {
  try {
    const key = process.env.IMPORT_KEY;
    const d = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
    if (!key || d.key !== key) { res.status(403).send('forbidden'); return; }
    runtime();
    if (d.op === 'sheet') { await fs_.replaceSheet(String(d.sheet).replace(/[^A-Za-z0-9_-]/g, '_'), (d.rows || []).map(r => r.map(x => (x && typeof x === 'object' && '$d' in x) ? new Date(x.$d) : x))); }
    else if (d.op === 'props') { await fs_.setProps(d.props || {}); }
    else { res.status(400).send('op?'); return; }
    res.send('ok');
  } catch (e) { console.error(e); res.status(500).send(String(e)); }
});
