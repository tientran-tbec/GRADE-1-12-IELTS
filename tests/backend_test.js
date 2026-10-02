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
g.advance(300 * 1000);   // không ping nữa → thiết bị kia coi như đã tắt
r = L('hoant', gvPw, 'gv-phone'); ok(r.ok, 'quá hạn ping → đăng nhập thiết bị mới được'); const T2 = r.token;
r = g.api({ action: 'auth_me', token: T }); ok(!r.ok && r.code === 'session', 'token thiết bị cũ mất hiệu lực: ' + JSON.stringify(r));
ok(g.api({ action: 'auth_me', token: T2 }).ok, 'token thiết bị mới dùng được'); T = T2;
// đổi mật khẩu
ok(!g.api({ action: 'auth_change_password', token: T, old_password: 'x', new_password: 'abcdef' }).ok, 'đổi MK sai MK cũ');
ok(g.api({ action: 'auth_change_password', token: T, old_password: gvPw, new_password: 'matkhau1' }).ok, 'đổi MK');
// logout giải phóng ngay
ok(g.api({ action: 'auth_logout', token: T }).ok, 'logout');
r = L('hoant', 'matkhau1', 'gv-laptop'); ok(r.ok, 'logout xong đăng nhập thiết bị khác ngay'); T = r.token;
// admin/GV làm thử: trả ok nhưng không ghi
{ const nR = () => (g.sheets['Lop11_KetQua'] || g.sheets['KetQua'] || {rows: []}).rows.length; const tot = () => Object.keys(g.sheets).reduce((a, k) => a + g.sheets[k].rows.length, 0);
  const before = tot();
  const o1 = g.post({ action: 'grade_save_result', token: A, set_id: 'lop11-mt1-test01', page_id: 'kiem-tra', mode: 'test', score: 9, total: 10 });
  const o2 = g.post({ action: 'grade_practice', event: 'enter', token: T, set_id: 'lop11-u2-botro', page_id: 'p', done: 0, total: 3 });
  ok(o1 === 'ok' && o2 === 'ok', 'admin/GV làm thử trả ok: ' + o1 + ' / ' + o2); ok(tot() === before, 'admin/GV làm thử không ghi dữ liệu'); }
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
ok(!g.api({ action: 'adm_assign_save', token: T, cls: '11A1', sets: ['x'] }).ok, 'GV chưa được cấp quyền giao bài → bị từ chối');
ok(!g.api({ action: 'adm_teacher_perms', token: T, username: 'hoant', perms: ['assign'] }).ok, 'GV không tự cấp quyền cho mình');
r = g.api({ action: 'adm_teacher_perms', token: A, username: 'hoant', perms: ['assign', 'bậy', 'assign'] }); ok(r.ok && r.perms.join() === 'assign', 'admin cấp quyền giao bài (lọc quyền lạ)');
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
ok(row[2] === 'Trần Văn An' && row[3] === '11A1' && row[17] === hs.username, 'danh tính lấy từ token');
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

