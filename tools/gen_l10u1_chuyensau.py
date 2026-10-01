"""Chuyển đổi 1 lần: Word 'Bài tập chuyên sâu' Lớp 10 Unit 1 (Family life) -> units/lop10_u1_chuyensau.py (khung câu hỏi).
Đáp án + giải thích soạn tay ở units/lop10_u1_chuyensau_dapan.py (đối chiếu khoá trong cs_key_c.txt rồi tự giải).
Nguồn src/l10u1/cs_c.txt: dòng 1-1190 = Unit 1 (file Word còn chứa Unit 2-5 + ôn tập, KHÔNG thuộc bộ này).
Gồm: lý thuyết (từ vựng + thì hiện tại đơn/tiếp diễn), bài tập vận dụng, Test 1, Test 2 (nhãn gốc 'TEST 1' thứ hai), Test 3."""
import re, sys, os, shutil, glob
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import parse_mcq, cl
from theory import theory_html
import pprint

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = open(os.path.join(ROOT, 'src/l10u1/cs_c.txt'), encoding='utf8').read()

# ---- sửa lỗi nguồn (chuỗi -> chuỗi), không đổi số dòng
FIX = [
    ('C . on', 'C. on'),
    ('saỵ', 'say'),
    ('fatory', 'factory'),
    ('hale going abroad', 'hate going abroad'),
    ('Tct holiday', 'Tet holiday'),
    ('they-are always', 'they are always'),
    ('other last roads', 'other fast roads'),
    ('ot family', 'of family'),
    ('lor the whole society', 'for the whole society'),
    ('w hole society', 'whole society'),
    ('w ill be unhappy to fry his best', 'will be unhappy to try his best'),
    ('Hinnly members', 'Family members'),
    ('Families impacts very much', 'Families impact very much'),
    ('I28.', '128.'),
    ('mark the letter A, B, C, or Don your', 'mark the letter A, B, C, or D on your'),
    ('wouldn t have', "wouldn't have"),
    ('Although I usually like red. I wore', 'Although I usually like red, I wore'),
    ('thank you very muchTom said to you.', 'thank you very much,” Tom said to you.'),
    ('Thank you very muchTom said to you.', 'Thank you very much,” Tom said to you.'),
    ('muchTom said', 'much,” Tom said'),
    ('Jenny usually eats out because she is not knowing', 'Jenny usually eats out because she is not knowing'),
    ('4 Jenny usually', '4. Jenny usually'),
    ('W hat', 'What'),
    ('A.will boil', 'A. will boil'),
]
for a, b in FIX:
    RAW = RAW.replace(a, b)
L = RAW.split('\n')
# đánh số lại hai câu trùng/nhảy trong Test 3 Exercise 9 (121,121,122 -> 121,122,123)
for i, ln in enumerate(L):
    if ln.startswith('121. Roger'):
        L[i] = ln.replace('121.', '122.', 1)
    if ln.startswith('122. The word “mature”'):
        L[i] = ln.replace('122.', '123.', 1)


def R(a, b):
    """dòng a..b (1-based, gồm cả hai đầu) của cs_c.txt"""
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


def numbered(lines):
    """[(n, text)] gộp dòng tiếp theo vào câu trước"""
    out = []
    for ln in lines:
        t = cl(ln)
        if not t:
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
    """câu có '(a/ b)' trong ngoặc -> mcq plain 2 phương án"""
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


def mcq_group(gid, a, b, expect, fix_numbers=False):
    ev = parse_mcq(R(a, b), expect=1)
    its = items_of(ev)
    assert len(its) == expect, (gid, len(its), expect)
    for it in its:
        assert len(it['o']) >= 2, (gid, it)
    return mk_mcq(gid, its)


# ====================================================================== LÝ THUYẾT
def theory():
    raw = open(os.path.join(ROOT, 'src/l10u1/cs.txt'), encoding='utf8').read().split('\n')
    s1 = next(i for i, l in enumerate(raw) if 'BÀI TẬP VẬN DỤNG CƠ BẢN' in l)                     # hết lý thuyết thì HTĐ
    s2 = next(i for i, l in enumerate(raw) if 'THE PRESENT CONTINUOUS TENSE' in l)
    s3 = next(i for i in range(s2, len(raw)) if 'BÀI TẬP VẬN DỤNG CƠ BẢN' in raw[i])
    return theory_html(raw[:s1] + raw[s2:s3], '')


