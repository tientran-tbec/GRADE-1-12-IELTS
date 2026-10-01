/**
 * GOOGLE APPS SCRIPT – nhận kết quả bài luyện tập / kiểm tra lớp 6-12 (GRADE-6-12).
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
var GRADE_SHEET_RESULT = 'Lop6-12_KetQua';
var GRADE_SHEET_LOG = 'Lop6-12_NhatKy';

function handleGrade(d) {
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    var ss = SpreadsheetApp.openById(SHEET_ID);
    var isResult = d.action === 'grade_save_result' || d.action === 'grade_save_partial';
    var sh = ss.getSheetByName(isResult ? GRADE_SHEET_RESULT : GRADE_SHEET_LOG) || ss.insertSheet(isResult ? GRADE_SHEET_RESULT : GRADE_SHEET_LOG);
    if (isResult) {
      if (sh.getLastRow() === 0) { sh.appendRow(['Thời gian', 'Loại', 'Học sinh', 'Lớp', 'Bộ bài', 'Trang', 'Chế độ', 'Điểm', 'Tổng', '%', 'Thang 10',
        'Thời gian làm (s)', 'Chuyển tab', 'Mất focus', 'Thoát toàn màn hình', 'Số lần nghe', 'Chi tiết câu trả lời']); sh.setFrozenRows(1); }
      sh.appendRow([d.ts || new Date().toISOString(), d.action === 'grade_save_partial' ? 'LƯU DỞ (rời trang)' : 'ĐÃ NỘP',
        d.student_name, d.student_class, d.set_id, d.page_id, d.mode, d.score, d.total, d.pct, d.score10,
        d.time_spent, d.tab_switch, d.blur, d.fullscreen_exit, d.audio_plays, d.answers ? JSON.stringify(d.answers) : '']);
    } else {
      if (sh.getLastRow() === 0) { sh.appendRow(['Thời gian', 'Sự kiện', 'Học sinh', 'Lớp', 'Bộ bài', 'Trang', 'Chế độ']); sh.setFrozenRows(1); }
      sh.appendRow([d.ts || new Date().toISOString(), 'VÀO BÀI', d.student_name, d.student_class, d.set_id, d.page_id, d.mode]);
    }
    return ContentService.createTextOutput('ok');
  } catch (err) {
    return ContentService.createTextOutput('error: ' + err);
  } finally { lock.releaseLock(); }
}

/* Chỉ cần khi dùng CÁCH 2 (script riêng). Với CÁCH 1 hãy xoá doPost này, giữ doPost cũ. */
function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);
    if (String(d.action || '').indexOf('grade_') === 0) return handleGrade(d);
    return ContentService.createTextOutput('ignored');
  } catch (err) { return ContentService.createTextOutput('error: ' + err); }
}
