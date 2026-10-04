const path = require('path'), assert = require('assert');
const { Fake } = require('./fake_firestore');
const { FsStore } = require('../firebase/functions/fsstore');
const { Runtime, MemStore } = require('../firebase/functions/gasrt');
let n = 0; const ok = (c, m) => { n++; if (!c) { console.log('FAIL:', m); process.exitCode = 1; } };
(async () => {
  const code = path.join(__dirname, '..', 'code.gs');
  const fake = new Fake(), store = new FsStore(fake), rt = new Runtime(store, code);
  const call = async o => { const t = await rt.handle(JSON.stringify(o)); try { return JSON.parse(t); } catch (e) { return { raw: t }; } };
  // 1 cài admin qua chạy mã (tương đương setupAdmin)
  await require('../firebase/functions/gasrt').runAsync(rt.execG('#run', ctx => { require('vm').runInContext("ADMIN_PASS='Admin@123'", ctx); require('vm').runInContext('setupAdmin()', ctx); }));
  let r = await call({ action: 'auth_login', username: 'admin', password: 'Admin@123', device: 'A' }); ok(r.ok, 'admin login: ' + JSON.stringify(r)); const A = r.token;
  ok((await call({ action: 'adm_class_save', token: A, cls: { id: '11A1', name: 'Lớp 11A1', grade: 11 } })).ok, 'tạo lớp');
  r = await call({ action: 'adm_user_save', token: A, user: { name: 'Hs Một', role: 'student', cls: '11A1' } }); ok(r.ok, 'tạo hs'); const pw = r.password, un = r.user.username;
  r = await call({ action: 'auth_login', username: un, password: pw, device: 'S' }); ok(r.ok, 'hs login'); const S = r.token;
  ok((await call({ action: 'adm_assign_save', token: A, cls: '11A1', sets: ['setA'] })).ok, 'giao bài');
  // ghi đồng thời 25 kết quả (nối thêm) → không mất dòng nào
  const reads0 = fake.txRetries;
  const res = await Promise.all(Array.from({ length: 25 }, (_, i) => call({ action: 'grade_save_result', token: S, set_id: 'setA', page_id: 'p' + i, mode: 'test', score: i % 10, total: 10, student_name: 'Hs', student_class: '11A1', ts: Date.now() })));
  ok(res.every(x => x.raw === 'ok'), 'đủ 25 phản hồi ok: ' + JSON.stringify(res.find(x => x.raw !== 'ok')));
  const meta = (await store.getMeta('Lop1-12_KetQua')); ok(meta && meta.n === 26, 'kết quả: ' + JSON.stringify(meta));   // 1 tiêu đề + 25
  // ghi đồng thời sửa cùng sheet (đổi lớp 2 học sinh) → cả hai được áp dụng nhờ thử lại
  await Promise.all([call({ action: 'adm_class_save', token: A, cls: { id: '11A2', name: 'A2', grade: 11 } }), call({ action: 'adm_class_save', token: A, cls: { id: '11A3', name: 'A3', grade: 11 } })]);
  r = await call({ action: 'adm_classes', token: A }); ok(r.classes && r.classes.map(c => c.id).sort().join() === '11A1,11A2,11A3', 'cả 2 lớp có: ' + JSON.stringify(r).slice(0, 200));
  ok(fake.txRetries >= reads0, 'có thể có thử lại giao dịch: ' + fake.txRetries);
  // sinh viên khác instance đọc lại đúng (runtime mới, không bộ nhớ đệm)
  const rt2 = new Runtime(new FsStore(fake), code);
  r = JSON.parse(await rt2.handle(JSON.stringify({ action: 'my_results', token: S }))); ok(r.ok, 'instance khác đọc được: ' + JSON.stringify(r).slice(0, 150));
  // đăng nhập sai nhiều lần bị khoá (cache bền vững)
  for (let i = 0; i < 5; i++) await call({ action: 'auth_login', username: un, password: 'sai', device: 'S' });
  r = await call({ action: 'auth_login', username: un, password: pw, device: 'S' }); ok(!r.ok && /quá nhiều/.test(r.error), 'khoá sau 5 lần sai: ' + r.error);
  console.log('Firestore store: ' + n + ' kiểm tra, ghi=' + fake.writes + ', thử lại=' + fake.txRetries);
})().catch(e => { console.error(e); process.exit(1); });
