# Hướng dẫn dựng đề Lớp 4 (cho agent phụ)

Dự án: web bài tập tĩnh `/home/claude/proj` (build bằng `python build.py`). Mục tiêu: chuyển các đề thi Lớp 4 (docx đã dump sang text + ảnh) thành bộ bài trắc nghiệm có chấm điểm.

## Nguồn
- Text đã dump: `/home/claude/g4/exi/<tên>.txt` (⟦ ⟧ = đoạn tô vàng trong docx = thường là ĐÁP ÁN; `[img:imgNN]` = vị trí ảnh).
- Ảnh tách sẵn: `/home/claude/g4/exi/<tên>/imgNN.png` (nền trắng). **Hãy xem ảnh bằng Read khi cần biết tranh nói gì.**
- docx gốc: `/home/claude/g4/ex/thuvienhoclieu.com-<tên>.docx` (có thể render `soffice --headless --convert-to pdf --outdir /tmp/x file.docx` rồi `pdftoppm -r 70 -png` để xem bố cục thật, rồi Read ảnh).
- Âm thanh: `/home/claude/g4/mp3/*.mp3` (tên `thuvienhoclieu.com-Nghe-...mp3`). Không thể nghe/phiên âm → đáp án phần nghe phải lấy từ KEY/Audio script trong đề.

## Thư viện `tools/g4_exam.py` (ĐỌC FILE NÀY TRƯỚC) — mẫu dùng: `tools/gen_lop4_gk2.py`, `tools/gen_lop4_cuoiky.py`, `tools/gen_lop4_gk1_nghe.py` (định dạng "Question n." -> `build_qn`)
```
ex = Exam(tag, unit, title, src, slug='testNN', minutes=35, warn_at=5, audio=[tên mp3,...] hoặc None)
   tag: duy nhất, vd 'on1_de5'  | unit: thư mục (OnHK1, OnHK2, CuoiKy1, DeCuongHK1, DeCuongHK2, HSG ...) | src: tên file dump (không .txt) | slug: test05 ... (duy nhất trong unit)
   audio: nhiều file sẽ được nối, ghi ra audio/lop4_<tag>.mp3
ex.mcq_words(gid, instr, rows[[a,b,c]], keys['B','A'..], q=...)        # chọn từ (chữ)
ex.mcq_pics(gid, instr, rows[[img,img,img]], keys, q=...)              # chọn tranh A/B/C (ghép dải ảnh có nhãn); phần tử row có thể là dict {'q','o'} để đổi sang câu chữ
ex.mcq_text(gid, instr, rows[(imgs|None, câu hỏi, [opts])], keys)      # câu hỏi (kèm ảnh) + đáp án chữ; keys là CHỮ CÁI A/B/C
ex.fill(gid, instr, rows[(q có {_}, [đáp án chấp nhận], img|None|list, giải thích)], passage=html, bank=[từ])
ex.tf(gid, instr, rows[(câu,'T'|'F', img|None, giải thích)], passage=html)
ex.order(gid, instr, rows[(words, câu đúng)])                          # words kèm dấu câu dính từ, vd 'sister.' 'like?'; check_set bắt buộc cùng multiset từ với đáp án
ex.match(gid, instr, left[{'t':..,'img':..}], opts[], keys[], exp, picture=html)  # nối: mỗi dòng 1 ô chọn
ex.number_pics(...)
ex.add(gid, instr, [(item_dict, ANS, EXP)...], passage=, bank=)        # mức thấp, tự tạo item (t='mcq'|'tf'|'fill'|'order'|'match'|'open')
ex.single(imgs, 'ten.png', w, h)  -> lưu ảnh (có thể ghép nhiều ảnh) vào assets/lop4_<tag>/ ; ex.strip(imgs, labels, out) ghép dải có nhãn ; ex.asset('ten.png') -> đường dẫn dùng trong passage <img class="wide" src=...>
ex.save()   # ghi units/lop4_<tag>.py, _dapan.py, units/reg/<tag>.json (đăng ký) và nối mp3
Dump(src).sec()/.keys() ; rows_words/rows_pics/rows_q/keyletters/blank_answers/passage()/parse_keys/imgs/cells ; std_family / std_cuoi (họ đề có sẵn) ; parse_qn/build_qn (định dạng "Question n.")
```
Quy ước quan trọng:
- mcq (chữ): ANS là **chữ cái** 'A'/'B'/'C'...; mcq `plain` (chỉ A/B/C dưới ảnh): ANS là giá trị trong `o`. tf: 'T'/'F'. fill: danh sách đáp án chấp nhận (không phân biệt hoa/thường/dấu câu/’). order: [câu đúng]. match: {'blanks': [[x],...]}.
- Mọi câu phải có EXPLANATION (lib tự tạo). Id câu: `<gid>.<số thứ tự liên tục toàn đề>`.
- Chỉ dùng đáp án có trong đề (KEY/ĐÁP ÁN/tô vàng). Câu nào không xác định chắc đáp án → bỏ câu và ghi vào `ex.notes`. KHÔNG bịa đáp án. Phần Speaking → bỏ.
- Tranh nào mất dấu hiệu phân biệt (vd các tranh A/B/C giống hệt nhau do mất vòng tròn/dấu tick) → chuyển thành câu chữ từ script nghe (xem `PT` trong gen_lop4_gk2.py) hoặc bỏ câu.
- Phần nghe chỉ giữ nếu có file mp3 tương ứng; không có mp3 → bỏ phần nghe, `minutes` điều chỉnh, ghi notes. Đề có audio: truyền `audio=[...]`.
- minutes: đề đủ 4 kỹ năng 35–40; đề ngắn 15–25. warn_at 3–5.
- Trang đề test: slug bắt đầu `test`.

