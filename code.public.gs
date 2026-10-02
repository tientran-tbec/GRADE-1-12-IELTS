/**
 * GOOGLE APPS SCRIPT – nhận kết quả bài luyện tập / kiểm tra lớp 1-12 (GRADE-6-12).
 * Các action dùng tiền tố "grade_" nên CHẠY CHUNG được với code.gs cũ (Reading/Listening...) mà không đụng nhau.
 *
 * CÁCH 1 (khuyên dùng – dùng chung URL production cũ):
 *   Mở code.gs cũ, dán hàm handleGrade() + hằng GRADE_* bên dưới vào cuối file,
 *   rồi trong doPost() cũ thêm 1 dòng ngay sau khi parse JSON:
 *       if (String(data.action || '').indexOf('grade_') === 0) return handleGrade(data);
 *   Sau đó Deploy > Manage deployments > Edit > New version (URL giữ nguyên).
 *
 * CÁCH 2 (script mới riêng): dán nguyên file này vào Apps Script mới, Deploy web app (Anyone),
 *   rồi chạy: python update_links.py "<link /exec mới>"
 */
var SHEET_ID = "1Xl515oEdU1j-NrptU-3aUKK0fsOa9VylSIrMD7jqikQ";
var GRADE_SHEET_RESULT = 'Lop1-12_KetQua';
var GRADE_SHEET_LOG = 'Lop1-12_NhatKy';
var GRADE_SHEET_PRACTICE = 'Lop1-12_LuyenTap';

// Tự đổi tên tab cũ (Lop6-12_*) sang tên mới (Lop1-12_*) – giữ nguyên dữ liệu cũ.
function migrateOldSheets_(ss) {
  var map = {'Lop6-12_KetQua': GRADE_SHEET_RESULT, 'Lop6-12_NhatKy': GRADE_SHEET_LOG, 'Lop6-12_LuyenTap': GRADE_SHEET_PRACTICE};
  for (var oldName in map) {
    var o = ss.getSheetByName(oldName);
    if (o && !ss.getSheetByName(map[oldName])) o.setName(map[oldName]);
  }
}

/* Sự kiện vi phạm (do trình duyệt gửi) → chuỗi gọn 'loại:giây;loại:giây' để giáo viên xem lại */
var VIOLATION_EV = {tab_hidden: 1, blur: 1, fs_exit: 1, paste: 1, copy: 1, cut: 1, contextmenu: 1, shortcut: 1, dragstart: 1, drop: 1};
function evStr_(ev) {
  if (!Array.isArray(ev)) return '';
  return ev.filter(function (e) { return e && VIOLATION_EV[e.ev]; }).slice(0, 80).map(function (e) { return e.ev + ':' + Math.round(+e.t || 0) + (e.ev === 'shortcut' && e.x ? ':' + String(e.x).replace(/[;:]/g, '').slice(0, 20) : ''); }).join(';').slice(0, 1800);
}
function ensureUserCol_(sh) {
  if (sh.getLastRow() > 0 && sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0].indexOf('Tài khoản') < 0) sh.getRange(1, sh.getLastColumn() + 1).setValue('Tài khoản');
}
function who_(d) {
  var id = identity_(d);
  if (id) {
    var cls = id.cls;
    if (id.role === 'student') {
      var info = assignedMap_(clsList_(id.cls), id.username)[String(d.set_id)];
      if (!info) return null;   // bài chưa được giao cho lớp nào của học sinh
      cls = info.cls;
      var end = dueEnd_(info.due);
      if (end && Date.now() > end) {   // quá hạn: chỉ nhận bài nộp của người đã vào làm, tối đa 60 phút sau hạn
        if (/^grade_save_(result|partial)$/.test(String(d.action)) && Date.now() <= end + 60 * 60000) d._late = true; else return null;
      }
    }
    d.student_name = id.name; d.student_class = cls; d._role = id.role; return id.username;
  }
  if (REQUIRE_LOGIN) return null;
  return '';
}

function handlePractice(d) {
  var uname = who_(d);
  if (uname === null) return ContentService.createTextOutput('error: unauthorized');
  if (d._role && d._role !== 'student') return ContentService.createTextOutput('ok');   // admin/giáo viên làm thử: không lưu
  var ss = SpreadsheetApp.openById(SHEET_ID);
  migrateOldSheets_(ss);
  var sh = ss.getSheetByName(GRADE_SHEET_PRACTICE) || ss.insertSheet(GRADE_SHEET_PRACTICE);
  if (sh.getLastRow() === 0) { sh.appendRow(['Thời gian', 'Sự kiện', 'Học sinh', 'Lớp', 'Bộ bài', 'Trang', 'Đã làm', 'Đúng', 'Tổng', 'Câu sai', 'Số lần làm lại', 'Thời gian ở trang (s)', 'Tài khoản']); sh.setFrozenRows(1); }
  ensureUserCol_(sh);
  var ev = {enter: 'VÀO LÀM', reset: 'LÀM LẠI', leave: 'RỜI TRANG'}[d.event] || d.event;
  sh.appendRow([tsVN_(d.ts), ev, d.student_name, d.student_class, d.set_id, d.page_id, d.done, d.score, d.total, d.wrong, d.resets, d.time_spent, uname]);
  return ContentService.createTextOutput('ok');
}

function handleGrade(d) {
  if (d.action === 'grade_practice') { var lk = LockService.getScriptLock(); lk.waitLock(20000); try { return handlePractice(d); } finally { lk.releaseLock(); } }
  var uname = who_(d);
  if (uname === null) return ContentService.createTextOutput('error: unauthorized');
  if (d._role && d._role !== 'student') return ContentService.createTextOutput('ok');   // admin/giáo viên làm thử: không lưu
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    var ss = SpreadsheetApp.openById(SHEET_ID);
    var isResult = d.action === 'grade_save_result' || d.action === 'grade_save_partial';
    migrateOldSheets_(ss);
    var sh = ss.getSheetByName(isResult ? GRADE_SHEET_RESULT : GRADE_SHEET_LOG) || ss.insertSheet(isResult ? GRADE_SHEET_RESULT : GRADE_SHEET_LOG);
    if (isResult) {
      if (sh.getLastRow() === 0) { sh.appendRow(['Thời gian', 'Loại', 'Học sinh', 'Lớp', 'Bộ bài', 'Trang', 'Chế độ', 'Điểm', 'Tổng', '%', 'Thang 10',
        'Thời gian làm (s)', 'Chuyển tab', 'Mất focus', 'Thoát toàn màn hình', 'Số lần nghe', 'Chi tiết câu trả lời', 'Tài khoản']); sh.setFrozenRows(1); }
      ensureUserCol_(sh);
      if (sh.getRange(1, 19).getValue() !== 'Sự kiện vi phạm') sh.getRange(1, 19).setValue('Sự kiện vi phạm');
      sh.appendRow([tsVN_(d.ts), d.action === 'grade_save_partial' ? 'LƯU DỞ (rời trang)' : (d._late ? 'ĐÃ NỘP (TRỄ HẠN)' : 'ĐÃ NỘP'),
        d.student_name, d.student_class, d.set_id, d.page_id, d.mode, d.score, d.total, d.pct, d.score10,
        d.time_spent, d.tab_switch, d.blur, d.fullscreen_exit, d.audio_plays, d.answers ? JSON.stringify(d.answers) : '', uname, evStr_(d.events)]);
    } else {
      if (sh.getLastRow() === 0) { sh.appendRow(['Thời gian', 'Sự kiện', 'Học sinh', 'Lớp', 'Bộ bài', 'Trang', 'Chế độ', 'Tài khoản']); sh.setFrozenRows(1); }
      ensureUserCol_(sh);
      sh.appendRow([tsVN_(d.ts), d.action === 'grade_rd_event' ? 'IELTS · ' + String(d.event || '').slice(0, 40) + (d.detail ? ' · ' + String(d.detail).slice(0, 120) : '') : 'VÀO BÀI', d.student_name, d.student_class, d.set_id, d.page_id, d.mode || 'ielts-reading', uname]);
    }
    return ContentService.createTextOutput('ok');
  } catch (err) {
    return ContentService.createTextOutput('error: ' + err);
  } finally { lock.releaseLock(); }
}


/* =====================================================================================
 *  ĐĂNG NHẬP & QUẢN LÝ TÀI KHOẢN (admin / giáo viên / học sinh)
 *  Cài đặt lần đầu: đặt ADMIN_PASS (>= 6 ký tự) bên dưới → chọn hàm setupAdmin → Run → xoá ADMIN_PASS khỏi code.
 *  Dữ liệu: tab "Users" (mật khẩu chỉ lưu dạng băm), tab "Classes". Token đăng nhập ký HMAC, hạn TOKEN_DAYS ngày.
 * ===================================================================================== */
