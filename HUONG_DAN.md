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

## IELTS Reading (mục IELTS trên trang chủ)

- Nguồn: `ielts_src/reading/FullTest` (10 đề) và `ielts_src/reading/TheoDang/<Dạng>` (74 trang, 5 dạng). Giữ nguyên nội dung; khi `build.py` chạy sẽ chèn đăng nhập + cầu nối kết quả rồi ghi ra `WebBaiTap/IELTS/Reading/`.
- **Thêm/sửa đề:** thay file trong `ielts_src/reading/...` (giữ tên `TestN_Reading.html`, `TestN_PassageP_<Dạng>.html`) rồi chạy `python build.py` và `push_github.bat`.
- **Lớp IELTS:** tab *Lớp* → tạo lớp, ô *Khối* nhập `IELTS`. Tab *Giao bài* của lớp IELTS chỉ liệt kê 15 mục: Full Test 1–10 và 5 dạng bài (giao 1 dạng = mở toàn bộ trang của dạng đó).
- Học sinh đã đăng nhập không phải nhập tên/lớp; kết quả vào cùng Sheet (`Lop1-12_KetQua`, `Lop1-12_NhatKy`) với cột *Chế độ* = `ielts-reading`, *Chi tiết* bắt đầu bằng `Band x.x`. Admin/giáo viên làm thử không ghi.
- Listening, Writing, Speaking: thẻ "Sắp có" (chỉ admin/giáo viên thấy).
- **Phải dán lại `code.gs` và Deploy phiên bản mới** (có thêm nhật ký sự kiện IELTS).


## Giao diện, nhiều lớp, hạn nộp, góp ý
- Tên hệ thống: **GRADE 1-12-IELTS** (trang chủ, đăng nhập, quản trị, điểm của tôi).
- **Học sinh nhiều lớp:** khi thêm/sửa học sinh, tick nhiều lớp (nhập danh sách: ngăn các lớp bằng dấu `;`, vd `Nguyễn Văn An, 11A1;IELTS1`). Học sinh thấy bài được giao cho mọi lớp mình thuộc; kết quả ghi vào lớp đã giao bài đó. Giáo viên chỉ đổi được các lớp mình phụ trách, lớp của giáo viên khác được giữ nguyên.
- **Hạn nộp:** tab Giao bài → ô ngày cạnh bộ đã tích (hoặc chọn ngày rồi *Áp dụng* cho cả các bộ đã tích). Hết ngày hạn (giờ VN) bài hiện mờ “Hết hạn”, không vào làm được; bài đang làm dở nộp được trong 60 phút (ghi “ĐÃ NỘP (TRỄ HẠN)”).
- **Tab Tiến độ:** số trang đã nộp, điểm TB thang 10 theo lớp; nút Tải CSV (cũng có ở tab Kết quả).
- **Góp ý:** xem mục *Quy tắc ô góp ý* bên dưới (cũng có trong `tools/MT1_SPEC.md`).


---

## QUY TẮC BẮT BUỘC: Ô GÓP Ý (CHAT HỌC SINH ↔ GIÁO VIÊN) — ÁP DỤNG CHO MỌI BÀI TẬP / TEST (WEB)

Mọi trang bài (luyện tập, kiểm tra, IELTS Reading/Listening/Writing/Speaking, bài mới sau này) đều phải có **nút "💬 Góp ý"** để học sinh gửi ý kiến về bài cho giáo viên, và giáo viên trả lời lại (chat qua lại, mỗi học sinh một cuộc trò chuyện cho mỗi trang bài).

**Cách có được tính năng này (không cần viết lại trong từng file HTML):**
1. Ô góp ý là `engine/feedback.js`, được `build.py` / `ielts.py` **tự chèn vào cuối mọi trang** khi build. Người tạo đề **không** tự viết khung chat, **không** tự gọi API góp ý.
2. Đưa đề vào đúng chỗ để build bọc được: IELTS → `ielts_src/reading/FullTest/TestN_Reading.html` hoặc `ielts_src/reading/TheoDang/<Dạng>/TestN_PassageP_<Dạng>.html` (tên file đúng mẫu); bài Lớp 1–12 → khai báo trong `REGISTRY` của `build.py`. Trang phải có đủ thẻ `<head>` và `</body>`.
3. Kỹ năng/bộ bài mới (vd Listening, Writing, Speaking, Lớp khác): thêm vào `ielts.py` (hoặc `REGISTRY`) với **mã bộ bài** riêng — ô góp ý dùng mã bộ bài + tên file trang để tách cuộc trò chuyện, nên không cần cấu hình thêm.

