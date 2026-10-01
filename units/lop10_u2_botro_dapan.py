# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Unit 2 Humans and the environment (Tiếng Anh 10 Global Success) – Bộ BÀI TẬP BỔ TRỢ.
Quy ước:
  mcq  : chữ cái 'A'-'D' (list nếu nhiều đáp án chấp nhận)      tf : 'T' / 'F'
  fill : danh sách đáp án chấp nhận (1 ô)
  open : không chấm điểm, EXPLANATIONS chứa đáp án mẫu
Đáp án lấy từ khoá tô màu trong nửa sau file Word (src/l10u2/bt_c.txt), sau đó tự giải độc lập để đối chiếu.
Khoá Word trùng bản tự giải ở mọi câu có tô màu; các điểm nghi vấn / chỗ khoá thiếu ghi ở GHI_CHU_RA_SOAT."""

GHI_CHU_RA_SOAT = [
    'Nguồn: E3 và E4 ("Choose the words or phrases from the box") có hộp từ nằm trong textbox của Word; đã đưa vào "bank" của từng nhóm. E3 có 8 từ: energy, eco-friendly, organic, adopt, household appliance, raise, meet, reduce; E4: protect, plastic, organic, set up, eco-friendly, household, awareness, drop.',
    'vg1.1 (E3 Q1): khoá Word gõ sai "roducts" (đề là "products"); đáp án chấp nhận "eco-friendly", "eco - friendly", "eco friendly".',
    'E5 (vg3, chuyển bị động): đáp án chấp nhận cả hai vị trí của trạng ngữ và có/không "by + tác nhân"; chấp nhận chính tả Anh/Mỹ (organise/organize, neighbourhood/neighborhood). Giáo viên nên xem lại các bài làm lệch dạng.',
    'vg4 (E6): khoá Word KHÔNG tô đáp án ở Q3, Q5, Q13 (và dòng Q15, Q16 có ký tự trống thừa). Tự giải: Q3 = B (responsible for), Q5 = C (is being repaired), Q13 = A (will be built).',
    'vg4.11 và vg4.15 (E6 Q11, Q15): hai câu gần như trùng nhau trong đề gốc (Switching to energy-saving light bulb); giữ nguyên cả hai.',
    'vg4.18 (E6 Q18): đề gốc thiếu dấu chấm cuối câu; đã thêm.',
    'vg4.25 (E6 Q25): nguồn gõ "…the window. please?" -> đã sửa "______ the window, please?"; dấu nháy ‘ và “ lỗi được chuẩn lại.',
    'vg4.30 (E6 Q30): khoá Word = D (won\'t go). "the headache isn\'t going away" (A) cũng đúng ngữ pháp và tự nhiên (hiện tại tiếp diễn chỉ tình trạng đang kéo dài) -> ANS = [D, A].',
    'vg4.31 (E6 Q31): khoá Word = B (am going to meet – kế hoạch). "will be meeting" (C, tương lai tiếp diễn tại thời điểm 8 giờ Chủ nhật) cũng đúng ngữ pháp nhưng ngoài phạm vi bài học -> ANS = [B, C].',
    'vg4.35, vg4.36 (E6 Q35, Q36): khoá Word B và C; giữ nguyên. Q35 "do you leave" chỉ dùng cho lịch trình cố định; Q36 "is going to win" cần có dấu hiệu ở hiện tại nên chọn will win.',
    'vg4.41 (E6 Q41): "The teacher ______ the student for lying" – khoá Word = C (punished) vì giáo viên là người thực hiện hành động (chủ động). Các câu A, B, D là bị động nên sai.',
    'ph1.1: produce (động từ) /prəˈdjuːs/ có o = /ə/; adopt /əˈdɒpt/ có o = /ɒ/ -> A. (nếu đọc danh từ produce /ˈprɒdjuːs/ thì câu không còn đáp án duy nhất).',
    'ph2.7: refillable /ˌriːˈfɪləbl/ có trọng âm chính ở âm 2 (/ˈfɪl/), khoá Word C (regularly) đúng.',
    'Từ vựng (theory): sửa phiên âm sai trong nguồn: Attend (copy nhầm của Atmosphere) -> /əˈtend/; Polluted -> /pəˈluːtɪd/; Turn off -> /tɜːn ɒf/.',
    'Lý thuyết: sơ đồ chuyển chủ động -> bị động (ảnh image1 của Word) được dựng lại thành bảng HTML; sửa lỗi gõ "FANT" -> "faint".',
    'li1 (Nghe): Word Unit 2 bổ trợ KHÔNG có file mp3 nên trang "Nghe" không có audio; giữ 8 câu T/F, kèm audio script gấp lại trong phần đề. Khoá T/F trong Word là dấu x trong bảng: 1T 2F 3F 4T 5T 6F 7T 8F; đối chiếu script đều khớp (Harry chơi bóng "every week", không phải every day; Carlos đang rất bận).',
    're1 (E7): nguồn gõ "plastic- tree shops" -> "plastic-free shops". Khoá Word C/C/C/A/A trùng bản tự giải.',
    're2 (E8): nguồn gõ "at no they cost" -> "at no cost". Khoá Word B/A/D/A/C/D/D/A trùng bản tự giải.',
    'sp1 (Nói) và wr2 (Viết đoạn văn): dạng tự luận, chỉ có bài mẫu; wr2 nguồn có ký tự rác "footprin{Firstly" đã sửa.',
    'wr1 (E10): đáp án chấp nhận nhiều cách viết (your/our/the carbon footprint, in/around the world…); giáo viên nên xem lại các bài làm lệch dạng.',
    'Ảnh trong Word: image2–image6 chỉ là biểu tượng nhỏ (<1KB) trang trí, không phải hình minh hoạ đề bài nên không đưa vào bài. Word bộ này không có đề kiểm tra riêng nên không có trang "kiem-tra".',
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


def variants(items):
    """thêm biến thể chính tả Anh/Mỹ cho đáp án điền."""
    out = []
    for s in items:
        for t in (s, s.replace('organised', 'organized').replace('neighbourhood', 'neighborhood')):
            if t not in out:
                out.append(t)
    return out


def combos(parts):
    res = ['']
    for p in parts:
        opts = p if isinstance(p, list) else [p]
        res = [(r + ' ' + o).strip() for r in res for o in opts]
    return res


# ======================= PHÁT ÂM (E1), TRỌNG ÂM (E2) =======================
put('ph1', [
    ('A', '<b>adopt</b> /əˈdɒpt/ (o = /ɒ/). protect /prəˈtekt/, carbon /ˈkɑːbən/, produce /prəˈdjuːs/ có o = /ə/.'),
    ('A', '<b>product</b> /ˈprɒdʌkt/ (o = /ɒ/). local /ˈləʊkl/, promote /prəˈməʊt/, stolen /ˈstəʊlən/ có o = /əʊ/.'),
    ('C', '<b>government</b> /ˈɡʌvənmənt/ (g = /ɡ/). energy /ˈenədʒi/, generate /ˈdʒenəreɪt/, emergency /ɪˈmɜːdʒənsi/ có g = /dʒ/.'),
    ('D', '<b>electricity</b> /ɪˌlekˈtrɪsəti/ (i = /ɪ/). financial /faɪˈnænʃl/, appliance /əˈplaɪəns/, environment /ɪnˈvaɪrənmənt/ có i = /aɪ/.'),
    ('B', '<b>expensive</b> /ɪkˈspensɪv/ (e = /ɪ/). access /ˈækses/, entertain /ˌentəˈteɪn/, effect /ɪˈfekt/ có chữ e được gạch chân đọc /e/.'),
])

put('ph2', [
    ('B', '<b>eco-friendly</b> /ˈiːkəʊ ˈfrendli/ nhấn âm 1. sustainable /səˈsteɪnəbl/, environment /ɪnˈvaɪrənmənt/, impossible /ɪmˈpɒsəbl/ nhấn âm 2.'),
    ('B', '<b>maintain</b> /meɪnˈteɪn/ nhấn âm 2. greenhouse /ˈɡriːnhaʊs/, lifestyle /ˈlaɪfstaɪl/, nature /ˈneɪtʃə/ nhấn âm 1.'),
    ('A', '<b>volleyball</b> /ˈvɒlibɔːl/ nhấn âm 1. appliance /əˈplaɪəns/, recycle /ˌriːˈsaɪkl/, polluted /pəˈluːtɪd/ nhấn âm 2.'),
    ('C', '<b>issue</b> /ˈɪʃuː/ nhấn âm 1. reduce /rɪˈdjuːs/, adopt /əˈdɒpt/, protect /prəˈtekt/ nhấn âm 2.'),
    ('A', '<b>awareness</b> /əˈweənəs/ nhấn âm 2. difference /ˈdɪfrəns/, instrument /ˈɪnstrəmənt/, character /ˈkærəktə/ nhấn âm 1.'),
    ('A', '<b>organic</b> /ɔːˈɡænɪk/ nhấn âm 2. dangerous /ˈdeɪndʒərəs/, chemical /ˈkemɪkl/, natural /ˈnætʃrəl/ nhấn âm 1.'),
    ('C', '<b>regularly</b> /ˈreɡjələli/ nhấn âm 1. material /məˈtɪəriəl/, compulsory /kəmˈpʌlsəri/, refillable /ˌriːˈfɪləbl/ (trọng âm chính /ˈfɪl/) nhấn âm 2.'),
    ('D', '<b>reserve</b> /rɪˈzɜːv/ nhấn âm 2. rubbish /ˈrʌbɪʃ/, plastic /ˈplæstɪk/, method /ˈmeθəd/ nhấn âm 1.'),
])

# ======================= TỪ VỰNG (E3, E4) =======================
put('vg1', [
    (['eco-friendly', 'eco - friendly', 'eco friendly'], 'as <b>eco-friendly</b> as possible = thân thiện với môi trường nhất có thể (cấu trúc as + adj + as).'),
    (['household appliance', 'household appliances'], 'a popular <b>household appliance</b> = thiết bị gia dụng phổ biến (toaster = máy nướng bánh mì).'),
    (['reduce'], 'to <b>reduce</b> the amount of electricity = giảm lượng điện sử dụng; to + V0.'),
    (['meet'], '<b>meet</b> people\'s needs = đáp ứng nhu cầu của con người.'),
    (['adopt'], 'people <b>adopt</b> a green lifestyle = theo/chọn lối sống xanh; chủ ngữ số nhiều (more and more people) nên giữ nguyên "adopt".'),
    (['energy'], 'a powerful <b>energy</b> source = nguồn năng lượng mạnh (energy source).'),
    (['organic', 'Organic'], '<b>Organic</b> farming = canh tác hữu cơ, không dùng hoá chất độc hại.'),
    (['raise'], 'to <b>raise</b> public awareness = nâng cao nhận thức của cộng đồng.'),
])

put('vg2', [
    (['plastic'], 'the negative impact of using <b>plastic</b> on the environment = tác động tiêu cực của việc dùng nhựa lên môi trường.'),
    (['drop'], 'not to <b>drop</b> litter = không xả/vứt rác (drop litter).'),
    (['eco-friendly', 'eco - friendly', 'eco friendly'], 'the most <b>eco-friendly</b> building materials = vật liệu xây dựng thân thiện môi trường nhất (tre).'),
    (['awareness'], 'raise people\'s <b>awareness</b> of environmental protection = nâng cao nhận thức về bảo vệ môi trường.'),
    (['protect'], 'help to <b>protect</b> the environment = giúp bảo vệ môi trường (help to V0).'),
    (['set up'], 'The club was <b>set up</b> = câu lạc bộ được thành lập (bị động của set up).'),
    (['household'], 'unnecessary <b>household</b> appliances = các thiết bị gia dụng không cần thiết.'),
    (['organic'], 'turn to <b>organic</b> products = chuyển sang dùng sản phẩm hữu cơ (không chứa hoá chất độc hại).'),
])

# ======================= BỊ ĐỘNG (E5) =======================
put('vg3', [
    (variants(['the environment is affected in many ways by pollution', 'the environment is affected by pollution in many ways']),
     '<b>Mẫu:</b> The environment is affected in many ways by pollution. (hiện tại đơn bị động: am/is/are + V3; the environment số ít -> is affected)'),
    (variants(["people's awareness of environmental issues will be raised by the club's activities", "people's awareness of environmental issues will be raised by the activities of the club"]),
     "<b>Mẫu:</b> People's awareness of environmental issues will be raised by the club's activities. (tương lai đơn bị động: will be + V3)"),
    (variants(['many more trees were planted in the neighbourhood last week by the local people', 'many more trees were planted in the neighbourhood by the local people last week', 'many more trees were planted in the neighbourhood last week']),
     '<b>Mẫu:</b> Many more trees were planted in the neighbourhood last week by the local people. (quá khứ đơn bị động: was/were + V3; trees số nhiều -> were planted)'),
    (variants(['the school playground is being cleaned this morning by the students', 'the school playground is being cleaned by the students this morning']),
     '<b>Mẫu:</b> The school playground is being cleaned this morning by the students. (hiện tại tiếp diễn bị động: am/is/are + being + V3)'),
    (variants(['around 100 billion plastic bags are used each year by americans', 'around 100 billion plastic bags are used by americans each year', 'around 100 billion plastic bags are used each year']),
     '<b>Mẫu:</b> Around 100 billion plastic bags are used each year by Americans. (hiện tại đơn bị động; bags số nhiều -> are used)'),
    (variants(['a green lifestyle is adopted by more and more people']),
     '<b>Mẫu:</b> A green lifestyle is adopted by more and more people. (hiện tại đơn bị động; a green lifestyle số ít -> is adopted)'),
    (variants(['rubbish in the central park is going to be picked up this weekend', 'rubbish is going to be picked up in the central park this weekend',
               'rubbish in the central park is going to be picked up this weekend by us', 'rubbish is going to be picked up in the central park this weekend by us']),
     '<b>Mẫu:</b> Rubbish in the central park is going to be picked up this weekend. (tương lai gần bị động: am/is/are + going to + be + V3; chủ ngữ "we" được lược bỏ)'),
    (variants(['a campaign will be organised to protect the environment by the youth union', 'a campaign to protect the environment will be organised by the youth union']),
     '<b>Mẫu:</b> A campaign will be organised to protect the environment by the Youth Union. (tương lai đơn bị động: will be + V3)'),
])

# ======================= NGỮ PHÁP – TỪ VỰNG (E6) =======================
put('vg4', [
    ('C', '<b>sustainable</b> energy = năng lượng bền vững (không cạn kiệt); remarkable = đáng chú ý, significant = đáng kể, affordable = hợp túi tiền.'),
    ('A', '<b>organic</b> food = thực phẩm hữu cơ (tốt cho sức khoẻ, giá cao hơn một chút); non-organic ngược nghĩa.'),
    ('B', 'be responsible <b>for</b> = chịu trách nhiệm về / gây ra.'),
    ('A', 'energy that <b>meets</b> the needs of… = đáp ứng nhu cầu của…; chủ ngữ "energy" số ít -> meets.'),
    ('C', 'the road <b>is being repaired</b> = con đường đang được sửa (hiện tại tiếp diễn bị động; đường không tự sửa).'),
    ('A', '<b>Eco-friendly</b> car models = các mẫu xe thân thiện môi trường.'),
    ('B', 'turn off your <b>household appliances</b> = tắt các thiết bị gia dụng khi không dùng (household chores = việc nhà).'),
    ('A', 'reduce the <b>carbon footprint</b> you produce = giảm lượng khí thải carbon (dấu chân carbon) bạn tạo ra.'),
    ('B', 'a <b>source</b> of energy = nguồn năng lượng (the sun). Resources = tài nguyên.'),
    ('C', '<b>pick up</b> litter = nhặt rác. Turn off = tắt; put off = hoãn; turn up = vặn to lên.'),
    ('C', '<b>energy-saving</b> light bulb = bóng đèn tiết kiệm năng lượng; các phương án còn lại mang nghĩa lãng phí/thiếu năng lượng.'),
    ('A', 'people <b>adopt</b> a green lifestyle = theo lối sống xanh; chủ ngữ số nhiều nên giữ nguyên.'),
    ('A', 'Bị động tương lai đơn: <b>will be built</b> (will + be + V3); "a hospital" không tự xây.'),
    ('B', 'cut down <b>on</b> = cắt giảm (cut down on electricity usage).'),
    ('D', '<b>energy-saving</b> eco light bulb = bóng đèn sinh thái tiết kiệm năng lượng.'),
    ('D', '<b>conserve</b> energy = tiết kiệm/bảo tồn năng lượng (ngữ cảnh: không để thiết bị ở chế độ chờ).'),
    ('C', 'Money <b>was donated</b> to… by Larry = bị động quá khứ đơn (tiền được quyên góp bởi Larry).'),
    ('B', 'be going <b>to be sold</b> = bị động tương lai gần (am/is/are + going to + be + V3).'),
    ('A', 'The ancient houses <b>were destroyed</b> by the fire = bị động quá khứ đơn (nhà cổ bị lửa phá huỷ, nay đang được xây lại).'),
    ('A', '<b>sustainable</b> agriculture = nền nông nghiệp bền vững (hạn chế hoá chất, phân bón).'),
    ('C', '<b>recycle</b> 80% of all waste = tái chế 80% rác thải.'),
    ('D', 'Quyết định ngay lúc nói (nghe thấy có người ở cửa) -> <b>will open</b>.'),
    ('B', 'Dự đoán có bằng chứng (mây đen) -> <b>is going to rain</b>; "it" số ít nên dùng is.'),
    ('B', 'last week + bị động quá khứ đơn: I <b>was given</b> a lot of presents (tôi được tặng).'),
    ('C', 'Lời yêu cầu lịch sự: <b>Will you open</b> the window, please?'),
    ('D', 'Cậu bé <b>was taken</b> to the hospital (quá khứ đơn bị động).'),
    ('D', 'My bike <b>was repainted</b> by my father (xe được sơn lại bởi bố; bị động quá khứ đơn).'),
    ('D', 'They <b>were told</b> this story by their grandmother (bị động quá khứ đơn, có "last week").'),
    ('B', 'More than 120,000 people <b>were killed</b> (bị động quá khứ đơn, có mốc 1945).'),
    (['D', 'A'], 'Khoá Word: headache <b>won\'t go</b> away (dù đã uống thuốc, cơn đau đầu "không chịu" hết). "isn\'t going away" (A) cũng đúng nghĩa: cơn đau vẫn chưa hết.'),
    (['B', 'C'], 'Kế hoạch đã định cho Chủ nhật lúc 8 giờ -> <b>am going to meet</b> (khoá Word). "will be meeting" cũng đúng (tương lai tiếp diễn tại thời điểm cụ thể) nhưng ngoài phạm vi bài học.'),
    ('D', 'Quyết định tức thời (Wait!) -> <b>will drive</b> you to the station.'),
    ('C', 'Kế hoạch đã định (as planned) -> <b>am going to see</b> my sister in April.'),
    ('D', 'Perhaps (có lẽ) -> dự đoán/khả năng không có cơ sở -> <b>will visit</b>.'),
    ('B', 'Hỏi về kế hoạch đã sắp xếp: What time <b>are you going to leave</b> tomorrow? (do you leave chỉ dùng với lịch trình cố định).'),
    ('C', 'Dự đoán không có căn cứ: Who <b>will win</b> the next World Cup? (is wining sai chính tả).'),
    ('B', 'Có vé miễn phí -> sắp xếp đã định, dùng hiện tại tiếp diễn chỉ kế hoạch gần: He <b>is going</b> to the theatre tonight.'),
    ('B', 'Đã mua vé tàu (I already bought…) -> kế hoạch có căn cứ -> <b>am going to visit</b>.'),
    ('D', 'be born: Stephen Hawking <b>was born</b> on 8 January, 1942 (bị động quá khứ).'),
    ('D', 'Câu hỏi bị động quá khứ đơn: <b>Was that book written</b> by your father? (Was + S + V3).'),
    ('C', 'The teacher <b>punished</b> the student for lying: giáo viên là người thực hiện hành động -> câu chủ động quá khứ đơn (các câu bị động A, B, D sai nghĩa).'),
    ('C', 'the patient <b>was carried</b> home in a wheel chair (anh ta được đưa về; bị động quá khứ đơn).'),
    ('C', 'The injured (những người bị thương – số nhiều) <b>were taken</b> to the hospital in an ambulance.'),
    ('B', 'It <b>is believed</b> that… = Người ta tin rằng… (bị động hiện tại đơn với chủ ngữ giả "it").'),
])

# ======================= NGHE (E9 – không audio) =======================
put('li1', [
    ('T', 'Script: Magda: "He\'s <b>off sick</b>" (Tony nghỉ ốm) -> Tony không đi làm vì bị bệnh.'),
    ('F', 'Harry: "I couldn\'t find anywhere to park my car" và "sometimes it\'s just easier to drive" -> anh ấy lái xe tới, không đạp xe.'),
    ('F', 'Harry: "I do lots of sport — play football <b>every week</b>" -> mỗi tuần chứ không phải mỗi ngày.'),
    ('T', 'Johnny: "Of course I drive. How else would I get around?" -> anh ấy đi đâu cũng lái xe.'),
    ('T', 'Magda: "I always use public transport. It\'s <b>very good here in London</b>…" -> cô ấy cho rằng giao thông công cộng ở London tốt.'),
    ('F', 'Johnny: "I\'m not cycling. It\'s tiring, and <b>dangerous</b>!" -> anh ấy cho rằng đạp xe nguy hiểm.'),
    ('T', 'Olivia: "…think about your health and the future of the planet!… we should all help the planet" -> cô ấy lo lắng cho hành tinh.'),
    ('F', 'Magda: "it\'s <b>really busy</b> in here right now" -> Carlos (đầu bếp thay thế, phải làm cả phục vụ) rất bận.'),
])

# ======================= NÓI =======================
put_open('sp1', [
    '<b>Bài mẫu:</b> There are several things I should do to make the environment better. First, I should reduce the amount of energy I use in the home. For example, I have to turn off all the electrical appliances when they are not in use. Second, I should use organic products because they are not only good for my health but also good for the environment. Last, I should avoid using products that are made from plastic. As it takes plastic a long time to break down, we should reduce the use of plastic as much as possible.',
])

# ======================= ĐỌC =======================
put('re1', [
    ('C', 'Cả bài nói về việc các siêu thị và cửa hàng nhỏ hướng tới tương lai bền vững (giảm rác nhựa, rác thực phẩm) -> <b>Sustainable Supermarkets</b>. A quá chung, B và D không bao quát nội dung.'),
    ('C', 'Đoạn 2: "growing consumer backlash against the huge amounts of plastic waste" -> người tiêu dùng muốn siêu thị <b>reduce their plastic waste</b>.'),
    ('C', '<b>backlash</b> = phản ứng dữ dội/phản ứng của công chúng ≈ <b>reaction</b>.'),
    ('A', '<b>the lion\'s share</b> = phần lớn nhất ≈ the largest part.'),
    ('A', 'Đoạn 3: "Most supermarkets operate under a veil of secrecy when asked for exact figures of food wastage" -> siêu thị không cho biết họ lãng phí bao nhiêu thức ăn. B, C, D trái với bài.'),
])

put('re2', [
    ('B', 'Genzyme Center: giảm 43% năng lượng; Vauban: nhà dùng ít hơn 30% năng lượng; cả hai xây theo nguyên tắc công trình xanh, giảm đáng kể năng lượng. C, D không đúng cho cả hai.'),
    ('A', 'Đoạn 3: "builders also add <b>insulation</b> to the walls so that the building stays warmer in winter and cooler in summer" -> vật liệu cách nhiệt, chống mất/hấp thụ nhiệt.'),
    ('D', 'Đoạn 1: "Now, however, the movement is growing, as builders have been able to take advantage of new technology" -> trước đây công nghệ chưa cho phép nên mục tiêu bị cho là phi thực tế.'),
    ('A', 'Đoạn cuối và các đoạn 4-6: Mỹ, Đức, Trung Quốc; "Green building ideas… are spreading" -> ngày càng phổ biến trên thế giới. B ("produce no pollution"), C, D sai/không được nói.'),
    ('C', '<b>under way</b> = đang diễn ra, đã được bắt đầu ≈ <b>being launched</b>.'),
    ('D', 'Đoạn 7 nêu: thân thiện môi trường, cải thiện điều kiện sống và làm việc, tiết kiệm tiền về lâu dài; <b>không</b> nói tăng năng suất làm việc.'),
    ('D', 'Cả bài nói về phong trào và cách tiếp cận xây dựng thân thiện với môi trường (công trình xanh) -> An environmentally friendly approach to constructing buildings.'),
    ('A', '"Once installed, <b>they</b> provide energy at no cost" -> they = <b>solar panels</b> (các tấm pin mặt trời) ở câu trước.'),
])

# ======================= VIẾT =======================
put('wr1', [
    (variants(combos([['reducing', 'reduce'][:1], 'the amount of air travel is', ['a good way', 'one good way', 'one way', 'the best way'], 'to reduce', ['your', 'our', 'the', 'my'], 'carbon footprint'])),
     '<b>Mẫu:</b> Reducing the amount of air travel is a good way to reduce your carbon footprint. (V-ing làm chủ ngữ + is a good way to V)'),
    (variants(combos(['you should turn off', ['your household appliances', 'your appliances', 'the household appliances', 'the appliances', 'household appliances', 'appliances'], 'when they are', ['not in use', 'not being used', 'not used'], 'to save energy'])),
     '<b>Mẫu:</b> You should turn off your household appliances when they are not in use to save energy. (should + V0; to V = để; in use = đang được sử dụng)'),
    (variants(combos(['you should use public transport such as', ['buses or trains', 'buses and trains', 'a bus or a train', 'bus or train'], 'rather than', ['using your private vehicles', 'using private vehicles', 'your private vehicles', 'private vehicles']])),
     '<b>Mẫu:</b> You should use public transport such as buses or trains rather than using your private vehicles. (rather than + V-ing / N)'),
    (variants(combos([['cutting down on', 'cutting down', 'cutting', 'cutting back on'], 'plastic products', ['can reduce', 'will reduce', 'reduces', 'helps reduce', 'can help reduce'], 'plastic pollution'])),
     '<b>Mẫu:</b> Cutting down on plastic products can reduce plastic pollution. (cut down on + N làm chủ ngữ dạng V-ing)'),
    (variants(combos(['you should buy organic food', ['because it', 'as it', 'since it'], ['does not contain', 'doesn\'t contain'], ['harmful chemicals', 'any harmful chemicals']]) +
              combos(['you should buy organic food', ['which', 'that'], ['does not contain', 'doesn\'t contain'], ['harmful chemicals', 'any harmful chemicals']])),
     '<b>Mẫu:</b> You should buy organic food because it does not contain harmful chemicals. (should + V0; because + mệnh đề)'),
    (variants(combos(['planting trees', ['provides', 'can provide'], 'shade and', ['makes', 'make'], 'the environment', ['beautiful', 'look beautiful', 'more beautiful']]) ),
     '<b>Mẫu:</b> Planting trees provides shade and makes the environment beautiful. (V-ing làm chủ ngữ số ít -> provides, makes)'),
    (variants(combos(['green living is', ['adopted', 'being adopted'], 'by', ['more and more people', 'people', 'many people'], ['in the world', 'around the world', 'all over the world']]) +
              combos(['green living has been adopted by', ['more and more people', 'people', 'many people'], ['in the world', 'around the world', 'all over the world']])),
     '<b>Mẫu:</b> Green living is adopted by more and more people in the world. (bị động hiện tại đơn: is + V3 + by + O)'),
    (variants(["people's awareness of environmental protection has been raised since they took part in the campaign",
               "people's awareness of environmental protection has been raised since they took part in a campaign",
               "people's awareness of environmental protection has been raised since they have taken part in the campaign"]),
     "<b>Mẫu:</b> People's awareness of environmental protection has been raised since they took part in the campaign. (hiện tại hoàn thành bị động: has been + V3; since + mệnh đề quá khứ đơn)"),
])

put_open('wr2', [
    '<b>Bài mẫu:</b> There are several things that I can do to reduce my carbon footprint. Firstly, I should try to save energy. I can do this by turning off all the electrical appliances when they are not in use and taking shorter showers. This will help me not to waste electricity and water. Secondly, I should start using public transport like buses or trains instead of asking my dad to drive me. This will reduce the harmful gases in the air, therefore making it cleaner. Finally, I can reduce the amount of air travel I take because planes use more energy than other means of transport. I should avoid flying as much as possible and only fly when the distance is long. By saving energy and water, using public transport and avoiding air travel, I can effectively reduce the amount of carbon footprint that I produce.',
])
