# -*- coding: utf-8 -*-
"""Đáp án + giải thích chi tiết – Unit 3 (Tiếng Anh 11 Global Success) – Bộ BÀI TẬP 4 KỸ NĂNG.
Quy ước như file lop11_u2_4kn_dapan.py. Đáp án theo khoá trong file Word gốc (đã đối chiếu độc lập).
Các câu khoá Word có vấn đề được giữ nguyên khoá và ghi chú trong lời giải (pr1.3, kt.17, kt.22, kt.45, wr2.1, gr1.8).
Phần Nghe: trích script có sẵn trong file Word."""

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


def put_open(prefix, rows):
    for i, e in enumerate(rows, 1):
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ======================= PHÁT ÂM =======================
put('pr1', [
    ('A', 've<b>h</b>icle /ˈviːəkl/ (h câm). housing /ˈhaʊzɪŋ/, neighbourhood /ˈneɪbəhʊd/, high-rise /ˈhaɪraɪz/ (h = /h/).'),
    ('B', '<b>c</b>entre /ˈsentə/ (c = /s/). carbon /ˈkɑːbən/, cope /kəʊp/, article /ˈɑːtɪkl/ (c = /k/).'),
    ('D', 'pr<b>i</b>vacy /ˈpraɪvəsi/ (i = /aɪ/). liveable /ˈlɪvəbl/, interact /ˌɪntərˈækt/, install /ɪnˈstɔːl/ (i = /ɪ/). Lưu ý: theo từ điển Anh-Anh, privacy còn có cách đọc /ˈprɪvəsi/ nên câu này dễ gây tranh cãi; giữ khoá của Word.'),
    ('A', 'are<b>a</b> /ˈeəriə/ (a = /ə/). gas, tram, transport (a = /æ/).'),
    ('D', 'probl<b>e</b>m /ˈprɒbləm/ (e = /ə/). dweller /ˈdwelə/, sensor /ˈsensə/, pedal /ˈpedl/ (e = /e/).'),
    ('C', '<b>u</b>rban /ˈɜːbən/ (u = /ɜː/). public /ˈpʌblɪk/, refund /ˈriːfʌnd/, underground /ˈʌndəɡraʊnd/ (u = /ʌ/).'),
    ('C', 'b<b>i</b>odiversity /ˌbaɪəʊdaɪˈvɜːsəti/ (i = /aɪ/). footprint /ˈfʊtprɪnt/, city /ˈsɪti/, farming /ˈfɑːmɪŋ/ (i = /ɪ/).'),
    ('B', 'g<b>a</b>rden /ˈɡɑːdn/ (a = /ɑː/). skyscraper /ˈskaɪskreɪpə/, sustainable /səˈsteɪnəbl/, space /speɪs/ (a = /eɪ/).'),
    ('A', '<b>o</b>perate /ˈɒpəreɪt/ (o = /ɒ/). computer /kəmˈpjuːtə/, community /kəˈmjuːnəti/, recommendation /ˌrekəmenˈdeɪʃn/ (o = /ə/).'),
    ('D', 'organi<b>s</b>ation /ˌɔːɡənaɪˈzeɪʃn/ (s = /z/). smart, pedestrian /pəˈdestriən/, prescription /prɪˈskrɪpʃn/ (s = /s/).'),
])
put('pr2', [
    ('D', '<b>install</b> /ɪnˈstɔːl/ nhấn âm 2. city, area, public nhấn âm 1.'),
    ('C', '<b>sustainable</b> /səˈsteɪnəbl/ nhấn âm 2. private, transport (n), vehicle nhấn âm 1.'),
    ('A', '<b>biodiversity</b> /ˌbaɪəʊdaɪˈvɜːsəti/ nhấn âm 4. dweller, sensor, infrastructure nhấn âm 1.'),
    ('D', '<b>computer</b> /kəmˈpjuːtə/ nhấn âm 2. problem, carbon, footprint nhấn âm 1.'),
    ('B', '<b>controlled</b> /kənˈtrəʊld/ nhấn âm 2. building, centre, urban nhấn âm 1.'),
    ('A', '<b>emission</b> /ɪˈmɪʃn/ nhấn âm 2. farming, underground (n), skyscraper nhấn âm 1.'),
    ('C', '<b>pedestrian</b> /pəˈdestriən/ nhấn âm 2. liveable, privacy, cybercrime nhấn âm 1.'),
    ('A', '<b>interact</b> /ˌɪntərˈækt/ nhấn âm 3. article, neighbourhood, operate nhấn âm 1.'),
    ('B', '<b>community</b> /kəˈmjuːnəti/ nhấn âm 2. pedal, reader, greenhouse nhấn âm 1.'),
    ('D', '<b>prescription</b> /prɪˈskrɪpʃn/ nhấn âm 2. booking, rooftop, future nhấn âm 1.'),
])

