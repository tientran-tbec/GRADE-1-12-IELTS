# -*- coding: utf-8 -*-
"""Cuối kỳ 1 – Đề 17..21 (25-26). Dựng tay vì bố cục docx lộn xộn (đã đối chiếu bản render PDF)."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g4_exam import *

P = 'De-on-tap-cuoi-HK-1-Tieng-Anh-4-Global-25-26-De-%d'
A = 'thuvienhoclieu.com-Nghe-De-on-tap-cuoi-HK-1-Tieng-Anh-4-Global-25-26-De-%d.mp3'


def new(n):
    return Exam('ck1_de%d' % n, 'CuoiKy1', 'Cuối kỳ 1 – Đề %d (25-26)' % n, P % n, slug='test%02d' % (n - 12),
                minutes=35, warn_at=5, audio=[A % n])


def tick(ex, pics, keys):
    ex.mcq_pics('a1', 'I. Listen and tick (nghe và chọn tranh đúng).', pics, keys)


def number(ex, pics, keys):
    """pics: 4 ảnh A-D; keys: chữ cái của tranh ứng với câu 1..4"""
    nm = ex.strip(pics, list('ABCD'), 'a2.png', w=150, h=125)
    items = [({'t': 'mcq', 'plain': True, 'q': 'Nghe câu số %d: câu đó ứng với tranh nào?' % (i + 1), 'o': list('ABCD')}, k,
              'Câu %d ứng với tranh %s (theo đáp án của đề).' % (i + 1, k)) for i, k in enumerate(keys)]
    ex.add('a2', 'II. Listen and number (nghe và chọn tranh cho từng câu).', items,
           passage='<img class="wide" src="%s" alt="Tranh A-D">' % ex.asset(nm))


def tickcross(ex, imgs2, keys):
    ex.tf('a3', 'III. Listen and tick or cross (nghe, nội dung nghe có khớp với tranh không?).',
          [('Nội dung nghe có đúng với tranh không? (đúng = True, sai = False)', k, im,
            'Đáp án: %s (theo đáp án của đề: %s).' % ('True' if k == 'T' else 'False', '✓' if k == 'T' else '✗')) for im, k in zip(imgs2, keys)])


def lw(ex, rows):
    ex.fill('a4', 'IV. Listen and write (nghe và điền từ).', rows)


def ordw(ex, gid, rows):
    out = []
    norm = lambda t: t.strip('.?!,').lower()
    for doc, ans in rows:
        toks = [t for t in re.split(r'[/\s]+', doc) if t and t not in ('.', '?', '!')]
        at = ans.split()
        used, words = set(), []
        for t in toks:
            j = next(i for i, a in enumerate(at) if i not in used and norm(a) == norm(t))
            used.add(j); words.append(at[j])
        assert len(used) == len(at), (doc, ans)
        out.append((words, ans))
    ex.order(gid, 'Reorder the words (sắp xếp từ thành câu đúng).', out)


def pic_choice(ex, gid, instr, rows, keys):
    items = []
    for i, ((q, pics), k) in enumerate(zip(rows, keys), 1):
        nm = ex.strip(pics, list('AB'), '%s_%d.png' % (gid, i), w=170, h=140)
        items.append(({'t': 'mcq', 'plain': True, 'wide': True, 'img': nm, 'q': q, 'o': ['A', 'B']}, k,
                      'Đáp án: %s (theo đáp án của đề).' % k))
    ex.add(gid, instr, items)


def match_pics(ex, gid, instr, texts, pics, keys, note):
    lab = list('abcdef')
    nm = ex.strip(pics, lab, '%s.png' % gid, w=130, h=110)
    ex.match(gid, instr, [{'t': t} for t in texts], lab, keys,
             'Đáp án: ' + ', '.join('%d–%s' % (i + 1, k) for i, k in enumerate(keys)),
             picture='<img class="wide" src="%s" alt="Tranh a-f">' % ex.asset(nm))


def para(t):
    return '<p>' + t + '</p>'


# ================================================================ Đề 17
ex = new(17)
tick(ex, [['img07', 'img05'], ['img08', 'img06'], ['img09', 'img10'], ['img11', 'img12']], 'ABBA')
number(ex, ['img19', 'img13', 'img14', 'img18'], 'BCDA')
tickcross(ex, ['img24', 'img23'], 'TF')
lw(ex, [("A: Where’s he from?<br>B: He’s from {_}.", ['Malaysia']),
        ("A: What subjects do you have today?<br>B: I have {_}.", ['Science'])])
ex.tf('b1', 'I. Look, read and write true (T) or false (F).', [
    ('A: Where were you last weekend? B: I was on the beach.', 'T', 'img27'),
    ('My favourite subject is English. I want to be an English teacher.', 'F', 'img28'),
    ('My school is in the city.', 'F', 'img29'),
    ('A: What time do you go to school? B: I go to school at six thirty.', 'T', ['img30', 'img31']),
    ('My friend is from America.', 'F', 'img32')])
t17 = ('Hi! My name is Bao. I’m ten years old and I am a student at a primary school. My school is in the village and it is near my house. '
       'Everyday, I often get up at six o’clock. After breakfast, I ride my bike to school at six forty – five. I have many subjects at school, but my favourite subject is English. '
       'I want to be an English teacher. Mai is my best friend in my class. Her favourite subject is music, because she wants to be a singer.')
ex.fill('b2', 'II. Read and complete the sentences (đọc đoạn văn và điền từ).', [
    ('Bao’s school is in the {_}.', ['village']), ('He gets up at {_}.', ['6 o’clock', 'six o’clock', '6', 'six']),
    ('Bao’s favourite subject is {_}.', ['English']), ('Bao wants to be a(n) {_}.', ['English teacher']),
    ('Mai’s favourite subject is music. She wants to be a(n) {_}.', ['singer'])], passage=para(t17))
ex.fill('c1', 'I. Look and complete (nhìn tranh, điền từ).', [
    ('I {_} at 9.30.', ['go to bed'], 'img34'), ('Last Sunday, I was {_}.', ['at the zoo'], 'img35'),
    ('There are three {_} at my school.', ['buildings'], 'img36'), ('I like art, because I want to be a {_}.', ['painter'], 'img37'),
    ('A: What do you want to drink?<br>B: I want some {_}.', ['lemonade'], 'img38')])
ordw(ex, 'c2', [('yesterday?/ were/ Where/ you/', 'Where were you yesterday?'), ('on/ Sundays/ I/ listen/ music/ to/.', 'I listen to music on Sundays.'),
                ('music/ have/ I/ on/ Thursdays/.', 'I have music on Thursdays.'), ('six forty-five./ breakfast/ at/ I/ have/', 'I have breakfast at six forty-five.'),
                ('subject/ is/ My/ favourite/ maths/.', 'My favourite subject is maths.')])
ex.notes += ['bỏ Speaking', 'Nghe III: tick/cross -> True/False theo key', 'C.II.5 key ghi "Math" nhưng từ cho sẵn là "maths": dùng "maths"']
ex.save()

# ================================================================ Đề 18
ex = new(18)
tick(ex, [['img06', 'img07'], ['img08', 'img05'], ['img09', 'img10'], ['img11', 'img12']], 'BAAB')
number(ex, ['img17', 'img16', 'img15', 'img14'], 'CDBA')
tickcross(ex, ['img25', 'img24'], 'TF')
lw(ex, [("A: When do you have {_}?<br>B: I have it on Wednesday.", ['music']), ("Our sports day is in {_}.", ['February'])])
match_pics(ex, 'b1', 'I. Look, read and match (đọc câu và chọn tranh a–f).',
           ['A: How many playgrounds are there at your school? B: There is one.', 'A: What do you do on Sundays? B: I do housework.',
            'I was on the beach yesterday.', 'My birthday is in July.', 'A: Why do you like music? B: Because I want to be a singer.'],
           ['img29', 'img30', 'img26', 'img27', 'img28', 'img31'], list('fe' + 'acb'), '')
t18 = ('Hello, everyone. My name is Uyen. At school, I have many (0) <u>friends</u>. We can do different things. Thu can play (1) ______, but she (2) ______ swim. '
       'Nam can roller skate, but he can’t (3) ______ a horse. Linh likes music so much. She can play both the (4) ______ and the guitar well. '
       'I can (5) ______, but I can’t play sports. We can all ride a bike. Everyday, we often go to school by bike together.')
ex.fill('b2', 'II. Read and complete the sentences (chọn từ trong khung).', [('Chỗ trống (%d): {_}' % (i + 1), [a]) for i, a in enumerate(
    ['badminton', 'can’t', 'ride', 'piano', 'draw'])], passage=para(t18), bank=['draw', 'friends', 'ride', 'badminton', 'can’t', 'piano'])
ex.fill('c1', 'I. Look and complete (nhìn tranh, điền từ).', [
    ('My friends want some {_}.', ['grapes'], 'img32'), ('I {_} at 6.45.', ['go to school'], 'img34'),
    ('I like art because I want to be a {_}.', ['painter'], 'img35'), ('There are two {_} at my school.', ['buildings'], 'img36'),
    ('My friend, Hakim is from {_}.', ['Malaysia'], 'img37')])
ordw(ex, 'c2', [('music/ on/ have/ Mondays/ I/ .', 'I have music on Mondays.'), ('birthday/ is/ My/ in/ August/.', 'My birthday is in August.'),
                ('subject/ art/ My/ is/ favourite/.', 'My favourite subject is art.'), ('get up/ at/ five thirty/ I/.', 'I get up at five thirty.'),
                ('at/ school/ many/ gardens/ How/ are/ your/ there/ ?', 'How many gardens are there at your school?')])
ex.notes += ['bỏ Speaking', 'B.I key ghi "1.D" nhưng d là tranh ví dụ (đồng hồ); câu 1 (playground) -> f (theo nghĩa)',
             'C.II: sửa lỗi gõ trong key (iss, garderns); câu 4 thêm dấu chấm; câu 5 từ cho sẵn "you" -> "your"']
ex.save()

# ================================================================ Đề 19
ex = new(19)
tick(ex, [['img07', 'img05'], ['img08', 'img06'], ['img09', 'img10'], ['img12', 'img11']], 'BAAB')
number(ex, ['img13', 'img14', 'img15', 'img06'], 'CADB')
tickcross(ex, ['img23', 'img24'], 'FT')
lw(ex, [("A: I can fly a kite.<br>B: I can {_}.", ['skip']), ("A: What do you do on {_}?<br>B: I go to school.", ['Wednesdays', 'Wednesday'])])
pic_choice(ex, 'b1', 'I. Look, read and tick the correct picture (đọc câu và chọn tranh đúng).', [
    ('A: What day is it today? B: It’s Tuesday.', ['img27', 'img28']), ('My favourite subject is PE.', ['img31', 'img29']),
    ('A: What time do you go to school? B: I go to school at 7.15.', ['img30', 'img32']),
    ('I was at the campsite last weekend.', ['img36', 'img33']), ('A: What do you want to eat? B: I want some jam.', ['img35', 'img34'])], 'BBABA')
t19 = ('Hello, everyone. My name is Duong and I’m 10 years old. I’m a student at a primary school. It’s big and it is in the village. There are three buildings and a large garden at our school. '
       'The garden has a lot of trees and flowers. There is a big and beautiful playground at my school, too. Students often play sports and games there at break time. '
       'Nam is my penpal friend. His school is in the city. It’s a big and modern school in Ha Noi. There are two computer rooms and four high buildings at his school. '
       'I wish I will have a chance to visit his school some day.')
ex.fill('b2', 'II. Read the passage and answer the questions (đọc và trả lời câu hỏi).', [
    ('Where is Duong’s school?<br>{_}', ['It’s in the village.', 'In the village.', 'In the village', 'village']),
    ('How many buildings are there at his school?<br>{_}', ['There are three.', 'There are three buildings.', 'three', '3']),
    ('Is there a garden at his school?<br>{_}', ['Yes, there is.', 'Yes']),
    ('Where is Nam’s school?<br>{_}', ['It’s in the city.', 'In the city.', 'In the city', 'city']),
    ('How many computer rooms are there at Nam’s school?<br>{_}', ['There are two.', 'There are two computer rooms.', 'two', '2'])], passage=para(t19))
ex.fill('c1', 'I. Look and complete (nhìn tranh, điền từ).', [
    ('I have {_} and Vietnamese on Mondays.', ['maths', 'math'], 'img38'), ('I was in the {_} last weekend.', ['countryside'], 'img39'),
    ('I get up at {_} everyday.', ['5.45', 'five forty-five', 'five forty five'], 'img40'),
    ('A: What do you do on Sundays?<br>B: I {_}.', ['listen to music'], 'img41'),
    ('A: What do you want to eat?<br>B: I want some {_}.', ['grapes'], ['img42', 'img43', 'img44'])])
ordw(ex, 'c2', [('big/ There/ a/ is/ at/ playground/ school/ my/', 'There is a big playground at my school.'),
                ('some/ want/ lemonade/ I/.', 'I want some lemonade.'), ('breakfast/ I/ at/ 6.30/ have/.', 'I have breakfast at 6.30.'),
                ('zoo/ I/ at/ the/ was/ yesterday/.', 'I was at the zoo yesterday.'),
                ('Mondays/ maths/ I/ and music/ have/ on', 'I have maths and music on Mondays.')])
ex.notes += ['bỏ Speaking', 'B.I: câu 1 (đồng hồ) là ví dụ, 5 câu còn lại theo key', 'C.II.3 key thiếu "breakfast"; C.II.5 key thiếu "and music" -> dùng đúng từ cho sẵn']
ex.save()

# ================================================================ Đề 20
ex = new(20)
tick(ex, [['img06', 'img07'], ['img05', 'img08'], ['img11', 'img09'], ['img10', 'img12']], 'BAAB')
number(ex, ['img17', 'img16', 'img15', 'img14'], 'CDBA')
tickcross(ex, ['img23', 'img24'], 'TF')
lw(ex, [("A: What do you do on Thursday?<br>B: I {_}.", ['study at school']), ("A: Where’s your school, Bill?<br>B: It’s in the {_}.", ['town'])])
ex.mcq_text('b1', 'I. Look, read and circle a or b (nhìn tranh, chọn câu đúng).', [
    (['img26'], 'Chọn câu đúng với tranh.', ['I like maths because I want to be a math teacher.', 'I like art because I want to be an art teacher.']),
    (['img27'], 'Chọn câu đúng với tranh.', ['I have breakfast at six thirty.', 'I have breakfast at six fifty.']),
    (['img28'], 'What do you want to eat?', ['I want some chips.', 'I want some grapes.']),
    (['img29'], 'What do you do on Sundays?', ['I listen to music.', 'I do housework.']),
    (['img30'], 'When’s your birthday?', ['It’s in August.', 'It’s in March.'])], 'BAABA')
t20 = ('Hello, everyone. My name is Gia Bao. I’m nine years old. I live in Nam Dinh province with my family. My school is not very big. It’s in the town. '
       'There are three buildings, a garden and a yard at my school. The garden has many trees and flowers. The playground is very big. '
       'The students can play football, badminton and skip there. I love my school because it is very beautiful.')
ex.fill('b2', 'II. Read and complete the sentences (đọc đoạn văn và điền từ).', [
    ('He is {_} years old.', ['nine', '9']), ('His school is in the {_}.', ['town']), ('There are three {_} at his school.', ['buildings']),
    ('There are many trees and flowers in the {_}.', ['garden']), ('The students can play football and skip in the {_}.', ['playground'])], passage=para(t20))
ex.fill('c1', 'I. Look and complete (nhìn tranh, điền từ).', [
    ('Can she {_}? – Yes, she can.', ['roller skate'], 'img35'), ('My favourite subject is {_}.', ['music'], 'img32'),
    ('– Were you at the {_} yesterday? – Yes, I was.', ['campsite'], 'img33'),
    ('A: What do you do on Tuesday?<br>B: I {_}.', ['study at school'], 'img36'),
    ('A: What do you want to drink?<br>B: I want some {_}.', ['lemonade'], 'img34')])
ordw(ex, 'c2', [('eat ?/ do/ What/ to/ want/ you/', 'What do you want to eat?'), ('today/ It/ Saturday/ is/.', 'It is Saturday today.'),
                ('school/ at/ go/ I/ to/6.45/ .', 'I go to school at 6.45.'), ('can/ piano/play/She/ the/.', 'She can play the piano.'),
                ('in/ last/ Da Nang/ was/ I/summer/.', 'I was in Da Nang last summer.')])
ex.notes += ['bỏ Speaking', 'B.I: câu 1 là ví dụ, 5 câu còn lại theo key', 'C.II.1 key gõ "Whatdo" -> sửa']
ex.save()

# ================================================================ Đề 21
ex = new(21)
tick(ex, [['img05', 'img06'], ['img07', 'img08'], ['img10', 'img09'], ['img11', 'img12']], 'BAAB')
number(ex, ['img17', 'img16', 'img15', 'img14'], 'BCDA')
tickcross(ex, ['img25', 'img24'], 'FT')
lw(ex, [("A: Why do you like English?<br>B: Because I want to be an English {_}.", ['teacher']),
        ("A: How many {_} are there at your school?<br>B: There are three.", ['buildings'])])
match_pics(ex, 'b1', 'I. Look, read and match (đọc câu và chọn tranh a–f).',
           ['My friend is from England.', 'I study at school on Tuesdays.', 'There is one playground at my school.',
            'A: Where were you last weekend? B: I was in the countryside.', 'A: What do you want to eat? B: I want some chips.'],
           ['img26', 'img27', 'img28', 'img29', 'img30', 'img31'], list('eabfd'), '')
t21 = ('Hello, everyone. My name is Trang. I’m a student in class 4A at a primary school. Uyen, Bao and Duong are my classmates. Uyen likes English, because she wants to be an English teacher. '
       'Bao likes P.E., because he wants to be a footballer. Duong likes art, because he wants to be a famous artist. I like music, because I want to be a singer. We are very happy at our school.')
ex.tf('b2', 'II. Read and tick True or False (đọc đoạn văn, True hay False?).', [
    ('Trang, Bao, Uyen and Duong are in the same class.', 'T'), ('Uyen likes P.E. because she wants to be a P.E. teacher.', 'F'),
    ('Bao likes English very much.', 'F'), ('Duong wants to be a famous artist.', 'T'), ('Trang wants to be a singer.', 'T')], passage=para(t21))
ex.fill('c1', 'I. Look and complete (nhìn tranh, điền từ).', [
    ('I {_} on Sundays.', ['listen to music'], 'img33'), ('– Where is your school? – It’s in the {_}.', ['village'], 'img34'),
    ('I have {_} on Tuesdays and Thursdays.', ['Science'], 'img35'), ('She can {_}.', ['ride a bike'], 'img36'),
    ('I {_} at 6.30 in the evening.', ['eat dinner', 'have dinner'], 'img37')])
ordw(ex, 'c2', [('buildings/ three/ are/ school/ my/at/ There/.', 'There are three buildings at my school.'),
                ('today/ It/ Sunday/ is/.', 'It is Sunday today.'), ('breakfast/ 6.15/eat/I/at/.', 'I eat breakfast at 6.15.'),
                ('can’t/ badminton/ I/ play/.', 'I can’t play badminton.'), ('in/ last/ Da Nang/ was/ I/weekend/.', 'I was in Da Nang last weekend.')])
ex.notes += ['bỏ Speaking', 'B.II: câu 1 (Trang is a primary student) là ví dụ; key 1-5 ứng câu 2-6', 'C.I.5 chấp nhận thêm "have dinner"']
ex.save()
