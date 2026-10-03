# -*- coding: utf-8 -*-
"""Nhóm on2b: Đề ôn tập HK2 – Đề 10, 11, 12 (file 'Nghe-De-on-tap-HK2...') và Đề 13, 14, 15 (file 'De-on-tap-HK2...').
Các đề này KHÔNG có đáp án phần nghe (trừ Đề 10 có bảng đáp án đầy đủ): đáp án phần nghe suy ra từ bản phiên âm của file mp3
(Whisper small.en, đối chiếu đúng 100% với đáp án chính thức của Đề 10) kết hợp tranh; phần đọc/viết suy ra từ nội dung bài/tranh/ngữ pháp.
Đã bỏ Speaking. Chạy: python3 tools/gen_lop4_on2b.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g4_exam import *

MP = 'thuvienhoclieu.com-Nghe-De-on-tap-HK2-Tieng-Anh-4-global-Success-De-%d.mp3'
SRC_N = 'Nghe-De-on-tap-HK2-Tieng-Anh-4-global-Success-De-%d'
SRC_D = 'De-on-tap-HK2-Tieng-Anh-4-global-Success-De-%d'
TFH = ' (True = tick ✓, False = cross ✗)'


def mk(n):
    src = (SRC_N if n <= 12 else SRC_D) % n
    return Exam('on2_de%d' % n, 'OnHK2', 'Ôn HK2 – Đề %d' % n, src, slug='test%02d' % n, minutes=35, warn_at=5, audio=[MP % n])


def imgp(ex, nm):
    return '<img class="wide" src="%s" alt="Tranh">' % ex.asset(nm)


def listen_number(ex, gid, instr, pics, labels, keys, scripts, example=''):
    """Nghe và đánh số: pics a-e, keys = nhãn tranh cho câu 1..4."""
    nm = ex.strip(pics, labels, '%s.png' % gid, w=150, h=125)
    items = []
    for i, (k, s) in enumerate(zip(keys, scripts), 1):
        items.append(({'t': 'mcq', 'plain': True, 'q': 'Nghe câu số %d: câu đó ứng với tranh nào?' % i, 'o': list(labels)}, k,
                      'Theo bài nghe: “%s” → tranh %s.' % (s, k)))
    ex.add(gid, instr + (' ' + example if example else ''), items, passage=imgp(ex, nm))


def listen_match(ex, gid, instr, pics, labels, keys, scripts):
    nm = ex.strip(pics, labels, '%s.png' % gid, w=150, h=125)
    left = [{'t': 'Nghe câu số %d' % i} for i in range(1, len(keys) + 1)]
    ex.match(gid, instr, left, list(labels), keys,
             'Theo bài nghe: ' + '; '.join('câu %d “%s” → %s' % (i, s, k) for i, (s, k) in enumerate(zip(scripts, keys), 1)), picture=imgp(ex, nm))


def pic_rows(ex, gid, instr, rows):
    """rows: [(num, [imgA,imgB,imgC], key, script)] – nghe, chọn tranh A/B/C."""
    items = []
    for num, pics, key, script in rows:
        nm = ex.strip(pics, ['A', 'B', 'C'], '%s_%d.png' % (gid, num), w=150, h=125)
        items.append(({'t': 'mcq', 'plain': True, 'wide': True, 'img': nm, 'q': 'Nghe câu số %d và chọn tranh đúng.' % num, 'o': ['A', 'B', 'C']}, key,
                      'Theo bài nghe: “%s” → tranh %s.' % (script, key)))
    ex.add(gid, instr, items)


def tf_pics(ex, gid, instr, rows):
    """rows: [(num, img, 'T'|'F', script)] – nghe, tranh có khớp không?"""
    items = []
    for num, im, a, script in rows:
        nm = ex.single(im, '%s_%d.png' % (gid, num), w=210, h=150)
        items.append(({'t': 'tf', 'q': 'Nghe câu số %d: nội dung nghe có khớp với tranh không?%s' % (num, TFH), 'img': nm}, a,
                      'Theo bài nghe: “%s” → %s với tranh.' % (script, 'khớp' if a == 'T' else 'không khớp')))
    ex.add(gid, instr, items)


def fill_listen(ex, gid, instr, rows):
    """rows: [(q, [đáp án], script)]"""
    ex.fill(gid, instr, [(q, a, None, 'Theo bài nghe: “%s” → %s' % (s, a[0])) for q, a, s in rows])


def mcq_pics_q(ex, gid, instr, rows):
    """Đọc: câu hỏi + 3 tranh A/B/C. rows: [(câu, [3 ảnh], key)]"""
    items = []
    for i, (q, pics, key) in enumerate(rows, 1):
        nm = ex.strip(pics, ['A', 'B', 'C'], '%s_%d.png' % (gid, i), w=150, h=125)
        items.append(({'t': 'mcq', 'plain': True, 'wide': True, 'img': nm, 'q': q, 'o': ['A', 'B', 'C']}, key, 'Đáp án: %s (khớp với nội dung câu).' % key))
    ex.add(gid, instr, items)


def order_rows(ex, gid, instr, rows):
    """rows: [(words_str 'a/ b/ c', [đáp án,...])] ; words tách theo '/' """
    out = []
    for w, a in rows:
        ws = [t for x in w.split('/') for t in x.split() if t not in ('.', '?', '!')]    # mỗi từ một chip
        a0 = a[0] if isinstance(a, list) else a
        pu = a0[-1]
        if pu in '.?!' and not any(t.endswith(pu) for t in ws):     # dấu câu cuối: dính vào từ cuối của câu đáp án
            last = a0.split()[-1].rstrip('.?!').lower()
            for j in range(len(ws) - 1, -1, -1):
                if ws[j].lower() == last or ws[j].lower().endswith(' ' + last):
                    ws[j] += pu; break
        out.append((ws, a))
    items = [({'t': 'order', 'q': 'Sắp xếp thành câu đúng:', 'words': w}, a if isinstance(a, list) else [a], 'Câu đúng: ' + (a[0] if isinstance(a, list) else a)) for w, a in out]
    ex.add(gid, instr, items)


# =====================================================================  ĐỀ 10  (có đáp án chính thức)
ex = mk(10)
listen_number(ex, 'l1', 'Question 1. Listen and number (nghe và đánh số).', ['img01', 'img02', 'img03', 'img04', 'img05'], list('ABCDE'),
              ['D', 'C', 'A', 'E'], ['Where do you live? – I live at 21 Tran Hung Dao Street.', 'What does he do? – He is a policeman.',
                                      'What do you do in the morning? – I wash the dishes.', 'She cooks meals for her family on Sundays.'], '(Ví dụ: câu 0 – tranh B.)')
tf_pics(ex, 'l2', 'Question 2. Listen and tick or cross (nghe, tranh đúng thì tick ✓, sai thì cross ✗).',
        [(1, 'img08', 'T', 'This is my friend Doraemon. He has a round face.'), (2, 'img09', 'F', 'Do you want to go to the water park when it’s sunny? – Great! Let’s go!'),
         (3, 'img10', 'T', 'The T-shirt is fifty thousand dong.'), (4, 'img11', 'T', 'Why do you like lions? – Because they roar very loudly.')])
ex.tf('l3', 'Question 3. Listen and tick true or false (nghe và chọn đúng/sai).',
      [('My brother has small eyes.', 'T', None, 'Bài nghe: “He has small eyes.” → True.'), ('I clean the floor at night.', 'F', None, 'Bài nghe: “I clean the floor at noon.” → False.'),
       ('She goes to the sports center on Saturdays.', 'F', None, 'Bài nghe: “She goes to the Sports Center on Sundays.” → False.'), ('The hat is ninety-nine thousand dong.', 'T', None, 'Bài nghe: “It is 99,000 dong.” → True.')])
nm = ex.strip(['img13', 'img14', 'img15', 'img16', 'img17'], list('ABCDE'), 'r1.png', w=150, h=125)
ex.match('r1', 'Question 4. Read and match (đọc và nối câu với tranh). Ví dụ: “Where do you live? – I live in a village.” → B.',
         [{'t': 'Does she work at a hospital? – No, she doesn’t. She works at a nursing home.'}, {'t': 'What do you do in the evening? – I help my mother with the cooking.'},
          {'t': 'What does it say? – It says “GO”.'}, {'t': 'What animals do you like? – I like lions because they roar loudly.'}],
         list('ABCDE'), ['C', 'A', 'E', 'D'], 'Đáp án của đề: 1–C, 2–A, 3–E, 4–D.', picture=imgp(ex, nm))
ex.mcq_text('r2', 'Question 5. Read and choose A, B or C (đọc và chọn đáp án đúng).', [
    (None, 'What does your mother ____________? – She is tall and slim.', ['look like', 'like', 'look']),
    (None, 'My father wants some grapes and beans. He goes to the _____________.', ['cinema', 'supermarket', 'swimming pool']),
    (None, 'Why do you like birds? – Because they ________________.', ['run quickly', 'roar loudly', 'sing merrily'])], ['A', 'B', 'C'])
ex.tf('r3', 'Question 6. Read and tick True or False (đọc đoạn văn, chọn đúng/sai).',
      [('The weather is windy and sunny.', 'F', None, 'Đoạn văn: “The weather is windy.” và sau đó “it is rainy” → không có “sunny”: False.'),
       ('My brother and I go swimming.', 'T', None, 'Đoạn văn: “My brother and I go swimming in the swimming pool.” → True.'),
       ('We watch films at home because it is rainy.', 'T', None, 'Đoạn văn: “But it is rainy, we must come back and watch films at home.” → True.')],
      passage='<p>Today is Sunday. The weather is windy. We are at the water park in the morning. My brother and I go swimming in the swimming pool. In the afternoon, we go on a picnic. '
              'My father will help my mother with cooking. But it is rainy, we must come back and watch films at home.</p><p><i>Ví dụ: “Today is Friday.” → False.</i></p>')
ex.fill('w1', 'Question 7. Reorder the letters to make a word (sắp xếp chữ cái thành từ, nhìn tranh). Ví dụ: s T i t r h → T-shirt.', [
    ('c o p i e l a n m → {_}', ['policeman'], 'img19', 'policeman = cảnh sát.'), ('k o p s o b o h → {_}', ['bookshop'], 'img20', 'bookshop = hiệu sách.'),
    ('i l c o d e r c o → {_}', ['crocodile'], 'img21', 'crocodile = cá sấu.'), ('d o u c l y → {_}', ['cloudy'], 'img22', 'cloudy = nhiều mây.')])
order_rows(ex, 'w2', 'Question 8. Reorder the words to make complete sentences (sắp xếp từ thành câu đúng).', [
    ('the/ Turn/ to/ get/ stall./ to/ left/ food', 'Turn left to get to the food stall.'), ('much/ this/ is/ bag?/ How', 'How much is this bag?'),
    ('the/ Because/ roar/ lions/ loudly.', 'Because the lions roar loudly.'), ('Sundays./ My/ washes/ clothes/ the/ mother/ on', 'My mother washes the clothes on Sundays.')])
ex.fill('w3', 'Question 9. Answer the questions with the given words (trả lời bằng từ cho sẵn). Ví dụ: What does his father do? (factory worker) – He’s a factory worker.', [
    ('What’s the weather like today? (sunny and windy)<br>{_}', ['It’s sunny and windy', 'It is sunny and windy'], None, 'Đáp án của đề: It’s sunny and windy.'),
    ('How can I get to the cinema? (go straight, turn right)<br>{_}', ['Go straight and turn right', 'Go straight then turn right', 'Go straight, turn right'], None, 'Đáp án của đề: Go straight and turn right.')])
ex.notes.append('có đáp án chính thức; bỏ Speaking')
ex.save()

# =====================================================================  ĐỀ 11
ex = mk(11)
listen_number(ex, 'l1', 'Question 1. Listen and number (nghe và đánh số).', ['img03', 'img01', 'img02', 'img05', 'img04'], list('abcde'),
              ['c', 'e', 'b', 'd'], ['What do you do in the morning? – I wash my clothes.', 'What does he do on Sundays? – He watches films.',
                                      'What does it say? – It says turn left.', 'Do you want to go to the food stall? – Great! Let’s go!'], '(Ví dụ: câu 0 – tranh a.)')
pic_rows(ex, 'l2', 'Question 2. Listen and circle the correct answer A, B or C (nghe và chọn tranh đúng).', [
    (1, ['img08', 'img09', 'img10'], 'A', 'What does your mother do? – She’s a farmer.'),
    (2, ['img11', 'img04', 'img12'], 'C', 'Where does he go on Saturdays? – He goes to the Sports Centre.'),
    (3, ['img15', 'img14', 'img13'], 'B', 'What was the weather like last weekend? – It was rainy.'),
    (4, ['img18', 'img17', 'img16'], 'C', 'When do you watch TV? – I watch TV at noon.')])
fill_listen(ex, 'l3', 'Question 3. Listen and write the missing words (nghe và điền từ). Ví dụ: How can I get to the supermarket? – Turn right.', [
    ('A: Where does she go on Saturdays?<br>B: She goes to the {_}.', ['cinema'], 'She goes to the cinema.'),
    ('A: What does she look like?<br>B: She has {_}.', ['short hair'], 'She has short hair.'),
    ('A: When do you watch TV?<br>B: I watch TV {_}.', ['in the morning'], 'I watch TV in the morning.'),
    ('A: What is the road like?<br>B: It’s a {_}.', ['noisy road', 'noisy'], 'It’s a noisy road.')])
ex.match('r1', 'Question 4. Read and match (đọc và nối). Ví dụ: Where does your father work? – c. He works at a store.',
         [{'t': '1. What does your sister look like?'}, {'t': '2. What does he do on Sundays?'}, {'t': '3. Do you want to go to the cinema?'},
          {'t': '4. What does it say?'}, {'t': '5. How much is the T-shirt?'}],
         ['a. It’s fifty thousand dong.', 'b. It says “turn left”.', 'd. He cooks meals.', 'e. She is slim.', 'f. Great! Let’s go.'],
         ['e. She is slim.', 'd. He cooks meals.', 'f. Great! Let’s go.', 'b. It says “turn left”.', 'a. It’s fifty thousand dong.'],
         'Đáp án: 1–e, 2–d, 3–f, 4–b, 5–a (ghép theo nghĩa).')
ex.tf('r2', 'Question 5. Read and write Yes or No (đọc đoạn văn: Yes = True, No = False). Ví dụ: Tri is a pupil at Le Manh Trinh Primary school. → Yes.', [
    ('He usually goes to the zoo in the morning.', 'F', None, 'Đoạn văn: “I usually go to the cinema in the morning” → No (False).'),
    ('Dung is very slim with a round face.', 'T', None, 'Đoạn văn: “She is very slim with a round face.” → Yes (True).'),
    ('The book shop is near Tri’s house.', 'T', None, 'Đoạn văn: “the bookshop near our house” → Yes (True).'),
    ('The English book is 30,000 dong.', 'T', None, 'Đoạn văn: “It’s thirty thousand dong.” → Yes (True).'),
    ('They love peacocks because they roar loudly.', 'F', None, 'Đoạn văn: “We love lions because they roar loudly.” (lions, không phải peacocks) → No (False).')],
      passage='<p>I’m Tri. I’m a pupil at Le Manh Trinh Primary school. On Sundays, I usually go to the cinema in the morning and watch films with my sister, Dung. '
              'She is very slim with a round face. She also wants to the bookshop near our house to buy an English book. It’s thirty thousand dong. In the afternoon, we go to the zoo. '
              'We can see many peacocks and lions. We love lions because they roar loudly. We have a lot of fun on Sundays.</p>')
ex.fill('r3', 'Question 6. Look and write (nhìn tranh và hoàn thành câu). Ví dụ: What does your mother do? – She is a farmer.', [
    ('How much is the T-shirt?<br>It’s {_}.', ['seventy thousand dong', 'seventy thousand', '70,000 dong', '70.000 dong'], 'img20', 'Áo có giá 70.000đ: seventy thousand dong.'),
    ('What do you do in the morning?<br>I {_}.', ['wash the dishes', 'wash dishes', 'wash my dishes', 'do the dishes'], 'img21', 'Tranh cô bé rửa bát: wash the dishes.'),
    ('Do you want to go to the bakery?<br>{_}', ['Sorry, I can’t', 'Sorry, I can not', 'No, I don’t', 'No, thanks'], 'img22', 'Biển “NO” → từ chối: Sorry, I can’t.'),
    ('Why do you like giraffes?<br>Because they run {_}.', ['quickly'], 'img23', 'Giraffes chạy nhanh: Because they run quickly.')])
order_rows(ex, 'w1', 'Question 7. Rearrange the words to make complete sentences (sắp xếp từ thành câu đúng).', [
    ('My/ eyes/ grandfather/ has/ big/ .', 'My grandfather has big eyes.'), ('the/ I/ do/ in/ afternoon/ the/ housework/ .', 'I do the housework in the afternoon.'),
    ('was/ last/ rainy/ It/ Sapa/ in/ Sunday/ .', 'It was rainy in Sapa last Sunday.'),
    ('and/ is/ shop/ sports/ food/ The/ between/ the/ shop/ the/ bookshop/ .', ['The food shop is between the sports shop and the bookshop.', 'The sports shop is between the food shop and the bookshop.']),
    ('like/ lions/ they/ loudly/ They/ because/ roar/ .', 'They like lions because they roar loudly.')])
ex.notes.append('không có key: đáp án nghe từ phiên âm mp3; Q2.2 (Sports Centre -> tranh quần vợt) hơi suy đoán; bỏ Q6.2 (tranh cậu bé, không rõ đáp án); bỏ Speaking')
ex.save()

# =====================================================================  ĐỀ 12
ex = mk(12)
listen_match(ex, 'l1', 'Question 1. Listen and draw lines (nghe và nối số với tranh). Ví dụ: 0 – c.', ['img07', 'img01', 'img02', 'img03', 'img04'], list('abcde'),
             ['e', 'a', 'b', 'd'], ['What are these animals? – The hippos.', 'When do you watch TV? – I watch TV in the morning.',
                                    'How can I get to the bakery? – Turn right/round (còn lại là tranh b).', 'Where’s the bookshop? – It’s opposite the sports shop.'])
pic_rows(ex, 'l2', 'Question 2. Listen and tick the correct answer (nghe và chọn tranh đúng).', [
    (1, ['img11', 'img09', 'img10'], 'A', 'What do you do in the afternoon? – I clean the floor.'),
    (2, ['img14', 'img13', 'img12'], 'B', 'Where does she work? – She works at a school.'),
    (4, ['img20', 'img19', 'img18'], 'A', 'Where does he go on Saturdays? – He goes to the swimming pool.')])
fill_listen(ex, 'l3', 'Question 3. Listen and complete each question with ONE word (nghe và điền một từ). Ví dụ: What does she look like? – She is slim.', [
    ('A: How much is the T-shirt?<br>B: It’s {_} thousand dong.', ['fifty'], 'It’s 50,000 dong.'),
    ('A: What was the weather like last weekend?<br>B: It was {_}.', ['sunny'], 'It was sunny.'),
    ('A: Where do you live?<br>B: I live at nine Quang Trung {_}.', ['Road'], 'I live at 9 Quang Trung Road.'),
    ('A: What does she do on {_}?<br>B: She cooks meals.', ['Sundays'], 'What does she do on Sundays? – She cooks meals.')])
ex.mcq_text('r1', 'Question 4. Read and tick (nhìn tranh, chọn câu đúng). Ví dụ: (biển rẽ trái) A. It says “turn left”.', [
    ('img23', 'Chọn câu đúng với tranh:', ['She has white hair.', 'She has big eyes.']),
    ('img24', 'Chọn câu đúng với tranh:', ['Do you want to go to the book shop? – Great! Let’s go.', 'Do you want to go to the supermarket? – Great! Let’s go.']),
    ('img25', 'Chọn câu đúng với tranh:', ['She goes to the cinema on Saturdays.', 'She goes to the shopping centre on Saturdays.']),
    ('img26', 'Chọn câu đúng với tranh:', ['How can I get to the bakery? – Go straight and turn left.', 'How can I get to the bakery? – Turn round.']),
    ('img27', 'Chọn câu đúng với tranh:', ['The pen is fifty thousand dong.', 'The pen is twenty thousand dong.'])], ['B', 'A', 'B', 'B', 'B'],
    exps=['Cô bé tóc đen, mắt to: She has big eyes.', 'Tranh hiệu sách: book shop.', 'Tranh trung tâm mua sắm: shopping centre.',
          'Mũi tên quay đầu (U-turn) quanh tiệm bánh: Turn round.', 'Bút giá 20.000đ: twenty thousand dong.'])
ex.match('r2', 'Question 5. Read and match (đọc và nối). Ví dụ: What does she do? – f. She is an actor.',
         [{'t': '1. What does he look like?'}, {'t': '2. How much is the skirt?'}, {'t': '3. Why do you like giraffes?'}, {'t': '4. Where is the sports centre?'}, {'t': '5. What are they doing?'}],
         ['a. Because they run quickly.', 'b. They are telling a story.', 'c. He is big.', 'd. It’s behind the gift shop.', 'e. It’s seventy thousand dong.'],
         ['c. He is big.', 'e. It’s seventy thousand dong.', 'a. Because they run quickly.', 'd. It’s behind the gift shop.', 'b. They are telling a story.'],
         'Đáp án: 1–c, 2–e, 3–a, 4–d, 5–b (ghép theo nghĩa).')
ex.tf('r3', 'Question 6. Read and decide the statements True (T) or False (F) (đọc và chọn đúng/sai). Ví dụ: Last weekend was rainy. → T.', [
    ('Hoang Hoa Tham Street is a busy street.', 'T', None, 'Đoạn văn: “It’s a busy street.” → True.'),
    ('The English book is sixty thousand dong.', 'F', None, 'Đoạn văn: “It’s fifty thousand dong.” → False.'),
    ('Her friend wants to go to the cinema to watch films.', 'T', None, 'Đoạn văn: “Hoa wants to go to the cinema to watch films.” → True.'),
    ('The cinema is in Hoang Hoa Tham Street.', 'F', None, 'Đoạn văn: rạp ở Tran Xuan Soan Street → False.'),
    ('The cinema is very big.', 'T', None, 'Đoạn văn: “It’s very big.” → True.')],
      passage='<p>Last weekend, it was rainy. Jenny didn’t go out. It’s nice today. Jenny wants to go to the bookshop. The bookshop is in Hoang Hoa Tham Street. It’s a busy street. '
              'She wants to buy an English book. It’s fifty thousand dong.</p><p>Her friend, Hoa wants to go to the cinema to watch films. The cinema is in Tran Xuan Soan Street near the swimming pool. '
              'She can go straight and turn right. The cinema is on the right. It’s very big.</p>')
order_rows(ex, 'w1', 'Question 7. Rearrange the words to make complete sentences (sắp xếp từ thành câu đúng). Ví dụ: The supermarket is behind the swimming pool.', [
    ('hippos / They / are/ .', 'They are hippos.'), ('roar / because / they / I / lions / like / loudly/ .', 'I like lions because they roar loudly.'),
    ('How / the / much / school / is / bag/ ?', 'How much is the school bag?'),
    ('like / the / in / weather / was / What / Thanh Hoa/ last / weekend/ ?', 'What was the weather like in Thanh Hoa last weekend?'),
    ('sister / look / your / like / What / does/ ?', 'What does your sister look like?')])
ex.notes.append('không có key: đáp án nghe từ phiên âm mp3; Q1.3 (b) suy ra bằng loại trừ (băng nói “Turn round/right”); bỏ Q2.3 (đường “noisy”: tranh B hay C không chắc); bỏ Speaking')
ex.save()

# =====================================================================  ĐỀ 13
ex = mk(13)
listen_number(ex, 'l1', 'Question 1. Listen and number (nghe và đánh số).', ['img01', 'img05', 'img04', 'img02', 'img03'], list('abcde'),
              ['b', 'c', 'e', 'a'], ['Where’s the bookshop? – It’s behind the bakery.', 'When do you watch TV? – I watch TV in the evening.',
                                    'What does she do on Sundays? – She does yoga.', 'What does it say? – It says “Go straight!”'], '(Ví dụ: câu 0 – tranh d.)')
pic_rows(ex, 'l2', 'Question 2. Listen and circle the correct pictures (nghe và chọn tranh đúng).', [
    (1, ['img09', 'img11', 'img10'], 'C', 'What does he do on Sundays? – He plays tennis.'),
    (2, ['img12', 'img13', 'img14'], 'A', 'What’s the street like? – It’s a busy street.'),
    (3, ['img17', 'img16', 'img15'], 'B', 'What was the weather like last weekend? – It was windy!'),
    (4, ['img20', 'img19', 'img18'], 'C', 'Where’s the bookshop? – It’s between the gift shop and the bakery.')])
fill_listen(ex, 'l3', 'Question 3. Listen and write the missing words (nghe và điền từ). Ví dụ: What does it say? – It says “Stop”.', [
    ('A: Where does he work?<br>B: He works {_}.', ['at a factory', 'at the factory', 'in a factory'], 'He works at a factory.'),
    ('A: How much is the pen?<br>B: It’s twenty {_} dong.', ['thousand'], 'It’s 20,000 dong.'),
    ('A: Do you want to go to the {_}?<br>B: Great! Let’s go.', ['supermarket'], 'Do you want to go to the supermarket?'),
    ('A: Where do you live?<br>B: I live at {_} Tran Hung Dao Street.', ['81', 'eighty-one', 'eighty one'], 'I live at 81 Tran Hung Dao Street.')])
CLOUD = Image.open('/home/claude/g4/exi/De-on-tap-HK2-Tieng-Anh-4-global-Success-De-15/img11.png').convert('RGB')   # tranh trời nhiều mây (ảnh gốc của đề 13 bị lỗi định dạng EMF)
tf_rows = [('What do you do in the morning?<br>– I wash the clothes.', 'T', 'img24', 'Tranh cô bé giặt quần áo → khớp (tick ✓).'),
           ('What was the weather like last weekend?<br>– It was windy.', 'F', CLOUD, 'Tranh trời nhiều mây (cloudy), không phải windy → cross ✗.'),
           ('Why do you like peacocks?<br>– Because they dance beautifully.', 'T', 'img26', 'Tranh chim công xòe đuôi → khớp (tick ✓).'),
           ('Where does your brother work?<br>– He works at a bank.', 'F', 'img27', 'Tranh người nông dân (farmer), không phải bank → cross ✗.'),
           ('How much is the pen?<br>– It’s fifteen thousand dong.', 'F', 'img28', 'Bút giá 25.000đ, không phải fifteen → cross ✗.')]
items = []
for i, (q, a, im, e) in enumerate(tf_rows, 1):
    items.append(({'t': 'tf', 'q': q + '<br>(Câu trả lời có đúng với tranh không?)', 'img': ex.single(im, 'r1_%d.png' % i, w=200, h=150)}, a, e))
ex.add('r1', 'Question 4. Look, read and put a tick or cross (nhìn tranh, đọc: đúng ✓ = True, sai ✗ = False). Ví dụ: She has round face ✓; She is big ✗.', items)
ex.mcq_text('r2', 'Question 5. Read and choose the correct answer (chọn đáp án đúng). Ví dụ: Do you want to go to the food stall? (A. to go)', [
    (None, '………… is the road like? – It’s a noisy road.', ['How', 'Why', 'Who', 'What']),
    (None, 'Why does she like giraffes? – ………… they run quickly.', ['But', 'Because', 'And', 'So']),
    (None, 'Where’s the Sports shop? – ………………', ['I went to the Sports shop last weekend', 'I like the Sports shop.', 'It’s near the pets shop.', 'It’s quiet.']),
    (None, 'What does it say? – It ……… “stop”.', ['say', 'saying', 'to say', 'says']),
    (None, 'When do you watch TV? – I watch TV ……… the evening.', ['in', 'at', 'on', 'for'])], ['D', 'B', 'C', 'D', 'A'])
ex.fill('r3', 'Question 6. Look and write (nhìn tranh, viết từ/cụm từ đúng). Ví dụ: (tranh con phố yên tĩnh) → quiet.', [
    ('Tranh người làm việc văn phòng (gợi ý: 6 + 6 chữ cái): {_}', ['office worker'], 'img06', 'office worker = nhân viên văn phòng.'),
    ('Tranh người tập yoga (gợi ý: 6 chữ cái): {_}', ['do yoga', 'doyoga'], 'img03', 'do yoga = tập yoga.'),
    ('Tranh mặt trời (gợi ý: 5 chữ cái): {_}', ['sunny'], 'img29', 'sunny = có nắng.'),
    ('Biển báo (gợi ý: 9 chữ cái): {_}', ['turn right', 'turnright'], 'img30', 'Biển rẽ phải: turn right.'),
    ('Tranh các cửa hàng, mũi tên chỉ cửa hàng giữa (gợi ý: 8 chữ cái): {_}', ['bookshop', 'book shop'], 'img18', 'Mũi tên chỉ “BOOKSHOP” (cửa hàng giữa): bookshop.')])
order_rows(ex, 'w1', 'Question 7. Rearrange the words to make complete sentences (sắp xếp từ thành câu đúng).', [
    ('What\'s / the / like / street/ ?', 'What\'s the street like?'), ('the / floor / in / the / afternoon / I / clean/ .', 'I clean the floor in the afternoon.'),
    ('weather / yesterday / like / What / the / Hue / in / was/ ?', 'What was the weather like in Hue yesterday?'),
    ('left / turn / go / the / I / to / bakery / get / can / to / and / straight/ .', 'I can go straight and turn left to get to the bakery.'),
    ('because / merrily / Her / birds / friends / they / like / sing/ .', 'Her friends like birds because they sing merrily.')])
ex.notes.append('không có key: đáp án nghe từ phiên âm mp3, đọc/viết suy từ nội dung; Q4.2 dùng ảnh mây của Đề 15 (ảnh gốc lỗi); Q6.5 hơi suy đoán (bookshop vs gift shop); bỏ Speaking')
ex.save()

# =====================================================================  ĐỀ 14
ex = mk(14)
tf_pics(ex, 'l1', 'Question 1. Listen and tick or cross (nghe, tranh đúng thì tick ✓, sai thì cross ✗). Ví dụ: 0 – ✗.', [
    (1, 'img07', 'T', 'What does he look like? – He’s short.'), (2, 'img06', 'F', 'How can I get to the supermarket? – Turn right. (tranh là tiệm bánh, không khớp)'),
    (3, 'img05', 'T', 'Where do you live? – I live in Tran Hung Dao Street.'), (4, 'img04', 'T', 'What are these animals? – They’re crocodiles!')])
pic_rows(ex, 'l2', 'Question 2. Listen and circle A, B or C (nghe và chọn tranh đúng).', [
    (1, ['img14', 'img13', 'img12'], 'C', 'Do you want to go to the bookshop? – Sorry, I can’t.'),
    (2, ['img17', 'img16', 'img15'], 'A', 'What does she look like? – She’s tall.'),
    (3, ['img20', 'img18', 'img19'], 'B', 'What does it say? – It says turn right.'),
    (4, ['img22', 'img23', 'img21'], 'B', 'How much is it? – It’s 90,000 dong.')])
fill_listen(ex, 'l3', 'Question 3. Listen and complete (nghe và hoàn thành câu). Ví dụ: What do you do in the morning? → I wash my clothes.', [
    ('Do you want to go to the food store?<br>→ {_}', ['Great! Let’s go', 'Great, let’s go', 'Great! Let’s go!'], 'Great! Let’s go!'),
    ('What does it say?<br>→ It says “{_}”.', ['turn left'], 'It says turn left.'),
    ('What does he do on Sundays?<br>→ He {_}.', ['watches films', 'watches a film', 'watches movies', 'watches TV'], 'He watches films.'),
    ('What does she look like?<br>→ She has {_}.', ['long hair'], 'She has long hair.')])
ex.mcq_words('r1', 'Question 4. Read and odd one out (chọn từ khác loại). Ví dụ: Street – Road – City – Busy → D.', [
    ['nursing home', 'bank', 'policeman', 'hospital'], ['swimming pool', 'cinema', 'water park', 'between'], ['weather', 'cloudy', 'rainy', 'windy'],
    ['beautifully', 'sunny', 'loudly', 'merrily'], ['crocodile', 'giraffe', 'clothes', 'hippo']], ['C', 'D', 'A', 'B', 'C'], q='Chọn từ khác loại.',
    exps=['policeman là nghề nghiệp; còn lại là nơi chốn.', 'between là giới từ; còn lại là địa điểm.', 'weather là danh từ; còn lại là tính từ chỉ thời tiết.',
          'sunny là tính từ; còn lại là trạng từ chỉ cách thức.', 'clothes là quần áo; còn lại là con vật.'])
ex.fill('r2', 'Question 5. Read and complete with one word or phrase (đọc và hoàn thành). Ví dụ: Her name is Jenny.', [
    ('Jenny’s mother is a {_}.', ['nurse'], None, 'Đoạn văn: “my mother is a nurse”.'), ('The street is {_}.', ['quiet'], None, 'Đoạn văn: “It’s a quiet street.”'),
    ('{_}, it was rainy.', ['Last weekend'], None, 'Đoạn văn: “Last weekend, it was rainy”.'), ('The zoo is {_} the house.', ['behind'], None, 'Đoạn văn: “the zoo behind our house”.'),
    ('Jenny loves peacocks because they {_}.', ['dance beautifully'], None, 'Đoạn văn: “because they dance beautifully”.')],
        passage='<p>I’m Jenny. My father is a farmer and my mother is a nurse. We live at 8 Thanh Nam Street. It’s a quiet street. My father works on the farm every day but my mother doesn’t work at a hospital at the weekend. '
                'Last weekend, it was rainy but today it’s sunny. We are going to the zoo behind our house. I love peacocks there because they dance beautifully.</p>')
ex.fill('r3', 'Question 6. Look and write (nhìn tranh và hoàn thành câu). Ví dụ: What does it say? – It says “go straight”.', [
    ('What does he do?<br>He is {_}.', ['an office worker', 'office worker', 'a office worker'], 'img25', 'Tranh người làm việc ở bàn giấy: an office worker.'),
    ('When do you watch TV?<br>I watch TV {_}.', ['in the evening', 'at night', 'in the night'], 'img27', 'Đồng hồ 7:30 pm, trời tối: in the evening.'),
    ('Where’s the book shop?<br>It’s {_} the sports shop.', ['opposite'], 'img26', 'Hiệu sách đối diện hiệu đồ thể thao: opposite.'),
    ('What are these animals?<br>They are {_}.', ['lions'], 'img28', 'Hai con sư tử: lions.'),
    ('How can I get to the supermarket?<br>Go straight and {_}.', ['turn left'], 'img20', 'Biển rẽ trái: turn left.')])
order_rows(ex, 'w1', 'Question 7. Rearrange the words to make complete sentences (sắp xếp từ thành câu đúng).', [
    ('is / dong / thousand / seventy / The / skirt', 'The skirt is seventy thousand dong.'), ('these / animals / What / are/ ?', 'What are these animals?'),
    ('He / a / up / at / is / tent / the / putting / campsite', 'He is putting up a tent at the campsite.'),
    ('Do / the / want / to / me / go / park / to / you / with / water/ ?', 'Do you want to go to the water park with me?'),
    ('mother / does / on / Tuesdays / go / your / Where/ ?', 'Where does your mother go on Tuesdays?')])
ex.notes.append('không có key: đáp án nghe từ phiên âm mp3, đọc/viết suy từ nội dung; bỏ Speaking')
ex.save()

# =====================================================================  ĐỀ 15
ex = mk(15)
listen_match(ex, 'l1', 'Question 1. Listen and match (nghe và nối số với tranh). Ví dụ: 0 – d.', ['img01', 'img05', 'img04', 'img02', 'img03'], list('abcde'),
             ['a', 'e', 'b', 'c'], ['What does your father do? – He’s a farmer.', 'What do you do at noon? – I wash the dishes.',
                                    'How can I get to the bookshop? – Go straight.', 'Where’s the bookshop? – It’s near the bakery.'])
ex.mcq_text('l2', 'Question 2. Listen and circle the correct answer (nghe và chọn đáp án đúng). Ví dụ: 0. A. It was cloudy.', [
    (None, 'Nghe câu số 1.', ['She goes to the shopping center.', 'She goes to the zoo.']),
    (None, 'Nghe câu số 2.', ['She has big ears.', 'She has long hair.']),
    (None, 'Nghe câu số 3.', ['The skirt is sixty thousand dong.', 'The skirt is eighty thousand dong.']),
    (None, 'Nghe câu số 4.', ['The mother is a nurse.', 'The mother is a farmer.'])], ['A', 'A', 'B', 'B'],
    exps=['Bài nghe: “She goes to the shopping centre.”', 'Bài nghe: “She has big e… (ears)” – không phải long hair.', 'Bài nghe: “It’s 80,000 dong.”', 'Bài nghe: “She’s a farmer.”'])
fill_listen(ex, 'l3', 'Question 3. Listen and write the missing words (nghe và điền từ). Ví dụ: I watch TV in the afternoon.', [
    ('A: How can I get to the cinema?<br>B: {_}.', ['Turn left'], 'Turn left.'), ('A: What does he {_}?<br>B: He’s big.', ['look like'], 'What does he look like? – He’s big.'),
    ('A: Where does he work?<br>B: He works {_}.', ['on a farm', 'on the farm'], 'He works on a farm.'), ('A: What are these animals?<br>B: These are {_}.', ['lions'], 'These are lions.')])
mcq_pics_q(ex, 'r1', 'Question 4. Look, read and put a tick in the box (nhìn tranh, đọc và chọn tranh đúng). Ví dụ: What does it say? – It says “Turn right” → c.', [
    ('What was the weather like last weekend? – It’s cloudy.', ['img10', 'img12', 'img11'], 'C'), ('What does your sister look like? – She is tall.', ['img14', 'img13', 'img15'], 'A'),
    ('Where’s the bookshop? – It’s behind the bakery.', ['img17', 'img16', 'img18'], 'B'), ('Why do you like peacocks? – Because they dance beautifully.', ['img21', 'img20', 'img19'], 'A'),
    ('What does she do on Sundays? – She does yoga.', ['img22', 'img23', 'img24'], 'C')])
ex.fill('r2', 'Question 5. Read and complete using words in the box (chọn từ trong khung). Ví dụ: (0) sunny.', [
    ('Chỗ trống (1): {_}', ['shopping centre'], None, 'going to the shopping centre.'), ('Chỗ trống (2): {_}', ['opposite'], None, 'It is opposite the swimming pool.'),
    ('Chỗ trống (3): {_}', ['wants'], None, 'My mum wants to buy some food (he/she/it + wants).'), ('Chỗ trống (4): {_}', ['merrily'], None, 'the birds because they sing merrily.'),
    ('Chỗ trống (5): {_}', ['thousand'], None, 'eighty-eight thousand dong.')],
        passage='<p>Today is Sunday. It’s (0) <b>sunny</b>. My mum and I are going to the <b>(1) ______</b>. It is <b>(2) ______</b> the swimming pool. My mum <b>(3) ______</b> to buy some food. '
                'I go there to buy some books about wildlife, especially the birds because they sing <b>(4) ______</b>. The books are eighty-eight <b>(5) ______</b> dong. I’m happy to have new books.</p>',
        bank=['opposite', 'thousand', 'merrily', 'wants', 'shopping centre', 'sunny'])
ex.fill('r3', 'Question 6. Order the letters (sắp xếp chữ cái thành từ, nhìn tranh). Ví dụ: s h t o r → short.', [
    ('b a r y k e → {_}', ['bakery'], 'img25', 'bakery = tiệm bánh.'), ('f m e a r r → {_}', ['farmer'], 'img26', 'farmer = nông dân.'),
    ('u r t n e f t l → {_}', ['turn left', 'turnleft'], 'img27', 'turn left = rẽ trái.'), ('c l e r o d I o c s → {_}', ['crocodiles'], 'img29', 'crocodiles = cá sấu.'),
    ('r n d o u → {_}', ['round'], 'img28', 'round = tròn (round face).')])
order_rows(ex, 'w1', 'Question 7. Rearrange the words to make complete sentences (sắp xếp từ thành câu đúng). Ví dụ: She goes to the shopping centre on Saturdays.', [
    ('you / do / When / TV / watch/ ?', 'When do you watch TV?'), ('food store / go / to / to / you / the / want / Do/ ?', 'Do you want to go to the food store?'),
    ('to / the / can / I / How / supermarket / get/ ?', 'How can I get to the supermarket?'), ('at / is / She / campsite / campfire / a / the / building/ .', 'She is building a campfire at the campsite.'),
    ('the / shop / bookshop / is / The / shop / and / sports / the / gift / between/ .', 'The bookshop is between the gift shop and the sports shop.')])
ex.notes.append('không có key (chỉ có đáp án Q4 trong đề): đáp án nghe từ phiên âm mp3; Q2.2 “big ears” (băng nghe như eyes/ears) hơi suy đoán; bỏ Speaking')
ex.save()
