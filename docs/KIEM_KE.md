# Kiểm kê code.gs → Firebase

## Hành động (doPost)
- grade_*: grade_practice, grade_rd_event, grade_save_result, grade_save_partial (ghi kết quả/nhật ký)
- auth_*: login, logout, me, ping, change_password
- adm_*: users, user_save, user_reset, user_kick, user_ai, users_import, teacher_perms, teacher_classes, classes, class_save, class_delete, assign_get/save, results, result_detail, result_delete, student_summary, student_ranks, bootstrap, ai_get/save, backup, backup_info, restore, reset
- my_*: results, reminders
- fb_*: send, list, mine, thread, reply, inbox
- team_*: fb, progress, remind
- ai_*: chat, status
- ly_*: essay, essay_list, essay_mine, essay_review
- tt_*: state, theory, board, home, overview, mode_get/set, cfg_set, progress, student, unlock, reset, resets, undo, remind, note_seen

## Sheet → Firestore collection
Users→users, Classes→classes, Assignments→assignments, Lop1-12_KetQua→results, Lop1-12_NhatKy→log,
Lop1-12_LuyenTap→practice, Feedback→feedback, Reminders→reminders, AI→aiLog, TuLuan→essays,
ThuThach→ttConfig, TienDo→ttProgress (id=user|step), TienDoLog→ttResetLog, TtNhacNho→ttNotes.

## Ràng buộc kỹ thuật cần thay
LockService→transaction; CacheService→cache bộ nhớ/doc tóm tắt; PropertiesService→Secret Manager + doc config;
UrlFetchApp (AI, TT_URL)→fetch; Utilities.computeDigest/HMAC→crypto; ContentService→HTTPS response.
Mật khẩu: giữ salt+hash cũ, kiểm tra kiểu cũ khi đăng nhập, sau đó nâng lên scrypt.
