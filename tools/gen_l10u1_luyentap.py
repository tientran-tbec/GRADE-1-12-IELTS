"""Chuyển đổi 1 lần: Word Lớp 10 Unit 1 (Bài tập luyện tập) -> units/lop10_u1_luyentap.py (khung câu hỏi).
Nguồn: src/l10u1/lt.txt (lý thuyết, có bảng) & src/l10u1/lt_c.txt (bài tập). Đáp án + giải thích soạn tay ở units/lop10_u1_luyentap_dapan.py."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import cl
from theory import theory_html
from gen_units import keepu, dump

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = open(os.path.join(ROOT, 'src/l10u1/lt.txt'), encoding='utf8').read().split('\n')
LC = open(os.path.join(ROOT, 'src/l10u1/lt_c.txt'), encoding='utf8').read().split('\n')
END = next(i for i, l in enumerate(LC) if 'ĐÁP ÁN' in l and '⟦' in l)
L = LC[:END]


def fnd(pat, start=0):
    for i in range(start, len(L)):
        if re.search(pat, L[i]):
            return i
    raise KeyError(pat)


def fixblank(s):
    s = re.sub(r'\s*_{3,}\s*', ' ______ ', s)
    s = re.sub(r'\s+([.,?!;:])', r'\1', s)
    return re.sub(r'[ \t]+', ' ', s).strip()


def parse_items(lines, first=1, kind='mcq'):
    """tách câu theo số thứ tự liên tiếp; mỗi câu: stem + 4 phương án"""
    items, cur, exp = [], None, first
    for ln in lines:
        t = cl(ln)
        if not t or t.startswith('=>') or re.fullmatch(r'[A-D](?:\s+[A-D])*', t):
            continue
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m and int(m.group(1)) == exp:
            cur = {'n': exp, 'lines': [m.group(2)]}
            items.append(cur)
            exp += 1
        elif cur is not None:
            cur['lines'].append(t)
    out = []
    for it in items:
        ls = [x for x in it['lines'] if x != '']
        txt = '\n'.join(ls)
        if kind == 'err':
            txt1 = re.sub(r'\s*\n\s*', ' ', txt)
            segs = re.findall(r'<u>(.*?)</u>', txt1)
            assert len(segs) == 4, (it['n'], segs)
            k = iter('ABCD')
            q = re.sub(r'<u>(.*?)</u>', lambda mm: '<u>%s</u><sup>%s</sup>' % (mm.group(1).strip(), next(k)), txt1)
            q = re.sub(r'(</sup>)(?=\w)', r'\1 ', q)
            out.append({'n': it['n'], 'q': re.sub(r'\s+', ' ', q).strip(), 'o': [s.strip() for s in segs]})
            continue
        mm = re.search(r'(?:^|\s)A\.\s+(.*?)\s+B\.\s+(.*?)\s+C\.\s+(.*?)\s+D\.\s+(.*)$', txt, re.S)
        assert mm, (it['n'], txt)
        stem = txt[:mm.start()].strip()
        out.append({'n': it['n'], 'stem': stem, 'o': [re.sub(r'\s+', ' ', x).strip() for x in mm.groups()]})
    return out


def mcq(prefix, its, dialog=False):
    res = []
    for k, it in enumerate(its, 1):
        if 'q' in it:
            q = it['q']
        elif dialog:
            q = '<br>'.join(re.sub(r'^([A-Z][a-z]+):', r'<b>\1:</b>', fixblank(x)) for x in it['stem'].split('\n'))
        else:
            q = fixblank(re.sub(r'\s*\n\s*', ' ', it['stem']))
        res.append({'id': '%s.%d' % (prefix, it.get('n', k) if prefix.startswith('t') and prefix[1:3] in ('15', '45') else k),
                    't': 'mcq', 'q': keepu(q), 'o': [keepu(x) for x in it['o']]})
    return res


def P(lines):
    paras = []
    for l in lines:
        t = keepu(cl(l))
        if not t:
            continue
        t = re.sub(r'\((\d+)\)\s*_{2,}\s*', r'<b>(\1) ______</b> ', t)
        if paras and t[0].islower():
            paras[-1] += ' ' + t
        else:
            paras.append(t)
    out = ''
    for p in paras:
        p = re.sub(r'\s+([.,?!;:])', r'\1', re.sub(r'\s+', ' ', p)).strip()
        out += '<p>%s</p>' % p
    return out


def fillq(s):
    s = re.sub(r'\s*_{3,}\s*', ' {_} ', s)
    return re.sub(r'\s+([.,?!;:])', r'\1', re.sub(r'\s+', ' ', s)).strip()


def build():
    # ---------------- lý thuyết
    b = next(i for i, l in enumerate(RAW) if 'PRACTICE EXERCISES' in l)
    th = theory_html(RAW[:b])
    th = th.replace('<mark>', '').replace('</mark>', '')
    th = th.replace('<p>be is: số ít</p>', '<p>be: am (I) / is (số ít) / are (số nhiều)</p>').replace('<p>am: I</p>', '')
    th = th.replace('<p>V</p><p>V (s/es): số ít</p>', '<p>V (s/es): số ít</p>')
    pages = []
    # ---------------- A. Phonetics
    a0 = fnd(r'A\. PHONETICS'); a_s = fnd(r'position of primary stress', a0); b0 = fnd(r'<b>B\. VOCABULARY')
    pa1 = mcq('pa1', parse_items(L[a0 + 2:a_s]))
    pa2 = mcq('pa2', parse_items(L[a_s + 1:b0]))
    assert len(pa1) == 5 and len(pa2) == 5
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'pa1', 'instr': 'Mark the letter A, B, C, or D to indicate the word whose underlined part differs from the other three in pronunciation in each of the following questions.', 'items': pa1},
        {'id': 'pa2', 'instr': 'Mark the letter A, B, C, or D to indicate the word that differs from the other three in the position of primary stress in each of the following questions.', 'items': pa2}]})
    # ---------------- B. Vocabulary
    v_cl = fnd(r'CLOSEST', b0); v_op = fnd(r'OPPOSITE', v_cl); v_wf = fnd(r'Give the correct forms of words', v_op)
    v_mc = fnd(r'indicate the correct answer to each of the following sentences', v_wf); v_pr = fnd(r'suitable prepositions', v_mc)
    v_er = fnd(r'needs correction', v_pr); c0 = fnd(r'<b>C\. GRAMMAR')
    vb1 = mcq('vb1', parse_items(L[v_cl + 1:v_op])); vb2 = mcq('vb2', parse_items(L[v_op + 1:v_wf]))
    vb1[3]['q'] = vb1[3]['q'].replace('<u>encourag</u>e', '<u>encourage</u>')
    wf = []
    for l in L[v_wf + 1:v_mc]:
        t = cl(l); m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            s = m.group(2); h = re.search(r'\(([A-Z]+)\)', s).group(1)
            s = fillq(s.replace('(%s)' % h, ''))
            wf.append({'id': 'vb3.%d' % len(wf + [0]), 't': 'fill', 'q': s, 'hint': h})
    vb4 = mcq('vb4', parse_items(L[v_mc + 1:v_pr]))
    pr = []
    for l in L[v_pr + 1:v_er]:
        t = cl(l); m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            pr.append({'id': 'vb5.%d' % (len(pr) + 1), 't': 'fill', 'q': fillq(m.group(2))})
    vb6 = mcq('vb6', parse_items(L[v_er + 1:c0], kind='err'))
    assert (len(vb1), len(vb2), len(wf), len(vb4), len(pr), len(vb6)) == (5, 5, 5, 15, 5, 10), (len(vb1), len(vb2), len(wf), len(vb4), len(pr), len(vb6))
    pages.append({'id': 'tu-vung', 'title': 'Từ vựng', 'mode': 'practice', 'groups': [
        {'id': 'vb1', 'instr': 'Mark the letter A, B, C, or D to indicate the word(s) CLOSEST in meaning to the underlined word(s) in each of the following sentences.', 'items': vb1},
        {'id': 'vb2', 'instr': 'Mark the letter A, B, C, or D to indicate the word(s) OPPOSITE in meaning to the underlined word(s) in each of the following sentences.', 'items': vb2},
        {'id': 'vb3', 'instr': 'Give the correct forms of words in brackets.', 'items': wf},
        {'id': 'vb4', 'instr': 'Mark the letter A, B, C, or D to indicate the correct answer to each of the following sentences.', 'items': vb4},
        {'id': 'vb5', 'instr': 'Fill in the blanks with suitable prepositions.', 'items': pr},
        {'id': 'vb6', 'instr': 'Mark the letter A, B, C, or D to indicate the underlined part that needs correction in each of the following questions.', 'items': vb6}]})
    # ---------------- C. Grammar (điền dạng đúng của động từ)
    d0 = fnd(r'<b>D\. SPEAKING')
    gr = [
        ('What time {_} for Hanoi in the afternoons, Dad?', 'this train (leave)'),
        ('I often {_} breakfast at 7 a.m in the morning.', 'have'),
        ('This knife {_} very well. It {_} sharp enough.', 'not cut / not be'),
        ('- {_} reading books?\n- Yes, I do. I’m really into fiction books.', 'you (like)'),
        ('My mother usually {_} in the morning to prepare breakfast for my family.', 'get up'),
        ('The school year {_} in early September and {_} in May.', 'begin / end'),
        ('Don’t call Mary now. She {_} an important exam now.', 'have'),
        ('Mrs Brown {_} on holiday in Hawaii next week. She has already booked a flight ticket.', 'go'),
        ('Linda often goes to school by bus, but she {_} her bike today.', 'ride'),
        ('Tom {_} late. This makes his boss very angry.', 'always + come'),
        ('We can go out now. It {_} .', 'not rain'),
        ('Who {_} in the kitchen, Mary?', 'cook'),
    ]
    src = [cl(l) for l in L[fnd(r'Give the correct forms of the verbs', c0) + 1:d0] if cl(l)]
    assert len([s for s in src if re.match(r'^\d+\.', s)]) == 12
    gi = [{'id': 'gr1.%d' % i, 't': 'fill', 'q': q.replace('\n', '<br>'), 'hint': h} for i, (q, h) in enumerate(gr, 1)]
    pages.append({'id': 'ngu-phap', 'title': 'Ngữ pháp', 'mode': 'practice', 'groups': [
        {'id': 'gr1', 'instr': 'Give the correct forms of the verbs in brackets. (Present simple / present continuous)', 'items': gi}]})
    # ---------------- D. Speaking
    e0 = fnd(r'<b>E\. READING')
    sp = mcq('sp1', parse_items(L[d0 + 2:e0]), dialog=True)
    assert len(sp) == 5
    # ---------------- E. Reading
    r1 = fnd(r'best fits each of the numbered blanks', e0); r2 = fnd(r'correct answer to each of the questions', r1); t15 = fnd(r'15-MINUTE TEST')
    k1 = next(i for i in range(r1, r2) if re.match(r'^1\.\s', cl(L[i])))
    rd1 = mcq('rd1', parse_items(L[k1:r2]))
    for k, it in enumerate(rd1, 1):
        it['q'] = 'Blank (%d)' % k
    ps1 = P(L[r1 + 1:k1])
    ps1 = ps1.replace('<p>What is tiger parenting?</p>', '<h4>What is tiger parenting?</h4>').replace('selfharm', 'self-harm')
    ps1 = re.sub(r'<p>\(Adapted from ([^)]*)\)</p>', r'<p class="src">(Adapted from \1)</p>', ps1)
    k2 = next(i for i in range(r2, t15) if re.match(r'^11\.\s', cl(L[i])))
    ps2 = P(L[r2 + 1:k2])
    ps2 = ps2.replace('accepts these sorts of living arrangements</p>', 'accepts these sorts of living arrangements.</p>').replace('living arrangements</p>', 'living arrangements.</p>').replace('living arrangements..', 'living arrangements.')
    ps2 = ps2.replace('<p>(Adapted from THE SCHOOL OF LIFE)</p>', '<p class="src">(Adapted from THE SCHOOL OF LIFE)</p>')
    rd2 = mcq('rd2', parse_items(L[k2:t15], first=11))
    rd2 = [dict(x, id='rd2.%d' % k) for k, x in enumerate(rd2, 1)]
    assert len(rd1) == 10 and len(rd2) == 5
    pages.append({'id': 'noi', 'title': 'Nói (hội thoại)', 'mode': 'practice', 'groups': [
        {'id': 'sp1', 'instr': 'Mark the letter A, B, C or D to indicate the sentence that best completes each of the following exchanges.', 'items': sp}]})
    pages.append({'id': 'doc', 'title': 'Đọc hiểu', 'mode': 'practice', 'groups': [
        {'id': 'rd1', 'instr': 'Read the following passage and mark the letter A, B, C, or D to indicate the correct word or phrase that best fits each of the numbered blanks.', 'passage': ps1, 'items': rd1},
        {'id': 'rd2', 'instr': 'Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each of the questions.', 'passage': ps2, 'items': rd2}]})
    # ---------------- 15-minute test
    t45 = fnd(r'45-MINUTE TEST')
    f_same = fnd(r'Find the sentence having the same meaning', t15)
    h1 = mcq('t15', parse_items(L[t15 + 2:f_same]))
    h2 = mcq('t15', parse_items(L[f_same + 1:t45], first=12))
    assert len(h1) == 11 and len(h2) == 4
    pages.append({'id': 'kiem-tra-15', 'title': 'Kiểm tra 15 phút', 'mode': 'test', 'minutes': 15, 'groups': [
        {'id': 'k15a', 'instr': 'Mark the letter A, B, C, or D to indicate the correct answer to each of the following sentences.', 'items': h1},
        {'id': 'k15b', 'instr': 'Find the sentence having the same meaning.', 'items': h2[:2]},
        {'id': 'k15c', 'instr': 'Mark the letter A, B, C, or D to indicate the correct answer to each of the following sentences.', 'items': h2[2:]}]})
    # ---------------- 45-minute test
    A = [fnd(p, t45) for p in [r'whose underlined part differs', r'position of primary stress', r'CLOSEST', r'OPPOSITE',
                               r'indicate the correct answer to each of the following sentences', r'needs correction',
                               r'numbered blanks from 26 to 30', r'questions from 31 to 35', r'best completes each of the following exchanges',
                               r'closest in meaning to each of the following questions']] + [len(L)]
    spec = [('k45a', 1, 'mcq'), ('k45b', 3, 'mcq'), ('k45c', 6, 'mcq'), ('k45d', 8, 'mcq'), ('k45e', 10, 'mcq'), ('k45f', 23, 'err'),
            None, None, ('k45i', 36, 'dlg'), ('k45j', 38, 'mcq')]
    groups = []
    for gi_, sp_ in enumerate(spec):
        instr = cl(L[A[gi_]])
        if sp_ is None:
            first = 26 if gi_ == 6 else 31
            kk = next(i for i in range(A[gi_] + 1, A[gi_ + 1]) if re.match(r'^%d\.\s' % first, cl(L[i])))
            its = mcq('t45', parse_items(L[kk:A[gi_ + 1]], first=first))
            for it in its:
                it['q'] = 'Blank (%s)' % it['id'].split('.')[1] if gi_ == 6 else it['q']
            ps = P(L[A[gi_] + 1:kk])
            ps = re.sub(r'<p>\(Source: ([^)]*)\)</p>', r'<p class="src">(Source: \1)</p>', ps)
            ps = re.sub(r'<p>\(Adapted from ([^)]*)\)</p>', r'<p class="src">(Adapted from \1)</p>', ps)
            groups.append({'id': 'k45g' if gi_ == 6 else 'k45h', 'instr': instr, 'passage': ps, 'items': its})
            continue
        gid, first, kind = sp_
        its = parse_items(L[A[gi_] + 1:A[gi_ + 1]], first=first, kind='err' if kind == 'err' else 'mcq')
        groups.append({'id': gid, 'instr': instr, 'items': mcq('t45', its, dialog=(kind == 'dlg'))})
    nums = [int(it['id'].split('.')[1]) for g in groups for it in g['items']]
    assert nums == list(range(1, 41)), nums
    pages.append({'id': 'kiem-tra-45', 'title': 'Kiểm tra 45 phút', 'mode': 'test', 'minutes': 45, 'groups': groups})
    # ---------------- sửa lỗi nguồn
    for pg in pages:
        for g in pg['groups']:
            for it in g['items']:
                i = it['id']
                it['q'] = re.sub(r'\s*READING\s*$', '', it['q'])
                it['q'] = re.sub(r'"([^"”]*?)”', r'“\1”', it['q'])
                it['q'] = it['q'].replace('______.', '______').replace('{_} .', '{_}.')
                if i == 't45.23':
                    it['q'] = it['q'].replace('<u>for example.</u><sup>C</sup> teaching', '<u>for example</u><sup>C</sup>, teaching').replace('benefits for children;', 'benefits for children,')
                    it['o'][2] = 'for example'
                if i == 'rd2.4':
                    it['q'] = 'According to the passage, young women ______.'
                it['q'] = it['q'].replace("'", '’')
                if 'o' in it:
                    it['o'] = [x.replace("'", '’') for x in it['o']]
    return {'id': 'lop10-u1-luyentap', 'title': 'Unit 1 – Family life: Bài tập luyện tập', 'grade': 10, 'unit': 1, 'theory': th, 'pages': pages}


if __name__ == '__main__':
    b = build()
    dump(os.path.join(ROOT, 'units/lop10_u1_luyentap.py'), 'SET', b)
    tot = 0
    for p in b['pages']:
        n = sum(len(g['items']) for g in p['groups']); tot += n
        print(p['id'], n, [(g['id'], len(g['items'])) for g in p['groups']])
    print('TOTAL', tot)
