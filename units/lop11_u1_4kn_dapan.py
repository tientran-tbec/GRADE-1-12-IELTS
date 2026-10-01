# -*- coding: utf-8 -*-
"""Đáp án + giải thích – Unit 1 – Bộ BÀI TẬP 4 KỸ NĂNG (Tiếng Anh 11 Global Success).
Phần Nghe (li1, li2): CHƯA có transcript/audio xử lý -> không có ANS (hiển thị 'đáp án đang cập nhật')."""
ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ---------------- PHÁT ÂM ----------------
put('pr1', [
    ('D', '<b>label</b> /ˈleɪbl/: a đọc /eɪ/. habit /ˈhæbɪt/, balance /ˈbæləns/, examine /ɪɡˈzæmɪn/: a đọc /æ/.'),
    ('C', '<b>give</b> /ɡɪv/: i đọc /ɪ/. micron /ˈmaɪkrɒn/, diet /ˈdaɪət/, diameter /daɪˈæmɪtə/: i đọc /aɪ/.'),
    ('A', '<b>full</b> /fʊl/: u đọc /ʊ/. cut, suffer, muscle: u đọc /ʌ/.'),
    ('C', '<b>strength</b> /streŋθ/: e đọc /e/. Ba từ còn lại (energy /ˈenədʒi/ là /e/ nhưng treatment, nutrient có âm yếu /ə/) – xem ghi chú trong báo cáo rà soát: câu này cần giáo viên xác nhận lại.'),
    ('D', '<b>germ</b> /dʒɜːm/: e đọc /ɜː/. expectancy /ɪkˈspektənsi/, repetitive /rɪˈpetətɪv/, fitness /ˈfɪtnəs/: e đọc /ɪ/, /e/, /ə/.'),
    ('B', '<b>squat</b> /skwɒt/: a đọc /ɒ/. take, stay, replace: a đọc /eɪ/.'),
    ('B', '<b>work</b> /wɜːk/: o đọc /ɜː/. spot, from, antibiotic: o đọc /ɒ/.'),
    ('A', '<b>ingredient</b> /ɪnˈɡriːdiənt/: e đọc /iː/. strength, infectious, exercise: e đọc /e/.'),
    ('A', '<b>yoghurt</b> /ˈjɒɡət/: h là âm câm. healthy, holiday, human: h đọc /h/.'),
    ('C', '<b>range</b> /reɪndʒ/: a đọc /eɪ/. animal, bacteria, active: a đọc /æ/.'),
])
put('pr2', [
    ('A', '<b>examine</b> /ɪɡˈzæmɪn/ nhấn âm 2. diet, energy, active nhấn âm 1.'),
    ('D', '<b>expectancy</b> /ɪkˈspektənsi/ nhấn âm 2. balanced, habit, treatment nhấn âm 1.'),
    ('B', '<b>ingredient</b> /ɪnˈɡriːdiənt/ nhấn âm 2. muscle, suffer, nutrient nhấn âm 1.'),
    ('C', '<b>repetitive</b> /rɪˈpetətɪv/ nhấn âm 2. fitness, yoghurt, organism nhấn âm 1.'),
    ('A', '<b>replace</b> /rɪˈpleɪs/ nhấn âm 2. micron, healthy, lifestyle nhấn âm 1.'),
    ('C', '<b>bacteria</b> /bækˈtɪəriə/ nhấn âm 2. vaccine /ˈvæksiːn/, organism, virus nhấn âm 1.'),
    ('D', '<b>illness</b> /ˈɪlnəs/ nhấn âm 1. infectious /ɪnˈfekʃəs/, disease /dɪˈziːz/, infection /ɪnˈfekʃn/ nhấn âm 2.'),
    ('C', '<b>tuberculosis</b> /tjuːˌbɜːkjuˈləʊsɪs/ nhấn âm 3. burger, exercise, regular nhấn âm 1.'),
    ('D', '<b>antibiotic</b> /ˌæntibaɪˈɒtɪk/ nhấn âm 3. label, vegetable, physical nhấn âm 1.'),
    ('B', '<b>amount</b> /əˈmaʊnt/ nhấn âm 2. frequent, mental, quality nhấn âm 1.'),
])

