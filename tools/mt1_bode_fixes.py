# -*- coding: utf-8 -*-
# Sửa lỗi nguồn + đáp án cho gen_mt1_bode.py (được exec trong gen_mt1_bode.py)
_COMMON_SRC = [('Read of the following', 'Read the following')]
FIX = {
 1: {'src': _COMMON_SRC,
     'notes': [
        'Sửa nguồn: chỉ dẫn "Read of the following leaflet" -> "Read the following leaflet" (câu 7-12).',
        'Q34 (EXCEPT): khoá Word = D (property values không được nhắc tới) - đúng; các dòng giải thích ĐÚNG của A/B/C nghĩa là "có trong bài".',
        'Q9 (touchscreen/display): cả 2 đều hợp nghĩa ("The beautiful display is large and clear"); ANS = [A, B], khoá Word = A.',
        'Q12 (Lots/Dozens/Hundreds/Plenty + of): về ngữ pháp cả 4 đều dùng được; giữ khoá Word = D, câu MƠ HỒ - nên xem xét loại câu hoặc chấp nhận mọi đáp án.',
     ],
     'key': {9: (['A', 'B'], 'Q9: chấp nhận cả A (touchscreen) và B (display)')}},
 2: {'src': _COMMON_SRC + [('Health mordern experts', 'Health modern experts')],
     'notes': [
        'Sửa nguồn: chỉ dẫn "Read of the following leaflet" -> "Read the following leaflet" (câu 7-12); Q2 phương án A "mordern" -> "modern".',
        'Q9 (melody/lyrics): "The lyrics of our songs will touch your heart" cũng hợp lý; ANS = [B, C], khoá Word = B.',
        'Q12 (Plenty/Lots/A number + of): A, B, D đều đúng ngữ pháp; giữ khoá Word = A, câu MƠ HỒ (Some of tickets mới sai).',
        'Q17 (sắp xếp): khoá Word b-e-c-a-d (B); thứ tự b-a-e-c-d (C) cũng khá mạch lạc ("The piano pieces..." nối tự nhiên sau b); giữ khoá Word.',
        'Q31 (were all ears ~ take in): nghĩa thực là "rất chăm chú/háo hức nghe"; "listen in" (nghe lén) cũng gần; giữ khoá Word = C.',
        'Q6: "To learn to balance..." (D) cũng đúng ngữ pháp nhưng gượng; giữ khoá Word = C (Learning).',
     ],
     'key': {9: (['B', 'C'], 'Q9: chấp nhận cả B (melody) và C (lyrics)')}},
 3: {'src': _COMMON_SRC + [('(20__________', '(20)_________'), ('Paragrapgh', 'Paragraph'),
                           ('sonic Pi', 'Sonic Pi'), ('earSketch', 'EarSketch'), ('tidalCycles', 'TidalCycles'), ('codeHarmony', 'CodeHarmony')],
     'notes': [
        'Sửa nguồn: "Read of the following leaflet" -> "Read the following leaflet"; ô trống "(20__________" -> "(20) ______"; "Paragrapgh" -> "Paragraph" (Q29-30); '
        'tên nền tảng ở Q34 viết hoa đúng (Sonic Pi, EarSketch, TidalCycles, CodeHarmony).',
        'Q9 (project/program): "The innovation of our program" cũng hợp lý (Word loại vì lặp từ, không thuyết phục); ANS = [C, D], khoá Word = C.',
        'Q11 (services/platform/resources): platform và resources cũng dùng được; giữ khoá Word = C, câu MƠ HỒ.',
        'Q12 (A lot/few/majority/number of): A lot / A number / A few / A majority đều đúng ngữ pháp; giữ khoá Word = A, câu MƠ HỒ.',
        'Q31 (struck gold ~ hit upon / lucked out): "lucked out" cũng gần nghĩa; giữ khoá Word = D.',
     ],
     'key': {9: (['C', 'D'], 'Q9: chấp nhận cả C (project) và D (program)')}},
}