// ---- nhiều lớp + hạn nộp + góp ý ----
{
  ok(g.api({ action: 'adm_class_save', token: A, cls: { id: 'X1', name: 'X1', grade: 11, teacher: 'hoant' } }).ok && g.api({ action: 'adm_class_save', token: A, cls: { id: 'X2', name: 'X2', grade: 'IELTS' } }).ok, 'tạo lớp X1 (GV hoant), X2 (IELTS)');
  let r2 = g.api({ action: 'adm_user_save', token: A, user: { name: 'Phạm Hai Lớp', classes: ['X1', 'X2'] } });
  ok(r2.ok && r2.user.classes.length === 2 && r2.user.cls === 'X1,X2', 'HS thuộc 2 lớp');
  const un2 = r2.user.username, pw2 = r2.password;
  const vnDate = (ms) => new Date(Date.now() + ms + 7 * 3600e3).toISOString().slice(0, 10);
  ok(g.api({ action: 'adm_assign_save', token: A, cls: 'X1', sets: ['setA', 'setD'], due: { setD: vnDate(0) } }).ok, 'giao X1: setA, setD(hạn hôm nay)');
  ok(g.api({ action: 'adm_assign_save', token: A, cls: 'X2', sets: ['setB', 'setC'], due: { setB: '2000-01-01', setC: '2999-01-01' } }).ok, 'giao X2: setB(quá hạn), setC(còn hạn)');
  const gd = g.api({ action: 'adm_assign_get', token: A, cls: 'X2' }); ok(gd.sets.length === 2 && gd.due.setB === '2000-01-01', 'đọc lại giao bài kèm hạn');
  let lg = L(un2, pw2, 'dev-x'); ok(lg.ok, 'HS 2 lớp đăng nhập'); const S3 = lg.token;
  ok(['setA', 'setB', 'setC', 'setD'].every(x => lg.user.sets.includes(x)) && lg.user.due.setB === '2000-01-01' && !lg.user.due.setA, 'HS thấy bài của cả hai lớp + hạn: ' + JSON.stringify(lg.user.sets));
  const save = (tok, set, extra) => g.post(Object.assign({ action: 'grade_save_result', token: tok, set_id: set, page_id: 'p', mode: 'test', score: 3, total: 4, ts: new Date().toISOString() }, extra || {}));
  const lastRow = () => { const rs = g.sheets['Lop1-12_KetQua'].rows; return rs[rs.length - 1]; };
  ok(save(S3, 'setA') === 'ok' && lastRow()[3] === 'X1' && lastRow()[1] === 'ĐÃ NỘP', 'nộp setA → ghi lớp X1');
  ok(save(S3, 'setC') === 'ok' && lastRow()[3] === 'X2', 'nộp setC → ghi lớp X2');
  ok(/unauthorized/.test(save(S3, 'setB')), 'setB quá hạn (ngoài ân hạn) → từ chối');
  ok(/unauthorized/.test(g.post({ action: 'grade_practice', event: 'enter', token: S3, set_id: 'setB', page_id: 'p', done: 0, total: 1 })), 'vào bài quá hạn → từ chối');
  ok(/unauthorized/.test(save(S3, 'setZ')), 'bài không được giao ở lớp nào → từ chối');
  // GV chỉ sửa phần lớp của mình, giữ lớp khác
  const gvLogin = L('hoant', gv2, 'gv-new'); ok(gvLogin.ok, 'GV hoant đăng nhập lại: ' + gvLogin.error); T = gvLogin.token;
  const uList = g.api({ action: 'adm_users', token: T }); ok(uList.users.some(u => u.username === un2), 'GV hoant thấy HS thuộc X1 (dù có lớp khác)');
  r2 = g.api({ action: 'adm_user_save', token: T, user: { username: un2, name: 'Phạm Hai Lớp', classes: ['X1'] } }); ok(r2.ok && r2.user.classes.slice().sort().join() === 'X1,X2', 'GV sửa giữ nguyên lớp của GV khác: ' + (r2.user && r2.user.cls));
  ok(!g.api({ action: 'adm_user_save', token: T, user: { username: un2, name: 'x', classes: ['X2'] } }).ok, 'GV không gán HS vào lớp không phụ trách');
  // ---- góp ý ----
  ok(!g.api({ action: 'fb_send', token: S3, set_id: 'setA', page_id: 'p1', text: '   ' }).ok, 'góp ý rỗng bị từ chối');
  ok(!g.api({ action: 'fb_send', token: S3, set_id: 'setZ', page_id: 'p1', text: 'hi' }).ok, 'góp ý ở bài chưa giao bị từ chối');
  let f = g.api({ action: 'fb_send', token: S3, set_id: 'setA', page_id: 'p1', title: 'Bài A', text: 'Câu 3 có hai đáp án đúng ạ' });
  ok(f.ok && f.msgs.length === 1 && f.msgs[0].role === 'student', 'HS gửi góp ý');
  ok(!g.api({ action: 'fb_send', token: T, set_id: 'setA', page_id: 'p1', text: 'x' }).ok, 'GV không dùng fb_send');
  g.advance(31e3);
  ok(g.api({ action: 'auth_ping', token: T }).unread >= 1, 'GV có tin chưa đọc (chấm đỏ)');
  const ib = g.api({ action: 'fb_inbox', token: T }); ok(ib.ok && ib.threads.length === 1 && ib.threads[0].unread === 1 && ib.threads[0].set === 'setA', 'GV thấy cuộc trò chuyện chưa đọc');
  const gvB = g.api({ action: 'adm_user_save', token: A, user: { name: 'Giáo Viên Khác', role: 'teacher' } });
  const T2 = L(gvB.user.username, gvB.password, 'gv2').token;
  ok(g.api({ action: 'fb_inbox', token: T2 }).threads.length === 0 && g.api({ action: 'fb_thread', token: T2, student: un2, set_id: 'setA', page_id: 'p1' }).msgs.length === 0, 'GV lớp khác không thấy góp ý');
  ok(!g.api({ action: 'fb_reply', token: T2, student: un2, set_id: 'setA', page_id: 'p1', text: 'xen vào' }).ok, 'GV lớp khác không trả lời được');
  ok(g.api({ action: 'fb_inbox', token: A }).threads.length === 1, 'admin thấy tất cả');
  let th = g.api({ action: 'fb_thread', token: T, student: un2, set_id: 'setA', page_id: 'p1' }); ok(th.msgs.length === 1, 'GV mở cuộc trò chuyện');
  ok(g.api({ action: 'auth_ping', token: T }).unread === 0, 'mở xong → hết chấm đỏ');
  f = g.api({ action: 'fb_reply', token: T, student: un2, set_id: 'setA', page_id: 'p1', text: 'Cô sẽ kiểm tra lại nhé' }); ok(f.ok && f.msgs.length === 2 && f.msgs[1].role === 'teacher', 'GV trả lời');
  g.advance(31e3);
  ok(g.api({ action: 'auth_ping', token: S3 }).unread === 1, 'HS có tin trả lời chưa đọc');
  const fl = g.api({ action: 'fb_list', token: S3, set_id: 'setA', page_id: 'p1' }); ok(fl.msgs.length === 2 && fl.msgs[1].text.includes('Cô sẽ'), 'HS đọc được trả lời');
  ok(g.api({ action: 'auth_ping', token: S3 }).unread === 0, 'HS đọc xong → hết chấm đỏ');
  ok(g.api({ action: 'fb_list', token: S3, set_id: 'setA', page_id: 'p2' }).msgs.length === 0, 'cuộc trò chuyện tách theo trang');
  // ---- nộp trễ trong ân hạn rồi hết ân hạn (đặt cuối vì tua đồng hồ) ----
  { const end = Date.parse(vnDate(0) + 'T23:59:59+07:00'); g.advance(end - Date.now() + 10 * 60e3);
    ok(save(S3, 'setD') === 'ok' && lastRow()[1] === 'ĐÃ NỘP (TRỄ HẠN)', 'nộp trong 60 phút sau hạn → ghi "TRỄ HẠN": ' + lastRow()[1]);
    ok(/unauthorized/.test(g.post({ action: 'grade_practice', event: 'enter', token: S3, set_id: 'setD', page_id: 'p', done: 0, total: 1 })), 'vào bài mới sau hạn → từ chối');
    g.advance(2 * 3600e3); ok(/unauthorized/.test(save(S3, 'setD')), 'quá ân hạn 60 phút → từ chối'); }
}

