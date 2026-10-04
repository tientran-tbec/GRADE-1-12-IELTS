// Máy chủ giả lập Apps Script cho test Thử thách: đọc thuthach/*.json từ đĩa
const http = require('http'), path = require('path'), fs = require('fs');
const { loadGas } = require('./gas_mock');
const g = loadGas(path.join(__dirname, '..', 'code.gs'));
g.run("ADMIN_PASS='Admin@123'"); g.run('setupAdmin()');
const dir = path.join(__dirname, '..', 'thuthach');
g.setFetch(url => { const f = path.join(dir, path.basename(url)); return fs.existsSync(f) ? { getResponseCode: () => 200, getContentText: () => fs.readFileSync(f, 'utf8') } : { getResponseCode: () => 404, getContentText: () => '' }; });
http.createServer((req, res) => {
  let b = ''; req.on('data', c => b += c);
  req.on('end', () => {
    res.setHeader('Access-Control-Allow-Origin', '*'); res.setHeader('Access-Control-Allow-Headers', '*');
    if (req.method === 'OPTIONS') { res.end(); return; }
    if (req.url === '/dump') { res.setHeader('Content-Type', 'application/json'); res.end(JSON.stringify(Object.fromEntries(Object.entries(g.sheets).map(([k, v]) => [k, v.rows])))); return; }
    if (req.url === '/advance') { g.advance(+b || 0); res.end('ok'); return; }
    if (req.method === 'GET') { res.end('GRADE script OK'); return; }
    res.end(g.post(JSON.parse(b)));
  });
}).listen(+process.argv[2] || 8787, () => console.log('listening'));