# ====================================================================== CÁC TRANG
def build():
    pages = []

    # ---------------------------------------------------------------- 1. Phát âm & trọng âm (Test 1, Test 2)
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'p1', 'instr': 'Test 1 – Choose the word that has the underlined part pronounced differently from the others.', 'items': mcq_group('p1', 289, 293, 5)},
        {'id': 'p2', 'instr': 'Test 1 – Pick out the word whose stress pattern is different from that of the others.', 'items': mcq_group('p2', 295, 299, 5)},
        {'id': 'p3', 'instr': 'Test 2 – Choose the word whose underlined part is pronounced differently from that of the others.', 'items': mcq_group('p3', 691, 695, 5)},
        {'id': 'p4', 'instr': 'Test 2 – Choose the word whose stress pattern is different from that of the others.', 'items': mcq_group('p4', 697, 701, 5)},
    ]})

    # ---------------------------------------------------------------- 2. Thì hiện tại đơn (cơ bản)
    hs2 = []
    for n, s in numbered(R(117, 126)):
        pass
    qs = []
    cur = None
    for ln in R(117, 126):
        t = cl(ln)
        if not t:
            continue
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            cur = {'id': 'hs2.%d' % (len(qs) + 1), 't': 'fill', 'q': keepu(m.group(2)) + '<br>Câu hỏi: {_}', 'long': True}
            qs.append(cur)
    assert len(qs) == 5
    hs3_bank = ['wake up', 'open', 'speak', 'take', 'do', 'cause', 'live', 'play', 'close', 'drink']
    hs4_lines = R(141, 141)
    cl141 = cl(hs4_lines[0])
    hs4 = []
    for m in re.finditer(r'\((\d+)\)', cl141):
        hs4.append({'id': 'hs4.%d' % int(m.group(1)), 't': 'fill', 'q': '<b>(%s)</b> {_}' % m.group(1)})
    assert len(hs4) == 16
    pass_hs4 = re.sub(r'\((\d+)\)\s*(?:…+\.*|\.{4,}|_{3,})', r'<b>(\1) ______</b>', cl141)
    pages.append({'id': 'ht-don', 'title': 'Thì hiện tại đơn (cơ bản)', 'mode': 'practice', 'groups': [
        {'id': 'hs1', 'instr': 'I. Put the verbs into the correct form (present simple tense).', 'items': fills('hs1', R(111, 115), 5)},
        {'id': 'hs2', 'instr': 'II. Make questions for the underlined part of the sentence.', 'items': qs},
        {'id': 'hs3', 'instr': 'III. Complete the sentence with the correct form of the verbs in the box.', 'bank': hs3_bank, 'items': fills('hs3', R(129, 139), 10)},
        {'id': 'hs4', 'instr': 'IV. Fill in the blank with only ONE suitable word.', 'passage': '<p>%s</p>' % pass_hs4, 'items': hs4},
        {'id': 'hs5', 'instr': 'V. Choose the best answer.', 'items': mcq_group('hs5', 143, 154, 5)},
    ]})

    # ---------------------------------------------------------------- 3. Thì hiện tại tiếp diễn (cơ bản)
    pages.append({'id': 'ht-tiep-dien', 'title': 'Thì hiện tại tiếp diễn (cơ bản)', 'mode': 'practice', 'groups': [
        {'id': 'hc1', 'instr': 'VI. Put the verbs in the present continuous tense.', 'items': fills('hc1', R(196, 205), 10)},
        {'id': 'hc2', 'instr': 'VII. Choose the correct answer in the bracket.', 'items': choose_bracket('hc2', R(207, 216), 10)},
    ]})

    # ---------------------------------------------------------------- 4. Hiện tại đơn và tiếp diễn
    hk2 = fills('hk2', R(229, 238), 10)
    x_line = cl(L[240 - 1])
    x_items = [{'id': 'hk3.%d' % int(m.group(1)), 't': 'fill', 'q': '<b>(%s)</b> {_}' % m.group(1)} for m in re.finditer(r'\((\d+)\)', x_line)]
    assert len(x_items) == 10
    x_pass = re.sub(r'\((\d+)\)\s*(?:…+\.*|\.{4,}|_{3,})', r'<b>(\1) ______</b>', x_line)
    for it in hk2:
        it['q'] = it['q'].replace('{_} We (meet)', '{_}. We (meet)')
    pages.append({'id': 'ht-don-tiep-dien', 'title': 'Hiện tại đơn và hiện tại tiếp diễn', 'mode': 'practice', 'groups': [
        {'id': 'hk1', 'instr': 'VIII. Put the verbs in the present simple tense or present continuous tense.', 'items': fills('hk1', R(218, 227), 10)},
        {'id': 'hk2', 'instr': 'IX. Put the verbs in the present simple tense or present continuous tense.', 'items': hk2},
        {'id': 'hk3', 'instr': 'X. Fill in the blank with only ONE suitable word.', 'passage': '<p>%s</p>' % x_pass, 'items': x_items},
    ]})

    # ---------------------------------------------------------------- 5. Nâng cao
    camp = cl(L[285 - 1])
    hn4 = []
    for m in re.finditer(r'\((\d+)\.\s*([a-z]+)\)', camp):
        hn4.append({'id': 'hn4.%d' % int(m.group(1)), 't': 'fill', 'q': '<b>(%s)</b> (%s) {_}' % (m.group(1), m.group(2))})
    assert len(hn4) == 10
    camp_pass = re.sub(r'\((\d+)\.\s*([a-z]+)\)\s*(?:…+\.*|\.{4,}|_{3,})', r'<b>(\1) ______</b> (\2)', camp)
    hn3_bank = ['enjoy', 'prefer', 'play', 'work', 'seem', 'know', 'interview', 'wait', 'talk', 'finish']
    pages.append({'id': 'ht-nang-cao', 'title': 'Hiện tại đơn và tiếp diễn (nâng cao)', 'mode': 'practice', 'groups': [
        {'id': 'hn1', 'instr': 'XI. Choose the correct answer in the bracket.', 'items': choose_bracket('hn1', R(243, 250), 8)},
        {'id': 'hn2', 'instr': 'XII. Put the verbs in the correct form (present simple/ present continuous tense).', 'items': fills('hn2', R(252, 271), 20)},
        {'id': 'hn3', 'instr': 'XIII. Complete the sentence using the verbs in the box in the correct form.', 'bank': hn3_bank, 'items': fills('hn3', R(274, 283), 10)},
        {'id': 'hn4', 'instr': 'XIV. Put the verb in brackets in the correct form (present simple or present continuous).', 'passage': '<p>%s</p>' % camp_pass, 'items': hn4},
    ]})

    # ---------------------------------------------------------------- 6. Từ vựng (Test 1 – B)
    tv1_words = ['a. the floor', 'b. the houseplants', 'c. the heavy lifting', 'd. the baby', 'e. the table']
    tv1 = [{'id': 'tv1.%d' % i, 't': 'mcq', 'q': '<b>%s</b> …' % w, 'o': list('abcde'), 'plain': True} for i, w in enumerate(['set', 'mop', 'feed', 'water', 'do'], 1)]
    tv1_note = '<div class="note"><ol type="a">%s</ol></div>' % ''.join('<li>%s</li>' % w[3:] for w in tv1_words)
    tv2 = mcq_group('tv2', 313, 317, 5)
    tv3 = mcq_group('tv3', 319, 335, 8)
    tv4_bank = ['bathing the baby', 'watering the houseplants', 'take out the garbage', 'mop the house', 'doing the laundry', 'doing the cooking',
                'do the washing-up', 'folding the clothes', 'doing the shopping', 'feeding the cats']
    tv4 = []
    for n, s in numbered(R(347, 355)):
        tv4.append({'id': 'tv4.%d' % n, 't': 'fill', 'q': blankify(s)})
    assert len(tv4) == 8, len(tv4)
    tv5 = []
    ev = parse_mcq(R(357, 386), expect=1)
    # mỗi câu có 3 phương án trên các dòng riêng (không có nhãn A-D chuẩn trong stem)
    tv5 = mk_mcq('tv5', items_of(ev))
    assert len(tv5) == 8
    pics = ['feed the cat', 'do the shopping', 'lay the table', 'cook', 'bathe the baby', 'do the washing-up']
    img_order = ['image3.jpg', 'image2.png', 'image5.jpg', 'image1.jpg', 'image6.jpg', 'image4.jpg']
    tv6 = [{'id': 'tv6.%d' % i, 't': 'mcq', 'q': '<b>Hình %d</b> – chọn cụm từ đúng' % i, 'img': 'image%s' % ('1.jpg 2.png 3.jpg 4.jpg 5.jpg 6.jpg'.split()[i - 1]), 'o': pics[:], 'plain': True} for i in range(1, 7)]
    tv7_src = [
        ('1', 'image7.jpg', ['Bathing a newborn baby is never an easy task as it requires skill and experience.', 'Mrs. Laura and her ten-year-old daughter go to the swimming pool every day.', 'Shaking a baby is believed to have bad impacts on his/her development.']),
        ('2', 'image8.jpg', ['The man is taking out the rubbish.', 'Rubbish should be thrown away every day or it may cause awful smell.', 'The child is setting the table for dinner.']),
        ('3', 'image9.jpg', ['The girl is ironing her clothes.', 'Clothes are being folded neatly.', 'Susan is putting clothes in an airing cupboard.']),
        ('4', 'image10.jpg', ["Mopping the garden path is David's favourite activity.", 'Though David has a lot of spare time, he hardly helps his parents do the gardening.', 'At the weekend, David usually helps his grandmother mow the lawn.']),
        ('5', 'image11.jpg', ['Many children are too lazy to help their parents with housework.', 'The girl is doing some cleaning with her mother.', 'The girl is doing the cooking while her mother is sweeping the kitchen floor.']),
    ]
    tv7 = [{'id': 'tv7.%s' % n, 't': 'mcq', 'q': '', 'img': img, 'o': o} for n, img, o in tv7_src]
    pages.append({'id': 'tu-vung', 'title': 'Từ vựng việc nhà (Test 1)', 'mode': 'practice', 'groups': [
        {'id': 'tv1', 'instr': 'I. Match the two columns to make correct phrases (chọn chữ cái a–e).', 'passage': tv1_note, 'items': tv1},
        {'id': 'tv2', 'instr': 'II. Choose the odd one out.', 'items': tv2},
        {'id': 'tv3', 'instr': 'III. Choose the best options to fill in the blanks.', 'items': tv3},
        {'id': 'tv4', 'instr': "IV. Complete the following sentences using the given phrases. There are two phrases that you don't need.", 'bank': tv4_bank, 'items': tv4},
        {'id': 'tv5', 'instr': 'V. Choose the best options to complete the following sentences.', 'items': tv5},
        {'id': 'tv6', 'instr': 'VI. Choose the right words to the pictures.', 'items': tv6},
        {'id': 'tv7', 'instr': 'VII. Choose the sentence that best describes the picture.', 'items': tv7},
    ]})

    # ---------------------------------------------------------------- 7. Ngữ pháp Test 1 (1)
    gp3 = [{'id': 'gp3.%d' % n, 't': 'mcq', 'q': keepu(s), 'o': ['Correct', 'Incorrect'], 'plain': True} for n, s in
           numbered([l for l in R(462, 481) if not re.match(r'^\s*A\.\s*Correct', cl(l))])]
    assert len(gp3) == 10, len(gp3)
    gp1_ev = parse_mcq(R(434, 449), expect=1)
    gp1 = mk_mcq('gp1', items_of(gp1_ev))
    assert len(gp1) == 8
    pages.append({'id': 'ngu-phap-1', 'title': 'Ngữ pháp hiện tại – Test 1 (phần 1)', 'mode': 'practice', 'groups': [
        {'id': 'gp1', 'instr': 'VIII. Choose the correct options to complete the following sentences.', 'items': gp1},
        {'id': 'gp2', 'instr': 'IX. Complete the sentences using the Present Simple or the Present Continuous.', 'items': fills('gp2', R(451, 460), 10)},
        {'id': 'gp3', 'instr': 'X. Decide whether the following sentences are correct or incorrect.', 'items': gp3},
    ]})

    # ---------------------------------------------------------------- 8. Ngữ pháp Test 1 (2)
    gp4_bank = ['have', 'take out', 'take', 'split', 'prepare', 'shop', 'do']
    gp5 = []
    k = 0
    for n, s in numbered([l for l in R(499, 508) if not re.fullmatch(r'_+', cl(l))]):
        gp5.append({'id': 'gp5.%d' % n, 't': 'fill', 'q': keepu(s) + '<br>Từ/cụm từ đúng thay cho chỗ sai: {_}'})
    assert len(gp5) == 5
    gp6 = mk_mcq('gp6', items_of(parse_mcq(R(510, 529), expect=1)))
    assert len(gp6) == 10
    gp8 = mk_mcq('gp8', items_of(parse_mcq(R(581, 598), expect=1)))
    assert len(gp8) == 5
    pages.append({'id': 'ngu-phap-2', 'title': 'Ngữ pháp hiện tại – Test 1 (phần 2)', 'mode': 'practice', 'groups': [
        {'id': 'gp4', 'instr': 'XI. Fill in the blanks with the correct forms of the verbs given. Use negative form if necessary. You can use a word twice.', 'bank': gp4_bank, 'items': fills('gp4', R(490, 497), 8)},
        {'id': 'gp5', 'instr': 'XII. Find ONE mistake in each sentence and fill in the blank with the correct word(s).', 'items': gp5},
        {'id': 'gp6', 'instr': 'XIII. Choose the correct options to complete the following sentences.', 'items': gp6},
        {'id': 'gp7', 'instr': 'XIV. Complete the sentences using the Present simple or the Present Continuous.', 'items': fills('gp7', R(531, 535), 5)},
        {'id': 'gp8', 'instr': 'Choose the TRUE sentences according to the given statements.', 'items': gp8},
    ]})

    # ---------------------------------------------------------------- 9. Ngữ pháp Test 2
    gq3 = []
    for n, s in numbered(R(746, 750)):
        m = re.match(r'^(.*?)\(([A-Z]+)\)\s*$', s)
        gq3.append({'id': 'gq3.%d' % n, 't': 'fill', 'q': blankify(m.group(1)), 'hint': m.group(2)})
    gq4 = fills('gq4', R(752, 756), 5)
    pages.append({'id': 'ngu-phap-test2', 'title': 'Ngữ pháp & từ vựng – Test 2', 'mode': 'practice', 'groups': [
        {'id': 'gq1', 'instr': 'I. Choose the best answer from the four options marked A, B, C or D to complete each sentence below.', 'items': mcq_group('gq1', 704, 733, 15)},
        {'id': 'gq2', 'instr': 'II. Choose the underlined words or phrases (A, B, C or D) that are incorrect in standard English.', 'items': err_items('gq2', R(735, 744), 5)},
        {'id': 'gq3', 'instr': 'III. Give the correct form of the words in CAPITAL to complete the sentences.', 'items': gq3},
        {'id': 'gq4', 'instr': 'IV. Give the correct form of the verbs in brackets.', 'items': gq4},
    ]})

    # ---------------------------------------------------------------- 10. Đọc – Test 1
    p_r1 = para_html(R(538, 541)).replace('because they feel less guilty', 'because <b>they</b> feel less guilty')
    r1a = [{'id': 'r1.%d' % n, 't': 'fill', 'q': blankify(re.sub(r'\s*-\s*_+$', '', s)) + ' – {_}'} for n, s in numbered(R(543, 548))]
    # sửa q: bỏ dấu '-' thừa
    for it in r1a:
        it['q'] = it['q'].replace(' - {_}', ' – {_}')
    r1b = mk_mcq('r2', items_of(parse_mcq(R(550, 567), expect=1)))
    assert len(r1b) == 6 and len(r1a) == 6
    r3_st = []
    buf = None
    for ln in R(572, 579):
        t = cl(ln)
        if not t:
            continue
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            buf = [m.group(2)]
            r3_st.append(buf)
        elif buf is not None:
            buf.append(t)
    r3 = [{'id': 'r3.%d' % i, 't': 'tfng', 'q': ' '.join(b)} for i, b in enumerate(r3_st, 1)]
    assert len(r3) == 4
    cloze_text = para_html(R(600, 601))
    cloze_text = re.sub(r'\((\d+)\)', r'<b>(\1)</b>', cloze_text)
    cloze_text = re.sub(r'____\s*<b>\((\d+)\)</b>', r'<b>(\1) ______</b>', cloze_text)
    r4 = mk_mcq('r4', items_of(parse_mcq(R(602, 611), expect=1)))
    for i, it in enumerate(r4, 1):
        it['q'] = 'Blank (%d)' % i
    assert len(r4) == 10
    pages.append({'id': 'doc-test1', 'title': 'Đọc hiểu – Test 1', 'mode': 'practice', 'groups': [
        {'id': 'r1', 'instr': 'I. Read the passage and do the tasks below. Part 1. Choose no more than THREE WORDS from the reading text that have the same meaning as the given definition to fill in each blank.', 'passage': p_r1, 'items': r1a},
        {'id': 'r2', 'instr': 'Part 2. Choose the best answers for the following questions.', 'passage': p_r1, 'items': r1b},
        {'id': 'r3', 'instr': 'Part 3. Decide whether the following statements are True (T), False (F) or Not Given (NG).', 'passage': p_r1, 'items': r3},
        {'id': 'r4', 'instr': 'III. Choose the best answer to fill in the blank.', 'passage': cloze_text, 'items': r4},
    ]})

    # ---------------------------------------------------------------- 11. Đọc – Test 2
    c1 = para_html(R(759, 761))
    c1 = c1.replace('tuition (7) ____</p><p>and this amount', 'tuition (7) ____ and this amount')
    c1 = re.sub(r'\((\d+)\)\s*____', r'<b>(\1) ______</b>', c1)
    rq1 = mk_mcq('rq1', items_of(parse_mcq(R(762, 771), expect=1)))
    for i, it in enumerate(rq1, 1):
        it['q'] = 'Blank (%d)' % i
    c2_text = ' '.join(cl(l) for l in R(773, 777))
    c2_text = c2_text.replace('often (10) __________________ the volume', 'often (10) __________________ the volume')
    c2_paras = para_html(R(773, 777))
    c2_paras = c2_paras.replace('</p><p>the volume up.', ' the volume up.')
    c2_paras = re.sub(r'\((\d+)\)\s*_+', r'<b>(\1) ______</b>', c2_paras)
    rq2 = [{'id': 'rq2.%d' % i, 't': 'fill', 'q': '<b>(%d)</b> {_}' % i} for i in range(1, 11)]
    assert len(re.findall(r'<b>\(\d+\) ______</b>', c2_paras)) == 10
    c3 = para_html(R(779, 784))
    rq3 = mk_mcq('rq3', items_of(parse_mcq(R(785, 813), expect=1)))
    assert len(rq1) == 10 and len(rq3) == 10, (len(rq1), len(rq3))
    pages.append({'id': 'doc-test2', 'title': 'Đọc hiểu – Test 2', 'mode': 'practice', 'groups': [
        {'id': 'rq1', 'instr': 'I. Read the following passage and mark the letter A, B, C, or D to indicate the correct word or phrase for each of the blanks.', 'passage': c1, 'items': rq1},
        {'id': 'rq2', 'instr': 'II. Fill in each of the numbered blanks with ONE suitable word to complete the following passages.', 'passage': c2_paras, 'items': rq2},
        {'id': 'rq3', 'instr': 'III. Read the following passage on transport, and mark the letter A, B, C, or D to indicate the correct answer to each of the questions.', 'passage': c3, 'items': rq3},
    ]})

    # ---------------------------------------------------------------- 12. Viết – Test 1
    w1_src = [re.sub(r'\s*_{3,}\s*$', '', s) for n, s in numbered(R(657, 666))]
    w1 = [{'id': 'w1.%d' % i, 't': 'fill', 'q': 'Từ cho sẵn: <i>%s</i><br>Câu hoàn chỉnh: {_}' % keepu(s), 'long': True} for i, s in enumerate(w1_src, 1)]
    assert len(w1) == 5
    w2 = [{'id': 'w2.1', 't': 'open', 'q': 'Write a paragraph about doing household chores.'}]
    w3 = []
    cur = None
    for ln in R(668, 687):
        t = cl(ln)
        if not t or re.fullmatch(r'_+', t):
            continue
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            cur = {'n': int(m.group(1)), 'a': m.group(2).strip(), 'b': ''}
            w3.append(cur)
        elif cur is not None and not cur['b']:
            cur['b'] = re.sub(r'\s*_{3,}\s*$', '', t)
    assert len(w3) == 10
    w3 = [{'id': 'w3.%d' % i, 't': 'fill', 'q': '%s<br><b>%s</b> {_}' % (keepu(c['a']), keepu(c['b'])), 'long': True} for i, c in enumerate(w3, 1)]
    w4 = mk_mcq('w4', items_of(parse_mcq(R(613, 654), expect=1)))
    assert len(w4) == 10
    pages.append({'id': 'viet-test1', 'title': 'Viết & diễn đạt lại câu – Test 1', 'mode': 'practice', 'groups': [
        {'id': 'w4', 'instr': 'IV (Reading). Choose the sentence which is closest in meaning with the given one.', 'items': w4},
        {'id': 'w1', 'instr': 'D. WRITING – I. Use the given words to write sentences in present simple or present continuous tense. Remember to capitalize the initial letter of each sentence.', 'items': w1},
        {'id': 'w2', 'instr': 'II. Write a paragraph about doing household chores (tự luận – xem bài mẫu).', 'items': w2},
        {'id': 'w3', 'instr': 'III. Rewrite the following sentences without changing their meaning, using the given words.', 'items': w3},
    ]})

    # ---------------------------------------------------------------- 13. Viết – Test 2
    wq1_src = [re.sub(r'\s*_{3,}\s*$', '', s) for n, s in numbered(R(816, 820))]
    wq1 = [{'id': 'wq1.%d' % i, 't': 'fill', 'q': keepu(s) + '<br>Viết lại câu: {_}', 'long': True} for i, s in enumerate(wq1_src, 1)]
    assert len(wq1) == 5
    wq2 = [{'id': 'wq2.%d' % i, 't': 'fill', 'q': keepu(s) + '<br>Câu hoàn chỉnh: {_}', 'long': True} for i, s in enumerate([s for n, s in numbered(R(822, 831))][:5], 1)]
    wq2 = []
    for n, s in numbered([l for l in R(822, 831) if not re.fullmatch(r'_+', cl(l))]):
        wq2.append({'id': 'wq2.%d' % n, 't': 'fill', 'q': keepu(s) + '<br>Câu hoàn chỉnh: {_}', 'long': True})
    assert len(wq2) == 5
    pages.append({'id': 'viet-test2', 'title': 'Viết – Test 2', 'mode': 'practice', 'groups': [
        {'id': 'wq1', 'instr': 'I. Write the sentence so that it has a similar meaning to the original one.', 'items': wq1},
        {'id': 'wq2', 'instr': 'II. Reorder the following sets of words to make meaningful sentences.', 'items': wq2},
    ]})

    # ---------------------------------------------------------------- 14. Kiểm tra (Test 3 – 140 câu)
    kt = []

    def add(gid, instr, a, b, expect, passage='', kind='mcq'):
        if kind == 'err':
            its = err_items('tmp', R(a, b), expect)
        else:
            first = next(int(re.match(r'^\s*(\d+)', cl(l)).group(1)) for l in R(a, b) if re.match(r'^\s*\d+', cl(l)))
            off = first - 1        # parse_mcq chỉ nhận số câu 1-2 chữ số -> dịch số câu về 1..n

            def shift(l):
                return re.sub(r'^(\s*)(\d+)(\s*\.)', lambda m: '%s%d%s' % (m.group(1), int(m.group(2)) - off, m.group(3)), l)
            its = items_of(parse_mcq([shift(l) for l in R(a, b)], expect=1))
            its = mk_mcq('tmp', its)
        assert len(its) == expect, (gid, len(its), expect)
        base = sum(len(g['items']) for g in kt)
        for j, it in enumerate(its, 1):
            it['id'] = 'kt.%d' % (base + j)
        g = {'id': gid, 'instr': instr, 'items': its}
        if passage:
            g['passage'] = passage
        kt.append(g)

    add('kt1', 'Exercise 1. Mark the letter A, B, C or D to indicate the word whose underlined part differs from the other three in pronunciation in each of the following questions.', 835, 844, 10)
    add('kt2', 'Exercise 2. Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.', 847, 886, 20)
    add('kt3', 'Exercise 3. Mark the letter A, B, C or D to indicate the word(s) CLOSEST in meaning to the underlined word(s) in each of the following questions.', 888, 907, 10)
    add('kt4', 'Exercise 4. Mark the letter A, B, C or D to indicate the word(s) OPPOSITE in meaning to the underlined word(s) in each of the following questions.', 909, 933, 10)
    add('kt5', 'Exercise 5. Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.', 936, 975, 20)
    add('kt6', 'Exercise 6. Mark the letter A, B, C or D to indicate the underlined part that needs correction in each of the following questions.', 977, 1016, 20, kind='err')
    add('kt7', 'Exercise 7. Mark the letter A, B, C or D to indicate the correct response to each of the following exchanges.', 1019, 1068, 15)
    ex8 = para_html(R(1071, 1073))
    ex8 = re.sub(r'\((\d+)\)\s*____', r'<b>(\1) ______</b>', ex8)
    add('kt8', 'Exercise 8. Read the following passage and mark the letter A, B, C, or D to indicate the correct word or phrase that best fits each of the numbered blanks.', 1074, 1086, 13, passage=ex8)
    ex9 = ''.join('<p>%s</p>' % re.sub(r'^(\w+):', r'<b>\1:</b>', keepu(cl(l))) for l in R(1088, 1092))
    add('kt9', 'Exercise 9. Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each of the questions.', 1093, 1105, 5, passage=ex9)
    ex10 = para_html(R(1107, 1110))
    add('kt10', 'Exercise 10. Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each of the questions.', 1111, 1137, 7, passage=ex10)
    add('kt11', 'Exercise 11. Mark the letter A, B, C, or D to indicate the sentence that is closest in meaning to each of the following questions.', 1140, 1164, 5)
    add('kt12', 'Exercise 12. Mark the letter A, B, C, or D to indicate the sentence that best combines each pair of sentences in the following questions.', 1166, 1190, 5)
    for g in kt:
        for it in g['items']:
            if it['q'].count('“') > it['q'].count('”'):
                it['q'] += '”'
    n = sum(len(g['items']) for g in kt)
    assert n == 140, n
    # câu 106-118 (khoảng trống): đề gốc ghi sẵn 'N. A. ...' – giữ thân câu rỗng, hiện nhãn blank
    for it in kt[7]['items']:
        it['q'] = 'Blank (%d)' % (int(it['id'].split('.')[1]) - 1 + 1 - 0)
    # đánh số blank theo đề gốc (106..118)
    for it in kt[7]['items']:
        it['q'] = 'Blank (%d)' % int(it['id'].split('.')[1])
    pages.append({'id': 'kiem-tra', 'title': 'Bài kiểm tra Test 3 (140 câu)', 'mode': 'test', 'minutes': 120, 'groups': kt})

    return {'id': 'lop10-u1-chuyensau', 'title': 'Unit 1 – Family life: Bài tập chuyên sâu', 'grade': 10, 'unit': 1, 'theory': theory(), 'pages': pages}


