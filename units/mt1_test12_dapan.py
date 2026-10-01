# -*- coding: utf-8 -*-
"""Đáp án + giải thích – Test 12 – Mid-term 1 (Tiếng Anh 11 Global Success) – nguồn: Đề ôn tập giữa HK1 Anh 11 Global – Đề 3.
Quy ước: mcq = chữ cái 'A'-'D' (hoặc list nếu nhiều đáp án đều đúng); fill = danh sách cách viết chấp nhận.
Word KHÔNG có khoá: toàn bộ đáp án tự giải; phần nghe dựa trên script nhận dạng bằng Whisper (large-v3) từ 2 file mp3."""

GHI_CHU_RA_SOAT = [
    'Word không có đáp án -> tự giải toàn bộ; phần nghe đối chiếu Whisper (Part-1 trùng nội dung với bài "pessimistic/optimistic" của Unit 3; Part-2 là bài về lịch sử đô thị hóa).',
    'g2.10: audio nói "Global population is currently more than 7 billion and is predicted to top out around 10 billion" -> D (7 là số hiện tại, bẫy).',
    'g2.9: audio "more people were drawn from the countryside to the cities as more jobs and opportunities became available" -> A (Jobs).',
    'g5.16: "This" khớp tốt nhất với cả tình huống ở câu trước (cha mẹ khó tách khỏi con tuổi teen muốn tự do) -> D; B chỉ là vế đầu của câu.',
    'g5.18: câu hỏi "sollution" (nguồn gõ sai -> "solution"); "Complain and resist" là phản ứng của teen chứ không phải giải pháp -> A.',
    'g6.20: had better / should / ought to đều đúng -> D (All are correct), theo đúng phương án của đề. g6.21: "open-minded" (D) cũng đúng ngữ pháp nhưng "strict ... but also very fair" tự nhiên hơn -> giữ B.',
    'Sửa nguồn: số câu ở nguồn bị đánh lại nhiều lần (Ex 3 và Ex 4 đánh 5-8 và 9-12, phần Tự luận đánh 1-6 / không đánh số) -> đã đánh số liên tục 1-32; "sollution" -> "solution", "CLOSET" -> "CLOSEST", "What lead" -> "What led", "willing is" -> thêm dấu nháy.',
    'Đề d3.txt chỉ 83 dòng nhưng ĐỦ 32 câu (không chỉ có phần nghe). Không ghi giờ: 45 phút. Không có ảnh.',
]

ANS = {}
EXPLANATIONS = {}


def put(prefix, rows, start=1):
    for i, (a, e) in enumerate(rows, start):
        ANS['%s.%d' % (prefix, i)] = a
        EXPLANATIONS['%s.%d' % (prefix, i)] = e


