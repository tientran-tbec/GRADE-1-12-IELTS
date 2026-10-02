// Máy chủ giả lập Apps Script cho test e2e: node tests/gas_server.js <port>
const http = require('http'), path = require('path');
const { loadGas } = require('./gas_mock');
const g = loadGas(path.join(__dirname, '..', 'code.gs'));
g.run("ADMIN_PASS='Admin@123'"); g.run('setupAdmin()');
let delay = +process.env.DELAY_MS || 0;
http.createServer((req, res) => {
  let b = ''; req.on('data', c => b += c);
  req.on('end', () => {
    res.setHeader('Access-Control-Allow-Origin', '*'); res.setHeader('Access-Control-Allow-Headers', '*');
    if (req.method === 'OPTIONS') { res.end(); return; }
    if (req.url === '/dump') { res.setHeader('Content-Type', 'application/json'); res.end(JSON.stringify(Object.fromEntries(Object.entries(g.sheets).map(([k, v]) => [k, v.rows])))); return; }
    if (req.url.indexOf('/delay') === 0) { delay = +(req.url.split('=')[1] || 0); res.end('ok'); return; }
    if (req.method === 'GET') { res.end('GRADE script OK'); return; }
    const out = g.post(JSON.parse(b)), dl = delay;   // DELAY_MS: giả lập Apps Script chậm
    if (dl) setTimeout(() => res.end(out), dl); else res.end(out);
  });
}).listen(+process.argv[2] || 8787, () => console.log('listening'));
