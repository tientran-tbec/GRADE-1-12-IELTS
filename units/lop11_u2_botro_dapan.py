# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Unit 2 (Tiếng Anh 11 Global Success) – Bộ BÀI TẬP BỔ TRỢ.
Quy ước:
  mcq  : chữ cái 'A'-'D'            tf : 'T' / 'F'
  fill : danh sách đáp án chấp nhận (1 ô)  hoặc {'blanks': [[...],[...]]} (nhiều ô)
  open : không chấm điểm, EXPLANATIONS chứa đáp án mẫu
Đáp án được SOẠN LẠI ĐỘC LẬP rồi đối chiếu với khoá trong file Word gốc; chỗ lệch/mơ hồ được ghi trong BAO_CAO_RA_SOAT.md."""

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


def put_open(prefix, rows):
    for i, e in enumerate(rows, 1):
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ======================= PHONETIC – Exercise 2 (phát âm) =======================
put('ph2', [
    ('B', '<b>wear</b> /weə/. clear /klɪə/, nuclear /ˈnjuːkliə/, experience /ɪkˈspɪəriəns/ đều chứa âm /ɪə/.'),
    ('A', '<b>engineer</b> /ˌendʒɪˈnɪə/ (ee = /ɪə/). screen /skriːn/, three /θriː/, teenager /ˈtiːneɪdʒə/ (ee = /iː/).'),
    ('D', '<b>argument</b> /ˈɑːɡjumənt/ (g = /ɡ/). generation /ˌdʒenəˈreɪʃn/, gender /ˈdʒendə/, digital /ˈdɪdʒɪtl/ (g = /dʒ/).'),
    ('B', '<b>generation</b> /ˌdʒenəˈreɪʃn/ (g = /dʒ/). gap /ɡæp/, grandparent /ˈɡrænpeərənt/, great /ɡreɪt/ (g = /ɡ/).'),
    ('A', '<b>behavior</b> /bɪˈheɪvjə/ (a = /eɪ/). application /ˌæplɪˈkeɪʃn/, value /ˈvæljuː/, gap /ɡæp/ (a = /æ/).'),
    ('C', '<b>force</b> /fɔːs/ (o = /ɔː/). hold /həʊld/, follow /ˈfɒləʊ/, notice /ˈnəʊtɪs/ có âm /əʊ/ ở chữ o được gạch chân.'),
    ('C', '<b>confidence</b> /ˈkɒnfɪdəns/ (o = /ɒ/). control /kənˈtrəʊl/, economic /ˌiːkəˈnɒmɪk/, condition /kənˈdɪʃn/ (o = /ə/).'),
    ('D', '<b>argue</b> /ˈɑːɡjuː/ (ar = /ɑː/). extend /ɪkˈstend/, breadwinner /ˈbredwɪnə/, express /ɪkˈspres/ (e/ea = /e/).'),
    ('C', '<b>footstep</b> /ˈfʊtstep/ (oo = /ʊ/). food /fuːd/, roof /ruːf/, fool /fuːl/ (oo = /uː/).'),
    ('D', '<b>gender</b> /ˈdʒendə/ (e = /e/). believe /bɪˈliːv/, extend /ɪkˈstend/, respect /rɪˈspekt/ (e = /ɪ/).'),
])

# ======================= PHONETIC – Exercise 3 (trọng âm) =======================
put('ph3', [
    ('D', '<b>understand</b> /ˌʌndəˈstænd/ nhấn âm 3 (từ ghép nhận trọng âm ở âm cuối). critical /ˈkrɪtɪkl/, cultural /ˈkʌltʃərəl/, influence /ˈɪnfluəns/ nhấn âm 1.'),
    ('C', '<b>millennial</b> /mɪˈleniəl/ nhấn âm 2 (trước -ial). education /ˌedʒuˈkeɪʃn/, individual /ˌɪndɪˈvɪdʒuəl/, generation /ˌdʒenəˈreɪʃn/ nhấn âm 3.'),
    ('D', '<b>create</b> /kriˈeɪt/ nhấn âm 2. notice /ˈnəʊtɪs/, platform /ˈplætfɔːm/, label /ˈleɪbl/ nhấn âm 1.'),
    ('B', '<b>permission</b> /pəˈmɪʃn/ nhấn âm 2 (đuôi -ion → nhấn âm liền trước). difference /ˈdɪfrəns/, argument /ˈɑːɡjumənt/, cultural /ˈkʌltʃərəl/ nhấn âm 1.'),
    ('C', '<b>experience</b> /ɪkˈspɪəriəns/ nhấn âm 2. economic /ˌiːkəˈnɒmɪk/, generation /ˌdʒenəˈreɪʃn/, electronic /ɪˌlekˈtrɒnɪk/ nhấn âm 3.'),
    ('D', '<b>curious</b> /ˈkjʊəriəs/ nhấn âm 1. refer /rɪˈfɜː/, prepare /prɪˈpeə/, achieve /əˈtʃiːv/ nhấn âm 2.'),
    ('D', '<b>accept</b> /əkˈsept/ nhấn âm 2 (động từ). value /ˈvæljuː/, teamwork /ˈtiːmwɜːk/, welcome /ˈwelkəm/ nhấn âm 1.'),
    ('D', '<b>musician</b> /mjuˈzɪʃn/ nhấn âm 2 (đuôi -ian). difference /ˈdɪfrəns/, grandparent /ˈɡrænpeərənt/, character /ˈkærəktə/ nhấn âm 1.'),
    ('D', '<b>influence</b> /ˈɪnfluəns/ nhấn âm 1. expression /ɪkˈspreʃn/, important /ɪmˈpɔːtnt/, tradition /trəˈdɪʃn/ nhấn âm 2.'),
    ('C', '<b>respect</b> /rɪˈspekt/ nhấn âm 2. eyesight /ˈaɪsaɪt/, worry /ˈwʌri/, limit /ˈlɪmɪt/ nhấn âm 1.'),
])

# ======================= VOCAB & GRAMMAR =======================
put('vg1', [
    (['historical'], 'of <b>historical</b> importance = có tầm quan trọng về mặt lịch sử (tính từ đứng trước danh từ importance).'),
    (['lifestyle'], 'the simple <b>lifestyle</b> of the islanders = lối sống giản dị của người dân đảo.'),
    (['influence'], 'Sau trợ động từ <i>Do</i> + chủ ngữ cần động từ nguyên thể → <b>influence</b> children\'s behaviour = ảnh hưởng đến hành vi của trẻ.'),
    (['view'], 'My mum\'s <b>view</b> of the situation = quan điểm của mẹ tôi về tình huống.'),
    (['characteristics'], 'several + danh từ số nhiều → <b>characteristics</b> (đặc điểm) khiến anh ta khác các thành viên còn lại.'),
    (['choice'], 'a free <b>choice</b> of what to study = quyền tự do lựa chọn ngành học.'),
    (['culture'], 'In our <b>culture</b> it is rude to … = trong nền văn hoá của chúng tôi, hỏi lương là bất lịch sự.'),
    (['social'], 'develop <b>social</b> skills = phát triển kĩ năng xã hội.'),
    (['traditional'], 'return to <b>traditional</b> values = quay về các giá trị truyền thống.'),
    (['suit'], 'vary the style to <b>suit</b> the circumstances = thay đổi văn phong cho phù hợp hoàn cảnh (suit + O).'),
])

put('vg2', [
    ('D', 'Các ví dụ (không làm tổn thương người khác, xin phép khi mượn đồ) là hành vi <b>respectful</b> (biết tôn trọng).'),
    ('C', 'As children get older and more <b>mature</b> (trưởng thành) → luật lệ cũng phát triển theo.'),
    ('A', 'the <b>burden</b> is lighter = gánh nặng nhẹ hơn khi việc nhà được chia sẻ.'),
    ('B', 'appeared on the <b>scene</b> = xuất hiện trên (sân khấu) đời sống/âm nhạc; cụm "on the scene".'),
    ('C', 'avoid family <b>conflict</b> = tránh xung đột trong gia đình. (argument/debate không dùng tự nhiên ở dạng số ít không mạo từ; "qua…" là phương án bị cắt trong đề, chữa thành <i>quarrel</i>.)'),
    ('A', 'as <b>common</b> in American homes as televisions = phổ biến như tivi. (popular dùng với người/vật được yêu thích, không hợp).'),
    ('B', 'the widening <b>gap</b> between the rich and the poor = khoảng cách giàu nghèo ngày càng rộng.'),
    ('D', 'accept each other\'s <b>cultural</b> differences = chấp nhận khác biệt văn hoá.'),
    ('A', 'we were all <b>prepared</b> for the storm = đã chuẩn bị sẵn sàng cho cơn bão (prepared for).'),
    ('C', 'improve your <b>social</b> life = cải thiện đời sống xã hội.'),
    ('D', '<b>historical</b> figures = nhân vật lịch sử (Alexander Đại đế).'),
    ('A', '<b>curious</b> glances = những cái liếc nhìn tò mò.'),
    ('C', 'develop <b>critical</b> thinking = phát triển tư duy phản biện (không chấp nhận ý kiến mà không đặt câu hỏi).'),
    ('C', 'They are <b>trying out</b> a new sound system = đang thử nghiệm hệ thống âm thanh mới (thì hiện tại tiếp diễn: are + V-ing).'),
    ('A', 'Several factors are likely to <b>influence</b> this decision = ảnh hưởng đến quyết định.'),
    ('D', 'have an influence <b>on</b> sb/sth = có ảnh hưởng lên.'),
    ('C', 'have respect <b>for</b> sb/sth = tôn trọng.'),
    ('B', 'attitude <b>towards</b> sb/sth = thái độ đối với (cũng dùng "attitude to").'),
    ('D', 'be different <b>from</b> = khác với.'),
    ('A', 'adapt <b>to</b> sth = thích nghi với.'),
    ('B', 'follow <b>in</b> sb\'s footsteps = nối nghiệp, theo bước chân ai.'),
    ('D', 'Cheat in the exams is against the rules → cấm: <b>mustn\'t</b>.'),
    ('C', 'Không có lớp học Chủ nhật → không cần đi: <b>don\'t have to</b>.'),
    ('D', 'Thi đóng sách (closed-book) → cấm dùng tài liệu: <b>mustn\'t</b>.'),
    ('C', 'Dự án tự chọn (optional) → không bắt buộc: <b>don\'t have to</b>.'),
    ('B', 'Quy định của trường (a rule) → bắt buộc từ bên ngoài: <b>have to</b>. (must cũng gần nghĩa nhưng đáp án chuẩn là have to vì nhấn mạnh luật/quy định.)'),
    ('C', 'Hành động đã xảy ra trong quá khứ (yesterday) → <b>had to</b> (quá khứ của have to).'),
    ('A', 'Bí mật → cấm tiết lộ: <b>mustn\'t</b> tell anyone. (Lưu ý: "had better not tell" cũng đúng ngữ pháp nhưng sai đáp án đề vì thiếu sắc thái cấm tuyệt đối.)'),
    ('B', 'Trẻ chơi/bơi ở hồ bơi bắt buộc có cha mẹ đi cùng → <b>must</b> (an toàn). (have to cũng chấp nhận được; đề chọn must.)'),
    ('C', 'Sky train là lựa chọn khôn ngoan → không nên đi ô tô: <b>shouldn\'t</b> go by car.'),
    ('A', 'Hoàn thành bài tập trước khi ngủ: nghĩa vụ → <b>must</b> (đáp án theo đề gốc; have to/should/ought to cũng có thể dùng được tuỳ ngữ cảnh – câu này mơ hồ, xem BAO_CAO_RA_SOAT).'),
    ('B', 'Biển cảnh báo cấm giẫm lên cỏ: <b>mustn\'t</b>.'),
    ('C', 'Cho vay tiền nhưng "next week phải trả": nghĩa vụ → <b>must</b> pay it back. (mustn\'t sai nghĩa.)'),
    ('B', 'Mẹ đã cho mèo ăn rồi → không cần nữa: <b>doesn\'t have to</b>.'),
    ('A', 'Khán giả phải xuất trình vé: <b>have to</b>. (must cũng đúng nghĩa; đề chọn have to.)'),
    ('C', 'Trẻ không nên chơi game quá nhiều: <b>shouldn\'t</b>. ("ought to not" sai cấu trúc, đúng là "ought not to".)'),
    ('D', 'Trẻ dưới 6 tuổi được miễn phí → bạn không cần trả: <b>don\'t have to</b>.'),
    ('A', 'Trông kiệt sức → lời khuyên: <b>should</b> take a rest. (ought thiếu "to"; has better sai.)'),
    ('D', 'Bất kì ai (Anyone – ngôi 3 số ít) <b>has to</b> có hộ chiếu. (must cũng được nhưng đề chọn has to.)'),
    ('C', 'Mùa cao điểm → lời khuyên nên đặt chỗ sớm: <b>should</b>. (ought thiếu "to".)'),
])

put('vg3', [
    (['should'], 'Giáo viên bực → Quân <b>should</b> cư xử tốt hơn (lời khuyên).'),
    (['shouldn\'t', 'shouldn’t', 'should not'], 'Chơi game là lãng phí thời gian → <b>shouldn\'t</b> chơi.'),
    (['should'], 'Nên đặt bàn cho tiệc sinh nhật → <b>should</b>.'),
    (['should'], 'Hôm sau đi học → <b>should</b> đi ngủ sớm.'),
    (['shouldn\'t', 'shouldn’t', 'should not'], 'Đồ ăn nhanh có hại → <b>shouldn\'t</b> ăn nhiều.'),
    (['should'], 'Nên tìm người hỏi bài tập → <b>should</b>.'),
])

put('vg4', [
    ('A', 'Thư viện cho phép (không bắt buộc) mượn tối đa 6 cuốn → <b>may</b> (được phép).'),
    ('A', 'Trong kì thi, học sinh bắt buộc trả lời mọi câu hỏi → <b>must</b>. (mustn\'t sai nghĩa.)'),
    ('B', 'Quy định pháp luật về tuổi lái xe → <b>have to</b> (bắt buộc theo luật).'),
    ('B', 'Quy định của khách sạn → <b>have to</b> (nghĩa vụ đặt ra từ bên ngoài). Chú ý: đề gốc cho "have to".'),
    ('B', 'Biển báo cấm đi trên cỏ → <b>mustn\'t</b>.'),
    ('B', 'Trên xe buýt cấm nói chuyện với tài xế → <b>mustn\'t</b>.'),
])

put('vg5', [
    ('C', '<b>norm</b> (chuẩn mực) ≈ <b>rule</b> (quy tắc). routine = thói quen; barrier = rào cản; conflict = xung đột.'),
    ('B', '<b>conflicts</b> (xung đột) ≈ <b>disagreements</b> (bất đồng). agreements/similarities là nghĩa trái.'),
    ('C', '<b>Domestic</b> problems = vấn đề <b>trong gia đình</b> (within the family) — ví dụ tranh cãi với bố mẹ.'),
    ('B', '<b>typical</b> (điển hình) ≈ <b>characteristic</b> (đặc trưng). rare/surprising khác nghĩa.'),
    ('D', '<b>impose</b> (áp đặt) ≈ <b>force</b> (ép buộc).'),
    ('C', '<b>frustrating</b> (gây bực bội) ≈ <b>annoying</b> (khó chịu).'),
    ('B', '<b>problems</b> ≈ <b>issues</b> (vấn đề).'),
    ('C', '<b>the chores</b> (việc nhà) ≈ <b>housework</b>.'),
    ('A', '<b>table manners</b> (phép tắc ăn uống) ≈ <b>etiquette</b> (nghi thức, phép xã giao).'),
    ('D', '<b>increases</b> (động từ có tân ngữ: increases the risk) ≈ <b>raise</b> (làm tăng). "rise" là nội động từ nên không đi với tân ngữ.'),
])

put('vg6', [
    ('C', '<b>state-owned</b> (nhà nước) trái nghĩa <b>privately-owned</b> (tư nhân). (private-owned không đúng dạng chuẩn.)'),
    ('B', '<b>takes care of</b> (chăm sóc) trái nghĩa <b>abandons</b> (bỏ rơi).'),
    ('D', '<b>respect</b> = look up to; trái nghĩa <b>look down on</b> (coi thường).'),
    ('A', '<b>forbidden</b> (bị cấm) trái nghĩa <b>permitted</b> (được phép).'),
    ('B', '<b>conflict</b> (xung đột) trái nghĩa <b>harmony</b> (hoà thuận).'),
    ('C', '<b>concentrate</b> (tập trung) trái nghĩa <b>neglect</b> (lơ là, bỏ bê). focus là đồng nghĩa.'),
    ('A', '<b>conservative</b> (bảo thủ) trái nghĩa <b>progressive</b> (tiến bộ). traditional/conventional là đồng nghĩa.'),
    ('B', '<b>lack</b> (sự thiếu) trái nghĩa <b>abundance</b> (sự dồi dào). shortage/scarcity/deficiency đều là đồng nghĩa.'),
    ('C', '<b>extended family</b> (gia đình nhiều thế hệ) trái nghĩa <b>nuclear family</b> (gia đình hạt nhân).'),
    ('D', '<b>open-minded</b> (cởi mở) trái nghĩa <b>narrow-minded</b> (hẹp hòi).'),
])

put('vg7', [
    ('B', 'Sau <i>ought to</i> dùng động từ nguyên thể: ought <b>to take</b> (không phải to taking).'),
    ('A', 'Câu hỏi với <i>have to</i> ở hiện tại: <b>Do</b> you have to…? (does sai vì chủ ngữ là you).'),
    ('A', 'Ở thư viện/lớp học bị cấm ăn uống → <b>mustn\'t</b> consume (don\'t have to nghĩa là "không cần", sai nghĩa).'),
    ('C', 'Em bé đang ngủ → cấm la hét: <b>mustn\'t</b> shout (don\'t have to shout nghĩa là "không cần phải la" – sai ngữ cảnh).'),
    ('B', 'Sau must dùng động từ nguyên thể: we must <b>be</b> quicker (không phải are).'),
    ('A', 'Mình đã cho chó ăn rồi → bạn <b>không cần</b> cho ăn: <b>don\'t have to</b> feed the dog.'),
    ('B', 'Get out of the grass! → cấm giẫm lên cỏ: you <b>mustn\'t</b> walk on the grass.'),
    ('B', 'have to + V nguyên thể: have to <b>make</b> sure (không phải made).'),
    ('B', 'mustn\'t + V nguyên thể: mustn\'t <b>use</b> (không phải uses).'),
    ('A', 'Dạng phủ định của have to là <b>don\'t have to</b> (haven\'t to sai). Tài xế không cần dừng ở đèn vàng.'),
])

put('vg8', [
    ('A', 'Món mình không thích → <b>không cần</b> ăn: don\'t have to. (must eat nghĩa là bắt buộc ăn – vô lý.)'),
    ('B', 'Không muốn đau họng → <b>oughtn\'t</b> (không nên) uống nhiều nước đá. (don\'t have to nghĩa là không cần – không hợp lí do.)'),
    ('A', 'Tiếp viên hàng không <b>phải</b> (have to) chăm sóc hành khách. mustn\'t sai nghĩa.'),
    ('B', 'Học sinh <b>không được</b> rời lớp khi chưa được phép → mustn\'t.'),
    ('A', 'Mẹ nấu ăn cho cô ấy → cô ấy <b>không cần</b> nấu: doesn\'t have to.'),
    ('B', 'Luật mới quy định → hút thuốc nơi công cộng là <b>bị cấm</b>: mustn\'t.'),
    ('A', 'Đồ uống miễn phí → bạn <b>không cần</b> trả tiền: don\'t have to.'),
    ('A', 'Kelvin trúng số → anh ấy <b>không cần</b> đi làm: doesn\'t have to.'),
    ('A', 'Theo quy định công ty (nghĩa vụ từ bên ngoài) → staff <b>have to</b> finish… (must cũng chấp nhận được trong ngữ cảnh này; đáp án đề chọn have to.)'),
    ('B', 'Để khỏe mạnh, chúng ta <b>nên</b> (ought to) ăn đồ lành mạnh và tập thể dục. mustn\'t sai nghĩa.'),
])

put('vg9', [
    (['should spend more time talking with your children', 'should spend more time talking to your children'], 'If I were you, I would… = lời khuyên → <b>You should spend more time talking with your children</b>.'),
    (["mustn't use that computer", 'must not use that computer'], 'doesn\'t get permission = không được phép → <b>John mustn\'t use that computer</b>.'),
    (['must leave by 6 pm', 'must leave by 6 p.m', 'must leave by 6 p.m.'], 'It is necessary that… = bắt buộc → <b>People who work here must leave by 6 p.m.</b>'),
    (["mustn't smoke or eat in the office", 'must not smoke or eat in the office'], 'isn\'t allowed to = bị cấm → <b>Every staff mustn\'t smoke or eat in the office</b>.'),
    (["mustn't cheat in the exam", 'must not cheat in the exam', "mustn't cheat in exams", "mustn't cheat in the exams"], 'It is forbidden for sb to do sth → <b>Students mustn\'t cheat in the exam</b>.'),
    (['has to clean the floor every day', 'has to clear the floor every day'], 'be in charge of cleaning = có trách nhiệm dọn → <b>Ms. Ly has to clean the floor every day</b> (chủ ngữ số ít → has to).'),
    (["mustn't take photographs in the museum", 'must not take photographs in the museum', "mustn't take photos in the museum", "mustn't take pictures in the museum"], 'are not allowed to = bị cấm → <b>You mustn\'t take photographs in the museum</b>.'),
    (["doesn't have to call ben today", 'does not have to call ben today'], 'It is not necessary for sb to do sth → <b>Jack doesn\'t have to call Ben today</b> (chủ ngữ số ít → doesn\'t have to).'),
])

put('vg10', [
    (["my secret, but you mustn't tell anyone", 'my secret, but you must not tell anyone'], 'Đặt <b>mustn\'t</b> trước động từ tell: I will tell you my secret, but you <b>mustn\'t</b> tell anyone.'),
    (['too much time playing computer games. you must stop that', 'too much time playing computer games you must stop that'], 'Đặt <b>must</b> trước stop (bắt buộc): …You <b>must</b> stop that.'),
    (['have to wear helmets when we ride a motorbike'], 'Đặt <b>have to</b> trước wear: We <b>have to</b> wear helmets when we ride a motorbike.'),
    (["don't have to book the tickets in advance", 'do not have to book the tickets in advance'], 'Đặt <b>don\'t have to</b> trước book: I <b>don\'t have to</b> book the tickets in advance (không cần đặt trước).'),
    (["mustn't say rude words like that", 'must not say rude words like that'], 'Đặt <b>mustn\'t</b> trước say: Alia, you <b>mustn\'t</b> say rude words like that.'),
    (["don't have to play table tennis. we can play chess instead", "don't have to play table tennis we can play chess instead"], 'Không cần chơi bóng bàn vì còn có thể chơi cờ: We <b>don\'t have to</b> play table tennis.'),
    (["mustn't put their hands into sockets. that is very dangerous", "mustn't put their hands into sockets that is very dangerous"], 'Nguy hiểm → cấm: Children <b>mustn\'t</b> put their hands into sockets.'),
    (['have to work at the weekends and on national holidays'], 'Bác sĩ đôi khi <b>phải</b> làm việc: Doctors sometimes <b>have to</b> work…'),
])

put('vg11', [
    (['must finish your homework before going to bed'], 'It\'s necessary for you to… = bắt buộc → <b>You must finish your homework before going to bed</b>.'),
    (["don't have to bring food and drink for lunch", 'do not have to bring food and drink for lunch'], 'It isn\'t necessary = không cần → <b>You don\'t have to bring food and drink for lunch</b>.'),
    (["mustn't fish in this park", 'must not fish in this park'], 'Fishing is not allowed = cấm → <b>You mustn\'t fish in this park</b>.'),
    (['in our hotel has to wear a uniform', 'has to wear a uniform in our hotel'], 'is obliged to = bắt buộc; chủ ngữ số ít → <b>Every receptionist in our hotel has to wear a uniform</b>.'),
    (['must not sell cigarettes to children', "mustn't sell cigarettes to children"], 'It\'s forbidden to sell… → <b>Shops must not sell cigarettes to children</b>.'),
    (["has to keep the company's information secret", "has to keep the company's information secret"], 'It\'s obligatory for every employee to… → <b>Every employee has to keep the company\'s information secret</b>.'),
])

# ======================= LISTENING =======================
put('li1', [
    ('F', 'Linda: "Just my parents keep complaining about my clothes … They think my trousers are too skinny and my tops are too tight." → bố mẹ <b>không hài lòng</b>.'),
    ('F', 'Tom: "I don\'t think you should wear flashy clothes every day … have you thought about the cost?" → Tom <b>không</b> cùng quan điểm với Linda.'),
    ('T', 'Linda: "But I really want to look <b>more elegant and fashionable</b>."'),
    ('T', 'Tom: "But they <b>forbid me to play computer games</b>."'),
    ('T', 'Tom: "Playing computer games after school also helps me <b>to relax</b> after a hard day."'),
])
put('li2', [
    ('T', '"During the teenage years, it is at times <b>difficult for parents to talk to their children</b>."'),
    ('F', '"Teenagers often seem to hate being questioned. They seem <b>unwilling to talk about their work at school</b>." → không phải lúc nào cũng thích nói.'),
    ('T', '"Young people often dislike talking if they realise that parents are <b>trying to check up on them</b>."'),
    ('F', '"Parents should find ways to talk … about school, work and future plans, but <b>should not push them</b> to talk if they don\'t want to."'),
    ('T', '"Parents should also <b>watch for danger signs</b> … may experiment with alcohol, drugs or smoking."'),
])

# ======================= SPEAKING =======================
put('sp1', [
    ('B', 'Bạn than bố mẹ không cho làm điều mình muốn → đáp lại bằng lời khuyên: <b>they should respect your privacy</b>. (a "bạn có bố mẹ biết ủng hộ" mâu thuẫn với lời than.)'),
    ('B', 'Bố mẹ muốn nối nghiệp → <b>you have your own dreams of job</b> (bạn có ước mơ nghề nghiệp riêng). Phương án a chơi chữ "walk" không hợp ngữ cảnh.'),
    ('A', 'Hỏi "Do you help with housework?" → <b>Certainly. All of us share the chores</b>.'),
    ('B', 'Hỏi có khoảng cách thế hệ không → <b>No. My parents are very understanding</b> (bố mẹ rất thấu hiểu). (Phương án a nói về gia đình hạt nhân – không liên quan trực tiếp.)'),
    ('A', 'Hỏi làm sao tự quyết định → khuyên <b>explain them to your parents</b> (giải thích với bố mẹ).'),
    ('A', 'Hỏi cách tránh xung đột → <b>You should set the family rules</b> (đặt ra quy tắc gia đình).'),
    ('A', 'Bố mẹ không cho chơi game → <b>You can do it when you finish homework</b> (gợi ý thoả hiệp).'),
    ('B', 'Con nói mẹ ăn mặc, làm tóc xấu → đáp phủ định <b>No. They were popular 20 years ago</b> (kiểu đó từng thịnh hành). Phương án a ("looked younger and nicer, didn\'t she?") mâu thuẫn với "badly, ugly".'),
    ('B', 'Hỏi "Who do you talk with…?" (ai) → trả lời bằng người: <b>My mum, of course</b>.'),
    ('A', 'Hỏi có nên nói với bố mẹ trước khi quyết định lớn → <b>Of course. It\'s a must</b> (đương nhiên, bắt buộc).'),
])

put('sp2', [
    ('G', 'Sam hỏi "what fights…?" → Nick trả lời liệt kê: <b>Oh, a lot. The clothes you wear, the food you eat…</b> (G).'),
    ('B', 'Sau câu "small kids need protection" → <b>But when kids grow up and become teens, they develop their own identity…</b> (B) – chuyển ý bằng "But".'),
    ('D', 'Trước câu "We want to cover our walls with new posters…" (ví dụ) → <b>In most families, the fact that kids make their own decisions can cause a lot of fighting</b> (D).'),
    ('A', 'Sam: "Clashes like these small things are very common…" → Nick: <b>But these small things can make teens angry…</b> (A).'),
    ('F', 'Sam: "parents also get angry because they disagree with the teen decisions." → <b>The good news about fighting with parents is that they get more comfortable…</b> (F). C và E là hai câu thừa.'),
])

put('sp3', [
    ('C', '"Can I try your new camera?" – cho mượn có điều kiện: <b>Sure. But please be careful with it.</b>'),
    ('C', '"May I speak to the manager?" – <b>I\'m afraid he\'s not in. Can I take a message?</b> (cách đáp lịch sự khi gọi điện.)'),
    ('B', 'Đáp "Yes, it\'s OK. But could you clean your room first?" → câu xin phép phía trước: <b>Can I go to Helen\'s party this weekend?</b>'),
    ('D', '"Could I speak to Ann?" – <b>I\'m sorry. Ann\'s not in.</b> (A "This is Daisy speaking" giới thiệu người khác; B sẽ hợp lí hơn sau khi báo Ann vắng.)'),
    ('A', '"Do you mind if I use your phone?" – đồng ý: <b>Not at all. Help yourself.</b>'),
    ('C', '"Would you mind if I shut the window?" – đồng ý dùng "No" (không phiền): <b>No, please do.</b>'),
    ('B', '"Do you mind my taking this seat?" – <b>No, of course not</b> (không phiền, mời ngồi).'),
    ('A', '"Would you mind if I used your computer?" – <b>Not at all. I\'ve finished my job.</b>'),
    ('C', 'Bệnh nhân xin đặt lịch → lễ tân: <b>OK, let me check the diary.</b>'),
    ('B', '"Would you bother if I had a look at your paper?" – từ chối lịch sự: <b>Well, actually I\'d rather you didn\'t.</b>'),
])

# ======================= READING =======================
put('re1a', [
    ('B', 'a popular <b>term</b> used to describe… = một thuật ngữ phổ biến dùng để mô tả (name/description không đi với "used to describe" tự nhiên bằng term).'),
    ('C', '<b>because of</b> + danh từ (their experiences, opinions…) = vì, do. owing cần "to"; in spite of/with sai nghĩa.'),
    ('D', 'think they should <b>arrange</b> everything for their children = sắp xếp mọi việc cho con (từ chọn trường tiểu học đến công việc…).'),
    ('C', 'many things children want but their parents think <b>those</b> are unnecessary → "those" thay cho "những thứ đó" (things).'),
    ('A', 'That causes misunderstanding and <b>makes</b> gaps → động từ chia ngôi 3 số ít (That = chủ ngữ), song song với "causes".'),
])
put('re1b', [
    ('C', 'When a person <b>feels</b> influenced by… = cảm thấy bị ảnh hưởng (chủ ngữ a person số ít, động từ cảm giác). are sai chia; remains/smells sai nghĩa.'),
    ('B', 'deal <b>with</b> sth = đối phó với, giải quyết.'),
    ('D', '<b>many</b> + danh từ đếm được số nhiều (people). much không đi với people; a little/another sai.'),
    ('D', 'boosts a person\'s feelings of wellness and <b>happiness</b> – ngược với unhappy, unwell ở vế trước; arguments/conflicts/anger mang nghĩa tiêu cực.'),
    ('A', 'Vế sau là ví dụ cụ thể (join a club, work hard…) → <b>For example</b>.'),
])
put('re2a', [
    ('C', 'Cả bài nói về cấu trúc các gia đình Mĩ hiện nay (đa dạng, ít gia đình truyền thống) → <b>The current American family</b>.'),
    ('A', '"the so-called traditional American family was always <b>more varied</b> than we had been led to believe" → luôn đa dạng hơn ta nghĩ.'),
    ('B', '<b>current</b> (hiện tại) ≈ <b>present</b>.'),
    ('A', '"another third consists of married couples who either have no children or have none still living at home" → khoảng <b>một phần ba (33%)</b>.'),
    ('C', '"20 percent … are single people, usually <b>women over sixty-five</b> years old" → phụ nữ độc thân ngoài 65 tuổi.'),
])
put('re2b', [
    ('B', 'Ba nguyên nhân: khác nhau về thái độ sống, quan điểm về vấn đề, và thiếu giao tiếp ("different attitudes… different views… a lack of communication") → <b>3</b>.'),
    ('A', '"they prefer to be free to <b>make their own decisions</b> on their future career".'),
    ('C', '"it is considered to be an act of rebellion <b>against social norms</b>".'),
    ('B', '"When facing problems, young people prefer to <b>seek help from their classmates or friends</b>."'),
    ('A', '"mutual understanding is the vital key … treat each other <b>as friends</b>".'),
])
put('re2c', [
    ('D', 'Afghanistan: "Dating is <b>rare</b>"; Iran: "It is <b>against the law</b> to date" → rare or prohibited.'),
    ('B', '"Girls often ask boys out and pay" — nhưng không phải <b>chỉ</b> con gái (only) → B sai nên là đáp án EXCEPT.'),
    ('A', '"In Spain, teens join a <b>pandilla</b>, a club for a group of friends with the same interests".'),
    ('C', '"In Russia, dates take place at <b>dances or at clubs</b> … cinema".'),
    ('C', '"In Japan and Korea, most high school students <b>don\'t date</b> …" → hẹn hò rất hiếm với học sinh THPT.'),
])
put('re3', [
    ('T', '"Following rules at home can help children learn to follow rules in other places."'),
    ('T', '"Breaking a rule is a child\'s way of <b>learning about his world</b>."'),
    ('F', '"It is normal for children to break rules and test limits" → không phải đứa trẻ nào phá luật cũng cứng đầu/hư.'),
    ('T', '"everyone needs to know, understand, and follow the rules" → áp dụng như nhau cho mọi thành viên.'),
    ('F', '"It is also <b>hard for parents to consistently enforce</b> lots of new rules" → trẻ nhỏ không thể theo luật mới một cách nhất quán; chỉ nên 2–3 luật quan trọng.'),
    ('T', '"The number of rules you set <b>depends on your child\'s ability</b> to understand and remember" → số luật khác nhau theo từng trẻ/gia đình, khó đặt giống nhau.'),
])
put_open('re4', [
    '<b>Mẫu:</b> Because they maintain peace and order in the family. (đoạn 1)',
    '<b>Mẫu:</b> Everybody (all family members) should be involved in making the decisions of important matters. (đoạn 2)',
    '<b>Mẫu:</b> Parents are the pillars of the family; they guide the children to be responsible and practise good values. (đoạn 3)',
    '<b>Mẫu:</b> Rules teach children to be more responsible and disciplined, not only at home but also outside. (đoạn 4)',
    '<b>Mẫu:</b> They help prevent conflicts, misunderstanding, quarrels and fights among children. (đoạn 4)',
])

# ======================= WRITING =======================
put('wr1', [
    ('D', 'When parents limit their children\'s screen time, <b>they are taking away their children\'s independence</b>. (D)'),
    ('C', 'When parents limit <b>our</b> screen time, <b>we lose the opportunity to learn to self-regulate</b>. (C) — cùng ngôi "our/we".'),
    ('A', 'Another reason for the issue is <b>the lack of face-to-face interactions</b>. (A) — "is" + danh từ.'),
    ('E', 'Technology is very popular, <b>but some teenagers still interact face-to-face all the time</b>. (E) — "but" chỉ sự tương phản.'),
    ('B', 'Lacking face-to-face interactions may lead <b>them to spend more time on screen</b>. (B) — lead sb to V.'),
])
put('wr2', [
    ('D', '"Although some screen time can be educational, <b>too much of it may have a negative effect on a child\'s development and overall well-being</b>."'),
    ('F', 'increase the risk of <b>inconsistent sleep, obesity or problems with behaviour and attention</b>.'),
    ('B', '"The more screen time a child has, <b>the more likely he will be to have trouble falling asleep</b>…" – cấu trúc so sánh kép (The more…, the more…).'),
    ('A', 'more <b>likely to have foods high in fat and sugar</b> – hợp với "advertisements for fast food".'),
    ('C', 'also <b>less likely to be active</b> – kết quả của việc ngồi trước màn hình lâu.'),
    ('E', 'difficulties in school, <b>attention problems and behavioural issues</b>.'),
])
put_open('wr3', [
    '<b>Bài mẫu (≈150 từ):</b><br><i>In today\'s digital age, teenagers are often found glued to their screens. Although technology has its benefits, limiting teenagers\' screen time is essential for their overall well-being.</i><br>'
    '<i>Firstly, prolonged screen time can contribute to a sedentary lifestyle, leading to physical health problems like obesity. Furthermore, excessive use of devices may strain teenagers\' eyes and affect their sleep. Moreover, too much screen time means less time for physical activities and face-to-face interactions, which are crucial for their social and emotional development.</i><br>'
    '<i>In conclusion, limiting screen time is crucial for teenagers\' health and well-being. Parents and educators must work together to set reasonable limits and encourage alternative activities.</i><br>'
    '<b>Gợi ý cấu trúc:</b> mở bài nêu quan điểm → 2–3 lí do (sức khoẻ thể chất, mắt/giấc ngủ, giao tiếp trực tiếp) → kết bài khẳng định lại.'
])

# ======================= BÀI KIỂM TRA (50 câu) =======================
put('kt', [
    ('A', 'media /ˈmiːdiə/ chữ a = /ə/; adapt /əˈdæpt/ (a gạch chân = /æ/), family /ˈfæməli/, characteristic /ˌkærəktəˈrɪstɪk/ = /æ/.'),
    ('D', 'scene /siːn/ chữ e = /iː/; experience, extended, belief đọc /ɪ/.'),
    ('C', 'social /ˈsəʊʃl/ chữ c = /ʃ/; influence /ˈɪnfluəns/, honesty /ˈɒnɪsti/, curious /ˈkjʊəriəs/ chữ c/s = /s/.'),
    ('B', 'musician /mjuˈzɪʃn/ nhấn âm 2; curious, grandmother, argument nhấn âm 1.'),
    ('A', 'generational /ˌdʒenəˈreɪʃənl/ nhấn âm 3; characteristic, developmental, experimental nhấn âm 4.'),
    ('C', 'Firefighters arrived on the <b>scene</b> = đến hiện trường (collocation: arrive on the scene).'),
    ('D', 'different social <b>values</b> = những giá trị xã hội khác nhau.'),
    ('A', 'all the <b>characteristics</b> of a great father = mọi đặc điểm của một người cha tuyệt vời.'),
    ('B', 'hear people\'s <b>views</b> on a range of subjects = nghe quan điểm của mọi người.'),
    ('D', '<b>Conflicts</b> between parents and children = xung đột giữa cha mẹ và con cái (collocation chuẩn). fights/wars quá mạnh.'),
    ('C', 'school regulations (quy định) → bắt buộc từ bên ngoài: <b>have to</b>. (should chỉ là lời khuyên; can sai nghĩa; must cũng gần nghĩa nhưng đề chọn have to.)'),
    ('B', 'Trẻ <b>không được</b> phá luật hay cãi bố mẹ → mustn\'t.'),
    ('C', '"…or you\'ll get punishment" → bắt buộc: <b>must</b>.'),
    ('A', 'Làm những việc vui cùng nhau là điều <b>nên</b> làm: should.'),
    ('D', 'Không xả rác ở bất cứ đâu → cấm: <b>mustn\'t</b>.'),
    ('C', '<b>Traditional</b> (truyền thống) ≈ <b>conventional</b> (theo lệ thường).'),
    ('D', '<b>influence</b> (ảnh hưởng) ≈ <b>affect</b>.'),
    ('B', '<b>typical</b> (điển hình) trái nghĩa <b>unusual</b> (khác thường).'),
    ('A', '<b>Tight</b> (chật) trái nghĩa <b>loose</b> (rộng).'),
    ('D', 'Được nhắc làm bài tập → đáp lại: <b>Thank you for reminding me.</b>'),
    ('D', 'Ý kiến "all family members should share the chores equally" → đồng tình: <b>There\'s no doubt about it.</b>'),
    ('C', 'Nghe nói thấy John ở workshop → phản hồi nghi ngờ: <b>That can\'t be John because he\'s in Paris now.</b>'),
    ('C', 'Nhận học bổng Harvard → chúc mừng: <b>Good job!</b>'),
    ('B', 'Cảm ơn → đáp: <b>You\'re welcome.</b>'),
    ('C', 'lead <b>to</b>/result <b>in</b> complaints: "(25) in complaints" → <b>results</b> (results in). leads cần "to".'),
    ('B', 'Sau "are" cần tính từ: young people are <b>disrespectful</b> (thiếu tôn trọng) and disobedient.'),
    ('C', 'appreciate the <b>value</b> of money = trân trọng giá trị đồng tiền.'),
    ('C', 'One explanation <b>lies</b> in how society has changed = lời giải thích nằm ở (lie in).'),
    ('A', 'parents are very <b>ambitious</b> for their children (hoài bão/kì vọng cho con) because they want them to achieve more.'),
    ('D', 'Tuổi teen khó khăn vì "parents don\'t understand what their children think and believe" – ý chung của cả bài (xung đột về giờ giấc, xe, điểm, điện thoại, ăn uống).'),
    ('B', '"Teenage is a time when a lot of kids want to <b>show their independence</b>… refuse to give them their own bikes".'),
    ('A', 'Nguyên nhân điểm giảm: "increasing difficulty level of school work, newer subjects, more socializing" – còn <b>sympathy from parents</b> thì không phải (EXCEPT) vì "their parents are not sympathetic".'),
    ('C', '"parents believe that a growing body needs <b>proper nutrition</b>".'),
    ('B', 'Ý chính: các lí do phổ biến khiến thanh thiếu niên cãi nhau với bố mẹ (giờ giấc, xe, điểm, điện thoại, ăn uống).'),
    ('B', 'Sau mustn\'t dùng động từ nguyên thể → bỏ "to": You mustn\'t <b>drive</b> a car.'),
    ('A', 'Hẹn bác sĩ bất cứ lúc nào bạn muốn → không cần hẹn trước: <b>don\'t have to</b> make an appointment (shouldn\'t sai ý).'),
    ('C', 'Trời sắp mưa → khuyên mang áo mưa: <b>should</b> bring (must quá mạnh so với một lời khuyên).'),
    ('D', 'because I must <b>study</b> (sau must là động từ nguyên thể, không phải studying).'),
    ('C', 'Chủ Nhật không cần đến trường: "because I <b>didn\'t have to</b> go" (không phải mustn\'t, vì mustn\'t là cấm).'),
    ('C', 'Dù có ít cơ hội thắng, bạn <b>shouldn\'t</b> từ bỏ ước mơ. (should → shouldn\'t)'),
])
ANS['kt.41'] = ['should speak in a polite voice to other people', 'speak in a polite voice to other people']
EXPLANATIONS['kt.41'] = 'expect sb to V = "It is sb\'s wish that + S (should) V" → <b>I should speak in a polite voice to other people</b>.'
ANS['kt.42'] = ['have to bring your cell phone with you at any time', 'have to bring your cellphone with you at any time', 'have to bring your mobile phone with you at any time']
EXPLANATIONS['kt.42'] = 'It is unnecessary to… = <b>don\'t have to</b> + V → <b>You don\'t have to bring your cell phone with you at any time.</b>'
ANS['kt.43'] = ['have to stop when the red light is on', 'must stop when the red light is on']
EXPLANATIONS['kt.43'] = 'It is a rule to… = <b>have to / must</b> → <b>You have to stop when the red light is on.</b>'
ANS['kt.44'] = ['must study for the test if you dont want to fail', 'should study for the test if you dont want to fail', "must study for the test if you don't want to fail", "should study for the test if you don't want to fail"]
EXPLANATIONS['kt.44'] = 'It is a good thing that you… = lời khuyên → <b>You should (must) study for the test if you don\'t want to fail.</b>'
ANS['kt.45'] = ["mustn't bring pets into that restaurant", 'must not bring pets into that restaurant']
EXPLANATIONS['kt.45'] = '… is against the rules = cấm → <b>You mustn\'t bring pets into that restaurant.</b>'
ANS['kt.46'] = ['parents should be a role model for the kind of habits that they want their child to develop',
                "dont just talk the talk parents should be a role model for the kind of habits that they want their child to develop",
                'parents should be a role model for the kind of habits they want their child to develop']
EXPLANATIONS['kt.46'] = '<b>Mẫu:</b> Don\'t just talk the talk. Parents should be a role model for the kind of habits that they want their child to develop.'
ANS['kt.47'] = ['parents should create a family game or walk or other activities that their child enjoys as a result the child doesnt sit in front of a screen any more',
                'parents should create a family game or walk or other activities that their child enjoys as a result the child doesnt sit in front of a screen anymore']
EXPLANATIONS['kt.47'] = '<b>Mẫu:</b> Encourage other activities. Parents should create a family game or walk, or other activities that their child enjoys. As a result, the child doesn\'t sit in front of a screen any more.'
ANS['kt.48'] = ['an hour before the bedtime is ideal for everyone because it helps minimize problems',
                'an hour before bedtime is ideal for everyone because it helps minimize problems',
                'an hour before the bedtime is ideal for everyone because it helps minimise problems']
EXPLANATIONS['kt.48'] = '<b>Mẫu:</b> Have set times to power down. An hour before the bedtime is ideal for everyone because it helps minimize problems.'
ANS['kt.49'] = ['parents should make the dinner table screen free or ban devices from other areas that they want to reserve for family time',
                'parents should make the dinner table screen-free or ban devices from other areas that they want to reserve for family time']
EXPLANATIONS['kt.49'] = '<b>Mẫu:</b> Set tech-free zones. Parents should make the dinner table screen-free or ban devices from other areas that they want to reserve for family time.'
ANS['kt.50'] = ['if children understand why their parents are limiting screen time it is easier to get them to cooperate',
                'it is easier to get them to cooperate if children understand why their parents are limiting screen time']
EXPLANATIONS['kt.50'] = '<b>Mẫu:</b> Talk to children. If children understand why their parents are limiting screen time, it is easier to get them to cooperate.'

# vg4, vg8 dùng lựa chọn dạng chữ (plain) -> đáp án là chính từ/cụm từ đúng
for _i, _v in enumerate(['may', 'must', 'have to', 'have to', "mustn't", "mustn't"], 1):
    ANS['vg4.%d' % _i] = _v
for _i, _v in enumerate(["don't have to", "oughtn't", 'have to', "mustn't", "doesn't have to", "mustn't", "don't have to", "doesn't have to", 'have to', 'ought to'], 1):
    ANS['vg8.%d' % _i] = _v
