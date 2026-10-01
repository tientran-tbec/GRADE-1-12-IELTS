# -*- coding: utf-8 -*-
"""Lý thuyết dùng chung cho bộ ôn tập đề cương Mid-term 1 (được exec trong gen_mt1_ontap.py). Biến đầu ra: THEORY."""


def _tbl(head, rows):
    h = ''.join('<th>%s</th>' % x for x in head)
    b = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows)
    return '<table class="th"><tr>%s</tr>%s</table>' % (h, b)


_V1 = [
    ('life expectancy', 'n', 'tuổi thọ trung bình (≈ longevity)'), ('balanced diet', 'n', 'chế độ ăn cân bằng'),
    ('work out', 'v', 'tập thể dục (≈ exercise)'), ('suffer from', 'v', 'chịu đựng, bị (bệnh)'),
    ('infection / infectious', 'n / adj', 'sự nhiễm trùng / lây nhiễm'), ('immune system', 'n', 'hệ miễn dịch'),
    ('boost', 'v', 'tăng cường (≈ increase)'), ('nutrient', 'n', 'chất dinh dưỡng (vitamin, mineral)'),
    ('obesity', 'n', 'béo phì (≈ being overweight)'), ('bacteria / virus / vaccine', 'n', 'vi khuẩn / vi-rút / vắc-xin'),
    ('spread (of diseases)', 'n', 'sự lây lan'), ('give off', 'phr v', 'phát ra (ánh sáng, mùi, nhiệt)'),
    ('take up (a sport)', 'phr v', 'bắt đầu theo một môn (thể thao)'), ('home remedy', 'n', 'bài thuốc dân gian, cách chữa tại nhà'),
    ('food poisoning', 'n', 'ngộ độc thực phẩm'), ('dietary', 'adj', 'thuộc chế độ ăn'),
    ('lose ↔ gain (weight)', 'v', 'giảm cân ↔ tăng cân'), ('stretch ↔ shrink', 'v', 'giãn ra ↔ co lại'),
]
_V2 = [
    ('generation gap', 'n', 'khoảng cách thế hệ'), ('extended family ↔ nuclear family', 'n', 'gia đình nhiều thế hệ ↔ gia đình hạt nhân'),
    ('conflict ↔ harmony', 'n', 'xung đột ↔ hòa thuận'), ('viewpoint / traditional views', 'n', 'quan điểm / quan điểm truyền thống'),
    ('cultural values; norm', 'n', 'giá trị văn hóa; chuẩn mực'), ('follow in someone\'s footsteps', 'idiom', 'nối nghiệp, theo bước chân ai'),
    ('rely on; self-reliant; dependent on', 'v / adj', 'dựa vào; tự lực; phụ thuộc vào'), ('concentrate on', 'v', 'tập trung vào (≠ neglect)'),
    ('complain about', 'v', 'phàn nàn về'), ('impose sth on sb', 'v', 'áp đặt cái gì lên ai'),
    ('judge sb by appearance', 'v', 'đánh giá ai qua vẻ bề ngoài'), ('obey / follow rules; oblige (≈ force)', 'v', 'tuân thủ luật; bắt buộc'),
    ('lend a sympathetic ear', 'idiom', 'lắng nghe thông cảm'), ('interact with', 'v', 'tương tác với'),
    ('cope with', 'v', 'đối phó, vượt qua'), ('interpersonal skills', 'n', 'kỹ năng giao tiếp liên cá nhân'),
    ('single-sex education', 'n', 'giáo dục đơn giới'), ('open-minded ↔ narrow-minded; conservative; flashy', 'adj', 'cởi mở ↔ hẹp hòi; bảo thủ; loè loẹt'),
    ('counselor; reconcile', 'n / v', 'chuyên viên tư vấn; hòa giải, làm lành'), ('oppose ≈ forbid; reliable ≈ dependable', 'v / adj', 'phản đối; đáng tin cậy'),
]
_V3 = [
    ('city dweller', 'n', 'cư dân thành phố'), ('infrastructure', 'n', 'cơ sở hạ tầng'),
    ('renewable energy; alternative energy', 'n', 'năng lượng tái tạo; năng lượng thay thế'), ('sustainable ↔ short-term', 'adj', 'bền vững ↔ ngắn hạn'),
    ('liveable ↔ uninhabitable', 'adj', 'đáng sống ↔ không thể sống'), ('urban ↔ rural', 'adj', 'đô thị ↔ nông thôn'),
    ('eco-friendly', 'adj', 'thân thiện với môi trường'), ('greenhouse gas emissions', 'n', 'khí thải nhà kính'),
    ('exhaust fumes', 'n', 'khí thải xe cộ'), ('generate ≈ produce', 'v', 'tạo ra, sản xuất'),
    ('be made up of', 'phr', 'được tạo thành từ'), ('a solution to', 'phr', 'giải pháp cho'),
    ('pour into; fill up', 'phr v', 'đổ xô vào; làm đầy'), ('get round; go into', 'phr v', 'đi lại quanh; đi sâu vào (vấn đề)'),
    ('be involved in ≈ be engaged in', 'phr', 'tham gia vào'), ('become home to', 'phr', 'trở thành nơi sinh sống của'),
    ('sensor; privacy', 'n', 'cảm biến; quyền riêng tư'), ('pedestrian zone; high-rise building', 'n', 'khu đi bộ; tòa nhà cao tầng'),
]

