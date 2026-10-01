# -*- coding: utf-8 -*-
"""Đáp án + giải thích – Test 9 – Mid-term 1 (Đề ôn tập giữa HK1 Anh 11 Global 25-26 – Đề 10).
Đáp án lấy từ khoá tô màu trong Word (src/mt1/d10.txt) rồi tự giải độc lập để đối chiếu.
Phần nghe: đối chiếu script Word với Whisper (large-v3) trên file mp3 (Task 1 và Task 2, mỗi bài nghe 2 lần) – trùng khớp."""

GHI_CHU_RA_SOAT = [
    'Audio: file mp3 gốc dài 368 s chỉ gồm đúng phần nghe của đề (Task 1 + Task 2, mỗi task 2 lần); không cần cắt. Nội dung khớp script Word.',
    'g1.4: nguồn gõ "What does Math pay" -> sửa thành "Matt".',
    'g3.9-g3.14, g3.19: nguồn thiếu nhãn "A." ở phương án đầu -> đã bổ sung; g3.19 "train s" -> "trains".',
    'g3.15: khoá Word A (have to); "must" (D) cũng đúng ngữ pháp và nghĩa (nội quy bắt buộc) -> chấp nhận A và D.',
    'g3.18 và g3.10 giữ nguyên khoá Word (think; had to).',
    'g8: ô trống chỉ là phần cần viết; chấp nhận nhiều cách viết hợp lý (xem ANS). Khoá Word 38: "first time Linda has listened to this song".',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ======================= NGHE – TASK 1 (Matt) =======================
put('g1', [
    ('A', 'Script: "Like many boys of his own age, Matt <b>loved watching TV and playing video games</b> in his free time." (Matt từng thích xem TV và chơi điện tử lúc rảnh.)'),
    ('C', 'Script: "<b>His uncle has just found out he has a heart disease</b>, the same condition that Matt\'s late grandfather suffered from. This news has pushed Matt to make some changes." -> chú bị bệnh tim.'),
    ('C', 'Script: "Even when he\'s late for school, Matt now tries to make time for a <b>healthy breakfast</b>." -> ăn sáng nhanh trước khi đến trường. (Anh ấy ăn ít chất béo và muối hơn, không phải bỏ hẳn nên A sai.)'),
    ('B', 'Script: "He also <b>pays more attention to his fitness</b> and works out properly." (Matt chú ý hơn tới thể lực/rèn luyện sức khoẻ.)'),
], 1)

# ======================= NGHE – TASK 2 (Anna & grandpa) =======================
put('g2', [
    ('T', 'Grandpa: "I <b>moved to this city when I was just 8 years old</b>." -> ông sống ở thành phố từ năm 8 tuổi. ĐÚNG.'),
    ('F', 'Grandpa: "To get to places, I had to <b>walk or use my bike</b>." -> ông đi bộ hoặc đi xe đạp, không dùng xe điện. SAI.'),
    ('T', 'Grandpa: "<b>Pollution, traffic jams, and a lack of green space</b> are just a few problems facing our city." ĐÚNG.'),
    ('T', 'Anna: "Aware of these problems, people are solving them with car-free transport systems and roof gardens ... <b>You should watch the documentary</b>." ĐÚNG.'),
], 5)

# ======================= LEXICO-GRAMMAR 9-19 =======================
put('g3', [
    ('C', 'life <b>expectancy</b> = tuổi thọ. expect (động từ), expectation (sự mong đợi), expectational (hiếm dùng). Tạm dịch: Tuổi thọ của chúng ta đã tăng trong vài thập kỷ qua.'),
    ('A', 'In the past ... "but now they have more freedom" -> nghĩa vụ trong quá khứ: <b>had to</b> follow. must/mustn\'t là hiện tại; didn\'t have to (không cần) sai nghĩa.'),
    ('B', '"when I was young" (quá khứ) -> <b>was</b> often ill. "I" đi với was, không đi với were.'),
    ('D', 'adapt to change = thích nghi với thay đổi (Gen Z sáng tạo và thích phiêu lưu). accept/follow/build không đi với "to change" theo nghĩa này.'),
    ('A', 'The <b>housing problem</b> in the city = vấn đề nhà ở (giá cao, ít lựa chọn giá rẻ). house problem không dùng; rooftop farming/farm không liên quan.'),
    ('B', 'looks + tính từ: looks <b>beautiful</b> from a distance (trông đẹp từ xa).'),
    (['A', 'D'], 'Nội quy bắt buộc: All students <b>have to / must</b> wear uniforms. Khoá Word là A (have to); "must" (D) cũng đúng nên chấp nhận cả hai. "don\'t have to" = không cần; "should" chỉ là lời khuyên.'),
    ('B', 'Check the <b>ingredients</b> of all food products = kiểm tra thành phần trong thực phẩm để biết mình ăn gì.'),
    ('C', 'Câu sau nói "a lot of green space ... more plants and animals" -> thành phố <b>sustainable</b> (bền vững). popular/efficient/polluted không khớp với ngữ cảnh.'),
    ('A', 'Cấu trúc nêu ý kiến: "I <b>think</b> they won\'t force him ..." (think là động từ trạng thái, dùng hiện tại đơn; thì tiếp diễn không hợp).'),
    ('A', 'Everyday ... heavy <b>traffic jams</b> on many streets = tắc đường nặng sau giờ làm.'),
], 9)

# ======================= CLOZE 20-24 =======================
put('g4', [
    ('A', '<b>take part in</b> = tham gia. Tạm dịch: Mỗi công dân được khuyến khích tham gia bảo vệ môi trường.'),
    ('B', '<b>Each</b> area ... will have smart waste bins: sau Each dùng danh từ số ít (area). All + danh từ số nhiều; A/Some không hợp ngữ cảnh.'),
    ('C', 'be equipped <b>with</b> = được trang bị (cái gì). Tạm dịch: Tất cả đường phố sẽ được trang bị camera hiện đại.'),
    ('B', 'this <b>urban development</b> city project: urban development là cụm danh từ (phát triển đô thị) bổ nghĩa cho "city project".'),
    ('D', 'a <b>sustainable</b> future = tương lai bền vững: trước danh từ future cần tính từ.'),
], 20)

# ======================= READING 25-29 =======================
put('g5', [
    ('B', 'Bài mở đầu bằng câu hỏi khoảng cách thế hệ ở Mỹ có còn nghiêm trọng không, rồi nói "the tension between generations has been <b>alleviated</b>" -> chủ đề: sự giảm bớt khoảng cách thế hệ ở Mỹ ngày nay.'),
    ('A', '"..., instead of going to church every weekend, <b>they</b> were exposed to various forms of social media" -> they = teenagers (thanh thiếu niên) ở đầu câu.'),
    ('D', '"they were exposed to various forms of social media like <b>television and radios</b>." -> truyền hình và radio.'),
    ('C', '"many older people were conservative and <b>didn\'t accept differences disturbing their normal life</b>" -> họ không muốn thay đổi cuộc sống bình thường.'),
    ('C', 'Suy luận: người lớn tuổi học dùng laptop/điện thoại từ con cháu nên khoảng cách thu hẹp -> dạy người già dùng thiết bị hiện đại có thể thu hẹp khoảng cách thế hệ. A, B quá tuyệt đối; D trái với bài (người lớn ít chỉ trích gu nhạc hơn).'),
], 25)

# ======================= SẮP XẾP 30-32 =======================
put('g6', [
    ('B', 'd – c – b – a: Bà đang làm gì? (d, câu hỏi mở đầu) -> Vâng, giúp cháu với (c) -> Không sao đâu, cháu sẽ chỉ từng bước (b) -> Cảm ơn cháu (a).'),
    ('A', 'b – d – c – e – a: câu chủ đề về xung đột (b) -> First, thanh thiếu niên nên bày tỏ bình tĩnh (d) -> Also, cha mẹ tránh so sánh (c) -> khi hai bên tôn trọng nhau (e) -> In conclusion (a).'),
    ('D', 'a – d – c – e – b: giới thiệu năng lượng tái tạo (a) -> These innovations (d) làm giao thông nhanh/sạch hơn -> Besides (c) -> However (e) -> In conclusion (b).'),
], 30)

# ======================= WORD FORM 33-37 =======================
put('g7', [
    (['creative'], 'the most <b>creative</b> generation: sau "the most" + danh từ cần tính từ (CREATE -> creative). Tạm dịch: Thế hệ Z tự coi mình là thế hệ sáng tạo nhất từ trước đến nay.'),
    (['generational'], 'The <b>generational</b> conflicts = xung đột giữa các thế hệ: tính từ đứng trước danh từ conflicts (GENERATION -> generational).'),
    (['has examined', 'has been examining'], '"since she came to the hospital" -> hiện tại hoàn thành: The doctor <b>has examined</b> her patients thoroughly.'),
    (['arguments'], 'a lot of <b>arguments</b> = nhiều cuộc tranh cãi: sau "a lot of" dùng danh từ số nhiều (ARGUE -> arguments).'),
    (['exercise'], 'should + V nguyên mẫu: he should <b>exercise</b> regularly (nên tập thể dục đều đặn).'),
], 33)

# ======================= VIẾT LẠI CÂU 38-41 =======================
put('g8', [
    (['first time Linda has listened to this song', 'first time Linda has ever listened to this song', 'first time that Linda has listened to this song',
      'first time Linda has listened to this song before'],
     'Linda has never listened to this song before = This is the <b>first time</b> Linda <b>has listened</b> to this song (cấu trúc This is the first time + S + have/has + V3). Điền vào ô: first time Linda has listened to this song.'),
    (['don\'t have to live with', 'do not have to live with'],
     'it is not necessary for ... to V = S + <b>don\'t have to</b> V. Điền: don\'t have to live with (câu sau ô trống là "their parents").'),
    (['should spend more time'],
     'It\'s a good idea for parents to ... = Parents <b>should</b> spend more time with their children. Điền: should spend more time.'),
    (['hasn\'t played basketball for', 'has not played basketball for'],
     'He gave up playing basketball 3 years ago = He <b>hasn\'t played</b> basketball <b>for</b> 3 years (hiện tại hoàn thành phủ định + for). Điền: hasn\'t played basketball for.'),
], 38)
