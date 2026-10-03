# -*- coding: utf-8 -*-
"""Lớp 4 – nhóm dc1: 3 tài liệu Đề cương HK1 (unit DeCuongHK1) -> 3 bộ luyện tập (slug luyentap_a/_b/_c) có trang lý thuyết + trang bài tập có đáp án.
Chạy: python3 tools/gen_lop4_dc1.py"""
import os, re, sys, json, zlib, random, pprint, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g4_exam import Exam, ROOT, IMGROOT, FONT, cells, imgs
from PIL import Image, ImageDraw

UNIT = 'DeCuongHK1'
TITLES = {1: 'My friends', 2: 'Time and daily routines', 3: 'My week', 4: 'My birthday party', 5: 'Things we can do', 6: 'Our school facilities', 7: 'Our timetables',
          8: 'My favourite subjects', 9: 'Our sports day', 10: 'Our summer holidays'}
E = html.escape


# ------------------------------------------------------------------ tiện ích
def shuffled(words, seed):
    w = list(words)
    for k in range(40):
        random.Random(seed + k).shuffle(w)
        if w != list(words): break
    return w


def lines_of(src):
    return [l.replace('⟦', '').replace('⟧', '') for l in open(os.path.join(IMGROOT, src + '.txt'), encoding='utf8').read().split('\n')]


def new_exam(tag, title, src):
    ex = Exam(tag, UNIT, title, src, slug='luyentap_' + tag.split('_')[1])
    ex.pages = []
    ex._start = 0
    return ex


def begin(ex):
    ex._start = len(ex.groups)


def end(ex, pid, title):
    gs = ex.groups[ex._start:]
    n = sum(len(g['items']) for g in gs)
    assert 0 < n <= 40, (pid, n)
    ex.pages.append({'id': pid, 'title': title, 'mode': 'practice', 'groups': gs})


def mcq(ex, gid, instr, rows, keys, passage=None, img=None):
    """rows: [(câu hỏi, [opts])] ; keys: chuỗi chữ cái. img: list ảnh (cùng độ dài rows) hoặc None"""
    items = []
    for i, ((q, o), k) in enumerate(zip(rows, keys)):
        it = {'t': 'mcq', 'q': q, 'o': list(o)}
        if img and img[i]:
            it['img'] = ex.single(img[i], '%s_%d.png' % (gid, i + 1), w=210, h=150)
        items.append((it, k, 'Đáp án: %s. %s' % (k, o['ABCDEFG'.index(k)])))
    ex.add(gid, instr, items, passage=passage)


def plain_mcq(q, opts, ans, exp=None):
    return ({'t': 'mcq', 'plain': True, 'q': q, 'o': list(opts)}, ans, exp or 'Đáp án: %s' % ans)


def order_rows(ex, gid, instr, sents):
    rows = [(shuffled(s.split(), zlib.crc32((gid + s).encode())), s) for s in sents]
    ex.order(gid, instr, rows)