THEORY = (
    '<p><b>A. TỪ VỰNG TRỌNG TÂM (Unit 1 – 3)</b></p>'
    '<p><b>Unit 1 – A long and healthy life</b></p>' + _tbl(['Từ / cụm từ', 'Loại', 'Nghĩa'], _V1) +
    '<p><b>Unit 2 – The generation gap</b></p>' + _tbl(['Từ / cụm từ', 'Loại', 'Nghĩa'], _V2) +
    '<p><b>Unit 3 – Cities of the future</b></p>' + _tbl(['Từ / cụm từ', 'Loại', 'Nghĩa'], _V3) +
    '<p class="note"><b>Mẹo từ vựng:</b> chú ý <b>giới từ đi kèm</b> (suffer <u>from</u>, rely <u>on</u>, complain <u>about</u>, impose <u>on</u>, a solution <u>to</u>, be good <u>for</u>) và <b>dạng từ</b> (sau linking verb → tính từ; sau động từ thường → trạng từ; sau tính từ sở hữu/mạo từ → danh từ).</p>'

    '<p><b>B. PHÁT ÂM & TRỌNG ÂM</b></p>' +
    _tbl(['Chủ đề', 'Quy tắc / ví dụ'], [
        ['Âm /ʃ/ ≠ /s/', 'sure, sugar, machine, special đọc /ʃ/; soup /s/.'],
        ['Âm /θ/ ≠ /ð/', 'health, strength, enthusiasm /θ/; <i>with</i>out, <i>th</i>ey /ð/.'],
        ['Âm /g/ ≠ /dʒ/', 'gap, great, grandparent /g/; generation, gender /dʒ/.'],
        ['Chữ -y cuối từ', '/i/: study, ready, puppy; /aɪ/: occupy, apply.'],
        ['Chữ o', 'hold, notice, follow(-ow) /əʊ/; force /ɔː/; problem, confident /ɒ/; romantic /əʊ/.'],
        ['Chữ e', 'dweller, sensor, energy /e/; reduce, believe, respect /ɪ/.'],
        ['Chữ i', 'design /aɪ/; impact, public, traffic, vitamin /ɪ/.'],
        ['Chữ a', 'gap, value, casual /æ/; behavior, taste, table /eɪ/; charge /ɑː/.'],
        ['Chữ c', 'common, conflict /k/; special /ʃ/; accept /ks/.'],
        ['Trọng âm 2 âm tiết', 'Danh từ/tính từ thường nhấn âm 1 (<b>fit</b>ness, <b>bal</b>ance, <b>mod</b>el); động từ thường nhấn âm 2 (pre<b>vent</b>, be<b>have</b>, com<b>plain</b>, im<b>pose</b>). Ngoại lệ: <b>vi</b>tamin, <b>pro</b>perly…'],
        ['Trọng âm từ dài', 'Đuôi -tion, -sion, -ic, -ity, -ian, -ious kéo trọng âm về <b>ngay trước</b> đuôi: pol<b>lu</b>tion, in<b>fec</b>tious, pe<b>des</b>trian, activity, tech<b>no</b>logy, informa<b>tion</b>.'],
        ['Trọng âm khác', 'Từ có tiền tố in-, un-, im- thường nhấn gốc từ: in<b>depend</b>ent → inde<b>pen</b>dence; <b>in</b>frastructure, <b>ar</b>chitecture nhấn âm 1.'],
    ]) +

    '<p><b>C. NGỮ PHÁP TRỌNG TÂM</b></p>'
    '<p><b>1. Quá khứ đơn và hiện tại hoàn thành</b></p>' +
    _tbl(['Thì', 'Công thức', 'Dấu hiệu & cách dùng'], [
        ['Quá khứ đơn', 'S + V2/ed', 'yesterday, last night/week, ago, in 1982, when I was… → hành động đã kết thúc, thời gian xác định.'],
        ['Hiện tại hoàn thành', 'S + have/has + V3', 'since + mốc, for + khoảng, so far, recently, just, already, yet, this month, ever/never → liên hệ hiện tại, kết quả còn ở hiện tại.'],
        ['Cấu trúc since', 'S + have/has + V3 + since + S + V2', 'I haven\'t met him since we <b>left</b> school.'],
    ]) +
    '<p><b>Các cấu trúc viết lại câu thường gặp:</b></p>'
    '<ul>'
    '<li><b>The last time</b> + S + V2 + <b>was</b> + khoảng thời gian + <b>ago</b> / (in) mốc = S + <b>haven\'t/hasn\'t</b> + V3 + <b>for</b> + khoảng / <b>since</b> + mốc.</li>'
    '<li><b>It is + khoảng thời gian + since</b> + S + (last) + V2 = S + haven\'t + V3 + for + khoảng thời gian.</li>'
    '<li><b>This is the first time</b> + S + have/has + V3 = S + have/has <b>never</b> + V3 + <b>before</b>.</li>'
    '<li>S + started/began + V-ing + khoảng thời gian + <b>ago</b> = S + have/has + V3 (hoặc been V-ing) + <b>for</b> + khoảng thời gian.</li>'
    '<li><b>How long</b> have you lived here? = <b>When</b> did you start living here?</li>'
    '</ul>'

    '<p><b>2. Động từ khuyết thiếu (Modal verbs)</b></p>' +
    _tbl(['Nghĩa', 'Dạng khẳng định', 'Dạng phủ định'], [
        ['Lời khuyên', 'should, ought to', 'shouldn\'t, ought <b>not to</b> (KHÔNG phải "ought to not")'],
        ['Bắt buộc (luật, quy định)', 'must, have to', 'mustn\'t = <b>cấm</b>'],
        ['Không cần thiết', '—', 'don\'t/doesn\'t have to, needn\'t (= not necessary)'],
        ['Được phép / cấm', 'can, may', 'not allowed to = mustn\'t, can\'t'],
        ['Suy đoán chắc chắn về quá khứ', 'must + have + V3', '—'],
    ]) +
    '<ul>'
    '<li>Sau modal luôn là <b>động từ nguyên mẫu không "to"</b> (must <u>pay</u>, have to <u>show</u>…). <b>mustn\'t ≠ don\'t have to</b>: mustn\'t = cấm; don\'t have to = không cần.</li>'
    '<li>I\'d advise you to V / If I were you, I would V / It would be a good idea for you to V = <b>You should V</b>.</li>'
    '<li>It is (not) necessary for S to V = S must / have to / needn\'t / don\'t have to V.</li>'
    '<li><b>suggest (that)</b> + S + (should) + V nguyên mẫu: I suggest that Gen Z <u>should</u> be encouraged….</li>'
    '<li>Xin phép lịch sự: <b>Do you mind if + S + V (hiện tại)</b>? / <b>Would you mind if + S + V (quá khứ)</b>? – đồng ý: "Of course not / No, go ahead".</li>'
    '</ul>'

    '<p><b>3. Động từ nối (linking verbs) và động từ trạng thái (stative verbs)</b></p>'
    '<ul>'
    '<li><b>Linking verbs</b> (look, feel, smell, taste, sound, seem, become, get, grow…) + <b>tính từ</b> (không dùng trạng từ): He looks <u>worried</u>; the milk smells <u>terrible</u>; she looks <u>adorable</u>; seems <u>exciting</u>.</li>'
    '<li>Bổ nghĩa cho <b>động từ thường</b> → <b>trạng từ</b>: The system works <u>effectively</u>; speak <u>impolitely</u>; needs cleaning <u>immediately</u>.</li>'
    '<li><b>Stative verbs</b> (think = cho rằng, see = hiểu/thấy, remember, know, understand, like, love, hate, want, have = sở hữu, believe, belong, sound, seem…) <b>không dùng thể tiếp diễn</b>: I <u>think</u> that…; I <u>see</u> your point; he <u>has</u> a big house.</li>'
    '<li>Một số động từ có <b>hai nghĩa</b>: think about (cân nhắc), see (gặp/hẹn), have (ăn, uống, tổ chức), smell/taste (ngửi/nếm – hành động) → được dùng tiếp diễn: I am <u>thinking</u> about…, Why are you <u>smelling</u> the flowers?</li>'
    '<li>Tính từ V-ing (chỉ tính chất sự vật: exciting, disappointing) ↔ V-ed (cảm xúc người: excited, disappointed).</li>'
    '</ul>'

    '<p><b>4. Dạng từ & cấu trúc khác</b></p>'
    '<ul>'
    '<li>Đảo ngữ điều kiện loại 1: <b>Should + S + V</b>, … (= If + S + should + V). </li>'
    '<li>Bị động hiện tại hoàn thành: <b>has/have been + V3</b> (This room has been painted since I was born).</li>'
    '<li>Rút gọn bị động: aspirations <u>compared</u> to older generations; <b>By + V-ing</b> = bằng cách.</li>'
    '<li>Liên từ: <b>Although</b> + mệnh đề; <b>However,</b> (đầu câu, chỉ sự đối lập); <b>Therefore</b> (kết quả); <b>Moreover / In addition</b> (bổ sung); <b>On the contrary</b> (trái lại).</li>'
    '<li>Sắp xếp đoạn văn: câu chủ đề → <i>Firstly / Also / In addition / Furthermore</i> → <i>Last but not least / Overall</i> (kết luận). Thư: <i>Dear…</i> mở đầu, <i>Please let me know…</i> + chữ ký kết thúc.</li>'
    '</ul>'
)
