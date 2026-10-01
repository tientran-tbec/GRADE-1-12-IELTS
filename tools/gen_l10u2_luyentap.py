"""Chuyển đổi 1 lần: Word Lớp 10 Unit 2 (Bài tập luyện tập) -> units/lop10_u2_luyentap.py (khung câu hỏi).
Nguồn: src/l10u2/lt.txt (lý thuyết, có bảng) & src/l10u2/lt_c.txt (bài tập). Đáp án + giải thích soạn tay ở units/lop10_u2_luyentap_dapan.py."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import cl
from theory import theory_html
from gen_units import keepu, dump

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = open(os.path.join(ROOT, 'src/l10u2/lt.txt'), encoding='utf8').read().split('\n')
LC = open(os.path.join(ROOT, 'src/l10u2/lt_c.txt'), encoding='utf8').read().split('\n')
END = next(i for i, l in enumerate(LC) if 'ĐÁP ÁN CHI TIẾT' in l)
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


def split_opts(txt):
    """tách stem + 4 phương án theo chữ cái (chịu được bố cục 2 cột A C / B D)"""
    ms = list(re.finditer(r'(?:^|\s)([A-D])\.\s+', txt))
    first = {}
    a = next((m for m in ms if m.group(1) == 'A'), None)
    if a is None:
        return None
    pos = {}
    for m in ms:
        if m.start() >= a.start() and m.group(1) not in pos:
            pos[m.group(1)] = m
    if sorted(pos) != list('ABCD'):
        return None
    order = sorted(pos.values(), key=lambda m: m.start())
    res = {}
    for k, m in enumerate(order):
        e = order[k + 1].start() if k + 1 < len(order) else len(txt)
        res[m.group(1)] = re.sub(r'\s+', ' ', txt[m.end():e]).strip()
    return txt[:a.start()].strip(), [res[c] for c in 'ABCD']


def parse_items(lines, first=1, kind='mcq'):
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
            txt1 = re.sub(r'([,.;])</u>', r'</u>\1', txt1)
            segs = re.findall(r'<u>(.*?)</u>', txt1)
            assert len(segs) == 4, (it['n'], segs)
            k = iter('ABCD')
            q = re.sub(r'<u>(.*?)</u>', lambda mm: '<u>%s</u><sup>%s</sup>' % (mm.group(1).strip(), next(k)), txt1)
            q = re.sub(r'(</sup>)(?=\w)', r'\1 ', q)
            out.append({'n': it['n'], 'q': re.sub(r'\s+', ' ', q).strip(), 'o': [s.strip() for s in segs]})
            continue
        r = split_opts(txt)
        assert r, (it['n'], txt)
        out.append({'n': it['n'], 'stem': r[0], 'o': r[1]})
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
        num = it.get('n', k) if prefix in ('t15', 't45') else k
        res.append({'id': '%s.%d' % (prefix, num), 't': 'mcq', 'q': keepu(q), 'o': [keepu(x) for x in it['o']]})
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


def src_p(ps):
    ps = re.sub(r'<p>\((Adapted from|Source:)([^)]*)\)</p>', r'<p class="src">(\1\2)</p>', ps)
    return ps


def build():
    # ---------------- lý thuyết
    b = next(i for i, l in enumerate(RAW) if 'PRACTICE EXERCISES' in l)
    th = theory_html(RAW[:b])
    th = th.replace('<mark>', '').replace('</mark>', '').replace('”', '"').replace('“', '"')
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
    wf = []
    for l in L[v_wf + 1:v_mc]:
        t = cl(l); m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            s = m.group(2); h = re.search(r'\(([A-Z]+)\)', s).group(1)
            s = fillq(s.replace('(%s)' % h, ''))
            wf.append({'id': 'vb3.%d' % (len(wf) + 1), 't': 'fill', 'q': s, 'hint': h})
    vb4 = mcq('vb4', parse_items(L[v_mc + 1:v_pr]))
    pr = []
    for l in L[v_pr + 1:v_er]:
        t = cl(l); m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            pr.append({'id': 'vb5.%d' % (len(pr) + 1), 't': 'fill', 'q': fillq(m.group(2))})
    vb6 = mcq('vb6', parse_items(L[v_er + 1:c0], kind='err'))
    assert (len(vb1), len(vb2), len(wf), len(vb4), len(pr), len(vb6)) == (5, 5, 5, 15, 5, 5), (len(vb1), len(vb2), len(wf), len(vb4), len(pr), len(vb6))
    pages.append({'id': 'tu-vung', 'title': 'Từ vựng', 'mode': 'practice', 'groups': [
        {'id': 'vb1', 'instr': 'Mark the letter A, B, C, or D to indicate the word(s) CLOSEST in meaning to the underlined word(s) in each of the following sentences.', 'items': vb1},
        {'id': 'vb2', 'instr': 'Mark the letter A, B, C, or D to indicate the word(s) OPPOSITE in meaning to the underlined word(s) in each of the following sentences.', 'items': vb2},
        {'id': 'vb3', 'instr': 'Give the correct forms of words in brackets.', 'items': wf},
        {'id': 'vb4', 'instr': 'Mark the letter A, B, C, or D to indicate the correct answer to each of the following sentences.', 'items': vb4},
        {'id': 'vb5', 'instr': 'Fill in the blanks with suitable prepositions.', 'items': pr},
        {'id': 'vb6', 'instr': 'Mark the letter A, B, C, or D to indicate the underlined part that needs correction in each of the following questions.', 'items': vb6}]})
    # ---------------- C. Grammar
    d0 = fnd(r'<b>D\. SPEAKING')
    g_v = fnd(r'Give the correct forms of the verbs', c0); g_m = fnd(r'correct answer to each of the following questions', g_v)
    g_r = fnd(r'Rewrite the following sentences', g_m)
    gi = []
    for l in L[g_v + 1:g_m]:
        t = cl(l); m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            s = m.group(2); h = re.search(r'\(([^)]*)\)', s).group(1)
            s = fillq(s.replace('(%s)' % h, ''))
            gi.append({'id': 'gr1.%d' % (len(gi) + 1), 't': 'fill', 'q': s, 'hint': h})
    assert len(gi) == 10
    # câu 5: "You (cook) ... ?" -> khoá "Are you going to cook": đảo chủ ngữ vào ô trống
    gi[4]['q'] = '{_} for the party? I see a lot of ingredients in the kitchen.'
    gi[4]['hint'] = 'you (cook)'
    gr2 = mcq('gr2', parse_items(L[g_m + 1:g_r], first=11))
    assert len(gr2) == 10
    rw = []
    cur = None
    for l in L[g_r + 1:d0]:
        t = cl(l)
        if not t:
            continue
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            cur = {'s': m.group(2), 'b': ''}; rw.append(cur)
        elif t.startswith('=>') and cur is not None:
            cur['b'] = t[2:].strip()
    assert len(rw) == 5
    gr3 = []
    for k, r in enumerate(rw, 1):
        beg = r['b']
        end = beg[-1] if beg[-1] in '.?' else ''
        beg = beg.rstrip('.?').strip()
        gr3.append({'id': 'gr3.%d' % k, 't': 'open',
                    'q': '%s<br>=> <b>%s</b> ……………………%s' % (r['s'].rstrip(), beg, end or '.')})
    gr3[3]['q'] = gr3[3]['q'].replace('shopping<br>', 'shopping.<br>')
    pages.append({'id': 'ngu-phap', 'title': 'Ngữ pháp', 'mode': 'practice', 'groups': [
        {'id': 'gr1', 'instr': 'Give the correct forms of the verbs in brackets. (Future simple: will / be going to)', 'items': gi},
        {'id': 'gr2', 'instr': 'Mark the letter A, B, C, or D to indicate the correct answer to each of the following questions. (Passive voice)', 'items': gr2},
        {'id': 'gr3', 'instr': 'Rewrite the following sentences using the passive voice. Begin each sentence as shown.', 'items': gr3}]})
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
    ps1 = src_p(P(L[r1 + 1:k1]))
    k2 = next(i for i in range(r2, t15) if re.match(r'^6\.\s', cl(L[i])))
    ps2 = src_p(P(L[r2 + 1:k2]))
    rd2 = mcq('rd2', parse_items(L[k2:t15], first=6))
    rd2 = [dict(x, id='rd2.%d' % k) for k, x in enumerate(rd2, 1)]
    assert len(rd1) == 5 and len(rd2) == 5
    pages.append({'id': 'noi', 'title': 'Nói (hội thoại)', 'mode': 'practice', 'groups': [
        {'id': 'sp1', 'instr': 'Mark the letter A, B, C or D to indicate the sentence that best completes each of the following exchanges.', 'items': sp}]})
    pages.append({'id': 'doc', 'title': 'Đọc hiểu', 'mode': 'practice', 'groups': [
        {'id': 'rd1', 'instr': 'Read the following passage and mark the letter A, B, C, or D to indicate the correct word or phrase that best fits each of the numbered blanks.', 'passage': ps1, 'items': rd1},
        {'id': 'rd2', 'instr': 'Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each of the questions.', 'passage': ps2, 'items': rd2}]})
    # ---------------- 15-minute test
    t45 = fnd(r'45-MINUTE TEST')
    h1 = mcq('t15', parse_items(L[t15 + 2:t45]))
    assert [int(x['id'].split('.')[1]) for x in h1] == list(range(1, 16))
    pages.append({'id': 'kiem-tra-15', 'title': 'Kiểm tra 15 phút', 'mode': 'test', 'minutes': 15, 'groups': [
        {'id': 'k15a', 'instr': cl(L[t15 + 1]), 'items': h1}]})
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
        if cl(L[A[gi_] + 1]).startswith('word(s)'):
            instr += ' ' + cl(L[A[gi_] + 1])
        instr = re.sub(r'\s+', ' ', instr)
        if sp_ is None:
            first = 26 if gi_ == 6 else 31
            kk = next(i for i in range(A[gi_] + 1, A[gi_ + 1]) if re.match(r'^%d\.\s' % first, cl(L[i])))
            its = mcq('t45', parse_items(L[kk:A[gi_ + 1]], first=first))
            for it in its:
                it['q'] = 'Blank (%s)' % it['id'].split('.')[1] if gi_ == 6 else it['q']
            ps = src_p(P(L[A[gi_] + 1:kk]))
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
            if g.get('passage'):
                g['passage'] = re.sub(r'"([^"<>]*?)”\s*"', r'“\1” “', g['passage']).replace("'", '’')
                g['passage'] = re.sub(r'(?<=\s)"(?=[A-Za-z])|(?<=[.!?])"', lambda m: '“' if m.group(0) == '"' and False else m.group(0), g['passage'])
            for it in g['items']:
                i = it['id']
                it['q'] = re.sub(r'\s*READING\s*$', '', it['q'])
                it['q'] = re.sub(r'"([^"”]*?)”', r'“\1”', it['q'])
                it['q'] = it['q'].replace('______.', '______').replace('{_} .', '{_}.')
                if i in ('rd2.2', 't45.35'):
                    it['q'] = it['q'].replace(' NOT ', ' <b>NOT</b> ').replace('NOT true', '<b>NOT</b> true')
                if i == 'rd2.4':
                    it['q'] = it['q'].replace('EXCEPT', '<b>EXCEPT</b>')
                if i == 't45.34':
                    it['q'] = 'The word “<u>it</u>” in paragraph 2 refers to ______'
                if i == 't45.32':
                    it['q'] = 'The word “<u>ran</u>” in paragraph 1 is closest in meaning to ______'
                if i == 'gr2.4':
                    it['q'] = '“When ______?” – “In 1876.”'
                it['q'] = re.sub(r'"([^"<>]*?)"', r'“\1”', it['q'])
                it['q'] = re.sub(r'<u>([^<]*?)\s+</u>(?=\S)', r'<u>\1</u> ', it['q'])
                it['q'] = it['q'].replace('=>', '&rarr;')
                it['q'] = it['q'].replace("'", '’')
                if 'o' in it:
                    it['o'] = [x.replace("'", '’') for x in it['o']]
    return {'id': 'lop10-u2-luyentap', 'title': 'Unit 2 – Humans and the environment: Bài tập luyện tập', 'grade': 10, 'unit': 2, 'theory': th, 'pages': pages}


if __name__ == '__main__':
    b = build()
    dump(os.path.join(ROOT, 'units/lop10_u2_luyentap.py'), 'SET', b)
    tot = 0
    for p in b['pages']:
        n = sum(len(g['items']) for g in p['groups']); tot += n
        print(p['id'], n, [(g['id'], len(g['items'])) for g in p['groups']])
    print('TOTAL', tot)