var ADMIN_USER = 'admin';
var ADMIN_PASS = '';            // ← đặt mật khẩu admin ở đây, chạy setupAdmin(), rồi xoá lại thành ''
var SHEET_USERS = 'Users', SHEET_CLASSES = 'Classes';
var USER_HEADERS = ['Tài khoản', 'Họ tên', 'Vai trò', 'Lớp', 'Salt', 'Hash', 'Hoạt động', 'Phải đổi MK', 'Ngày tạo', 'Đăng nhập gần nhất', 'Phiên', 'Thiết bị', 'Quyền', 'Chức vụ'];
var SHEET_ASSIGN = 'Assignments', ASSIGN_HEADERS = ['Lớp', 'Bộ bài', 'Giao bởi', 'Ngày', 'Hạn', 'Học sinh'];
var PING_SEC = 200;   // thiết bị coi là đang online nếu có tín hiệu trong ngần này giây
var CLASS_HEADERS = ['Mã lớp', 'Tên lớp', 'Khối', 'GV phụ trách', 'Ghi chú'];
var TOKEN_DAYS = 3;
var REQUIRE_LOGIN = true;       // true: chỉ ghi kết quả của người đã đăng nhập (token hợp lệ)
var MAX_FAILS = 5, LOCK_MIN = 10;

function ss_() { return SpreadsheetApp.openById(SHEET_ID); }
function sheetOf_(name, headers) {
  var ss = ss_(), sh = ss.getSheetByName(name) || ss.insertSheet(name);
  if (sh.getLastRow() === 0) { sh.appendRow(headers); sh.setFrozenRows(1); }
  else if (sh.getLastColumn() < headers.length) sh.getRange(1, 1, 1, headers.length).setValues([headers]);   // thêm cột mới cho bảng cũ
  return sh;
}
function secret_() {
  var p = PropertiesService.getScriptProperties(), k = p.getProperty('GN_SECRET');
  if (!k) { k = Utilities.getUuid() + Utilities.getUuid(); p.setProperty('GN_SECRET', k); }
  return k;
}
function b64u_(bytes) { return Utilities.base64EncodeWebSafe(bytes).replace(/=+$/, ''); }
function hashPw_(salt, pw) {
  var h = salt + '|' + pw;
  for (var i = 0; i < 300; i++) h = Utilities.base64Encode(Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, h + salt, Utilities.Charset.UTF_8));
  return h;
}
function newSalt_() { return Utilities.getUuid().replace(/-/g, '').slice(0, 16); }
function genPassword_() {
  var c = 'abcdefghjkmnpqrstuvwxyz23456789', s = '';
  for (var i = 0; i < 6; i++) s += c.charAt(Math.floor(Math.random() * c.length));
  return s;
}
function makeToken_(u) {
  var payload = b64u_(Utilities.newBlob(JSON.stringify({u: u.username, r: u.role, e: Date.now() + TOKEN_DAYS * 86400000, s: u.sid || ''})).getBytes());
  var sig = b64u_(Utilities.computeHmacSha256Signature(payload, secret_()));
  return payload + '.' + sig;
}
function verifyToken_(tok) {
  try {
    if (!tok) return null;
    var p = String(tok).split('.');
    if (p.length !== 2) return null;
    var sig = b64u_(Utilities.computeHmacSha256Signature(p[0], secret_()));
    if (sig !== p[1]) return null;
    var pl = JSON.parse(Utilities.newBlob(Utilities.base64DecodeWebSafe(p[0])).getDataAsString());
    if (!pl.e || pl.e < Date.now()) return null;
    return pl;
  } catch (e) { return null; }
}
function strip_(s) { return String(s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/g, 'd').replace(/Đ/g, 'D'); }

/* ----- người dùng ----- */
function readUsers_() {
  var raw = ss_().getSheetByName(SHEET_USERS), oldCols = raw ? raw.getLastColumn() : 99;
  var sh = sheetOf_(SHEET_USERS, USER_HEADERS), v = sh.getDataRange().getValues(), out = [];
  if (oldCols < 13 && v.length > 1) {   // bảng cũ chưa có cột Quyền: giáo viên hiện có giữ quyền giao bài như trước
    for (var m = 1; m < v.length; m++) if (v[m][0] && v[m][2] === 'teacher') { sh.getRange(m + 1, 13).setValue('assign'); v[m][12] = 'assign'; }
  }
  for (var i = 1; i < v.length; i++) {
    if (!v[i][0]) continue;
    out.push({row: i + 1, username: String(v[i][0]).toLowerCase(), name: v[i][1], role: v[i][2], cls: String(v[i][3] || ''), salt: v[i][4], hash: v[i][5],
      active: v[i][6] === true || String(v[i][6]).toUpperCase() === 'TRUE', mustChange: v[i][7] === true || String(v[i][7]).toUpperCase() === 'TRUE', created: fmtT_(v[i][8]), last: fmtT_(v[i][9]),
      sid: String(v[i][10] || ''), dev: String(v[i][11] || ''), perms: clsList_(String(v[i][12] || '')), ranks: parseRanks_(v[i][13])});
  }
  return out;
}
function findUser_(username, list) {
  username = String(username || '').trim().toLowerCase();
  list = list || readUsers_();
  for (var i = 0; i < list.length; i++) if (list[i].username === username) return list[i];
  return null;
}
function clsList_(v) {
  var a = Array.isArray(v) ? v : String(v == null ? '' : v).split(/[,;]+/), seen = {}, out = [];
  a.forEach(function (x) { x = String(x).trim(); if (x && !seen[x]) { seen[x] = 1; out.push(x); } });
  return out;
}
function sharesClass_(mine, u) { return clsList_(u.cls).some(function (c) { return mine.indexOf(c) >= 0; }); }
/* ----- QUYỀN CẤP THÊM -----
   Giáo viên: assign (giao bài), viewall (xem kết quả/tiến độ mọi lớp, chỉ đọc), fball (xem & trả lời góp ý mọi lớp), classes (tạo/sửa/xoá lớp), anystudent (quản lý học sinh ngoài lớp mình).
   Học sinh có chức vụ (T = trưởng nhóm, P = phó nhóm) theo từng lớp: tview (xem tiến độ cả lớp), tscores (xem điểm từng bạn), tremind (nhắc nộp bài), tfb (góp ý thay nhóm). */
var TPERMS = ['full', 'assign', 'viewall', 'fball', 'classes', 'anystudent'], SPERMS = ['tview', 'tscores', 'tremind', 'tfb'];
function parseRanks_(v) { var o = {}; String(v || '').split(',').forEach(function (x) { var m = /^\s*([^:]+):([TP])\s*$/.exec(x); if (m) o[m[1].trim()] = m[2]; }); return o; }
function ranksStr_(o) { return Object.keys(o || {}).filter(function (k) { return o[k] === 'T' || o[k] === 'P'; }).map(function (k) { return k + ':' + o[k]; }).join(','); }
function has_(u, k) { return !!u && (u.role === 'admin' || (u.role === 'teacher' && ((u.perms || []).indexOf(k) >= 0 || (u.perms || []).indexOf('full') >= 0))); }   // 'full' = giáo viên ngang admin (trừ việc tạo/sửa tài khoản admin)
function readAll_(me) { return me.role === 'admin' || has_(me, 'viewall') || has_(me, 'anystudent'); }   // được đọc dữ liệu mọi lớp
function stuPerm_(u, cls, k) { return !!u && u.role === 'student' && !!(u.ranks || {})[cls] && (u.perms || []).indexOf(k) >= 0 && clsList_(u.cls).indexOf(cls) >= 0; }
function pub_(u) { return {username: u.username, name: u.name, role: u.role, cls: clsList_(u.cls).join(','), classes: clsList_(u.cls), active: u.active, mustChange: u.mustChange, created: u.created, last: u.last, online: isOnline_(u), perms: u.perms || [], ranks: u.ranks || {}}; }
function isOnline_(u) { return !!(u.sid && CacheService.getScriptCache().get('ping_' + u.username)); }
function userView_(u) {
  var o = pub_(u); o.sets = null; o.due = null;
  if (u.role === 'student') { var m = assignedMap_(clsList_(u.cls), u.username); o.sets = Object.keys(m); o.due = {}; o.sets.forEach(function (k) { if (m[k].due) o.due[k] = m[k].due; }); }
  return o;
}
function writeUser_(u, isNew) {
  var sh = sheetOf_(SHEET_USERS, USER_HEADERS);
  var row = [u.username, u.name, u.role, u.cls, u.salt, u.hash, u.active, u.mustChange, u.created || tsVN_(), u.last || '', u.sid || '', u.dev || '', (u.perms || []).join(','), ranksStr_(u.ranks)];
  if (isNew) sh.appendRow(row); else sh.getRange(u.row, 1, 1, row.length).setValues([row]);
}
function setupAdmin() {
  if (!ADMIN_PASS || ADMIN_PASS.length < 6) throw new Error('Hãy đặt ADMIN_PASS (>= 6 ký tự) ở đầu phần ĐĂNG NHẬP rồi chạy lại.');
  sheetOf_(SHEET_USERS, USER_HEADERS); sheetOf_(SHEET_CLASSES, CLASS_HEADERS); secret_();
  var u = findUser_(ADMIN_USER), salt = newSalt_();
  var obj = {username: ADMIN_USER.toLowerCase(), name: 'Quản trị viên', role: 'admin', cls: '', salt: salt, hash: hashPw_(salt, ADMIN_PASS), active: true, mustChange: false, created: tsVN_(), last: ''};
  if (u) { obj.row = u.row; obj.created = u.created; writeUser_(obj, false); } else writeUser_(obj, true);
  Logger.log('Đã tạo/đặt lại tài khoản admin "' + ADMIN_USER + '". Hãy xoá ADMIN_PASS khỏi code.');
}