# ---------------- TỪ VỰNG ----------------
put('vo1', [
    (['muscle', 'muscles'], 'Hình cơ bắp → <b>muscle</b>.'),
    (['squat', 'squats'], 'Hình tư thế gập gối → <b>squat</b> (động tác squat).'),
    (['fast food'], 'Hình đồ ăn nhanh → <b>fast food</b>.'),
    (['recipe', 'recipes'], 'Hình công thức nấu ăn → <b>recipe</b>.'),
    (['diet'], 'Hình chế độ ăn → <b>diet</b>.'),
    (['energy drink', 'energy drinks'], 'Hình nước tăng lực → <b>energy drink</b>.'),
    (['antibiotic', 'antibiotics'], 'Hình thuốc kháng sinh → <b>antibiotic</b>.'),
    (['yoghurt', 'yogurt'], 'Hình sữa chua → <b>yoghurt</b>.'),
    (['press-up', 'press up', 'press-ups', 'press ups', 'pressup'], 'Hình hít đất → <b>press-up</b>.'),
    (['vaccine', 'vaccines'], 'Hình tiêm chủng → <b>vaccine</b>.'),
])
put('vo2', [
    (['replace'], '<b>replace A with B</b> = thay A bằng B; sau "can" dùng nguyên mẫu.'),
    (['food label', 'food labels'], '<b>food label</b> = nhãn thực phẩm, cho biết nguồn gốc sản phẩm.'),
    (['food poisoning'], '<b>food poisoning</b> = ngộ độc thực phẩm (sau khi ăn sushi không tươi).'),
    (['diet'], '<b>low-carb diet</b> = chế độ ăn ít tinh bột, để giảm cân.'),
    (['ingredients', 'ingredient'], '<b>ingredients</b> = nguyên liệu (làm spaghetti); "all the ..." đi với danh từ số nhiều.'),
    (['yoghurt', 'yogurt'], '<b>plain yoghurt</b> with fresh fruit = sữa chua không đường ăn kèm trái cây.'),
    (['fast food'], '<b>fast food</b> = đồ ăn nhanh, "not very healthy", có thể gây tiểu đường.'),
    (['recipe', 'recipes'], '<b>recipe</b> = công thức; "follow it" = làm theo công thức.'),
])
put('vo3', [
    ('C', '<b>balanced diet</b> = chế độ ăn cân bằng, ăn đa dạng chất dinh dưỡng.'),
    ('D', '<b>the spread of COVID-19</b> = sự lây lan của COVID-19; sau "the" và trước "of" cần danh từ.'),
    ('B', 'Ebola là một <b>virus</b> gây chết người (deadly virus).'),
    ('B', '<b>full of energy</b> = tràn đầy năng lượng.'),
    ('A', '<b>working out</b> = tập luyện thể dục; "goes to the sports centre 4–5 times a week".'),
    ('C', '<b>flu vaccine</b> = vắc-xin cúm.'),
    ('D', '<b>cut down on</b> = cắt giảm.'),
    ('C', '<b>do squats</b> = tập squat (do + bài tập).'),
    ('A', '<b>Taking regular exercise</b> = tập thể dục đều đặn (take exercise).'),
    ('C', '<b>get rid of</b> smoking = bỏ/loại bỏ thói quen hút thuốc. give off = phát ra, workout = buổi tập, stay up = thức khuya.'),
])
put('vo4', [
    ('A', '<b>remedies</b> (phương thuốc) ≈ <b>treatments</b> (cách điều trị).'),
    ('B', '<b>avoid</b> (tránh) ≈ <b>prevent</b> (ngăn ngừa) trong ngữ cảnh "tránh tập thể dục ngay trước giờ ngủ".'),
    ('A', '<b>conditions</b> (điều kiện sống) ≈ <b>qualities</b>: living conditions/qualities of life. (Từ ngữ cảnh ý "chất lượng sống"; câu này nghĩa tương đối, xem báo cáo rà soát.)'),
    ('C', '<b>Developing</b> healthy habits ≈ <b>starting</b> healthy habits (bắt đầu hình thành thói quen).'),
    ('D', '<b>regularly</b> (đều đặn) ≈ <b>frequently</b> (thường xuyên).'),
])
put('vo5', [
    (['healthy', 'healthier'], 'Sau "to be" cần tính từ: <b>healthy</b> (khoẻ mạnh). HEALTH → healthy.'),
    (['strength'], 'Sau "muscle" cần danh từ: <b>muscle strength</b> (sức mạnh cơ bắp). STRONG → strength.'),
    (['examine'], 'Sau "Doctors will" cần động từ: <b>examine</b> patients. EXAMINATION → examine.'),
    (['repetitive'], 'Trước danh từ "routine" cần tính từ: <b>repetitive</b> routine (thói quen lặp lại). REPEAT → repetitive.'),
    (['poisoning'], '<b>food poisoning</b> = ngộ độc thực phẩm. POISON → poisoning.'),
    (['fitness'], '<b>fitness centre</b> = trung tâm thể hình. FIT → fitness.'),
    (['infectious'], 'Sau "an" và trước "disease" cần tính từ: <b>infectious</b> (dễ lây). INFECT → infectious.'),
    (['helpful'], 'Sau "are" cần tính từ: <b>helpful</b> (có ích), đối lập với "harmful". HELP → helpful.'),
    (['energy', 'energetic'], '<b>energy drinks</b> = nước tăng lực (danh từ ghép: energy + drinks). Từ gốc ENERGETIC (tính từ) cũng chấp nhận được về nghĩa nhưng cụm chuẩn là <b>energy drinks</b>.'),
    (['treatment'], 'Sau "receiving" cần danh từ: <b>treatment</b> (sự điều trị). TREAT → treatment.'),
])
put('vo6', [
    (['full of energy'], '<b>keep you full of energy</b> = giúp bạn tràn đầy năng lượng, không đói hay mệt.'),
    (['give up'], '<b>give up</b> unhealthy habits = từ bỏ thói quen xấu.'),
    (['gives off'], 'Chủ ngữ "it" số ít, hiện tại đơn → <b>gives off</b> blue light (phát ra ánh sáng xanh).'),
    (['develop healthy habits'], 'Sau "important to" dùng nguyên mẫu: <b>develop healthy habits</b> such as regular exercise and proper sleep.'),
    (['get rid of'], '<b>help get rid of stress</b> = giúp loại bỏ căng thẳng.'),
    (['pay attention to'], '<b>pay attention to</b> the expiry date = chú ý đến hạn sử dụng.'),
    (['have a balanced diet'], '<b>have a balanced diet</b> = có chế độ ăn cân đối; câu sau nêu ví dụ rau, trái cây, ít thịt đỏ.'),
    (['stay up late'], '<b>stay up late</b> = thức khuya → hôm sau mệt.'),
    (['food label', 'food labels'], 'Đọc <b>food label</b> để hiểu thành phần (ingredients) của sản phẩm.'),
    (['fall asleep'], '<b>fall asleep</b> quickly = nhanh chóng ngủ, không dùng thiết bị số.'),
])

