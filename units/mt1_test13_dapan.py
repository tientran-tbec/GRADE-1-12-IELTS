# -*- coding: utf-8 -*-
"""Đáp án + giải thích – Test 13 – Mid-term 1 (Tiếng Anh 11 Global Success) – nguồn: Đề ôn tập giữa HK1 Anh 11 Global – Đề 4.
Quy ước: mcq = chữ cái 'A'-'D' (hoặc list nếu nhiều đáp án đều đúng); fill = danh sách cách viết chấp nhận
(fill nhiều ô: {'blanks': [[ô 1], [ô 2], ...]}).
Word KHÔNG có khoá: toàn bộ đáp án tự giải; phần nghe dựa trên script nhận dạng bằng Whisper (large-v3) từ 2 file mp3."""

GHI_CHU_RA_SOAT = [
    'Word không có đáp án -> tự giải toàn bộ; phần nghe đối chiếu Whisper.',
    'g2.6-10: Part 2 là bài "pessimistic / optimistic viewpoints" (cùng nội dung bài nghe Đề 3): (6) healthy, (7) effective, (8) overcrowded, (9) medicine, (10) fossil fuels.',
    'g5.17: "must" (B) là đáp án phù hợp nhất ("agreed rules ... members must follow"); "had to" sai thì, "don\'t have to / mustn\'t" sai nghĩa.',
    'g5.18: "think of" (cân nhắc, định) dùng tiếp diễn -> is thinking (B); "thinks" (A) chỉ đúng nếu "think" = tin rằng, không đi với "of going on a diet" -> giữ B.',
    'g7.27-29: nguồn là các chỗ trống chấm chấm quanh động từ trong ngoặc ("1....scientists (discover)....a new cancer drug yet ?"), được hiểu là: Have + scientists + discovered; I have bought; John has built ... he started. Mỗi ô nhập trợ động từ/dạng động từ tương ứng.',
    'g8.32: nguồn đánh số "3." hai lần (TRADITION và TREAT) và phần viết lại đánh "8." -> đã đánh số lại liên tục 1-37.',
    'Sửa nguồn: "toget" -> "to get", "doesnot" -> "does not", "technologyand" -> "technology and", "Al technologies" -> "AI technologies", "sinces" -> "since", chữ bị tách rời ("c ook", "n ow", "m uscles"), "heaviertraffic"/"andheavier" tách từ, "Miss/Ms Stevens" giữ như nguồn.',
    'Đề d4.txt chỉ 115 dòng nhưng ĐỦ 37 câu (không chỉ có phần nghe). Không ghi giờ: 45 phút. Không có ảnh.',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ---------- Nghe Part 1: interview with Ms Stevens
put('g1', [
    ('B', '"In today\'s program, we\'ll be talking about the <b>disadvantages</b> of living in a smart city." -> phỏng vấn chủ yếu về <b>problems of living in a smart city</b>.'),
    ('A', '"cameras and sensors are everywhere, and they <b>collect information about me and my activities</b>." -> thu thập thông tin về người dân và hoạt động của họ.'),
    ('C', '"The government and some companies have so much <b>personal information about city dwellers</b>" = so much private information about city residents.'),
    ('B', '"It took me a long time to get familiar with all the smart devices at home. I don\'t really have any friends to ask for help in the neighbourhood." -> <b>She doesn\'t have any neighborhood friends for help</b>.'),
    ('A', '"I <b>interact with very few people face-to-face</b> because most of the activities can be done online." ... "we\'re becoming lonelier than any previous generation." -> cô cảm thấy cô đơn vì ít giao tiếp trực tiếp.'),
], 1)
# ---------- Nghe Part 2: viewpoints
put('g2', [
    (['healthy'], '"so they will no longer be safe and <b>healthy</b> places to live in" (không còn là nơi an toàn và lành mạnh).'),
    (['effective'], '"governments have no <b>effective</b> ways to control them" (chính phủ không có cách hiệu quả để kiểm soát).'),
    (['overcrowded', 'over-crowded'], '"As a result, cities will become <b>overcrowded</b>. This means there will be more people, more waste, and heavier traffic."'),
    (['medicine'], '"a better life thanks to important achievements in technology and <b>medicine</b>" (nhờ những thành tựu về công nghệ và y học).'),
    (['fossil fuels', 'fossil fuel'], '"They hope that these energy sources will step-by-step replace <b>fossil fuels</b>, such as gas, coal, and oil, in the next 20 years."'),
], 6)
# ---------- Phát âm / trọng âm
put('g3', [
    ('A', 'pr<b>i</b>vate /ˈpraɪvət/ (i = /aɪ/). public /ˈpʌblɪk/, city /ˈsɪti/, interact /ˈɪntərækt/ có i = /ɪ/.'),
    ('C', 'de<b>s</b>igner /dɪˈzaɪnə/ (s = /z/). solar /ˈsəʊlə/, infrastructure /ˈɪnfrəstrʌktʃə/, focus /ˈfəʊkəs/ có s = /s/.'),
], 11)
put('g4', [
    ('D', '<b>harmony</b> /ˈhɑːməni/ nhấn âm 1; apartment /əˈpɑːtmənt/, emission /ɪˈmɪʃn/, location /ləʊˈkeɪʃn/ nhấn âm 2.'),
    ('D', '<b>solution</b> /səˈluːʃn/ nhấn âm 2; article /ˈɑːtɪkl/, privacy /ˈprɪvəsi/, quality /ˈkwɒləti/ nhấn âm 1.'),
], 13)
# ---------- Từ vựng / ngữ pháp
put('g5', [
    ('B', '<b>examined</b> by the doctor = được bác sĩ khám. (fixed/repaired dùng cho đồ vật; investigated dùng cho vụ việc.)'),
    ('C', 'life <b>expectancy</b> = tuổi thọ (danh từ cố định). Tạm dịch: Tuổi thọ của người hút thuốc ngắn hơn người không hút.'),
    ('B', '"agreed rules ... its members <b>must</b> follow": nghĩa vụ/quy định mà thành viên phải tuân theo. don\'t have to: không cần; mustn\'t: cấm; had to: quá khứ.'),
    ('B', 'think of going on a diet = đang cân nhắc ăn kiêng (hành động đang diễn ra trong suy nghĩ) -> <b>is thinking</b> (hiện tại tiếp diễn).'),
    ('A', 'catch the <b>eye</b> of sb = thu hút sự chú ý của ai (collocation).'),
    ('A', '"recently" -> thì hiện tại hoàn thành: <b>has improved</b>. Tạm dịch: Chính phủ gần đây đã cải thiện cơ sở hạ tầng các thành phố lớn để thúc đẩy kinh tế.'),
], 15)
# ---------- Đọc hiểu
put('g6', [
    ('A', 'Bài nói về lợi ích của việc tập vào các thời điểm khác nhau: sáng, chiều, tối -> <b>Workouts at different times and their benefits</b>.'),
    ('C', '"Morning exercise also helps many people <b>sleep better at night</b>." -> You have a better night\'s sleep.'),
    ('B', '<b>endurance</b> = khả năng chịu đựng/duy trì việc gì khó nhọc trong thời gian dài: "the ability to continue doing something painful or difficult for a long period of time".'),
    ('D', '"Exercising at this time decreases your chances of injury" -> <b>You can avoid the risk of injury</b>. (Nhiệt độ cơ thể cao nhất, nhịp tim và huyết áp thấp nhất nên A, C sai; phản xạ nhanh nhất nên B sai.)'),
    ('C', '"In the afternoon or evening, your reaction time is at <b>its</b> quickest" -> "its" thay cho <b>reaction time</b>.'),
    ('A', '<b>blood pressure</b> (huyết áp) = a measure of the force with which blood flows through the body.'),
], 21)
# ---------- Chia động từ
put('g7', [
    ({'blanks': [['Have', 'have'], ['discovered']]}, '"... yet?" -> hiện tại hoàn thành, nghi vấn: <b>Have scientists discovered</b> a new cancer drug yet? (Các nhà khoa học đã tìm ra thuốc điều trị ung thư mới chưa?)'),
    ({'blanks': [['have'], ['bought']]}, 'Hành động đã xong, còn liên quan hiện tại ("Can you help me cook the dish now?") -> hiện tại hoàn thành: <b>I have bought</b> all the ingredients.'),
    ({'blanks': [['has built', 'has been building'], ['started']]}, '"since he started ..." : mệnh đề sau since dùng quá khứ đơn <b>started</b>; mệnh đề chính dùng hiện tại hoàn thành <b>has built</b> (hoặc has been building) muscles.'),
], 27)
# ---------- Từ loại
put('g8', [
    (['negative'], 'Trước danh từ "impact" cần tính từ: NEGATE -> <b>negative</b> impact (tác động tiêu cực).'),
    (['efficiently'], 'Sau "operate more" cần trạng từ: EFFICIENCY -> <b>efficiently</b> (một cách hiệu quả).'),
    (['traditional'], 'Trước danh từ "views" cần tính từ: TRADITION -> <b>traditional</b> views (quan điểm truyền thống).'),
    (['treatment', 'treatments'], 'receive + danh từ: TREAT -> <b>treatment</b> (sự điều trị).'),
], 30)
# ---------- Viết lại câu
put('g9', [
    (['should not leave their jobs after getting', 'shouldn\'t leave their jobs after getting', 'should not quit their jobs after getting',
      'should not give up their jobs after getting'],
     '<b>Mẫu:</b> Women should not leave their jobs after getting married. (It is not a good idea for sb to V = sb should not V)'),
    (['must follow the family house rules', 'must follow the house rules', 'must follow the family rules', 'must obey the family house rules'],
     '<b>Mẫu:</b> All family members must follow the family house rules. (It is important for sb to V = sb must V)'),
    (['called each other for a long time', 'phoned each other for a long time', 'called each other for ages', 'called each other for a long time.'],
     '<b>Mẫu:</b> We haven\'t called each other for a long time. (It has been a long time since we last V-ed = we haven\'t V3 for a long time)'),
    (['have you been receiving the treatment', 'have you been having the treatment', 'have you had the treatment', 'have you been getting the treatment',
      'have you been undergoing the treatment', 'have you been on the treatment', 'have you been on treatment', 'have you been in treatment',
      'have you been receiving treatment', 'have you been having treatment'],
     '<b>Mẫu:</b> How long have you been receiving/having the treatment? (When did you start ...? = How long + have you + been V-ing / V3 ...?)'),
], 34)