# ======================= TỪ VỰNG =======================
put('vo1', [
    ('tram', 'Hình a: xe điện chạy trên đường ray → <b>tram</b>.'),
    ('pedestrian zone', 'Hình b: người đi bộ qua vạch kẻ đường trong khu đô thị → <b>pedestrian zone</b> (khu dành cho người đi bộ).'),
    ('roof garden', 'Hình c: vườn rau trồng trên mái nhà → <b>roof garden</b> (vườn trên sân thượng).'),
    ('cycle path', 'Hình d: làn đường dành riêng cho xe đạp → <b>cycle path</b>.'),
    ('skyscraper', 'Hình e: các toà nhà cao tầng → <b>skyscraper</b> (nhà chọc trời).'),
])
put('vo2', [
    ('d', '<b>public transport</b> = hệ thống giao thông công cộng (xe buýt, tàu, tàu điện…) → d.'),
    ('b', '<b>carbon footprint</b> = lượng khí nhà kính (như CO2) do hoạt động của con người thải ra → b (dấu chân carbon).'),
    ('a', '<b>city dweller</b> = người sống ở thành phố → a.'),
    ('e', '<b>urban centre</b> = khu trung tâm của thành phố/thị trấn → e.'),
    ('c', '<b>greenhouse gas</b> = khí nhà kính (đặc biệt CO2) giữ nhiệt không thoát ra không gian → c.'),
])
put('vo3', [
    (['public transport'], 'a variety of means of <b>public transport</b> = nhiều phương tiện giao thông công cộng.'),
    (['cycle path', 'cycle paths'], 'khuyến khích người dân đi xe đạp, giảm ùn tắc → <b>cycle path</b> (làn xe đạp).'),
    (['pedestrian zone', 'pedestrian zones'], 'khu vực trung tâm an toàn, dễ chịu hơn cho người đi bộ → <b>pedestrian zone</b>.'),
    (['skyscrapers'], 'Động từ "are" + "tall buildings" → danh từ số nhiều <b>Skyscrapers</b> (nhà chọc trời).'),
    (['city dweller'], 'As a <b>city dweller</b> = với tư cách là người dân thành phố (sau "a" dùng danh từ số ít).'),
    (['tram'], 'hệ thống giao thông công cộng đáng tin cậy, kết nối các khu trong thành phố → <b>tram</b> system.'),
    (['urban centre', 'urban center'], 'khu vực sầm uất, phát triển nơi người ta sống, làm việc, vui chơi → <b>urban centre</b> (sau "An" dùng được vì urban bắt đầu bằng nguyên âm).'),
    (['greenhouse gases', 'greenhouse gas'], 'emission of <b>greenhouse gases</b> → góp phần gây nóng lên toàn cầu (dạng số nhiều).'),
    (['carbon footprint'], 'Decreasing our <b>carbon footprint</b> = giảm lượng khí thải carbon của chúng ta.'),
    (['rooftop garden', 'roof garden', 'rooftop gardens', 'roof gardens'], '"oasis" xanh giữa lòng thành phố → <b>roof garden</b> (khoá Word ghi "rooftop garden", cùng nghĩa).'),
])
put('vo4', [
    ('A', 'giá nhà cao, ít lựa chọn giá rẻ → <b>housing problem</b> (vấn đề nhà ở). "house problem" không tự nhiên.'),
    ('A', '<b>Biodiversity</b> (đa dạng sinh học) giữ vai trò quan trọng trong duy trì hệ sinh thái khoẻ mạnh.'),
    ('D', 'Cần tính từ: <b>liveable</b> (đáng sống). "most liveable cities" = các thành phố đáng sống nhất.'),
    ('B', 'interact <b>with</b> sth = tương tác với.'),
    ('C', 'be <b>made up of</b> = được tạo thành từ. run out of = hết; put off = hoãn; take after = giống (người thân).'),
    ('A', '<b>High-rise</b> buildings = các toà nhà cao tầng (tính từ ghép).'),
    ('C', 'parking <b>spaces</b> = chỗ đỗ xe.'),
    ('D', 'mobile <b>app</b> = ứng dụng di động, đặt nhà hàng qua app.'),
    ('B', 'medical <b>check-ups</b> = khám sức khoẻ định kỳ.'),
    ('C', 'risk of <b>cybercrime</b> = nguy cơ tội phạm mạng, khi thành phố ngày càng kết nối.'),
])
put('vo5', [
    ('B', '<b>privacy</b> (quyền riêng tư) ≈ <b>confidentiality</b> (sự bảo mật). publicity là trái nghĩa.'),
    ('A', '<b>recommendation</b> (lời đề xuất) ≈ <b>suggestion</b>.'),
    ('D', '<b>refunds</b> (tiền hoàn lại) ≈ <b>compensations</b> (khoản bồi hoàn) theo khoá đề; penalties/fines là tiền phạt, credits là tín dụng.'),
    ('C', '<b>operates</b> (vận hành) ≈ <b>functions</b>.'),
    ('A', '<b>cope with</b> (đối phó với) ≈ <b>deal with</b>.'),
])
put('vo6', [
    (['prescriptions'], 'giving out <b>prescriptions</b> = kê đơn thuốc (PRESCRIBE → prescription, số nhiều vì không có mạo từ).'),
    (['efficiently'], 'bổ nghĩa cho động từ "manage" → trạng từ <b>efficiently</b> (EFFICIENCY → efficiently).'),
    (['liveable', 'livable'], 'tính từ đứng trước "environment" → <b>liveable</b> (LIFE → liveable = đáng sống).'),
    (['private'], 'PRIVACY → <b>private</b> vehicles = phương tiện cá nhân (đối lập với public transport).'),
    (['reader', 'readers'], 'card <b>reader</b> systems = hệ thống đầu đọc thẻ (READ → reader).'),
    (['sensors'], '<b>sensors</b> (cảm biến) + "will be widely used" → danh từ số nhiều (SENSE → sensor).'),
    (['booking'], 'a user-friendly <b>booking</b> platform = nền tảng đặt chỗ (BOOK → booking).'),
    (['renewable'], '<b>Renewable</b> energy sources = nguồn năng lượng tái tạo (RENEW → renewable).'),
    (['environmental'], 'environmental protection = bảo vệ môi trường (ENVIRONMENT → environmental, tính từ).'),
    (['interact'], 'can easily <b>interact</b> with… (sau "can easily" cần động từ nguyên mẫu; INTERACTION → interact).'),
])
put('vo7', [
    ('eco-friendly', '<b>eco-friendly</b> ideas (ý tưởng thân thiện môi trường) hợp với "renewable energy, green transportation"; useless = vô dụng.'),
    ('victims', 'the number of crime <b>victims</b> = số nạn nhân của tội phạm.'),
    ('get around', '<b>get around</b> = đi lại, di chuyển (và khám phá). work out = tập thể dục/giải quyết.'),
    ('chores', 'household <b>chores</b> = việc nhà (rửa bát, lau nhà, gấp quần áo).'),
    ('electric', '<b>electric</b> buses = xe buýt điện, thân thiện môi trường. Khoá Word chọn "electric".'),
])