# ---------------- NGỮ PHÁP ----------------
put('gr1', [
    ('B', '"Yesterday" → quá khứ đơn: <b>ate</b>.'),
    ('C', '"last night" → quá khứ đơn: <b>went</b> to bed.'),
    ('C', '"Last weekend" (xác định, đã qua) → quá khứ đơn cả hai vế: <b>went / was</b>.'),
    ('D', '"Up to now" → hiện tại hoàn thành: <b>have tried</b>.'),
    ('B', '"before" (trải nghiệm tính đến hiện tại) → <b>has never taken</b>.'),
    ('D', '"when he was young" là mốc quá khứ → cả hai vế quá khứ đơn: <b>suffered / was</b>.'),
    ('B', '<b>take up</b> boxing = bắt đầu chơi boxing; "2 months ago" → quá khứ đơn took.'),
    ('A', '"Fortunately, the treatment is working" (kết quả ở hiện tại) → <b>has just examined</b>.'),
])
put('gr2', [
    (['has been'], '"since 2007" → hiện tại hoàn thành, The gym số ít: <b>has been</b>.'),
    (['jogged'], '"last night" → quá khứ đơn: <b>jogged</b> (gấp đôi phụ âm cuối).'),
    (['has practised', 'has practiced'], '"for years" → hiện tại hoàn thành, My mom số ít: <b>has practised</b>.'),
    (['have cooked'], '"for the past 2 years" → hiện tại hoàn thành: <b>have cooked</b>.'),
    (['quit'], '"4 years ago" → quá khứ đơn: <b>quit</b> (quit – quit – quit).'),
    (['have taken'], '"for 2 months... Now I feel much better" → hiện tại hoàn thành: <b>have taken</b>.'),
    (['cut'], '"last week" → quá khứ đơn: <b>cut</b> (cut – cut – cut).'),
    (['walked'], '"last Monday" → quá khứ đơn: <b>walked</b>.'),
])
put('gr3', [
    ('B', '"Last year ... quit smoking and <u>start</u>" → hai hành động song song ở quá khứ. Sửa: <b>start → started</b>.'),
    ('A', '"He usually <u>drank</u>" → thói quen hiện tại ("after his workout... to build"). Sửa: <b>drank → drinks</b> (hoặc used to drink).'),
    ('A', '<b>give up</b> (bỏ) chứ không phải "give in". Sửa: <b>in → up</b>.'),
    ('B', 'Nghĩa chung là kháng sinh nói chung. Sửa: <b>antibiotic → antibiotics</b>.'),
    ('C', 'Chủ động: life expectancy "has increased", không dùng bị động. Sửa: <b>has been increased → has increased</b>.'),
    ('B', '"<u>for</u> 10 years <u>ago</u>" sai: ago đi với quá khứ đơn, không đi với for. Sửa: <b>bỏ "for"</b> (started ... 10 years ago).'),
    ('D', '<b>take up yoga</b> (bắt đầu tập); "has been taking in" sai. Sửa: <b>in → up</b>.'),
    ('C', 'Ăn vặt giữa các bữa không giúp duy trì cân nặng khoẻ mạnh. Sửa: <b>should → shouldn\'t</b>. (Câu có độ chắc chắn trung bình – xem báo cáo rà soát.)'),
])

