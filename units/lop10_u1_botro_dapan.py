# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Unit 1 Family life (Tiếng Anh 10 Global Success) – Bộ BÀI TẬP BỔ TRỢ.
Quy ước:
  mcq  : chữ cái 'A'-'D'      tf : 'T' / 'F'
  fill : danh sách đáp án chấp nhận (1 ô)
  open : không chấm điểm, EXPLANATIONS chứa đáp án mẫu
Đáp án lấy từ khoá tô màu trong nửa sau file Word (src/l10u1/bt_c.txt), sau đó tự giải độc lập để đối chiếu.
Khoá Word cho E3, E4 (trừ Q18), E5, E7, E9-E11 trùng hoàn toàn với bản tự giải; các điểm lệch/nghi vấn ghi ở GHI_CHU_RA_SOAT."""

GHI_CHU_RA_SOAT = [
    'ph1.5: finance /ˈfaɪnæns/ (khoá Word = D) nhưng còn cách đọc /fɪˈnæns/ làm routine (/iː/) thành từ khác -> ANS = [D, C].',
    'E3 (vg1): nguồn nhảy số 33 -> 35 (thiếu Question 34); đã đánh số lại liên tục 1-35 (Question 35, 36 của Word = vg1.34, vg1.35).',
    'vg1.4 và vg1.24: nguồn mất chỗ trống (ghi "My mother the responsibility…", "Do you have to the rubbish out?."); đã thêm ______ vào đúng vị trí.',
    'vg1.15: nguồn gõ sai "leff" -> "left". vg1.21: bỏ gạch chân thừa ở chỗ trống.',
    'vg1.33: "responsible for" đúng (A); B, C sai cấu trúc nên D (Both B & C) sai. Khoá Word = A, trùng.',
    'vg2.18: khoá Word KHÔNG tô đáp án; tự giải = C (goes / is going: often ... but today ... at noon).',
    'vg2.5: phương án D nguồn có dấu chấm thừa ("goes.") đã bỏ; vg2.3, vg2.4: thêm chỗ trống/dấu câu cho đủ câu.',
    'vg2.19: "sometimes" -> hiện tại đơn, chủ ngữ Bich số ít -> has (D).',
    'vg3.1 (E5): nguồn gõ sai "tae care" -> "take care". Khoá Word cho cả 5 từ trùng bản tự giải.',
    'li1 (Nghe, Task 1): khoá Word dùng dấu x trong bảng T/F, đã đọc từ bảng: 1T 2T 3T 4F 5T; đối chiếu bài nghe/audio script đều khớp.',
    'li2 (Nghe, Task 2): nguồn đánh số lại thành 4-5-6 và đáp án mẫu nằm lẫn ảnh trang trí; đã đánh số 1-3.',
    're1.7: khoá Word = D (unimportant) – hợp nghĩa ("feel they are unimportant"); worthy (C) không hợp "feel they are worthy" trong ngữ cảnh bất bình đẳng. Giữ khoá.',
    're1: nguồn có dấu chấm thừa "hours. which leads" -> đã sửa thành dấu phẩy.',
    're2: nguồn re2.1 phương án A gõ sai "an many…" -> "in many industrialized countries". Câu cuối đoạn 2 nguồn lỗi ("same extended family includes…") -> đã sửa "…extended family, which includes…".',
    're3.1: nguồn thiếu "to" trong "an opportunity share" -> đã thêm "to share".',
    're3.3: khoá Word = D (setting aside regular dates to do housework). Câu C (movie night) cũng thuộc "family traditions" chứ không riêng "attention to the child" nên có thể gây tranh luận; D là điều bài KHÔNG nói rõ nhất (bài nói "special times", không nói "housework") nên giữ khoá. Giáo viên nên xem lại.',
    'wr1: khoá Word đánh số lẫn (l, 5, 6, 7, 5, 9, 10, 11) -> đã chuẩn lại 1-8. Câu 4 chấp nhận "from/at an early age".',
    'ảnh trong Word: 6 ảnh đều là biểu tượng/mũi tên/nhiễu kích thước rất nhỏ (<=28px) nằm trong phần khoá, không phải hình minh hoạ đề bài nên không đưa vào bài.',
    'Word bộ này không có đề kiểm tra riêng nên không có trang "kiem-tra".',
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


# ======================= PHÁT ÂM (E1), TRỌNG ÂM (E2) =======================
put('ph1', [
    ('C', '<b>together</b> /təˈɡeðə/ (o = /ə/). grocery /ˈɡrəʊsəri/, homemaker /ˈhəʊmmeɪkə/, promotion /prəˈməʊʃn/ có o = /əʊ/.'),
    ('D', '<b>agreement</b> /əˈɡriːmənt/ (a = /ə/). gratitude /ˈɡrætɪtjuːd/, character /ˈkærəktə/, activate /ˈæktɪveɪt/ có a = /æ/.'),
    ('A', '<b>prepare</b> /prɪˈpeə/ (e = /ɪ/). strengthen /ˈstreŋkθn/, respect /rɪˈspekt/, special /ˈspeʃl/ có e = /e/.'),
    ('C', '<b>contribute</b> /kənˈtrɪbjuːt/ (u = /juː/). husband /ˈhʌzbənd/, rubbish /ˈrʌbɪʃ/, vulnerable /ˈvʌlnərəbl/ có u = /ʌ/.'),
    (['D', 'C'], '<b>finance</b> /ˈfaɪnæns/ (i = /aɪ/) khác benefit /ˈbenɪfɪt/, children /ˈtʃɪldrən/ (i = /ɪ/) – khoá Word = D. Lưu ý: finance cũng đọc /fɪˈnæns/ (khi đó <b>routine</b> /ruːˈtiːn/, i = /iː/, mới là từ khác) nên C cũng được chấp nhận.'),
    ('B', '<b>value</b> /ˈvæljuː/ (a = /æ/). playtime /ˈpleɪtaɪm/, grateful /ˈɡreɪtfl/, table /ˈteɪbl/ có a = /eɪ/.'),
    ('D', '<b>grandparents</b> /ˈɡrænpeərənts/ (a = /æ/). generation /ˌdʒenəˈreɪʃn/, grateful /ˈɡreɪtfl/, educate /ˈedʒukeɪt/ có a = /eɪ/.'),
])

put('ph2', [
    ('C', '<b>develop</b> /dɪˈveləp/ nhấn âm 2. grocery /ˈɡrəʊsəri/, character /ˈkærəktə/, homemaker /ˈhəʊmmeɪkə/ nhấn âm 1.'),
    ('A', '<b>spotlessly</b> /ˈspɒtləsli/ nhấn âm 1. experience /ɪkˈspɪəriəns/, society /səˈsaɪəti/, responsible /rɪˈspɒnsəbl/ nhấn âm 2.'),
    ('A', '<b>routine</b> /ruːˈtiːn/ nhấn âm 2. laundry /ˈlɔːndri/, household /ˈhaʊshəʊld/, picnic /ˈpɪknɪk/ nhấn âm 1.'),
    ('B', '<b>important</b> /ɪmˈpɔːtnt/ nhấn âm 2. similar /ˈsɪmələ/, atmosphere /ˈætməsfɪə/, breadwinner /ˈbredwɪnə/ nhấn âm 1.'),
])

# ======================= E3 – Từ vựng =======================
put('vg1', [
    ('B', 'family <b>values</b> = giá trị gia đình, dạy trẻ điều đúng sai.'),
    ('A', '<b>Putting out</b> the rubbish = đem rác ra ngoài (put out the rubbish); danh động từ làm chủ ngữ.'),
    ('B', '<b>Homemaker</b> = người nội trợ, làm việc ở nhà và chăm sóc gia đình.'),
    ('B', '<b>take the responsibility for</b> + V-ing = chịu trách nhiệm về…; chia ở hiện tại: takes.'),
    ('A', 'strengthen <b>family bonds</b> = củng cố sự gắn kết gia đình.'),
    ('A', '<b>prepare</b> dinner = chuẩn bị bữa tối (be preparing – đang làm).'),
    ('B', 'a man of strong <b>character</b> = người có tính cách mạnh mẽ, đáng tin cậy.'),
    ('D', 'the sole <b>breadwinner</b> = trụ cột duy nhất kiếm tiền nuôi gia đình (sau khi có con).'),
    ('A', 'bring great <b>benefits</b> to… = mang lại nhiều lợi ích cho…'),
    ('A', 'the main <b>breadwinner</b> = người kiếm tiền chính (làm hai công việc).'),
    ('A', 'kindness, responsibility là <b>family values</b> mà cha mẹ muốn dạy con.'),
    ('D', '<b>honest</b> = trung thực, không gian lận trong thi cử.'),
    ('B', '<b>encourage</b> sb to do sth = khuyến khích ai làm gì (tự suy nghĩ).'),
    ('B', '<b>divide</b> household chores equally = chia đều việc nhà.'),
    ('C', '<b>support</b> sb through difficult times = ủng hộ, giúp ai vượt qua thời kỳ khó khăn (hiện tại hoàn thành: has supported).'),
    ('D', 'main <b>responsibility</b> = trách nhiệm chính (trong nhà).'),
    ('D', 'family <b>bonds</b> = sự gắn kết gia đình, sẽ chặt chẽ hơn khi chia sẻ việc nhà.'),
    ('B', '<b>life skills</b> = kĩ năng sống (nấu ăn, chuẩn bị bữa ăn).'),
    ('B', 'shop for <b>groceries</b> = mua thực phẩm, tạp hoá ở siêu thị.'),
    ('C', '<b>respect</b> sb for sth = tôn trọng ai vì điều gì.'),
    ('B', '<b>earn</b> money = kiếm tiền (lend/borrow = cho/vay mượn; raise không đi với job to… ở nghĩa này).'),
    ('D', '<b>supportive</b> (adj) = hay giúp đỡ, đứng trước danh từ brother (a(n) + adj + N).'),
    ('C', '<b>heavy</b> lifting = việc mang vác nặng (collocation cố định).'),
    ('A', '<b>put</b> the rubbish out = đem rác ra ngoài; sau have to dùng động từ nguyên mẫu.'),
    ('B', 'do the <b>laundry</b> = giặt quần áo (do the washing-up = rửa bát).'),
    ('A', 'give sb full <b>support</b> for… = hoàn toàn ủng hộ ai về…'),
    ('B', 'shop for <b>groceries</b> = đi mua thực phẩm và đồ tạp hoá.'),
    ('B', 'high school <b>routines</b> = thói quen/nề nếp sinh hoạt ở trường cấp 3.'),
    ('A', 'do the <b>washing-up</b> = rửa bát đĩa (danh từ không đếm được, không thêm -s).'),
    ('B', '<b>homemaker</b> = người ở nhà nội trợ, không đi làm.'),
    ('A', 'do the <b>heavy lifting</b> = làm việc nặng; người con trai khoẻ đảm nhận.'),
    ('A', '<b>breadwinner</b> = trụ cột kiếm tiền; vế sau nói ông vẫn giúp vợ việc nhà.'),
    ('A', '<b>be responsible for</b> + V-ing = chịu trách nhiệm về; B, C sai cấu trúc nên D sai.'),
    ('C', 'do <b>the washing-up</b> = rửa bát (do the mess / do your bed / do the cook không dùng).'),
    ('D', '<b>put out</b> the rubbish = đem rác ra ngoài.'),
])

# ======================= E4 – Hiện tại đơn / tiếp diễn =======================
put('vg2', [
    ('C', '"yesterday evening" -> quá khứ đơn: <b>went</b>.'),
    ('A', '"at the moment" -> hiện tại tiếp diễn: <b>is reading</b>.'),
    ('C', '"at the moment" -> <b>I’m working</b> on the computer.'),
    ('A', 'Hành động đang diễn ra khi nói (while I…): <b>am working</b>.'),
    ('A', 'Phủ định hiện tại đơn, ngôi he: <b>doesn’t usually go</b> (trợ động từ + trạng từ tần suất + V nguyên mẫu).'),
    ('D', '"Every day" -> hiện tại đơn; trạng từ tần suất đứng trước động từ thường: <b>usually cleans</b>.'),
    ('A', '"Listen!" -> đang diễn ra; someone số ít: <b>is singing</b>.'),
    ('C', '"First thing in the morning" = thói quen -> hiện tại đơn: <b>have</b> (chủ ngữ I).'),
    ('A', '"at the moment" -> <b>is studying</b>.'),
    ('C', '"usually" -> hiện tại đơn: <b>go</b>.'),
    ('B', '"now" -> hiện tại tiếp diễn, friends số nhiều: <b>are preparing</b>.'),
    ('A', '"right now" -> tiếp diễn, All staff coi là số nhiều: <b>are attending</b>.'),
    ('A', '"Yesterday morning" -> quá khứ đơn: <b>got</b> up.'),
    ('C', 'Don’t make noise. I <b>am studying</b>. (hành động đang diễn ra)'),
    ('B', '"every day" -> ride (thói quen); "today" -> <b>am going</b> (tạm thời, đang diễn ra).'),
    ('A', 'Sự thật hiển nhiên -> hiện tại đơn: water <b>boils</b>.'),
    ('B', 'Câu hỏi đang diễn ra, Who là chủ ngữ số ít: Who <b>is playing</b> the guitar?'),
    ('C', '"often" -> goes (thói quen); "today ... at noon" -> <b>is going</b> (kế hoạch/đang diễn ra hôm nay).'),
    ('D', '"sometimes" -> hiện tại đơn, Bich số ít: <b>has</b>.'),
    ('B', '"at the moment" -> <b>Is she living</b> in Hue at the moment?'),
    ('A', '"often" -> wears; "today" -> <b>is wearing</b>.'),
    ('D', '"usually" -> visits; "now" -> <b>is staying</b>.'),
    ('D', 'Đang trong giờ học nên không chơi bóng: <b>aren’t playing</b> (they’re having class now).'),
    ('B', 'Câu mệnh lệnh yêu cầu giữ trật tự vì bố mẹ đang ngủ: <b>are sleeping</b>.'),
    ('C', '"Look!" -> đang diễn ra: Minh <b>is singing</b>.'),
    ('B', '"at the moment" -> <b>am doing</b>.'),
    ('C', 'Sự thật khoa học -> hiện tại đơn: water <b>boils</b>.'),
    ('A', '"four times a week" -> thói quen: Hoang <b>checks</b>.'),
    ('B', '"At the moment" -> cả hai vế tiếp diễn; "do homework" (không phải make): <b>is doing - is playing</b>.'),
    ('A', '"Hurry up" -> đang chờ: Other friends <b>are waiting</b> for us.'),
    ('C', '"now" -> are having; "usually" -> eat: <b>are having - eat</b>.'),
    ('D', 'Thói quen/đặc điểm, Ms. Kim số ít, phủ định: <b>doesn’t work</b>.'),
    ('A', '"usually" -> hiện tại đơn: Hoa <b>takes</b> charge of…'),
    ('A', '"every Sunday" -> hiện tại đơn: <b>goes</b>.'),
    ('D', '"now" -> hiện tại tiếp diễn, She số ít: <b>is checking</b>.'),
])

# ======================= E5 – Word formation =======================
put('vg3', [
    (['responsibility'], 'duty and <b>responsibility</b> (danh từ, sau "and" song song với "duty") ← responsible.'),
    (['gratitude'], 'express my <b>gratitude</b> (danh từ sau tính từ sở hữu my) ← grateful.'),
    (['strengthen'], 'help create jobs and <b>strengthen</b> the economy (động từ, song song với "create") ← strong.'),
    (['encouragement'], 'all the support and <b>encouragement</b> (danh từ song song với support) ← encourage.'),
    (['spotlessly'], 'cleans up <b>spotlessly</b> (trạng từ bổ nghĩa cho động từ) ← spotless.'),
])

# ======================= NGHE =======================
put('li1', [
    ('T', 'Script: "Changes in family life have made men\'s and women\'s roles <b>more alike than ever</b>".'),
    ('T', 'Script: "the wives are also responsible for the family finances… Men are not the sole breadwinners" -> cả hai cùng góp tài chính cho gia đình.'),
    ('T', 'Script (Recreation): "Both partners have <b>an equal chance and time</b> for their own interests".'),
    ('F', 'Script (Breadwinning): "Husband\'s and wife\'s careers are <b>equally important</b>" -> sự nghiệp của chồng KHÔNG kém quan trọng hơn.'),
    ('T', 'Script: "families that can keep to those four principles… become <b>happier</b> and the divorce rate is the lowest".'),
])

put_open('li2', [
    '<b>Mẫu:</b> They are not the only breadwinner in the family, and they get more involved in housework and parenting. (Script: "Men are not the sole breadwinners… much more involved in housework and parenting".)',
    '<b>Mẫu:</b> Both are responsible for family finances, home-making / housework, and parenting.',
    '<b>Mẫu:</b> The families become happier and the divorce rate amongst them is the lowest.<br><br><b>Audio script:</b> Today we\'ll discuss the changes in roles performed by men and women in the family. Changes in family life have made men\'s and women\'s roles more alike than ever as the wives are also responsible for the family finances. Family experts say the old notions of who does what in families may be more and more unclear. Men are not the sole breadwinners for the family like they used to be and they are becoming much more involved in housework and parenting. Because men\'s and women\'s roles in families have become more alike, for couples to balance their work and family life, perhaps, \'equally shared parenting\' is the best solution. \'Equally shared parenting\' means the \'conscious and purposeful sharing\' in four domains of life: 1. Child-raising: Both parents have equal responsibility to nurture and to take care of the children; 2. Breadwinning: Husband\'s and wife\'s careers are equally important; 3. Housework: The household chores should be equally divided between the wife and the husband; 4. Recreation: Both partners have an equal chance and time for their own interests, and of course, to be with each other. Experts have found out that families that can keep to those four principles of \'equally shared parenting\' become happier and the divorce rate is the lowest amongst them.',
])

# ======================= NÓI =======================
put('sp1', [
    ('B', '<b>I strongly believe that</b> = tôi tin chắc rằng… (đồng ý, khẳng định routines cần thiết).'),
    ('D', '<b>In my opinion</b>, … = theo ý kiến của tôi (nêu quan điểm cá nhân). In their opinion / In a nutshell không hợp ngữ cảnh.'),
    ('C', '<b>I believe that</b> parents should let children do homework by themselves (nêu quan điểm để con tự lập). "I don\'t think" + should sẽ làm nghĩa ngược lại.'),
    ('A', '<b>I suppose that</b> they can learn it later (cho rằng sau này học cũng được) – phù hợp ý "teens nên dành thời gian cho việc học"; "I doubt that" mâu thuẫn với vế sau.'),
])

put_open('sp2', [
    '<b>Bài mẫu:</b> I think children should do housework for a number of reasons. First, doing housework helps children develop some important life skills such as doing the laundry, cleaning the house or taking care of others. They will certainly need those skills in their lives later, when they start their own families. Second, children can learn to take responsibility when they do housework. They know that they have to do something even though they don\'t like to do it. So doing housework is really good for children and I believe that they should do it.',
])

# ======================= ĐỌC =======================
put('re1', [
    ('B', '<b>despite</b> + the fact that… = mặc dù (in spite of the fact that; "in spite" thiếu "of").'),
    ('A', 'people <b>aged</b> between 18 and 65 = những người ở độ tuổi từ 18 đến 65 (rút gọn mệnh đề bị động).'),
    ('C', 'women <b>estimated</b> their share to be… = phụ nữ ước tính phần việc của mình gần gấp đôi (estimate sth to be…).'),
    ('B', 'affected by <b>whether</b> the woman was working or not = liệu… hay không.'),
    ('D', 'should <b>be</b> shared = should + be + V3 (bị động).'),
    ('C', 'did the <b>remainder</b> = làm phần còn lại (danh từ sau "the").'),
    ('D', 'feel they are <b>unimportant</b> = cảm thấy mình không quan trọng/không được coi trọng.'),
    ('A', 'increase … <b>by</b> 14 hours = tăng thêm 14 giờ (by chỉ mức tăng).'),
    ('C', 'for men <b>the</b> amount is just 90 minutes (the amount đã xác định ở vế trước).'),
    ('A', 'unbalanced, <b>as</b> the man\'s share increases much less… = vì/bởi vì.'),
    ('B', 'inequality and <b>loss</b> of respect = sự mất đi sự tôn trọng (loss of respect).'),
    ('A', 'leads to <b>anxiety</b> and depression = danh từ song song với depression.'),
    ('D', 'The research even <b>describes</b> housework as thankless… = mô tả công việc nhà là bạc bẽo, không thoả mãn (describe … as).'),
])

put('re2', [
    ('A', 'Đoạn 1: "In Western, industrialized societies, the nuclear family ranks as the most common family type" -> in many industrialized countries.'),
    ('B', 'Đoạn 1: "In the single-parent family… a mother or a father heads the family alone" -> chỉ có một phụ huynh sống với con.'),
    ('A', 'Đoạn 2: "These complex families usually contain several generations… including grandparents, parents and children" -> ba thế hệ điển hình của gia đình mở rộng.'),
    ('D', 'Đoạn 2 nói về các gia đình phức hợp/mở rộng (extended family) gồm nhiều thế hệ và họ hàng.'),
    ('C', '<b>blended</b> family = gia đình được hình thành từ hai gia đình (tái hôn) ≈ <b>mixed</b> (pha trộn).'),
])

put('re3', [
    ('A', 'Đoạn 1: "Regular family meals are a great chance for everyone to chat about their day" -> chia sẻ hoạt động hằng ngày.'),
    ('C', 'EXCEPT: bài chỉ nói chia sẻ suy nghĩ, cảm xúc ở phần "one-on-one time" (không phải outdoor activities) -> C không đúng với hoạt động ngoài trời.'),
    ('D', 'EXCEPT: các việc A, B (đoạn 4), C (movie night) có trong bài; bài không nói "setting aside regular dates to do housework" -> D.'),
    ('B', 'Đoạn cuối: "Agreed household responsibilities give kids… the sense that they\'re making an important contribution to family life" -> make the family life better.'),
    ('C', 'Cả bài đưa ra nhiều lời khuyên (bữa ăn, hoạt động, thời gian riêng, truyền thống, việc nhà) để cải thiện quan hệ gia đình.'),
])

# ======================= VIẾT =======================
put('wr1', [
    (['mr thanh hates doing housework but he still cleans the house once a week', 'mr thanh hates to do housework but he still cleans the house once a week'],
     '<b>Mẫu:</b> Mr Thanh hates doing housework but he still cleans the house once a week. (hate + V-ing; hiện tại đơn; once a week)'),
    (['i am having a holiday with my family in mai chau now we spend our summer holidays here every year'],
     '<b>Mẫu:</b> I\'m having a holiday with my family in Mai Chau now. We spend our summer holidays here every year. (now -> tiếp diễn; every year -> đơn)'),
    (['it is important for children to learn some life skills at home', "it's important for children to learn some life skills at home"],
     '<b>Mẫu:</b> It\'s important for children to learn some life skills at home. (It is + adj + for sb + to V)'),
    (['parents have to teach their children to be honest and show respect to older people from an early age', 'parents have to teach their children to be honest and show respect to older people at an early age'],
     '<b>Mẫu:</b> Parents have to teach their children to be honest and show respect to older people from / at an early age.'),
    (['jane is thinking of applying for another job she thinks her present job is boring', 'jane is thinking of applying to another job she thinks her present job is boring'],
     '<b>Mẫu:</b> Jane is thinking of applying for another job. She thinks her present job is boring. (think of -> tiếp diễn; think = nghĩ rằng -> đơn)'),
    (['doing housework helps children learn to take care of themselves'],
     '<b>Mẫu:</b> Doing housework helps children learn to take care of themselves. (chủ ngữ V-ing số ít: helps)'),
    (['family routines are connected with children\'s health and academic achievement', 'family routines are connected to children\'s health and academic achievement'],
     '<b>Mẫu:</b> Family routines are connected with children\'s health and academic achievement.'),
    (['children should learn to choose the right kind of clothes for the right occasion', 'children should learn to choose the right kind of clothes on the right occasion'],
     '<b>Mẫu:</b> Children should learn to choose the right kind of clothes for the right occasion.'),
])

put_open('wr2', [
    '<b>Bài mẫu:</b> In my family, we have a few routines to follow, one of which is having breakfast together. Every morning, we get up at 6:00. My sister and I help my mum prepare breakfast. My mum often cooks rice, meat or fish and vegetables for breakfast. Sometimes, we have bread, eggs, and butter for a change. She says a big meal in the early morning will help us work or study better during the day. My dad gets up a bit later and helps with laying the table. At about 6:45, we all sit down and have the meal together. During breakfast, we talk about what each of us is going to do during the day. My parents sometimes give us some advice about what we should do at school. At 7:30, we all leave home for work or school. Having breakfast with my family every morning makes me feel closer to my parents and sister and helps me feel more prepared for the day.',
])
