# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Unit 1 (Tiếng Anh 11 Global Success) – Bộ BÀI TẬP BỔ TRỢ.
Quy ước:
  mcq  : chữ cái 'A'-'D'            tf : 'T' / 'F'
  fill : danh sách đáp án chấp nhận (1 ô)  hoặc {'blanks': [[...],[...]]} (nhiều ô)
  open : không chấm điểm, EXPLANATIONS chứa đáp án mẫu
Đáp án được SOẠN LẠI ĐỘC LẬP rồi đối chiếu với khoá trong file Word gốc; chỗ lệch được ghi trong BAO_CAO_RA_SOAT.md."""

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


def put_open(prefix, rows):
    for i, e in enumerate(rows, 1):
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ======================= A. PHONETIC – Exercise 2 (phát âm) =======================
put('ph2', [
    ('B', '<b>called</b> /kɔːld/ đuôi -ed đọc /d/ (sau âm hữu thanh). smoked /sməʊkt/, photographed /ˈfəʊtəɡrɑːft/, based /beɪst/ đều đọc /t/ (sau âm vô thanh).'),
    ('A', '<b>demanded</b> /dɪˈmɑːndɪd/ đuôi -ed đọc /ɪd/ (sau âm /d/). lived /lɪvd/, questioned /ˈkwestʃənd/, supposed /səˈpəʊzd/ đọc /d/.'),
    ('A', '<b>sugar</b> /ˈʃʊɡə/ chữ s đọc /ʃ/. consume /kənˈsjuːm/, muscle /ˈmʌsl/, obesity /əʊˈbiːsəti/ đều đọc /s/.'),
    ('C', '<b>diet</b> /ˈdaɪət/ chữ i đọc /aɪ/. vitamin /ˈvɪtəmɪn/, mineral /ˈmɪnərəl/, fitness /ˈfɪtnəs/ đọc /ɪ/.'),
    ('D', '<b>obesity</b> /əʊˈbiːsəti/ chữ e đọc /iː/. medicine /ˈmedsn/, energy /ˈenədʒi/, exercise /ˈeksəsaɪz/ đọc /e/.'),
    ('B', '<b>yoga</b> /ˈjəʊɡə/ chữ a (cuối) đọc /ə/. balanced /ˈbælənst/, fatty /ˈfæti/, natural /ˈnætʃrəl/ đọc /æ/.'),
    ('C', '<b>sugary</b> /ˈʃʊɡəri/ chữ g đọc /ɡ/. vegetable /ˈvedʒtəbl/, hygiene /ˈhaɪdʒiːn/, longevity /lɒnˈdʒevəti/ đọc /dʒ/.'),
    ('A', '<b>naked</b> /ˈneɪkɪd/ (tính từ) -ed đọc /ɪd/. looked, booked, hooked đọc /t/.'),
    ('C', '<b>developed</b> /dɪˈveləpt/ -ed đọc /t/ (sau /p/). concerned, raised, maintained đọc /d/.'),
    ('D', '<b>extinct</b> /ɪkˈstɪŋkt/ "ex" đọc /ɪk/. exactly /ɪɡˈzæktli/, exist /ɪɡˈzɪst/, exhaust /ɪɡˈzɔːst/ "ex" đọc /ɪɡz/.'),
    ('C', '<b>chemical</b> /ˈkemɪkl/ "ch" đọc /k/. change, poaching, achievement "ch" đọc /tʃ/.'),
    ('B', '<b>prohibit</b> /prəˈhɪbɪt/ chữ i đọc /ɪ/. survive /səˈvaɪv/, fertilizer /ˈfɜːtəlaɪzə/, environment /ɪnˈvaɪrənmənt/ chữ i đọc /aɪ/.'),
    ('D', '<b>fitness</b> /ˈfɪtnəs/ chữ e đọc /ə/ (âm yếu). healthy /ˈhelθi/, mental /ˈmentl/, strength /streŋθ/ chữ e đọc /e/.'),
    ('D', '<b>without</b> /wɪˈðaʊt/ "th" đọc /ð/. health, enthusiasm, strength "th" đọc /θ/.'),
    ('A', '<b>stopped</b> /stɒpt/ -ed đọc /t/. stayed, happened, changed đọc /d/.'),
    ('A', '<b>pieces</b> /ˈpiːsɪz/ đuôi -es đọc /ɪz/ (sau âm /s/). muscles, decades, labels đuôi -s đọc /z/.'),
    ('C', '<b>yoghurt</b> /ˈjɒɡət/ chữ u đọc /ə/ (hoặc /ɒ/ tuỳ cách ghi, khác /ʌ/). muscle /ˈmʌsl/, suffer /ˈsʌfə/, instruct /ɪnˈstrʌkt/ chữ u đọc /ʌ/.'),
    ('B', '<b>diet</b> /ˈdaɪət/ "ie" đọc /aɪə/. fresh /freʃ/, flesh /fleʃ/, exercise /ˈeksəsaɪz/ chữ e đọc /e/.'),
    ('A', '<b>yoga</b> /ˈjəʊɡə/ chữ a (cuối) đọc /ə/. fatty /ˈfæti/, balance /ˈbæləns/, habit /ˈhæbɪt/ chữ a đọc /æ/.'),
    ('A', '<b>ache</b> /eɪk/ "ch" đọc /k/. chip, choose, cheese "ch" đọc /tʃ/.'),
])

# ======================= A. PHONETIC – Exercise 3 (trọng âm) =======================
put('ph3', [
    ('D', '<b>polite</b> /pəˈlaɪt/ nhấn âm 2. nervous /ˈnɜːvəs/, healthy /ˈhelθi/, verbal /ˈvɜːbl/ nhấn âm 1.'),
    ('C', '<b>unhealthy</b> /ʌnˈhelθi/ nhấn âm 2 (tiền tố un- không nhận trọng âm). natural, dangerous, regular nhấn âm 1.'),
    ('D', '<b>properly</b> /ˈprɒpəli/ nhấn âm 1. infectious /ɪnˈfekʃəs/, essential /ɪˈsenʃl/, resistant /rɪˈzɪstənt/ nhấn âm 2.'),
    ('C', '<b>routine</b> /ruːˈtiːn/ nhấn âm 2. lifestyle /ˈlaɪfstaɪl/, frequent /ˈfriːkwənt/, balance /ˈbæləns/ nhấn âm 1.'),
    ('A', '<b>device</b> /dɪˈvaɪs/ nhấn âm 2. treatment /ˈtriːtmənt/, muscle /ˈmʌsl/, movement /ˈmuːvmənt/ nhấn âm 1.'),
    ('B', '<b>proper</b> /ˈprɒpə/ nhấn âm 1. replace /rɪˈpleɪs/, instruct /ɪnˈstrʌkt/, routine /ruːˈtiːn/ nhấn âm 2.'),
    ('D', '<b>treadmill</b> /ˈtredmɪl/ nhấn âm 1 (danh từ ghép). accept /əkˈsept/, contain /kənˈteɪn/, return /rɪˈtɜːn/ nhấn âm 2.'),
    ('C', '<b>position</b> /pəˈzɪʃn/ nhấn âm 2. regular /ˈreɡjələ/, energy /ˈenədʒi/, diagram /ˈdaɪəɡræm/ nhấn âm 1.'),
    ('D', '<b>demonstrate</b> /ˈdemənstreɪt/ nhấn âm 1. infectious /ɪnˈfekʃəs/, attention /əˈtenʃn/, position /pəˈzɪʃn/ nhấn âm 2.'),
    ('C', '<b>formal</b> /ˈfɔːml/ nhấn âm 1. asleep /əˈsliːp/, avoid /əˈvɔɪd/, remind /rɪˈmaɪnd/ nhấn âm 2.'),
    ('A', '<b>capture</b> /ˈkæptʃə/ nhấn âm 1. discharge /dɪsˈtʃɑːdʒ/, survive /səˈvaɪv/, exhaust /ɪɡˈzɔːst/ nhấn âm 2.'),
    ('D', '<b>infection</b> /ɪnˈfekʃn/ nhấn âm 2 (từ tận cùng -ion nhấn âm liền trước). nutrient, vitamin, mineral nhấn âm 1.'),
    ('C', '<b>friendliness</b> /ˈfrendlinəs/ nhấn âm 1. expression /ɪkˈspreʃn/, example /ɪɡˈzɑːmpl/, superior /suːˈpɪəriə/ nhấn âm 2.'),
    ('A', '<b>fertilizer</b> /ˈfɜːtəlaɪzə/ nhấn âm 1. development /dɪˈveləpmənt/, environment /ɪnˈvaɪrənmənt/, advertisement /ədˈvɜːtɪsmənt/ nhấn âm 2.'),
    ('B', '<b>prohibit</b> /prəˈhɪbɪt/ nhấn âm 2. exercise /ˈeksəsaɪz/, operate /ˈɒpəreɪt/, cultivate /ˈkʌltɪveɪt/ nhấn âm 1.'),
    ('C', '<b>amount</b> /əˈmaʊnt/ nhấn âm 2. healthy, problem /ˈprɒbləm/, mental /ˈmentl/ nhấn âm 1.'),
    ('A', '<b>acupuncture</b> /ˈækjupʌŋktʃə/ nhấn âm 1. longevity /lɒnˈdʒevəti/, environment, establishment /ɪˈstæblɪʃmənt/ nhấn âm 2.'),
    ('A', '<b>prevent</b> /prɪˈvent/ nhấn âm 2. injure /ˈɪndʒə/, balance /ˈbæləns/, suffer /ˈsʌfə/ nhấn âm 1.'),
    ('B', '<b>disease</b> /dɪˈziːz/ nhấn âm 2. fitness, treatment, headache /ˈhedeɪk/ nhấn âm 1.'),
    ('C', '<b>immune</b> /ɪˈmjuːn/ nhấn âm 2. longer /ˈlɒŋɡə/, fatal /ˈfeɪtl/, careful /ˈkeəfl/ nhấn âm 1.'),
])

# ======================= B. VOCABULARIES AND GRAMMARS =======================
put('vg1', [
    (['ensure'], 'Sau "make this change and ..." cần động từ nguyên mẫu song song: <b>ensure</b> a balanced diet = đảm bảo chế độ ăn cân đối.'),
    (['includes'], 'Chủ ngữ "A healthy lifestyle" số ít, thì hiện tại đơn → <b>includes</b> (bao gồm) taking exercise...'),
    (['give off'], '<b>give off</b> heat = toả nhiệt. Sau "seem to" dùng động từ nguyên mẫu.'),
    (['falling'], '"drivers <b>falling</b> asleep" – V-ing sau danh từ; <b>fall asleep</b> = ngủ gật.'),
    (['leads'], '"My father always <b>leads</b> a very active life" – chủ ngữ số ít, hiện tại đơn; <b>lead a ... life</b> = sống một cuộc sống...'),
    (['treat'], 'Sau "difficult to" dùng nguyên mẫu: <b>treat</b> patients = điều trị bệnh nhân.'),
    (['help'], 'Sau modal "can" dùng nguyên mẫu: can <b>help</b> you (to) relax = giúp bạn thư giãn.'),
    (['stay'], '<b>stay</b> healthy = giữ gìn sức khoẻ. "Eat right to stay healthy".'),
    (['work out', 'workout'], '<b>work out</b> (with weights) = tập luyện (với tạ); song song với "go jogging", chủ ngữ I → work out.'),
    (['give up'], '<b>give up</b> football = từ bỏ chơi bóng đá; sau "decided to" dùng nguyên mẫu.'),
])

put('vg2', [
    ('A', 'Cụm <b>COVID pandemic</b> = đại dịch COVID. complication (biến chứng), side effects (tác dụng phụ), enamel (men răng) không hợp nghĩa.'),
    ('A', '<b>advances in the treatment of cancer</b> = những tiến bộ trong việc điều trị ung thư.'),
    ('C', 'Sau tính từ "healthier" cần danh từ: <b>lifestyle</b> = lối sống. "lead a healthier lifestyle".'),
    ('D', 'Máy tính thực hiện các việc <b>repetitive</b> tasks = công việc lặp đi lặp lại.'),
    ('C', '<b>balanced diet</b> = chế độ ăn cân bằng (collocation).'),
    ('A', '<b>fit</b> = khoẻ mạnh, cân đối. "You must be very fit if you do so much running."'),
    ('B', 'Tập thể dục giúp tăng cường <b>muscles</b> (cơ bắp).'),
    ('D', '<b>active participation</b> = sự tham gia tích cực.'),
    ('B', '<b>cut down on</b> = cắt giảm. look at: nhìn; work out: tập luyện; suffer from: chịu đựng.'),
    ('A', '<b>antibiotics</b> (thuốc kháng sinh) dùng điều trị nhiễm trùng cổ họng (throat infection).'),
    ('D', '<b>give off</b> blue light = phát ra ánh sáng xanh.'),
    ('C', 'Collocation: <b>good health</b> = sức khoẻ tốt.'),
    ('C', '<b>develop</b> liver cancer = mắc/phát triển ung thư gan (develop a disease).'),
    ('B', 'Phụ nữ mang thai nên <b>avoid</b> (tránh) thực phẩm như trứng sống.'),
    ('C', '<b>bacteria</b> (vi khuẩn) – một số vi khuẩn giúp cơ thể chống bệnh.'),
    ('D', '<b>the spread of disease</b> = sự lây lan của bệnh.'),
    ('C', 'Sau trạng từ "highly" và trước danh từ "virus" cần tính từ: <b>infectious</b> (dễ lây).'),
    ('C', '<b>Life expectancy</b> = tuổi thọ trung bình.'),
    ('C', 'Nhiễm trùng ngực lan xuống phổi → <b>infection</b> (sự nhiễm trùng).'),
    ('A', '<b>well-balanced diet</b> = chế độ ăn cân đối.'),
    ('C', '<b>refuse treatment</b> = từ chối điều trị, nên "không còn gì để làm".'),
    ('D', '<b>physical strength</b> = sức mạnh thể chất.'),
    ('C', '<b>look for</b> = tìm kiếm.'),
    ('D', '<b>prevent somebody from doing sth</b> = ngăn ai làm gì.'),
    ('D', '<b>cut down on</b> = cắt giảm (đồ béo).'),
    ('A', '<b>treat ... with</b> antibiotics = điều trị bằng kháng sinh.'),
    ('C', '<b>suffer from</b> = chịu đựng/mắc (bệnh).'),
    ('B', '"since we left school" → hiện tại hoàn thành: <b>haven\'t met</b> (chủ ngữ We).'),
    ('C', '<b>since</b> + mệnh đề quá khứ/mốc thời gian: since he was a child.'),
    ('C', 'Có kết quả ở hiện tại ("now she feels exhausted") → hiện tại hoàn thành <b>has run</b>.'),
    ('C', '"since we <b>left</b> school" – sau since dùng quá khứ đơn (ten years ago là mốc quá khứ).'),
    ('D', '"all day yesterday" → quá khứ đơn: <b>wore</b> (wear – wore – worn).'),
    ('A', '"since I was born": hiện tại hoàn thành bị động, vật (the room) được sơn: <b>has been painted</b>.'),
    ('C', '"last year" → quá khứ đơn: <b>did – go</b> (sau did dùng V nguyên mẫu).'),
    ('C', 'Hiện tại hoàn thành + <b>recently</b> (gần đây): "Have you seen it recently?"'),
    ('D', '<b>just</b> đứng giữa has và V3: "has just broken his leg" (vừa mới gãy chân).'),
    ('B', '<b>Twenty years ago</b> + quá khứ (used to read). "ago" dùng với quá khứ đơn.'),
    ('A', '"once a long time ago" → was; "since" + hiện tại hoàn thành → <b>was / have not been</b>.'),
    ('B', 'Thói quen trong quá khứ: <b>used to go</b> (đi biển thường xuyên hơn).'),
    ('C', '"yesterday" → quá khứ đơn; chủ ngữ Nam số ít → <b>was</b>.'),
    ('B', '"For the past five years" → hiện tại hoàn thành; Iceland số ít → <b>has been</b>.'),
    ('D', 'Câu phủ định hiện tại hoàn thành, hành động chưa xảy ra: <b>yet</b> (cuối câu).'),
    ('A', '<b>for</b> + khoảng thời gian (2 hours).'),
    ('A', '"since" + mệnh đề quá khứ đơn: since he <b>finished</b> upper secondary school.'),
    ('D', '"Since ... learnt" → mệnh chính hiện tại hoàn thành: he <b>has posted</b> many stories.'),
    ('A', '"since the Internet was invented" → <b>has changed</b> (hiện tại hoàn thành).'),
    ('D', '"used to go swimming ... when he <b>was</b> young" – mệnh đề thời gian ở quá khứ.'),
    ('A', '"since + quá khứ đơn" → <b>has become</b> cleaner.'),
    ('D', 'Since the pandemic broke out → hiện tại hoàn thành: <b>have stopped</b> working (khớp với phần lý thuyết "SỰ KẾT HỢP THÌ").'),
    ('B', '"Since Lan moved to Paris" → <b>haven\'t heard</b> anything from her.'),
    ('B', '<b>for</b> + khoảng thời gian: "for a long time".'),
    ('A', '<b>already</b> đứng giữa have và V3: "have already drunk".'),
    ('B', '<b>yet</b> đứng cuối câu phủ định: "haven\'t done ... yet".'),
    ('A', '"after the 1970s" → mốc quá khứ → quá khứ đơn: <b>began</b>.'),
    ('B', '"yesterday" → quá khứ đơn phủ định: <b>didn\'t catch</b>.'),
])
# lưu ý: file Word gốc nhảy từ câu 50 sang 56 nên câu 56–60 được đánh số lại thành 51–55.

put('vg3', [
    ('B', '<b>infection</b> (sự nhiễm trùng) ≈ <b>disease</b> (bệnh).'),
    ('C', '<b>boosting</b> (thúc đẩy, làm tăng) ≈ <b>increasing</b>.'),
    ('D', '<b>exercise</b> (tập thể dục – động từ) ≈ <b>work out</b>.'),
    ('A', '<b>frequently</b> (thường xuyên) ≈ <b>regularly</b>.'),
    ('C', '<b>organisms</b> (sinh vật) ≈ <b>creatures</b> (sinh vật).'),
    ('B', '<b>life expectancy</b> (tuổi thọ) ≈ <b>longevity</b> (sự sống lâu).'),
    ('B', '<b>off colour</b> (hơi mệt, không khoẻ) ≈ <b>ill</b>.'),
    ('B', '<b>infectious</b> (dễ lây) ≈ <b>contagious</b>.'),
    ('D', '<b>lead to</b> (dẫn đến) ≈ <b>cause</b> (gây ra). result from = do ... mà ra (ngược chiều).'),
    ('B', '<b>compulsory</b> (bắt buộc) ≈ <b>required</b>. optional là trái nghĩa.'),
])

put('vg4', [
    ('D', '<b>dangerous</b> (nguy hiểm) >< <b>secure</b> (an toàn).'),
    ('A', '<b>contagious</b> (dễ lây) >< <b>harmless</b> (vô hại, không gây hại).'),
    ('A', '<b>active</b> (năng động) >< <b>inactive</b> (ít vận động).'),
    ('B', '<b>healthy</b> (khoẻ mạnh) >< <b>ill</b> (ốm). blue/down/upset đều nghĩa là buồn.'),
    ('A', '<b>serious</b> (nghiêm trọng) >< <b>trivial</b> (nhỏ nhặt, không đáng kể).'),
    ('B', '<b>give off</b> (phát ra) >< <b>absorb</b> (hấp thụ).'),
    ('B', '<b>rejections</b> (sự từ chối) >< <b>approval</b> (sự chấp thuận).'),
    ('C', '<b>weaken</b> (làm yếu) >< <b>strengthen</b> (làm mạnh).'),
    ('A', '<b>prevent</b> (ngăn cản) >< <b>allow</b> (cho phép).'),
    ('D', '<b>generally</b> (nói chung, rộng rãi) >< <b>particularly</b> (đặc biệt, cụ thể). Đây là câu có mức độ trái nghĩa tương đối.'),
])

put('vg5', [
    ('A', '"for hours" + hành động còn ở hiện tại ("he\'s having a great time") → <b>has been</b>.'),
    ('B', '"yesterday" → quá khứ đơn: <b>Did your friends buy</b>.'),
    ('B', '"six months ago" → quá khứ đơn: <b>started</b>.'),
    ('A', '"So far this week" (thời gian chưa kết thúc) → hiện tại hoàn thành: <b>we\'ve seen</b>.'),
    ('B', '"last week" → quá khứ đơn: <b>I talked</b>.'),
    ('A', '"recently" + có kết quả hiện tại (tiếng ồn) → <b>Have your neighbours bought</b>.'),
    ('A', '"this week" (chưa hết tuần) → hiện tại hoàn thành: <b>Have you seen</b>.'),
    ('A', '"for three years" + hiện tại vẫn quen nhau ("we\'re really good friends") → <b>We\'ve known</b>.'),
])

put('vg6', [
    (['have just finished'], '<b>just</b> + hiện tại hoàn thành: I have just finished my homework.'),
    (['has already written'], '<b>already</b> + hiện tại hoàn thành; Mary số ít → has already written.'),
    (['moved'], '"in 1994" là mốc quá khứ xác định → quá khứ đơn: moved.'),
    (['was'], '"two years ago" → quá khứ đơn: was.'),
    (['have not been'], '"so far" → hiện tại hoàn thành phủ định: have not (haven\'t) been.'),
    (['already travelled', 'already traveled'], 'Đã có sẵn "have" trong câu → điền <b>already travelled</b> (have already travelled to London).'),
    (['went'], '"Last week" → quá khứ đơn: went.'),
    (['have not bought'], '"yet" → hiện tại hoàn thành phủ định: have not bought.'),
    (['did they spend'], '"last summer" → quá khứ đơn, câu hỏi: Did they spend...?'),
    (['have you ever seen'], '<b>ever</b> + hiện tại hoàn thành: Have you ever seen a whale?'),
    (['lost'], '"Last night" → quá khứ đơn: lost.'),
    (['have lost'], 'Nhấn mạnh kết quả hiện tại (chìa khoá đang mất) → have lost.'),
    (['lived'], 'Hành động đã kết thúc ("she died when he was eight") → quá khứ đơn: lived.'),
    (['has been'], '"for ten years, and she still enjoys it" → còn kéo dài đến hiện tại → has been.'),
    (['did she go'], '"last month" → quá khứ đơn, câu hỏi How many times did she go...?'),
    (['have not cleaned up'], 'Có dấu hiệu ở hiện tại (sàn nhà bẩn) → have not (haven\'t) cleaned up. (Đáp án gốc ghi sai "clean up".)'),
    (['did you enjoy'], '"last night" → quá khứ đơn: Did you enjoy...?'),
    (['has just taken'], '<b>just</b> + hiện tại hoàn thành, someone số ít → has just taken.'),
    (['have known'], '<b>since</b> + mốc thời gian → hiện tại hoàn thành: have known.'),
    (['has ever met'], 'So sánh nhất + <b>ever</b> → hiện tại hoàn thành: the most kind-hearted people he has ever met.'),
    (['was'], '"yesterday" → quá khứ đơn: was.'),
    (['donated'], '"Last year" → quá khứ đơn: donated.'),
    (['have been'], '<b>since 1996</b> → hiện tại hoàn thành: have been.'),
    (['felt'], '"Last month" → quá khứ đơn: felt.'),
    (['have known'], '"for over fifteen years. They still get together" → hiện tại hoàn thành: have known.'),
])

put('vg7', [
    ('A', '"last week" → quá khứ đơn. Sửa: <b>have sent → sent</b>.'),
    ('D', '"for six years now" → hiện tại hoàn thành. Sửa: <b>lived → have lived</b>.'),
    ('C', '<b>by + V-ing</b> (bằng cách). Sửa: <b>from → by</b>.'),
    ('C', 'Trạng từ never đứng giữa have và V3, và "been to" + địa điểm. Sửa: <b>have been never → have never been</b>.'),
    ('C', '<b>treatment for</b> + bệnh. Sửa: <b>in → for</b>.'),
    ('C', '"too much of" thay cho cholesterols (số nhiều) → dùng "them". Sửa: <b>it → them</b>.'),
    ('D', '<b>at risk of + V-ing</b>. Sửa: <b>develop → developing</b>.'),
    ('B', 'Sau "be able to" dùng nguyên mẫu. Sửa: <b>fights → fight</b>.'),
    ('D', 'Câu tường thuật lùi thì: "I drank ..., I couldn\'t sleep". Sửa: <b>can\'t → couldn\'t</b>.'),
    ('C', 'Câu điều kiện loại 2: if + quá khứ đơn, would + V. Sửa: <b>have → had</b>.'),
])

put('vg8', [
    (['won a trophy for 20 years'], 'The last time ... ago → <b>hasn\'t + V3 + for + khoảng thời gian</b>.'),
    (['to be successful three years ago', 'being successful three years ago'], 'has been ... for 3 years → <b>started + to V/V-ing + 3 years ago</b>.'),
    (['won a home game since september'], 'last ... in September → hasn\'t won ... <b>since September</b> (since + mốc thời gian).'),
    (['scored a goal 2 months ago', 'scored a goal two months ago'], 'hasn\'t scored ... for 2 months → <b>last scored ... 2 months ago</b>.'),
    (['played in this stadium since 2010'], 'started to play in 2010 → <b>has played ... since 2010</b>.'),
    (['been the marketing manager for 4 months', 'been the marketing manager for four months'], 'became ... 4 months ago → <b>has been ... for 4 months</b>.'),
    (['visited a centre for children with cognitive impairments for two weeks', 'visited a center for children with cognitive impairments for two weeks', 'visited a centre for children with cognitive impairments for 2 weeks', 'visited a center for children with cognitive impairments for 2 weeks'], 'last visited ... two weeks ago → <b>hasn\'t visited ... for two weeks</b>.'),
    (['been injured for three weeks', 'been injured for 3 weeks'], 'got injured three weeks ago and still → <b>has been injured for three weeks</b> (hiện tại hoàn thành bị động).'),
    (['taught english in ho chi minh city since 2018'], 'started teaching in 2018 → <b>has taught ... since 2018</b>.'),
    (['met me for 5 months', 'met me for five months'], 'The last time he met me was 5 months ago → <b>hasn\'t met me for 5 months</b>.'),
    (['met for a long time'], 'It is a long time since we last met → <b>haven\'t met for a long time</b>.'),
    (['have you had this computer'], 'When did you have...? = <b>How long have you had...?</b>'),
    (['had such a delicious meal before'], 'This is the first time + have/has V3 → <b>haven\'t + V3 + before</b>.'),
    (['time i went to work was a month ago', 'time i went to work was 1 month ago'], 'haven\'t gone for a month → <b>The last time I went ... was a month ago</b>.'),
    (['5 days since i last talked to him', 'five days since i last talked to him'], 'haven\'t talked for 5 days → <b>It is 5 days since I last talked to him</b>.'),
    (['have not celebrated christmas for 2 years', 'have not celebrated christmas for two years'], 'last celebrated 2 years ago → <b>haven\'t celebrated ... for 2 years</b>.'),
    (['time linda had her teeth checked was last year'], 'hasn\'t had ... since last year → <b>The last time Linda had her teeth checked was last year</b>.'),
    (['has collected stamps since 2015'], 'began to collect in 2015 → <b>has collected ... since 2015</b>.'),
    (['long is it since they opened this shopping center', 'long is it since they opened this shopping centre', 'long ago did they start opening this shopping center', 'long ago did they start opening this shopping centre'], 'When did they start...? = <b>How long is it since + S + V2?</b> (hoặc How long ago did they start...?).'),
    (['i went to the zoo was over a year ago'], 'haven\'t been to the zoo for over a year → <b>The last time I went to the zoo was over a year ago</b>.'),
])

# ======================= LISTENING =======================
put('li1', [
    ('F', 'Bài nghe nói về <b>lối sống lành mạnh</b> ("A Healthy Lifestyle"); rugby chỉ được nhắc như ví dụ về môn thể thao.'),
    ('T', 'Script: "It\'s important to eat a good amount of <b>fruits and vegetables</b>."'),
    ('T', 'Script: "You should also <b>avoid junk foods and sweets</b>." (một chút thỉnh thoảng thì không sao).'),
    ('T', 'Script: "Being active is also important" – các thói quen giúp "live longer".'),
    ('T', 'Script: "You can do yoga or dance… It doesn\'t matter what activity you do" → yoga hay rugby đều giúp có lối sống lành mạnh.'),
])

# ======================= SPEAKING =======================
put('sp1', [
    ('B', 'Hỏi lý do đánh răng 2 lần/ngày → "To prevent plaque on your teeth" (ngăn mảng bám).'),
    ('B', 'Hỏi "What\'s wrong with toothpicks?" → "They can damage your teeth at the base" (nêu tác hại).'),
    ('A', 'Hỏi lợi ích của tập thể dục → "It helps to reduce cholesterol level."'),
    ('A', 'Hỏi nên ăn gì nhiều hơn → "More fruit and vegetables, less sugar, salt."'),
    ('B', 'Hỏi cách giữ lạc quan, vui vẻ → "Control your anger and do yoga."'),
    ('A', '"Each food item has a nutrition label!" → "It tells you what\'s inside the food." (giải thích nhãn dinh dưỡng).'),
    ('B', 'Hỏi cách làm tươi mới đầu óc → "You should rest and read a book."'),
    ('A', 'A không thấy lợi ích → B phản hồi hợp lý: "It\'s good for our immune system." (b "Anything is good..." sai ý).'),
    ('A', 'Hỏi có dùng thuốc nam được không → "It\'s a good choice for minor illnesses."'),
    ('B', 'Hỏi có nên uống sữa nóng trước khi ngủ → "Many people do so, but we\'re not sure." (a – uống cà phê – không tốt cho giấc ngủ).'),
])

put('sp2', [
    ({'blanks': [['stand'], ['stretch']]}, '"First, <b>stand</b> up straight and <b>stretch</b> your arms above your head."'),
    (['point'], '<b>Point</b> to the ceiling = chỉ lên trần nhà.'),
    (['look'], '"Look up, <b>look</b> down." = nhìn lên, rồi nhìn xuống.'),
    (['slowly'], '"Next, <b>slowly</b> turn your head from side to side." – trạng từ bổ nghĩa cho động từ turn.'),
    (['touch'], '"Now <b>touch</b> your toes." = chạm vào các ngón chân.'),
    (['finally'], '"<b>Finally</b>, sit down on the floor." – từ nối chỉ bước cuối cùng.'),
])

put('sp3', [
    ('D', 'Đề nghị giúp xách vali → từ chối lịch sự: "No, I can manage them myself."'),
    ('B', '"Let me drive you home." → "Don\'t worry. I\'m all right." (từ chối lịch sự).'),
    ('A', '"Would you mind sending...?" → đồng ý: "Sure, I\'ll do it now." (Would you mind + V-ing: trả lời Sure/Not at all).'),
    ('B', '"Do you need any help?" → "No, thanks. I\'m strong enough to lift this box."'),
    ('B', 'Đề nghị gọi taxi → chấp nhận: "Yes, please, if it does not bother." Lưu ý: phương án D cũng là lời đáp lịch sự, đáp án gốc chọn B.'),
    ('C', '"Do you want me to turn up the heater?" → "No, it\'s quite warm here."'),
    ('C', '"Let me give you a lift home." → chấp nhận lịch sự: "If you don\'t mind."'),
    ('D', '"Can I carry these suitcases...?" → "Can you? That\'s very kind." (chấp nhận, cảm ơn).'),
    ('C', '"Shall I wait for you?" → "No, don\'t bother." (không cần đâu).'),
    ('B', '"Would you like me to send this package for you?" → "Yes, please, if you don\'t mind."'),
])

# ======================= READING =======================
put('re1a', [
    ('C', '<b>immensely popular</b> = cực kỳ phổ biến (immensely: vô cùng).'),
    ('D', '<b>thanks to</b> + danh từ = nhờ có (the quick thinking...). due to / despite có nghĩa không phù hợp.'),
    ('A', 'Đại từ quan hệ thay cho "one cassette tape" (vật) → <b>which</b> was full of Latin music.'),
    ('B', '<b>fed up with</b> = chán ngán. "people who were fed up with working out" → họ thích Zumba hơn.'),
    ('C', '<b>another</b> + danh từ số ít đếm được: "just another fitness fad" (lại thêm một trào lưu).'),
])
put('re1b', [
    ('D', '<b>prescribed drugs</b> = thuốc kê đơn (được bác sĩ kê).'),
    ('B', 'Mệnh đề không xác định, bổ nghĩa cho cả vế trước: ", <b>which</b> would require about 40,000 pills each".'),
    ('C', '<b>suffer from</b> arthritis and diabetes = mắc bệnh viêm khớp và tiểu đường.'),
    ('A', 'Hai vế đối lập: "asthma... when young, <b>but</b> enjoys good health until 50s".'),
    ('C', '<b>other</b> + danh từ số nhiều: other personal objects and documents.'),
])
put('re2a', [
    ('B', 'Cả bài đưa ra các lời khuyên (snacks, nấu ăn tại nhà) → ý chính: <b>Tips for healthy eating</b>.'),
    ('B', '<b>flavour</b> = hương vị ≈ <b>taste</b>.'),
    ('B', 'Đoạn "Healthy Snacks" khuyên ăn trái cây tươi → có thể suy ra chuối, cam là món ăn vặt lành mạnh. Các ý khác không được nói tới.'),
    ('C', '"then you will know exactly what you are eating" → <b>you know exactly what is included in the dishes</b>.'),
    ('D', '"use herbs and spices to give your dishes more flavour" → <b>Herbs and spices may make your dishes better</b>.'),
])
put('re2b', [
    ('D', 'Bài nói về bản chất và cách hoạt động của virus → <b>Understanding Viruses</b>.'),
    ('A', '<b>noxious</b> (độc hại, hôi thối gây bệnh) ≈ <b>deadly</b> trong các lựa chọn.'),
    ('C', 'Đoạn 2: virus quá nhỏ không thấy bằng kính hiển vi thường và "show no traces of biological activity by themselves".'),
    ('A', '"Unlike bacteria, <u>they</u> are not living agents" → they = <b>viruses</b>.'),
    ('C', 'Đoạn 3: "They are parasites, requiring human, animal, or plant cells to live" → virus giống ký sinh trùng cần vật chủ.'),
])
put('re3', [
    ('F', 'Bài viết chỉ nói "<b>In China</b>, it is believed..." → không phải "nhiều người trên thế giới".'),
    ('T', '"fall-related injuries are the leading cause of death from injury and disability among older adults".'),
    ('T', 'Thái cực quyền chậm, chuyển trọng tâm → "many have long assumed it helps improve balance and reduce fall frequency".'),
    ('F', 'Chỉ "54% of the subjects" cho biết tự tin hơn nhờ cải thiện thăng bằng, không phải tất cả.'),
    ('T', '"After just six weeks, statistically significant improvements were observed..." và tiếp tục tăng sau 12 tuần.'),
    ('F', '"one cannot directly point to studies showing a reduction in stress" → không có nghiên cứu trực tiếp chứng minh.'),
])
put_open('re4', [
    'The problem is that they get <b>less sleep than they need</b> (do bài tập và nghĩa vụ xã hội, ngủ muộn nhưng phải dậy sớm).',
    'They should <b>drink plenty of water</b> and eat a balance of <b>protein, whole grains, fruit and vegetables</b> every day, and not skip breakfast.',
    'Because physical activity <b>releases endorphins</b> – a chemical the body produces – which gives us a good feeling.',
    'It helps <b>build a strong body and mind</b>, helps <b>manage moods</b> and improves our overall <b>well-being</b>. (Đáp án gốc lặp lại câu 3; đây là đáp án mẫu đã chỉnh.)',
    'We can <b>talk about what is happening to us</b> instead of dealing with problems alone.',
    'It is <b>part of having balance in our life</b> (laugh, have fun, be with people who make us feel good).',
])

# ======================= WRITING =======================
put('wr1', [
    ('4', 'Câu <b>a</b> (hỏi có cần mang gì không) đặt cuối – lời đề nghị bổ sung sau khi đã xác nhận tham dự. Thứ tự đúng: d → c → b → a.'),
    ('3', 'Câu <b>b</b> (rất vui, hẹn gặp ở hội trường lúc 7 giờ) – xác nhận chi tiết, đứng sau lời cảm ơn và lời mong chờ.'),
    ('2', 'Câu <b>c</b> (We are looking forward to the celebration) – bày tỏ mong chờ, sau lời cảm ơn.'),
    ('1', 'Câu <b>d</b> (Thank you for the kind invitation...) – mở đầu bằng lời cảm ơn lời mời.'),
])
put_open('wr2', [
    'I am <b>happy to receive</b> your invitation to the Christmas party on December 24th at 7.00 pm.',
    'I am <b>glad to inform</b> you that I would be <b>delighted to join</b> the party at the specified time.',
    'I will <b>make sure that I am present</b> there on the scheduled date and time.',
    'I am <b>looking forward to</b> an enjoyable evening with our old friends.',
    '<b>Merry Christmas</b> and best wishes to you and your family.',
])
put_open('wr3', [
    'A long and healthy life is something that many people aspire to. <b>Proper nutrition, regular exercise and enough sleep</b> keep our body healthy, while <b>managing stress, building strong relationships</b> and doing meaningful activities support our mental well-being. Avoiding harmful habits such as <b>smoking and drinking too much</b> also plays an important role. Although nothing is guaranteed, taking care of ourselves both physically and mentally can increase our chances of living a fulfilling life for many years. <i>(Bài mẫu tham khảo; bản gốc dài hơn 100 từ, có thể rút gọn.)</i>',
])

# ======================= BÀI KIỂM TRA (40 câu) =======================
put('kt', [
    ('C', '<b>organism</b> /ˈɔːɡənɪzəm/: chữ a đọc /ə/. antibiotic /ˌæntibaɪˈɒtɪk/, bacteria /bækˈtɪəriə/, examine /ɪɡˈzæmɪn/: chữ a đọc /æ/.'),
    ('A', '<b>germ</b> /dʒɜːm/: chữ e đọc /ɜː/. spread /spred/, regular /ˈreɡjələ/, recipe /ˈresəpi/: chữ e đọc /e/.'),
    ('B', '<b>disease</b> /dɪˈziːz/: chữ s đọc /z/. fitness, illness, press-up: đọc /s/.'),
    ('B', '<b>poisoning</b> /ˈpɔɪzənɪŋ/ nhấn âm 1. examine /ɪɡˈzæmɪn/, bacteria /bækˈtɪəriə/, infection /ɪnˈfekʃn/ nhấn âm 2.'),
    ('D', '<b>organism</b> /ˈɔːɡənɪzəm/ nhấn âm 1. diameter /daɪˈæmɪtə/, expectancy /ɪkˈspektənsi/, ingredient /ɪnˈɡriːdiənt/ nhấn âm 2.'),
    ('D', '<b>life expectancy</b> = tuổi thọ trung bình. story: câu chuyện; membership: tư cách thành viên; history: lịch sử.'),
    ('A', '<b>balanced diet</b> = chế độ ăn cân đối, đi cùng "taking exercise". sensitive/poor/unhealthy không hợp nghĩa "lead a healthy life".'),
    ('C', '<b>active lifestyle</b> = lối sống năng động. life insurance (bảo hiểm nhân thọ), life cycle (vòng đời), life line (mạch sống) không hợp nghĩa.'),
    ('B', 'Tắm nước nóng giúp thư giãn <b>muscles</b> (cơ bắp) đau nhức; các bộ phận khác (mouth, knees, elbows) không phù hợp bằng.'),
    ('A', '<b>keep fit</b> = giữ gìn vóc dáng/sức khoẻ (collocation).'),
    ('B', '<b>treatment for a cold</b> = cách điều trị cảm lạnh. Nghĩa cả câu: cách điều trị tốt nhất là nghỉ ngơi và uống nhiều nước.'),
    ('D', 'Sau "many health" cần danh từ số nhiều: <b>benefits</b> = lợi ích sức khoẻ. (health care/issues/needs không hợp nghĩa "an active lifestyle has many ...").'),
    ('A', 'Sau tính từ sở hữu "his great" cần danh từ: <b>strength</b> (sức mạnh). powerful là tính từ.'),
    ('C', 'Trước danh từ "tasks" cần tính từ: <b>repetitive</b> (lặp đi lặp lại) – washing and ironing.'),
    ('A', '<b>spend + thời gian + V-ing</b>: spend an hour every day <b>working out</b> in the gym.'),
    ('A', '<b>recover</b> (hồi phục) ≈ <b>get well</b>. get on: lên xe/hoà thuận; get up: dậy; get in: vào.'),
    ('D', '<b>warn</b> (cảnh báo) ≈ <b>caution</b> → cautioned. shouted: la hét; threatened: đe doạ; punished: phạt.'),
    ('C', '<b>common</b> (phổ biến) >< <b>infrequent</b> (hiếm gặp). normal là đồng nghĩa nên sai.'),
    ('C', 'Đề yêu cầu "OPPOSITE" nhưng các phương án không có từ trái nghĩa của <b>intake</b>; <b>consumption</b> (lượng tiêu thụ) là từ gần nghĩa nhất. Đề gốc có thể sai nhãn → xem BAO_CAO_RA_SOAT.'),
    ('B', 'Hỏi "Do you do any sports?" → "I used to, but now I don\'t. I\'m too busy." (trả lời trực tiếp). Các phương án khác lạc đề.'),
    ('C', 'Hỏi "What do people do to keep fit?" → "They combine exercising and having a balanced diet." (trả lời đúng câu hỏi).'),
    ('B', 'Mệnh đề quan hệ không xác định thay cho "their diet" (vật): ", <b>which</b> is often high in sugars and fats".'),
    ('C', '<b>glue ... to</b> the television = dán mắt vào tivi (glued to).'),
    ('A', '<b>hectic lifestyles</b> = lối sống bận rộn, hối hả – ngăn ta dành thời gian giữ dáng.'),
    ('C', 'Đồ ăn tiện lợi "saves time but is often <b>unhealthy</b>" (tiết kiệm thời gian nhưng thường không tốt cho sức khoẻ) – vế đối lập với "but".'),
    ('B', '<b>be responsible for</b> = là nguyên nhân gây ra (many health problems).'),
    ('A', 'Cả bài nói về cuộc tranh luận quanh chạy chân trần và các lợi ích có thể có; đoạn 3 liệt kê lợi ích → <b>The benefits of barefoot running</b>.'),
    ('C', '"Some <b>athletes</b> say ...; <u>others</u> claim ..." → others = athletes (những vận động viên khác).'),
    ('B', '"Opponents ... say that there is no scientific or medical proof that barefoot running is safer or better" → chưa được chứng minh là hiệu quả hơn.'),
    ('B', '<b>suffer</b> (leg injuries) ≈ <b>endure</b> (chịu đựng, trải qua).'),
    ('A', 'Đoạn 3: strengthens muscles, improves balance, reduces shock, makes some runners faster. "relaxes the feet" <b>không</b> được nhắc tới.'),
    ('D', 'Lỗi ở <b>outlook</b>. Thành ngữ đúng: <b>be on the lookout for</b> = cảnh giác với.'),
    ('A', 'Lỗi ở <b>communicative</b> (giỏi giao tiếp). Từ đúng: <b>contagious / infectious</b> (dễ lây).'),
    (['studied english since they were in grade 2', 'learnt english since they were in grade 2', 'learned english since they were in grade 2'], 'started ... when they were in grade 2 → <b>have studied English since they were in grade 2</b>.'),
    (['been abroad before'], 'This is the first time + hiện tại hoàn thành → <b>haven\'t been abroad before</b>.'),
    (['met my aunt when i was 10 years old'], 'haven\'t met ... since I was 10 → <b>last met my aunt when I was 10 years old</b>.'),
    (['seen her parents for a long time'], 'It is a long time since she last saw her parents → <b>hasn\'t seen her parents for a long time</b>.'),
    (['written to each other for five years', 'written to each other for 5 years'], 'last wrote five years ago → <b>haven\'t written to each other for five years</b>.'),
    (['learnt english since he was in grade 6', 'learned english since he was in grade 6'], 'started to learn when he was in grade 6 → <b>has learnt English since he was in grade 6</b>.'),
    (['visited the museum three months ago', 'visited the museum 3 months ago'], 'haven\'t visited for three months → <b>last visited the museum three months ago</b>.'),
])