**Ràng buộc khi thiết kế trang (để ô góp ý không bị che / không bị chặn):**
- Nút góp ý nằm ở **cạnh phải, khoảng giữa-trên màn hình** (`right:0; top:38%`, z-index 9990–9991). Không đặt nút/phần tử `position:fixed` khác vào vùng này; các phần tử cố định khác dùng z-index < 9990.
- Không dùng id/class bắt đầu bằng `gnfb-`.
- Chức năng chống gian lận (chặn dán/chuột phải/phím tắt) không được chặn bên trong `.gnfb-box` (ô góp ý đã tự `stopPropagation` cho copy/paste; đừng thêm listener chặn phím ở pha capture lên `textarea`).
- Chỉ tài khoản **học sinh** thấy nút; admin/giáo viên làm thử không thấy. Học sinh chỉ góp ý được ở bài đã được giao cho mình.

**Phía giáo viên / admin:** trang Quản trị → tab **Góp ý** (hộp thư, chấm đỏ số tin chưa đọc, trả lời ngay). Giáo viên thấy góp ý của học sinh thuộc lớp mình phụ trách; admin thấy tất cả. Học sinh thấy chấm đỏ khi có trả lời, và liệt kê trong trang **Điểm của tôi → Góp ý của tôi**.

**Dữ liệu:** tab Sheet `Feedback` (mỗi tin một dòng: thời gian, học sinh, lớp, bộ bài, trang, người gửi, nội dung, đã đọc…). API `fb_send`, `fb_list`, `fb_mine`, `fb_inbox`, `fb_thread`, `fb_reply` (trong `code.gs`). Giới hạn 1000 ký tự/tin, tối đa 20 tin / 10 phút / học sinh.


## Giáo viên nhiều lớp, giao bài theo học sinh, bộ lọc lớp
- **Giáo viên phụ trách nhiều lớp:** tab *Giáo viên* → nút **Lớp phụ trách** → tích các lớp. Một lớp cũng có thể có nhiều giáo viên (tab *Lớp* → Sửa → tích nhiều giáo viên).
- **Giao bài theo học sinh:** tab *Giao bài* → tích bộ bài → bấm nút **👥 Cả lớp** cạnh bộ đó → tích những học sinh được giao. **Không tích ai (hoặc tích hết) = giao cho cả lớp.** Cùng một lớp có thể giao bộ A cho cả lớp, bộ B chỉ cho vài em.
- **Bộ lọc tab Lớp:** theo khối (kể cả IELTS), giáo viên, tình trạng (chưa giao bài / chưa có học sinh / chưa có giáo viên) và ô tìm mã/tên lớp.
- **Giờ hiển thị:** mọi thời gian trong trang quản trị hiện dạng `dd/MM/yyyy HH:mm:ss` giờ Việt Nam.


## Phân quyền thêm (giáo viên) và chức vụ học sinh (trưởng nhóm / phó nhóm)

**Giáo viên** – Quản trị → tab *Giáo viên* → nút **Quyền** → tích các quyền cấp thêm:
- **Giao bài**: giao/bỏ giao bộ bài, đặt hạn, giao theo từng học sinh (cho các lớp mình phụ trách). Giáo viên cũ giữ quyền này khi nâng cấp.
- **Xem lớp khác (chỉ đọc)**: xem học sinh, kết quả, tiến độ của mọi lớp.
- **Góp ý mọi lớp**: xem và trả lời góp ý ở mọi lớp.
- **Quản lý lớp**: tạo, sửa, xoá lớp và gán giáo viên.
- **Học sinh ngoài lớp mình**: thêm, sửa, đặt lại mật khẩu, khoá học sinh bất kỳ lớp nào.
Không tích gì = giáo viên chỉ xem kết quả/góp ý và quản lý học sinh của lớp mình. Chỉ admin cấp được quyền.

**Học sinh** – tab *Học sinh* → nút **Chức vụ** (admin hoặc giáo viên quản lý học sinh đó): chọn *Trưởng nhóm* / *Phó nhóm* cho từng lớp rồi tích quyền:
- **Xem tiến độ cả lớp** (ai đã nộp bộ nào; không xem đáp án) · **Xem điểm từng bạn** · **Nhắc nộp bài** · **Góp ý thay nhóm**.
Học sinh có chức vụ thấy khu **Nhóm của tôi** ở trang *Điểm của tôi*. Bạn được nhắc thấy chấm đỏ và thẻ **Nhắc nhở**. Mỗi bạn chỉ bị nhắc 1 lần cho mỗi bộ trong 6 giờ; mỗi người nhắc tối đa 8 lần/giờ. Góp ý của nhóm hiện trong hộp thư *Góp ý* của giáo viên (cuộc trò chuyện “Góp ý của nhóm – lớp …”).
Dữ liệu: Users có thêm cột **Quyền**, **Chức vụ** (tự thêm); tab mới **Reminders**.