# ======================= NGỮ PHÁP =======================
put('gr1', [
    ('are becoming', 'Diễn tả xu hướng đang diễn ra (more efficient and connected) → hiện tại tiếp diễn <b>are becoming</b>.'),
    ('look', '<b>look</b> là động từ nối (linking verb) + tính từ (modern) → không dùng tiếp diễn.'),
    ('seems', '<b>seem</b> là động từ nối, chỉ trạng thái → không chia tiếp diễn; chủ ngữ số ít → seems.'),
    ('sounds', '<b>sound</b> là động từ nối, chỉ trạng thái → không chia tiếp diễn → sounds.'),
    ('is thinking', '<b>think of</b> = đang cân nhắc (hành động đang diễn ra) → is thinking of buying.'),
    ('think', '<b>think</b> = cho rằng/nghĩ rằng (ý kiến, trạng thái) → hiện tại đơn: I think it is a great idea.'),
    ('is having', '<b>have a good time</b> = hành động (vui chơi), có thể chia tiếp diễn → is having.'),
    ('am feeling', 'Trạng thái tạm thời "right now" → <b>am feeling</b> (khoá Word). Lưu ý: "feel" cũng có thể đúng; ưu tiên "am feeling" vì có "right now".'),
    ('became', 'Sự việc xảy ra tại thời điểm xác định trong quá khứ (in 1999) → quá khứ đơn <b>became</b>.'),
])
put('gr2', [
    ('A', '<b>look</b> là động từ nối + tính từ: looks <b>beautiful</b>.'),
    ('C', 'Hành động đang xảy ra, ngày càng tệ (worse and worse), ngữ cảnh hiện tại → <b>is getting</b>.'),
    ('B', '<b>love</b> là động từ trạng thái, không chia tiếp diễn → "I love visiting".'),
    ('D', '<b>seem</b> + tính từ: seems <b>beneficial</b> to… (có lợi).'),
    ('C', '<b>taste</b> + tính từ: tastes really good (có vị ngon). Người nói bất ngờ vì món do robot nấu.'),
    ('B', '<b>think of</b> (nghĩ ra, cân nhắc) là hành động đang diễn ra ("Please stop talking") → am thinking.'),
    ('D', '"at the moment" + bị động tiếp diễn → <b>is being upgraded</b>.'),
    ('A', '<b>seem</b> + danh từ/cụm danh từ: seems a talented city planner; không dùng tiếp diễn hay bị động.'),
])
put('gr3', [
    ('C', 'Câu bị động, hiện tại hoàn thành: "have <b>been used</b>". Sửa: have used → <b>have been used</b>.'),
    ('B', 'seem + tính từ, không dùng trạng từ. Sửa: excitingly → <b>exciting</b>.'),
    ('B', 'Bổ nghĩa cho động từ "operate" cần trạng từ. Sửa: efficient → <b>efficiently</b>.'),
    ('A', 'Cần tính từ ghép bị động (hệ thống được điều khiển bằng máy tính). Sửa: Computer-control → <b>Computer-controlled</b>.'),
    ('C', 'be <b>made</b> available = được cung cấp sẵn. Sửa: taken → <b>made</b>.'),
])

