// Kiểm tra máy chủ Firebase sau khi chuyển dữ liệu: đăng nhập bằng tài khoản ADMIN và đếm dữ liệu.
const readline = require('readline');
const API = process.argv[2] || 'https://asia-southeast1-lms-learning-36841.cloudfunctions.net/api';
const rl = readline.createInterface({input: process.stdin, output: process.stdout});
const ask = q => new Promise(r => rl.question(q, r));
const call = async o => { const r = await fetch(API, {method: 'POST', headers: {'Content-Type': 'text/plain;charset=UTF-8'}, body: JSON.stringify(o)}); const t = await r.text(); try { return JSON.parse(t); } catch (e) { return {ok: false, error: t.slice(0, 200)}; } };
(async () => {
  const g = await fetch(API); console.log('GET /api →', (await g.text()).slice(0, 40));
  const u = await ask('Tài khoản ADMIN: '), p = await ask('Mật khẩu: '); rl.close();
  const L = await call({action: 'auth_login', username: u, password: p, device: 'check-' + Date.now()});
  console.log('Đăng nhập:', L.ok ? 'OK (' + L.user.role + ' – ' + L.user.name + ')' : 'LỖI: ' + L.error);
  if (!L.ok) return;
  const T = L.token;
  const us = await call({action: 'adm_users', token: T, role: 'student'}); console.log('Học sinh:', us.ok === false ? us.error : (us.users || []).length);
  const ts = await call({action: 'adm_users', token: T, role: 'teacher'}); console.log('Giáo viên:', ts.ok === false ? ts.error : (ts.users || []).length);
  const cs = await call({action: 'adm_classes', token: T}); console.log('Lớp:', cs.ok === false ? cs.error : (cs.classes || []).length);
  const rs = await call({action: 'adm_results', token: T}); console.log('Kết quả (adm_results):', rs.ok === false ? rs.error : ((rs.rows || []).length + ' dòng'));
  const ov = await call({action: 'tt_overview', token: T}); console.log('Thử thách (tổng quan):', ov.ok === false ? ov.error : 'OK');
  await call({action: 'auth_logout', token: T});
})().catch(e => console.error('LỖI:', e.message));
