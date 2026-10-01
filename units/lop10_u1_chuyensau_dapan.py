# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Unit 1 Family life (Tiếng Anh 10 Global Success) – Bộ BÀI TẬP CHUYÊN SÂU.
Quy ước:
  mcq  : chữ cái 'A'-'D' (plain: chính văn bản phương án; nhiều đáp án đúng: danh sách)
  tfng : 'T' / 'F' / 'NG'
  fill : danh sách đáp án chấp nhận (1 ô) hoặc {'blanks': [[...],[...]]} (nhiều ô)
  open : không chấm điểm, EXPLANATIONS chứa đáp án mẫu
Đáp án lấy từ khoá trong file Word (nửa sau file src/l10u1/cs_key_c.txt) rồi tự giải độc lập để đối chiếu;
những chỗ khoá Word sai/mơ hồ được liệt kê ở GHI_CHU_RA_SOAT."""

GHI_CHU_RA_SOAT = [
    'PHẠM VI: file Word gốc chứa cả Unit 2-5 và ôn tập/giữa kì; bộ này CHỈ lấy phần Unit 1 (dòng 1-1190 của cs_c.txt). Ba đề kiểm tra trong Unit 1 là Test 1, Test 2 (nhãn gốc ghi "TEST 1" lần hai) và Test 3; Test 3 (140 câu) làm trang kiểm tra tính giờ, thời gian 120 phút là do soạn giả tự đặt (Word không ghi).',
    'p3.3 (Test 2): khoá Word = B (necessary) nhưng cả bốn từ collection/necessary/explanation/reputation đều có e = /e/ nên câu có vấn đề về đề; giữ khoá Word.',
    'tv2.2 (mop / lawn / equity / resolution): khoá Word = A (mop) – mop vừa là động từ vừa là danh từ nên khá mơ hồ; giữ khoá Word.',
    'r2.5 (Test 1, bài đọc): khoá Word = A; đáp án này chỉ là lựa chọn tốt nhất trong ba phương án, nội dung bài khá khiên cưỡng.',
    'r2.6: khoá Word = B (Men); về mặt ngữ cảnh "they" cũng có thể hiểu là women – giữ khoá Word.',
    'gq1.9: "Students entering universities" (B) và "Students who enter universities" (D) đều đúng; khoá Word = D, đã chấp nhận cả B và D.',
    'gq2.5: khoá Word = A (up) – "Come over to my place" mới tự nhiên; giữ khoá Word.',
    'gq4.1: khoá Word = had been working; had worked cũng chấp nhận được (đã thêm).',
    'wq1.3: đề ghi "said to you" nhưng khoá Word là "me for helping him"; đã chấp nhận cả thanked you / thanked me.',
    'w3.8: khoá Word bị lỗi gõ ("made the confess"); đáp án đúng "He was made to confess after three days."',
    'kt.37: duties ~ chores (D, khoá Word) nhưng jobs (C) cũng gần nghĩa; giữ khoá Word D.',
    'kt.52: khoá Word = D (use); "are using" (B) cũng chấp nhận được với nowadays nên đã chấp nhận cả B và D.',
    'kt.56: khoá Word = B (is always talking – phàn nàn); "always talks" (C) cũng đúng ngữ pháp nên đã chấp nhận cả B và C.',
    'kt.82: khoá Word = A (will hold) – thực ra "will hold" không sai ngữ pháp, ý đề muốn "are holding" (kế hoạch đã sắp xếp); giữ khoá Word, câu có vấn đề.',
    'kt.84: khoá Word = C (will be) – "annual event" là sự thật nên dùng is; giữ khoá Word.',
    'kt.94: khoá Word = A ("I didn\'t, either.") là phương án ít sai nhất, nghĩa hơi gượng.',
    'kt.100: khoá Word = C; các phương án đều không lí tưởng.',
    'kt.129: khoá Word = D (Strong families build a wealthy society) nhưng bài đọc không nói về "wealthy"; bài đọc nêu mọi thành viên phải gương mẫu → đáp án đúng là C (Family members have responsibilities to set good examples). ĐÃ ĐỔI KHOÁ SANG C.',
    'kt.134: khoá Word = B (urged); "begged" (C) cũng hợp với "cried out" nên đã chấp nhận cả B và C.',
    'Lỗi nguồn đã sửa: kt.121 bị đánh số trùng (121, 121, 122) → đánh lại 119-123; "I28" → 128; nhiều lỗi OCR trong bài đọc Test 3 (Hinnly → Family, w hole → whole, ot → of, lor → for, fry → try); "A.will boil" thiếu khoảng trắng; "fatory" → factory; "last roads" → fast roads; "Tct" → Tet; "hale" → hate; kt.139 "red." → "red,"; dấu ngoặc kép của kt.91.',
    'Test 1 phần viết (II. Write a paragraph) chỉ có trong file khoá, đã thêm vào đề dạng câu mở (bài mẫu lấy từ khoá).',
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


# ============================================================ PHÁT ÂM & TRỌNG ÂM
put('p1', [
    ('A', '<b>responsible</b> /rɪˈspɒnsəbl/ (o = /ɒ/). homemaker /ˈhəʊmmeɪkə/, mow /məʊ/, overworked /ˌəʊvəˈwɜːkt/ có o = /əʊ/.'),
    ('A', '<b>bathe</b> /beɪð/ (a = /eɪ/). finance /ˈfaɪnæns/, program /ˈprəʊɡræm/, cat /kæt/ có a = /æ/.'),
    ('B', '<b>routine</b> /ruːˈtiːn/ (i = /iː/). lifting /ˈlɪftɪŋ/, split /splɪt/, divide /dɪˈvaɪd/ có i = /ɪ/.'),
    ('D', '<b>iron</b> /ˈaɪən/ (o = /ə/, câm). clothes /kləʊðz/, fold /fəʊld/, groceries /ˈɡrəʊsəriz/ có o = /əʊ/.'),
    ('A', '<b>duty</b> /ˈdjuːti/ (u = /juː/). clusters /ˈklʌstəz/, rubbish /ˈrʌbɪʃ/, washing-up /ˌwɒʃɪŋ ˈʌp/ có u = /ʌ/.'),
])
put('p2', [
    ('A', '<b>private</b> /ˈpraɪvət/ nhấn âm 1. provide /prəˈvaɪd/, arrange /əˈreɪndʒ/, advise /ədˈvaɪz/ nhấn âm 2.'),
    ('A', '<b>resurface</b> /ˌriːˈsɜːfɪs/ nhấn âm 2 (động từ). knowledge /ˈnɒlɪdʒ/, technical /ˈteknɪkl/, export (danh từ) /ˈekspɔːt/ nhấn âm 1.'),
    ('B', '<b>entertainment</b> /ˌentəˈteɪnmənt/ nhấn âm 3. medical /ˈmedɪkl/, atmosphere /ˈætməsfɪə/, suburb /ˈsʌbɜːb/ nhấn âm 1.'),
    ('D', '<b>expertise</b> /ˌekspɜːˈtiːz/ nhấn âm 3. recipe /ˈresəpi/, cinema /ˈsɪnəmə/, similar /ˈsɪmələ/ nhấn âm 1.'),
    ('C', '<b>procedure</b> /prəˈsiːdʒə/ nhấn âm 2. indicate /ˈɪndɪkeɪt/, forefinger /ˈfɔːfɪŋɡə/, enemy /ˈenəmi/ nhấn âm 1.'),
])
put('p3', [
    ('B', '<b>Islam</b> /ɪzˈlɑːm/ hoặc /ˈɪzlɑːm/ (a = /ɑː/). Tamil /ˈtæmɪl/, reaction /riˈækʃn/, gather /ˈɡæðə/ có a = /æ/.'),
    ('A', '<b>official</b> /əˈfɪʃl/ (o = /ə/). mosque /mɒsk/, optional /ˈɒpʃənl/, tropical /ˈtrɒpɪkl/ có o = /ɒ/.'),
    ('B', 'Khoá Word chọn <b>necessary</b>. Lưu ý: cả bốn từ (collection, necessary, explanation, reputation) đều có e đọc /e/, nên câu có vấn đề về đề – giáo viên cần kiểm tra lại.'),
    ('C', '<b>impression</b> /ɪmˈpreʃn/ (ss = /ʃ/). casual /ˈkæʒuəl/, occasion /əˈkeɪʒn/, usually /ˈjuːʒuəli/ có s = /ʒ/.'),
    ('D', '<b>campus</b> /ˈkæmpəs/ (u = /ə/). compulsory /kəmˈpʌlsəri/, adult /ˈædʌlt/, publish /ˈpʌblɪʃ/ có u = /ʌ/.'),
])
put('p4', [
    ('C', '<b>income</b> (danh từ) /ˈɪnkʌm/ nhấn âm 1. deny /dɪˈnaɪ/, remote /rɪˈməʊt/, unique /juˈniːk/ nhấn âm 2.'),
    ('D', '<b>tuition</b> /tjuˈɪʃn/ nhấn âm 2 (trước -ion). nature /ˈneɪtʃə/, subject /ˈsʌbdʒekt/, scenery /ˈsiːnəri/ nhấn âm 1.'),
    ('A', '<b>admire</b> /ədˈmaɪə/ nhấn âm 2. Internet /ˈɪntənet/, violent /ˈvaɪələnt/, website /ˈwebsaɪt/ nhấn âm 1.'),
    ('B', '<b>linguistics</b> /lɪŋˈɡwɪstɪks/ nhấn âm 2. government /ˈɡʌvənmənt/, territory /ˈterətri/, journalism /ˈdʒɜːnəlɪzəm/ nhấn âm 1.'),
    ('D', '<b>informative</b> /ɪnˈfɔːmətɪv/ nhấn âm 2. mausoleum /ˌmɔːsəˈliːəm/, vegetarian /ˌvedʒəˈteəriən/, intermediate /ˌɪntəˈmiːdiət/ nhấn âm 3.'),
])

# ============================================================ THÌ HIỆN TẠI ĐƠN (cơ bản)
put('hs1', [
    (['teaches'], 'Chủ ngữ Mr. Nam (ngôi 3 số ít) + often → HTĐ; teach tận cùng -ch nên thêm -es: <b>teaches</b>.'),
    (['throw'], 'Chủ ngữ We + always → HTĐ, động từ giữ nguyên: <b>throw</b>.'),
    (['stops'], 'The referee (số ít) + usually → <b>stops</b>.'),
    (['hurry'], 'The children (số nhiều) → HTĐ giữ nguyên: <b>hurry</b>.'),
    (['speaks'], 'He (ngôi 3 số ít) → <b>speaks</b>.'),
])
put('hs2', [
    (["When does Daisy go to school?", "What days does Daisy go to school?", "Which days does Daisy go to school?", "On which days does Daisy go to school?"],
     'Phần gạch chân chỉ thời gian → hỏi <b>When</b> (hoặc What/Which days); mượn does, động từ về nguyên mẫu. Mẫu: When does Daisy go to school?'),
    (["What does your father have in the garden?", "What does his father have in the garden?", "What does my father have in the garden?"],
     'Phần gạch chân "a cage" là vật → <b>What</b> + does + S + have? Mẫu: What does your father have in the garden?'),
    (["Why do the children like dogs?"], 'Phần gạch chân chỉ lí do (because…) → <b>Why</b> + do + the children + like dogs?'),
    (["Who is never late?"], 'Phần gạch chân là chủ ngữ chỉ người → <b>Who</b> + is never late? (không đảo, không mượn trợ động từ).'),
    (["How much does Mike's new mountain bike cost?"], 'Phần gạch chân chỉ giá tiền → <b>How much</b> + does + S + cost?'),
])
put('hs3', [
    (['plays'], 'Nick (số ít) → <b>plays</b> (play baseball).'),
    (['drink'], 'I never → <b>drink</b> coffee (không thêm s).'),
    (['opens'], 'The swimming pool (số ít) → <b>opens</b> (giờ mở cửa, lịch cố định).'),
    (['closes'], 'It closes at 9.00 in the evening – đối lập với "opens" ở câu trước.'),
    (['causes'], 'Bad driving (số ít) → <b>causes</b> many accidents.'),
    (['live'], 'My parents (số nhiều) → <b>live</b> in a very small house.'),
    (['take'], 'The Olympic Games (số nhiều) <b>take</b> place = diễn ra, sự thật lặp lại bốn năm một lần.'),
    (['do'], 'They always <b>do</b> their homework (do homework = làm bài tập).'),
    (['speak'], 'My students (số nhiều) → <b>speak</b> a little French.'),
    (['wake up'], 'I always <b>wake up</b> early in the morning – thói quen hằng ngày.'),
])
put('hs4', [
    (['every', 'each'], 'every day = hằng ngày (thói quen).'),
    (['in'], 'in the mornings = vào các buổi sáng.'),
    (['makes', 'prepares', 'cooks'], 'Mr. John (số ít) <b>makes</b> the breakfast = làm bữa sáng.'),
    (["don't", 'do not'], 'Câu phủ định: They both <b>don\'t</b> like drinking milk (chủ ngữ số nhiều).'),
    (['takes'], 'takes Bobby out to the park = dắt Bobby ra công viên; Mr. John số ít nên thêm s.'),
    (['is'], 'Mr. John <b>is</b> a graphic designer.'),
    (["isn't", 'is not'], 'He <b>isn\'t</b> an office worker – vế sau nói anh làm việc ở nhà.'),
    (['works'], 'He <b>works</b> from home (làm việc tại nhà).'),
    (['has'], 'have lunch → He <b>has</b> lunch (ngôi 3 số ít).'),
    (['at'], 'at half past twelve = vào lúc 12 giờ 30.'),
    (["doesn't", 'does not'], 'Then he <b>doesn\'t</b> start work immediately = anh không bắt đầu làm ngay.'),
    (['plays'], 'He <b>plays</b> with Bobby instead = thay vào đó anh chơi với Bobby.'),
    (['finishes', 'stops'], 'starts work again and <b>finishes</b> in the evening.'),
    (['eat', 'have'], 'They both (số nhiều) <b>eat</b> meat for dinner.'),
    (['watches'], 'He always <b>watches</b> his favorite TV show (số ít, always).'),
    (['at'], 'at night = vào ban đêm.'),
])
put('hs5', [
    ('A', '"keeps trying … but fails every time" → thói quen lặp lại, HTĐ: <b>keeps</b> (keep trying = cứ cố).'),
    ('C', 'never + HTĐ; chủ ngữ I → <b>travel</b> (động từ nguyên mẫu).'),
    ('A', 'Hai vế đều là thói quen: never takes / always does (does thay cho takes). Không dùng "never doesn\'t" (phủ định kép).'),
    ('D', 'Câu hỏi với have (sở hữu) trong HTĐ: <b>Do you have</b> the car keys?'),
    ('D', 'a train service <b>operates</b> = dịch vụ tàu hoạt động; takes/works/functions không hợp.'),
])

# ============================================================ THÌ HIỆN TẠI TIẾP DIỄN (cơ bản)
put('hc1', [
    (['is reading'], 'at the moment → HTTD: <b>is reading</b>.'),
    (B('are', 'laughing'), 'Câu hỏi HTTD: Why <b>are</b> you <b>laughing</b>? (laugh → laughing).'),
    (['am working'], 'now → HTTD: I <b>am working</b>.'),
    (['is raining'], 'Oh no! … again → đang xảy ra: It <b>is raining</b>.'),
    (B('Are', 'watching'), 'Câu hỏi HTTD: <b>Are</b> you <b>watching</b> the TV…?'),
    (B('is learning', 'is teaching'), 'at the moment → Bill <b>is learning</b>; His father <b>is teaching</b> him.'),
    (['are having'], 'Listen! → đang xảy ra: The neighbors <b>are having</b> an argument (have an argument = cãi nhau, không phải sở hữu).'),
    (['is wearing'], 'today → tạm thời: Sally <b>is wearing</b> her new T-shirt.'),
    (B('are', 'doing'), 'What <b>are</b> you <b>doing</b> here?'),
    (['am not sleeping'], 'at the moment → I <b>am not sleeping</b> very well.'),
])
put('hc2', [
    ('believe', 'believe là động từ chỉ trạng thái (stative) nên không chia tiếp diễn: I <b>believe</b>.'),
    ('is jumping', 'Look! → hành động đang xảy ra: Bin <b>is jumping</b>.'),
    ('think', 'think = cho rằng (ý kiến) → HTĐ: I <b>think</b> you\'re crazy.'),
    ('hates', 'hate là stative, không dùng tiếp diễn: She <b>hates</b> it.'),
    ('am going', 'next Thursday → kế hoạch đã sắp xếp: I <b>am going</b> to New York.'),
    ('go', 'Once a week → thói quen: I <b>go</b> to an English class.'),
    ('have', 'every day → thói quen: I <b>have</b> lunch in the cafeteria.'),
    ('drives', 'David is rich → thông tin lâu dài/thói quen: he <b>drives</b> a Mercedes.'),
    ('is studying', 'right now → đang xảy ra: He <b>is studying</b> in the library.'),
    ('is snowing', 'quite hard, tonight → đang xảy ra: It <b>is snowing</b>.'),
])

# ============================================================ HTĐ & HTTD
put('hk1', [
    (['is having'], 'at the moment → HTTD; have a holiday = động từ hành động nên chia tiếp diễn: <b>is having</b>.'),
    (['is barking'], 'again, tình huống đang xảy ra → <b>is barking</b>.'),
    (['gets'], 'every morning → HTĐ: Ann <b>gets</b> up.'),
    (['goes'], 'Then she <b>goes</b> – chuỗi thói quen hằng ngày.'),
    (['drives'], 'Then she <b>drives</b> to the beach and stays all day (chuỗi thói quen).'),
    (["doesn't work", 'does not work'], 'Sự việc kéo dài/thói quen (won the lottery) → HTĐ phủ định: She <b>doesn\'t work</b>.'),
    (['are you learning'], 'this year → tạm thời, HTTD: Why <b>are you learning</b> English this year?'),
    (['am living'], 'for two months, tình huống tạm thời → <b>am living</b>.'),
    (['are you wearing'], 'now (đang mặc gì) → <b>are you wearing</b>.'),
    (['is cooking'], 'Kate is in the kitchen (đang) → <b>is cooking</b>.'),
])
put('hk2', [
    (['is listening'], 'Where\'s Tim? (đang ở đâu) → đang xảy ra: <b>is listening</b>.'),
    (['rains'], 'always + sự thật về thời tiết ở London → HTĐ: <b>rains</b>.'),
    (B('works', "isn't working"), 'all day (thói quen) → <b>works</b>; at the moment → <b>isn\'t working</b>.'),
    (B('is running', 'wants'), 'Look! → <b>is running</b>; want là stative → <b>wants</b>.'),
    (B('speaks', 'comes'), 'Sự thật/thông tin lâu dài → HTĐ: <b>speaks</b>, <b>comes</b>.'),
    (B('is coming', 'are meeting'), 'Look! → <b>is coming</b>; in an hour (kế hoạch đã sắp xếp) → <b>are meeting</b>.'),
    (B('Do', 'go', 'do', 'stay'), 'usually → HTĐ nghi vấn: <b>Do</b> you usually <b>go</b> away … or <b>do</b> you <b>stay</b> at home?'),
    (B('is holding', 'smell'), 'hold = hành động đang diễn ra → <b>is holding</b>; smell chỉ trạng thái → <b>smell</b>.'),
    (B('is snowing', 'snows'), 'Look! → <b>is snowing</b>; always (thói quen/khí hậu) → <b>snows</b>.'),
    (B('swims', "doesn't run"), 'Khả năng/thói quen → HTĐ: <b>swims</b>, <b>doesn\'t run</b>.'),
])
put('hk3', [
    (['are'], 'Lisa and her friends <b>are</b> studying (HTTD, chủ ngữ số nhiều).'),
    (['now'], 'right now = ngay bây giờ.'),
    (['is'], 'Mary <b>is</b> helping the others.'),
    (["isn't", 'is not'], 'She <b>isn\'t</b> studying Maths; she is reading a book.'),
    (['reading'], 'She is <b>reading</b> a book (không học Toán nữa).'),
    (["aren't", 'are not'], 'They <b>aren\'t</b> talking loudly because they are at the library.'),
    (['moment'], 'at the <b>moment</b> = lúc này.'),
    (['surfing'], 'surf the net = lướt mạng.'),
    (['trying'], 'They are <b>trying</b> to solve her exercises.'),
    (['helping'], 'They are all <b>helping</b> each other.'),
])

# ============================================================ NÂNG CAO
put('hn1', [
    ('are killing', 'These (shoes) are killing me = đau chân lúc này; kill ở đây là động từ hành động đang xảy ra.'),
    ('am not reading', 'now (hiện giờ) + tạm thời → HTTD phủ định.'),
    ('love', 'love là stative, không dùng tiếp diễn.'),
    ('is moving', 'next month: kế hoạch đã sắp xếp → HTTD (cũng có thể HTĐ lịch trình, nhưng khoá chọn is moving).'),
    ('gives', 'every Wednesday → thói quen/lịch cố định → HTĐ.'),
    ('is always interrupting', 'always + HTTD diễn tả thói quen gây khó chịu (so irritating).'),
    ('are you busy', 'busy ở đây là trạng thái → <b>are you busy</b> (không dùng are you being busy).'),
    ('hate', 'hate là stative → HTĐ.'),
])
put('hn2', [
    (['am studying'], 'tạm thời (in New York… at a school) → <b>am studying</b>.'),
    (['is lying'], 'At the moment → <b>is lying</b> (lie → lying).'),
    (['work'], 'usually → <b>work</b>.'),
    (['rains'], 'always + thời tiết ở Huế → HTĐ: <b>rains</b>.'),
    (B('are saying', 'is talking'), 'đang xảy ra lúc nói: what you <b>are saying</b>; everyone <b>is talking</b>.'),
    (['is currently writing'], 'currently → HTTD: <b>is currently writing</b>.'),
    (['Do you want'], 'want là stative, mời lịch sự → HTĐ: <b>Do you want</b> to come…?'),
    (['makes'], 'A famous company (số ít) → HTĐ sự thật: <b>makes</b>.'),
    (['have'], 'have = sở hữu → HTĐ: I <b>have</b> two tickets.'),
    (['am holding'], 'hold = đang cầm → <b>am holding</b>.'),
    (B('makes', "doesn't make"), 'Sự thật về công ty: <b>makes</b> … <b>doesn\'t make</b>.'),
    (['is falling'], 'At present → <b>is falling</b>.'),
    (['are becoming'], 'these days, thay đổi dần → <b>are becoming</b>.'),
    (['needs'], 'Everyone (số ít) + need là stative → <b>needs</b>.'),
    (["doesn't taste", 'does not taste'], 'taste (có vị) là stative → <b>doesn\'t taste</b>.'),
    (['am seeing'], 'This afternoon = kế hoạch đã hẹn → <b>am seeing</b>.'),
    (['sounds'], 'sound là stative → <b>sounds</b>.'),
    (B('reads', 'think', 'is reading'), 'normally → <b>reads</b>; think (ý kiến) → <b>think</b>; right now → <b>is reading</b>.'),
    (['take'], 'Chân lí chung: people (số nhiều) → <b>take</b> (câu bắt đầu bằng "It is strange that…").'),
    (['does your brother do'], 'Hỏi nghề nghiệp: What <b>does your brother do</b> for a living?'),
])
put('hn3', [
    (['play'], 'always + Saturdays → <b>play</b> badminton.'),
    (['is finishing'], 'now → đang hoàn thành: <b>is finishing</b>.'),
    (['are enjoying'], 'enjoy oneself: đang tận hưởng, They <b>are enjoying</b> themselves in Hawaii.'),
    (['prefer'], 'prefer là stative → <b>prefer</b>.'),
    (['know'], 'know là stative → I <b>know</b> the answer.'),
    (['is waiting'], 'đang chờ (he is in his office) → <b>is waiting</b>.'),
    (['am interviewing'], 'tomorrow: kế hoạch đã sắp xếp → <b>am interviewing</b>.'),
    (['works'], 'My brother (số ít), công việc thường xuyên → <b>works</b>.'),
    (['is talking'], 'Who <b>is talking</b> to John? – đang nói chuyện.'),
    (['seems'], 'seem là stative → <b>seems</b>.'),
])
put('hn4', [
    (['are going'], 'Next week → kế hoạch đã sắp xếp: <b>are going</b>.'),
    (['am organizing'], 'Kế hoạch đã sắp xếp: <b>am organizing</b> (organise cũng được).'),
    (['like'], 'like là stative → <b>like</b>.'),
    (['has'], 'have (sở hữu) → Tom <b>has</b> a big car.'),
    (['is planning'], 'Kế hoạch đã sắp xếp → <b>is planning</b>.'),
    (['is bringing'], 'Kế hoạch đã sắp xếp → <b>is bringing</b>.'),
    (['goes'], 'every year → <b>goes</b>.'),
    (['has'], 'have (sở hữu) → <b>has</b>.'),
    (['thinks'], 'think (ý kiến) → <b>thinks</b>.'),
    (['is taking'], 'instead; kế hoạch tuần sau → <b>is taking</b>.'),
])

# ============================================================ TỪ VỰNG (Test 1 – B)
put('tv1', [
    ('e', 'set the table = dọn/bày bàn ăn (đáp án e).'),
    ('a', 'mop the floor = lau sàn nhà (đáp án a).'),
    ('d', 'feed the baby = cho em bé ăn (đáp án d).'),
    ('b', 'water the houseplants = tưới cây trong nhà (đáp án b).'),
    ('c', 'do the heavy lifting = làm việc nặng, mang vác (đáp án c).'),
])
put('tv2', [
    ('D', '<b>financial</b> là tính từ; satisfaction, household chore, breadwinner đều là danh từ.'),
    ('A', 'Khoá Word chọn <b>mop</b> (lau nhà – dụng cụ/hành động làm việc nhà, khác nhóm danh từ trừu tượng/khái niệm lawn, equity, resolution). Câu hơi mơ hồ vì mop cũng là danh từ.'),
    ('C', '<b>overworked</b> là tính từ; split, bathe, tidy là động từ.'),
    ('C', '<b>houseplant</b> là cây trồng trong nhà; housekeeper, housewife, homemaker đều chỉ người làm việc nhà.'),
    ('B', '<b>marital</b> (thuộc hôn nhân) là tính từ; conflict, chore, finance là danh từ.'),
])
put('tv3', [
    ('A', 'be responsible for + V-ing = chịu trách nhiệm về. B, C sai cấu trúc ("is … takes", "is … take").'),
    ('A', 'manage household finances = quản lí tài chính gia đình.'),
    ('D', 'Mẹ làm nhiều việc nhà hơn bố → chia việc không đều: B (split unequally) và C (don\'t share equally) đều đúng → D.'),
    ('D', 'marital satisfaction = sự hài lòng trong hôn nhân (collocation).'),
    ('D', 'chore equity = sự công bằng trong việc nhà.'),
    ('D', 'homemaker và house husband đều chỉ người đàn ông ở nhà nội trợ → D.'),
    ('A', 'conflict resolution skills = kĩ năng giải quyết xung đột.'),
    ('A', 'seeds must be watered = hạt giống phải được tưới nước để nảy mầm.'),
])
put('tv4', [
    (['doing the cooking', 'do the cooking'], 'Cả nhà ăn ngoài nên mẹ không nấu ăn: is not <b>doing the cooking</b>.'),
    (['doing the shopping', 'do the shopping'], 'Ông bị ốm nên không đi chợ: is not <b>doing the shopping</b>.'),
    (['folding the clothes', 'fold the clothes'], 'Ngày mai về quê nên đang gấp quần áo và thu dọn đồ: is <b>folding the clothes</b>.'),
    (['watering the houseplants', 'water the houseplants'], 'Phòng khách bị ướt vì em đang tưới cây: is <b>watering the houseplants</b>.'),
    (['doing the laundry', 'do the laundry'], 'Muốn có máy giặt vì chán giặt đồ mỗi ngày: tired of <b>doing the laundry</b>.'),
    (['do the washing-up', 'do the washing up'], 'help (to) <b>do the washing-up</b> after parties = giúp rửa bát sau tiệc.'),
    (['take out the garbage', 'take out the rubbish'], 'Nhà bếp bốc mùi → Don\'t you <b>take out the garbage</b>? (đổ rác).'),
    (['mop the house', 'mop the floor'], 'Nhà bẩn → Why don\'t you <b>mop the house</b>? (lau nhà).'),
])
put('tv5', [
    ('B', 'homemaker = người nội trợ → dành phần lớn thời gian chăm sóc gia đình.'),
    ('B', 'overworked = làm việc quá sức → không còn thời gian lo việc nhà.'),
    ('C', 'Chuẩn bị ăn tối → rửa tay cẩn thận trước khi ăn.'),
    ('A', 'lay the table = dọn bàn ăn → đã đến giờ ăn.'),
    ('A', 'Trời mưa → vội thu quần áo phơi vào (put away the clothes).'),
    ('B', 'breadwinner = người trụ cột kiếm tiền → Sarah làm việc chăm chỉ để nuôi gia đình.'),
    ('A', 'chore equity = chia đều việc nhà → họ làm việc nhà ngang nhau.'),
    ('B', 'heavy lifting = việc nặng → sửa mái nhà.'),
])
put('tv6', [
    ('cook', 'Hình người phụ nữ đang thái rau, nấu ăn → cook.'),
    ('do the shopping', 'Hình hai người đẩy xe hàng đầy đồ → do the shopping (đi chợ/mua sắm).'),
    ('feed the cat', 'Hình bàn tay đưa thức ăn cho mèo → feed the cat.'),
    ('do the washing-up', 'Hình mẹ và con rửa bát ở bồn rửa → do the washing-up.'),
    ('lay the table', 'Hình người đang bày bát đĩa lên bàn → lay the table.'),
    ('bathe the baby', 'Hình tắm cho em bé → bathe the baby.'),
])
put('tv7', [
    ('A', 'Hình tắm cho em bé sơ sinh → A. B (đi bơi) và C (lắc em bé) không khớp tranh.'),
    ('A', 'Hình cậu bé đổ rác vào thùng → The man/boy is taking out the rubbish.'),
    ('B', 'Hình gấp áo bằng dụng cụ gấp → Clothes are being folded neatly.'),
    ('C', 'Hình cậu bé đẩy máy cắt cỏ → mow the lawn.'),
    ('B', 'Hình mẹ và con gái mang găng tay lau dọn → The girl is doing some cleaning with her mother.'),
])

# ============================================================ NGỮ PHÁP TEST 1 (1)
put('gp1', [
    ('A', 'twice a week → thói quen: <b>play</b>.'),
    ('B', 'every morning → thói quen, nghi vấn HTĐ: <b>Do you have</b> breakfast…?'),
    ('B', 'so they have to cancel today → đang mưa: <b>is raining</b>.'),
    ('A', 'Thông tin/khả năng lâu dài → <b>speaks</b> three languages.'),
    ('A', 'know là stative → <b>don\'t know</b>.'),
    ('B', 'Listen! → đang xảy ra: <b>is playing</b>.'),
    ('A', 'like là stative → <b>Do you like</b>…?'),
    ('A', 'Hai hành động đang diễn ra cùng lúc: <b>I am not laughing, I am crying</b>.'),
])
put('gp2', [
    (['leave'], 'every morning → <b>leave</b>.'),
    (B('works', 'is doing'), 'Thường lệ → <b>works</b>; at the moment → <b>is doing</b>.'),
    (['cleans'], 'every weekend → <b>cleans</b>.'),
    (B('tries', 'plays'), 'Mọi trận đấu (thói quen) → <b>tries</b>, <b>plays</b>.'),
    (['are sitting'], 'Đang xảy ra (Excuse me) → <b>are sitting</b>.'),
    (['Do you listen'], 'very often → HTĐ nghi vấn: <b>Do you listen</b>…?'),
    (['am writing'], 'now → <b>am writing</b>.'),
    (['do they drive'], 'Sự thật chung → <b>do they drive</b> on the left in Britain?'),
    (B('rains', "isn't raining"), 'usually → <b>rains</b>; now → <b>isn\'t raining</b>.'),
    (['am baking'], 'at the moment → <b>am baking</b>.'),
])
put('gp3', [
    ('Correct', 'have a bath là hành động (không phải stative) nên dùng tiếp diễn được: đúng.'),
    ('Incorrect', 'hate là stative, không chia tiếp diễn → He <b>hates</b> doing the heavy lifting.'),
    ('Correct', 'always + HTĐ: thói quen, đúng.'),
    ('Incorrect', 'know là stative → …because she <b>doesn\'t know</b> how to cook.'),
    ('Incorrect', 'today (tạm thời) → …so my brother <b>is doing</b> it.'),
    ('Incorrect', 'believe là stative → She <b>believes</b> that men have to do housework as well.'),
    ('Correct', 'Việc đang làm tạm thời (for Christmas) → HTTD, đúng.'),
    ('Incorrect', 'every morning → chuỗi thói quen → …and then we <b>have</b> coffee…'),
    ('Incorrect', 'Sometimes + understand (stative) → I <b>watch</b> … but I <b>don\'t understand</b>.'),
    ('Incorrect', 'today (hôm nay khác thường) → You <b>aren\'t eating</b> much today.'),
])

# ============================================================ NGỮ PHÁP TEST 1 (2)
put('gp4', [
    (['take'], 'usually (thói quen) → <b>take</b> the bus.'),
    (['is shopping'], 'now → <b>is shopping</b> for groceries.'),
    (['do'], 'every Saturday → <b>do</b> the laundry.'),
    (["don't split", 'do not split'], 'Mình Ann làm hết việc → họ <b>don\'t split</b> housework.'),
    (['has'], 'have sb + V-ed: Kate always <b>has</b> her dog fed by her neighbor (nhờ hàng xóm cho chó ăn).'),
    (['is preparing'], 'today (khác thường) → my husband <b>is preparing</b> dinner.'),
    (['take out'], 'every day → <b>take out</b> the garbage.'),
    (['does'], 'rarely + HTĐ → she rarely <b>does</b> the heavy lifting.'),
])
put('gp5', [
    (['has'], 'Chủ ngữ she (số ít) → <b>has</b> to be.'),
    (['does'], 'do the washing-up (không dùng make) → <b>does</b>.'),
    (['am preparing'], 'today (My mom is busy today) → tạm thời: <b>am preparing</b>.'),
    (['am going'], 'this week (tạm thời) → <b>am going</b> by bus.'),
    (['are'], 'the elderly = những người già (số nhiều) → <b>are</b> sent.'),
])
put('gp6', [
    ('A', 'always + HTTD = phàn nàn: Why <b>are</b> you always <b>crying</b> over spilt milk?'),
    ('B', 'Sự thật, thói quen lâu dài → They <b>keep</b> us healthy.'),
    ('A', 'remind là stative → she <b>reminds</b> me of an old friend.'),
    ('B', 'mean là stative → What <b>do</b> you <b>mean</b>?'),
    ('C', 'Lịch trình tàu → HTĐ: What time <b>does</b> the train … <b>leave</b>?'),
    ('B', 'Ý kiến → <b>think</b>.'),
    ('B', 'Felix is very rich → thói quen/sự thật: <b>drives</b> a Mercedes.'),
    ('A', 'Only when + HTĐ (sau when không dùng tương lai): <b>feels</b> truly sorry.'),
    ('C', 'smell (có vẻ/mùi) là stative → It <b>smells</b> good.'),
    ('C', 'Lời hứa thực hiện ngay khi nói (performative) → I <b>promise</b>.'),
])
put('gp7', [
    (['are not watching', "aren't watching"], 'Bây giờ (must be in bed now) → HTTD phủ định: <b>aren\'t watching</b>.'),
    (['need'], 'need là stative → I <b>need</b> your help now.'),
    (['Do you have'], 'have (sở hữu) → HTĐ nghi vấn: <b>Do you have</b> a map…?'),
    (["don't have", 'do not have'], 'have (sở hữu) → <b>don\'t have</b> time now.'),
    (['calls'], 'In case + HTĐ, someone (số ít) → <b>calls</b>.'),
])
put('gp8', [
    ('B', 'HTĐ "on Thursdays" = thói quen mỗi thứ Năm → I meet Alex every Thursday.'),
    ('A', 'John\'s being weird = tạm thời cư xử lạ → hôm nay John không như bình thường.'),
    ('A', 'Do you smoke? hỏi về thói quen hút thuốc.'),
    ('B', 'is starting + giờ cụ thể = sự việc đã sắp xếp → buổi tiệc được ấn định lúc 6 giờ tối nay.'),
    ('C', 'HTĐ "it rains all day" = nhận xét chung/thói quen khí hậu → theo tôi nước Anh mưa nhiều.'),
])

# ============================================================ NGỮ PHÁP TEST 2
put('gq1', [
    ('C', 'If-clause loại 2: If + S + <b>were</b> (mọi ngôi).'),
    ('D', 'recently → hiện tại hoàn thành: <b>has bought</b>.'),
    ('A', 'not only … but also …: Nam <b>not only</b> speaks Chinese but also speaks Japanese.'),
    ('A', 'Hai mệnh đề nguyên nhân – kết quả: …, <b>so</b> we can\'t go camping.'),
    ('C', 'Mệnh đề quan hệ chỉ người, làm chủ ngữ: Mrs. Hoa <b>who</b> sings…'),
    ('C', 'enjoy + V-ing.'),
    ('A', '<b>on time</b> = đúng giờ (in time = kịp lúc).'),
    ('C', '<b>As</b> a kind of everlasting energy = với tư cách là.'),
    (['B', 'D'], 'Rút gọn mệnh đề quan hệ chủ động: Students <b>entering</b> universities = Students <b>who enter</b> universities (cả B và D đều đúng; khoá Word chọn D).'),
    ('C', 'Rút gọn hai mệnh đề cùng chủ ngữ: <b>Feeling</b> tired, I went to bed early.'),
    ('B', 'Either … or …: động từ hòa với chủ ngữ gần nhất (his brothers – số nhiều) → <b>have stolen</b>.'),
    ('B', 'as well as: động từ hòa với chủ ngữ đứng trước (my dog – số ít) → <b>eats</b>.'),
    ('C', 'Câu mệnh lệnh khẳng định → câu hỏi đuôi <b>will you?</b>'),
    ('D', 'advise sb <b>to V</b>.'),
    ('B', 'wish + quá khứ hoàn thành (tiếc nuối về quá khứ): I wish you <b>had come</b>.'),
])
put('gq2', [
    ('C', 'prefer V-ing <b>to</b> V-ing (không dùng than).'),
    ('B', 'have more <b>freedom</b> to participate (danh từ, không phải tính từ free).'),
    ('C', 'have sb + V (nguyên mẫu): had the gardener <b>plant</b>.'),
    ('B', 'The church <b>which</b> we are going to visit (visit cần tân ngữ, where thừa).'),
    ('A', 'Khoá Word chọn <b>up</b>: Come <b>over</b> to my place mới là cách dùng chuẩn.'),
])
put('gq3', [
    (['generosity'], 'treat sb with + danh từ: generous → <b>generosity</b>.'),
    (['poverty'], 'living in + danh từ: poor → <b>poverty</b> (cảnh nghèo).'),
    (['economical'], 'more … than: tính từ economy → <b>economical</b> (tiết kiệm).'),
    (['competitors'], 'How many + danh từ số nhiều chỉ người: compete → <b>competitors</b>.'),
    (['traditionally'], 'Housework has … been regarded: trạng từ <b>traditionally</b>.'),
])
put('gq4', [
    (['had been working', 'had worked'], 'I was tired when I got home → hành động kéo dài trước đó: <b>had been working</b> all day.'),
    (["haven't met", 'have not met'], 'yet → hiện tại hoàn thành phủ định: <b>haven\'t met</b>.'),
    (["didn't John want", 'did John not want'], 'last Sunday → quá khứ đơn nghi vấn phủ định: Why <b>didn\'t John want</b>…?'),
    (['are made'], 'Bị động HTĐ (clothes là số nhiều): <b>are made</b> from special materials.'),
    (['had left'], 'Điều kiện loại 3: if + quá khứ hoàn thành → <b>had left</b>.'),
])

# ============================================================ ĐỌC HIỂU – TEST 1
put('r1', [
    (['chore division'], 'Đoạn 1: "without a clear or equal <b>chore division</b>".'),
    (['gender equality'], 'Đoạn 1: "a slap in the face for <b>gender equality</b>".'),
    (['contractual relationship'], 'Đoạn 2: "turn their marriage into a business or <b>contractual relationship</b>".'),
    (['conflict resolution skills', 'conflict resolution skill'], 'Đoạn 2: "encourage conflicts rather than <b>conflict resolution skills</b>".'),
    (['marital satisfaction'], 'Đoạn 3: "report more <b>marital satisfaction</b>".'),
    (['well-being', 'well being', 'wellbeing'], 'Đoạn 4: "greater <b>well-being</b>" (sức khoẻ và hạnh phúc nói chung).'),
])
put('r2', [
    ('C', 'Bài nói về việc chia việc nhà và mức độ hạnh phúc trong hôn nhân → C.'),
    ('B', 'Đoạn 2: couples organize their marriage and work out the tasks and duties → mối quan hệ thành hợp đồng.'),
    ('C', 'unmoved = unshaken (không bị lay chuyển, không phản ứng).'),
    ('A', 'Đoạn 4: men report fewer family conflicts and greater well-being → họ hạnh phúc hơn.'),
    ('A', 'Khoá Word chọn A: kết quả khảo sát cho thấy bản thân việc nhà không quyết định mức hài lòng (nhóm chia không đều lại hài lòng hơn). B, C trái nội dung. Câu suy luận khá khiên cưỡng.'),
    ('B', '"they feel less guilty…" giải thích cho "men report fewer family conflicts and greater well-being" → they = Men (khoá Word).'),
])
put('r3', [
    ('NG', 'Bài chỉ nói tỉ lệ ly hôn ở nhóm chia đều cao hơn; không nói tỉ lệ ly hôn "đang tăng" ở nhóm chia không đều.'),
    ('F', 'Đoạn 2: chia đều khiến "encourage conflicts rather than conflict resolution skills" → họ KHÔNG biết giải quyết xung đột tốt.'),
    ('T', 'Đoạn 3: "they believe they can exchange their roles for their husbands\'".'),
    ('NG', 'Bài không nhắc chồng của họ có làm toàn thời gian hay không.'),
])
put('r4', [
    ('B', 'come in all shapes and sizes = có đủ hình dạng và kích cỡ.'),
    ('C', 'tell the machines <b>what</b> to do = bảo máy móc phải làm gì.'),
    ('A', 'personal computers = máy tính cá nhân.'),
    ('D', 'television <b>sets</b> = máy thu hình.'),
    ('A', 'cannot <b>even</b> see = thậm chí không thể nhìn thấy.'),
    ('B', 'cause problems = gây ra vấn đề.'),
    ('A', 'computers <b>lose</b> important information = làm mất thông tin.'),
    ('B', '<b>erase</b> information = xoá thông tin.'),
    ('B', '<b>like</b> chalk on a blackboard = như phấn trên bảng đen.'),
    ('D', '<b>another</b> different kind of problem = một loại vấn đề khác nữa.'),
])

# ============================================================ ĐỌC HIỂU – TEST 2
put('rq1', [
    ('C', 'do very little work (collocation) = làm rất ít việc.'),
    ('C', 'on a part-time basis = theo hình thức bán thời gian.'),
    ('A', '<b>highly</b> motivated = có động lực cao.'),
    ('C', 'this <b>situation</b> is changing = tình trạng này đang thay đổi.'),
    ('B', 'have + tân ngữ + V-ed: having their expenses <b>paid</b> for them.'),
    ('C', 'a loan <b>which</b> has to be paid back (đại từ quan hệ chỉ vật).'),
    ('B', 'tuition <b>fees</b> = học phí.'),
    ('D', 'students already <b>have to</b> pay = buộc phải trả.'),
    ('A', 'a financial aid package may <b>include</b> grants… = bao gồm.'),
    ('D', '<b>considerable</b> pressure = áp lực đáng kể.'),
])
put('rq2', [
    (['watching'], 'deal with the situation by <b>watching</b> TV.'),
    (['common'], 'have something in <b>common</b> = có điểm chung.'),
    (['look'], 'who <b>look</b> after themselves = tự chăm sóc bản thân.'),
    (['wearing'], 'a rule against <b>wearing</b> jewelry (against + V-ing).'),
    (['to'], 'tell sb <b>to</b> V.'),
    (['that'], 'learn <b>that</b> they were house keys (mệnh đề danh từ).'),
    (['talking', 'speaking'], 'began <b>talking</b> to the children.'),
    (['about'], 'worried <b>about</b> their own safety.'),
    (['is'], 'The most common way … <b>is</b> by hiding (động từ be, chủ ngữ số ít).'),
    (['turn'], 'turn the volume up = vặn âm lượng lớn lên.'),
])
put('rq3', [
    ('A', 'Câu đầu: Most journeys in Britain and the US are made by road.'),
    ('B', 'Đoạn 2: traffic is often heavy and it is difficult to park → giao thông đông đúc.'),
    ('B', 'Đoạn 3: In the US, large cities have good public transportation systems.'),
    ('A', 'Câu NOT true: bài nói "Many college and even high-school students have their own cars" → A (ít sinh viên có xe) sai.'),
    ('C', 'at their own convenience = vào thời gian, địa điểm thích hợp với họ.'),
    ('C', 'Đoạn 4: heavier items and raw materials often go by rail.'),
    ('B', 'Đoạn 5: by air, by bus (Greyhound/Trailways), by rail (Amtrak) → 3 loại.'),
    ('D', 'Đoạn cuối: traffic congestion and pollution.'),
    ('D', 'Most people say that public transport is simply not good enough.'),
    ('D', '"they" = Americans (see no reason to use their cars less).'),
])

# ============================================================ VIẾT – TEST 1
put('w4', [
    ('D', 'but we enjoyed it all the same = vẫn thích dù mưa → D.'),
    ('A', 'could not help weeping = could not stop himself from weeping.'),
    ('A', 'at a loss for words = không biết nói gì → puzzled about what to say.'),
    ('C', 'It\'s a pity that you didn\'t tell us = I wish you <b>had told</b> us (tiếc nuối về quá khứ).'),
    ('C', 'Without transportation = If there were no transportation (điều kiện loại 2).'),
    ('B', 'circulation of five million = năm triệu người đọc/số bản phát hành.'),
    ('A', 'No sooner had … than … = as soon as …'),
    ('C', 'It took him three months to get over his illness.'),
    ('A', 'Though … = However hard he tried, …'),
    ('B', 'still likes → has been a fan for years.'),
])
put('w1', [
    (['She only knows three words in Italian.', 'She only knows three words of Italian.'],
     'know là stative → HTĐ; "three words in Italian". Mẫu: She only knows three words in Italian.'),
    (['I usually walk, but I am travelling by bus this week.', 'I usually walk, but I am traveling by bus this week.', 'I usually walk, but I am travelling on the bus this week.'],
     'usually → HTĐ; this week (tạm thời) → HTTD. Mẫu: I usually walk, but I am travelling by bus this week.'),
    (["The sun is shining. Let's do the laundry.", 'The sun is shining. Let us do the laundry.'],
     'The sun is shining (đang xảy ra). Let\'s do the laundry.'),
    (['In Vietnam, an extended family usually consists of three or four generations.', 'In Vietnam, extended families usually consist of three or four generations.'],
     'Sự thật chung → HTĐ; consist of. Mẫu: In Vietnam, an extended family usually consists of three or four generations.'),
    (['Every day I leave my flat at eight and walk to my university.', 'Every day I leave my flat at eight o\'clock and walk to my university.'],
     'Every day → HTĐ. Mẫu: Every day I leave my flat at eight and walk to my university.'),
])
put_open('w2', [
    'Bài mẫu (từ khoá Word): Nowadays when the society develops day by day, people have no time in doing chores, especially women. Not only do they have full-time of job, but they also take care of children and do the housework. In my opinion, family members should share housework together. One reason is that sharing housework can connect family members. Adult members do labors like laundry and cooking, children just do simple chores like watering garden or making their bed. Sharing housework makes us feel less tired and equal. Another reason is that doing housework brings knowledge organization of things, especially children. They will know how to keep their belongings tidied and everything kept clean as well. In addition, we will feel responsible for our family. In conclusion, we should share housework to improve family life.',
])
put('w3', [
    (['called me for a long time', 'phoned me for a long time', 'called me for ages'], 'It\'s a long time since he last called me = He hasn\'t called me <b>for a long time</b>.'),
    (['did he get the job'], 'When did he get the job? = How long ago <b>did he get the job</b>?'),
    (['were you, I would book a table in advance', 'were you I would book a table in advance', "were you, I'd book a table in advance"], 'Lời khuyên → If I <b>were you, I would</b> book a table in advance.'),
    (['not tell them the secret'], 'would rather + V (nguyên mẫu) / not V: I would rather <b>not tell</b> them the secret.'),
    (['I to improve my English speaking skill, I would easily get that job'], 'Đảo ngữ câu điều kiện loại 2: <b>Were I to improve</b> my English speaking skill, I would easily get that job.'),
    (['to get good seats, we arrived early'], 'In order <b>to get</b> good seats, we arrived early.'),
    (['nearly an hour doing the crossword'], 'It took her … to do = She spent … <b>doing</b>.'),
    (['made to confess after three days'], 'Bị động của make sb V: He was made <b>to confess</b> after three days. (Khoá Word gõ sai "made the confess".)'),
    (['as easy as Maths for Nga', 'as easy for Nga as Maths'], 'Nga finds Maths easier than Physics = Physics is not <b>as easy as</b> Maths for Nga.'),
    (['to see a doctor'], 'advise you to see a doctor = You ought <b>to see</b> a doctor.'),
])

# ============================================================ VIẾT – TEST 2
put('wq1', [
    (["I wish I hadn't spent too much money on clothes.", 'I wish I had not spent too much money on clothes.', "If only I hadn't spent too much money on clothes."],
     'regret + V-ing (đã làm) → I wish I <b>hadn\'t spent</b> too much money on clothes.'),
    (['Football is said to be the best game to play.', 'It is said that football is the best game to play.'],
     'People say … → bị động: Football <b>is said to be</b> the best game to play.'),
    (['Tom thanked you for helping him.', 'Tom thanked me for helping him.', 'Tom thanked you for your help.'],
     'Lời cảm ơn → thank sb for V-ing: Tom <b>thanked you for helping</b> him. (Khoá Word: "me for helping him".)'),
    (['It is a three-hour drive from Hai Phong to Ha Noi.', "It's a three-hour drive from Hai Phong to Ha Noi."],
     'It takes three hours to drive = It is a <b>three-hour drive</b> (danh từ ghép, hours → hour).'),
    (['Never before has John been so rude to anybody.', 'Never has John been so rude to anybody.'],
     'Đảo ngữ với never (before): <b>Never before has John been</b> so rude to anybody.'),
])
put('wq2', [
    (['I am afraid that the air pollution in our city is getting worse and worse.'], 'Thứ tự: I am afraid that the air pollution in our city is getting worse and worse.'),
    (['We can use the Internet as an effective way for self-study.'], 'We can use the Internet as an effective way for self-study.'),
    (["We shouldn't swim in this river because its water is highly polluted.", 'We should not swim in this river because its water is highly polluted.'], "We shouldn't swim in this river because its water is highly polluted."),
    (['In the city there was so much traffic and noise and there was no time to relax.'], 'In the city there was so much traffic and noise and there was no time to relax.'),
    (['I will miss the train unless I leave now.'], 'I will miss the train unless I leave now.'),
])

# ============================================================ KIỂM TRA – TEST 3 (140 câu, id kt.N)
put('kt', [
    # ---- Exercise 1: phát âm (1-10)
    ('B', '<b>work</b> /wɜːk/ (o = /ɜː/). chore /tʃɔː/, more /mɔː/, divorce /dɪˈvɔːs/ có o = /ɔː/.'),
    ('D', '<b>loved</b> /lʌvd/ (-ed = /d/). trashed /træʃt/, talked /tɔːkt/, reached /riːtʃt/ có -ed = /t/.'),
    ('A', '<b>prepare</b> /prɪˈpeə/ (e = /ɪ/). help /help/, tennis /ˈtenɪs/, tell /tel/ có e = /e/.'),
    ('C', '<b>contribute</b> /kənˈtrɪbjuːt/ (u = /juː/). husband /ˈhʌzbənd/, mum /mʌm/, vulnerable /ˈvʌlnərəbl/ có u = /ʌ/.'),
    ('D', '<b>visited</b> /ˈvɪzɪtɪd/ (-ed = /ɪd/). cleaned /kliːnd/, shared /ʃeəd/, called /kɔːld/ có -ed = /d/.'),
    ('D', '<b>finance</b> /ˈfaɪnæns/ (i = /aɪ/). skill /skɪl/, split /splɪt/, children /ˈtʃɪldrən/ có i = /ɪ/.'),
    ('A', '<b>breadwinner</b> /ˈbredwɪnə/ (ea = /e/). clean /kliːn/, each /iːtʃ/, lead (v) /liːd/ có ea = /iː/.'),
    ('C', '<b>career</b> /kəˈrɪə/ (a = /ə/). balance /ˈbæləns/, challenge /ˈtʃælɪndʒ/, happy /ˈhæpi/ có a = /æ/.'),
    ('A', '<b>share</b> /ʃeə/ (a = /eə/). alike /əˈlaɪk/, tradition /trəˈdɪʃn/, equal /ˈiːkwəl/ có a = /ə/.'),
    ('D', '<b>grandparents</b> /ˈɡrænpeərənts/ (a = /æ/). generation /ˌdʒenəˈreɪʃn/, grateful /ˈɡreɪtfl/, educate /ˈedʒukeɪt/ có a = /eɪ/.'),
    # ---- Exercise 2: từ vựng (11-30)
    ('A', 'prepare meals / be preparing meal = đang chuẩn bị bữa ăn (collocation).'),
    ('D', 'work <b>late</b> = làm việc muộn (lately = gần đây; later = sau đó).'),
    ('B', '<b>take care of</b> my younger sisters = chăm sóc các em.'),
    ('B', '<b>divide</b> household chores equally = chia đều việc nhà.'),
    ('C', '<b>heavy</b> lifting = việc nặng, mang vác (collocation).'),
    ('B', 'do the <b>laundry</b> = giặt đồ.'),
    ('A', '<b>Taking out</b> the rubbish = đổ rác (danh động từ làm chủ ngữ).'),
    ('D', '<b>handle</b> most of the chores = đảm đương phần lớn việc nhà.'),
    ('C', 'the household <b>finances</b> = tài chính gia đình (danh từ số nhiều).'),
    ('B', '<b>Homemaker</b> = người ở nhà nội trợ, chăm sóc nhà cửa và gia đình.'),
    ('D', 'the sole <b>breadwinner</b> = người trụ cột kiếm tiền duy nhất.'),
    ('B', 'shop for <b>groceries</b> = mua đồ tạp hoá/thực phẩm.'),
    ('A', 'do the <b>washing-up</b> = rửa bát.'),
    ('C', 'care <b>about</b> sb; put (all of) the housework <b>on</b> sb = đổ hết việc nhà lên ai.'),
    ('C', 'set a good <b>example</b> for sb = làm gương tốt cho ai.'),
    ('D', 'take <b>turns</b> in doing sth = thay phiên nhau (turns luôn ở số nhiều).'),
    ('C', '<b>enormous</b> benefits = lợi ích to lớn (tính từ đứng trước danh từ).'),
    ('B', '<b>sociable</b> = hoà đồng, cởi mở; social = thuộc xã hội.'),
    ('D', 'keep a good <b>relationship</b> with sb = giữ quan hệ tốt.'),
    ('A', 'tend to + V = có xu hướng.'),
    # ---- Exercise 3: đồng nghĩa (31-40)
    ('C', 'split (chia) ≈ <b>share</b>.'),
    ('B', 'collaborate ≈ <b>cooperate</b> (hợp tác).'),
    ('A', 'vulnerable ≈ <b>easily hurt</b> (dễ bị tổn thương).'),
    ('C', 'nurtured ≈ <b>fostered</b> (được nuôi dưỡng, vun đắp).'),
    ('D', 'raise (children) ≈ <b>bring up</b> (nuôi nấng).'),
    ('B', 'earn money ≈ <b>make</b> money.'),
    ('D', 'duties ≈ <b>chores</b> (household duties = household chores). Khoá Word chọn D; C (jobs) cũng gần nghĩa.'),
    ('A', 'traditional ≈ <b>conventional</b> (truyền thống, theo lệ cũ).'),
    ('C', 'career ≈ <b>occupation</b> (nghề nghiệp).'),
    ('B', 'solution ≈ <b>remedy</b> (giải pháp, biện pháp khắc phục).'),
    # ---- Exercise 4: trái nghĩa (41-50)
    ('A', 'divorce (ly hôn = kết thúc hôn nhân) >< <b>beginning of a marriage</b>.'),
    ('A', 'balance (cân bằng) >< a situation in which things are <b>not treated the same</b> (mất cân bằng, bất bình đẳng).'),
    ('D', 'reduce (giảm) >< <b>increase</b> (tăng).'),
    ('C', 'security (an toàn) >< <b>danger</b> (nguy hiểm).'),
    ('B', 'willingly (sẵn lòng) >< <b>reluctantly</b> (miễn cưỡng).'),
    ('A', 'mending (sửa chữa) >< <b>impairing</b> (làm hỏng, làm suy yếu).'),
    ('D', 'tidy up (dọn dẹp) >< <b>mess up</b> (làm bừa bộn).'),
    ('B', 'critical of (chê trách) >< <b>favourable</b> (tán thành).'),
    ('C', 'neat and tidy (gọn gàng) >< <b>messy and dirty</b> (bừa bộn, bẩn).'),
    ('A', 'suitable (phù hợp) >< <b>inappropriate</b> (không phù hợp).'),
    # ---- Exercise 5: ngữ pháp thì hiện tại (51-70)
    ('A', 'four times a week → thói quen: Hoang <b>checks</b>.'),
    (['B', 'D'], 'Nowadays → có thể dùng HTĐ (use) hoặc HTTD (are using, xu hướng hiện nay); khoá Word chọn D.'),
    ('B', 'At the moment → HTTD cho cả hai vế: is doing – is playing.'),
    ('C', 'now → <b>are having</b>; usually → <b>eat</b> dinner.'),
    ('B', 'every day → <b>ride</b>; today (khác thường) → <b>am going</b>.'),
    (['B', 'C'], 'Phàn nàn: is always talking (khoá Word); "always talks" (thói quen) cũng đúng ngữ pháp.'),
    ('D', 'now → HTTD phủ định: <b>aren\'t playing</b>.'),
    ('A', 'usually + Hoa (số ít) → <b>takes</b> charge of.'),
    ('B', 'now → HTTD, Our friends (số nhiều) → <b>are preparing</b>.'),
    ('A', 'right now → HTTD; All staff (số nhiều) → <b>are attending</b>.'),
    ('C', 'Chân lí khoa học → HTĐ: water <b>boils</b> at 100°C.'),
    ('A', 'every Sunday → <b>goes</b>.'),
    ('C', 'Look! → đang xảy ra: Minh <b>is singing</b>.'),
    ('D', 'sometimes → HTĐ; Bich (số ít) → <b>has</b>.'),
    ('B', 'Câu hỏi về chủ ngữ + đang xảy ra: Who <b>is playing</b> the guitar in that room?'),
    ('A', 'often → <b>wears</b>; today → <b>is wearing</b>.'),
    ('C', 'First thing in the morning → thói quen: I <b>have</b> a cup of milk tea.'),
    ('D', 'when she\'s under pressure → thói quen/đặc điểm: Ms. Kim <b>doesn\'t work</b> very well.'),
    ('D', 'now → HTTD: She <b>is checking</b> her document.'),
    ('A', 'Hurry up → đang xảy ra: Other friends <b>are waiting</b> for us.'),
    # ---- Exercise 6: tìm lỗi (71-90)
    ('A', 'Đang tìm Daniel lúc này → <b>am looking</b> for Daniel.'),
    ('B', 'someone (số ít) → <b>is calling</b>.'),
    ('D', 'Thói quen (every morning, always) → HTĐ: I always <b>go</b> to school on time.'),
    ('B', 'Câu hỏi HTTD: What are you <b>searching</b> for?'),
    ('C', 'Đang mưa (We can\'t play golf) → It <b>is raining</b> outside.'),
    ('D', 'Song song với "sleep", "play": … and they play and <b>eat</b> at night.'),
    ('C', 'taste (có vị) là stative → a coffee <b>tastes</b> good.'),
    ('A', 'mind là stative, phủ định HTĐ: I <b>don\'t</b> mind if…'),
    ('B', 'Đang ngủ (Quiet) → my baby <b>is sleeping</b>.'),
    ('D', 'He (số ít) → He <b>keeps</b> telling me jokes.'),
    ('A', 'Hỏi lương: How much <b>does</b> she earn a month?'),
    ('A', 'Khoá Word chọn <b>will hold</b>: ý đề là kế hoạch đã sắp xếp → "are holding" (câu có vấn đề về đề).'),
    ('C', 'want là stative → we <b>don\'t want</b> to leave now.'),
    ('C', 'Khoá Word chọn <b>will be</b>: "annual event" là sự thật chung → "It <b>is</b> the annual event of my school".'),
    ('B', 'Câu hỏi HTTD: Is your friend <b>coming</b> to pick you up?'),
    ('D', 'Rút gọn phủ định: … but some people <b>don\'t</b>.'),
    ('D', 'Câu hỏi HTTD: Why are you <b>crying</b>?'),
    ('C', 'twice yearly (thói quen) → HTĐ: she <b>donates</b> thousands of pounds.'),
    ('A', 'Thói quen/khả năng với have been learning for 5 months → He <b>doesn\'t speak</b> English very well.'),
    ('C', 'regularly → HTĐ: She <b>practises</b> violin regularly (không có is).'),
    # ---- Exercise 7: giao tiếp (91-105)
    ('B', 'Được khen → cảm ơn lời khen: Thanks for your compliment.'),
    ('C', 'Nhân viên hỏi giúp gì → Thanks, I\'m just looking.'),
    ('D', 'Hỏi cảm nhận về buổi game show → Great. I gained more knowledge…'),
    ('A', 'Khoá Word chọn "I didn\'t, either." – phương án ít sai nhất (cùng không dự họp).'),
    ('B', 'Khách phàn nàn thợ chưa đến → xin lỗi và hứa sửa nhanh.'),
    ('A', 'Lời mời đi picnic → Yes, I\'d love to.'),
    ('A', 'Chúc một ngày tốt lành → Thanks. The same to you.'),
    ('D', 'Hỏi chọn váy vàng hay xanh → I prefer the blue.'),
    ('B', 'Hỏi hạn nộp bài → We have to submit it by Friday 12.'),
    ('C', 'Nam bị nhắc không chạm vào hiện vật → Sorry, I don\'t know (xin lỗi, không biết quy định). Khoá Word chọn C.'),
    ('B', 'Why do you like…? → Because it is soft and beautiful.'),
    ('C', 'What\'s your neighbourhood like? → It\'s good. I love it.'),
    ('A', '"It\'s nearly Tet holiday" → How time flies! (thời gian trôi nhanh quá).'),
    ('D', 'You can borrow my book → Thanks tons (cảm ơn nhiều).'),
    ('A', 'Hỏi đường → Sure. Just go along this street.'),
    # ---- Exercise 8: điền từ (106-118)
    ('B', '<b>despite</b> the fact that + mệnh đề = mặc dù (despite the fact that many more women now have jobs).'),
    ('A', 'people <b>aged</b> between 18 and 65 = những người trong độ tuổi từ 18 đến 65.'),
    ('C', 'the women <b>estimated</b> their share = phụ nữ ước tính phần của mình.'),
    ('B', 'affected by <b>whether</b> the woman was working or not.'),
    ('D', 'should <b>be</b> shared (should + be + V-ed).'),
    ('C', 'did the <b>remainder</b> = làm phần còn lại.'),
    ('D', 'feel they are <b>unimportant</b> = cảm thấy mình không quan trọng.'),
    ('A', 'increase … <b>by</b> 14 hours = tăng thêm 14 giờ.'),
    ('C', 'the amount: <b>the</b> (đã xác định).'),
    ('A', '<b>as</b> the man\'s share increases much less = bởi vì (mệnh đề lí do).'),
    ('B', 'inequality and <b>loss</b> of respect = mất sự tôn trọng.'),
    ('A', 'leads to <b>anxiety</b> and depression (danh từ song song với depression).'),
    ('D', 'The research even <b>describes</b> housework as thankless = mô tả công việc nhà là vô ơn.'),
    # ---- Exercise 9: đọc (119-123)
    ('A', 'Lorna: "my husband retired last year… I\'d really like to be there with him" → vì chồng đã nghỉ hưu.'),
    ('C', 'Cass: "I\'m only 26, so I\'m not going to retire soon" → C (muốn nghỉ hưu sớm) là KHÔNG đúng.'),
    ('B', 'Sue: "I love work and I don\'t want to retire!" → Sue không muốn nghỉ hưu sớm.'),
    ('C', 'Roger sẽ có "first long-awaited visit to Paris" → chưa từng đến Paris.'),
    ('B', 'mature ≈ grown-up (trưởng thành).'),
    # ---- Exercise 10: đọc (124-130)
    ('D', 'Bài không hề nói luật pháp có thể chống lại chức năng của gia đình (câu đầu: "no law … can go against the fact…").'),
    ('B', 'Despite all the odds, your family will take care of your well-being → gia đình luôn bên bạn dù khó khăn.'),
    ('B', 'parents teach children good habits → help shape their personalities (phát triển phẩm chất cá nhân).'),
    ('C', '"They are not only the elements which help the children to shape their personalities" → They = good habits (khoá Word).'),
    ('A', 'ruined ≈ destroyed (bị phá hỏng).'),
    ('C', 'Đoạn cuối: every family member has to work hard… they will set good examples for the whole society → C. (Khoá Word chọn D "wealthy society" nhưng bài không nói; đã đổi sang C.)'),
    ('B', 'Cả bài nói về vai trò thiết yếu của gia đình → The importance of family.'),
    # ---- Exercise 11: gần nghĩa (131-135)
    ('A', 'Khoá Word chọn A (giá giữ nguyên đến cuối tháng này) – cách diễn đạt khá khiên cưỡng so với câu gốc.'),
    ('C', 'All the other schools are more expensive than mine → mine is the least expensive.'),
    ('D', 'what this sculpture is worth = how much it costs/ is worth.'),
    (['B', 'C'], '"Stop treating me that way!" she cried out → urged (khoá Word) hoặc begged me not to treat her that way (cũng hợp).'),
    ('C', 'know the system inside out = hiểu hệ thống tường tận → understands it thoroughly.'),
    # ---- Exercise 12: kết hợp câu (136-140)
    ('A', 'Rút gọn lí do: <b>Being</b> the youngest son, I didn\'t have to do much housework.'),
    ('B', 'Mục đích/kết quả: We need to share the tasks <b>so</b> the burden … will be more tolerable.'),
    ('C', 'Dan saw all the paintings. He left right after. → Right after seeing all the paintings, Dan left.'),
    ('B', 'Đối lập: <b>Although</b> I usually like red, I wore black.'),
    ('D', 'Hai vế: tried his best – won the prize → nếu không cố gắng thì đã không thể thắng (If he hadn\'t tried…, he couldn\'t have won).'),
], start=1)