# ======================= ĐỌC =======================
put('re1', [
    ('B', 'have <b>access</b> to information = có quyền tiếp cận thông tin.'),
    ('A', 'be <b>motivated</b> to spend time… = có động lực. hindered = bị cản trở (sai nghĩa).'),
    ('D', 'Rút gọn mệnh đề chủ động: are connected everyday <b>using</b> mobile phones.'),
    ('A', '<b>Many</b> (seniors) have wearable devices: Many + danh từ số nhiều đếm được, hợp với "seniors".'),
    ('C', 'Đại từ quan hệ <b>that</b> thay cho "devices": wearable devices… that help monitor…'),
    ('C', 'Câu sau đưa ví dụ ("imagine an age-friendly smart city layer…") → <b>For example</b>.'),
    ('B', 'linked <b>to</b> a smart watch (link to).'),
    ('D', 'Tính từ <b>interactive</b> bổ nghĩa cho "smart city map" (bản đồ tương tác).'),
    ('C', 'Rút gọn bị động: The National Public Toilet Map, <b>created</b> by the Australian Department of Health and Ageing.'),
    ('B', 'are <b>among</b> other mobile apps = nằm trong số các ứng dụng khác (among + danh từ số nhiều).'),
])
put('re2', [
    ('A', 'Cả bài nói về chi phí ẩn, tiêu thụ năng lượng, rác điện tử… → <b>Downsides of Smart cities</b> (Mặt trái của thành phố thông minh).'),
    ('D', '"waste bins that alert city managers when <b>they</b> need collecting" → they = <b>waste bins</b>.'),
    ('B', '<b>warranties</b> (bảo hành) ≈ <b>guarantees</b>.'),
    ('D', 'Đoạn 4: studies show more ICT leads to higher energy use; "smart cities may end up a zero-sum game in terms of sustainability" → <b>có nghiên cứu cho rằng thành phố thông minh có thể không mang lại lợi ích về tính bền vững</b>.'),
    ('C', 'Bài viết: objects are built with durable materials, whereas <b>computer processors and software systems are short-lived</b> → C (phần mềm bền nên dùng lâu) là <b>sai</b>.'),
])
put('re3', [
    ('F', '"The results can provide higher-quality services at <b>lower cost</b>" → sai ở "higher … cost".'),
    ('F', 'Bài viết: riders "touch or tap <b>their phone or other mobile device</b>" → không nói thẻ tín dụng (credit cards).'),
    ('T', '"The city benefits by reducing the cost… including <b>avoiding issuing and distributing special smartcards</b>".'),
    ('T', '"The data collected are expected to… <b>address urban flooding</b>" (giải quyết ngập úng đô thị).'),
    ('NG', 'Bài không nói về việc dự án "Array of Things" sẽ được mở rộng rộng rãi hay không.'),
])

