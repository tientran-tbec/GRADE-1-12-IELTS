# -*- coding: utf-8 -*-
"""Nhóm on2a: Ôn HK2 – Đề 5..9 (unit OnHK2, tag on2_de5..on2_de9, slug test05..test09). Bỏ phần Speaking."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g4_exam import *
from PIL import ImageOps

SRC = 'De-on-tap-HK2-Tieng-Anh-4-global-Success-De-%d'
MP3N = 'thuvienhoclieu.com-Nghe-De-on-tap-HK2-Tieng-Anh-4-global-Success-De-%d.mp3'


def mk(n, minutes=35):
    return Exam('on2_de%d' % n, 'OnHK2', 'Ôn HK2 – Đề %d' % n, SRC % n, slug='test%02d' % n, minutes=minutes, warn_at=5, audio=[MP3N % n])


# ---------------------------------------------------------------- helpers
def img_tag(ex, name, text):
    """Ảnh + nhãn giá (vd '50k') vẽ lại vì chữ trong hộp văn bản bị mất khi tách docx."""
    im = ex.load(name).copy()
    d = ImageDraw.Draw(im)
    W, H = im.size
    f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', max(14, W // 8))
    tw = d.textlength(text, font=f)
    bw, bh = int(tw + 24), int(f.size + 16)
    x0, y0 = W - bw - 2, 2
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=8, fill='white', outline=(60, 60, 60), width=2)
    d.text((x0 + 12, y0 + 6), text, fill=(20, 20, 20), font=f)
    return im


def pic_mcq(ex, gid, instr, rows, passage=None, w=170, h=140):
    """rows: [(câu hỏi, [ảnh A, ảnh B, ...], 'B', giải thích|None)] -> mcq chọn tranh (plain)."""
    items = []
    for i, (q, pics, key, *e) in enumerate(rows, 1):
        nm = ex.strip(pics, [L(j) for j in range(len(pics))], '%s_%d.png' % (gid, i), w=w, h=h)
        items.append(({'t': 'mcq', 'plain': True, 'wide': True, 'img': nm, 'q': q, 'o': [L(j) for j in range(len(pics))]}, key,
                      (e[0] if e and e[0] else 'Đáp án: %s (theo đáp án của đề).' % key)))
    ex.add(gid, instr, items, passage=passage)


def txt_mcq(ex, gid, instr, rows, keys, passage=None, exps=None):
    """rows: [(q, [opts], img|None)] keys: chữ cái."""
    items = []
    for i, ((q, opts, *im), kk) in enumerate(zip(rows, keys)):
        it = {'t': 'mcq', 'q': q, 'o': list(opts)}
        if im and im[0]:
            it['img'] = ex.single(im[0], '%s_%d.png' % (gid, i + 1), w=200, h=150)
        items.append((it, kk, exps[i] if exps else 'Đáp án: %s. %s' % (kk, opts[letters_to_idx(kk)])))
    ex.add(gid, instr, items, passage=passage)


def sent(ex, gid, instr, rows, bank=None, imgs=None):
    """Viết câu: rows [(gợi ý, [đáp án chấp nhận])]; imgs: danh sách ảnh theo hàng (hoặc None)."""
    items = []
    for i, (p, a) in enumerate(rows):
        it = {'t': 'fill', 'q': '%s<br>→ {_}' % p}
        if imgs and imgs[i]:
            it['img'] = ex.single(imgs[i], '%s_%d.png' % (gid, i + 1), w=190, h=140)
        items.append((it, a, 'Câu đúng: %s' % a[0]))
    ex.add(gid, instr, items, bank=bank)


def img_html(ex, names, out, w=200, h=150):
    nm = ex.single(names, out, w=w, h=h)
    return '<img src="%s" alt="Hình" style="max-width:%dpx;height:auto">' % (ex.asset(nm), w)


def wide(ex, nm, alt='Hình'):
    return '<img class="wide" src="%s" alt="%s">' % (ex.asset(nm), alt)


def mirrored(ex, name):
    return ImageOps.mirror(ex.load(name))


# ================================================================ ĐỀ 5
ex = mk(5)
ex.number_pics('l1', 'Question 1. Listen and number (nghe và đánh số 1–4 cho các tranh; tranh B là ví dụ).',
               ['img01', 'img02', 'img03', 'img04', 'img05'], list('ABCDE'), [3, 0, 2, 1, 4], nums=['1', '2', '3', '4'], only=['A', 'C', 'D', 'E'])
ex.tf('l2', 'Question 2. Listen and tick (✓ = True) or cross (✗ = False) (nghe, tranh đúng thì chọn True, sai thì chọn False).',
      [('Nghe và quyết định: nội dung nghe có đúng với tranh không? (✓ = True, ✗ = False)', a, im, 'Đáp án: %s (theo đáp án của đề: %s).' % ('True' if a == 'T' else 'False', '✓' if a == 'T' else '✗'))
       for im, a in (('img08', 'T'), ('img09', 'F'), ('img10', 'T'), ('img11', 'T'))])
q3 = [('img14', ['She has small eyes.', 'He has small eyes.'], 'B'), ('img15', ['Yes, I do.', 'At noon.'], 'B'),
      ('img16', ['She goes to the sports center.', 'She has a round face.'], 'A'), ('img17', ['It’s windy.', 'They are dancing.'], 'B')]
txt_mcq(ex, 'l3', 'Question 3. Listen and choose the answer for the question (nghe câu hỏi trong bong bóng, chọn câu trả lời đúng).',
        [('Nghe câu hỏi và chọn câu trả lời đúng.', o, im) for im, o, k in q3], [k for _, _, k in q3])
pm = ex.strip(['img18', 'img19', 'img20', 'img21', 'img22'], list('ABCDE'), 'm4.png', w=170, h=140)
ex.match('r1', 'Question 4. Read and match (đọc và nối câu với tranh; tranh A đã dùng làm ví dụ).',
         [{'t': 'Does she work at a hospital? – No, she doesn’t. She works at a nursing home.'}, {'t': 'What do you do in the evening? – I help my mother with the cooking.'},
          {'t': 'What does it say? – It says “GO”.'}, {'t': 'What animals do you like? – I like lions because they roar loudly.'}],
         list('ABCDE'), ['C', 'A', 'E', 'D'],
         'Theo đáp án của đề: 1–C (bệnh viện/nhà dưỡng lão), 2–A (nấu ăn cùng mẹ), 3–E (biển báo GO), 4–D (sư tử). Tranh B (ngôi làng) là ví dụ “Where do you live?”.',
         picture=wide(ex, pm, 'Tranh A–E'))
txt_mcq(ex, 'r2', 'Question 5. Read and choose A, B or C (đọc và chọn đáp án đúng).', [
    ('What does your mother ____? – She is tall and slim.', ['look like', 'like', 'look']),
    ('My father wants some grapes and beans. He goes to the ____.', ['cinema', 'supermarket', 'swimming pool']),
    ('Why do you like birds? – Because they ____.', ['run quickly', 'roar loudly', 'sing merrily'])], ['A', 'B', 'C'],
    exps=['What does your mother look like? = Mẹ bạn trông thế nào?', 'Mua nho và đậu → đi siêu thị (supermarket).', 'Chim → hót líu lo (sing merrily).'])
P5 = ('<p>The weather is sunny today. We are at the campsite. Son is putting up a tent with Kiem. Dao and Huong are taking a photo. Hao is building a campfire to cook some food. Thuy Duong is singing a song. They are having a lot of fun together.</p>'
      + img_html(ex, ['img23'], 'p6.png', 220, 160))
ex.tf('r3', 'Question 6. Read and tick True or False (đọc đoạn văn, chọn True hoặc False).', [
    ('Son and Huong are taking a photo.', 'F', None, 'Sai: Dao and Huong are taking a photo (không phải Son).'),
    ('Kiem is putting a tent.', 'T', None, 'Đúng: Son is putting up a tent with Kiem.'),
    ('Hao wants to cook some food.', 'T', None, 'Đúng: Hao is building a campfire to cook some food.')], passage=P5)
ex.fill('w1', 'Question 7. Reorder the letters to make a word (sắp xếp các chữ cái thành từ đúng, nhìn tranh).', [
    ('c o p i e l a n m → {_}', ['policeman'], 'img25', 'policeman = cảnh sát.'),
    ('k o p s o b o h → {_}', ['bookshop'], 'img26', 'bookshop = hiệu sách.'),
    ('i l c o d e r c o → {_}', ['crocodile'], 'img27', 'crocodile = cá sấu.'),
    ('d o u c l y → {_}', ['cloudy'], 'img28', 'cloudy = nhiều mây.')])
ex.order('w2', 'Question 8. Reorder the words to make complete sentences (sắp xếp từ thành câu đúng).', [
    (['the', 'Turn', 'to', 'get', 'stall.', 'to', 'left', 'food'], 'Turn left to get to the food stall.'),
    (['much', 'this', 'is', 'bag?', 'How'], 'How much is this bag?'),
    (['the', 'Because', 'roar', 'lions', 'loudly.'], 'Because the lions roar loudly.'),
    (['Sundays.', 'My', 'washes', 'clothes', 'the', 'mother', 'on'], 'My mother washes the clothes on Sundays.')])
sent(ex, 'w3', 'Question 9. Answer the questions with the given words (dùng từ gợi ý để trả lời).', [
    ('What’s the weather like today? (sunny and windy)', ['It’s sunny and windy.', 'It is sunny and windy.']),
    ('How can I get to the cinema? (go straight, turn right)', ['Go straight and turn right.', 'Go straight, turn right.', 'Go straight then turn right.'])])
ex.notes.append('bỏ Speaking (Q10–12)')
ex.save()

# ================================================================ ĐỀ 6
ex = mk(6)
pm = ex.strip(['img01', 'img02', 'img03', 'img04', 'img05'], list('ABCDE'), 'm1.png', w=170, h=140)
ex.match('l1', 'Question 1. Listen and match (nghe và nối từng câu số 1–4 với tranh; tranh B là ví dụ).',
         [{'t': 'Câu %d' % i} for i in range(1, 5)], list('ABCDE'), ['D', 'A', 'E', 'C'],
         'Theo đáp án của đề: 1–D, 2–A, 3–E, 4–C (B là ví dụ số 0).', picture=wide(ex, pm, 'Tranh A–E'))
ex.tf('l2', 'Question 2. Listen and tick Right (✓ = True) or Wrong (✗ = False) (nghe, câu đúng chọn True, sai chọn False).', [
    ('I live in a small house in a village.', 'F'), ('She doesn’t have long hair and big eyes.', 'F'),
    ('They are crocodiles.', 'T'), ('The gift shop is between the bakery and the bookshop.', 'T')])
P6a = ('<p>My name is Lisa. I am tall and (0) <b>slim</b>. This is my father, Tony. He works in a <b>(1) ______</b>. This is my mother, Daisy. She has a <b>(2) ______</b>. She works in a school as a Maths teacher. '
       'My mother often goes to the <b>(3) ______</b> on Mondays. Today, my parents will take me to the campsite in the mountain. My class is playing <b>(4) ______</b> at the campsite. I am very happy.</p>')
ex.fill('l3', 'Question 3. Listen and complete (nghe và điền từ vào chỗ trống).', [
    ('Chỗ trống (1): {_}', ['factory'], None, 'factory = nhà máy.'), ('Chỗ trống (2): {_}', ['small face'], None, 'small face = khuôn mặt nhỏ.'),
    ('Chỗ trống (3): {_}', ['swimming pool'], None, 'swimming pool = bể bơi.'), ('Chỗ trống (4): {_}', ['tug of war'], None, 'tug of war = kéo co.')], passage=P6a)
txt_mcq(ex, 'r1', 'Question 4. Circle the odd one out (chọn từ khác loại).', [
    ('Chọn từ khác loại:', ['big', 'tall', 'eyes', 'slim']), ('Chọn từ khác loại:', ['rainy', 'sunny', 'weather', 'cloudy']),
    ('Chọn từ khác loại:', ['bakery', 'T-shirt', 'bookshop', 'supermarket']), ('Chọn từ khác loại:', ['crocodiles', 'giraffes', 'lions', 'dance'])], ['C', 'C', 'B', 'D'],
    exps=['eyes là danh từ; còn lại là tính từ.', 'weather là danh từ chung; còn lại là các kiểu thời tiết.', 'T-shirt là quần áo; còn lại là cửa hàng.', 'dance là động từ; còn lại là con vật.'])
P6b = ('<p>Today is Sunday. It is sunny and warm. Thuy Duong likes reading (0) <b>books</b>. She wants to go to the <b>(1) ______</b>. It is in Chu Van An Street. How can she get there? '
       'She can go <b>(2) ______</b> and turn right. The library is on the <b>(3) ______</b>.</p>' + img_html(ex, ['img11'], 'p5.png', 220, 160))
ex.fill('r2', 'Question 5. Fill in each blank with one given word (chọn từ trong khung điền vào chỗ trống).', [
    ('Chỗ trống (1): {_}', ['library'], None, 'Thư viện (library).'), ('Chỗ trống (2): {_}', ['straight'], None, 'go straight = đi thẳng.'),
    ('Chỗ trống (3): {_}', ['left'], None, 'on the left = bên trái.')], passage=P6b, bank=['straight', 'left', 'library', 'books'])
P6c = ('<p><b>Thang:</b> Hello, I am Thang. Today is Saturday. It is sunny and hot. Because I like swimming, my family goes to the water park. I can swim and play there.</p>'
       + img_html(ex, ['img12'], 'p6a.png', 220, 150) +
       '<p><b>Dao:</b> Hi there! I’m Dao. It is windy outside. My mother and I go to the shopping centre because my mother wants to buy clothes for winter. There is a bakery in the shopping centre. We can go there to have some cakes as well.</p>'
       + img_html(ex, ['img13'], 'p6b.png', 160, 150))
txt_mcq(ex, 'r3', 'Question 6. Read and choose A, B or C (đọc và chọn đáp án đúng).', [
    ('Is swimming Thang’s hobby?', ['Yes, it is.', 'No, it isn’t.', 'No information is given.']),
    ('Where is Dao?', ['She is in the water park with her family.', 'She is in the bakery.', 'She is in the shopping centre with her mother.']),
    ('Why do Dao and her mother go to the shopping centre?', ['Because she wants some cakes.', 'Because her mother wants to buy clothes.', 'Because they want to go to the bakery.'])],
    ['A', 'C', 'B'], passage=P6c)
ex.fill('w1', 'Question 7. Fill in the blanks (nhìn tranh, điền từ vào chỗ trống).', [
    ('Where’s the gift shop?<br>It is {_} the bookshop and the food stall.', ['between'], 'img15', 'between … and … = ở giữa … và …'),
    ('What are they doing?<br>They are {_}.', ['playing tug of war'], 'img16', 'playing tug of war = chơi kéo co.'),
    ('How much is this skirt?<br>It is {_}.', ['ninety thousand dong', 'ninety thousand'], 'img17', '90,000 đồng = ninety thousand dong.'),
    ('Why do you like peacocks?<br>Because they {_}.', ['dance beautifully'], 'img18', 'Công múa đẹp: dance beautifully.')])
sent(ex, 'w2', 'Question 8. Use the given words to make sentences (dùng từ gợi ý viết thành câu hoàn chỉnh).', [
    ('What/ you/ do/ morning?', ['What do you do in the morning?']),
    ('I/ live/ 12 Tran Hung Dao Street', ['I live at 12 Tran Hung Dao Street.', 'I live at 12 Tran Dung Dao Street.']),
    ('Do/ you/ want/ go/ supermarket?', ['Do you want to go to the supermarket?'])])
sent(ex, 'w3', 'Question 9. Answer the questions with the given words (dùng từ gợi ý để trả lời).', [
    ('When do you wash the clothes? (afternoon)', ['I wash the clothes in the afternoon.']),
    ('What does your father do on Saturdays? (play tennis)', ['He plays tennis on Saturdays.', 'My father plays tennis on Saturdays.']),
    ('What are Huong and Son doing? (build/ campfire)', ['They are building a campfire.'])])
ex.notes.append('bỏ Speaking (Q10–12); đáp án Q8.2 trong key ghi nhầm “Tran Dung Dao” (chấp nhận cả hai)')
ex.save()

# ================================================================ ĐỀ 7
ex = mk(7)
ex.tf('l1', 'Question 1. Listen and tick (✓ = True) or cross (✗ = False) (nghe, tranh đúng thì chọn True, sai thì chọn False; tranh A là ví dụ).', [
    ('Nghe và quyết định: nội dung nghe có đúng với tranh không? (✓ = True, ✗ = False)', a, im, 'Đáp án: %s (theo đáp án của đề: %s).' % ('True' if a == 'T' else 'False', '✓' if a == 'T' else '✗'))
    for im, a in (('img02', 'F'), ('img03', 'T'), ('img04', 'F'), ('img05', 'T'))])
items = []
for i, (im, k) in enumerate((('img07', 'A'), ('img08', 'B'), ('img09', 'B'), ('img10', 'A')), 1):
    items.append(({'t': 'mcq', 'q': 'Nghe và chọn Yes hoặc No cho tranh này.', 'o': ['Yes', 'No'], 'img': ex.single(im, 'l2_%d.png' % i, w=200, h=150)}, k,
                  'Đáp án: %s (theo đáp án của đề).' % ('Yes' if k == 'A' else 'No')))
ex.add('l2', 'Question 2. Listen and write Yes or No (nghe, chọn Yes hoặc No cho mỗi tranh).', items)
P7a = ('<p><b>Boy:</b> Hi, can I ask you some questions for my assignment?<br><b>Girl:</b> (0) <b>Yes</b>, please go ahead.<br><b>Boy:</b> What do you do <b>(1) ______</b>?<br><b>Girl:</b> I do my homework.<br>'
       '<b>Boy:</b> What about your sister? What does she do at noon?<br><b>Girl:</b> She <b>(2) ______</b>.<br><b>Boy:</b> OK, I already take note. Now, I want to go to the <b>(3) ______</b>. Where’s it?<br>'
       '<b>Girl:</b> It’s in Green Street.<br><b>Boy:</b> How can I get there?<br><b>Girl:</b> You can <b>(4) ______</b> and turn left.</p>')
ex.fill('l3', 'Question 3. Listen to the dialogue and complete (nghe đoạn hội thoại và điền từ).', [
    ('Chỗ trống (1): {_}', ['at noon'], None, 'Đáp án theo đề: at noon.'), ('Chỗ trống (2): {_}', ['cooks meal', 'cooks meals', 'cooks a meal'], None, 'Đáp án theo đề: cooks meal(s).'),
    ('Chỗ trống (3): {_}', ['bookshop'], None, 'bookshop = hiệu sách.'), ('Chỗ trống (4): {_}', ['go straight'], None, 'go straight and turn left = đi thẳng rồi rẽ trái.')], passage=P7a)
pic_mcq(ex, 'r1', 'Question 4. Read and choose A, B or C (đọc và chọn tranh đúng).', [
    ('The gift shop is between the bookshop and the bakery.', ['img14', 'img15', 'img16'], 'B'),
    ('What do your parents look like? – My father is big and tall, and my mother is slim and short.', ['img17', 'img18', 'img19'], 'C'),
    ('What was the weather like last weekend? – It was windy and rainy.', ['img20', 'img21', 'img22'], 'A'),
    ('How can I get to the water park? – Go straight, turn left, then turn right. The water park is on the left.',
     [[mirrored(ex, 'img23'), 'img24', 'img23'], ['img24', 'img23', mirrored(ex, 'img23')], ['img24', mirrored(ex, 'img23'), 'img23']], 'C',
     'Đáp án C: đi thẳng, rẽ trái, rồi rẽ phải. (Các mũi tên được dựng lại từ ảnh gốc đã bị mất chiều.)')], w=190, h=110)
ex.match('r2', 'Question 5. Read and match (nối câu hỏi với câu trả lời; câu 0 “How much is the skirt?” – C là ví dụ).',
         [{'t': 'Why do you like giraffes?'}, {'t': 'What’s Huong doing?'}, {'t': 'What does your sister do on Sundays?'}],
         ['Because they run quickly.', 'She helps my mother with the housework.', 'It’s eighty thousand dong.', 'She’s taking a photo.'],
         ['Because they run quickly.', 'She’s taking a photo.', 'She helps my mother with the housework.'],
         'Theo đáp án của đề: 1–A, 2–D, 3–B (C là ví dụ).')
P7b = ('<p>Thuy Duong loves the weekends so much. On Saturdays, her mother brings her to the supermarket to buy groceries and milk in the morning. On Saturday afternoon, Thuy Duong’s favorite hobby is flying a kite with her father. '
       'Or they cycle around the village. On Sundays, the family clean the house and cook meals together. They love watching television or listening to music on Sunday evening. They are a happy family.</p>' + img_html(ex, ['img25'], 'p6.png', 200, 160))
ex.tf('r3', 'Question 6. Read and tick True or False (đọc đoạn văn, chọn True hoặc False).', [
    ('Thuy Duong likes flying a kite with her father on Saturdays.', 'T', None, 'Đúng: On Saturday afternoon … flying a kite with her father.'),
    ('On Sundays, her family do housework and cook meals together.', 'T', None, 'Đúng: On Sundays, the family clean the house and cook meals together.'),
    ('Her family love watching television or listening to music on Saturday evening.', 'F', None, 'Sai: họ xem tivi/nghe nhạc vào tối Chủ nhật (Sunday evening).')], passage=P7b)
ex.fill('w1', 'Question 7. Fill in the blanks to make complete words (nhìn tranh, điền từ hoàn chỉnh; gợi ý một số chữ cái).', [
    ('F _ _ _ _ _ Y → {_}', ['factory'], 'img27', 'factory = nhà máy.'),
    ('_ I _ _ _ → {_}', ['hippo'], 'img28', 'hippo = hà mã.'),
    ('T _ _ _ R _ U _ _ → {_} (2 từ, gõ cách nhau)', ['turn round', 'turnround', 'turn around'], 'img29', 'turn round = quay đầu (TURN ROUND).'),
    ('_ I _ _ M _ R _ _ _ _ → {_} (2 từ, gõ cách nhau)', ['sing merrily', 'singmerrily'], ['img30', 'img31'], 'sing merrily = hót líu lo.')])
ex.order('w2', 'Question 8. Reorder the words to make complete sentences (sắp xếp từ thành câu đúng).', [
    (['campfire.', 'The', 'girls', 'around', 'are', 'the', 'dancing'], 'The girls are dancing around the campfire.'),
    (['in', 'water', 'The', 'park', 'Street.', 'is', 'Lac', 'Long', 'Quan'], 'The water park is in Lac Long Quan Street.'),
    (['the', 'My', 'clothes', 'washes', 'in', 'the', 'mother', 'evening.'], 'My mother washes the clothes in the evening.')])
sent(ex, 'w3', 'Question 9. Look at the pictures and answer the questions (nhìn tranh, trả lời câu hỏi).', [
    ('Where does your sister go on Saturdays?', ['She goes to the cinema on Saturdays.', 'She goes to the cinema.']),
    ('What’s the weather like today?', ['It’s sunny.', 'It is sunny.']),
    ('What does she do in the morning?', ['She does yoga in the morning.', 'She does yoga.'])], imgs=['img33', 'img34', 'img35'])
ex.notes.append('bỏ Speaking (Q10–12); mũi tên Q4.4 dựng lại bằng lật ảnh; Q3.(1)=at noon theo key')
ex.save()

# ================================================================ ĐỀ 8
ex = mk(8)
skirts = [img_tag(ex, 'img11', '50k'), img_tag(ex, 'img12', '60k'), img_tag(ex, 'img13', '60k')]
pic_mcq(ex, 'l1', 'Question 1. Listen and tick A, B or C (nghe và chọn tranh đúng).', [
    ('Nghe và chọn tranh đúng.', ['img04', 'img05', 'img06'], 'A'), ('Nghe và chọn tranh đúng.', ['img07', 'img08', 'img09'], 'B'),
    ('Nghe và chọn tranh đúng.', skirts, 'C'), ('Nghe và chọn tranh đúng.', ['img14', 'img15', 'img16'], 'B')])
P8a = ('<p>Ví dụ (0): <i>Where do you live? – I live in Quang Trung Street.</i> (hội thoại số 0). Nghe và điền số thứ tự 1–4 cho các hội thoại còn lại.</p>')
ex.match('l2', 'Question 2. Listen and order the dialogue (nghe và đánh số thứ tự các hội thoại).', [
    {'t': 'A: What does she look like? – B: She is fat and tall.'},
    {'t': 'A: Sorry, I want to go to the bakery. It is in Oxford Street. – B: You can turn round.'},
    {'t': 'A: What does he do? – B: He is a policeman.'},
    {'t': 'A: What was the weather like last weekend? – B: It was cloudy.'}],
    ['1', '2', '3', '4'], ['4', '3', '1', '2'], 'Theo đáp án của đề: she look like = 4; bakery = 3; he do = 1; weather = 2 (hội thoại “Where do you live?” là số 0).', picture=P8a)
P8b = ('<p>It is a nice day today. The weather is (0) <b>windy</b> and cloudy. In the morning, my family will go to the zoo to see some animals. We all like <b>(1) ______</b> because they have a long neck and legs. '
       'After the zoo, we will go to the <b>(2) ______</b> in the afternoon. Some of my friends are already there. They’re playing <b>(3) ______</b>. I promise to help my mom with <b>(4) ______</b> in the evening.</p>')
ex.fill('l3', 'Question 3. Listen to the passage and complete (nghe đoạn văn và điền từ).', [
    ('Chỗ trống (1): {_}', ['giraffes'], None, 'giraffes = hươu cao cổ.'), ('Chỗ trống (2): {_}', ['campsite'], None, 'campsite = khu cắm trại.'),
    ('Chỗ trống (3): {_}', ['card games'], None, 'card games = trò chơi bài.'), ('Chỗ trống (4): {_}', ['cooking'], None, 'help my mom with cooking = giúp mẹ nấu ăn.')], passage=P8b)
txt_mcq(ex, 'r1', 'Question 4. Read and answer the question by choosing A, B or C (chọn câu trả lời đúng).', [
    ('How can I get to the water park?', ['It’s so hot.', 'Turn left and go straight.', 'It’s in the busy city.']),
    ('Why do you like peacocks?', ['Because they run slowly.', 'Because they roar loudly.', 'Because they dance beautifully.']),
    ('What does your sister do on Sundays?', ['She goes to the cinema with her friends.', 'She likes running.', 'She hates cooking.'])], ['B', 'C', 'A'],
    exps=['Hỏi đường → Turn left and go straight.', 'Công → múa đẹp (dance beautifully).', 'Hỏi việc làm vào Chủ nhật → She goes to the cinema with her friends.'])
P8c = ('<p>Ginny and her mother are at a (0) <b>shopping</b> centre. Ginny wants to buy some stationery. They go to the <b>(1) ______</b>. The pen is ten thousand dong. The notebook is fifteen <b>(2) ______</b> dong. '
       'And the school bag is <b>(3) ______</b> thousand dong. Ginny buys two pens, a notebook, and a school bag. She is very happy with her new school things.</p>' + img_html(ex, ['img18'], 'p5.png', 240, 140))
ex.fill('r2', 'Question 5. Fill in each blank with one given word (chọn từ trong khung điền vào chỗ trống).', [
    ('Chỗ trống (1): {_}', ['bookshop'], None, 'They go to the bookshop (mua đồ dùng học tập).'), ('Chỗ trống (2): {_}', ['thousand'], None, 'fifteen thousand dong.'),
    ('Chỗ trống (3): {_}', ['ninety'], None, 'ninety thousand dong.')], passage=P8c, bank=['thousand', 'bookshop', 'ninety', 'shopping'])
ex.match('r3', 'Question 6. Reorder the sentences to make a complete conversation (sắp xếp thành hội thoại: chọn vị trí 2–5 của từng câu; câu “Hello Ben, look at this road sign. What does it say?” đã đứng đầu, là vị trí 1).',
         [{'t': 'Oh, ok. How can I get to the food stall, Ben?'}, {'t': 'Go straight, turn left, and turn right. The food stall is on the right.'},
          {'t': 'Thank you, Ben. Have a good day!'}, {'t': 'It says “Go straight”, Lucy.'}],
         ['2', '3', '4', '5'], ['3', '4', '5', '2'],
         'Thứ tự đúng (theo đề): 2 – 5 – 1 – 3 – 4, tức: Hello Ben… → It says “Go straight” → Oh, ok. How can I get… → Go straight, turn left… → Thank you, Ben.',
         picture='<p><b>1.</b> Hello Ben, look at this road sign. What does it say?</p>')
ex.fill('w1', 'Question 7. Fill in the blanks with suitable words (nhìn tranh, điền từ phù hợp).', [
    ('I help my mom with the housework {_}.', ['in the evening'], 'img20', 'in the evening = vào buổi tối.'),
    ('My brother {_} on Saturdays.', ['cooks meals', 'cooks meal'], 'img21', 'cooks meals = nấu ăn.'),
    ('It’s {_} today.', ['rainy'], 'img22', 'rainy = có mưa.'),
    ('They are playing {_}.', ['tug of war'], 'img23', 'tug of war = kéo co.')])
ex.order('w2', 'Question 8. Reorder the words to make complete sentences (sắp xếp từ thành câu đúng).', [
    (['dishes?', 'do', 'wash', 'you', 'When', 'the'], 'When do you wash the dishes?'),
    (['sports', 'goes', 'to', 'the', 'Saturdays.', 'father', 'centre', 'My', 'on'], 'My father goes to the sports centre on Saturdays.'),
    (['they', 'because', 'I', 'horses', 'like', 'quickly.', 'run'], 'I like horses because they run quickly.')])
sent(ex, 'w3', 'Question 9. Use the given words to make sentences (dùng từ gợi ý viết thành câu hoàn chỉnh).', [
    ('I/ live/ 84 Tran Hung Dao Street', ['I live at 84 Tran Hung Dao Street.']),
    ('turn left/ turn right/ hospital.', ['Turn left and turn right to get to the hospital.']),
    ('bookshop/ near/ gift shop.', ['The bookshop is near the gift shop.'])])
ex.notes.append('bỏ Speaking (Q10–12); nhãn giá 50k/60k Q1.3 vẽ lại; key ghi nhầm “Satudays” (sửa thành Saturdays)')
ex.save()

# ================================================================ ĐỀ 9
ex = mk(9)
pm = ex.strip(['img02', 'img03', 'img04', img_tag(ex, 'img05', '50k'), 'img06'], list('ABCDE'), 'm1.png', w=170, h=140)
ex.match('l1', 'Question 1. Listen and draw lines (nghe và nối từng câu số 1–4 với tranh; tranh C là ví dụ số 0).',
         [{'t': 'Câu %d' % i} for i in range(1, 5)], list('ABCDE'), ['A', 'E', 'B', 'D'],
         'Theo đáp án của đề: 1–A, 2–E, 3–B, 4–D (C là ví dụ số 0).', picture=wide(ex, pm, 'Tranh A–E'))
ex.tf('l2', 'Question 2. Listen and choose True or False (nghe, chọn True hoặc False).', [
    ('She looks young with short hair.', 'T'), ('I play basketball with my friends in the morning.', 'F'),
    ('The teacher is building a campfire.', 'T'), ('These animals are peacocks.', 'F')])
P9a = ('<p><b>Lucy:</b> Hello. My name is Lucy. I am (0) ______ of my family. We are having dinner. This man is my father. He is a <b>(1) ______</b>. He works very hard at a ______. '
       'That woman is my mother. Every Sunday, my mother does <b>(2) ______</b> at the ______.</p><p><i>Ví dụ (0): A. drawing a picture (Lucy đang vẽ tranh).</i></p>')
txt_mcq(ex, 'l3a', 'Question 3a. Listen to the passage (Lucy) and choose the correct answer (nghe và chọn đáp án đúng).', [
    ('(1) This man is Lucy’s father. He is a ____ . He works very hard at a ____ .', ['doctor / hospital', 'worker / factory', 'farmer / farm']),
    ('(2) Every Sunday, Lucy’s mother does ____ at the ____ .', ['yoga / gym', 'exercise / gym', 'yoga / sport center'])], ['B', 'A'], passage=P9a)
P9b = ('<p><b>Nam:</b> Hi everyone, I am Nam. The weather was <b>(3) ______</b> yesterday, so we were at a bookshop. It is next to the pet shop. My sister bought some books. It is <b>(4) ______</b> dong. We had a lot of fun.</p>'
       + img_html(ex, ['img09'], 'p3b.png', 120, 180))
txt_mcq(ex, 'l3b', 'Question 3b. Listen to the passage (Nam) and choose the correct answer (nghe và chọn đáp án đúng).', [
    ('(3) The weather yesterday was ____ .', ['sunny', 'windy', 'cloudy']),
    ('(4) The books are ____ dong.', ['fifty thousand', 'forty thousand', 'thirty thousand'])], ['A', 'C'], passage=P9b)
P9c = ('<p>Good morning, everyone! My name is Thuy Duong. I get up at six thirty (0) <b>in the morning</b>. I go to school at seven thirty. I have lunch at school with my classmates at noon. I go home at <b>(1) ______</b>. '
       'I help my mom <b>(2) ______</b> in the evening. We have dinner at seven o’clock. After dinner, I <b>(3) ______</b>. I go to bed at nine thirty. Can you tell me about your daily routines?</p>'
       + img_html(ex, ['img10'], 'p4.png', 130, 200))
ex.fill('r1', 'Question 4. Fill in each blank with one given phrase of words (chọn cụm từ trong khung điền vào chỗ trống).', [
    ('Chỗ trống (1): {_}', ['five o’clock', 'five'], None, 'I go home at five o’clock.'), ('Chỗ trống (2): {_}', ['with the cooking'], None, 'help my mom with the cooking = giúp mẹ nấu ăn.'),
    ('Chỗ trống (3): {_}', ['wash the dishes'], None, 'After dinner, I wash the dishes.')], passage=P9c, bank=['five o’clock', 'wash the dishes', 'with the cooking', 'in the morning'])
txt_mcq(ex, 'r2', 'Question 5. Read and choose A, B or C (đọc và chọn đáp án đúng).', [
    ('Where does your brother go ____ Sundays?', ['at', 'in', 'on']), ('Do you want to go ____ the cinema?', ['in', 'to', 'for']),
    ('The kids are dancing ____ the campfire.', ['in', 'on', 'around']), ('Nam and I are ____ the shopping centre.', ['at', 'on', 'under'])], ['C', 'B', 'C', 'A'],
    exps=['on Sundays = vào các ngày Chủ nhật.', 'go to the cinema = đi xem phim.', 'dancing around the campfire = nhảy quanh đống lửa trại.', 'at the shopping centre = ở trung tâm mua sắm.'])
P9d = ('<p>Hello, I’m Harry. It is sunny today. I and my family are at the zoo. I and my sister like the animals at the zoo. Look! They are lions. I like them because they roar loudly. These are hippos. They are swimming in the pond. '
       'I can see two giraffes. They are running very quickly on the field. My sister, Linda, likes birds because they sing merrily. She can see a couple of peacocks. She likes them because they dance beautifully. We have a lot of fun at the zoo!</p>'
       + img_html(ex, ['img11'], 'p6.png', 230, 150))
ex.tf('r3', 'Question 6. Read and tick True or False (đọc đoạn văn, chọn True hoặc False).', [
    ('The giraffes are running slowly on the field.', 'F', None, 'Sai: giraffes … running very quickly.'),
    ('Harry likes lions because they roar loudly.', 'T', None, 'Đúng: I like them because they roar loudly.'),
    ('Linda likes peacocks because they sing merrily.', 'F', None, 'Sai: Linda thích công vì chúng múa đẹp (dance beautifully); “sing merrily” là lý do thích chim.')], passage=P9d)
cl = ex.load('img16')
sign = Image.new('RGB', (230, 110), 'white')
sign.paste(cl.crop((10, 10, 118, 119)), (4, 0)); sign.paste(cl.crop((14, 277, 124, 386)), (120, 0))
ex.fill('w1', 'Question 7. Fill in the blanks (nhìn tranh, điền từ vào chỗ trống).', [
    ('Do you want to go to the {_}?<br>Great! Let’s go.', ['bakery'], 'img13', 'bakery = tiệm bánh.'),
    ('Where’s the bookshop?<br>It’s {_} the bakery.', ['opposite'], 'img14', 'opposite = đối diện.'),
    ('What do you do in the evening?<br>I {_} in the evening.', ['clean the floor'], 'img15', 'clean the floor = lau/dọn sàn nhà.'),
    ('How can I get to the food stall?<br>Go straight and {_}.', ['turn left'], sign, 'Biển báo: đi thẳng rồi rẽ trái (turn left).')])
sent(ex, 'w2', 'Question 8. Answer the questions with the given words (dùng từ gợi ý để trả lời).', [
    ('What does your sister look like? (short, big)', ['She is short and big.', 'She’s short and big.', 'She is short and big']),
    ('What does your mother do on Sundays? (clean the house)', ['She cleans the house on Sundays.', 'She cleans the house.']),
    ('How much is this book? (forty-five thousand dong)', ['It’s forty-five thousand dong.', 'It is forty-five thousand dong.'])])
sent(ex, 'w3', 'Question 9. Use the given words to make sentences (dùng từ gợi ý viết thành câu hoàn chỉnh).', [
    ('Why/ you/ like/ elephants?', ['Why do you like elephants?']),
    ('Kids/ dancing/ around the campfire.', ['The kids are dancing around the campfire.', 'Kids are dancing around the campfire.']),
    ('I/ like/ peacocks/ because/ dance beautifully.', ['I like peacocks because they dance beautifully.'])])
ex.notes.append('bỏ Speaking (Q10–12); nhãn 50k Q1 vẽ lại; biển báo Q7.4 cắt từ ảnh gốc')
ex.save()