# ---------------- ĐỌC ----------------
put('re1', [
    ('A', 'Cả bài nói về ăn uống, tập luyện và giấc ngủ → <b>How to Have a Healthy Lifestyle</b>.'),
    ('B', 'Đoạn 4: "avoiding <b>caffeine</b> and electronics before bedtime".'),
    ('D', '"make <u>them</u> a part of our daily routine" → them = <b>healthy habits</b>.'),
    ('A', '<b>adequate</b> (đủ) ≈ <b>enough</b>.'),
    ('C', 'Đoạn 2: tránh processed foods, sugary drinks và <b>saturated fats</b> (chất béo bão hoà), nhưng vẫn nên ăn "healthy fats". Nên "avoid all kinds of fats" là sai.'),
])
put('re2', [
    ('T', 'Đoạn 2: "foods high in fibre... promote feelings of fullness" → ăn trái cây giúp no nhanh hơn.'),
    ('F', 'Đoạn 2: balanced diet "can also help regulate blood sugar levels" → trái ngược với câu cho.'),
    ('F', 'Đoạn 3 chỉ nói "fatty fish" giàu omega-3, không phải <b>tất cả</b> các loại cá. (Có thể xem là NG – xem báo cáo rà soát.)'),
    ('NG', 'Bài không so sánh hay nói trái cây là thực phẩm được khuyên nhiều nhất cho người tập thể dục.'),
    ('T', 'Đoạn 3 (tinh thần) và đoạn 4 (thể chất) đều nêu ảnh hưởng của chế độ ăn.'),
])
put('re3', [
    ('A', '<b>gain popularity</b> = trở nên phổ biến.'),
    ('C', '<b>for its numerous health benefits</b> = nhờ rất nhiều lợi ích sức khoẻ.'),
    ('A', '<b>One of the key benefits</b> = một trong những lợi ích chính.'),
    ('B', '<b>ability to reduce</b> = khả năng làm giảm (ability + to V).'),
    ('D', 'Mệnh đề quan hệ không xác định bổ nghĩa cho cả vế trước: ", <b>which</b> can have a positive impact".'),
    ('C', 'the asanas <b>in</b> yoga = các tư thế (asana) trong yoga.'),
    ('B', 'regular <b>practice</b> of yoga = việc luyện tập yoga đều đặn.'),
    ('D', 'reduce the risk <b>of</b> heart diseases = giảm nguy cơ mắc bệnh tim.'),
    ('A', 'promoting deep <b>breathing</b> = thúc đẩy hít thở sâu.'),
    ('B', 'respiratory <b>conditions</b> such as asthma = các tình trạng về hô hấp như hen suyễn.'),
])

