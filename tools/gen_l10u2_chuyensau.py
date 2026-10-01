"""Chuyển đổi 1 lần: Word 'Bài tập chuyên sâu' Lớp 10 Unit 2 (Humans and the environment) -> units/lop10_u2_chuyensau.py (khung câu hỏi).
Đáp án + giải thích soạn tay ở units/lop10_u2_chuyensau_dapan.py (đối chiếu khoá nửa sau file src/l10u2/cs_c.txt rồi tự giải).
Nguồn src/l10u2/cs_c.txt: dòng 1-1315 = đề (lý thuyết, bài tập, Test 1, Test 2, Test 3 – nhãn gốc 'TEST 2' lần hai),
dòng 1316-2580 = khoá (lặp lại lý thuyết + đáp án). Không có phần Unit khác lẫn vào.
Gồm: lý thuyết (từ vựng, will/be going to, bị động), bài tập vận dụng, Test 1, Test 2, Test 3 (140 câu, trang kiểm tra)."""
import re, sys, os, glob, zipfile
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import parse_mcq, cl
from theory import theory_html
import pprint

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = open(os.path.join(ROOT, 'src/l10u2/cs_c.txt'), encoding='utf8').read()

# ---- sửa lỗi nguồn (chuỗi -> chuỗi), không đổi số dòng
FIX = [
    ('pultry', 'poultry'), ('museles', 'muscles'), ('some ot which', 'some of which'),
    ('l06.', '106.'), ('l08.', '108.'), ('(l10)', '(110)'), ('l10.', '110.'), ('6l.', '61.'),
    ('fiee', 'free'), ('ﬁrst', 'first'), ('ﬁber', 'fiber'), ('ﬁ', 'fi'),
    ('But now (111)', 'But how (111)'),
    ('113. A by ', '113. A. by '), ('D.with', 'D. with'), ('C. ump', 'C. jump'),
    ('too seared', 'too scared'), ('How arc you', 'How are you'), ('Can 1 listen', 'Can I listen'),
    ('shall 1 take', 'shall I take'), ('1 am sorry', 'I am sorry'),
    ('an At on', 'an A+ on'), ('Albeit Landon', 'Albert Landon'), ('Tottemham', 'Tottenham'), ('Edinburg ', 'Edinburgh '),
    ('The hrain', 'The brain'), ('tasks bellow', 'tasks below'), ('B. stabled', 'B. stabilized'),
    ('Skeleton', 'skeleton'), ('Mark the letter A. 8, C. or D', 'Mark the letter A, B, C, or D'),
    ('Wow!\t ____', 'Wow! ____'),
    ('What can I do for you?\n', 'What can I do for you?”\n'), ('clouds!“', 'clouds!”'), ("start?’", 'start?”'), ('D. Provides', 'D. provides'), ('C. Protect', 'C. protect'),
    ('C. Sore', 'C. sore'), ('D. Which', 'D. which'), ('C. Use\t', 'C. use\t'),
]
for a, b in FIX:
    RAW = RAW.replace(a, b)
RAW = re.sub(r'(_{3,})- tennis', r'\1 tennis', RAW)
RAW = RAW.replace('‘', '’')
L = RAW.split('\n')
assert L[1315].startswith('⟦<b>ĐÁP ÁN'), L[1315]


def R(a, b):
    """dòng a..b (1-based, gồm cả hai đầu) của cs_c.txt (phần đề)"""
    assert b <= 1315
    return L[a - 1:b]