## Toàn quyền, xem lại bài làm, trang tổng kết học sinh

- **Cấp toàn quyền cho giáo viên**: Quản trị → tab Giáo viên → nút "⭐ Cấp toàn quyền" (thu hồi bằng "Thu hồi toàn quyền"). Giáo viên đó ngang admin, chỉ không được tạo/sửa/xem tài khoản admin.
- **Xem lại bài làm**: tab Kết quả → nút "Xem bài" hiện từng câu: học sinh chọn gì, đáp án đúng, đúng/sai/bỏ trống (có lọc chỉ câu sai). Bài IELTS chỉ xem được dòng tóm tắt đã lưu.
- **Cảnh báo**: nút "⚠ n lần" hiện danh sách vi phạm kèm mốc phút:giây (chuyển tab, dán, copy, phím tắt...). Bài nộp trước bản cập nhật chỉ có số lần, không có chi tiết.
- **Trang tổng kết**: bấm tên học sinh ở tab Kết quả → trang `student.html?u=<tài khoản>` gồm thông tin, bài được giao, mọi lần nộp, hoạt động luyện tập, tải CSV.
- Sheet kết quả có thêm cột 19 "Sự kiện vi phạm" (tự tạo). Xem bài cần web chạy trên GitHub Pages (http/https).

## Sao lưu, khôi phục, reset, xoá kết quả, trang quản lý học sinh

- **Quản trị → tab "Sao lưu · Reset"** (chỉ admin):
  1. *Sao lưu*: tích các phần (tài khoản, lớp, bài đã giao, kết quả, luyện tập, nhật ký, góp ý, nhắc nhở) → tải 1 file `.json`. File có mã băm mật khẩu, cất cẩn thận.
  2. *Khôi phục*: chọn file → tích phần cần nạp → "Thay thế" (xoá dữ liệu hiện tại của phần đó rồi nạp lại) hoặc "Nối thêm". Khôi phục tài khoản luôn giữ admin hiện có.
  3. *Reset*: tích phần cần xoá sạch (học sinh, giáo viên, phiên đăng nhập, lớp, bài giao, kết quả, luyện tập, nhật ký, góp ý, nhắc nhở), gõ `RESET` để xác nhận. Mặc định tự tải file sao lưu trước khi xoá. Tài khoản admin không bao giờ bị xoá.
- **Xoá kết quả** (admin hoặc giáo viên toàn quyền): tab Kết quả có ô chọn nhiều dòng + nút "Xóa đã chọn", và nút "Xóa" ở từng dòng.
- **Trang quản lý học sinh**: ở tab Học sinh, bấm tên → `student.html`: sửa tên/lớp, chức vụ nhóm, đặt lại mật khẩu, đăng xuất thiết bị, khoá/mở khoá, xem bài đã giao, mọi lần nộp (xem bài, cảnh báo, xoá), hoạt động luyện tập.
- Code.gs mới có thêm các hàm `adm_backup_info`, `adm_backup`, `adm_restore`, `adm_reset`, `adm_result_delete` — cần Deploy phiên bản mới.

## Tăng tốc (đợt B)
- Máy chủ lưu đệm danh sách tài khoản 5 phút (tự làm mới khi có sửa tài khoản) và chỉ mở file Sheet 1 lần mỗi lần gọi.
- Học sinh: trình duyệt hỏi máy chủ tối đa 1 lần / 2 phút khi chuyển trang, và 3 phút/lần khi để trang mở. Giáo viên/admin luôn cập nhật quyền khi mở trang. Đăng xuất thiết bị khác có thể mất tới ~3 phút mới có hiệu lực ở máy bị đăng xuất. Trạng thái "đang đăng nhập" tính trong 7 phút.
- Tab Kết quả: mặc định 7 ngày qua, tải 200 dòng, nút "Tải thêm"; có lọc Hôm nay / 7 ngày / 30 ngày / Tháng này / Mọi lúc. Tải CSV xuất tối đa 3000 dòng theo bộ lọc hiện tại.