/* ----- lớp ----- */
function readClasses_() {
  var sh = sheetOf_(SHEET_CLASSES, CLASS_HEADERS), v = sh.getDataRange().getValues(), out = [];
  for (var i = 1; i < v.length; i++) if (v[i][0]) out.push({row: i + 1, id: String(v[i][0]), name: v[i][1], grade: v[i][2], teacher: String(v[i][3] || '').toLowerCase(), note: v[i][4]});
  return out;
}
function teacherClasses_(username, classes) {
  return (classes || readClasses_()).filter(function (c) { return clsList_(c.teacher).indexOf(username) >= 0; }).map(function (c) { return c.id; });
}

/* ----- xác thực yêu cầu ----- */
function authUser_(d, roles) {
  var t = verifyToken_(d.token);
  if (!t) throw new Error('SESSION|Phiên đăng nhập hết hạn, hãy đăng nhập lại.');
  var u = findUser_(t.u);
  if (!u || !u.active) throw new Error('Tài khoản không tồn tại hoặc đã bị khoá.');
  if (u.role !== 'admin' && (!u.sid || u.sid !== t.s)) throw new Error('SESSION|Tài khoản đã được đăng nhập ở thiết bị khác (hoặc bị đăng xuất). Hãy đăng nhập lại.');
  if (roles && roles.indexOf(u.role) < 0) throw new Error('Bạn không có quyền thực hiện thao tác này.');
  return u;
}
function jsonOut_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

/* ----- tạo tài khoản ----- */
function makeUsername_(name, taken) {
  var parts = strip_(name).toLowerCase().replace(/[^a-z\s]/g, ' ').split(/\s+/).filter(String);
  if (!parts.length) parts = ['hs'];
  var base = parts[parts.length - 1], i;
  for (i = 0; i < parts.length - 1; i++) base += parts[i].charAt(0);
  var u = base, n = 1;
  while (taken[u]) { n++; u = base + n; }
  taken[u] = true;
  return u;
}
function canManage_(me, target, classes) {
  if (me.role === 'admin') return true;
  if (me.role !== 'teacher') return false;
  if (has_(me, 'full')) return target.role !== 'admin';
  if (target.role !== 'student') return false;
  return has_(me, 'anystudent') || sharesClass_(teacherClasses_(me.username, classes), target);
}

/* ----- giao bài theo lớp ----- */
function readAssign_() {
  var sh = sheetOf_(SHEET_ASSIGN, ASSIGN_HEADERS), v = sh.getDataRange().getValues(), out = [];
  for (var i = 1; i < v.length; i++) if (v[i][0] && v[i][1]) out.push({row: i + 1, cls: String(v[i][0]), set: String(v[i][1]), due: dueStr_(v[i][4]), users: clsList_(String(v[i][5] || '').toLowerCase())});
  return out;
}
function dueStr_(x) {   // 'yyyy-MM-dd' hoặc ''
  if (x instanceof Date) return Utilities.formatDate(x, sheetTz_(), 'yyyy-MM-dd');
  var m = /^(\d{4})-(\d{2})-(\d{2})/.exec(String(x || '')); return m ? m[0] : '';
}
function dueEnd_(due) { return due ? new Date(due + 'T23:59:59+07:00').getTime() : 0; }   // hết ngày hạn (giờ VN)
function assignedOfClass_(cls) {
  var cache = CacheService.getScriptCache(), k = 'asg2_' + cls, c = cache.get(k);
  if (c) return JSON.parse(c);
  var r = readAssign_().filter(function (a) { return a.cls === cls; }).map(function (a) { return {set: a.set, due: a.due, users: a.users}; });
  cache.put(k, JSON.stringify(r), 60);
  return r;
}
/* Gộp bài được giao của nhiều lớp: {bộ: {cls, due}}. Dòng giao có danh sách học sinh → chỉ những học sinh đó nhận; để trống = cả lớp.
   Bộ giao cho nhiều lớp → lấy lớp không hạn, nếu không thì hạn muộn nhất. */
function assignedMap_(classes, username) {
  var m = {}, me = String(username || '').toLowerCase();
  clsList_(classes).forEach(function (cls) {
    assignedOfClass_(cls).forEach(function (a) {
      if (a.users && a.users.length && a.users.indexOf(me) < 0) return;
      var cur = m[a.set];
      if (!cur || (cur.due && (!a.due || a.due > cur.due))) m[a.set] = {cls: cls, due: a.due};
    });
  });
  return m;
}
function canAssign_(me, cls) {
  if (me.role === 'admin' || has_(me, 'full')) return true;
  return has_(me, 'assign') && teacherClasses_(me.username).indexOf(cls) >= 0;
}


/* ----- GÓP Ý / TRÒ CHUYỆN HỌC SINH ↔ GIÁO VIÊN (mỗi học sinh một cuộc cho mỗi trang bài) ----- */
var SHEET_FB = 'Feedback', FB_HEADERS = ['Mã', 'Thời gian', 'Tài khoản HS', 'Họ tên HS', 'Lớp', 'Bộ bài', 'Trang', 'Tiêu đề', 'Người gửi', 'Vai trò', 'Nội dung', 'HS đã đọc', 'GV đã đọc', 'Đường dẫn'];
function truthy_(x) { return x === true || String(x).toUpperCase() === 'TRUE'; }
function sheetTz_() { try { return ss_().getSpreadsheetTimeZone() || 'Asia/Ho_Chi_Minh'; } catch (e) { return 'Asia/Ho_Chi_Minh'; } }
/* Sheets tự đổi chuỗi 'dd/MM/yyyy HH:mm:ss' thành ngày-giờ (theo múi giờ của Sheet) → định dạng lại đúng múi giờ đó để ra lại đúng chuỗi giờ VN đã ghi. */
function fmtT_(x) { return x instanceof Date ? Utilities.formatDate(x, sheetTz_(), 'dd/MM/yyyy HH:mm:ss') : String(x || ''); }
function fbRows_() {
  var sh = sheetOf_(SHEET_FB, FB_HEADERS), v = sh.getDataRange().getValues(), out = [];
  for (var i = 1; i < v.length; i++) if (v[i][0]) out.push({row: i + 1, id: v[i][0], time: fmtT_(v[i][1]), student: String(v[i][2]).toLowerCase(), name: v[i][3], cls: String(v[i][4] || ''), set: String(v[i][5]),
    page: String(v[i][6]), title: v[i][7], from: String(v[i][8]), role: String(v[i][9]), text: String(v[i][10] || ''), rs: truthy_(v[i][11]), rt: truthy_(v[i][12]), path: String(v[i][13] || '')});
  return out;
}
function fbScope_(me) { return (me.role === 'admin' || has_(me, 'fball')) ? null : teacherClasses_(me.username); }
function fbVisible_(me, r, mine) {   // GV thấy cuộc trò chuyện của học sinh cùng lớp mình phụ trách; admin thấy tất cả
  return mine === null || sharesClass_(mine || [], {cls: r.cls});
}
function fbMsg_(r) { return {id: r.id, time: r.time, from: r.from, name: r.role === 'student' ? r.name : (r.name || r.from), role: r.role, text: r.text}; }
function unreadFor_(me) {
  var cache = CacheService.getScriptCache(), k = 'fbu_' + me.username, c = cache.get(k);
  if (c !== null && c !== undefined && c !== '') return +c;
  var n = 0;
  if (me.role === 'student') { fbRows_().forEach(function (r) { if (r.student === me.username && r.role !== 'student' && !r.rs) n++; }); remRows_().forEach(function (r) { if (r.to === me.username && !r.read) n++; }); }
  else { var mine = fbScope_(me); fbRows_().forEach(function (r) { if (r.role === 'student' && !r.rt && fbVisible_(me, r, mine)) n++; }); }
  cache.put(k, String(n), 30);
  return n;
}
function fbMark_(rows, col) { var sh = sheetOf_(SHEET_FB, FB_HEADERS); rows.forEach(function (r) { sh.getRange(r.row, col).setValue(true); }); }
function fbAppend_(vals) { var sh = sheetOf_(SHEET_FB, FB_HEADERS); sh.appendRow(vals); }
function fbText_(d) {
  var t = String(d.text || '').replace(/\r/g, '').trim();
  if (!t) throw new Error('Hãy nhập nội dung.');
  if (t.length > 1000) throw new Error('Tin nhắn quá dài (tối đa 1000 ký tự).');
  return t;
}

