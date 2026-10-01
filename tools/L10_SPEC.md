BỐI CẢNH. Project root: /home/claude/proj — web luyện tập tĩnh Tiếng Anh (user Tiên, giáo viên VN; trả lời tiếng Việt, ngắn gọn). Lớp 11 Unit 1–3 đã xong. Đang thêm "Lớp 10 · Unit 1 – Family Life" (sách Global Success), gồm 3 bộ độc lập, đã đăng ký trong build.py REGISTRY (KHÔNG sửa build.py, units/fixes.py, index):
  lop10-u1-luyentap  -> units/lop10_u1_luyentap.py  + units/lop10_u1_luyentap_dapan.py   (thư mục ảnh assets/lop10_u1/luyentap, audio/lop10_u1_luyentap_nghe.mp3 nếu có)
  lop10-u1-botro     -> units/lop10_u1_botro.py     + ..._dapan.py                        (assets/lop10_u1/botro, audio/lop10_u1_botro_nghe.mp3)
  lop10-u1-chuyensau -> units/lop10_u1_chuyensau.py + ..._dapan.py                        (assets/lop10_u1/chuyensau)
Mỗi agent làm ĐÚNG MỘT bộ (được giao ở prompt), không đụng file của bộ khác.

NGUỒN đã trích sang văn bản (tools/extract.py; ⟦…⟧ = tô sáng/đỏ = thường là khoá đáp án, <u> gạch chân, <b> đậm, [IMG:tên] ảnh): src/l10u1/lt.txt|lt_c.txt (luyện tập, KHÔNG có khoá), bt.txt|bt_c.txt (bổ trợ), cs.txt|cs_c.txt (chuyên sâu, đề), cs_key.txt|cs_key_c.txt (chuyên sâu có khoá). *_c.txt = bản đã bỏ dòng trống/thẻ bảng. File Word gốc ở /mnt/user-data/uploads/04. GRADE 1-12/GRADE 10/{1. BÀI TẬP LUYỆN TẬP, 2. BÀI TẬP BỔ TRỢ/0. GỐC, 3. BÀI TẬP CHUYÊN SÂU}/ (ảnh: unzip word/media; audio bổ trợ: ...Nghe-Bai-tap-bo-tro-...UNIT-1-FAMILY-LIFE.mp3 — nén ffmpeg mono 64k vào audio/).

MẪU PHẢI THEO (đọc kỹ trước): tools/gen_units_u3_botro.py + tools/gen_units_u3_4kn.py(nếu có)/gen_units_u3_4kn + tools/gen_units.py + tools/parse_src.py + tools/theory.py (cách sinh dữ liệu; generator một lần, viết bằng python), units/lop11_u3_botro.py và units/lop11_u3_4kn.py (định dạng SET: id, title, grade, unit, theory HTML, pages[{id,title,mode,groups[{id,instr,note,items[]}]}]), units/lop11_u3_botro_dapan.py (ANS + EXPLANATIONS + put()/put_open(), GHI_CHU_RA_SOAT), build.py (build_quiz_page, render_item — xem các kiểu câu: mcq, tf, tfng, fill, open; cách hiển thị ảnh, đoạn văn, bảng), units/fixes.py, tools/check_set.py.

