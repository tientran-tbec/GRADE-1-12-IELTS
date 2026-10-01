# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Unit 2 (Tiếng Anh 10 Global Success) – Bộ BÀI TẬP CHUYÊN SÂU.
Quy ước:
  mcq  : chữ cái 'A'-'D' (plain: chính văn bản phương án; nhiều đáp án đúng: danh sách)
  tfng : 'T' / 'F' / 'NG'
  fill : danh sách đáp án chấp nhận (1 ô) hoặc {'blanks': [[...],[...]]} (nhiều ô)
  open : không chấm điểm, EXPLANATIONS chứa đáp án mẫu
Đáp án lấy từ khoá trong file Word (nửa sau file src/l10u2/cs_c.txt, từ dòng 1316) rồi tự giải độc lập để đối chiếu;
phần không có khoá trong Word được tự giải. Những chỗ khoá Word sai/mơ hồ hoặc tự giải được liệt kê ở GHI_CHU_RA_SOAT."""

GHI_CHU_RA_SOAT = [
    'PHẠM VI: file Word chỉ chứa Unit 2 (phần đề dòng 1-1315 của cs_c.txt; phần khoá lặp lại lý thuyết + đáp án). Nội dung thực tế xoay quanh cơ thể/sức khoẻ + thì tương lai (will / be going to) + câu bị động. Ba đề: Test 1, Test 2 và đề thứ ba (nhãn gốc ghi "TEST 2" lần hai, khoá ghi "TEST 3") 140 câu → làm trang kiểm tra tính giờ; thời gian 120 phút là do soạn giả tự đặt (Word không ghi).',
    'KHÔNG CÓ KHOÁ trong Word cho: bài I-III phần cơ bản (tl1.x, tl2.x, tl3.x), Test 1 IX (intention/prediction) và XIV (correct/incorrect), Test 1 Reading Part 2 (T/F/NG), Test 1 II.1 (cột hệ cơ quan: chỉ liệt kê từ, không chia cột), các câu viết Test 1 I (thư), và Test 2 D.I (khoá chỉ có phần đuôi câu, KHÔNG có phần đầu). Các câu này do tự giải.',
    'tl3.x (bài III): đề không nói rõ nên một số câu chấp nhận cả will lẫn be going to (tl3.3, tl3.5, tl3.6, tl3.12). Giáo viên xem lại.',
    'tl6.2 (intention/prediction): "our country is going to join many multinational organizations" – tự giải = Prediction (không có chủ ý cá nhân); có thể hiểu là kế hoạch quốc gia. tl6.1/6.8/6.9/6.10 = Prediction (will); tl6.3-6.5, 6.7 = Intention; tl6.6 = Prediction (có bằng chứng). Giáo viên xem lại.',
    'tv1.12 (muscle): đề chỉ liệt kê 15 từ, khoá chỉ liệt kê tuần tự không chia cột rõ. Phân loại theo khoá: circulatory (blood, heart, pump, vessel); digestive (stomach, digestive); respiratory (breath, lung, air); skeletal (skull, bone, spine, muscle); nervous (brain, nerve). "muscle" xếp vào skeletal (hệ cơ-xương); dưới góc độ khác có thể không vừa hệ nào.',
    'tl4.x (Test 1 VII): theo khoá Word: 1 B, 2 A, 3 B, 4 A, 5 C; giữ nguyên.',
    'tl7.1 (Test 1 X): "Kate ___ (not join) us next Friday; she will be taking exams" – khoá Word = is not going to join; đã chấp nhận thêm will not join. tl7.4: khoá = will not work; chấp nhận thêm is not going to work (bằng chứng: động cơ vừa hỏng). tl7.8: khoá = are going to be; chấp nhận thêm will be (theo kế hoạch).',
    'tl8.4: khoá = will happen; chấp nhận thêm is going to happen. tl8.11: khoá = are going to move; chấp nhận thêm are moving.',
    'bt6.6: khoá Word = A (is going to be held) vì "As planned"; will be held (B) cũng đúng ngữ pháp nhưng giữ khoá Word.',
    'bt5.x (XVII): khoá Word chỉ ghi từ đã sửa; đề gốc yêu cầu tìm từ sai/thừa nên trên web chia 2 ô: ô 1 = từ sai (lấy từ phần gạch chân của khoá), ô 2 = từ sửa lại hoặc "bỏ" (khi từ thừa: bt5.8 be, bt5.9 was).',
    'nc1.2 (Word khoá = are going to have): thêm are having; nc1.3, nc1.4, nc1.5 chấp nhận cả hai dạng tương lai hợp lí (am going to / am meeting / is flying / is going to fly).',
    'nc2.4: khoá Word = was still being built (đề không in chữ "still" nên chấp nhận cả was being built).',
    'dt1.1 (Test 2 Reading cloze): khoá Word = A (started); D (appeared) cũng đúng nghĩa/ngữ pháp nên chấp nhận cả A và D.',
    'gt3.6: khoá Word ghi "disadvnatage" (lỗi gõ) → đáp án đúng "disadvantage" (đề cho ADVANTAGE, nghĩa "bất lợi chính của tỏi là hơi thở hôi").',
    'gt4.x (Test 2 IV, 10 lỗi): khoá Word ghi: industrialize → Industrialization; underpopulation → Overpopulation; great → Large; in → From; make → to make; attractively → Attractive; here → There; to → For; so as → such as; educational → Education. Học sinh phải liệt kê theo thứ tự xuất hiện trong đoạn.',
    'vw1.x (Test 2 D.I): Word khoá chỉ có phần ĐUÔI câu, phần đầu bị mất. Phần đầu trong đề trên web (Nobody… / It came… / If it… / Our hotel booking… / Her uncle didn\'t… / Betty is devoted… / Not only… / They stole… / All dogs…) do tự dựng lại cho khớp với phần đuôi của khoá. vw1.6 (khoá "to looking after handicapped people" nên chọn devoted/dedicated/committed to).',
    'vw1.8: khoá chỉ ghi "having witnessed the crime", không dựng lại được câu gốc → để dạng câu mở (không chấm), đáp án mẫu tự soạn: He denied having witnessed the crime as he had been a long way from the scene at the time. Giáo viên xem lại.',
    'vt2.1 (Test 1 viết thư trả lời Dr. Glenn): chỉ có đề, không có đáp án trong khoá → bài mẫu tự soạn.',
    'kt.32: cure ≈ treatment (khoá Word D) nhưng therapy (C) cũng gần nghĩa → chấp nhận cả C và D.',
    'kt.45: khoá Word = B (be ineffective); be unhelpful (D) cũng có thể chấp nhận, giữ khoá Word.',
    'kt.55: khoá Word = B (am going to meet); will be meeting (C) cũng đúng (sự việc đã sắp xếp tại thời điểm cụ thể) → chấp nhận B và C.',
    'kt.59: khoá Word = A; will you leave (C) cũng đúng → chấp nhận A và C (do you leave – lịch trình – cũng có thể dùng nhưng không chấp nhận).',
    'kt.60: khoá Word = C (will win – dự đoán); is going to win (A) cũng đúng → chấp nhận A và C.',
    'kt.63: khoá Word = D (will bite); is going to bite (C) cũng tự nhiên (có bằng chứng con chó dữ) → chấp nhận C và D.',
    'kt.21: spoil your breath – khoá Word = D; cách dùng khá hiếm nhưng các phương án còn lại sai hơn.',
    'kt.39: khoá Word = A (Eating); ingesting/swallowing cũng gần nghĩa nhưng giữ khoá Word. kt.127: khoá Word = D (suffering) – nghĩa của injury khá khiên cưỡng; giữ khoá Word. kt.129: khoá = C (rapidly); abruptly (A) cũng có thể gần nghĩa trái nhưng giữ khoá.',
    'kt.123: khoá Word = B (Gentle jogging); Keeping fit (C) cũng hợp lí nhưng bài chủ yếu nói về chạy bộ nhẹ nhàng → giữ khoá Word.',
    'kt.134: khoá Word = D; đề in sẵn đúng đáp án nhưng câu A cũng gần nghĩa (should be done) – D mới đúng thì quá khứ (should have been done).',
    'Lỗi nguồn đã sửa trong generator: pultry → poultry (kt.8); museles → muscles (kt.13); ot which → of which (kt.85); "l06/l08/l10", "6l" → 106/108/110/61; "fiee" → free; "ﬁrst/ﬁber" (ký tự ghép) → first/fiber; "But now (111)" → "But how (111)"; thiếu dấu chấm "113. A by" → "113. A. by", "D.with"; "C. ump" → "C. jump"; "too seared" → "too scared"; "How arc you" → "How are you"; "Can 1 listen", "shall 1 take", "1 am sorry" → I; "an At" → "an A+"; "Albeit Landon" → Albert; "Tottemham" → Tottenham; "Edinburg" → Edinburgh; "The hrain" → brain; "tasks bellow" → below; "stabled" → stabilized (kt.47); dấu nháy ‘ → ’; viết hoa thừa ở một số phương án (Provides, Protect, Sore, Use, Which); dấu ngoặc kép bị lỗi (clouds!“, start?’); "while (play) ____- tennis" bỏ dấu gạch thừa; câu 8 Test 1 VII "Both A & B" tách đúng thành 3 phương án.',
    'Bài ghép cột Test 1 II (tv3): khoá Word 1-a, 2-c, 3-b, 4-f, 5-e, 6-d. Ảnh Test 1 phần B.1 (tv2): lấy image9-14 của phần đề; khoá Word dùng image15-17 (bản lặp của image9-11) nên không đưa vào.',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


def put_open(prefix, rows):
    for i, e in enumerate(rows, 1):
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


def B(*blanks):
    """nhiều ô điền: mỗi tham số là 1 chuỗi hoặc danh sách đáp án chấp nhận cho ô đó"""
    return {'blanks': [list(b) if isinstance(b, (list, tuple)) else [b] for b in blanks]}


def S(*alts):
    """danh sách đáp án chấp nhận cho 1 ô"""
    return list(alts)


# ============================================================ PHÁT ÂM
_cl = {'/pl/': 'pl', '/pr/': 'pr', '/gl/': 'gl', '/gr/': 'gr'}
_pa1 = 'profit:/pr/ plan:/pl/ glean:/gl/ plough:/pl/ globe:/gl/ plane:/pl/ promotion:/pr/ plumber:/pl/ grimy:/gr/ grey:/gr/ groom:/gr/ play:/pl/ praise:/pr/ pronoun:/pr/ green:/gr/ practice:/pr/ grip:/gr/ glue:/gl/ glide:/gl/ global:/gl/'.split()
put('pa1', [(x.split(':')[1], '<b>%s</b> bắt đầu bằng "%s" → cụm phụ âm %s.' % (x.split(':')[0], _cl[x.split(':')[1]], x.split(':')[1])) for x in _pa1])
put('pa2', [
    ('B', '<b>chest</b> /tʃest/ (ch = /tʃ/). stomach /ˈstʌmək/, chord /kɔːd/, psychology /saɪˈkɒlədʒi/ có ch = /k/.'),
    ('C', '<b>massage</b> /ˈmæsɑːʒ/ (g = /ʒ/). digestive, suggest, allergy có g = /dʒ/.'),
    ('D', '<b>circulatory</b> /ˈsɜːkjələtri/ (u = /j/ + /ə/). skull /skʌl/, study /ˈstʌdi/, lung /lʌŋ/ có u = /ʌ/.'),
    ('A', '<b>resistance</b> /rɪˈzɪstəns/ (s = /z/). respiratory, vessel, system có s = /s/.'),
    ('C', '<b>intestine</b> /ɪnˈtestɪn/ (s = /s/). sugary /ˈʃʊɡəri/, acupressure /ˈækjuprɛʃə/, sure /ʃɔː/ có s/ss = /ʃ/.'),
])
put('pa3', [
    ('C', '<b>supposedly</b> /səˈpəʊzɪdli/ (ed = /ɪd/). relaxed /rɪˈlækst/, reached /riːtʃt/, crossed /krɒst/ có ed = /t/.'),
    ('A', '<b>machine</b> /məˈʃiːn/ (ch = /ʃ/). stomach, architecture, chorus có ch = /k/.'),
    ('A', '<b>mature</b> /məˈtʃʊə/ (ture = /tʃʊə/). pasture /ˈpɑːstʃə/, gesture /ˈdʒestʃə/, creature /ˈkriːtʃə/ có ture = /tʃə/.'),
    ('B', '<b>considerate</b> /kənˈsɪdərət/ (d = /d/). individual, education, procedure có d = /dʒ/.'),
    ('B', '<b>though</b> /ðəʊ/ (gh câm). laugh, tough, enough có gh = /f/.'),
])
put('pa4', [
    ('D', '<b>statistics</b> /stəˈtɪstɪks/ – nhấn âm 2. politics, literature, chemistry nhấn âm 1.'),
    ('C', '<b>museum</b> /mjuˈziːəm/ – nhấn âm 2. likeable, oxygen, energy nhấn âm 1.'),
    ('C', '<b>generously</b> /ˈdʒenərəsli/ – nhấn âm 1. apology, stupidity, astronomy nhấn âm 2.'),
    ('A', '<b>television</b> /ˈtelɪvɪʒn/ – nhấn âm 1. distinguish, immediate, acquaintance nhấn âm 2.'),
    ('B', '<b>introduce</b> /ˌɪntrəˈdjuːs/ – nhấn âm 3. experience, determine, appliance nhấn âm 2.'),
])

# ============================================================ TỪ VỰNG
_sys = {'circulatory': 'circulatory system', 'digestive': 'digestive system', 'respiratory': 'respiratory system', 'skeletal': 'skeletal system', 'nervous': 'nervous system'}
_tv1 = [('circulatory', 'blood = máu → hệ tuần hoàn.'), ('respiratory', 'breath = hơi thở → hệ hô hấp.'), ('skeletal', 'skull = hộp sọ → hệ xương.'),
        ('skeletal', 'bone = xương → hệ xương.'), ('circulatory', 'heart = tim → hệ tuần hoàn.'), ('nervous', 'brain = não → hệ thần kinh.'),
        ('respiratory', 'lung = phổi → hệ hô hấp.'), ('digestive', 'stomach = dạ dày → hệ tiêu hoá.'), ('digestive', 'digestive = thuộc tiêu hoá → hệ tiêu hoá.'),
        ('respiratory', 'air = không khí → hệ hô hấp.'), ('circulatory', 'pump = bơm (máu) → hệ tuần hoàn.'), ('skeletal', 'muscle = cơ → xếp vào hệ xương (theo khoá; xem ghi chú).'),
        ('skeletal', 'spine = cột sống → hệ xương.'), ('nervous', 'nerve = dây thần kinh → hệ thần kinh.'), ('circulatory', 'vessel (blood vessel) = mạch máu → hệ tuần hoàn.')]
put('tv1', [(_sys[a], e) for a, e in _tv1])
put('tv2', [
    ('brain', 'Hình bộ não phát sáng → <b>brain</b>.'),
    ('skin', 'Hình da mặt phóng to bằng kính lúp → <b>skin</b>.'),
    ('blood vessel', 'Hình mạch máu và các tế bào máu → <b>blood vessel</b>.'),
    ('lung', 'Hình hai lá phổi → <b>lung</b>.'),
    ('stomach', 'Hình dạ dày trong ổ bụng → <b>stomach</b>.'),
    ('bone', 'Hình bộ xương → <b>bone</b>.'),
])
put('tv3', [
    ('a', 'Stress <b>can be effectively reduced by doing yoga</b> (a).'),
    ('c', 'Treatment for this type of disease <b>can take a long time</b> (c).'),
    ('b', 'A healthy lifestyle <b>can prevent many common diseases</b> (b).'),
    ('f', 'Remember <b>to include these five foods in your diet to boost your health</b> (f).'),
    ('e', 'Read the following information <b>to learn about what a food allergy is</b> (e).'),
    ('d', 'Bad breath <b>is not just about embarrassment, it may be a sign of other health problems</b> (d).'),
])
put('tv4', [
    ('C', '<b>head massage</b> (xoa bóp đầu) thường đi kèm khi cắt tóc; bone, blood vessel, allergy không phải thứ "được làm".'),
    ('D', '<b>side effects</b> (tác dụng phụ) của thuốc có thể rất nguy hiểm.'),
    ('A', '<b>health care system</b> = hệ thống chăm sóc sức khoẻ (có bác sĩ và cơ sở vật chất).'),
    ('D', '<b>sleeplessness</b> = mất ngủ (giải thích "unhealthy sleep patterns").'),
    ('B', '<b>sleepiness</b> = buồn ngủ (cảm thấy buồn ngủ suốt ngày); sleeplessness là mất ngủ.'),
])
put('tv5', [
    (S('food pyramid'), '<b>food pyramid</b> (tháp dinh dưỡng) giúp chọn thực phẩm tốt hơn.'),
    (S('calorie need', 'calorie needs'), 'Your daily <b>calorie need</b> = nhu cầu calo hằng ngày.'),
    (S('harmony'), '<b>harmony</b> between people and their environment = sự hài hoà giữa con người và môi trường.'),
    (S('sugary drinks'), 'Ngoài sâu răng, <b>sugary drinks</b> (đồ uống có đường) còn gây nhiều vấn đề sức khoẻ.'),
    (S('whole grains', 'whole grain'), 'Khuyên ăn 3 loại thực phẩm trở lên từ <b>whole grains</b> (ngũ cốc nguyên hạt).'),
    (S('balance between yin and yang'), 'Khoẻ mạnh khi có <b>balance between yin and yang</b> (cân bằng âm dương).'),
])
put('tv6', [
    ('B', '<b>practices</b> = tập quán, cách làm (traditional health beliefs and practices).'),
    ('A', 'Kim mảnh châm vào huyệt → <b>acupuncture</b> (châm cứu).'),
    ('B', 'Tim <b>pump</b> (bơm) máu; change/sell không hợp nghĩa.'),
    ('C', 'Tự khỏi sau vài ngày → <b>common ailment</b> (bệnh vặt thông thường).'),
    ('A', 'safety <b>precautions</b> = các lưu ý an toàn.'),
])
put('tv7', [
    (S('immune system'), 'Hệ miễn dịch (<b>immune system</b>) bảo vệ cơ thể chống bệnh.'),
    (S('therapy'), 'Bạn đã thử <b>therapy</b> (liệu pháp) nào cho chứng mất ngủ chưa?'),
    (S('bacterium'), 'a strange <b>bacterium</b> type = một loại vi khuẩn lạ (danh từ số ít).'),
    (S('disorder'), 'sleeping <b>disorder</b> = rối loạn giấc ngủ.'),
    (S('intestine'), 'từ dạ dày xuống small <b>intestine</b> (ruột non) rồi tới ruột già.'),
    (S('skeleton'), 'The <b>skeleton</b> = bộ xương, cấu trúc xương nâng đỡ cơ thể.'),
])

# ============================================================ THÌ TƯƠNG LAI
put('tl1', [
    (S('will be'), 'Dự đoán của thầy bói → will + V: You <b>will be</b> very happy.'),
    (S('will get'), 'Dự đoán tương lai → <b>will get</b>.'),
    (S('will buy'), 'Dự đoán → <b>will buy</b>.'),
    (S('will envy'), 'Dự đoán → <b>will envy</b>.'),
    (S('will meet'), 'Dự đoán → <b>will meet</b>.'),
    (S('will marry'), 'Dự đoán → <b>will marry</b>.'),
    (S('will travel'), 'You and your wife <b>will travel</b> around the world.'),
    (S('will serve'), 'People <b>will serve</b> you.'),
    (S('will not refuse', "won't refuse", 'will never refuse'), 'Phủ định: will not (won\'t) + V → <b>will not refuse</b>.'),
    (S('will only happen', 'will happen only'), '"only" đứng giữa will và V: all this <b>will only happen</b> when you are 70.'),
])
put('tl2', [
    (S('My father is going to paint the room purple'), 'Hình người sơn tường màu tím → S + is going to + V: My father <b>is going to paint</b> the room purple.'),
    (S('My brother is going to ride a horse'), 'Hình cậu bé dắt ngựa → My brother <b>is going to ride</b> a horse.'),
    (S('I am going to learn the English alphabet'), 'I + <b>am going to</b> learn the English alphabet.'),
    (S('Are you going to do exercise'), 'Câu hỏi: <b>Are</b> you <b>going to</b> do exercise?'),
    (S('They are going to get married'), 'Hình cô dâu chú rể → They <b>are going to get</b> married.'),
    (S('I am going to have a big breakfast'), 'I <b>am going to have</b> a big breakfast.'),
    (S('We are going to have fun at the playground'), 'We <b>are going to have</b> fun at the playground.'),
    (S('Mickey is going to play computer games'), 'Mickey <b>is going to play</b> computer games.'),
])
put('tl3', [
    (S('will bring'), 'Vừa nhớ ra, quyết định tức thời/lời hứa → <b>will bring</b>.'),
    (S('am going to buy'), 'Đã biết mua gì (có kế hoạch) → <b>am going to buy</b>.'),
    (S('will stay', 'am going to stay'), '"I don\'t feel like going out" – quyết định tại lúc nói → <b>will stay</b> (am going to stay cũng chấp nhận).'),
    (S('will go'), 'Có người gõ cửa → quyết định tức thời: <b>will go</b>.'),
    (S('is going to open', 'is opening'), 'Mark đã có kế hoạch mở cửa hàng → <b>is going to open</b>.'),
    (S('am going to look', 'will look', 'am looking'), '"I\'ve decided" (đã quyết định) → <b>am going to look</b>.'),
    (S('will take'), 'Quyết định tức thời sau khi nghe thông tin → <b>will take</b>.'),
    (S('will go'), 'Quyết định tức thời trước tình huống kẹt xe → <b>will go</b>.'),
    (S('am going to buy'), 'Đã có dự định mua (đã biết mua gì) → <b>am going to buy</b>.'),
    (S('will bring'), 'Xin lỗi và hứa → <b>will bring</b>.'),
    (S('will open'), 'Quyết định tức thời/đề nghị giúp → <b>will open</b>.'),
    (S('are going to start', 'are starting'), '"We\'re planning to open…" (đã có kế hoạch) → <b>are going to start</b>.'),
])
put('tl4', [
    ('B', 'Có bằng chứng ở hiện tại (hàng dài) → <b>are going to</b> miss (dự đoán có căn cứ).'),
    ('A', 'Lời hứa/quyết định tức thời khi thấy Alex → <b>will</b>.'),
    ('B', 'Quyết định đã được đưa ra ("reached the final decision") → <b>is going to</b> lead.'),
    ('A', 'I hope + will: <b>will</b> visit.'),
    ('C', 'Dự đoán chung về tương lai ("in the future") → will hoặc be going to đều được → <b>Both A & B</b>.'),
])
put('tl5', [
    ('Incorrect', 'Chuyến đi đã sắp xếp, dự định → phải dùng <b>are going to visit</b> (không phải will).'),
    ('Correct', 'Quyết định tức thời "Just a moment" → <b>will help</b> là đúng.'),
    ('Incorrect', '"I think my mother ... like" – dự đoán chủ quan → <b>will like</b>, không dùng be going to.'),
    ('Correct', 'Dự đoán chung chung về tương lai ("In the future") → will replace.'),
    ('Incorrect', '"As planned" – kế hoạch đã định → <b>is going to visit</b>.'),
    ('Incorrect', 'Có bằng chứng ("so nervous") → <b>is going to have</b> a baby.'),
])
put('tl6', [
    ('Prediction', 'will + "when we grow older" → dự đoán chung (không có chủ ý).'),
    ('Prediction', 'Dự đoán xu hướng tương lai của đất nước, không phải ý định cá nhân. (Có thể hiểu là kế hoạch quốc gia – xem ghi chú.)'),
    ('Intention', 'Hỏi về dự định sử dụng khoản tiền: What are they <b>going to</b> do with…?'),
    ('Intention', '"She wants to settle down in her hometown" → dự định không dạy ở Việt Nam.'),
    ('Intention', 'Marian dự định tổ chức tiệc tuần sau (kế hoạch).'),
    ('Prediction', 'Còn 10 phút (bằng chứng hiện tại) → dự đoán sẽ trễ học.'),
    ('Intention', 'Jack và bạn dự định mở nhà hàng (kế hoạch).'),
    ('Prediction', 'will + "more and more" → dự đoán xu hướng.'),
    ('Prediction', '"What do you think will happen" → hỏi dự đoán.'),
    ('Prediction', '"Do you think he will be…" → hỏi dự đoán.'),
])
put('tl7', [
    (S('is not going to join', "isn't going to join", 'will not join', "won't join"), '"she will be taking exams that day" → kế hoạch/sự việc đã định: <b>is not going to join</b>.'),
    (S('am going to visit'), 'Hỏi về kế hoạch (plans) → <b>am going to visit</b>.'),
    (S('will take'), '"Alright" – quyết định tức thời giúp đỡ → <b>will take</b>.'),
    (S('will not work', "won't work", 'is not going to work', "isn't going to work"), 'Động cơ vừa hỏng (bằng chứng) → <b>will not work</b> (khoá Word) / is not going to work cũng hợp lí.'),
    (S('will take'), 'Lời hứa có điều kiện (as long as…) → <b>will take</b>.'),
    (S('will win'), 'Do you think… → dự đoán (hỏi ý kiến) → <b>will win</b>.'),
    (S('will have'), '"I think we…" + quyết định lúc gọi món → <b>will have</b>.'),
    (S('are going to be', 'will be'), '"According to schedule" – kế hoạch → <b>are going to be</b> distributed.'),
])
put('tl8', [
    (S('will remember'), 'Vừa nhận ra quên → quyết định tức thời/hứa: I <b>will remember</b> to buy some tomorrow.'),
    (S('am going to take'), '"Why are you putting on your coat?" → mục đích đã định: <b>am going to take</b> my dog out.'),
    (S('am going to stay'), '"I bought a new book this morning" – đã có dự định ở nhà đọc → <b>am going to stay</b>.'),
    (S('will happen', 'is going to happen'), 'Dự đoán "What will happen to…if…" → <b>will happen</b>.'),
    (S('am going to watch'), 'Giải thích lý do đã có kế hoạch (dậy lúc 2 giờ sáng) → <b>am going to watch</b>.'),
    (S('will turn'), 'Quyết định tức thời nghe yêu cầu → <b>will turn</b> it up.'),
    (S('will get'), 'Đề nghị giúp (offer) → <b>will get</b> you a cup of coffee.'),
    (B(['Will'], ['come']), 'Lời đề nghị/nhờ vả: <b>Will</b> you <b>come</b> to give a hand?'),
    (S('will walk'), 'Câu điều kiện thời gian "As soon as…" → <b>will walk</b>.'),
    (S('am going to study'), '"I\'ve always been interested…" – đã có dự định → <b>am going to study</b>.'),
    (S('are going to move', 'are moving'), 'Chồng đã nhận việc → kế hoạch đã định: <b>are going to move</b>.'),
])
put('tl9', [
    (S('are going to leave'), '"made a final decision yesterday" → kế hoạch: <b>are going to leave</b> Edinburgh for Nice.'),
    (S('will give'), 'Lời hứa "Don\'t worry" → <b>will give</b> you a ring.'),
    (S('am going to visit'), 'Dự định buổi chiều (lí do không gặp được) → <b>am going to visit</b>.'),
    (S('will give'), 'Lời hứa trả lại sách → <b>will give</b> it back.'),
    (S('is going to put'), '"has decided" → <b>is going to put</b> up with (chịu đựng).'),
    (B(['Will'], ['pick']), 'Lời nhờ: <b>Will</b> you <b>pick</b> up the children at 5?'),
    (S('will get'), 'I hope + will: you and Glenn <b>will get</b> along well.'),
    (S('is going to turn'), 'Đã mời Susan, kế hoạch → she <b>is going to turn</b> up at the party.'),
])

# ============================================================ BỊ ĐỘNG CƠ BẢN
put('bd1', [
    ('active voice', '"have never been to Paris": been là phân từ của <i>be</i> (đã từng đến) → câu chủ động.'),
    ('passive voice', 'have never been arrested = chưa bao giờ bị bắt → bị động.'),
    ('passive voice', 'was built in 1802 by… → bị động.'),
    ('active voice', 'Nothing happened: <i>happen</i> là nội động từ → chủ động.'),
    ('passive voice', 'was injured by the fire → bị động.'),
    ('passive voice', 'was given to the top student → bị động.'),
    ('active voice', 'We decided not to hire → chủ động.'),
    ('active voice', 'The pizza was delicious: was + tính từ, không phải bị động.'),
    ('passive voice', 'was ordered → bị động.'),
    ('active voice', 'The pizza made me sick: chủ động (made + O + adj).'),
])
put('bd2', [
    (S('are explained'), 'Hiện tại đơn bị động: are/is + V3 → The words <b>are explained</b>.'),
    (S('was stolen'), 'Quá khứ đơn bị động: <b>was stolen</b>.'),
    (S('will be opened'), 'Tương lai đơn bị động: will be + V3 → <b>will be opened</b>.'),
    (S('is being closed'), 'Hiện tại tiếp diễn bị động: is being + V3 → <b>is being closed</b>.'),
    (S('is going to be built'), 'Be going to bị động: is going to be + V3 → <b>is going to be built</b>.'),
])
put('bd3', [
    (S('are eaten'), 'HTĐ bị động, hamburgers số nhiều → <b>are eaten</b>.'),
    (S('is spoken'), 'English số ít → <b>is spoken</b>.'),
    (B(['was'], ['invented']), 'QKĐ nghi vấn bị động: Where <b>was</b> gun powder <b>invented</b>?'),
    (S("wasn't found", 'was not found'), 'QKĐ phủ định bị động → <b>wasn\'t found</b>.'),
    (S("isn't visited", 'is not visited'), 'HTĐ phủ định bị động → <b>isn\'t visited</b>.'),
    (S('is being built'), 'HTTD bị động → <b>is being built</b>.'),
    (B(['was'], ['translated']), 'QKĐ nghi vấn bị động: When <b>was</b> this book <b>translated</b>…?'),
    (S('are sent'), 'HTĐ bị động, emails số nhiều → <b>are sent</b>.'),
    (S('was brought'), 'Daisy brought me grapes → I <b>was brought</b> some fresh grapes by Daisy.'),
    (S('was being followed'), 'QKTD bị động → I <b>was being followed</b>.'),
])
put('bd4', [
    (S('Vietnamese is spoken in Vietnam'), 'People = chủ ngữ chung → bỏ "by people": Vietnamese <b>is spoken</b> in Vietnam.'),
    (S('A new road is being planned near my house by the government', 'A new road is being planned near my house'), 'HTTD bị động: <b>is being planned</b>.'),
    (S('This house was built by my grandfather in 1990', 'This house was built in 1990 by my grandfather'), 'QKĐ bị động: <b>was built</b> by… (by + O trước trạng từ thời gian).'),
    (S('Guernica was being painted by Picasso at that time'), 'QKTD bị động: <b>was being painted</b>.'),
    (S('The office has been cleaned by the cleaner', 'The office has been cleaned'), 'HTHT bị động: <b>has been cleaned</b>.'),
    (S('Three books had been written before 1867', 'Three books had been written by him before 1867'), 'QKHT bị động: <b>had been written</b>.'),
    (S('You will be told by John later', 'You will be told later by John', 'You will be told later'), 'Tương lai đơn bị động: <b>will be told</b>.'),
    (S('The work was done', 'The work was done by somebody'), 'Somebody là chủ ngữ không xác định → bỏ: The work <b>was done</b>.'),
])
put('bd5', [
    (S('The policemen help the children'), 'Bị động HTĐ → chủ động HTĐ: The policemen <b>help</b> the children.'),
    (S('The manager is typing a letter'), 'HTTD: The manager <b>is typing</b> a letter.'),
    (S('Sally will look after her little brother'), 'will be looked after → <b>will look after</b>.'),
    (S('The robber broke our window'), 'was broken → QKĐ <b>broke</b>.'),
    (S('We have cleaned the car'), 'has been cleaned → <b>have cleaned</b>.'),
    (S('My parents offered me a bike for my birthday', 'My parents offered a bike to me for my birthday'), 'was offered → <b>offered</b> (me là tân ngữ gián tiếp).'),
])
put('bd6', [
    (S('Are cars made in Thailand'), 'Are + S + V3 + nơi chốn?'),
    (S('Has she been taken to hospital', 'Has she been taken to the hospital'), 'HTHT bị động nghi vấn: Has + S + been + V3?'),
    (S('Can the potatoes be fried in ten minutes'), 'Can + S + be + V3?'),
    (S('Will the students be prepared for the exam'), 'Will + S + be + V3?'),
    (S('When will tea be served'), 'Từ để hỏi + will + S + be + V3?'),
    (S('Is lunch being provided today'), 'HTTD bị động nghi vấn: Is + S + being + V3?'),
    (S('Were laptops given to them last week'), 'QKĐ bị động nghi vấn: Were + S + V3?'),
    (S('May the videos be broadcasted', 'May the videos be broadcast'), 'May + S + be + V3?'),
])

# ============================================================ BỊ ĐỘNG – TEST 1
put('bt1', [
    (S('will not be accepted', "won't be accepted"), 'Tương lai đơn phủ định bị động: will not be accepted.'),
    (S('are read'), 'HTĐ bị động, articles số nhiều: are read.'),
    (S('is recycled'), 'HTĐ bị động, waste paper không đếm được: is recycled.'),
    (S('is thought'), 'It is thought that… (HTĐ bị động).'),
    (S('are going to be given'), 'Be going to bị động: are going to be given.'),
    (S('was punished'), 'QKĐ bị động: was punished.'),
    (S('have been taught'), 'HTHT bị động: have been taught (since April).'),
])
put('bt2', [
    ('Incorrect', 'apologize là nội động từ, không dùng bị động: She apologized to me.'),
    ('Incorrect', '"last month" → quá khứ: The problem <b>was</b> not paid enough attention to.'),
    ('Correct', 'HTĐ phủ định bị động: Artificial flowers are not given… đúng.'),
    ('Incorrect', '"found" = tìm thấy; thành lập là <i>founded</i> → This fund was founded in 2002.'),
    ('Incorrect', 'receive đã là tân ngữ "her letter" → He received her letter / bị động sai.'),
    ('Incorrect', 'take place là nội động từ, không có bị động: will take place.'),
    ('Correct', 'The job was offered to Yoko… đúng.'),
    ('Incorrect', 'react là nội động từ, không có bị động: How did he react…?'),
    ('Correct', 'will be punished (tương lai bị động) đúng.'),
    ('Incorrect', 'Trật tự sai: Will newspapers be delivered…?'),
])
put('bt3', [
    ('A', 'give → was given (QKĐ bị động); C sai V2 sau was; B sai thì.'),
    ('A', 'Traditional medicine is believed to be safer… (bị động); B/C sai cấu trúc.'),
    ('B', 'Where + are + S + V3? ; A thiếu đảo, C dùng "keep" sai dạng.'),
    ('B', 'The good news was not told to us (news là danh từ số ít không đếm được).'),
    ('C', 'will be taken care of (bị động của take care of).'),
    ('A', 'When will Johny be picked up? (will + S + be + V3).'),
    ('A', 'are going to be sold (bị động).'),
    ('B', 'has been brought up (HTHT bị động).'),
])
put('bt4', [
    (S('is assigned'), 'HTĐ bị động, homework số ít → is assigned.'),
    (B(['was'], ['stolen']), 'QKĐ nghi vấn bị động: Why was the car stolen?'),
    (S('are spoken'), 'French and English số nhiều → are spoken.'),
    (B(['is'], ['stored']), 'How is information stored…? (information không đếm được).'),
    (S('will be paid'), 'I promise → tương lai đơn bị động: will be paid.'),
    (S('were examined'), 'Yesterday + applicants → were examined.'),
    (S('was punished'), 'QKĐ bị động: was punished.'),
    (S('was offered'), 'last month → was offered.'),
    (S('will be recommended'), 'I think… if… doesn\'t work → will be recommended.'),
    (S('is being repaired'), '"at the moment" → HTTD bị động: is being repaired.'),
])
_bo = ['bỏ', 'bo', 'bỏ be', 'delete', 'remove']
put('bt5', [
    (B(['is'], ['was']), 'Cả câu ở quá khứ (yesterday, went) → the food <b>was</b> well cooked.'),
    (B(['tidy'], ['tidied']), 'was painted and <b>tidied</b> up (V3 song song).'),
    (B(['inhale'], ['inhaled']), 'are exhaled… and <b>inhaled</b> (V3 song song).'),
    (B(['frightening'], ['frightened']), 'were all <b>frightened</b> by the loud noise (V3 bị động).'),
    (B(['make'], ['made']), 'will be <b>made</b> (V3).'),
    (B(['knew'], ['known']), 'best <b>known</b> for (V3).'),
    (B(['discourage'], ['discouraged']), 'will be <b>discouraged</b> (V3).'),
    (B(['be'], _bo), '"won\'t hang out" – thừa "be" (không phải bị động).'),
    (B(['was'], _bo), 'started to be built: "The complex started to be built" – thừa "was".'),
    (B(['extract'], ['extracted']), 'Are natural oils <b>extracted</b> … (V3).'),
])
put('bt6', [
    ('A', '"Maybe" + dự đoán → will not be repaired; B dùng khi có kế hoạch; C sai thì.'),
    ('B', 'in 2009 → QKĐ bị động: was launched.'),
    ('B', 'weekly on Fridays → thói quen: HTĐ bị động is maintained.'),
    ('B', 'in 1962 → was founded (found = thành lập → founded).'),
    ('C', 'yesterday afternoon → was postponed.'),
    ('A', '"As planned" → kế hoạch: is going to be held (khoá Word; will be held cũng đúng ngữ pháp).'),
])

# ============================================================ TỔNG HỢP NÂNG CAO
put('nc1', [
    (S('arrives'), 'Thời gian biểu (timetable) → hiện tại đơn: arrives.'),
    (S('are having', 'are going to have'), 'Kế hoạch đã sắp xếp → are going to have (khoá Word) / are having.'),
    (S('will snow', 'is going to snow'), 'Dự báo thời tiết → will snow / is going to snow.'),
    (S('am meeting', 'am going to meet'), 'Cuộc hẹn đã sắp xếp → am meeting / am going to meet.'),
    (S('is flying', 'is going to fly'), 'Lịch bay đã sắp xếp → is flying.'),
    (S('will drive'), 'Wait! – quyết định tức thời → will drive.'),
    (S('starts'), 'Thời khoá biểu → hiện tại đơn starts.'),
    (S('finish'), 'Câu điều kiện loại 1: If + hiện tại đơn → finish.'),
    (S('will open'), 'Đề nghị giúp → will open.'),
    (S('is going to rain'), 'Có bằng chứng (mây đen) → is going to rain.'),
])
put('nc2', [
    (S('was burgled'), 'QKĐ bị động: My house was burgled.'),
    (S('had been given'), 'QKHT bị động: before he had been given directions.'),
    (S('had been sold'), 'QKHT bị động: all the houses had been sold.'),
    (S('was still being built', 'was being built'), 'QKTD bị động: The hotel was still being built.'),
    (S('was sent'), 'QKĐ bị động: My son was sent home.'),
    (S('was prescribed'), 'prescribe + O gián tiếp: I was prescribed some medicine.'),
    (S("hasn't been fixed", 'has not been fixed'), 'HTHT phủ định bị động: My car hasn\'t been fixed yet.'),
    (S('had been demolished'), 'QKHT bị động: the house… had been demolished.'),
])
put('nc3', [
    (S('Money is collected by Tim', 'Money is collected'), 'HTĐ bị động: is collected by Tim.'),
    (S('The window was opened by Mai'), 'QKĐ bị động: was opened by Mai.'),
    (S('Our homework has been done', 'Our homework has been done by us'), 'HTHT bị động: has been done.'),
    (S('A question will be asked', 'A question will be asked by me'), 'Tương lai đơn bị động: will be asked.'),
    (S('The picture can be cut out', 'The picture can be cut out by him'), 'Modal bị động: can be cut out.'),
    (S('Our rooms are not cleaned', 'Our rooms are not cleaned by us'), 'HTĐ phủ định bị động: are not cleaned.'),
    (S('The car will not be repaired by David', 'The car will not be repaired'), 'will not be repaired by David.'),
    (S('Was this circle drawn by Sue'), 'QKĐ nghi vấn bị động: Was this circle drawn by Sue?'),
])
put('nc4', [
    (S('was given'), 'QKĐ bị động: The Statue of Liberty was given to the US by France.'),
    (S('was'), 'It was a present (QKĐ).'),
    (S('was designed'), 'QKĐ bị động: was designed by…'),
    (S('was completed'), 'QKĐ bị động: was completed in July 1884.'),
    (S('was shipped'), 'QKĐ bị động: was shipped to New York.'),
    (S('arrived'), 'arrive là nội động từ → QKĐ chủ động: arrived.'),
    (S('were put'), 'The pieces (số nhiều) were put together.'),
    (S('took'), 'take place (chủ động, QKĐ): took.'),
    (S('is'), 'Sự thật hiện tại: is 46m high.'),
    (S('represents'), 'Sự thật hiện tại, chủ động: represents.'),
    (S('holds'), 'She holds a torch (HTĐ chủ động).'),
    (S('is visited'), 'Every year… by millions of people → HTĐ bị động: is visited.'),
])

# ============================================================ ĐỌC – TEST 1
put('dr1', [
    ('A', 'Câu đầu: "Most people relate stress to physical symptoms like an upset stomach or headaches."'),
    ('B', 'Thông tin tiêu cực được nhận biết "more easily and quickly" → thông tin tích cực cần <b>more time</b>.'),
    ('C', 'Negative stimuli produce more neural activity than equally intense positive ones → positive things produce less.'),
    ('C', 'Cả bài nói bad events có tác động mạnh hơn good ones.'),
])
put('dr2', [
    ('T', 'Chúng ta nhớ điều tiêu cực rõ hơn điều tích cực → điều tích cực dễ bị quên hơn.'),
    ('F', 'Bài nói: "The brain handles positive and negative information in different parts."'),
    ('NG', 'Bài nói chúng ta ruminate về chuyện xấu, nhưng không nói gì về việc cố quên.'),
    ('NG', 'Bài không nhắc positive thoughts bảo vệ khỏi stress.'),
    ('T', '"a basic and wide-ranging principle of psychology".'),
])
put('dr3', [
    ('B', 'Rick Hanson: little experiment with twenty people.'),
    ('A', 'Clifford Nass: "use stronger words to describe them than happy ones".'),
    ('C', 'Baumeister: losing your dream job, breaking up… (ví dụ cụ thể).'),
    ('C', 'Baumeister co-authored a journal article in 2001.'),
])
put('dr4', [
    ('D', 'The <b>result</b> is that… (kết quả là).'),
    ('A', 'complain <b>if</b> they don\'t like the music.'),
    ('B', 'One <b>answer</b> to this problem (giải pháp cho vấn đề).'),
    ('D', 'has just been <b>designed</b> by an engineer.'),
    ('D', 'a hollow <b>space</b> under the seat.'),
    ('C', 'the exact <b>source</b> from which low sounds come.'),
    ('C', 'it doesn\'t <b>matter</b> that… (không quan trọng).'),
    ('C', '<b>Consequently</b> = do đó (kết quả của việc âm thanh đi quãng ngắn).'),
    ('D', 'to <b>disturb</b> others = làm phiền người khác.'),
    ('B', 'Most of the sound is <b>absorbed</b> by the listeners.'),
])

# ============================================================ VIẾT – TEST 1
put('vt1', [
    ('A', 'so… that = too… for sb to do: too full for us to get in.'),
    ('C', 'I wish + QKHT = hối tiếc vì đã không chọn tiếng Anh.'),
    ('D', 'last longer than = don\'t last as long as.'),
    ('A', 'interest sb more than = more interesting than (tính từ -ing cho vật).'),
    ('C', 'did not allow to leave = made the class stay (make + O + V nguyên).'),
    ('D', 'suggest (that) + S + V nguyên (should).'),
    ('A', 'It was only when… that… (câu nhấn mạnh).'),
    ('C', 'find it difficult to get up early = isn\'t used to getting up early.'),
    ('B', 'when I was staying… = during my stay.'),
    ('D', 'Do shops stay open…? = Is it usual for shops to stay open…?'),
])
put_open('vt2', [
    'Bài mẫu tự soạn (Word không có đáp án): Dear Jack, Thank you for your letter. Before an important interview you should eat a light and balanced meal. Foods rich in whole grains, such as oatmeal, give you steady energy, and fruit, nuts and yoghurt help you stay calm and focused. Fish and eggs are good for your brain. You should avoid heavy, oily or very spicy food, too much sugar and caffeine because they can make you nervous or sleepy. Remember to drink plenty of water and get a good night\'s sleep. Good luck with your interview! Best wishes, Dr. Glenn.',
])
put('vt3', [
    (S('I had gone on holiday with my class last week'), 'It\'s a pity… (hiện tại tiếc nuối quá khứ) → I wish + QKHT: <b>I wish I had gone</b>…'),
    (S('have got lost in the woods if we had brought a compass', 'have gotten lost in the woods if we had brought a compass', 'have been lost in the woods if we had brought a compass'), 'Điều kiện loại 3: wouldn\'t have got lost if we had brought a compass.'),
    (S('coke to lemonade'), 'enjoy A more than B = prefer A <b>to</b> B.'),
    (S('many shirts as Jenny'), 'the same number of = as <b>many</b> … as.'),
    (S('go to the party with her boyfriend tonight'), 'It is possible that = may + V.'),
    (S('have been directed by Steven Spielberg'), 'HTHT bị động: have been directed by…'),
    (S('to have her hair cut'), 'need V-ing = need to have sth done (nhờ làm).'),
    (S('the bank clerk to give him all the money'), 'make sb V → force sb <b>to V</b>.'),
    (S('he would help me to repair my motorbike the following day', 'he would help me repair my motorbike the next day', 'that he would help me to repair my motorbike the following day', 'that he would help me repair my motorbike the next day', 'he would help me to repair my motorbike the next day'), 'Câu tường thuật: will → would; tomorrow → the following day / the next day.'),
    (S('a cold, Jimmy still wants to take part in the football match', 'a cold Jimmy still wants to take part in the football match'), 'Despite + V-ing / N, mệnh đề: Despite having a cold, Jimmy still wants…'),
])

# ============================================================ TỪ VỰNG – NGỮ PHÁP TEST 2
put('gt1', [
    ('A', 'put off + V-ing = trì hoãn.'),
    ('C', 'blame sb for sth = đổ lỗi cho ai về việc gì.'),
    ('B', 'the Internet (duy nhất) ; a means of… (một phương tiện).'),
    ('C', 'her car is being serviced = xe đang được bảo dưỡng.'),
    ('A', 'make a habit of = tạo thói quen.'),
    ('C', 'drop out of college = bỏ học đại học.'),
    ('D', 'get on one\'s nerves = làm ai bực mình.'),
    ('C', 'Đảo ngữ với cụm giới từ chỉ nơi chốn: On the table <b>lay the disks</b>.'),
    ('D', 'look like → hỏi "what … looked like".'),
    ('C', 'safe from bankruptcy = an toàn khỏi phá sản.'),
    ('B', 'none (of the girls)… = không ai trong số các nam giỏi bằng các nữ.'),
    ('C', 'is reported to have been robbed (hành động xảy ra trước).'),
    ('A', 'advantages over <b>that</b> made of… (that thay cho clothing – danh từ không đếm được).'),
    ('C', 'Đảo ngữ điều kiện: were further rioting to occur = if further rioting were to occur.'),
    ('B', 'Now that + mệnh đề = vì bây giờ (đã).'),
    ('D', 'I\'m all ears = tôi đang chăm chú nghe.'),
    ('C', 'If only + would + V (mong muốn về hành vi của người khác).'),
    ('D', 'give way to one\'s anger = để cơn giận chi phối.'),
    ('C', 'on the grounds that = với lí do là.'),
    ('B', 'Hard as he worked = Although he worked hard (đảo ngữ nhượng bộ).'),
    ('A', 'That + mệnh đề làm chủ ngữ: That Philip Glass is more interested… is apparent.'),
    ('D', 'Although (it is) invisible… (rút gọn mệnh đề nhượng bộ).'),
    ('C', 'didn\'t need to break in (không cần phá cửa vì cửa mở – chưa chắc đã làm). needn\'t have broken = đã phá nhưng không cần; ngữ cảnh "they just walked in" → didn\'t need to.'),
    ('A', 'Đồng ý hoàn toàn: There is no doubt about it.'),
    ('A', 'Từ chối lịch sự: I\'d rather you didn\'t. It\'s stuffy.'),
])
put('gt2', [
    (S("didn't wear", 'did not wear'), 'would rather + S + V quá khứ (hiện tại) → didn\'t wear.'),
    (S('stolen'), 'Mệnh đề quan hệ rút gọn bị động: The money stolen in the robbery.'),
    (S('will have been finished'), 'by the end of 2018 → tương lai hoàn thành bị động.'),
    (S('should have informed', 'ought to have informed'), 'It was our fault → should have + V3.'),
    (B(['Have'], ['been working']), 'You look tired → Have you been working hard? (HTHT tiếp diễn).'),
    (S('was wearing'), 'Hành động đang diễn ra tại một thời điểm quá khứ → was wearing.'),
    (S('being given'), 'remember + V-ing (nhớ đã làm) bị động: being given.'),
    (S('leave', 'should leave'), 'It was urgent that + S + (should) V nguyên.'),
    (S("couldn't have stolen", 'could not have stolen', "can't have stolen"), 'Suy đoán chắc chắn trong quá khứ: couldn\'t have stolen.'),
    (S('playing'), 'while + V-ing (rút gọn mệnh đề cùng chủ ngữ).'),
])
put('gt3', [
    (S('traditionally'), 'trạng từ bổ nghĩa cho "used".'),
    (S('valuable'), 'a valuable medicine (tính từ).'),
    (S('professionals'), 'danh từ chỉ người số nhiều: professionals.'),
    (S('surprising'), 'quite surprising (tính từ -ing).'),
    (S('illnesses'), 'various + danh từ số nhiều: illnesses.'),
    (S('disadvantage'), 'The main disadvantage = bất lợi chính, vì sau đó nói về hơi thở hôi (khoá Word gõ sai "disadvnatage").'),
    (S('breath'), 'bad breath = hơi thở hôi.'),
    (S('minimize', 'minimise'), 'helps + V nguyên: minimize the smell.'),
    (S('seriously'), 'take sth seriously = coi trọng.'),
    (S('favorite', 'favourite'), 'your favorite dishes.'),
])
put('gt4', [
    (B(['industrialize'], ['industrialization', 'industrialisation']), 'in the process of + danh từ → industrialization.'),
    (B(['underpopulation'], ['overpopulation']), 'Thành phố đông đúc → overpopulation (dân số quá đông).'),
    (B(['great'], ['large', 'huge', 'vast']), 'a large number of people (khoá Word: Large).'),
    (B(['in'], ['from']), 'the drift of people from the rural areas (di cư khỏi nông thôn).'),
    (B(['make'], ['to make']), 'The only solution is to make life… (to V).'),
    (B(['attractively'], ['attractive']), 'make life more attractive (tính từ).'),
    (B(['here'], ['there']), 'stay there (ở lại nông thôn đã nhắc đến).'),
    (B(['to'], ['for']), 'incentives for people.'),
    (B(['so as'], ['such as']), 'facilities such as transportation… (ví dụ).'),
    (B(['educational'], ['education']), 'danh từ song song: transportation, health, and education services.'),
])

# ============================================================ ĐỌC – TEST 2
put('dt1', [
    (['A', 'D'], 'sports started/appeared in Europe or the USA in the 19th century (khoá Word: A).'),
    ('D', 'the <b>way</b> people lived = cách sống.'),
    ('C', 'no <b>regular</b> time off = không có thời gian nghỉ cố định.'),
    ('A', 'found themselves with regular free time.'),
    ('C', 'more leisure time than <b>ever</b> before.'),
    ('D', 'result <b>in</b> sth = dẫn đến.'),
    ('B', 'take sides = đứng về một phe.'),
    ('A', 'The <b>recent</b> explosion in TV = sự bùng nổ gần đây.'),
    ('D', 'an increase in <b>demand</b> for = tăng nhu cầu về.'),
    ('C', 'The money… <b>means</b> that… (có nghĩa là).'),
])
put('dt2', [
    (S('before'), 'wandered… before finally settling down.'),
    (S('where'), 'Australia, <b>where</b> he was trained (mệnh đề quan hệ nơi chốn).'),
    (S('question'), 'out of the <b>question</b> = không thể.'),
    (S('made'), 'His retirement suddenly <b>made</b> him realize…'),
    (S('take'), 'take up a hobby = bắt đầu một sở thích.'),
    (S('with'), 'radio contact <b>with</b> other radio amateurs.'),
    (S('whom'), 'with <b>whom</b> he had much in common.'),
    (S('loss'), 'at a <b>loss</b> for words = không nói nên lời.'),
    (S('in'), 'fill <b>in</b> the details = điền, bổ sung chi tiết.'),
    (S('be'), 'flew to California to <b>be</b> reunited with his brother.'),
])
put('dt3', [
    ('B', 'Bài nói về những yếu tố làm Winterthur trở thành một bảo tàng khác thường.'),
    ('D', 'devoted to ≈ specializing in (chuyên về).'),
    ('C', 'extensive renovations = tu sửa lớn → the house was repaired.'),
    ('B', 'Ấn tượng ngôi nhà đang có người ở → không giống bảo tàng thông thường.'),
    ('C', 'assembled = gom lại → brought together.'),
    ('A', 'renovations made to it → it = Winterthur Museum (the house).'),
    ('D', 'developing concepts = những quan niệm đang tiến triển → evolving.'),
    ('D', 'Đoạn 2: related by style, date, place of manufacture – không có past ownership.'),
    ('A', 'Đoạn 2 giải thích khái niệm "period room" đã nhắc ở đoạn 1.'),
])

# ============================================================ VIẾT – TEST 2
_dogs = []
for _a in ['are thought', 'are believed', 'are said', 'are considered']:
    for _b in ['evolved', 'descended']:
        _dogs.append('%s to have %s from wolves' % (_a, _b))
put('vw1', [
    (S('took any notice of my protests', 'took notice of my protests', 'paid any attention to my protests', 'took any notice of my protest'), 'Nobody + V chủ động: took any notice of my protests (take notice of = để ý đến).'),
    (S('as no surprise to me to hear that Harry had failed his driving test', 'as no surprise to me to hear that Harry failed his driving test', 'as no surprise to me that Harry had failed his driving test', 'as no surprise to me that Harry failed his driving test'), 'It came as no surprise to me to hear that Harry had failed his driving test.'),
    (S("hadn't been for the fog, there wouldn't have been a traffic problem", "hadn't been for the fog, there wouldn't have been any traffic problem", "hadn't been for the fog, there wouldn't have been traffic problems", "hadn't been for the fog, there wouldn't have been the traffic problem", "hadn't been for the fog, the traffic problem wouldn't have happened"), 'Điều kiện loại 3: If it hadn\'t been for the fog, there wouldn\'t have been a traffic problem.'),
    (S("hasn't been confirmed yet", "hasn't been confirmed", 'has not been confirmed yet'), 'HTHT bị động: Our hotel booking hasn\'t been confirmed yet.'),
    (S('leave her anything in his will', 'leave her anything in the will', 'leave anything to her in his will'), 'Her uncle didn\'t leave her anything in his will (khoá Word: leave her anything in his will).'),
    (S('to looking after handicapped people', 'to looking after the handicapped', 'to looking after disabled people'), 'be devoted/dedicated to + V-ing (khoá Word: to looking after handicapped people).'),
    (S('does Nicky run a successful company, but she also manages to look after her four children', 'does Nicky run a successful company but also manages to look after her four children', 'does Nicky run a successful company, but she also manages to look after her four kids'), 'Not only + trợ động từ đảo: Not only <b>does Nicky run</b> a successful company, but she also manages…'),
    (None, 'Đáp án mẫu (tự soạn – khoá Word chỉ có "having witnessed the crime"): He denied having witnessed the crime as he had been a long way from the scene at the time.'),
    (S('everything but the television', 'everything except the television', 'everything except for the television', 'everything but the TV', 'everything apart from the television'), 'The only thing they didn\'t steal = They stole everything but/except the television.'),
    (S(*_dogs), 'Experts think… → All dogs are thought/believed/said to have evolved/descended from wolves.'),
])
del ANS['vw1.8']
put('vw2', [
    (S("I'll lend you the money as long as you pay it back next week", "I'll lend you the money so long as you pay it back next week", 'I will lend you the money as long as you pay it back next week', 'I will lend you the money so long as you pay it back next week'), 'on condition that = as/so long as.'),
    (S('Bill was on the verge of speeding when he saw the patrolman'), 'be about to = be on the verge of + V-ing.'),
    (S('I have got to finish this homework tonight', "I've got to finish this homework tonight"), 'It is necessary for me to = I have got to.'),
    (S('She was taken for a ride when she sold the jewelry at such a low price', 'She was taken for a ride when she sold the jewellery at such a low price'), 'take sb for a ride = lừa ai (cheated).'),
    (S('They arrived at their destination safe and sound'), 'safe and sound = bình an vô sự (alive and kicking).'),
    (S("The telephonist was to blame for the fact that they didn't get the message", 'The telephonist was to blame for their not getting the message', 'The telephonist was to blame for them not getting the message', 'The telephonist was to blame for the fact that they did not get the message'), 'be to blame for = chịu trách nhiệm/lỗi về.'),
    (S('The disagreement is a storm in a teacup'), 'a storm in a teacup = chuyện bé xé ra to.'),
    (S('Defence alliances are as old as the hills'), 'as old as the hills = rất cũ, xưa như trái đất.'),
    (S("They couldn't reach a decision on where to go on holiday", "They couldn't reach a decision about where to go on holiday", 'They could not reach a decision on where to go on holiday', 'They could not reach a decision about where to go on holiday'), 'reach a decision = đi đến quyết định.'),
    (S('I should have been told about these changes earlier'), 'Phàn nàn quá khứ: should have been told (bị động).'),
])

# ============================================================ KIỂM TRA (Test 3 – 140 câu)
put('kt', [
    ('D', '<b>sugar</b> /ˈʃʊɡə/: g = /ɡ/. allergy, digest, oxygen có g = /dʒ/.'),
    ('D', '<b>heart</b> /hɑːt/ (ea = /ɑː/). breath, head, health có ea = /e/.'),
    ('A', '<b>among</b> /əˈmʌŋ/ (o = /ʌ/). belong, body, strong có o = /ɒ/.'),
    ('D', '<b>stomach</b> /ˈstʌmək/ (ch = /k/). approach, children, chocolate có ch = /tʃ/.'),
    ('A', '<b>intestine</b> /ɪnˈtestɪn/ (i = /ɪ/). mind, spine, reliable có i = /aɪ/.'),
    # Exercise 2: trọng âm (6-10)
    ('B', '<b>disease</b> nhấn âm 2. ailment, poultry, nervous nhấn âm 1.'),
    ('D', '<b>evidence</b> nhấn âm 1. digestive, intestine, condition nhấn âm 2.'),
    ('A', '<b>internal</b> nhấn âm 2. skeletal, therapy, willpower nhấn âm 1.'),
    ('D', '<b>scientific</b> nhấn âm 3. alternative, bacteria, respiratory nhấn âm 2.'),
    ('A', '<b>acupuncturist</b> nhấn âm 1. circulatory, ineffectively, vegetarian nhấn âm 3 (hoặc 4).'),
    # Exercise 3: từ vựng (11-28)
    ('C', 'Điều khiển cơ thể, do não và dây thần kinh → <b>nervous</b> system (hệ thần kinh).'),
    ('B', 'Phân giải thức ăn thành năng lượng → <b>Digestive</b> system (tiêu hoá).'),
    ('A', 'Skeletal system gồm các <b>bones</b> (xương).'),
    ('B', 'Bơm máu mang oxy tới từng tế bào → <b>heart</b> (tim).'),
    ('D', 'Hít oxy, thải CO2 → <b>respiratory</b> system.'),
    ('A', 'a healthy <b>balance</b> between work and play = sự cân bằng.'),
    ('D', '<b>take</b> a nap = ngủ một giấc ngắn.'),
    ('C', '<b>staying</b> up late = thức khuya.'),
    ('C', '<b>kick</b> a bad habit = bỏ thói quen xấu.'),
    ('C', 'Hít sâu → <b>lungs</b> (phổi) nở ra gấp đôi.'),
    ('D', '<b>spoil</b> your breath = làm hơi thở có mùi (khoá Word).'),
    ('C', '<b>make up</b> half of… = chiếm một nửa (make up of sai ngữ pháp).'),
    ('D', 'Another name for the backbone = <b>spine</b>.'),
    ('B', 'an <b>imbalance</b> of yin and yang = mất cân bằng âm dương.'),
    ('C', 'endurance, <b>strength</b> and flexibility (danh từ song song).'),
    ('D', 'strongly <b>stimulate</b> the body = kích thích mạnh cơ thể.'),
    ('D', 'cut people\'s <b>risk</b> of heart disease = giảm nguy cơ.'),
    ('C', '<b>insert</b> needles = cắm kim.'),
    # Exercise 4: đồng nghĩa (29-42)
    ('A', 'originate ≈ <b>begin</b> (bắt nguồn).'),
    ('C', 'evidence ≈ <b>proof</b> (bằng chứng).'),
    ('B', 'ailments ≈ <b>diseases</b> (bệnh tật).'),
    (['C', 'D'], 'cure ≈ <b>treatment</b> (khoá Word) / therapy cũng gần nghĩa.'),
    ('C', 'ease nausea ≈ <b>reduce</b> (làm giảm).'),
    ('A', 'alternatives ≈ <b>choices</b> (lựa chọn).'),
    ('C', 'eliminated ≈ <b>removed</b> (loại bỏ).'),
    ('A', 'conscious of ≈ <b>aware of</b> (nhận thức).'),
    ('A', 'stimulate ≈ <b>encourage</b> (kích thích, khuyến khích).'),
    ('D', 'side effects = tác dụng phụ → "side" ≈ <b>unwanted</b>.'),
    ('A', 'consuming ≈ <b>eating</b> (ăn).'),
    ('A', 'prevent ≈ <b>avoid</b> (phòng tránh).'),
    ('B', 'contains ≈ <b>comprises</b> (gồm có).'),
    ('A', 'heal ≈ <b>cure</b> (chữa lành).'),
    # Exercise 5: trái nghĩa (43-50)
    ('D', 'expelling (thở ra) >< <b>inhaling</b> (hít vào).'),
    ('C', 'boosting (tăng cường) >< <b>weakening</b> (làm yếu).'),
    ('B', 'work (có tác dụng) >< <b>be ineffective</b> (không hiệu quả).'),
    ('B', 'promotes (thúc đẩy) >< <b>discourages</b> (ngăn cản).'),
    ('A', 'increased >< <b>reduced</b>.'),
    ('B', 'safe >< <b>dangerous</b>.'),
    ('D', 'compound (phức hợp) >< <b>single</b> (đơn lẻ, như isolation exercises).'),
    ('A', 'inner (bên trong) >< <b>external</b> (bên ngoài).'),
    # Exercise 6: ngữ pháp (51-76)
    ('D', 'Quyết định tức thời khi nghe có người gõ cửa → <b>will open</b>.'),
    ('B', 'Có bằng chứng (mây đen) → <b>is going to rain</b>.'),
    ('C', 'Lời yêu cầu lịch sự → <b>Will you open</b> the window, please?'),
    ('D', 'won\'t go away = (sẽ) không hết (dự đoán/từ chối).'),
    (['B', 'C'], 'Cuộc hẹn đã sắp xếp lúc 8 giờ Chủ Nhật → am going to meet (khoá Word) / will be meeting.'),
    ('D', 'Wait! → quyết định tức thời → <b>will drive</b>.'),
    ('C', '"as planned" → kế hoạch → <b>am going to see</b>.'),
    ('D', 'Perhaps + will: <b>will visit</b>.'),
    (['A', 'C'], 'Hỏi kế hoạch → are you going to leave (khoá Word); will you leave cũng đúng.'),
    (['A', 'C'], 'Who will win the next World Cup? (dự đoán, khoá Word C); is going to win cũng được.'),
    ('B', 'Đã có vé miễn phí, đã sắp xếp → <b>is going</b> (HTTD cho kế hoạch).'),
    ('B', '"already bought a train ticket" → kế hoạch → <b>am going to visit</b>.'),
    (['C', 'D'], 'Cảnh báo, có bằng chứng → is going to bite / will bite (khoá Word D).'),
    ('A', 'It is suggested that… (bị động).'),
    ('B', 'Foods are broken down… (bị động của break down; broken – V3).'),
    ('D', 'was born (bị động) on 8 January, 1942.'),
    ('D', 'Was that book written by your father? (QKĐ bị động nghi vấn).'),
    ('A', 'has been used (HTHT bị động) for thousands of years.'),
    ('A', 'since 1985 → HTHT chủ động: hasn\'t taught.'),
    ('B', 'will be used (bị động sau will).'),
    ('C', 'The teacher punished the student → chủ động (the student là tân ngữ).'),
    ('C', 'As the patient could not walk → he <b>was carried</b> home (bị động).'),
    ('C', 'The injured (số nhiều) were taken to the hospital.'),
    ('B', 'It is believed that…'),
    ('C', 'Most studies <b>have shown</b> (chủ động, HTHT).'),
    ('D', 'may not <b>be recommended</b> (bị động sau modal).'),
    # Exercise 7: tìm lỗi (77-90)
    ('A', '<b>Despite of</b> sai → Despite / In spite of.'),
    ('D', 'Có bằng chứng (mây đen) → <b>is going to rain</b>, không dùng will rain.'),
    ('C', 'one of the oldest medical <b>treatments</b> (danh từ số nhiều).'),
    ('B', 'Many accidents <b>are</b> caused (chủ ngữ số nhiều).'),
    ('A', '<b>was gave</b> → was given.'),
    ('B', 'Measles <b>is</b> (danh từ số ít, tên bệnh).'),
    ('A', 'often dismiss → are often <b>dismissed</b> (bị động).'),
    ('C', 'harmony <b>between</b> human and the world (giữa hai đối tượng).'),
    ('A', 'Human infants <b>are born</b> (bị động).'),
    ('C', 'is helped → <b>helps</b> (chủ động: acupuncture helps with side effects).'),
    ('B', 'is believed <b>to be cured / to have been cured</b> (to cured sai).'),
    ('B', 'It <b>is also called</b> (bị động).'),
    ('A', 'You can <b>put</b> yourself at risk (be put sai).'),
    ('C', 'is compared → <b>compared</b> (rút gọn quá khứ phân từ).'),
    # Exercise 8: giao tiếp (91-105)
    ('C', 'Bác sĩ hỏi "What can I do for you?" → bệnh nhân nêu triệu chứng: I have got a bad cough.'),
    ('C', 'Phản ứng ngạc nhiên về thông tin: That\'s incredible.'),
    ('B', 'How long → For a week (khoảng thời gian).'),
    ('D', 'Can I listen to your chest? → Of course.'),
    ('A', 'Trấn an bệnh nhân: Don\'t worry.'),
    ('C', 'How shall I take it? → Take it twice per day.'),
    ('C', 'Is the surgery a major one? → Yes, it is.'),
    ('C', 'Trả lời "You\'ll be given painkillers" → hỏi Will it be painful afterwards?'),
    ('C', 'How much → £35.'),
    ('B', 'How are you coming → By bus or car (phương tiện).'),
    ('C', 'Do you think you\'ll get better? → Well, I hope so.'),
    ('C', 'Đồng ý với câu phủ định: Neither do I.'),
    ('D', 'Have you had a flu shot…? → No, not in the last few years.'),
    ('A', 'When did the pain start? → About 2 weeks ago.'),
    ('A', 'Nhận giấy chứng nhận → Thank you.'),
    # Exercise 9: cloze GOOD HEALTH (106-117)
    ('C', 'a state <b>where</b> you are free from sickness (mệnh đề quan hệ chỉ trạng thái).'),
    ('C', '<b>Despite</b> this = mặc dù điều này.'),
    ('B', 'People used to think of their health <b>when</b> they were sick.'),
    ('B', '<b>make</b> sure = đảm bảo.'),
    ('D', 'in <b>the first</b> place = ngay từ đầu.'),
    ('D', 'how <b>much</b> is enough?'),
    ('B', 'simple things <b>like</b> cleaning the house.'),
    ('B', '<b>for</b> instance = ví dụ.'),
    ('B', '<b>any</b> kind of exercise is good (bất kỳ).'),
    ('D', 'should <b>be eaten</b> (bị động sau should).'),
    ('B', 'Fiber helps your body <b>digest</b> the food.'),
    ('C', 'in <b>other</b> ways = theo những cách khác.'),
    # Exercise 10 (118-122)
    ('C', 'We forget about 80% of the medical information → thông tin bác sĩ đưa ra phần lớn bị quên.'),
    ('D', 'complicated (phức tạp) >< <b>simple</b>.'),
    ('C', 'we are more likely to focus on the diagnosis rather than the treatment → chỉ muốn biết mình bị gì.'),
    ('D', 'absorb ≈ <b>take in</b> (tiếp thu).'),
    ('B', 'record the consultation → replay at home to understand better.'),
    # Exercise 11 (123-130)
    ('B', 'Bài chủ yếu khuyên bắt đầu bằng chạy bộ nhẹ nhàng → <b>Gentle jogging</b>.'),
    ('D', 'Typically, people who buy them use them for a week or so and then forget about them.'),
    ('B', 'determined ≈ <b>decisive</b> (kiên quyết).'),
    ('B', 'It\'s always best to get expert advice, and the best place is a sports shop → mua giày chất lượng ở cửa hàng thể thao.'),
    ('D', 'injury ≈ <b>suffering</b> (khoá Word).'),
    ('D', 'somebody who exercises twice as hard doesn\'t automatically become twice as fit.'),
    ('C', 'gently >< <b>rapidly</b>.'),
    ('A', '<b>that</b> = a mixture of walking and running.'),
    # Exercise 12 (131-136)
    ('A', 'This surprises me = I am surprised by this (HTĐ).'),
    ('B', 'were interviewing → was being interviewed (QKTD bị động).'),
    ('B', 'may + be + V3 → may be forgotten.'),
    ('D', 'should have + been + V3 → should have been done.'),
    ('B', 'understands (HTĐ) → is understood.'),
    ('B', 'The doctor told him… → He was told by the doctor… (QKĐ bị động).'),
    # Exercise 13 (137-140)
    ('A', 'Rút gọn hợp lí: Protein in meats and foods which is consumed helps us…'),
    ('B', 'It doesn\'t matter if you are not fit = no matter how fit you are.'),
    ('D', '<b>Since</b> + mệnh đề (vì) – visible results will be brought by days.'),
    ('A', '<b>Because of</b> + cụm danh từ: Because of low fatty acid…'),
])
