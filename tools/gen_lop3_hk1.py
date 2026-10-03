# -*- coding: utf-8 -*-
"""Lớp 3 – Cuối kỳ 1 (5 đề, có file nghe). Nguồn: 'Đề ôn tập cuối HK1 Tiếng Anh 3 Global 25-26' Đề 1–5 (thuvienhoclieu.com).
Ảnh tách từ docx (/tmp/ex/w<n>/pX_NN.png) rồi ghép nhãn A/B/C… bằng PIL -> assets/lop3_hk1/deNN/.
Bỏ phần Speaking (D). Đáp án nghe lấy theo đáp án của đề; phần còn lại đã đối chiếu lại bằng logic (xem GHI_CHU)."""
import os, pprint
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = '/tmp/ex'
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)


def load(n, name):
    return Image.open('%s/w%d/%s.png' % (SRC, n, name)).convert('RGB')


def fit(im, w, h):
    s = min(w / im.width, h / im.height)
    return im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)


def cell(n, names, w, h):
    """names: tên ảnh hoặc list (ghép ngang)."""
    names = [names] if isinstance(names, str) else names
    c = Image.new('RGB', (w, h), 'white')
    k = len(names)
    for i, nm in enumerate(names):
        im = fit(load(n, nm), w // k - 6, h - 8)
        c.paste(im, (i * (w // k) + (w // k - im.width) // 2, (h - im.height) // 2))
    ImageDraw.Draw(c).rectangle([0, 0, w - 1, h - 1], outline=(190, 190, 190))
    return c


def strip(n, items, labels, out, w=170, h=140):
    """items: list tên ảnh; labels: nhãn (A,B,... hoặc a,b,...) dưới mỗi ảnh."""
    gap = 12
    W = len(items) * w + (len(items) - 1) * gap
    S = Image.new('RGB', (W, h + 34), 'white')
    d = ImageDraw.Draw(S)
    for i, (nm, lb) in enumerate(zip(items, labels)):
        x = i * (w + gap)
        S.paste(cell(n, nm, w, h), (x, 0))
        tw = d.textlength(lb, font=FONT)
        d.text((x + (w - tw) / 2, h + 4), lb, fill=(20, 20, 20), font=FONT)
    path = os.path.join(ROOT, 'assets/lop3_hk1/de%02d' % n)
    os.makedirs(path, exist_ok=True)
    S.save(os.path.join(path, out), optimize=True)


def single(n, name, out, w=190, h=150):
    path = os.path.join(ROOT, 'assets/lop3_hk1/de%02d' % n)
    os.makedirs(path, exist_ok=True)
    cell(n, name, w, h).save(os.path.join(path, out), optimize=True)


# ---------------------------------------------------------------- khung câu hỏi
def build(n, spec):
    """spec: dict -> (SET, ANS, EXP)"""
    ANS, EXP, groups, k = {}, {}, [], 0
    ASSET = '../../../../assets/lop3_hk1/de%02d/' % n

    def add(gid, instr, items, passage=None, bank=None):
        nonlocal k
        out = []
        for it, a, e in items:
            k += 1
            it = dict(it)
            it['id'] = '%s.%d' % (gid, k)
            out.append(it)
            ANS[it['id']] = a
            EXP[it['id']] = e
        g = {'id': gid, 'instr': instr, 'items': out}
        if passage:
            g['passage'] = passage
        if bank:
            g['bank'] = bank
        groups.append(g)

    for sec in spec:
        add(*sec)
    S = {'id': 'lop3-hk1-de%02d' % n, 'title': 'Cuối kỳ 1 – Đề %d' % n, 'grade': 3, 'unit': 'CuoiKy1', 'theory': '',
         'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 40, 'warn_at': 5, 'audio': True, 'audio_max_plays': 3, 'groups': groups}]}
    return S, ANS, EXP


def dump(path, name, obj):
    with open(os.path.join(ROOT, path), 'w', encoding='utf8') as f:
        f.write('# -*- coding: utf-8 -*-\n"""Sinh bởi tools/gen_lop3_hk1.py"""\n\n%s = %s\n' % (name, pprint.pformat(obj, width=160)))


# ---- mẫu câu hỏi dùng chung
def LAB(i):
    return 'ABCDE'[i]


def sec_ab(n, pairs, keys):
    """Listening I: pairs = [(tênA, tênB)...], keys = ['B','A',...]"""
    items = []
    for i, ((a, b), key) in enumerate(zip(pairs, keys), 1):
        strip(n, [a, b], ['A', 'B'], 'l1_%d.png' % i, w=200, h=150)
        items.append(({'t': 'mcq', 'plain': True, 'wide': True, 'img': 'l1_%d.png' % i, 'q': 'Nghe và chọn tranh đúng.', 'o': ['A', 'B']}, key,
                      'Đáp án %s (theo đáp án của đề). Nghe lại file âm thanh và đối chiếu với tranh.' % key))
    return ('l1', 'PART A – Listening. I. Listen and tick (nghe và chọn tranh A hoặc B).', items)


def sec_num(n, pics, keys):
    """Listening II: pics = 5 ảnh A–E; keys cho câu 1–4"""
    strip(n, pics, list('ABCDE'), 'l2.png', w=150, h=125)
    items = [({'t': 'mcq', 'plain': True, 'q': 'Câu %d nghe được ứng với tranh nào?' % i, 'o': list('ABCDE')}, key,
              'Đáp án %s (theo đáp án của đề).' % key) for i, key in enumerate(keys, 1)]
    return ('l2', 'II. Listen and number (nghe và chọn tranh A–E cho từng câu).', items,
            '<img class="wide" src="../../../../assets/lop3_hk1/de%02d/l2.png" alt="Tranh A–E">' % n)


def sec_write(prompts, answers, exps):
    """Listening III: prompts = [q có {_}], answers = [list|str]"""
    items = [({'t': 'fill', 'q': q}, a if isinstance(a, list) else [a], e) for q, a, e in zip(prompts, answers, exps)]
    return ('l3', 'III. Listen and write (nghe và điền từ).', items)


def sec_circle(gid, instr, rows, ans_exp):
    """rows: [(img, q, [opt1,opt2])]; ans_exp: [(đáp án, giải thích)]"""
    items = [({'t': 'mcq', 'plain': True, 'img': im, 'q': q, 'o': o}, a, e) for (im, q, o), (a, e) in zip(rows, ans_exp)]
    return (gid, instr, items)


def sec_tf(gid, instr, rows, ans_exp):
    items = [({'t': 'tf', 'img': im, 'q': q}, a, e) for (im, q), (a, e) in zip(rows, ans_exp)]
    return (gid, instr, items)


def sec_match(gid, instr, left, opts, keys, exp, picture=None):
    it = {'t': 'match', 'q': 'Nối (chọn đáp án đúng cho từng dòng):', 'left': left, 'o': opts}
    return (gid, instr, [(it, {'blanks': [[x] for x in keys]}, exp)], picture)


def sec_fill(gid, instr, rows, bank=None):
    """rows: [(q, [đáp án], giải thích, img|None)]"""
    items = []
    for q, a, e, im in rows:
        it = {'t': 'fill', 'q': q}
        if im:
            it['img'] = im
        items.append((it, a, e))
    return (gid, instr, items, None, bank)


def sec_order(gid, instr, rows):
    """rows: [(words, câu đúng)]"""
    items = [({'t': 'order', 'q': 'Sắp xếp thành câu đúng:', 'words': w}, [a], 'Câu đúng: ' + a) for w, a in rows]
    return (gid, instr, items)


def img1(n, name, out, **kw):
    single(n, name, out, **kw)
    return out


# ================================================================ ĐỀ 1
def de1():
    n = 1
    secs = [
        sec_ab(n, [('p1_04', 'p1_07'), ('p1_05', 'p1_06'), ('p1_08', 'p1_09'), ('p1_10', 'p1_11')], ['B', 'A', 'A', 'B']),
        sec_num(n, ['p1_13', 'p1_14', 'p1_15', 'p1_16', 'p1_12'], ['C', 'D', 'B', 'A']),
        sec_write(['How old are you? – I\'m {_} years old.', "What's your hobby? – I like {_}.", "Let's go to the {_} room. – OK, let's go.", 'I play {_} at break time.'],
                  ['eight', 'drawing', 'music', 'volleyball'],
                  ['I\'m eight years old. (tranh bánh sinh nhật số 8)', 'I like drawing.', "Let's go to the music room.", 'I play volleyball at break time.']),
    ]
    # ---- Reading
    # Reading I: nối 4 tranh với từ
    for i, nm in enumerate(['p2_02', 'p2_03', 'p2_05', 'p2_01'], 1):
        single(n, nm, 'r1_%d.png' % i)
    secs.append(sec_match('r1', 'PART B – Reading. I. Look, read and match (nhìn tranh, chọn từ đúng).',
                          [{'img': 'r1_%d.png' % i} for i in range(1, 5)], ['eyes', 'walking', 'pencil', 'volleyball', 'go out'],
                          ['volleyball', 'walking', 'eyes', 'go out'], 'Tranh 1: bóng chuyền (volleyball); 2: đi bộ (walking); 3: đôi mắt (eyes); 4: đi ra ngoài (go out).'))
    rows = []
    for i, (nm, q) in enumerate([('p2_08', 'A: May I go out? B: Yes, you can.'), ('p2_07', 'A: What do you do at break time? B: I play word puzzles.'),
                                   ('p2_09', "A: What's your hobby? B: I like running."), ('p2_10', "A: What's this? B: It's a mouth.")], 1):
        rows.append((img1(n, nm, 'r2_%d.png' % i, w=200, h=150), q))
    secs.append(sec_tf('r2', 'II. Read and tick or cross (câu có đúng với tranh không? True = đúng, False = sai).', rows,
                       [('T', 'Học sinh xin phép giáo viên đi ra ngoài – khớp tranh.'), ('F', 'Tranh là hai bạn chơi cờ (chess), không phải word puzzles.'),
                        ('F', 'Tranh là bạn đang bơi (swimming), không phải running.'), ('T', 'Mũi tên chỉ vào miệng (mouth) – khớp tranh.')]))
    secs.append(sec_fill('r3', 'III. Look, read and complete (chọn từ trong khung điền vào chỗ trống).',
                         [('A: May I {_}? B: Yes, you can.', ['come in'], 'May I come in? – Yes, you can.', None),
                          ("A: What's your hobby? B: It's {_}.", ['drawing'], "It's drawing.", None),
                          ("Let's go to the {_}.", ['playground'], "Let's go to the playground.", None),
                          ('A: Do you have an {_}? B: Yes, I do.', ['eraser'], 'an eraser (bắt đầu bằng nguyên âm → an).', None)],
                         bank=['come in', 'playground', 'eraser', 'drawing', 'nine']))
    rows = []
    for i, (nm, hint, ans) in enumerate([('p3_03', 'gnicoko', 'cooking'), ('p3_04', 'arlriyb', 'library'), ('p3_05', 'lalsektbab', 'basketball'), ('p3_01', 'okobteno', 'notebook')], 1):
        rows.append(('%s → {_}' % hint, [ans], '%s = %s' % (hint, ans), img1(n, nm, 'w1_%d.png' % i)))
    secs.append(sec_fill('w1', 'PART C – Writing. I. Reorder the letters (sắp xếp lại chữ cái, nhìn tranh).', rows))
    secs.append(sec_order('w2', 'II. Reorder the words (sắp xếp từ thành câu).',
                          [(['chess', 'time.', 'at', 'play', 'break', 'I'], 'I play chess at break time.'), (['eraser?', 'Do', 'you', 'an', 'have'], 'Do you have an eraser?')]))
    return build(n, secs)


# ================================================================ ĐỀ 2
def de2():
    n = 2
    secs = [
        sec_ab(n, [('p1_06', 'p1_07'), ('p1_05', ['p1_08', 'p1_09']), ('p1_11', 'p1_12'), ('p1_13', 'p1_10')], ['B', 'A', 'A', 'B']),
        sec_num(n, ['p1_15', 'p1_16', 'p1_17', 'p1_14', 'p1_18'], ['C', 'A', 'D', 'B']),
        sec_write(["What's your hobby? – I like {_}.", 'Do you have a {_}? – Yes, I do.', 'What do you do at break time? – I play {_}.', "What colour is it? – It's {_}."],
                  ['running', 'pencil case', 'football', 'orange'],
                  ['I like running.', 'Do you have a pencil case?', 'I play football.', "It's orange."]),
    ]
    # Reading I: nối tranh – từ
    for i, nm in enumerate(['p2_03', 'p2_04', 'p2_05', 'p2_01'], 1):
        single(n, nm, 'r1_%d.png' % i)
    secs.append(sec_match('r1', 'PART B – Reading. I. Look, read and match (nhìn tranh, chọn từ đúng).',
                          [{'img': 'r1_%d.png' % i} for i in range(1, 5)], ['drawing', 'music room', 'pencil', 'nose', 'good bye'],
                          ['nose', 'good bye', 'drawing', 'music room'], 'Tranh 1: cái mũi (nose); 2: tạm biệt (good bye); 3: vẽ (drawing); 4: phòng âm nhạc (music room).'))
    rows = []
    for i, (a, b, q, op, ans, e) in enumerate([
            ('p2_08', 'p2_09', 'I play table tennis at break time.', ['a. chess', 'b. table tennis'], 'b', 'table tennis = bóng bàn (tranh b).'),
            ('p2_10', 'p2_11', "A: Do you have a ruler? B: No, I don't. I have a pen.", ['a. ruler', 'b. pen'], 'b', 'Bạn ấy có bút (pen), không có thước (ruler).'),
            ('p2_12', 'p2_13', 'A: Is it our classroom? B: Yes, it is.', ['a. classroom', 'b. library'], 'a', 'classroom = lớp học (tranh a).'),
            ('p2_14', 'p2_15', "A: What's your hobby? B: I like running.", ['a. singing', 'b. running'], 'b', 'running = chạy (tranh b).')], 1):
        strip(n, [a, b], ['a', 'b'], 'r2_%d.png' % i, w=190, h=140)
        rows.append(('r2_%d.png' % i, q, ['a', 'b']))
    secs.append(('r2', 'II. Read and circle a or b (đọc câu, chọn tranh a hoặc b).',
                 [({'t': 'mcq', 'plain': True, 'wide': True, 'img': im, 'q': q, 'o': o}, a, e) for (im, q, o), (a, e) in zip(rows, [
                     ('b', 'table tennis = bóng bàn (tranh b).'), ('b', 'Bạn ấy có bút (pen), không có thước (ruler).'), ('a', 'classroom = lớp học (tranh a).'), ('b', 'running = chạy (tranh b).')])]))
    secs.append(sec_fill('r3', 'III. Look, read and complete (chọn từ trong khung điền vào chỗ trống).',
                         [('A: Is this the {_}? B: Yes, it is.', ['playground'], 'the playground = sân chơi.', None),
                          ('A: May I {_}? B: Yes, you can.', ['sit down'], 'May I sit down? – Yes, you can.', None),
                          ('I have a {_}.', ['school bag'], 'I have a school bag.', None),
                          ('A: Is {_} Minh? B: No, it isn\'t. It\'s Nam.', ['that'], 'Is that Minh? (người ở xa)', None)],
                         bank=['School bag', 'playground', 'that', 'Sit down', 'nine']))
    rows = []
    for i, (nm, q, ans, e) in enumerate([('p3_01', 'I like {_}. (r _ _ _ _ _ _)', 'running', 'I like running.'), ('p3_02', '{_} your ears. (t _ _ _ _)', 'touch', 'Touch your ears.'),
                                         ('p3_03', 'I have a {_}. (n _ _ _ _ _ _ _)', 'notebook', 'I have a notebook.'), ('p3_04', 'A: Is it the {_}? B: Yes, it is. (p _ _ _ _ _ _ _ _ _)', 'playground', 'the playground.')], 1):
        rows.append((q, [ans], e, img1(n, nm, 'w1_%d.png' % i)))
    secs.append(sec_fill('w1', 'PART C – Writing. I. Look and write (nhìn tranh, điền từ).', rows))
    secs.append(sec_order('w2', 'II. Reorder the words (sắp xếp từ thành câu).',
                          [(['colour', 'they?', 'What', 'are'], 'What colour are they?'), (['pencil?', 'Do', 'you', 'a', 'have'], 'Do you have a pencil?')]))
    return build(n, secs)


# ================================================================ ĐỀ 3
def de3():
    n = 3
    secs = [
        sec_ab(n, [('p1_06', 'p1_07'), ('p1_04', 'p1_05'), ('p1_08', 'p1_11'), ('p1_10', 'p1_09')], ['B', 'A', 'A', 'B']),
        sec_num(n, ['p1_12', 'p1_13', 'p1_15', 'p1_16', 'p1_14'], ['B', 'C', 'D', 'A']),
        sec_write(["What's your hobby? – I like {_}.", 'What colour are they? – They\'re {_}.', "Hi, I'm Ben. I play {_} at break time.", "Let's go to the {_}."],
                  [['painting'], 'green', 'basketball', 'classroom'],
                  ['I like painting.', "They're green.", 'I play basketball at break time.', "Let's go to the classroom."]),
    ]
    rows = []
    for i, (nm, q, op, ans, e) in enumerate([('p2_02', '', ['Sit down', 'Stand up'], 'Stand up', 'Tranh bạn đứng lên: Stand up.'),
                                             ('p2_03', '', ['Hand', 'Hair'], 'Hand', 'Tranh bàn tay: Hand.'),
                                             ('p2_04', '', ['Dancing', 'Singing'], 'Dancing', 'Tranh hai bạn nhảy: Dancing.'),
                                             ('p2_05', '', ['Table tennis', 'Badminton'], 'Badminton', 'Tranh vợt cầu lông: Badminton.')], 1):
        rows.append((img1(n, nm, 'r1_%d.png' % i), 'Nhìn tranh, chọn từ đúng:', op))
    secs.append(sec_circle('r1', 'PART B – Reading. I. Look, read and circle a or b (nhìn tranh, chọn từ đúng).', rows,
                           [('Stand up', 'Tranh bạn đứng lên: Stand up.'), ('Hand', 'Tranh bàn tay: Hand.'), ('Dancing', 'Tranh hai bạn nhảy: Dancing.'), ('Badminton', 'Tranh vợt cầu lông: Badminton.')]))
    strip(n, ['p2_06', 'p2_07', 'p2_08', 'p2_09', 'p2_10'], list('abcde'), 'r2.png', w=150, h=125)
    secs.append(sec_match('r2', 'II. Look, read and match (nối câu với tranh a–e).',
                          [{'t': "What's this? – It's an ear."}, {'t': 'May I go out? – Yes, you can.'}, {'t': 'Is this our classroom? – Yes, it is.'}, {'t': 'I play basketball at break time.'}],
                          list('abcde'), ['e', 'a', 'b', 'c'], 'Ear → e; May I go out → a (xin phép đi ra); classroom → b; basketball → c.',
                          picture='<img class="wide" src="../../../../assets/lop3_hk1/de03/r2.png" alt="Tranh a–e">'))
    secs.append(sec_fill('r3', 'III. Look, read and complete (chọn từ trong khung điền vào chỗ trống).',
                         [('A: Do you have an {_}? B: Yes, I do.', ['eraser'], 'an eraser.', None),
                          ("A: What's your {_}? B: I like singing.", ['hobby'], "What's your hobby?", None),
                          ("A: What colour are they? B: They're {_}.", ['black'], "They're black.", None),
                          ("A: What's this? B: It's a {_}.", ['nose'], "It's a nose.", None)],
                         bank=['hobby', 'nose', 'eraser', 'black', 'nine']))
    rows = []
    for i, (nm, q, ans, e) in enumerate([('p3_01', 'A: Do you have a pen? B: No, I don\'t. I have a {_}.', 'pencil', 'I have a pencil.'),
                                         ('p3_03', 'Open your {_}, please.', 'mouth', 'Open your mouth, please.'),
                                         ('p3_02', 'I like {_}.', 'walking', 'I like walking.'),
                                         ('p3_04', 'A: I like drawing. B: Oh, let\'s go to the {_} room.', 'art', 'the art room (phòng mỹ thuật).')], 1):
        rows.append((q, [ans], e, img1(n, nm, 'w1_%d.png' % i)))
    secs.append(sec_fill('w1', 'PART C – Writing. I. Look and write (nhìn tranh, điền từ).', rows))
    secs.append(sec_order('w2', 'II. Reorder the words (sắp xếp từ thành câu).',
                          [(['pen', 'blue.', 'The', 'is'], 'The pen is blue.'), (['notebook?', 'Do', 'have', 'a', 'you'], 'Do you have a notebook?')]))
    return build(n, secs)


# ================================================================ ĐỀ 4
def de4():
    n = 4
    secs = [
        sec_ab(n, [('p1_06', 'p1_07'), ('p1_04', 'p1_05'), ('p1_08', 'p1_09'), ('p1_10', 'p1_11')], ['A', 'A', 'A', 'B']),
        sec_num(n, ['p1_12', 'p1_13', 'p1_14', 'p1_15', 'p1_16'], ['B', 'C', 'D', 'A']),
        sec_write(['I have a {_}.', "Let's go to the {_} room.", 'A: What colour is it? B: My eraser is {_}.', 'A: What do you do at {_}? B: I play volleyball.'],
                  ['school bag', 'music', 'yellow', 'break time'],
                  ['I have a school bag.', "Let's go to the music room.", 'My eraser is yellow.', 'What do you do at break time?']),
    ]
    rows = []
    for i, (nm, op, ans, e) in enumerate([('p2_04', ['come in', 'go out'], 'go out', 'Tranh bạn nhỏ xin đi ra: go out.'), ('p2_02', ['chess', 'puzzle word'], 'chess', 'Tranh bàn cờ: chess.'),
                                          ('p2_03', ['running', 'walking'], 'running', 'Tranh bạn chạy: running.'), ('p2_05', ['ears', 'eyes'], 'eyes', 'Tranh đôi mắt: eyes.')], 1):
        rows.append((img1(n, nm, 'r1_%d.png' % i), 'Nhìn tranh, chọn từ đúng:', op))
    secs.append(sec_circle('r1', 'PART B – Reading. I. Look, read and circle a or b (nhìn tranh, chọn từ đúng).', rows,
                           [('go out', 'Tranh bạn nhỏ xin đi ra: go out.'), ('chess', 'Tranh bàn cờ: chess.'), ('running', 'Tranh bạn chạy: running.'), ('eyes', 'Tranh đôi mắt: eyes.')]))
    rows = []
    for i, (nm, q, op, ans, e) in enumerate([('p2_07', "– What's this? It's a ___.", ['mouth', 'nose'], 'nose', 'Tranh cái mũi: nose.'),
                                             ('p2_08', '– What colour is it? It\'s ___.', ['orange', 'yellow'], 'orange', 'Quyển vở màu cam: orange.'),
                                             ('p2_09', "– What's your hobby? It's ___.", ['dancing', 'painting'], 'painting', 'Tranh bạn đang vẽ: painting.'),
                                             ('p2_10', '– What do you do at break time? I play ___.', ['volleyball', 'football'], 'volleyball', 'Tranh bạn chơi bóng chuyền: volleyball.')], 1):
        rows.append((img1(n, nm, 'r2_%d.png' % i), q, op))
    secs.append(sec_circle('r2', 'II. Look, read and choose the correct word (nhìn tranh, chọn từ đúng).', rows,
                           [('nose', 'Tranh cái mũi: nose.'), ('orange', 'Quyển vở màu cam: orange.'), ('painting', 'Tranh bạn đang vẽ: painting.'), ('volleyball', 'Tranh bạn chơi bóng chuyền: volleyball.')]))
    secs.append(sec_fill('r3', 'III. Look, read and complete (chọn từ trong khung điền vào chỗ trống).',
                         [('A: What do you do at break time? B: I play {_}.', ['word puzzles', 'word puzzle'], 'I play word puzzles.', None),
                          ("A: What's your hobby? B: I like {_}.", ['swimming'], 'I like swimming.', None),
                          ('A: Is this our {_}? B: Yes, it is.', ['playground'], 'our playground.', None),
                          ("A: I like singing. B: Let's go to the {_}.", ['music room'], "Let's go to the music room.", None)],
                         bank=['swimming', 'music room', 'word puzzles', 'playground', 'nine']))
    rows = []
    for i, (nm, ans) in enumerate([('p3_02', 'mouth'), ('p3_03', 'school bag'), ('p3_04', 'volleyball'), ('p3_05', 'colour')], 1):
        rows.append(('Look and write: {_}', [ans], '%s' % ans, img1(n, nm, 'w1_%d.png' % i)))
    secs.append(sec_fill('w1', 'PART C – Writing. I. Write the words (nhìn tranh, viết từ).', rows))
    secs.append(sec_order('w2', 'II. Reorder the words (sắp xếp từ thành câu).',
                          [(['gym.', "Let's", 'the', 'to', 'go'], "Let's go to the gym."), (['break', 'time?', 'do', 'What', 'at', 'do', 'you'], 'What do you do at break time?')]))
    return build(n, secs)


# ================================================================ ĐỀ 5
def de5():
    n = 5
    secs = [
        sec_ab(n, [('p1_04', 'p1_07'), ('p1_05', 'p1_06'), ('p1_09', 'p1_11'), ('p1_08', 'p1_10')], ['A', 'A', 'B', 'B']),
        sec_num(n, ['p1_14', 'p1_12', 'p1_13', 'p1_15', 'p1_16'], ['C', 'A', 'D', 'B']),
        sec_write(["A: What's your hobby? B: It's {_}.", 'A: May I {_} Vietnamese? B: No, you can\'t.', 'A: Is this our {_}? B: Yes, it is.', 'A: What do you do at break time? B: I play {_}.'],
                  ['running', 'speak', 'playground', 'badminton'],
                  ["It's running.", 'May I speak Vietnamese?', 'Is this our playground?', 'I play badminton.']),
    ]
    rows = []
    for i, (nm, q, a, e) in enumerate([('p2_03', 'goodbye', 'T', 'Tranh vẫy tay chào: goodbye – khớp.'), ('p2_04', 'open', 'F', 'Tranh bạn che mũi/miệng, không phải open.'),
                                       ('p2_05', 'library', 'T', 'Tranh thư viện: library – khớp.'), ('p2_06', 'puzzle', 'F', 'Tranh bàn cờ (chess), không phải puzzle.')], 1):
        rows.append((img1(n, nm, 'r1_%d.png' % i), 'Tranh và từ "%s" – đúng hay sai?' % q))
    secs.append(sec_tf('r1', 'PART B – Reading. I. Look, read and tick or cross (từ có đúng với tranh không? True = đúng, False = sai).', rows,
                       [('T', 'Tranh vẫy tay chào: goodbye – khớp.'), ('F', 'Tranh bạn che mũi/miệng, không phải open.'), ('T', 'Tranh thư viện: library – khớp.'), ('F', 'Tranh bàn cờ (chess), không phải puzzle.')]))
    strip(n, ['p2_08', 'p2_09', 'p2_10', 'p2_11', 'p2_12'], list('abcde'), 'r2.png', w=150, h=125)
    secs.append(sec_match('r2', 'II. Look, read and match (nối câu với tranh a–e).',
                          [{'t': "Is this your gym? – Yes, it is."}, {'t': "Do you have a notebook? – No, I don't."}, {'t': "What's your hobby? – It's walking."}, {'t': 'What do you do at break time? – I play word puzzles.'}],
                          list('abcde'), ['d', 'e', 'a', 'b'], 'gym → d (phòng thể dục); notebook → e; walking → a; word puzzles → b (ô chữ).',
                          picture='<img class="wide" src="../../../../assets/lop3_hk1/de05/r2.png" alt="Tranh a–e">'))
    secs.append(sec_fill('r3', 'III. Look, read and complete (chọn từ trong khung điền vào chỗ trống).',
                         [('A: What do you do at break time? B: I play {_}.', ['chess'], 'I play chess.', None),
                          ("A: What's your hobby? B: I like {_}.", ['dancing'], 'I like dancing.', None),
                          ("A: I like painting. B: Let's go to the {_} room.", ['art'], "Let's go to the art room.", None),
                          ('{_} your mouth, please.', ['open'], 'Open your mouth, please.', None)],
                         bank=['art', 'dancing', 'open', 'chess', 'nine']))
    rows = []
    for i, (nm, q, a, e) in enumerate([('p3_01', 'A: Do you have an eraser? B: {_}', ['Yes, I do.'], 'Yes, I do. (tranh cục tẩy có dấu tick)'),
                                       ('p3_03', "A: What's this? B: {_}", ["It's a nose.", 'A nose.'], "It's a nose."),
                                       ('p3_04', "A: What's your hobby? B: {_}", ["I like drawing.", "It's drawing.", 'Drawing.'], "I like drawing. / It's drawing."),
                                       ('p3_05', 'A: What do you do at break time? B: {_}', ['I chat with friends.', 'We chat with friends.', 'Chat with friends.'], 'I chat with friends. (tranh hai bạn đang trò chuyện)')], 1):
        rows.append((q, a, e, img1(n, nm, 'w1_%d.png' % i)))
    secs.append(sec_fill('w1', 'PART C – Writing. I. Look and write (nhìn tranh, viết câu trả lời).', rows))
    secs.append(sec_order('w2', 'II. Reorder the words (sắp xếp từ thành câu).',
                          [(['swimming.', 'like', 'I'], 'I like swimming.'), (['chess', 'I', 'play', 'break', 'at', 'time.'], 'I play chess at break time.')]))
    return build(n, secs)


if __name__ == '__main__':
    for n, fn in enumerate([de1, de2, de3, de4, de5], 1):
        S, ANS, EXP = fn()
        dump('units/lop3_hk1_de%02d.py' % n, 'SET', S)
        dump('units/lop3_hk1_de%02d_dapan.py' % n, 'ANS', ANS)
        with open(os.path.join(ROOT, 'units/lop3_hk1_de%02d_dapan.py' % n), 'a', encoding='utf8') as f:
            f.write('\nEXPLANATIONS = %s\n' % pprint.pformat(EXP, width=160))
        print(n, sum(len(g['items']) for g in S['pages'][0]['groups']), 'câu')