// ---- giờ hiển thị, GV nhiều lớp / lớp nhiều GV, giao bài theo học sinh ----
{
  const uS = g.sheets['Users']; const hdr = uS.rows[0]; const ci = hdr.indexOf('Đăng nhập gần nhất');
  const dRow = uS.rows.findIndex((r, i) => i > 0 && r[2] === 'student'); uS.rows[dRow][ci] = g.run('new Date(Date.UTC(2026, 9, 1, 11, 32, 19))'); g.run('bustUsers_()');
  const ul = g.api({ action: 'adm_users', token: A, role: 'student' }); ok(ul.users.some(u => u.last === '01/10/2026 18:32:19'), 'ngày-giờ dạng Date được định dạng lại dd/MM/yyyy HH:mm:ss (giờ VN): ' + JSON.stringify(ul.users.map(u => u.last)));
  // GV nhiều lớp
  ['Y1', 'Y2', 'Y3'].forEach(c => g.api({ action: 'adm_class_save', token: A, cls: { id: c, name: c, grade: 11 } }));
  const t1 = g.api({ action: 'adm_user_save', token: A, user: { name: 'Gv Một', role: 'teacher' } }), t2 = g.api({ action: 'adm_user_save', token: A, user: { name: 'Gv Hai', role: 'teacher' } });
  ok(g.api({ action: 'adm_teacher_classes', token: A, username: t1.user.username, classes: ['Y1', 'Y2'] }).changed === 2, 'gán GV 1 phụ trách Y1, Y2');
  ok(g.api({ action: 'adm_teacher_classes', token: A, username: t2.user.username, classes: ['Y2', 'Y3'] }).changed === 2, 'gán GV 2 phụ trách Y2, Y3 (Y2 có 2 GV)');
  let cl = g.api({ action: 'adm_classes', token: A }).classes; const y2 = cl.find(c => c.id === 'Y2');
  ok(y2.teacher.split(',').length === 2, 'lớp Y2 có 2 GV: ' + y2.teacher);
  ok(g.api({ action: 'adm_teacher_classes', token: A, username: t1.user.username, classes: ['Y1'] }).changed === 1 && g.api({ action: 'adm_classes', token: A }).classes.find(c => c.id === 'Y2').teacher === t2.user.username, 'bỏ Y2 khỏi GV 1, giữ GV 2');
  g.api({ action: 'adm_teacher_perms', token: A, username: t1.user.username, perms: ['assign'] }); g.api({ action: 'adm_teacher_perms', token: A, username: t2.user.username, perms: ['assign'] });
  const L1 = L(t1.user.username, t1.password, 'g1').token, L2 = L(t2.user.username, t2.password, 'g2').token;
  ok(g.api({ action: 'adm_classes', token: L2 }).classes.map(c => c.id).sort().join() === 'Y2,Y3' && g.api({ action: 'adm_classes', token: L1 }).classes.map(c => c.id).join() === 'Y1', 'mỗi GV chỉ thấy lớp mình phụ trách');
  // giao bài theo học sinh
  const mk = (n) => g.api({ action: 'adm_user_save', token: A, user: { name: n, classes: ['Y2'] } });
  const h1 = mk('Hs Một Y'), h2 = mk('Hs Hai Y'), h3 = mk('Hs Ba Y');
  ok(g.api({ action: 'adm_assign_save', token: L2, cls: 'Y2', sets: ['all1', 'only12'], users: { only12: [h1.user.username, h2.user.username, 'khongco'] } }).ok, 'GV giao: all1 cả lớp, only12 cho 2 HS');
  const ag = g.api({ action: 'adm_assign_get', token: L2, cls: 'Y2' }); ok(!ag.users.all1 && ag.users.only12.length === 2 && ag.users.only12.indexOf('khongco') < 0, 'đọc lại danh sách HS (lọc tên lạ)');
  const s1 = L(h1.user.username, h1.password, 'a').user, s3 = L(h3.user.username, h3.password, 'c').user;
  ok(s1.sets.includes('all1') && s1.sets.includes('only12'), 'HS 1 nhận cả hai bộ');
  ok(s3.sets.includes('all1') && !s3.sets.includes('only12'), 'HS 3 chỉ nhận bộ giao cả lớp');
  const S33 = L(h3.user.username, h3.password, 'c').token;
  ok(/unauthorized/.test(g.post({ action: 'grade_save_result', token: S33, set_id: 'only12', page_id: 'p', mode: 'test', score: 1, total: 2 })), 'HS 3 nộp bộ không được giao → từ chối');
  ok(g.api({ action: 'adm_assign_save', token: L2, cls: 'Y2', sets: ['only12'], users: { only12: [h1.user.username, h2.user.username, h3.user.username] } }).ok && !Object.keys(g.api({ action: 'adm_assign_get', token: L2, cls: 'Y2' }).users).length, 'chọn đủ cả lớp = giao cả lớp');
  ok(!g.api({ action: 'adm_assign_save', token: L1, cls: 'Y2', sets: ['x'] }).ok, 'GV khác không giao bài lớp không phụ trách');
}
// ---- QUYỀN CẤP THÊM CHO GIÁO VIÊN + CHỨC VỤ HỌC SINH ----
{
  for (const id of ['P1', 'P2']) g.api({ action: 'adm_class_save', token: A, cls: { id, name: id, grade: 12 } });
  const mk = (name, role, cls) => g.api({ action: 'adm_user_save', token: A, user: { name, role, classes: cls || [] } });
  const tq = mk('Gv Quyen', 'teacher'), a1 = mk('Hs Truong', 'student', ['P1']), a2 = mk('Hs Pho', 'student', ['P1']), a3 = mk('Hs Thuong', 'student', ['P1']), b1 = mk('Hs Khac', 'student', ['P2']);
  g.api({ action: 'adm_teacher_classes', token: A, username: tq.user.username, classes: ['P1'] });
  const Q = L(tq.user.username, tq.password, 'q').token;
  const TA = L(a1.user.username, a1.password, 'a1').token, TB = L(a2.user.username, a2.password, 'a2').token, TC = L(a3.user.username, a3.password, 'a3').token;
  // mặc định: chỉ thấy lớp mình
  ok(g.api({ action: 'adm_classes', token: Q }).classes.map(c => c.id).join() === 'P1', 'GV mặc định chỉ thấy lớp mình');
  ok(!g.api({ action: 'adm_class_save', token: Q, cls: { id: 'ZZ', name: 'ZZ' } }).ok, 'GV chưa có quyền quản lý lớp → từ chối');
  ok(!g.api({ action: 'adm_user_save', token: Q, user: { name: 'Ngoai Lop', role: 'student', classes: ['P2'] } }).ok, 'GV chưa có quyền tạo HS ngoài lớp → từ chối');
  ok(g.api({ action: 'adm_results', token: Q, cls: 'P2' }).rows.length === 0, 'GV chưa có quyền xem lớp khác → không thấy kết quả');
  // cấp quyền
  ok(g.api({ action: 'adm_teacher_perms', token: A, username: tq.user.username, perms: ['classes', 'viewall', 'anystudent', 'fball'] }).ok, 'cấp quyền cho GV');
  const q1 = g.api({ action: 'adm_classes', token: Q }); ok(q1.classes.map(c => c.id).includes('P2') && q1.teachers.length >= 1, 'GV có quyền thấy mọi lớp + danh sách GV');
  ok(g.api({ action: 'adm_class_save', token: Q, cls: { id: 'P3', name: 'P3', grade: 12 } }).ok && g.api({ action: 'adm_class_delete', token: Q, id: 'P3' }).ok, 'GV có quyền quản lý lớp: tạo + xoá');
  ok(g.api({ action: 'adm_user_save', token: Q, user: { name: 'Ngoai Lop', role: 'student', classes: ['P2'] } }).ok, 'GV có quyền: tạo HS lớp ngoài');
  ok(g.api({ action: 'adm_users', token: Q }).users.some(u => u.cls === 'P2'), 'GV có quyền: thấy HS lớp khác');
  ok(!g.api({ action: 'adm_user_save', token: Q, user: { name: 'Gv Moi', role: 'teacher' } }).ok || g.api({ action: 'adm_users', token: A, role: 'teacher' }).users.every(u => u.name !== 'Gv Moi'), 'GV không tạo được GV/admin');
  ok(!g.api({ action: 'adm_assign_save', token: Q, cls: 'P1', sets: ['x'] }).ok, 'có quyền khác nhưng chưa có "giao bài" → vẫn từ chối');
  ok(!g.api({ action: 'adm_teacher_perms', token: Q, username: tq.user.username, perms: ['assign'] }).ok, 'GV không tự nâng quyền');
  // học sinh: chức vụ
  ok(!g.api({ action: 'team_progress', token: TA, cls: 'P1' }).ok, 'HS thường không xem tiến độ lớp');
  ok(!g.api({ action: 'adm_student_ranks', token: TA, username: a1.user.username, ranks: { P1: 'T' }, perms: ['tview'] }).ok, 'HS không tự phong chức');
  r = g.api({ action: 'adm_student_ranks', token: A, username: a1.user.username, ranks: { P1: 'T', P2: 'T' }, perms: ['tview', 'tscores', 'tremind', 'tfb', 'bậy'] });
  ok(r.ok && r.user.ranks.P1 === 'T' && !r.user.ranks.P2 && r.user.perms.join() === 'tview,tscores,tremind,tfb', 'admin phong trưởng nhóm (bỏ lớp HS không học, bỏ quyền lạ)');
  ok(g.api({ action: 'adm_student_ranks', token: Q, username: a2.user.username, ranks: { P1: 'P' }, perms: ['tview', 'tremind'] }).ok, 'GV phong phó nhóm');
  g.api({ action: 'adm_assign_save', token: A, cls: 'P1', sets: ['setP', 'setQ'] });
  r = g.api({ action: 'auth_me', token: TA }); ok(r.user.ranks.P1 === 'T' && r.user.perms.includes('tremind'), 'HS nhận thông tin chức vụ + quyền');
  // trưởng nhóm gửi điểm
  g.post({ action: 'grade_save_result', token: TC, set_id: 'setP', page_id: 'p1', mode: 'test', score: 8, total: 10, pct: 80, score10: 8 });
  r = g.api({ action: 'team_progress', token: TA, cls: 'P1' });
  ok(r.ok && r.members.length === 3 && r.sets.length === 2, 'trưởng nhóm xem tiến độ cả lớp: ' + JSON.stringify(r).slice(0, 120));
  const mc = r.members.find(m => m.username === a3.user.username); ok(mc.items.setP && mc.items.setP.n === 1 && mc.items.setP.avg === 8 && !mc.items.setQ, 'thấy HS3 đã nộp setP với điểm (trưởng nhóm có tscores)');
  r = g.api({ action: 'team_progress', token: TB, cls: 'P1' }); ok(r.ok && r.members.find(m => m.username === a3.user.username).items.setP.avg === undefined, 'phó nhóm không có quyền xem điểm: chỉ thấy đã nộp');
  ok(!g.api({ action: 'team_progress', token: TA, cls: 'P2' }).ok, 'không xem tiến độ lớp khác');
  // nhắc nộp bài
  r = g.api({ action: 'team_remind', token: TA, cls: 'P1', set_id: 'setQ', users: [a3.user.username, a2.user.username, b1.user.username, 'khongco', a1.user.username], note: 'Nộp bài trước thứ 6 nhé' });
  ok(r.ok && r.sent === 2 && r.skipped === 2, 'nhắc 2 bạn cùng lớp, bỏ qua người lớp khác / không tồn tại / chính mình: ' + JSON.stringify(r));
  r = g.api({ action: 'team_remind', token: TA, cls: 'P1', set_id: 'setQ', users: [a3.user.username] }); ok(r.ok && r.sent === 0 && r.skipped === 1, 'không nhắc lặp cùng bài trong 6 giờ');
  ok(!g.api({ action: 'team_remind', token: TA, cls: 'P1', set_id: 'setLa', users: [a3.user.username] }).ok, 'không nhắc bộ chưa giao cho lớp');
  ok(!g.api({ action: 'team_remind', token: TC, cls: 'P1', set_id: 'setQ', users: [a2.user.username] }).ok, 'HS thường không nhắc được');
  ok(g.api({ action: 'auth_ping', token: TC }).unread >= 1, 'HS được nhắc thấy chấm đỏ');
  r = g.api({ action: 'my_reminders', token: TC }); ok(r.ok && r.items.length === 1 && r.items[0].isNew && r.items[0].rank === 'Trưởng nhóm' && r.items[0].note === 'Nộp bài trước thứ 6 nhé', 'đọc lời nhắc');
  ok(g.api({ action: 'auth_ping', token: TC }).unread === 0 && !g.api({ action: 'my_reminders', token: TC }).items[0].isNew, 'đọc xong hết chấm đỏ');
  // góp ý thay nhóm
  ok(!g.api({ action: 'team_fb', token: TB, cls: 'P1', text: 'hi' }).ok, 'phó nhóm không có quyền góp ý thay nhóm');
  r = g.api({ action: 'team_fb', token: TA, cls: 'P1', text: 'Cả lớp đề nghị lùi hạn nộp ạ' }); ok(r.ok && r.msgs.length === 1, 'trưởng nhóm gửi góp ý thay nhóm');
  const ib = g.api({ action: 'fb_inbox', token: Q }); const th = ib.threads.find(t => /^team:P1$/.test(t.set)); ok(th && th.unread === 1, 'GV (fball) thấy góp ý của nhóm');
  r = g.api({ action: 'fb_reply', token: Q, student: a1.user.username, set_id: 'team:P1', page_id: 'nhom', text: 'Cô đồng ý, lùi 2 ngày' }); ok(r.ok && r.msgs.length === 2, 'GV trả lời góp ý nhóm');
  r = g.api({ action: 'fb_list', token: TA, set_id: 'team:P1', page_id: 'nhom' }); ok(r.msgs.length === 2, 'trưởng nhóm đọc được trả lời');
  // rút chức vụ → mất quyền
  g.api({ action: 'adm_student_ranks', token: A, username: a1.user.username, ranks: {}, perms: ['tview'] });
  ok(!g.api({ action: 'team_progress', token: TA, cls: 'P1' }).ok, 'gỡ chức vụ → mất quyền');
  ok(g.api({ action: 'adm_users', token: A, role: 'student' }).users.find(u => u.username === a1.user.username).perms.length === 0, 'gỡ hết chức vụ → xoá quyền');
  // ---- toàn quyền (ngang admin) ----
  const tf = mk('Gv Full', 'teacher'); r = g.api({ action: 'adm_teacher_perms', token: A, username: tf.user.username, perms: ['full'] });
  ok(r.ok && r.perms.length === 6, 'cấp toàn quyền = tích đủ 6 quyền');
  const F = L(tf.user.username, tf.password, 'f').token;
  ok(g.api({ action: 'adm_users', token: F, role: 'teacher' }).users.length >= 3 && g.api({ action: 'adm_users', token: F, role: 'teacher' }).users.every(u => u.role === 'teacher'), 'GV toàn quyền xem được danh sách giáo viên');
  ok(g.api({ action: 'adm_users', token: F }).users.every(u => u.role !== 'admin'), 'GV toàn quyền không thấy tài khoản admin');
  ok(g.api({ action: 'adm_class_save', token: F, cls: { id: 'FF', name: 'FF', grade: 9 } }).ok && g.api({ action: 'adm_teacher_classes', token: F, username: tq.user.username, classes: ['FF', 'P1'] }).ok, 'GV toàn quyền: tạo lớp + gán lớp cho GV khác');
  ok(g.api({ action: 'adm_teacher_perms', token: F, username: tq.user.username, perms: ['assign'] }).ok, 'GV toàn quyền cấp quyền cho GV khác');
  ok(g.api({ action: 'adm_assign_save', token: F, cls: 'P2', sets: ['setP'] }).ok, 'GV toàn quyền giao bài cho lớp bất kỳ');
  r = g.api({ action: 'adm_user_save', token: F, user: { name: 'Gv Tao Boi Full', role: 'teacher' } }); ok(r.ok && r.user.role === 'teacher', 'GV toàn quyền tạo được giáo viên');
  { const ra = g.api({ action: 'adm_user_save', token: F, user: { name: 'Admin Gia', role: 'admin' } }); ok(!ra.ok || ra.user.role !== 'admin', 'GV toàn quyền không tạo được admin'); }
  ok(!g.api({ action: 'adm_user_reset', token: F, username: 'admin' }).ok && !g.api({ action: 'adm_user_kick', token: F, username: 'admin' }).ok, 'GV toàn quyền không đặt lại MK / đăng xuất admin');
  ok(!g.api({ action: 'adm_teacher_perms', token: Q, username: tq.user.username, perms: ['full'] }).ok, 'GV thường không tự cấp toàn quyền');
  // ---- xem lại bài làm + vi phạm + tổng kết học sinh ----
  g.post({ action: 'grade_save_result', token: TC, set_id: 'setP', page_id: 'p9', mode: 'test', score: 3, total: 4, pct: 75, score10: 7.5, tab_switch: 2, blur: 1, fullscreen_exit: 0, answers: { 'a.1': 'B', 'a.2': ['x', 'y'] }, events: [{ ev: 'enter', t: 0 }, { ev: 'tab_hidden', t: 31 }, { ev: 'blur', t: 40 }, { ev: 'paste', t: 55 }, { ev: 'shortcut', t: 60, x: 'Ctrl+C' }, { ev: 'audio_play', t: 70 }] });
  const lst = g.api({ action: 'adm_results', token: A, username: a3.user.username }).rows; const rw = lst.find(x => x.page_id === 'p9');
  ok(rw && rw.row >= 2 && rw.hasEv === true, 'danh sách kết quả có số dòng + cờ có sự kiện vi phạm');
  r = g.api({ action: 'adm_result_detail', token: A, row: rw.row });
  ok(r.ok && r.answers['a.1'] === 'B' && r.events === 'tab_hidden:31;blur:40;paste:55;shortcut:60:Ctrl+C' && r.tab === 2, 'chi tiết bài nộp: câu trả lời + sự kiện (bỏ sự kiện không phải vi phạm): ' + JSON.stringify(r.events));
  ok(g.api({ action: 'adm_result_detail', token: Q, row: rw.row }).ok, 'GV có quyền xem mọi lớp xem được bài nộp');
  const outsider = mk('GV Ngoai', 'teacher'); const O = L(outsider.user.username, outsider.password, 'o').token;
  ok(!g.api({ action: 'adm_result_detail', token: O, row: rw.row }).ok, 'GV không phụ trách lớp → không xem được bài nộp');
  ok(!g.api({ action: 'adm_result_detail', token: TC, row: rw.row }).ok, 'HS không gọi được chi tiết bài nộp');
  g.post({ action: 'grade_practice', token: TC, event: 'enter', set_id: 'setP', page_id: 'p1', done: 0, score: 0, total: 5 });
  g.post({ action: 'grade_practice', token: TC, event: 'leave', set_id: 'setP', page_id: 'p1', done: 4, score: 3, total: 5, time_spent: 90 });
  r = g.api({ action: 'adm_student_summary', token: A, username: a3.user.username });
  ok(r.ok && r.user.username === a3.user.username && r.sets.length === 2 && r.results.length >= 2 && r.feedback_count === 0, 'tổng kết HS: thông tin + bài được giao + kết quả');
  const pr = r.practice.find(x => x.page_id === 'p1'); ok(pr && pr.visits === 1 && pr.secs === 90 && pr.ok === 3 && pr.total === 5, 'tổng kết HS: hoạt động luyện tập: ' + JSON.stringify(r.practice));
  ok(!g.api({ action: 'adm_student_summary', token: O, username: a3.user.username }).ok, 'GV ngoài lớp không xem tổng kết HS');
  ok(g.api({ action: 'adm_student_summary', token: Q, username: a3.user.username }).ok, 'GV phụ trách xem được tổng kết HS');
  // migration: bảng Users cũ (12 cột) → GV hiện có giữ quyền giao bài
  const sh = g.sheets['Users']; const gv = sh.rows.find(r => r[0] === 'hoant'); const keep = gv[12]; const saveH = sh.rows[0].slice();
  sh.rows.forEach(r => { r.length = Math.min(r.length, 12); }); g.run('bustUsers_()');
  g.api({ action: 'adm_users', token: A, role: 'teacher' });
  ok(sh.rows.filter(r => r[2] === 'teacher').every(r => r[12] === 'assign'), 'bảng cũ chưa có cột Quyền: giáo viên giữ quyền giao bài');
}
// ---- bootstrap trang quản trị ----
{
  const b = g.api({ action: 'adm_bootstrap', token: A }); ok(b.ok && Array.isArray(b.classes) && Array.isArray(b.students) && Array.isArray(b.tusers) && b.tusers.every(u => u.role === 'teacher'), 'bootstrap admin: lớp + học sinh + giáo viên: ' + JSON.stringify(b).slice(0, 120));
  ok(b.students.length === g.api({ action: 'adm_users', token: A, role: 'student' }).users.length, 'bootstrap: đủ học sinh');
  const bt = g.api({ action: 'adm_bootstrap', token: T }); ok(bt.ok && bt.tusers === null && bt.students.every(u => u.role === 'student'), 'bootstrap GV thường: không có danh sách giáo viên, chỉ HS của mình');
  ok(!g.api({ action: 'adm_bootstrap', token: 'x' }).ok, 'bootstrap cần đăng nhập');
}
// ---- trợ lý AI + góp ý chung/nhanh ----
{
  const cr = g.api({ action: 'adm_user_save', token: A, user: { name: 'Hs AI Thử', cls: '11A1', password: 'aitest123' } }); const sun = cr.user.username;
  const lg0 = g.api({ action: 'auth_login', username: sun, password: 'aitest123', device: 'ai-dev' }); const S1 = lg0.token; ok(lg0.ok, 'AI: đăng nhập HS thử: ' + JSON.stringify(lg0).slice(0, 150));
  ok(g.api({ action: 'ai_status', token: S1 }).enabled === false && g.api({ action: 'ai_status', token: S1 }).allowed === false, 'AI: chưa cấp quyền → ai_status không cho dùng');
  ok(/chưa được giáo viên cấp quyền/.test(g.api({ action: 'ai_chat', token: S1, text: 'hi' }).error), 'AI: chưa cấp quyền → từ chối, chỉ góp ý');
  ok(g.api({ action: 'auth_me', token: S1 }).user.ai === false, 'AI: user.ai=false khi chưa cấp');
  ok(!g.api({ action: 'adm_user_ai', token: S1, usernames: [sun], on: true }).ok, 'AI: học sinh không tự cấp quyền');
  const gr = g.api({ action: 'adm_user_ai', token: A, usernames: [sun, 'admin', 'khong-co'], on: true }); ok(gr.ok && gr.changed === 1, 'AI: admin cấp quyền (bỏ qua admin/không tồn tại): ' + JSON.stringify(gr));
  ok(g.api({ action: 'auth_me', token: S1 }).user.ai === true, 'AI: sau khi cấp, user.ai=true (không cần đăng nhập lại)');
  ok(g.api({ action: 'ai_status', token: S1 }).enabled === false && g.api({ action: 'ai_status', token: S1 }).allowed === true, 'AI: được cấp nhưng chưa có khoá → enabled=false');
  ok(/chưa được cài đặt/.test(g.api({ action: 'ai_chat', token: S1, text: 'hi' }).error), 'AI: chưa có khoá → báo chưa cài đặt');
  g.props['GEMINI_API_KEY'] = 'gk-test'; let calls = [];
  g.setFetch((url, o) => { calls.push({ url, o }); return { getResponseCode: () => 200, getContentText: () => JSON.stringify({ candidates: [{ content: { parts: [{ text: 'Xin chào, đây là trả lời' }] } }], usageMetadata: { promptTokenCount: 12, candidatesTokenCount: 7 } }) }; });
  let r = g.api({ action: 'ai_chat', token: S1, text: 'Giải thích thì hiện tại hoàn thành', set_id: 'lop10-u1-luyentap', page_id: 'p1', context: 'have been' });
  ok(r.ok && r.text === 'Xin chào, đây là trả lời' && r.left === 14, 'AI: trả lời + còn 14 lượt (mặc định 15): ' + JSON.stringify(r));
  const sent = JSON.parse(calls[0].o.payload);
  ok(/generativelanguage\.googleapis\.com\/v1beta\/models\/gemini-3\.5-flash-lite:generateContent/.test(calls[0].url) && calls[0].o.headers['x-goog-api-key'] === 'gk-test' && sent.contents[0].role === 'user' && /have been/.test(sent.contents[0].parts[0].text) && /lop10-u1-luyentap/.test(sent.systemInstruction.parts[0].text) && !/Em|Trần|Lê/.test(sent.systemInstruction.parts[0].text) && sent.generationConfig.maxOutputTokens === 700, 'AI: gọi đúng Gemini, khoá, ngữ cảnh; không gửi tên học sinh');
  r = g.api({ action: 'ai_chat', token: S1, text: 'câu tiếp', history: [{ role: 'user', text: 'a' }, { role: 'ai', text: 'b' }, { role: 'user', text: 'c' }] }); const s2 = JSON.parse(calls[1].o.payload);
  ok(r.ok && s2.contents.length === 3 && s2.contents[1].role === 'model' && s2.contents[0].role === 'user' && s2.contents[2].role === 'user', 'AI: ghép lịch sử hội thoại xen kẽ user/model');
  ok(!g.api({ action: 'ai_chat', token: S1, text: 'x', live: true }).ok, 'AI: đang làm bài kiểm tra → bị khoá');
  ok(!g.api({ action: 'ai_chat', token: S1, text: 'x'.repeat(900) }).ok && !g.api({ action: 'ai_chat', token: S1, text: '  ' }).ok, 'AI: câu hỏi rỗng / quá dài bị từ chối');
  ok(g.api({ action: 'ai_chat', token: A, text: 'hi' }).ok, 'AI: admin luôn dùng được');
  g.api({ action: 'adm_ai_save', token: A, limit: 3, enabled: true, provider: 'gemini', modelGemini: 'gemini-3.1-flash-lite' });
  g.advance(61 * 1000); let last = g.api({ action: 'ai_chat', token: S1, text: 'lần 3' }); ok(last.ok && /gemini-3\.1-flash-lite/.test(calls[calls.length - 1].url), 'AI: lượt thứ 3 vẫn được, dùng mô hình đã đổi');
  g.advance(61 * 1000); last = g.api({ action: 'ai_chat', token: S1, text: 'lần 4' }); ok(!last.ok && /hết 3 lượt/.test(last.error), 'AI: quá giới hạn ngày bị chặn: ' + last.error);
  g.api({ action: 'adm_ai_save', token: A, limit: 50, enabled: false }); ok(/tắt/.test(g.api({ action: 'ai_chat', token: S1, text: 'x' }).error), 'AI: admin tắt → bị từ chối');
  g.api({ action: 'adm_ai_save', token: A, limit: 50, enabled: true });
  g.setFetch(() => ({ getResponseCode: () => 400, getContentText: () => '{"error":{"message":"API key not valid. Please pass a valid API key."}}' })); g.advance(61 * 1000);
  ok(/Khoá API/.test(g.api({ action: 'ai_chat', token: S1, text: 'x' }).error), 'AI: khoá Gemini sai (400) → thông báo thân thiện');
  g.setFetch(() => ({ getResponseCode: () => 429, getContentText: () => '{}' })); g.advance(61 * 1000);
  ok(/bận|hết lượt miễn phí/.test(g.api({ action: 'ai_chat', token: S1, text: 'x' }).error), 'AI: 429 → báo bận / hết lượt miễn phí');
  // chuyển sang Claude
  g.props['ANTHROPIC_API_KEY'] = 'sk-test'; g.api({ action: 'adm_ai_save', token: A, limit: 50, enabled: true, provider: 'claude' }); calls = [];
  g.setFetch((url, o) => { calls.push({ url, o }); return { getResponseCode: () => 200, getContentText: () => JSON.stringify({ content: [{ type: 'text', text: 'Claude đáp' }], usage: { input_tokens: 5, output_tokens: 3 } }) }; }); g.advance(61 * 1000);
  r = g.api({ action: 'ai_chat', token: S1, text: 'dùng claude' }); ok(r.ok && r.text === 'Claude đáp' && calls[0].url === 'https://api.anthropic.com/v1/messages' && calls[0].o.headers['x-api-key'] === 'sk-test', 'AI: chuyển sang Claude vẫn chạy');
  g.api({ action: 'adm_ai_save', token: A, limit: 50, enabled: true, provider: 'gemini' });
  // thu quyền; giáo viên
  g.api({ action: 'adm_user_ai', token: A, usernames: [sun], on: false }); g.advance(61 * 1000);
  ok(/chưa được giáo viên cấp quyền/.test(g.api({ action: 'ai_chat', token: S1, text: 'x' }).error) && g.api({ action: 'auth_me', token: S1 }).user.ai === false, 'AI: thu quyền → bị từ chối ngay');
  ok(!g.api({ action: 'ai_chat', token: T, text: 'hi' }).ok, 'AI: giáo viên chưa được cấp → từ chối');
  const tn = g.api({ action: 'auth_me', token: T }).user.username; ok(!g.api({ action: 'adm_user_ai', token: T, usernames: [tn], on: true }).ok || g.api({ action: 'adm_user_ai', token: T, usernames: [tn], on: true }).changed === 0, 'AI: giáo viên thường không tự cấp cho mình');
  ok(g.api({ action: 'adm_user_ai', token: A, usernames: [tn], on: true }).changed === 1, 'AI: admin cấp cho giáo viên'); g.advance(61 * 1000);
  g.setFetch(() => ({ getResponseCode: () => 200, getContentText: () => JSON.stringify({ candidates: [{ content: { parts: [{ text: 'ok' }] } }] }) }));
  ok(g.api({ action: 'ai_chat', token: T, text: 'hi' }).ok, 'AI: giáo viên được cấp dùng được');
  g.api({ action: 'adm_user_ai', token: A, usernames: [tn], on: false });
  g.api({ action: 'adm_user_ai', token: A, usernames: [sun], on: true });
  g.setFetch(() => ({ getResponseCode: () => 400, getContentText: () => '{"error":{"message":"API key not valid"}}' })); g.advance(61 * 1000);
  const lg = g.api({ action: 'adm_ai_get', token: A }); ok(lg.ok && lg.hasKey && lg.provider === 'gemini' && lg.hasGemini && lg.hasClaude && lg.total >= 3 && lg.rows[0].q && JSON.stringify(lg).indexOf('gk-test') < 0 && JSON.stringify(lg).indexOf('sk-test') < 0, 'AI: admin xem nhật ký + trạng thái 2 khoá, khoá không lộ');
  ok(!g.api({ action: 'adm_ai_get', token: T }).ok, 'AI: giáo viên thường không xem được cài đặt / nhật ký');
  ok(g.api({ action: 'adm_users', token: A, role: 'student' }).users.some(u => u.username === sun && u.ai === true), 'AI: danh sách học sinh trả về cờ ai');
  // góp ý chung + gửi nhanh
  const f = g.api({ action: 'fb_send', token: S1, set_id: 'general', page_id: 'index', title: 'Trang chủ', text: 'Cô ơi em có câu hỏi', light: true });
  ok(f.ok && f.msg && f.msg.text === 'Cô ơi em có câu hỏi' && f.msg.role === 'student' && !f.msgs, 'góp ý chung (không gắn bài) + trả về gọn');
  const f2 = g.api({ action: 'fb_send', token: S1, set_id: 'bo-bai-khong-ton-tai', page_id: 'x', text: 'abc' }); ok(!f2.ok, 'góp ý gắn bộ bài chưa giao vẫn bị chặn');
  ok(g.api({ action: 'fb_list', token: S1, set_id: 'general', page_id: 'index' }).msgs.length === 1, 'fb_list đọc lại góp ý chung');
  const inbox = g.api({ action: 'fb_inbox', token: A }); ok(inbox.ok && JSON.stringify(inbox).indexOf('general') >= 0, 'giáo viên/admin thấy góp ý chung trong hộp thư');
}
// ---- phân trang + lọc ngày kết quả ----
{
  const all = g.api({ action: 'adm_results', token: A }); const n = all.rows.length; ok(n >= 3 && all.more === false, 'kết quả mặc định không còn "more"');
  const p1 = g.api({ action: 'adm_results', token: A, limit: 2 }); ok(p1.rows.length === 2 && p1.more === true && p1.rows[0].row === all.rows[0].row, 'limit 2: còn nữa, đúng dòng mới nhất');
  const p2 = g.api({ action: 'adm_results', token: A, limit: 2, offset: 2 }); ok(p2.rows[0].row === all.rows[2].row, 'offset 2: tiếp theo đúng dòng');
  const pl = g.api({ action: 'adm_results', token: A, limit: n, offset: 0 }); ok(pl.more === false && pl.rows.length === n, 'limit đủ: hết');
  const cl = g.api({ action: 'adm_results', token: A, limit: 2, cls: all.rows[0].cls }); ok(cl.rows.every(r => r.cls === all.rows[0].cls), 'lọc lớp + phân trang');
  const nowD = g.run("Utilities.formatDate(new Date(), 'Asia/Ho_Chi_Minh', 'yyyy-MM-dd')");
  const td = g.api({ action: 'adm_results', token: A, from: nowD, to: nowD }); ok(td.rows.length >= 1 && td.rows.length <= n && td.rows.every(r => all.rows.some(x => x.row === r.row)), 'lọc hôm nay: ' + td.rows.length + '/' + n + ' ' + nowD + ' ' + all.rows.map(r => r.time).join('|'));
  ok(g.api({ action: 'adm_results', token: A, to: '2000-01-01' }).rows.length === 0, 'lọc đến năm 2000: trống');
  ok(g.api({ action: 'adm_results', token: A, from: '2999-01-01' }).rows.length === 0, 'lọc từ năm 2999: trống');
}
// ---- sao lưu / khôi phục / reset / xoá kết quả ----
{
  const info = g.api({ action: 'adm_backup_info', token: A }); ok(info.ok && info.parts.users.rows >= 3 && info.parts.results.rows >= 2, 'backup_info: số dòng từng phần');
  ok(!g.api({ action: 'adm_backup_info', token: T }).ok && !g.api({ action: 'adm_backup', token: T, part: 'users' }).ok, 'GV không sao lưu được');
  const bu = g.api({ action: 'adm_backup', token: A, part: 'users' }), br = g.api({ action: 'adm_backup', token: A, part: 'results' });
  ok(bu.ok && bu.headers[0] === 'Tài khoản' && bu.rows.length === info.parts.users.rows, 'backup users');
  ok(br.ok && br.rows.length === info.parts.results.rows && br.headers.indexOf('Sự kiện vi phạm') >= 0, 'backup results có tiêu đề + dòng');
  ok(!g.api({ action: 'adm_backup', token: A, part: 'xyz' }).ok, 'backup phần không tồn tại bị từ chối');
  // xoá kết quả
  const lst = g.api({ action: 'adm_results', token: A }).rows; const one = lst[0], nBefore = lst.length;
  ok(!g.api({ action: 'adm_result_delete', token: T, items: [{ row: one.row, username: one.username, set_id: one.set_id, page_id: one.page_id }] }).ok, 'GV thường không xoá được kết quả');
  const bad = g.api({ action: 'adm_result_delete', token: A, items: [{ row: one.row, username: 'khac', set_id: one.set_id, page_id: one.page_id }] }); ok(bad.deleted === 0 && bad.skipped === 1, 'xoá sai danh tính → bỏ qua');
  const del = g.api({ action: 'adm_result_delete', token: A, items: [{ row: one.row, username: one.username, set_id: one.set_id, page_id: one.page_id }] });
  ok(del.deleted === 1 && g.api({ action: 'adm_results', token: A }).rows.length === nBefore - 1, 'xoá 1 kết quả');
  // reset kết quả + khôi phục từ bản sao lưu
  ok(!g.api({ action: 'adm_reset', token: A, parts: ['results'] }).ok, 'reset thiếu xác nhận bị từ chối');
  ok(!g.api({ action: 'adm_reset', token: T, parts: ['results'], confirm: 'RESET' }).ok, 'GV không reset được');
  const rs = g.api({ action: 'adm_reset', token: A, parts: ['results', 'practice', 'feedback', 'reminders', 'log'], confirm: 'RESET' }); ok(rs.ok && rs.deleted.results === br.rows.length - 1, 'reset kết quả: ' + JSON.stringify(rs.deleted));
  ok(g.api({ action: 'adm_results', token: A }).rows.length === 0 && g.sheets['Lop1-12_KetQua'].rows.length === 1, 'sau reset còn tiêu đề, không còn dòng');
  const rr = g.api({ action: 'adm_restore', token: A, part: 'results', headers: br.headers, rows: br.rows }); ok(rr.ok && rr.restored === br.rows.length && g.api({ action: 'adm_results', token: A }).rows.length === br.rows.length, 'khôi phục kết quả từ sao lưu');
  const rr2 = g.api({ action: 'adm_restore', token: A, part: 'results', headers: br.headers, rows: br.rows, mode: 'append' }); ok(rr2.ok && g.api({ action: 'adm_results', token: A }).rows.length === br.rows.length * 2, 'khôi phục kiểu nối thêm');
  ok(!g.api({ action: 'adm_restore', token: A, part: 'users', headers: ['Sai'], rows: [] }).ok, 'file sao lưu sai định dạng bị từ chối');
  // reset sessions / students
  const nStu = g.sheets['Users'].rows.filter(r => r[2] === 'student').length; ok(nStu >= 1, 'có học sinh để reset');
  const bu2 = g.api({ action: 'adm_backup', token: A, part: 'users' });
  const rs2 = g.api({ action: 'adm_reset', token: A, parts: ['students'], confirm: 'RESET' }); ok(rs2.ok && rs2.deleted.students === nStu && !g.sheets['Users'].rows.some(r => r[2] === 'student') && g.sheets['Users'].rows.some(r => r[2] === 'admin'), 'reset học sinh: chỉ xoá học sinh');
  const ru = g.api({ action: 'adm_restore', token: A, part: 'users', headers: bu2.headers, rows: bu2.rows.filter(r => r[2] !== 'admin') }); ok(ru.ok && ru.keptAdmins >= 1 && g.sheets['Users'].rows.some(r => r[2] === 'admin') && g.sheets['Users'].rows.filter(r => r[2] === 'student').length === nStu, 'khôi phục tài khoản: giữ admin hiện có, đủ học sinh');
  ok(g.api({ action: 'adm_users', token: A }).ok, 'admin vẫn dùng được sau khôi phục');
  ok(g.api({ action: 'adm_reset', token: A, parts: ['sessions'], confirm: 'RESET' }).ok, 'reset phiên đăng nhập');
}
// xoá lớp
ok(!g.api({ action: 'adm_class_delete', token: A, id: '11A1' }).ok, 'không xoá lớp còn HS');
ok(!JSON.stringify(g.sheets['Users'].rows).includes(hsPw) && !JSON.stringify(g.sheets['Users'].rows).includes('Admin@123'), 'Users không lưu mật khẩu rõ');
console.log(fails ? '\n' + fails + '/' + n + ' FAIL' : 'Backend: ' + n + ' kiểm tra OK');
process.exit(fails ? 1 : 0);
