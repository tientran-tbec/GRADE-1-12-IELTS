# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Lớp 10 Unit 3 – Music (Global Success) – Bộ BÀI TẬP LUYỆN TẬP.
Quy ước:
  mcq  : chữ cái 'A'-'D' (hoặc list nếu chấp nhận nhiều đáp án)
  fill : danh sách đáp án chấp nhận (1 ô)
  open : chỉ có giải thích / đáp án mẫu (không chấm tự động)
Bộ này tự giải từng câu; sau đó đối chiếu với phần "ĐÁP ÁN CHI TIẾT" có sẵn ở cuối file Word. Các câu còn nghi vấn ghi ở GHI_CHU_RA_SOAT."""

GHI_CHU_RA_SOAT = [
    'Đối chiếu: đáp án tự giải khớp 100% khoá có sẵn cuối file Word (bài luyện tập, 15-minute test và 45-minute test). Phần "REVIEW 1 (Unit 1-2-3)" trong file Word là ôn tập nhiều unit nên KHÔNG đưa vào bộ này.',
    'vb1.3 (identify with): khoá Word = B (support). Nghĩa sát nhất là "đồng cảm/hiểu và chia sẻ"; không phương án nào hoàn hảo, B là lựa chọn gần nhất; giáo viên xem lại.',
    'vb1.2: khoá C (knocked out). B (expelled) cũng gần nghĩa nhưng expel thường dùng cho đuổi học/trục xuất.',
    'vb2.4 (delay): khoá A (speed up). C (hurry) cũng có thể xem là trái nghĩa nhưng không hợp collocation "hurry their concert"; giữ A.',
    'vb3.4 / vb3.5: chấp nhận cả số ít và số nhiều (competition(s), participant(s)) vì đều đúng ngữ pháp.',
    'vb5.1: chấp nhận "into" (khoá) và "to"; vb5.5: chấp nhận "on" (khoá) và "about".',
    'vb4.5: khoá D (cash prize); "money prize" không là cụm tự nhiên.',
    'vb6.2: "TV spectators" – khoá chọn B (spectators dùng cho khán giả tại sân/sự kiện, TV thì dùng viewers/audiences).',
    'vb6.3: nguồn câu cụt ("…last year," kết thúc bằng dấu phẩy) – đã sửa thành "last year." ; đáp án C (held → was held) không đổi.',
    'rd2.2 (which): khoá B (cả cụm "more musical instruments were developed and played together"). Đáp án A (musical instruments) có thể gây tranh luận nhưng "resulted in more complex sounds" là kết quả của việc phát triển và chơi cùng nhau.',
    'rd2.5: khoá C. Câu B ("nhịp sống nhanh GÂY RA mất kết nối với thiên nhiên") bài chỉ nói "possibly reflecting", không khẳng định nhân quả; D chỉ là một lý do nên không đủ "due to". Nguồn có lỗi gõ "thel980s" – đã sửa thành "the 1980s".',
    'rd2.4 / rd2.2 / rd2.3: nguồn dùng dấu nháy kép thẳng và "____" – đã chuẩn hoá thành “ ” và ______.',
    't15.10: câu gốc "No parents will not let…" (phủ định kép, lỗi nguồn); giữ nguyên đề, đáp án C (let + V bare) không đổi.',
    't15.11: đề viết "People have to find" (thì hiện tại) nhưng ngữ cảnh quá khứ ("At that time"); khoá Word dùng "had to". Là câu mở nên chấp nhận cả hai.',
    't15.15: nguồn kết thúc bằng dấu phẩy – đã sửa thành dấu chấm.',
    't45.19: khoá Word = A (culture); D (heritage) cũng hoàn toàn đúng nghĩa/ngữ pháp ("national heritage") nên chấp nhận cả A và D.',
    't45.27: khoá Word = C (on the contrary) – dùng để đối lập "âm nhạc không cần thiết" với "ngôn ngữ có mặt khắp nơi vì lý do hiển nhiên". "moreover/in addition" mang nghĩa bổ sung nên kém hợp hơn; giáo viên xem lại (chỉ nhận C).',
    't45.33: nguồn "What did the event happen after…" (sai ngữ pháp) – đã sửa thành "What event happened after…"; đáp án D theo khoá. t45.34: nguồn "between and ______" thiếu chỗ trống – đã sửa thành "between ______ and ______".',
    't45.3: online (tính từ đứng trước danh từ) nhấn âm 1 /ˈɒnlaɪn/, trong khi include nhấn âm 2 → khoá B đúng; nếu online dùng làm trạng từ/vị ngữ (/ɒnˈlaɪn/) thì cả hai nhấn âm 2, nhưng đề kiểm tra theo nghĩa tính từ.',
    'pa2.2: upload (động từ) nhấn âm 2 /ˌʌpˈləʊd/; theo khoá D khác với social, trumpet, couple (nhấn âm 1).',
    'vb1.4: nguồn thiếu dấu chấm cuối câu; vb2.1: nguồn có hai dấu chấm ".." – đã sửa.',
    'Đoạn đọc k45h (Blues): giữ nguyên nội dung; chỉ chuẩn hoá dấu nháy. Nguồn không có ảnh/audio.',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


def put_open(prefix, rows, start=1):
    for i, e in enumerate(rows, start):
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ======================= A. PHONETICS =======================
put('pa1', [
    ('C', '<b>award</b> /əˈwɔːd/: a = /ə/. travel /ˈtrævl/, talented /ˈtæləntɪd/, charity /ˈtʃærəti/: a = /æ/.'),
    ('B', '<b>music</b> /ˈmjuːzɪk/: u = /juː/. result /rɪˈzʌlt/, yummy /ˈjʌmi/, drum /drʌm/: u = /ʌ/.'),
    ('A', '<b>excited</b> /ɪkˈsaɪtɪd/: c = /s/. because /bɪˈkɒz/, cool /kuːl/, compete /kəmˈpiːt/: c = /k/.'),
    ('B', '<b>together</b> /təˈɡeðə/: ge = /ɡe/. stage /steɪdʒ/, message /ˈmesɪdʒ/, judge /dʒʌdʒ/: ge = /dʒ/.'),
    ('C', '<b>spectator</b> /spekˈteɪtə/: e = /e/. recording /rɪˈkɔːdɪŋ/, receive /rɪˈsiːv/, become /bɪˈkʌm/: e = /ɪ/.'),
])
put('pa2', [
    ('A', '<b>amazing</b> /əˈmeɪzɪŋ/ nhấn âm 2 (âm /ə/ không nhận trọng âm). beautiful, teenager, musical nhấn âm 1.'),
    ('D', '<b>upload</b> /ˌʌpˈləʊd/ nhấn âm 2 (nguyên âm đôi /əʊ/). social /ˈsəʊʃl/, trumpet /ˈtrʌmpɪt/, couple /ˈkʌpl/ nhấn âm 1.'),
    ('A', '<b>perform</b> /pəˈfɔːm/ nhấn âm 2 (động từ, âm đầu là /ə/). season, local, total nhấn âm 1.'),
    ('C', '<b>performance</b> /pəˈfɔːməns/ nhấn âm 2. instrument, popular, media nhấn âm 1.'),
    ('B', '<b>competition</b> /ˌkɒmpəˈtɪʃn/ nhấn âm 3 (đuôi -tion nhấn trước nó). identify, participant, eliminate nhấn âm 2.'),
])

# ======================= B. VOCABULARY =======================
put('vb1', [
    ('A', '<b>popular</b> (được nhiều người yêu thích, nổi tiếng) ≈ <b>well-known</b>. common = thông thường; well-received = được đón nhận; well-done = chín kỹ.'),
    ('C', '<b>eliminated</b> (bị loại) ≈ <b>knocked out</b> (bị loại khỏi cuộc thi). dropped = rơi/giảm; expelled = bị đuổi học/trục xuất; put out = dập tắt.'),
    ('B', '<b>identify with</b> (đồng cảm, hiểu và ủng hộ ai) ≈ <b>support</b> trong các phương án. recognize = nhận ra/công nhận; remember = nhớ; establish = thành lập.'),
    ('D', '<b>in search of</b> (đi tìm) ≈ <b>looking for</b>. chasing = đuổi theo; doing experiments = làm thí nghiệm; studying = học.'),
    ('C', '<b>opinions</b> (ý kiến, quan điểm) ≈ <b>points of view</b>. proverbs = tục ngữ; sayings = lời nói/châm ngôn; slogans = khẩu hiệu.'),
])
put('vb2', [
    ('A', '<b>ancient</b> (cổ xưa) ↔ <b>modern</b> (hiện đại). old-fashioned là đồng nghĩa với ancient/lỗi thời; young, late không hợp.'),
    ('C', '<b>recognised</b> (được công nhận) ↔ <b>unidentified</b> (không được xác định/nhận ra). acknowledged, conceded, accepted đều là đồng nghĩa.'),
    ('B', '<b>talented</b> (có tài) ↔ <b>talentless</b> (không có tài). gifted, brilliant là đồng nghĩa; ancient không liên quan.'),
    ('A', '<b>delay</b> (trì hoãn) ↔ <b>speed up</b> (đẩy nhanh). slow down gần nghĩa với delay; promote = quảng bá/thăng tiến; hurry = vội.'),
    ('C', '<b>arguments</b> (tranh luận, ý kiến bất đồng) ↔ <b>agreements</b> (sự đồng thuận). disagreements, comments, discussions gần nghĩa với arguments.'),
])
put('vb3', [
    (['performed'], 'Sau chủ ngữ "he" cần động từ quá khứ (When he was a teenager…) → PERFORMANCE → <b>performed</b> (biểu diễn).'),
    (['musician'], 'Sau "a(n)" cần danh từ chỉ người → <b>musician</b> (nhạc sĩ, nhạc công): "he has a nice voice, and he is a musician".'),
    (['talent'], 'Danh từ ghép "talent show" (chương trình tìm kiếm tài năng): cần danh từ <b>talent</b>, không dùng tính từ talented.'),
    (['competitions', 'competition'], '"no reality … on TV" cần danh từ: <b>competitions</b> / competition (cuộc thi truyền hình thực tế).'),
    (['participants', 'participant'], '"short performances to choose from ___" cần danh từ chỉ người tham gia: <b>participants</b> (những người tham gia).'),
])
put('vb4', [
    ('D', '<b>judges</b> (giám khảo) – "play an important role in the competition". referees: trọng tài thể thao; assessors: người đánh giá; viewers: người xem.'),
    ('B', 'perform as famous … <b>artists</b> (nghệ sĩ). spectators/judges/runners-up không phải đối tượng được "perform as".'),
    ('C', '<b>runner-up</b> = người về nhì (đứng thứ hai trong cuộc thi).'),
    ('A', '<b>vote for</b> = bỏ phiếu bình chọn cho. dress up = ăn diện; take place = diễn ra; depend on = phụ thuộc.'),
    ('D', '<b>cash prize</b> = giải thưởng tiền mặt (collocation). "money prize" không tự nhiên.'),
    ('B', '<b>on stage</b> = trên sân khấu (cụm cố định).'),
    ('C', 'Vế sau "so there was plenty of space" (quá khứ) → động từ quá khứ <b>took place</b> (diễn ra). "festival" là chủ ngữ nên cần động từ chia.'),
    ('A', 'play an important <b>role</b> in = đóng vai trò quan trọng trong.'),
    ('D', 'artists … going to <b>perform</b> in the programme = biểu diễn trong chương trình. act = diễn xuất, show = trình chiếu (kém phù hợp).'),
    ('A', '<b>depend on</b> = phụ thuộc vào (trang phục phụ thuộc vào cấp bậc của các vị thánh); chia ở số ít "depends".'),
    ('C', 'big <b>fans</b> of … music = người hâm mộ cuồng nhiệt.'),
    ('B', 'Going to <b>concerts</b> – nói về các sự kiện âm nhạc (music events) ở vế sau.'),
    ('A', '<b>made</b> her sing: make + O + V (bare) = khiến/bắt ai làm gì.'),
    ('D', 'receive <b>awards</b> such as the Grammy… = nhận giải thưởng (awards). prizes thường đi với cuộc thi cụ thể; gifts/scholarships không hợp.'),
    ('C', '<b>upload</b> videos on social media = đăng tải video lên mạng. download = tải xuống.'),
])
put('vb5', [
    (['into'], 'bring love <b>into</b> people’s lives = mang tình yêu vào cuộc sống của mọi người (chấp nhận cả "to").'),
    (['to'], 'plan <b>to</b> V = dự định làm gì.'),
    (['for'], 'vote <b>for</b> sb/sth = bình chọn cho ai/cái gì.'),
    (['of'], 'in search <b>of</b> = để tìm kiếm.'),
    (['on', 'about'], 'programmes <b>on</b> the same subject = chương trình về cùng một chủ đề (chấp nhận cả "about").'),
])
put('vb6', [
    ('B', 'Sau "not only … but also" cần cấu trúc song song: <b>not only to see … but also to hear</b>. Sửa "in order see" → "in order to see" (thiếu "to"), hoặc bỏ "in order".'),
    ('B', '<b>spectators</b> dùng cho người xem trực tiếp tại sân/sự kiện; xem qua TV phải dùng <b>viewers/audiences</b>.'),
    ('C', 'Mệnh đề quan hệ bị động: the festival which <b>was held</b> on the beach last year. "held" thiếu "was" → sửa thành "was held".'),
    ('C', 'perform <b>live</b> (trạng từ, nghĩa "trực tiếp"). "lively" là tính từ/trạng từ chỉ sự sống động, không đúng nghĩa. Sửa: lively → live.'),
    ('B', 'Sau tính từ "natural" cần danh từ: natural <b>ability</b> (khả năng bẩm sinh). Sửa: able → ability.'),
])

# ======================= C. GRAMMAR =======================
put('gr1', [
    ('D', 'Sau động từ khuyết thiếu <b>could</b> + V (bare): could <b>help</b>.'),
    ('C', '<b>make + O + V (bare)</b>: made me <b>laugh</b>.'),
    ('A', "I’d like (= would like) <b>to V</b>: I’d like to invite."),
    ('B', 'expect sb <b>to V</b>; nghĩa "mong Linh KHÔNG đến muộn" → <b>not to come</b> (phủ định đặt trước to).'),
    ('B', "had better + V (bare): You’d better <b>go</b>."),
    ('C', '<b>let + O + V (bare)</b>: let my sister <b>go</b>.'),
    ('D', 'intend <b>to V</b>; "for fear that he’ll fly into a fit of madness" → không muốn nói sự thật → <b>not to tell</b>.'),
    ('B', 'Vế sau là kết quả của vế trước (yêu thích → đặt thường xuyên) → <b>so</b> (vì vậy).'),
    ('A', 'Vế sau là kết quả của vế trước (trò chơi khó → khó mà chơi ít) → <b>so</b>.'),
    ('C', 'Hai vế tương phản (hại sức khoẻ NHƯNG nhiều người vẫn hút) → <b>yet</b> (= but).'),
    ('D', 'Hai vế tương phản (bị lạc NHƯNG may mắn có bản đồ) → <b>but</b>.'),
    ('B', 'Đưa ra lựa chọn giữa hai thứ → <b>or</b>.'),
    ('D', 'Hai vế tương phản (răng bị sâu NHƯNG từ chối đi nha sĩ) → <b>but</b>.'),
    ('C', 'Vế sau giải thích lý do cho vế trước → <b>for</b> (= because, dùng sau dấu phẩy).'),
    ('A', 'Hai vế tương phản (đầu tư nhiều tiền NHƯNG phá sản) → <b>but</b>.'),
])
put('gr2', [
    ('B', 'plan <b>to V</b>: "plans <u>to study</u> abroad". Sửa: study → to study.'),
    ('C', 'let + O + V (bare), phủ định bằng "doesn’t let"; không dùng "not use" sau let. Sửa: not use → use (không để học sinh DÙNG điện thoại).'),
    ('A', 'hope <b>to V</b>: "We hope to have a chance". Sửa: having → to have.'),
    ('D', 'make + O + <b>V (bare)</b>: made me <b>cry</b>. Sửa: crying → cry.'),
    ('C', 'decide <b>to V</b>: decided to expand. Sửa: to expanding → to expand.'),
    ('A', "Had better + (<b>not</b>) V: You’d better <b>not spend</b> too much money… Sửa: spend → not spend."),
    ('B', 'learn <b>to V</b>: learn to fix. Sửa: fixing → to fix.'),
    ('C', 'Hai vế cùng bổ sung mục đích (thăm bà và ngắm tháp Eiffel) → nối bằng <b>and</b>, không dùng "so". Sửa: so → and.'),
    ('B', 'Hai vế cùng nghĩa tích cực (học chăm → đỗ xuất sắc) → dùng <b>and/so</b>, không dùng "but" (tương phản). Sửa: but → and (hoặc so).'),
    ('B', 'Vế sau tương phản với vế trước (đang giảm calo NHƯNG muốn ăn tráng miệng) → <b>but</b>. Sửa: so → but.'),
    ('D', 'make + O + <b>V (bare)</b>: make you <b>feel</b> betrayed. Sửa: feeling → feel.'),
    ('B', 'Vế sau "phát hiện ra nó đóng cửa" đối lập với việc đã đến → <b>but</b>/and, không phải kết quả. Sửa: so → but (hoặc and).'),
    ('C', 'Don’t forget …, <b>or</b> you’ll have trouble: "nếu không thì" → dùng <b>or</b>. Sửa: and → or.'),
    ('C', 'We also have to do the assignment, <b>or</b> we’ll be punished (nếu không thì bị phạt). Sửa: and → or.'),
    ('C', 'Hai hành động nối tiếp nhau cùng chiều (đón rồi đi dạo) → <b>and</b>, không dùng "but". Sửa: but → and.'),
])

# ======================= D. SPEAKING =======================
put('sp1', [
    ('B', 'Hỏi "Who is that?" (đó là ai?) → giới thiệu danh tính: <b>He’s a famous singer.</b>'),
    ('C', 'Hỏi "Do you know that singer?" → <b>Yes. I’m a big fan of his.</b> (trả lời Yes + thông tin). "Yes, he is" sai trợ động từ.'),
    ('A', 'Hỏi "Why do you love…?" (lý do) → <b>His music is great.</b>'),
    ('D', 'Hỏi "Can he play a musical instrument?" → <b>I’m not sure but he’s learning to play the guitar.</b> (liên quan nhạc cụ). He can dance / He’s good at singing không trả lời câu hỏi về nhạc cụ.'),
    ('B', 'Hỏi về sự nghiệp (career) → <b>He became an online star at the age of 12.</b>'),
])

# ======================= E. READING =======================
put('rd1', [
    ('B', 'music has been found to <b>reduce</b> stress and anxiety levels = giảm căng thẳng. terminate/stop = chấm dứt hẳn; diminish là từ gần nghĩa nhưng reduce là collocation phổ biến nhất với stress.'),
    ('A', 'Đại từ quan hệ chỉ vật thay cho "a chemical in the brain": <b>that</b> makes us feel happy. who dùng cho người; when/where không hợp.'),
    ('B', 'stay focused on the task <b>at hand</b> = tập trung vào nhiệm vụ trước mắt (cụm cố định).'),
    ('C', '<b>Another</b> benefit is… = một lợi ích khác (another + danh từ số ít). Others/Other không đi với danh từ số ít.'),
    ('A', 'enhance brain <b>function</b> = tăng cường chức năng não. role/mission/task không hợp collocation.'),
    ('B', 'the ability to <b>evoke</b> emotions and memories = gợi lên cảm xúc và ký ức.'),
    ('C', 'incorporate sth <b>into</b> sth = đưa/kết hợp cái gì vào cái gì.'),
    ('D', '<b>reap</b> the benefits = gặt hái lợi ích (collocation cố định). earn/take/maximize không đi với benefits tự nhiên bằng.'),
])
put('rd2', [
    ('B', 'Bài nói âm nhạc thay đổi qua thời gian cùng sự thay đổi của xã hội → tiêu đề phù hợp: <b>Music: Now and Then</b>. Các phương án khác chỉ nêu một phần nội dung.'),
    ('B', '"With time, more musical instruments were developed and played together, <b>which</b> resulted in more sophisticated sounds" → which thay cho cả mệnh đề: việc phát triển và chơi cùng nhau nhiều nhạc cụ.'),
    ('A', '<b>retain</b> (giữ lại, duy trì) ≈ <b>preserve</b> (bảo tồn). reduce = giảm; exchange = trao đổi; combine = kết hợp.'),
    ('C', 'Đoạn 2: "modern society has lost this connection (to nature)" → mối liên hệ với thiên nhiên GIẢM, các đặc điểm khác (volume louder, faster pace, more complex) đều tăng → EXCEPT <b>the connection to nature</b>.'),
    ('C', 'Đoạn 2: "The beats, rhythms, tempo and lyrics of songs all changed along with the change in cultures" → gần như mọi đặc điểm thay đổi khi văn hoá thay đổi (C). A không được nêu; B bài không khẳng định quan hệ nhân quả; D chỉ là một nguyên nhân phụ.'),
])

# ======================= 15-MINUTE TEST =======================
put('t15', [
    ('A', 'a big <b>fan</b> of sb/sth = người hâm mộ cuồng nhiệt.'),
    ('B', 'Khi còn học trung học, anh ấy đã <b>performed</b> (biểu diễn) ở trường vào những ngày đặc biệt.'),
    ('D', 'From the semi-final <b>onwards</b> = từ vòng bán kết trở đi.'),
    ('C', 'short <b>performances</b> (những phần trình diễn ngắn) – cần danh từ số nhiều sau tính từ "short".'),
    ('A', 'organised <b>in search of</b> = được tổ chức để tìm kiếm. in spite of = mặc dù; due to/because of = vì (chỉ nguyên nhân).'),
    ('C', '<b>play</b> an important role = đóng vai trò quan trọng.'),
    ('B', 'Chủ ngữ số nhiều cần danh từ: <b>participants</b> (người tham gia) sẽ hóa trang và biểu diễn.'),
    ('D', 'vote <b>for</b> sb/sth.'),
    ('A', 'expect <b>to V</b>: expected to see.'),
    ('C', '<b>let + O + V (bare)</b>: let their teenage kids watch.'),
], start=1)
put_open('t15', [
    '<b>Đáp án mẫu:</b> At that time there were many movies and TV series, <b>so</b> people had to find them on the Internet. (vế sau là kết quả → so; chấp nhận "have to".)',
    '<b>Đáp án mẫu:</b> The style of clothes in Chau van singing has changed over time, <b>but</b> the rules about the colours stayed the same. (hai ý tương phản → but)',
    '<b>Đáp án mẫu:</b> Their favourite music is American pop music, <b>so</b> they always listen to it. (vế sau là kết quả → so)',
    '<b>Đáp án mẫu:</b> She writes her own songs, <b>and</b> they always become hits right after they are introduced. (bổ sung thông tin → and)',
    '<b>Đáp án mẫu:</b> We can go to a live concert at the stadium, <b>or</b> we can watch it live on TV at home. (hai lựa chọn → or)',
], start=11)

# ======================= 45-MINUTE TEST =======================
put('t45', [
    ('A', '<b>idol</b> /ˈaɪdl/: i = /aɪ/. singer /ˈsɪŋə/, opinion /əˈpɪnjən/, winner /ˈwɪnə/: i = /ɪ/.'),
    ('C', 'season /ˈsiːzn/: s = /z/. see /siː/, stage /steɪdʒ/, series /ˈsɪəriːz/ (âm s đầu) = /s/.'),
    ('B', '<b>include</b> /ɪnˈkluːd/ nhấn âm 2. famous /ˈfeɪməs/, comment /ˈkɒment/, online (tính từ) /ˈɒnlaɪn/ nhấn âm 1.'),
    ('D', '<b>competition</b> /ˌkɒmpəˈtɪʃn/ nhấn âm 3. reality /riˈæləti/, identify /aɪˈdentɪfaɪ/, participants /pɑːˈtɪsɪpənts/ nhấn âm 2.'),
    ('C', '<b>exciting</b> /ɪkˈsaɪtɪŋ/ nhấn âm 2. programme /ˈprəʊɡræm/, argument /ˈɑːɡjumənt/, different /ˈdɪfrənt/ nhấn âm 1.'),
    ('A', 'argument for fun (tranh luận cho vui) ≈ <b>debate</b> (cuộc tranh luận). reason = lý do; excuse = lời bào chữa; issue = vấn đề.'),
    ('D', '<b>preferred</b> (được ưa thích hơn) ≈ <b>favourite</b> (yêu thích).'),
    ('C', '<b>good at</b> (giỏi về) ↔ <b>bad at</b> (kém về). keen on / excited about gần nghĩa tích cực.'),
    ('A', '<b>stay the same</b> (giữ nguyên) ↔ <b>become different</b> (trở nên khác). "are similar" gần nghĩa với stay the same.'),
    ('C', 'make + O + <b>adj</b>: make the show <b>exciting</b> (khiến chương trình thú vị). exciting mô tả sự việc; excited mô tả người.'),
    ('B', 'shown <b>on</b> television (trên truyền hình) – cụm cố định.'),
    ('D', '<b>dress up</b> and perform as famous artists = hóa trang thành các nghệ sĩ nổi tiếng.'),
    ('A', 'The <b>prize</b> for the winner = giải thưởng dành cho người thắng cuộc. cost/price = chi phí/giá cả; score = điểm.'),
    ('D', '<b>vote for</b> the participant you love most = bình chọn cho thí sinh bạn thích nhất.'),
    ('C', 'decided to be a <b>musician</b> = nhạc sĩ/nhạc công (danh từ chỉ nghề sau mạo từ a).'),
    ('A', 'Sau tính từ "exciting" cần danh từ số nhiều: <b>performances</b> (các buổi biểu diễn).'),
    ('B', 'plenty of <b>space</b> = nhiều không gian. vacancies = vị trí còn trống (tuyển dụng); positions/points không hợp.'),
    ('D', 'a <b>typical</b> type of Chau Van singing = một loại hình tiêu biểu của hát Chầu văn.'),
    (['A', 'D'], 'national <b>culture</b> (văn hoá quốc gia) – khoá Word; <b>heritage</b> (di sản quốc gia) cũng đúng nghĩa nên chấp nhận cả hai. costume = trang phục; custom = phong tục.'),
    ('C', 'hesitate <b>to V</b> = do dự làm gì.'),
    ('B', 'Trước danh từ "ability" cần tính từ: <b>natural</b> ability (khả năng bẩm sinh).'),
    ('D', '<b>famous for</b> = nổi tiếng vì. popular with/among; helpful to; good at – không đi với "for" theo nghĩa này.'),
    ('B', 'Hurried as fast as I could <b>but</b> I arrived late as usual: hai vế tương phản (đã cố gắng nhưng vẫn muộn) → sửa "so" → "but".'),
    ('C', 'decide <b>to V</b>: decided to delay. Sửa: delaying → to delay.'),
    ('A', 'Sau "Five best" cần danh từ chỉ người: <b>participants</b> (thí sinh). participations (sự tham gia) sai nghĩa. Sửa: participations → participants.'),
    ('B', 'one of the human species’ relatively few <b>omnipresent</b> abilities = khả năng có ở mọi nơi/mọi người. parochial = hẹp hòi; sophisticated = tinh vi; divergent = khác biệt.'),
    ('C', 'Language, <b>on the contrary</b>, is also everywhere: đối lập "âm nhạc không cần thiết" với "ngôn ngữ có mặt khắp nơi vì lý do hiển nhiên" (theo khoá Word).'),
    ('A', 'spring directly <b>from</b> = bắt nguồn trực tiếp từ.'),
    ('D', 'be <b>fascinated</b> by sth = bị hấp dẫn, say mê bởi. repulsed = ghê tởm; counteracted = chống lại; defeated = bị đánh bại.'),
    ('A', 'Chủ ngữ số ít "language" + thì hiện tại hoàn thành bị động: <b>has long been considered</b>. Trạng từ long đứng giữa has và been.'),
    ('C', 'Đoạn 1: "created in the late 19th century, by the black slaves…" → <b>in the late 19th century by the black slaves</b>.'),
    ('B', 'Đoạn 2: "The purpose of making the blues… the expression of intense emotions" → <b>express the intense emotions</b>.'),
    ('D', 'Đoạn 3: "Chicago blues came next, when the delta musicians started traveling to the big city to look for a better life" → <b>immigrated to the large city</b> (di cư lên thành phố lớn).'),
    ('C', 'Đoạn 3: "The biggest difference between the two styles (Mississippi delta & Chicago) is the use of electric guitars and a slightly faster pace in the latter" → <b>Chicago blues – Mississippi delta blues</b>.'),
    ('A', 'Đoạn 3: Texas blues "was made famous by artists like Lightnin’ Hopkins and Freddie King" → <b>Freddie King</b>.'),
    ('D', 'Ann rủ cuối tuần cùng làm gì → Minh từ chối lịch sự, đưa lý do: <b>Sorry, I can’t. I have to prepare for my exam.</b> A, B, C không phù hợp ngữ cảnh.'),
    ('C', 'Ann rủ đi xem show → đồng ý: <b>Sounds great.</b> Never mind / Don’t mention it dùng đáp lại lời xin lỗi/cảm ơn.'),
    ('B', 'Hai câu hỏi là hai lựa chọn → nối bằng <b>or</b>: Should we watch TV <b>or</b> go to the cinema tonight?'),
    ('D', '"Let’s + V" (đề nghị) ≈ <b>How about + V-ing?</b>. Why don’t you / You should là lời khuyên; have to là bắt buộc.'),
    ('A', 'allow sb to do sth ≈ <b>let sb do sth</b> (cho phép). make = bắt buộc; expect/ask khác nghĩa.'),
])
