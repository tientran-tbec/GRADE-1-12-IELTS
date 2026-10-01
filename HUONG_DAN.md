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

---

## Đăng nhập & quản lý giáo viên – học sinh

**Vai trò:** *Admin* (toàn quyền: lớp, giáo viên, học sinh, kết quả) · *Giáo viên* (chỉ học sinh/kết quả của lớp được gán) · *Học sinh* (làm bài, xem điểm của mình). Mọi trang bài tập đều yêu cầu đăng nhập; kết quả gắn với tài khoản (máy chủ lấy họ tên/lớp từ token, không tin dữ liệu trình duyệt gửi).

**Cài đặt (làm 1 lần):**
1. Apps Script → xoá code cũ, dán toàn bộ `code.gs` mới.
2. Tìm dòng `var ADMIN_PASS = '';` → đặt mật khẩu admin (≥ 6 ký tự) → chọn hàm **setupAdmin** → *Run* (cấp quyền nếu được hỏi). Xong **xoá lại** mật khẩu khỏi dòng đó và lưu.
3. *Triển khai → Quản lý bản triển khai → ✏️ → Phiên bản: Phiên bản mới → Triển khai* (link `/exec` giữ nguyên).
4. Chạy `push_github.bat` để đưa web mới lên.
5. Mở `…/login.html`, đăng nhập `admin` → tab **Lớp** (tạo lớp) → tab **Giáo viên** (thêm GV, gán lớp ở tab Lớp) → tab **Học sinh** (*Nhập danh sách*: dán họ tên mỗi dòng, hệ thống tự tạo tên đăng nhập + mật khẩu; tải CSV/in phát cho học sinh).

**Quy ước:** tên đăng nhập tự sinh từ họ tên (Trần Văn An → `antv`, trùng thì thêm số). Mật khẩu ngẫu nhiên 6 ký tự, học sinh/giáo viên phải đổi ở lần đăng nhập đầu. Quên mật khẩu → giáo viên/admin bấm *Đặt lại MK*. Đăng nhập sai 5 lần bị khoá 10 phút. Phiên đăng nhập hết hạn sau 3 ngày.

**Lưu ý bảo mật:** web chạy trên GitHub Pages (tệp tĩnh) nên cổng đăng nhập chỉ chặn ở trình duyệt – người rành kỹ thuật vẫn có thể mở thẳng file bài tập (đáp án nằm trong trang). Điều được bảo vệ chắc chắn là **dữ liệu**: danh sách tài khoản, quản lý, và kết quả chỉ ghi/đọc qua máy chủ khi có token hợp lệ. Mật khẩu lưu dạng băm (SHA-256 có muối) trong tab `Users` của Sheet – đừng chia sẻ Sheet này.

**Kiểm thử tự động:** `node tests/backend_test.js` (40 kiểm tra logic máy chủ), `python tests/auth_e2e_test.py` (24 kiểm tra giao diện đăng nhập → quản lý → làm bài → xem điểm).

### Bổ sung: giao bài, sửa học sinh, 1 thiết bị / 1 tài khoản
- **Thêm / sửa học sinh trên web:** admin và giáo viên bấm *+ Thêm học sinh* hoặc *Nhập danh sách* (gán lớp ngay khi tạo); bấm *Sửa* để đổi họ tên, chuyển lớp (giáo viên chỉ chuyển trong các lớp mình phụ trách); *Khoá / Mở khoá*; *Đặt lại MK*.
- **Giao bài:** tab *Giao bài* (hoặc nút *Giao bài* ở tab Lớp) → chọn lớp → tích các bộ bài (Unit, Test, Ôn tập…) → *Lưu*. Học sinh chỉ thấy và làm được bài đã giao cho lớp mình; vào link bài chưa giao sẽ bị đưa về trang chủ, và máy chủ cũng từ chối ghi kết quả của bài chưa giao. Giáo viên chỉ giao cho lớp mình phụ trách. Lớp chưa được giao bài thì học sinh thấy thông báo "Chưa có bài nào được giao".
- **Mỗi tài khoản một thiết bị:** học sinh/giáo viên đang đăng nhập ở một thiết bị thì thiết bị khác không đăng nhập được (admin không bị giới hạn). Thiết bị đang dùng gửi tín hiệu mỗi 60 giây; nếu tắt trình duyệt mà không bấm *Đăng xuất*, sau khoảng 3 phút tài khoản được giải phóng. Giáo viên/admin có thể bấm *Đăng xuất thiết bị* ở danh sách để giải phóng ngay (cột *Thiết bị* hiện ● Đang đăng nhập). Đặt lại mật khẩu cũng đăng xuất thiết bị đang dùng.
- Sau khi cập nhật `code.gs`, tab `Users` tự thêm 2 cột *Phiên*, *Thiết bị* và tab `Assignments` tự tạo — chỉ cần dán code, Deploy bản mới và chạy `push_github.bat`.