## Trang quản trị nhanh hơn, khung dịch kéo thả, sửa khung góp ý
- Trang quản trị: mở lần đầu chỉ gọi máy chủ 1 lần (thay vì 3 lần nối tiếp); từ lần 2 hiện bảng ngay từ bản lưu trong trình duyệt rồi cập nhật ngầm. Tìm kiếm / lọc chạy tại chỗ. Khoá/mở khoá, cấp toàn quyền, xoá kết quả đổi giao diện ngay (lỗi thì tự hoàn lại). Có dải "⏳ Đang lưu…" khi đang ghi. Bản lưu tự xoá khi đăng xuất.
- Khung dịch (tra từ) kéo thả được: giữ chuột ở dải trên cùng "⠿ Kéo để di chuyển" (hoặc viền khung) rồi kéo; lần dịch sau mở đúng chỗ đã kéo.
- Khung 💬 Góp ý: nằm trên mọi lớp phủ (kể cả hộp thoại kết quả, trang IELTS), gõ / dán bình thường kể cả khi đang làm bài kiểm tra.

## Góp ý nhanh, hiện ở mọi trang, và Trợ lý AI
- Nút **💬 Hỏi · Góp ý** nổi bên phải hiện ở MỌI trang của học sinh (trang chủ, Điểm của tôi, mọi bài). Ở trang không thuộc bài nào, tin gửi vào "Góp ý chung" (giáo viên vẫn thấy trong tab Góp ý). Thanh menu có chữ "💬 Góp ý" kèm số tin mới.
- Gửi tin: tin hiện ngay khi bấm Gửi (có "⏳ đang gửi…"), gửi ngầm phía sau; lỗi thì hiện "Chưa gửi được – thử lại".
- **Trợ lý AI** (tab 🤖 trong cùng khung): hỏi từ vựng, ngữ pháp, cách làm bài. **Chỉ tài khoản được admin cấp quyền** mới thấy tab này; chưa cấp thì học sinh chỉ gửi được góp ý cho giáo viên. **Ở mọi trang làm bài (có nút Nộp bài), AI chỉ mở sau khi học sinh nộp bài.** AI tự đọc nội dung trang (bài đọc, câu hỏi, đáp án/giải thích) nên học sinh chỉ cần gõ "Giải thích chi tiết câu 32", không cần bôi đen hay chép lại. Mặc định 50 lượt / học sinh / ngày, 100 lượt / giáo viên / ngày, admin không giới hạn (chỉnh ở tab "Trợ lý AI"). Giáo viên xem lại mọi câu hỏi ở Quản trị → tab "Trợ lý AI".
- **Cấp quyền AI:** tab Học sinh / Giáo viên → nút **🤖 Cấp AI** / **Thu AI** ở từng dòng; tab Học sinh có nút **Cấp AI cho danh sách đang lọc** (lọc theo lớp rồi cấp cả lớp) và **Thu AI**; trang quản lý từng học sinh cũng có nút. Quyền có hiệu lực trên máy học sinh sau vài phút (khi trang tự cập nhật) hoặc khi tải lại. Giáo viên thường chỉ cấp được cho học sinh mình quản lý. Giáo viên/admin được cấp sẽ thấy khung "🤖 Trợ lý AI" ở trang chủ và trang bài.
- **Cài đặt Gemini miễn phí (admin, làm 1 lần):** vào aistudio.google.com → Get API key → Create API key (không cần thẻ). Apps Script → Project Settings → Script properties → thêm `GEMINI_API_KEY` = khoá vừa tạo. Triển khai lại code.gs (Deploy → Manage deployments → Edit → New version). Tab "Trợ lý AI" sẽ báo "Đã có khoá Gemini". Mô hình thử theo thứ tự từ mạnh → nhẹ: `gemini-3.8-flash, 3.7-flash, 3.6-flash, 3.5-flash, 3.5-flash-lite, 3.1-flash-lite`. Mô hình nào đang bận/hết lượt miễn phí thì hệ thống tự chuyển sang mô hình nhẹ hơn (mô hình bận được bỏ qua 2 phút rồi thử lại). Sửa danh sách ở ô "Mô hình Gemini" (ngăn bằng dấu phẩy). Nhật ký ghi rõ mỗi câu trả lời do mô hình nào. Gói miễn phí có giới hạn lượt/phút và /ngày; hết lượt học sinh thấy "đang bận / hết lượt miễn phí". Google có thể dùng nội dung hỏi ở gói miễn phí để cải thiện sản phẩm → dặn học sinh không nhập thông tin cá nhân (hệ thống không gửi họ tên cho AI).
- **Muốn dùng Claude thay Gemini:** thêm `ANTHROPIC_API_KEY` (console.anthropic.com, trả phí) rồi chọn "Claude" ở ô Dịch vụ trong tab "Trợ lý AI".
- Cần Deploy phiên bản mới của Apps Script (có các hàm `ai_chat`, `ai_status`, `adm_ai_get`, `adm_ai_save`).
