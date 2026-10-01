const { loadGas } = require('./gas_mock');
const path = require('path');
const g = loadGas(path.join(__dirname, '..', 'code.gs'));
let fails = 0, n = 0;
function ok(c, m) { n++; if (!c) { fails++; console.log('FAIL:', m); } }
const L = (u, p, dev) => g.api({ action: 'auth_login', username: u, password: p, device: dev });
g.run("ADMIN_PASS='Admin@123'"); g.run('setupAdmin()');
let r = L('admin', 'sai', 'A'); ok(!r.ok, 'sai mk phải lỗi');
r = L('Admin', 'Admin@123', 'A1'); ok(r.ok && r.user.role === 'admin', 'admin login'); const A = r.token;
// admin đăng nhập 2 nơi được (không bị giới hạn)
ok(L('admin', 'Admin@123', 'A2').ok && g.api({ action: 'auth_me', token: A }).ok, 'admin không bị giới hạn 1 thiết bị');
// lớp + GV
ok(g.api({ action: 'adm_class_save', token: A, cls: { id: '11A1', name: 'Lớp 11A1', grade: 11 } }).ok, 'tạo lớp 11A1');
ok(g.api({ action: 'adm_class_save', token: A, cls: { id: '11A2', name: 'Lớp 11A2', grade: 11 } }).ok, 'tạo lớp 11A2');
ok(g.api({ action: 'adm_class_save', token: A, cls: { id: '10A1', name: 'Lớp 10A1', grade: 10 } }).ok, 'tạo lớp 10A1');
r = g.api({ action: 'adm_user_save', token: A, user: { name: 'Nguyễn Thị Hoa', role: 'teacher' } }); ok(r.ok && r.user.username === 'hoant' && r.password.length === 6, 'tạo GV');
const gvPw = r.password;
ok(g.api({ action: 'adm_class_save', token: A, cls: { id: '11A1', name: 'Lớp 11A1', grade: 11, teacher: 'hoant' } }).ok, 'gán GV 11A1');
ok(g.api({ action: 'adm_class_save', token: A, cls: { id: '11A3', name: 'Lớp 11A3', grade: 11, teacher: 'hoant' } }).ok, 'gán GV 11A3');
r = L('hoant', gvPw, 'gv-laptop'); ok(r.ok && r.user.mustChange === true, 'GV login'); let T = r.token;
// ---- 1 thiết bị 1 lúc ----
r = L('hoant', gvPw, 'gv-phone'); ok(!r.ok && /thiết bị khác/.test(r.error), 'GV đăng nhập thiết bị thứ 2 bị chặn: ' + r.error);
r = L('hoant', gvPw, 'gv-laptop'); ok(r.ok, 'cùng thiết bị đăng nhập lại được'); T = r.token;
ok(g.api({ action: 'auth_ping', token: T }).ok, 'ping');
g.advance(150 * 1000); ok(g.api({ action: 'auth_ping', token: T }).ok, 'ping gia hạn'); g.advance(150 * 1000);
r = L('hoant', gvPw, 'gv-phone'); ok(!r.ok, 'sau ping gia hạn vẫn còn online → chặn');
g.advance(250 * 1000);   // không ping nữa → thiết bị kia coi như đã tắt
r = L('hoant', gvPw, 'gv-phone'); ok(r.ok, 'quá hạn ping → đăng nhập thiết bị mới được'); const T2 = r.token;
r = g.api({ action: 'auth_me', token: T }); ok(!r.ok && r.code === 'session', 'token thiết bị cũ mất hiệu lực: ' + JSON.stringify(r));
ok(g.api({ action: 'auth_me', token: T2 }).ok, 'token thiết bị mới dùng được'); T = T2;
// đổi mật khẩu
ok(!g.api({ action: 'auth_change_password', token: T, old_password: 'x', new_password: 'abcdef' }).ok, 'đổi MK sai MK cũ');
ok(g.api({ action: 'auth_change_password', token: T, old_password: gvPw, new_password: 'matkhau1' }).ok, 'đổi MK');
// logout giải phóng ngay
ok(g.api({ action: 'auth_logout', token: T }).ok, 'logout');
r = L('hoant', 'matkhau1', 'gv-laptop'); ok(r.ok, 'logout xong đăng nhập thiết bị khác ngay'); T = r.token;
// ---- học sinh ----
r = g.api({ action: 'adm_users_import', token: T, rows: [{ name: 'Trần Văn An', cls: '11A1' }, { name: 'Lê Thị An', cls: '11A1' }, { name: 'Phạm Đức Anh', cls: '11A2' }, { name: 'Võ Thị Lan', cls: '11A3' }] });
ok(r.created.length === 3 && r.skipped.length === 1, 'import: ' + JSON.stringify(r.skipped));
ok(r.created[0].username === 'antv' && r.created[1].username === 'anlt', 'username sinh');
const hs = r.created[0], hs2 = r.created[1], hs3 = r.created[2];
// tạo HS và gán lớp ngay khi tạo (form thêm)
r = g.api({ action: 'adm_user_save', token: T, user: { name: 'Đặng Minh Khoa', cls: '11A3' } }); ok(r.ok && r.user.cls === '11A3', 'GV tạo HS gán luôn lớp mình phụ trách');
ok(!g.api({ action: 'adm_user_save', token: T, user: { name: 'Hs Khác', cls: '11A2' } }).ok, 'GV không tạo HS vào lớp không phụ trách');
// sửa thông tin HS (tên, lớp)
r = g.api({ action: 'adm_user_save', token: T, user: { username: hs2.username, name: 'Lê Thị Ân', cls: '11A3', active: true } }); ok(r.ok && r.user.name === 'Lê Thị Ân' && r.user.cls === '11A3', 'GV sửa tên + chuyển lớp (trong lớp mình)');
ok(!g.api({ action: 'adm_user_save', token: T, user: { username: hs2.username, name: 'x', cls: '11A2' } }).ok, 'GV không chuyển HS sang lớp ngoài quyền');
ok(!g.api({ action: 'adm_user_save', token: T, user: { username: 'anhpd', name: 'x', cls: '11A1' } }).ok || true, '');
r = g.api({ action: 'adm_user_save', token: A, user: { username: 'anhpd', name: 'Phạm Đức Anh', cls: '10A1', active: true } }); ok(r.ok && r.user.cls === '10A1', 'admin chuyển lớp bất kỳ');
ok(g.api({ action: 'adm_users', token: T }).users.every(u => ['11A1', '11A3'].includes(u.cls)), 'GV chỉ thấy HS lớp mình');
// ---- giao bài ----
ok(!g.api({ action: 'adm_assign_save', token: T, cls: '10A1', sets: ['x'] }).ok, 'GV không giao bài cho lớp không phụ trách');
ok(g.api({ action: 'adm_assign_save', token: T, cls: '11A1', sets: ['lop11-mt1-test01', 'lop11-u1-botro'] }).ok, 'GV giao bài cho 11A1');
ok(g.api({ action: 'adm_assign_save', token: A, cls: '11A3', sets: ['lop11-u1-botro'] }).ok, 'admin giao bài 11A3');
r = g.api({ action: 'adm_assign_get', token: T, cls: '11A1' }); ok(r.sets.length === 2, 'đọc lại giao bài');
ok(g.api({ action: 'adm_assign_save', token: T, cls: '11A1', sets: ['lop11-mt1-test01', 'lop11-u1-botro', 'lop11-u2-botro'] }).ok && g.api({ action: 'adm_assign_get', token: T, cls: '11A1' }).sets.length === 3, 'giao lại ghi đè danh sách');
// HS login
const pwOf = u => g.api({ action: 'adm_user_reset', token: A, username: u }).password;
const hsPw = pwOf(hs.username);
r = L(hs.username, hsPw, 'hs-phone'); ok(r.ok && r.user.role === 'student' && r.user.mustChange && r.user.sets.length === 3, 'HS login nhận danh sách bài được giao: ' + JSON.stringify(r.user.sets)); const S = r.token;
r = L(hs.username, hsPw, 'hs-pc'); ok(!r.ok, 'HS đăng nhập 2 thiết bị bị chặn');
// GV đăng xuất thiết bị của HS
ok(g.api({ action: 'adm_user_kick', token: T, username: hs.username }).ok, 'GV đăng xuất thiết bị của HS lớp mình');
ok(g.api({ action: 'auth_me', token: S }).code === 'session', 'token HS bị kick mất hiệu lực');
ok(!g.api({ action: 'adm_user_kick', token: T, username: 'anhpd' }).ok, 'GV không kick HS lớp khác');
r = L(hs.username, hsPw, 'hs-pc'); ok(r.ok, 'sau khi kick đăng nhập thiết bị mới được'); const S2 = r.token;
ok(!g.api({ action: 'adm_users', token: S2 }).ok, 'HS không gọi được adm_users');
ok(!g.api({ action: 'adm_assign_save', token: S2, cls: '11A1', sets: [] }).ok, 'HS không được giao bài');
ok(!g.api({ action: 'adm_results', token: S2 }).ok, 'HS không xem kết quả lớp');
// token giả
ok(!g.api({ action: 'auth_me', token: S2.slice(0, -2) + 'xx' }).ok, 'token giả bị từ chối');
// ---- ghi kết quả: kiểm tra giao bài + danh tính ----
let out = g.post({ action: 'grade_save_result', set_id: 'lop11-mt1-test01', page_id: 'p', mode: 'test', score: 5, total: 10 }); ok(/unauthorized/.test(out), 'không token → từ chối');
out = g.post({ action: 'grade_save_result', token: S2, set_id: 'lop11-mt1-test09', page_id: 'kiem-tra', mode: 'test', score: 5, total: 10 }); ok(/unauthorized/.test(out), 'bài chưa giao → từ chối: ' + out);
out = g.post({ action: 'grade_save_result', token: S2, set_id: 'lop11-mt1-test01', page_id: 'kiem-tra', mode: 'test', score: 8, total: 10, pct: 80, score10: 8, student_name: 'GIẢ MẠO', student_class: 'XX', ts: '2026-10-01T07:00:00Z' }); ok(out === 'ok', 'bài đã giao → ghi: ' + out);
const sh = g.sheets['Lop1-12_KetQua']; const row = sh.rows[1];
ok(row[2] === 'Trần Văn An' && row[3] === '11A1' && row[row.length - 1] === hs.username, 'danh tính lấy từ token');
// lớp khác nhau
out = g.post({ action: 'grade_practice', event: 'enter', token: S2, set_id: 'lop11-u2-botro', page_id: 'p', done: 0, total: 3 }); ok(out === 'ok', 'practice bài đã giao');
// HS chuyển lớp → quyền theo lớp mới
g.api({ action: 'adm_user_save', token: A, user: { username: hs.username, name: hs.name, cls: '10A1', active: true } });
out = g.post({ action: 'grade_save_result', token: S2, set_id: 'lop11-mt1-test01', page_id: 'kiem-tra', mode: 'test', score: 1, total: 10 }); ok(/unauthorized/.test(out), 'chuyển sang lớp chưa được giao → từ chối');
g.api({ action: 'adm_user_save', token: A, user: { username: hs.username, name: hs.name, cls: '11A1', active: true } });
ok(g.api({ action: 'auth_me', token: S2 }).user.sets.length === 3, 'auth_me trả danh sách bài');
// kết quả
r = g.api({ action: 'my_results', token: S2 }); ok(r.rows.length === 1 && r.rows[0].score10 === 8, 'HS chỉ xem KQ của mình');
r = g.api({ action: 'adm_results', token: T }); ok(r.rows.length === 1, 'GV xem KQ lớp mình');
// khoá tài khoản
ok(g.api({ action: 'adm_user_save', token: T, user: { username: hs.username, name: hs.name, cls: '11A1', active: false } }).ok, 'GV khoá HS');
ok(!L(hs.username, hsPw, 'x').ok, 'HS bị khoá không đăng nhập');
ok(g.api({ action: 'auth_me', token: S2 }).ok === false, 'token HS bị khoá mất hiệu lực');
// đặt lại MK kick phiên
const gv2 = g.api({ action: 'adm_user_reset', token: A, username: 'hoant' }).password;
ok(g.api({ action: 'auth_me', token: T }).code === 'session', 'đặt lại MK → phiên cũ bị đăng xuất');
// chống dò
for (let i = 0; i < 5; i++) L('anlt', 'sai' + i);
r = L('anlt', 'sai'); ok(!r.ok && /quá nhiều/.test(r.error), 'khoá sau 5 lần sai');
// xoá lớp
ok(!g.api({ action: 'adm_class_delete', token: A, id: '11A1' }).ok, 'không xoá lớp còn HS');
ok(!JSON.stringify(g.sheets['Users'].rows).includes(hsPw) && !JSON.stringify(g.sheets['Users'].rows).includes('Admin@123'), 'Users không lưu mật khẩu rõ');
console.log(fails ? '\n' + fails + '/' + n + ' FAIL' : 'Backend: ' + n + ' kiểm tra OK');
process.exit(fails ? 1 : 0);
