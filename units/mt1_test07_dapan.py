# -*- coding: utf-8 -*-
"""Đáp án + giải thích – Test 7 – Mid-term 1 (Tiếng Anh 11 Global Success) – nguồn: Đề ôn tập giữa HK1 Anh 11 Global 25-26 (Đề 8).
Quy ước: mcq = chữ cái 'A'-'D' (hoặc list nếu nhiều đáp án đều đúng); fill = list đáp án chấp nhận.
Đáp án lấy từ khoá (tô màu ⟦…⟧) trong phần ĐÁP ÁN của Word, đã tự giải độc lập để đối chiếu.
Phần nghe: Word không có script; script nhận dạng bằng Whisper (large-v3) trên file RAW ...De-8.mp3, khớp khoá Word."""

GHI_CHU_RA_SOAT = [
    'Đánh lại số câu liên tục 1-38 (đề gốc đánh lại từ 1 ở mỗi phần). Đề gốc ghi "blanks from 1 to 6" nhưng chỉ có 5 ô -> sửa thành 1 to 5.',
    'File RAW ...De-8.mp3 có thêm Part 1 (hội thoại về cửa hàng quần áo, ~3,5 phút) không thuộc đề; đã cắt bỏ, audio/mt1_test07.mp3 bắt đầu từ "Now look at part two" (phần rạp chiếu phim, phát 2 lần).',
    'g1.4 (câu nghe 4): Whisper nghe "Hoxton" nhưng người đọc đánh vần H-A-U-X-T-O-N -> đáp án Hauxton (khớp khoá Word).',
    'g2.7 (Q7): khoá Word tô cả balanced (B) và regular (C) -> ANS = [B, C]; balanced diet là cụm chuẩn nhất.',
    'g2.12 (Q12): khoá Word = B (have to); must (D) cũng đúng nghĩa -> ANS = [B, D].',
    'g3.17 (Blank 1): khoá Word = A (Living); "To live an eco-friendly lifestyle is crucial" (B) cũng đúng ngữ pháp -> ANS = [A, B].',
    'g4.22 (EXCEPT): trong đề, Word tô cả 4 phương án; ở phần đáp án chỉ tô D (poor people eat more fatty foods) – đúng, vì bài nói chất béo chiếm 10% calo ở cộng đồng nghèo, 40% ở cộng đồng giàu.',
    'g2.15 (Q15): đề gốc ghi "You ______ must tidy up" (thừa must); câu đáp án dùng "You ______ tidy up" -> dùng dạng không có must. Phương án B gõ sai "musn\'t" -> mustn’t.',
    'Sửa nguồn: Q4 mất nhãn "A." (Experienced); Q8 "visted"/"lastweek" -> visited / last week; Q9 "Linda ... since he left" -> she; Q11 "I_____" -> "I ______."; Q3 "fat free" -> fat-free; passage "conies" -> comes; "Leaning English" -> Learning; câu hỏi dòng b Q3 sắp xếp bỏ dấu "?." thừa.',
    'g6.34 (HAPPY): từ gợi ý trùng với đáp án (looks happy) – giữ nguyên theo Word.',
    'g7.36: đáp án mẫu Word chỉ "understand teenage children"; đã chấp nhận thêm "try to understand their teenage children". g7.38: "Every staff" là cách dùng của nguồn.',
    'Đề không ghi thời gian: đặt 45 phút (38 câu).',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


put('g1', [
    (['meeting'], 'Script: "we will show an Italian film called <b>Midnight Meeting</b>" -> Meeting.'),
    (['monday'], 'Script: "You can see that film from <b>Monday</b> to Thursday." -> Monday.'),
    (['4', 'four'], 'Script: "Tickets are <b>£4</b>. But there is a special student ticket at £2.80" -> giá vé thường là 4 (vé sinh viên £2.80 là bẫy).'),
    (['hauxton'], 'Script: "The nearest car park to the cinema is in ... Street. That\'s <b>H-A-U-X-T-O-N</b>" -> đánh vần: Hauxton.'),
    (['5', 'five'], 'Script: "It\'s just <b>five</b> minutes\' walk from the cinema." -> 5.'),
], 1)

put('g2', [
    ('D', 'build your <b>muscles</b> = xây dựng cơ bắp (nâng tạ). health/treatment/habit không hợp với "build... lift weights".'),
    (['B', 'C'], 'a <b>balanced</b> diet = chế độ ăn cân bằng (với trái cây, rau, đạm) – cụm chuẩn. Khoá Word cũng tô "regular" (a regular diet = chế độ ăn thường xuyên/thông thường) nên chấp nhận cả hai.'),
    ('C', 'exercise <b>regularly</b> = tập thể dục đều đặn (trạng từ bổ nghĩa động từ exercise).'),
    ('C', 'come up with new ideas = nảy ra ý tưởng mới -> <b>creative</b> (sáng tạo). curious = tò mò; experienced = có kinh nghiệm; traditional = truyền thống.'),
    ('D', 'since + mốc quá khứ -> hiện tại hoàn thành: Linda <b>has lived</b> in this city since she left school.'),
    ('C', 'roof garden of <b>high-rise</b> buildings = vườn trên mái của các tòa nhà cao tầng.'),
    (['B', 'D'], 'Quy định của trường (bắt buộc): <b>have to</b> (hoặc must) obey the school rules. mustn\'t = cấm; should = nên (không đủ mạnh).'),
    ('A', 'last week -> quá khứ đơn: He <b>visited</b> his grandparents last week.'),
    ('D', 'Peter <b>has just finished</b> his essay: just đứng giữa trợ động từ has và V3; chủ ngữ số ít -> has.'),
    ('C', '"No one can clean it for you" -> nghĩa bắt buộc phải tự làm: You <b>must</b> tidy up your bedroom. (don\'t have to = không cần: sai nghĩa.)'),
    ('B', 'Please be quiet! I <b>am thinking</b> – hành động đang diễn ra ngay lúc nói (tiếp diễn).'),
], 6)

put('g3', [
    (['A', 'B'], 'Chủ ngữ của câu: <b>Living</b> an eco-friendly lifestyle is crucial (danh động từ làm chủ ngữ). Khoá Word chọn Living; "To live an eco-friendly lifestyle is crucial" cũng đúng.'),
    ('D', 'Trật tự tính từ trước danh từ: <b>simple daily habits</b> (simple = ý kiến/đặc điểm, daily = tính chất phân loại, đứng sát danh từ).'),
    ('B', 'feel <b>bored</b> with = cảm thấy chán với (tính từ -ed chỉ cảm xúc của người).'),
    ('D', 'contribute (efforts) <b>to</b> = đóng góp (nỗ lực) cho bảo vệ môi trường.'),
    ('A', '<b>make</b> a change = tạo ra sự thay đổi.'),
], 17)

put('g4', [
    ('D', 'Bài nói tỉ lệ calo từ chất béo là 10% ở cộng đồng nghèo và 40% ở cộng đồng giàu -> người nghèo ăn ÍT chất béo hơn, nên "poor people eat more fatty foods" là sai (câu EXCEPT). A, B, C đều đúng theo bài.'),
    ('D', '"Two fatty acids, linoleic and arachidonic acids, prevent these abnormalities and hence are called essential fatty acids. <b>They</b> are required by a number of other animals" -> They = <b>Fatty acids</b>.'),
    ('D', '"When rats are fed a fat-free diet, their growth eventually ceases" -> <b>They stop growing</b> (tăng trưởng ngừng lại). Các ý khác không được nhắc.'),
    ('B', '<b>essential</b> (thiết yếu) ≈ <b>necessary</b> (cần thiết).'),
    ('D', 'Bài bàn về chất đạm, chất béo, vitamin, axit béo thiết yếu... -> nhiều khả năng trích từ <b>A book on basic nutrition</b> (sách dinh dưỡng cơ bản).'),
], 22)

put('g5', [
    ('C', 'a (chào hỏi, How have you been?) – c (Mike trả lời và hỏi lại How about you?) – b (Sarah đáp "Same here..."): <b>a – c – b</b>.'),
    ('A', 'c (Emma chào mừng) – a (John chúc mừng, có quà) – d (Emma cảm ơn, hỏi là gì) – e (Open it and see!) – b (Wow! A beautiful blue scarf!): <b>c – a – d – e – b</b>.'),
    ('D', 'd (câu chủ đề: ba lý do) – c (First) – a (Second) – e (Third) – b (câu kết, câu hỏi tu từ): <b>d – c – a – e – b</b>.'),
], 27)

put('g6', [
    (['arguments', 'argument'], 'get into <b>arguments</b> (over...) = cãi vã – danh từ của ARGUE (số nhiều vì "different generations... sometimes").'),
    (['critical'], 'a <b>critical</b> thinker = người có tư duy phản biện – tính từ của CRITIC đứng trước danh từ thinker.'),
    (['have loved', 'have been loving'], 'since + mệnh đề quá khứ đơn -> hiện tại hoàn thành: John and Mary <b>have loved</b> each other since they were at high school.'),
    (['stay'], 'should not + V nguyên mẫu: You should not <b>stay</b> up late.'),
    (['happy'], 'look + tính từ: The little boy looks <b>happy</b> (trông vui vẻ).'),
], 30)

W = {}
W[35] = (['and Jean have learned how to drive for 2 weeks', 'and Jean have learnt how to drive for 2 weeks', 'and Jean have been learning how to drive for 2 weeks', 'and Jean have learned how to drive for two weeks'],
         'started ... 2 weeks ago -> hiện tại hoàn thành với for: <b>Mẫu:</b> Jack <b>and Jean have learned how to drive for 2 weeks</b>.')
W[36] = (['understand teenage children', 'try to understand their teenage children', 'try to understand teenage children', 'understand their teenage children'],
         'It is a good idea for... to V = lời khuyên -> should + V. <b>Mẫu:</b> Parents should <b>(try to) understand (their) teenage children</b>.')
W[37] = (['hasn\'t smoked since 2020', 'has not smoked since 2020'],
         'quit ... in 2020 -> hiện tại hoàn thành phủ định + since: <b>Mẫu:</b> He <b>hasn\'t smoked since 2020</b>.')
W[38] = (['mustn\'t smoke or eat in the office', 'must not smoke or eat in the office', 'mustn\'t smoke or eat in the office'],
         'isn\'t allowed to V = bị cấm -> mustn\'t + V. <b>Mẫu:</b> Every staff <b>mustn\'t smoke or eat in the office</b>.')
for n, (a, e) in W.items():
    ANS['g7.%d' % n] = a
    EXPLANATIONS['g7.%d' % n] = e