# ---------------- VIẾT ----------------
put('wr1', [
    (['our living conditions have improved over the last few decades'], 'Hiện tại hoàn thành + "over the last few decades": <b>Our living conditions have improved over the last few decades.</b>'),
    (['you can burn fat by doing this simple exercise'], '<b>by + V-ing</b>: You can burn fat by doing this simple exercise.'),
    (['antibiotics are often used to treat infections caused by bacteria'], 'Bị động: <b>Antibiotics are often used to treat infections caused by bacteria.</b> (caused by = rút gọn mệnh đề bị động).'),
    (['regular exercise can help you improve your muscle strength'], '<b>help + O + V</b>: Regular exercise can help you improve your muscle strength.'),
    (['i have given up bad habits for a better lifestyle'], '<b>I have given up bad habits for a better lifestyle.</b> (give up + danh từ).'),
])
put('wr2', [
    (['he hasn\'t played basketball for 3 years', 'he has not played basketball for 3 years', 'he hasn\'t played basketball for three years', 'he has not played basketball for three years'], 'gave up ... 3 years ago → <b>hasn\'t played ... for 3 years</b> (hiện tại hoàn thành + for).'),
    (['we need to cut down on fast food if we don\'t want to get heart diseases in the future', 'we need to cut down on the amount of fast food if we don\'t want to get heart diseases in the future', 'we need to cut down on fast food if we do not want to get heart diseases in the future'], 'reduce the amount of → <b>cut down on</b>.'),
    (['he started cooking for the family 10 years ago', 'he started to cook for the family 10 years ago', 'he started cooking for the family ten years ago', 'he started to cook for the family ten years ago'], 'has cooked for 10 years → <b>started cooking ... 10 years ago</b>.'),
    (['it is really important to have a good sleep at night', 'it is really important to have good sleep at night', 'it\'s really important to have a good sleep at night'], 'Dùng chủ ngữ giả <b>It is + adj + to V</b>.'),
    (['how about going to the gym with me next week', 'how about going to the gym with me next week'], 'Why don\'t you ...? = <b>How about + V-ing ...?</b>'),
])