var SHEET_REM = 'Reminders', REM_HEADERS = ['Mã', 'Thời gian', 'Lớp', 'Từ (tài khoản)', 'Từ (họ tên)', 'Chức vụ', 'Đến', 'Bộ bài', 'Nội dung', 'Đã đọc'];
function remRows_() {
  var sh = sheetOf_(SHEET_REM, REM_HEADERS), v = sh.getDataRange().getValues(), out = [];
  for (var i = 1; i < v.length; i++) if (v[i][0]) out.push({row: i + 1, id: v[i][0], time: fmtT_(v[i][1]), cls: String(v[i][2]), from: String(v[i][3]), fromName: String(v[i][4]), rank: String(v[i][5]), to: String(v[i][6]).toLowerCase(), set: String(v[i][7]), note: String(v[i][8] || ''), read: truthy_(v[i][9])});
  return out;
}

var API = {
  auth_login: function (d) {
    var uname = String(d.username || '').trim().toLowerCase(), cache = CacheService.getScriptCache(), key = 'fail_' + uname;
    if (+cache.get(key) >= MAX_FAILS) throw new Error('Đăng nhập sai quá nhiều lần. Hãy thử lại sau ' + LOCK_MIN + ' phút.');
    var u = findUser_(uname);
    if (!u || !u.active || u.hash !== hashPw_(u.salt, String(d.password || ''))) {
      cache.put(key, String((+cache.get(key) || 0) + 1), LOCK_MIN * 60);
      throw new Error('Sai tài khoản hoặc mật khẩu.');
    }
    cache.remove(key);
    var dev = String(d.device || '');
    if (u.role !== 'admin') {
      if (u.sid && cache.get('ping_' + u.username) && (!dev || u.dev !== dev))
        throw new Error('Tài khoản này đang được đăng nhập ở thiết bị khác. Hãy đăng xuất ở thiết bị đó, hoặc nhờ giáo viên bấm "Đăng xuất thiết bị" (hoặc chờ khoảng ' + Math.ceil(PING_SEC / 60) + ' phút nếu thiết bị kia đã tắt).');
      u.sid = Utilities.getUuid().replace(/-/g, ''); u.dev = dev;
    } else { u.sid = u.sid || Utilities.getUuid().replace(/-/g, ''); u.dev = dev; }
    u.last = tsVN_(); writeUser_(u, false);
    cache.put('ping_' + u.username, dev || '1', PING_SEC);
    return {token: makeToken_(u), user: userView_(u)};
  },
  auth_me: function (d) { var u = authUser_(d); CacheService.getScriptCache().put('ping_' + u.username, u.dev || '1', PING_SEC); return {user: userView_(u)}; },
  auth_ping: function (d) { var u = authUser_(d); CacheService.getScriptCache().put('ping_' + u.username, u.dev || '1', PING_SEC); return {user: userView_(u), unread: unreadFor_(u)}; },
  auth_logout: function (d) {
    var t = verifyToken_(d.token), u = t ? findUser_(t.u) : null;
    if (u && u.sid === t.s && u.role !== 'admin') { u.sid = ''; u.dev = ''; writeUser_(u, false); CacheService.getScriptCache().remove('ping_' + u.username); }
    return {};
  },
  adm_user_kick: function (d) {
    var me = authUser_(d, ['admin', 'teacher']), u = findUser_(d.username);
    if (!u) throw new Error('Không tìm thấy tài khoản.');
    if (u.role === 'admin' || !canManage_(me, u, readClasses_())) throw new Error('Bạn không có quyền với tài khoản này.');
    u.sid = ''; u.dev = ''; writeUser_(u, false); CacheService.getScriptCache().remove('ping_' + u.username);
    return {};
  },
  auth_change_password: function (d) {
    var u = authUser_(d), np = String(d.new_password || '');
    if (u.hash !== hashPw_(u.salt, String(d.old_password || ''))) throw new Error('Mật khẩu hiện tại không đúng.');
    if (np.length < 6) throw new Error('Mật khẩu mới phải có ít nhất 6 ký tự.');
    u.salt = newSalt_(); u.hash = hashPw_(u.salt, np); u.mustChange = false; writeUser_(u, false);
    return {};
  },
  adm_users: function (d) {
    var me = authUser_(d, ['admin', 'teacher']), all = readUsers_(), cl = readClasses_();
    var mine = readAll_(me) ? null : teacherClasses_(me.username, cl);
    var list = all.filter(function (u) {
      if (me.role === 'teacher' && !has_(me, 'full')) return u.role === 'student' && (mine === null || sharesClass_(mine, u));
      if (u.role === 'admin' && me.role !== 'admin') return false;
      return !d.role || u.role === d.role;
    });
    if (d.cls) list = list.filter(function (u) { return clsList_(u.cls).indexOf(String(d.cls)) >= 0; });
    return {users: list.map(pub_)};
  },
  adm_user_save: function (d) {
    var me = authUser_(d, ['admin', 'teacher']), cl = readClasses_(), all = readUsers_(), x = d.user || {}, name = String(x.name || '').trim();
    if (!name) throw new Error('Thiếu họ tên.');
    var role = (me.role === 'teacher' && !has_(me, 'full')) ? 'student' : ((me.role === 'admin' ? ['admin', 'teacher', 'student'] : ['teacher', 'student']).indexOf(x.role) >= 0 ? x.role : 'student');
    var chosen = role === 'student' ? clsList_(x.classes !== undefined ? x.classes : x.cls) : [];
    var target = x.username ? findUser_(x.username, all) : null, pw = null, cls = chosen.join(',');
    if (me.role === 'teacher' && !has_(me, 'anystudent')) {
      var mineC = teacherClasses_(me.username, cl);
      if (!chosen.length || chosen.some(function (c) { return mineC.indexOf(c) < 0; })) throw new Error('Bạn chỉ quản lý học sinh thuộc lớp mình phụ trách.');
      if (target) cls = clsList_(target.cls).filter(function (c) { return mineC.indexOf(c) < 0; }).concat(chosen).join(',');   // giữ nguyên các lớp của GV khác
    }
    if (target) {
      if (!canManage_(me, target, cl)) throw new Error('Bạn không có quyền sửa tài khoản này.');
      if (target.username === me.username && x.active === false) throw new Error('Không thể tự khoá tài khoản của mình.');
      target.name = name; target.cls = cls;
      if (has_(me, 'full') && target.username !== me.username && target.role !== 'admin') target.role = role;
      if (typeof x.active === 'boolean') target.active = x.active;
      writeUser_(target, false);
      return {user: pub_(target)};
    }
    var taken = {}; all.forEach(function (u) { taken[u.username] = true; });
    var uname = x.new_username ? String(x.new_username).trim().toLowerCase().replace(/[^a-z0-9._-]/g, '') : '';
    if (uname && taken[uname]) throw new Error('Tên đăng nhập đã tồn tại.');
    if (!uname) uname = makeUsername_(name, taken);
    pw = String(x.password || '') || genPassword_();
    if (me.role === 'teacher' && role === 'student' && !chosen.length) throw new Error('Hãy chọn ít nhất một lớp.');
    var salt = newSalt_(), nu = {username: uname, name: name, role: role, cls: cls, salt: salt, hash: hashPw_(salt, pw), active: true, mustChange: true, created: tsVN_(), last: ''};
    writeUser_(nu, true);
    return {user: pub_(nu), password: pw};
  },
  adm_user_reset: function (d) {
    var me = authUser_(d, ['admin', 'teacher']), u = findUser_(d.username);
    if (!u) throw new Error('Không tìm thấy tài khoản.');
    if (!canManage_(me, u, readClasses_())) throw new Error('Bạn không có quyền đặt lại mật khẩu tài khoản này.');
    var pw = String(d.password || '') || genPassword_();
    u.salt = newSalt_(); u.hash = hashPw_(u.salt, pw); u.mustChange = true; u.sid = ''; u.dev = ''; writeUser_(u, false); CacheService.getScriptCache().remove('ping_' + u.username);
    return {username: u.username, password: pw};
  },
  adm_users_import: function (d) {
    var me = authUser_(d, ['admin', 'teacher']), cl = readClasses_(), all = readUsers_(), taken = {}, mine = (me.role === 'teacher' && !has_(me, 'anystudent')) ? teacherClasses_(me.username, cl) : null;
    all.forEach(function (u) { taken[u.username] = true; });
    var created = [], skipped = [];
    (d.rows || []).forEach(function (r) {
      var name = String(r.name || '').trim(), cls = clsList_(r.cls || d.cls || '').join(',');
      if (!name) return;
      if (me.role === 'teacher' && (!cls || (mine && clsList_(cls).some(function (c) { return mine.indexOf(c) < 0; })))) { skipped.push({name: name, reason: 'Lớp "' + cls + '" không thuộc quyền quản lý'}); return; }
      var uname = makeUsername_(name, taken), pw = genPassword_(), salt = newSalt_();
      writeUser_({username: uname, name: name, role: 'student', cls: cls, salt: salt, hash: hashPw_(salt, pw), active: true, mustChange: true, created: tsVN_(), last: ''}, true);
      created.push({username: uname, name: name, cls: cls, password: pw});
    });
    return {created: created, skipped: skipped};
  },
  adm_classes: function (d) {
    var me = authUser_(d, ['admin', 'teacher']), cl = readClasses_();
    var list = (me.role === 'teacher' && !readAll_(me) && !has_(me, 'classes')) ? cl.filter(function (c) { return clsList_(c.teacher).indexOf(me.username) >= 0; }) : cl;
    var teachers = (me.role === 'admin' || has_(me, 'classes') || readAll_(me)) ? readUsers_().filter(function (u) { return u.role === 'teacher'; }).map(pub_) : [];
    var asg = readAssign_(), cnt = {}; asg.forEach(function (a) { cnt[a.cls] = (cnt[a.cls] || 0) + 1; });
    return {classes: list.map(function (c) { return {id: c.id, name: c.name, grade: c.grade, teacher: c.teacher, note: c.note, sets: cnt[c.id] || 0}; }), teachers: teachers};
  },
  adm_class_save: function (d) {
    var me0 = authUser_(d, ['admin', 'teacher']); if (!has_(me0, 'classes')) throw new Error('Bạn không có quyền quản lý lớp.');
    var c = d.cls || {}, id = String(c.id || '').trim();
    if (!id) throw new Error('Thiếu mã lớp.');
    var sh = sheetOf_(SHEET_CLASSES, CLASS_HEADERS), ex = readClasses_().filter(function (k) { return k.id === id; })[0];
    var row = [id, c.name || id, c.grade || '', clsList_(c.teacher).join(',').toLowerCase(), c.note || ''];
    if (ex) sh.getRange(ex.row, 1, 1, row.length).setValues([row]); else sh.appendRow(row);
    return {};
  },
  adm_teacher_classes: function (d) {   // đặt danh sách lớp phụ trách của một giáo viên (thêm/bớt tên GV ở từng lớp, giữ nguyên GV khác)
    var me0 = authUser_(d, ['admin', 'teacher']); if (!has_(me0, 'full')) throw new Error('Chỉ quản trị viên (hoặc giáo viên toàn quyền) làm được việc này.');
    var t = findUser_(d.username); if (!t || t.role !== 'teacher') throw new Error('Không tìm thấy giáo viên.');
    var want = clsList_(d.classes), sh = sheetOf_(SHEET_CLASSES, CLASS_HEADERS), n = 0;
    readClasses_().forEach(function (c) {
      var cur = clsList_(c.teacher), has = cur.indexOf(t.username) >= 0, need = want.indexOf(c.id) >= 0;
      if (has === need) return;
      var next = need ? cur.concat([t.username]) : cur.filter(function (x) { return x !== t.username; });
      sh.getRange(c.row, 4).setValue(next.join(',')); n++;
    });
    return {changed: n};
  },
  adm_class_delete: function (d) {
    var me0 = authUser_(d, ['admin', 'teacher']); if (!has_(me0, 'classes')) throw new Error('Bạn không có quyền quản lý lớp.');
    var ex = readClasses_().filter(function (k) { return k.id === String(d.id); })[0];
    if (!ex) throw new Error('Không tìm thấy lớp.');
    if (readUsers_().some(function (u) { return u.role === 'student' && clsList_(u.cls).indexOf(ex.id) >= 0 && u.active; })) throw new Error('Lớp còn học sinh đang hoạt động – hãy chuyển hoặc khoá họ trước.');
    sheetOf_(SHEET_CLASSES, CLASS_HEADERS).deleteRow(ex.row);
    return {};
  },
  adm_assign_get: function (d) {
    var me = authUser_(d, ['admin', 'teacher']), cls = String(d.cls || '');
    if (!(readAll_(me) || teacherClasses_(me.username).indexOf(cls) >= 0)) throw new Error('Bạn không phụ trách lớp này.');   // xem được; còn lưu giao bài cần quyền "assign" 
    return {sets: readAssign_().filter(function (a) { return a.cls === cls; }).map(function (a) { return a.set; }),
            due: readAssign_().filter(function (a) { return a.cls === cls && a.due; }).reduce(function (o, a) { o[a.set] = a.due; return o; }, {}),
            users: readAssign_().filter(function (a) { return a.cls === cls && a.users.length; }).reduce(function (o, a) { o[a.set] = a.users; return o; }, {})};
  },
  adm_assign_save: function (d) {
    var me = authUser_(d, ['admin', 'teacher']), cls = String(d.cls || ''), sets = d.sets || [];
    if (!cls || !canAssign_(me, cls)) throw new Error('Bạn không phụ trách lớp này.');
    var lock = LockService.getScriptLock(); lock.waitLock(20000);
    try {
      var sh = sheetOf_(SHEET_ASSIGN, ASSIGN_HEADERS), all = readAssign_();
      sh.getRange(1, 5).setValue('Hạn'); sh.getRange(1, 6).setValue('Học sinh'); sh.getRange(2, 5, Math.max(sh.getLastRow() - 1, 1), 2).setNumberFormat('@');   // cột Hạn dạng văn bản (tránh bị đổi thành ngày)
      for (var i = all.length - 1; i >= 0; i--) if (all[i].cls === cls) sh.deleteRow(all[i].row);
      var seen = {};
      var dues = d.due || {}, onlyU = d.users || {}, inCls = readUsers_().filter(function (u) { return u.role === 'student' && clsList_(u.cls).indexOf(cls) >= 0; }).map(function (u) { return u.username; });
      sets.forEach(function (s) {
        s = String(s); if (!s || seen[s]) return; seen[s] = 1;
        var us = clsList_(onlyU[s] || []).map(function (x) { return x.toLowerCase(); }).filter(function (x) { return inCls.indexOf(x) >= 0; });
        if (us.length >= inCls.length) us = [];   // chọn đủ cả lớp = giao cả lớp
        sh.appendRow([cls, s, me.username, tsVN_(), dueStr_(dues[s]), us.join(',')]);
      });
      CacheService.getScriptCache().remove('asg2_' + cls);
    } finally { lock.releaseLock(); }
    return {count: Object.keys(seen).length};
  },
  fb_send: function (d) {
    var u = authUser_(d, ['student']), text = fbText_(d), set = String(d.set_id || ''), page = String(d.page_id || ''), cache = CacheService.getScriptCache(), rk = 'fbr_' + u.username;
    if (!set || !page) throw new Error('Thiếu thông tin bài.');
    if (!assignedMap_(clsList_(u.cls), u.username)[set]) throw new Error('Bài này chưa được giao cho bạn.');
    var n = +cache.get(rk) || 0; if (n >= 20) throw new Error('Bạn gửi quá nhiều tin trong thời gian ngắn, hãy thử lại sau ít phút.');
    cache.put(rk, String(n + 1), 600);
    var lock = LockService.getScriptLock(); lock.waitLock(20000);
    try { fbAppend_([Utilities.getUuid(), tsVN_(), u.username, u.name, clsList_(u.cls).join(','), set, page, String(d.title || '').slice(0, 120), u.username, 'student', text, true, false, /^WebBaiTap\/[\w\/.\-]+\.html$/.test(String(d.path || '')) ? d.path : '']); }
    finally { lock.releaseLock(); }
    cache.remove('fbu_' + u.username);
    return {msgs: fbRows_().filter(function (r) { return r.student === u.username && r.set === set && r.page === page; }).map(fbMsg_)};
  },
  fb_list: function (d) {
    var u = authUser_(d), set = String(d.set_id || ''), page = String(d.page_id || '');
    if (u.role !== 'student') return {msgs: []};
    var rows = fbRows_().filter(function (r) { return r.student === u.username && r.set === set && r.page === page; });
    var un = rows.filter(function (r) { return r.role !== 'student' && !r.rs; });
    if (un.length) { fbMark_(un, 12); CacheService.getScriptCache().remove('fbu_' + u.username); }
    return {msgs: rows.map(fbMsg_)};
  },
  fb_mine: function (d) {   // học sinh: danh sách cuộc trò chuyện của mình
    var u = authUser_(d, ['student']), th = {}, order = [];
    fbRows_().forEach(function (r) {
      if (r.student !== u.username) return;
      var k = r.set + '|' + r.page, t = th[k];
      if (!t) { t = th[k] = {set: r.set, page: r.page, title: r.title, path: r.path, count: 0, unread: 0}; order.push(k); }
      t.count++; t.last = r.time; t.lastText = r.text.slice(0, 80); t.order = r.row;
      if (r.role !== 'student' && !r.rs) t.unread++;
    });
    return {threads: order.map(function (k) { return th[k]; }).sort(function (a, b) { return b.order - a.order; })};
  },
  fb_inbox: function (d) {
    var me = authUser_(d, ['admin', 'teacher']), mine = fbScope_(me), th = {}, order = [];
    fbRows_().forEach(function (r) {
      if (!fbVisible_(me, r, mine)) return;
      var k = r.student + '|' + r.set + '|' + r.page, t = th[k];
      if (!t) { t = th[k] = {student: r.student, name: r.name, cls: r.cls, set: r.set, page: r.page, title: r.title, path: r.path, count: 0, unread: 0}; order.push(k); }
      t.count++; t.last = r.time; t.lastText = r.text.slice(0, 80); t.lastRole = r.role; t.order = r.row;
      if (r.role === 'student' && !r.rt) t.unread++;
    });
    var list = order.map(function (k) { return th[k]; }).sort(function (a, b) { return b.order - a.order; }).slice(0, 300);
    return {threads: list, unread: list.reduce(function (n, t) { return n + t.unread; }, 0)};
  },
  fb_thread: function (d) {
    var me = authUser_(d, ['admin', 'teacher']), mine = fbScope_(me), st = String(d.student || '').toLowerCase();
    var rows = fbRows_().filter(function (r) { return r.student === st && r.set === String(d.set_id) && r.page === String(d.page_id) && fbVisible_(me, r, mine); });
    var un = rows.filter(function (r) { return r.role === 'student' && !r.rt; });
    if (un.length) { fbMark_(un, 13); CacheService.getScriptCache().remove('fbu_' + me.username); }
    return {msgs: rows.map(fbMsg_)};
  },
  fb_reply: function (d) {
    var me = authUser_(d, ['admin', 'teacher']), text = fbText_(d), st = findUser_(d.student), set = String(d.set_id || ''), page = String(d.page_id || '');
    if (!st || st.role !== 'student') throw new Error('Không tìm thấy học sinh.');
    if (!canManage_(me, st, readClasses_()) && !(has_(me, 'fball') || sharesClass_(teacherClasses_(me.username), st))) throw new Error('Học sinh này không thuộc lớp bạn phụ trách.');
    var prev = fbRows_().filter(function (r) { return r.student === st.username && r.set === set && r.page === page; });
    if (!prev.length) throw new Error('Chưa có góp ý nào ở bài này.');
    var lock = LockService.getScriptLock(); lock.waitLock(20000);
    try { fbAppend_([Utilities.getUuid(), tsVN_(), st.username, st.name, clsList_(st.cls).join(','), set, page, prev[0].title, me.username, me.role, text, false, true, prev[0].path]); }
    finally { lock.releaseLock(); }
    var un = prev.filter(function (r) { return r.role === 'student' && !r.rt; }); if (un.length) fbMark_(un, 13);
    CacheService.getScriptCache().remove('fbu_' + me.username);
    return {msgs: fbRows_().filter(function (r) { return r.student === st.username && r.set === set && r.page === page; }).map(fbMsg_)};
  },
  adm_teacher_perms: function (d) {   // admin tick quyền cấp thêm cho giáo viên
    var me0 = authUser_(d, ['admin', 'teacher']); if (me0.role !== 'admin' && !has_(me0, 'full')) throw new Error('Chỉ quản trị viên (hoặc giáo viên toàn quyền) cấp được quyền.');
    var t = findUser_(d.username); if (!t || t.role !== 'teacher') throw new Error('Không tìm thấy giáo viên.');
    t.perms = clsList_(d.perms).filter(function (k) { return TPERMS.indexOf(k) >= 0; });
    if (t.perms.indexOf('full') >= 0) t.perms = TPERMS.slice();   // toàn quyền = tích hết
    writeUser_(t, false);
    return {perms: t.perms};
  },
  adm_student_ranks: function (d) {   // trưởng nhóm / phó nhóm (theo từng lớp) + quyền của họ; admin hoặc giáo viên quản lý học sinh đó
    var me = authUser_(d, ['admin', 'teacher']), t = findUser_(d.username), cl = readClasses_();
    if (!t || t.role !== 'student') throw new Error('Không tìm thấy học sinh.');
    if (!canManage_(me, t, cl)) throw new Error('Bạn không có quyền với học sinh này.');
    var mine = t.cls ? clsList_(t.cls) : [], free = (me.role === 'admin' || has_(me, 'anystudent')) ? mine : mine.filter(function (c) { return teacherClasses_(me.username, cl).indexOf(c) >= 0; });
    var next = {}, old = t.ranks || {}, want = d.ranks || {};
    mine.forEach(function (c) {
      var r = free.indexOf(c) >= 0 ? want[c] : old[c];
      if (r === 'T' || r === 'P') next[c] = r;
    });
    t.ranks = next;
    t.perms = Object.keys(next).length ? clsList_(d.perms).filter(function (k) { return SPERMS.indexOf(k) >= 0; }) : [];
    writeUser_(t, false);
    CacheService.getScriptCache().remove('fbu_' + t.username);
    return {user: pub_(t)};
  },
  team_progress: function (d) {   // trưởng/phó nhóm xem tiến độ cả lớp (không xem đáp án)
    var me = authUser_(d, ['student']), cls = String(d.cls || '');
    if (!stuPerm_(me, cls, 'tview')) throw new Error('Bạn không có quyền xem tiến độ lớp này.');
    var showScore = stuPerm_(me, cls, 'tscores'), asg = assignedOfClass_(cls);
    var members = readUsers_().filter(function (u) { return u.role === 'student' && u.active && clsList_(u.cls).indexOf(cls) >= 0; });
    var byU = {}; members.forEach(function (u) { byU[u.username] = {}; });
    var setIdx = {}; asg.forEach(function (a) { setIdx[a.set] = 1; });
    var sh = ss_().getSheetByName(GRADE_SHEET_RESULT);
    if (sh && sh.getLastRow() > 1) {
      var v = sh.getDataRange().getValues(), col = {}; v[0].forEach(function (x, i) { col[x] = i; });
      var ui = col['Tài khoản'], seen = {};
      if (ui !== undefined) for (var i = v.length - 1; i >= 1 && i > v.length - 6000; i--) {
        var r = v[i], u = String(r[ui] || '').toLowerCase(), set = String(r[col['Bộ bài']]);
        if (!byU[u] || !setIdx[set] || !/^ĐÃ NỘP/.test(String(r[col['Loại']] || ''))) continue;
        var k = u + '|' + set + '|' + r[col['Trang']]; if (seen[k]) continue; seen[k] = 1;
        var it = byU[u][set] || (byU[u][set] = {n: 0, sum: 0}); it.n++; it.sum += +r[col['Thang 10']] || 0;
      }
    }
    return {sets: asg.map(function (a) { return {set: a.set, due: a.due}; }), perms: {tscores: showScore, tremind: stuPerm_(me, cls, 'tremind')},
      members: members.map(function (u) {
        var items = {}, app = [];
        asg.forEach(function (a) { if (a.users && a.users.length && a.users.indexOf(u.username) < 0) return; app.push(a.set); var it = byU[u.username][a.set]; if (it) items[a.set] = showScore ? {n: it.n, avg: Math.round(it.sum / it.n * 10) / 10} : {n: it.n}; });
        return {username: u.username, name: u.name, me: u.username === me.username, applies: app, items: items};
      }).sort(function (a, b) { return a.name < b.name ? -1 : a.name > b.name ? 1 : 0; })};
  },
  team_remind: function (d) {   // nhắc các bạn trong lớp chưa nộp bài
    var me = authUser_(d, ['student']), cls = String(d.cls || ''), cache = CacheService.getScriptCache();
    if (!stuPerm_(me, cls, 'tremind')) throw new Error('Bạn không có quyền nhắc nộp bài ở lớp này.');
    var set = String(d.set_id || ''), note = String(d.note || '').replace(/[\r\n]+/g, ' ').trim().slice(0, 120);
    if (set && !assignedOfClass_(cls).some(function (a) { return a.set === set; })) throw new Error('Bộ bài này chưa được giao cho lớp.');
    var want = clsList_(d.users).map(function (x) { return x.toLowerCase(); }).filter(function (x) { return x !== me.username; }).slice(0, 40);
    if (!want.length) throw new Error('Hãy chọn ít nhất một bạn.');
    var rk = 'rmr_' + me.username, n = +cache.get(rk) || 0; if (n >= 8) throw new Error('Bạn nhắc quá nhiều lần trong thời gian ngắn, hãy thử lại sau.');
    cache.put(rk, String(n + 1), 3600);
    var ok = {}; readUsers_().forEach(function (u) { if (u.role === 'student' && u.active && clsList_(u.cls).indexOf(cls) >= 0) ok[u.username] = 1; });
    var rank = me.ranks[cls] === 'T' ? 'Trưởng nhóm' : 'Phó nhóm', sent = 0, skipped = 0;
    var lock = LockService.getScriptLock(); lock.waitLock(20000);
    try {
      var sh = sheetOf_(SHEET_REM, REM_HEADERS);
      want.forEach(function (to) {
        var dk = 'rmt_' + to + '_' + set;
        if (!ok[to] || cache.get(dk)) { skipped++; return; }   // không cùng lớp, hoặc vừa được nhắc bài này (6 giờ)
        cache.put(dk, '1', 6 * 3600);
        sh.appendRow([Utilities.getUuid(), tsVN_(), cls, me.username, me.name, rank, to, set, note, false]); sent++;
        cache.remove('fbu_' + to);
      });
    } finally { lock.releaseLock(); }
    return {sent: sent, skipped: skipped};
  },
  my_reminders: function (d) {
    var me = authUser_(d, ['student']), rows = remRows_().filter(function (r) { return r.to === me.username; }).reverse().slice(0, 50);
    var sh = sheetOf_(SHEET_REM, REM_HEADERS), un = rows.filter(function (r) { return !r.read; });
    un.forEach(function (r) { sh.getRange(r.row, 10).setValue(true); });
    if (un.length) CacheService.getScriptCache().remove('fbu_' + me.username);
    return {items: rows.map(function (r) { return {time: r.time, cls: r.cls, from: r.fromName, rank: r.rank, set: r.set, note: r.note, isNew: !r.read}; })};
  },
  team_fb: function (d) {   // trưởng/phó nhóm gửi góp ý thay cả nhóm cho giáo viên (cuộc trò chuyện riêng của lớp đó)
    var me = authUser_(d, ['student']), cls = String(d.cls || ''), text = fbText_(d), cache = CacheService.getScriptCache(), rk = 'fbr_' + me.username;
    if (!stuPerm_(me, cls, 'tfb')) throw new Error('Bạn không có quyền gửi góp ý thay nhóm.');
    var n = +cache.get(rk) || 0; if (n >= 20) throw new Error('Bạn gửi quá nhiều tin trong thời gian ngắn, hãy thử lại sau ít phút.');
    cache.put(rk, String(n + 1), 600);
    var set = 'team:' + cls, lock = LockService.getScriptLock(); lock.waitLock(20000);
    try { fbAppend_([Utilities.getUuid(), tsVN_(), me.username, me.name, cls, set, 'nhom', 'Góp ý của nhóm – lớp ' + cls, me.username, 'student', text, true, false, '']); }
    finally { lock.releaseLock(); }
    cache.remove('fbu_' + me.username);
    return {msgs: fbRows_().filter(function (r) { return r.student === me.username && r.set === set && r.page === 'nhom'; }).map(fbMsg_)};
  },
  adm_result_detail: function (d) {   // chi tiết một lần nộp: câu trả lời + sự kiện vi phạm
    var me = authUser_(d, ['admin', 'teacher']), sh = ss_().getSheetByName(GRADE_SHEET_RESULT), row = +d.row;
    if (!sh || !(row >= 2) || row > sh.getLastRow()) throw new Error('Không tìm thấy bài nộp.');
    var h = sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0], col = {}; h.forEach(function (x, i) { col[x] = i; });
    var r = sh.getRange(row, 1, 1, h.length).getValues()[0], user = String(r[col['Tài khoản']] || '').toLowerCase(), cls = String(r[col['Lớp']] || '');
    if (!(readAll_(me) || teacherClasses_(me.username).indexOf(cls) >= 0)) throw new Error('Bạn không có quyền xem bài này.');
    var ans = {}; try { ans = JSON.parse(String(r[col['Chi tiết câu trả lời']] || '{}')); } catch (e) { ans = {raw: String(r[col['Chi tiết câu trả lời']] || '')}; }
    return {time: fmtT_(r[0]), type: r[col['Loại']], name: r[col['Học sinh']], username: user, cls: cls, set_id: r[col['Bộ bài']], page_id: r[col['Trang']], mode: r[col['Chế độ']],
      score: r[col['Điểm']], total: r[col['Tổng']], score10: r[col['Thang 10']], time_spent: r[col['Thời gian làm (s)']], tab: r[col['Chuyển tab']], blur: r[col['Mất focus']], fs: r[col['Thoát toàn màn hình']],
      plays: r[col['Số lần nghe']], answers: ans, events: String(r[col['Sự kiện vi phạm']] || '')};
  },
  adm_student_summary: function (d) {   // trang tổng kết một học sinh
    var me = authUser_(d, ['admin', 'teacher']), u = findUser_(d.username);
    if (!u || u.role !== 'student') throw new Error('Không tìm thấy học sinh.');
    if (!(readAll_(me) || sharesClass_(teacherClasses_(me.username), u))) throw new Error('Học sinh này không thuộc lớp bạn phụ trách.');
    var view = userView_(u), m = assignedMap_(clsList_(u.cls), u.username);
    var rows = resultRows_(me, {username: u.username}), practice = {};
    var ps = ss_().getSheetByName(GRADE_SHEET_PRACTICE);
    if (ps && ps.getLastRow() > 1) {
      var v = ps.getDataRange().getValues(), col = {}; v[0].forEach(function (x, i) { col[x] = i; });
      var ui = col['Tài khoản'];
      if (ui !== undefined) for (var i = v.length - 1; i >= 1 && i > v.length - 8000; i--) {
        var r = v[i]; if (String(r[ui] || '').toLowerCase() !== u.username) continue;
        var k = r[col['Bộ bài']] + '|' + r[col['Trang']], p = practice[k] || (practice[k] = {set_id: r[col['Bộ bài']], page_id: r[col['Trang']], visits: 0, secs: 0, resets: 0, last: fmtT_(r[0]), done: 0, ok: 0, total: 0});
        var ev = String(r[col['Sự kiện']]);
        if (ev === 'VÀO LÀM') p.visits++;
        if (ev === 'LÀM LẠI') p.resets++;
        if (ev === 'RỜI TRANG') { p.secs += +r[col['Thời gian ở trang (s)']] || 0; if (!p.seenState) { p.seenState = 1; p.done = +r[col['Đã làm']] || 0; p.ok = +r[col['Đúng']] || 0; p.total = +r[col['Tổng']] || 0; } }
      }
    }
    var fbN = fbRows_().filter(function (r) { return r.student === u.username && r.role === 'student'; }).length;
    return {user: pub_(u), sets: Object.keys(m).map(function (k) { return {set_id: k, cls: m[k].cls, due: m[k].due}; }), results: rows, practice: Object.keys(practice).map(function (k) { delete practice[k].seenState; return practice[k]; }), feedback_count: fbN};
  },
  adm_backup_info: function (d) {   // số dòng của từng phần dữ liệu
    adminOnly_(d); var out = {};
    Object.keys(BK_PARTS).forEach(function (k) { var sh = ss_().getSheetByName(BK_PARTS[k].sheet); out[k] = {name: BK_PARTS[k].name, rows: sh ? Math.max(0, sh.getLastRow() - 1) : 0}; });
    return {parts: out};
  },
  adm_backup: function (d) {   // lấy dữ liệu MỘT phần (trình duyệt gọi lần lượt từng phần rồi gộp thành 1 file)
    adminOnly_(d); var p = bkPart_(d.part), sh = ss_().getSheetByName(p.sheet);
    if (!sh || sh.getLastRow() < 1) return {part: d.part, headers: p.headers || [], rows: []};
    var v = sh.getDataRange().getValues(), start = Math.max(1, +d.from || 1), end = Math.min(v.length, start + (+d.max || 20000));
    return {part: d.part, headers: v[0].map(String), rows: v.slice(start, end).map(function (r) { return r.map(cellOut_); }), total: v.length - 1, next: end < v.length ? end : 0};
  },
  adm_restore: function (d) {   // khôi phục MỘT phần: thay thế (replace) hoặc nối thêm (append)
    var me = adminOnly_(d), p = bkPart_(d.part), hd = (d.headers || []).map(String), rows = d.rows || [], append = d.mode === 'append' || d.append === true;
    if (!hd.length || !Array.isArray(rows)) throw new Error('File sao lưu không hợp lệ.');
    if (p.headers && hd[0] !== p.headers[0]) throw new Error('File sao lưu của phần "' + p.name + '" không đúng định dạng.');
    var lock = LockService.getScriptLock(); lock.waitLock(30000);
    try {
      var sh = ss_().getSheetByName(p.sheet) || ss_().insertSheet(p.sheet), w = hd.length, keepAdmins = [];
      if (d.part === 'users' && !append) {
        var ri = hd.indexOf('Vai trò'), hasAdmin = rows.some(function (r) { return String(r[ri]) === 'admin'; });
        if (!hasAdmin) { var cur = readUsers_().filter(function (u) { return u.role === 'admin'; }); keepAdmins = cur.map(function (u) { return u.row; }); }
      }
      var keep = [];
      if (keepAdmins.length) { var all = sh.getDataRange().getValues(); keepAdmins.forEach(function (rn) { keep.push(all[rn - 1]); }); }
      if (!append) {
        wipeData_(sh);
        if (sh.getLastRow() === 0 || sh.getLastColumn() < w || true) { sh.getRange(1, 1, 1, w).setValues([hd]); sh.setFrozenRows(1); }
      } else if (sh.getLastRow() === 0) { sh.getRange(1, 1, 1, w).setValues([hd]); sh.setFrozenRows(1); }
      var out = keep.concat(rows).map(function (r) { var a = r.slice(0, w); while (a.length < w) a.push(''); return a; });
      var at = Math.max(sh.getLastRow(), 1) + 1;
      for (var i = 0; i < out.length; i += 2000) { var ch = out.slice(i, i + 2000); sh.getRange(at + i, 1, ch.length, w).setValues(ch); }
      return {part: d.part, restored: out.length, keptAdmins: keep.length};
    } finally { lock.releaseLock(); }
  },
  adm_reset: function (d) {   // xoá dữ liệu các phần được chọn (cần confirm = 'RESET')
    var me = adminOnly_(d), parts = d.parts || [], res = {};
    if (String(d.confirm) !== 'RESET') throw new Error('Thiếu xác nhận.');
    if (!parts.length) throw new Error('Chưa chọn phần nào.');
    var lock = LockService.getScriptLock(); lock.waitLock(30000);
    try {
      parts.forEach(function (k) {
        if (k === 'students' || k === 'teachers') {
          var role = k === 'students' ? 'student' : 'teacher', sh = sheetOf_(SHEET_USERS, USER_HEADERS), us = readUsers_().filter(function (u) { return u.role === role; });
          us.map(function (u) { return u.row; }).sort(function (a, b) { return b - a; }).forEach(function (r) { deleteRowSafe_(sh, r); });
          us.forEach(function (u) { CacheService.getScriptCache().remove('ping_' + u.username); });
          res[k] = us.length;
        } else if (k === 'sessions') {
          var n = 0; readUsers_().forEach(function (u) { if (u.role !== 'admin' && (u.sid || u.dev)) { u.sid = ''; u.dev = ''; writeUser_(u, false); CacheService.getScriptCache().remove('ping_' + u.username); n++; } });
          res[k] = n;
        } else {
          if (k === 'users') throw new Error('Dùng "học sinh" / "giáo viên" để xoá tài khoản.');
          var p = bkPart_(k), s2 = ss_().getSheetByName(p.sheet); res[k] = s2 ? wipeData_(s2) : 0;
        }
      });
    } finally { lock.releaseLock(); }
    return {deleted: res};
  },
  adm_result_delete: function (d) {   // xoá một hay nhiều lần nộp (admin hoặc giáo viên toàn quyền)
    var me = authUser_(d, ['admin', 'teacher']);
    if (!has_(me, 'full')) throw new Error('Chỉ admin hoặc giáo viên toàn quyền được xoá kết quả.');
    var sh = ss_().getSheetByName(GRADE_SHEET_RESULT), items = d.items || [];
    if (!sh || !items.length) return {deleted: 0, skipped: items.length};
    var h = sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0], col = {}; h.forEach(function (x, i) { col[x] = i; });
    var del = 0, skip = 0, lock = LockService.getScriptLock(); lock.waitLock(30000);
    try {
      var v = sh.getDataRange().getValues(), seen = {}, ok = [];
      items.forEach(function (it) {
        var r = +it.row, row = v[r - 1];
        if (!(r >= 2) || !row || seen[r]) { skip++; return; }
        if (String(row[col['Tài khoản']] || '').toLowerCase() !== String(it.username || '').toLowerCase() || String(row[col['Bộ bài']]) !== String(it.set_id) || String(row[col['Trang']]) !== String(it.page_id)) { skip++; return; }
        seen[r] = 1; ok.push(r);
      });
      ok.sort(function (a, b) { return b - a; }).forEach(function (r) { deleteRowSafe_(sh, r); del++; });
    } finally { lock.releaseLock(); }
    return {deleted: del, skipped: skip};
  },
  adm_results: function (d) { return {rows: resultRows_(authUser_(d, ['admin', 'teacher']), d)}; },
  my_results: function (d) { return {rows: resultRows_(authUser_(d), d, true)}; }
};