# ======================= VIẾT =======================
put('wr1', [
    (['smart technologies have made the lives of city dwellers more convenient'], 'Cấu trúc: S (Smart technologies) + have made + O (the lives of city dwellers) + adj (more convenient).'),
    (['more people are moving away from the urban centre of large cities'], 'More people + are moving away from + the urban centre of large cities (hiện tại tiếp diễn).'),
    (['smart cities are built on technologies to improve peoples lives', "smart cities are built on technologies to improve people's lives"], 'Smart cities are built on technologies + to V (mục đích) improve people\'s lives.'),
    (['the mobile app allows you to book a parking space and make a payment'], 'allow sb <b>to V</b>: The mobile app allows you to book a parking space and make a payment.'),
    (['people become worried because their personal information might not be protected'], 'People become worried <b>because</b> + mệnh đề (their personal information might not be protected – bị động với modal).'),
])
put('wr2', [
    ('B', 'Câu gốc chủ động → B là câu bị động tương ứng (Information… collected by sensors and cameras). C thiếu "are"; A, D sai nghĩa. Lưu ý ngữ pháp: "information" không đếm được nên "is collected" chuẩn hơn, nhưng B vẫn là đáp án gần nghĩa nhất.'),
    ('D', '"will not know how to use" ≈ "will <b>lack the knowledge</b> to use". B sai (nếu được đào tạo thì không struggle).'),
    ('C', 'improve old infrastructure ≈ <b>enhance the outdated infrastructure</b>; creating pedestrian zones and cycle paths ≈ constructing additional areas for pedestrians and cyclists.'),
    ('B', '"negative impacts… are fewer" ≈ smart cities have <b>fewer</b> negative environmental influences than regular cities.'),
    ('C', 'expensive, so could not afford ≈ <b>too expensive for sb to V</b>.'),
])
put_open('wr3', ['<b>Bài mẫu:</b><br><i>Living in a smart city has its benefits, but there are also important concerns to consider. One major worry is about privacy and data security. Smart cities collect a lot of information through sensors and cameras, which raises concerns about personal information being accessed without permission. Data leaks can have serious consequences, and people may feel like their privacy is being invaded. Another issue is the heavy reliance on technology. In a smart city, if there are cyber attacks or system failures, critical services can be affected. It is important to address these drawbacks to ensure that the advantages of a smart city are balanced with protecting people’s rights and well-being.</i><br><b>Dịch:</b> Sống trong một thành phố thông minh có những lợi ích của nó, nhưng cũng có những mối quan tâm quan trọng cần xem xét. Một lo lắng lớn là về quyền riêng tư và bảo mật dữ liệu. Các thành phố thông minh thu thập rất nhiều thông tin thông qua các cảm biến và camera, điều này làm dấy lên mối lo ngại về việc thông tin cá nhân bị truy cập trái phép. Rò rỉ dữ liệu có thể gây ra hậu quả nghiêm trọng và mọi người có thể cảm thấy như quyền riêng tư của họ đang bị xâm phạm. Một vấn đề khác là sự phụ thuộc nặng nề vào công nghệ. Trong một thành phố thông minh, nếu có các cuộc tấn công mạng hoặc lỗi hệ thống, các dịch vụ quan trọng có thể bị ảnh hưởng. Điều quan trọng là phải giải quyết những nhược điểm này để đảm bảo rằng những lợi thế của một thành phố thông minh được cân bằng với việc bảo vệ quyền và hạnh phúc của người dân.'])

