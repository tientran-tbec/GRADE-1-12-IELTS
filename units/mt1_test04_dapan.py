# -*- coding: utf-8 -*-
"""Đáp án + giải thích – Test 4 – Mid-term 1 (Tiếng Anh 11 Global Success) – nguồn: Đề kiểm tra giữa HK1 Anh 11 (Đề 5).
Quy ước: mcq = chữ cái 'A'-'D' (hoặc list nếu nhiều đáp án đều đúng).
Đáp án lấy từ khoá (tô màu ⟦…⟧) trong phần ĐÁP ÁN của Word, đã tự giải độc lập để đối chiếu. Đề không có phần nghe."""

GHI_CHU_RA_SOAT = [
    'g7.28 (Q28): khoá Word = A (that) nhưng "an activity which brings you delight" (B) cũng đúng ngữ pháp -> ANS = [A, B].',
    'g9.36 (Q36): khoá Word = A (homelessness); câu hỏi kém chặt chẽ ("people" chỉ những người vô gia cư; phương án gần nhất là homelessness). Giữ khoá Word.',
    'g6.20 (Q20): lời giải Word gọi "that" là mệnh đề quan hệ; thực chất là liên từ mở mệnh đề danh ngữ sau "thought" (đáp án A vẫn đúng).',
    'g5.17 (Q17): phương án A của nguồn có 2 chữ d ("... f – d – b"), phương án sai rõ ràng; giữ nguyên như đề.',
    'Sửa nguồn: Q7 mất chỗ trống (gạch chân rỗng) -> thêm ______; Q29 "C ." -> "C."; "closet" -> "closest" (Q31, 38, 39 gốc); Q18-23 bỏ lặp "high blood pressure" trong đoạn văn (khoá Word đã bỏ).',
    'Q10-12 và Q13-15 là hai văn bản ảnh (image1.png, image2.png); đề gốc để chung một đề bài "10 to 15" -> tách 2 nhóm g4 và g4b; image3.png trong Word là bản lặp của image2 (phần đáp án) nên không dùng.',
    'Đề không ghi thời gian: đặt 45 phút (40 câu).',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ---------- Phát âm / trọng âm
put('g1', [
    ('A', '<b>diet</b> /ˈdaɪət/ (i = /aɪ/). mineral /ˈmɪnərəl/, fitness /ˈfɪtnəs/, vitamin /ˈvɪtəmɪn/ đều có i = /ɪ/.'),
    ('B', '<b>obesity</b> /əʊˈbiːsəti/ (e = /iː/). exercise /ˈeksəsaɪz/, remedy /ˈremədi/, medicine /ˈmedsn/ đều có e = /e/.'),
], 1)
put('g2', [
    ('D', '<b>fascinate</b> /ˈfæsɪneɪt/ nhấn âm 1; accept /əkˈsept/, believe /bɪˈliːv/, support /səˈpɔːt/ nhấn âm 2.'),
    ('C', '<b>properly</b> /ˈprɒpəli/ nhấn âm 1; essential /ɪˈsenʃl/, precaution /prɪˈkɔːʃn/, infectious /ɪnˈfekʃəs/ nhấn âm 2.'),
], 3)
# ---------- Ngôn ngữ
put('g3', [
    ('B', 'Câu điều kiện loại 1: If + hiện tại hoàn thành (haven\'t missed), mệnh đề chính dùng mệnh lệnh. Tạm dịch: Nếu bạn chưa bỏ lỡ điều quan trọng nào, hãy chú ý trong lớp và chỉ hỏi khi cần thiết.'),
    ('C', 'So sánh nhất của tính từ ngắn: the + adj-est -> <b>the luckiest</b> girl in the world (người may mắn nhất thế giới).'),
    ('D', '<b>do away with</b> = bãi bỏ, loại bỏ (abolish). put down to: quy cho; catch up on: bù lại; get down to: bắt tay vào làm. Tạm dịch: Cô ấy tin rằng mọi quốc gia nên bãi bỏ án tử hình vì nó vô nhân đạo.'),
    ('B', '<b>relieve stress</b> = làm dịu, giảm căng thẳng (collocation). relax: thư giãn (không đi với stress), remove: loại bỏ, require: yêu cầu.'),
    ('A', 'Biển báo cấm: <b>mustn\'t</b> = cấm, không được phép. shouldn\'t/ought not to: không nên; don\'t have to: không bắt buộc. Tạm dịch: Biển báo cho biết bạn không được bước lên cỏ.'),
], 5)
put('g4', [
    ('C', '"policy updates we\'ve <b>implemented</b>" = các cập nhật chính sách chúng tôi đã thực hiện. activated: kích hoạt; occurred: xảy ra (nội động từ); illustrated: minh hoạ.'),
    ('A', 'Bị động hiện tại đơn: "Parents <b>are asked</b> to please drop off and pick up students" (Phụ huynh được yêu cầu đưa đón học sinh).'),
    ('B', 'Đảo ngữ câu điều kiện loại 1: <b>Should</b> you have any questions, please contact us. (= If you should have...). Tạm dịch: Nếu bạn có thắc mắc nào, vui lòng liên hệ chúng tôi.'),
], 10)
put('g4b', [
    ('D', '"experience" (kinh nghiệm) ở nghĩa chung là danh từ không đếm được, không cần mạo từ: Gain <b>Ø</b> experience in hotel operations.'),
    ('A', '<b>suit your needs</b> = phù hợp với nhu cầu của bạn. Tạm dịch: Lịch học linh hoạt phù hợp với nhu cầu của bạn.'),
    ('D', 'Sau giới từ "toward" cần danh từ: your journey toward <b>success</b> (hành trình hướng tới thành công).'),
], 13)
# ---------- Sắp xếp
put('g5', [
    ('B', 'Thư: e (Dear John...) -> c (mở đầu: rất vui báo tin) -> g (Firstly) -> a (In addition) -> d (Finally) -> f (Ultimately: kết luận) -> b (Warm regards). Đáp án <b>e – c – g – a – d – f – b</b>.'),
    ('C', 'Đoạn văn: c (câu chủ đề) -> g (Firstly) -> e (ví dụ giao việc) -> a (Moreover) -> d (Additionally) -> b (Finally) -> f (Overall: kết luận). Đáp án <b>c – g – e – a – d – b – f</b>. (Phương án A lặp chữ d nên sai.)'),
], 16)
# ---------- Cloze tai chi
put('g6', [
    ('C', '"tai chi" là chủ ngữ số ít, cần động từ hiện tại đơn: tai chi <b>has several benefits</b> (có nhiều lợi ích). "has been several benefits" sai cấu trúc.'),
    ('B', 'Song song với "improving balance and ...": <b>reducing the risk of falls</b> (cùng dạng V-ing sau giới từ "on").'),
    ('A', '"have long thought <b>that</b> tai chi helps with balance" - that mở mệnh đề danh ngữ sau động từ think. which/when/whom không phù hợp.'),
    ('D', 'Tính từ sở hữu của "participants" (they) là <b>their</b>: their increased self-assurance (sự tự tin tăng lên của họ).'),
    ('B', 'Câu bị động quá khứ đơn, chủ ngữ số nhiều "gains": Statistically substantial gains <b>were noted</b> in flexibility... (những tiến bộ đáng kể đã được ghi nhận).'),
    ('B', 'Nghĩa nhượng bộ: <b>Although</b> there is no hard evidence that tai chi reduces stress, ... could be the perfect antidote. Because/For/But không hợp nghĩa hoặc cấu trúc.'),
], 18)
# ---------- Cloze thể dục
put('g7', [
    ('D', '"don\'t do <b>much</b>" - much + danh từ không đếm được / dùng như đại từ trong câu phủ định (không làm được nhiều). many/every/each cần danh từ đếm được.'),
    ('C', '<b>prevent sb from doing sth</b> = ngăn ai làm gì: Our hectic schedules have prevented us from exercising.'),
    ('C', '<b>Maintaining</b> a regular exercise routine = duy trì thói quen tập luyện đều đặn, là điều cần thiết. Ignoring/Abolishing/Removing mang nghĩa bỏ đi nên sai nghĩa.'),
    ('B', '<b>Furthermore</b> (hơn nữa) bổ sung ý ở câu trước. Although/Because tạo mệnh đề phụ (cần hai vế); However chỉ sự tương phản - không hợp.'),
    (['A', 'B'], 'Mệnh đề quan hệ chỉ vật làm chủ ngữ: an activity <b>that/which</b> brings you delight. Khoá Word chọn A (that); B (which) cũng đúng nên chấp nhận cả hai. what/why không dùng được.'),
], 24)
# ---------- Bài đọc McDonald's
put('g8', [
    ('C', 'Bài nói về vụ kiện của thanh thiếu niên béo phì kiện McDonald\'s và việc tòa bác bỏ vì "không phải việc của luật pháp bảo vệ con người khỏi sự quá độ của chính họ" -> tiêu đề <b>Obesity - who is to blame?</b> (Béo phì - ai đáng trách?).'),
    ('A', 'Đoạn 1 nêu nguy cơ "diabetes, hypertension, and obesity". <b>Heart disease</b> (bệnh tim) không được nhắc tới.'),
    ('D', '<b>excessive</b> (quá mức) ~ <b>extreme</b> (cực độ). Excite: kích thích; express: bày tỏ; exact: chính xác.'),
    ('C', '"they have no right to hold the food industry responsible if <b>they</b> opt to consume..." - "they" chỉ <b>obese teenagers</b> (những thanh thiếu niên béo phì kiện McDonald\'s).'),
    ('B', 'Bài nói fast food gây nghiện (addictive), nguy hiểm (harmful), nhiều chất béo và muối. <b>Nutritious</b> (bổ dưỡng) không được đề cập / trái nội dung -> NOT true.'),
    ('A', 'Tòa bác vụ kiện: họ "have no right to hold the food industry responsible" -> <b>They can\'t force the company to be responsible for them</b> (Họ không thể buộc công ty chịu trách nhiệm).'),
], 29)
# ---------- Bài đọc vô gia cư
put('g9', [
    ('C', 'Bài nói về hoàn cảnh khốn khó của thanh thiếu niên vô gia cư ở Anh -> <b>The unpleasant condition of young, homeless people</b>.'),
    ('A', '"Some shelters are run by nonprofits and hostels where <b>people</b> can stay for up to ten weeks for free" - "people" chỉ những người vô gia cư (homelessness - phương án gần nhất). Đây là câu hỏi hơi gượng; giữ khoá của đề.'),
    ('D', '"having no permanent address makes it impossible to acquire a job" -> <b>they will find it difficult to find work</b>.'),
    ('B', '<b>affordable</b> (giá phải chăng) ~ <b>inexpensive</b> (rẻ, không đắt). inequality: bất bình đẳng; incapable/inability: không có khả năng.'),
    ('D', '<b>permanent</b> (cố định, lâu dài) >< <b>temporary</b> (tạm thời).'),
    ('A', '"individuals between sixteen and twenty-five receive less money than older individuals due to recent changes" -> <b>young people do not receive as much money as those over twenty-five</b>.'),
], 35)
