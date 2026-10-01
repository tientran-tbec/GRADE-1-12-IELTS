"""Chuyển đổi 1 lần: Word Lớp 10 Unit 1 (Bài tập bổ trợ) -> units/lop10_u1_botro.py (khung câu hỏi).
Nguồn src/l10u1/bt_c.txt: nửa đầu (đến dòng 'ĐÁP ÁN') = đề; nửa sau = khoá (⟦…⟧ tô màu).
Đáp án + giải thích: units/lop10_u1_botro_dapan.py (đối chiếu khoá Word và tự giải độc lập)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import parse_mcq, cl
import gen_units as G
from gen_units import mk_mcq, keepu, dump

ROOT = G.ROOT
RAW = open(os.path.join(ROOT, 'src/l10u1/bt_c.txt'), encoding='utf8').read().split('\n')
END = next(i for i, l in enumerate(RAW) if 'ĐÁP ÁN' in l)
BR = [l.replace('C </b>were sleeping', 'C. </b>were sleeping').replace('Question 20:</b>____', 'Question 20:</b> ____') for l in RAW[:END]]   # nguồn thiếu dấu chấm sau C


def fnd(pat, start=1):
    for i in range(start - 1, len(BR)):
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


def mcq(gid, lines, expect=1):
    its = items_of(parse_mcq(lines, expect=expect))
    out = mk_mcq(gid, its)
    for it in out:
        it['q'] = fixblank(it['q'])
        assert len(it['o']) == 4, (it, )
    return out


# ------------------------------------------------------------------ lý thuyết
def theory():
    a = fnd(r'A\. VOCABULARY')
    vocab = []
    for l in rng(a + 1, fnd(r'B\. GRAMMAR') - 1):
        t = l.replace('⟦', '').replace('⟧', '')
        m = re.match(r'^(.*?)\s*\(([a-z,]+)\)\s*(/[^/]+/)\s*:\s*(.*)$', t.strip())
        assert m, t
        w, ty, ipa, vi = m.groups()
        if w == 'Value':
            ty = 'n'                        # nguồn ghi (adj); khoá ghi (n)
        vocab.append((w, ty, ipa, vi.strip()))
    assert len(vocab) == 45, len(vocab)
    h = '<p><b>A. VOCABULARY</b> (Từ vựng)</p><table class="th"><tr><th>Word</th><th>Type</th><th>Pronunciation</th><th>Meaning</th></tr>'
    for w, ty, ipa, vi in vocab:
        h += '<tr><td>%s</td><td>(%s)</td><td>%s</td><td>%s</td></tr>' % (w, ty, ipa, vi)
    h += '</table>'
    h += '<p><b>B. GRAMMAR</b> (Ngữ pháp)</p>'
    h += '<p><b>I. PRESENT SIMPLE (Thì hiện tại đơn)</b></p>'
    h += ('<p><b>1. Công thức</b></p><table class="th"><tr><th>Thể</th><th>Cấu trúc</th></tr>'
          '<tr><td>Khẳng định</td><td><b>S + V1 / V-s/es</b></td></tr>'
          '<tr><td>Phủ định</td><td><b>S + do not (don’t) / does not (doesn’t) + V0</b></td></tr>'
          '<tr><td>Nghi vấn</td><td><b>(Wh-) + do (not) / does (not) + S + V0 ?</b></td></tr></table>')
    h += ('<p><u>Cách thêm “s/es” cho động từ:</u></p>'
          '<p>- Động từ kết thúc bằng <b>sh, ch, ss, o, x, z</b> thì thêm “es”. Vd: wash – washes, go – goes, watch – watches, miss – misses, mix – mixes, buzz – buzzes…</p>'
          '<p>- Động từ tận cùng là phụ âm + “y”: đổi “y” thành “i” rồi thêm “es”. Vd: study – studies, fly – flies, cry – cries… <b>Lưu ý:</b> play – plays, pay – pays (nguyên âm + “y”).</p>'
          '<p>- Riêng động từ “have” biến đổi thành “has”.</p>')
    h += ('<p><b>2. Cách sử dụng:</b> diễn tả hành động lặp lại theo <b>thói quen</b>, sự thật hiển nhiên.</p>'
          '<p><b>Dấu hiệu:</b> always, usually, often, sometimes, seldom, rarely, never, every day, once a day/week/month…, twice a day/week/month…, 3 times a day/week/month…</p>'
          '<p><b>Ví dụ:</b> a. My brother <mark>goes</mark> (go) to school every day. b. He <mark>is</mark> (be) often tired. c. We usually <mark>go</mark> (go) to the cinema twice a week. '
          'd. My mom <mark>cooks</mark> (cook) once a day. e. They always <mark>prepare</mark> (prepare) dinner in the evening.</p>')
    h += '<p><b>II. PRESENT CONTINUOUS (Thì hiện tại tiếp diễn)</b></p>'
    h += ('<p><b>1. Công thức</b></p><table class="th"><tr><th>Thể</th><th>Cấu trúc</th></tr>'
          '<tr><td>Khẳng định</td><td><b>S + am/is/are + V-ing</b></td></tr>'
          '<tr><td>Phủ định</td><td><b>S + am/is/are + not + V-ing</b></td></tr>'
          '<tr><td>Nghi vấn</td><td><b>(Wh-) + am/is/are + (not) + S + V-ing ?</b></td></tr></table>')
    h += ('<p><u>Cách thêm đuôi “-ing” cho động từ:</u></p>'
          '<p>- Động từ tận cùng là “e”: bỏ “e” trước khi thêm “-ing”. Vd: have – having, write – writing…</p>'
          '<p>- Động từ tận cùng là “ee”: giữ nguyên “ee”. Vd: see – seeing, agree – agreeing…</p>'
          '<p>- Động từ 1 âm tiết, hoặc 2 âm tiết có trọng âm rơi vào âm 2 (kết thúc bằng 1 nguyên âm + 1 phụ âm): gấp đôi phụ âm cuối. Vd: sit – sitting, prefer – preferring, swim – swimming, begin – beginning… <b>Lưu ý:</b> flow – flowing.</p>'
          '<p>- die, lie, tie… : die – dying, lie – lying, tie – tying…</p>')
    h += ('<p><b>2. Cách sử dụng:</b> diễn tả hành động <b>đang diễn ra</b> ở hiện tại, ngay lúc nói.</p>'
          '<p><b>Dấu hiệu:</b> now, at the moment, at present, Look!, Listen!, Be careful!, Be quiet!, today, this term, this month…</p>'
          '<p><b>Lưu ý:</b> KHÔNG dùng thì hiện tại tiếp diễn với động từ chỉ trạng thái (stative verbs): like, love, hate, need, want, know, agree, understand, feel, seem, smell, hear, see…</p>'
          '<p><b>Ví dụ:</b> a. I <mark>am waiting</mark> (wait) for the bus at the moment. b. Where <mark>are</mark> you <mark>going</mark> (go) now? c. Listen! Someone <mark>is singing</mark> (sing). '
          'd. I <mark>am facing</mark> (face) difficulties in learning English this term. e. She <mark>is learning</mark> (learn) English at present.</p>')
    return h


def pquote(s):
    return s


def build():
    pages = []
    H = {}
    seq = [('e1', r'^<b>E1:'), ('e2', r'^<b>E2:'), ('e3', r'^<b>E3:'), ('e4', r'^<b>E4:'), ('e5', r'^<b>E5:'),
           ('e6', r'^<b>E6:'), ('t2', r'^<b>Task 2:'), ('e7', r'^<b>E7:'), ('e8', r'^<b>E8:'), ('e9', r'^<b>E9:'),
           ('e10', r'^<b>E10:'), ('e11', r'^<b>E11:'), ('e12', r'^<b>E12:'), ('e13', r'^<b>E13:')]
    cur = 1
    for k, pat in seq:
        cur = fnd(pat, cur)
        H[k] = cur
    H['t1'] = fnd(r'^<b>Task 1:', H['e6'])
    H['end'] = len(BR) + 1

    # ---- phát âm
    ph1 = mcq('ph1', rng(H['e1'] + 1, H['e2'] - 1)); assert len(ph1) == 7
    ph2 = mcq('ph2', rng(H['e2'] + 1, fnd(r'II-VOCABULARY') - 1)); assert len(ph2) == 4
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'ph1', 'instr': 'E1: Mark the letter A, B, C or D to indicate the word whose underlined part differs from the other three in pronunciation in each of the following questions.', 'items': ph1},
        {'id': 'ph2', 'instr': 'E2: Mark the letter A, B, C, or D to indicate the word that differs from the other three in the position of the primary stress in each of the following questions.', 'items': ph2}]})

    # ---- từ vựng & ngữ pháp
    l3 = [l for l in rng(H['e3'] + 1, H['e4'] - 1)]
    vg1 = mcq('vg1', l3)
    assert len(vg1) == 35, len(vg1)                  # nguồn nhảy số 33 -> 35; đánh số lại 1..35
    fix = {4: 'My mother ______ the responsibility for running the household.',
           24: 'Do you have to ______ the rubbish out?'}
    for n, q in fix.items():
        vg1[n - 1]['q'] = q
    vg1[14]['o'][1] = 'left'                         # 'leff'
    vg1[19]['q'] = vg1[19]['q']                      # giữ nguyên
    vg1[20]['q'] = fixblank(re.sub(r'<u>\s*______\s*</u>', '______', vg1[20]['q']))
    vg2 = mcq('vg2', rng(H['e4'] + 1, H['e5'] - 1)); print(len(vg2), [x['id'] for x in vg2][-3:]); assert len(vg2) == 35
    vg2[4]['o'][3] = vg2[4]['o'][3].rstrip('.')
    vg2[2]['q'] = "I’m busy at the moment, ______ on the computer."
    vg2[3]['q'] = "Don’t bother me while I ______."
    vg3 = []
    for l in rng(H['e5'] + 1, H['e6'] - 1):
        t = cl(l)
        m = re.match(r'^Question (\d+):\s*(.*?)\s*\(\s*([A-Z]+)\s*\)\s*$', t)
        if m:
            q = fixblank(m.group(2)).replace('tae care', 'take care').replace('______', '{_}')
            vg3.append({'id': 'vg3.%d' % len(vg3 + [0]), 't': 'fill', 'q': q, 'hint': m.group(3)})
    assert len(vg3) == 5
    pages.append({'id': 'tu-vung-ngu-phap', 'title': 'Từ vựng & Ngữ pháp', 'mode': 'practice', 'groups': [
        {'id': 'vg1', 'instr': 'E3: Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.', 'items': vg1},
        {'id': 'vg2', 'instr': 'E4: Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.', 'items': vg2},
        {'id': 'vg3', 'instr': 'E5: Complete the following sentences with the correct forms of the words in capitals.', 'items': vg3}]})

    # ---- nghe
    stm = []
    for l in rng(H['t1'] + 1, fnd(r'IMG:image1', H['t1'])):
        m = re.match(r'^\s*<b>(\d)\.\s*</b>\s*(.*)$', l)
        if m:
            stm.append({'id': 'li1.%s' % m.group(1), 't': 'tf', 'q': keepu(cl(m.group(2)))})
    assert len(stm) == 5
    qs = []
    for l in rng(H['t2'] + 1, H['e7'] - 1):
        m = re.match(r'^(\d)\.\s*(.*\?)\s*$', cl(l))
        if m:
            qs.append({'id': 'li2.%d' % (len(qs) + 1), 't': 'open', 'q': m.group(2)})
    assert len(qs) == 3
    pages.append({'id': 'nghe', 'title': 'Nghe', 'mode': 'practice', 'audio': 'botro_nghe.mp3', 'groups': [
        {'id': 'li1', 'instr': 'E6 – Task 1: Listen to a family expert talking about how the roles of men and women in families have changed. Decide whether the following statements are true (T) or false (F).', 'items': stm},
        {'id': 'li2', 'instr': 'E6 – Task 2: Answer the questions (tự luận – đối chiếu đáp án mẫu).', 'items': qs}]})

    # ---- nói
    sp1 = []
    L = rng(H['e7'] + 1, H['e8'] - 1)
    i = 0
    while i < len(L):
        m = re.match(r'^<b>Question (\d):</b>\s*<b>Lan:</b>\s*(.*)$', L[i])
        if m:
            nam = cl(L[i + 1]); nam = re.sub(r'^Nam:\s*', '', nam)
            o = parse_mcq([L[i + 2]], expect=1)
            opts = split_opts_line(L[i + 2])
            assert len(opts) == 4, L[i + 2]
            sp1.append({'id': 'sp1.%s' % m.group(1), 't': 'mcq',
                        'q': '<b>Lan:</b> %s<br><b>Nam:</b> %s' % (cl(m.group(2)), fixblank(nam)), 'o': opts})
            i += 3
        else:
            i += 1
    assert len(sp1) == 4
    sp2 = [{'id': 'sp2.1', 't': 'open', 'q': 'Talk about why children should or should not do housework.'}]
    pages.append({'id': 'noi', 'title': 'Nói (hội thoại)', 'mode': 'practice', 'groups': [
        {'id': 'sp1', 'instr': 'E7: Complete the conversations by circling the best answers. Then practise reading them.', 'items': sp1},
        {'id': 'sp2', 'instr': 'E8: Talk about why children should or should not do housework. (nói/viết – đối chiếu bài mẫu)', 'items': sp2}]})

    # ---- đọc
    def para(lines):
        out = []
        for l in lines:
            t = keepu(cl(l))
            if t:
                t = re.sub(r'\((\d+)\)\s*_+', r'<b>(\1) ______</b>', t)
                out.append('<p>%s</p>' % t)
        return ''.join(out)
    k9 = fnd(r'^<b>Question 1:</b>', H['e9'])
    p9 = para(rng(H['e9'] + 1, k9 - 1)).replace('hours. which leads', 'hours, which leads')
    re1 = mcq('re1', rng(k9, H['e10'] - 1)); assert len(re1) == 13
    for i, it in enumerate(re1, 1):
        it['q'] = 'Blank (%d)' % i
    k10 = fnd(r'^<b>Question 1:</b>', H['e10'])
    p10 = para(rng(H['e10'] + 1, k10 - 1)).replace('same extended family includes', 'same extended family, which includes')
    re2 = mcq('re2', rng(k10, H['e11'] - 1)); assert len(re2) == 5
    k11 = fnd(r'^<b>Question 1:</b>', H['e11'])
    lines11 = rng(H['e11'] + 1, k11 - 1)
    p11 = '<h4>%s</h4>' % cl(lines11[0]) + para(lines11[1:])
    re3 = mcq('re3', rng(k11, H['e12'] - 2 if False else fnd(r'V-WRITING') - 1)); assert len(re3) == 5
    for g in (re2, re3):
        for it in g:
            q = it['q']
            q = re.sub(r'\s*\.?$', '', q)
            it['q'] = q + ' ______.'
    re2[0]['o'][0] = 'in many industrialized countries'
    re3[0]['o'][0] = 'to have an opportunity to share their daily activities'
    pages.append({'id': 'doc', 'title': 'Đọc hiểu', 'mode': 'practice', 'groups': [
        {'id': 're1', 'instr': 'E9: Read the following passage and mark the letter A, B, C, or D to indicate the correct word or phrase that best fits each of the numbered blanks.', 'passage': p9, 'items': re1},
        {'id': 're2', 'instr': 'E10: Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each of the questions.', 'passage': p10, 'items': re2},
        {'id': 're3', 'instr': 'E11: Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each of the questions.', 'passage': p11, 'items': re3}]})

    # ---- viết
    wr1 = []
    for l in rng(H['e12'] + 1, H['e13'] - 1):
        m = re.match(r'^Question (\d):\s*(.*?)\s*$', cl(l))
        if m:
            wr1.append({'id': 'wr1.%s' % m.group(1), 't': 'fill', 'long': True,
                        'q': '<b>Từ gợi ý:</b> %s<br>Câu hoàn chỉnh: {_}' % m.group(2).strip()})
    assert len(wr1) == 8
    cues = ''.join('<li>%s</li>' % re.sub(r'^\d\.\s*', '', cl(l)) for l in rng(H['e13'] + 1, H['end'] - 1) if cl(l))
    wr2 = [{'id': 'wr2.1', 't': 'open', 'q': 'Write a paragraph (120 – 150 words) about one of your family routines. Use the following questions as cues:<ol>%s</ol>' % cues}]
    pages.append({'id': 'viet', 'title': 'Viết', 'mode': 'practice', 'groups': [
        {'id': 'wr1', 'instr': 'E12: Use the verbs in their correct forms and add some words where necessary to make meaningful sentences.', 'items': wr1},
        {'id': 'wr2', 'instr': 'E13: Write a paragraph (120 – 150 words) about one of your family routines. (tự luận – xem bài mẫu)', 'items': wr2}]})
    return {'id': 'lop10-u1-botro', 'title': 'Unit 1 – Family life: Bài tập bổ trợ', 'grade': 10, 'unit': 1, 'theory': theory(), 'pages': pages}


def split_opts_line(line):
    t = cl(line)
    parts = re.split(r'(?:^|\s)([A-D])\.\s*', t)
    return [parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)]


if __name__ == '__main__':
    b = build()
    dump(os.path.join(ROOT, 'units/lop10_u1_botro.py'), 'SET', b)
    tot = 0
    for p in b['pages']:
        n = sum(len(g['items']) for g in p['groups']); tot += n
        print(p['id'], n, [(g['id'], len(g['items'])) for g in p['groups']])
    print('TOTAL', tot)
