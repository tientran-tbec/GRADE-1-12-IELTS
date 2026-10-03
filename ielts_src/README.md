# ielts_src — nguồn IELTS cho web (build bằng ielts.py)

Cây thư mục (mỗi kỹ năng một nhánh, cùng cấu trúc):

```
ielts_src/
  reading/                 <- ĐÃ XONG: 49 test
    FullTest/              Test{N}_Reading.html          (web full test, 60 phút, 40 câu)
    TheoDang/
      Completion/ Matching/ MultipleChoice/ TrueFalseNotGiven/ YesNoNotGiven/
                           Test{N}_Passage{P}_{Dạng}.html (web từng dạng, 1 passage)
    TaiLieu_Word/          Word: file tổng, TungTest/ (từng test), TheoDang/ (5 tài liệu theo dạng)
  listening/               <- SẮP LÀM (cùng kiểu: FullTest/, TheoDang/, TaiLieu_Word/, audio/)
  writing/                 <- SẮP LÀM
  speaking/                <- SẮP LÀM
tools/ielts_reading/       Bộ sinh Reading từ dữ liệu JSON (json/final2, json/expl2) -> HTML + Word. Xem README bên dưới.
```

Thêm kỹ năng mới: tạo ielts_src/<kỹ năng>/ theo đúng khuôn trên, rồi mở rộng ielts.py (hàm build đọc theo thư mục).
Sửa nội dung Reading: sửa JSON trong tools/ielts_reading/json/ rồi chạy
  python tools/ielts_reading/genweb.py   (HTML)   và   python tools/ielts_reading/gendocs.py   (Word)
(chạy từ thư mục tools/ielts_reading, kết quả ghi ra out2/PACK/... rồi chép đè vào ielts_src/reading).