QUY ƯỚC:
- File: tools/gen_l10u1_<slug>.py (generator), units/lop10_u1_<slug>.py, units/lop10_u1_<slug>_dapan.py.
- SET: id 'lop10-u1-<slug>', title 'Unit 1 – Family life: Bài tập luyện tập' / 'Bài tập bổ trợ' / 'Bài tập chuyên sâu', 'grade': 10, 'unit': 1, theory = phần lý thuyết (từ vựng, cấu trúc, ngữ pháp) lấy từ file Word, dựng bảng class="th" như Lớp 11 (dùng tools/theory.py nếu phù hợp).
- Chia trang như Lớp 11 theo kỹ năng: phat-am, tu-vung-ngu-phap (hoặc tu-vung + ngu-phap), nghe (chỉ khi có audio), noi, doc, viet, và một trang 'kiem-tra' (mode 'test', có minutes) cho đề kiểm tra có sẵn trong Word (vd 15-minute test, 45-minute test của bộ luyện tập). Mỗi bài tập trong Word thành một group với instr đúng đề bài. Không bỏ sót bài tập nào. Câu trọng âm/phát âm dùng <u>…</u> giữ nguyên gạch chân.
- id câu: '<mã nhóm>.<số thứ tự>'; id duy nhất toàn bộ. Trang test: phần sau dấu chấm là SỐ CÂU liên tục toàn đề.
- Ảnh trong đề: trích ra assets/lop10_u1/<slug>/ và dùng như Lớp 11 (xem cách gen_units_u3_4kn render ảnh).
- Đáp án: bộ có khoá (chuyên sâu, bổ trợ nếu có tô màu) → lấy từ khoá RỒI TỰ GIẢI độc lập để đối chiếu; khoá Word sai/mơ hồ → dùng đáp án đúng, ghi GHI_CHU_RA_SOAT; mơ hồ nhiều đáp án đúng → ANS là list. Bộ KHÔNG có khoá (luyện tập) → tự giải từng câu cẩn thận (ngữ pháp, từ vựng, bài đọc dựa vào nội dung bài), ghi rõ ở GHI_CHU_RA_SOAT các câu chưa chắc để giáo viên xem lại.
- Mỗi câu (trừ open) có ANS và EXPLANATIONS tiếng Việt ngắn gọn, nêu lý do (từ khoá, quy tắc ngữ pháp, nghĩa). Câu viết/mở (open) có đáp án mẫu trong EXPLANATIONS. Câu điền từ (fill) nhận danh sách đáp án chấp nhận được.
- Sửa lỗi nguồn (ký tự rác, số câu nhảy, phương án bị cắt…) trong generator và ghi vào GHI_CHU_RA_SOAT.
- Kiểm tra bắt buộc: `python tools/check_set.py lop10_u1_<slug>` = 0 lỗi; sau đó `python build.py lop10-u1-<slug>` (chạy build cho riêng bộ này, KHÔNG chạy build toàn bộ) rồi mở một vài trang trong WebBaiTap/Lop10/Unit1/<slug>/ bằng playwright (python, chromium sẵn có), điền đáp án đúng, nộp, xác nhận 100% và không lỗi JS (xem tests/smoke_test.py, tests/authstub.py để tham khảo cách mở trang không cần đăng nhập). Không hỏi lại; tự quyết hợp lý.
- Báo cáo cuối (≤ 200 từ, tiếng Việt): số trang, số câu mỗi trang, có nghe/ảnh không, danh sách câu đã sửa khoá hoặc còn nghi ngờ, tên file tạo ra.


---
BỔ SUNG CHO UNIT 2 & 3 (Lớp 10). Unit 1 đã xong — LÀM THEO ĐÚNG KIỂU của units/lop10_u1_*.py, units/lop10_u1_*_dapan.py và tools/gen_l10u1_*.py (cùng cấu trúc trang, cách ghi GHI_CHU_RA_SOAT, cách test). Thay u1→uN:
  Unit 2 = HUMANS AND THE ENVIRONMENT (title 'Unit 2 – Humans and the environment: ...'), nguồn src/l10u2/{lt,bt,cs}.txt và *_c.txt.
  Unit 3 = MUSIC (title 'Unit 3 – Music: ...'), nguồn src/l10u3/{lt,bt,cs}.txt và *_c.txt.
  id: lop10-uN-luyentap | lop10-uN-botro | lop10-uN-chuyensau; file units/lop10_uN_<slug>.py và _dapan.py, tools/gen_l10uN_<slug>.py, ảnh assets/lop10_uN/<slug>/, audio audio/lop10_uN_<slug>_nghe.mp3 (đã đăng ký sẵn trong build.py; KHÔNG sửa build.py). Build riêng: python build.py lop10-uN-<slug>.
  Word gốc ở /mnt/user-data/uploads/04. GRADE 1-12/GRADE 10/... (Unit 3 bổ trợ có mp3 'Nghe-Bai-tap-bo-tro-...UNIT-3-MUSIC.mp3' cùng thư mục "2. BÀI TẬP BỔ TRỢ/0. GỐC"; Unit 2 bổ trợ không có mp3 -> không có trang nghe audio, nếu Word có bài nghe thì giữ dạng câu hỏi không audio hoặc bỏ và ghi chú).
  Chỉ lấy đúng nội dung của Unit đó; nếu file nguồn lẫn nội dung unit khác (vd ôn tập nhiều unit) thì chỉ lấy phần đúng unit, ghi chú.
  Nếu bộ có khoá tô màu (⟦…⟧) thì lấy khoá rồi tự giải đối chiếu; nếu không có khoá thì tự giải kỹ và ghi các câu chưa chắc.
