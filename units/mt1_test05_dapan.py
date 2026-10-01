# -*- coding: utf-8 -*-
"""Đáp án + giải thích – Test 5 – Mid-term 1 (Tiếng Anh 11 Global Success) – nguồn: Đề kiểm tra giữa HK1 Anh 11 (Đề 6).
Quy ước: mcq = chữ cái 'A'-'D' (hoặc list nếu nhiều đáp án đều đúng).
Đáp án lấy từ khoá (tô màu ⟦…⟧) trong phần LỜI GIẢI của Word, đã tự giải độc lập để đối chiếu. Đề không có phần nghe."""

GHI_CHU_RA_SOAT = [
    'g8.32 (Q32): khoá Word = C (searing) nhưng "melting" (tan chảy) gần nghĩa "warming" (B) hơn "searing" (nóng thiêu đốt) -> ANS = [C, B]; đề nghị giáo viên xem lại.',
    'g8.29 (Q29): khoá Word = B; D (implications of climate change...) cũng có thể bàn cãi nhưng giữ khoá Word.',
    'g6.23 (Q23): "impress other people" -> D đúng (khoá Word D); A "impress others people" không đúng vì others không đi trước danh từ.',
    'Sửa nguồn: Q11 D "signicantly" -> "significantly"; Q17: "wich" -> "which", "Last but on least" -> "Last but not least"; "closet" -> "closest" (Q32, 39); Q16 C bỏ dấu chấm thừa ở cuối.',
    'Q10-12 (ảnh UN Volunteers, image1.png) và Q13-15 (thông báo Tết, image2.png) đề gốc để chung đề bài "10 to 15" -> tách 2 nhóm g4 và g4b; image3.png trong Word là bản lặp của image1 nên không dùng.',
    'Đề không ghi thời gian: đặt 45 phút (40 câu).',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


put('g1', [
    ('B', '<b>here</b> /hɪə/ (ere = /ɪə/). beak /biːk/, piece /piːs/, people /ˈpiːpl/ đều có âm /iː/.'),
    ('D', '<b>solidarity</b> /ˌsɒlɪˈdærəti/ (o = /ɒ/). cooperation /kəʊˌɒpəˈreɪʃn/, bowling /ˈbəʊlɪŋ/, aerobics /eəˈrəʊbɪks/ có o = /əʊ/.'),
], 1)
put('g2', [
    ('A', '<b>necessary</b> /ˈnesəsəri/ nhấn âm 1; reliable /rɪˈlaɪəbl/, desirable /dɪˈzaɪərəbl/, advisable /ədˈvaɪzəbl/ nhấn âm 2.'),
    ('C', '<b>appreciative</b> /əˈpriːʃətɪv/ nhấn âm 2; archaeologist /ˌɑːkiˈɒlədʒɪst/, cosmopolitan /ˌkɒzməˈpɒlɪtən/, architectural /ˌɑːkɪˈtektʃərəl/ nhấn âm 3.'),
], 3)
put('g3', [
    ('B', '"Since + mốc quá khứ" -> thì hiện tại hoàn thành: I <b>have offered</b> my time. Tạm dịch: Từ khi học xong lớp 11, tôi đã dành thời gian giúp các em ở trường chuyên biệt.'),
    ('C', 'Lời khuyên để phòng tiểu đường: kids <b>shouldn\'t</b> drink sugary drinks (không nên uống đồ uống có đường). can/may/have to không hợp nghĩa.'),
    ('A', 'Có "than" -> so sánh hơn: good -> <b>better</b> deals (giá tốt hơn). the best dùng cho so sánh nhất; more good/gooder sai.'),
    ('D', '<b>drop in on sb</b> = ghé thăm ai. turn up: xuất hiện; come across: tình cờ gặp; go through: trải qua. Tạm dịch: Tối qua Martin và Louis ghé thăm nên tôi phải rã đông pizza gấp.'),
    ('B', '<b>change one\'s mind</b> = thay đổi ý định. Tạm dịch: Bố mẹ không bao giờ thay đổi ý định về việc đó.'),
], 5)
put('g4', [
    ('B', '"This is <b>an</b> opportunity" - opportunity bắt đầu bằng nguyên âm /ɒ/ nên dùng "an" (cơ hội để tạo tác động tích cực).'),
    ('C', 'Trước danh từ "force" (lực lượng) cần tính từ: a <b>significant</b> force (một lực lượng đáng kể).'),
    ('A', 'Bị động với động từ khuyết thiếu: all of which <b>must be completed</b> before you can apply (tất cả đều phải được hoàn thành trước khi bạn nộp đơn).'),
], 10)
put('g4b', [
    ('D', 'Bị động hiện tại đơn: All students <b>are supposed</b> to be present at 7:30 (tất cả học sinh phải có mặt lúc 7:30).'),
    ('C', 'Each class is to <b>nominate</b> one student (đề cử một học sinh) to take part in the event. appreciate: biết ơn; activate: kích hoạt; communicate: giao tiếp.'),
    ('B', 'Đảo ngữ câu điều kiện loại 2: <b>Were</b> it to rain, the festival would be held... (= If it were to rain). Should dùng cho loại 1, Had cho loại 3.'),
], 13)
put('g5', [
    ('B', 'Thư: c (Dear colleagues, quyết định tái cấu trúc) -> d (As you know, công ty phát triển) -> f (It is therefore obvious... cần thay đổi) -> b (chưa hoàn tất chi tiết nhưng không sa thải) -> e (In fact, cơ hội mới) -> a (In light of this restructuring, sẽ liên hệ từng người) -> g (Yours sincerely). Đáp án <b>c - d - f - b - e - a - g</b>.'),
    ('A', 'Đoạn văn: d (câu chủ đề) -> a (Firstly) -> c (Besides) -> f (They may learn... giải thích kỹ năng ở c) -> b (Last but not least) -> e (To sum up). Đáp án <b>d-a-c-f-b-e</b>.'),
], 16)
put('g6', [
    ('C', 'Liệt kê các lời phàn nàn: "...; and <b>that they do not have a sense of humor</b>" - that là liên từ lặp lại sau "complained". do they not (đảo ngữ) / which / that it không đúng.'),
    ('D', 'Cần tính từ sở hữu của "parents/they" -> underestimate <b>their adolescents</b> (đánh giá thấp con cái tuổi vị thành niên của họ).'),
    ('A', 'Quên cảm giác của chính mình <b>when they were younger</b> (khi còn trẻ hơn) - mốc quá khứ, phù hợp với "felt".'),
    ('B', 'find sth + adj/V-ing: find their haircuts <b>irritating</b> (thấy kiểu tóc của họ gây khó chịu). Sau "haircuts" cần tính từ V-ing chỉ tính chất.'),
    ('C', '<b>intention of + V-ing</b>: the intention of taking charge of your life (ý định tự làm chủ cuộc sống).'),
    ('D', 'Sau chỗ trống là "people": You can also impress <b>other</b> people (tính từ "other" + danh từ số nhiều). "others" là đại từ nên không đứng trước "people".'),
], 18)
put('g7', [
    ('C', '<b>still</b> worthwhile = vẫn còn đáng giá. Tạm dịch: Với bao lựa chọn giải trí hiện nay, đọc sách có còn đáng giá không?'),
    ('A', '<b>Some</b> argue that... (Một số người cho rằng). Much/Little đi với danh từ không đếm được; Few cần "A few/Few people".'),
    ('B', 'so + adj + <b>that</b> + mệnh đề: so engrossing that you can\'t put it down (hấp dẫn đến mức không thể đặt xuống).'),
    ('D', '<b>genres</b> = thể loại (tiểu thuyết trinh thám, tự truyện, sách thông tin). actions: hành động; techniques: kỹ thuật; troubles: rắc rối.'),
    ('D', '<b>manage to do sth</b> = xoay xở / làm được việc gì: I can manage to live without television with relative ease.'),
], 24)
put('g8', [
    ('B', 'Bài nói công viên quốc gia giúp theo dõi biến đổi khí hậu, đồng thời kết bằng mục tiêu bảo vệ công viên -> tiêu đề <b>The importance of national parks is more than for scenery</b> (vai trò của công viên quốc gia vượt ngoài cảnh quan). D cũng có thể bàn cãi nhưng giữ khoá của đề.'),
    ('D', 'Đoạn 1 nhắc: wilderness (A), thu thập dữ liệu khi đi bộ (B), giám sát bằng drone (C). Không có thông tin về <b>rừng biến thành khu dân cư</b> (D) -> NOT.'),
    ('D', '"moving some animals and plants by hand if it turns out <b>they</b> can\'t live in the park\'s changing environments" - they chỉ <b>species</b> (các loài động, thực vật).'),
    (['C', 'B'], '<b>melting</b> (tan chảy). Khoá Word chọn C (searing - nóng thiêu đốt, gần "nóng chảy"), nhưng B (warming - nóng lên) sát nghĩa ngữ cảnh hơn; chấp nhận cả C và B. cooling: làm lạnh (ngược nghĩa); making: không liên quan.'),
    ('C', '"Climate change is killing trees... twice as many trees" -> <b>It increases death rates of trees through disturbances</b> (hạn hán, cháy rừng, bọ vỏ cây).'),
], 29)
put('g9', [
    ('C', 'Cả bài bàn về tác động của đô thị hoá lên sức khoẻ (ô nhiễm không khí, ăn uống) -> <b>Urbanization - How people\'s health is impacted?</b>. B (pros and cons) sai vì bài chỉ nói tác hại.'),
    ('B', '"The predicted negative impacts of urbanization on physical health... China is dealing with <b>these issues</b>" -> chỉ <b>negative physical health effects</b>.'),
    ('C', 'Đoạn 3 nêu: chất thải nhà máy, nhà máy lọc dầu, hoá chất, phương tiện giao thông. <b>Sewage</b> (nước thải) không được nhắc -> EXCEPT.'),
    ('C', '<b>diminished</b> (suy giảm) >< <b>increased</b> (tăng lên).'),
    ('D', 'Đoạn cuối: đồ ăn tiện lợi "has a lot of sugar and sodium, probably not very good quality" -> bệnh vì <b>chất lượng thấp, nhiều natri và đường</b>.'),
    ('A', 'Trong ngữ cảnh "any dangerous <b>material</b> that floats around in the air", material ~ <b>matter</b> (vật chất). litter: rác; depress: làm buồn; station: trạm.'),
    ('B', 'Câu 2 đoạn 2: tác động tiêu cực "more pronounced in emerging nations compared to modern nations" -> suy ra <b>people in developed countries suffer less harmful health effects than those in developing nations</b>.'),
], 34)
