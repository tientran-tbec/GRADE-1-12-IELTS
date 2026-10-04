// Kiểm thử chế độ Thử thách ở máy chủ: node tests/tt_backend_test.js   (cần thư mục thuthach/ đã sinh: python3 tests/tt_gen.py)
const { loadGas } = require('./gas_mock');
const path = require('path'), fs = require('fs');
const g = loadGas(path.join(__dirname, '..', 'code.gs'));
let fails = 0, n = 0;
function ok(c, m) { n++; if (!c) { fails++; console.log('FAIL:', m); } else console.log('ok  ', m); }
const dir = path.join(__dirname, '..', 'thuthach');
g.setFetch(url => { const f = path.join(dir, path.basename(url)); return fs.existsSync(f) ? { getResponseCode: () => 200, getContentText: () => fs.readFileSync(f, 'utf8') } : { getResponseCode: () => 404, getContentText: () => '' }; });
g.run("ADMIN_PASS='Admin@123'"); g.run('setupAdmin()');
const A = g.api({ action: 'auth_login', username: 'admin', password: 'Admin@123', device: 'a' }).token;
const P = JSON.parse(fs.readFileSync(path.join(dir, 'lop3.json'), 'utf8')), SETS = Object.keys(JSON.parse(fs.readFileSync(path.join(dir, 'index.json'), 'utf8')).paths);
const steps = P.chapters.flatMap(c => c.steps), S = i => steps[i].id;
g.api({ action: 'adm_class_save', token: A, cls: { id: '3A', name: '3A', grade: 3 } });
g.api({ action: 'adm_class_save', token: A, cls: { id: '3B', name: '3B', grade: 3 } });
let r = g.api({ action: 'adm_user_save', token: A, user: { name: 'Gv Mot', role: 'teacher' } }); const gv1 = r.user.username, gv1pw = r.password;
ok(g.api({ action: 'adm_teacher_perms', token: A, username: gv1, perms: ['mode'] }).perms[0] === 'mode', 'cấp quyền mode cho GV1');
r = g.api({ action: 'adm_user_save', token: A, user: { name: 'Gv Hai', role: 'teacher' } }); const gv2 = r.user.username, gv2pw = r.password;
g.api({ action: 'adm_class_save', token: A, cls: { id: '3A', name: '3A', grade: 3, teacher: gv1 + ',' + gv2 } });
r = g.api({ action: 'adm_user_save', token: A, user: { name: 'Em Mot', classes: ['3A'], password: 'hs1234' } }); const hs1 = r.user.username;
r = g.api({ action: 'adm_user_save', token: A, user: { name: 'Em Hai', classes: ['3A'], password: 'hs1234' } }); const hs2 = r.user.username;
r = g.api({ action: 'adm_user_save', token: A, user: { name: 'Em Ba', classes: ['3B'], password: 'hs1234' } }); const hs3 = r.user.username;
ok(g.api({ action: 'adm_assign_save', token: A, cls: '3A', sets: SETS }).ok, 'giao bài lớp 3A');
g.api({ action: 'adm_assign_save', token: A, cls: '3B', sets: SETS });
const login = (u, p, d) => g.api({ action: 'auth_login', username: u, password: p, device: d });
let H1 = login(hs1, 'hs1234', 'd1'), H2 = login(hs2, 'hs1234', 'd2'), H3 = login(hs3, 'hs1234', 'd3'), T1 = login(gv1, gv1pw, 'd4'), T2 = login(gv2, gv2pw, 'd5');
ok(H1.user.tt === 'tudo', 'mặc định: Tự do');
// kết quả nộp
const sub = (H, step, pct) => g.post({ action: 'grade_save_result', token: H.token, set_id: step.split('|')[0], page_id: step.split('|')[1], mode: 'practice', score: pct, total: 100, pct, score10: pct / 10, ts: new Date().toISOString() });
const rowsKQ = () => (g.sheets['Lop1-12_KetQua'] ? g.sheets['Lop1-12_KetQua'].rows.length : 0);
// 0) làm trước ở chế độ Tự do (sẽ được tính khi chuyển sang Thử thách): em 2 nộp bước 1 (từ vựng) 90%
ok(sub(H2, S(1), 90) === 'ok', 'chế độ Tự do: nộp bước bất kỳ được');
ok(sub(H1, S(3), 40) === 'ok', 'Tự do: HS1 nộp bước 4 (40%)');
// 1) quyền đặt chế độ
ok(!g.api({ action: 'tt_mode_set', token: T2.token, scope: 'cls', key: '3A', mode: 'thuthach' }).ok, 'GV không có quyền mode bị từ chối');
ok(!g.api({ action: 'tt_mode_set', token: H1.token, scope: 'cls', key: '3A', mode: 'thuthach' }).ok, 'học sinh không đặt được');
ok(!g.api({ action: 'tt_mode_set', token: T1.token, scope: 'cls', key: '3B', mode: 'thuthach' }).ok, 'GV mode chỉ đặt lớp mình phụ trách');
ok(g.api({ action: 'tt_mode_set', token: T1.token, scope: 'cls', key: '3A', mode: 'thuthach' }).ok, 'GV có quyền mode đặt lớp 3A = Thử thách');
H1 = login(hs1, 'hs1234', 'd1'); // đăng nhập lại để lấy user view mới
ok(H1.user.tt === 'thuthach' && H3.user && login(hs3, 'hs1234', 'd3').user.tt === 'tudo', 'user.tt theo lớp; lớp 3B vẫn Tự do');
// 2) trạng thái + khoá
let st = g.api({ action: 'tt_state', token: H1.token });
ok(st.mode === 'thuthach' && st.paths.length === 1 && st.paths[0].steps.length === steps.length, 'tt_state: 1 lộ trình, ' + steps.length + ' bước');
ok(Object.keys(st.paths[0].done).length === 0, 'HS1 (nộp bước 4 khi chưa qua bước trước, 40%): chưa có bước nào xong ' + JSON.stringify(st.paths[0].done));
let k0 = rowsKQ(); const rej = sub(H1, S(2), 90);
ok(/^error: locked/.test(rej) && rowsKQ() === k0, 'bước 3 còn khoá → máy chủ từ chối ghi điểm: ' + rej);
// 3) lý thuyết
ok(!g.api({ action: 'tt_theory', token: H1.token, step: S(1), event: 'start' }).ok, 'không bắt đầu được bước 2 khi chưa xong lý thuyết');
ok(g.api({ action: 'tt_theory', token: H1.token, step: S(0), event: 'start' }).ok, 'bắt đầu lý thuyết');
r = g.api({ action: 'tt_theory', token: H1.token, step: S(0), event: 'done' }); ok(!r.ok && /Chưa đủ thời gian/.test(r.error), 'xong sớm bị từ chối: ' + r.error);
g.advance(125000);
r = g.api({ action: 'tt_theory', token: H1.token, step: S(0), event: 'done' }); ok(r.ok && r.done && r.state.paths[0].done[S(0)] !== undefined, 'đủ 2 phút → xong lý thuyết');
// 4) luyện tập 80%
ok(sub(H1, S(1), 70) === 'ok', 'nộp từ vựng 70% được ghi nhận (lần thử)');
st = g.api({ action: 'tt_state', token: H1.token }); ok(st.paths[0].done[S(1)] === undefined, '70% < 80% → chưa qua');
ok(/^error: locked/.test(sub(H1, S(2), 100)), 'bước sau vẫn khoá');
ok(sub(H1, S(1), 82) === 'ok', 'nộp lại 82%');
st = g.api({ action: 'tt_state', token: H1.token }); ok(st.paths[0].done[S(1)] === 82, '82% ≥ 80% → qua, tốt nhất = 82');
ok(sub(H1, S(2), 80) === 'ok' && g.api({ action: 'tt_state', token: H1.token }).paths[0].done[S(2)] === 80, 'đúng 80% → qua');
// 5) bài kiểm tra 75%
const ti = steps.findIndex(s => s.kind === 'test');
ok(ti > 0, 'có bước kiểm tra tại ' + ti);
// 6) giáo viên mở khoá thủ công / xem tiến độ
ok(!g.api({ action: 'tt_unlock', token: T2.token, username: hs1, step: S(3), how: 'pass' }).ok, 'GV không quyền mode không mở khoá');
ok(g.api({ action: 'tt_unlock', token: T1.token, username: hs1, step: S(3), how: 'pass' }).ok, 'GV mở khoá thủ công bước 4');
st = g.api({ action: 'tt_state', token: H1.token }); ok(st.paths[0].manual.indexOf(S(3)) >= 0 && st.paths[0].done[S(3)] !== undefined, 'bước 4 tính là xong (thủ công)');
ok(g.api({ action: 'tt_unlock', token: T1.token, username: hs1, step: S(3), how: 'revoke' }).ok && g.api({ action: 'tt_state', token: H1.token }).paths[0].done[S(3)] === undefined, 'thu hồi mở khoá');
ok(!g.api({ action: 'tt_unlock', token: T1.token, username: hs3, step: S(3), how: 'pass' }).ok, 'không mở khoá HS lớp khác');
r = g.api({ action: 'tt_progress', token: T1.token, cls: '3A', fresh: true }); const row1 = r.rows.filter(x => x.username === hs1)[0];
ok(r.ok && r.rows.length === 2 && row1.done === 3 && row1.pct === Math.round(300 / steps.length) && /Mẫu câu|Nghe|Chính|Từ vựng|Unit/.test(row1.current), 'tiến độ lớp: HS1 xong 3 bước (' + row1.pct + '%) · đang ở ' + row1.current);
ok(g.api({ action: 'tt_student', token: T1.token, username: hs1 }).paths[0].steps.length === steps.length, 'tt_student chi tiết');
// 7) backfill: HS2 đã nộp từ vựng 90% khi còn Tự do → khi chuyển sang Thử thách, bước đó (và lý thuyết trước nó) được tính
st = g.api({ action: 'tt_state', token: H2.token });
ok(st.paths[0].done[S(1)] === 90 && st.paths[0].done[S(0)] !== undefined, 'HS2 được tính bài đã làm trước đó (từ vựng 90% + lý thuyết)');
// 8) ghi đè theo học sinh: HS2 → Tự do
ok(g.api({ action: 'tt_mode_set', token: T1.token, scope: 'user', key: hs2, mode: 'tudo' }).ok, 'đặt HS2 = Tự do');
H2 = login(hs2, 'hs1234', 'd2'); ok(H2.user.tt === 'tudo' && g.api({ action: 'tt_state', token: H2.token }).mode === 'tudo', 'HS2: Tự do dù lớp là Thử thách');
ok(sub(H2, S(9), 100) === 'ok', 'HS2 (Tự do) nộp bước xa được');
ok(g.api({ action: 'tt_mode_set', token: T1.token, scope: 'user', key: hs3, mode: 'thuthach' }).ok === false, 'GV không đặt được HS lớp khác');
ok(g.api({ action: 'tt_mode_set', token: A, scope: 'user', key: hs3, mode: 'thuthach' }).ok, 'admin đặt HS3 (lớp 3B) = Thử thách');
H3 = login(hs3, 'hs1234', 'd3'); ok(H3.user.tt === 'thuthach', 'HS3: Thử thách theo cá nhân');
// 9) cấu hình ngưỡng và bước bỏ qua
r = g.api({ action: 'tt_cfg_set', token: T1.token, path: 'lop3', cfg: { theory_min: 1, practice_pass: 60, test_pass: 50, skip: [S(2)] } }); ok(r.ok && r.cfg.practice_pass === 60, 'đặt ngưỡng 60/50 + bỏ qua bước 3');
st = g.api({ action: 'tt_state', token: H1.token }); ok(st.paths[0].steps.indexOf(S(2)) < 0 && st.paths[0].cfg.practice_pass === 60, 'bước bị bỏ qua biến khỏi lộ trình');
ok(sub(H1, S(3), 62) === 'ok' && g.api({ action: 'tt_state', token: H1.token }).paths[0].done[S(3)] === 62, 'ngưỡng 60% áp dụng');
g.api({ action: 'tt_cfg_set', token: T1.token, path: 'lop3', cfg: { theory_min: 2, practice_pass: 80, test_pass: 75, skip: [] } });
// 10) bảng lớp + chuỗi ngày
r = g.api({ action: 'tt_board', token: H1.token }); ok(r.ok && r.rows.length === 2 && r.rows.some(x => x.me) && r.rows[0].pct >= r.rows[1].pct, 'bảng lớp: ' + JSON.stringify(r.rows.map(x => x.name + ':' + x.pct)));
st = g.api({ action: 'tt_state', token: H1.token }); ok(st.streak >= 1, 'chuỗi ngày = ' + st.streak);
console.log(fails ? '\n' + fails + '/' + n + ' LỖI' : '\nTẤT CẢ ĐẠT (' + n + ')'); process.exit(fails ? 1 : 0);
