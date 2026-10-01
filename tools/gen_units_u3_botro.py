"""Chuyển đổi 1 lần: Word Unit 3 (Bài tập bổ trợ) -> units/lop11_u3_botro.py (khung câu hỏi).
Đáp án + giải thích ở units/lop11_u3_botro_dapan.py (soạn tay, đối chiếu với khoá highlight trong nửa sau file Word).
Nguồn src/u3/botro.txt: nửa đầu (đến '--- THE END ---' lần 1) = đề; nửa sau = bản có đáp án tô đậm ⟦…⟧."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import parse_mcq, cl
from theory import theory_html
import gen_units as G
from gen_units import mk_mcq, groups_from_events, keepu, dump

ROOT = G.ROOT
_RAW = open(os.path.join(ROOT, 'src/u3/botro.txt')).read()
# --- sửa lỗi nguồn (không đổi số dòng)
for a, b in [('C harmless', 'C. harmless'), ('D. much cautious ly', 'D. much cautiously'), ('D. clearly\t.', 'D. clearly'),
             ('We\'ll tum off', "We'll turn off"), ("won' t", "won't")]:
    _RAW = _RAW.replace(a, b)
BR = _RAW.split('\n')
SPLIT = next(i for i, l in enumerate(BR) if 'THE END' in l) + 1     # 0-based: dòng đầu nửa sau


def fnd(pat, start=1, end=None):
    """1-based index của dòng đầu tiên >= start khớp regex"""
    for i in range(start - 1, (end or len(BR))):
        if re.search(pat, BR[i]):
            return i + 1
    raise KeyError(pat)


def rng(a, b):
    return BR[a - 1:b]


def items_of(ev):
    return [v for k, v in ev if k == 'item']


def fixblank(s):
    s = re.sub(r'\s*_{3,}\s*', ' ______ ', s)
    s = re.sub(r'\s+([.,?!;:])', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def mcq(gid, ev_or_items, start=1):
    its = items_of(ev_or_items) if ev_or_items and isinstance(ev_or_items[0], tuple) else ev_or_items
    out = mk_mcq(gid, its, start)
    for it in out:
        it['q'] = fixblank(it['q'])
        it['o'] = [x.replace('non- renewable', 'non-renewable') for x in it['o']]
    return out


def err_items(gid, lines):
    out = []
    for ln in lines:
        t = cl(ln)
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if not m:
            continue
        s = re.sub(r'</u>\s*<u>', ' ', m.group(2))
        segs = []

        def rep(mm):
            segs.append(mm.group(2).strip())
            return '<u>%s</u><sup>%s</sup>' % (mm.group(2).strip(), mm.group(1))
        s2 = re.sub(r'\(([A-D])\)\s*<u>(.*?)</u>', rep, s)
        s2 = re.sub(r'<u>([^<]*)</u>(?!<sup>)', r'\1', s2)       # gạch chân thừa (không nhãn)
        s2 = re.sub(r'(</sup>)(?=\w)', r'\1 ', s2)
        segs = [re.sub(r'\s+', ' ', x) for x in segs]
        assert len(segs) == 4, (t, segs)
        out.append({'id': '%s.%d' % (gid, len(out) + 1), 't': 'mcq', 'q': keepu(s2), 'o': segs})
    return out


def P(lines):
    """đoạn văn: nối dòng bắt đầu bằng chữ thường vào dòng trước; bỏ dòng trống"""
    paras = []
    for l in lines:
        t = keepu(cl(l))
        if not t:
            continue
        if paras and t[0].islower():
            paras[-1] += ' ' + t
        else:
            paras.append(t)
    return ''.join('<p>%s</p>' % fixblank_num(p) for p in paras)


def fixblank_num(p):
    p = re.sub(r'\((\d+)\)\s*_{2,}\s*', r'<b>(\1) ______</b> ', p)
    for a, b in [('independence on', 'dependence on'), ('around the global', 'around the globe'), ('lar e number', 'large number'),
                 ('ai m to', 'aim to'), ('pl an', 'plan'), ('coming to lie', 'coming to life'), ('­', '')]:
        p = p.replace(a, b)
    return re.sub(r'\s+([.,?!;:])', r'\1', re.sub(r'\s+', ' ', p)).strip()


def split_pi(lines, expect=1):
    """tách đoạn văn (trước dòng '1. ...') và các câu trắc nghiệm"""
    k = next(i for i, l in enumerate(lines) if re.match(r'^\s*1\.\s', cl(l)) or re.match(r'^\s*1\.\s*$', cl(l)))
    return lines[:k], parse_mcq(lines[k:], expect=expect)


def blankify(s):
    s = re.sub(r'_{3,}', '{_}', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def tf_items(gid, lines, kind='tf'):
    out = []
    for l in lines:
        t = cl(l)
        m = re.match(r'^(\d+)\.\s*(.*?)\s*_*\s*$', t)
        if m:
            out.append({'id': '%s.%d' % (gid, len(out) + 1), 't': kind, 'q': m.group(2).strip()})
    return out


def table_pairs(lines):
    """bảng 'N.' + 'A./B. câu có chỗ trống' -> danh sách câu (A,B từng câu thành 1 item)"""
    out = []
    for l in lines:
        m = re.match(r'^\s*<b>([AB])\.\s*</b>\s*(.*)$', l)
        if m:
            s = m.group(2).replace('⟦', '').replace('⟧', '')
            s = re.sub(r'</?b>', '', s)
            s = re.sub(r'\(([a-z]+)\)', r'<b>(\1)</b>', s)
            out.append(blankify(s))
    return out


def build():
    pages = []
    H = {}
    seq = [('thA', r'PART I\. VOCABULARY'), ('thB', r'A\. PHONETIC'),
           ('ph1', r'Exercise 1: Read the following sentences aloud'),
           ('ph2', r'Exercise 2: Mark the letter A, B, C, or D to indicate the word whose underlined'),
           ('ph3', r'Exercise 3: Mark the letter A, B, C, or D to indicate the word that differs'),
           ('vgB', r'B\. VOCABULARIES AND GRAMMARS'),
           ('vg1', r'Exercise 1: Mark the letter A, B, C, or D to indicate the correct answer'),
           ('vg2', r'Exercise 2: Choose the correct verb form'),
           ('vg3', r'Exercise 3: Mark the letter A.*CLOSEST'), ('vg4', r'Exercise 4: Mark the letter A.*OPPOSITE'),
           ('vg5', r'Exercise 5: Put the verbs'), ('vg6', r'Exercise 6: Put the verbs'), ('vg7', r'Exercise 7'),
           ('vg8', r'indicate the underlined part that needs correction'),
           ('li0', r'A\. LISTENING'), ('li1', r'Exercise 1: Listen and complete'), ('li2', r'Exercise 2: Listen to the recording'),
           ('sp0', r'B\. SPEAKING'), ('sp1', r'Exercise 1: Choose the correct response'),
           ('sp2', r'Exercise 2: Mark the letter A, B, C, or D to indicate the correct response'),
           ('sp3', r'Exercise 3: Complete the conversation'), ('sp4', r'Exercise 4: Choose the correct option'),
           ('re0', r'READING</b>'), ('re1', r'Exercise 1: Read the following passage'), ('re2', r'Exercise 2: Read the following passage'),
           ('re3', r'Exercise 3: Read the passage'), ('re4', r'Exercise 4: Read the passage about green'),
           ('wr0', r'WRITING</b>'), ('wr1', r'An article about the advantages'), ('wr2', r'Exercise 2: Write an article'),
           ('kt0', r'^\[IMG:image6')]
    cur = 1
    for k, pat in seq:
        cur = fnd(pat, cur)
        H[k] = cur
    H['end1'] = SPLIT
    # ---------------- lý thuyết
    theory = theory_html(BR[H['thA'] - 1:H['thB'] - 1], '')

    # ---------------- Phát âm
    ph1_l = [cl(l) for l in rng(H['ph1'] + 1, H['ph2'] - 1) if cl(l)]
    ph1 = [{'id': 'ph1.%d' % i, 't': 'open', 'q': re.sub(r'^\d+\.\s*', '', t)} for i, t in enumerate(ph1_l, 1)]
    note = ('<p class="note"><b>Nối âm (linking):</b> khi từ trước kết thúc bằng <b>phụ âm</b> và từ sau bắt đầu bằng <b>nguyên âm</b>, '
            'ta đọc nối phụ âm đó với nguyên âm (ví dụ <i>of us</i> đọc như <i>o-fus</i>). Hãy đánh dấu (‿) các chỗ nối trong từng câu, '
            'đọc to rồi bấm “Xem đáp án mẫu” để đối chiếu (không chấm điểm).</p>')
    ph2 = parse_mcq(rng(H['ph2'] + 1, H['ph3'] - 1), expect=1)
    ph3 = parse_mcq(rng(H['ph3'] + 1, H['vgB'] - 1), expect=1)
    assert len(items_of(ph2)) == 10 and len(items_of(ph3)) == 10
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'ph1', 'instr': 'Exercise 1: Read the following sentences aloud, and mark (‿) the consonant sounds that link with the vowel sounds.', 'note': note, 'items': ph1},
        {'id': 'ph2', 'instr': 'Exercise 2: Mark the letter A, B, C, or D to indicate the word whose underlined part differs from the other three in pronunciation in each of the following questions.', 'items': mcq('ph2', ph2)},
        {'id': 'ph3', 'instr': 'Exercise 3: Mark the letter A, B, C, or D to indicate the word that differs from the other three in the position of primary stress in each of the following questions.', 'items': mcq('ph3', ph3)},
    ]})

    # ---------------- Từ vựng & ngữ pháp
    vg1 = mcq('vg1', parse_mcq(rng(H['vg1'] + 1, H['vg2'] - 1), expect=1))
    assert len(vg1) == 35, len(vg1)
    vg1[28]['o'] = ['attracts', 'pays', 'gives', 'takes']        # nguồn lặp 'pays' (B và D) -> câu 29: đáp án A không đổi
    vg2 = []
    for l in rng(H['vg2'] + 1, H['vg3'] - 1):
        t = re.sub(r'⟦|⟧', '', l)
        m = re.match(r'^(\d+)\.\s*(.*?)<b>(.*?)</b>\s*/\s*<b>(.*?)</b>\s*(.*)$', t)
        if not m:
            continue
        q = cl('%s ______ %s' % (m.group(2), m.group(5)))
        vg2.append({'id': 'vg2.%d' % (len(vg2) + 1), 't': 'mcq', 'q': q, 'o': [cl(m.group(3)), cl(m.group(4))], 'plain': True})
    assert len(vg2) == 10
    vg3 = mcq('vg3', parse_mcq(rng(H['vg3'] + 1, H['vg4'] - 1), expect=1)); assert len(vg3) == 10
    vg4 = mcq('vg4', parse_mcq(rng(H['vg4'] + 1, H['vg5'] - 1), expect=1)); assert len(vg4) == 10
    vg5 = [{'id': 'vg5.%d' % i, 't': 'fill', 'q': q} for i, q in enumerate(table_pairs(rng(H['vg5'], H['vg6'] - 1)), 1)]
    vg6 = [{'id': 'vg6.%d' % i, 't': 'fill', 'q': q} for i, q in enumerate(table_pairs(rng(H['vg6'], H['vg7'] - 1)), 1)]
    assert len(vg5) == 10 and len(vg6) == 20, (len(vg5), len(vg6))
    # 6.10A: 'What ___ it (look) ___ like?' -> 2 ô
    vg7 = []
    for l in rng(H['vg7'] + 1, H['vg8'] - 1):
        t = cl(l)
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            s = re.sub(r'\(([a-z]+)\)', r'<b>(\1)</b>', blankify(m.group(2)))
            vg7.append({'id': 'vg7.%d' % (len(vg7) + 1), 't': 'fill', 'q': s})
    assert len(vg7) == 10
    # lỗi sai: dùng bản nửa sau (gạch chân sạch hơn)
    e0 = fnd(r'indicate the underlined part that needs correction', SPLIT)
    vg8 = err_items('vg8', rng(e0 + 1, e0 + 10)); assert len(vg8) == 10
    pages.append({'id': 'tu-vung-ngu-phap', 'title': 'Từ vựng & Ngữ pháp', 'mode': 'practice', 'groups': [
        {'id': 'vg1', 'instr': 'Exercise 1: Mark the letter A, B, C, or D to indicate the correct answer to each of the following questions.', 'items': vg1},
        {'id': 'vg2', 'instr': 'Exercise 2: Choose the correct verb form.', 'items': vg2},
        {'id': 'vg3', 'instr': 'Exercise 3: Mark the letter A, B, C, or D to indicate the word(s) CLOSEST in meaning to the underlined word(s) in each of the following questions.', 'items': vg3},
        {'id': 'vg4', 'instr': 'Exercise 4: Mark the letter A, B, C, or D to indicate the word(s) OPPOSITE in meaning to the underlined word(s) in each of the following questions.', 'items': vg4},
        {'id': 'vg5', 'instr': 'Exercise 5: Put the verbs in brackets into the present simple or the present continuous. (Mỗi cặp A/B: cùng một động từ nhưng nghĩa khác nhau.)', 'items': vg5},
        {'id': 'vg6', 'instr': 'Exercise 6: Put the verbs in brackets into the present simple or the present continuous.', 'items': vg6},
        {'id': 'vg7', 'instr': 'Exercise 7: Put the verbs in brackets into the present simple or the present continuous.', 'items': vg7},
        {'id': 'vg8', 'instr': 'Exercise 8: Mark the letter A, B, C, or D to indicate the underlined part that needs correction in each of the following questions.', 'items': vg8},
    ]})

    # ---------------- Nghe
    sl = [cl(l) for l in rng(H['li1'] + 1, H['li2'] - 1) if cl(l)]
    summ = ''.join('<p>%s</p>' % re.sub(r'\((\d)\)\s*_+', r'<b>(\1) ______</b>', t) for t in sl)
    li1 = [{'id': 'li1.%d' % i, 't': 'fill', 'q': 'Blank (%d): {_}' % i} for i in range(1, 6)]
    li2 = mcq('li2', parse_mcq(rng(H['li2'] + 1, H['sp0'] - 1), expect=1))
    assert len(li2) == 5
    pages.append({'id': 'nghe', 'title': 'Nghe', 'mode': 'practice', 'audio': 'bt_nghe.mp3', 'groups': [
        {'id': 'li1', 'instr': 'Exercise 1: Listen and complete the summaries of the two viewpoints.', 'passage': summ, 'items': li1},
        {'id': 'li2', 'instr': 'Exercise 2: Listen to the recording and choose the correct answer A, B, C or D.', 'items': li2},
    ]})

    # ---------------- Nói
    sp1 = []
    cur_n, qa, opts = None, '', []
    rows = {}
    for l in rng(H['sp1'] + 1, H['sp2'] - 1):
        mn = re.match(r'^\s*<b>(\d+)\.</b>\s*$', l)
        if mn:
            cur_n = int(mn.group(1)); rows.setdefault(cur_n, {'q': '', 'o': []}); continue
        ma = re.match(r'^\s*<b>A:\s*</b>\s*(.*)$', l)
        if ma and cur_n:
            rows[cur_n]['q'] = re.sub(r'(\?)\s*\.$', r'\1', cl(ma.group(1))); continue
        mo = re.match(r'^\s*([ab])/\s*(.*)$', cl(l))
        if mo and cur_n:
            rows[cur_n]['o'].append(mo.group(2).strip())
    assert sorted(rows) == list(range(1, 11)), sorted(rows)
    for n in range(1, 11):
        o = rows[n]['o']; assert len(o) == 2
        if n == 8:
            o[0] = "They're flexible with fewer hours in the future."     # nguồn: '... fewer hours the future?'
        sp1.append({'id': 'sp1.%d' % n, 't': 'mcq', 'q': '<b>A:</b> %s<br><b>B:</b> ______' % rows[n]['q'], 'o': o})
    sp2 = mcq('sp2', parse_mcq(rng(H['sp2'] + 1, H['sp3'] - 1), expect=1)); assert len(sp2) == 10
    resp = []
    for l in rng(H['sp3'] + 1, H['sp3'] + 8):
        m = re.match(r'^<b>([A-F])\.\s*</b>\s*(.*)$', l)
        if m:
            resp.append(cl(m.group(2)))
    assert len(resp) == 6, resp
    dl = [cl(l) for l in rng(H['sp3'] + 1, H['sp4'] - 1)]
    dl = [t for t in dl if t and t not in ('<TABLE>', '</TABLE>', '<ROW>', '<CELL>')]
    conv, spk = '', None
    for t in dl:
        if re.match(r'^[A-F]\.\s', t) and not spk:
            continue
        ms = re.match(r'^(Phong|Chi):$', t)
        if ms:
            spk = ms.group(1); continue
        if spk:
            conv += '<p><b>%s:</b> %s</p>' % (spk, re.sub(r'\((\d)\)\s*_+', r'<b>(\1) ______</b>', t)); spk = None
    assert conv.count('______') == 5, conv
    bank_html = '<div class="note"><b>Responses:</b><ol type="A">%s</ol></div>' % ''.join('<li>%s</li>' % r for r in resp)
    sp3 = [{'id': 'sp3.%d' % i, 't': 'mcq', 'q': 'Chỗ trống (%d) – chọn A–F' % i, 'o': list('ABCDEF'), 'plain': True} for i in range(1, 6)]
    sp4 = []
    for l in rng(H['sp4'], H['re0'] - 1):
        mm = re.match(r'^\s*(\d+)\.\s*$', l)
        mm2 = re.search(r'<b>([^<]*/[^<]*)</b>', l)
        if mm2 is None and not re.search(r'<b>[^<]*/', l):
            continue
        s = l.replace('⟦', '').replace('⟧', '')
        s = re.sub(r'</b>\s*<b>', '', s)
        mb = re.search(r'<b>(.*?/.*?)</b>', s)
        o = [x.strip() for x in mb.group(1).split('/')]
        assert len(o) == 3, (l, o)
        q = fixblank(cl(s[:mb.start()] + ' ______ ' + s[mb.end():]))
        sp4.append({'id': 'sp4.%d' % (len(sp4) + 1), 't': 'mcq', 'q': q, 'o': o, 'plain': True})
    assert len(sp4) == 11, len(sp4)
    # sửa lỗi gõ trong nguồn (câu 2 'name of t painter', câu 3, câu 5, câu 6, câu 4)
    for it in sp4:
        if not re.search(r'[.?!]$', it['q']):
            it['q'] += '.'
        it['q'] = (it['q'].replace('name of t painter', 'name of the painter').replace('What about t bedroom', 'What about the bedroom')
                   .replace('three hour', 'three hours').replace("She always prefers yours", 'She always prefers yours.'))
    pages.append({'id': 'noi', 'title': 'Nói (hội thoại)', 'mode': 'practice', 'groups': [
        {'id': 'sp1', 'instr': 'Exercise 1: Choose the correct response. Then practise the short exchanges in pairs.', 'items': sp1},
        {'id': 'sp2', 'instr': 'Exercise 2: Mark the letter A, B, C, or D to indicate the correct response to each of the following exchanges.', 'items': sp2},
        {'id': 'sp3', 'instr': "Exercise 3: Complete the conversation about the world's first carbon-neutral city, using the responses (A–F) given. There is one extra response. Then practise the dialogue with your partner.", 'passage': bank_html + conv, 'items': sp3},
        {'id': 'sp4', 'instr': 'Exercise 4: Choose the correct option to complete the sentences.', 'items': sp4},
    ]})

    # ---------------- Đọc
    t1 = fnd(r'<b>World Car free Day</b>', H['re1']); t2 = fnd(r'A future in the dark', H['re1'])
    pa, ev = split_pi(rng(t1 + 1, t2 - 1)); re1a_items = mcq('re1a', ev)
    pb, ev = split_pi(rng(t2 + 1, H['re2'] - 1)); re1b_items = mcq('re1b', ev)
    for g in (re1a_items, re1b_items):
        for i, it in enumerate(g, 1):
            it['q'] = 'Blank (%d)' % i
        assert len(g) == 5
    re1a = {'id': 're1a', 'instr': 'Exercise 1a: Read the following passage and mark the letter A, B, C, or D to choose the word or phrase that best fits each of the numbered blanks from 1 to 5.',
            'passage': '<h4>World Car free Day</h4>' + P(pa), 'items': re1a_items}
    re1b = {'id': 're1b', 'instr': 'Exercise 1b: Read the following passage and mark the letter A, B, C, or D to choose the word or phrase that best fits each of the numbered blanks from 1 to 5.',
            'passage': '<h4>A future in the dark</h4>' + P(pb), 'items': re1b_items}
    t3 = fnd(r'<b>2026</b>', H['re2']); t4 = fnd(r'A NEW CAPITAL', H['re2'])
    pc, ev = split_pi(rng(t3 + 1, t4 - 1)); re2a_items = mcq('re2a', ev); assert len(re2a_items) == 5
    pd, ev = split_pi(rng(t4 + 1, H['re3'] - 1)); re2b_items = mcq('re2b', ev); assert len(re2b_items) == 5
    re2a = {'id': 're2a', 'instr': 'Exercise 2a: Read the following passage and mark the letter A, B, C or D to indicate the correct answer to each of the questions from 1 to 5.',
            'passage': '<h4>2026</h4>' + P(pc), 'items': re2a_items}
    re2b = {'id': 're2b', 'instr': 'Exercise 2b: Read the following passage and mark the letter A, B, C or D to indicate the correct answer to each of the questions from 1 to 5.',
            'passage': '<h4>A NEW CAPITAL</h4>' + P(pd), 'items': re2b_items}
    l3 = rng(H['re3'] + 1, H['re4'] - 1)
    k3 = next(i for i, l in enumerate(l3) if re.match(r'^\s*1\.\s', cl(l)))
    re3 = {'id': 're3', 'instr': 'Exercise 3: Read the passage, and then decide whether the statements are true (T) or false (F).', 'passage': P(l3[:k3]),
           'items': tf_items('re3', l3[k3:])}
    assert len(re3['items']) == 8
    l4 = rng(H['re4'] + 1, H['wr0'] - 1)
    k4 = next(i for i, l in enumerate(l4) if re.match(r'^\s*1\.\s', cl(l)))
    q4 = [re.sub(r'^\d+\.\s*', '', cl(l)) for l in l4[k4:] if re.match(r'^\d+\.', cl(l))]
    re4 = {'id': 're4', 'instr': 'Exercise 4: Read the passage about green cities, and then answer the questions (tự luận – đối chiếu đáp án mẫu).',
           'passage': P(l4[:k4]), 'items': [{'id': 're4.%d' % i, 't': 'open', 'q': q} for i, q in enumerate(q4, 1)]}
    assert len(re4['items']) == 6
    pages.append({'id': 'doc', 'title': 'Đọc hiểu', 'mode': 'practice', 'groups': [re1a, re1b, re2a, re2b, re3, re4]})

    # ---------------- Viết
    wl = [cl(l) for l in rng(H['wr1'] + 1, H['wr2'] - 1) if cl(l)]
    wr1 = []
    for t in wl:
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            q = '<b>Từ gợi ý:</b> ' + m.group(2).replace('citizens I such as', 'citizens / such as') + '<br>Câu hoàn chỉnh: {_}'
            if m.group(1) == '1':
                q = '<i>There are some advantages of living in a smart city.</i><br>' + q
            if m.group(1) == '5':
                q = '<i>However, there are some disadvantages we have to overcome when we live in a smart city.</i><br>' + q
            wr1.append({'id': 'wr1.%s' % m.group(1), 't': 'fill', 'q': q, 'long': True})
    assert len(wr1) == 7
    pages.append({'id': 'viet', 'title': 'Viết', 'mode': 'practice', 'groups': [
        {'id': 'wr1', 'instr': 'Exercise 1: Write an article about the advantages and disadvantages of living in a smart city, using the words given (viết thành câu hoàn chỉnh).', 'items': wr1},
        {'id': 'wr2', 'instr': 'Exercise 2: Write an article (120–150 words) about other advantages and disadvantages of living in a smart city (tự luận – xem bài mẫu).',
         'items': [{'id': 'wr2.1', 't': 'open', 'q': 'Write an article (120–150 words) about other advantages and disadvantages of living in a smart city.'}]},
    ]})

    # ---------------- Kiểm tra 50 câu
    a1 = fnd(r'Fill in each blank in the passage', H['kt0'])
    ev = parse_mcq(rng(H['kt0'] + 1, a1 - 1), expect=1)
    g = groups_from_events('kt', ev)
    for gg in g:
        for it in gg['items']:
            it.pop('_n', None)
            it['q'] = fixblank(it['q'])
    assert [len(x['items']) for x in g] == [3, 2, 10], [len(x['items']) for x in g]
    for it in g[2]['items']:
        it['q'] = it['q'].replace('Your English is improving. It is getting ______', 'Your English is improving. It is getting ______')
    groups = g
    cz = []
    for l in rng(a1 + 1, a1 + 12):
        if re.match(r'^<b>Mark the letter', l):
            break
        cz.append(cl(l))
    cz_txt = ''.join('<p>%s</p>' % re.sub(r'\((\d\d)\)\s*_+', r'<b>(\1) ______</b>', t) for t in cz[1:] if t and not t.startswith('Mark the letter'))
    cz_txt = cz_txt.replace('<p>Panasonic Works with Denver to Improve Residents\' Lives</p>', '<h4>Panasonic Works with Denver to Improve Residents\' Lives</h4>')
    cz_items = [{'id': 'kt.%d' % n, 't': 'fill', 'q': 'Blank (%d): {_}' % n} for n in range(16, 22)]
    bank = sorted(['network', 'urban', 'efficient', 'energy', 'enjoyable', 'space', 'connect', 'convenience'])
    groups.append({'id': 'kt4', 'instr': 'Fill in each blank in the passage with the correct word below. There are TWO extra words.', 'bank': bank, 'passage': cz_txt, 'items': cz_items})
    b2 = fnd(r'indicate the word\(s\) CLOSEST', a1)
    b3 = fnd(r'Complete the sentences with the correct form', b2)
    ev = parse_mcq(rng(b2, b3 - 1), expect=22)
    g2 = groups_from_events('kt', ev)
    for k, gg in enumerate(g2, 5):
        gg['id'] = 'kt%d' % k
        for it in gg['items']:
            it.pop('_n', None)
            it['q'] = fixblank(it['q'])
    assert [len(x['items']) for x in g2] == [2, 2, 5, 5, 5], [len(x['items']) for x in g2]
    # nối nhóm đoạn văn: groups_from_events đã gắn passage
    groups += g2
    vb = []
    for l in rng(b3 + 1, b3 + 5):
        t = cl(l)
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        assert m, t
        s = re.sub(r'\(([^()]+)\)', r'<b>(\1)</b>', blankify(m.group(2)))
        vb.append({'id': 'kt.%s' % m.group(1), 't': 'fill', 'q': s})
    groups.append({'id': 'kt10', 'instr': 'Complete the sentences with the correct form of the verbs in brackets (present simple or present continuous).', 'items': vb})
    e0 = fnd(r'Write complete sentences about advantages', b3)
    cue = []
    lines = rng(e0 + 1, e0 + 40)
    i = 0
    while i < len(lines):
        t = cl(lines[i])
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m and int(m.group(1)) >= 46:
            cue.append({'id': 'kt.%s' % m.group(1), 't': 'fill', 'long': True,
                        'q': '<b>%s</b><br>%s<br>Viết thành câu hoàn chỉnh: {_}' % (m.group(2), cl(lines[i + 1]))})
            i += 2
            continue
        i += 1
    assert len(cue) == 5, len(cue)
    groups.append({'id': 'kt11', 'instr': 'Write complete sentences about advantages of living in a smart city, using the words/phrases given in their correct forms. You can add some more necessary words, but you have to use all the words given.',
                   'passage': '<h4>Advantages of Living in a Smart City</h4>', 'items': cue})
    for gg in groups:
        if gg.get('passage'):
            ps = gg['passage']
            ps = re.sub(r'(?<!<b>)\((\d\d)\)\s*_+', r'<b>(\1) ______</b>', ps)
            for a, b in [('bot archaeological', 'both archaeological'), ('land a created', 'land and created'), ('pl an', 'plan'),
                         ('<p>MARRAKECH</p>', '<h4>MARRAKECH</h4>'), ('<p>Predictions about the Cities of the Future</p>', '<h4>Predictions about the Cities of the Future</h4>')]:
                ps = ps.replace(a, b)
            gg['passage'] = ps
        if gg['id'] in ('kt8',):
            for it in gg['items']:
                it['q'] = 'Blank (%s)' % it['id'].split('.')[1]
    for gg in groups:
        for it in gg['items']:
            if it['id'] == 'kt.50':
                it['q'] = it['q'].replace('<b>job opportunities</b>', '<b>Job opportunities</b>')
            it['q'] = it['q'].replace('citizens I such as', 'citizens / such as')
    pages.append({'id': 'kiem-tra', 'title': 'Bài kiểm tra Unit 3 (50 câu)', 'mode': 'test', 'minutes': 50, 'groups': groups})
    return {'id': 'lop11-u3-botro', 'title': 'Unit 3 – Cities of the future: Bài tập bổ trợ', 'grade': 11, 'unit': 3, 'theory': theory, 'pages': pages}


if __name__ == '__main__':
    b = build()
    dump(os.path.join(ROOT, 'units/lop11_u3_botro.py'), 'SET', b)
    tot = 0
    for p in b['pages']:
        n = sum(len(g['items']) for g in p['groups']); tot += n
        print(p['id'], n, [(g['id'], len(g['items'])) for g in p['groups']])
    print('TOTAL', tot)
