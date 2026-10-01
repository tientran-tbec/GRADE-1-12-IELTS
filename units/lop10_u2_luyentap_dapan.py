# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Lớp 10 Unit 2 (Global Success) – Bộ BÀI TẬP LUYỆN TẬP.
Quy ước:
  mcq  : chữ cái 'A'-'D' (hoặc list nếu chấp nhận nhiều đáp án)
  fill : danh sách đáp án chấp nhận (1 ô)  hoặc {'blanks': [[...],[...]]} (nhiều ô)
  open : không chấm, EXPLANATIONS là bài mẫu
Bộ này tự giải từng câu, sau đó đối chiếu với phần "ĐÁP ÁN CHI TIẾT" có sẵn cuối file Word. Các câu còn nghi vấn ghi ở GHI_CHU_RA_SOAT."""

GHI_CHU_RA_SOAT = [
    'Đối chiếu: đáp án tự giải khớp 100% khoá có sẵn cuối file Word (bài luyện tập, 15-minute và 45-minute test). Các câu dưới đây khoá chấp nhận được nhưng có phương án khác cũng có thể đúng – giáo viên xem lại.',
    'vb1.3 (impact ≈ ?): khoá C (effect); A (influence) cũng đồng nghĩa với impact nên chấp nhận cả C và A. vb1.2 (eco-friendly): khoá D; climate-friendly (A) hẹp nghĩa hơn nên chỉ nhận D. vb1.5 (modern): khoá D (up-to-date); current/contemporary/recent cũng gần nghĩa nhưng khoá chọn D.',
    'vb2.3 (sustainable): khoá C (untenable); wasteful (D) cũng là từ trái nghĩa theo ngữ cảnh lối sống nên chấp nhận cả C và D. vb2.4 (raw materials): khoá D (prepared); cooked (C) trái nghĩa với raw khi nói về thức ăn, không hợp "raw materials" nên chỉ nhận D.',
    'vb4.2 (The club’s ___ is to improve…): khoá D (aim); purpose (C) cũng đúng nên chấp nhận cả D và C. t45.6 (issues): khoá C (matters); concerns (A) cũng đồng nghĩa nên chấp nhận cả C và A.',
    'vb3.3 (ELECTRIC): khoá electrical; "electric appliances" cũng đúng nên chấp nhận cả hai. vb6.5: khoá C (electric → electrical company, "công ty điện lực"); "electric company" vẫn dùng được trong tiếng Anh Mỹ nên đây là câu hơi mơ hồ – giáo viên xem lại.',
    'gr1.5: nguồn "You (cook) ___ for the party?" nhưng khoá là "Are you going to cook" (đảo chủ ngữ); đã đưa "You" vào ô trống để khớp khoá. gr1.1: khoá will be, nhưng "is going to be" (dự đoán/sự việc chắc chắn) cũng chấp nhận.',
    'gr2.3: khoá B "have been showed" – dạng đúng chuẩn là "shown" (showed là quá khứ); đề nguồn không có "shown" nên vẫn chọn B (đúng cấu trúc hiện tại hoàn thành bị động), ghi chú trong lời giải. gr3 (viết lại câu): câu mở, không chấm, có đáp án mẫu theo khoá.',
    'sp1.4: khoá A ("How do you know about it?") – đây là câu hỏi lại ngầm xác nhận; C "I’m excited about it." cũng là câu đáp tự nhiên nhưng không trả lời trực tiếp nên giữ khoá A; giáo viên xem lại.',
    't15.5: khoá B (isn’t going to invite); D (won’t invite) cũng hợp lý (quyết định/suy nghĩ của người nói) nên chấp nhận cả B và D. Các câu t15 còn lại theo khoá.',
    'Đề nguồn: vb5.2 dấu nháy "…" đã đổi thành “…”; vb1.3 khoảng trắng thừa trong thẻ gạch chân "impact " đã sửa; dấu nháy ’ thống nhất; phần "READING" lẫn vào cuối câu 25 (45-minute) đã bỏ; câu 14 phần Grammar (When … ?) đã dựng lại dạng hội thoại.',
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


# ======================= A. PHONETICS =======================
put('pa1', [
    ('D', 'r<b>ea</b>dy /ˈredi/: ea = /e/. please /pliːz/, team /tiːm/, clean /kliːn/: ea = /iː/.'),
    ('B', 'p<b>o</b>llute /pəˈluːt/: o = /ə/. adopt /əˈdɒpt/, bottle /ˈbɒtl/, topic /ˈtɒpɪk/: o = /ɒ/.'),
    ('A', 'cl<b>i</b>mate /ˈklaɪmət/: i = /aɪ/. include /ɪnˈkluːd/, different /ˈdɪfrənt/, Internet /ˈɪntənet/: i = /ɪ/.'),
    ('C', '<b>c</b>arbon /ˈkɑːbən/: c = /k/. source /sɔːs/, decide /dɪˈsaɪd/, cycle /ˈsaɪkl/: c = /s/.'),
    ('D', '<b>th</b>under /ˈθʌndə/: th = /θ/ (vô thanh). other /ˈʌðə/, although /ɔːlˈðəʊ/, those /ðəʊz/: th = /ð/.'),
])
put('pa2', [
    ('B', '<b>weekend</b> /ˈwiːkend/ nhấn âm 1 (danh từ ghép). improve /ɪmˈpruːv/, attend /əˈtend/, reduce /rɪˈdjuːs/ nhấn âm 2.'),
    ('D', '<b>protect</b> /prəˈtekt/ nhấn âm 2 (không nhấn /ə/). local /ˈləʊkl/, welcome /ˈwelkəm/, issue /ˈɪʃuː/ nhấn âm 1.'),
    ('A', '<b>interesting</b> /ˈɪntrəstɪŋ/ nhấn âm 1. awareness /əˈweənəs/, encourage /ɪnˈkʌrɪdʒ/, protection /prəˈtekʃn/ nhấn âm 2.'),
    ('B', '<b>environment</b> /ɪnˈvaɪrənmənt/ nhấn âm 2. exhibition /ˌeksɪˈbɪʃn/, electronic /ɪˌlekˈtrɒnɪk/, estimation /ˌestɪˈmeɪʃn/ nhấn âm 3.'),
    ('D', '<b>remind</b> /rɪˈmaɪnd/ nhấn âm 2 (động từ). lifestyle /ˈlaɪfstaɪl/, footprint /ˈfʊtprɪnt/, member /ˈmembə/ nhấn âm 1.'),
])

# ======================= B. VOCABULARY =======================
put('vb1', [
    ('A', '<b>lead to</b> = <b>result in</b> (dẫn đến). result from = do bởi (ngược chiều); involve in và turn up không hợp nghĩa.'),
    ('D', '<b>eco-friendly</b> = <b>environmentally-friendly</b> (thân thiện với môi trường). climate-friendly chỉ riêng khí hậu; unfriendly = không thân thiện; kindly = tử tế.'),
    (['C', 'A'], '<b>impact on</b> = <b>effect on</b> (tác động đến). influence cũng đồng nghĩa nên chấp nhận; consequence = hậu quả; circumstance = hoàn cảnh.'),
    ('A', '<b>emissions</b> (sự thải ra) ≈ <b>discharges</b> (sự xả thải). controls = kiểm soát; reductions = giảm bớt; expansion = mở rộng.'),
    ('D', '<b>modern</b> (hiện đại) ≈ <b>up-to-date</b> (cập nhật, hiện đại). current/contemporary/recent cũng gần nghĩa nhưng khoá chọn up-to-date (mô tả thiết bị mới).'),
])
put('vb2', [
    ('B', '<b>natural</b> (tự nhiên) ↔ <b>artificial</b> (nhân tạo). gentle = nhẹ nhàng; pure = tinh khiết; uncommon = hiếm.'),
    ('B', '<b>reduce</b> (giảm) ↔ <b>increase</b> (tăng). lower = hạ thấp (đồng nghĩa); rise = tăng nhưng là nội động từ (không đi với tân ngữ); improve = cải thiện.'),
    (['C', 'D'], '<b>sustainable</b> (bền vững) ↔ <b>untenable</b> (không thể duy trì); wasteful (lãng phí) cũng trái nghĩa theo ngữ cảnh lối sống. continual/viable gần nghĩa với sustainable.'),
    ('D', '<b>raw</b> (thô, chưa qua xử lý) ↔ <b>prepared</b> (đã được chế biến/xử lý). unprocessed cùng nghĩa với raw; well-done/cooked chỉ dùng cho thức ăn.'),
    ('D', '<b>harmful</b> (có hại) ↔ <b>helpful</b> (có ích). fortunate = may mắn; profitable = sinh lời; favorable = thuận lợi.'),
])
put('vb3', [
    (['reusable'], 'Sau mạo từ "a", trước danh từ "bag" cần <b>tính từ</b>: use → <b>reusable</b> (có thể tái sử dụng).'),
    (['refillable'], 'Trước danh từ "bottle" cần tính từ: refill → <b>refillable</b> (có thể làm đầy lại).'),
    (['electrical', 'electric'], 'Trước danh từ "appliances" cần tính từ: <b>electrical</b> appliances = thiết bị điện (electric cũng được chấp nhận).'),
    (['heat'], 'Sau "to" cần động từ nguyên mẫu: hot → <b>heat</b> (làm nóng): "to heat the water".'),
    (['estimated'], 'It can be + <b>V3/ed</b> (bị động): estimation → <b>estimated</b> (được ước tính).'),
])
put('vb4', [
    ('B', 'be <b>keen to</b> do sth = háo hức làm gì ("I’m keen to reduce…"). keen on + V-ing; be used to + V-ing; be used for + V-ing nên không hợp sau chỗ trống là "reduce".'),
    (['D', 'C'], 'The club’s <b>aim</b> is to… = mục tiêu của câu lạc bộ (aim for/at). purpose cũng chấp nhận; wish/desire là mong muốn cá nhân.'),
    ('A', 'raise people’s <b>awareness</b> of sth (nâng cao nhận thức); sau tính từ sở hữu cần danh từ. aware/unaware là tính từ.'),
    ('C', '<b>sort</b> and recycle = phân loại và tái chế (theo bài từ vựng "sort"). reduce = giảm; produce = sản xuất; break = làm vỡ.'),
    ('B', 'the <b>average</b> carbon footprint = lượng phát thải trung bình (average = trung bình). medium = cỡ vừa; personal = cá nhân.'),
    ('D', 'your <b>personal</b> car or motorbike = xe riêng, đối lập với public transport.'),
    ('A', '<b>turn off</b> appliances = tắt thiết bị để tiết kiệm năng lượng. turn on = bật; turn up = vặn to; turn down = vặn nhỏ.'),
    ('C', 'thích nghe nhạc to nên <b>turned up</b> the radio = vặn to đài.'),
    ('B', '<b>drop</b> litter = vứt rác bừa bãi (collocation). make/keep/hold litter không dùng.'),
    ('D', '<b>set up</b> = thành lập: "The club is set up by the Youth Union." (bị động). clean up = dọn dẹp; pick up = nhặt/đón; be based on = dựa trên.'),
    ('A', 'be able <b>to do</b> sth = có thể làm gì.'),
    ('C', '<b>remind</b> sb to do sth = nhắc ai làm gì ("Students are reminded to pick up litter").'),
    ('B', 'attract <b>attention</b> = thu hút sự chú ý. attend là động từ; attentive là tính từ; attentively là trạng từ.'),
    ('D', 'a <b>source</b> of energy = nguồn năng lượng ("the Sun is a source of energy"). resource = tài nguyên (nói chung); base/root không hợp.'),
    ('B', '<b>make</b> a decision = đưa ra quyết định (collocation). have/take/get a decision không dùng.'),
])
put('vb5', [
    (['down'], 'break <b>down</b> = phân hủy, vỡ ra thành mảnh nhỏ.'),
    (['on'], 'cut down <b>on</b> sth = cắt giảm cái gì.'),
    (['in', 'In'], '<b>In</b> conclusion = tóm lại, kết luận lại.'),
    (['for'], 'be compulsory <b>for</b> sb = bắt buộc đối với ai.'),
    (['on'], 'give a presentation <b>on</b> sth = thuyết trình về cái gì.'),
])
put('vb6', [
    ('B', 'encourage sb <b>to do</b> sth: <b>planting</b> → <b>to plant</b> more trees.'),
    ('D', 'make a big <b>difference</b> (danh từ) = tạo ra khác biệt lớn: <b>different</b> → <b>difference</b>.'),
    ('A', 'search <b>for</b> sth = tìm kiếm cái gì; "search on" sai: <b>on</b> → <b>for</b> information.'),
    ('B', 'be <b>based on</b> sth = dựa trên cái gì: <b>based in</b> → <b>based on</b>.'),
    ('C', 'electric = chạy bằng điện (máy móc); <b>electrical</b> = liên quan đến điện (ngành/công ty điện): <b>electric</b> → <b>electrical</b> company (công ty điện lực). Các phần còn lại (has been working for, more than) đều đúng.'),
])

# ======================= C. GRAMMAR =======================
put('gr1', [
    (['will be', 'is going to be'], '"next month" – sự việc chắc chắn trong tương lai (tuổi tăng) → tương lai đơn: Tommy <b>will be</b> fifteen years old next month.'),
    (['is going to be'], '"Look at the Sun" – dự đoán dựa trên dấu hiệu nhìn thấy → <b>be going to</b>: It <b>is going to be</b> a beautiful day.'),
    (['is going to buy'], 'Dự định đã có từ trước ("has already saved enough money") → <b>be going to</b>: David <b>is going to buy</b> a new car.'),
    (['will lose'], '"I think …" – dự đoán theo suy nghĩ cá nhân → <b>will</b>: Thompson <b>will lose</b> his job.'),
    (['Are you going to cook'], 'Có căn cứ nhìn thấy ("I see a lot of ingredients") → <b>be going to</b>, câu hỏi đảo: <b>Are you going to cook</b> for the party?'),
    (['will call'], '"I promise" – lời hứa → <b>will</b> + V: I <b>will call</b> as soon as I arrive. (sau as soon as dùng hiện tại đơn "arrive").'),
    (['are going to hold'], '"as planned" – kế hoạch đã định trước → <b>be going to</b>: We <b>are going to hold</b> an international conference.'),
    (['will do'], 'Quyết định ngay tại lúc nói ("I forgot to phone Dad. I … right after lunch") → <b>will</b>: I <b>will do</b> it.'),
    (["won't go", 'will not go'], 'Dự đoán không có căn cứ cụ thể ("before the 22nd century") → <b>will</b>: People <b>won’t go</b> to Mars before the 22nd century.'),
    (['are going to take'], 'Dự định đã chuẩn bị từ lâu ("have already prepared well…") → <b>be going to</b>: Linda and her friends <b>are going to take</b> a trip.'),
])
put('gr2', [
    ('B', '"last week" → quá khứ đơn bị động: <b>was made</b> (was/were + V3).'),
    ('B', '"every day" → hiện tại đơn bị động: flowers and plants <b>are watered</b> (am/is/are + V3).'),
    ('B', '"since January" → hiện tại hoàn thành bị động: <b>have been showed</b> (have + been + V3; dạng chuẩn của show là "shown", đề dùng showed nhưng B là phương án duy nhất đúng cấu trúc).'),
    ('B', 'Câu trả lời "In 1876" → quá khứ; câu hỏi bị động đảo: <b>was the telephone invented</b>?'),
    ('A', 'by the time + quá khứ đơn (came), mệnh đề chính quá khứ hoàn thành bị động: <b>had been finished</b> – came.'),
    ('B', 'Đang xảy ra lúc nói ("Do you hear the footsteps…?") → hiện tại tiếp diễn bị động: <b>are being followed</b>.'),
    ('A', '"at this time last night" → quá khứ tiếp diễn bị động: <b>was being repaired</b> (was/were + being + V3).'),
    ('A', '"next Monday" → tương lai đơn bị động: <b>will be done</b>.'),
    ('C', '"this weekend" – dự định → be going to bị động: <b>are going to be organized</b> (activities số nhiều).'),
    ('C', 'Động từ khuyết thiếu bị động: must <b>be checked</b> (modal + be + V3).'),
])
put_open('gr3', [
    '<b>Đáp án:</b> All the classrooms will be cleaned up by the club members. (Bị động của thì tương lai đơn: will + be + V3.)',
    '<b>Đáp án:</b> Their presentation on environmental protection is being practiced by the students. (Bị động của hiện tại tiếp diễn: is/are being + V3.)',
    '<b>Đáp án:</b> A green lifestyle is adopted by more and more people. (Bị động của hiện tại đơn: is/are + V3.)',
    '<b>Đáp án:</b> A reusable bag should be brought when we go shopping. (Bị động của should: should + be + V3.)',
    '<b>Đáp án:</b> Has the problem been discussed with anyone? (Bị động của hiện tại hoàn thành, nghi vấn: Has/Have + S + been + V3?)',
])

# ======================= D. SPEAKING =======================
put('sp1', [
    ('B', 'Câu hỏi What về kế hoạch → trả lời nêu kế hoạch: <b>Nothing special. I have a meeting.</b> Câu D (Yes) không hợp câu hỏi What.'),
    ('A', 'Hỏi "What club…?" → nêu tên/loại câu lạc bộ: <b>A club run by the Youth Union.</b> B trả lời nơi chốn, C thời gian, D tính chất.'),
    ('D', 'Hỏi "Does your club have social activities?" → <b>Sure. Its aim is to protect the environment.</b> (khẳng định + giải thích). C "No. I don’t agree." không hợp.'),
    ('A', 'Câu hỏi xác nhận kế hoạch → <b>How do you know about it?</b> (ngầm xác nhận là đúng). C "I’m excited about it." cũng tự nhiên nhưng không trả lời trực tiếp; B "Yes, that’s it" không hợp; D sai chủ ngữ.'),
    ('C', 'Xin tham gia câu lạc bộ → đồng ý: <b>Yes, of course.</b> A/D từ chối vô lý; B "you’ll be fine" không phù hợp.'),
])

# ======================= E. READING =======================
put('rd1', [
    ('B', 'all <b>contribute</b> to this = cùng góp phần vào (contribute to). cause + O (không đi với to); induce/result không hợp "to this".'),
    ('D', 'a congestion charge, a <b>fee</b> paid by drivers = một khoản phí. pension = lương hưu; stipend = trợ cấp; fine = tiền phạt (không hợp ngữ cảnh phí).'),
    ('D', 'Ý đối lập: ban đầu dư luận phản đối, <b>but</b> người dân sớm ủng hộ.'),
    ('C', 'the <b>number</b> of cars = số lượng ô tô (danh từ đếm được, cần "the number of").'),
    ('A', 'Đại từ quan hệ thay cho cả mệnh đề trước (dấu phẩy + which): "the scheme proved massively profitable, <b>which</b> allowed the city council to invest…".'),
])
put('rd2', [
    ('A', 'Cả bài nói về ô nhiễm nước ở Việt Nam (nguyên nhân, hậu quả, giải pháp) → tiêu đề: <b>Water Pollution in Vietnam</b>.'),
    ('C', 'Đoạn 1: "Vietnam ranks fourth with 1.8 million" – xếp thứ tư trong danh sách <b>12 quốc gia</b> (toàn cầu), không phải xếp hạng trong khu vực Đông Nam Á → C <b>không đúng</b>. A (5 trên 12 nước), B (5 giây tạo ra, 500–1000 năm phân huỷ), D (10 năm gần đây) đều đúng với bài.'),
    ('D', '"…pour waste into rivers and streams, <b>which</b> the government cannot control at all" → which thay cho cả hành động: các công ty không quản lý rác và xả thải ra sông suối.'),
    ('D', 'Các nguyên nhân gây bệnh gồm: thiếu nước sạch/nhà vệ sinh, không có hệ thống lọc, giếng đào không sạch. Sinh vật biển chết là hậu quả ô nhiễm, <b>không phải</b> lý do bệnh ở vùng sâu → D.'),
    ('B', '<b>urgent</b> (cấp bách) ≈ <b>pressing</b>. trivial = tầm thường; nervous = lo lắng; dangerous = nguy hiểm.'),
])

# ======================= 15-MINUTE TEST =======================
put('t15', [
    ('C', 'Quyết định ngay lúc nói ("This shirt looks beautiful. I … it.") → <b>will buy</b>.'),
    ('A', 'Đã đặt chỗ trước ("I have made a reservation") → kế hoạch có từ trước: <b>are going to have</b>.'),
    ('D', '"The Sun is shining" – dự đoán dựa trên dấu hiệu hiện tại → <b>is going to be</b>.'),
    ('B', 'Câu điều kiện "or" (cảnh báo/dự đoán): "or the neighbour <b>will get</b> angry".'),
    (['B', 'D'], 'Quyết định/dự định không mời: <b>isn’t going to invite</b> (khoá) hoặc <b>won’t invite</b> đều hợp lý.'),
    ('D', '"I’m sure…" – dự đoán theo niềm tin → <b>will be</b>.'),
    ('A', '"no matter who calls her" – sự từ chối nhất quán, ý chí → <b>will not answer</b>.'),
    ('C', 'Dự đoán về tương lai (với kính mới) → <b>will be</b> able to see. "You" đi với are/will be.'),
    ('B', '"I don’t think…" – quan điểm cá nhân, dự đoán → <b>will get</b>.'),
    ('A', '"Look at the child’s face." – dấu hiệu nhìn thấy → <b>is going to cry</b>.'),
    ('D', 'aim at + <b>V-ing</b>: aims at <b>joining</b> the Environment Club.'),
    ('B', 'raise people’s <b>awareness</b> of sth (danh từ sau sở hữu cách).'),
    ('A', '<b>Turning off</b> your appliances = tắt thiết bị khi không dùng (in use = đang dùng) để tiết kiệm năng lượng. V-ing làm chủ ngữ.'),
    ('C', '<b>refillable</b> bottles = chai có thể làm đầy lại, giảm rác nhựa. renewable = có thể tái tạo (năng lượng); remarkable = đáng chú ý.'),
    ('D', 'instead of + V-ing: sort and recycle instead of <b>throwing away</b> them (vứt đi). Các cụm còn lại không hợp nghĩa.'),
])

# ======================= 45-MINUTE TEST =======================
put('t45', [
    ('D', 'r<b>u</b>bbish /ˈrʌbɪʃ/: u = /ʌ/. pollute /pəˈluːt/, reduce /rɪˈdjuːs/, fortune /ˈfɔːtʃuːn/: u = /uː/ (/juː/).'),
    ('A', '<b>i</b>mprove /ɪmˈpruːv/: i = /ɪ/. environment /ɪnˈvaɪrənmənt/, organize /ˈɔːɡənaɪz/, criteria /kraɪˈtɪəriə/: i = /aɪ/.'),
    ('B', '<b>conclusion</b> /kənˈkluːʒn/ nhấn âm 2. beautiful /ˈbjuːtɪfl/, regular /ˈreɡjələ/, difference /ˈdɪfrəns/ nhấn âm 1.'),
    ('A', '<b>lifestyle</b> /ˈlaɪfstaɪl/ nhấn âm 1. adopt /əˈdɒpt/, event /ɪˈvent/, aware /əˈweə/ nhấn âm 2.'),
    ('D', '<b>interesting</b> /ˈɪntrəstɪŋ/ nhấn âm 1. protection /prəˈtekʃn/, activity /ækˈtɪvəti/, achievement /əˈtʃiːvmənt/ nhấn âm 2.'),
    (['C', 'A'], '<b>issues</b> (vấn đề) ≈ <b>matters</b>. concerns cũng đồng nghĩa nên chấp nhận; views = quan điểm; editions = ấn bản.'),
    ('A', '<b>habits</b> (thói quen) ≈ <b>routines</b>. rules = quy tắc; addictions = chứng nghiện; weakness = điểm yếu.'),
    ('D', '<b>save</b> energy ↔ <b>waste</b> energy (lãng phí). rescue/recover/gather không trái nghĩa.'),
    ('B', '<b>harmful</b> (có hại) ↔ <b>healthy</b> (lành mạnh, có lợi). toxic/hazardous = độc hại; disadvantageous = bất lợi.'),
    ('C', 'Sau mạo từ "a", trước "bag" cần tính từ: <b>reusable</b> (có thể tái sử dụng). usable/useful không hợp nghĩa; reuse là động từ.'),
    ('B', '<b>instead of</b> + V-ing = thay vì (đi xe đạp thay vì lái xe). in spite of = mặc dù; due to/because of = vì.'),
    ('A', '<b>break down</b> into small pieces = phân hủy thành mảnh nhỏ. break up = chia tay/chia nhỏ; turn down/up không hợp.'),
    ('A', 'Appliances should be <b>turned off</b> to save energy (bị động: be + V3).'),
    ('D', 'waste + danh từ: waste <b>electricity</b> (điện). electric/electrical là tính từ; electrically là trạng từ.'),
    ('C', 'make the street dirty and <b>pollute</b> the environment: "make" sau "will" → hai động từ nguyên mẫu song song (will make… and pollute…).'),
    ('B', 'will be + V3 (bị động): Rubbish will be <b>picked up</b>.'),
    ('C', 'be keen on + <b>V-ing</b>: keen on <b>joining</b>.'),
    ('B', 'make a big <b>difference</b> = tạo nên sự khác biệt lớn. improvement/diversity/contrast không đi với make a big.'),
    ('D', 'The <b>emission</b> of greenhouse gases = sự thải khí nhà kính. estimation = ước tính; diffusion = khuếch tán; ejection = phóng ra.'),
    ('C', 'lead <b>to</b> sth = dẫn đến.'),
    ('A', 'be <b>compulsory</b> for sb = bắt buộc ("They are not allowed to be late"). helpful/good/useful không mang nghĩa bắt buộc.'),
    ('D', 'have an impact <b>on</b> sth = tác động đến.'),
    ('C', 'great <b>attending</b> → great <b>attention</b> (thu hút sự chú ý): attract great attention.'),
    ('B', 'Natural resources là chủ ngữ bị động: <b>are protecting</b> → <b>are protected</b> (bị động).'),
    ('C', 'is <b>encouragement</b> → is <b>encouraged</b> (bị động, "most students bring one" là kết quả).'),
    ('B', 'we are <b>making</b> new products from old products = tạo ra sản phẩm mới. doing/using/throwing không hợp.'),
    ('C', 'not throwing away… and <b>instead</b> utilizing them = mà thay vào đó tận dụng chúng. yet/then/but không hợp cấu trúc.'),
    ('D', 'the <b>whole</b> idea: reduce, reuse and recycle = toàn bộ ý tưởng. most/other/number không hợp.'),
    ('A', 'old and waste products <b>that</b> are of no use = đại từ quan hệ chỉ vật (that/which). what/where/who không đúng.'),
    ('D', 'space required to <b>dump</b> these wastes = chôn/đổ chất thải. entomb = chôn cất; burry sai chính tả; hide = giấu.'),
    ('B', 'Bài nói về chiếc máy giặt chạy bằng xe đạp do Alex phát minh → <b>An ingenious invention</b> (một phát minh sáng tạo).'),
    ('A', '<b>ran</b> a business = <b>managed</b> (điều hành, quản lý). moved/allowed/changed không hợp.'),
    ('B', 'Đoạn 1: "he saves on his energy bills" → hoá đơn điện giảm: <b>His electric bills have been decreased</b>.'),
    ('A', '"I keep <b>it</b> in the garden" → it = <b>the cycle washer</b> (máy giặt xe đạp).'),
    ('A', 'Bài nói cỗ máy giúp giặt sạch quần áo, không dùng điện, giúp khoẻ mạnh → "Alex’s machine isn’t very good at washing garments" là <b>không đúng</b>.'),
    ('C', 'Lời mời đi câu lạc bộ → nhận lời: <b>I’d love to.</b> Really?/I love watching it/I will do it không hợp.'),
    ('B', 'Nghe kế hoạch dọn dẹp → phản hồi tích cực: <b>Sounds interesting.</b> It doesn’t matter/It’s a pity/It’s unlucky không hợp.'),
    ('D', '"instead of plastic bags" = "paper bags instead of plastic bags" → <b>She made a decision to reduce plastic waste by using paper bags instead of plastic bags.</b>'),
    ('A', 'Remember to do sth = <b>Don’t forget to do</b> sth. Try doing/Try to do khác nghĩa.'),
    ('C', 'usually cooked (thói quen trong quá khứ) = <b>used to cook</b>. be used to + V-ing = quen với (hiện tại).'),
])
