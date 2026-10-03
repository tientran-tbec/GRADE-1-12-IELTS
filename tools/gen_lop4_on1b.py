# -*- coding: utf-8 -*-
"""Nhóm on1b: Đề ôn thi HK1 – Đề 13, 14, 15, 16 (Lớp 4). Bỏ Speaking."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g4_exam import *

NUMS = ['1', '2', '3', '4']


class ExamA(Exam):
    """mp3 nguồn có ảnh bìa PNG hỏng -> bỏ luồng video (-vn); dùng tên tạm riêng để không đụng agent khác."""

    def make_audio(self, dst):
        import subprocess
        src = os.path.join(MP3, self.audio_src[0])
        assert os.path.exists(src), src
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src, '-vn', '-map', '0:a:0', '-ac', '1', '-ab', '48k', '-ar', '22050', dst], check=True)

# mỗi đề: khóa theo đáp án của đề
DE = {
    13: dict(
        l1='BCAB', l2={1: 'E', 2: 'A', 3: 'D', 4: 'C'}, l3={1: 'E', 2: 'D', 3: 'C', 4: 'A'},
        l4=[('There’s some {_} on the table.', ['jam']), ('He’s from {_}.', ['Australia']),
            ('What day is it today? – It’s {_}.', ['Friday']), ('My favourite subject is {_}.', ['Maths', 'Math'])],
        r1_words=['go to bed', 'water', 'nine forty-five', 'birthday party'], r1='DEAC',
        r2_pass=('<p>Hello, my name is Hoa. I’m from <b>Viet Nam</b>. I was on holiday in Nha Trang last summer. The beach was very beautiful. '
                 'We went <b>(1) ______</b> in the sea and then built sandcastles in the afternoon.</p>'
                 '<p>In the evening, we had seafood at a restaurant, it was excellent. The people were friendly <b>(2) ______</b> helpful. '
                 'We also watched a film at the <b>(3) ______</b>, it was interesting. My holiday was very nice.</p>'),
        r2=[['swimming', 'singing', 'cooking'], ['of', 'and', 'on'], ['mountain', 'hospital', 'cinema']], r2k='ABC',
        r3_pass=('<p>Hung is a pupil at Quang Trung Primary school. Every day he gets up at 6 o’clock. He has breakfast at six twenty and goes to school at '
                 'six forty-five. School starts at 7:00 a.m and finishes at 10:30 a.m. He goes home at 10:45. He has lunch at 11:15. In the afternoon, '
                 'he often plays football with his friends at 4:00. In the evening he does his homework or listens to music. Then, he goes to bed at 9:30.</p>'),
        r3=[('He has breakfast at 6:25.', 'T'), ('School starts at seven a.m and finishes at ten thirty a.m.', 'T'),
            ('In the evening, he does his housework or listens to music.', 'F')],
        w1=[('niraBit', 'img34', ['Britain']), ('naledemo', 'img35', ['lemonade']), ('tar', 'img36', ['art'])],
        w2=[(['five', 'I', 'at', 'get', 'thirty.', 'up'], 'I get up at five thirty.'),
            (['subject?', 'your', 'What’s', 'favourite'], 'What’s your favourite subject?'),
            (['do', 'on', 'I', 'Sunday.', 'housework'], 'I do housework on Sunday.')],
    ),
    14: dict(
        l1='BACB', l2={1: 'D', 2: 'A', 3: 'E', 4: 'C'}, l3={1: 'A', 2: 'E', 3: 'C', 4: 'D'},
        l4=[('I’m from {_}.', ['America']), ('I want to be a {_} teacher.', ['Maths', 'Math']),
            ('He likes {_}.', ['running']), ('When’s your birthday? – It’s in {_}.', ['January'])],
        r1_words=['grapes', 'English teacher', 'Britain', 'listen to music'], r1='CEAD',
        r2_pass=('<p>There are four people in my <b>family</b>. My father <b>(1) ______</b> swim very well. My mother can cook but she can’t '
                 '<b>(2) ______</b> the piano. My brother can play football and play the guitar but he can’t dance. I like music, I can sing '
                 '<b>(3) ______</b> dance but I can’t cook.</p>'),
        r2=[['do', 'can', 'is'], ['play', 'does', 'do'], ['on', 'to', 'and']], r2k='BAC',
        r3_pass=('<p>Hello. My name is Lucy. It is Wednesday today. It is a school day. My friend Mary and I go to school on Mondays, Tuesdays, '
                 'Wednesdays, Thursdays and Fridays. At the weekend, we stay at home. We do housework on Saturdays. We listen to music and watch TV on Sundays.</p>'),
        r3=[('Mary and Lucy go to school from Mondays to Fridays.', 'T'), ('At the weekend, they don’t stay at home.', 'F'),
            ('On Saturdays, they do homework.', 'F')],
        w1=[('shicp', 'img34', ['chips']), ('misw', 'img35', ['swim']), ('cecisen', 'img36', ['Science'])],
        w2=[(['six', 'I', 'at', 'breakfast', 'have', 'fifteen.'], 'I have breakfast at six fifteen.'),
            (['want', 'do', 'What', 'to', 'you', 'eat?'], 'What do you want to eat?'),
            (['school', 'has', 'My', 'playground.', 'a'], 'My school has a playground.')],
    ),
    15: dict(
        l1='CABC', l2={1: 'D', 2: 'A', 3: 'E', 4: 'C'}, l3={1: 'C', 2: 'E', 3: 'A', 4: 'D'},
        l4=[('I want to be a {_}.', ['painter']), ('She’s from {_}.', ['Thailand']),
            ('He goes to {_} at six fifteen.', ['school']), ('What do you do on {_}? – I listen to music.', ['Friday', 'Fridays'])],
        r1_words=['birthday party', 'buildings', 'study at school', 'play the guitar'], r1='DAEC',
        r2_pass=('<p>Dear penfriend,</p><p>Hi! My <b>name</b> is Mary. I’m <b>(1) ______</b> America. My birthday is in <b>(2) ______</b>. '
                 'I have many presents from my family. My parents give me a new blue bike and I receive a new pink doll from my sister. '
                 'I’m very happy. What about you? <b>(3) ______</b> your birthday?</p>'),
        r2=[['from', 'singing', 'cooking'], ['nineteen', 'nine', 'September'], ['When', 'When’s', 'Where']], r2k='ACB',
        r3_pass=('<p>Hello, my name is Lan. I have four friends: Mary, Lucy, Ben, Minh. Mary can play the piano, but she can’t play the guitar. '
                 'Lucy can cook, but she can’t ride a bike. Ben can ride a horse, but he can’t draw. Minh can play football, but he can’t roller skate. '
                 'I can cook, but I can’t swim. We all can sing and dance.</p>'),
        r3=[('Mary can play the piano, but she can’t play the guitar.', 'T'), ('Ben can ride a horse and draw.', 'F'),
            ('Lan, Mary, Lucy, Ben and Minh can sing and dance.', 'T')],
        w1=[('nuringn', 'img33', ['running']), ('sepgar', 'img34', ['grapes']), ('saninomut', 'img35', ['mountains'])],
        w2=[(['she', 'Where', 'from?', 'is'], 'Where is she from?'),
            (['in', 'My', 'February.', 'is', 'birthday'], 'My birthday is in February.'),
            (['up', 'I', 'five', 'at', 'get', 'forty-five.'], 'I get up at five forty-five.')],
    ),
    16: dict(
        l1='BCAB', l2={1: 'A', 2: 'D', 3: 'E', 4: 'C'}, l3={1: 'D', 2: 'E', 3: 'A', 4: 'C'},
        l4=[('I {_} to be a painter.', ['want']), ('Were you at the {_} yesterday?', ['campsite']),
            ('My family have breakfast at {_} o’clock.', ['six']), ('My new friend is from {_}.', ['Japan'])],
        r1_words=['Maths teacher', 'ride a bike', 'on the beach', 'computer room'], r1='DAEC',
        r2_pass=('<p>My school is <b>in</b> the village. It has many trees. There is one playground. <b>(1) ______</b> is one computer room '
                 'with many computers in it. And there <b>(2) ______</b> two gardens. At break time, I and my friends often <b>(3) ______</b> '
                 'football and games in the playground. I love my school very much.</p>'),
        r2=[['The', 'There', 'There’s'], ['are', 'is', 'am'], ['playing', 'playes', 'play']], r2k='BAC',
        r3_pass=('<p>Good afternoon! I’m Linh. I’m in Class 4C. This is my classroom. Today is Wednesday. We’re having an English class now. '
                 'We always have English on Wednesdays and Fridays. Mrs Hoa, my mother, is our English teacher. I like English classes very much. '
                 'I can speak English and sing many English songs, but I can’t play football.</p>'),
        r3=[('Today is Thursday.', 'F'), ('Today, Linh is having Music class now.', 'F'),
            ('Linh’s mother is Mrs Hoa. She’s an English teacher.', 'T')],
        w1=[('retwa', 'img33', ['water']), ('denrag', 'img34', ['garden']), ('nEshilg', 'img14', ['English'])],
        w2=[(['subject?', 'your', 'What’s', 'favourite'], 'What’s your favourite subject?'),
            (['school.', 'two', 'are', 'my', 'There', 'buildings', 'at'], 'There are two buildings at my school.'),
            (['you', 'do', 'What', 'Tuesdays?', 'do', 'on'], 'What do you do on Tuesdays?')],
    ),
}


def build(n):
    c = DE[n]
    src = 'De-on-thi-HK1-Anh-4-Global-De-%d' % n
    ex = ExamA('on1_de%d' % n, 'OnHK1', 'Ôn HK1 – Đề %d' % n, src, slug='test%d' % n, minutes=35, warn_at=5,
              audio=['thuvienhoclieu.com-Nghe-De-on-thi-HK1-Anh-4-Global-De-%d.mp3' % n])
    d = Dump(src)
    ls = d.body
    # ---- Listening 1: tick
    rows = []
    for k in range(4):
        base = 6 + 3 * k
        rows.append(['img%02d' % (base + j) for j in range(3)])
    ex.mcq_pics('l1', 'Listening – Part 1. Listen and tick (nghe và chọn tranh đúng).', rows, list(c['l1']))
    # ---- Listening 2 / 3: nghe và đánh số (tranh -> số thứ tự)
    for gid, key, first, title in (('l2', 'l2', 18, 'Part 2. Listen and number (nghe và đánh số tranh; tranh B là ví dụ = 0).'),
                                   ('l3', 'l3', 23, 'Part 3. Listen and draw line (nghe và nối tranh với số; tranh B là ví dụ = 0).')):
        inv = {v: str(k) for k, v in c[key].items()}   # chữ -> số
        pics = ['img%02d' % (first + i) for i in range(5)]
        labels = list('ABCDE')
        keys = [inv.get(lb, '0') for lb in labels]
        only = [lb for lb in labels if lb in inv]
        ex.number_pics(gid, 'Listening – ' + title, pics, labels, keys, nums=NUMS, only=only)
    # ---- Listening 4: nghe và điền từ
    ex.fill('l4', 'Listening – Part 4. Listen and write (nghe và điền từ).', [(q, a) for q, a in c['l4']])
    # ---- Reading 1: nối
    rp = ex.strip(['img%02d' % (28 + i) for i in range(5)], list('ABCDE'), 'r1_pics.png', w=150, h=125)
    ex.match('r1', 'Reading – Part 1. Read and match the words with pictures (nối từ với tranh).',
             [{'t': w} for w in c['r1_words']], list('ABCDE'), list(c['r1']),
             'Đáp án theo đáp án của đề: ' + ', '.join('%s–%s' % (w, k) for w, k in zip(c['r1_words'], c['r1'])),
             picture='<img class="wide" src="%s" alt="Tranh A–E">' % ex.asset(rp))
    # ---- Reading 2: cloze
    items = []
    for i, (o, kk) in enumerate(zip(c['r2'], c['r2k']), 1):
        items.append(({'t': 'mcq', 'q': 'Chọn từ điền vào chỗ trống (%d).' % i, 'o': o}, kk, 'Đáp án: %s. %s' % (kk, o['ABC'.index(kk)])))
    ex.add('r2', 'Reading – Part 2. Read and choose A, B or C to complete the text (đọc và chọn từ điền vào chỗ trống).', items, passage=c['r2_pass'])
    # ---- Reading 3: T/F
    ex.tf('r3', 'Reading – Part 3. Read and tick True or False (đọc đoạn văn, True hay False?).', c['r3'], passage=c['r3_pass'])
    # ---- Writing 1: sắp xếp chữ cái
    ex.fill('w1', 'Writing – Part 1. Look at the pictures and the letters. Write the words (nhìn tranh, sắp xếp chữ cái thành từ).',
            [('Sắp xếp chữ cái: <b>%s</b> → {_}' % s, a, im, 'Từ đúng: %s' % a[0]) for s, im, a in c['w1']])
    # ---- Writing 2: sắp xếp từ
    ex.order('w2', 'Writing – Part 2. Rearrange the words to make sentences (sắp xếp từ thành câu đúng).', c['w2'])
    ex.notes.append('bỏ Speaking; bỏ câu ví dụ (0)')
    if n == 13: ex.notes.append('Writing P2 ví dụ không có đáp án nên bỏ; key đề đánh nhầm nhãn PART 2/3 phần Reading (đã đối chiếu nội dung)')
    if n == 15: ex.notes.append('key W2.3 ghi "forty – five" -> chuẩn hóa "forty-five"')
    ex.save()


if __name__ == '__main__':
    for n in (13, 14, 15, 16):
        build(n)
