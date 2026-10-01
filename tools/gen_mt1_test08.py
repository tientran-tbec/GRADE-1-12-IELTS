"""Chuyển đổi 1 lần: Đề ôn tập giữa HK1 Anh 11 Global 25-26 Đề 9 (src/mt1/d9.txt) -> units/mt1_test08.py (khung câu hỏi).
Đáp án + giải thích: units/mt1_test08_dapan.py (soạn tay). Audio: audio/mt1_test08.mp3 (ffmpeg, mono 64kbps)."""
import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from mt1_common import *

L = load_src('d9', fixes=[('Question 3.</b>Tom', 'Question 3. </b>Tom')])
END = find(L, r'ĐÁP ÁN ĐỀ CƯƠNG')
EX = L[:END]


def seg(a, b):
    return EX[find(EX, a):find(EX, b)]


def tf_items(gid, bl):
    out = []
    for n in sorted(bl):
        stem = []
        for t in bl[n]:
            if re.match(r'^A\.', t):
                break
            stem.append(t)
        out.append({'id': '%s.%d' % (gid, n), 't': 'tf', 'q': ' '.join(stem).strip()})
    return out


def build():
    groups = []
    # --- Listening
    b1 = blocks(seg(r'PART 1\.', r'PART 2\.'))
    b2 = blocks(seg(r'PART 2\.', r'II\. LEXICO'))
    assert sorted(b1) == [1, 2, 3, 4] and sorted(b2) == [5, 6, 7, 8]
    groups.append({'id': 'g1', 'instr': 'PART 1. You will listen to Grace and Tom talking about exams and decide whether the statements are true or false. You will listen TWICE.',
                   'items': tf_items('g1', b1)})
    groups.append({'id': 'g2', 'instr': 'PART 2. You will hear a lecture about climate changes. Listen and choose the correct answer A, B, C, or D to each of the following questions. You will hear the recording TWICE.',
                   'items': [mcq_item('g2', n, b2[n]) for n in sorted(b2)]})
    # --- Lexico-grammar
    lg = blocks(seg(r'II\. LEXICO', r'Read the following passage and mark the letter A, B, C or D'))
    # blocks của dòng 'A. x  B. y' nằm cùng 1 dòng
    assert sorted(lg) == list(range(9, 20)), sorted(lg)
    groups.append({'id': 'g3', 'instr': 'Mark the letter A, B, C or D on your answer sheet to indicate the correct answer to each of the following questions.',
                   'items': [mcq_item('g3', n, lg[n]) for n in sorted(lg)]})
    # --- Cloze
    i0 = find(EX, r'BLUE DRAGON')
    i1 = find(EX, r'Homeless people are')
    para = cl(EX[i1])
    para = re.sub(r'\((\d\d)\)\s*_+\s*', r'<b>(\1) ______</b> ', para)   # (20)  ___ of -> (20) ______ of
    para = re.sub(r'\s+([.,])', r'\1', para)
    para = para.replace('is  a non', 'is a non')
    para = re.sub(r'(______</b>) (of homeless)', r'\1 \2', para)
    para = re.sub(r'(______</b>)(?=\w)', r'\1 ', para)
    cz = blocks(EX[i1 + 1:find(EX, r'Read the following passage and mark the letter A, B, C, or D')])
    assert sorted(cz) == list(range(20, 25)), sorted(cz)
    for n in cz:        # "Question 20. A. plenty ..." -> dòng bắt đầu bằng 'A.'
        pass
    groups.append({'id': 'g4', 'instr': 'Read the following passage and mark the letter A, B, C or D on your answer sheet to choose the word or phrase that best fits each other numbered blanks.',
                   'passage': '<h4>BLUE DRAGON CHILDREN’S FOUNDATION</h4><p>%s</p>' % para,
                   'items': [dict(mcq_item('g4', n, cz[n]), q='Blank (%d)' % n) for n in sorted(cz)]})
    # --- Reading
    r0 = find(EX, r'In today.s fast-paced')
    rq = find(EX, r'^<b>Question 25')
    paras = []
    for l in EX[r0:rq]:
        t = cl(l)
        if not t:
            continue
        t = re.sub(r'<u>\s*([^<]*?)\s*</u>', r'<u>\1</u>', re.sub(r'</?b>', '', re.sub(r'<b>', '<b>', l.replace('⟦', '').replace('⟧', ''))))
        paras.append(t.strip())
    paras = [p.replace('<b>', '').replace('</b>', '') for p in paras]
    paras = [re.sub(r'\s+', ' ', p) for p in paras]
    paras[3] = paras[3].replace('Keeping a consistent', 'Keeping a <b>consistent</b>')
    paras[4] = paras[4].replace('<u>them</u>', '<b><u>them</u></b>')
    cite = paras.pop()      # (Adapted from ...)
    rd = blocks(EX[rq:find(EX, r'correct arrangement')])
    assert sorted(rd) == list(range(25, 30)), sorted(rd)
    items = []
    for n in sorted(rd):
        it = mcq_item('g5', n, rd[n])
        it['q'] = it['q'].replace('“them”', '“<u>them</u>”')
        items.append(it)
    groups.append({'id': 'g5', 'instr': 'Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each of the questions below.',
                   'passage': ''.join('<p>%s</p>' % p for p in paras) + '<p class="src"><i>%s</i></p>' % cite, 'items': items})
    # --- Sắp xếp câu
    ar = blocks(EX[find(EX, r'correct arrangement'):find(EX, r'IV\.WRITING')])
    assert sorted(ar) == [30, 31, 32]
    items = []
    for n in sorted(ar):
        blk = ar[n]
        k = next(i for i, t in enumerate(blk) if re.match(r'^[A-D]\.? ?[a-e]? ?[–-]', t) or re.match(r'^A\.', t))
        sents = [t for t in blk[:k]]
        opts = split_opts(' '.join(blk[k:]))
        opts = [o.replace(' – ', ' – ') for o in opts]
        items.append({'id': 'g6.%d' % n, 't': 'mcq', 'q': '<br>'.join(sents), 'o': opts})
    groups.append({'id': 'g6', 'instr': 'Mark the letter A, B, C, or D on your answer sheet to indicate the correct arrangement of the sentences to make a meaningful paragraph/letter in each of the following questions.',
                   'items': items})
    # --- Writing
    wb = blocks(EX[find(EX, r'IV\.WRITING'):find(EX, r'Finish each of')])
    assert sorted(wb) == list(range(33, 38)), sorted(wb)
    items = []
    for n in sorted(wb):
        s = ' '.join(wb[n])
        m = re.match(r'^(.*?)\s*\(([A-Z]+)\)\s*$', s)
        q = re.sub(r'\s*_{3,}\s*', ' {_} ', m.group(1)).strip()
        q = re.sub(r'\s+([.,])', r'\1', q)
        items.append({'id': 'g7.%d' % n, 't': 'fill', 'q': q, 'hint': m.group(2)})
    groups.append({'id': 'g7', 'instr': 'Supply the correct form or tense of the given verb in each of the following questions to make meaningful sentences. (1.0 pt)', 'items': items})
    wr = blocks(EX[find(EX, r'Finish each of'):])
    assert sorted(wr) == list(range(38, 42)), sorted(wr)
    items = []
    for n in sorted(wr):
        s = ' '.join(wr[n])
        m = re.match(r'^(.*?)\s*\((use [^)]*)\)\.?\s*$', s)
        items.append({'id': 'g8.%d' % n, 't': 'fill', 'long': True,
                      'q': '<b>%s</b> <i>(%s)</i><br>→ {_}' % (m.group(1), m.group(2))})
    groups.append({'id': 'g8', 'instr': 'Finish each of the following sentences in such a way that it means the same as the original sentence printed before it.', 'items': items})
    for g in groups:
        for it in g['items']:
            if g['id'] == 'g6':
                it['o'] = [re.sub(r'\s*[–-]\s*', ' – ', o) for o in it['o']]      # chuẩn hoá 'a – b – c'
            if it.get('o'):
                it['o'] = [o.replace('two- thirds', 'two-thirds').replace('temperature increase.', 'temperature increase') for o in it['o']]
    return {'id': 'lop11-mt1-test08', 'title': 'Test 8 – Mid-term 1', 'grade': 11, 'unit': 'MidTerm1', 'theory': '',
            'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 60, 'audio': True, 'groups': groups}]}


if __name__ == '__main__':
    b = build()
    dump(os.path.join(ROOT, 'units/mt1_test08.py'), 'SET', b)
    n = 0
    for g in b['pages'][0]['groups']:
        n += len(g['items']); print(g['id'], len(g['items']))
    print('TOTAL', n)
