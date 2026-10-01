# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Unit 3 (Tiếng Anh 11 Global Success) – Bộ BÀI TẬP BỔ TRỢ.
Quy ước:
  mcq  : chữ cái 'A'-'D' (plain: chính văn bản phương án)   tf : 'T' / 'F'
  fill : danh sách đáp án chấp nhận (1 ô)  hoặc {'blanks': [[...],[...]]} (nhiều ô)
  open : không chấm điểm, EXPLANATIONS chứa đáp án mẫu
Đáp án lấy từ khoá (tô đậm) trong file Word gốc (nửa sau file src/u3/botro.txt) và đối chiếu lại độc lập.
Giữ nguyên khoá Word ở những chỗ mơ hồ/nghi sai; danh sách ghi ở GHI_CHU_RA_SOAT bên dưới."""

GHI_CHU_RA_SOAT = [
    'ph3.6: cả 4 từ (teleconference/television/telephone/telephoto) đều nhấn âm 1; khoá Word = D (câu có vấn đề).',
    'ph3.8: khoá Word không tô; đáp án D (development) suy ra.',
    'vg1.2: khoá Word = C (site); cụm chuẩn là pedestrian zone (D).',
    'vg1.29: nguồn lặp phương án "pays" (B và D); đã đổi D thành "takes". Đáp án A không đổi.',
    'vg3.8: advanced ~ modern (A) / latest (D) đều chấp nhận được; giữ khoá Word A.',
    'vg6.11, vg6.13: khoá Word dùng tiếp diễn (am depending / am seeing); cách dùng thông thường là đơn.',
    'vg7.4: "whenever I see him" -> thói quen; khoá Word is mowing, đã chấp nhận thêm "mows".',
    'sp1.8: nguồn lỗi gõ ở phương án a (đã sửa nhẹ). sp1.9: trả lời Yes/No cho câu hỏi đuôi phủ định gây tranh cãi.',
    'sp4.4: khoá Word = I wonder (không đi với "that"); "No doubt" hợp nghĩa hơn.',
    're3.5 (driverless cars save energy): khoá Word = F nhưng đoạn văn nói self-driven cars save gas -> nên là T.',
    're3.8: khoá Word = F nhưng nội dung bài khá khớp (cost considerable + attract investments).',
    'kt.13: khoá Word = good (getting good); better tự nhiên hơn nhưng không có trong đề.',
    'kt16-21: nguồn thiếu bảng từ cho sẵn (có 2 từ thừa); đã thêm 2 từ nhiễu connect, convenience.',
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


# ======================= PHONETIC – Exercise 1 (nối âm, không chấm điểm) =======================
put_open('ph1', [
    'Các chỗ nối: All of‿us are spending lots‿of time‿in front‿of screens.',
    'Các chỗ nối: It uses‿a range‿of technologies to provide services.',
    'Các chỗ nối: Cities will‿include‿a lot‿of green space‿and become‿even greener.',
    'Các chỗ nối: What‿are the qualities‿of‿a smart city?',
    'Các chỗ nối: These‿are modes‿of transportation‿in‿a big city.',
    'Các chỗ nối: Smart street‿infrastructure will provide‿information for better decision-making.',
    'Các chỗ nối: In Toronto, you can book‿an‿appointment‿and see a doctor‿online from your own home.',
    'Các chỗ nối: Smart cities‿are built‿on new technologies,‿and we consider their‿advantages.',
])

# ======================= PHONETIC – Exercise 2, 3 =======================
put('ph2', [
    ('A', '<b>operate</b> /ˈɒpəreɪt/ (o = /ɒ/). sensor /ˈsensə/, neighbourhood /ˈneɪbəhʊd/, environment /ɪnˈvaɪrənmənt/ đều có o = /ə/.'),
    ('D', '<b>livable</b> /ˈlɪvəbl/ (a = /ə/). garden /ˈɡɑːdn/, path /pɑːθ/, article /ˈɑːtɪkl/ có a = /ɑː/.'),
    ('B', '<b>efficient</b> /ɪˈfɪʃnt/ (c = /ʃ/). privacy /ˈprɪvəsi/, city /ˈsɪti/, centre /ˈsentə/ có c = /s/.'),
    ('A', '<b>provide</b> /prəˈvaɪd/ (o = /ə/). province /ˈprɒvɪns/, volunteer /ˌvɒlənˈtɪə/, population /ˌpɒpjuˈleɪʃn/ có o = /ɒ/.'),
    ('C', '<b>discussion</b> /dɪˈskʌʃn/ (i = /ɪ/). climate /ˈklaɪmət/, designer /dɪˈzaɪnə/, environment /ɪnˈvaɪrənmənt/ có i = /aɪ/.'),
    ('D', '<b>electricity</b> /ɪˌlekˈtrɪsəti/ (e = /ɪ/). dweller /ˈdwelə/, energy /ˈenədʒi/, technology /tekˈnɒlədʒi/ có e = /e/.'),
    ('B', '<b>designer</b> /dɪˈzaɪnə/ (s = /z/). sustainable /səˈsteɪnəbl/, infrastructure /ˈɪnfrəstrʌktʃə/, rescue /ˈreskjuː/ có s = /s/.'),
    ('C', '<b>conservation</b> /ˌkɒnsəˈveɪʃn/ (o = /ɒ/). atmosphere /ˈætməsfɪə/, compulsory /kəmˈpʌlsəri/, opportunity /ˌɒpəˈtjuːnəti/ có o được gạch chân = /ə/.'),
    ('B', '<b>mosaic</b> /məʊˈzeɪɪk/ (o = /əʊ/). popular /ˈpɒpjələ/, optimist /ˈɒptɪmɪst/, responsible /rɪˈspɒnsəbl/ có o = /ɒ/.'),
    ('B', '<b>infrastructure</b> /ˈɪnfrəstrʌktʃə/ (u = /ʌ/). sustainable /səˈsteɪnəbl/, campus /ˈkæmpəs/, surprised /səˈpraɪzd/ có u = /ə/.'),
])

put('ph3', [
    ('A', '<b>understand</b> /ˌʌndəˈstænd/ nhấn âm 3 (động từ ghép nhấn âm cuối). generate /ˈdʒenəreɪt/, innovate /ˈɪnəveɪt/, concentrate /ˈkɒnsntreɪt/ (đuôi -ate, từ 3 âm tiết) nhấn âm 1.'),
    ('D', '<b>domestic</b> /dəˈmestɪk/ nhấn âm 2. different /ˈdɪfrənt/, comfortable /ˈkʌmftəbl/, natural /ˈnætʃrəl/ nhấn âm 1.'),
    ('B', '<b>appear</b> /əˈpɪə/ nhấn âm 2. threaten /ˈθretn/, modernize /ˈmɒdənaɪz/, damage /ˈdæmɪdʒ/ nhấn âm 1.'),
    ('C', '<b>assistance</b> /əˈsɪstəns/ nhấn âm 2. influence /ˈɪnfluəns/, confidence /ˈkɒnfɪdəns/, terrorism /ˈterərɪzəm/ nhấn âm 1.'),
    ('A', '<b>interviewer</b> /ˈɪntəvjuːə/ nhấn âm 1. preparation /ˌprepəˈreɪʃn/, economics /ˌiːkəˈnɒmɪks/, education /ˌedʒuˈkeɪʃn/ nhấn âm 3 (trước -ion, -ics).'),
    ('D', 'Đáp án theo file Word: <b>telephoto</b>. Lưu ý: cả bốn từ teleconference /ˈtelɪkɒnfərəns/, television /ˈtelɪvɪʒn/, telephone /ˈtelɪfəʊn/, telephoto /ˈtelɪfəʊtəʊ/ đều nhấn âm 1 nên câu này có vấn đề về đề, giáo viên cần kiểm tra lại.'),
    ('B', '<b>generate</b> /ˈdʒenəreɪt/ nhấn âm 1. understand /ˌʌndəˈstænd/, represent /ˌreprɪˈzent/, introduce /ˌɪntrəˈdjuːs/ nhấn âm 3 (đuôi -stand, -sent, -duce).'),
    ('D', '<b>development</b> /dɪˈveləpmənt/ nhấn âm 2. presentations /ˌprezənˈteɪʃnz/, individual /ˌɪndɪˈvɪdʒuəl/, innovation /ˌɪnəˈveɪʃn/ nhấn âm 3. (File Word không tô khoá câu này; đáp án D được suy ra.)'),
    ('C', '<b>underground</b> (tính từ/trạng từ) /ˌʌndəˈɡraʊnd/ nhấn âm 3. skyscraper /ˈskaɪskreɪpə/, operate /ˈɒpəreɪt/, government /ˈɡʌvənmənt/ nhấn âm 1.'),
    ('B', '<b>eco-friendly</b> /ˈiːkəʊˌfrendli/ nhấn âm 1. renewable /rɪˈnjuːəbl/, environment /ɪnˈvaɪrənmənt/, sustainable /səˈsteɪnəbl/ nhấn âm 2.'),
])

# ======================= VOCABULARY & GRAMMAR =======================
put('vg1', [
    ('C', '"one of the world\'s richest areas of <b>biodiversity</b>" = một trong những khu vực giàu đa dạng sinh học nhất. variety đi với "a variety of"; numerous là tính từ.'),
    ('C', 'Đáp án theo file Word: C (site). Lưu ý: nghĩa của câu là "khu phố cổ giờ là khu dành cho người đi bộ" nên cụm chuẩn là <b>pedestrian zone</b> (D); "pedestrian site" không phải cụm thông dụng, giáo viên nên kiểm tra lại khoá.'),
    ('B', '<b>eco-friendly</b> cleaning products = sản phẩm làm sạch thân thiện với môi trường. "friendly" đứng riêng không rõ nghĩa; ecological = thuộc hệ sinh thái; economical = tiết kiệm.'),
    ('D', 'invest in <b>infrastructure</b> = đầu tư vào cơ sở hạ tầng để đáp ứng lượng người đổ về Mecca.'),
    ('A', '<b>sustainable</b> design = thiết kế bền vững; sustained = kéo dài liên tục; harmless = vô hại.'),
    ('C', 'feel + tính từ: "I\'ll feel <b>happy</b>". Sau liên động từ (feel, look, smell, taste, sound…) dùng tính từ, không dùng trạng từ.'),
    ('B', 'smell + tính từ. "Although… he refused to eat" (dù… vẫn không ăn) nên món ăn <b>smelt good</b> (mùi thơm) mới hợp nghĩa.'),
    ('A', 'taste + tính từ: "The fish tastes <b>awful</b> (so) I won\'t eat it" = cá có vị kinh khủng nên tôi không ăn.'),
    ('C', 'look + tính từ: "The situation looks <b>bad</b>" = tình hình trông tồi tệ, cần phải làm gì đó.'),
    ('D', 'seem + tính từ: "He seemed a bit <b>strange</b> today" = hôm nay anh ấy có vẻ hơi lạ.'),
    ('B', '<b>alternative</b> sources of energy = nguồn năng lượng thay thế (mặt trời, hạt nhân…).'),
    ('A', 'city <b>dwellers</b> = cư dân thành thị (cụm cố định). inhabitants cũng là "cư dân" nhưng đáp án theo cụm "city dwellers".'),
    ('B', '<b>optimistic</b> = lạc quan, hy vọng vào tương lai; pessimistic = bi quan.'),
    ('A', 'Sau tính từ "constant" cần danh từ: constant <b>threat</b> of attack = mối đe dọa tấn công thường trực.'),
    ('B', 'Trạng từ bổ nghĩa cho tính từ friendly: <b>environmentally friendly</b> city = thành phố thân thiện với môi trường.'),
    ('D', '"cannot be replaced after use" → tài nguyên <b>non-renewable</b> (không tái tạo được).'),
    ('C', 'Giải pháp cho ùn tắc: cấm xe <b>private</b> (xe cá nhân) ở trung tâm; public vehicles là phương tiện công cộng nên không bị cấm.'),
    ('C', 'Chiến tranh tàn phá <b>infrastructure</b> (cơ sở hạ tầng) của đất nước. building/skyscraper/centre không hợp với "the country\'s…".'),
    ('C', '<b>renewable</b> energy capacity = công suất năng lượng tái tạo; nonrenewable/fossil fuel không phải xu hướng tăng.'),
    ('D', 'improve <b>quality</b> of life = nâng cao chất lượng cuộc sống.'),
    ('C', 'help the city <b>operate</b> more efficiently = giúp thành phố vận hành hiệu quả hơn.'),
    ('B', '"Electric buses and trains will produce less greenhouse gas emissions" → hạ tầng sẽ <b>eco-friendly</b> hơn (thân thiện môi trường). Các lựa chọn còn lại sai cấu trúc (phải là tính từ ghép/trạng từ + friendly).'),
    ('B', 'big downtown <b>skyscrapers</b> = những toà nhà chọc trời ở khu trung tâm (nhà hàng nằm trên tầng cao).'),
    ('D', '<b>urban</b> population = dân số đô thị (các thành phố chưa tồn tại ở Châu Phi, Đông Nam Á…).'),
    ('A', 'city <b>dwellers</b> = cư dân thành phố (404 triệu người sẽ thêm vào dân số Ấn Độ).'),
    ('C', 'hệ thống đèn giao thông mới <b>detects</b> (phát hiện) khi nhiều xe đạp đang đến gần rồi giữ đèn xanh lâu hơn.'),
    ('B', '<b>infrastructure</b> and transportation = hạ tầng và giao thông kết nối nhu cầu của người dân mọi thế hệ.'),
    ('B', 'Song song với "faster" và "eco-friendly": public transport more <b>convenient</b> = tiện lợi hơn.'),
    ('A', '<b>attracts</b> people\'s attention = thu hút sự chú ý. (Trong đề, B và D đều là "pays"; "pay attention" cần "to" nên vẫn sai.)'),
    ('C', '<b>sensors</b> (cảm biến) có thể báo cho đội thu gom rác khi thùng đầy.'),
    ('C', 'offering city <b>inhabitants</b> something… = mang đến cho cư dân thành phố điều họ chưa từng có.'),
    ('B', 'officials are <b>optimistic</b> that… = các quan chức lạc quan rằng khu trung tâm vẫn xanh; pessimistic trái nghĩa.'),
    ('D', 'problems such as <b>overcrowded</b> roads = đường xá quá tải do dân số tăng nhanh.'),
    ('D', 'greenhouse gas <b>emissions</b> = khí thải nhà kính (reduce emissions).'),
    ('D', '<b>pedestrian</b> zones = khu vực dành cho người đi bộ (walking and cycle paths).'),
])

put('vg2', [
    ('wants', '<b>wants</b>: want là động từ trạng thái (stative) → không dùng tiếp diễn.'),
    ('is thinking', '<b>is thinking</b> about holding a party: think = cân nhắc/đang tính toán (hành động) → dùng hiện tại tiếp diễn.'),
    ('tastes', 'This soup <b>tastes</b> delicious: taste = "có vị" (liên động từ, trạng thái) → hiện tại đơn, theo sau là tính từ.'),
    ('tastes', 'always + thói quen → hiện tại đơn: The chef always <b>tastes</b> the food (đầu bếp luôn nếm món ăn).'),
    ('are you smelling', 'smell = ngửi (hành động có chủ ý, đang diễn ra): Why <b>are you smelling</b> the flowers? Nếu là "có mùi" (trạng thái) mới dùng đơn.'),
    ('is having', 'have a great time = vui vẻ (hành động) → <b>is having</b> (đang vui) ở buổi tiệc.'),
    ('has', 'have = sở hữu (stative) → <b>has</b> some great fancy dress costumes, không dùng tiếp diễn.'),
    ('believes', 'believe là động từ trạng thái → <b>believes</b> in UFOs.'),
    ('think', 'think = tin rằng, nghĩ rằng (quan điểm) → hiện tại đơn: I <b>think</b> they are tired.'),
    ('are going', 'Kế hoạch đã sắp xếp cho tối nay (tonight) → hiện tại tiếp diễn với nghĩa tương lai: We <b>are going</b> to a concert tonight.'),
])

put('vg3', [
    ('D', 'dwellers ≈ <b>residents</b> (cư dân).'),
    ('A', 'efficient (hiệu quả) ≈ <b>effective</b>.'),
    ('A', 'interact with ≈ <b>communicate</b> (giao tiếp, tương tác).'),
    ('B', 'well-being (sự khoẻ mạnh, hạnh phúc) ≈ <b>quality of life</b> (chất lượng cuộc sống).'),
    ('B', 'traffic jams ≈ <b>congestion</b> (tắc nghẽn giao thông).'),
    ('B', 'benefits (lợi ích) ≈ <b>advantages</b>; drawbacks mới là disadvantages.'),
    ('C', 'smart (thông minh) ≈ <b>intelligent</b>; stupid là trái nghĩa.'),
    ('A', 'advanced (tiên tiến) ≈ <b>modern</b> (hiện đại). (latest cũng gần nghĩa nhưng giữ khoá Word là A.)'),
    ('A', 'includes (bao gồm) ≈ <b>consists of</b>; excludes là trái nghĩa.'),
    ('D', 'advantageous (có lợi) ≈ <b>beneficial</b>; disadvantaged = thiệt thòi.'),
])

put('vg4', [
    ('B', 'sustainable (bền vững, lâu dài) ↔ <b>short-term</b> (ngắn hạn).'),
    ('D', 'upgraded (được nâng cấp) ↔ <b>deteriorated</b> (xuống cấp).'),
    ('C', 'detect (phát hiện) ↔ <b>ignore</b> (bỏ qua, không để ý).'),
    ('B', 'pessimistic (bi quan) ↔ <b>optimistic</b> (lạc quan).'),
    ('A', 'private (cá nhân) ↔ <b>public</b> (công cộng).'),
    ('B', 'renewable (tái tạo được, dùng mãi) ↔ <b>limited</b> (hạn chế).'),
    ('C', 'modern (hiện đại) ↔ <b>traditional</b> (truyền thống).'),
    ('D', 'urban (đô thị) ↔ <b>rural</b> (nông thôn).'),
    ('C', 'overcrowded (quá đông) ↔ <b>empty</b> (vắng, trống).'),
    ('B', 'livable (có thể sống được) ↔ <b>uninhabitable</b> (không thể ở được).'),
])

put('vg5', [
    (['feels'], 'feel = cảm thấy (trạng thái, giác quan) → hiện tại đơn: The sun <b>feels</b> hot.'),
    (['is feeling'], 'feel = sờ, chạm vào (hành động đang làm) → hiện tại tiếp diễn: He <b>is feeling</b> the jumper.'),
    (['has'], 'have = có, sở hữu (stative) → <b>has</b> three boxes of sweets.'),
    (['is having'], 'have a party = tổ chức tiệc (hành động; "tomorrow" là kế hoạch) → <b>is having</b>.'),
    (['tastes'], 'taste = có vị (trạng thái, theo sau là tính từ awful) → <b>tastes</b>.'),
    (['is tasting'], 'taste = nếm thử (hành động đang làm) → <b>is tasting</b> the soup.'),
    (['thinks'], 'think = nghĩ rằng (quan điểm) → <b>thinks</b> the party sounds good.'),
    (['is thinking'], 'think of = đang cân nhắc (hành động) → <b>is thinking</b> of going away.'),
    (['looks'], 'look + tính từ = trông có vẻ (trạng thái) → Nam <b>looks</b> happy.'),
    (['is looking'], 'look for = đang tìm (hành động) → Nam <b>is looking</b> for his costume.'),
])

put('vg6', [
    (['am expecting', "'m expecting"], 'expect = đang chờ đợi (hành động, có "a parcel") → <b>am expecting</b>.'),
    (['expect'], 'expect = cho rằng, đoán rằng (quan điểm) → <b>expect</b> you are tired.'),
    (['are considering'], 'consider = đang xem xét (hành động diễn ra lúc này, "at least they…") → <b>are considering</b>.'),
    (['consider'], 'consider = cho rằng, coi là (quan điểm chung) → <b>consider</b> him to be the best guitarist.'),
    (['see'], 'see = nhận ra, hiểu ra (trạng thái nhận thức) → I <b>see</b> the price has gone up.'),
    ({'blanks': [['are'], ['seeing']]}, 'see = gặp (hẹn, kế hoạch tương lai "again") → When <b>are</b> you <b>seeing</b> Nam again?'),
    (['holds'], 'hold = chứa được (trạng thái) → This jug <b>holds</b> one litre exactly.'),
    (['are holding'], 'hold a meeting = tổ chức họp (hành động đang diễn ra) → They <b>are holding</b> a meeting.'),
    (['is tasting'], 'taste = nếm thử (hành động) → He <b>is tasting</b> the wine to see…'),
    (['tastes'], 'taste + tính từ funny (có vị lạ) → This soup <b>tastes</b> funny.'),
    (['am depending', "'m depending"], 'depend on (đang trông cậy, nhấn mạnh tạm thời) → Đáp án theo file Word: <b>am depending</b> on you. (Cách dùng thông thường là "I depend on you", nhưng giữ khoá Word.)'),
    (['depends'], 'depend (stative) → It <b>depends</b> what you mean by "love".'),
    (['am seeing', "'m seeing"], 'Đáp án theo file Word: <b>am seeing</b> double (đang nhìn thấy hai hình – tình trạng tạm thời của mắt).'),
    (['see'], 'see = nhìn thấy (khả năng, trạng thái) → I <b>see</b> much better with glasses.'),
    (['think'], 'think = nghĩ rằng (quan điểm) → I <b>think</b> it is going to rain.'),
    (['am thinking', "'m thinking"], 'think of = đang tính, cân nhắc (hành động) → I <b>am thinking</b> of going to Hoi An.'),
    (['appears'], 'appear to be = có vẻ như (stative) → He <b>appears</b> to be very ill.'),
    (['is appearing'], 'appear = xuất hiện, trình diện (hành động) → She <b>is appearing</b> in cosplay at the festival.'),
    ({'blanks': [['does'], ['look']]}, 'What does it look like? = Nó trông như thế nào? → What <b>does</b> it (look) <b>look</b> like? (hai ô: does / look)'),
    (['is looking'], 'look for = tìm kiếm (hành động đang diễn ra) → He <b>is looking</b> for a job.'),
])

put('vg7', [
    ({'blanks': [['is going'], ['has']]}, 'go to the doctor (đang đi – hành động tạm thời) → <b>is going</b>; have a headache (bị đau đầu – trạng thái) → <b>has</b>.'),
    ({'blanks': [['is having'], ['has']]}, 'have dinner (đang ăn tối) → <b>is having</b>; have a good appetite (có khẩu vị tốt – trạng thái) → <b>has</b>.'),
    ({'blanks': [['are living'], ['like']]}, '"at the moment" → <b>are living</b> (tạm thời); like (stative) → <b>like</b>.'),
    ({'blanks': [['is mowing', 'mows'], ['see']]}, 'Đáp án theo file Word: <b>is mowing</b> ... <b>see</b>. (Vì có "whenever" – thói quen – nên dạng "mows" cũng đúng; hệ thống chấp nhận cả hai.) see = nhìn thấy → hiện tại đơn.'),
    ({'blanks': [['is touching'], ['feels']]}, 'touch the kettle (đang chạm vào) → <b>is touching</b>; feel + tính từ hot (trạng thái) → <b>feels</b>.'),
    ({'blanks': [['are smelling'], ['smells']]}, '"now" – smell the coffee (đang ngửi, chủ ý) → <b>are smelling</b>; smell + tính từ good → <b>smells</b>.'),
    ({'blanks': [['is rising'], ['appears']]}, 'rise (đang mọc, "now") → <b>is rising</b>; appear over the horizon (xuất hiện, trạng thái/sự kiện) → <b>appears</b>.'),
    ({'blanks': [['is'], ['doing'], ['is thinking'], ['loves']]}, '"What <b>is</b> he <b>doing</b> there now?" (đang làm gì); think of (đang nghĩ về) → <b>is thinking</b>; love (stative) → <b>loves</b>.'),
    ({'blanks': [['are looking'], ['appear']]}, 'look at (đang nhìn) → <b>are looking</b>; appear + tính từ (trông có vẻ) → <b>appear</b>.'),
    ({'blanks': [['believe'], ['are enjoying']]}, 'believe (stative) → <b>believe</b>; "now" → <b>are enjoying</b> your holiday.'),
])

put('vg8', [
    ('B', '<b>(B) seriously → serious</b>: look + tính từ ("looked serious"), không dùng trạng từ.'),
    ('D', '<b>(D) impressive → impressionable</b>: "at an impressionable age" = ở độ tuổi dễ bị ảnh hưởng.'),
    ('C', '<b>(C) have → has</b>: "The number of + N số nhiều" chia động từ số ít.'),
    ('B', '<b>(B) bored → boring</b>: find + O + adj chỉ tính chất của việc nhà → boring (tẻ nhạt).'),
    ('C', '<b>(C) pay room → make room</b>: make room for = dọn chỗ/nhường chỗ cho.'),
    ('D', '<b>(D) economy → economics</b>: study economics = học môn kinh tế học.'),
    ('D', '<b>(D) economic → economical</b>: economical on fuel = tiết kiệm nhiên liệu.'),
    ('D', '<b>(D) his jobs → their jobs</b>: chủ ngữ "workers" số nhiều → their.'),
    ('C', '<b>(C) hardly → hard</b>: work hard = làm việc chăm chỉ (hardly = hầu như không).'),
    ('D', '<b>(D) very quick → very quickly</b>: bổ nghĩa cho động từ "woke up" cần trạng từ.'),
])

# ======================= LISTENING =======================
put('li1', [
    (['healthy'], 'Script: "…so they will no longer be safe and <b>healthy</b> places to live in."'),
    (['effective'], 'Script: "…governments have no <b>effective</b> ways to control them (global warming and pollution)."'),
    (['overcrowded'], 'Script: "…cities will become <b>overcrowded</b>. This means there will be more people, more waste and heavier traffic."'),
    (['heavier'], 'Script: "…more people, more waste and <b>heavier</b> traffic." (so sánh hơn của heavy)'),
    (['medicine'], 'Script: "…city dwellers will have a better life thanks to important achievements in technology and <b>medicine</b>."'),
])

put('li2', [
    ('B', 'Script: "as recently as 100 years ago, only <b>two out of ten</b> people lived in a city" = 20%.'),
    ('D', 'Script: "our ancestors began to learn… early <b>agricultural</b> techniques… this led to the development of semi-permanent villages" → tiến bộ trong nông nghiệp.'),
    ('C', 'Script: "as trade flourished, so did technologies that facilitated it, like carts, ships, <b>roads</b>, and ports."'),
    ('A', 'Script: "more people were drawn from the countryside to the cities as more <b>jobs</b> and opportunities became available."'),
    ('D', 'Script: "Global population is currently more than 7 billion and is predicted to top out around <b>10 billion</b>."'),
])

# ======================= SPEAKING =======================
put('sp1', [
    ('A', 'What\'s life in cities in the future like? → mô tả cuộc sống tương lai: "We can enjoy the highest quality of life." (b "We used to…" sai thì: used to chỉ quá khứ).'),
    ('B', 'What\'s it like in 2050? → đáp án theo Word: "I think it\'s the most livable city." (nhận định về Tokyo tương lai); a chỉ nói tàu quá tải, là mô tả tiêu cực/tại hiện tại.'),
    ('B', 'Hỏi về kế hoạch giao thông tương lai → "It promotes self-driving cars and public transport." (a nói về eco-city chung chung, không nói về giao thông).'),
    ('A', 'How can we make our city green? → cách thực hiện: "We try to use wind and sun energy more." (b là tạo việc làm, không liên quan "green").'),
    ('B', 'Một ý kiến (metro không còn kẹt xe) → "I hope it can come true." (phản hồi phù hợp với dự đoán tương lai); a "Is it unbelievable?" là câu hỏi kém tự nhiên.'),
    ('A', 'What\'s the purpose of the project? → "It tries to supply enough drinking water." (mục đích tích cực); b "fails" không phải mục đích.'),
    ('B', 'How can we save energy with street lighting? → "We\'ll install the smart lighting system." (đúng chủ đề street lighting); a nói về tắt đèn trong nhà.'),
    ('A', 'Working hours in the future → "They\'re flexible with fewer hours in the future." (a, đáp án theo Word; b lạc đề). Nguồn có lỗi gõ ở câu a, đã chỉnh nhẹ.'),
    ('A', 'Đáp án theo file Word: a "Yes, healthcare will be free." (b "No, health care will cost lower" sai ngữ pháp). Lưu ý: câu hỏi đuôi phủ định nên cách trả lời Yes/No có thể gây tranh cãi.'),
    ('B', 'What\'s the prediction from pessimists? → "Cities will be overpopulated and traffic will be heavy." (dự đoán bi quan); a (năng lượng tái tạo miễn phí) là lạc quan.'),
])

put('sp2', [
    ('C', '"It\'s ten minutes\' walk from here" trả lời cho câu hỏi về khoảng cách: <b>How far is it from here to the town centre?</b>'),
    ('A', "Câu cảm thán + đồng ý: <b>Yes, it was dull, wasn't it?</b> (câu hỏi đuôi quá khứ, đồng tình)."),
    ('C', 'Câu tiếp theo "Life will be more enjoyable…, won\'t it?" cho thấy người nói đồng ý: <b>Yes, I agree.</b>'),
    ('A', 'Câu đáp "That\'s right" → câu trước phải là câu hỏi đuôi: "there\'ll be no pollution" (khẳng định) → <b>will there?</b> (phủ định "no" nên đuôi khẳng định).'),
    ('C', "Có dự báo thời tiết + lời nhắc: <b>It's going to rain. Don't forget your raincoat, will you?</b> (câu mệnh lệnh phủ định → đuôi will you?)."),
    ('B', "Đồng ý với nhận định về nóng lên toàn cầu: <b>Then we can't afford to ignore its effects any longer, can we?</b> (đuôi can we cho can't)."),
    ('C', '"Am I disturbing you?" → đáp lịch sự: <b>No, never mind.</b> (không sao đâu).'),
    ('B', 'Phản bác câu hỏi đuôi phủ định: <b>On the contrary, it will be.</b> (trái lại, nó sẽ là nơi tốt).'),
    ('C', 'Nhờ vả lịch sự: Get me…, <b>could you?</b> (đuôi của mệnh lệnh khẳng định có thể là could you/will you).'),
    ('C', "Gợi ý khi không có kế hoạch: <b>Let's go to the cinema, shall we?</b> (Let's… shall we?)."),
])

put('sp3', [
    ('C', '(1) <b>C</b>: "The government needs to solve the pollution problems <i>to make our city livable, and eco cities will be the new trend…</i>"'),
    ('E', '(2) <b>E</b>: "It plans to be <i>the first carbon-neutral city in the world</i>" (Masdar City).'),
    ('A', '(3) <b>A</b>: "there are no traditional cars; instead, people <i>either walk or travel in electric podcars</i>".'),
    ('F', '(4) <b>F</b>: "Many big solar farms, using power from the sun, <i>will provide the city with its energy</i>".'),
    ('D', '(5) <b>D</b>: "There are no high-rise buildings, and people <i>live in comfortable apartments</i>". (Phương án B là câu thừa.)'),
])

put('sp4', [
    ("I'm sure", '"She always prefers yours" cho thấy tin chắc → <b>I\'m sure</b> your mum will like your present.'),
    ('No doubt', 'Có tên hoạ sĩ trên tranh nên chắc chắn → <b>No doubt</b> this is the Mona Lisa painting.'),
    ('Perhaps', "Hai khả năng (bị phạt hoặc thích) → không chắc chắn → <b>Perhaps</b> the teacher will punish you… or she'll like them."),
    ('I wonder', 'Đáp án theo file Word: <b>I wonder</b> (tự hỏi). Lưu ý: "No doubt" cũng hợp nghĩa hơn; giáo viên nên xem lại.'),
    ("I'm not sure", 'Câu sau gợi ý chỗ khác ("What about the bedroom?") → <b>I\'m not sure</b> that is the right place.'),
    ("I'm certain", '"has been sitting in the sun for three hours" → chắc chắn sẽ ốm: <b>I\'m certain</b> he will be ill.'),
    ("I'm certain", "Tin chắc rằng bạn có thể giúp bảo vệ môi trường: <b>I'm certain</b>."),
    ('I wonder', 'Which story… → câu hỏi gián tiếp tự hỏi: <b>I wonder</b> which story Grandma is going to tell us.'),
    ("I'm sure", '"The weather is lovely" → suy đoán chắc chắn: <b>I\'m sure</b> they are enjoying the picnic.'),
    ('Maybe', 'Suy đoán có thể xảy ra: <b>Maybe</b> she has a lot of work to do.'),
    ('No doubt', "Không thể thoát khỏi con cá mập đáng sợ → chắc chắn: <b>No doubt</b> he won't be able to escape."),
])

# ======================= READING =======================
put('re1a', [
    ('A', 'celebrate World Car free Day = tổ chức/kỷ niệm Ngày Thế giới không xe hơi. host = đăng cai (chủ ngữ là người dân nên không hợp).'),
    ('C', 'Mệnh đề không xác định bổ nghĩa cho "event" (vật), đứng sau dấu phẩy → <b>which</b>.'),
    ('D', 'raise awareness <b>of</b> the problems = nâng cao nhận thức về các vấn đề (cụm cố định awareness of).'),
    ('B', 'what their city might <b>look</b> like = thành phố của họ trông như thế nào (look like).'),
    ('D', 'take <b>part</b> in = tham gia (cụm cố định).'),
])

put('re1b', [
    ('A', 'tests being <b>carried out</b> by scientists = các thí nghiệm đang được các nhà khoa học tiến hành (carry out tests).'),
    ('A', 'We are <b>creating</b> a conflict between… = chúng ta đang tạo ra sự xung đột giữa mong muốn của trí óc và đồng hồ sinh học.'),
    ('D', 'the multiple rhythms of the body <b>representing</b> the various orchestra sections = các nhịp của cơ thể đại diện cho các bộ phận dàn nhạc.'),
    ('D', 'every <b>type</b> of activity and rest = mọi loại hoạt động và nghỉ ngơi.'),
    ('A', 'not taking into <b>account</b> the dark side = không tính đến mặt tối (take into account).'),
])

put('re2a', [
    ('D', '"The four-day working week will certainly be a reality" → cuối tuần sẽ dài hơn (<b>the weekends will be longer</b>).'),
    ('C', '"If you ask a hundred people… you will probably get a hundred answers" → mỗi người một ý kiến: <b>different people tend to have different opinions</b>.'),
    ('D', 'emerge = xuất hiện, nổi lên ≈ <b>come up</b>.'),
    ('C', '"one of a number of choices, along with living in groups and living alone" → <b>You may choose to live with other people in groups</b>.'),
    ('A', '"More people will work from home at computers linked to a head office" → <b>More people will work from home</b> instead of travelling.'),
])

put('re2b', [
    ('C', '"In 1959, a commission was established to investigate the possible locations of this new city" → <b>to look into possibilities of the locations</b>.'),
    ('B', '"They then produced a report suggesting <b>two</b> possible areas" (Karachi và Rawalpindi).'),
    ('A', 'Các yếu tố được xét: transportation, water, economic factors, national interest. Khí hậu và tình trạng toà nhà là lý do bỏ Karachi (chưa phải yếu tố chọn địa điểm) → <b>A</b> là NOT considered.'),
    ('D', 'Bài không nói Islamabad "đóng vai trò quan trọng nhất" (mỗi phần có vai trò khác nhau) → <b>D</b> là NOT true.'),
    ('D', 'Cả bài kể quá trình chọn địa điểm và quy hoạch Islamabad → <b>The choice and development of Islamabad as the modern capital</b>.'),
])

put('re3', [
    ('T', 'T – "intelligent homes that can interact with their owners" (nhà thông minh có tương tác với chủ nhà).'),
    ('T', 'T – "things that were earlier considered science fiction are already coming to life in smart cities such as Masdar".'),
    ('T', 'T – Masdar có "automated underground transport network fully fueled by solar power" (năng lượng mặt trời là tái tạo).'),
    ('F', 'F – Đèn đường "will switch on only when you are close by" (chỉ sáng khi có người đến gần), không phải bật sau khi phát triển cảm biến.'),
    ('F', 'Đáp án theo file Word: F. Lưu ý: đoạn văn nói "self-driven cars will enable you to save on gas and other non-renewable energy sources" nên có thể xem là T; giáo viên nên kiểm tra lại.'),
    ('F', 'F – Thành phố thông minh nhằm "neutralize the use of fossil fuels" (trung hoà việc dùng nhiên liệu hoá thạch), không phải làm cho nhiên liệu "trung tính".'),
    ('T', 'T – "have to adapt quickly to rapid technological advancements… will make these cities more open and social".'),
    ('F', 'Đáp án theo file Word: F. Lưu ý: bài nói chi phí xây dựng lớn và Ấn Độ đang kêu gọi đầu tư (attract investments) nên câu này rất gần với nội dung bài; giáo viên nên kiểm tra lại.'),
])

put_open('re4', [
    '<b>Mẫu:</b> Recycling, renewable energy, transportation options, building construction, air quality and emissions make a city green.',
    '<b>Mẫu:</b> Because there are lots of electric and manual bikes, organic food, clean water, sustainable buildings and hotels, lots of green space and fewer cars.',
    '<b>Mẫu:</b> It will focus on transportation and renewable energy (and doubling the number of cyclists).',
    '<b>Mẫu:</b> Bristol will concentrate on low carbon sectors.',
    '<b>Mẫu:</b> Because it is mild and it leads the way for forward thinking and environmental awareness in North America.',
    '<b>Mẫu:</b> It will try to be powered entirely by renewable energy by the year 2050.',
])

# ======================= WRITING =======================
put('wr1', [
    (['first we regulate lighting to reduce energy costs', 'first we regulate lighting to reduce the energy costs'], '<b>Mẫu:</b> First, we regulate lighting to reduce energy costs. (to + V chỉ mục đích)'),
    (['next we use smart cards for citizens such as health ids transportation cards etc', 'next we use smart cards for citizens such as health ids transportation cards etc'], '<b>Mẫu:</b> Next, we use smart cards for citizens such as health IDs, transportation cards, etc. (thêm "for" và "such as")'),
    (['mobility systems will be based on bicycle sharing and better traffic control', 'mobility systems are based on bicycle sharing and better traffic control'], '<b>Mẫu:</b> Mobility systems will be based on bicycle sharing and better traffic control. (be based on)'),
    (['then intelligent water supply intelligent energy management such as public lighting and more efficient waste management are available', 'then intelligent water supply intelligent energy management such as public lighting and more efficient waste management will be available'], '<b>Mẫu:</b> Then, intelligent water supply, intelligent energy management, such as public lighting, and more efficient waste management are available.'),
    (['to be more efficient the authorities must observe what habits the consumer has in all aspects and levels so there will be a reduction of privacy', 'to be more efficient the authorities observe what habits the consumer has in all aspects and levels so there is a reduction of privacy'], '<b>Mẫu:</b> To be more efficient, the authorities must observe what habits the consumer has in all aspects and levels, so there will be a reduction of privacy.'),
    (['smart cities require a significant investment in technology so not all cities can afford such a cost', 'smart cities require a significant investment in technology so not all cities can afford a cost'], '<b>Mẫu:</b> Smart cities require a significant investment in technology, so not all cities can afford such a cost. (afford + a cost; thêm can/such)'),
    (['smart cities depend on companies that offer the services of a high degree of technology', 'smart cities depend on companies that offer services of a high degree of technology'], '<b>Mẫu:</b> Smart cities depend on companies that offer the services of a high degree of technology. (depend on + mệnh đề quan hệ)'),
])

put_open('wr2', [
    "<b>Bài mẫu:</b> Living in a smart city offers various advantages and disadvantages beyond the convenience and efficiency they promise. Additional advantages include improved safety and security. Smart cities employ advanced surveillance systems, sensors, and AI technology to monitor and prevent crimes, providing residents with a sense of security. Efficient waste management and reduced pollution are other positives of smart cities, as they utilize real-time data to optimize waste collection and implement sustainable practices.<br><br>However, there are also drawbacks to consider. The heavy reliance on technology increases the risk of cyber-attacks, leaving personal information vulnerable to hacking and privacy invasion. Additionally, the omnipresence of data collection might infringe upon citizens' privacy rights. Social inequality may also arise due to the digital divide, where some residents may struggle to access or afford the technologies and services provided by smart cities.<br><br>While smart cities offer numerous benefits, striking a balance between technological advancements and safeguarding privacy and equality remains a challenge. Nevertheless, with careful planning and policies, these cities have the potential to bring long-term positive changes to urban living.",
])

# ======================= TEST – 50 câu =======================
put('kt', [
    ('B', '<b>efficient</b> /ɪˈfɪʃnt/ (e = /ɪ/). dweller /ˈdwelə/, technology /tekˈnɒlədʒi/, exhibition /ˌeksɪˈbɪʃn/ có e = /e/.'),
    ('C', '<b>skyscraper</b> /ˈskaɪskreɪpə/ (a = /eɪ/). pedestrian /pəˈdestriən/, privacy /ˈprɪvəsi/, infrastructure /ˈɪnfrəstrʌktʃə/ có a = /ə/.'),
    ('A', '<b>high-rise</b> /ˈhaɪraɪz/ (s = /z/). sensor, sustainable, pedestrian có s = /s/.'),
    ('C', '<b>interact</b> /ˌɪntərˈækt/ nhấn âm 3. skyscraper /ˈskaɪskreɪpə/, livable /ˈlɪvəbl/, neighbourhood /ˈneɪbəhʊd/ nhấn âm 1.'),
    ('D', '<b>infrastructure</b> /ˈɪnfrəstrʌktʃə/ nhấn âm 1. pedestrian /pəˈdestriən/, community /kəˈmjuːnəti/, sustainable /səˈsteɪnəbl/ nhấn âm 2.'),
    ('A', 'Sau "make it more…" cần tính từ: <b>eco-friendly</b> (thân thiện môi trường), đi với "reducing heating costs".'),
    ('C', 'one of the most <b>livable</b> towns = một trong những thị trấn đáng sống nhất.'),
    ('D', 'promote <b>sustainable</b> development = thúc đẩy phát triển bền vững.'),
    ('A', '<b>urban</b> areas = các khu vực đô thị (ô nhiễm ở các khu đô thị).'),
    ('B', 'make the company <b>operate</b> more efficiently = làm cho công ty vận hành hiệu quả hơn (make + O + V).'),
    ('A', 'sound + tính từ: Tom sounded <b>angry</b> (nghe giọng tức giận).'),
    ('A', 'look + tính từ so sánh: The garden looks <b>better</b> since you tidied it up (trông đẹp hơn).'),
    ('B', 'get + tính từ: It is getting <b>good</b> (đang trở nên tốt). Đáp án theo file Word. (Dạng "better" tự nhiên hơn nhưng không có trong đề.)'),
    ('C', 'Trạng từ bổ nghĩa cho động từ tasted: tasted the meat <b>cautiously</b> (nếm cẩn thận).'),
    ('D', 'look + tính từ: she looked rather <b>worried</b> (trông khá lo lắng) vì anh ấy không đến.'),
    (['network'], 'a(n) <b>network</b> of programmable LED street lights = một mạng lưới đèn đường LED.'),
    (['urban'], 'address multiple <b>urban</b> concerns = giải quyết nhiều mối lo của đô thị.'),
    (['efficient'], 'making transportation more <b>efficient</b> = làm giao thông hiệu quả hơn (song song với "improving…").'),
    (['energy'], 'improving green <b>energy</b> = cải thiện năng lượng xanh.'),
    (['enjoyable'], 'a simpler and more <b>enjoyable</b> place to work, live and travel = nơi dễ chịu hơn. (Từ nhiễu trong bài: connect, convenience.)'),
    (['space'], 'Internet of Things (IoT) <b>space</b> = lĩnh vực/thị trường IoT dành cho người tiêu dùng.'),
    ('D', 'display (trưng bày) ≈ <b>exhibition</b> (triển lãm).'),
    ('A', 'installed (lắp đặt) ≈ <b>set up</b>.'),
    ('B', 'densely (dày đặc) ↔ <b>sparsely</b> (thưa thớt).'),
    ('C', 'pollution (ô nhiễm) ↔ <b>purity</b> (sự trong sạch).'),
    ('B', "Đồng tình với nhận xét: <b>Sure. I couldn't agree more</b> (hoàn toàn đồng ý)."),
    ('D', 'Lời rủ đi sân vận động: <b>That would be great.</b> (đồng ý).'),
    ('A', '"It\'s an opportunity to test my general knowledge" → ý kiến tích cực: <b>I think it\'s great.</b>'),
    ('A', "Đáp lại lời cảm ơn: <b>It's my pleasure.</b>"),
    ('B', 'Đáp án theo Word: <b>Why do you believe so?</b> (hỏi lý do niềm tin). Các câu còn lại không hợp ngữ cảnh.'),
    ('C', 'a four-hour <b>flight</b> from Britain = chuyến bay bốn tiếng từ Anh.'),
    ('B', 'regarded as one of the top hotels = được xem là một trong những khách sạn hàng đầu (regard … as).'),
    ('D', '<b>Although</b> Marrakech is… busiest and most modern, the influence of the Middle Ages is still evident (mệnh đề nhượng bộ).'),
    ('A', '<b>do</b> sport = chơi/tập thể thao (do sport).'),
    ('B', 'the <b>views</b> of the surrounding area are spectacular = quang cảnh xung quanh ngoạn mục.'),
    ('A', '"City planning, as an organized profession, has existed for less than a century" → <b>to have become a profession for about a hundred years</b>.'),
    ('C', '"how sustainable the cities of the future would be" → nhiệm vụ quan trọng nhất là <b>to make cities in the future sustainable</b>.'),
    ('B', 'Bài nói đèn giao thông "would be eliminated by smart driving" (bị loại bỏ), không phải "được điều khiển" → <b>B</b> sai (EXCEPT).'),
    ('D', '"sensors to monitor the water mains. Warning would be issued…" → <b>there may be no disruption to water supply</b>.'),
    ('B', 'Amy Glasmier là người hoài nghi thành phố thông minh ("skeptic… gravely oversold") → thái độ <b>doubtful</b>.'),
    (['appears'], 'appear to V (có vẻ) là động từ trạng thái → <b>appears</b> (hiện tại đơn, chủ ngữ số ít).'),
    ({'blanks': [["don't think", 'do not think'], ['knows'], ['is saying']]}, 'think/know là động từ trạng thái → <b>don\'t think</b>, <b>knows</b>; "what he is saying" (đang nói ra) → <b>is saying</b>.'),
    (['stands'], 'stand (nằm, tọa lạc – trạng thái) → The monument <b>stands</b> on a hill.'),
    ({'blanks': [['Do'], ['realise', 'realize'], ['are standing']]}, '<b>Do</b> you <b>realise</b> (realise là stative) that you <b>are standing</b> on my toe? (đang giẫm chân – hành động đang diễn ra)'),
    ({'blanks': [['says'], ['knows'], ['wonder'], ['is thinking']]}, 'say / know / wonder → hiện tại đơn (<b>says, knows, wonder</b>); "who he is thinking of" (đang nghĩ đến ai) → <b>is thinking</b>.'),
    (['a smart city has the potential to dramatically improve the current level of transportation throughout a city', 'better transportation services a smart city has the potential to dramatically improve the current level of transportation throughout a city', 'a smart city has the potential to dramatically improve the current level of transportation throughout the city'], '<b>Mẫu:</b> A smart city has the potential to dramatically improve the current level of transportation throughout a city. (have the potential to V; current level of N)'),
    (['a smart city will have the most technological advances and there will be less criminal activity', 'a smart city has the most technological advances and there is less criminal activity', 'a smart city has the most technological advances and there will be less criminal activity', 'safer communication a smart city will have the most technological advances and there will be less criminal activity'], '<b>Mẫu:</b> A smart city will have the most technological advances, and there will be less criminal activity. (thì tương lai đơn)'),
    (['since there is a limited amount of natural resources left to meet the demand of people smart cities will have technologies and the necessary tools to cut down on our usage of natural resources and decrease waste of water electricity etc without having to cut down on any factors', 'since there is a limited amount of natural resources left to meet the demand of people smart cities have technologies and the necessary tools to cut down on our usage of natural resources and decrease waste of water electricity etc without having to cut down on any factors'], '<b>Mẫu:</b> Since there is a limited amount of natural resources left to meet the demand of people, smart cities will have technologies and the necessary tools to cut down on our usage of natural resources and decrease waste of water, electricity, etc. without having to cut down on any factors.'),
    (['a smart city has thousands of energy-efficient buildings that can improve the air quality use renewable energy sources and decrease the dependence on non-renewable energy sources', 'a smart city has thousands of energy efficient buildings that can improve the air quality use renewable energy sources and decrease the dependence on non renewable energy sources'], '<b>Mẫu:</b> A smart city has thousands of energy-efficient buildings that can improve the air quality, use renewable energy sources, and decrease the dependence on non-renewable energy sources.'),
    (['a smart city will have many businesses and job opportunities since people will get equal access to basic resources such as transportation internet connection and job offers', 'a smart city will have many businesses and job opportunities because people will get equal access to basic resources such as transportation internet connection and job offers', 'a smart city has many businesses and job opportunities because people get equal access to basic resources such as transportation internet connection and job offers'], '<b>Mẫu:</b> A smart city will have many businesses and job opportunities since people will get equal access to basic resources such as transportation, internet connection, and job offers.'),
])

