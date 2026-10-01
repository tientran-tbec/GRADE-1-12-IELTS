"""Chuyển đổi 1 lần: Word Lớp 10 Unit 2 (Bài tập bổ trợ) -> units/lop10_u2_botro.py (khung câu hỏi).
Nguồn src/l10u2/bt_c.txt: nửa đầu (đến dòng 'ĐÁP ÁN') = đề; nửa sau = khoá (⟦…⟧ tô màu).
Đáp án + giải thích: units/lop10_u2_botro_dapan.py (đối chiếu khoá Word và tự giải độc lập)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import parse_mcq, cl
import gen_units as G
from gen_units import mk_mcq, keepu, dump

ROOT = G.ROOT
RAW = open(os.path.join(ROOT, 'src/l10u2/bt_c.txt'), encoding='utf8').read().split('\n')
END = next(i for i, l in enumerate(RAW) if 'ĐÁP ÁN' in l)
BR = RAW[:END]


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
    s = s.replace('‘', '’')
    s = re.sub(r'\s*_{3,}\s*', ' ______ ', s)
    s = re.sub(r'\s+([.,?!;:])', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def mcq(gid, lines, expect=1):
    its = items_of(parse_mcq(lines, expect=expect))
    out = mk_mcq(gid, its)
    for it in out:
        it['q'] = fixblank(it['q'])
        it['o'] = [x.replace('‘', '’').strip() for x in it['o']]
        assert len(it['o']) == 4, it
    return out


# ------------------------------------------------------------------ lý thuyết
IPA_FIX = {'Attend': '/əˈtend/', 'Polluted': '/pəˈluːtɪd/', 'Turn off': '/tɜːn ɒf/'}


def theory():
    a = fnd(r'A\. VOCABULARY')
    b = fnd(r'B\. GRAMMAR')
    L = [cl(l) for l in rng(a + 1, b - 1)]
    L = [l for l in L if l]
    L = L[4:]                                    # bỏ tiêu đề cột
    assert len(L) == 88 * 4, len(L)
    vocab = []
    for i in range(0, len(L), 4):
        w = re.sub(r'^\d+\.\s*', '', L[i]).strip()
        ty = L[i + 1].strip('()')
        ipa = L[i + 2].strip()
        vi = L[i + 3].strip()
        ipa = IPA_FIX.get(w, ipa)
        vocab.append((w, ty, ipa, vi))
    h = '<p><b>A. VOCABULARY</b> (Từ vựng)</p><table class="th"><tr><th>Word</th><th>Type</th><th>Pronunciation</th><th>Meaning</th></tr>'
    for w, ty, ipa, vi in vocab:
        h += '<tr><td>%s</td><td>(%s)</td><td>%s</td><td>%s</td></tr>' % (w, ty, ipa, vi)
    h += '</table>'
    h += '<p><b>B. GRAMMAR</b> (Ngữ pháp)</p>'
    h += '<p><b>I. FUTURE SIMPLE (Tương lai đơn) &amp; NEAR FUTURE (Tương lai gần)</b></p>'
    h += ('<p><b>1. Tương lai đơn (Future simple)</b></p><table class="th"><tr><th>Thể</th><th>Cấu trúc</th></tr>'
          '<tr><td>Khẳng định</td><td><b>S + will + V0</b></td></tr>'
          '<tr><td>Phủ định</td><td><b>S + will + not + V0</b></td></tr>'
          '<tr><td>Nghi vấn</td><td><b>(Wh-) + will (not) + S + V0 ?</b></td></tr></table>'
          '<p><b>Lưu ý:</b> will = shall = ’ll; will not = won’t.</p>')
    h += ('<p><b>2. Tương lai gần (Near future)</b></p><table class="th"><tr><th>Thể</th><th>Cấu trúc</th></tr>'
          '<tr><td>Khẳng định</td><td><b>S + am/is/are + going to + V0</b></td></tr>'
          '<tr><td>Phủ định</td><td><b>S + am/is/are + not + going to + V0</b></td></tr>'
          '<tr><td>Nghi vấn</td><td><b>(Wh-) + am/is/are (+ not) + S + going to + V0 ?</b></td></tr></table>')
    h += ('<p><b>3. Cách phân biệt “tương lai đơn” và “tương lai gần”</b></p>'
          '<table class="th"><tr><th></th><th>Tương lai đơn (will)</th><th>Tương lai gần (be going to)</th></tr>'
          '<tr><td><b>Dự định, quyết định</b></td>'
          '<td>Quyết định/dự định nảy ra <b>ngay trong lúc nói</b>.<br>a. Please lend me your money! I <b>will bring</b> it back soon.<br>b. The floor looks dirty. I <b>will help</b> you to clean it.</td>'
          '<td>Ý định, kế hoạch <b>đã dự tính trước</b>.<br>a. Oh, really? <b>Is</b> she <b>going to have</b> a birthday party?<br>b. I’m so excited! We <b>are going to move</b> to a bigger house next month.</td></tr>'
          '<tr><td><b>Dự đoán</b></td>'
          '<td>Dự đoán <b>không</b> có cơ sở, bằng chứng.<br>a. I think our team <b>will win</b> the competition.<br>b. I think my sister <b>will pass</b> the exam.</td>'
          '<td>Dự đoán <b>có</b> cơ sở, bằng chứng ở hiện tại.<br>a. Look at these dark clouds! I think it <b>is going to rain</b>.<br>b. I’m not feeling well, I think I <b>am going to faint</b>.</td></tr></table>')
    h += '<p><b>II. PASSIVE VOICE (Thể bị động)</b></p>'
    h += ('<p><b>Muốn chuyển câu chủ động sang bị động, ta thực hiện các bước sau:</b></p>'
          '<table class="th"><tr><th>Active (chủ động)</th><th></th><th>Passive (bị động)</th></tr>'
          '<tr><td><b>S</b> (chủ ngữ)</td><td>→</td><td><b>by + O</b> (by + tân ngữ)</td></tr>'
          '<tr><td><b>V<sub>A</sub></b> (động từ chủ động)</td><td>→</td><td><b>BE + V<sub>P</sub></b> (động từ bị động)</td></tr>'
          '<tr><td><b>O</b> (tân ngữ)</td><td>→</td><td><b>S</b> (chủ ngữ)</td></tr></table>'
          '<p>1) Lấy tân ngữ của câu chủ động (active) làm chủ ngữ của câu bị động (passive).</p>'
          '<p>2) Đổi động từ chủ động (V<sub>A</sub>) thành động từ bị động (V<sub>P</sub>) (theo công thức).</p>'
          '<p>3) Chủ ngữ của câu chủ động chuyển thành tân ngữ của câu bị động, đứng sau giới từ <b>by</b> (by + O).</p>'
          '<p><u>Lưu ý:</u> chủ ngữ là <b>I, you, we, they, he, she, it, one, people, someone, somebody, nobody, no one</b> thường được bỏ đi khi chuyển sang câu bị động.</p>')
    rows = [
        ('Simple present<br>(hiện tại đơn)', 'S + V(s/es)', 'They <b>learn</b> English.', 'S + am/is/are + V3/ed (+ by O)', 'English <b>is learned</b> (by them).'),
        ('Present continuous<br>(hiện tại tiếp diễn)', 'S + am/is/are + V-ing', 'We <b>are planting</b> trees.', 'S + am/is/are + being + V3/ed (+ by O)', 'Trees <b>are being planted</b> (by us).'),
        ('Present perfect<br>(hiện tại hoàn thành)', 'S + have/has + V3/ed', 'Students <b>have cleaned</b> up the class.', 'S + have/has + been + V3/ed (+ by O)', 'The class <b>has been cleaned</b> up by students.'),
        ('Simple past<br>(quá khứ đơn)', 'S + V2/ed', 'I <b>did</b> my homework yesterday.', 'S + was/were + V3/ed (+ by O)', 'My homework <b>was done</b> (by me) yesterday.'),
        ('Past continuous<br>(quá khứ tiếp diễn)', 'S + was/were + V-ing', 'I <b>was driving</b> a car at this time yesterday.', 'S + was/were + being + V3/ed (+ by O)', 'A car <b>was being driven</b> (by me) at this time yesterday.'),
        ('Past perfect<br>(quá khứ hoàn thành)', 'S + had + V3/ed', 'Dung <b>had done</b> the task before I came.', 'S + had been + V3/ed (+ by O)', 'The task <b>had been done</b> by Dung before I came.'),
        ('Simple future<br>(tương lai đơn)', 'S + will + V0', 'Tuan <b>will water</b> the flowers.', 'S + will + be + V3/ed (+ by O)', 'The flowers <b>will be watered</b> by Tuan.'),
        ('Near future<br>(tương lai gần)', 'S + am/is/are + going to + V0', 'Our teacher <b>is going to move</b> the tables.', 'S + am/is/are + going to + be + V3/ed (+ by O)', 'The tables <b>are going to be moved</b> by our teacher.'),
    ]
    h += '<p><b>Công thức biến đổi từ câu chủ động sang câu bị động của các thì</b></p><table class="th"><tr><th>Tenses (các thì)</th><th>Active voice</th><th>Ví dụ</th><th>Passive voice</th><th>Ví dụ</th></tr>'
    for r in rows:
        h += '<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>'
    h += '</table>'
    return h


def build():
    pages = []
    H = {}
    seq = [('e1', r'^<b>E1:'), ('e2', r'^<b>E2:'), ('e3', r'^<b>E3:'), ('e4', r'^<b>E4:'), ('e5', r'^<b>E5:'),
           ('e6', r'^<b>E6:'), ('e7', r'^<b>E7:'), ('e8', r'^<b>E8:'), ('l', r'^IV-LISTENING'), ('e9', r'^<b>E9:'),
           ('sp', r'^V-SPEAKING'), ('e10', r'^<b>E10:'), ('e11', r'^<b>E11:')]
    cur = 1
    for k, pat in seq:
        cur = fnd(pat, cur)
        H[k] = cur
    H['end'] = len(BR) + 1

    # ---- phát âm
    ph1 = mcq('ph1', rng(H['e1'] + 1, H['e2'] - 1)); assert len(ph1) == 5
    ph2 = mcq('ph2', rng(H['e2'] + 1, fnd(r'II-VOCABULARY') - 1)); assert len(ph2) == 8
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'ph1', 'instr': 'E1: Mark the letter A, B, C or D to indicate the word whose underlined part differs from the other three in pronunciation in each of the following questions.', 'items': ph1},
        {'id': 'ph2', 'instr': 'E2: Mark the letter A, B, C, or D to indicate the word that differs from the other three in the position of the primary stress in each of the following questions.', 'items': ph2}]})

    # ---- từ vựng & ngữ pháp
    def fills(gid, a, b):
        out = []
        for l in rng(a, b):
            m = re.match(r'^Question (\d+):\s*(.*)$', cl(l))
            if m:
                q = fixblank(m.group(2))
                q = re.sub(r'(?<!\{)______', '{_}', q)
                q = q.replace('{_}farming', '{_} farming')
                out.append({'id': '%s.%d' % (gid, len(out) + 1), 't': 'fill', 'q': re.sub(r'\s+', ' ', q).replace('people\'s{_}', "people's {_}")})
        return out
    vg1 = fills('vg1', H['e3'] + 1, H['e4'] - 1); assert len(vg1) == 8
    vg2 = fills('vg2', H['e4'] + 1, H['e5'] - 1); assert len(vg2) == 8
    for it in vg1 + vg2:
        assert it['q'].count('{_}') == 1, it
    vg3 = []
    for l in rng(H['e5'] + 1, H['e6'] - 1):
        m = re.match(r'^Question (\d+):\s*(.*)$', cl(l))
        if m:
            vg3.append({'id': 'vg3.%d' % (len(vg3) + 1), 't': 'fill', 'long': True,
                        'q': '<b>Active:</b> %s<br><b>Passive:</b> {_}' % m.group(2).strip()})
    assert len(vg3) == 8
    vg4 = mcq('vg4', rng(H['e6'] + 1, H['e7'] - 1)); assert len(vg4) == 44, len(vg4)
    vg4[24]['q'] = 'It’s very hot. ______ the window, please?'
    vg4[22]['q'] = '“Look at those dark clouds!” - “Yes, it ______ in some minutes.”'
    vg4[39]['q'] = '______ by your father?'
    vg4[17]['q'] = 'This house is going ______ by my mother.'
    pages.append({'id': 'tu-vung-ngu-phap', 'title': 'Từ vựng & Ngữ pháp', 'mode': 'practice', 'groups': [
        {'id': 'vg1', 'instr': 'E3: Choose the words or phrases from the box to complete the sentences.',
         'bank': ['energy', 'eco-friendly', 'organic', 'adopt', 'household appliance', 'raise', 'meet', 'reduce'], 'items': vg1},
        {'id': 'vg2', 'instr': 'E4: Choose the words or phrases from the box to complete the sentences.',
         'bank': ['protect', 'plastic', 'organic', 'set up', 'eco-friendly', 'household', 'awareness', 'drop'], 'items': vg2},
        {'id': 'vg3', 'instr': 'E5: Rewrite the following sentences using the passive voice.', 'items': vg3},
        {'id': 'vg4', 'instr': 'E6: Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.', 'items': vg4}]})

    # ---- nghe (Word không kèm audio)
    stm = []
    for l in rng(H['e9'] + 1, H['sp'] - 1):
        m = re.match(r'^(\d)\.\s*(.*)$', cl(l))
        if m:
            stm.append({'id': 'li1.%s' % m.group(1), 't': 'tf', 'q': m.group(2)})
    assert len(stm) == 8
    script = []
    k_end = next(i for i, l in enumerate(RAW) if 'IV-LISTENING' in l and i > END)
    ks = next(i for i, l in enumerate(RAW) if 'Audio script' in l and i > END)
    ke = next(i for i, l in enumerate(RAW) if l.startswith('<b>E9:') and i > ks)
    txt = ' '.join(RAW[ks + 1:ke])
    txt = re.sub(r'\[IMG:[^\]]*\]', ' ', txt)
    txt = re.sub(r'\s+(?=(?:Harry|Olivia|Magda|Johnny|Carlos|All)[:.] )', '\n', txt)
    for ln in txt.split('\n'):
        ln = ln.strip()
        if ln:
            ln = re.sub(r'^(Olivia|Magda)\.', r'\1:', ln)
            ln = re.sub(r'^(\w+): ', r'<b>\1:</b> ', ln)
            script.append('<p>%s</p>' % ln.replace('Usually', 'Usually…') if ln.endswith('Usually') else '<p>%s</p>' % ln)
    sc = ('<div class="note"><b>Lưu ý:</b> bộ Word này không kèm file audio nên chưa có bài nghe. Bạn có thể đọc audio script dưới đây rồi làm bài (hoặc nhờ giáo viên đọc).</div>'
          '<details><summary><b>Audio script</b> (bấm để mở)</summary>%s</details>' % ''.join(script))
    pages.append({'id': 'nghe', 'title': 'Nghe (không audio)', 'mode': 'practice', 'groups': [
        {'id': 'li1', 'instr': 'E9: Decide whether the following statements are true (T) or false (F).', 'passage': sc, 'items': stm}]})

    # ---- nói
    sp = [{'id': 'sp1.1', 't': 'open', 'q': 'Talk about things you should do to make the environment better. You may use the suggested ideas below. You can start with the sentence: <i>“There are several things I should do to make the environment better …”</i>'
           '<ul><li>Reducing the amount of energy you use in the home</li><li>Using organic food</li><li>Avoiding products that are made from plastic</li></ul>'}]
    pages.append({'id': 'noi', 'title': 'Nói', 'mode': 'practice', 'groups': [
        {'id': 'sp1', 'instr': 'V – Speaking: Talk about things you should do to make the environment better. (nói/viết – đối chiếu bài mẫu)', 'items': sp}]})

    # ---- đọc
    def para(lines):
        out = []
        for l in lines:
            t = keepu(cl(l))
            if t and not t.startswith('(Adapted'):
                out.append('<p>%s</p>' % t)
            elif t:
                out.append('<p><i>%s</i></p>' % t)
        return ''.join(out)
    k7 = fnd(r'^<b>Question 1:', H['e7'])
    p7 = para(rng(H['e7'] + 1, k7 - 1)).replace('plastic- tree shops', 'plastic-free shops')
    re1 = mcq('re1', rng(k7, H['e8'] - 1)); assert len(re1) == 5
    k8 = fnd(r'^<b>Question 1:', H['e8'])
    p8 = para(rng(H['e8'] + 1, k8 - 1)).replace('at no they cost', 'at no cost')
    re2 = mcq('re2', rng(k8, H['l'] - 1)); assert len(re2) == 8
    for it in re1 + re2:
        it['q'] = re.sub(r'"(<u>.*?</u>)[”"]', r'“\1”', it['q'])
    pages.append({'id': 'doc', 'title': 'Đọc hiểu', 'mode': 'practice', 'groups': [
        {'id': 're1', 'instr': 'E7: Read the following passage and mark the letter A, B, C, or D on your answer sheet to indicate the correct answer to each of the questions.', 'passage': p7, 'items': re1},
        {'id': 're2', 'instr': 'E8: Read the following passage and mark the letter A, B, C, or D on your answer sheet to indicate the correct answer to each of the questions.', 'passage': p8, 'items': re2}]})

    # ---- viết
    wr1 = []
    for l in rng(H['e10'] + 1, H['e11'] - 1):
        m = re.match(r'^Question (\d):\s*(.*?)\s*$', cl(l))
        if m:
            wr1.append({'id': 'wr1.%s' % m.group(1), 't': 'fill', 'long': True,
                        'q': '<b>Từ gợi ý:</b> %s<br>Câu hoàn chỉnh: {_}' % m.group(2).strip()})
    assert len(wr1) == 8
    wr2 = [{'id': 'wr2.1', 't': 'open', 'q': 'Write a paragraph (120 – 150 words) about ways to reduce your carbon footprint.'}]
    pages.append({'id': 'viet', 'title': 'Viết', 'mode': 'practice', 'groups': [
        {'id': 'wr1', 'instr': 'E10: Use the verbs in their correct forms and add some words where necessary to make meaningful sentences.', 'items': wr1},
        {'id': 'wr2', 'instr': 'E11: Write a paragraph (120 – 150 words) about ways to reduce your carbon footprint. (tự luận – xem bài mẫu)', 'items': wr2}]})
    return {'id': 'lop10-u2-botro', 'title': 'Unit 2 – Humans and the environment: Bài tập bổ trợ', 'grade': 10, 'unit': 2, 'theory': theory(), 'pages': pages}


if __name__ == '__main__':
    b = build()
    dump(os.path.join(ROOT, 'units/lop10_u2_botro.py'), 'SET', b)
    tot = 0
    for p in b['pages']:
        n = sum(len(g['items']) for g in p['groups']); tot += n
        print(p['id'], n, [(g['id'], len(g['items'])) for g in p['groups']])
    print('TOTAL', tot)
