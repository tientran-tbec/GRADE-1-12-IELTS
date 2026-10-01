# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Unit 3 Music (Tiếng Anh 10 Global Success) – Bộ BÀI TẬP BỔ TRỢ.
Quy ước:
  mcq  : chữ cái 'A'-'D' (hoặc list nếu nhiều đáp án chấp nhận)      tf : 'T' / 'F'
  fill : danh sách đáp án chấp nhận (1 ô)
  open : không chấm điểm, EXPLANATIONS chứa đáp án mẫu
Đáp án lấy từ khoá tô màu trong nửa sau file Word (src/l10u3/bt_c.txt), sau đó tự giải độc lập để đối chiếu."""

GHI_CHU_RA_SOAT = [
    'ph1.9 (E1, Q9): khoá Word = C (receive) nhưng SAI. upload /ʌpˈləʊd/ (động từ), receive /rɪˈsiːv/, guitar /ɡɪˈtɑː/ đều nhấn âm 2; chỉ theatre /ˈθɪətə/ nhấn âm 1 -> ANS = B.',
    'vg1.11 (E3): "originated" (khoá Word B) và "originating" (C, mệnh đề quan hệ rút gọn chủ động) đều dùng được -> ANS = [B, C].',
    'vg1.13 (E3): khoá Word = C (season); "episode" (D) cũng hợp nghĩa ("the 4th episode I\'ve seen") -> ANS = [C, D].',
    'vg1.22 (E3): khoá Word = B (fans); "people" (A) cũng đúng ngữ pháp/nghĩa -> ANS = [B, A].',
    'vg1.50 (E3): khoá Word = B (yet); "and" (D) nối hai vế song song cũng chấp nhận được -> ANS = [B, D]. vg1.52: khoá C (so), "and" (B) cũng được -> [C, B]. vg1.56: khoá A (but), "yet" (C) cùng nghĩa -> [A, C].',
    'vg1.59 (E3): khoá Word = A (and) nhưng "10 đề cử, nhưng chỉ thắng 2" hợp nhất với but (D) -> ANS = [D, A]. Giáo viên nên xem lại.',
    'vg1.17 (E3): nguồn mất chỗ trống ("released her Free Yourself"); đã thêm ______ trước "Free Yourself". vg1.22, 23, 27: bỏ gạch chân thừa quanh chỗ trống; vg1.27 bỏ "for" thừa ("seeking for" -> "seeking").',
    'vg1.45 (E3): nguồn "Peter wonders he should…" thiếu "whether"; đã thêm.',
    'vg2.4 (E4): nguồn "a gift from at least once…" thiếu tân ngữ; đã thêm "someone". vg2.37: bỏ gạch chân thừa. vg2.26 nguồn thiếu dấu cách sau "Question 26:" (đã xử lý trong generator).',
    'vg2.61 (E4): phương án A nguồn gõ "to lean" (nhiễu, có thể là lỗi gõ của "to learn"); giữ nguyên, đáp án D (to learn) không bị ảnh hưởng.',
    'vg2.34: khoá Word KHÔNG tô đáp án; tự giải = B (not to come). vg2.42 = A, vg2.45 = B, vg2.55 = C cũng không được tô; tự giải khớp.',
    'vg2.47: khoá Word = C (used to). Mệnh đề "When he lived in the countryside, he used to walk…" đúng.',
    'E4 thứ hai (vg3): nguồn đánh trùng nhãn "E4" cho bài nối câu; đã tách thành vg3 (8 câu). vg3.5 nguồn thiếu dấu chấm ("yesterday She"), vg3.8 thừa dấu phẩy; đã sửa. Khoá Q7 gõ sai "ou will" -> "you will". Đã bổ sung nhiều cách viết chấp nhận.',
    'li1 (E5 Nghe): khoá Word F-T-F-F-T. Đối chiếu audio script: bài nói "June 11, 2002" (đề ghi 2003) -> F; Simon Fuller T; finalists do khán giả bình chọn -> F; mùa 13 có 3 giám khảo -> F; Star World T. Đề E5 nguồn gõ "June 11,2003", đã chuẩn hoá khoảng trắng.',
    're2 (E7): nguồn gõ sai "new while R&B music" -> "new white R&B music", "new eroup" -> "new group"; đã sửa trong đoạn văn.',
    're2.3: "Noticing the success of…" khoá A; các lựa chọn khác (Detecting, Warning, Perceiving) không hợp. re2.8: "start by singing" (D) theo khoá.',
    'Dữ liệu E5 là bài nghe (mp3 đã nén mono 64k tại audio/lop10_u3_botro_nghe.mp3). Chỉ có phần T/F; audio script nằm trong khoá Word nên chép vào giải thích li1.',
    'ảnh trong Word: 2 ảnh image1.jpeg (35x2) và image2.jpeg (1x1) chỉ là hình trang trí/nhiễu nên không đưa vào bài.',
    'Word bộ này không có đề kiểm tra riêng nên không có trang "kiem-tra". Phần lý thuyết: sửa vài ví dụ nguồn sai ngữ pháp ("for dogs is" -> "for dogs are"; "nor we don\'t want" -> "nor do we want"; "or she comes" -> "or she will come").',
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


# ======================= TRỌNG ÂM (E1) =======================
put('ph1', [
    ('A', '<b>become</b> /bɪˈkʌm/ nhấn âm 2. idol /ˈaɪdl/, comment /ˈkɒment/, season /ˈsiːzn/ nhấn âm 1.'),
    ('D', '<b>talent</b> /ˈtælənt/ nhấn âm 1. perform /pəˈfɔːm/, release /rɪˈliːs/, receive /rɪˈsiːv/ nhấn âm 2.'),
    ('C', '<b>award</b> /əˈwɔːd/ nhấn âm 2. talent /ˈtælənt/, artist /ˈɑːtɪst/, famous /ˈfeɪməs/ nhấn âm 1.'),
    ('D', '<b>attend</b> /əˈtend/ nhấn âm 2. theatre /ˈθɪətə/, movie /ˈmuːvi/, famous /ˈfeɪməs/ nhấn âm 1.'),
    ('C', '<b>suffer</b> /ˈsʌfə/ nhấn âm 1. enjoy /ɪnˈdʒɔɪ/, perform /pəˈfɔːm/, agree /əˈɡriː/ nhấn âm 2.'),
    ('D', '<b>expect</b> /ɪkˈspekt/ nhấn âm 2. weather /ˈweðə/, birthday /ˈbɜːθdeɪ/, boring /ˈbɔːrɪŋ/ nhấn âm 1.'),
    ('B', '<b>receive</b> /rɪˈsiːv/ nhấn âm 2. singer /ˈsɪŋə/, programme /ˈprəʊɡræm/, lyrics /ˈlɪrɪks/ nhấn âm 1.'),
    ('A', '<b>compose</b> /kəmˈpəʊz/ nhấn âm 2. careful /ˈkeəfl/, second /ˈsekənd/, album /ˈælbəm/ nhấn âm 1.'),
    ('B', '<b>theatre</b> /ˈθɪətə/ nhấn âm 1. upload /ʌpˈləʊd/ (động từ), receive /rɪˈsiːv/, guitar /ɡɪˈtɑː/ đều nhấn âm 2. (Khoá Word ghi C – sai, xem ghi chú.)'),
    ('B', '<b>compose</b> /kəmˈpəʊz/ nhấn âm 2. singer /ˈsɪŋə/, common /ˈkɒmən/, programme /ˈprəʊɡræm/ nhấn âm 1.'),
    ('A', '<b>favour</b> /ˈfeɪvə/ nhấn âm 1. enjoy /ɪnˈdʒɔɪ/, reveal /rɪˈviːl/, perform /pəˈfɔːm/ nhấn âm 2.'),
    ('D', '<b>perform</b> /pəˈfɔːm/ nhấn âm 2. common /ˈkɒmən/, music /ˈmjuːzɪk/, people /ˈpiːpl/ nhấn âm 1.'),
    ('D', '<b>contestant</b> /kənˈtestənt/ nhấn âm 2. melody /ˈmelədi/, festival /ˈfestɪvl/, positive /ˈpɒzətɪv/ nhấn âm 1.'),
])

# ======================= PHÁT ÂM (E2) =======================
put('ph2', [
    ('B', 'music /ˈmjuːzɪk/: s = /z/. single /ˈsɪŋɡl/, contest /ˈkɒntest/, release /rɪˈliːs/: s = /s/.'),
    ('A', 'compose /kəmˈpəʊz/: -se = /z/. purchase /ˈpɜːtʃəs/, release /rɪˈliːs/, increase /ɪnˈkriːs/: -se = /s/.'),
    ('A', 'version /ˈvɜːʃn/: s = /ʃ/. process /ˈprəʊses/, modest /ˈmɒdɪst/, contestant /kənˈtestənt/: s = /s/.'),
    ('C', 'debut /ˈdeɪbjuː/: u = /juː/. instrument /ˈɪnstrəmənt/, platinum /ˈplætɪnəm/, album /ˈælbəm/: u = /ə/.'),
    ('D', 'passionate /ˈpæʃənət/: -ate = /ət/ (tính từ). eliminate, nominate, originate (động từ): -ate = /eɪt/.'),
    ('B', 'content (n) /ˈkɒntent/: -ent = /ent/. moment /ˈməʊmənt/, parent /ˈpeərənt/, talent /ˈtælənt/: -ent = /ənt/.'),
    ('A', 'latest /ˈleɪtɪst/: -est = /ɪst/. contest /ˈkɒntest/, request /rɪˈkwest/, suggest /səˈdʒest/: -est = /est/.'),
    ('C', 'certificate (n) /səˈtɪfɪkət/: -ate = /ət/. debate /dɪˈbeɪt/, commemorate /kəˈmeməreɪt/, educate /ˈedʒukeɪt/: -ate = /eɪt/.'),
    ('D', 'comment /ˈkɒment/: -ent = /ent/. current /ˈkʌrənt/, moment /ˈməʊmənt/, talent /ˈtælənt/: -ent = /ənt/.'),
    ('C', 'establish /ɪˈstæblɪʃ/: est- = /ɪst/. protest (v) /prəˈtest/, arrest /əˈrest/, nest /nest/: est = /est/.'),
])

# ======================= TỪ VỰNG & LIÊN TỪ (E3) =======================
put('vg1', [
    ('C', '<b>audience</b> = khán giả (nói chung); "judges and audience". spectators/viewers thường dùng cho thể thao/TV; passer-by = người qua đường.'),
    ('A', '<b>perform</b> at the local theatre = biểu diễn ở nhà hát địa phương.'),
    ('B', 'the panel of <b>judges</b> = ban giám khảo của chương trình tài năng truyền hình.'),
    ('A', '<b>identify with</b> = đồng cảm/hoà mình với (nhân vật).'),
    ('B', '<b>in search of</b> = để tìm kiếm.'),
    ('C', '<b>musical instruments</b> = nhạc cụ (flute, guitar).'),
    ('C', 'be <b>eliminated</b> = bị loại sau chương trình.'),
    ('D', 'be invited to be a <b>judge</b> in competitions = làm giám khảo.'),
    ('A', '13 number-one <b>singles</b> = 13 đĩa đơn quán quân (danh từ số nhiều sau số từ).'),
    ('B', '<b>play</b> an important role = đóng vai trò quan trọng.'),
    (['B', 'C'], 'Rút gọn mệnh đề quan hệ: competition <b>originated</b> / <b>originating</b> in the UK. Khoá Word chọn B; C cũng chấp nhận.'),
    ('A', '<b>debut</b> album = album đầu tay.'),
    (['C', 'D'], 'Khoá Word = <b>season</b> (mùa thứ 4 của chương trình). <b>episode</b> (tập) cũng hợp nghĩa nên được chấp nhận.'),
    ('D', 'a prominent <b>figure</b> of modern Vietnamese music = nhân vật nổi bật.'),
    ('D', 'The best singer <b>award</b> = giải thưởng ca sĩ xuất sắc nhất.'),
    ('D', 'national <b>anthem</b> = quốc ca.'),
    ('A', '<b>debut album</b> = album đầu tay "Free Yourself".'),
    ('A', 'national <b>anthem</b> = quốc ca (Tiến quân ca).'),
    ('A', '<b>pop</b> music: giai điệu đơn giản, dễ nghe, dễ nhớ.'),
    ('A', 'The <b>audience</b> cheered loudly = khán giả reo hò.'),
    ('A', 'my <b>idol</b> = thần tượng của tôi.'),
    (['B', 'A'], 'over 150000 <b>fans</b> packed into the stadium to support… = hơn 150.000 cổ động viên (khoá Word = B; "people" cũng đúng).'),
    ('C', 'win the Grand Music <b>Competition</b> = giành chiến thắng cuộc thi.'),
    ('C', 'was <b>judged</b> to be the best = được đánh giá là hay nhất (bị động).'),
    ('B', 'sign a lot of <b>contracts</b> with celebrities = ký nhiều hợp đồng với người nổi tiếng.'),
    ('C', 'Chopin là một trong những <b>composers</b> (nhà soạn nhạc) piano vĩ đại nhất.'),
    ('D', 'seeking the <b>talented</b> musician = nhạc sĩ có tài năng.'),
    ('A', 'Vế sau là KẾT QUẢ của vế trước ("trò chơi thử thách nên không dễ dành ít thời gian…") -> <b>so</b>.'),
    ('A', 'Vế sau giải thích NGUYÊN NHÂN ("vì nó ngày càng chán") -> <b>for</b>.'),
    ('B', 'whether… <b>or</b> … = hay là (lựa chọn).'),
    ('C', 'Hai vế trái ngược ("có hại nhưng nhiều người vẫn hút") -> <b>yet</b> (nor, so sai nghĩa).'),
    ('D', 'Do you like singing <b>or</b> dancing? = lựa chọn.'),
    ('D', 'I admire Celine Dion <b>for</b> she has a nice voice = vì cô ấy có giọng hay (nguyên nhân).'),
    ('C', 'Mất chìa khoá -> không vào nhà được: KẾT QUẢ -> <b>so</b>.'),
    ('D', 'Bị lạc nhưng may là có bản đồ: TRÁI NGƯỢC -> <b>but</b>.'),
    ('A', 'Nhạc pop phổ biến vì giai điệu đơn giản, dễ nhớ: NGUYÊN NHÂN -> <b>for</b>.'),
    ('B', 'Would you like milk tea <b>or</b> hot chocolate? = lựa chọn.'),
    ('D', 'Răng sâu nhưng từ chối đi nha sĩ: TRÁI NGƯỢC -> <b>but</b>.'),
    ('B', 'Phải làm tốt bài thi, <b>or</b> (nếu không) sẽ không tốt nghiệp -> or = "nếu không thì".'),
    ('C', 'Cô ấy nghĩ nên học đại học <b>for</b> (vì) muốn có bằng cấp cho công việc mơ ước.'),
    ('A', 'You can go with us <b>or</b> you can go alone = lựa chọn.'),
    ('A', 'Đầu tư nhiều tiền <b>but</b> doanh nghiệp phá sản nhanh: TRÁI NGƯỢC.'),
    ('C', 'Mưa to nên chương trình bị huỷ: KẾT QUẢ -> <b>so</b>.'),
    ('A', 'Sau <b>nor</b> phải đảo ngữ: "…, nor did they realise…".'),
    ('B', 'whether he should stay home… <b>or</b> he should go out = lựa chọn.'),
    ('C', 'Hai vế song song, cùng diễn ra ("các cậu bé chơi game, các cô bé xem TV") -> <b>and</b>.'),
    ('A', 'Linda luyện hát mỗi ngày <b>for</b> (vì) cô ấy muốn trở thành ca sĩ.'),
    ('C', 'Chương trình bị hoãn <b>for</b> (vì) ca sĩ gặp tai nạn.'),
    ('A', 'Cố gắng hết sức <b>but</b> kết quả không như mong đợi: TRÁI NGƯỢC.'),
    (['B', 'D'], 'Hai vế đối lập/song song ("cô ấy thích hài, chồng thích phim hành động"): khoá Word = <b>yet</b>; <b>and</b> cũng chấp nhận được.'),
    ('B', 'Gia đình rất thích món Nhật nên đặt hai lần/tuần: KẾT QUẢ -> <b>so</b>.'),
    (['C', 'B'], 'Van Cao là nhạc sĩ tài năng <b>so</b> (nên) giành nhiều giải thưởng: KẾT QUẢ (khoá Word = so; <b>and</b> cũng chấp nhận được).'),
    ('C', 'Nên tập nhiều hơn, <b>but</b> sức khoẻ gần đây không tốt: TRÁI NGƯỢC.'),
    ('B', 'Có thể đi xem phim với tôi <b>or</b> đi xem hòa nhạc một mình: lựa chọn.'),
    ('B', 'Would you like to go to the cinema <b>or</b> watch at home? = lựa chọn.'),
    (['A', 'C'], 'Có giọng tiềm năng <b>but / yet</b> không định theo nghề: TRÁI NGƯỢC (khoá Word = but, yet cũng đúng).'),
    ('A', 'emotive voice <b>and</b> skillful performance = thêm ý (giọng truyền cảm và biểu diễn điêu luyện).'),
    ('D', 'Giọng hay <b>but</b> phong cách trình diễn chưa đủ tốt: TRÁI NGƯỢC.'),
    (['D', 'A'], 'Được đề cử 10 giải Grammy <b>but</b> chỉ thắng 2: TRÁI NGƯỢC. (Khoá Word = and; "and" vẫn có thể chấp nhận.)'),
    ('C', 'Mike là ca sĩ nổi tiếng <b>but</b> giọng hát lại dở: TRÁI NGƯỢC.'),
    ('D', 'Close the window <b>and</b> turn off the lights = thêm ý, hai hành động liên tiếp.'),
    ('C', 'Buổi diễn tẻ nhạt <b>so</b> tôi ngủ gật: KẾT QUẢ.'),
    ('A', 'Muốn trở thành nghệ sĩ violin <b>yet</b> bố mẹ không cho: TRÁI NGƯỢC (but không có trong phương án).'),
    ('A', 'Lúc đầu hấp dẫn <b>yet</b> về sau chán: TRÁI NGƯỢC.'),
])

# ======================= TO V / V0 (E4) =======================
put('vg2', [
    ('B', 'decide + <b>to V</b>.'),
    ('B', 'begin + <b>to V</b> (hoặc V-ing): began to rain.'),
    ('D', 'see + O + <b>V0</b> (thấy toàn bộ hành động): saw her cross the street.'),
    ('B', 'It\'s customary <b>to V</b> (It is + adj + to V).'),
    ('A', 'decide + <b>to V</b>: decided to attend.'),
    ('D', 'manage + <b>to V</b>.'),
    ('A', 'let + O + <b>V0</b>.'),
    ('D', 'It\'s dangerous <b>to V</b>.'),
    ('A', 'encourage + O + <b>to V</b>.'),
    ('D', 'happy <b>to hear</b> (to V sau tính từ chỉ cảm xúc).'),
    ('C', 'invite + O + <b>to V</b>.'),
    ('B', 'require + O + <b>to V</b>.'),
    ('B', 'allow + O + <b>to V</b>.'),
    ('A', 'deserve + <b>to V</b>; "to be treated" (bị động: được đối xử).'),
    ('C', 'It\'s impolite <b>not to take</b> off shoes… (ở Nhật bỏ giày là lịch sự).'),
    ('D', 'forget + <b>to V</b> = quên làm (việc cần làm): forgot to lock.'),
    ('B', 'learn how <b>to V</b>.'),
    ('D', 'intend + <b>to V</b>.'),
    ('C', 'make + O + <b>V0</b>.'),
    ('C', 'make + O + <b>V0</b>.'),
    ('D', 'see + O + <b>V0</b>.'),
    ('B', 'be about <b>to V</b> = sắp sửa.'),
    ('C', 'enough + N + <b>to V</b>: enough candies to share.'),
    ('A', 'I\'d like <b>to V</b>.'),
    ('D', 'see + O + <b>V0</b> (feed).'),
    ('A', 'promise + <b>to V</b>.'),
    ('C', 'enough + N + <b>to V</b>: enough money to buy.'),
    ('D', 'make + O + <b>V0</b>.'),
    ('B', 'remind + O + <b>not to V</b> = nhắc ai đừng…'),
    ('B', 'had better + <b>V0</b>.'),
    ('D', 'refuse + <b>to V</b>.'),
    ('A', 'would like + <b>to V</b>; "to be promoted" (bị động: được thăng chức).'),
    ('B', 'let + O + <b>V0</b>.'),
    ('B', 'expect + O + <b>not to V</b> (không mong John đến muộn).'),
    ('C', 'promise + <b>to V</b>.'),
    ('B', 'make + O + <b>V0</b>.'),
    ('A', 'encourage + O + <b>to V</b>; bị động: were encouraged to learn.'),
    ('D', 'adj + enough + <b>to V</b>.'),
    ('B', 'It takes + O + time + <b>to V</b>.'),
    ('B', 'allow + <b>to V</b> (bị động: are not allowed to wear).'),
    ('C', 'let + O + <b>V0</b>.'),
    ('A', 'manage + <b>to V</b>.'),
    ('B', 'Chỉ mục đích: <b>so as to</b> + V0 ("để đọc Kim Vân Kiều"); so that cần mệnh đề, in order not to/so as not to là phủ định.'),
    ('A', 'determine + <b>to V</b>.'),
    ('B', 'advise + O + <b>not to V</b> (cấu trúc phủ định đúng).'),
    ('B', 'whether + <b>to V</b>.'),
    ('C', '<b>used to</b> + V0 = từng (thói quen trong quá khứ).'),
    ('A', 'promise + <b>to V</b>.'),
    ('B', 'plan + <b>to V</b>.'),
    ('A', 'Let\'s + <b>V0</b>.'),
    ('D', 'could + <b>V0</b> (động từ khuyết thiếu).'),
    ('D', 'agree + <b>to V</b>.'),
    ('D', 'make + O + <b>V0</b>.'),
    ('A', 'hesitate + <b>to V</b>.'),
    ('C', 'decide + <b>to V</b>.'),
    ('D', 'intend + <b>not to V</b>: "không định nói sự thật cho anh ta vì sợ anh ta nổi cơn điên" (for fear that… = vì sợ rằng…).'),
    ('B', 'would love + <b>to V</b>.'),
    ('D', 'let + O + <b>V0</b>.'),
    ('C', 'adj + enough + <b>to V</b>.'),
    ('D', 'hear + O + <b>V0</b> (nghe toàn bộ hành động).'),
    ('D', 'want + <b>to V</b>: to learn (phương án A "to lean" sai chính tả/nghĩa).'),
])

# ======================= NỐI CÂU (E4 bài 2) =======================
put('vg3', [
    (["i'd like to go to the party but i'm too busy", 'i would like to go to the party but i am too busy', "i'd like to go to the party, but i'm too busy"],
     '<b>Mẫu:</b> I\'d like to go to the party, but I\'m too busy. (but: trái ngược)'),
    (['it was sunny so lan took an umbrella', 'it was sunny, so lan took an umbrella'],
     '<b>Mẫu:</b> It was sunny, so Lan took an umbrella. (so: kết quả)'),
    (['anna is an amazing dancer and her parents are proud of her', 'anna is an amazing dancer, and her parents are proud of her'],
     '<b>Mẫu:</b> Anna is an amazing dancer, and her parents are proud of her. (and: thêm ý)'),
    (['you can vote online for your favourite singer or you can send text messages', 'you can vote online for your favourite singer, or you can send text messages'],
     '<b>Mẫu:</b> You can vote online for your favourite singer, or you can send text messages. (or: lựa chọn)'),
    (['lisa went shopping yesterday but she did not buy anything', "lisa went shopping yesterday but she didn't buy anything", "lisa went shopping yesterday, but she didn't buy anything"],
     '<b>Mẫu:</b> Lisa went shopping yesterday, but she didn\'t buy anything. (but: trái ngược)'),
    (["john's parents own a restaurant and sometimes he helps in the kitchen at weekends", "john's parents own a restaurant, and sometimes he helps in the kitchen at weekends"],
     '<b>Mẫu:</b> John\'s parents own a restaurant, and sometimes he helps in the kitchen at weekends. (and: thêm ý)'),
    (['go inside or you will catch a cold', 'go inside, or you will catch a cold', "go inside or you'll catch a cold", "go inside, or you'll catch a cold"],
     '<b>Mẫu:</b> Go inside, or you will catch a cold. (or = nếu không thì). Khoá Word gõ sai "ou will".'),
    (['rita is a good drummer so she will probably be invited to join the band', 'rita is a good drummer, so she will probably be invited to join the band'],
     '<b>Mẫu:</b> Rita is a good drummer, so she will probably be invited to join the band. (so: kết quả)'),
])

# ======================= NGHE (E5) =======================
put('li1', [
    ('F', 'Audio: "The first season of American Idol premiered in June 11, <b>2002</b>" -> đề ghi 2003 nên SAI.'),
    ('T', 'Audio: "…British Pop Idol program founded by producer <b>Simon Fuller</b>".'),
    ('F', 'Audio: "the finalists will be decided by the vote of the <b>audience</b> by phone" (không phải vote của giám khảo).'),
    ('F', 'Audio: "Currently, from the 13th season, the program has <b>three judges</b>" (không phải bốn).'),
    ('T', 'Audio: "Viewers from Vietnamese and some Asian countries can also watch American Idol on <b>Star World channel</b>".'),
])

# ======================= NÓI =======================
put_open('sp1', [
    '<b>Bài mẫu:</b> One of my favourite TV music shows is The Voice of Vietnam. It is a singing competition on television purchased from the original "The Voice" by Cat Tien Sa and broadcast in Vietnam starting from July 8, 2012 on VTV3 channel. '
    'I know this programme through some means of media such as TV and magazines. The Voice is rated as one of the most popular entertainment programmes. This comes from not only the coaches – the outstanding faces of the entertainment industry – but also how contestants are chosen. '
    'There are some reasons why I like it. Firstly, it\'s new and different from other shows. The typical feature of the programme is that in the blind audition, in order to select contestants for 4 teams, the coaches turn their seats back to the stage and only choose contestants based on their singing voice. '
    'The criterion that the voice matters more than the appearance is considered new and has attracted a large number of viewers. In addition, the coaches are Vietnamese leading singers and composers. They have a sense of humour and real enthusiasm for potential young singers, which partly helps them reduce stress. The show is interesting and it\'s worth watching!',
])

# ======================= ĐỌC (E6, E7) =======================
put('re1', [
    ('A', 'Đoạn 1: "Based on the original <b>The Voice of Holland</b>, The Voice of America…" -> chương trình bắt nguồn từ Hà Lan. B, D sai (Holland không phát trên NBC/BBC theo bài); C bài nói thành công ở Holland.'),
    ('B', 'Đoạn 2: "Only those <b>fifteen and over</b> are eligible" = ít nhất 15 tuổi.'),
    ('C', 'Đoạn 3: "the winner is determined by votes from the <b>television audience</b>".'),
    ('D', 'Đoạn 3: bình chọn bằng "online voting on the official website, <b>SMS text</b> and <b>iTunes stores purchases</b>" -> D (khoá Word = D).'),
    ('D', 'Đoạn 3: "receives US$ 100,000 <b>and</b> a record contract with Universal Music Group" -> tiền thưởng lớn + cơ hội làm việc với công ty âm nhạc.'),
])

put('re2', [
    ('B', 'very <b>popular</b> with black Americans = rất được ưa chuộng (popular with).'),
    ('C', 'a mixture <b>of</b> A and B = hỗn hợp của…'),
    ('A', '<b>Noticing</b> the success of R&B music, white musicians started to copy = Nhận thấy thành công…'),
    ('D', '<b>this</b> new white R&B music (this + danh từ số ít không đếm được: music).'),
    ('C', 'Singers <b>attracted</b> millions of teenage fans = thu hút hàng triệu fan.'),
    ('A', 'was very <b>dangerous</b> (tính từ sau "very", động từ to be).'),
    ('B', 'sound the <b>same</b> = nghe giống nhau.'),
    ('D', 'start <b>by</b> + V-ing = bắt đầu bằng việc… (khoá Word = D).'),
    ('A', 'more <b>complicated</b> melodies = giai điệu phức tạp hơn (tính từ trước danh từ).'),
    ('B', 'different instruments, <b>such</b> as the Indian sitar = chẳng hạn như.'),
    ('D', 'have an influence <b>on</b> = có ảnh hưởng đến.'),
    ('A', 'the <b>early</b> 1970s = đầu những năm 1970.'),
    ('C', 'Electronics had <b>replaced</b> the amplified guitars… = đã thay thế (changed không đi với tân ngữ này theo nghĩa).'),
])

# ======================= VIẾT =======================
put('wr1', [
    (['i have admired my tam since i was a university student', "i've admired my tam since i was a university student", 'i have admired my tam since i was a student at university', 'i have admired my tam since i was a university student.'],
     '<b>Mẫu:</b> I have admired My Tam since I was a university student. (since + mệnh đề quá khứ -> hiện tại hoàn thành)'),
    (['she is not only a beautiful singer but also a talented composer', "she's not only a beautiful singer but also a talented composer"],
     '<b>Mẫu:</b> She is not only a beautiful singer but also a talented composer. (not only … but also)'),
    (['she participated as a judge in famous tv programs such as vietnam idol and the voice of vietnam a few years ago',
      'she participated as a judge in famous tv programmes such as vietnam idol and the voice of vietnam a few years ago',
      'she participated as a judge in famous tv programs such as vietnam idol and the voice of vietnam few years ago'],
     '<b>Mẫu:</b> She participated as a judge in famous TV programs such as Vietnam Idol and The Voice of Vietnam a few years ago. (a few years ago -> quá khứ đơn)'),
    (['she has won a lot of international and national prizes so far', 'she has won a lot of national and international prizes so far'],
     '<b>Mẫu:</b> She has won a lot of international and national prizes so far. (so far -> hiện tại hoàn thành)'),
    (['my tam became the first southeast asian artist to hold her own concert at jangchung gymnasium in korea in 2018',
      'my tam became the first southeast asian artist that held her own concert at jangchung gymnasium in korea in 2018',
      'my tam became the first southeast asian artist who held her own concert at jangchung gymnasium in korea in 2018',
      'my tam became the first southeast asian artist to hold her own concert at jangchung gymnasium, korea in 2018'],
     '<b>Mẫu:</b> My Tam became the first Southeast Asian artist to hold her own concert at Jangchung Gymnasium in Korea in 2018. (the first + to V; 2018 -> quá khứ đơn)'),
])

put_open('wr2', [
    '<b>Bài mẫu:</b><br>To: linda@gmail.com<br>Subject: My favourite singer<br>Dear Linda,<br>'
    'I am writing to tell you about my favourite singer, Celine Dion. She is a Canadian singer and was born in 1968. Celine Dion is a pop singer with melodious songs. However, her songs are also influenced by several genres like rock, classical, gospel, etc. '
    'Her music touches the hearts of millions of people around the world, including fans of different ages.<br>'
    'I admire her a lot because of her clear voice and attractive performance style. Her songs are not just noise; they have a special inner meaning instead. In addition, her great devotion to her musical career interests me. '
    'Her talent is shown by her singing in several languages such as French, Chinese, English, Italian, Latin, Japanese and Spanish. Moreover, she has won a lot of important awards, for example five Grammy Awards, including "Album of the Year" and "Record of the Year". '
    'All of the above reasons show why she is my favourite singer.<br>Best wishes,<br>Nancy',
])
