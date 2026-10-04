// Chuyển dữ liệu Google Sheets → Firestore qua 2 điểm cuối HTTP (không cần khoá dịch vụ).
// Dùng:  node migrate.js <APPS_SCRIPT_URL> <EXPORT_KEY> <IMPORTER_URL> <IMPORT_KEY> [--dry] [--only=Users,Classes]
const [, , GAS, EKEY, IMP, IKEY, ...flags] = process.argv;
if (!GAS || !EKEY || !IMP || !IKEY) { console.log('node migrate.js <APPS_SCRIPT_URL> <EXPORT_KEY> <IMPORTER_URL> <IMPORT_KEY> [--dry] [--only=A,B]'); process.exit(1); }
const dry = flags.includes('--dry'), only = (flags.find(f => f.startsWith('--only=')) || '').slice(7).split(',').filter(Boolean);
const post = async (url, body) => { const r = await fetch(url, {method: 'POST', headers: {'Content-Type': 'text/plain;charset=UTF-8'}, body: JSON.stringify(body)}); const t = await r.text(); try { return JSON.parse(t); } catch (e) { return {ok: false, error: t.slice(0, 200)}; } };
const keyOf = n => String(n).replace(/[^A-Za-z0-9_-]/g, '_');
(async () => {
  const lst = await post(GAS, {action: 'export_list', key: EKEY});
  if (!lst.ok) throw new Error('export_list: ' + lst.error);
  const report = [];
  for (const s of lst.sheets) {
    if (only.length && !only.includes(s.name)) continue;
    const rows = []; let from = 1;
    for (;;) {
      const r = await post(GAS, {action: 'export_sheet', key: EKEY, name: s.name, from, count: 2000});
      if (!r.ok) throw new Error(s.name + ': ' + r.error);
      rows.push(...r.rows); from += r.rows.length;
      if (!r.rows.length || from > r.total) break;
    }
    // bỏ hàng trống ở cuối
    while (rows.length && rows[rows.length - 1].every(x => x === '' || x === null)) rows.pop();
    const check = {name: s.name, expected: s.rows, got: rows.length};
    if (!dry) {
      // gửi theo mảnh ≤ 5MB không được: replaceSheet ghi trọn sheet → gửi 1 lần (nếu quá lớn, tăng giới hạn hoặc chia sheet)
      const out = await fetch(IMP, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({key: IKEY, op: 'sheet', sheet: s.name, rows})});
      check.import = (await out.text()).slice(0, 80);
    }
    report.push(check); console.log(JSON.stringify(check));
  }
  if (!only.length) {
    const p = await post(GAS, {action: 'export_props', key: EKEY});
    if (p.ok) {
      const props = {}; Object.keys(p.props).filter(k => k !== 'EXPORT_KEY').forEach(k => { props[k] = p.props[k]; });
      console.log('thuộc tính script:', Object.keys(props).join(', '));
      if (!dry) console.log('props →', await (await fetch(IMP, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({key: IKEY, op: 'props', props})})).text());
    }
  }
  const bad = report.filter(r => r.expected !== r.got && r.expected - r.got > 1);
  console.log(bad.length ? 'LỆCH SỐ DÒNG: ' + JSON.stringify(bad) : 'Số dòng khớp.');
})().catch(e => { console.error('LỖI:', e.message); process.exit(1); });
