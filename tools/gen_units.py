"""Chuyển đổi 1 lần: nội dung Word Unit 1 -> units/lop11_u1_botro.py & units/lop11_u1_4kn.py (khung câu hỏi).
Đáp án + giải thích nằm ở file riêng *_dapan.py (soạn tay, đối chiếu với đáp án gốc)."""
import re, sys, os, pprint
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import parse_mcq, cl
from theory import theory_html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = open(os.path.join(ROOT, 'src/botro_c.txt')).read().split('\n')
K = open(os.path.join(ROOT, 'src/4kn_c.txt')).read().split('\n')
B_RAW = open(os.path.join(ROOT, 'src/botro.txt')).read().split('\n')
K_RAW = open(os.path.join(ROOT, 'src/4kn.txt')).read().split('\n')


def rng(L, a, b):  # 1-based inclusive
    return L[a - 1:b]


def keepu(s):
    """chuẩn hoá HTML ngắn: giữ <u>, bỏ khoảng trắng thừa"""
    s = re.sub(r'<u>(\s*)</u>', r'\1', s)
    s = re.sub(r'</u>(\s*)<u>', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def mk_mcq(gid, items, start=1):
    out = []
    for k, it in enumerate(items, start):
        out.append({'id': '%s.%d' % (gid, k), 't': 'mcq', 'q': keepu(it['q']), 'o': [keepu(x) for x in it['o']]})
    return out


def blank(s):
    s = re.sub(r'(?:<u>)?\s*_{3,}\s*(?:</u>)?', ' {_} ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return re.sub(r'\s+([.,?!;:])', r'\1', s)


def fill_numbered(gid, lines, hint=False):
    """câu điền từ có đánh số 'N. ... ____ ...'"""
    out = []
    for ln in lines:
        t = cl(ln)
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if not m:
            continue
        s = blank(m.group(2))
        h = None
        if hint:
            mh = re.search(r'\(([^()]*)\)', s)
            if mh:
                h = mh.group(1).strip()
                s = (s[:mh.start()] + s[mh.end():])
        s = re.sub(r'\s+', ' ', s).strip()
        s = s.replace(' .', '.').replace(' ?', '?').replace('{_}.', '{_}.')
        it = {'id': '%s.%d' % (gid, len(out) + 1), 't': 'fill', 'q': s}
        if h:
            it['hint'] = h
        out.append(it)
    return out


def err_items(gid, lines):
    """Ex7: nhận câu có 4 chỗ gạch chân, gắn nhãn A-D."""
    chunks, cur = [], None
    for ln in lines:
        t = cl(ln)
        if re.fullmatch(r'(?:[A-D]\s*)+', t) or not t or re.fullmatch(r'=>.*', t):
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
        assert len(segs) == 4, (k, segs)
        letters = iter('ABCD')
        s2 = re.sub(r'<u>(.*?)</u>', lambda m: '<u>%s</u><sup>%s</sup>' % (m.group(1), next(letters)), s)
        out.append({'id': '%s.%d' % (gid, k), 't': 'mcq', 'q': keepu(s2), 'o': [x.strip() for x in segs]})
    return out


def rewrite_items(gid, lines):
    out, cur = [], None
    for ln in lines:
        t = cl(ln)
        if not t:
            continue
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            cur = {'id': '%s.%d' % (gid, len(out) + 1), 't': 'fill', 'q': m.group(2).strip(), 'q2': ''}
            out.append(cur)
        elif cur is not None and not cur['q2']:
            cur['q2'] = t
    for it in out:
        it['q'] = it['q'] + '<br>' + it['q2'] + ' {_}'
        del it['q2']
    return out


def groups_from_events(prefix, ev, global_numbering=True, first_instr=None):
    groups, cur = [], None

    def newg(instr):
        nonlocal cur
        cur = {'id': '%s%d' % (prefix, len(groups) + 1), 'instr': instr, 'passage': '', 'items': []}
        groups.append(cur)

    for kind, v in ev:
        if kind == 'instr':
            newg(v)
        elif kind == 'para':
            if cur is None:
                newg(first_instr or '')
            if cur['items']:
                newg('')
            cur['passage'] += '<p>%s</p>' % keepu(v)
        else:
            if cur is None:
                newg(first_instr or '')
            cur['items'].append({'id': '%s.%d' % (prefix, v['n']) if global_numbering else '', 't': 'mcq',
                                 'q': keepu(v['q']), 'o': [keepu(x) for x in v['o']], '_n': v['n']})
    return groups


def passage_group(gid, instr, ev, first_item_id_prefix=None):
    """1 bài đọc + các câu trắc nghiệm (đánh số lại từ 1)"""
    paras = [keepu(v) for k, v in ev if k == 'para']
    items = [v for k, v in ev if k == 'item']
    return {'id': gid, 'instr': instr, 'passage': ''.join('<p>%s</p>' % p for p in paras), 'items': mk_mcq(gid, items)}


def dump(path, name, data):
    s = '# -*- coding: utf-8 -*-\n"""Dữ liệu nội dung %s (sinh từ file Word bằng tools/gen_units.py rồi có thể chỉnh tay).\nĐáp án + giải thích: xem file *_dapan.py cùng tên."""\n\n%s = ' % (name, name)
    s += pprint.pformat(data, width=150, sort_dicts=False) + '\n'
    open(path, 'w', encoding='utf8').write(s)


# =====================================================================
# BỘ 1: BÀI TẬP BỔ TRỢ
# =====================================================================
def build_botro():
    th_a = next(i for i, l in enumerate(B_RAW) if 'PART I. VOCABULARY' in l)
    th_b = next(i for i, l in enumerate(B_RAW) if 'A. PHONETIC' in l)
    theory = theory_html(B_RAW[th_a:th_b], '')

    pages = []
    # ---------------- Phonetic
    ph_notes = []
    for ln in rng(B, 185, 204):
        t = cl(ln)
        if t:
            ph_notes.append(t)
    ph1_html = '<p class="note"><b>Quy tắc:</b> trợ động từ đứng đầu câu hỏi Yes/No đọc dạng <b>yếu</b> (không nhấn); ở cuối câu trả lời ngắn đọc dạng <b>mạnh</b> (có nhấn). Chữ gạch chân là chữ cần chú ý khi đọc.</p><ol class="ex">'
    cur = ''
    pairs = []
    for t in ph_notes:
        t = re.sub(r'^\d+\.\s*', '', t)
        if t.startswith('- A:') or t.startswith('A:'):
            cur = t
        elif t.startswith('- B:') or t.startswith('B:'):
            pairs.append((cur, t))
    for a, b in pairs:
        ph1_html += '<li>%s<br>%s</li>' % (a.replace('- A:', '<b>A:</b>'), b.replace('- B:', '<b>B:</b>'))
    ph1_html += '</ol>'
    ph2 = parse_mcq(rng(B, 206, 225))
    ph3 = parse_mcq(rng(B, 227, 246))
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'ph1', 'instr': 'Exercise 1: Weak and strong forms of auxiliary verbs (luyện đọc theo cặp – không chấm điểm).', 'note': ph1_html, 'items': []},
        {'id': 'ph2', 'instr': 'Exercise 2: Mark the letter A, B, C, or D to indicate the word whose underlined part differs from the other three in pronunciation.', 'items': mk_mcq('ph2', [v for k, v in ph2 if k == 'item'])},
        {'id': 'ph3', 'instr': 'Exercise 3: Mark the letter A, B, C, or D to indicate the word that differs from the other three in the position of primary stress.', 'items': mk_mcq('ph3', [v for k, v in ph3 if k == 'item'])},
    ]})

    # ---------------- Vocabulary & Grammar
    vg1 = fill_numbered('vg1', rng(B, 249, 258))
    vg2 = parse_mcq(rng(B, 260, 370))
    vg3 = parse_mcq(rng(B, 372, 391))
    vg4 = parse_mcq(rng(B, 393, 412))
    vg5 = [
        ('David {_} at the beach for hours. I think he\'s having a great time there.', ['has been', 'was']),
        ('{_} tickets for the concert yesterday?', ['Have your friends bought', 'Did your friends buy']),
        ('My younger sister {_} school six months ago.', ['has started', 'started']),
        ('So far this week {_} two funny films on TV.', ["we've seen", 'we saw']),
        ('{_} to my grandparents on the phone last week.', ["I've talked", 'I talked']),
        ("What's that noise? {_} a new TV recently?", ['Have your neighbours bought', 'Did your neighbours buy']),
        ('{_} Nick this week?', ['Have you seen', 'Did you see']),
        ("{_} Ann and Tom for three years. We're really good friends now.", ["We've known", 'We knew']),
    ]
    vg5_items = [{'id': 'vg5.%d' % i, 't': 'mcq', 'q': q.replace('{_}', '______'), 'o': o} for i, (q, o) in enumerate(vg5, 1)]
    vg6 = fill_numbered('vg6', rng(B, 423, 447), hint=True)
    vg7 = err_items('vg7', rng(B, 449, 470))
    vg8 = rewrite_items('vg8', rng(B, 472, 512))
    pages.append({'id': 'tu-vung-ngu-phap', 'title': 'Từ vựng & Ngữ pháp', 'mode': 'practice', 'groups': [
        {'id': 'vg1', 'instr': 'Exercise 1: Complete the sentences with the verbs given in the correct form.',
         'bank': ['fall', 'lead', 'include', 'help', 'ensure', 'give off', 'treat', 'work out', 'give up', 'stay'], 'items': vg1},
        {'id': 'vg2', 'instr': 'Exercise 2: Mark the letter A, B, C, or D to indicate the correct answer to each of the following questions.', 'items': mk_mcq('vg2', [v for k, v in vg2 if k == 'item'])},
        {'id': 'vg3', 'instr': 'Exercise 3: Mark the letter A, B, C, or D to indicate the word(s) CLOSEST in meaning to the underlined word(s).', 'items': mk_mcq('vg3', [v for k, v in vg3 if k == 'item'])},
        {'id': 'vg4', 'instr': 'Exercise 4: Mark the letter A, B, C, or D to indicate the word(s) OPPOSITE in meaning to the underlined word(s).', 'items': mk_mcq('vg4', [v for k, v in vg4 if k == 'item'])},
        {'id': 'vg5', 'instr': 'Exercise 5: Choose the correct words.', 'items': vg5_items},
        {'id': 'vg6', 'instr': 'Exercise 6: Give the correct forms of the verbs in brackets using simple past or present perfect.', 'items': vg6},
        {'id': 'vg7', 'instr': 'Exercise 7: Mark the letter A, B, C, or D to indicate the underlined part that needs correction.', 'items': vg7},
        {'id': 'vg8', 'instr': 'Exercise 8: Complete the second sentence so that it has the same meaning as the first one.', 'items': vg8},
    ]})

    # ---------------- Listening
    li_items = [{'id': 'li1.%d' % i, 't': 'tf', 'q': q} for i, q in enumerate([
        'The passage is about rugby.',
        'Eating fruits and vegetables is an important part of a healthy diet.',
        'The passage says you should not have junk foods and sweets.',
        'Being active is important for living a long life.',
        'Doing yoga or playing rugby can help ensure a healthy lifestyle.'], 1)]
    pages.append({'id': 'nghe', 'title': 'Nghe', 'mode': 'practice', 'audio': 'bt_nghe.mp3', 'groups': [
        {'id': 'li1', 'instr': 'Listen to the recording and decide whether the following statements are true or false.', 'items': li_items}]})

    # ---------------- Speaking
    sp1_raw = rng(B, 525, 544)
    sp1, cur = [], None
    for ln in sp1_raw:
        t = cl(ln)
        m = re.match(r'^(\d+)\.\s*A:\s*(.*)$', t)
        if m:
            cur = {'id': 'sp1.%d' % len(sp1) + '', 'q': m.group(2)}
            cur['id'] = 'sp1.%d' % (len(sp1) + 1)
            sp1.append(cur)
            continue
        m = re.match(r'^B:\s*a\)\s*(.*?)\s+[bB]\)\s*(.*)$', t)
        if m and cur is not None:
            cur['o'] = [m.group(1).strip(), m.group(2).strip()]
    sp1_items = [{'id': x['id'], 't': 'mcq', 'q': '<b>A:</b> ' + x['q'] + '<br><b>B:</b> ______', 'o': x['o']} for x in sp1]
    sp2_items = [
        {'id': 'sp2.1', 't': 'fill', 'q': 'First, {_} up straight and {_} your arms above your head.'},
        {'id': 'sp2.2', 't': 'fill', 'q': '{_} to the ceiling.'},
        {'id': 'sp2.3', 't': 'fill', 'q': 'Look up, {_} down.'},
        {'id': 'sp2.4', 't': 'fill', 'q': 'Next, {_} turn your head from side to side.'},
        {'id': 'sp2.5', 't': 'fill', 'q': 'Now {_} your toes.'},
        {'id': 'sp2.6', 't': 'fill', 'q': '{_}, sit down on the floor.'},
    ]
    sp3 = parse_mcq(rng(B, 553, 583))
    pages.append({'id': 'noi', 'title': 'Nói (hội thoại)', 'mode': 'practice', 'groups': [
        {'id': 'sp1', 'instr': 'Exercise 1: Choose the correct response. Then practice the short exchanges in pairs.', 'items': sp1_items},
        {'id': 'sp2', 'instr': 'Exercise 2: Complete the instructions with the words below.', 'bank': ['finally', 'point', 'slowly', 'stand', 'stretch', 'look', 'touch'], 'items': sp2_items},
        {'id': 'sp3', 'instr': 'Exercise 3: Circle A, B, C, or D to indicate the correct response to each of the following exchanges.', 'items': mk_mcq('sp3', [v for k, v in sp3 if k == 'item'])},
    ]})

    # ---------------- Reading
    re1a = parse_mcq(rng(B, 585, 595))
    re1b = parse_mcq(rng(B, 596, 605))
    re2a = parse_mcq(rng(B, 607, 629))
    re2b = parse_mcq(rng(B, 630, 650))
    # bài đọc 1 có câu chữ nhúng "Adapted from" -> bỏ khỏi item
    g_re1a = passage_group('re1a', 'Exercise 1a: Read the passage and choose the word or phrase that best fits each numbered blank (1–5).', re1a)
    g_re1b = passage_group('re1b', 'Exercise 1b: Read the passage and choose the word or phrase that best fits each numbered blank (1–5).', re1b)
    g_re2a = passage_group('re2a', 'Exercise 2a: Read the passage and choose the correct answer to each question (1–5).', re2a)
    # 2b: các câu hỏi nằm sau bài đọc nhưng bị tính là 'para' (đánh số lại 1-5)
    paras2b = [cl(l) for l in rng(B, 630, 650)]
    ps = [t for t in paras2b if t and not re.match(r'^(\d+\.|[A-D]\.)', t)]
    pass2b = [t for t in ps[:4]]
    qs, cur = [], None
    for t in paras2b:
        if not t:
            continue
        m = re.match(r'^(\d)\.\s*(.*)$', t)
        if m:
            cur = {'n': int(m.group(1)), 'q': m.group(2), 'o': []}
            qs.append(cur)
        elif cur and re.match(r'^[A-D]\.\s', t):
            cur['o'] += re.findall(r'(?:^|\s)[A-D]\.\s+(.*?)(?=\s+[A-D]\.\s|$)', t)
    g_re2b = {'id': 're2b', 'instr': 'Exercise 2b: Read the passage and choose the correct answer to each question (1–5).',
              'passage': ''.join('<p>%s</p>' % keepu(p) for p in pass2b), 'items': mk_mcq('re2b', qs)}
    re3_stm = [re.sub(r'^\d+\.\s*', '', cl(l)) for l in rng(B, 659, 666) if re.match(r'^\s*\d+\.', cl(l))]
    re3_pass = ''.join('<p>%s</p>' % keepu(cl(l)) for l in rng(B, 653, 656))
    g_re3 = {'id': 're3', 'instr': 'Exercise 3: Read the passage, and then decide whether the statements are true (T) or false (F).',
             'passage': '<h4>No Pain, Big Gains</h4>' + re3_pass,
             'items': [{'id': 're3.%d' % i, 't': 'tf', 'q': q} for i, q in enumerate(re3_stm, 1)]}
    re4_pass = ''.join('<p>%s</p>' % keepu(cl(l)) for l in rng(B, 668, 674))
    re4_q = [re.sub(r'^\d+\.\s*', '', cl(l)) for l in rng(B, 675, 680)]
    g_re4 = {'id': 're4', 'instr': 'Exercise 4: Read the text and answer the following questions (tự luận – đối chiếu đáp án mẫu).',
             'passage': '<h4>A Healthy Lifestyle</h4>' + re4_pass,
             'items': [{'id': 're4.%d' % i, 't': 'open', 'q': q} for i, q in enumerate(re4_q, 1)]}
    pages.append({'id': 'doc', 'title': 'Đọc hiểu', 'mode': 'practice', 'groups': [g_re1a, g_re1b, g_re2a, g_re2b, g_re3, g_re4]})

    # ---------------- Writing
    wr1_items = [
        {'id': 'wr1.1', 't': 'mcq', 'q': 'Sentence <b>a</b>: Please let us know if we might bring something.', 'o': ['1', '2', '3', '4'], 'plain': True},
        {'id': 'wr1.2', 't': 'mcq', 'q': 'Sentence <b>b</b>: We are thrilled to be included in such a happy event and plan to meet you in the school auditorium on the evening of October 10th at seven o\'clock.', 'o': ['1', '2', '3', '4'], 'plain': True},
        {'id': 'wr1.3', 't': 'mcq', 'q': 'Sentence <b>c</b>: We are looking forward to the celebration.', 'o': ['1', '2', '3', '4'], 'plain': True},
        {'id': 'wr1.4', 't': 'mcq', 'q': 'Sentence <b>d</b>: Thank you for the kind invitation to the end-of-term party.', 'o': ['1', '2', '3', '4'], 'plain': True},
    ]
    wr2 = [
        'I / happy / receive / your invitation / Christmas party / December 24th / 7.00 pm',
        'I / glad / inform you / I / delighted / join / party / specified time',
        'I / make sure / I / present there / scheduled date / time',
        'I / look forward / enjoyable evening / our old friends',
        'Merry Christmas / best wishes / you / your family',
    ]
    pages.append({'id': 'viet', 'title': 'Viết', 'mode': 'practice', 'groups': [
        {'id': 'wr1', 'instr': 'Exercise 1: Put the sentences in a message in the correct order (chọn số thứ tự 1–4 cho từng câu). Message: "Dear Phong, … Nick".', 'items': wr1_items},
        {'id': 'wr2', 'instr': 'Exercise 2: Use the words or phrases given to write a short message ("Dear Sir, …"). Viết thành câu hoàn chỉnh rồi đối chiếu đáp án mẫu.',
         'items': [{'id': 'wr2.%d' % i, 't': 'open', 'q': q} for i, q in enumerate(wr2, 1)]},
        {'id': 'wr3', 'instr': 'Exercise 3: Write a paragraph of 100 words about a long and healthy life (tự luận – xem bài mẫu).',
         'items': [{'id': 'wr3.1', 't': 'open', 'q': 'Write a paragraph of about 100 words about a long and healthy life.'}]},
    ]})

    # ---------------- Test (40 câu)
    ev = parse_mcq(rng(B, 712, 807))
    groups = groups_from_events('kt', ev)
    # chỉnh nhóm: câu 34-40 là viết lại câu
    clean = []
    for g in groups:
        if any(it['_n'] >= 34 for it in g['items']):
            continue
        clean.append(g)
    rw = []
    for it in groups[-1]['items']:
        if it['_n'] >= 34:
            m = it['q']
            rw.append(it)
    # câu 34-40: parse thủ công từ nguồn
    rwl = [cl(l) for l in rng(B, 794, 807)]
    rwi, cur = [], None
    for t in rwl:
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m and int(m.group(1)) >= 34:
            cur = {'id': 'kt.%s' % m.group(1), 't': 'fill', 'q': m.group(2).strip() + '<br>', '_n': int(m.group(1))}
            rwi.append(cur)
        elif cur is not None and t and not t.startswith('---'):
            cur['q'] += t + ' {_}'
    clean.append({'id': 'kt-rw', 'instr': 'Complete the second sentence so that it has the same meaning as the first one.', 'passage': '', 'items': rwi})
    # câu 18/19 nhóm đối nghĩa: giữ nguyên nội dung gốc, ghi chú trong đáp án
    for g in clean:
        for it in g['items']:
            it.pop('_n', None)
    pages.append({'id': 'kiem-tra', 'title': 'Bài kiểm tra Unit 1 (40 câu)', 'mode': 'test', 'minutes': 40, 'groups': clean})

    return {'id': 'lop11-u1-botro', 'title': 'Unit 1 – A long and healthy life: Bài tập bổ trợ', 'grade': 11, 'unit': 1,
            'theory': theory, 'pages': pages}