function resultRows_(me, d, onlyMe) {
  var sh = ss_().getSheetByName(GRADE_SHEET_RESULT);
  if (!sh || sh.getLastRow() < 2) return [];
  var v = sh.getDataRange().getValues(), h = v[0], col = {};
  h.forEach(function (x, i) { col[x] = i; });
  var ui = col['Tài khoản'], mine = null;
  if (!onlyMe && me.role === 'teacher' && !readAll_(me)) mine = teacherClasses_(me.username);
  var out = [];
  for (var i = v.length - 1; i >= 1 && out.length < 3000; i--) {
    var r = v[i], user = ui === undefined ? '' : String(r[ui] || '').toLowerCase(), cls = String(r[col['Lớp']] || '');
    if (onlyMe && user !== me.username) continue;
    if (mine && mine.indexOf(cls) < 0) continue;
    if (d.cls && cls !== d.cls) continue;
    if (d.username && user !== String(d.username).toLowerCase()) continue;
    if (d.set_id && String(r[col['Bộ bài']]) !== d.set_id) continue;
    out.push({row: i + 1, hasEv: !!(col['Sự kiện vi phạm'] !== undefined && r[col['Sự kiện vi phạm']]), time: fmtT_(r[0]), type: r[col['Loại']], name: r[col['Học sinh']], cls: cls, username: user, set_id: r[col['Bộ bài']], page_id: r[col['Trang']], mode: r[col['Chế độ']],
      score: r[col['Điểm']], total: r[col['Tổng']], pct: r[col['%']], score10: r[col['Thang 10']], time_spent: r[col['Thời gian làm (s)']],
      tab: r[col['Chuyển tab']], blur: r[col['Mất focus']], fs: r[col['Thoát toàn màn hình']]});
  }
  return out;
}

