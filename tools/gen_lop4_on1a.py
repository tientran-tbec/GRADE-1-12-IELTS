# -*- coding: utf-8 -*-
"""Nhóm on1a: Đề ôn thi HK1 – Đề 5, 6, 7, 8 (Lớp 4, unit OnHK1). Bỏ Speaking.
Chạy: python3 tools/gen_lop4_on1a.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g4_exam import *

AUDIO = 'thuvienhoclieu.com-Nghe-De-on-thi-HK1-Anh-4-Global-De-%d.mp3'
IMG = lambda ex, nm: '<img class="wide" src="%s" alt="Tranh">' % ex.asset(nm)


def cloze(ex, gid, instr, passage_html, rows, keys):
    """rows: [[a,b,c]] cho từng chỗ trống (1),(2),(3); keys: 'ABC'."""
    items = []
    for i, (o, kk) in enumerate(zip(rows, keys), 1):
        items.append(({'t': 'mcq', 'q': 'Chọn từ điền vào chỗ trống (%d).' % i, 'o': list(o)}, kk,
                      'Đáp án: %s. %s' % (kk, o[letters_to_idx(kk)])))
    ex.add(gid, instr, items, passage=passage_html)


def build(n, d):
    ex = Exam('on1_de%d' % n, 'OnHK1', 'Ôn HK1 – Đề %d' % n, 'De-on-thi-HK1-Anh-4-Global-De-%d' % n, slug='test%02d' % n,
              minutes=35, warn_at=5, audio=[AUDIO % n])
    ex.notes.append('bỏ Speaking')

    # ---------------- LISTENING
    ex.mcq_pics('l1', 'Listening – Part 1. Listen and tick (nghe và chọn tranh đúng).', d['p1'], d['p1k'], exps=d['p1e'])

    # Part 2: nghe và đánh số (B là tranh ví dụ = 0)
    nm = ex.strip(d['p2'], list('ABCDE'), 'l2.png', w=150, h=125)
    items = []
    for lb, kk in zip('ABCDE', d['p2k']):
        if lb == 'B': continue
        items.append(({'t': 'mcq', 'plain': True, 'q': 'Tranh %s là câu số mấy trong bài nghe?' % lb, 'o': ['1', '2', '3', '4']}, str(kk),
                      'Tranh %s ứng với câu %s (theo đáp án của đề).' % (lb, kk)))
    ex.add('l2', 'Listening – Part 2. Listen and number (nghe và đánh số; tranh B là ví dụ).', items, passage=IMG(ex, nm))

    # Part 3: nghe và nối (câu 0 -> B là ví dụ)
    nm = ex.strip(d['p3'], list('ABCDE'), 'l3.png', w=150, h=125)
    ex.match('l3', 'Listening – Part 3. Listen and draw line (nghe và nối số thứ tự với tranh; câu 0 – tranh B là ví dụ).',
             [{'t': 'Câu %d' % i} for i in range(1, 5)], list('ABCDE'), d['p3k'],
             'Đáp án theo đáp án của đề: ' + ', '.join('%d–%s' % (i, k) for i, k in enumerate(d['p3k'], 1)), picture=IMG(ex, nm))

    # Part 4: nghe và điền từ
    ex.fill('l4', 'Listening – Part 4. Listen and write (nghe và điền từ).',
            [(q, a, None, 'Đáp án: %s' % a[0]) for q, a in d['p4']])

    # ---------------- READING
    nm = ex.strip(d['r1'], list('ABCDE'), 'r1.png', w=150, h=125)
    ex.match('r1', 'Reading – Part 1. Read and match the words with pictures (nối từ với tranh; tranh B là ví dụ).',
             [{'t': w} for w in d['r1w']], list('ABCDE'), d['r1k'],
             'Đáp án: ' + ', '.join('%s – %s' % (w, k) for w, k in zip(d['r1w'], d['r1k'])), picture=IMG(ex, nm))

    cloze(ex, 'r2', 'Reading – Part 2. Read and choose A, B or C to complete the text (đọc, chọn từ điền vào chỗ trống).',
          d['r2p'], d['r2o'], d['r2k'])

    ex.tf('r3', 'Reading – Part 3. Read and tick True or False (đọc đoạn văn, True hay False?).', d['r3'], passage=d['r3p'])

    # ---------------- WRITING
    ex.fill('w1', 'Writing – Part 1. Look at the pictures and the letters. Write the words (nhìn tranh, sắp xếp chữ cái thành từ).',
            [('Sắp xếp các chữ cái: <b>%s</b> → {_}' % s, [a], im, 'Đáp án: %s' % a) for s, a, im in d['w1']])
    ex.order('w2', 'Writing – Part 2. Rearrange the words to make the sentences (sắp xếp từ thành câu đúng).', d['w2'])

    ex.save()
    return ex


# =============================================================== ĐỀ 5
D5 = dict(
    p1=[['img06', 'img07', 'img08'], ['img09', 'img10', 'img11'], ['img12', 'img13', 'img14'], ['img15', 'img16', 'img17']], p1k='BCAB',
    p1e=['Đáp án B: tranh nho (grapes).', 'Đáp án C: tranh cậu bé chơi guitar.', 'Đáp án A: tranh cô giáo dạy tiếng Anh (“Do you speak English?”).',
         'Đáp án B: tranh cậu bé đang vẽ (painting).'],
    p2=['img18', 'img19', 'img20', 'img21', 'img22'], p2k=[2, 0, 4, 3, 1],
    p3=['img23', 'img24', 'img25', 'img26', 'img27'], p3k=['E', 'D', 'C', 'A'],
    p4=[('There’s some {_} on the table.', ['jam']), ('He’s from {_}.', ['Australia']),
        ('What day is it today? – It’s {_}.', ['Friday']), ('My favourite subject is {_}.', ['Maths', 'Math'])],
    r1=['img28', 'img29', 'img30', 'img31', 'img32'], r1w=['go to bed', 'water', 'nine forty-five', 'birthday party'], r1k=['D', 'E', 'A', 'C'],
    r2p=('<p>Hello, my name is Hoa. I’m from Viet Nam. I was on holiday in Nha Trang last summer. The beach was very beautiful. '
         'We went <b>(1) ______</b> in the sea and then built sandcastles in the afternoon.</p>'
         '<p>In the evening, we had seafood at a restaurant, it was excellent. The people were friendly <b>(2) ______</b> helpful. '
         'We also watched a film at the <b>(3) ______</b>, it was interesting. My holiday was very nice.</p>'),
    r2o=[['swimming', 'singing', 'cooking'], ['of', 'and', 'on'], ['mountain', 'hospital', 'cinema']], r2k='ABC',
    r3p=('<p>Hung is a pupil at Quang Trung Primary school. Every day he gets up at 6 o’clock. He has breakfast at six twenty and goes to school at six forty-five. '
         'School starts at 7:00 a.m and finishes at 10:30 a.m. He goes home at 10:45. He has lunch at 11.15. In the afternoon, he often plays football with his friends at 4:00. '
         'In the evening he does his homework or listens to music. Then, he goes to bed at 9:30.</p>'),
    r3=[('School starts at seven a.m and finishes at ten thirty a.m.', 'T', None, 'Đúng: School starts at 7:00 a.m and finishes at 10:30 a.m.'),
        ('In the evening, he does his housework or listens to music.', 'F', None, 'Sai: buổi tối cậu ấy làm bài tập về nhà (homework), không phải việc nhà (housework).')],
    w1=[('niraBit', 'Britain', 'img34'), ('naledemo', 'lemonade', 'img35'), ('tar', 'art', 'img36')],
    w2=[(['five', 'I', 'at', 'get', 'thirty.', 'up'], 'I get up at five thirty.'),
        (['subject?', 'your', 'What’s', 'favourite'], 'What’s your favourite subject?'),
        (['do', 'on', 'I', 'Sunday.', 'housework'], 'I do housework on Sunday.')],
)

# =============================================================== ĐỀ 6
D6 = dict(
    p1=[['img06', 'img07', 'img08'], ['img09', 'img10', 'img11'], ['img12', 'img13', 'img14'], ['img15', 'img16', 'img17']], p1k='BACB',
    p1e=['Đáp án B: tranh cậu bé nấu ăn (cook).', 'Đáp án A: tranh lều trại (camp).', 'Đáp án C: tờ lịch Friday 15.', 'Đáp án B: tranh cô bé hút bụi (làm việc nhà).'],
    p2=['img18', 'img19', 'img20', 'img21', 'img22'], p2k=[2, 0, 4, 1, 3],
    p3=['img23', 'img24', 'img25', 'img26', 'img27'], p3k=['A', 'E', 'C', 'D'],
    p4=[('I’m from {_}.', ['America']), ('I want to be a {_} teacher.', ['Maths', 'Math']),
        ('He likes {_}.', ['running']), ('When’s your birthday? – It’s in {_}.', ['January'])],
    r1=['img28', 'img29', 'img30', 'img31', 'img32'], r1w=['grapes', 'English teacher', 'Britain', 'listen to music'], r1k=['C', 'E', 'A', 'D'],
    r2p=('<p>There are four people in my family. My father <b>(1) ______</b> swim very well. My mother can cook but she can’t <b>(2) ______</b> the piano. '
         'My brother can play football and play the guitar but he can’t dance. I like music, I can sing <b>(3) ______</b> dance but I can’t cook.</p>'),
    r2o=[['do', 'can', 'is'], ['play', 'does', 'do'], ['on', 'to', 'and']], r2k='BAC',
    r3p=('<p>Hello. My name is Lucy. It is Wednesday today. It is a school day. My friend Mary and I go to school on Mondays, Tuesdays, Wednesdays, Thursdays and Fridays. '
         'At the weekend, we stay at home. We do housework on Saturdays. We listen to music and watch TV on Sundays.</p>'),
    r3=[('Mary and Lucy go to school from Mondays to Fridays.', 'T', None, 'Đúng: they go to school on Mondays to Fridays.'),
        ('At the weekend, they don’t stay at home.', 'F', None, 'Sai: At the weekend, we stay at home.'),
        ('On Saturdays, they do homework.', 'F', None, 'Sai: On Saturdays they do housework (việc nhà).')],
    w1=[('shicp', 'chips', 'img34'), ('misw', 'swim', 'img35'), ('cecisen', 'Science', 'img36')],
    w2=[(['six', 'I', 'at', 'breakfast', 'have', 'fifteen.'], 'I have breakfast at six fifteen.'),
        (['want', 'do', 'What', 'to', 'you', 'eat?'], 'What do you want to eat?'),
        (['school', 'has', 'My', 'playground.', 'a'], 'My school has a playground.')],
)

# =============================================================== ĐỀ 7
D7 = dict(
    p1=[['img06', 'img07', 'img08'], ['img09', 'img10', 'img11'], ['img12', 'img13', 'img14'], ['img15', 'img16', 'img17']], p1k='CABC',
    p1e=['Đáp án C: tranh cậu bé cầm cờ Malaysia.', 'Đáp án A: tranh cậu bé trượt patin (roller skate).', 'Đáp án B: đồng hồ 6:00 AM.',
         'Đáp án C: tranh cô bé hút bụi (làm việc nhà).'],
    p2=['img18', 'img19', 'img20', 'img21', 'img22'], p2k=[2, 0, 4, 1, 3],
    p3=['img23', 'img24', 'img25', 'img26', 'img27'], p3k=['C', 'E', 'A', 'D'],
    p4=[('I want to be a {_}.', ['painter']), ('She’s from {_}.', ['Thailand']), ('He goes to {_} at six fifteen.', ['school']),
        ('What do you do on {_}? – I listen to music.', ['Friday', 'Fridays'])],
    r1=['img28', 'img29', 'img30', 'img31', 'img32'], r1w=['birthday party', 'buildings', 'study at school', 'play the guitar'], r1k=['D', 'A', 'E', 'C'],
    r2p=('<p>Dear penfriend,</p><p>Hi! My name is Mary. I’m <b>(1) ______</b> America. My birthday is in <b>(2) ______</b>. I have many presents from my family. '
         'My parents give me a new blue bike and I receive a new pink doll from my sister. I’m very happy. What about you? <b>(3) ______</b> your birthday?</p>'),
    r2o=[['from', 'singing', 'cooking'], ['nineteen', 'nine', 'September'], ['When', 'When’s', 'Where']], r2k='ACB',
    r3p=('<p>Hello, my name is Lan. I have four friends: Mary, Lucy, Ben, Minh. Mary can play the piano, but she can’t play the guitar. Lucy can cook, but she can’t ride a bike. '
         'Ben can ride a horse, but he can’t draw. Minh can play football, but he can’t roller skate. I can cook, but I can’t swim. We all can sing and dance.</p>'),
    r3=[('Mary can play the piano, but she can’t play the guitar.', 'T', None, 'Đúng: đúng như bài đọc.'),
        ('Ben can ride a horse and draw.', 'F', None, 'Sai: Ben can ride a horse, but he can’t draw.'),
        ('Lan, Mary, Lucy, Ben and Minh can sing and dance.', 'T', None, 'Đúng: We all can sing and dance.')],
    w1=[('nuringn', 'running', 'img33'), ('sepgar', 'grapes', 'img34'), ('saninomut', 'mountains', 'img35')],
    w2=[(['she', 'Where', 'from?', 'is'], 'Where is she from?'),
        (['in', 'My', 'February.', 'is', 'birthday'], 'My birthday is in February.'),
        (['up', 'I', 'five', 'at', 'get', 'forty-five.'], 'I get up at five forty-five.')],
)

# =============================================================== ĐỀ 8
D8 = dict(
    p1=[['img06', 'img07', 'img08'], ['img09', 'img10', 'img11'], ['img12', 'img13', 'img14'], ['img15', 'img16', 'img17']], p1k='BCAB',
    p1e=['Đáp án B: tranh đầu bếp nấu ăn (cook).', 'Đáp án C: cờ Australia.', 'Đáp án A: sách Toán 4 (Maths).', 'Đáp án B: Big Ben và cờ Anh (Britain).'],
    p2=['img18', 'img19', 'img20', 'img21', 'img22'], p2k=[1, 0, 4, 2, 3],
    p3=['img23', 'img24', 'img25', 'img26', 'img27'], p3k=['D', 'E', 'A', 'C'],
    p4=[('I {_} to be a painter.', ['want']), ('Were you at the {_} yesterday?', ['campsite']),
        ('My family have breakfast at {_} o’clock.', ['six', '6']), ('My new friend is from {_}.', ['Japan'])],
    r1=['img28', 'img29', 'img30', 'img31', 'img32'], r1w=['Maths teacher', 'ride a bike', 'on the beach', 'computer room'], r1k=['D', 'A', 'E', 'C'],
    r2p=('<p>My school is in the village. It has many trees. There is one playground. <b>(1) ______</b> is one computer room with many computers in it. '
         'And there <b>(2) ______</b> two gardens. At break time, I and my friends often <b>(3) ______</b> football and game in the playground. I love my school very much.</p>'),
    r2o=[['The', 'There', 'There’s'], ['are', 'is', 'am'], ['playing', 'playes', 'play']], r2k='BAC',
    r3p=('<p>Good afternoon! I’m Linh. I’m in Class 4C. This is my classroom. Today is Wednesday. We’re having an English class now. We always have English on Wednesdays and Fridays. '
         'Mrs Hoa, my mother, is our English teacher. I like English classes very much. I can speak English and sing many English songs, but I can’t play football.</p>'),
    r3=[('Today is Thursday.', 'F', None, 'Sai: Today is Wednesday.'),
        ('Today, Linh is having Music class now.', 'F', None, 'Sai: They are having an English class now.'),
        ('Linh’s mother is Mrs Hoa. She’s an English teacher.', 'T', None, 'Đúng: Mrs Hoa, my mother, is our English teacher.')],
    w1=[('retwa', 'water', 'img33'), ('denrag', 'garden', 'img34'), ('nEshilg', 'English', 'img14')],
    w2=[(['subject?', 'your', 'What’s', 'favourite'], 'What’s your favourite subject?'),
        (['school.', 'two', 'are', 'my', 'There', 'buildings', 'at'], 'There are two buildings at my school.'),
        (['you', 'do', 'What', 'Tuesdays?', 'do', 'on'], 'What do you do on Tuesdays?')],
)

if __name__ == '__main__':
    for n, d in ((5, D5), (6, D6), (7, D7), (8, D8)):
        build(n, d)