## Việc của bạn
1. Viết **một file** `tools/gen_lop4_<nhóm>.py` (chạy được độc lập `python3 tools/gen_lop4_<nhóm>.py`) dựng các đề được giao. Chỉ tạo file mới: units/lop4_<tag>*, assets/lop4_<tag>/, audio/lop4_<tag>.mp3, units/reg/<tag>.json, tools/gen_lop4_<nhóm>.py. **KHÔNG sửa** build.py, engine/, tools/g4_exam.py, tools/g4_hl.py hay file của agent khác. Nếu cần hàm mới → viết trong file riêng của bạn. Nếu lib có lỗi → ghi lại ở báo cáo (đừng sửa).
2. Kiểm tra: `python3 tools/check_set.py lop4_<tag>` → 0 lỗi, cho mọi tag.
3. Kiểm tra giao diện: **KHÔNG chạy build.py trong /home/claude/proj** (nhiều agent chạy chung). Sao chép: `cp -r /home/claude/proj /tmp/p_<nhóm>` rồi `cd /tmp/p_<nhóm> && python build.py` và chạy `python3 /tmp/shot.py <đường dẫn tuyệt đối tới WebBaiTap/Lop4/<unit>/<slug>/kiem-tra.html> /tmp/<nhóm>_x.png` (cắt ảnh bằng PIL rồi Read để xem) cho ít nhất 1–2 đề/nhóm; và smoke test đúng đề của bạn: `cd /tmp/p_<nhóm> && python3 tests/smoke_test.py Lop4/<Unit>/<slug>/` (điền đáp án đúng, phải 100%). (Chạy nền với timeout nếu lâu.)
4. Báo cáo cuối (ngắn, tiếng Việt): mỗi đề bao nhiêu câu, câu/đoạn nào bị bỏ hoặc nghi ngờ đáp án và lý do, lỗi lib nếu có. Không dán code.

Tiêu đề (title) kiểu: `Ôn HK1 – Đề 5`, `Cuối kỳ 1 – Đề 17 (25-26)`.

## Phụ lục cho nhóm Đề cương / HSG (không phải đề thi)
Mỗi tài liệu → 1 bộ (set) kiểu luyện tập (slug `luyentap`, không phải `test`), unit = `DeCuongHK1` / `DeCuongHK2` / `HSG`:
- `theory`: HTML (chuỗi) chuyển từ docx: bảng từ vựng, mẫu câu, ngữ pháp (dùng `<h3>`, `<table class="tb">`, `<p>`, `<ul>`; xem units/lop4_u1_luyentap.py để biết mẫu `theory` và cấu trúc SET có `pages` với `'mode': 'practice'`). Ảnh trong tài liệu nếu cần thì lưu bằng PIL vào assets/lop4_<tag>/ và dùng `<img src="../../../../assets/lop4_<tag>/x.png">` (xem cách gen_lop4.py làm: tools/gen_lop4.py, hàm write_set/build_unit).
- Trang luyện tập (pages, mode practice): lấy từ các bài tập có đáp án trong tài liệu; nếu tài liệu chỉ có lý thuyết/từ vựng thì tự sinh bài trắc nghiệm từ vựng (Anh→Việt, 4 lựa chọn, nhiễu lấy từ chính tài liệu) và điền từ/trắc nghiệm mẫu câu — **nhưng chỉ dùng nội dung có trong tài liệu**. Mỗi bộ ≥ 1 trang luyện tập, mỗi trang ≤ ~40 câu (chia trang nếu nhiều).
- Đăng ký: ghi `units/reg/<tag>.json` = `[set_id, 'units/lop4_<tag>.py', 'units/lop4_<tag>_dapan.py', 'Lop4', '<Unit>', 'luyentap', 'assets/lop4_<tag>', '']` (nếu có nhiều bộ cùng unit thì slug khác nhau: luyentap, luyentap2, ...). set id dạng `lop4-<tag-với-gạch-ngang>`.
- Dùng `ex = Exam(...)` được nhưng `save()` luôn sinh trang mode test; với đề cương hãy tự dựng SET + ANS + EXPLANATIONS và ghi file giống save() (xem mã save()). Có thể dùng class Exam để lấy `ex.add`/`ex.groups`/`ex.ANS`, rồi tự tạo page practice thay vì dùng save().
