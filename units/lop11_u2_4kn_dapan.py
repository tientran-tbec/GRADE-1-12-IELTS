# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Unit 2 (Tiếng Anh 11 Global Success) – Bộ BÀI TẬP 4 KỸ NĂNG.
Quy ước như file lop11_u1_botro_dapan.py. Đáp án soạn độc lập rồi đối chiếu khoá trong file Word gốc.
Phần Nghe: dùng script có sẵn trong file Word."""

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


def put_open(prefix, rows):
    for i, e in enumerate(rows, 1):
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ======================= PHÁT ÂM =======================
put('pr1', [
    ('A', '<b>belief</b> /bɪˈliːf/ (e = /ɪ/). express /ɪkˈspres/, gender /ˈdʒendə/, Millennial /mɪˈleniəl/ (e = /e/).'),
    ('D', '<b>accept</b> /əkˈsept/ (cc: chữ c thứ hai = /s/). nuclear, critical, curious (c = /k/).'),
    ('A', '<b>hire</b> /ˈhaɪə/ (i = /aɪ/). conflict /ˈkɒnflɪkt/, limit /ˈlɪmɪt/, influence /ˈɪnfluəns/ (i = /ɪ/).'),
    ('B', '<b>honesty</b> /ˈɒnɪsti/ (h câm). hold /həʊld/, housework /ˈhaʊswɜːk/, historical /hɪˈstɒrɪkl/ (h = /h/).'),
    ('C', '<b>argue</b> /ˈɑːɡjuː/ (g = /ɡ/). generation, digital, damage (g = /dʒ/).'),
    ('D', '<b>argument</b> /ˈɑːɡjumənt/ (a = /ɑː/). take, male, native (a = /eɪ/).'),
    ('B', '<b>role</b> /rəʊl/ (o = /əʊ/). job /dʒɒb/, follow /ˈfɒləʊ/, electronic /ɪˌlekˈtrɒnɪk/ (o = /ɒ/).'),
    ('C', '<b>media</b> /ˈmiːdiə/ (a = /ə/). family, value, characteristic (a = /æ/).'),
    ('D', 'individuali<b>s</b>m /ɪndɪˈvɪdʒuəlɪzəm/ (s = /z/). suit, screen, social (s = /s/).'),
    ('A', '<b>device</b> /dɪˈvaɪs/ (i = /aɪ/). difference /ˈdɪfrəns/, thinker /ˈθɪŋkə/ (i = /ɪ/), experience /ɪkˈspɪəriəns/ (/ɪə/).'),
])
put('pr2', [
    ('C', '<b>belief</b> /bɪˈliːf/ nhấn âm 2. argument, nuclear, gender nhấn âm 1.'),
    ('B', '<b>experience</b> /ɪkˈspɪəriəns/ nhấn âm 2. value, thinker, curious nhấn âm 1.'),
    ('A', '<b>millennial</b> /mɪˈleniəl/ nhấn âm 2. digital /ˈdɪdʒɪtl/, freedom /ˈfriːdəm/, honesty /ˈɒnɪsti/ nhấn âm 1.'),
    ('A', '<b>express</b> /ɪkˈspres/ nhấn âm 2. native, media, platform nhấn âm 1.'),
    ('D', '<b>opinion</b> /əˈpɪnjən/ nhấn âm 2. influence, limit, damage nhấn âm 1.'),
    ('C', '<b>characteristic</b> /ˌkærəktəˈrɪstɪk/ nhấn âm 4. conflict, eyesight, common nhấn âm 1.'),
    ('D', '<b>extended</b> /ɪkˈstendɪd/ nhấn âm 2. music, social, footstep nhấn âm 1.'),
    ('B', '<b>accept</b> /əkˈsept/ nhấn âm 2. follow, hire, family nhấn âm 1.'),
    ('A', '<b>adapt</b> /əˈdæpt/ nhấn âm 2. difference, parent, children nhấn âm 1.'),
    ('C', '<b>housework</b> /ˈhaʊswɜːk/ nhấn âm 1. generational, individualism, electronic nhấn âm 3.'),
])

# ======================= TỪ VỰNG =======================
put('vo1', [
    ('e', '<b>nuclear family</b> = a family consisting of two parents and their children (gia đình hạt nhân).'),
    ('i', '<b>extended family</b> = gia đình gồm ông bà, cô dì chú bác… ngoài bố mẹ và con cái.'),
    ('a', '<b>Millennial</b> = người sinh khoảng 1981–1996 (thế hệ Y).'),
    ('h', '<b>conflict</b> = an active disagreement between people with different opinions (xung đột).'),
    ('d', '<b>generation gap</b> = khác biệt giữa người lớn tuổi và người trẻ về kinh nghiệm, quan điểm, thói quen, hành vi.'),
    ('b', '<b>male jobs</b> = công việc truyền thống được coi là của nam giới.'),
    ('j', '<b>gender roles</b> = hành vi, thái độ, đặc điểm tính cách được xác định bởi giới tính.'),
    ('c', '<b>digital natives</b> = người lớn lên trong thời đại số, quen với công nghệ từ nhỏ.'),
    ('f', '<b>belief</b> = cảm giác chắc chắn rằng điều gì đó tồn tại hoặc đúng (niềm tin).'),
    ('g', '<b>individualism</b> = coi trọng tự do cá nhân và độc lập hơn lợi ích tập thể (chủ nghĩa cá nhân).'),
])
put('vo2', [
    (['individualism'], '<b>Individualism</b> nhấn mạnh tự do và độc lập cá nhân → được đề cao ở văn hoá phương Tây.'),
    (['gender roles'], 'Nhiều phụ nữ đảm nhận vai trò vốn của nam → <b>Gender roles</b> (số nhiều, đi với "have changed").'),
    (['generation gap'], 'sự khác biệt giữa cha mẹ và con cái về giá trị văn hoá, công nghệ → <b>generation gap</b>.'),
    (['millennial', 'a millennial'], 'sinh năm 1996 → thuộc thế hệ <b>Millennial</b> (sau "a" nên điền danh từ đếm được số ít).'),
    (['belief'], 'hold a strong <b>belief</b> that… = có niềm tin mạnh mẽ rằng…'),
    (['extended family'], 'gia đình nhiều thế hệ cùng sống → <b>extended family</b>, được đánh giá cao vì sự hỗ trợ.'),
    (['digital natives'], 'lớn lên cùng công nghệ → <b>digital natives</b>.'),
    (['conflict'], 'a <b>conflict</b> between my friend and I do khác biệt quan điểm.'),
    (['male jobs'], 'công việc chân tay nặng nhọc xưa được xếp vào <b>male jobs</b>.'),
    (['nuclear family'], 'chỉ gồm bố mẹ và con cái → <b>nuclear family</b>.'),
])
put('vo3', [
    ('C', 'argue <b>over</b> trivial matters = cãi nhau về chuyện vặt (argue over/about).'),
    ('B', '<b>rely on</b> their family = dựa vào gia đình khi gặp khó khăn. run into = tình cờ gặp; get through = vượt qua.'),
    ('A', '<b>adapt</b> to changes = thích nghi với thay đổi.'),
    ('D', 'Ánh sáng xanh có thể <b>damage</b> eyesight (gây hại thị lực) → trẻ bị các vấn đề về mắt.'),
    ('A', '<b>experiment</b> with platforms = thử nghiệm với các nền tảng (hợp với "try new things").'),
    ('B', '<b>take away</b> electronic devices from sb = lấy thiết bị của ai đi (nếu họ lạm dụng).'),
    ('C', 'be <b>hired</b> by an employer = được thuê bởi chủ.'),
    ('D', 'cultural <b>values</b> được truyền từ thế hệ này sang thế hệ khác.'),
    ('A', 'rely on <b>electronic devices</b> for communication, entertainment and accessing information.'),
    ('C', 'teach to <b>respect</b> others regardless of age or background = dạy tôn trọng người khác.'),
])
put('vo4', [
    ('A', '<b>curious</b> (tò mò) ↔ <b>indifferent</b> (thờ ơ).'),
    ('B', '<b>freedom</b> (tự do) ↔ <b>restriction</b> (sự hạn chế).'),
    ('D', '<b>adapt</b> (thích nghi) ↔ <b>neglect</b> (bỏ mặc, không chú ý đến sự thay đổi). Đây là cặp trái nghĩa theo khoá đề; các phương án còn lại không đối lập.'),
    ('D', '<b>permission</b> (sự cho phép) ↔ <b>disagreement</b> (sự không đồng ý). acceptance/approval là đồng nghĩa.'),
    ('C', '<b>honesty</b> (trung thực) ↔ <b>cheating</b> (gian lận). sincerity là đồng nghĩa.'),
])
put('vo5', [
    (['arguments'], 'get into <b>arguments</b> over viewpoints (ARGUE → arguments, danh từ số nhiều).'),
    (['critical'], 'a <b>critical</b> thinker = người có tư duy phản biện (CRITIC → critical).'),
    (['social'], 'make use of <b>social</b> media (SOCIETY → social).'),
    (['beliefs'], 'share common <b>beliefs</b> (BELIEVE → beliefs).'),
    (['cultural'], 'follow native country\'s <b>cultural</b> values (CULTURE → cultural).'),
    (['different'], 'has <b>different</b> experiences (DIFFERENCE → different).'),
    (['characteristic'], 'a common <b>characteristic</b> (CHARACTER → characteristic, sau "a" nên số ít).'),
    (['extended'], 'an <b>extended</b> family (EXTEND → extended).'),
    (['valuable'], 'brings <b>valuable</b> opinions (VALUE → valuable = có giá trị).'),
    (['generational'], 'The <b>generational</b> conflicts (GENERATION → generational) = xung đột thế hệ.'),
])
put('vo6', [
    ('achieve', 'potential to <b>achieve</b> great things = có tiềm năng đạt được điều lớn lao. (allow cần tân ngữ + to V.)'),
    ('force', 'should not <b>force</b> their beliefs upon sb = không nên áp đặt. upset không đi với "upon".'),
    ('educational', 'ưu tiên cơ hội <b>educational</b> như học lên cao.'),
    ('permission', 'ask for parents\' <b>permission</b> before going out late = xin phép bố mẹ.'),
    ('gain', 'contribute to weight <b>gain</b> = góp phần gây tăng cân.'),
])

# ======================= NGỮ PHÁP =======================
put('gr1', [
    ('must', 'Giá trị truyền thống là điều trẻ em <b>phải</b> nhận ra tầm quan trọng (bắt buộc, quan điểm người nói) → must.'),
    ('should', 'Lời khuyên: ông bà <b>nên</b> học dùng điện thoại → should.'),
    ('have to', 'Quy tắc/chuẩn mực xã hội: trẻ <b>phải</b> kính trọng người già → have to.'),
    ('mustn\'t', 'Cha mẹ <b>không được</b> ép con theo nghề của mình ("instead… let children choose") → mustn\'t.'),
    ('had to', '"Older generations <b>had to</b> rely on newspapers… but today\'s youth don\'t have to" → quá khứ: had to.'),
    ('must', 'Thanh thiếu niên <b>phải</b> biết trân trọng nỗ lực của cha mẹ → must.'),
    ('should', 'Lời khuyên: <b>nên</b> nghe lời khuyên của cha mẹ → should (shouldn\'t sai nghĩa).'),
    ('don\'t have to', 'Ngày nay phụ nữ <b>không cần</b> (don\'t have to) giới hạn ước mơ. mustn\'t (cấm) không hợp.'),
])
put('gr2', [
    ('B', 'In the past + "but now they have more freedom" → quá khứ bắt buộc: <b>had to</b>.'),
    ('A', 'Cha mẹ <b>nên</b> dành thời gian chất lượng cho con → should.'),
    ('A', 'Trẻ <b>phải</b> luôn vâng lời → have to (theo khoá đề). Lưu ý: nghĩa "luôn luôn vâng lời" mang tính bắt buộc.'),
    ('D', 'Thanh thiếu niên <b>nên</b> trao đổi cởi mở với cha mẹ → should.'),
    ('B', 'In the near future (tương lai) → <b>will have to</b>.'),
])
put('gr3', [
    ('D', 'Sau giới từ without cần V-ing: without <b>questioning</b> their authority.'),
    ('C', 'differences <b>in</b> musical preferences (difference in sth).'),
    ('A', 'effect là danh từ; động từ "ảnh hưởng" là <b>affect</b>: can affect fashion trends.'),
    ('B', 'rely solely <b>on</b> (rely on), không phải "at".'),
    ('A', 'Chịu trách nhiệm và đối mặt hậu quả là nghĩa vụ → <b>must/have to</b>; "don\'t have to" (không cần) sai nghĩa.'),
])

# ======================= ĐỌC =======================
put('re1', [
    ('A', 'an <b>inevitable</b> aspect = khía cạnh không thể tránh khỏi.'),
    ('C', 'different age <b>groups</b> = nhóm tuổi.'),
    ('D', 'social and cultural changes <b>which</b> shape… (mệnh đề quan hệ thay cho changes).'),
    ('B', 'Younger generations, <b>who</b> have grown up in the digital age (mệnh đề quan hệ chỉ người).'),
    ('C', 'Vế trước nói người trẻ quen công nghệ; vế sau nói người già khó thích nghi → tương phản: <b>In contrast</b>.'),
    ('A', 'struggle to adapt <b>to</b> sth (adapt to).'),
    ('D', 'differences <b>in</b> social norms and values.'),
    ('C', 'tính từ bổ nghĩa cho practices: <b>cultural</b> practices.'),
    ('C', 'each + danh từ số ít: <b>each</b> generation.'),
    ('D', 'find <b>common</b> ground = tìm điểm chung.'),
])
put('re2', [
    ('A', 'Bài nói về nguyên nhân: khác biệt giá trị, giao tiếp, kì vọng chưa được đáp ứng → <b>Reasons for Family Conflicts</b>.'),
    ('D', '"influenced by their upbringing, personal experiences, and social influences" → <b>disagreements</b> không phải yếu tố ảnh hưởng.'),
    ('C', '"Ineffective communication, whether <b>it</b> be through misinterpretation…" → it = ineffective communication.'),
    ('B', '<b>exacerbate</b> = làm trầm trọng thêm ≈ <b>worsen</b>.'),
    ('C', 'Đoạn cuối: "Family members should also be willing to <b>adapt and adjust their expectations</b>" → mọi người cần điều chỉnh kì vọng, nên C (không cần từ bỏ mong muốn) là <b>sai</b>.'),
])
put('re3', [
    ('T', '"older individuals might find it challenging to use … new modes of communication like <b>emojis and abbreviations</b>".'),
    ('F', '"Older generations often value respect to authority figures, while younger generations … question traditional social ranking" → giới trẻ không nhất thiết tôn trọng.'),
    ('F', '"This difference in technological proficiency can create a <b>gap in communication</b>" → khoảng cách số là nguyên nhân gây rạn nứt giao tiếp.'),
    ('NG', 'Bài không nói tần suất các thế hệ trò chuyện với nhau.'),
    ('T', '"bridging the digital gap through <b>inter-generational technology training programs</b> can help older individuals feel more included".'),
])

# ======================= VIẾT =======================
put('wr1', [
    (['older generations should access technology to connect with younger ones'], 'Older generations <b>should</b> access technology to connect with younger ones.'),
    (['young people must respect their parents traditional values and customs', 'young people must respect their parents\' traditional values and customs'], 'Young people <b>must</b> respect their parents\' traditional values and customs.'),
    (['young people must prioritise face-to-face interactions to build stronger relationships', 'young people must prioritize face-to-face interactions to build stronger relationships'], 'Young people <b>must</b> prioritise face-to-face interactions to build stronger relationships.'),
    (['newcomers should value the experiences of older professionals in the workplace'], 'Newcomers <b>should</b> value the experiences of older professionals in the workplace.'),
    (['older people should recognize the importance of digital literacy in todays world', 'older people should recognise the importance of digital literacy in todays world', "older people should recognize the importance of digital literacy in today's world"], 'Older people <b>should</b> recognize the importance of digital literacy in today\'s world.'),
])
put('wr2', [
    ('A', '"should be more patient" ≈ "should have more patience". B đổi chủ thể; C, D sai nghĩa.'),
    ('B', '"You cannot treat him like that" (cấm) = <b>You mustn\'t treat him that way</b> as he is older.'),
    ('C', '"too much … leads to…" ≈ <b>The more you use…, the more … problems you will have</b> (so sánh kép).'),
    ('B', '"may fail to have children follow" ≈ <b>may not always succeed in passing down</b>.'),
    ('D', '"are interested in starting" ≈ <b>have a keen interest in starting</b>; "Many" ≈ "A number of".'),
])
put_open('wr3', [
    '<b>Bài mẫu (đồng ý):</b><br><i>Nowadays, many children use social media. In my view, parents should have a certain level of control of their children\'s activities on social media for the following reasons.<br>'
    'First of all, one reason for parental control is to protect children from potential online risks. Social media platforms can expose children to cyberbullying and inappropriate content. By monitoring their online activities and setting limits, parents can help safeguard their children from these dangers.<br>'
    'Furthermore, children may lack the maturity to understand the complex online world. Parents need to provide guidance and educate their children about responsible social media use.<br>'
    'In conclusion, I think that parents should control their children\'s activities on social media. This will ensure that their children encounter appropriate content and develop a healthy mindset.</i>'
])

# ======================= NÓI =======================
put_open('sp1', [
    '<b>Mẫu:</b> I try to spend time talking with my parents every day. We usually have dinner together, which gives us an opportunity to discuss our day and any important matters. However, I do sometimes encounter difficulties when chatting with them. Sometimes, it feels like they don\'t understand the pressures and challenges I face because of the generation gap.<br><i>Dịch:</i> Tôi cố gắng dành thời gian nói chuyện với bố mẹ mỗi ngày…',
    '<b>Mẫu:</b> My parents and I have different ideas about technology. I think it\'s important for communication and learning, but they worry about me spending too much time on screens and they try to limit screen time. Besides, they prefer talking face-to-face, while I\'m more comfortable with talking to my friends online.',
])
put_open('sp2', [
    '<b>Mẫu (gợi ý ý chính):</b> (1) Hoàn cảnh: buổi họp mặt gia đình nhiều thế hệ. (2) Vấn đề: khác biệt quan điểm về công nghệ và mạng xã hội – ông bà lo về quyền riêng tư, an ninh và quan hệ giữa người với người. (3) Cảm xúc: lạc lõng, thất vọng. (4) Giải pháp: kiên nhẫn, cởi mở, lắng nghe, tìm điểm chung → hiểu nhau hơn.<br>'
    '<i>I vividly recall a time when I faced a difficulty related to the generation gap within my family… Over time, I realised that patience and open-mindedness were essential in narrowing the generation gap.</i>'
])

# ======================= NGHE (script trong file Word) =======================
put('li1', [
    ('C', 'Speaker C: "My parents have strict rules about how I should spend my <b>allowance</b>… They want me to save every penny" → <b>quản lí tiền bạc</b>.'),
    ('B', 'Speaker B: "they constantly want to <b>control every aspect of my life</b>… I also need the freedom to make my own decisions" → <b>độc lập và kiểm soát</b>.'),
    ('A', 'Speaker A: "we are speaking different languages… they always <b>dismiss my opinions</b>… I want to be heard" → <b>giao tiếp và thấu hiểu</b>.'),
])
put('li2', [
    ('T', '"If anyone says that they have never had conflict with their parents… they\'re probably lying. Even the most calm, <b>well-behaved</b>… people have conflicts."'),
    ('T', '"a long period of conflict … can cause both you and your parents much <b>unhappiness and stress</b>."'),
    ('F', 'Xung đột còn "may even impact your mental health" <b>và</b> sức khoẻ thể chất ("impact your physical health, causing you to eat less, exercise less") → không phải "chỉ" tinh thần.'),
    ('T', '"Think carefully about why you and your parents are arguing. <b>Put yourselves in their position</b>."'),
    ('T', '"Talk to your parents, <b>don\'t maintain a stubborn silence</b>."'),
])

# ======================= BÀI KIỂM TRA (50 câu) =======================
put('kt', [
    ('C', '<b>device</b> /dɪˈvaɪs/ (i = /aɪ/). digital /ˈdɪdʒɪtl/, millennial /mɪˈleniəl/, limit /ˈlɪmɪt/ (i = /ɪ/).'),
    ('B', 'influen<b>c</b>e /ˈɪnfluəns/ (c = /s/). conflict, critical, colour (c = /k/).'),
    ('C', '<b>traditional</b> /trəˈdɪʃənl/ nhấn âm 2. electronic, generational, individualism nhấn âm 3.'),
    ('A', '<b>conflict</b> (n) /ˈkɒnflɪkt/ nhấn âm 1. accept, rely, adapt nhấn âm 2.'),
    ('B', 'Theo chuyên gia dinh dưỡng, trẻ <b>phải</b> tránh đồ uống có đường trước khi ngủ để không bị tiểu đường → have to.'),
    ('D', 'Lời khuyên để sống khoẻ: <b>should</b> tập thể dục đều đặn.'),
    ('C', 'Sau mạo từ "a" + ___ + thinker cần tính từ: <b>critical</b> thinker (người có tư duy phản biện).'),
    ('D', 'try sth <b>out</b> = thử làm gì.'),
    ('C', '<b>value</b> your parents\' love = trân trọng tình yêu của cha mẹ.'),
    ('A', '<b>rely on</b> someone = dựa dẫm vào ai ("be more independent").'),
    ('A', '<b>argue over</b> social values = tranh cãi về các giá trị xã hội (bond over = gắn kết nhờ cùng thích).'),
    ('C', 'Các thế hệ <b>không cần</b> đồng ý về mọi thứ (nhưng cần thảo luận cởi mở) → don\'t have to.'),
    ('B', 'I suggest that GenZ <b>should</b> be encouraged… (suggest that S (should) V).'),
    ('D', 'Gia đình có 3 thế hệ → <b>extended</b> family.'),
    ('C', 'Không được thô lỗ với người khác nhóm tuổi → <b>mustn\'t</b>.'),
    ('B', 'many <b>common</b> characteristics = nhiều đặc điểm chung với bố.'),
    ('D', 'a digital <b>native</b> (danh từ, người sinh ra trong thời đại số).'),
    ('A', 'Chủ ngữ cần danh từ: <b>Individualism</b> (chủ nghĩa cá nhân) là nét đặc trưng của GenZ.'),
    ('D', 'Khi bàn về khác biệt thế hệ, ta <b>không nên</b> (shouldn\'t) khái quát hoá/định kiến.'),
    ('D', 'Người cha từ chối: <b>I\'m afraid you can\'t</b> (vì còn nhiều bài tập).'),
    ('A', 'Xin xem album ảnh → đồng ý: <b>Of course, you can.</b>'),
    ('A', '<b>prolonged</b> (kéo dài) ≈ <b>extended</b>. redundant = thừa; mild = nhẹ; sensible = hợp lí.'),
    ('D', '<b>emphasises</b> ≈ <b>highlights</b> (nhấn mạnh).'),
    ('B', '<b>conflict</b> (xung đột) ↔ <b>harmony</b> (hoà thuận). battle/competition/difference khác nghĩa trái.'),
    ('D', '<b>contrast</b> (sự tương phản) ↔ <b>similarity</b> (sự tương đồng).'),
    ('B', '<b>communicative</b> (có khả năng giao tiếp tốt) sai nghĩa; cần danh từ bổ nghĩa: misunderstandings and <b>communication</b> challenges (thách thức trong giao tiếp).'),
    ('D', 'a strong desire <b>for</b> social changes (desire for), không phải "in".'),
    ('A', '"You <b>don\'t have to</b> disregard…" sai nghĩa; phải là <b>mustn\'t</b> disregard (không được coi thường nỗ lực của ông bà).'),
    ('B', 'by <b>recalling</b> positive memories = hồi tưởng lại những kỉ niệm đẹp.'),
    ('C', 'has become a <b>recognised</b> marketing strategy (phân từ quá khứ làm tính từ: được công nhận).'),
    ('B', 'result <b>in</b> sth = dẫn đến.'),
    ('D', '…flip phones <b>as</b> they use memories of a previous era = vì họ dùng ký ức (as = bởi vì).'),
    ('A', 'those <b>who</b> grew up using older devices (đại từ quan hệ thay cho those = people).'),
    ('A', 'Bài viết về nguyên nhân xung đột trong gia đình nhập cư (văn hoá, ngôn ngữ, khác biệt thế hệ) → <b>Family Conflicts within Immigrant Families: Why?</b>'),
    ('C', 'their native customs → "their" = <b>immigrants\'</b> (Immigrants often face the task of reconciling their native customs).'),
    ('B', '<b>stems</b> (from) = bắt nguồn từ ≈ <b>arises</b>.'),
    ('A', 'Đoạn 3: "Parents who are less proficient in the host country\'s language <b>may struggle to communicate</b>" → A (không thấy khó) là <b>sai</b>.'),
    ('C', 'Đoạn cuối: "open dialogue and mutual respect are vital" → <b>Encouraging open dialogue and mutual respect</b>.'),
    ('D', 'Bài nói cách tiếp thị đến các thế hệ, tránh ageism, ngôn ngữ bao trùm → <b>Narrowing the Age Gap in Marketing</b>.'),
    ('A', '<b>wrapping their heads around</b> = cố gắng hiểu (trying to understand).'),
    ('A', '<b>defying</b> norms = chống lại các chuẩn mực ≈ <b>opposing</b>.'),
    ('C', '"Early-career workers are leading the great resignation rather than taking whatever job <b>they</b> can get" → they = early-career workers.'),
    ('B', '"For many years, knowing how to market to <b>Millennials</b> was the hot ticket for most marketers."'),
    ('A', 'Đoạn 3: "Women are <b>delaying having children</b>" → phụ nữ sinh con muộn hơn các thế hệ trước.'),
    ('C', 'Đoạn cuối: cách gọi tên nhóm tuổi "could keep customers away" → ngôn ngữ <b>có</b> ảnh hưởng; C sai (NOT true).'),
    ('B', 'find it hard to catch up with = It is hard for sb to keep up with → B. C có "must" (thêm nghĩa bắt buộc); A, D sai nghĩa.'),
    ('C', 'Câu tường thuật: Do you have → <b>if she had</b> any disagreements with <b>her parents</b> (lùi thì, giữ nguyên "parents").'),
    ('B', 'It is unnecessary = <b>don\'t have to</b>.'),
    ('A', '<b>But for</b> + N = Without… → câu điều kiện loại 3: <b>But for my father\'s sacrifice, I could not have gone to college</b>.'),
    ('D', 'Thực tế hiện tại (không hay nói chuyện nên không hiểu) → điều kiện loại 2: <b>If you talked… more often, they could understand you</b>.'),
])
