# -*- coding: utf-8 -*-
"""Đáp án + giải thích – Test 10 – Mid-term 1 (Tiếng Anh 11 Global Success) – nguồn: Đề ôn tập giữa HK1 Anh 11 Global – Đề 1.
Quy ước: mcq = chữ cái 'A'-'D' (hoặc list nếu nhiều đáp án đều đúng); fill = danh sách cách viết chấp nhận.
Word chỉ có khoá (tô màu) cho Q1–5 phần nghe và đáp án (đã tô) của câu 'POPULATE'; các phần còn lại tự giải.
Phần nghe: script nhận dạng bằng Whisper (large-v3) từ 2 file mp3 của đề."""

GHI_CHU_RA_SOAT = [
    'g1.2: khoá Word = B (their own food) nhưng audio: "I\'m going to make some nice food myself... I can only make things that are easy" -> A (simple food). Đã ghi đáp án ĐÚNG = A.',
    'g1.5: khoá Word = A (music CDs) nhưng audio: "I won\'t need a CD player. Some of my friends have offered to play music. They\'re in a band" -> B (play musical instruments). Đã ghi đáp án ĐÚNG = B.',
    'g1.1: khoá Word = A (chưa gửi thiệp) nhưng audio: "Have you sent everyone an invitation?" - "Yes, but they\'re still in the post" -> Zoe ĐÃ gửi, chưa ai nhận được -> C. Đã ghi đáp án ĐÚNG = C.',
    'g1.3, g1.4: khoá Word (B, C) khớp audio.',
    'g5.15: "because it\'s a rule" -> have to (B, quy định bên ngoài); "must" (C) cũng có thể chấp nhận -> giữ khoá B, đề xuất (nếu muốn thoáng) ANS = [B, C].',
    'g6.21: heading đoạn 1 mơ hồ (A bao quát cả đoạn, B nêu lợi ích ở nửa sau) -> ANS = [A, B].',
    'g8.36: "fair to / on / for the elder sister" đều dùng được -> chấp nhận to, on, for.',
    'g7.32: nguồn gõ nhầm "POLULATE" (-> POPULATE) và đáp án (overpopulation) bị tô cùng phần định nghĩa; đã sửa đề, đáp án = overpopulation.',
    'Sửa nguồn: "agressive" -> "aggressive"; "worst living conditions" -> "worse"; "constrasting" -> "contrasting"; "In American" giữ nguyên như đoạn văn gốc; thêm "I" vào câu preposition số 1 ("knew what food..." mất đại từ I).',
    'd1.txt chứa cả bộ 10 đề; Đề 1 chỉ gồm 39 câu (nghe 10, âm 4, từ vựng/ngữ pháp 6, đọc 8, từ loại 4, giới từ 4, viết lại 3). Không có ảnh. Đề không ghi giờ: 45 phút.',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ---------- Nghe (Part 1: Zoe & Pete)
put('g1', [
    ('C', 'Pete: "Have you sent everyone an invitation?" - Zoe: "Yes, but they\'re still in the post, so I don\'t know how many people will come yet." -> thiệp đã gửi nhưng còn đang trên đường qua bưu điện: <b>No one has received an invitation yet</b>. (Khoá Word ghi A là sai.)'),
    ('A', 'Zoe: "No, I\'m going to make some nice food myself... I can only make things that are easy" và "I don\'t need to [ask everyone to bring food]" -> khách ăn <b>simple food</b> (đồ ăn đơn giản Zoe tự nấu), không phải đồ họ mang theo. (Khoá Word ghi B là sai.)'),
    ('B', 'Zoe: "I\'m only going to have just a few friends. I won\'t feel comfortable if I invite my whole class or any people that I don\'t know very well." -> <b>a small number of friends</b>.'),
    ('C', 'Zoe: "I\'ll serve some snacks outside if the weather\'s nice, but we\'ll have the main course inside." -> chỉ phục vụ đồ ăn nhẹ ngoài trời: <b>will offer her friends some food outside</b>. Không có barbecue và tiệc chính ở trong nhà.'),
    ('B', 'Zoe: "I won\'t need a CD player. Some of my friends have offered to play music. They\'re in a band." -> bạn bè sẽ chơi nhạc cụ: <b>They will play musical instruments</b>. (Khoá Word ghi A là sai.)'),
], 1)
# ---------- Nghe (Part 2: school play)
put('g2', [
    (['Friday', 'on Friday', 'until Friday'], '"Tickets will be on sale in the gym during the break until <b>Friday</b>." -> ngày cuối mua vé: Friday.'),
    (['4', '£4', '4 pounds'], '"Adult tickets will cost £3 for parents and <b>£4</b> for guests." -> khách mời trả £4.'),
    (['costumes', 'costume'], '"We still need people to help make <b>costumes</b>." -> cần người giúp làm trang phục.'),
    (['Field', 'field'], '"Please speak to Mr <b>Field</b>, that\'s F-I-E-L-D" -> thầy Field.'),
    (['drinks', 'drink'], '"We need people to sell ice cream and <b>drinks</b> before the play starts." -> bán kem và đồ uống.'),
], 6)
# ---------- Phát âm / trọng âm
put('g3', [
    ('D', '<b>reduce</b> /rɪˈdjuːs/ (e = /ɪ/). dweller /ˈdwelə/, sensor /ˈsensə/, energy /ˈenədʒi/ có e = /e/.'),
    ('C', '<b>confidence</b> /ˈkɒnfɪdəns/ (o = /ɒ/). control /kənˈtrəʊl/, economic /ˌiːkəˈnɒmɪk/, condition /kənˈdɪʃn/ có o = /ə/.'),
], 11)
put('g4', [
    ('A', '<b>feature</b> /ˈfiːtʃə/ nhấn âm 1; sustain /səˈsteɪn/, predict /prɪˈdɪkt/, produce (v) /prəˈdjuːs/ nhấn âm 2.'),
    ('A', '<b>permission</b> /pəˈmɪʃn/ nhấn âm 2; difference /ˈdɪfrəns/, argument /ˈɑːɡjumənt/, cultural /ˈkʌltʃərəl/ nhấn âm 1.'),
], 13)
# ---------- Từ vựng / ngữ pháp
put('g5', [
    ('B', '"because it\'s a rule" -> nghĩa vụ do quy định bên ngoài: <b>have to</b>. (must chỉ nghĩa vụ do người nói/áp đặt cá nhân, ought to/should chỉ lời khuyên.) Tạm dịch: Mọi học sinh phải làm xong bài tập trước khi vào lớp vì đó là quy định.'),
    ('C', '<b>aggressive behaviour</b> (hành vi hung hăng). Tạm dịch: Cha mẹ không phải lúc nào cũng phản ứng hiệu quả với hành vi hung hăng của con cái.'),
    ('C', '"now" -> hiện tại tiếp diễn: <b>are tasting</b> (các giám khảo đang nếm món ăn).'),
    ('C', 'reduce traffic <b>congestion</b> (giảm ùn tắc giao thông). Noise/pollution không khớp với "move around easily".'),
    ('B', '<b>a range of</b> + danh từ số nhiều = một loạt, nhiều. "a great deal of" đi với danh từ không đếm được; "the number of/the amount of" không hợp nghĩa.'),
    ('C', 'a list of <b>ingredients</b> = danh sách thành phần (trên bao bì thực phẩm).'),
], 15)
# ---------- Đọc hiểu
put('g6', [
    (['A', 'B'], 'Đoạn 1 nói về xu hướng nam giới tham gia việc nhà nhiều hơn và lợi ích của điều đó với vợ/chồng và con cái -> <b>Men\'s involvement at home</b> bao quát cả đoạn; <b>Benefits of men\'s involvement at home</b> nêu đúng ý chính ở nửa sau (cả hai đều chấp nhận).'),
    ('B', '"Today, 41 per cent of couples say they share childcare equally" -> <b>41%</b>.'),
    ('C', '"Older people ... have more opportunity to develop a relationship with their grandchildren" + gia đình chăm sóc người già -> <b>have better relationships with their children and grandchildren</b> là ý gần nhất. Các phương án còn lại trái nội dung (tuổi thọ tăng, được chăm sóc nhiều).'),
    ('C', '"A lower proportion of children from divorced families are exhibiting problems than in earlier decades" -> câu C (trẻ em từ gia đình ly hôn gây nhiều vấn đề hơn) là <b>sai</b>.'),
    ('A', '<b>equivalent</b> (tương đương) ≈ <b>comparable</b>; opposed/dissimilar/contrasting là các từ trái nghĩa.'),
    ('D', '<b>manageable</b> (có thể xử lý được) ≈ <b>easy</b>; difficult/challenging/demanding trái nghĩa.'),
    ('B', '"when parents minimize conflict, family bonds can be maintained. And many families are doing <b>this</b>" -> "this" = <b>minimizing conflict</b>.'),
    ('A', 'Đoạn cuối cho thấy nhiều xu hướng tích cực (giữ liên lạc, hỗ trợ con cái, ít vấn đề hơn) -> tương lai gia đình Mỹ có thể <b>positive</b>.'),
], 21)
# ---------- Tự luận
put('g7', [
    (['strength', 'strengths'], 'Sau sở hữu cách "body\'s" cần danh từ: STRONG -> <b>strength</b> (sức mạnh, thể lực). Tạm dịch: Dành nhiều thời gian ngoài trời có thể tăng cường sức mạnh cơ thể.'),
    (['renewable'], 'NEW -> <b>renewable</b> energy sources (nguồn năng lượng tái tạo), song song với "sustainable".'),
    (['environmentally', 'environment-ally'], 'Cần trạng từ bổ nghĩa cho tính từ "friendly": ENVIRONMENT -> <b>environmentally</b> friendly (thân thiện với môi trường).'),
    (['overpopulation', 'over-population'], 'Định nghĩa "the fact of a country or city having too many people living in it" -> <b>overpopulation</b> (dân số quá đông).'),
], 29)
put('g8', [
    (['for'], 'be good <b>for</b> sb/sth = tốt cho. Tạm dịch: Tôi biết món nào ngon nhưng không biết món nào tốt cho cơ thể.'),
    (['to'], 'make no difference <b>to</b> sth = không ảnh hưởng gì đến. Tạm dịch: Ý kiến của cha mẹ không ảnh hưởng đến quyết định của cô ấy.'),
    (['on'], 'take <b>on</b> new staff = tuyển thêm nhân viên mới. Tạm dịch: Hiện chúng tôi đang tuyển nhân viên mới.'),
    (['to', 'on', 'for'], 'fair <b>to</b> sb (công bằng với ai) – cũng dùng "fair on sb" hoặc "fair for sb to do". Tạm dịch: Chị cả bị giao hết việc nhà như vậy có thực sự công bằng không?'),
], 33)
put('g9', [
    (['working for this electronics firm in 1999', 'to work for this electronics firm in 1999', 'working for this firm in 1999',
      'working at this electronics firm in 1999'],
     '<b>Mẫu:</b> John started working (hoặc to work) for this electronics firm in 1999. (has worked ... since 1999 = started working ... in 1999)'),
    (['is not allowed to use that computer', 'is not permitted to use that computer', 'is not allowed to use the computer',
      'does not have permission to use that computer', 'is not given permission to use that computer'],
     '<b>Mẫu:</b> John isn\'t allowed to use that computer. (doesn\'t get permission = isn\'t allowed/permitted)'),
    (['opinion about living in a smart city', 'opinion of living in a smart city', 'opinion on living in a smart city',
      'opinion about life in a smart city', 'view of living in a smart city', 'view on living in a smart city'],
     '<b>Mẫu:</b> What is your opinion about/on/of living in a smart city? (What do you think about ... = What is your opinion on ...)'),
], 37)