# ======================= NÓI =======================
put_open('sp1', ['<b>Bài mẫu:</b><br><i>Yes, I would like to live in a smart city for several reasons. Firstly, it can make life easier with advanced technology. Smart transportation helps reduce traffic and saves time. Besides, smart cities care about the environment and use clean energy. Moreover, they also improve public services like waste management and healthcare.</i><br><b>Dịch:</b> Có, tôi muốn sống trong một thành phố thông minh vì nhiều lý do. Thứ nhất, nó có thể làm cho cuộc sống dễ dàng hơn với công nghệ tiên tiến. Giao thông thông minh giúp giảm lưu lượng và tiết kiệm thời gian. Bên cạnh đó, thành phố thông minh quan tâm đến môi trường và sử dụng năng lượng sạch. Hơn nữa, họ cũng cải thiện các dịch vụ công cộng như quản lý chất thải và chăm sóc sức khỏe.', '<b>Bài mẫu:</b><br><i>In my perspective, I believe cities in the future will be highly connected and sustainable. Advanced technologies like artificial intelligence, Internet of Things, and renewable energy systems will be popular. There will be efficient transportation networks, smart infrastructure, and widespread use of automation. Besides, cities will have more green spaces, high-rise buildings.</i><br><b>Dịch:</b> Theo quan điểm của tôi, tôi tin rằng các thành phố trong tương lai sẽ có tính kết nối cao và bền vững. Các công nghệ tiên tiến như trí tuệ nhân tạo, Internet vạn vật và hệ thống năng lượng tái tạo sẽ trở nên phổ biến. Sẽ có mạng lưới giao thông hiệu quả, cơ sở hạ tầng thông minh và việc sử dụng tự động hóa rộng rãi. Bên cạnh đó, các thành phố sẽ có thêm không gian xanh, nhà cao tầng.'])
put_open('sp2', ['<b>Bài mẫu:</b><br><i>In Ha Noi, one smart technology that has been widely used is QR Pay, a convenient and contactless payment system.<br>QR Pay allows residents and visitors to make payments using their smartphones by scanning QR codes displayed at various places, including retail stores, restaurants, transportation services, and even street vendors. This system benefits from the widespread adoption of smartphones and mobile payment applications. To use QR Pay, individuals simply need to have a digital wallet or link their bank accounts to a payment application. Once the payment application is set up, they can scan the QR code presented by the merchant, enter the desired payment amount, and confirm the transaction. The funds are securely transferred, making the entire process quick and risk-free.<br>Using QR Pay has brought numerous benefits. Firstly, it reduces the need for physical cash or cards which are traditional payment methods. This enhances convenience for both consumers and merchants. Another advantage of QR Pay is its flexibility. It can be used in various places from large shopping centres to small street vendors. Therefore, more people are able to access this service.<br>In short, the QR Pay technology has transformed the way people make payments, bringing convenience, speed, and security to daily transactions.</i><br><b>Dịch:</b> Tại Hà Nội, một công nghệ thông minh đã được sử dụng rộng rãi là QR Pay, một hệ thống thanh toán tiện lợi và không cần tiếp xúc.<br>QR Pay cho phép người dân và du khách thanh toán bằng điện thoại thông minh của họ bằng cách quét mã QR được hiển thị ở nhiều nơi khác nhau, bao gồm cửa hàng bán lẻ, nhà hàng, dịch vụ vận chuyển và thậm chí cả những người bán hàng rong. Hệ thống này được hưởng lợi từ việc áp dụng rộng rãi điện thoại thông minh và các ứng dụng thanh toán di động. Để sử dụng QR Pay, các cá nhân chỉ cần có một ví kỹ thuật số hoặc liên kết tài khoản ngân hàng của họ với một ứng dụng thanh toán. Sau khi ứng dụng thanh toán được thiết lập, họ có thể quét mã QR do người bán cung cấp, nhập số tiền thanh toán mong muốn và xác nhận giao dịch. Tiền được chuyển an toàn, làm cho toàn bộ quá trình nhanh chóng và không có rủi ro.<br>Sử dụng QR Pay đã mang lại vô số lợi ích. Thứ nhất, nó làm giảm nhu cầu về tiền mặt hoặc thẻ là phương thức thanh toán truyền thống. Điều này nâng cao sự thuận tiện cho cả người tiêu dùng và thương nhân. Một ưu điểm khác của QR Pay là tính linh hoạt của nó. Nó có thể được sử dụng ở nhiều nơi từ các trung tâm mua sắm lớn đến những người bán hàng rong nhỏ. Do đó, nhiều người có thể truy cập dịch vụ này.<br>Tóm lại, công nghệ QR Pay đã thay đổi cách mọi người thực hiện thanh toán, mang lại sự tiện lợi, nhanh chóng và bảo mật cho các giao dịch hàng ngày.'])

