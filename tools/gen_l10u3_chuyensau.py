"""Chuyển đổi 1 lần: Word 'Bài tập chuyên sâu' Lớp 10 Unit 3 (Music) -> units/lop10_u3_chuyensau.py (khung câu hỏi).
Đáp án + giải thích soạn tay ở units/lop10_u3_chuyensau_dapan.py (đối chiếu khoá trong nửa sau của src/l10u3/cs_c.txt rồi tự giải).
Nguồn src/l10u3/cs_c.txt: nửa đầu (đến dòng 'ĐÁP ÁN') = đề không khoá; nửa sau = bản đề có khoá tô màu (không dùng để sinh đề).
Gồm: lý thuyết (từ vựng + to-V/V + câu ghép), bài tập vận dụng 1-14, Test 1, Test 2, Test 3 (140 câu, trang kiểm tra).
File Word không có ảnh."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import parse_mcq, cl
from theory import theory_html
import pprint

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = open(os.path.join(ROOT, 'src/l10u3/cs_c.txt'), encoding='utf8').read()

# ---- sửa lỗi nguồn (chuỗi -> chuỗi)
FIX = [
    ('GRAMMARR', 'GRAMMAR'),
    ('test.They didn', 'test. They didn'),
    ('10.The boss', '10. The boss'),
    ('hard.D. I couldn', 'hard. D. I couldn'),
    ('home.They', 'home. They'),
    ('( not/tell)', '(not/tell)'),
    ('“devoted"', '“devoted”'),
    ('“outstanding"', '“outstanding”'),
    ("run out of paper.’", "run out of paper.”"),
    ("We didn't have managed without my father's money.", "We wouldn't have managed without my father's money."),
    ('mother.D. My mother had just', 'mother. D. My mother had just'),
    ('C . I was busy enough', 'C. I was busy enough'),
    ('I960', '1960'),
    ('Iivc-performed', 'live-performed'),
    ('D. a eompany', 'D. a company'),
    ('new eomputer programme', 'new computer programme'),
    ('a new eroup from England', 'a new group from England'),
    ('this projeet is mine', 'this project is mine'),
    ('very mueh', 'very much'),
    ('modernnisation', 'modernisation'),
    ('Take yourself at home', 'Make yourself at home'),
    ('W hen looking Anna playing piano', 'When watching Anna play the piano'),
    ('(113 )', '(113)'),
    ('new while R&B music', 'new white R&B music'),
    ('particularly in American,', 'particularly in America,'),
    ('The world first film', "The world's first film"),
    ('Contestants must be at least rs old.', 'Contestants must be at least 18 years old.'),
    ('In recent year,', 'In recent years,'),
    ('record other their songs', 'record their songs'),
    ('Mark the letter A. B, C, or D', 'Mark the letter A, B, C, or D'),
    ('Mark the letter A, B. C, or D', 'Mark the letter A, B, C, or D'),
    ('Exercise 12.  Mark', 'Exercise 12. Mark'),
    ('Wolfgang Amadeus Mozart’s was the only-surviving son', 'Wolfgang Amadeus Mozart was the only surviving son'),
    ('Moby Dick', 'Moby Dick'),
]
for a, b in FIX:
    RAW = RAW.replace(a, b)
RAW = re.sub(r'“(<b>[^<]*</b>)"', r'“\1”', RAW)
RAW = re.sub(r'(?m)^_{3,}(?=\d+\.)', '', RAW)          # '____6. That man' -> '6. That man'
L = RAW.split('\n')
L = L[:next(i for i, l in enumerate(L) if 'ĐÁP ÁN' in l)]       # nửa đầu: đề không khoá


def find(pat, frm=0):
    for i in range(frm, len(L)):
        if re.search(pat, re.sub(r'</?[bu]>', '', cl(L[i])).strip()):
            return i
    raise KeyError(pat)


def between(p1, p2, frm=0):
    a = find(p1, frm)
    b = find(p2, a + 1)
    return L[a + 1:b], b


def keepu(s):
    s = re.sub(r'<u>(\s*)</u>', r'\1', s)
    s = re.sub(r'</u>(\s*)<u>', r'\1', s)
    s = re.sub(r'_{3,}', '______', s)
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


def isdots(t):
    return re.fullmatch(r'[\s.…_]*', t) is not None


def numbered(lines):
    """[(n, text)] gộp dòng tiếp theo vào câu trước (bỏ dòng chấm/gạch)"""
    out = []
    for ln in lines:
        t = cl(ln)
        if not t or isdots(t):
            continue
        m = re.match(r'^(\d+)\s*\.\s*(.*)$', t)
        if m:
            out.append([int(m.group(1)), m.group(2).strip()])
        elif out:
            out[-1][1] += ' ' + t
    return [(n, s) for n, s in out]


def fills(gid, lines, expect=None, long=False):
    out = []
    for n, s in numbered(lines):
        q = blankify(s)
        if q.endswith('{_}'):
            q += '.'
        it = {'id': '%s.%d' % (gid, len(out) + 1), 't': 'fill', 'q': q}
        if long:
            it['long'] = True
        out.append(it)
    if expect:
        assert len(out) == expect, (gid, len(out), expect)
    return out


def choose_bracket(gid, lines, expect):
    out = []
    for n, s in numbered(lines):
        m = re.search(r'\(([^()]*/[^()]*)\)', s)
        opts = [x.strip() for x in m.group(1).split('/')]
        q = (s[:m.start()] + '______' + s[m.end():]).strip()
        out.append({'id': '%s.%d' % (gid, len(out) + 1), 't': 'mcq', 'q': keepu(q), 'o': opts, 'plain': True})
    assert len(out) == expect, (gid, len(out))
    return out


def para_html(lines):
    out = []
    for l in lines:
        t = keepu(cl(l))
        if t:
            out.append('<p>%s</p>' % t)
    return ''.join(out)


def err_items(gid, lines, expect):
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


def mcq_lines(gid, lines, expect):
    ev = parse_mcq(lines, expect=1)
    its = items_of(ev)
    assert len(its) == expect, (gid, len(its), expect)
    for it in its:
        assert len(it['o']) >= 2, (gid, it)
    return mk_mcq(gid, its)


def ci_items(gid, lines, expect, opts=('Correct', 'Incorrect')):
    out = [{'id': '%s.%d' % (gid, len(r) + 0), 't': 'mcq'} for r in []]
    out = []
    for n, s in numbered(lines):
        out.append({'id': '%s.%d' % (gid, len(out) + 1), 't': 'mcq', 'q': keepu(s), 'o': list(opts), 'plain': True})
    assert len(out) == expect, (gid, len(out))
    return out


def blank_label(items):
    for i, it in enumerate(items, 1):
        it['q'] = 'Blank (%d)' % i
    return items


# ====================================================================== LÝ THUYẾT
def theory():
    raw = open(os.path.join(ROOT, 'src/l10u3/cs.txt'), encoding='utf8').read().replace('⟦', '').replace('⟧', '').split('\n')
    s1 = next(i for i, l in enumerate(raw) if 'BÀI TẬP VẬN DỤNG CƠ BẢN' in l)
    c1 = next(i for i, l in enumerate(raw) if 'II. COMPOUND SENTENCES' in l)
    c2 = next(i for i in range(c1, len(raw)) if 'BÀI TẬP VẬN DỤNG' in raw[i])
    lines = raw[:s1] + raw[c1:c2]
    html = theory_html(lines, '')
    for a, b in [('Vela', 'V-inf'), ('Conjuntions', 'Conjunctions'), ('I + think/ thought', 'S + think/ thought'),
                 ('S + V + 0 + to + V-inf', 'S + V + O + to + V-inf'), ('<p><b>B. GRAMMAR</b></p>', ''), ('GRAMMARR', 'GRAMMAR'), ('thê giới', 'thế giới'),
                 ('Is there anything to eat? (Có gì để ăn ko?)', 'Is there anything to eat? (Có gì để ăn không?)')]:
        html = html.replace(a, b)
    return html


# ====================================================================== CÁC TRANG
def build():
    pages = []

    # ============================== TRANG 1: to-V / V nguyên mẫu (cơ bản)
    b1, _ = between(r'^Bài 1:', r'^Bài 2:')
    b2, _ = between(r'^Bài 2:', r'^Bài 3:')
    b2 = b2[next(i for i, l in enumerate(b2) if re.match(r'^1\.', cl(l))):]
    b3, _ = between(r'^Bài 3:', r'^Bài 4:')
    left = [cl(l) for l in b3 if re.match(r'^\d\.', cl(l))]
    right = [cl(l) for l in b3 if re.match(r'^[a-f]\.', cl(l))]
    assert len(left) == 6 and len(right) == 6
    b3_items = [{'id': 'v3.%d' % i, 't': 'mcq', 'q': '<b>%s</b> …' % re.sub(r'^\d\.\s*', '', s), 'o': list('abcdef'), 'plain': True} for i, s in enumerate(left, 1)]
    b3_note = '<div class="note"><ol type="a">%s</ol></div>' % ''.join('<li>%s</li>' % re.sub(r'^[a-f]\.\s*', '', s) for s in right)
    b4, _ = between(r'^Bài 4:', r'^Bài 5:')
    b5, _ = between(r'^Bài 5:', r'^Bài 6:')
    b6, _ = between(r'^Bài 6:', r'^Bài 7:')
    v6 = []
    for n, s in numbered(b6):
        v6.append({'id': 'v6.%d' % n, 't': 'fill', 'q': 'Sắp xếp các từ/cụm từ thành câu hoàn chỉnh: <i>%s</i><br>{_}' % keepu(s), 'long': True})
    assert len(v6) == 5
    b7, _ = between(r'^Bài 7:', r'^II\. COMPOUND')
    b7txt = ' '.join(cl(l) for l in b7 if cl(l))
    bank7 = ['wake up', 'seems', 'try', 'excited', 'home', 'in the middle']
    m7 = re.search(r'My daily life.*', b7txt)
    p7 = re.sub(r'(\d)\s*_{3,}', r'<b>(\1) ______</b> ', m7.group(0))
    p7 = re.sub(r'\s+', ' ', p7).replace(' ______</b>  ', ' ______</b> ')
    v7 = [{'id': 'v7.%d' % i, 't': 'fill', 'q': '<b>(%d)</b> {_}' % i} for i in range(1, 7)]
    assert len(re.findall(r'<b>\(\d\) ______</b>', p7)) == 6, p7
    pages.append({'id': 'v-inf', 'title': 'To-V và V nguyên mẫu (cơ bản)', 'mode': 'practice', 'groups': [
        {'id': 'v1', 'instr': 'Bài 1: Put the verbs into the correct form (infinitive with or without to).', 'items': fills('v1', b1, 10)},
        {'id': 'v2', 'instr': 'Bài 2: Rewrite the following sentences using an infinitive. (Ví dụ: It is no use trying to convince her of this. → It is no use for us to try to convince her of this.)',
         'items': [{'id': 'v2.%d' % n, 't': 'fill', 'q': keepu(s) + '<br>Viết lại: {_}', 'long': True} for n, s in numbered(b2)]},
        {'id': 'v3', 'instr': 'Bài 3: Match the words in the column A with the words in the column B to make a meaningful sentence (chọn chữ cái a–f).', 'passage': b3_note, 'items': b3_items},
        {'id': 'v4', 'instr': 'Bài 4: Put the verbs into the correct form.', 'items': fills('v4', b4, 15)},
        {'id': 'v5', 'instr': 'Bài 5: Choose the correct answer in the bracket.', 'items': choose_bracket('v5', b5, 6)},
        {'id': 'v6', 'instr': 'Bài 6: Rearrange the jumbled words to make sentences.', 'items': v6},
        {'id': 'v7', 'instr': 'Bài 7: Complete the passage with words from the box.', 'bank': bank7, 'passage': '<p>%s</p>' % p7, 'items': v7},
    ]})
    assert len(pages[0]['groups'][1]['items']) == 5

    # ============================== TRANG 2: câu ghép
    c8, _ = between(r'^Bài 8:', r'^Bài 9:')
    c9, _ = between(r'^Bài 9:', r'^Bài 10:')
    c10, _ = between(r'^Bài 10:', r'^BÀI TẬP TỔNG HỢP')
    ten = []
    for ln in c10:
        t = cl(ln)
        if not t or isdots(t):
            continue
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            ten.append({'n': int(m.group(1)), 's': m.group(2), 'p': ''})
        elif t.startswith('-'):
            ten[-1]['p'] = t.lstrip('- ').strip()
        else:
            ten[-1]['s'] += ' ' + t
    assert len(ten) == 10
    c10_items = [{'id': 'c10.%d' % i, 't': 'fill', 'q': '%s<br><i>Yêu cầu: %s</i><br>Viết thành một câu ghép: {_}' % (keepu(d['s']), d['p']), 'long': True} for i, d in enumerate(ten, 1)]
    pages.append({'id': 'cau-ghep', 'title': 'Câu ghép (cơ bản)', 'mode': 'practice', 'groups': [
        {'id': 'c8', 'instr': 'Bài 8: Decide if each sentence is a simple sentence or a compound sentence.', 'items': ci_items('c8', c8, 5, ('Simple sentence', 'Compound sentence'))},
        {'id': 'c9', 'instr': 'Bài 9: Choose the best answer to complete the sentence.', 'items': choose_bracket('c9', c9, 5)},
        {'id': 'c10', 'instr': 'Bài 10: Use FANBOYS (for, and, nor, but, or, yet, so) to write one compound sentence using the two simple sentences.', 'items': c10_items},
    ]})

    # ============================== TRANG 3: tổng hợp nâng cao
    n11, _ = between(r'^Bài 11:', r'^Bài 12:')
    n12, _ = between(r'^Bài 12:', r'^Bài 13:')
    n13, _ = between(r'^Bài 13:', r'^Bài 14:')
    n14, _ = between(r'^Bài 14:', r'^TEST 1')
    n14_items = []
    for n, s in numbered(n14):
        n14_items.append({'id': 'n14.%d' % n, 't': 'fill', 'q': keepu(s) + '<br>Viết thành một câu ghép: {_}', 'long': True})
    assert len(n14_items) == 5
    pages.append({'id': 'nang-cao', 'title': 'Tổng hợp nâng cao', 'mode': 'practice', 'groups': [
        {'id': 'n11', 'instr': 'Bài 11: Choose the correct answer in the bracket.', 'items': choose_bracket('n11', n11, 10)},
        {'id': 'n12', 'instr': 'Bài 12: Choose the best answer to complete the sentence.', 'items': mcq_lines('n12', n12, 10)},
        {'id': 'n13', 'instr': 'Bài 13: Put the verbs into the correct form.', 'items': fills('n13', n13, 10)},
        {'id': 'n14', 'instr': 'Bài 14: Use FANBOYS (for, and, nor, but, or, yet, so) to write one compound sentence using the two simple sentences.', 'items': n14_items},
    ]})

    # ============================== TEST 1
    t1 = find(r'^TEST 1')
    t2 = find(r'^TEST 2', t1)
    t3 = find(r'^TEST 3', t2)
    # ---- phát âm Test 1 + Test 2
    a1, _ = between(r'^I\. Choose the word that has the underlined', r'^II\. Choose the word that has the underlined', t1)
    a2, _ = between(r'^II\. Choose the word that has the underlined', r'^B\. VOCABULARY AND GRAMMAR', t1)
    p1 = mcq_lines('p1', a1, 6)
    p2 = mcq_lines('p2', a2, 6)
    q1, _ = between(r'^I\. Choose the word whose underlined', r'^II\. Choose the word whose main stress', t2)
    q2, _ = between(r'^II\. Choose the word whose main stress', r'^B\. GRAMMAR AND VOCABULARY', t2)
    p3 = mcq_lines('p3', q1, 5)
    p4 = mcq_lines('p4', q2, 5)
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'p1', 'instr': 'Test 1 – I. Choose the word that has the underlined part pronounced differently from the others.', 'items': p1},
        {'id': 'p2', 'instr': 'Test 1 – II. Choose the word that has the underlined part pronounced differently from the others.', 'items': p2},
        {'id': 'p3', 'instr': 'Test 2 – I. Choose the word whose underlined part is pronounced differently from that of the others.', 'items': p3},
        {'id': 'p4', 'instr': 'Test 2 – II. Choose the word whose main stress pattern is not the same as that of the others.', 'items': p4},
    ]})

    # ---- từ vựng Test 1
    s_bi, _ = between(r'^I\. Choose the best options to fill', r'^II\. Choose the right words', t1)
    s_bii, _ = between(r'^II\. Choose the right words', r'^III\. Match the words', t1)
    s_biii, _ = between(r'^III\. Match the words', r'^IV\. Choose the words', t1)
    s_biv, _ = between(r'^IV\. Choose the words', r'^V\. Choose the options that best fit', t1)
    s_bv, _ = between(r'^V\. Choose the options that best fit', r'^VI\. Choose the options', t1)
    s_bvi, _ = between(r'^VI\. Choose the options that best fit', r'^VII\. Decide whether', t1)
    bank2 = ['inspirational', 'celebrity panel', 'conquer', 'audition', 'patriotism', 'demanding']
    tv2 = fills('tv2', [l for l in s_bii if re.match(r'^\d+\.', cl(l))], 6)
    left = [re.sub(r'^\d\.\s*', '', cl(l)) for l in s_biii if re.match(r'^\d\.', cl(l))]
    right = [re.sub(r'^[a-d]\.\s*', '', cl(l)) for l in s_biii if re.match(r'^[a-d]\.', cl(l))]
    assert len(left) == 4 and len(right) == 4
    tv3 = [{'id': 'tv3.%d' % i, 't': 'mcq', 'q': '<b>%s</b> …' % w, 'o': list('abcd'), 'plain': True} for i, w in enumerate(left, 1)]
    tv3_note = '<div class="note"><ol type="a">%s</ol></div>' % ''.join('<li>%s</li>' % w for w in right)
    pages.append({'id': 'tu-vung', 'title': 'Từ vựng âm nhạc (Test 1)', 'mode': 'practice', 'groups': [
        {'id': 'tv1', 'instr': 'Test 1 – B. I. Choose the best options to fill in the blanks.', 'items': mcq_lines('tv1', s_bi, 10)},
        {'id': 'tv2', 'instr': 'II. Choose the right words to complete the sentences.', 'bank': bank2, 'items': tv2},
        {'id': 'tv3', 'instr': 'III. Match the words with the corresponding definitions (chọn chữ cái a–d).', 'passage': tv3_note, 'items': tv3},
        {'id': 'tv4', 'instr': 'IV. Choose the words/ phrases that are SAME in meaning to the underlined parts.', 'items': mcq_lines('tv4', s_biv, 6)},
        {'id': 'tv5', 'instr': 'V. Choose the options that best fit the blanks.', 'items': mcq_lines('tv5', s_bv, 8)},
        {'id': 'tv6', 'instr': 'VI. Choose the options that best fit the blanks.', 'items': mcq_lines('tv6', s_bvi, 8)},
    ]})

    # ---- ngữ pháp 1 (câu ghép) Test 1: VII - X
    g7, _ = between(r'^VII\. Decide whether', r'^VIII\. Fill in the blanks', t1)
    g8, _ = between(r'^VIII\. Fill in the blanks', r'^IX\. Choose the best compound', t1)
    g9, _ = between(r'^IX\. Choose the best compound', r'^X\. Determine ONE', t1)
    g10, _ = between(r'^X\. Determine ONE', r'^XI\. Choose the options', t1)
    g10_items = []
    for n, s in numbered(g10):
        g10_items.append({'id': 'g10.%d' % len(g10_items + [0]), 't': 'fill', 'q': keepu(s) + '<br>Từ/cụm từ sai hoặc thừa: {_}'})
    assert len(g10_items) == 8
    pages.append({'id': 'ngu-phap-1', 'title': 'Câu ghép – Test 1', 'mode': 'practice', 'groups': [
        {'id': 'g7', 'instr': 'VII. Decide whether the following sentences are Correct or Incorrect.', 'items': ci_items('g7', g7, 8)},
        {'id': 'g8', 'instr': 'VIII. Fill in the blanks with coordinating conjunctions.', 'items': fills('g8', g8, 8)},
        {'id': 'g9', 'instr': 'IX. Choose the best compound sentence for each sentence pair.', 'items': mcq_lines('g9', g9, 8)},
        {'id': 'g10', 'instr': 'X. Determine ONE wrong/ redundant word in each sentence.', 'items': g10_items},
    ]})

    # ---- ngữ pháp 2 (to-V / V) Test 1: XI - XV
    g11, _ = between(r'^XI\. Choose the options', r'^XII\. Give the correct forms', t1)
    g12, _ = between(r'^XII\. Give the correct forms', r'^XIII\. Use to-infinitives', t1)
    g13, _ = between(r'^XIII\. Use to-infinitives', r'^XIV\. Determine whether', t1)
    g14, _ = between(r'^XIV\. Determine whether', r'^XV\. Complete the sentences', t1)
    g15, _ = between(r'^XV\. Complete the sentences', r'^C\. READING', t1)
    farm = ' '.join(cl(l) for l in g12 if cl(l))
    g12_items = [{'id': 'g12.%d' % int(m.group(1)), 't': 'fill', 'q': '<b>(%s)</b> (%s) {_}' % (m.group(1), m.group(2).strip())} for m in re.finditer(r'\((\d+)\.\s*([a-z]+)\)', farm)]
    assert len(g12_items) == 10
    farm_p = re.sub(r'\((\d+)\.\s*([a-z]+)\)\s*_+', r'<b>(\1) ______</b> (\2)', farm)
    g13_items = fills('g13', g13, 8)
    bank15 = ['leave', 'change', 'know', 'come', 'reveal', 'finish', 'feed', 'share', 'refuse', 'return']
    pages.append({'id': 'ngu-phap-2', 'title': 'To-V và V nguyên mẫu – Test 1', 'mode': 'practice', 'groups': [
        {'id': 'g11', 'instr': 'XI. Choose the options that best fit the blanks.', 'items': mcq_lines('g11', g11, 10)},
        {'id': 'g12', 'instr': 'XII. Give the correct forms of the verbs.', 'passage': '<p>%s</p>' % farm_p, 'items': g12_items},
        {'id': 'g13', 'instr': 'XIII. Use to-infinitives or bare infinitives to complete the following sentences.', 'items': g13_items},
        {'id': 'g14', 'instr': 'XIV. Determine whether the following sentences are Correct or Incorrect.', 'items': ci_items('g14', g14, 10)},
        {'id': 'g15', 'instr': 'XV. Complete the sentences with the correct forms of the verbs in the box.', 'bank': bank15, 'items': fills('g15', g15, 10)},
    ]})

    # ---- Đọc Test 1
    rd = find(r'^C\. READING', t1)
    r_a = find(r'^I\. Read the passage and do the tasks', rd)
    r_p1 = find(r'^Part 1\.', r_a)
    r_p2 = find(r'^Part 2\.', r_p1)
    r_II = find(r'^II\. Choose the best answer to fill', r_p2)
    r_III = find(r'^III\. Choose the sentence which is closest', r_II)
    r_D = find(r'^D\. WRITING', r_III)
    voice = para_html(L[r_a + 1:r_p1])
    rp1 = mcq_lines('r1', L[r_p1 + 1:r_p2], 7)
    rp2 = mcq_lines('r2', L[r_p2 + 1:r_II], 5)
    pop = [l for l in L[r_II + 1:r_III] if cl(l)]
    pop_title = cl(pop[0])
    pop_par = keepu(cl(pop[1]))
    pop_par = re.sub(r'\((\d+)\)\s*_{3,}', r'<b>(\1) ______</b>', pop_par)
    assert len(re.findall(r'______</b>', pop_par)) == 10
    pop_items = blank_label(mcq_lines('r3', pop[2:], 10))
    r4 = mcq_lines('r4', L[r_III + 1:r_D], 15)
    pages.append({'id': 'doc-test1', 'title': 'Đọc hiểu – Test 1', 'mode': 'practice', 'groups': [
        {'id': 'r1', 'instr': 'I. Read the passage and do the tasks below. Part 1. Choose the appropriate meaning for each word from the text.', 'passage': voice, 'items': rp1},
        {'id': 'r2', 'instr': 'Part 2. Choose the best answers to the following questions.', 'passage': voice, 'items': rp2},
        {'id': 'r3', 'instr': 'II. Choose the best answer to fill in the blank.', 'passage': '<p><b>%s</b></p><p>%s</p>' % (pop_title, pop_par), 'items': pop_items},
        {'id': 'r4', 'instr': 'III. Choose the sentence which is closest in meaning with the given one.', 'items': r4},
    ]})

    # ---- Viết Test 1
    w_I = find(r'^I\. Write a brief biography', r_D)
    w_II = find(r'^II\. Rewrite the following sentences', w_I)
    w1 = [{'id': 'w1.1', 't': 'open', 'q': 'Write a brief biography about a famous artist (khoảng 100–120 từ).'}]
    rows = []
    for ln in L[w_II + 1:t2]:
        t = cl(ln)
        if not t:
            continue
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            rows.append({'s': m.group(2), 'p': ''})
        elif rows and not rows[-1]['p']:
            rows[-1]['p'] = re.sub(r'\s*_{3,}\s*$', '', t)
    assert len(rows) == 10, len(rows)
    w2 = [{'id': 'w2.%d' % i, 't': 'fill', 'q': '%s<br><b>%s</b> {_}' % (keepu(d['s']), keepu(d['p'])), 'long': True} for i, d in enumerate(rows, 1)]
    pages.append({'id': 'viet-test1', 'title': 'Viết – Test 1', 'mode': 'practice', 'groups': [
        {'id': 'w1', 'instr': 'D. WRITING – I. Write a brief biography about a famous artist (tự luận – xem bài mẫu).', 'items': w1},
        {'id': 'w2', 'instr': 'II. Rewrite the following sentences without changing their meaning, using the given words.', 'items': w2},
    ]})

    # ============================== TEST 2
    b2_I, _ = between(r'^I\. Choose the most suitable word', r'^II\. Error identification', t2)
    b2_II, _ = between(r'^II\. Error identification', r'^C\. READING', t2)
    u1 = mcq_lines('u1', b2_I, 20)
    # câu 20: dòng đề bị đảo thứ tự (A, C, D, B) -> sắp lại
    o = u1[19]['o']
    assert len(o) == 4
    u1[19]['o'] = [o[0], o[3], o[1], o[2]]
    u1[6]['q'] = u1[6]['q'].replace('Anna:', '<br>Anna:')
    u2 = err_items('u2', b2_II, 5)
    pages.append({'id': 'ngu-phap-test2', 'title': 'Ngữ pháp & từ vựng – Test 2', 'mode': 'practice', 'groups': [
        {'id': 'u1', 'instr': 'B. GRAMMAR AND VOCABULARY – I. Choose the most suitable word or phrase A, B, C or D to complete each sentence.', 'items': u1},
        {'id': 'u2', 'instr': 'II. Error identification (chọn phần gạch chân sai).', 'items': u2},
    ]})

    # ---- đọc Test 2
    rc = find(r'^C\. READING', t2)
    rc_I = find(r'^I\. Read the text below', rc)
    rc_II = find(r'^II\. Read the passage and choose', rc_I)
    rc_D = find(r'^D\. WRITING', rc_II)
    hist_lines = [l for l in L[rc_I + 2:rc_II]]
    first_item = next(i for i, l in enumerate(hist_lines) if re.match(r'^1\.\s*A\.', cl(l)))
    hist_text = ' '.join(cl(l) for l in hist_lines[:first_item] if cl(l))
    hist_text = re.sub(r'____\s*\((\d+)\)', r'<b>(\1) ______</b>', hist_text)
    assert len(re.findall(r'______</b>', hist_text)) == 10
    u3 = blank_label(mcq_lines('u3', hist_lines[first_item:], 10))
    mel_lines = L[rc_II + 1:rc_D]
    mel_first = next(i for i, l in enumerate(mel_lines) if re.match(r'^1\.\s*The main subject', cl(l)))
    mel_par = para_html(mel_lines[:mel_first])
    u4 = mcq_lines('u4', mel_lines[mel_first:], 10)
    u4[1]['q'] = u4[1]['q'].replace('were_', 'were ______')
    pages.append({'id': 'doc-test2', 'title': 'Đọc hiểu – Test 2', 'mode': 'practice', 'groups': [
        {'id': 'u3', 'instr': 'I. Read the text below and decide which answer A, B, C, or D, best fits each space.', 'passage': '<p><b>THE HISTORY OF FILM</b></p><p>%s</p>' % hist_text, 'items': u3},
        {'id': 'u4', 'instr': 'II. Read the passage and choose the correct answer A, B, C, or D for each question.', 'passage': mel_par, 'items': u4},
    ]})

    # ---- viết Test 2
    d_I = find(r'^I\. Give the correct form of the following verbs', rc_D)
    d_II = find(r'^II\. Fill in each blank', d_I)
    d_III = find(r'^III\. Give the correct form of the words', d_II)
    d_IV = find(r'^VI\. Complete the second sentence', d_III)
    d_V = find(r'^V\. Using the prompts', d_IV)
    # D.I
    sub = []
    for ln in L[d_I + 1:d_II]:
        t = cl(ln)
        if not t:
            continue
        if re.match(r'^[a-f]\.\s', t):
            sub.append(t)
        else:
            sub[-1] += ' ' + t
    assert len(sub) == 6
    sub_html = []
    items_d1 = []
    for s in sub:
        def rep(m):
            n = m.group(1)
            return '<b>(%s) ______</b> (%s)' % (n, m.group(2).strip())
        s2 = re.sub(r'\((\d+)\)\s*_{3,}\s*\(([^)]*)\)', rep, s)
        s2 = re.sub(r'\s+', ' ', s2)
        sub_html.append('<p>%s</p>' % s2)
    for m in re.finditer(r'<b>\((\d+)\) ______</b> \(([^)]*)\)', ''.join(sub_html)):
        items_d1.append({'id': 'x1.%d' % int(m.group(1)), 't': 'fill', 'q': '<b>(%s)</b> (%s) {_}' % (m.group(1), m.group(2))})
    assert len(items_d1) == 10, len(items_d1)
    # D.II
    job = ' '.join(cl(l) for l in L[d_II + 1:d_III] if cl(l))
    job = re.sub(r'\((\d+)\)\s*_{3,}', r'<b>(\1) ______</b>', job)
    assert len(re.findall(r'______</b>', job)) == 10
    items_d2 = [{'id': 'x2.%d' % i, 't': 'fill', 'q': '<b>(%d)</b> {_}' % i} for i in range(1, 11)]
    # D.III
    items_d3 = []
    for n, s in numbered(L[d_III + 1:d_IV]):
        m = re.search(r'\(([a-z]+)\)\s*$', s)
        hint = m.group(1).upper()
        q = s[:m.start()].strip()
        q = re.sub(r'\(\d+\)\s*_{3,}', '{_}', q)
        q = re.sub(r'\s+', ' ', q)
        items_d3.append({'id': 'x3.%d' % n, 't': 'fill', 'q': q, 'hint': hint})
    assert len(items_d3) == 10
    # D.IV – đề gốc mất từ gợi ý/ vế sau -> open
    items_d4 = []
    for n, s in numbered(L[d_IV + 1:d_V]):
        items_d4.append({'id': 'x4.%d' % n, 't': 'open', 'q': '<b>%s</b><br><i>Viết lại câu sao cho nghĩa không đổi (đề gốc bị mất từ gợi ý – xem đáp án mẫu).</i>' % keepu(s)})
    assert len(items_d4) == 10
    # D.V
    items_d5 = []
    for ln in L[d_V + 1:t3]:
        t = cl(ln)
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            items_d5.append({'id': 'x5.%d' % int(m.group(1)), 't': 'open', 'q': 'Viết thành câu hoàn chỉnh từ các từ gợi ý: <b>%s</b>' % keepu(m.group(2))})
    assert len(items_d5) == 10
    pages.append({'id': 'viet-test2', 'title': 'Viết – Test 2', 'mode': 'practice', 'groups': [
        {'id': 'x1', 'instr': 'D. WRITING – I. Give the correct form of the following verbs.', 'passage': ''.join(sub_html), 'items': items_d1},
        {'id': 'x2', 'instr': 'II. Fill in each blank with a suitable word.', 'passage': '<p>%s</p>' % job, 'items': items_d2},
        {'id': 'x3', 'instr': 'III. Give the correct form of the words in capitals (từ gốc ghi trong ngoặc).', 'items': items_d3},
        {'id': 'x4', 'instr': 'IV. Complete the second sentence so that it has a similar meaning to the first sentence.', 'items': items_d4},
        {'id': 'x5', 'instr': 'V. Using the prompts provided to write full sentences to make a complete letter.', 'passage': '<p>Dear Sir/Madam,</p><p><i>(các câu 1–10 bên dưới tạo thành nội dung bức thư)</i></p><p>Yours truly,<br>Thomas Cruise.</p>', 'items': items_d5},
    ]})

    # ============================== TEST 3 – trang kiểm tra (140 câu)
    kt = []

    def add(gid, instr, a, b, expect, passage='', kind='mcq'):
        lines = L[a:b]
        if kind == 'err':
            its = err_items('tmp', lines, expect)
        else:
            first = next(int(re.match(r'^\s*(\d+)', cl(l)).group(1)) for l in lines if re.match(r'^\s*\d+', cl(l)))
            off = first - 1

            def shift(l):
                return re.sub(r'^(\s*)(\d+)(\s*\.)', lambda m: '%s%d%s' % (m.group(1), int(m.group(2)) - off, m.group(3)), l)
            its = mk_mcq('tmp', items_of(parse_mcq([shift(l) for l in lines], expect=1)))
        assert len(its) == expect, (gid, len(its), expect)
        base = sum(len(g['items']) for g in kt)
        for j, it in enumerate(its, 1):
            it['id'] = 'kt.%d' % (base + j)
        g = {'id': gid, 'instr': instr, 'items': its}
        if passage:
            g['passage'] = passage
        kt.append(g)

    ex = {}
    pos = t3
    for k in range(1, 13):
        pos = find(r'^Exercise %d\.' % k, pos)
        ex[k] = pos
    ex[13] = len(L)
    heads = {k: cl(L[ex[k]]) for k in range(1, 13)}
    for k in range(1, 13):
        a, b = ex[k] + 1, ex[k + 1]
        # bỏ dòng nhãn 'Part ...' ở cuối (nếu có) trước Exercise kế tiếp
        while b > a and re.match(r'^Part ', cl(L[b - 1])):
            b -= 1
        instr = heads[k]
        if k == 8:
            ps = [i for i in range(a, b) if re.search(r'\(106\)', cl(L[i]))][0]
            pe = next(i for i in range(ps, b) if re.match(r'^106\.', cl(L[i])))
            txt = ' '.join(cl(l) for l in L[a:pe] if cl(l))
            txt = re.sub(r'\((\d+)\)\s*_{3,}', r'<b>(\1) ______</b>', txt)
            assert len(re.findall(r'______</b>', txt)) == 13
            add('kt%d' % k, instr, pe, b, 13, passage='<p>%s</p>' % txt)
            for it in kt[-1]['items']:
                it['q'] = 'Blank (%d)' % int(it['id'].split('.')[1])
        elif k in (9, 10):
            first = next(i for i in range(a, b) if re.match(r'^\d+\.', cl(L[i])))
            par = ''.join('<p>%s</p>' % keepu(cl(l)) for l in L[a:first] if cl(l))
            add('kt%d' % k, instr, first, b, {9: 5, 10: 7}[k], passage=par)
        elif k == 6:
            add('kt6', instr, a, b, 20, kind='err')
        else:
            exp = {1: 10, 2: 20, 3: 10, 4: 10, 5: 20, 7: 15, 11: 5, 12: 5}[k]
            add('kt%d' % k, instr, a, b, exp)
    for g in kt:
        for it in g['items']:
            if it['q'].count('“') > it['q'].count('”'):
                it['q'] += '”'
    n = sum(len(g['items']) for g in kt)
    assert n == 140, n
    pages.append({'id': 'kiem-tra', 'title': 'Bài kiểm tra Test 3 (140 câu)', 'mode': 'test', 'minutes': 120, 'groups': kt})

    return {'id': 'lop10-u3-chuyensau', 'title': 'Unit 3 – Music: Bài tập chuyên sâu', 'grade': 10, 'unit': 3, 'theory': theory(), 'pages': pages}


def dump(path, name, data):
    s = '# -*- coding: utf-8 -*-\n"""Dữ liệu nội dung %s (sinh từ file Word bằng tools/gen_l10u3_chuyensau.py rồi có thể chỉnh tay).\nĐáp án + giải thích: xem file *_dapan.py cùng tên."""\n\n%s = ' % (name, name)
    s += pprint.pformat(data, width=150, sort_dicts=False) + '\n'
    open(path, 'w', encoding='utf8').write(s)


if __name__ == '__main__':
    k = build()
    dump(os.path.join(ROOT, 'units/lop10_u3_chuyensau.py'), 'SET', k)
    tot = 0
    for p in k['pages']:
        c = sum(len(g['items']) for g in p['groups']); tot += c
        print(p['id'], c, [(g['id'], len(g['items'])) for g in p['groups']])
    print('TOTAL', tot)