def keepu(s):
    s = re.sub(r'<u>(\s*)</u>', r'\1', s)
    s = re.sub(r'</u>(\s*)<u>', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def items_of(ev):
    return [v for k, v in ev if k == 'item']


def mk_mcq(gid, items, start=1, plain=False):
    out = []
    for k, it in enumerate(items, start):
        d = {'id': '%s.%d' % (gid, k), 't': 'mcq', 'q': keepu(it['q']), 'o': [keepu(x) for x in it['o']]}
        if plain:
            d['plain'] = True
        out.append(d)
    return out


def blankify(s):
    s = re.sub(r'(?:<u>)?\s*(?:…+\.*|_{3,}|\.{4,})\s*(?:</u>)?', ' {_} ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'\s+([.,?!;:])', r'\1', s)
    return s


def numbered(lines, br=False):
    """[(n, text)] gộp dòng tiếp theo vào câu trước (br=True: dòng 'A:'/'B:' xuống dòng)"""
    out = []
    for ln in lines:
        t = cl(ln)
        if not t:
            continue
        m = re.match(r'^(\d+)\s*\.\s*(.*)$', t)
        if m:
            out.append([int(m.group(1)), m.group(2).strip()])
        elif out:
            out[-1][1] += (' <br>' if br and re.match(r'^[AB]:', t) else ' ') + t
    return [(n, s) for n, s in out]


def fills(gid, lines, expect=None, long=False, br=False, tail=True):
    out = []
    for n, s in numbered(lines, br=br):
        q = blankify(s)
        if tail and q.endswith('{_}'):
            q += '.'
        it = {'id': '%s.%d' % (gid, len(out) + 1), 't': 'fill', 'q': q}
        if long:
            it['long'] = True
        out.append(it)
    if expect:
        assert len(out) == expect, (gid, len(out), expect)
    return out


def two_choice(gid, lines, opts, expect):
    """câu đánh số, chọn 1 trong 2-3 nhãn (plain)"""
    its = []
    for n, s in numbered(lines):
        its.append({'id': '%s.%d' % (gid, len(its) + 1), 't': 'mcq', 'q': keepu(s), 'o': list(opts), 'plain': True})
    assert len(its) == expect, (gid, len(its))
    return its


def para_html(lines, keepb=True):
    out = []
    for l in lines:
        t = l.replace('⟦', '').replace('⟧', '').replace('\t', ' ').replace('\xa0', ' ')
        if not keepb:
            t = re.sub(r'</?b>', '', t)
        t = keepu(t)
        if t:
            out.append('<p>%s</p>' % t)
    return ''.join(out)


def mcq_range(gid, a, b, expect, plain=False, shift_numbers=False):
    lines = R(a, b)
    if shift_numbers:
        first = next(int(re.match(r'^\s*(\d+)', cl(l)).group(1)) for l in lines if re.match(r'^\s*\d+', cl(l)))
        off = first - 1
        lines = [re.sub(r'^(\s*)(\d+)(\s*\.)', lambda m: '%s%d%s' % (m.group(1), int(m.group(2)) - off, m.group(3)), l) for l in lines]
    ev = parse_mcq(lines, expect=1)
    its = items_of(ev)
    assert len(its) == expect, (gid, len(its), expect)
    for it in its:
        assert len(it['o']) >= 2, (gid, it)
    return mk_mcq(gid, its, plain=plain)


def err_items(gid, lines, expect):
    """câu có 4 chỗ gạch chân + dòng nhãn A B C D bên dưới"""
    chunks, cur = [], None
    for ln in lines:
        t = cl(ln)
        if not t or re.fullmatch(r'(?:[A-D]\s*)+', t):
            continue
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            cur = [m.group(2)]
            chunks.append(cur)
        elif cur is not None:
            cur.append(t)
    out = []
    for k, c in enumerate(chunks, 1):
        s = ' '.join(c)
        segs = re.findall(r'<u>(.*?)</u>', s)
        assert len(segs) == 4, (gid, k, segs)
        letters = iter('ABCD')
        s2 = re.sub(r'<u>(.*?)</u>', lambda m: '<u>%s</u><sup>%s</sup>' % (m.group(1).strip(), next(letters)), s)
        out.append({'id': '%s.%d' % (gid, k), 't': 'mcq', 'q': keepu(s2), 'o': [x.strip() for x in segs]})
    assert len(out) == expect, (gid, len(out))
    return out


def arrow_pairs(gid, lines, expect):
    """câu gốc đánh số + dòng '🡪 ... ……' -> fill nhiều ô"""
    out, cur = [], None
    for ln in lines:
        t = cl(ln)
        if not t:
            continue
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            cur = {'o': m.group(2).strip(), 'a': ''}
            out.append(cur)
        elif t.startswith('🡪') and cur is not None:
            cur['a'] += ' ' + t[1:].strip()
        elif cur is not None and not cur['a']:
            cur['o'] += ' ' + t
    its = []
    for k, c in enumerate(out, 1):
        a = blankify(c['a'])
        if a.endswith('{_}'):
            a += '.'
        its.append({'id': '%s.%d' % (gid, k), 't': 'fill', 'q': '%s<br>🡪 %s' % (keepu(c['o']), a)})
    assert len(its) == expect, (gid, len(its))
    return its


def long_rewrite(gid, lines, expect, label):
    """câu gốc đánh số + dòng gạch trống -> fill long"""
    its = []
    for n, s in numbered([l for l in lines if not re.fullmatch(r'[\s….]+', cl(l) or '.')]):
        its.append({'id': '%s.%d' % (gid, len(its) + 1), 't': 'fill', 'q': '%s<br>%s {_}' % (keepu(s), label), 'long': True})
    assert len(its) == expect, (gid, len(its))
    return its


def passage_blanks(txt, fmt=r'<b>(\1) ______</b>'):
    return re.sub(r'\((\d+)\)\s*_{3,}', fmt, txt)


# ====================================================================== LÝ THUYẾT
def theory():
    raw = open(os.path.join(ROOT, 'src/l10u2/cs.txt'), encoding='utf8').read().split('\n')
    assert raw[0].startswith('⟦<b>UNIT 2') and raw[26].startswith('PRACTISE')
    assert raw[115].startswith('<b>GRAMMAR') and raw[196].startswith('<b>BÀI TẬP')
    assert raw[273].startswith('<b>II. THE PASSIVE') and raw[415].startswith('<b>BÀI TẬP')
    return theory_html(raw[1:26] + raw[115:196] + raw[273:415], '')


# ====================================================================== CÁC TRANG
def build():
    pages = []

    # ---------------------------------------------------------------- 1. Phát âm & trọng âm
    words = 'profit plan glean plough globe plane promotion plumber grimy grey groom play praise pronoun green practice grip glue glide global'.split()
    pa1 = [{'id': 'pa1.%d' % i, 't': 'mcq', 'q': '<b>%s</b>' % w, 'o': ['/pl/', '/pr/', '/gl/', '/gr/'], 'plain': True} for i, w in enumerate(words, 1)]
    assert len(pa1) == 20
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'pa1', 'instr': 'Put these words into the correct column (chọn cụm phụ âm đầu: /pl/, /pr/, /gl/ hay /gr/). Then pronounce the words exactly.', 'items': pa1},
        {'id': 'pa2', 'instr': 'Test 1 – Choose the word that has the underlined part pronounced differently from the others.', 'items': mcq_range('pa2', 415, 419, 5)},
        {'id': 'pa3', 'instr': 'Test 2 – Choose the word whose underlined part is pronounced differently from the rest.', 'items': mcq_range('pa3', 782, 786, 5)},
        {'id': 'pa4', 'instr': 'Test 2 – Choose the word whose stress pattern is different from that of the others.', 'items': mcq_range('pa4', 788, 792, 5)},
    ]})

    # ---------------------------------------------------------------- 2. Từ vựng
    systems = ['circulatory system', 'digestive system', 'respiratory system', 'skeletal system', 'nervous system']
    cls_words = 'blood breath skull bone heart brain lung stomach digestive air pump muscle spine nerve vessel'.split()
    tv1 = [{'id': 'tv1.%d' % i, 't': 'mcq', 'q': '<b>%s</b>' % w, 'o': systems[:], 'plain': True} for i, w in enumerate(cls_words, 1)]
    pics = ['bone', 'lung', 'blood vessel', 'skin', 'stomach', 'brain']
    pic_img = ['image9.jpg', 'image10.jpg', 'image11.jpg', 'image12.png', 'image13.jpg', 'image14.jpg']
    tv2 = [{'id': 'tv2.%d' % i, 't': 'mcq', 'q': '<b>Hình %d</b> – chọn từ đúng' % i, 'img': pic_img[i - 1], 'o': pics[:], 'plain': True} for i in range(1, 7)]
    left = ['Stress', 'Treatment for this type of disease', 'A healthy lifestyle', 'Remember', 'Read the following information', 'Bad breath']
    right = ['can be effective reduced by doing yoga.', 'can prevent many common diseases.', 'can take a long time.',
             'is not just about embarrassment, it may be a sign of other health problems.', 'to learn about what a food allergy is.',
             'to include these five foods in your diet to boost your health.']
    note = '<div class="note"><ol type="a">%s</ol></div>' % ''.join('<li>%s</li>' % x for x in right)
    tv3 = [{'id': 'tv3.%d' % i, 't': 'mcq', 'q': '<b>%s</b> …' % w, 'o': list('abcdef'), 'plain': True} for i, w in enumerate(left, 1)]
    tv5 = fills('tv5', R(462, 467), 6)
    tv5_bank = ['allergy', 'sugary drinks', 'calorie need', 'whole grains', 'harmony', 'treatment', 'food pyramid', 'balance between yin and yang']
    tv7 = fills('tv7', R(489, 494), 6)
    tv7_bank = ['disorder', 'therapy', 'nerve', 'bacterium', 'intestine', 'skull', 'skeleton', 'spine', 'immune system']
    pages.append({'id': 'tu-vung', 'title': 'Từ vựng cơ thể & sức khoẻ (Test 1)', 'mode': 'practice', 'groups': [
        {'id': 'tv1', 'instr': 'II.1 – Decide these words into the correct column (chọn hệ cơ quan phù hợp).', 'items': tv1},
        {'id': 'tv2', 'instr': 'Test 1 – B. VOCABULARY AND GRAMMAR – 1. Choose the right words to the pictures.', 'items': tv2},
        {'id': 'tv3', 'instr': 'II. Match the two columns to make meaningful sentences (chọn chữ cái a–f).', 'passage': note, 'items': tv3},
        {'id': 'tv4', 'instr': 'III. Choose the best options to fill in the blanks.', 'items': mcq_range('tv4', 449, 458, 5)},
        {'id': 'tv5', 'instr': "IV. Complete the following sentences using the given phrases. There are two phrases that you don't need.", 'bank': tv5_bank, 'items': tv5},
        {'id': 'tv6', 'instr': 'V. Choose the best options to fill in the blanks.', 'items': mcq_range('tv6', 469, 478, 5)},
        {'id': 'tv7', 'instr': "VI. Complete the following sentences using the given words/phrases. There are three words/phrases that you don't need.", 'bank': tv7_bank, 'items': tv7},
    ]})

    # ---------------------------------------------------------------- 3. Thì tương lai
    tl1 = fills('tl1', R(146, 155), 10)
    pic_src = [(1, 'image1.jpg', 'My father/ paint the room purple.'), (2, 'image2.jpg', 'My brother/ ride a horse.'),
               (3, 'image3.png', 'I/ learn the English alphabet.'), (4, 'image4.jpg', 'You/ do exercise?'),
               (5, 'image5.jpg', 'They/ get married.'), (6, 'image6.jpg', 'I/ have a big breakfast.'),
               (7, 'image7.jpg', 'We/ have fun at the playground.'), (8, 'image8.gif', 'Mickey/ play computer games.')]
    tl2 = [{'id': 'tl2.%d' % n, 't': 'fill', 'q': 'Từ gợi ý: <i>%s</i><br>Viết câu với “going to”: {_}' % s, 'img': img, 'long': True} for n, img, s in pic_src]
    tl5 = two_choice('tl5', R(507, 512), ['Correct', 'Incorrect'], 6)
    tl4 = mcq_range('tl4', 496, 505, 5)
    for it in tl4:
        it['o'] = ['will', 'are going to', 'Both A & B']
    tl6 = two_choice('tl6', R(516, 525), ['Intention', 'Prediction'], 10)
    tl9_bank = ['put', 'leave', 'pick', 'give', 'give', 'visit', 'get', 'turn']
    pages.append({'id': 'tuong-lai', 'title': 'Thì tương lai: will & be going to', 'mode': 'practice', 'groups': [
        {'id': 'tl1', 'instr': 'I. Put the verbs into the correct form (future simple tense will).', 'passage': '<p>Tim, 16 years old, asked an ugly fortune teller about his future. Here is what she told him:</p>', 'items': tl1},
        {'id': 'tl2', 'instr': 'II. Look at the pictures and complete the sentences with the given words using “going to” future.', 'items': tl2},
        {'id': 'tl3', 'instr': "III. Put the verbs in the brackets into the correct tense (the future simple ‘will’ or ‘going to’ future).", 'items': fills('tl3', R(182, 193), 12, br=False)},
        {'id': 'tl4', 'instr': 'Test 1 – VII. Choose the options that best fit the blanks.', 'items': tl4},
        {'id': 'tl5', 'instr': 'Test 1 – VIII. Decide whether the following sentences are Correct or Incorrect.', 'items': tl5},
        {'id': 'tl6', 'instr': 'Test 1 – IX. Decide whether the following sentences are intention or prediction.', 'items': tl6},
        {'id': 'tl7', 'instr': 'Test 1 – X. Provide the correct verbs in the form of "will" or "be going to" to fill in the blanks.', 'items': fills('tl7', R(527, 537), 8, br=True)},
        {'id': 'tl8', 'instr': 'Test 1 – XI. Provide the correct verbs in the form of "will" or "be going to" to fill in the blanks.', 'items': fills('tl8', R(539, 557), 11, br=True)},
        {'id': 'tl9', 'instr': 'Test 1 – XII. Choose from the given verbs to fill in each blank ("will" or "be going to"): put, leave, pick, give (x2), visit, get, turn.', 'bank': tl9_bank, 'items': fills('tl9', R(559, 566), 8)},
    ]})

    # ---------------------------------------------------------------- 4. Bị động (cơ bản)
    bd1 = two_choice('bd1', R(279, 288), ['active voice', 'passive voice'], 10)
    for it in bd1:
        it['q'] = re.sub(r'\s*\(active voice/ passive voice\)\s*$', '', it['q'])
    bd5 = long_rewrite('bd4', R(317, 332), 8, 'Câu bị động:')
    bd6 = long_rewrite('bd5', R(334, 345), 6, 'Câu chủ động:')
    bd7 = []
    for n, t in numbered(R(347, 361)):
        t = re.sub(r'[….]{3,}', ' ', t)
        t = re.sub(r'[\s/?]+$', '', t.strip())
        bd7.append({'id': 'bd6.%d' % (len(bd7) + 1), 't': 'fill', 'q': 'Các từ/cụm từ: <i>%s</i> (câu hỏi)<br>Sắp xếp thành câu hoàn chỉnh: {_}' % t, 'long': True})
    assert len(bd7) == 8
    pages.append({'id': 'bi-dong', 'title': 'Câu bị động (cơ bản)', 'mode': 'practice', 'groups': [
        {'id': 'bd1', 'instr': 'IV. Decide whether the following sentences belong to the active voice or passive voice.', 'items': bd1},
        {'id': 'bd2', 'instr': 'V. Fill in the blank with the correct form of the passive voice.', 'items': fills('bd2', R(290, 294), 5)},
        {'id': 'bd3', 'instr': 'VI. Change the sentences into the passive voice by filling in the missing words.', 'items': arrow_pairs('bd3', R(296, 315), 10)},
        {'id': 'bd4', 'instr': 'VII. Change the sentences into the passive voice.', 'items': bd5},
        {'id': 'bd5', 'instr': 'VIII. Change the sentences into the active voice.', 'items': bd6},
        {'id': 'bd6', 'instr': 'IX. Reorder the words to make a complete sentence.', 'items': bd7},
    ]})

    # ---------------------------------------------------------------- 5. Bị động – Test 1
    bt1 = fills('bt1', R(568, 574), 7)
    bt2 = two_choice('bt2', R(576, 587), ['Correct', 'Incorrect'], 10)
    # XV: 3 phương án A/B/C, câu không có đề -> q rỗng
    bt3 = mcq_range('bt3', 589, 612, 8)
    for it in bt3:
        it['q'] = ''
    bt4 = fills('bt4', R(614, 623), 10)
    bt5 = []
    for n, s in numbered([l for l in R(625, 638) if not re.fullmatch(r'_+', cl(l) or '.')]):
        s = re.sub(r'\s*_{5,}.*$', '', s)
        bt5.append({'id': 'bt5.%d' % (len(bt5) + 1), 't': 'fill',
                    'q': '%s<br>Từ/cụm từ sai: {_} → sửa thành (ghi “bỏ” nếu từ đó thừa): {_}' % keepu(s)})
    assert len(bt5) == 10
    bt6 = mcq_range('bt6', 640, 651, 6)
    pages.append({'id': 'bi-dong-test1', 'title': 'Câu bị động – Test 1', 'mode': 'practice', 'groups': [
        {'id': 'bt1', 'instr': 'Test 1 – XIII. Give the correct forms in Passive Voice of the verbs. Use the tenses in the brackets.', 'items': bt1},
        {'id': 'bt2', 'instr': 'Test 1 – XIV. Decide whether the following sentences are Correct or Incorrect.', 'items': bt2},
        {'id': 'bt3', 'instr': 'Test 1 – XV. Choose the correct sentence among the given ones.', 'items': bt3},
        {'id': 'bt4', 'instr': 'Test 1 – XVI. Give the correct forms in Passive voice of the verbs given in the brackets.', 'items': bt4},
        {'id': 'bt5', 'instr': 'Test 1 – XVII. Find a wrong/ redundant word in each sentence.', 'items': bt5},
        {'id': 'bt6', 'instr': 'Test 1 – XVIII. Choose the options that best fit the blanks.', 'items': bt6},
    ]})

    # ---------------------------------------------------------------- 6. Tổng hợp nâng cao
    nc3 = long_rewrite('nc3', R(393, 408), 8, 'Câu bị động:')
    st = cl(L[411 - 1])
    nd = []
    for m in re.finditer(r'\((\d+)\.\s*([a-z]+)\)', st):
        nd.append({'id': 'nc4.%d' % int(m.group(1)), 't': 'fill', 'q': '<b>(%s)</b> (%s) {_}' % (m.group(1), m.group(2))})
    assert len(nd) == 12
    st_pass = '<p>%s</p>' % re.sub(r'\((\d+)\.\s*([a-z]+)\)\s*(?:…+\.*|\.{4,}|_{3,})', r'<b>(\1) ______</b> (\2)', st)
    pages.append({'id': 'nang-cao', 'title': 'Tổng hợp nâng cao: tương lai & bị động', 'mode': 'practice', 'groups': [
        {'id': 'nc1', 'instr': 'X. Put the verbs in the brackets into the correct tense.', 'items': fills('nc1', R(365, 374), 10)},
        {'id': 'nc2', 'instr': 'XI. Change the sentences into the passive voice by filling in the missing words.', 'items': arrow_pairs('nc2', R(376, 391), 8)},
        {'id': 'nc3', 'instr': 'XII. Change the sentences into the passive voice.', 'items': nc3},
        {'id': 'nc4', 'instr': 'XIII. Complete the sentences (Active or Passive Voice). You must either use the Simple Present or the Past Simple.',
         'passage': '<p><b>The Statue of Liberty</b></p>' + st_pass, 'items': nd},
    ]})

    # ---------------------------------------------------------------- 7. Đọc – Test 1
    p_r1 = para_html(R(654, 656), keepb=False)
    dr2 = []
    for n, s in numbered(R(674, 678)):
        dr2.append({'id': 'dr2.%d' % len(dr2) + '', 't': 'tfng', 'q': s})
    for k, it in enumerate(dr2, 1):
        it['id'] = 'dr2.%d' % k
    assert len(dr2) == 5
    cloze = para_html(R(689, 693), keepb=False)
    cloze = re.sub(r'\((\d+)\)\s*____', r'<b>(\1) ______</b>', cloze).replace('been(4)', 'been (4)')
    cloze = re.sub(r'(?<!>)\((4)\) ____', r'<b>(\1) ______</b>', cloze)
    dr4 = mcq_range('dr4', 694, 703, 10)
    for i, it in enumerate(dr4, 1):
        it['q'] = 'Blank (%d)' % i
    pages.append({'id': 'doc-test1', 'title': 'Đọc hiểu – Test 1', 'mode': 'practice', 'groups': [
        {'id': 'dr1', 'instr': 'C. READING – I. Read the passage and do the tasks below. Part 1. Choose the best answers to complete the following sentences.', 'passage': p_r1, 'items': mcq_range('dr1', 658, 669, 4)},
        {'id': 'dr2', 'instr': 'Part 2. Decide whether the following statements are True (T), False (F) or Not Given (NG).', 'passage': p_r1, 'items': dr2},
        {'id': 'dr3', 'instr': 'Part 3. Choose A, B or C to answer the following questions. Which person ...?', 'passage': p_r1, 'items': mcq_range('dr3', 680, 687, 4)},
        {'id': 'dr4', 'instr': 'II. Choose the best answer to fill in the blank.', 'passage': cloze, 'items': dr4},
    ]})

    # ---------------------------------------------------------------- 8. Viết – Test 1
    vt1 = mcq_range('vt1', 705, 750, 10)
    vt2 = [{'id': 'vt2.1', 't': 'open', 'q': 'Write and reply to an inquiry letter for health advice.',
            }]
    letter = ('<div class="note"><p><b>Dear Dr. Glenn,</b></p><p>I am coming to an important interview next Friday, but I have no ideas about what to eat before the interview. '
              'Could you give me some suggestions on what foods to eat and avoid?</p><p>I am looking forward to hearing from you.</p><p>Regards,<br>Jack</p></div>')
    vt3 = []
    lines = R(759, 778)
    cur = None
    for ln in lines:
        t = cl(ln)
        if not t:
            continue
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            cur = {'o': m.group(2).strip(), 's': ''}
            vt3.append(cur)
        else:
            cur['s'] += ' ' + t
    assert len(vt3) == 10
    out3 = []
    for i, c in enumerate(vt3, 1):
        stem = c['s'].strip()
        stem = re.sub(r'\s*_{3,}\s*', ' {_} ', stem)
        stem = re.sub(r'\s+([.,])', r'\1', stem).strip()
        assert stem.count('{_}') == 1, stem
        out3.append({'id': 'vt3.%d' % i, 't': 'fill', 'q': '%s<br><b>%s</b>' % (keepu(c['o']), stem), 'long': True})
    vt3 = out3
    pages.append({'id': 'viet-test1', 'title': 'Viết & diễn đạt lại câu – Test 1', 'mode': 'practice', 'groups': [
        {'id': 'vt1', 'instr': 'III (Reading). Choose the sentence which is closest in meaning with the given one.', 'items': vt1},
        {'id': 'vt2', 'instr': 'D. WRITING – I. Write and reply to an inquiry letter for health advice (tự luận – xem thư mẫu).', 'passage': letter, 'items': vt2},
        {'id': 'vt3', 'instr': 'II. Rewrite the following sentences without changing their meaning, using the given words.', 'items': vt3},
    ]})

    # ---------------------------------------------------------------- 9. Từ vựng – ngữ pháp Test 2
    gt1 = mcq_range('gt1', 795, 848, 25)
    for it in gt1:
        it['q'] = it['q'].replace(' Lan:', '<br>Lan:').replace(' Dr.', ' Dr.')
    gt2 = fills('gt2', R(850, 860), 10, br=True)
    wf = cl(L[862 - 1])
    gt3 = []
    for m in re.finditer(r'\((\d+)\.\s*([A-Z]+)\)', wf):
        gt3.append({'id': 'gt3.%s' % m.group(1), 't': 'fill', 'q': '<b>(%s)</b> {_}' % m.group(1), 'hint': m.group(2)})
    assert len(gt3) == 10
    wf_pass = '<p>%s</p>' % re.sub(r'\((\d+)\.\s*([A-Z]+)\)\s*_{3,}', r'<b>(\1) ______</b> (\2)', wf)
    mist = '<p>%s</p>' % cl(L[864 - 1])
    gt4 = [{'id': 'gt4.%d' % i, 't': 'fill', 'q': '<b>Lỗi %d</b> – từ/cụm từ sai: {_} → sửa thành: {_}' % i} for i in range(1, 11)]
    pages.append({'id': 'ngu-phap-test2', 'title': 'Từ vựng – ngữ pháp – Test 2', 'mode': 'practice', 'groups': [
        {'id': 'gt1', 'instr': 'B. LEXICO-GRAMMAR – I. Choose the best answer to complete each of the following sentences.', 'items': gt1},
        {'id': 'gt2', 'instr': 'II. Supply the correct tense or form of the verb in each of the following brackets.', 'items': gt2},
        {'id': 'gt3', 'instr': 'III. Give the correct form of the word in each bracket in the following passage.', 'passage': wf_pass, 'items': gt3},
        {'id': 'gt4', 'instr': 'IV. There are ten mistakes in the following passage. Find and correct them (liệt kê theo thứ tự xuất hiện trong đoạn văn).', 'passage': mist, 'items': gt4},
    ]})

    # ---------------------------------------------------------------- 10. Đọc – Test 2
    c1 = para_html(R(882, 882), keepb=False)
    c1 = passage_blanks(c1)
    dt1 = mcq_range('dt1', 883, 892, 10)
    for i, it in enumerate(dt1, 1):
        it['q'] = 'Blank (%d)' % i
    c2 = para_html(R(894, 896), keepb=False)
    c2 = re.sub(r'\((\d+)\)\s*_+', r'<b>(\1) ______</b>', c2)
    assert len(re.findall(r'\) ______</b>', c2)) == 10
    dt2 = [{'id': 'dt2.%d' % i, 't': 'fill', 'q': '<b>(%d)</b> {_}' % i} for i in range(1, 11)]
    c3 = para_html(R(898, 899), keepb=True)
    dt3 = mcq_range('dt3', 900, 925, 9)
    for it in dt3:
        it['q'] = re.sub(r'(?:"|“)([^"”“]+?)(?:"|”)', lambda m: '“<b>%s</b>”' % m.group(1), it['q']) if 'word' in it['q'] or 'phrase' in it['q'] or 'author mean' in it['q'] else it['q']
    pages.append({'id': 'doc-test2', 'title': 'Đọc hiểu – Test 2', 'mode': 'practice', 'groups': [
        {'id': 'dt1', 'instr': 'C. READING – 1. Read the passage and choose the best option for each of the following blanks. (SPECTACULAR SPORTS)', 'passage': c1, 'items': dt1},
        {'id': 'dt2', 'instr': 'II. Read the text below and fill in each blank with ONE suitable word.', 'passage': c2, 'items': dt2},
        {'id': 'dt3', 'instr': 'III. Read the following passage and choose the option that indicates the correct answer to each of the following questions.', 'passage': c3, 'items': dt3},
    ]})

    # ---------------------------------------------------------------- 11. Viết – Test 2
    stems = ['Nobody {_}.', 'It came {_}.', 'If it {_}.', 'Our hotel booking {_}.', "Her uncle didn't {_}.", 'Betty is devoted {_}.',
             'Not only {_}.', None, 'They stole {_}.', 'All dogs {_}.']
    src1 = [s for n, s in numbered(R(928, 937))]
    assert len(src1) == 10
    vw1 = []
    for i, (s, st_) in enumerate(zip(src1, stems), 1):
        if st_ is None:
            vw1.append({'id': 'vw1.%d' % i, 't': 'open', 'q': keepu(s) + '<br>(Viết lại câu bắt đầu bằng <i>He denied …</i> hoặc dùng cụm <i>having witnessed the crime</i> – xem đáp án mẫu)'})
        else:
            vw1.append({'id': 'vw1.%d' % i, 't': 'fill', 'q': '%s<br><b>%s</b>' % (keepu(s), st_), 'long': True})
    w2 = []
    cur = None
    for ln in R(939, 958):
        t = cl(ln)
        if not t or re.fullmatch(r'_+', t):
            continue
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            w2.append(m.group(2).strip())
    assert len(w2) == 10
    vw2 = []
    for i, s in enumerate(w2, 1):
        m = re.match(r'^(.*)\(([a-z]+)\)\s*$', s)
        vw2.append({'id': 'vw2.%d' % i, 't': 'fill', 'q': '%s<br>Từ cho sẵn: <b>%s</b> (không đổi dạng)<br>Câu mới: {_}' % (keepu(m.group(1)), m.group(2)), 'long': True})
    pages.append({'id': 'viet-test2', 'title': 'Viết – Test 2', 'mode': 'practice', 'groups': [
        {'id': 'vw1', 'instr': 'D. WRITING – I. Finish the second sentence in such a way that it means exactly the same as the sentence printed before it.', 'items': vw1},
        {'id': 'vw2', 'instr': 'II. Write a new sentence similar in meaning to the given one, using the word given in the brackets. Do not alter the word in any way.', 'items': vw2},
    ]})

    # ---------------------------------------------------------------- 12. Kiểm tra (Test 3 – 140 câu)
    kt = []

    def add(gid, instr, a, b, expect, passage='', kind='mcq', bold_quote=False):
        if kind == 'err':
            its = err_items('tmp', R(a, b), expect)
        else:
            its = mcq_range('tmp', a, b, expect, shift_numbers=True)
        assert len(its) == expect, (gid, len(its), expect)
        base = sum(len(g['items']) for g in kt)
        for j, it in enumerate(its, 1):
            it['id'] = 'kt.%d' % (base + j)
            if bold_quote:
                it['q'] = re.sub(r'(?:"|“)([^"”“]+?)(?:"|”)', lambda m: '“<b>%s</b>”' % m.group(1), it['q'])
        g = {'id': gid, 'instr': instr, 'items': its}
        if passage:
            g['passage'] = passage
        kt.append(g)

    add('kt1', 'Exercise 1. Mark the letter A, B, C, or D to indicate the word whose underlined part differs from the other three in pronunciation in each of the following questions.', 962, 966, 5)
    add('kt2', 'Exercise 2. Mark the letter A, B, C, or D to indicate the word that differs from the other three in the position of the primary stress in each of the following questions.', 968, 972, 5)
    add('kt3', 'Exercise 3. Mark the letter A, B, C, or D to indicate the correct answer to each of the following questions.', 975, 1010, 18)
    add('kt4', 'Exercise 4. Mark the letter A, B, C or D to indicate the word(s) CLOSEST in meaning to the underlined word(s) in each of the following questions.', 1012, 1039, 14)
    add('kt5', 'Exercise 5. Mark the letter A, B, C, or D to indicate the word(s) OPPOSITE in meaning to the underlined word(s) in each of the following questions.', 1041, 1056, 8)
    add('kt6', 'Exercise 6. Mark the letter A, B, C, or D to indicate the correct answer to each of the following questions.', 1059, 1112, 26)
    add('kt7', 'Exercise 7. Mark the letter A, B, C, or D to indicate the underlined part that needs correction in each of the following questions.', 1114, 1152, 14, kind='err')
    add('kt8', 'Exercise 8. Mark the letter A, B, C, or D to indicate the correct response to each of the following exchanges.', 1155, 1199, 15)
    ex9 = para_html(R(1203, 1205), keepb=False)
    ex9 = passage_blanks(ex9)
    add('kt9', 'Exercise 9. Read the following passage and mark the letter A, B, C, or D to indicate the correct word or phrase that best fits each of the numbered blanks. (GOOD HEALTH)', 1206, 1217, 12, passage=ex9)
    ex10 = para_html(R(1219, 1221), keepb=True)
    add('kt10', 'Exercise 10. Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each of the questions.', 1222, 1238, 5, passage=ex10, bold_quote=True)
    ex11 = para_html(R(1240, 1242), keepb=True)
    add('kt11', 'Exercise 11. Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each of the questions.', 1243, 1268, 8, passage=ex11, bold_quote=True)
    add('kt12', 'Exercise 12. Mark the letter A, B, C, or D to indicate the sentence that is closest in meaning to each of the following questions.', 1271, 1294, 6)
    add('kt13', 'Exercise 13. Mark the letter A, B, C, or D to indicate the sentence that best combines each pair of sentences in the following questions.', 1296, 1315, 4)
    n = sum(len(g['items']) for g in kt)
    assert n == 140, n
    for it in kt[7]['items']:
        it['q'] = re.sub(r'\s+(Patient|Doctor|Claire):', r'<br>\1:', it['q'])
    for it in kt[8]['items']:
        it['q'] = 'Blank (%d)' % (int(it['id'].split('.')[1]))
    pages.append({'id': 'kiem-tra', 'title': 'Bài kiểm tra Test 3 (140 câu)', 'mode': 'test', 'minutes': 120, 'groups': kt})

    return {'id': 'lop10-u2-chuyensau', 'title': 'Unit 2 – Humans and the environment: Bài tập chuyên sâu', 'grade': 10, 'unit': 2, 'theory': theory(), 'pages': pages}