# ======================= NGHE (script trong file Word) =======================
put('li1', [
    ('D', 'Presenter: "it\'s an umbrella term for the <b>high tech programs</b>… a broad range of technologies" → Cities with a range of high-tech programs and technologies.'),
    ('A', '"A UniSA survey found <b>45 per cent</b> of respondents said they\'d never heard of the term smart cities" (54% là số người không hiểu khái niệm).'),
    ('A', '"Researchers believe it\'s <b>the fear of the unknown</b>." – nỗi sợ điều chưa biết.'),
    ('A', 'Grant: "facial recognition technology… certainly contributes to <b>preventing crime and solving crime</b>."'),
    ('D', '"councils will adopt these smart city technologies <b>as they become available and affordable</b>" → được áp dụng nếu sẵn có và giá hợp lí.'),
])
put('li2', [
    (['technology'], '"smart cities that make use of <b>technology</b> to serve the people and the environment."'),
    (['connected'], '"Everything in a smart city will be <b>connected</b> and interactive."'),
    (['public'], '"…improve <b>public</b> services and help people in their daily lives."'),
    (['pedestrian'], '"Street lights… increasing or decreasing their glow based on <b>pedestrian</b> usage."'),
    (['traffic'], '"Sensors will regulate <b>traffic</b> lights to prevent traffic jams."'),
    (['parking', 'park'], '"Someone looking for a place to <b>park</b> will be told where to find one." → parking spots.'),
    (['watering'], '"Weather sensors will automatically activate <b>watering</b> systems."'),
    (['nature'], '"<b>Nature</b> will be an important part of these new cities with the creation of parks, urban woods and urban farms."'),
    (['vegetation'], '"Buildings covered with <b>vegetation</b> like the planned forest city near Johor in Malaysia."'),
    (['self-driving', 'self driving', 'driverless'], '"Milton Keynes… first public taxi service using <b>self-driving</b> vehicles."'),
    (['control'], '"Songdo… monitored from a central <b>control</b> station."'),
    (['clean'], '"Masdar City… a hub for <b>clean</b> tech companies."'),
])

