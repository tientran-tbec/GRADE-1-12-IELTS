# -*- coding: utf-8 -*-
"""Đáp án + giải thích – Test 6 – Mid-term 1 (Tiếng Anh 11 Global Success) – nguồn: Đề ôn tập giữa HK1 Anh 11 Global 25-26 (Đề 7).
Quy ước: mcq = chữ cái 'A'-'D' (hoặc list nếu nhiều đáp án đều đúng); tf = 'T'/'F'; fill = list đáp án chấp nhận.
Đáp án lấy từ khoá (tô màu ⟦…⟧) trong phần ĐÁP ÁN của Word, đã tự giải độc lập để đối chiếu.
Phần nghe: script Word đối chiếu bằng Whisper (large-v3) trên audio/mt1_test06.mp3 — khớp."""

GHI_CHU_RA_SOAT = [
    'g3.13 (Q13): khoá Word không tô đáp án; đáp án đúng D (footsteps) — thành ngữ follow in someone\'s footsteps.',
    'g4.22 (Q22): khoá Word = D (each) nhưng "Every building" (C) cũng đúng ngữ pháp và nghĩa -> ANS = [C, D].',
    'g3.9 (Q9): khoá Word = A (strength); endurance (C) cũng có thể chấp nhận về nghĩa nhưng strength tự nhiên nhất -> giữ A.',
    'g3.10 (Q10): khoá Word = A (treatment); giữ nguyên (advances in the treatment of cancer là cụm quen thuộc; research/diagnosis ít tự nhiên hơn).',
    'g7.34 (Q34): khoá Word "impression" (make an impression on); g7.37 giữ "must wear" theo gợi ý (must / wear).',
    'g8.39 (Q39): đề gốc bị cụt "was in" (thiếu năm), năm 2019 lấy từ phần đáp án -> đã bổ sung "in 2019" vào đề.',
    'g8.38 (Q38): đề gốc thiếu từ gợi ý "(first)" và "This is the" ở phần đề (chỉ có trong đáp án) -> đã bổ sung.',
    'g8.40, g8.41: đề gốc ghi "(using a modal verb)" -> giữ; thêm các cách viết hợp lý (can\'t / had better).',
    'Nguồn lỗi nhỏ đã sửa: "Question 22/24" mục D dính chữ ("D.each"); Q2 dính phương án True/False cùng dòng; Q31 khoá Word tô lệch ký tự nhưng đáp án A; Q37 thiếu dấu chấm cuối câu; Q8 "______of" dính chữ.',
    'Phần nghe: audio gốc chỉ phát MỘT lần (không lặp lại) dù đề ghi "listen TWICE"; Word ghi điểm phần nghe là 1.0 pt ở đáp án nhưng 2.0 pt ở đề.',
    'Đề không ghi thời gian: đặt 60 phút (41 câu).',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


put('g1', [
    ('T', 'Script: "your diet may also significantly affect your mood and sense of wellness" -> chế độ ăn có thể ảnh hưởng đáng kể đến tâm trạng và cảm giác khoẻ mạnh: <b>True</b>.'),
    ('T', 'Script: "A normal Western diet, which includes processed meats, packaged meals, takeout food, and sugary snacks" -> các món đó là phổ biến trong bữa ăn phương Tây: <b>True</b>.'),
    ('F', 'Script: "lowering your sugar intake ... may help to improve mood" -> phải <b>giảm</b> đường, không phải tăng đường: <b>False</b>.'),
    ('F', 'Script: "You don\'t have to completely eliminate foods you enjoy to have a healthy diet" -> KHÔNG cần loại bỏ hoàn toàn món yêu thích: <b>False</b>.'),
], 1)
for i, (a, e) in enumerate([
    (['future'], 'Script: "His team\'s projects have created many designs that give forms to the <b>future</b>." -> các công trình định hình tương lai.'),
    (['wood'], 'Script: "a social housing project in Copenhagen, where they use blocks of <b>wood</b>" -> nhà xây bằng các khối gỗ (lấy cảm hứng từ LEGO).'),
    (['toxins', 'toxin'], 'Script: "the cleanest waste-to-energy power plant in the world, there are no <b>toxins</b> coming out of the chimney" -> không thải ra chất độc.'),
    (['roof'], 'Script: "He even put a ski slope on its sloping <b>roof</b> so people can ski on the roof of the power plant" -> trượt tuyết trên mái dốc của nhà máy.'),
], 5):
    ANS['g2.%d' % i] = a
    EXPLANATIONS['g2.%d' % i] = e

put('g3', [
    ('A', 'physical <b>strength</b> (sức mạnh thể chất) – "required considerable physical strength": nhiệm vụ đòi hỏi nhiều sức lực. (endurance = sức bền cũng có thể chấp nhận, nhưng strength tự nhiên nhất.)'),
    ('A', 'advances in the <b>treatment</b> of cancer = những tiến bộ trong điều trị ung thư.'),
    ('A', '<b>give up</b> football = từ bỏ/bỏ môn bóng đá. take over = tiếp quản; sign up for = đăng ký tham gia; drop in = ghé qua.'),
    ('C', 'Trước danh từ "food" cần tính từ: <b>nutritious</b> food = thực phẩm bổ dưỡng.'),
    ('D', 'follow in one\'s <b>footsteps</b> = nối nghiệp, noi gương (cha). Các phương án còn lại không phải thành ngữ.'),
    ('A', 'consider all the different <b>views</b> about the issue = xem xét mọi quan điểm khác nhau về vấn đề.'),
    ('A', 'be stuck in a <b>traffic jam</b> = bị kẹt xe.'),
    ('C', 'impress somebody <b>with</b> something = gây ấn tượng với ai bởi điều gì.'),
    ('C', 'want là động từ trạng thái (không chia tiếp diễn); chủ ngữ Jane số ít, hiện tại đơn: Jane <b>wants</b> to be a nurse when she grows up.'),
    ('D', 'Lời khuyên: You <b>should</b> eat more vegetables if you want to stay healthy. (mustn\'t = cấm; don\'t have to = không cần; shouldn\'t = không nên: sai nghĩa).'),
    ('C', 'make room <b>for</b> something = nhường chỗ cho (công trình hiện đại).'),
], 9)

put('g4', [
    ('C', 'encourage + danh từ: encourage <b>innovation</b> (khuyến khích sự đổi mới).'),
    ('B', 'take responsibility for = chịu trách nhiệm về. (<b>take</b>)'),
    (['C', 'D'], '<b>Every</b>/<b>Each</b> + danh từ số ít: "Each building" / "Every building in the city is powered by clean energy" (cả hai đều đúng; Word chọn each). another và all không hợp.'),
    ('C', 'be equipped <b>with</b> something = được trang bị cái gì.'),
    ('B', 'Trật tự danh từ ghép: <b>urban project development</b> (sự phát triển dự án đô thị) – "project development" là cụm danh từ, "urban" bổ nghĩa đứng trước.'),
], 20)

put('g5', [
    ('B', '"very few teens feel their parents really listen to <b>them</b>" -> them thay cho <b>the teens</b>.'),
    ('D', 'Đoạn văn nêu: thiếu tin tưởng/tôn trọng (A), không lắng nghe (B), bố mẹ bất đồng về kỷ luật (C); KHÔNG nhắc đến việc bố mẹ không giúp con làm bài tập (D).'),
    ('B', '<b>authoritarian</b> (độc đoán, nghiêm khắc) ≈ <b>strict</b> (nghiêm khắc) – "very authoritarian homes where kids have very little freedom".'),
    ('C', 'Cả bài nói về những điều cha mẹ nên/không nên làm (tin tưởng, lắng nghe, cho tự do, làm gương) để giành được sự tôn trọng của con -> <b>C</b>.'),
    ('C', '"Teens don\'t have much respect for their parents if neither of them actually does things that they expect their children to do" -> cha mẹ không làm gương tốt: <b>C</b>.'),
], 25)

put('g6', [
    ('B', 'c (chào, hỏi có cần giúp điện thoại không) – d (ông trả lời đang tải ảnh nhưng không biết) – a (cháu nhận giúp) – b (ông cảm ơn): <b>c – d – a – b</b>.'),
    ('A', 'e (nêu vấn đề) – d (First...) – a (Besides...) – b (As a result...) – c (In conclusion...): <b>e – d – a – b – c</b>. "As a result" nói về kết quả của việc nói chuyện và lắng nghe nên phải đứng sau cả d và a.'),
    ('A', 'b (câu chủ đề: thành phố tương lai) – a (These cities... công nghệ) – c (thiết bị thông minh) – d (However...) – e (In conclusion): <b>b – a – c – d – e</b>.'),
], 30)

put('g7', [
    (['energetic'], 'remains + tính từ, song song với "enthusiastic": <b>energetic</b> (tràn đầy năng lượng) – từ ENERGY.'),
    (['impression'], 'make a strong <b>impression</b> on somebody = gây ấn tượng mạnh với ai – danh từ của IMPRESS.'),
    (['looks'], 'always + hiện tại đơn, chủ ngữ she: She always <b>looks</b> happy (look + tính từ = trông có vẻ).'),
    (['has gained', 'has been gaining'], 'since + mệnh đề quá khứ đơn -> hiện tại hoàn thành: She <b>has gained</b> a lot of experience.'),
    (['must wear'], 'Quy định/bắt buộc: Students <b>must wear</b> their uniforms when they come to school.'),
], 33)

W = {}
W[38] = (['first time she has visited Ha Long Bay', 'first time she has been to Ha Long Bay', 'first time she has ever visited Ha Long Bay', 'first time she has ever been to Ha Long Bay'],
         'Cấu trúc: This is the first time + S + have/has + V3. <b>Mẫu:</b> This is the <b>first time she has visited Ha Long Bay</b>. (Cô ấy chưa từng đến Hạ Long trước đây.)')
W[39] = (['not seen her grandparents since 2019', 'not seen them since 2019', 'not seen her grandparents since the year 2019'],
         'The last time + quá khứ đơn -> S + have/has + not + V3 + since. <b>Mẫu:</b> She has <b>not seen her grandparents since 2019</b>.')
W[40] = (['mustn\'t leave the campus during class time', 'must not leave the campus during class time', 'can\'t leave the campus during class time', 'cannot leave the campus during class time'],
         'It\'s against the rules to V = bị cấm -> modal cấm <b>mustn\'t</b> (hoặc can\'t). <b>Mẫu:</b> Students <b>mustn\'t leave the campus during class time</b>.')
W[41] = (['should talk to your parents when you have problems at school', 'had better talk to your parents when you have problems at school', 'ought to talk to your parents when you have problems at school'],
         'It would be better for you to V = lời khuyên -> <b>should</b> + V. <b>Mẫu:</b> You <b>should talk to your parents when you have problems at school</b>.')
for n, (a, e) in W.items():
    ANS['g8.%d' % n] = a
    EXPLANATIONS['g8.%d' % n] = e