# =====================================================================
# BỘ 2: BÀI TẬP 4 KỸ NĂNG
# =====================================================================
def split_bank(lines):
    bank, sent = [], []
    for ln in lines:
        if not cl(ln):
            continue
        if ln.startswith(' '):
            bank.append(cl(ln))
        else:
            sent.append(ln)
    return bank, sent


def plain_fill(gid, lines, hint_re=None):
    out = []
    for ln in lines:
        t = cl(ln)
        if not t:
            continue
        s = blank(t)
        h = None
        mh = re.search(r'\(([A-Z ]+)\)\s*$', s)
        if mh:
            h = mh.group(1).strip()
            s = s[:mh.start()].strip()
        it = {'id': '%s.%d' % (gid, len(out) + 1), 't': 'fill', 'q': s}
        if h:
            it['hint'] = h
        out.append(it)
    return out


def build_4kn():
    th_b = next(i for i, l in enumerate(K_RAW) if 'B. THỰC HÀNH' in l)
    theory = theory_html(K_RAW[:th_b], '')
    pages = []
    ev1 = parse_mcq(rng(K, 467, 476)); ev2 = parse_mcq(rng(K, 478, 487))
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'pr1', 'instr': 'Task 1. Find the word whose underlined part differs from the other three in pronunciation.', 'items': mk_mcq('pr1', [v for k, v in ev1 if k == 'item'])},
        {'id': 'pr2', 'instr': 'Task 2. Find the word that differs from the other three in the position of stress.', 'items': mk_mcq('pr2', [v for k, v in ev2 if k == 'item'])},
    ]})
    # vocabulary
    vo1_words = ['yoghurt', 'recipe', 'squat', 'vaccine', 'muscle', 'energy drink', 'antibiotic', 'fast food', 'press-up', 'diet']
    vo1_items = [{'id': 'vo1.%d' % i, 't': 'fill', 'q': '{_}', 'img': 'vo1_%d.jpg' % i} for i in range(1, 11)]
    bank2, s2 = split_bank(rng(K, 513, 528))
    vo2_items = plain_fill('vo2', s2)
    ev3 = parse_mcq(rng(K, 530, 549)); ev4 = parse_mcq(rng(K, 551, 560))
    vo5_items = plain_fill('vo5', rng(K, 562, 571))
    bank6, s6 = split_bank(rng(K, 573, 592))
    vo6_items = plain_fill('vo6', s6)
    pages.append({'id': 'tu-vung', 'title': 'Từ vựng', 'mode': 'practice', 'groups': [
        {'id': 'vo1', 'instr': 'Task 1. Write the words/phrases below the pictures.', 'bank': vo1_words[:], 'items': vo1_items},
        {'id': 'vo2', 'instr': 'Task 2. Fill in the blanks with one suitable word or phrase.', 'bank': bank2, 'items': vo2_items},
        {'id': 'vo3', 'instr': 'Task 3. Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.', 'items': mk_mcq('vo3', [v for k, v in ev3 if k == 'item'])},
        {'id': 'vo4', 'instr': 'Task 4. Choose the word(s) CLOSEST in meaning to the underlined word(s).', 'items': mk_mcq('vo4', [v for k, v in ev4 if k == 'item'])},
        {'id': 'vo5', 'instr': 'Task 5. Complete the sentences using the correct form of the word in brackets.', 'items': vo5_items},
        {'id': 'vo6', 'instr': 'Task 6. Fill in each blank with one suitable phrase.', 'bank': bank6, 'items': vo6_items},
    ]})
    # grammar
    ev_g1 = parse_mcq(rng(K, 595, 611)); ev_g3 = parse_mcq(rng(K, 622, 637))
    gr2_items = plain_fill('gr2', rng(K, 613, 620))
    for it in gr2_items:
        m = re.search(r'\((\w+)\)\s*\{_\}', it['q'])
        if m:
            it['hint'] = m.group(1)
            it['q'] = re.sub(r'\(\w+\)\s*\{_\}', '{_}', it['q'])
    pages.append({'id': 'ngu-phap', 'title': 'Ngữ pháp', 'mode': 'practice', 'groups': [
        {'id': 'gr1', 'instr': 'Task 1. Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.', 'items': mk_mcq('gr1', [v for k, v in ev_g1 if k == 'item'])},
        {'id': 'gr2', 'instr': 'Task 2. Complete the sentences with the correct form of the verbs (past simple or present perfect) in brackets.', 'items': gr2_items},
        {'id': 'gr3', 'instr': 'Task 3. Mark the letter A, B, C or D to indicate the mistake in each of the following sentences (rồi sửa lại cho đúng).', 'items': mk_mcq('gr3', [v for k, v in ev_g3 if k == 'item'])},
    ]})
    # reading
    ev_r1 = parse_mcq(rng(K, 640, 658)); ev_r3 = parse_mcq(rng(K, 671, 685))
    r2_pass = ''.join('<p>%s</p>' % keepu(cl(l)) for l in rng(K, 660, 666) if cl(l) and not re.match(r'^\d+\.', cl(l)))
    r2_st = [re.sub(r'\s*_{3,}\s*$', '', re.sub(r'^\d+\.\s*', '', cl(l))) for l in rng(K, 660, 669) if re.match(r'^\s*\d+\.', cl(l))]
    pages.append({'id': 'doc', 'title': 'Đọc hiểu', 'mode': 'practice', 'groups': [
        passage_group('re1', 'Task 1. Read the following passage and choose the correct answer to each of the following questions.', ev_r1),
        {'id': 're2', 'instr': 'Task 2. Read the passage and decide whether the following statements are true (T), false (F) or not given (NG).', 'passage': r2_pass,
         'items': [{'id': 're2.%d' % i, 't': 'tfng', 'q': q} for i, q in enumerate(r2_st, 1)]},
        passage_group('re3', 'Task 3. Read the following passage and mark the letter A, B, C or D to indicate the correct word that best fits each of the numbered blanks.', ev_r3),
    ]})
    # writing
    wr1_src = [cl(l) for l in rng(K, 688, 697) if re.match(r'^\d+\.', cl(l))]
    wr1_items = []
    for t in wr1_src:
        m = re.match(r'^\d+\.\s*(.*?)\s*\((\d+) words\)$', t)
        wr1_items.append({'id': 'wr1.%d' % (len(wr1_items) + 1), 't': 'fill', 'q': 'Từ cho sẵn: <i>%s</i><br>Câu hoàn chỉnh: {_}' % m.group(1), 'nwords': int(m.group(2))})
    wr2_src = [cl(l) for l in rng(K, 699, 708) if re.match(r'^\d+\.', cl(l))]
    wr2_items = []
    for t in wr2_src:
        m = re.match(r'^\d+\.\s*(.*?)\s*\(([A-Z]+)\)$', t)
        wr2_items.append({'id': 'wr2.%d' % (len(wr2_items) + 1), 't': 'fill', 'q': m.group(1) + '<br>Từ cho sẵn: <b>%s</b><br>Viết lại: {_}' % m.group(2)})
    pages.append({'id': 'viet', 'title': 'Viết', 'mode': 'practice', 'groups': [
        {'id': 'wr1', 'instr': 'Task 1. Reorder the given words and phrases to form meaningful sentences.', 'items': wr1_items},
        {'id': 'wr2', 'instr': 'Task 2. Rewrite each sentence using the given word in brackets as long as its meaning stays the same as the original one.', 'items': wr2_items},
    ]})
    # listening (CHỜ transcript)
    ev_l1 = parse_mcq(rng(K, 711, 729))
    li2 = [
        {'id': 'li2.1', 't': 'fill', 'q': 'Food that we need to {_} — sugar, {_}, butter'},
        {'id': 'li2.2', 't': 'fill', 'q': 'Food that we eat in moderation — milk, lean meat, fish, nuts, {_}'},
        {'id': 'li2.3', 't': 'fill', 'q': 'Food that we eat a lot — {_}, vegetables, fruit'},
    ]
    pages.append({'id': 'nghe', 'title': 'Nghe', 'mode': 'practice', 'audio': 'kn_nghe.mp3', 'pending': True, 'groups': [
        {'id': 'li1', 'instr': 'Task 1. Listen to the talk about a healthy diet and choose the correct answers. You can listen to each recording TWICE.', 'items': mk_mcq('li1', [v for k, v in ev_l1 if k == 'item'])},
        {'id': 'li2', 'instr': 'Task 2. Listen to the second part of the listening about a healthy diet and complete the Healthy Diet Pyramid.', 'items': li2},
    ]})
    # test
    ev_t = parse_mcq(rng(K, 738, 887))
    tg = groups_from_events('kt', ev_t)
    for g in tg:
        for it in g['items']:
            it.pop('_n', None)
    pages.append({'id': 'kiem-tra', 'title': 'Bài kiểm tra Unit 1 (50 câu)', 'mode': 'test', 'minutes': 50, 'groups': tg})
    return {'id': 'lop11-u1-4kn', 'title': 'Unit 1 – A long and healthy life: Bài tập 4 kỹ năng', 'grade': 11, 'unit': 1,
            'theory': theory, 'pages': pages}


if __name__ == '__main__':
    os.makedirs(os.path.join(ROOT, 'units'), exist_ok=True)
    b = build_botro()
    dump(os.path.join(ROOT, 'units/lop11_u1_botro.py'), 'SET', b)
    k = build_4kn()
    dump(os.path.join(ROOT, 'units/lop11_u1_4kn.py'), 'SET', k)
    for s in (b, k):
        tot = 0
        for p in s['pages']:
            n = sum(len(g['items']) for g in p['groups'])
            tot += n
            print(s['id'], p['id'], n, [ (g['id'], len(g['items'])) for g in p['groups']])
        print('TOTAL', tot)