# ======================= BÀI KIỂM TRA (50 câu) =======================
put('kt', [
    ('C', 'install<b>ed</b> /ɪnˈstɔːld/ (đọc /d/ sau âm /l/ hữu thanh). interacted, operated, refunded: -ed = /ɪd/ (sau /t/, /d/).'),
    ('A', 'cybercr<b>i</b>me /ˈsaɪbəkraɪm/ (i = /aɪ/). liveable, article, booking (i = /ɪ/).'),
    ('D', '<b>controlled</b> /kənˈtrəʊld/ nhấn âm 2. private, transport (n), rooftop nhấn âm 1.'),
    ('C', '<b>computer</b> /kəmˈpjuːtə/ nhấn âm 2. neighbourhood, underground (n/adj), skyscraper nhấn âm 1.'),
    ('B', 'think of + V-ing (đang cân nhắc, hành động đang diễn ra) → <b>am thinking</b> of pedalling…'),
    ('C', 'Sau "the busiest and" cần cấu trúc so sánh nhất: <b>most</b> crowded.'),
    ('B', '<b>cope with</b> the challenges = đối phó với các thách thức.'),
    ('D', 'increase green areas and <b>biodiversity</b> = tăng không gian xanh và đa dạng sinh học (vườn trên mái).'),
    ('C', 'Trước danh từ "city" cần tính từ: <b>sustainable</b> city (thành phố bền vững).'),
    ('D', 'pedestrian zones are areas <b>where</b> people can walk… (where thay cho giới từ + areas, chỉ nơi chốn).'),
    ('A', '"City dwellers <b>agree</b> that…" – hiện tại đơn diễn tả quan điểm chung; agree là động từ trạng thái nên không dùng tiếp diễn.'),
    ('C', 'interact <b>with</b> the city administration.'),
    ('B', '<b>due to</b> + cụm danh từ (the risk of cybercrime) = do, bởi vì. despite = mặc dù; so that + mệnh đề; but không hợp nghĩa.'),
    ('B', '<b>seems</b> (linking verb) + tính từ <b>essential</b>.'),
    ('A', 'a <b>sense</b> of community = tinh thần/ý thức cộng đồng (collocation cố định).'),
    ('A', '<b>looks</b> + tính từ: looks more <b>modern</b>.'),
    ('B', '<b>believe</b> là động từ trạng thái, chia hiện tại đơn "I believe". Lỗi nguồn: B và C trùng nhau ("believe"); đã đổi C thành "believes", khoá giữ B.'),
    ('C', 'route recommendation = gợi ý lộ trình (collocation); "navigate in the city".'),
    ('D', '<b>Underground</b> farming = trồng trọt ở không gian dưới mặt đất. Rooftop là trên mái.'),
    ('A', 'Mike nêu "There are still significant challenges" → không chắc chắn: <b>I am not sure this is true.</b> (C, D đồng ý hoàn toàn, mâu thuẫn).'),
    ('D', 'Kathy dựa trên "fast development of technology" → đồng ý: <b>Yes, I\'m pretty sure about it.</b>'),
    ('A', 'Theo khoá Word: <b>liveable</b> (đáng sống) ≈ <b>loveable</b> (đáng yêu) – cặp gần nghĩa nhất trong các phương án; unsuitable/inconvenient/terrible đều tiêu cực. Câu có chất lượng đáp án kém (loveable ≠ liveable), giữ khoá Word.'),
    ('D', 'city <b>dwellers</b> (cư dân thành phố) ≈ <b>residents</b>.'),
    ('D', '<b>private</b> (cá nhân) ↔ <b>shared</b> (dùng chung). personal, individual là đồng nghĩa.'),
    ('A', '<b>urban</b> (đô thị) ↔ <b>rural</b> (nông thôn).'),
    ('A', 'Chủ ngữ "Many people" số nhiều, believe là động từ trạng thái: <b>is believing</b> → <b>believe</b>.'),
    ('C', '<b>appears</b> + tính từ (linking verb). Sửa: efficiently → <b>efficient</b>.'),
    ('B', 'be <b>made up of</b> (được tạo thành từ). Sửa: for → <b>of</b>.'),
    ('C', 'have a lasting effect on = có ảnh hưởng lâu dài lên.'),
    ('D', '"Until recently… guessed at. Now, <b>however</b>, mobile tech… offers…" → tương phản giữa trước đây và hiện nay.'),
    ('B', 'City <b>developers</b> and officials = các nhà phát triển và quan chức thành phố (danh từ chỉ người, song song với "officials").'),
    ('A', '<b>every</b> footstep + danh từ số ít (mỗi bước chân tạo năng lượng).'),
    ('D', ', <b>which</b> extends far beyond… – mệnh đề quan hệ không xác định, which thay cho cả mệnh đề trước (a unique user experience).'),
    ('B', 'Bài nói về khái niệm và lợi ích của thành phố thông minh (tối ưu không gian, tăng kết nối, tiết kiệm thời gian/tiền, thân thiện môi trường) → <b>The Concept and Benefits of Smart cities</b>.'),
    ('A', '<b>dearth</b> (sự khan hiếm, thiếu hụt) ≈ <b>scarcity</b>. surplus/abundance là trái nghĩa.'),
    ('C', 'Đoạn 2: "designed for optimum usage of space and resources… increasing connectivity at various levels among citizens" → <b>maximise the usage of space and resources and enhance connectivity</b>.'),
    ('A', '"Smart cities are designed… <b>It</b> also aims at increasing connectivity" → It = việc xây dựng thành phố thông minh (theo khoá Word; ngữ cảnh chung là smart city).'),
    ('D', 'Đoạn 3: "There are devices which can keep track of air purity level, as well as other environmental and health-related factors" → D.'),
    ('B', 'Cả bài bàn về các thách thức (cơ sở hạ tầng, quyền riêng tư, giáo dục cộng đồng) và vai trò của nhà phát triển trong giải quyết → <b>The Evolution of Smart cities: Challenges and Solutions</b>.'),
    ('A', 'Đoạn 2: "replacing decades-old infrastructure… there are still areas… where access is limited" → thay thế hạ tầng cũ và hạn chế truy cập băng thông rộng.'),
    ('D', '<b>alleviate</b> (làm giảm bớt) ≈ <b>lessen</b>. worsen là trái nghĩa.'),
    ('B', 'Đoạn 3: "nobody wants to feel like they are constantly being monitored by Big Brother" → <b>the constant feeling of being monitored by cameras</b>.'),
    ('C', '"Developers can help alleviate some of the anxieties… by adding transparency and education to <b>their</b> solutions" → their = <b>developers\'</b>.'),
    ('C', '<b>thrive</b> (phát triển mạnh) ≈ <b>prosper</b>.'),
    ('C', 'Theo khoá Word là C, nhưng đây là lựa chọn đáng ngờ: bài viết nói nhà phát triển cần cân nhắc thách thức hạ tầng và cân bằng chất lượng sống – quyền riêng tư (đáp án B hợp lí hơn với "inferred"); C chỉ nói nhà phát triển "chịu trách nhiệm thay thế hạ tầng", bài không nói vậy. Giữ khoá Word.'),
    ('C', 'because + <b>of its benefits</b> ≈ "good for the environment"; public vehicles = public transport. A, B, D sai nghĩa/quan hệ.'),
    ('B', '"smart cities more liveable than cities in the past" = "cities in the past less liveable than smart cities" (đảo chủ ngữ so sánh, cùng nghĩa).'),
    ('D', '<b>Only when</b> = <b>Not until</b> + mệnh đề + đảo ngữ (can the quality of life be improved). B, C sai cấu trúc "It is not until… that".'),
    ('B', 'Hai vế tương phản (nguy cơ tội phạm mạng ↔ biện pháp an ninh) → <b>Although</b>.'),
    ('A', 'Rút gọn bằng V-ing chỉ kết quả: …decrease, <b>encouraging</b> residents to use public transport more often.'),
])