/* ----- sao lưu / khôi phục / reset (chỉ admin) ----- */
var BK_PARTS = {
  users: {name: 'Tài khoản (admin, giáo viên, học sinh)', sheet: SHEET_USERS, headers: USER_HEADERS},
  classes: {name: 'Lớp học', sheet: SHEET_CLASSES, headers: CLASS_HEADERS},
  assign: {name: 'Bài đã giao', sheet: SHEET_ASSIGN, headers: ASSIGN_HEADERS},
  results: {name: 'Kết quả nộp bài', sheet: GRADE_SHEET_RESULT},
  practice: {name: 'Hoạt động luyện tập', sheet: GRADE_SHEET_PRACTICE},
  log: {name: 'Nhật ký', sheet: GRADE_SHEET_LOG},
  feedback: {name: 'Góp ý', sheet: SHEET_FB, headers: FB_HEADERS},
  reminders: {name: 'Nhắc nhở', sheet: SHEET_REM, headers: REM_HEADERS}
};
function bkPart_(k) { var p = BK_PARTS[k]; if (!p) throw new Error('Phần dữ liệu không hợp lệ: ' + k); return p; }
function adminOnly_(d) { var me = authUser_(d, ['admin']); return me; }
function wipeData_(sh) {   // xoá mọi dòng dữ liệu, giữ dòng tiêu đề
  var last = sh.getLastRow(), n = 0;
  if (last > 1) { n = last - 1; sh.getRange(2, 1, n, Math.max(1, sh.getLastColumn())).clearContent(); }
  return n;
}
function cellOut_(x) { return x instanceof Date ? fmtT_(x) : x; }
function deleteRowSafe_(sh, r) {
  try { sh.deleteRow(r); } catch (e) { sh.getRange(r, 1, 1, Math.max(1, sh.getLastColumn())).clearContent(); }
}