# ---------------- NGHE (transcript nhận dạng bằng Whisper large-v3, đã đối chiếu nội dung) ----------------
put('li1', [
    ('B', 'Bài nghe: <i>"if you lack vitamins in any way, the solution isn\'t to rush off and take vitamin pills… No, it\'s far better to look at your diet and how you prepare your food."</i> → nên <b>thay đổi thói quen ăn uống</b>.'),
    ('A', 'Bài nghe: <i>"there are fat-soluble vitamins, which can be stored for quite some time by the body, and water-soluble vitamins, which are removed more rapidly."</i> → vitamin tan trong chất béo <b>được cơ thể dự trữ lâu</b>.'),
    ('C', 'Bài nghe: <i>"you need to ensure that you eat at least four servings of fruit and vegetables daily."</i> → <b>four servings daily</b>.'),
    ('A', 'Bài nghe: <i>"firstly, you must eat a variety of foods."</i> → ăn <b>nhiều loại thực phẩm khác nhau</b>. (Mua đồ tươi 2–3 lần/tuần, không phải một lần/tuần; "No more chips at the canteen" là bỏ khoai chiên.)'),
    ('D', 'Bài nghe: <i>"store your vegetables in the fridge or in a cool, dark place."</i> → <b>trong tủ lạnh hoặc nơi mát, tối</b> (phương án D gộp cả hai).'),
])
put('li2', [
    ({'blanks': [['avoid'], ['salt']]}, 'Bài nghe: <i>"at the top… are the things which we should really be trying to <b>avoid</b> as much as possible… sugar, <b>salt</b>, butter."</i>'),
    (['eggs', 'egg'], 'Bài nghe: <i>"in the middle… things that we can eat in moderation… milk, lean meat, fish, nuts, <b>eggs</b>."</i>'),
    (['bread'], 'Bài nghe: <i>"at the bottom… things that you can eat lots of… we have <b>bread</b>, vegetables and fruit."</i>'),
])


