# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Lớp 10 Unit 1 (Global Success) – Bộ BÀI TẬP LUYỆN TẬP.
Quy ước:
  mcq  : chữ cái 'A'-'D' (hoặc list nếu chấp nhận nhiều đáp án)
  fill : danh sách đáp án chấp nhận (1 ô)  hoặc {'blanks': [[...],[...]]} (nhiều ô)
Bộ này tự giải từng câu; sau đó đối chiếu với phần "ĐÁP ÁN CHI TIẾT" có sẵn ở cuối file Word. Các câu còn nghi vấn ghi ở GHI_CHU_RA_SOAT."""

GHI_CHU_RA_SOAT = [
    'Đối chiếu: đáp án tự giải khớp 100% khoá có sẵn cuối file Word (cả bài luyện tập, 15-minute và 45-minute test).',
    'rd1.4 (Children ___ grew up): khoá Word = who (D); "that" cũng đúng ngữ pháp khi chỉ người nên chấp nhận cả B và D.',
    'rd2.4: nguồn lỗi "young women to ___" (thừa "to"); đã sửa thành "young women ______". Đáp án B (used to believe…) theo khoá Word; đoạn văn chỉ nói phụ nữ "no longer feel the urge to get married fast". A sai vì bài nói higher education, không phải mọi cấp học.',
    't15.8: khoá Word = A (is thinking - visits). C (thinks - visits) cũng đúng ngữ pháp nhưng nghĩa "đang nghĩ đến mẹ nhưng hiếm khi thăm" hợp hơn; giáo viên xem lại.',
    't45.32: regulates ~ controls (A) theo khoá; manages (B) cũng gần nghĩa nhưng "regulate emotions" = kiểm soát cảm xúc.',
    't45.37: khoá Word = D (Just 5 minutes more); "I see" (C) cũng là câu đáp tự nhiên nên chấp nhận cả C và D.',
    'vb4.8: litter (B) theo khoá Word và theo định nghĩa trong phần từ vựng (mẩu rác nhỏ như lon, giấy); rubbish/garbage không hợp "collect … such as empty cans".',
    'gr1.1, gr1.4, gr1.10: nguồn đặt (động từ) sau chỗ trống nên khó ghép; đã dựng lại ô trống để khớp khoá Word (does this train leave / Do you like / is always coming). gr1.10 chấp nhận thêm "always comes" (đúng ngữ pháp, nhưng mất sắc thái phàn nàn).',
    'vb1.4: nguồn gạch chân sót chữ (encourag|e) – đã sửa thành encourage. t45.22: nguồn "makes children to create" (thừa "to" sau make); giữ nguyên đề, đáp án C không đổi. t45.23: nguồn "for example." – đã chỉnh dấu câu thành "for example,"; đáp án B (helps bringing → helps bring) không đổi.',
    'Đoạn văn rd2 thiếu dấu chấm cuối; đã bổ sung. Dấu nháy trong đề được thống nhất thành ’.',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ======================= A. PHONETICS =======================
put('pa1', [
    ('A', '<b>character</b> /ˈkærəktə/: ch = /k/. chores /tʃɔːz/, children /ˈtʃɪldrən/, check /tʃek/: ch = /tʃ/.'),
    ('B', '<b>create</b> /kriˈeɪt/: ea = /i/. bread /bred/, tread /tred/, threaten /ˈθretn/: ea = /e/.'),
    ('D', '<b>bond</b> /bɒnd/: o = /ɒ/. homemaker /ˈhəʊmmeɪkə/, clothes /kləʊðz/, close /kləʊz/: o = /əʊ/.'),
    ('C', '<b>connection</b> /kəˈnekʃn/: t = /ʃ/. teach /tiːtʃ/, teenager /ˈtiːneɪdʒə/, appreciate /əˈpriːʃieɪt/: t = /t/ (chữ t cuối của appreciate vẫn là /t/).'),
    ('A', '<b>waste</b> /weɪst/: a = /eɪ/. value /ˈvæljuː/, damage /ˈdæmɪdʒ/, gratitude /ˈɡrætɪtjuːd/: a = /æ/.'),
])
put('pa2', [
    ('D', '<b>afraid</b> /əˈfreɪd/ nhấn âm 2 (âm 1 là /ə/). household /ˈhaʊshəʊld/, family /ˈfæməli/, laundry /ˈlɔːndri/ nhấn âm 1.'),
    ('A', '<b>divide</b> /dɪˈvaɪd/ nhấn âm 2 (động từ 2 âm tiết, nguyên âm đôi /aɪ/). rubbish, heavy, equal nhấn âm 1.'),
    ('B', '<b>prepare</b> /prɪˈpeə/ nhấn âm 2 (động từ). manage /ˈmænɪdʒ/, housework /ˈhaʊswɜːk/ (danh từ ghép), breakfast /ˈbrekfəst/ nhấn âm 1.'),
    ('A', '<b>favourite</b> /ˈfeɪvərɪt/ nhấn âm 1. develop /dɪˈveləp/, encourage /ɪnˈkʌrɪdʒ/, important /ɪmˈpɔːtnt/ nhấn âm 2.'),
    ('A', '<b>experience</b> /ɪkˈspɪəriəns/ nhấn âm 2. gratitude /ˈɡrætɪtjuːd/, benefit /ˈbenɪfɪt/, honesty /ˈɒnɪsti/ nhấn âm 1.'),
])

# ======================= B. VOCABULARY =======================
put('vb1', [
    ('A', 'a <b>wealth</b> of = a large amount of → <b>abundance</b> (sự phong phú, dồi dào): "a wealth of life experiences" = nhiều kinh nghiệm sống.'),
    ('C', '<b>gratitude</b> (lòng biết ơn) ≈ <b>thankfulness</b> (sự biết ơn). approval = sự chấp thuận; honour = danh dự; responsibility = trách nhiệm.'),
    ('B', '<b>appreciate</b> (trân trọng, biết ơn) ≈ <b>be grateful for</b>. be responsible for = chịu trách nhiệm; take account of = cân nhắc; be useful for = có ích cho.'),
    ('D', '<b>encourage</b> (khuyến khích) ≈ <b>stimulate</b> (thúc đẩy, khích lệ). comfort = an ủi; respect = tôn trọng; appreciate = đánh giá cao.'),
    ('A', '<b>damage</b> (làm hư hại) ≈ <b>destroy</b> (phá hủy). lose = đánh mất; suffer = chịu đựng; gain = đạt được.'),
])
put('vb2', [
    ('C', '<b>necessary</b> (cần thiết) ↔ <b>nonessential</b> (không thiết yếu). certain, unavoidable, inevitable đều có nghĩa "không thể tránh khỏi, chắc chắn".'),
    ('A', '<b>valuable</b> (quý giá) ↔ <b>worthless</b> (vô giá trị). helpful, beneficial, precious đều mang nghĩa tích cực, gần nghĩa với valuable.'),
    ('D', '<b>carry on</b> (tiếp tục) ↔ <b>give up</b> (từ bỏ). put out = dập tắt/đổ (rác); go by = trôi qua; try on = thử (quần áo).'),
    ('C', '<b>recent</b> (gần đây) ↔ <b>ancient</b> (cổ xưa, xa xưa). up-to-date, modern, latest đều là các từ đồng nghĩa với recent.'),
    ('A', '<b>traditional</b> (truyền thống) ↔ <b>modern</b> (hiện đại). standard và conventional gần nghĩa với traditional; unusual (khác thường) không phải trái nghĩa.'),
])
put('vb3', [
    (['equally'], 'Cần <b>trạng từ</b> bổ nghĩa cho động từ "divide": equal → <b>equally</b> (chia đều, chia ngang nhau).'),
    (['responsibility'], 'Sau mạo từ "the" cần <b>danh từ</b>: "the responsibility of mothers and wives" (trách nhiệm của mẹ và vợ). Không dùng tính từ responsible.'),
    (['strengthen'], 'help + (to) V: "help strengthen family bonds" → <b>strengthen</b> (củng cố, làm vững mạnh) từ strong.'),
    (['spotlessly'], 'Cần <b>trạng từ</b> bổ nghĩa cho tính từ "clean": <b>spotlessly</b> clean = sạch không một vết nhơ.'),
    (['values'], '"Family ___ are ideas…": cần <b>danh từ số nhiều</b> (đi với "are") → family <b>values</b> (giá trị gia đình).'),
])
put('vb4', [
    ('C', 'do the <b>laundry</b> = giặt quần áo ("clothes are ready for the next morning"). heavy lifting = việc nặng; cooking/cleaning không liên quan đến quần áo.'),
    ('A', '<b>homemaker</b> = người nội trợ (quản lý nhà cửa, nuôi con thay vì đi kiếm tiền). breadwinner là người trụ cột kiếm tiền – ngược nghĩa.'),
    ('D', 'shop <b>for</b> sth = mua sắm cái gì (shop for groceries).'),
    ('C', '<b>respectable</b> (đáng kính, đứng đắn): "a respectable young woman from a good family". respectful = lễ phép (với người khác); respective = riêng từng người.'),
    ('B', 'help sb <b>with</b> sth = giúp ai việc gì (help her mother with the washing-up).'),
    ('A', 'have sb <b>pick up</b> sb = nhờ ai đón ai (have + O + V nguyên thể). put out = đổ/dập; grow up = lớn lên; carry on = tiếp tục.'),
    ('C', '<b>put out</b> the rubbish = đổ rác. put off = hoãn; put on = mặc vào; put up with = chịu đựng.'),
    ('B', '<b>litter</b> = rác nhỏ (lon, giấy…) vứt bừa bãi nơi công cộng – đúng với "empty cans, used papers". rubbish/garbage = đồ bỏ đi nói chung; waste = chất thải.'),
    ('B', 'show any <b>appreciation</b> for sth = tỏ lòng biết ơn/sự cảm kích. Sau "any" cần danh từ.'),
    ('C', 'be <b>good</b> for sb = tốt/có ích cho ai. useless = vô ích; responsible = chịu trách nhiệm; respective không hợp nghĩa.'),
    ('A', 'teach children to <b>show respect</b> to old people = dạy trẻ biết tôn trọng người già. take care phải đi với "of"; spend time/cheer up không hợp.'),
    ('D', '<b>In the end</b> = cuối cùng (kết quả sau khi cân nhắc: quyết định chọn trường đại học địa phương). At the end phải có "of…"; All in all = nhìn chung; Besides = ngoài ra.'),
    ('B', 'try <b>to V</b> = cố gắng làm gì ("have to try to finish their tasks" – vẫn phải cố hoàn thành). try V-ing = thử làm.'),
    ('A', 'strengthen the family <b>bonds</b> = củng cố gắn kết gia đình (collocation).'),
    ('C', 'take <b>responsibility</b> for sth = chịu trách nhiệm về việc gì.'),
])
put('vb5', [
    (['into'], 'divide sth <b>into</b> = chia cái gì thành các phần.'),
    (['for'], 'shop <b>for</b> sth = mua sắm cái gì.'),
    (['at'], 'be good <b>at</b> doing sth = giỏi làm gì.'),
    (['for'], 'take responsibility <b>for</b> sth = chịu trách nhiệm về việc gì.'),
    (['for'], 'be useful <b>for</b> sth/doing sth = có ích cho việc gì.'),
])
put('vb6', [
    ('A', '<b>Instead</b> → <b>Instead of</b> sitting… (instead of + V-ing = thay vì).'),
    ('C', 'ask sb <b>to do</b> sth: <b>pick up</b> → <b>to pick up</b> me from school.'),
    ('B', 'try <b>to V</b> = cố gắng (ở đây là cố giúp mẹ): <b>helping</b> → <b>to help</b>. (try V-ing = thử làm.)'),
    ('C', 'enjoy + <b>V-ing</b>: <b>do</b> → <b>doing</b> the housework.'),
    ('A', '<b>In all</b> → <b>All in all</b> (nhìn chung, tóm lại).'),
    ('C', 'take care <b>of</b> sb: bị động "to be taken care <b>of</b>" – thiếu giới từ <b>of</b>: <b>taken care</b> → <b>taken care of</b>.'),
    ('B', '"grow" ở đây cần là cụm <b>grew up</b> (lớn lên): <b>grew</b> → <b>grew up</b>.'),
    ('D', '<b>look at</b> (nhìn) → <b>look after</b> the family (chăm sóc gia đình).'),
    ('A', '<b>In the end</b> of → <b>At the end</b> of the day (vào cuối ngày). In the end = cuối cùng, không đi với "of".'),
    ('D', 'crash sth <b>into</b> sth = đâm cái gì vào cái gì: <b>to</b> → <b>into</b> a tree.'),
])

# ======================= C. GRAMMAR =======================
put('gr1', [
    (['does this train leave'], 'Lịch trình tàu xe → <b>hiện tại đơn</b>. Câu hỏi: What time + does + this train (số ít) + leave…? → <b>does this train leave</b>.'),
    (['have'], 'Có trạng từ tần suất "often", chủ ngữ I → hiện tại đơn: <b>have</b> breakfast.'),
    ({'blanks': [["doesn't cut", 'does not cut'], ["isn't", 'is not']]}, 'Nhận xét, đánh giá (hiện tại đơn). Chủ ngữ số ít: <b>doesn\'t cut</b>; tobe phủ định: <b>isn\'t</b> sharp enough.'),
    (['do you like'], 'Diễn tả sở thích → hiện tại đơn, chủ ngữ you: <b>Do you like</b> reading books?'),
    (['gets up'], 'Có "usually" (thói quen), chủ ngữ số ít "my mother" → <b>gets up</b>.'),
    ({'blanks': [['begins'], ['ends']]}, 'Lịch trình cố định (năm học) → hiện tại đơn, chủ ngữ số ít: <b>begins</b>, <b>ends</b>.'),
    (['is having'], 'Có "now" và "Don\'t call Mary now" → hành động đang xảy ra → <b>is having</b> (have an exam = có bài thi, dùng tiếp diễn được).'),
    (['is going'], '"next week" + kế hoạch đã đặt vé ("already booked") → hiện tại tiếp diễn chỉ tương lai: <b>is going</b>.'),
    (['is riding'], '"often goes… but today…" → hôm nay khác thói quen → hiện tại tiếp diễn: <b>is riding</b>.'),
    (['is always coming', 'always comes'], 'Có "always" + "makes his boss very angry" → phàn nàn: <b>is always coming</b> late (hiện tại tiếp diễn với always). "always comes" cũng đúng ngữ pháp nhưng không có sắc thái phàn nàn.'),
    (["isn't raining", 'is not raining'], '"now" → đang xảy ra: <b>isn\'t raining</b> (hiện tại tiếp diễn phủ định).'),
    (['is cooking'], '"Who … in the kitchen" – ai đang nấu ăn lúc này (Mary đang hỏi người trong bếp) → <b>is cooking</b>.'),
])

# ======================= D. SPEAKING =======================
put('sp1', [
    ('A', 'Lời mời: từ chối lịch sự → <b>I\'d love to but I\'m afraid I can\'t.</b> Các câu khác không trả lời đúng lời mời.'),
    ('B', 'Câu hỏi "Who is preparing dinner?" (hiện tại tiếp diễn, đang diễn ra) → <b>My mum is doing it.</b> (Mẹ mình đang nấu).'),
    ('A', 'Hỏi "Does your sister help…?" → trả lời Yes/No hiện tại đơn có lý do: <b>Definitely not. She is busy.</b> Yes, she will (sai thì); "No. She sometimes studies" không liên quan.'),
    ('C', 'Hỏi cách chia việc nhà → trả lời nêu phân công: <b>My mum cooks and I clean the house.</b>'),
    ('D', '"Does your mum…?" → trả lời cùng thì hiện tại đơn: <b>No, she doesn\'t.</b> (did/will sai thì; "No, she does" mâu thuẫn).'),
])

# ======================= E. READING =======================
put('rd1', [
    ('A', 'at all <b>costs</b> = bằng mọi giá (cụm cố định).'),
    ('C', 'no <b>room</b> for sth = không có chỗ/không cho phép điều gì ("little to no room for the child to negotiate").'),
    ('B', 'enforce <b>many</b> rules: rules là danh từ đếm được số nhiều → many (much/little/any không hợp).'),
    ('D', 'Mệnh đề quan hệ thay thế cho người "children" làm chủ ngữ: <b>who</b> grew up… (that cũng có thể dùng; which cho vật; whose + N).'),
    ('D', '"may cause poor outcomes <b>such as</b> increasing risks of anxiety…" = như là (liệt kê ví dụ về hậu quả).'),
    ('C', 'Câu sau đưa ví dụ cho "poor social skills" → <b>For example</b>.'),
    ('C', 'miss out on opportunities = bỏ lỡ cơ hội (cụm miss out on).'),
    ('A', '"Family patterns can be passed on, <b>including</b> parenting styles and childhood trauma" = bao gồm cả… (liệt kê một phần).'),
    ('B', '<b>approach</b> things differently = tiếp cận/giải quyết mọi việc theo cách khác.'),
    ('C', 'interact <b>with</b> sb = tương tác với ai.'),
])
put('rd2', [
    ('A', 'Cả bài nói về lý do con người <b>kết hôn muộn</b> (học cao, độc lập, tài chính…) → "Marriage can be postponed".'),
    ('B', '"many <b>young people</b> start living alone… As a result, they do not see the need to commit" → they = young people.'),
    ('B', 'run a home = <b>manage</b> (quản lý, điều hành một gia đình).'),
    ('B', '"Women in particular <b>no longer</b> feel the urge to get married fast" → trước đây từng tin phải lấy chồng sớm → used to believe they had to marry someone fast. A sai: bài chỉ nói higher education, và cho mọi giới.'),
    ('B', 'Bài nói tài chính là một nguyên nhân, nhưng KHÔNG nói "phần lớn mọi người không kết hôn vì đám cưới đắt" → B không đúng (NOT TRUE).'),
])

# ======================= 15-MINUTE TEST =======================
put('t15', [
    ('B', '"as a part of my job… a lot" → thói quen: hiện tại đơn, chủ ngữ I → <b>travel</b>.'),
    ('D', '"comes from Italy" (nguồn gốc – đơn) + "at the moment" → <b>is studying</b>.'),
    ('A', 'Khả năng/sự thật hiện tại (nói được tiếng Anh) → hiện tại đơn, chủ ngữ số ít: <b>speaks</b>.'),
    ('C', '"Don\'t bother me now" → đang xảy ra: <b>am writing</b> (chủ ngữ I).'),
    ('A', '"this week" (tạm thời) → <b>is sleeping</b>; "she is having her house painted" (đang nhờ sơn nhà) → <b>is having</b>. Have sth done dạng tiếp diễn.'),
    ('D', '"tomorrow morning" – kế hoạch → hiện tại tiếp diễn: <b>Why are you leaving</b> early tomorrow?'),
    ('B', '"In the afternoons" (thói quen), chủ ngữ they → <b>go – try</b>.'),
    ('A', 'Hiện tại tiếp diễn cho hành động đang diễn ra: <b>is thinking</b> about his mother; "hardly ever" → thói quen hiếm: <b>visits</b>.'),
    ('C', 'Lịch trình xe buýt → hiện tại đơn: <b>leaves – returns</b>.'),
    ('D', 'Kế hoạch đã sắp xếp trong tương lai ("tomorrow") → hiện tại tiếp diễn: <b>are meeting</b>.'),
    ('B', 'help sb <b>with</b> sth = giúp ai việc gì (help with the cooking).'),
    ('A', 'John <b>never stops</b> criticizing = lúc nào cũng chỉ trích → <b>always criticizes</b>. B/C trái nghĩa; D thiếu ý "liên tục" (đang chỉ trích).'),
    ('B', 'Jack đã tìm được việc ở siêu thị cho mùa hè này → <b>is working</b> in a supermarket this summer (hành động tạm thời, kế hoạch).'),
    ('D', 'Người kiếm tiền cho gia đình = <b>breadwinner</b> (người trụ cột).'),
    ('A', 'take out the rubbish = đổ rác (take out). turn up = bật to/xuất hiện; cut down = cắt giảm; crash into = đâm vào.'),
])

# ======================= 45-MINUTE TEST =======================
put('t45', [
    ('B', '<b>taking</b> /ˈteɪkɪŋ/: a = /eɪ/. damage /ˈdæmɪdʒ/, dad /dæd/, trash /træʃ/: a = /æ/.'),
    ('D', 'appre<b>c</b>iate có c = /ʃ/ (/əˈpriːʃieɪt/). create /kriˈeɪt/, care /keə/, encourage /ɪnˈkʌrɪdʒ/: c = /k/.'),
    ('C', '<b>divide</b> /dɪˈvaɪd/ nhấn âm 2. football /ˈfʊtbɔːl/, money /ˈmʌni/, children /ˈtʃɪldrən/ nhấn âm 1.'),
    ('B', '<b>important</b> /ɪmˈpɔːtnt/ nhấn âm 2. grocery /ˈɡrəʊsəri/, family /ˈfæməli/, homemaker /ˈhəʊmmeɪkə/ nhấn âm 1.'),
    ('A', '<b>responsible</b> /rɪˈspɒnsəbl/ nhấn âm 2. gratitude, character /ˈkærəktə/, benefit nhấn âm 1.'),
    ('C', '<b>appreciate</b> (trân trọng, biết ơn) ≈ <b>feel grateful for</b>.'),
    ('A', '<b>encourage</b> (khuyến khích) ≈ <b>stimulate</b>. dispirit = làm nản lòng; persuade = thuyết phục; prevent = ngăn cản.'),
    ('D', '<b>cheer up</b> (làm vui lên, động viên) ↔ <b>discourage</b> (làm nản lòng). inspire/enhance/brighten cùng nghĩa tích cực.'),
    ('B', '<b>basic</b> (cơ bản) ↔ <b>inessential</b> (không thiết yếu). fundamental, vital, elementary ≈ basic.'),
    ('A', '<b>taking care of</b> others = chăm sóc người khác. cleaning up = dọn dẹp; cheering up = cổ vũ; carrying on = tiếp tục.'),
    ('C', '"every morning" → thói quen: <b>shops</b>; "but today" → <b>is cooking</b> (hôm nay khác thường, đang ở nhà nấu ăn).'),
    ('B', 'Thói quen/xu hướng chung ("some women") → hiện tại đơn, chủ ngữ số nhiều: <b>don\'t go – stay</b>. (Câu A sai vì doesn\'t với "some women".)'),
    ('D', 'Cần <b>trạng từ</b> bổ nghĩa cho động từ "are divided": divided <b>equally</b> = chia đều.'),
    ('A', 'help (sb) <b>with</b> sth = giúp việc gì (the cooking).'),
    ('C', '<b>breadwinner</b> = người trụ cột kiếm tiền; "but he still helps his wife with the housework" – vế sau tương phản với vai trò kiếm tiền.'),
    ('B', 'Hai việc diễn ra đồng thời đang xảy ra: <b>are doing</b> … <b>is tidying up</b> (hiện tại tiếp diễn).'),
    ('D', 'Sau "the" cần danh từ: "the <b>responsibility</b> of wives and mothers only".'),
    ('A', 'try <b>to V</b> = cố gắng (have to try to finish their chores).'),
    ('B', '<b>In addition,</b> + mệnh đề = hơn nữa, ngoài ra. In the end = cuối cùng; Instead = thay vào đó; In addition to + N/V-ing (cần thêm danh từ).'),
    ('A', 'be <b>good for</b> sb = tốt cho ai ("I don\'t think playing too much is good for children").'),
    ('A', 'task is <b>putting out</b> the rubbish = nhiệm vụ là đổ rác (be + V-ing, chủ ngữ là task). make up/turn on/get up không hợp với "rubbish".'),
    ('C', 'help/make + O + V: sau "children to" cần động từ nguyên thể: <b>create</b> special moments. creation/creative/creativity là danh từ/tính từ.'),
    ('B', 'help + (to) V: <b>bringing</b> → <b>bring</b> (helps bring a lot of benefits).'),
    ('C', 'spend time + V-ing: <b>talk</b> → <b>talking</b> with him.'),
    ('B', 'have a <b>wealth</b> of sth (danh từ) = có nhiều cái gì; "wealthy" là tính từ nên sai: <b>a wealthy of</b> → <b>a wealth of</b>.'),
    ('B', 'We <b>tend</b> to be happier = chúng ta có xu hướng. intend to = có ý định; pretend = giả vờ; attend = tham dự.'),
    ('A', 'a sense of <b>belonging</b> = cảm giác thuộc về (gia đình). Các từ còn lại không hợp cụm.'),
    ('B', 'parent-child <b>bonds</b> = mối gắn kết cha mẹ – con cái (bonds là từ khóa của chủ đề). friendships/partnerships/fellowships không phù hợp.'),
    ('D', '"Changes in family structure, <b>such as</b> divorce or remarriage" = như là (nêu ví dụ). for instance không dùng trực tiếp trước danh từ không có dấu phẩy.'),
    ('C', 'The benefits are <b>numerous</b> (rất nhiều) và đóng góp cho sức khỏe tinh thần. tiny/small trái ý; essential không hợp "benefits are…" như vậy.'),
    ('B', 'Cả bài nói về ảnh hưởng của cha mẹ đối với con cái tuổi teen → "<b>Parents\' influence on children</b>".'),
    ('A', '<b>regulate</b> emotions = điều chỉnh, kiểm soát cảm xúc ≈ <b>controls</b>.'),
    ('D', '"Now\'s a good time for this" – ngay trước đó: "You can also <b>talk</b> more with your child about the differences between right and wrong" → this = talking to your child.'),
    ('A', 'Đoạn 3: bạn bè ảnh hưởng hành vi thường ngày (âm nhạc, quần áo); cha mẹ ảnh hưởng giá trị cơ bản và lựa chọn tương lai → A.'),
    ('C', 'Bài nêu cha mẹ ảnh hưởng hành vi, giá trị/niềm tin (beliefs), chọn học vấn (educational choices). "Passion" không được nhắc → <b>passion</b>.'),
    ('A', 'Hỏi "Are you interested in cooking?" → trả lời Yes/No: <b>Not really.</b> (không hẳn). Not at all quá gay gắt; I do, too sai; No problem không hợp.'),
    (['D', 'C'], 'Mary nói phải đi về nấu bữa tối → Peter đáp: <b>Just 5 minutes more.</b> (xin ở lại thêm chút nữa). "I see" (hiểu rồi) cũng là câu đáp tự nhiên nên chấp nhận.'),
    ('B', 'Câu gốc: trường không dạy đầy đủ (nguyên nhân) nên trẻ cần học ở nhà (kết quả) → <b>because</b> schools can\'t teach them fully. "and" chỉ nối thêm; "but" và "or" sai quan hệ.'),
    ('A', '"avoids cooking it" = không bao giờ nấu món cay vì chúng không thích → <b>never cooks</b> spicy food.'),
    ('D', '"has decided to shop… this afternoon" = đã quyết định, kế hoạch → hiện tại tiếp diễn chỉ tương lai: <b>is shopping</b>.'),
])
