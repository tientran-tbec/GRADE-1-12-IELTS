# Hướng dẫn nhanh – Dự án luyện tập Tiếng Anh lớp 1–12 (hiện có Lớp 11 · Unit 1–2)

## Mở thử
Mở `index.html` bằng trình duyệt → chọn bộ (Bài tập bổ trợ / Bài tập 4 kỹ năng) → chọn trang.
- Trang **Luyện tập**: chọn đáp án là có chấm + giải thích ngay (điền từ: bấm *Kiểm tra* hoặc Enter).
- Trang **Kiểm tra**: có đồng hồ, cảnh báo còn 10 phút, ghi nhận chuyển tab/thoát toàn màn hình, nộp xong mới hiện giải thích.

## Nối Google Sheet – cách 1 nút bấm
Bấm đúp **setup_apps_script.bat** (cần Node.js, đăng nhập Google 1 lần). File tự tạo Apps Script mới, ghi vào Google Sheet cũ (ID 1Xl515…jqikQ, sheet `Lop6-12_KetQua`, `Lop6-12_NhatKy`), lấy link /exec và gắn vào web. Sau đó chạy `push_github.bat`.
(Cách thủ công: dán `handleGrade()` vào code.gs cũ như hướng dẫn trong file `code.gs`.)

Nhật ký luyện tập: tab `Lop1-12_LuyenTap` ghi 3 sự kiện/phiên (VÀO LÀM, LÀM LẠI, RỜI TRANG) kèm số câu đã làm/đúng, câu sai, số lần làm lại. Cần dán bản `code.gs` mới này vào Apps Script rồi Deploy lại.

## Đưa lên GitHub
Chạy `push_github.bat` (build lại + push lên https://github.com/tientran-tbec/GRADE-1-12-IELTS.git, nhánh main).
Lần đầu: GitHub repo → Settings → Pages → Branch `main` / root. Link web: https://tientran-tbec.github.io/GRADE-1-12-IELTS/

## Sửa nội dung
- Câu hỏi: `units/*.py` (không chạy lại `tools/gen_units.py` vì sẽ ghi đè các chỉnh sửa tay).
- Đáp án + giải thích: `units/*_dapan.py` (ANS / EXPLANATIONS). Câu không có ANS → hiện "đáp án đang cập nhật".
- Sau khi sửa: `python update_links.py` rồi `python tests/smoke_test.py` (cần `pip install playwright`).

## Thêm Unit mới
Thêm 1 dòng vào REGISTRY trong `build.py`, tạo `units/<ten>.py` + `<ten>_dapan.py`, chép ảnh vào `assets/`, mp3 vào `audio/`.


## Đẩy lên GitHub (1 file)
Bấm đúp `push_github.bat`. Lần đầu nó hỏi link repo (lưu vào `.repo_url`). Sau đó tự build, push, chờ ~60 giây và báo `[OK]` nếu trang thật đã dùng link Apps Script mới.