# ---------- Nghe Ex1: pessimistic / optimistic
put('g1', [
    (['healthy'], '"Those who are pessimistic think that our cities will become more and more polluted, so they will no longer be safe and <b>healthy</b> places to live in."'),
    (['effective'], '"governments have no <b>effective</b> ways to control them" (chính phủ không có cách hiệu quả để kiểm soát ô nhiễm).'),
    (['overcrowded', 'over-crowded'], '"As a result, cities will become <b>overcrowded</b>. This means there will be more people, more waste, and heavier traffic."'),
    (['medicine'], '"city dwellers will have a better life thanks to important achievements in technology and <b>medicine</b>. Modern machines and well-equipped hospitals ..."'),
    (['renewable', 'Renewable'], '"scientists will find ways to cut down the cost of <b>renewable</b> energy sources ... They hope that these energy sources will step-by-step replace fossil fuels ... in the next 20 years."'),
], 1)
# ---------- Nghe Ex2: history of cities
put('g2', [
    ('B', '"as recently as 100 years ago, only <b>2 out of 10</b> people lived in a city" -> 20%.'),
    ('D', '"our ancestors began to learn ... early agricultural techniques ... and this led to the development of semi-permanent villages" -> <b>Advancements in agriculture</b>.'),
    ('C', '"as trade flourished, so did technologies that facilitated it, like carts, ships, <b>roads</b>, and ports" -> trong các phương án chỉ có Roads.'),
    ('A', '"more people were drawn from the countryside to the cities as more <b>jobs</b> and opportunities became available" -> Jobs.'),
    ('D', '"Global population is currently more than 7 billion and is predicted to top out around <b>10 billion</b>."'),
], 6)
# ---------- Phát âm / trọng âm
put('g3', [
    ('C', 'yogh<b>u</b>rt /ˈjɒɡət/ (u = /ɒ/ hoặc /əʊ/ tùy giọng). muscle /ˈmʌsl/, suffer /ˈsʌfə/, instruct /ɪnˈstrʌkt/ có u = /ʌ/.'),
    ('B', 'd<b>ie</b>t /ˈdaɪət/ (ie = /aɪə/). fresh /freʃ/, flesh /fleʃ/, exercise /ˈeksəsaɪz/ có e = /e/.'),
], 11)
put('g4', [
    ('C', '<b>formal</b> /ˈfɔːml/ nhấn âm 1; asleep /əˈsliːp/, avoid /əˈvɔɪd/, remind /rɪˈmaɪnd/ nhấn âm 2.'),
    ('C', '<b>impress</b> /ɪmˈpres/ nhấn âm 2; robot /ˈrəʊbɒt/, sensor /ˈsensə/, urban /ˈɜːbən/ nhấn âm 1.'),
], 13)
# ---------- Đọc hiểu
put('g5', [
    ('C', 'Cả bài nói về cách quan hệ cha mẹ - thanh thiếu niên thay đổi khi con lớn, nguyên nhân xung đột và cách giữ gắn kết -> <b>Parent-teen relationship</b>.'),
    ('D', '"it can often feel hard for them [parents] to separate from their teen, who wants to develop their own identity and to have new freedoms. <b>This</b> may lead to conflict" -> "This" chỉ tình huống cha mẹ khó buông con trong khi con muốn tự do: <b>Parents cannot separate from their teens who want to be free</b>.'),
    ('B', '<b>willing</b> (sẵn lòng) ≈ <b>ready</b>. Tạm dịch: ... hãy có mặt và sẵn sàng.'),
    ('A', 'Giải pháp khi con lớn: giao trách nhiệm (D), đặt quy tắc rõ ràng (C), giao tiếp thường xuyên và linh hoạt (B). "Complain and resist" là phản ứng của thanh thiếu niên, không phải giải pháp -> <b>A không đúng</b>.'),
], 15)
# ---------- Ngữ pháp
put('g6', [
    ('C', 'This is the first time + S + <b>have/has + V3</b>: This is the first time I have tried to play it.'),
    ('D', 'had better, should, ought to đều dùng được để khuyên -> <b>All are correct</b>. Tạm dịch: Chúng ta nên ăn càng nhiều trái cây càng tốt để đủ vitamin.'),
    ('B', 'appear + tính từ: appear <b>strict</b> with you, but also very fair (có vẻ nghiêm khắc với bạn nhưng cũng rất công bằng). strictly là trạng từ; strictness là danh từ.'),
    ('A', 'remain + tính từ (calm) = vẫn giữ bình tĩnh; "At present" -> hiện tại đơn, chủ ngữ I -> <b>remain</b>.'),
], 19)
# ---------- Từ loại
put('g7', [
    (['bacteria'], 'Sau tính từ "harmful" cần danh từ số nhiều (meat and poultry contain ...): BACTERIUM -> <b>bacteria</b> (vi khuẩn).'),
    (['sugary'], 'Trước danh từ "desserts and drinks" cần tính từ: SUGAR -> <b>sugary</b> (nhiều đường). Tạm dịch: nên cắt giảm đồ tráng miệng và đồ uống có nhiều đường.'),
    (['historical'], 'Trước danh từ "documents" cần tính từ: HISTORY -> <b>historical</b> (mang tính lịch sử).'),
    (['curiosity'], 'Chủ ngữ của câu cần danh từ: CURIOUS -> <b>Curiosity</b> (sự tò mò) là đặc điểm của thế hệ Y.'),
    (['pollution'], 'high risk of + danh từ: POLLUTE -> <b>pollution</b> (ô nhiễm).'),
    (['dwellers'], 'slum <b>dwellers</b> = cư dân khu ổ chuột (danh từ chỉ người, số nhiều vì có "the poor").'),
], 23)
# ---------- Viết lại câu
put('g8', [
    (['going camping this summer'],
     '<b>Mẫu:</b> How about going camping this summer? (Why don\'t we + V = How about + V-ing)'),
    (['are not allowed to cheat in the exam', 'are forbidden to cheat in the exam', 'must not cheat in the exam', 'are not permitted to cheat in the exam',
      'are not allowed to cheat in the exams', 'are prohibited from cheating in the exam', 'cannot cheat in the exam'],
     '<b>Mẫu:</b> Students are not allowed to cheat in the exam. / Students must not cheat in the exam. (It is forbidden for sb to V = sb mustn\'t V / sb isn\'t allowed to V)'),
    (['he played basketball was 6 months ago', 'he played basketball was six months ago'],
     '<b>Mẫu:</b> The last time he played basketball was 6 months ago. (hasn\'t + V3 for + khoảng thời gian = The last time + S + V quá khứ + khoảng thời gian + ago)'),
    (['was so dirty that I decided not to stay', 'was so dirty that I decided not to stay there'],
     '<b>Mẫu:</b> The beach was so dirty that I decided not to stay. (such a + adj + N + that = so + adj + that)'),
], 29)
