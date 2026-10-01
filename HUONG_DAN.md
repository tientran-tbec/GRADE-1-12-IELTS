# Hướng dẫn nhanh – Dự án luyện tập Tiếng Anh 11 (Unit 1)

## Mở thử
Mở `index.html` bằng trình duyệt → chọn bộ (Bài tập bổ trợ / Bài tập 4 kỹ năng) → chọn trang.
- Trang **Luyện tập**: chọn đáp án là có chấm + giải thích ngay (điền từ: bấm *Kiểm tra* hoặc Enter).
- Trang **Kiểm tra**: có đồng hồ, cảnh báo còn 10 phút, ghi nhận chuyển tab/thoát toàn màn hình, nộp xong mới hiện giải thích.

## Nối Google Sheet (ghi kết quả học sinh)
Web đang trỏ sẵn tới URL Apps Script production cũ (Sheet ID 1Xl515…jqikQ). Các action của dự án này có tiền tố `grade_` nên không đụng code cũ.
1. Mở **code.gs cũ** (Apps Script) → dán hàm `handleGrade()` + 3 hằng `SHEET_ID / GRADE_SHEET_*` từ file `code.gs` này vào cuối file.
2. Trong `doPost()` cũ, ngay sau dòng parse JSON thêm: `if (String(data.action||'').indexOf('grade_')===0) return handleGrade(data);`
3. Deploy → Manage deployments → Edit → New version (URL giữ nguyên).
→ Kết quả vào sheet **Lop6-12_KetQua** (đã nộp / lưu dở khi rời trang), vào bài ghi ở **Lop6-12_NhatKy**.
Muốn dùng script/sheet MỚI: `python update_links.py "<link Sheet>" "<link /exec>"`.

## Đưa lên GitHub
Chạy `push_github.bat` (build lại + push lên https://github.com/tientran-tbec/GRADE-6-12.git, nhánh main).
Lần đầu: GitHub repo → Settings → Pages → Branch `main` / root. Link web: https://tientran-tbec.github.io/GRADE-6-12/

## Sửa nội dung
- Câu hỏi: `units/*.py` (không chạy lại `tools/gen_units.py` vì sẽ ghi đè các chỉnh sửa tay).
- Đáp án + giải thích: `units/*_dapan.py` (ANS / EXPLANATIONS). Câu không có ANS → hiện "đáp án đang cập nhật".
- Sau khi sửa: `python update_links.py` rồi `python tests/smoke_test.py` (cần `pip install playwright`).

## Thêm Unit mới
Thêm 1 dòng vào REGISTRY trong `build.py`, tạo `units/<ten>.py` + `<ten>_dapan.py`, chép ảnh vào `assets/`, mp3 vào `audio/`.
