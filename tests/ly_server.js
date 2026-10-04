// Máy chủ giả lập Apps Script cho test Vật lí: đọc essay_key.json từ đĩa, AI giả trả JSON chấm / văn bản chat
const http = require('http'), path = require('path'), fs = require('fs');
const { loadGas } = require('./gas_mock');
const g = loadGas(path.join(__dirname, '..', 'code.gs'));
g.run("ADMIN_PASS='Admin@123'"); g.run('setupAdmin()');
g.props['GEMINI_API_KEY'] = 'gk-test';
const keyFile = path.join(__dirname, '..', 'WebBaiTap', 'Lop11', 'Ly', 'essay_key.json');
global.__last = { sys: '', text: '' };
g.setFetch((url, o) => {
  if (/essay_key/.test(url)) return { getResponseCode: () => 200, getContentText: () => fs.readFileSync(keyFile, 'utf8') };
  const p = JSON.parse(o.payload), sys = p.systemInstruction.parts[0].text, last = p.contents[p.contents.length - 1].parts.slice(-1)[0].text;
  global.__last = { sys, text: last };
  let text;
  if (/chấm bài tự luận/.test(sys)) text = '{"items":[{"i":0,"got":0.25,"note":"ổn"}],"comment":"AI nhận xét thử: viết thêm đơn vị."}';
  else text = 'Lời giải: $x=A\\cos(\\omega t)$ ; ctx=' + (sys.indexOf('BÀI LÀM CỦA HỌC SINH') >= 0 ? 'có-bài-làm' : 'không') + ' ; hỏi=' + last.slice(0, 60);
  return { getResponseCode: () => 200, getContentText: () => JSON.stringify({ candidates: [{ content: { parts: [{ text }] } }], usageMetadata: { promptTokenCount: 10, candidatesTokenCount: 5 } }) };
});
http.createServer((req, res) => {
  let b = ''; req.on('data', c => b += c);
  req.on('end', () => {
    res.setHeader('Access-Control-Allow-Origin', '*'); res.setHeader('Access-Control-Allow-Headers', '*');
    if (req.method === 'OPTIONS') { res.end(); return; }
    if (req.url === '/dump') { res.setHeader('Content-Type', 'application/json'); res.end(JSON.stringify(Object.fromEntries(Object.entries(g.sheets).map(([k, v]) => [k, v.rows])))); return; }
    if (req.url === '/last') { res.setHeader('Content-Type', 'application/json'); res.end(JSON.stringify(global.__last)); return; }
    if (req.method === 'GET') { res.end('GRADE script OK'); return; }
    res.end(g.post(JSON.parse(b)));
  });
}).listen(+process.argv[2] || 8787, () => console.log('listening'));