def dump(path, name, data):
    s = '# -*- coding: utf-8 -*-\n"""Dữ liệu nội dung %s (sinh từ file Word bằng tools/gen_l10u1_chuyensau.py rồi có thể chỉnh tay).\nĐáp án + giải thích: xem file *_dapan.py cùng tên."""\n\n%s = ' % (name, name)
    s += pprint.pformat(data, width=150, sort_dicts=False) + '\n'
    open(path, 'w', encoding='utf8').write(s)


if __name__ == '__main__':
    k = build()
    dump(os.path.join(ROOT, 'units/lop10_u1_chuyensau.py'), 'SET', k)
    dst = os.path.join(ROOT, 'assets/lop10_u1/chuyensau')
    os.makedirs(dst, exist_ok=True)
    import zipfile
    DOCX = glob.glob('/mnt/user-data/uploads/04. GRADE 1-12/GRADE 10/3. BÀI TẬP CHUYÊN SÂU/*FAMILY-LIFE.docx')
    if DOCX:      # ảnh image1..image11 của file đề (Unit 1)
        with zipfile.ZipFile(DOCX[0]) as z:
            for i, e in enumerate('jpg png jpg jpg jpg jpg jpg jpg jpg jpg jpg'.split(), 1):
                with z.open('word/media/image%d.%s' % (i, e)) as f, open(os.path.join(dst, 'image%d.%s' % (i, e)), 'wb') as o:
                    o.write(f.read())
    tot = 0
    for p in k['pages']:
        c = sum(len(g['items']) for g in p['groups']); tot += c
        print(p['id'], c, [(g['id'], len(g['items'])) for g in p['groups']])
    print('TOTAL', tot)