function handleApi(d) {
  try {
    var fn = API[d.action];
    if (!fn) throw new Error('Hành động không hợp lệ.');
    var r = fn(d); r.ok = true;
    return jsonOut_(r);
  } catch (err) {
    var m = String(err.message || err), code = '';
    if (m.indexOf('SESSION|') === 0) { code = 'session'; m = m.slice(8); }
    return jsonOut_({ok: false, error: m, code: code});
  }
}

/* Danh tính người làm bài: lấy từ token (không tin họ tên/lớp do trình duyệt gửi). */
function identity_(d) {
  var t = verifyToken_(d.token);
  var u = t ? findUser_(t.u) : null;
  if (u && u.active && (u.role === 'admin' || (u.sid && u.sid === t.s))) return {username: u.username, name: u.name, cls: u.cls, role: u.role};
  return null;
}

/* Chỉ cần khi dùng CÁCH 2 (script riêng). Với CÁCH 1 hãy xoá doPost này, giữ doPost cũ. */
function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);
    var a = String(d.action || '');
    if (a.indexOf('grade_') === 0) return handleGrade(d);
    if (/^(auth_|adm_|my_|fb_|team_)/.test(a)) return handleApi(d);
    return ContentService.createTextOutput('ignored');
  } catch (err) { return ContentService.createTextOutput('error: ' + err); }
}

/* Kiểm tra nhanh: mở link /exec trên trình duyệt phải hiện "GRADE script OK". */
function doGet(e) { return ContentService.createTextOutput('GRADE script OK'); }

/* Chạy thử trong trình soạn thảo (chọn hàm testWrite > Run): cấp quyền + ghi 1 dòng thử vào Sheet. */
function testWrite() {
  handlePractice({event: 'enter', student_name: 'TEST', student_class: 'x', set_id: 'test', page_id: 'test'});
  Logger.log('Đã ghi thử – xem tab ' + GRADE_SHEET_PRACTICE);
}


// Gio Viet Nam dang dd/MM/yyyy HH:mm:ss (thay cho chuoi UTC ISO)
function tsVN_(ts) {
  var dt = ts ? new Date(ts) : new Date();
  if (isNaN(dt.getTime())) dt = new Date();
  return Utilities.formatDate(dt, 'Asia/Ho_Chi_Minh', 'dd/MM/yyyy HH:mm:ss');
}
