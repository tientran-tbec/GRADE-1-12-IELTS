# -*- coding: utf-8 -*-
"""Đáp án + giải thích – Test 8 – Mid-term 1 (Đề ôn tập giữa HK1 Anh 11 Global 25-26 – Đề 9).
Đáp án lấy từ khoá tô màu trong Word (src/mt1/d9.txt) rồi tự giải độc lập để đối chiếu.
Phần nghe: đối chiếu script Word với Whisper (large-v3) trên file mp3 – trùng khớp."""

GHI_CHU_RA_SOAT = [
    'Audio: file mp3 gốc dài 557 s, gồm lời dẫn + Part 1 (nghe 2 lần) + Part 2 (nghe 2 lần) + lời kết "Thank you" (~527-557 s); đã cắt còn 500 s (bỏ phần cuối im lặng/lời cảm ơn). Nội dung khớp 100% script trong Word.',
    'g2.6: script đọc "75%" ~ three-fourths (C) – khoá Word C đúng.',
    'g3.10: khoá Word B (had to); "must" (A) cũng đúng với xã hội truyền thống (nghĩa vụ chung) -> chấp nhận cả A và B.',
    'g3.11: khoá Word A (used to); "had to work ... when he was young" (C) cũng đúng ngữ pháp và nghĩa -> chấp nhận A và C.',
    'g3.19: khoá Word A (traffic congestion); "heavy traffic jam" (C) kém tự nhiên, giữ A.',
    'g4.20: khoá Word D (numbers) – "the exact number of" mới tự nhiên, nhưng đề chỉ có "numbers"/"amount"; amount không đi với danh từ đếm được, giữ D.',
    'g5.29: khoá Word D (khám bệnh định kỳ). Nhưng C (uống hơn 2 lít nước) CŨNG không được nhắc trong bài -> chấp nhận cả C và D.',
    'g7.37: khoá Word "to consider" nhưng câu đã có sẵn "to" trước ô trống ("advised me to ____") -> đáp án đúng là "consider".',
    'Nguồn: sửa "Question 3.</b>Tom" thiếu dấu cách; bỏ dấu chấm thừa ở phương án "temperature increase."; chuẩn hoá "two- thirds" -> "two-thirds"; thêm dấu cách trong (20)  ___ of.',
    'g8: đề không ghi rõ ô trống – học sinh viết lại cả câu; chấp nhận nhiều cách viết hợp lý (xem ANS).',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ======================= NGHE – PART 1 (Grace & Tom) =======================
put('g1', [
    ('F', 'Grace nói: "You always get good marks in class." -> Tom thường được điểm tốt ở lớp, nên "Tom doesn\'t usually get good grades" là SAI. (Tom chỉ hoảng khi thi: "In exams, I panic.")'),
    ('T', 'Grace: "If you continue like this, you\'ll get ill." -> Grace cho rằng Tom sẽ bị ốm nếu không thư giãn (ill = sick). ĐÚNG.'),
    ('F', 'Tom nói: "I get really nervous about exams" và "It\'s true, I\'m not very confident." -> Tom không hề tự tin, thư giãn khi thi. SAI.'),
    ('F', 'Grace: "Of course I get nervous. But I try to be positive." -> Grace cũng có lo lắng về kỳ thi. SAI.'),
], 1)

# ======================= NGHE – PART 2 (Climate change) =======================
put('g2', [
    ('D', 'Script: "A slight <b>temperature increase</b> in some colder parts of the world may improve conditions for agriculture." (Hiệu ứng nhà kính làm tăng nhẹ nhiệt độ ở vùng lạnh có thể có lợi cho nông nghiệp.)'),
    ('C', 'Script: "the developed, industrialized world is responsible for <b>75%</b> of all CO2 emissions" -> 75% = three-fourths (ba phần tư).'),
    ('C', 'Script: "as sea levels rise countries like <b>Bangladesh</b> will suffer much more ... than European or North American countries" -> các nước nghèo như Bangladesh chịu ảnh hưởng nặng nhất.'),
    ('B', 'Script: "<b>The effect of drowning coastlines</b> could lead to hundreds of millions of climate refugees." (Bờ biển bị nhấn chìm có thể tạo ra hàng trăm triệu người tị nạn khí hậu.)'),
], 5)

# ======================= LEXICO-GRAMMAR 9-19 =======================
put('g3', [
    ('A', 'life expectancy = tuổi thọ (danh từ ghép: life + expectancy). expectation = sự mong đợi, nghĩa khác. Tạm dịch: Chính phủ ban hành chính sách nâng cao tuổi thọ của người dân bằng cách cải thiện y tế và giáo dục.'),
    (['B', 'A'], 'Chủ ngữ chung "young people" trong xã hội truyền thống: nghĩa vụ -> <b>had to</b> (phải, trong quá khứ/truyền thống). Khoá Word là B; "must" (A) cũng chấp nhận được. "were to" (C) không hợp; "should" (D) chỉ là lời khuyên.'),
    (['A', 'C'], '"when he was young" + thói quen trong quá khứ -> <b>used to work</b> (đã từng làm). "had to work" (C) cũng đúng ngữ pháp (đã phải làm). "has to", "is used to" (+V-ing) không hợp.'),
    ('A', '<b>adapt to</b> = thích nghi với. adopt = áp dụng/nhận nuôi (không đi với "to"); accept to / attach to không hợp nghĩa. Tạm dịch: ... con người phải nhanh chóng thích nghi với thay đổi công nghệ.'),
    ('A', '<b>housing issues</b> = các vấn đề về nhà ở (housing là danh từ làm định ngữ). households = hộ gia đình; home, inhabitant không tạo cụm hợp nghĩa.'),
    ('D', 'look + tính từ: looks so <b>beautiful</b> (trông rất đẹp). beautifully là trạng từ, beautify là động từ, beauty là danh từ.'),
    ('A', 'Cần nghĩa vụ/sự cần thiết: Citizens <b>need to</b> separate ... (công dân cần phân loại rác). might/can/may not không diễn đạt đúng nghĩa bắt buộc ở đây.'),
    ('C', 'Reading the product\'s <b>label</b> = đọc nhãn sản phẩm để tránh hàng có hoá chất độc hại. composition/ingredient/description không đi với "đọc" tự nhiên bằng "label" (reading the label = đọc nhãn).'),
    ('A', 'be more <b>sustainable</b> = bền vững hơn, kết hợp đổi mới với bảo vệ môi trường. industrial/economic/temporary không hợp nghĩa.'),
    ('B', '"I firmly <b>believe</b> that ..." – believe là động từ trạng thái, không dùng tiếp diễn (am believing) và dùng thì hiện tại đơn khi nêu quan điểm chung.'),
    ('A', '"Heavy <b>traffic congestion</b> ... causes serious delays" = tắc nghẽn giao thông nghiêm trọng. traffic lights (đèn giao thông) và street noise không gây trễ giờ; "heavy traffic jam" ít tự nhiên.'),
], 9)

# ======================= CLOZE 20-24 (Blue Dragon) =======================
put('g4', [
    ('D', 'the exact <b>numbers</b> of homeless children = con số chính xác của trẻ em vô gia cư. (plenty/amount/level không phù hợp với "of homeless children" đếm được.) Tạm dịch: Không ai biết chính xác số lượng trẻ em vô gia cư.'),
    ('D', 'Sau chỗ trống là cụm danh từ "family problems" -> dùng <b>because of</b> + N (vì các vấn đề gia đình). although + mệnh đề; despite = mặc dù (sai nghĩa); as a result không đi với danh từ như vậy.'),
    ('B', '<b>make ends meet</b> = xoay xở đủ sống (thành ngữ). Tạm dịch: Chúng vật lộn để kiếm sống bằng cách đánh giày, bán vặt.'),
    ('D', 'has worked <b>nonstop</b> = làm việc không ngừng nghỉ (nonstop có thể là trạng từ). continuous/endless/limitless là tính từ, không đứng sau động từ "worked" như vậy.'),
    ('A', 'receive a proper <b>education</b> = được giáo dục đúng đắn (sau tính từ proper cần danh từ). educated (tính từ), educational (tính từ), educating (V-ing) không phù hợp.'),
], 20)

# ======================= READING 25-29 =======================
put('g5', [
    ('A', 'Bài nói về lối sống lành mạnh: chế độ ăn, tập thể dục, giấc ngủ -> "How to Have a Healthy Lifestyle". B và D chỉ là một ý nhỏ; C không được bàn tới.'),
    ('B', 'Đoạn 4: "Keeping a consistent sleep schedule, <b>avoiding caffeine</b>, and limiting electronic use before bed can help achieve better sleep." -> tránh caffeine trước khi ngủ.'),
    ('D', '"It is essential to prioritise <b>healthy habits</b> and make them a part of our daily routine." -> "them" thay cho healthy habits (những thói quen lành mạnh).'),
    ('A', 'consistent = đều đặn, nhất quán; trái nghĩa là <b>changeable</b> (hay thay đổi). regular là đồng nghĩa; positive, beneficial không phải trái nghĩa.'),
    (['D', 'C'], 'Bài có nhắc: 30 phút vận động mỗi ngày (A), ngủ đủ giúp cải thiện trí nhớ (B). KHÔNG nhắc: uống hơn 2 lít nước (C) và khám bác sĩ định kỳ (D). Khoá Word chỉ nêu D; thực tế C cũng không có trong bài nên chấp nhận cả C và D.'),
], 25)

# ======================= SẮP XẾP 30-32 =======================
put('g6', [
    ('B', 'c – a – b: Nam hỏi "How do you stay healthy every day?" (c) -> Lan trả lời "I usually go jogging every morning" (a) -> Nam đáp "That\'s great! I also try to eat more vegetables..." (b).'),
    ('C', 'b – a – e – c – d: Lời chào "Hi Anna!" (b) -> "I\'ve just joined a new health club" (a) -> "They have great fitness classes..." (e, giải thích về câu lạc bộ) -> "I think it would be fun ... if you joined with me" (c) -> "Let\'s go together this weekend!" (d, lời mời kết thúc).'),
    ('A', 'c – a – e – b – d: câu mở đoạn (c) -> First (a) -> Moreover (e) -> Finally (b) -> In conclusion (d). Trình tự các từ nối First – Moreover – Finally – In conclusion.'),
], 30)

# ======================= WORD FORM 33-37 =======================
put('g7', [
    (['skillful', 'skilful', 'skilled'], 'be more <b>skillful</b> in using technology: sau "more" cần tính từ. (SKILL -> skillful/skilful/skilled). Tạm dịch: Học sinh ở thành phố thông minh được kỳ vọng thành thạo hơn trong việc dùng công nghệ để học.'),
    (['effective'], 'The <b>effective</b> communication = giao tiếp hiệu quả: trước danh từ communication cần tính từ (EFFECT -> effective).'),
    (['has proposed', 'has been proposing'], '"Since the project started" -> hiện tại hoàn thành: our group <b>has proposed</b> many ideas (nhóm đã đề xuất nhiều ý tưởng).'),
    (['arguments'], 'heated <b>arguments</b> = những cuộc tranh cãi gay gắt: sau tính từ heated và có "often ... between" cần danh từ số nhiều (ARGUE -> arguments).'),
    (['consider'], 'advise somebody <b>to consider</b>: trong câu đã có sẵn "to" trước ô trống nên chỉ điền <b>consider</b> (Khoá Word ghi "to consider" – tính cả "to" của câu). Tạm dịch: Giáo viên khuyên tôi cân nhắc mục tiêu trước khi đưa ra quyết định quan trọng.'),
], 33)

# ======================= VIẾT LẠI CÂU 38-41 =======================
put('g8', [
    (['Young people should communicate with their parents to bridge the generation gap.',
      'Young people ought to communicate with their parents to bridge the generation gap.',
      'Young people must communicate with their parents to bridge the generation gap.',
      'Young people need to communicate with their parents to bridge the generation gap.'],
     'It is important for ... to V -> dùng động từ khuyết thiếu <b>should/ought to/must/need to</b>. Đáp án mẫu: Young people should communicate with their parents to bridge the generation gap.'),
    (['It is two weeks since I last visited my grandparents.', 'It has been two weeks since I last visited my grandparents.',
      'It\'s two weeks since I last visited my grandparents.', 'It\'s been two weeks since I last visited my grandparents.'],
     'S + haven\'t + V3 + for + time = It is/has been + time + since + S + last + V2. Đáp án mẫu: It has been two weeks since I last visited my grandparents.'),
    (['We have been learning about smart cities since last month.', 'We have learned about smart cities since last month.',
      'We have learnt about smart cities since last month.'],
     'Hành động bắt đầu từ quá khứ (last month) và còn tiếp diễn -> hiện tại hoàn thành (tiếp diễn): <b>have been learning / have learned</b> ... since last month.'),
    (['We must not use our mobile phones during the movie screening.', 'We cannot use our mobile phones during the movie screening.',
      'We may not use our mobile phones during the movie screening.', 'We should not use our mobile phones during the movie screening.'],
     'be not allowed to V = <b>must not / cannot / may not</b> V (cấm). Đáp án mẫu: We must not use our mobile phones during the movie screening.'),
], 38)
