"""Chuyển đổi 1 lần: Word Unit 3 (Cities of the Future) bộ BÀI TẬP 4 KỸ NĂNG -> units/lop11_u3_4kn.py (khung câu hỏi).
Đáp án + giải thích soạn tay ở units/lop11_u3_4kn_dapan.py.
Nguồn src/u3/4kn.txt: phần đề (1..1456, gồm lý thuyết, thực hành, bài kiểm tra) rồi bản có đáp án (từ 'ĐÁP ÁN')."""
import re, sys, os, shutil
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import parse_mcq, cl
from theory import theory_html
import gen_units as G
from gen_units import mk_mcq, groups_from_events, keepu, dump

ROOT = G.ROOT
KR = open(os.path.join(ROOT, 'src/u3/4kn.txt')).read().split('\n')
END_Q = next(i for i, l in enumerate(KR) if 'ĐÁP ÁN' in l)          # 0-based: hết phần đề
KQ = KR[:END_Q]

NAMES = ['pr1', 'pr2', 'vo1', 'vo2', 'vo3', 'vo4', 'vo5', 'vo6', 'vo7', 'gr1', 'gr2', 'gr3',
         're1', 're2', 're3', 'wr1', 'wr2', 'wr3', 'sp1', 'sp2', 'li1', 'li2']
START = next(i for i, l in enumerate(KQ) if 'B. THỰC' in l)
HEAD = [i for i in range(START, len(KQ)) if re.match(r'^<b>Task \d', KQ[i]) or re.match(r'^<b>[IVX]+\. ', KQ[i]) or 'C. BÀI KIỂM TRA' in KQ[i]]
TASKS = [i for i in HEAD if KQ[i].startswith('<b>Task')]
assert len(TASKS) == len(NAMES), len(TASKS)
SEC = {}
for n, i in zip(NAMES, TASKS):
    nxt = next(j for j in HEAD if j > i)
    SEC[n] = KQ[i + 1:nxt]
TEST = KQ[next(i for i, l in enumerate(KQ) if 'C. BÀI KIỂM TRA' in l) + 1:]


def items_of(ev):
    return [v for k, v in ev if k == 'item']


def para_html(lines):
    out = []
    for l in lines:
        t = keepu(cl(l))
        if t and not t.startswith('Source:') and not t.startswith('Adapted from'):
            out.append('<p>%s</p>' % t)
    return ''.join(out)


def boldblank(s):
    return re.sub(r'\((\d+)\)\s*_+', r'<b>(\1) ______</b>', s)


