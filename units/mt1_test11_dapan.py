# -*- coding: utf-8 -*-
"""Đáp án + giải thích – Test 11 – Mid-term 1 (Tiếng Anh 11 Global Success) – nguồn: Đề ôn tập giữa HK1 Anh 11 Global – Đề 2.
Quy ước: mcq/tf = chữ cái / T,F (hoặc list nếu nhiều đáp án đều đúng); fill = danh sách cách viết chấp nhận.
Word KHÔNG có khoá: toàn bộ đáp án tự giải; phần nghe dựa trên script nhận dạng bằng Whisper (large-v3) từ 2 file mp3."""

GHI_CHU_RA_SOAT = [
    'Word không có đáp án -> tự giải toàn bộ; phần nghe đối chiếu Whisper.',
    'Thứ tự file nghe: trong thư mục Word, "De-2-Part-1.mp3" là bài nói về generation gap (Q6-10) còn "Part-2.mp3" là bài Singapore (Q1-5) -> audio ghép theo thứ tự Part-2 rồi Part-1 để khớp thứ tự đề.',
    'g1: nguồn "92 reduction" thiếu dấu % (audio: "92% reduction in bus overcrowding"); "annalysed" -> "analysed"; "(5)even" -> "(5) even".',
    'g2.8: nguồn "hlep" -> "help". Câu g2.7 và g2.8 là hai câu gài bẫy (storytelling skills): trong bài, thanh niên dạy người già kỹ năng công nghệ, không phải kể chuyện.',
    'g5.17: phương án "key" (key to ...); "solution" mới là từ tự nhiên nhất nhưng không có trong đề. g5.16: nguồn "brige" -> "bridge".',
    'g5.19: phương án C mở đầu bằng lời đồng ý nhưng vế sau ("I am searching for information on the internet") mâu thuẫn -> chọn A (từ chối lịch sự có lý do).',
    'g6.22: câu mơ hồ: nghĩa hợp lý là "untraditional" (ra ở riêng bị xem là không truyền thống) nhưng Word có thể kỳ vọng "traditional" -> ANS chấp nhận cả hai. Nguồn "consider" thiếu -ed và "parents\'s" -> đã sửa thành "considered", "parents\'".',
    'g8.29: "Young people are more ..." -> đáp án mẫu "likely to be creative than old people" (tend to = be likely to); cách viết khác dùng "inclined to be creative than old people".',
    'Đề d2.txt tuy chỉ 72 dòng nhưng ĐỦ 35 câu (không phải chỉ có phần nghe). Đề không ghi giờ: 45 phút. Không có ảnh.',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ---------- Nghe: Singapore
put('g1', [
    (['wide range', 'range', 'wide-range'], '"Singapore\'s Smart Nation program has introduced a <b>wide range</b> of smart technologies in both its public and private sectors." (a wide range of = nhiều loại)'),
    (['data'], '"public <b>data</b> is being used in a trial to support transport planning" (dữ liệu công cộng được dùng thử nghiệm để hỗ trợ quy hoạch giao thông).'),
    (['sensors', 'sensor'], '"Data from fare cards to <b>sensors</b> in more than 5,000 vehicles, and the real-time tracking of buses, is analysed." (dữ liệu từ thẻ vé đến cảm biến trên hơn 5.000 xe).'),
    (['bus overcrowding', 'overcrowding', 'overcrowding on buses'], '"The trial has achieved an impressive result with a 92% reduction in <b>bus overcrowding</b>." (giảm 92% tình trạng xe buýt quá tải).'),
    (['journeys', 'journey'], '"commuters can pay using contactless cards or mobile wallets, making their <b>journeys</b> even more convenient" (khiến hành trình thuận tiện hơn).'),
], 1)
# ---------- Nghe: generation gap
put('g2', [
    ('F', 'Người nói: "The first solution ... is to care for the elderly in the <b>same way</b> we would for younger children." -> chăm sóc theo cách <b>giống nhau</b>, không phải khác nhau -> False.'),
    ('F', 'Trung tâm chăm sóc cộng đồng chỉ giúp người già "get out and about" (có chỗ để đến) và "boost their confidence"; không nói về kỹ năng kể chuyện -> False.'),
    ('F', 'Thanh niên giúp người già bằng kỹ năng công nghệ: "teach them about the internet, apps, phones". Chuyện kể về chiến tranh là do người già chia sẻ cho giới trẻ -> False.'),
    ('T', '"By sharing our knowledge, we can help improve their knowledge while also boosting our own confidence." -> True.'),
    ('T', '"I know from my personal experience that listening to personal stories about the war can be much more interesting than just reading about it in a textbook." -> True.'),
], 6)
# ---------- Phát âm / trọng âm
put('g3', [
    ('B', 'mat<b>ure</b> /məˈtʃʊə/ (ure = /ʊə/). nature /ˈneɪtʃə/, culture /ˈkʌltʃə/, posture /ˈpɒstʃə/ có ure = /ə/.'),
    ('C', 'priv<b>a</b>cy /ˈprɪvəsi/ (a = /ə/). examine /ɪɡˈzæmɪn/, financial /faɪˈnænʃl/, interact /ˌɪntərˈækt/ có a = /æ/.'),
], 11)
put('g4', [
    ('D', '<b>adapt</b> /əˈdæpt/ nhấn âm 2; sensor /ˈsensə/, muscle /ˈmʌsl/, fitness /ˈfɪtnəs/ nhấn âm 1.'),
    ('C', '<b>bacteria</b> /bækˈtɪəriə/ nhấn âm 2; properly /ˈprɒpəli/, curious /ˈkjʊəriəs/, nutrient /ˈnjuːtriənt/ nhấn âm 1.'),
], 13)
# ---------- Từ vựng / ngữ pháp
put('g5', [
    ('C', '<b>keep fit</b> = giữ dáng, giữ sức khỏe tốt (collocation). Tạm dịch: Nhiều bạn trẻ giữ dáng bằng cách tập gym.'),
    ('A', '<b>come into conflict(s)</b> = xung đột, bất hòa. Tạm dịch: Cha mẹ và con cái thường xung đột vì những chuyện nhỏ. (follow in sb\'s footsteps: nối nghiệp; bridge the gap: thu hẹp khoảng cách; increase life expectancy: tăng tuổi thọ - không hợp nghĩa.)'),
    ('B', '<b>the key to</b> + N = chìa khóa/giải pháp cho. Tạm dịch: Giao thông công cộng được cho là chìa khóa giải quyết ô nhiễm không khí ở các thành phố lớn. ("cause" đi với of, không phải to.)'),
    ('B', 'That <b>sounds great</b>: sau linking verb "sound" dùng tính từ (great), không dùng trạng từ greatly. "looks great" không dùng để đáp lời đề nghị.'),
    ('A', 'Từ chối lịch sự và nêu lý do: <b>I\'m sorry but that\'s not possible. I am expecting a call from a relative</b>. C tự mâu thuẫn (Feel free to use it nhưng lại đang dùng điện thoại), B và D không phù hợp ngữ cảnh.'),
    ('B', '"I think you ..." đưa lời khuyên -> <b>should</b> respect the elderly (bạn nên tôn trọng người cao tuổi). "must" quá mạnh, "shouldn\'t/mustn\'t" sai nghĩa.'),
], 15)
# ---------- Từ loại
put('g6', [
    (['interaction', 'interactions'], 'Sở hữu cách "children\'s" + danh từ: INTERACT -> <b>interaction</b> (sự tương tác) with other people.'),
    (['untraditional', 'non-traditional', 'nontraditional', 'not traditional', 'traditional'],
     'be considered + tính từ: TRADITION -> <b>untraditional</b> (không theo truyền thống). Tạm dịch: Ra ở riêng khỏi nhà cha mẹ sau khi cưới bị xem là không truyền thống trong văn hóa Việt Nam (gia đình nhiều thế hệ là truyền thống). Đề gốc có thể muốn "traditional" nên hệ thống chấp nhận cả hai.'),
    (['fitness'], 'FIT -> <b>fitness</b> programmes (chương trình thể dục thể hình): danh từ làm bổ ngữ cho danh từ "programmes".'),
], 21)
# ---------- Chia động từ
put('g7', [
    (['remain'], '"At present" -> hiện tại; remain là động từ trạng thái, chủ ngữ số nhiều "many people" -> <b>remain</b> (dùng hiện tại đơn). Tạm dịch: Hiện nay nhiều người vẫn độc thân cả đời.'),
    (['did your team score', 'has your team scored', 'have your team scored'],
     '"in the first half" nói về hiệp một đã kết thúc (quá khứ) -> <b>did your team score</b>. (Cũng chấp nhận "has your team scored" nếu trận đang diễn ra.)'),
    (['has wanted'], '"since she was a child" -> hiện tại hoàn thành: <b>has wanted</b> (cô ấy đã muốn trở thành cảnh sát từ nhỏ).'),
], 24)
# ---------- Viết lại câu
put('g8', [
    (['for younger people to show their respect to the seniors', 'for younger people to show respect to the seniors',
      'for younger people to show their respect to seniors', 'for young people to show their respect to the seniors'],
     '<b>Mẫu:</b> It is necessary for younger people to show their respect to the seniors. (need to V = it is necessary for sb to V)'),
    (['been a long time since we saw our uncle', 'been a long time since we last saw our uncle', 'been a long time since we have seen our uncle',
      'been a long time since we had seen our uncle'],
     '<b>Mẫu:</b> It has been a long time since we (last) saw our uncle. (haven\'t seen ... for a long time = It has been a long time since + S + V quá khứ)'),
    (['likely to be creative than old people', 'likely to be more creative than old people', 'inclined to be creative than old people'],
     '<b>Mẫu:</b> Young people are more likely to be creative than old people. (tend to V = be likely to V) – "Young people are more" đã có sẵn nên điền "likely to be creative than old people".'),
    (['parents and children can be caused by differences in thinking', 'parents and children can be caused by differences in the way of thinking',
      'parents and children can be caused by differences in thought'],
     '<b>Mẫu:</b> Conflicts between parents and children can be caused by differences in thinking. (chuyển sang bị động: S + can be + V3 + by ...)'),
], 27)
# ---------- Điền đoạn
put('g9', [
    ('C', 'benefit from sth = hưởng lợi từ. "Most of us can <b>benefit</b> from eating a lot of fruit and vegetables" (suffer from: chịu đựng; develop không đi với from).'),
    ('A', 'infectious <b>diseases</b> = các bệnh truyền nhiễm (collocation).'),
    ('C', 'in <b>season</b> = đang vào mùa (trái cây/rau củ đúng mùa vụ, "being produced in the area").'),
    ('B', 'Lời khuyên/khuyến nghị về lượng rau quả mỗi ngày: "You <b>should</b> eat at least five serves of vegetables ...".'),
    ('A', 'not really <b>look forward to</b> eating = không mấy mong đợi/hào hứng việc ăn; sau đó là gợi ý "start slowly with those you do like".'),
], 31)
