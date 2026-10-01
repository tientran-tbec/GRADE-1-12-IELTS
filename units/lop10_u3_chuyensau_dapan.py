# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Unit 3 Music (Tiếng Anh 10 Global Success) – Bộ BÀI TẬP CHUYÊN SÂU.
Quy ước:
  mcq  : chữ cái 'A'-'D' (plain: chính văn bản phương án; nhiều đáp án đúng: danh sách)
  fill : danh sách đáp án chấp nhận (1 ô) hoặc {'blanks': [[...],[...]]} (nhiều ô)
  open : không chấm điểm, EXPLANATIONS chứa đáp án mẫu
Đáp án lấy từ khoá tô màu trong nửa sau file src/l10u3/cs_c.txt rồi tự giải độc lập để đối chiếu;
những chỗ khoá Word sai/mơ hồ được liệt kê ở GHI_CHU_RA_SOAT."""

GHI_CHU_RA_SOAT = [
    'PHẠM VI: file Word gốc chỉ có Unit 3 (lý thuyết, Bài 1-14, Test 1, Test 2, Test 3). Test 3 (140 câu, có khoá) làm trang kiểm tra tính giờ; thời gian 120 phút là do người soạn tự đặt (Word không ghi). File không có ảnh/audio.',
    'u3.5 (Test 2, THE HISTORY OF FILM, "in this ____ the first film stars appeared"): khoá Word = D (result) nhưng "in this result" không tồn tại; cụm đúng là "in this way" (B). ĐÃ ĐỔI KHOÁ SANG B.',
    'kt.23: khoá Word = A (remains); "becomes" (C) cũng hợp nghĩa ("trở thành ảnh hưởng sâu sắc") nên chấp nhận cả A và C.',
    'kt.25: khoá Word = C (season); "episode" (D) cũng có thể đúng về nghĩa nhưng "the 4th season I\'ve seen" tự nhiên hơn khi nói về một show yêu thích; giữ khoá Word.',
    'kt.126-128: kt.128 "Record companies don\'t always ____" – câu hỏi gượng (bài đọc nói công ty đĩa hay áp đặt, KHÔNG cho ban nhạc tự do); giữ khoá Word = C.',
    'kt.135: khoá Word = D ("suggested me going") – cấu trúc suggest + O + V-ing sai ngữ pháp, nhưng D là phương án gần nghĩa nhất (đề nghị đi xem phim); giữ khoá Word.',
    'r4.8 (Test 1, C.III câu 8): khoá Word = C ("The coffee wasn\'t strong enough to keep us awake") – nghĩa mâu thuẫn với câu gốc (cà phê đậm nhưng không giữ tỉnh táo); đây là phương án ít sai nhất, câu có vấn đề về đề.',
    'r4.9 (Test 1, C.III câu 9): khoá Word = D (đảo ngữ "Hardly can he…"); giữ khoá Word.',
    'r4.14: khoá Word = B – ý ngầm "nhiều người Mỹ uống coke, nên việc anh ấy không uống là đáng ngạc nhiên"; giữ khoá Word.',
    'r2.2 (Test 1, bài đọc The Voice): phương án A trong file nguồn bị lỗi OCR ("at least rs old"); đã khôi phục thành "at least 18 years old"; đáp án đúng C (15 tuổi trở lên) theo bài đọc "fifteen and over".',
    'g8.4: khoá Word = for; "but/yet" cũng hợp nghĩa (kỳ nghỉ trọn gói NHƯNG tôi không biết nhiều về thành phố) nên chấp nhận for / but / yet.',
    'g10.8: khoá Word sửa "yet" → "and" (10 đề cử, thắng 8 – không đối lập rõ); giữ khoá. g10.5: khoá Word = bỏ "and".',
    'g12.2, g13.1, g13.3, g13.5, g15.7: chấp nhận thêm dạng V-ing/ nguyên mẫu khi hai dạng đều đúng ngữ pháp (began to rain/raining, intended to visit/visiting, saw him go/going, saw … feed/feeding).',
    'v4.5 và v4.14: khoá Word ghi hai dạng (to talk/talk; play/playing) – đã chấp nhận cả hai.',
    'c10.6 (Bài 10): khoá Word dùng "or" nhưng yêu cầu của đề là "Show additional information" (bổ sung) → đáp án chính dùng "and"; vẫn chấp nhận câu dùng "or" theo khoá Word.',
    'x3.4: khoá Word = "collection" nhưng cần số nhiều "collections" (one of the biggest art collections) – chấp nhận cả hai. x2.10: chấp nhận another / a.',
    'x4 (Test 2, "VI. Complete the second sentence…"): file nguồn bị mất toàn bộ từ gợi ý và vế sau (chỉ còn câu gốc), khoá Word chỉ còn đoạn cuối câu → chuyển thành câu mở (open) kèm đáp án mẫu soạn lại đầy đủ từ khoá. Câu 7 gốc "We didn\'t have managed without my father\'s money" sai chính tả → sửa thành "We wouldn\'t have managed without my father\'s money".',
    'Đáp án phát âm có thể khác nhau giữa giọng Anh/Mỹ: p2.4 (version /ʃ/ hoặc /ʒ/), p1.6 (learned tính từ /ɪd/), p1.3 (waltz /s/); khoá Word giữ nguyên.',
    'Test 1 phần viết (D.I biography): câu mở, bài mẫu lấy từ khoá (sửa lỗi chính tả "ae" → "are").',
    'Lỗi nguồn đã sửa trong generator: "10.The boss" thiếu khoảng trắng; "test.They" / "home.They"; "hard.D." và "mother.D." dính nhau (C.III câu 6, 10); "C . I was busy"; "I960" → 1960; "Iivc-performed" → live-performed; "eompany/ eomputer/ eroup/ projeet/ mueh"; "modernnisation"; "Take yourself at home" → "Make yourself at home"; "W hen looking Anna playing piano" → "When watching Anna play the piano"; "(113 )"; "new while R&B" → "new white R&B"; "in American," → "in America,"; "The world first film" → "The world\'s first film"; "In recent year" → "years"; "record other their songs" → "record their songs"; dấu ngoặc kép kt.96/121/123; "Mark the letter A. B, C" ở đề bài.',
    'u1.20 (Test 2): file nguồn xếp lệch thứ tự phương án (A, C, D, B); đã sắp lại A-D đúng thứ tự, đáp án = C (Driving cars at very high speeds).',
    'Các câu có khoá Word đúng nhưng đề hơi lạ (giữ nguyên): kt.19 ("No longer did Pokémon Go become…"), kt.62, kt.98 (haven\'t you? – Sorry, but I need more time), u1.9, u2.4.',
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


def S(tpl, *subs):
    """tạo các biến thể câu: tpl chứa {} thay bằng từng phần tử của subs"""
    return [tpl.replace('{}', s) for s in subs]


# ============================================================ BÀI 1-7: TO-V / V NGUYÊN MẪU
put('v1', [
    (['speak'], 'can + V (động từ khuyết thiếu + nguyên mẫu không to): can <b>speak</b>.'),
    (['do'], 'have to + V: have to <b>do</b>.'),
    (['stay'], 'must + V: must <b>stay</b>.'),
    (['help'], 'will + V: will <b>help</b>.'),
    (['see'], 'cannot + V: cannot <b>see</b>.'),
    (['to speak'], 'learn + to V (học làm gì): learns <b>to speak</b>.'),
    (['to go'], 'want + to V: want <b>to go</b>.'),
    (['ask'], 'should + V: should <b>ask</b>.'),
    (['to have'], "would like + to V: I'd like <b>to have</b> a dog."),
    (['come'], 'May I + V: May I <b>come</b> in?'),
])
put('v2', [
    (S('It won\'t be any good for {} to talk to her about it.', 'me', 'us', 'you'), 'Thêm "for + O" trước to V: It won\'t be any good <b>for me to talk</b> to her about it.'),
    (S('It wouldn\'t be much good for {} to complain to the minister about it.', 'us', 'me', 'you'), 'It wouldn\'t be much good <b>for us to complain</b> to the minister about it.'),
    (S('It is no fun for {} to have so many children to look after.', 'me', 'us', 'you'), 'It is no fun <b>for me to have</b> so many children to look after.'),
    (S('Will it be any good for {} to see the boss about it?', 'me', 'us', 'you'), 'Will it be any good <b>for me to see</b> the boss about it? (my seeing → for me to see)'),
    (S('It is just silly for {} to throw away your chances like that.', 'you', 'him', 'her', 'them'), 'It is just silly <b>for you to throw away</b> your chances like that.'),
])
put('v3', [
    ('e', 'force sb + to V: forces me <b>to do my homework</b>.'),
    ('c', 'encourage sb + to V: encourages others <b>to try new things with her</b>.'),
    ('f', "can't get sth + to V: can't get her suitcase <b>to close properly</b> (không đóng được)."),
    ('d', 'have sb + V: had his friend <b>help him with his homework</b> (nhờ bạn giúp).'),
    ('a', 'help sb + (to) V: help my grandmother <b>do chores around her house</b>.'),
    ('b', 'tell sb + to V: tells him <b>to do the dishes after dinner</b>.'),
])
put('v4', [
    (['making'], 'stop + V-ing (ngừng làm gì): stop <b>making</b> so much noise.'),
    (['to lend'], 'refuse + to V: refused <b>to lend</b> me any money.'),
    (['try'], 'let sb + V (nguyên mẫu không to): let him <b>try</b>.'),
    (['writing'], 'enjoy + V-ing: enjoy <b>writing</b> letters.'),
    (['to talk', 'talk'], 'dare + to V hoặc V (dám làm gì): No one dared <b>(to) talk</b>.'),
    (['to play'], 'arrange + to V: arranged <b>to play</b> tennis.'),
    (['cry'], 'make sb + V: made Mary <b>cry</b>.'),
    (['washing'], 'finish + V-ing: finished <b>washing</b> your hair.'),
    (['to look'], 'offer + to V: offered <b>to look</b> after our children.'),
    (['stealing'], 'admit + V-ing: admitted <b>stealing</b>.'),
    (['to go'], 'want + to V: doesn\'t want <b>to go</b> home.'),
    (['to talk'], 'be allowed + to V: are not allowed <b>to talk</b>.'),
    (['answering'], 'Would you mind + V-ing: mind <b>answering</b>.'),
    (['play', 'playing'], 'watch sb + V / V-ing: watched their children <b>play/playing</b> football.'),
    (['not to tell'], 'beg sb + (not) to V: begged her <b>not to tell</b> his mother.'),
])
put('v5', [
    ('convinced', 'convince sb to V (thuyết phục ai làm gì) – "made" phải đi với V không to: made me practice. Đáp án: <b>convinced</b>.'),
    ('convince', 'convince sb to V → "convince you to come"; make + O + V (không to) nên "make you to come" sai.'),
    ('lets', 'let sb + V: my mother <b>lets</b> me go out (cho phép); get sb + to V nên "gets me go" sai.'),
    ('persuading', 'persuade sb + to V: always <b>persuading</b> us to go shopping.'),
    ('have', 'have sb + V (nhờ/ bảo ai làm gì): <b>have</b> me take a special math class; get + to V.'),
    ('forces', 'force sb + to V: <b>forces</b> him to go; have + O + V (không to).'),
])
put('v6', [
    (['It would be awful for me to do that again.'], 'It + would be + adj + for sb + to V: <b>It would be awful for me to do that again.</b>'),
    (['It took the team ten years to win the championship.'], 'It took + O + thời gian + to V: <b>It took the team ten years to win the championship.</b>'),
    (['It costs four dollars to buy lunch.'], 'It costs + tiền + to V: <b>It costs four dollars to buy lunch.</b>'),
    (['The Internet allows us to get information from anywhere.'], 'allow sb to V: <b>The Internet allows us to get information from anywhere.</b>'),
    (['My mother persuaded my teacher to give me less homework.'], 'persuade sb to V: <b>My mother persuaded my teacher to give me less homework.</b>'),
])
put('v7', [
    (['seems'], 'My daily life <b>seems</b> to be pretty boring (seem + to V).'),
    (['excited'], 'get <b>excited</b> to meet my friends (get + adj).'),
    (['home'], 'go <b>home</b> to eat dinner (home không có giới từ "to").'),
    (['try'], 'I <b>try</b> to finish my homework.'),
    (['in the middle'], 'stop <b>in the middle</b> to take a nap (dừng giữa chừng).'),
    (['wake up'], 'I then <b>wake up</b> to finish my homework (thức dậy làm tiếp).'),
])

# ============================================================ BÀI 8-10: CÂU GHÉP
put('c8', [
    ('Simple sentence', 'Chỉ có một mệnh đề độc lập → câu đơn.'),
    ('Compound sentence', 'Hai mệnh đề độc lập nối bởi <b>, but</b> → câu ghép.'),
    ('Compound sentence', 'Hai mệnh đề độc lập nối bởi <b>, and</b> → câu ghép (that riding… là mệnh đề danh ngữ, không tính).'),
    ('Simple sentence', 'Một mệnh đề độc lập (There don\'t seem to be many bears…) → câu đơn.'),
    ('Simple sentence', 'Một mệnh đề → câu đơn (cụm trạng từ Suddenly, giới từ out the car window…).'),
])
put('c9', [
    ('but', 'Đối lập (dark ↔ white) → <b>but</b>.'),
    ('but', 'Hai vế đối chiếu nhẹ (đang chơi nhưng cũng đang học) → <b>but</b> (khoá Word).'),
    ('and', 'Bổ sung/ kết quả (ăn nhiều, lớn nhanh) → <b>and</b>.'),
    ('and', 'Hai hành động nối tiếp → <b>and</b>.'),
    ('or', 'maybe… or maybe… (có lẽ… hoặc có lẽ…) → <b>or</b>.'),
])
put('c10', [
    (['Mark drove to visit his friend, and they went out for dinner.'], 'Trình tự sự kiện → <b>and</b>.'),
    (['Linda thinks she should go to school, for she wants to get qualifications for a new profession.'], 'Chỉ lí do → <b>for</b>.'),
    (['David invested a lot of money in the business, but the business went bankrupt.', 'David invested a lot of money in the business, yet the business went bankrupt.'], 'Kết quả bất ngờ → <b>but/ yet</b>.'),
    (["John didn't understand the homework assignment, so he asked the teacher for help."], 'Hành động do một lí do → <b>so</b>.'),
    (["The students didn't prepare for the test, nor did they realize how important the test was."], 'Phủ định cả hai vế → <b>nor</b> + đảo ngữ (nor did they realize).'),
    (['Sue thinks she should stay home and relax, and she also thinks she should go on vacation.', 'Sue thinks she should stay home and relax, and she thinks she should go on vacation.', 'Sue thinks she should stay home and relax, or she should go on vacation.'],
     'Yêu cầu "bổ sung" → <b>and</b>. (Khoá Word dùng "or" nên cũng được chấp nhận.)'),
    (['The doctors looked at the x-rays, so they decided to operate on the patient.'], 'Hành động do một lí do → <b>so</b>.'),
    (['We went out on the town, and we came home late.'], 'Trình tự sự kiện → <b>and</b>.'),
    (['Tim flew to London to visit his Uncle, and he also wanted to visit the National Museum.', 'Tim flew to London to visit his Uncle, and he wanted to visit the National Museum.'], 'Bổ sung → <b>and</b>.'),
    (['It is sunny, but it is very cold.', 'It is sunny, yet it is very cold.'], 'Đối lập → <b>but/ yet</b>.'),
])

# ============================================================ BÀI 11-14: NÂNG CAO
put('n11', [
    ('going', 'imagine + V-ing.'),
    ('to buy', 'agree + to V.'),
    ('to answer', 'be + adj (easy) + to V.'),
    ('to get', 'how + to V.'),
    ('seeing', 'look forward to + V-ing (to là giới từ).'),
    ('visiting', 'giới từ (of) + V-ing.'),
    ('to run', 'decide + to V.'),
    ('to study', 'expect sb + to V.'),
    ('working', "doesn't mind + V-ing."),
    ('to ride', 'learn + to V.'),
])
put('n12', [
    ('B', 'risk + V-ing: couldn\'t risk <b>leaving</b> her alone.'),
    ('B', 'have + sth + V3/ed (nhờ làm gì – bị động): had the roof <b>repaired</b>.'),
    ('B', 'let sb + V: let our son <b>stay</b> up late.'),
    ('A', 'eager + to V: eager <b>to see</b> their parents.'),
    ('D', "had better/ would rather + V: He'd rather <b>stay</b> at home."),
    ('A', 'make sb + V: makes me <b>laugh</b>.'),
    ('A', 'see sb + V (thấy toàn bộ hành động): saw him <b>sign</b> the agreement.'),
    ('D', 'It is necessary for sb + to V: for her <b>to come</b> back home.'),
    ('B', 'would rather + V + than + V: They would <b>rather</b> go… than travel…'),
    ('A', 'allow sb + to V: allows <b>us to stay</b> home.'),
])
put('n13', [
    (B(['going'], ['buying']), 'think of (giới từ) + V-ing: going; without (giới từ) + V-ing: buying.'),
    (['to ask'], 'hesitate + to V.'),
    (['to show'], 'It is + adj (kind) + of sb + to V.'),
    (['seeing'], 'look forward to + V-ing.'),
    (['to study', 'studying'], 'intend + to V (hoặc intend + V-ing): intend <b>to study</b>.'),
    (B(['marrying'], ['to buy']), 'plan on (giới từ) + V-ing: marrying; refuse + to V: to buy.'),
    (['eating'], "can't resist + V-ing (không cưỡng lại được)."),
    (B(['going'], ['dancing']), 'enjoy + V-ing (hai việc song song): going… dancing.'),
    (B(['living'], ['to move']), 'stop + V-ing (ngừng sống); it was time for me + to V: to move.'),
    (['to turn'], 'forget + to V (quên làm một việc cần làm).'),
])
put('n14', [
    (['I have studied French for many years, so my French-speaking friends can chat easily with me now.'], '"As a result" (kết quả) → <b>so</b>.'),
    (["You are quite intelligent, but you don't think before you act.", "You are quite intelligent, yet you don't think before you act."], '"However" (đối lập) → <b>but/ yet</b>.'),
    (["My friends Jane and Jennifer have just moved into a new home, and they've made many changes in its appearance.", "My friends Jane and Jennifer have just moved into a new home, and they have made many changes in its appearance."], 'Bổ sung → <b>and</b>.'),
    (['Sue could study music next year, or she could study drama instead.', 'Sue could study music next year, or she could study drama.'], 'Hai lựa chọn → <b>or</b>.'),
    (['Tom watches the news, but Bill makes news.', 'Tom watches the news, yet Bill makes news.'], 'Đối lập (xem tin ↔ làm ra tin) → <b>but</b>.'),
])

# ============================================================ PHÁT ÂM & TRỌNG ÂM
put('p1', [
    ('A', '<b>guest</b> /ɡest/ (g = /ɡ/). manage /ˈmænɪdʒ/, prodigy /ˈprɒdɪdʒi/, teenager /ˈtiːneɪdʒə/ có g = /dʒ/.'),
    ('D', '<b>polonaise</b> /ˌpɒləˈneɪz/ (a = /eɪ/). demanding /dɪˈmɑːndɪŋ/, nuance /ˈnjuːɑːns/, ballade /bæˈlɑːd/ có a = /ɑː/.'),
    ('A', '<b>waltz</b> /wɔːls/ (z = /s/). franchise /ˈfræntʃaɪz/, patriotism /ˈpætriətɪzəm/, composer /kəmˈpəʊzə/ có s = /z/.'),
    ('A', '<b>sonata</b> /səˈnɑːtə/ (o = /ə/). phenomenon /fəˈnɒmɪnən/, nocturne /ˈnɒktɜːn/, polonaise /ˌpɒləˈneɪz/ có o = /ɒ/.'),
    ('C', '<b>chorus</b> /ˈkɔːrəs/ (ch = /k/). achievement /əˈtʃiːvmənt/, charity /ˈtʃærəti/, franchise /ˈfræntʃaɪz/ có ch = /tʃ/.'),
    ('A', '<b>renowned</b> /rɪˈnaʊnd/ (-ed = /d/). talented /ˈtæləntɪd/, gifted /ˈɡɪftɪd/, learned (tính từ) /ˈlɜːnɪd/ có -ed = /ɪd/.'),
])
put('p2', [
    ('B', '<b>music</b> /ˈmjuːzɪk/ (s = /z/). single /ˈsɪŋɡl/, contest /ˈkɒntest/, release /rɪˈliːs/ có s = /s/.'),
    ('B', '<b>sonata</b> /səˈnɑːtə/ (a = /ɑː/). platinum /ˈplætɪnəm/, anthem /ˈænθəm/, smash /smæʃ/ có a = /æ/.'),
    ('A', '<b>compose</b> /kəmˈpəʊz/ (-se = /z/). purchase /ˈpɜːtʃəs/, release /rɪˈliːs/, increase /ɪnˈkriːs/ có -se = /s/.'),
    ('A', '<b>version</b> /ˈvɜːʃn/ (s = /ʃ/; Anh-Mỹ /ʒn/). process /ˈprəʊses/, modest /ˈmɒdɪst/, contestant /kənˈtestənt/ có s = /s/.'),
    ('C', '<b>debut</b> /ˈdeɪbjuː/ (u = /juː/). instrument /ˈɪnstrəmənt/, platinum /ˈplætɪnəm/, album /ˈælbəm/ có u = /ə/.'),
    ('D', '<b>passionate</b> /ˈpæʃənət/ (-ate = /ət/). eliminate /ɪˈlɪmɪneɪt/, nominate /ˈnɒmɪneɪt/, originate /əˈrɪdʒɪneɪt/ có -ate = /eɪt/.'),
])
put('p3', [
    ('B', '<b>parachute</b> /ˈpærəʃuːt/ (ch = /ʃ/). architect /ˈɑːkɪtekt/, school /skuːl/, psychology /saɪˈkɒlədʒi/ có ch = /k/.'),
    ('D', '<b>jealous</b> /ˈdʒeləs/ (ea = /e/). treason /ˈtriːzn/, reason /ˈriːzn/, season /ˈsiːzn/ có ea = /iː/.'),
    ('D', '<b>needed</b> /ˈniːdɪd/ (-ed = /ɪd/). worked /wɜːkt/, laughed /lɑːft/, hoped /həʊpt/ có -ed = /t/.'),
    ('A', '<b>erupt</b> /ɪˈrʌpt/ (u = /ʌ/). humour /ˈhjuːmə/, UFO /ˌjuː ef ˈəʊ/, communicate /kəˈmjuːnɪkeɪt/ có u = /juː/.'),
    ('A', '<b>author</b> /ˈɔːθə/ (th = /θ/). other /ˈʌðə/, there /ðeə/, they /ðeɪ/ có th = /ð/.'),
])
put('p4', [
    ('C', '<b>along</b> /əˈlɒŋ/ nhấn âm 2. friendly /ˈfrendli/, extra /ˈekstrə/, orphanage /ˈɔːfənɪdʒ/ nhấn âm 1.'),
    ('A', '<b>interesting</b> /ˈɪntrəstɪŋ/ nhấn âm 1. surprising /səˈpraɪzɪŋ/, amusing /əˈmjuːzɪŋ/, successful /səkˈsesfl/ nhấn âm 2.'),
    ('C', '<b>benefit</b> /ˈbenɪfɪt/ nhấn âm 1. understand /ˌʌndəˈstænd/, engineer /ˌendʒɪˈnɪə/, Vietnamese /ˌvjetnəˈmiːz/ nhấn âm 3.'),
    ('B', '<b>tonight</b> /təˈnaɪt/ nhấn âm 2. paper /ˈpeɪpə/, lecture /ˈlektʃə/, story /ˈstɔːri/ nhấn âm 1.'),
    ('C', '<b>organize</b> /ˈɔːɡənaɪz/ nhấn âm 1. important /ɪmˈpɔːtnt/, community /kəˈmjuːnəti/, disease /dɪˈziːz/ nhấn âm 2.'),
])

# ============================================================ TỪ VỰNG TEST 1
put('tv1', [
    ('B', '<b>reality TV shows</b> = chương trình truyền hình thực tế (real/actuality TV shows không dùng).'),
    ('B', '<b>cultural figures</b> = nhân vật văn hoá; culture là danh từ, cần tính từ cultural.'),
    ('A', '<b>infant prodigy</b> = thần đồng (cụm cố định).'),
    ('A', 'Tập phim được <b>aired</b> (phát sóng); announce/ transmit không hợp collocation này.'),
    ('C', '<b>originate in</b> = bắt nguồn từ (folk songs originated in rural areas).'),
    ('B', '<b>renowned</b> = nổi tiếng, được kính trọng; notorious mang nghĩa tiếng xấu.'),
    ('C', '<b>nominate for the prize</b> = được đề cử giải thưởng.'),
    ('A', 'Sau mạo từ a cần danh từ: a <b>phenomenon</b> (hiện tượng); phenomenal là tính từ.'),
    ('C', '<b>prominent</b> (nổi bật) và <b>famous</b> (nổi tiếng) đều hợp → cả hai đúng (C).'),
    ('B', '<b>conquer</b> several competitions = chinh phục/ vượt qua nhiều cuộc thi.'),
])
put('tv2', [
    (['conquer'], 'It\'s not easy to <b>conquer</b> such a big competition = chinh phục một cuộc thi lớn.'),
    (['celebrity panel'], 'The <b>celebrity panel</b> = ban giám khảo là người nổi tiếng, nhận xét thí sinh.'),
    (['audition'], 'pass the <b>audition</b> (vòng thử giọng) để vào bán kết.'),
    (['demanding'], 'technically <b>demanding</b> = đòi hỏi kỹ thuật cao.'),
    (['inspirational'], '<b>inspirational</b> songs = những bài hát truyền cảm hứng.'),
    (['patriotism'], 'songs which praise <b>patriotism</b> = ca ngợi lòng yêu nước (thời chiến).'),
])
put('tv3', [
    ('c', 'biography = tiểu sử (câu chuyện cuộc đời do người khác viết).'),
    ('a', 'competition = cuộc thi tìm ra người giỏi nhất.'),
    ('b', 'platinum = chứng nhận cho album bán được một triệu bản.'),
    ('d', 'box office = quầy bán vé.'),
])
put('tv4', [
    ('A', 'smash hit = thành công lớn → great success.'),
    ('B', 'passionate = đam mê → enthusiastic.'),
    ('C', 'talented = tài năng → gifted.'),
    ('B', 'contestants = thí sinh → competitors.'),
    ('B', 'versions (các phiên bản) ≈ copies theo khoá Word; originals là bản gốc, categories là thể loại.'),
    ('C', 'released (phát hành) ≈ launched.'),
])
put('tv5', [
    ('A', 'a highly <b>competitive</b> round (vòng thi cạnh tranh cao); competitor là danh từ.'),
    ('D', 'The Idol program <b>process</b> (quy trình) consists of auditions, semi-finals and finals.'),
    ('C', 'play the flute and the guitar → <b>musical instruments</b> (nhạc cụ).'),
    ('C', 'bị loại sau buổi diễn → <b>eliminated</b>.'),
    ('A', 'make significant <b>innovations</b> in classical music (những đổi mới đáng kể).'),
    ('A', '<b>deceive</b> sb into doing sth = lừa ai làm gì.'),
    ('D', 'major <b>achievements</b> = thành tựu lớn của nhà soạn nhạc.'),
    ('D', 'launched in 2002 / aired in 2002 đều hợp → cả hai (D).'),
])
put('tv6', [
    ('C', 'Hai việc diễn ra song song → <b>and</b>.'),
    ('A', 'tried my best, <b>but</b> the result was not as good (đối lập).'),
    ('C', 'lost the key, <b>so</b> couldn\'t get in (kết quả).'),
    ('B', 'loves comedies, <b>yet</b> her husband… action films (đối lập).'),
    ('B', 'must do well, <b>or</b> you will not graduate (nếu không thì…).'),
    ('A', 'Pop music is popular, <b>for</b> the melody is simple (lí do).'),
    ('C', 'should practice more, <b>but</b> my health hasn\'t been good (đối lập).'),
    ('B', 'can go with me, <b>or</b> you can go alone (lựa chọn).'),
])

# ============================================================ NGỮ PHÁP 1 (câu ghép) TEST 1
put('g7', [
    ('Correct', 'but nối hai mệnh đề đối lập: đúng.'),
    ('Incorrect', 'nor phải đảo ngữ: nor <b>does she like</b> its plot.'),
    ('Correct', 'yet = nhưng; hai mệnh đề đối lập: đúng.'),
    ('Incorrect', 'Mệt nên dừng nghỉ là quan hệ nguyên nhân – kết quả → dùng <b>so</b>, không dùng yet.'),
    ('Incorrect', 'maybe… <b>or</b> maybe… (hai khả năng), không dùng and.'),
    ('Correct', 'and bổ sung thông tin: đúng (khoá Word).'),
    ('Incorrect', '<b>so that</b> = để; nên dùng <b>so</b> (kết quả): …two years, so I can recommend…'),
    ('Incorrect', 'Because và so không dùng chung: bỏ một từ (Because… , my father… hoặc …, so my father…).'),
])
put('g8', [
    (['but', 'yet'], 'Đối lập: tried to read… <b>but/ yet</b> it was too difficult.'),
    (['or'], 'Lựa chọn: pick me up <b>or</b> will I take the bus?'),
    (['yet', 'but'], 'Đối lập: quite old, <b>yet/ but</b> he exercises more than I do.'),
    (['for', 'but', 'yet'], 'Khoá Word: <b>for</b> (lí do). Nghĩa đối lập (but/ yet) cũng chấp nhận được.'),
    (['or'], 'Lựa chọn: design himself <b>or</b> have it designed by an architect?'),
    (['and'], 'Bổ sung: gave me money <b>and</b> also a new dress.'),
    (['nor'], 'never… <b>nor</b> did she leave him any money (nor + đảo ngữ).'),
    (['so'], 'Kết quả: failed once, <b>so</b> I was very nervous.'),
])
put('g9', [
    ('B', 'Không thích đi học nhưng vẫn đi → đối lập: <b>yet</b>.'),
    ('C', 'Đã có kế hoạch nên bắt đầu tiết kiệm → kết quả: <b>so</b>.'),
    ('A', 'Hai sự kiện song song → <b>and</b>.'),
    ('C', 'Chơi được bóng chuyền nhưng không chơi được bóng rổ → <b>but</b>.'),
    ('A', 'Đi bơi vì trời nóng → lí do: <b>for</b>.'),
    ('A', 'Hai lựa chọn → <b>or</b>.'),
    ('C', 'Hát hay nên được vỗ tay → kết quả: <b>so</b>.'),
    ('B', 'Mưa to mà vẫn chơi bóng → đối lập: <b>yet</b>.'),
])
put('g10', [
    (['likes'], '"nor does she <b>likes</b>" sai → <b>like</b> (sau does dùng nguyên mẫu).'),
    (['that', 'so that'], '"so <b>that</b> we had to…" thừa that → <b>so</b> we had to come.'),
    (['or'], 'Hai việc cùng làm trước khi đi → dùng <b>and</b>, không dùng or.'),
    (['so'], 'Muốn cải thiện phát âm nên muốn biết lỗi → quan hệ lí do: <b>for</b> she wants to improve…'),
    (['and'], '"For this computer is broken, <b>and</b> you can use that tablet" → bỏ "and": For this computer is broken, you can use…'),
    (["isn't"], '"and he <b>isn\'t</b>… He always gives others a hand" mâu thuẫn → <b>is</b>.'),
    (["mustn't"], 'Vì họ không bán vé online nên phải đến quầy: <b>must</b> go (mustn\'t = cấm).'),
    (['yet'], '10 đề cử, thắng 8 là bổ sung chứ không đối lập → <b>and</b> (khoá Word).'),
])

# ============================================================ NGỮ PHÁP 2 (to-V / V) TEST 1
put('g11', [
    ('B', 'refuse + to V.'),
    ('B', 'hire sb + to V (mục đích): a young man <b>to work</b>.'),
    ('B', 'hear sb + V (nghe toàn bộ hành động): heard someone <b>fall</b>.'),
    ('C', 'be able + to V.'),
    ('A', 'advise sb + to V.'),
    ('C', 'seem + to V: seem <b>to have</b> passion.'),
    ('B', 'would like + to V.'),
    ('C', 'want sb + to V.'),
    ('A', 'expect + to V.'),
    ('B', 'force sb + to V.'),
])
put('g12', [
    (['to marry'], 'determine/ ask sb + to V: ask Jane <b>to marry</b> him.'),
    (['to get'], 'try + to V (cố gắng): tried <b>to get</b> up early.'),
    (['to increase'], 'decide + to V.'),
    (['to buy'], 'persuade sb + to V.'),
    (['help'], "couldn't + V: couldn't <b>help</b>."),
    (['eat'], 'let sb + V: let the fox <b>eat</b>.'),
    (['to work'], 'seem + to V.'),
    (['to try'], 'advise sb + to V.'),
    (['stay'], 'make sb + V: make the fox <b>stay</b> away.'),
    (['buy'], 'have sb + V: had his wife <b>buy</b>.'),
])
put('g13', [
    (['to rain', 'raining'], 'begin + to V / V-ing: began <b>to rain</b>.'),
    (['to attend'], 'decide + to V.'),
    (['to visit', 'visiting'], 'intend + to V: intended <b>to visit</b>.'),
    (['know'], 'let sb + V: let him <b>know</b>.'),
    (['go', 'going'], 'see sb + V/ V-ing: saw him <b>go</b>.'),
    (['feel'], 'make sb + V: makes everybody <b>feel</b>.'),
    (['to go'], 'It is + adj (dangerous) + to V.'),
    (['to buy'], 'promise + to V.'),
])
put('g14', [
    ('Correct', "don't hesitate + to V: đúng."),
    ('Incorrect', 'encourage sb <b>to study</b>, không dùng V-ing.'),
    ('Correct', 'invite sb + to V: đúng.'),
    ('Incorrect', 'require sb <b>to sign</b> in the form.'),
    ('Correct', 'deserve + to V (be treated): đúng.'),
    ('Correct', "It's impolite + not to V: đúng."),
    ('Correct', 'forget + to V (quên làm việc cần làm): đúng.'),
    ('Incorrect', 'adj + enough + <b>to</b> V: mature enough <b>to discuss</b>.'),
    ('Incorrect', 'learn <b>how to make</b> (how + to V).'),
    ('Incorrect', 'enough money <b>to buy</b> the coat (thiếu to).'),
])
put('g15', [
    (['change'], 'make sb + V: make Alex <b>change</b> her mind.'),
    (['know'], 'let me + V: let me <b>know</b> your decision.'),
    (['to refuse'], "It's customary + to V: <b>to refuse</b> a gift once or twice."),
    (['to leave'], 'be about + to V (sắp sửa): about <b>to leave</b>.'),
    (['to come'], 'whether + to V: whether <b>to come</b> to the wedding or not.'),
    (['to share'], 'enough + noun + to V: enough candies <b>to share</b>.'),
    (['feed', 'feeding'], 'see sb + V: saw my sister <b>feed</b> the dog.'),
    (['to finish'], 'determine + to V.'),
    (['to return'], 'promise + to V.'),
    (['to reveal'], 'adj + enough + to V: reliable enough <b>to reveal</b> my secrets.'),
])

# ============================================================ ĐỌC TEST 1
put('r1', [
    ('A', 'to air = phát sóng trên truyền hình (aired on NBC).'),
    ('B', 'a big hit = thành công lớn.'),
    ('A', 'a season = một mùa/ bộ của chương trình truyền hình.'),
    ('B', 'process = một chuỗi các bước (Blind Auditions, Battles, Knockouts…).'),
    ('A', 'a live performance = biểu diễn trực tiếp, không thu sẵn.'),
    ('B', 'television audience = khán giả theo dõi qua màn hình TV.'),
    ('B', 'to franchise = bán công thức (format) chương trình cho nơi khác.'),
])
put('r2', [
    ('A', 'Đoạn 1: "Based on the original The Voice of Holland…" → chương trình bắt nguồn từ Hà Lan.'),
    ('C', 'Only those fifteen and over are eligible → ít nhất 15 tuổi.'),
    ('C', 'the winner is determined by votes from the television audience → khán giả truyền hình.'),
    ('B', 'online voting, SMS text and iTunes purchases → tin nhắn và mua bản trình diễn online.'),
    ('C', 'receives US$100,000 and a record contract with Universal Music Group → tiền thưởng và cơ hội làm việc với hãng đĩa.'),
])
put('r3', [
    ('C', 'decide <b>whether</b> … or … (liệu… hay…).'),
    ('C', 'So <b>many</b> different types (types đếm được).'),
    ('D', 'at one time or <b>another</b> (cụm cố định).'),
    ('A', 'be considered <b>to be</b> black music.'),
    ('B', 'I found out <b>afterwards</b> (sau đó mới biết).'),
    ('B', 'close <b>enough</b> to his for them to imitate (adj + enough + to).'),
    ('A', 'white singers <b>like</b> Bob Dylan (như).'),
    ('B', '<b>young people</b> have more money to spend.'),
    ('D', 'to such an extent that (đến mức mà).'),
    ('A', 'worked against <b>its being</b> a genuine music (giới từ + V-ing).'),
])
put('r4', [
    ('C', 'hand in = nộp → give their assignments to her.'),
    ('A', 'Because of working hard, she fell ill = She worked so hard that she fell ill.'),
    ('B', "It's been 14 years since I last saw = I haven't seen my brother for 14 years."),
    ('C', 'gain weight = become fat; stops smoking = gives up smoking.'),
    ('C', 'Fewer people came than expected = We had expected more people to come.'),
    ('D', 'should have studied but too tired = couldn\'t study because very tired (khoá Word).'),
    ('C', 'Although + clause = Despite + N: Despite his serious illness, Mr Pike still composed…'),
    ('C', 'Khoá Word: C (câu gốc mâu thuẫn nghĩa); đây là phương án ít sai nhất (xem ghi chú rà soát).'),
    ('D', 'Câu gốc: không hiểu vì quá trẻ. Khoá Word chọn D (đảo ngữ Hardly can he…).'),
    ('A', 'have sth done = had someone decorate the house.'),
    ('C', 'Could you hold the line = wait.'),
    ('D', "look it up in the dictionary = find it in the dictionary."),
    ('C', 'prefers buying food in small shops or street markets → often buys food there.'),
    ('B', 'Surprisingly for an American → ngầm hiểu nhiều người Mỹ uống coke (khoá Word).'),
    ('C', 'is the same as smoking 40 cigarettes → has the same effect.'),
])

# ============================================================ VIẾT TEST 1
put_open('w1', [
    'Bài mẫu (từ khoá Word): My Tam was born in 1981 in Da Nang. She is a famous pop singer in Vietnam. She had a passion for music and started learning musical instruments at an early age. Her best-known songs are Hoa Mi Toc Nau, Uoc Gi, and Cay Dan Sinh Vien, which became an iconic song in the 2000s among Vietnamese university students. My Tam won the bronze medal at the Asian Music Festival held in Shanghai in 2000. One year later, she graduated from the Conservatory of Ho Chi Minh City with flying colors. She was also the first Vietnamese singer to participate in the Asian Song Festival in Seoul, Korea. My Tam is one of the most famous and influential pop singers in Vietnam and still maintains a passionate and active performing career.',
])
put('w2', [
    (["the plane leave on time, we'll arrive in Paris at noon", 'the plane leaves on time, we will arrive in Paris at noon'], 'Đảo ngữ câu điều kiện loại 1 với <b>Should</b>: Should the plane leave on time, we\'ll arrive in Paris at noon.'),
    (['were seen running out of the bank with big bags on their shoulders'], 'Bị động của see + V-ing: Two men <b>were seen running out</b> of the bank…'),
    (['he had seen the movie she had recommended the night before', 'he had seen the movie she had recommended the previous night'], 'Câu gián tiếp lùi thì: saw → had seen; last night → the night before.'),
    (['eats a lot every day, she still looks rawboned'], 'Even though + mệnh đề: Even though Sam <b>eats a lot every day, she still looks rawboned</b>.'),
    (["not to disturb him, I didn't call him"], 'So as <b>not to</b> + V: So as not to disturb him, I didn\'t call him.'),
    (['is too expensive for us to buy'], 'such… that → too… (for sb) to V: This television <b>is too expensive for us to buy</b>.'),
    (['to listening to music when I am stressed and tired'], 'be used to + V-ing: I am used <b>to listening</b> to music…'),
    (['do we go to the beach in winter'], 'Đảo ngữ với trạng từ phủ định Seldom: Seldom <b>do we go</b> to the beach in winter.'),
    (['that spilled coffee on the laptop', 'who spilled coffee on the laptop'], 'Câu chẻ: It wasn\'t him <b>that spilled</b> coffee on the laptop.'),
    (["you practice, the better you'll play", 'you practice, the better you will play'], 'So sánh kép: The more <b>you practice, the better you\'ll play</b>.'),
])

# ============================================================ TEST 2 – NGỮ PHÁP & TỪ VỰNG
put('u1', [
    ('D', '<b>Lately</b> + thì hiện tại hoàn thành = gần đây.'),
    ('A', '<b>put off</b> your holiday = hoãn kỳ nghỉ.'),
    ('C', 'It is recommended that + S + (should) V: that he <b>take</b> (giả định cách).'),
    ('B', 'define <b>what success is</b> (mệnh đề danh ngữ, trật tự S-V).'),
    ('C', 'Câu mệnh lệnh phủ định, câu hỏi đuôi: Don\'t…, <b>will you</b>?'),
    ('B', 'the first person + <b>to V</b>: the first person to discover the fire.'),
    ('A', 'Đáp lại "I didn\'t pass my driving test": <b>Better luck next time</b> (Chúc may mắn lần sau).'),
    ('B', 'have lived… <b>since</b> 2002 (mốc thời gian).'),
    ('A', '<b>in the interest of</b> public health = vì lợi ích sức khoẻ cộng đồng.'),
    ('C', 'Mệnh đề quan hệ không xác định thay Mr. Vo Van Kiet (người, chủ ngữ): <b>who</b>.'),
    ('C', '<b>individual</b> needs = nhu cầu riêng của từng cá nhân.'),
    ('D', 'discipline = kỷ luật/ trừng phạt ≈ <b>punish</b>.'),
    ('D', 'recover from = hồi phục sau ≈ <b>get over</b>.'),
    ('A', 'have + O + V3: <b>We had our house</b> broken into (nhà bị đột nhập).'),
    ('B', 'Rút gọn mệnh đề hoàn thành phủ định: <b>Not having been</b> to the national park before…'),
    ('D', 'nursing, teaching, engineering là các <b>professions</b> (nghề nghiệp).'),
    ('A', 'look <b>for</b> = tìm kiếm.'),
    ('D', 'wish + quá khứ giả định: He wishes he <b>had</b> a brother.'),
    ('B', 'Câu tường thuật: He asked me <b>where I lived</b> (không đảo ngữ).'),
    ('C', 'Chủ ngữ V-ing: <b>Driving cars at very high speeds</b> is extremely dangerous.'),
])
put('u2', [
    ('D', 'It was not until the match ended that everybody <b>left</b> (had left → left).'),
    ('B', 'The plants (số nhiều) → <b>look</b> unhealthy (looks → look).'),
    ('D', 'have it <b>repaired</b> (have + O + V3).'),
    ('B', 'Câu điều kiện: The astronauts <b>wouldn\'t walk</b> far… if they were hampered (didn\'t walk → wouldn\'t walk).'),
    ('B', '<b>highly</b> developed (trạng từ bổ nghĩa tính từ): highlier → highly.'),
])

# ============================================================ ĐỌC TEST 2
put('u3', [
    ('A', 'consist <b>of</b> = gồm có.'),
    ('B', 'have <b>been</b> popular ever since.'),
    ('C', 'titles on the screen to <b>explain</b> the story.'),
    ('D', 'the public had <b>their</b> favourite actors.'),
    ('B', 'in this <b>way</b> = bằng cách này. Khoá Word chọn D (result) nhưng "in this result" không tồn tại → đã đổi sang B.'),
    ('B', 'the public <b>would</b> only accept (tương lai trong quá khứ).'),
    ('D', 'America, <b>which</b> produced 95% of all films (mệnh đề quan hệ không xác định, vật).'),
    ('C', '<b>fewer</b> people went to see films (people đếm được).'),
    ('A', 'in <b>recent</b> years = những năm gần đây.'),
    ('A', 'currently <b>many</b> national film industries (industries đếm được).'),
])
put('u4', [
    ('B', 'Cả bài nói về sự nổi tiếng của các tiểu thuyết của Melville (the popularity of Melville\'s novels).'),
    ('D', 'used the knowledge gained during his travels as the basis → based on his travels.'),
    ('D', 'Redburn (1849) viết về chuyến đi làm cabin boy.'),
    ('A', 'basis ≈ foundation.'),
    ('A', 'After jumping ship in Tahiti → rời tàu không chính thức.'),
    ('B', 'a navy frigate = một con tàu.'),
    ('C', 'with the publication of Moby Dick, Melville\'s popularity started to diminish → giảm.'),
    ('D', 'a heavily symbolic allegory of the heroic struggle of humanity against the universe.'),
    ('B', 'metamorphosis (biến thái) ≈ change.'),
    ('A', 'Bài viết về tiểu thuyết thế kỷ 19 → nineteenth-century novels.'),
])

# ============================================================ VIẾT TEST 2
put('x1', [
    (['looked'], 'When I <b>looked</b> at my suitcase (quá khứ đơn).'),
    (['had tried'], 'somebody <b>had tried</b> to open it (xảy ra trước, quá khứ hoàn thành).'),
    (['glanced'], 'The man <b>glanced</b> my way (quá khứ đơn).'),
    (['was listening'], 'to see if I <b>was listening</b> (quá khứ tiếp diễn).'),
    (['take'], 'It is recommended that he <b>take</b> (giả định cách).'),
    (['was learning'], 'While he <b>was learning</b> to drive (quá khứ tiếp diễn).'),
    (['had'], 'he <b>had</b> twenty-five accidents (quá khứ đơn).'),
    (['to avoid'], 'wore the sunglasses <b>to avoid</b> (chỉ mục đích).'),
    (['being recognized', 'being recognised'], 'avoid + V-ing bị động: <b>being recognized</b>.'),
    (['is being considered'], 'right now → hiện tại tiếp diễn bị động: <b>is being considered</b>.'),
])
put('x2', [
    (['for'], 'It is difficult <b>for</b> sb to V.'),
    (['enough'], 'lucky <b>enough</b> to be asked (adj + enough + to V).'),
    (['that'], 'find <b>that</b> there are at least twenty other applicants.'),
    (['job'], 'applicants for the <b>job</b>.'),
    (['you'], 'offering <b>you</b> a job.'),
    (['or'], 'either… <b>or</b>…'),
    (['before'], '<b>Before</b> taking up your job… (trước khi nhận việc).'),
    (['which'], ', <b>which</b> helps you… (mệnh đề quan hệ chỉ cả câu trước).'),
    (['hard'], 'work <b>hard</b> to get promotion.'),
    (['another', 'a'], 'find <b>another</b> job (một công việc khác).'),
])
put('x3', [
    (['frightening'], 'experience (danh từ) cần tính từ: <b>frightening</b> (đáng sợ).'),
    (['typically'], 'divided (V3) cần trạng từ: <b>typically</b>.'),
    (['imagination'], 'children\'s + danh từ: <b>imagination</b>.'),
    (['collections', 'collection'], 'one of the biggest art <b>collections</b> (số nhiều; khoá Word ghi collection).'),
    (['pollution'], 'because of + danh từ: <b>pollution</b>.'),
    (['entrance'], 'the <b>entrance</b> to the pagoda (lối vào).'),
    (['modernized', 'modernised'], 'is being enlarged and <b>modernized</b> (V3 bị động).'),
    (['conservationists', 'Conservationists'], 'Danh từ chỉ người làm chủ ngữ số nhiều: <b>Conservationists</b> (nhà bảo tồn).'),
    (['sportsmanship'], 'the true spirit of <b>sportsmanship</b> (tinh thần thể thao).'),
    (['fame'], "stay behind his father's <b>fame</b> (danh tiếng)."),
])
put_open('x4', [
    'Mẫu: No sooner had he returned from his work than he got down to writing a letter. (khoá Word: "had he returned from his work than he got down writing a letter")',
    "Mẫu: I wish they hadn't closed the shop at lunch time. (khoá Word: they hadn't closed the shop at lunch time)",
    "Mẫu: I'd rather you didn't ask me that question. (khoá Word: you didn't ask me that question)",
    'Mẫu: It was not until he phoned us that we found out about the meeting. (khoá Word: until he phoned us that we found out about the meeting)',
    'Mẫu: By the time I arrived, David had gone home. (khoá Word: David had gone home)',
    'Mẫu: Not until their second child was born did Alice and Charles decide to move to a bigger house. (khoá Word: their second child was born did Alice and Charles decided…)',
    "Mẫu: Had it not been for my father's money, we wouldn't have managed. (khoá Word: hadn't been for my father's money, we wouldn't have managed)",
    "Mẫu: This room hasn't been tidied for 3 months. (khoá Word: room hasn't (been) tidied for 3 months)",
    'Mẫu: Despite being severely disabled, Judy participated in many sports. / In spite of her severe disability, Judy participated in many sports.',
    'Mẫu: This will be the first time the orchestra has performed outside London. (khoá Word: the orchestra played/ performed outside London)',
])
put_open('x5', [
    'Mẫu: I would like to express my concern about the increasing number of Karaoke bars in the city.',
    'Mẫu: There are a lot of reasons why I object to these places.',
    'Mẫu: Firstly, the owners take too much money from those who come to sing.',
    'Mẫu: Secondly, they cause too much noise in the neighborhood.',
    'Mẫu: Thirdly, there are a number of pupils who play truant just to go to those places to sing.',
    'Mẫu: Last but not least, these bars do harm to the appearance of the city because of their ugly flashing lights.',
    'Mẫu: I want to say I am not an old-fashioned person.',
    'Mẫu: I hope the authorities will take this matter into careful consideration.',
    'Mẫu: I do not mean to ban them, but there should be an effective way to control this kind of entertainment places.',
    'Mẫu: I am looking forward to seeing the city council do something about this matter.',
])

# ============================================================ TEST 3 – KIỂM TRA (kt.1 - kt.140, đánh số theo đề gốc)
put('kt', [
    # ---- Exercise 1 (1-10)
    ('C', '<b>kissed</b> /kɪst/ (-ed = /t/). banned, cleared, raised có -ed = /d/.'),
    ('D', '<b>watched</b> /wɒtʃt/ (-ed = /t/). recognised, stringed, conquered có -ed = /d/.'),
    ('C', '<b>encouraged</b> /ɪnˈkʌrɪdʒd/ (-ed = /d/). liked, backed, reversed có -ed = /t/.'),
    ('B', '<b>finished</b> /ˈfɪnɪʃt/ (-ed = /t/). enjoyed, suffered, agreed có -ed = /d/.'),
    ('B', '<b>released</b> /rɪˈliːst/ (-ed = /t/). performed, received, adored có -ed = /d/.'),
    ('A', '<b>artists</b> /ˈɑːtɪsts/ (-s = /s/). singers, listeners, drums có -s = /z/.'),
    ('C', '<b>organs</b> /ˈɔːɡənz/ (-s = /z/). poets, flutes, instruments có -s = /s/.'),
    ('D', '<b>contests</b> /ˈkɒntests/ (-s = /s/). melodies, festivals, guitars có -s = /z/.'),
    ('A', '<b>clips</b> /klɪps/ (-s = /s/). recordings, views, manners có -s = /z/.'),
    ('B', '<b>laughs</b> /lɑːfs/ (-s = /s/). writers, loves, awards có -s = /z/.'),
    # ---- Exercise 2 (11-30)
    ('D', 'a <b>passionate</b> interest (tính từ đứng trước danh từ).'),
    ('B', 'a writing task about the <b>biography</b> of favorite singers (tiểu sử).'),
    ('C', 'has <b>become</b> very popular (have + V3 của become).'),
    ('A', 'the <b>debut</b> album = album đầu tay.'),
    ('A', 'The <b>audience</b> cheered loudly (khán giả).'),
    ('C', 'was <b>judged</b> to be the best (được đánh giá là).'),
    ('D', '<b>launch</b> a campaign = phát động chiến dịch.'),
    ('B', '<b>invented</b> a comic style = sáng tạo ra thể loại hài.'),
    ('B', 'widespread <b>phenomenon</b> = hiện tượng phổ biến.'),
    ('A', 'attract <b>worldwide</b> attention = thu hút sự chú ý toàn cầu.'),
    ('D', 'cover <b>versions</b> = bản hát lại.'),
    ('B', '<b>folk</b> music = nhạc dân gian (Quan họ, Ca trù…).'),
    (['A', 'C'], '<b>remains</b> (khoá Word) hoặc <b>becomes</b> a profound influence – cả hai đều hợp nghĩa.'),
    ('C', 'a global <b>smash</b> hit = thành công vang dội toàn cầu.'),
    ('C', 'the 4th <b>season</b> I\'ve seen (khoá Word; episode cũng có thể nhưng ít tự nhiên).'),
    ('A', 'national <b>anthem</b> = quốc ca.'),
    ('C', 'Chopin là một trong những <b>composers</b> (nhà soạn nhạc) piano vĩ đại.'),
    ('D', 'a prominent <b>figure</b> of music = nhân vật nổi bật.'),
    ('B', '<b>conquer</b> our nerves = vượt qua nỗi lo lắng.'),
    ('D', 'best singer <b>award</b> = giải ca sĩ xuất sắc nhất.'),
    # ---- Exercise 3 (31-40)
    ('B', 'super star (ngôi sao hát) ≈ famous singer.'),
    ('B', 'fans (người hâm mộ) ≈ admirers.'),
    ('C', 'competition ≈ contest.'),
    ('C', 'well-known ≈ renowned.'),
    ('A', 'release (phát hành) ≈ put out.'),
    ('D', 'aired (phát sóng) ≈ broadcasted.'),
    ('B', 'contracts (hợp đồng) ≈ agreements.'),
    ('A', 'originated in ≈ came from.'),
    ('C', 'child prodigy ≈ genius.'),
    ('D', 'talented ≈ gifted.'),
    # ---- Exercise 4 (41-50)
    ('B', 'incredible (khó tin) ↔ <b>believable</b> (đáng tin). Các phương án còn lại đồng nghĩa.'),
    ('C', 'achievement (thành tựu) ↔ <b>failure</b>.'),
    ('A', 'eliminate (loại bỏ) ↔ <b>retain</b> (giữ lại).'),
    ('D', 'innovations (đổi mới) ↔ <b>stagnation</b> (trì trệ).'),
    ('B', 'prominent (nổi bật) ↔ <b>unknown</b> (vô danh).'),
    ('C', 'popular (phổ biến) ↔ <b>unknown</b> (ít người biết).'),
    ('B', 'wartime ↔ <b>peacetime</b> (thời bình).'),
    ('A', 'affected (giả tạo) ↔ <b>natural</b> (tự nhiên).'),
    ('B', 'adore (yêu mến) ↔ <b>hate</b> (ghét).'),
    ('D', 'confident (tự tin) ↔ <b>fearful</b> (sợ hãi).'),
    # ---- Exercise 5 (51-70)
    ('D', 'could + V: could <b>help</b>.'),
    ('C', 'make sb + V: made me <b>laugh</b>.'),
    ('A', "I'd like <b>to invite</b>."),
    ('B', 'expect sb + not to V: expect Linh <b>not to come</b> late.'),
    ('D', 'happy + to V: happy <b>to hear</b>.'),
    ('D', 'would rather + V: would rather <b>travel</b> to Hoi An than Nha Trang.'),
    ('B', 'allow sb + to V: allow my daughter <b>to play</b>.'),
    ('B', "You'd better + V: You'd better <b>go</b> out."),
    ('C', 'let sb + V: let my sister <b>go</b> camping.'),
    ('D', 'intend + not to V: intend <b>not to tell</b> him the truth.'),
    ('B', 'Kết quả → <b>so</b>: loves Japanese food, so we order it twice a week.'),
    ('A', 'Kết quả → <b>so</b> (khoá Word).'),
    ('C', 'Đối lập → <b>yet</b>: harmful, yet many people continue to smoke.'),
    ('D', 'Đối lập → <b>but</b>: lost in the forest, but luckily…'),
    ('B', 'Lựa chọn → <b>or</b>: milk tea or hot chocolate?'),
    ('D', 'Đối lập → <b>but</b>: had decayed teeth, but refused to see the dentist.'),
    ('C', 'Lí do → <b>for</b>: ought to go to university, for she wants qualifications.'),
    ('A', 'Đối lập → <b>but</b>: invested a lot, but it went bankrupt.'),
    ('A', 'Phủ định kép → <b>nor</b> did they realise.'),
    ('B', 'Lựa chọn → <b>or</b>: stay home… or go out.'),
    # ---- Exercise 6 (71-90)
    ('B', 'plan + <b>to study</b> (study → to study).'),
    ('C', "forget + to V: Don't forget <b>to call</b> (calling → to call)."),
    ('B', 'consider + V-ing: consider <b>becoming</b> (to become → becoming).'),
    ('C', "doesn't let her students + V (không dùng not): <b>use</b> (not use → use)."),
    ('A', 'hope + to V: hope <b>to have</b> (having → to have).'),
    ('D', 'make sb + V: made me <b>cry</b> (crying → cry).'),
    ('C', 'decide + to V: decided <b>to expand</b> (to expanding → to expand).'),
    ('D', 'would like to be + V3: to <b>be promoted</b> (promoted → be promoted).'),
    ('A', "had better not + V: You'd better <b>not spend</b> too much money (spend → not spend)."),
    ('B', 'learn + to V: learn <b>to fix</b> (fixing → to fix).'),
    ('A', 'Kết quả: looked at the result, <b>so</b> they decided… (but → so).'),
    ('C', 'Bổ sung: …to visit her grandma, <b>and</b> to see the Eiffel Tower (so → and).'),
    ('B', 'Kết quả: studied hard, <b>and</b> she passed (but → and).'),
    ('B', 'Đối lập: counting her calories, <b>but</b> she really wants dessert (so → but).'),
    ('C', 'nor + đảo ngữ: nor <b>did they</b> have money (they didn\'t → did they).'),
    ('D', 'make sb + V: make you <b>feel</b> betrayed (feeling → feel).'),
    ('B', 'Hai sự việc nối tiếp: went to the restaurant, <b>and</b> found out it was closed (so → and).'),
    ('C', 'Điều kiện: Don\'t forget your passport, <b>or</b> you\'ll have trouble (and → or).'),
    ('C', 'Điều kiện: have to do the assignment, <b>or</b> we\'ll be punished (and → or).'),
    ('C', 'John picked me up, <b>and</b> we went out for a walk (but → and).'),
    # ---- Exercise 7 (91-105)
    ('B', 'Hỏi giờ kết thúc → "Maybe 10:00 a.m." (dự đoán thời gian).'),
    ('A', 'Hỏi chuyên ngành → "Economics."'),
    ('D', 'Hỏi nhà vệ sinh ở đâu → chỉ đường: One flight up…'),
    ('C', 'Muốn đặt hai phòng đôi → "Sorry, we only have one double room left."'),
    ('A', 'Cảm ơn quà → "I\'m happy you like it."'),
    ('D', 'Máy in hết giấy → đề nghị giải pháp: I\'ll go and get some…'),
    ('C', 'Rủ đi mua sắm → từ chối lịch sự: Sorry, I have to work overtime.'),
    ('B', 'Hỏi đuôi "haven\'t you?" → trả lời "Sorry, but I need more time." (khoá Word, câu hơi gượng).'),
    ('B', 'Khen mèo → "Thanks. My mom gave it to me last week."'),
    ('A', 'How frequently…? → "At least once a week."'),
    ('A', 'What are you arguing about? → "Nothing."'),
    ('B', 'What\'s going on? (tại sao vui) → "I have passed the exam."'),
    ('D', 'How have you been? → "Pretty good. Thanks."'),
    ('B', 'Would you mind turning down the TV? → xin lỗi và đồng ý: Sorry. I didn\'t know…'),
    ('C', 'Do you like playing football? → "Yes, I love it."'),
    # ---- Exercise 8 (106-118)
    ('B', 'very <b>popular</b> with black Americans (phổ biến với…).'),
    ('C', 'a mixture <b>of</b> A and B.'),
    ('A', '<b>Noticing</b> the success of R&B music (nhận thấy thành công…).'),
    ('D', '<b>this</b> new white R&B music (this + danh từ số ít).'),
    ('C', 'singers <b>attracted</b> millions of teenage fans.'),
    ('A', 'very <b>dangerous</b> (tính từ sau very).'),
    ('B', 'sound the <b>same</b> (nghe giống nhau).'),
    ('D', 'started <b>by</b> singing (bắt đầu bằng việc hát) – khoá Word.'),
    ('A', 'more <b>complicated</b> melodies (tính từ).'),
    ('B', 'different instruments, <b>such</b> as the Indian sitar.'),
    ('D', 'have an influence <b>on</b> the style of popular music.'),
    ('A', 'By the <b>early</b> 1970s.'),
    ('C', 'Electronics had <b>replaced</b> the amplified guitars and drums.'),
    # ---- Exercise 9 (119-123)
    ('B', 'Leopold là nhà soạn nhạc, nghệ sĩ violin, trợ lí nhạc trưởng ở Salzburg → có nhiều vai trò trong cộng đồng âm nhạc.'),
    ('B', 'Mimicking her playing → Wolfgang bắt chước (imitated) chị.'),
    ('C', 'devoted (tận tụy) ≈ committed.'),
    ('D', 'Soon, he too was being tutored by his father → cha là người dạy đầu tiên.'),
    ('D', 'outstanding (xuất sắc) ≈ impressive.'),
    # ---- Exercise 10 (124-130)
    ('A', 'Thập niên 1960 chỉ mất một hai ngày, nay mất hàng tháng → lâu hơn trước.'),
    ('A', '"a CD or cassette will always sound very different from a live concert."'),
    ('C', 'Máy tính chỉ cần một bài thu mà hát được nhiều bài khác → "only one recorded song" KHÔNG đúng.'),
    ('D', '"the computer can sing it" → it = a song (the lyrics and music of a song).'),
    ('C', 'Công ty thường bảo ban nhạc mặc gì, nói gì, chơi thế nào → thường KHÔNG cho tự do (khoá Word).'),
    ('B', '"an image for the band that they think will attract…" → that = an image.'),
    ('D', 'too commercial = quá thiên về kiếm tiền → money-oriented.'),
    # ---- Exercise 11 (131-135)
    ('A', 'There has never been a more successful… = Pop Idol is the most successful… ever.'),
    ('C', "couldn't stand being eliminated = unable to accept the failure."),
    ('B', 'in spite of the rain = Even though it rained.'),
    ('D', 'Settling in Paris, he then took up piano → Piano was the first instrument he learnt after moving to Paris.'),
    ('D', 'Why don\'t you…? = lời gợi ý → suggested (khoá Word; "suggested me going" sai ngữ pháp nhưng là đáp án gần nhất).'),
    # ---- Exercise 12 (136-140)
    ('B', 'so busy that couldn\'t come = too busy <b>to come</b>.'),
    ('D', 'intended to study in New Jersey but studied in New York = was going to… but then…'),
    ('A', 'died in 1960, award in 1970 → After his death, he received the award.'),
    ('C', 'Hai ý đối lập → <b>but</b>.'),
    ('B', 'Hát tệ nên mọi người rời phòng → <b>so</b>.'),
], start=1)