def build_4kn():
    theory = theory_html(KR[:START], '')
    pages = []

    # ---- Phát âm
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'pr1', 'instr': 'Task 1. Find the word whose underlined part differs from the other three in pronunciation.', 'items': mk_mcq('pr1', items_of(parse_mcq(SEC['pr1'], expect=1)))},
        {'id': 'pr2', 'instr': 'Task 2. Find the word that differs from the other three in the position of stress.', 'items': mk_mcq('pr2', items_of(parse_mcq(SEC['pr2'], expect=1)))},
    ]})

    # ---- Từ vựng
    w1 = ['roof garden', 'skyscraper', 'pedestrian zone', 'tram', 'cycle path']
    pics = ['a', 'b', 'c', 'd', 'e']
    vo1 = [{'id': 'vo1.%d' % i, 't': 'mcq', 'q': '<b>Hình %s</b> – chọn từ/cụm từ đúng' % pics[i - 1], 'img': 'image%d.jpeg' % i, 'o': w1[:], 'plain': True} for i in range(1, 6)]
    terms = ['public transport', 'carbon footprint', 'city dweller', 'urban centre', 'greenhouse gas']
    defs = ['a person who lives in a city',
            'the amount of greenhouse gases, like carbon dioxide, produced by our activities',
            'gas, especially carbon dioxide, that prevents heat from the earth escaping into space',
            'a system of transport that is available for use by the general public, including services such as buses, trains, trams, and subways.',
            'the middle part of a city/town']
    dl = '<div class="note"><ol type="a">%s</ol></div>' % ''.join('<li>%s</li>' % d for d in defs)
    vo2 = [{'id': 'vo2.%d' % i, 't': 'mcq', 'q': '<b>%s</b> – chọn a–e' % t, 'o': list('abcde'), 'plain': True} for i, t in enumerate(terms, 1)]
    vo3 = G.plain_fill('vo3', SEC['vo3'])
    assert len(vo3) == 10
    vo4 = mk_mcq('vo4', items_of(parse_mcq(SEC['vo4'], expect=1)))
    vo5 = mk_mcq('vo5', items_of(parse_mcq(SEC['vo5'], expect=1)))
    vo6 = G.plain_fill('vo6', SEC['vo6'])
    assert len(vo6) == 10 and all(it.get('hint') for it in vo6), [it.get('hint') for it in vo6]
    vo7_src = [('Cities worldwide are adopting ______ ideas such as renewable energy, green transportation.', ['eco-friendly', 'useless']),
               ('The city implemented various measures to reduce the number of crime ______ in the community.', ['victims', 'appointments']),
               ('The city offers various transportation options, making it easy for residents and visitors to ______ and explore all its attractions.', ['work out', 'get around']),
               ('I spent my Saturday morning doing household ______ like washing the dishes, cleaning the floors, and folding clothes.', ['chores', 'models']),
               ('The city recently introduced ______ buses as a sustainable and eco-friendly mode of public transportation.', ['renewable', 'electric'])]
    vo7 = [{'id': 'vo7.%d' % i, 't': 'mcq', 'q': q, 'o': o, 'plain': True} for i, (q, o) in enumerate(vo7_src, 1)]
    pages.append({'id': 'tu-vung', 'title': 'Từ vựng', 'mode': 'practice', 'groups': [
        {'id': 'vo1', 'instr': 'Task 1. Match the words or phrases with the pictures.', 'items': vo1},
        {'id': 'vo2', 'instr': 'Task 2. Match the words on the left with their meanings on the right (chọn chữ cái a–e).', 'passage': dl, 'items': vo2},
        {'id': 'vo3', 'instr': 'Task 3. Complete the following sentences using words or phrases from Task 1 and 2. Make any changes if necessary.', 'bank': w1 + terms, 'items': vo3},
        {'id': 'vo4', 'instr': 'Task 4. Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.', 'items': vo4},
        {'id': 'vo5', 'instr': 'Task 5. Choose the word(s) CLOSEST in meaning to the underlined word(s) in each of the following questions.', 'items': vo5},
        {'id': 'vo6', 'instr': 'Task 6. Complete the sentences using the correct form of the word in brackets.', 'items': vo6},
        {'id': 'vo7', 'instr': 'Task 7. Choose the correct words to complete the sentences.', 'items': vo7},
    ]})

    # ---- Ngữ pháp
    gr1_src = [('Smart cities ______ more efficient and connected.', ['are becoming', 'become']),
               ('Smart cities ______ modern with smart infrastructure and digital technologies everywhere.', ['look', 'are looking']),
               ('The urban lifestyle ______ fast-paced and dynamic with endless opportunities for work, entertainment, and cultural experiences.', ['is seeming', 'seems']),
               ('The urban lifestyle ______ busy with traffic and people talking all around.', ['is sounding', 'sounds']),
               ('He ______ of buying a new apartment in this modern city.', ['is thinking', 'thinks']),
               ('I ______ it is a great idea.', ['think', 'am thinking']),
               ('My mom ______ a good time visiting some famous tourist attractions in Ha Noi.', ['is having', 'has']),
               ('I am on the 87th floor of this building. I ______ nauseous and dizzy right now because I am scared of heights.', ['am feeling', 'feel']),
               ('Ha Noi ______ "the city for Peace" in 1999. I am living here now.', ['became', 'was becoming'])]
    gr1 = [{'id': 'gr1.%d' % i, 't': 'mcq', 'q': q, 'o': o, 'plain': True} for i, (q, o) in enumerate(gr1_src, 1)]
    gr2 = mk_mcq('gr2', items_of(parse_mcq(SEC['gr2'], expect=1)))
    gr3 = []
    for ln in SEC['gr3']:
        m = re.match(r'^(\d+)\.\s*(.*)$', cl(ln))
        if not m:
            continue
        s = m.group(2)
        segs = re.findall(r'<u>(.*?)</u>', s)
        assert len(segs) == 4, segs
        it = iter('ABCD')
        s2 = re.sub(r'<u>(.*?)</u>', lambda mm: '<u>%s</u><sup>%s</sup>' % (mm.group(1).strip(), next(it)), s)
        gr3.append({'id': 'gr3.%s' % m.group(1), 't': 'mcq', 'q': keepu(s2), 'o': [x.strip() for x in segs]})
    pages.append({'id': 'ngu-phap', 'title': 'Ngữ pháp', 'mode': 'practice', 'groups': [
        {'id': 'gr1', 'instr': 'Task 1. Choose the appropriate verb form to complete the sentences.', 'items': gr1},
        {'id': 'gr2', 'instr': 'Task 2. Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.', 'items': gr2},
        {'id': 'gr3', 'instr': 'Task 3. Mark the letter A, B, C or D to indicate the mistake in each of the following sentences (rồi tự sửa lại cho đúng).', 'items': gr3},
    ]})

    # ---- Đọc
    def upto(lines, pat):
        return lines[:next(i for i, l in enumerate(lines) if re.match(pat, cl(l)))]
    r1 = SEC['re1']; r2 = SEC['re2']; r3 = SEC['re3']
    re1 = {'id': 're1', 'instr': 'Task 1. Read the following passage and mark the letter A, B, C or D to indicate the correct word that best fits each of the numbered blanks.',
           'passage': boldblank(para_html(upto(r1, r'^1\.\s'))), 'items': mk_mcq('re1', items_of(parse_mcq(r1[len(upto(r1, r'^1\.\s')):], expect=1)))}
    for i, it in enumerate(re1['items'], 1):
        it['q'] = 'Blank (%d)' % i
    p2 = upto(r2, r'^1\.\s')
    re2 = {'id': 're2', 'instr': 'Task 2. Read the following passage and choose the correct answer to each of the questions.', 'passage': para_html(p2),
           'items': mk_mcq('re2', items_of(parse_mcq(r2[len(p2):], expect=1)))}
    p3 = upto(r3, r'^_+\s*\d')
    st = [re.sub(r'^[_\s]*\d+\.\s*', '', cl(l)) for l in r3[len(p3):] if re.match(r'^_+\s*\d', cl(l))]
    assert len(st) == 5
    re3 = {'id': 're3', 'instr': 'Task 3. Read the passage and decide whether the following statements are true (T), false (F) or not given (NG).', 'passage': para_html(p3),
           'items': [{'id': 're3.%d' % i, 't': 'tfng', 'q': q} for i, q in enumerate(st, 1)]}
    pages.append({'id': 'doc', 'title': 'Đọc hiểu', 'mode': 'practice', 'groups': [re1, re2, re3]})

    # ---- Viết
    wr1 = []
    for ln in SEC['wr1']:
        t = cl(ln)
        if re.match(r'^\d+\.', t):
            m = re.match(r'^\d+\.\s*(.*?)\s*\((\d+) words\)$', t)
            wr1.append({'id': 'wr1.%d' % (len(wr1) + 1), 't': 'fill', 'q': 'Từ cho sẵn: <i>%s</i><br>Câu hoàn chỉnh: {_}' % m.group(1), 'nwords': int(m.group(2))})
    assert len(wr1) == 5
    wr2 = mk_mcq('wr2', items_of(parse_mcq(SEC['wr2'], expect=1)))
    pages.append({'id': 'viet', 'title': 'Viết', 'mode': 'practice', 'groups': [
        {'id': 'wr1', 'instr': 'Task 1. Reorder the given words and phrases to form meaningful sentences.', 'items': wr1},
        {'id': 'wr2', 'instr': 'Task 2. Mark the letter A, B, C or D to indicate the sentence that is closest in meaning to each of the given sentences.', 'items': wr2},
        {'id': 'wr3', 'instr': 'Task 3. Write a paragraph (120–150 words) about the benefits or downsides of living in a smart city (tự luận – xem bài mẫu).',
         'items': [{'id': 'wr3.1', 't': 'open', 'q': 'Write a paragraph (120–150 words) about the benefits or downsides of living in a smart city.'}]},
    ]})

    # ---- Nói
    pages.append({'id': 'noi', 'title': 'Nói', 'mode': 'practice', 'groups': [
        {'id': 'sp1', 'instr': 'Task 1. Answer the following questions (luyện nói – đối chiếu câu trả lời mẫu).', 'items': [
            {'id': 'sp1.1', 't': 'open', 'q': 'Do you want to live in a smart city? Why/ Why not?'},
            {'id': 'sp1.2', 't': 'open', 'q': 'In your opinion, how cities in the future will be?'}]},
        {'id': 'sp2', 'instr': 'Task 2. Describe a smart technology that has been integrated to operate your city in 2–3 minutes.', 'items': [
            {'id': 'sp2.1', 't': 'open', 'q': 'Describe a smart technology that has been integrated to operate your city.'}]},
    ]})

    # ---- Nghe
    li1 = mk_mcq('li1', items_of(parse_mcq(SEC['li1'], expect=1)))
    li2 = []
    for ln in SEC['li2']:
        t = cl(ln)
        if t:
            li2.append({'id': 'li2.%d' % (len(li2) + 1), 't': 'fill', 'q': G.blank(t)})
    assert len(li1) == 5 and len(li2) == 12
    pages.append({'id': 'nghe', 'title': 'Nghe', 'mode': 'practice', 'audio': 'kn_nghe.mp3', 'groups': [
        {'id': 'li1', 'instr': 'Task 1. Listen and choose the correct answers. You can listen to each recording TWICE.', 'items': li1},
        {'id': 'li2', 'instr': 'Task 2. Listen to a talk about the cities of the future and fill in the blanks with the missing information. You can listen to each recording TWICE.', 'items': li2},
    ]})

    # ---- Kiểm tra (50 câu)
    ev_t = parse_mcq([l for l in TEST if not cl(l).startswith('Source:') and not cl(l).startswith('Adapted from')], expect=1)
    tg = groups_from_events('kt', ev_t)
    for g in tg:
        for it in g['items']:
            it.pop('_n', None)
            if it['id'] in ('kt.20', 'kt.21'):
                it['q'] = re.sub(r'\s+(Mary:|Mike:|Lucy:|Kathy:)', r'<br><b>\1</b>', it['q'])
        # sửa lỗi nguồn: lệnh của câu 5–19 ghi nhầm là "exchanges"
        if g['instr'].startswith('Mark the letter A, B, C or D to indicate the sentence that best completes each of the following exchanges'):
            g['instr'] = 'Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.'
    # sửa lỗi nguồn: câu 17 có 2 phương án trùng 'believe' (B và C) -> C đổi thành 'believes' (khoá giữ B)
    for g in tg:
        for it in g['items']:
            if it['id'] == 'kt.17' and it['o'][1] == it['o'][2]:
                it['o'][2] = 'believes'
    nums = sorted(int(it['id'].split('.')[1]) for g in tg for it in g['items'])
    assert nums == list(range(1, 51)), nums
    pages.append({'id': 'kiem-tra', 'title': 'Bài kiểm tra Unit 3 (50 câu)', 'mode': 'test', 'minutes': 50, 'groups': tg})
    return {'id': 'lop11-u3-4kn', 'title': 'Unit 3 – Cities of the future: Bài tập 4 kỹ năng', 'grade': 11, 'unit': 3, 'theory': theory, 'pages': pages}


if __name__ == '__main__':
    k = build_4kn()
    dump(os.path.join(ROOT, 'units/lop11_u3_4kn.py'), 'SET', k)
    dst = os.path.join(ROOT, 'assets/lop11_u3/4kn')
    os.makedirs(dst, exist_ok=True)
    for i in range(1, 6):
        shutil.copy(os.path.join(ROOT, 'src/u3/img4kn/word/media/image%d.jpeg' % i), os.path.join(dst, 'image%d.jpeg' % i))
    tot = 0
    for p in k['pages']:
        n = sum(len(g['items']) for g in p['groups']); tot += n
        print(p['id'], n, [(g['id'], len(g['items'])) for g in p['groups']])
    print('TOTAL', tot)