# ---------------- BÀI KIỂM TRA (50 câu) ----------------
put('kt', [
    ('B', '<b>balanced</b> đọc /t/ (sau âm vô thanh /s/). suffered, examined, received đọc /d/.'),
    ('C', '<b>replace</b> /rɪˈpleɪs/: a đọc /eɪ/. examine, bacteria, vaccine: a đọc /æ/.'),
    ('A', '<b>disease</b> /dɪˈziːz/ nhấn âm 2. nutrient /ˈnjuːtriənt/, treatment, diet nhấn âm 1.'),
    ('D', '<b>ingredient</b> /ɪnˈɡriːdiənt/ nhấn âm 2. energy, fitness, organism nhấn âm 1.'),
    ('C', '"2 days ago" → quá khứ đơn: <b>went</b>.'),
    ('C', '<b>life expectancy</b> = tuổi thọ (danh từ).'),
    ('D', '<b>stay up late</b> = thức khuya.'),
    ('C', '<b>virus</b>: COVID-19 virus, nguy hiểm với người có bệnh nền.'),
    ('A', 'Trước danh từ "diet" cần tính từ: <b>balanced diet</b>.'),
    ('B', '"when I was young" (quá khứ) → <b>was</b> often ill.'),
    ('A', '"since her parents forced her to" → vế chính hiện tại hoàn thành: <b>has eaten</b>; vế sau since + quá khứ: <b>forced</b>.'),
    ('D', '<b>work out</b> = tập luyện để cơ bắp được tăng cường.'),
    ('D', 'Bổ nghĩa cho động từ "Doing": trạng từ <b>repetitively</b> (lặp đi lặp lại).'),
    ('B', '"twice" (hai lần tính đến nay) → hiện tại hoàn thành: <b>have been</b> here twice.'),
    ('A', '<b>suffer from</b> tuberculosis = mắc bệnh lao.'),
    ('C', '"since the 1990s" → hiện tại hoàn thành: <b>have opposed</b>.'),
    ('B', '<b>cut down on</b> = cắt giảm.'),
    ('C', '<b>take exercise(s)</b> = tập thể dục.'),
    ('D', 'Vi khuẩn "good for your digestive system" → <b>beneficial</b> (có lợi).'),
    ('B', 'Đề nghị giúp đỡ → đáp lại bằng lời cảm ơn: <b>Thanks for your help.</b>'),
    ('C', 'Đề nghị giúp làm salad → lời đáp lịch sự, chấp nhận: <b>That\'s very kind of you.</b>'),
    ('B', '<b>adequate</b> (đủ) ≈ <b>sufficient</b>.'),
    ('C', '<b>negative</b> effects ≈ <b>detrimental</b> (có hại).'),
    ('A', '<b>crucial</b> (quan trọng) trái nghĩa <b>unimportant</b>.'),
    ('D', '<b>enough</b> (đủ) trái nghĩa <b>insufficient</b> (không đủ).'),
    ('B', 'Lỗi ở <b>regular</b> (tính từ). Sau động từ exercising cần trạng từ: <b>regularly</b>.'),
    ('A', 'Có "last week" → quá khứ đơn. Sửa: <b>have eaten → ate</b>.'),
    ('D', 'Lỗi ở <b>them</b>: fast food không đếm được → <b>it</b>.'),
    ('B', '<b>take steps in managing</b> = có những bước trong việc quản lý (sức khoẻ).'),
    ('C', '<b>since research shows</b> = vì nghiên cứu cho thấy (nêu lý do).'),
    ('A', '<b>consider</b> taking transit = cân nhắc việc đi phương tiện công cộng.'),
    ('A', '<b>Other</b> ways = những cách khác (danh từ số nhiều).'),
    ('D', 'Mệnh đề quan hệ thay cho "activities" (vật): <b>which</b> seem simple.'),
    ('B', 'Bài nói về mức độ nghiêm trọng của vấn đề sức khoẻ tinh thần → <b>Mental Health – an Alarming Issue</b>.'),
    ('C', '"<u>they</u>\'ve gotten worse" → they = <b>mental health issues</b> (anxiety and depression).'),
    ('A', '<b>surge</b> (sự tăng vọt) ≈ <b>growth</b>.'),
    ('B', 'Đoạn 1: "anxiety and depression rates worldwide have increased by 25%".'),
    ('D', 'Đoạn 2 nói "young adults and <b>women</b>" bị ảnh hưởng nhiều nhất, không phải đàn ông.'),
    ('A', 'Cả bài nói về nghiện thiết bị số trong thời gian giãn cách → <b>Digital Addiction During Pandemic Lockdown</b>.'),
    ('C', '<b>procrastinate</b> (trì hoãn) ≈ <b>delay</b>.'),
    ('B', '"increase the time <u>they</u> spend looking at screens" → they = <b>users</b>.'),
    ('D', '<b>consensus</b> (sự đồng thuận) ≈ <b>agreement</b>.'),
    ('A', 'Đoạn 4: "no simple way to determine... lack of consensus" → cách đo lường nghiện thiết bị số cần được nghiên cứu thêm.'),
    ('C', 'Đoạn 2: thói quen lặp lại "can develop into addictive patterns" → nói nền tảng số "cannot become addictive" là <b>sai</b>.'),
    ('A', 'Đoạn 2: lạm dụng "can affect a user\'s wellbeing" → <b>negative health effect</b>.'),
    ('C', '"The last time I went ... 6 years ago" = <b>I haven\'t gone bowling for 6 years</b>.'),
    ('A', '<b>compulsory</b> (bắt buộc) = <b>must</b>.'),
    ('D', 'Vaccines used to prevent → <b>Vaccines are necessary to prevent people from a disease</b>.'),
    ('A', 'Hai câu quan hệ nguyên nhân – kết quả → nối bằng <b>so</b>.'),
    ('C', 'Gộp hai câu: điều kiện "Unless you help her (= If you don\'t help her), Lan will not be able to find...".'),
])