def grid(ex, names, labels, out, cols=3, w=200, h=150):
    rows = (len(names) + cols - 1) // cols
    gap = 12
    S = Image.new('RGB', (cols * w + (cols - 1) * gap, rows * (h + 34)), 'white')
    d = ImageDraw.Draw(S)
    for i, (nm, lb) in enumerate(zip(names, labels)):
        x, y = (i % cols) * (w + gap), (i // cols) * (h + 34)
        S.paste(ex.cell(nm, w, h), (x, y))
        tw = d.textlength(lb, font=FONT)
        d.text((x + (w - tw) / 2, y + h + 4), lb, fill=(20, 20, 20), font=FONT)
    S.save(os.path.join(ex.out, out), optimize=True)
    return out


def img_tag(ex, nm, alt=''):
    return '<img class="wide" src="%s" alt="%s">' % (ex.asset(nm), alt)


def table(rows, head=None, cls='tb'):
    out = ['<table class="%s">' % cls]
    if head: out.append('<tr>%s</tr>' % ''.join('<th>%s</th>' % h for h in head))
    for r in rows: out.append('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r))
    out.append('</table>')
    return ''.join(out)


def save(ex, theory):
    total = sum(len(g['items']) for p in ex.pages for g in p['groups'])
    S = {'id': 'lop4-%s' % ex.tag.replace('_', '-'), 'title': ex.title, 'grade': 4, 'unit': UNIT, 'theory': theory, 'pages': ex.pages}
    base = 'units/lop4_%s' % ex.tag
    for path, name, obj in ((base + '.py', 'SET', S), (base + '_dapan.py', 'ANS', ex.ANS)):
        with open(os.path.join(ROOT, path), 'w', encoding='utf8') as f:
            f.write('# -*- coding: utf-8 -*-\n"""Sinh bởi tools/gen_lop4_dc1.py"""\n\n%s = %s\n' % (name, pprint.pformat(obj, width=160)))
    with open(os.path.join(ROOT, base + '_dapan.py'), 'a', encoding='utf8') as f:
        f.write('\nEXPLANATIONS = %s\n' % pprint.pformat(ex.EXP, width=160))
    os.makedirs(os.path.join(ROOT, 'units/reg'), exist_ok=True)
    json.dump([S['id'], base + '.py', base + '_dapan.py', 'Lop4', UNIT, ex.slug, 'assets/lop4_%s' % ex.tag, ''],
              open(os.path.join(ROOT, 'units/reg/%s.json' % ex.tag), 'w', encoding='utf8'), ensure_ascii=False)
    print('%-8s %3d câu / %d trang  %s' % (ex.tag, total, len(ex.pages), ' | '.join(ex.notes)))


# ================================================================== (a) Đề cương HK1 2024-2025 (từ vựng Unit 1-10)
def meaning_fix(m):
    m = m.strip()
    if m.count('(') > m.count(')'): m += ')'
    m = re.sub(r'(\S)\(', r'\1 (', m)
    m = m.replace('(dạy TAnh)', '(dạy Tiếng Anh)').replace('Số 30', 'số 30')
    return m


def parse_vocab(L):
    i0 = next(i for i, l in enumerate(L) if l.startswith('IV.'))
    i1 = next(i for i, l in enumerate(L) if l.startswith('V.'))
    units, cur = {}, None
    for l in L[i0 + 1:i1]:
        if not l.startswith('|'): continue
        c = cells(l)
        m = re.match(r'^Unit (\d+)', c[0][0])
        if len(c) == 1 and m:
            cur = int(m.group(1)); units[cur] = []
        elif len(c) == 4 and cur:
            for k in (0, 2):
                units[cur].append((c[k][0].strip(), meaning_fix(c[k + 1][0])))
    return units


def gen_a():
    src = 'De-cuong-on-tap-HK1-Tieng-Anh-4-Global'
    L = lines_of(src)
    ex = new_exam('dc1_a', 'Đề cương HK1 (2024-25)', src)
    V = parse_vocab(L)
    allm = [m for u in V.values() for _, m in u]
    # ---- mẫu câu (bảng 20 cặp)
    pats = []
    iv = next(i for i, l in enumerate(L) if l.startswith('VI.'))
    for l in L[:iv]:
        m = re.match(r'^\|\s*(\d+)\.\s*(.*?)\s*\|\s*(.*?)\s*\|$', l)
        if m and '?' in m.group(2): pats.append((m.group(2).strip(), m.group(3).strip().rstrip('.') + '.' if not m.group(3).strip().endswith(('.', '?')) else m.group(3).strip()))
    assert len(pats) == 20, len(pats)
    # ---- lý thuyết
    th = ['<h3>Đề cương ôn tập môn Tiếng Anh 4 – Học kì 1 (năm học 2024-2025)</h3>',
          '<p>Nội dung: ôn tập từ vựng, mẫu câu, các điểm ngữ pháp và các bài nghe từ Unit 1 đến Unit 10. Bài kiểm tra gồm các kĩ năng nghe, nói, đọc, viết.</p>',
          '<h3>Dạng câu hỏi thường gặp</h3><ul>'
          '<li><b>Listening:</b> listen and number / tick / complete / match.</li>'
          '<li><b>Reading:</b> look, read and complete; choose the correct answer; read and match; read and tick the correct picture.</li>'
          '<li><b>Writing:</b> put the words in order; look at the picture and complete the sentences; write the missing letter.</li></ul>',
          '<h3>Từ vựng Unit 1 – 10</h3>']
    for u in range(1, 11):
        th.append('<h4>Unit %d: %s</h4>' % (u, TITLES[u]))
        w = V[u]
        rows = []
        for i in range(0, len(w), 2):
            a = w[i]; b = w[i + 1] if i + 1 < len(w) else ('', '')
            rows.append(['<b>%s</b>' % E(a[0]), E(a[1]), '<b>%s</b>' % E(b[0]), E(b[1])])
        th.append(table(rows, head=['Vocabulary', 'Meaning', 'Vocabulary', 'Meaning']))
    th.append('<h3>Cấu trúc câu từ Unit 1 đến Unit 10</h3>')
    i0 = next(i for i, l in enumerate(L) if l.startswith('V.'))
    i1 = next(i for i, l in enumerate(L) if l.startswith('| 1.Where'))
    txt = re.sub(r'(?<=\S)(Unit \d+:)', r'\n\1', '\n'.join(L[i0 + 1:i1]))
    cur = None
    for l in txt.split('\n'):
        l = l.strip()
        if not l: continue
        m = re.match(r'^Unit (\d+):$', l)
        if m:
            if cur is not None: th.append('</ul>')
            th.append('<p><b>Unit %s – %s</b></p><ul>' % (m.group(1), TITLES[int(m.group(1))])); cur = 1
        else:
            th.append('<li>%s</li>' % E(l.lstrip('- ').strip()))
    th.append('</ul>')
    th.append('<h3>20 mẫu câu hỏi – trả lời</h3>')
    th.append(table([[E(q), E(a)] for q, a in pats], head=['Hỏi', 'Trả lời']))
    theory = ''.join(th)

    # ---- Trang từ vựng (Anh -> Việt)
    def vocab_items(units, gid):
        its = []
        for u in units:
            for k, (w, m) in enumerate(V[u]):
                same = [x for _, x in V[u] if x != m]
                oth = [x for x in dict.fromkeys(allm) if x != m and x not in same]
                rnd = random.Random(zlib.crc32(w.encode()))
                d = rnd.sample(same, min(3, len(same)))
                if len(d) < 3: d += rnd.sample(oth, 3 - len(d))
                o = shuffled([m] + d, zlib.crc32((w + 'o').encode()))
                its.append(plain_mcq('Unit %d – “%s” nghĩa là gì?' % (u, w), o, m))
        return its
    for pid, ttl, us in (('tu-vung-1', 'Từ vựng Unit 1–3', (1, 2, 3)), ('tu-vung-2', 'Từ vựng Unit 4–5', (4, 5)), ('tu-vung-3', 'Từ vựng Unit 6–10', (6, 7, 8, 9, 10))):
        begin(ex)
        ex.add('v' + pid[-1], 'Chọn nghĩa tiếng Việt đúng của từ / cụm từ. (Unit %s)' % ('–'.join([str(us[0]), str(us[-1])]) if len(us) > 1 else us[0]), vocab_items(us, pid))
        end(ex, pid, ttl)
    # ---- mẫu câu
    begin(ex)
    its = []
    for i, (q, a) in enumerate(pats):
        others = [x for j, (_, x) in enumerate(pats) if j != i and x != a]
        d = random.Random(zlib.crc32(q.encode())).sample(others, 3)
        its.append(plain_mcq('Chọn câu trả lời phù hợp: “%s”' % q, shuffled([a] + d, zlib.crc32((q + 'o').encode())), a))
    ex.add('mc', 'Chọn câu trả lời phù hợp với câu hỏi. (20 mẫu câu Unit 1–10)', its)
    end(ex, 'mau-cau', 'Mẫu câu hỏi – đáp')

    # ---- 1. Look, read and circle
    begin(ex)
    rows = [('A: Where are you from?<br>B: I’m from ………….', ['Viet Nam', 'Japan', 'Thailand']),
            ('A: Where is he from?<br>B: He’s from ………….', ['Malaysia', 'Singapore', 'Japan']),
            ('A: What subjects do you have today?<br>B: I have ………….', ['Maths', 'Art', 'English']),
            ('A: Can you ………….?<br>B: Yes, I can.', ['ride a bike', 'swim', 'ride a horse']),
            ('A: What do you do on Mondays?<br>B: I ………….', ['cook', 'do homework', 'study at school']),
            ('A: What time is it?<br>B: It’s ………….', ['six fifteen', 'six thirty', 'six forty-five']),
            ('A: Why do you like Music?<br>B: Because I want to be a(n) ………….', ['music teacher', 'singer', 'painter']),
            ('There are three ………….. at my school.', ['playground', 'buildings', 'gardens']),
            ('A: When’s your birthday?<br>B: It’s in …………', ['January', 'December', 'November'])]
    mcq(ex, 'c1', 'Look, read and circle the correct answer. (Nhìn tranh, đọc và chọn đáp án đúng.)', rows, 'AAAACCBBB',
        img=[['img0%d' % i] for i in range(1, 10)])
    end(ex, 'nhin-tranh-chon', 'Nhìn tranh, chọn đáp án')
    ex.notes.append('Ex1: đáp án suy từ tranh/ngữ cảnh (đề không có key); câu 5 (img05, lớp học) = study at school, câu 6 (đồng hồ 6:45) = six forty-five, câu 8 (3 dãy nhà) = buildings')

    # ---- 2. Read and complete
    begin(ex)
    paras = [
        ('Ben', '<p>My name is (0) <u>Ben</u>. I am from <b>(1) ______</b>. I <b>(2) ______</b> from Mondays to Fridays. I do housework on Saturdays. I like cooking. I can cook rice, <b>(3) ______</b> and eggs. My <b>(4) ______</b> is in April. I want a big cake at my birthday party.</p>',
         ['Ben', 'birthday', 'go to school', 'Australia', 'chicken'], ['Australia', 'go to school', 'chicken', 'birthday']),
        ('School', '<p>We have a lot of fun at school. In our English lessons, we (0) <u>listen</u> to English songs. We <b>(1) ______</b> and chant. We play board games to learn English. We do projects together at the end of each <b>(2) ______</b>. Today, it is <b>(3) ______</b>. We are in the school garden. There are many <b>(4) ______</b> and birds. We are happy.</p>',
         ['flowers', 'unit', 'sing', 'listen', 'sunny'], ['sing', 'unit', 'sunny', 'flowers']),
        ('Trung', '<p>My name is Trung. I study at ….. Primary School. My school is in the (0) <u>village</u>. There are twenty <b>(1) ______</b>, two computer rooms and a beautiful garden. My favourite <b>(2) ______</b> is Music. I can play the <b>(3) ______</b> and sing with my friends. It is our sports day today. The <b>(4) ______</b> there are fun. It is very great. How about your school?</p>',
         ['activities', 'village', 'piano', 'classrooms', 'subject'], ['classrooms', 'subject', 'piano', 'activities']),
        ('Ben 2', '<p>My name is Ben. I am nine years old. I am from (0) <u>Australia</u>. I am a <b>(1) ______</b> at Rose Primary School. I go to school from Mondays to <b>(2) ______</b>. I like sports and music. I <b>(3) ______</b> on Tuesdays. I play the guitar on Wednesdays. At the weekend, I <b>(4) ______</b> and do housework with my mother.</p>',
         ['Australia', 'stay at home', 'Fridays', 'pupil', 'play football'], ['pupil', 'Fridays', 'play football', 'stay at home'])]
    for k, (nm, ps, bank, ans) in enumerate(paras, 1):
        ex.fill('c2%s' % 'abcd'[k - 1], 'Read and complete. (Đoạn %d – chọn từ trong khung điền vào chỗ trống; từ ở (0) là ví dụ.)' % k,
                [('Chỗ trống (%d): {_}' % (i + 1), [a], None) for i, a in enumerate(ans)], passage=ps, bank=bank)
    end(ex, 'doc-dien-tu', 'Đọc và điền từ')

    # ---- 3. Read and match
    begin(ex)
    names = ['img%d' % i for i in range(10, 19)]
    nm = grid(ex, names, list('abcdefghi'), 'match_pics.png', cols=3, w=200, h=150)
    left = [{'t': t} for t in ['That’s Mr Long.', 'Our Sports Day is in July.', 'I go to school at one fifteen.', 'I want some grapes at my birthday party.',
                               'My school is in the village.', 'She is from Japan.', 'Today is Thursday.', 'He can’t play badminton but he can roller skate.',
                               'I have science on Wednesdays and Fridays.']]
    keys = ['b', 'i', 'e', 'a', 'h', 'g', 'c', 'd', 'f']
    ex.match('c3a', 'Read and match. (Nối mỗi câu với tranh phù hợp a–i.)', left, list('abcdefghi'), keys,
             'Đáp án: ' + ', '.join('%d–%s' % (i + 1, k) for i, k in enumerate(keys)), picture=img_tag(ex, nm, 'Tranh a–i'))
    Q = ['What time is it?', 'What time do you have music class?', 'When’s your birthday?', 'What do you do on Sundays?', 'What subjects do you have today?',
         'What do you do on sports day?', 'Where’s she from?', 'Can your brother ride a bike?', 'What do you want to drink?']
    A = ['It’s six thirty.', 'I have music class at eight fifteen.', 'It’s in October.', 'I stay at home.', 'I have maths and Vietnamese.',
         'We play sports and games.', 'She’s from Singapore.', 'No, he can’t.', 'I want some milk and juice.']
    ex.match('c3b', 'Read and match. (Nối câu hỏi với câu trả lời phù hợp.)', [{'t': q} for q in Q], shuffled(A, 7), A,
             'Đáp án: ' + '; '.join('%s → %s' % (q, a) for q, a in zip(Q, A)))
    end(ex, 'doc-noi', 'Đọc và nối')

    # ---- 4. Order the words
    begin(ex)
    S4 = ['Our Sports Day is in July.', 'There are three music rooms at my school.', 'I want some grapes at my birthday party.', 'My favourite subject is English.',
          'Music is not his favourite subject.', 'They play basketball on Sports day.', 'We do housework at the weekend.', 'There is one building at my school.',
          'I like English because I want to be an English teacher.', 'My brother can’t ride a horse but he can roller skate.',
          'My sister can’t play the piano but she can sing.', 'My parents have dinner at seven o’clock.', 'We go to school from Mondays to Fridays.']
    order_rows(ex, 'c4', 'Order the words to make a complete sentence. (Sắp xếp từ thành câu đúng.)', S4)
    end(ex, 'sap-xep-tu', 'Sắp xếp từ thành câu')
    ex.notes.append('Ex4: đáp án = câu đúng ngữ pháp từ các từ cho sẵn (đề không có key); câu 3 bỏ "to" thừa trong "want to"')

    # ---- 5. Look at the picture and complete
    begin(ex)
    R5 = [('I want some {_} at the party.', ['lemonade'], 'img19'), ('I {_} at school on Friday.', ['study'], 'img20'),
          ('My brother can play the {_}.', ['guitar'], 'img21'), ('I have {_} on Mondays.', ['science'], 'img22'),
          ('My school is in the {_}.', ['mountains', 'mountain'], 'img23'), ('Lucy is from {_}.', ['Britain'], 'img24'),
          ('I have breakfast at six {_}.', ['fifteen'], 'img25'), ('There is one {_} at my school.', ['building', 'garden'], 'img26'),
          ('He is from {_}.', ['America'], 'img27'), ('I have {_} today.', ['history and geography', 'geography and history'], 'img28'),
          ('My birthday is in {_}.', ['August'], 'img29'), ('There is a {_}.', ['playground'], 'img30'),
          ('I like art because I want to be a(n) {_}.', ['painter'], 'img31'), ('I have {_} at six o’clock.', ['breakfast'], 'img32'),
          ('My birthday is in {_}.', ['March'], 'img33'), ('I stay at home on {_}.', ['Saturdays', 'Saturday'], 'img34'),
          ('I have music on {_}.', ['Wednesdays', 'Wednesday'], 'img35'), ('My school is in the {_}.', ['village'], 'img36')]
    ex.fill('c5', 'Look at the picture and complete the sentences. (Nhìn tranh và hoàn thành câu.)', R5)
    end(ex, 'nhin-tranh-dien', 'Nhìn tranh, hoàn thành câu')
    ex.notes.append('Bỏ Speaking; đề gốc không có key nên mọi đáp án suy từ tranh (câu 8 chấp nhận building/garden)')
    save(ex, theory)


# ================================================================== (b) Đề cương cuối HK1
def gen_b():
    src = 'De-cuong-on-tap-cuoi-HK1-Tieng-Anh-4'
    L = lines_of(src)
    ex = new_exam('dc1_b', 'Đề cương cuối HK1', src)
    # ---- lý thuyết: các mẫu câu từng unit
    i0 = next(i for i, l in enumerate(L) if l.startswith('CÁC MẪU CÂU'))
    th = ['<h3>Các mẫu câu của từng Unit</h3>', '<p>Đề cương cuối HK1 gồm 4 phần: Speaking, Listening, Reading, Writing. Dưới đây là các mẫu câu cần nhớ (Unit 1–9).</p>']
    rows, pend, first = [], None, True

    def flush():
        nonlocal rows
        if rows: th.append(table([[E(a), E(b)] for a, b in rows], head=['Câu hỏi', 'Câu trả lời'])); rows = []

    def clean(s):
        s = s.replace('housewwork', 'housework').replace('No. I can’t', 'No, I can’t')
        return re.sub(r'[….]{3,}', '……', s).strip()
    for l in L[i0 + 1:]:
        l = l.strip()
        if not l: continue
        m = re.match(r'^UNIT (\d+): (.*)$', l)
        if m:
            if pend: rows.append((pend, '')); pend = None
            flush(); th.append('<h4>Unit %s: %s</h4>' % (m.group(1), E(m.group(2)))); continue
        if l.startswith('→'):
            rows.append((pend, clean(l[1:]))); pend = None
        elif '→' in l:
            if pend: rows.append((pend, '')); pend = None
            q, a = l.split('→', 1); rows.append((clean(q), clean(a)))
        else:
            if pend: rows.append((pend, ''))
            pend = clean(l)
    if pend: rows.append((pend, ''))
    flush()
    theory = ''.join(th)

    # ---- Reading part 1
    begin(ex)
    rows1 = [('Where are you from? – I ____ from Viet Nam.', ['am', 'is']), ('____ science on Mondays and Fridays. (I ____)', ['have', 'has']),
             ('How many ____ are there at your school?', ['garden', 'gardens']), ('What do you want to ____? – I want some grapes.', ['eat', 'drink']),
             ('My birthday is in ____.', ['Monday', 'September'])]
    rows1[1] = ('I ____ science on Mondays and Fridays.', ['have', 'has'])
    mcq(ex, 'r1', 'Read and circle the correct word. (Đọc và chọn từ đúng.)', rows1, 'AABAB')
    # ---- Part 2 T/F
    ben = ('My name is Ben. I am nine years old. I am from Australia. I am a pupil at Rose Primary School. I go to school from Mondays to Fridays. I like sports and music. '
           'I play football on Tuesdays. I play the guitar on Wednesdays. At the weekend, I stay at home and do housework with my mother.')
    nm = ex.single(['img01'], 'ben.png', w=180, h=200)
    ex.tf('r2', 'Look and read. Tick True or False. (Đọc đoạn văn về Ben và chọn Đúng/Sai.)',
          [('His name is Ben.', 'T', None, 'Đúng: “My name is Ben.”'), ('He is from Australia.', 'T', None, 'Đúng: “I am from Australia.”'),
           ('He doesn’t go to school on Saturdays and Sundays.', 'T', None, 'Đúng: Ben đi học từ thứ Hai đến thứ Sáu.'),
           ('He plays the piano on Wednesdays.', 'F', None, 'Sai: Ben chơi đàn guitar vào thứ Tư (“I play the guitar on Wednesdays”).'),
           ('He stays at home and does housework on Tuesdays.', 'F', None, 'Sai: Ben ở nhà làm việc nhà vào cuối tuần; thứ Ba Ben chơi bóng đá.')],
          passage='<p>%s</p>%s' % (ben, img_tag(ex, nm, 'Ben')))
    end(ex, 'doc-chon', 'Đọc: chọn từ, Đúng/Sai')

    # ---- Part 3, 4 match
    begin(ex)
    Q = ['What time is it?', 'Where’s she from?', 'When’s your birthday?', 'What do you want to drink?', 'What subjects do you have today?']
    A = ['It’s six thirty.', 'She’s from Singapore.', 'It’s in October.', 'I want some milk and juice.', 'I have English, maths and Vietnamese.']
    ex.match('r3', 'Read and match. (Nối câu hỏi với câu trả lời phù hợp.)', [{'t': q} for q in Q], shuffled(A, 3), A, 'Đáp án: ' + '; '.join('%s → %s' % x for x in zip(Q, A)))
    Q = ['What time is it?', 'What do you do on sports day?', 'What time do you have music class?', 'Can your brother ride a bike?', 'What do you do on Sundays?']
    A = ['It’s six thirty.', 'We play sports and games.', 'I have music class at eight fifteen.', 'No, he can’t.', 'I stay at home.']
    ex.match('r4', 'Read and match. (Nối câu hỏi với câu trả lời phù hợp.)', [{'t': q} for q in Q], shuffled(A, 5), A, 'Đáp án: ' + '; '.join('%s → %s' % x for x in zip(Q, A)))
    end(ex, 'doc-noi', 'Đọc và nối')

    # ---- Part 5 read and complete
    begin(ex)
    bank_imgs = ['img05', 'img06', 'img07', 'img08', 'img09']
    bank_words = ['Sports day', 'village', 'sing', 'computer rooms', 'Music']
    nm = ex.strip(bank_imgs, bank_words, 'bank5.png', w=150, h=115)
    ps = ('<p>My name is Trung. I study at Nghia Lam Primary School. My school is in the (0) <u>village</u>. There are twenty classrooms, two <b>(1) ______</b> and a beautiful garden. '
          'My favourite subject is <b>(2) ______</b>. I can play the piano and <b>(3) ______</b> with my friends. It is our <b>(4) ______</b> today. The activities there are fun. It is very great. How about your school?</p>')
    ex.fill('r5', 'Read and complete. (Chọn từ trong khung điền vào chỗ trống; từ ở (0) là ví dụ.)',
            [('Chỗ trống (%d): {_}' % (i + 1), [a], None) for i, a in enumerate(['computer rooms', 'Music', 'sing', 'Sports day'])],
            passage=ps + img_tag(ex, nm, 'Khung từ'), bank=bank_words)
    # ---- Part 6 tick the correct picture
    its = []
    spec = [('I can roller skate.', None), ]
    P6 = [('He is from Singapore.', ['img16', 'img18'], ['Japan', 'Singapore'], 1),
          ('I want some chips.', ['img22', 'img20'], ['chips', 'fish'], 0),
          ('My school is in the town.', ['img26', 'img24'], ['mountains', 'town'], 1),
          ('I like music because I want to be a singer.', ['img28', 'img30', 'img11'], ['doctor', 'singer', 'painter'], 1)]
    for k, (q, pics, labs, ai) in enumerate(P6, 1):
        lt = 'ABC'[:len(pics)]
        f = ex.strip(pics, list(lt), 'p6_%d.png' % k, w=150, h=125)
        its.append(({'t': 'mcq', 'plain': True, 'wide': True, 'img': f, 'q': '“%s” – Chọn tranh đúng.' % q, 'o': list(lt)}, lt[ai],
                    'Đáp án %s: tranh %s (%s).' % (lt[ai], lt[ai], labs[ai])))
    ex.add('r6', 'Read and tick the correct picture. (Đọc câu và chọn tranh đúng.)', its)
    end(ex, 'doc-dien-tranh', 'Đọc: điền từ, chọn tranh')
    ex.notes.append('Part 6: tranh bị mất dấu tick (các tranh nhân đôi) -> chọn tranh theo nghĩa câu; bỏ câu ví dụ 0; câu 3 suy từ tranh (img24 trường thị trấn, img26 có núi)')

    # ---- Writing
    begin(ex)
    ex.fill('w1', 'Look at the picture and complete the sentences. (Nhìn tranh và hoàn thành câu.)',
            [('Lucy is from {_}.', ['Britain'], 'img32'), ('I want some {_} at the party.', ['lemonade'], 'img33'),
             ('There is one {_} at my school.', ['building', 'garden'], 'img34')])
    S2 = ['Music is not his favourite subject.', 'They play basketball on Sports day.', 'We go to school from Mondays to Fridays.', 'We do housework at the weekend.',
          'There is one building at my school.', 'They have English on Tuesdays and Thursdays.', 'My sister can’t play the piano but she can sing.',
          'I like English because I want to be an English teacher.', 'There are three buildings at my school.', 'I have history and geography on Mondays.']
    order_rows(ex, 'w2', 'Reorder the words to make a correct sentence. (Sắp xếp từ thành câu đúng.)', S2)
    ex.fill('w3', 'Write the missing letters. (Viết các chữ cái còn thiếu.)',
            [('Sat{_}day', ['ur'], 'img36'), ('vi{_}ge', ['lla'], 'img37')])
    ex.fill('w4', 'Look at the picture and complete the sentences. (Nhìn tranh và hoàn thành câu.)',
            [('I have breakfast at six {_}.', ['fifteen'], 'img38'), ('I go to school on {_}.', ['Wednesday', 'Wednesdays'], 'img39'),
             ('My school is in the {_}.', ['mountains', 'mountain'], 'img40')])
    end(ex, 'viet', 'Viết')
    ex.notes.append('Bỏ Speaking và các câu ví dụ (0); đề không có key nên đáp án suy từ tranh/ngữ pháp')
    save(ex, theory)


# ================================================================== (c) Đề cương HK1 2025-2026
def theory_c(L):
    i0 = next(i for i, l in enumerate(L) if l.startswith('ÔN LÝ THUYẾT'))
    i1 = next(i for i, l in enumerate(L) if l.startswith('ÔN BÀI TẬP'))
    out, tb = ['<h3>Ôn lý thuyết Unit 1 – 10 (năm học 2025-2026)</h3>'], []

    def flush():
        nonlocal tb
        if not tb: return
        mx = max(len(r) for r in tb)
        rs = []
        for r in tb:
            if all(not c.strip() for c in r): continue
            tds = []
            for j, c in enumerate(r):
                span = ' colspan="%d"' % (mx - len(r) + 1) if j == len(r) - 1 and len(r) < mx else ''
                c = E(c).replace(' ¦ ', '<br>').replace('¦', '<br>')
                if j == 0 and c.strip().endswith(':') and len(r) > 1: c = '<b>%s</b>' % c
                tds.append('<td%s>%s</td>' % (span, c))
            rs.append('<tr>%s</tr>' % ''.join(tds))
        out.append('<table class="tb">%s</table>' % ''.join(rs)); tb = []
    for l in L[i0 + 1:i1]:
        s = l.strip()
        if not s: continue
        if s.startswith('|'):
            tb.append([c.strip() for c in s.strip('|').split('|')]); continue
        flush()
        m = re.match(r'^UNIT (\d+)$', s)
        if m:
            out.append('<h3>Unit %s: %s</h3>' % (m.group(1), TITLES[int(m.group(1))]))
        elif re.match(r'^\d+\.\s', s) or s.startswith('Cách'):
            out.append('<h4>%s</h4>' % E(s))
        elif re.match(r'^(Lưu ý|Mở rộng):', s):
            a, b = s.split(':', 1); out.append('<p><b>%s:</b> %s</p>' % (a, E(b.strip())))
        else:
            out.append('<p>%s</p>' % E(s))
    flush()
    return ''.join(out)


def gen_c():
    src = 'De-cuong-on-tap-HK1-Tieng-Anh-4-Global-25-26'
    L = lines_of(src)
    ex = new_exam('dc1_c', 'Đề cương HK1 (2025-26)', src)
    theory = theory_c(L)
    ex.k = 0
    MC = lambda *a: a

    def block(gid, instr, rows, keys):
        mcq(ex, gid, instr, [(r[0], list(r[1:])) for r in rows], keys)
    CIR = 'Read and circle the best answer. (Đọc và chọn đáp án đúng.)'
    ORD = 'Reorder the words to make sentences. (Sắp xếp từ thành câu đúng.)'
    FIL = 'Complete these sentences by filling in the blank. (Điền từ vào chỗ trống.)'
    MAT = 'Match each question with a suitable answer. (Nối câu hỏi với câu trả lời phù hợp.)'

    def match(gid, Q, A, keys):
        ans = [A[ord(k) - 65] for k in keys]
        ex.match(gid, MAT, [{'t': q} for q in Q], shuffled(A, zlib.crc32(gid.encode())), ans, 'Đáp án: ' + '; '.join('%d–%s' % (i + 1, k) for i, k in enumerate(keys)))

    def fills(gid, instr, rows, passage=None):
        ex.fill(gid, instr, [(q.replace('____', '{_}') if '{_}' not in q else q, a if isinstance(a, list) else [a], None) for q, a in rows], passage=passage)

    def correct(gid, instr, rows):
        ex.fill(gid, instr, [('Tìm lỗi sai và viết lại câu đúng: <i>%s</i><br>{_}' % q, a, None, 'Câu đúng: %s' % a[0]) for q, a in rows])

    # ===== Unit 1–2
    begin(ex)
    tb = table([['<b>Name</b>', 'Lucy', 'Ben', 'Akiko', 'Mary', 'Hoa'], ['<b>Country</b>', 'England', 'America', 'Japan', 'America', 'Viet Nam']])
    ex.fill('e1', 'Exercise 1. Look at the table and fill in the blank. (Nhìn bảng và điền từ.)',
            [('I am {_} Viet Nam.', ['from'], None), ('Lucy is from {_}.', ['England'], None), ('Ben and Mary are from {_}.', ['America'], None),
             ('{_} is from Japan.', ['Akiko'], None), ('{_} is from Viet Nam.', ['Hoa'], None)], passage=tb)
    block('e2', 'Exercise 2. ' + CIR, [
        ('Ben is ______ Australia.', 'come', 'from', 'new', 'friend'), ('______ are you from?', 'What', 'Who', 'Where', 'How'),
        ('They are from ______.', 'Britain', 'friend', 'new', 'where'), ('John is my new ______.', 'come', 'America', 'friend', 'from'),
        ('Where are you from? – I ______ from Vietnam.', 'am', 'is', 'are', 'new'), ('Mary ______ from Malaysia.', 'is', 'new', 'am', 'are'),
        ('Akiko and Mina ______ new friends.', 'are', 'from', 'is', 'am'), ('They ______ from Japan.', 'friends', 'is', 'am', 'are'),
        ('Is Minh from Vietnam? – Yes, he ______.', 'is', 'am', 'are', 'come'), ('______ you from Britain?', 'Is', 'Am', 'Are', 'We')], 'BCACAAADAC')
    order_rows(ex, 'e3', 'Exercise 3. ' + ORD, ['Where are you from?', 'I am from Britain.', 'Where is Quan from?', 'She is from Singapore.', 'Are they from Thailand?'])
    end(ex, 'unit-1', 'Unit 1')
    begin(ex)
    ex.fill('e4', 'Exercise 4. Write the time in two ways. (Viết giờ theo cách thứ hai: giờ kém / giờ quá.)',
            [('4:15 – It’s four fifteen. = It’s {_} past four.', ['a quarter', 'quarter'], None, 'Đáp án: It’s a quarter past four.'),
             ('6:45 – It’s six forty-five. = It’s {_} to seven.', ['a quarter', 'quarter'], None, 'Đáp án: It’s a quarter to seven.'),
             ('5:30 – It’s five thirty. = It’s {_} past five.', ['half', 'a half'], None, 'Đáp án: It’s half past five.'),
             ('11:50 – It’s eleven fifty. = It’s {_} to twelve.', ['ten'], None, 'Đáp án: It’s ten to twelve.'),
             ('9:40 – It’s nine forty. = It’s {_} to ten.', ['twenty'], None, 'Đáp án: It’s twenty to ten.')])
    match('e5', ['Hi Nam! How are you?', 'What time is it?', 'What time do you get up today?', 'What does he do at 4 p.m.?', 'Do you have breakfast at 6:30?'],
          ['I get up at 6 o’clock.', 'He plays chess with his friends.', 'No. I have breakfast at 6:15.', 'I’m well. And you?', 'It’s seven o’clock.'], 'DEABC')
    order_rows(ex, 'e6', 'Exercise 6. ' + ORD, ['What time do you get up?', 'My father gets up at 6 o’clock.', 'I go to school at 7 o’clock.',
                                                'My brother goes to bed at ten o’clock.', 'What do you do at 9 P.M.?'])
    end(ex, 'unit-2', 'Unit 2')

    # ===== Unit 3
    begin(ex)
    block('e7', 'Exercise 7. ' + CIR, [
        ('______, Tuesday, Wednesday.', 'Sunday', 'Monday', 'Thursday', 'Saturday'), ('Thursday, Friday, ______.', 'Saturday', 'Sunday', 'Thursday', 'Wednesday'),
        ('Sunday, Saturday, ______.', 'Monday', 'Friday', 'Tuesday', 'Wednesday'), ('Monday, ______, Wednesday.', 'Friday', 'weekend', 'Thursday', 'Tuesday'),
        ('______ is after Tuesday.', 'Sunday', 'Monday', 'Wednesday', 'Thursday'), ('______ is before Sunday.', 'Saturday', 'Monday', 'Friday', 'weekday'),
        ('______ is between Friday and Sunday.', 'Thursday', 'Monday', 'Saturday', 'Wednesday'), ('What day is it today? – It’s ______.', 'weekend', 'today', 'Sunday', 'morning'),
        ('What do you do on Sundays? – I ______ housework.', 'go', 'do', 'help', 'study'), ('What do you do ______ Mondays?', 'in', 'on', 'at', 'from')], 'BABDCACCBB')
    fills('e8', 'Exercise 8. ' + FIL, [
        ('What {_} is it today, Minh?', 'day'), ('{_} is Friday.', 'It'), ('She {_} the piano on Sundays.', 'plays'), ('{_} the morning, I go to school.', 'In'),
        ('{_} Saturdays, John does housework.', 'On'), ('I usually go to the library {_} the weekend.', 'at'), ('What {_} you do on Thursdays?', 'do'),
        ('What day {_} it today?', 'is'), ('{_} he go to school on Wednesdays?', 'Does'), ('I visit my grandparents {_} Sundays.', 'on')])
    end(ex, 'unit-3', 'Unit 3')

    # ===== Unit 5 (đề cương không có bài Unit 4)
    begin(ex)
    match('e9', ['I can play guitar.', 'Can he draw?', 'Can she ride a bike?', 'What can they do?', 'What can your father do?'],
          ['They can play football.', 'I can play guitar, too.', 'Yes, he can.', 'No, she can’t.', 'He can swim.'], 'BCDAE')
    block('e10', 'Exercise 10. ' + CIR, [
        ('______ you play chess?', 'can', 'what', 'does', 'are'), ('What can he ______?', 'do', 'does', 'is', 'are'), ('______ can they do?', 'What', 'When', 'How', 'Where'),
        ('What can ______ do?', 'your', 'his', 'her', 'she'), ('Can he ride a ______?', 'kite', 'horse', 'skate', 'car'), ('Can she draw a picture? – ______, she can.', 'No', 'Yes', 'Can', 'What'),
        ('Can Peter swim? – No, he ______.', 'No', 'Yes', 'can', 'can’t'), ('Can they read a book? – Yes, ______ can.', 'he', 'she', 'they', 'you'),
        ('Can they ______ a picture?', 'draws', 'draw', 'drawing', 'drew'), ('My mother can ______.', 'cooks', 'cook', 'cooking', 'cooked')], 'AAADBBDCBB')
    order_rows(ex, 'e11', 'Exercise 11. ' + ORD, ['What can you do, Jim?', 'Can you ride a horse?', 'I can’t cook but I can fly a kite.', 'What can dogs do?',
                                                  'Monkey can climb the tree and eat the bananas.'])
    end(ex, 'unit-5', 'Unit 5')

    # ===== Unit 6
    begin(ex)
    ex.fill('e12', 'Exercise 12. Read and fill in the blank by using “is” or “are”. (Điền is hoặc are.)',
            [('There {_} two buildings at my school.', ['are'], None), ('There {_} one garden at my school.', ['is'], None), ('There {_} ten classrooms at my school.', ['are'], None),
             ('There {_} a library at my school.', ['is'], None), ('There {_} one playground at my school.', ['is'], None)])
    block('e13', 'Exercise 13. ' + CIR, [
        ('______ is your school?', 'What', 'When', 'Where', 'How'), ('Where is ______ school?', 'she', 'him', 'his', 'hers'), ('Where is ______ school?', 'them', 'they', 'her', 'his'),
        ('It’s ______ the city.', 'on', 'in', 'at', 'from'), ('How many ______ are there at your school?', 'building', 'buildings', 'classroom', 'classroomes'),
        ('How many ______ are there at his school?', 'gardens', 'garden', 'playground', 'playgroundes'), ('There ______ a library at my school.', 'is', 'are', 'have', 'has'),
        ('There ______ some classrooms at my school.', 'is', 'are', 'have', 'has'), ('Is there a ______ at your school?', 'computer room', 'gardens', 'playgrounds', 'classrooms'),
        ('Are there five ______ in your village?', 'schools', 'city', 'library', 'house')], 'CCCBBAABAA')
    order_rows(ex, 'e14', 'Exercise 14. ' + ORD, ['Where is your school?', 'It is in the city.', 'There are four buildings at my school.',
                                                  'How many gardens are there at her school?', 'Is your school in the mountains?'])
    end(ex, 'unit-6', 'Unit 6')

    # ===== Unit 7
    begin(ex)
    block('e15', 'Exercise 15. ' + CIR, [
        ('What ______ do you have today?', 'subject', 'maths', 'maths', 'subjects'), ('I have ______ today.', 'Japan', 'Australia', 'Vietnamese', 'America'),
        ('When ______ you have English?', 'do', 'does', 'did', 'done'), ('What subjects does Bob have ______ Tuesdays?', 'in', 'on', 'at', 'from'),
        ('When ______ Lina have English?', 'do', 'does', 'did', 'done'), ('They ______ maths today.', 'have', 'has', 'doesn’t', 'does'),
        ('Giang ______ music on Thursday.', 'have', 'has', 'doesn’t', 'does'), ('I ______ science on Tuesdays.', 'have', 'has', 'had', 'haves'),
        ('Ryan ______ Vietnamese, maths, and art today.', 'have', 'has', 'had', 'haves'), ('We ______ English, history and geography, and music on Mondays.', 'have', 'has', 'had', 'haves')], 'DCABBABABA')
    correct('e16', 'Exercise 16. Find mistakes in each sentence and correct them. (Tìm lỗi sai và sửa.)', [
        ('Today is on Monday.', ['Today is Monday.']), ('She have science, art and English.', ['She has science, art and English.']),
        ('She doesn’t has maths on Tuesday.', ['She doesn’t have maths on Tuesday.', 'She doesn’t have maths on Tuesdays.']),
        ('Music and Art is my favourite subjects.', ['Music and Art are my favourite subjects.']),
        ('When do she have Science? She has it on Monday and Wednesday.', ['When does she have Science? She has it on Monday and Wednesday.', 'When does she have Science? She has it on Mondays and Wednesdays.']),
        ('What subject do you have today?', ['What subjects do you have today?'])])
    order_rows(ex, 'e17', 'Exercise 17. ' + ORD, ['What subjects do you have on Friday?', 'John has geography and history today.', 'Do you have Vietnamese today?',
                                                  'I do not have music and art on Mondays.', 'Maths is my favourite subject.'])
    end(ex, 'unit-7', 'Unit 7')

    # ===== Unit 8
    begin(ex)
    fills('e18', 'Exercise 18. ' + FIL, [
        ('What is your {_} subject?', 'favourite'), ('{_} is her favourite subject?', 'What'), ('His {_} subject is English.', 'favourite'), ('{_} does Huy like Maths?', 'Why'),
        ('She wants to be a {_} because she likes drawing.', 'painter'), ('Music is my {_} subject.', 'favourite'), ('We learn how to use computers in {_}.', 'IT'),
        ('Science is my favourite {_}.', 'subject'), ('Ms. Hoa is my {_} teacher. She teaches us how to read and write.', 'Vietnamese'), ('Mr. Long is my favourite {_}.', 'teacher')])
    correct('e19', 'Exercise 19. Find mistakes in each sentence and correct them. (Tìm lỗi sai và sửa.)', [
        ('Today is on Monday.', ['Today is Monday.']), ('What is you favourite subject?', ['What is your favourite subject?']),
        ('Why is her favourite subject?', ['What is her favourite subject?']), ('What are his favourite subject?', ['What is his favourite subject?']),
        ('It are English.', ['It is English.', 'It’s English.']), ('He favourite subject is maths.', ['His favourite subject is maths.']),
        ('English are my favourite subject.', ['English is my favourite subject.']), ('Why does you like science?', ['Why do you like science?']),
        ('Because he want to be a painter.', ['Because he wants to be a painter.']), ('Why does Lina likes music?', ['Why does Lina like music?'])])
    end(ex, 'unit-8', 'Unit 8')

    # ===== Unit 9–10
    begin(ex)
    block('e20', 'Exercise 20. ' + CIR, [
        ('Is your sports day ______ June?', 'in', 'on', 'at', 'from'), ('______ is your sports day?', 'What', 'When', 'Where', 'Why'),
        ('Is their sports day in May? – ______, it is.', 'Yes', 'No', 'Too', 'Do'), ('Is his sports day in September? – No, it ______.', 'is', 'are', 'isn’t', 'aren’t'),
        ('When is ______ sports day?', 'her', 'she', 'he', 'him'), ('When is ______ sports day?', 'they', 'we', 'their', 'us'),
        ('When is your sports day? – It’s in ______.', 'Monday', 'Wednesday', 'October', 'month'), ('Is her ______ day in January?', 'sport', 'sports', 'month', 'months'),
        ('Is her sports day in May? – Yes, it ______.', 'is', 'are', 'isn’t', 'aren’t'), ('Is his sports day in May? – No, it ______.', 'is', 'are', 'isn’t', 'aren’t')], 'ABACACCBAC')
    order_rows(ex, 'e21', 'Exercise 21. ' + ORD, ['When is your sports day?', 'My sports day is in May.', 'Is Linda’s sports day in September?', 'No, it isn’t. It is in June.', 'When is his sports day?'])
    match('e22', ['Were you on the beach last summer?', 'Where were you last weekend?', 'Was she at the campsite yesterday?', 'Where was Tony last summer?', 'How was your holiday?'],
          ['No, she wasn’t.', 'He was in Sydney.', 'It was great.', 'I was at the zoo.', 'Yes, I was.'], 'EDABC')
    end(ex, 'unit-9', 'Unit 9')
    begin(ex)
    block('e23', 'Exercise 23. ' + CIR, [
        ('______ you on the beach last summer?', 'Was', 'Were', 'Is', 'Are'), ('______ she at the campsite yesterday?', 'Was', 'Were', 'Is', 'Are'),
        ('Was he ______ the zoo last weekend?', 'in', 'on', 'at', 'from'), ('Were you ______ the countryside last summer?', 'in', 'on', 'at', 'from'),
        ('______ were you last summer?', 'Where', 'When', 'What', 'Which'), ('Where was ______ last summer?', 'they', 'he', 'we', 'her'),
        ('Where were ______ last summer?', 'she', 'he', 'Linda', 'they'), ('Were you in the mountains last weekend? – ______, I was.', 'Yes', 'No', 'Do', 'Don’t'),
        ('Were John in the mountains last weekend? – ______, I wasn’t.', 'Yes', 'No', 'Do', 'Don’t'), ('I ______ in the countryside last weekend.', 'was', 'were', 'is', 'are')], 'BACAABDABA')
    order_rows(ex, 'e24', 'Exercise 24. ' + ORD, ['Were you in the countryside last summer?', 'I was on the beach.', 'Mary was at the campsite yesterday.', 'Where were you last weekend?', 'My holiday was great.'])
    end(ex, 'unit-10', 'Unit 10')
    ex.notes.append('Sửa lỗi gõ trong đề: Ex10.7 "can’"->"can’t", Ex20.2 thiếu nhãn C, Ex14.3 "building"->"buildings"; Ex17.4 dùng "do not" theo từ cho sẵn; Ex24.5 suy từ các từ cho sẵn (key thiếu)')
    save(ex, theory)


if __name__ == '__main__':
    gen_a(); gen_b(); gen_c()
    d = os.path.join(ROOT, 'assets/lop4_dc1_c')
    if os.path.isdir(d) and not os.listdir(d): os.rmdir(d)