def dump(path, name, data):
    s = '# -*- coding: utf-8 -*-\n"""Dữ liệu nội dung %s (sinh từ file Word bằng tools/gen_l10u2_chuyensau.py rồi có thể chỉnh tay).\nĐáp án + giải thích: xem file *_dapan.py cùng tên."""\n\n%s = ' % (name, name)
    s += pprint.pformat(data, width=150, sort_dicts=False) + '\n'
    open(path, 'w', encoding='utf8').write(s)


if __name__ == '__main__':
    k = build()
    dump(os.path.join(ROOT, 'units/lop10_u2_chuyensau.py'), 'SET', k)
    dst = os.path.join(ROOT, 'assets/lop10_u2/chuyensau')
    os.makedirs(dst, exist_ok=True)
    DOCX = glob.glob('/mnt/user-data/uploads/04. GRADE 1-12/GRADE 10/3. BÀI TẬP CHUYÊN SÂU/*Unit-2-HUMANS*.docx')
    if DOCX:      # ảnh image1..image14 của phần đề (image15-17 chỉ là bản lặp trong phần khoá)
        names = 'image1.jpg image2.jpg image3.png image4.jpg image5.jpg image6.jpg image7.jpg image8.gif image9.jpg image10.jpg image11.jpg image12.png image13.jpg image14.jpg'.split()
        with zipfile.ZipFile(DOCX[0]) as z:
            for nm in names:
                with z.open('word/media/' + nm) as f, open(os.path.join(dst, nm), 'wb') as o:
                    o.write(f.read())
    tot = 0
    for p in k['pages']:
        c = sum(len(g['items']) for g in p['groups']); tot += c
        print(p['id'], c, [(g['id'], len(g['items'])) for g in p['groups']])
    print('TOTAL', tot)
