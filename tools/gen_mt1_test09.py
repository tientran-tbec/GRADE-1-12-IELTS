"""Chuyển đổi 1 lần: Đề ôn tập giữa HK1 Anh 11 Global 25-26 Đề 10 (src/mt1/d10.txt) -> units/mt1_test09.py (khung câu hỏi).
Đáp án + giải thích: units/mt1_test09_dapan.py (soạn tay). Audio: audio/mt1_test09.mp3 (ffmpeg, mono 64kbps; file gốc chỉ gồm đúng phần nghe của đề)."""
import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from mt1_common import *

L = load_src('d10', fixes=[('Math pay', 'Matt pay')])
END = find(L, r'ĐÁP ÁN ĐỀ ÔN GIỮA KÌ')
EX = [l for l in L[:END] if not re.match(r'^\s*</?(TABLE|ROW|CELL)', l)]


def seg(a, b):
    return EX[find(EX, a):find(EX, b)]


def num_blocks(lines):
    """khối đánh số '1. ...' (không có chữ Question)"""
    out, cur = {}, None
    for ln in lines:
        t = cl(ln)
        m = re.match(r'^(\d)\.\s+(.*)$', t)
        if m:
            cur = int(m.group(1)); out[cur] = [m.group(2)]
        elif cur is not None and t:
            out[cur].append(t)
    return out


def opts_of(blk):
    """tách stem + phương án; phương án đầu có thể thiếu 'A.'"""
    k = next((i for i, t in enumerate(blk) if re.match(r'^A\.', t)), None)
    if k is None:
        k = 1
        blk = blk[:1] + ['A. ' + blk[1]] + blk[2:]
    stem = ' '.join(blk[:k])
    return stem, split_opts(' '.join(blk[k:]))


def build():
    groups = []
    # --- Listening task 1
    b = num_blocks(seg(r'Task 1:', r'Statements'))
    assert sorted(b) == [1, 2, 3, 4]
    items = []
    for n in sorted(b):
        stem, o = opts_of(b[n])
        assert len(o) == 3, (n, o)
        items.append({'id': 'g1.%d' % n, 't': 'mcq', 'q': stem, 'o': o})
    groups.append({'id': 'g1', 'instr': 'Task 1: Listen to some information about a student’s health and habits. Circle the best answer A, B, or C. You will listen TWICE.', 'items': items})
    # --- Task 2 (bảng true/false)
    items = []
    for l in seg(r'Statements', r'PART 2: LEXICO'):
        t = cl(l)
        m = re.match(r'^(\d)\.\s+(.*)$', t)
        if m:
            items.append({'id': 'g2.%s' % m.group(1), 't': 'tf', 'q': m.group(2)})
    assert [i['id'] for i in items] == ['g2.5', 'g2.6', 'g2.7', 'g2.8']
    groups.append({'id': 'g2', 'instr': 'Task 2: Listen to a student and her grandfather and tick (√) to decide if the statements are true (T) or false (F). You will listen TWICE.', 'items': items})
    # --- Lexico-grammar
    bl = blocks(seg(r'Question 9\.', r'II/ Read the following announcement'))
    assert sorted(bl) == list(range(9, 20)), sorted(bl)
    items = []
    for n in sorted(bl):
        stem, o = opts_of(bl[n])
        assert len(o) == 4, (n, o)
        items.append({'id': 'g3.%d' % n, 't': 'mcq', 'q': fix_blank(stem), 'o': o})
    items[-1]['o'] = [x.replace('train s', 'trains') for x in items[-1]['o']]
    groups.append({'id': 'g3', 'instr': 'I. Write the letter A, B, C, or D on your answer sheet to indicate the correct answer to each of the following questions. (0,25 pt/ 1 sentence)', 'items': items})
    # --- Cloze
    i0 = find(EX, r'II/ Read the following announcement')
    ann = ' '.join(cl(x) for x in EX[i0 + 1:find(EX, r'Question 20')])
    ann = re.sub(r'\((\d\d)\)\s*_+', r'<b>(\1) ______</b>', ann)
    ann = re.sub(r'\s+', ' ', ann).replace('urban life, from', 'urban life, from')
    cz = blocks(EX[find(EX, r'Question 20'):find(EX, r'PART 3: READING')])
    assert sorted(cz) == list(range(20, 25)), sorted(cz)
    items = []
    for n in sorted(cz):
        it = mcq_item('g4', n, cz[n]); assert len(it['o']) == 4, (n, it)
        it['q'] = 'Blank (%d)' % n
        items.append(it)
    groups.append({'id': 'g4', 'instr': 'II/ Read the following announcement and mark the letter A, B, C and D on your answer sheet to indicate the option that best fits each of the numbered blanks. (0,25 pt/ 1 sentence)',
                   'passage': '<p>%s</p>' % ann, 'items': items})
    # --- Reading
    r0 = find(EX, r'Is the generation gap')
    para = re.sub(r'<b><u>they</u></b>', '<b><u>they</u></b>', EX[r0].strip())
    para = re.sub(r'\s+', ' ', para)
    rd = blocks(EX[r0 + 1:find(EX, r'PART 4: WRITING')])
    assert sorted(rd) == list(range(25, 30)), sorted(rd)
    items = []
    for n in sorted(rd):
        it = mcq_item('g5', n, rd[n]); assert len(it['o']) == 4, (n, it)
        it['q'] = it['q'].replace(' they ', ' <u>they</u> ')
        items.append(it)
    groups.append({'id': 'g5', 'instr': 'Read the following passage and mark the letter A, B, C, or D to indicate the answer to each of the question. (0,25 pt/ 1 sentence)',
                   'passage': '<p>%s</p>' % para, 'items': items})
    # --- Sắp xếp
    ar = blocks(seg(r'^Question 30', r'II\. Supply'))
    assert sorted(ar) == [30, 31, 32]
    items = []
    for n in sorted(ar):
        blk = ar[n]
        k = next(i for i, t in enumerate(blk) if re.match(r'^A\.', t))
        o = [re.sub(r'\s*[–-]\s*', ' – ', x) for x in split_opts(' '.join(blk[k:]))]
        assert len(o) == 4
        items.append({'id': 'g6.%d' % n, 't': 'mcq', 'q': '<br>'.join(blk[:k]), 'o': o})
    groups.append({'id': 'g6', 'instr': 'I/ Mark the letter A, B, C or D on your answer sheet to indicate the best arrangement of utterances or sentences to make a meaningful exchange or text in each of the following questions. (0,25 pt/ 1 sentence)', 'items': items})
    # --- Word form
    wb = blocks(seg(r'II\. Supply', r'III/For each'))
    assert sorted(wb) == list(range(33, 38)), sorted(wb)
    items = []
    for n in sorted(wb):
        s = ' '.join(wb[n])
        m = re.match(r'^(.*?)\s*\(([A-Z]+)\)\s*$', s)
        q = re.sub(r'\s+([.,])', r'\1', re.sub(r'\s*_{3,}\s*', ' {_} ', m.group(1))).strip()
        items.append({'id': 'g7.%d' % n, 't': 'fill', 'q': q, 'hint': m.group(2)})
    groups.append({'id': 'g7', 'instr': 'II. Supply the correct form or tense of the given verb in each of the following questions to make meaningful sentences. (1.0 pt)', 'items': items})
    # --- Rewrite
    wr = blocks(EX[find(EX, r'III/For each'):])
    assert sorted(wr) == list(range(38, 42)), sorted(wr)
    items = []
    for n in sorted(wr):
        stem, tail = wr[n][0], ' '.join(wr[n][1:])
        m = re.match(r'^(.*?)\s*\(([a-z]+)\)\s*$', stem)
        tail = re.sub(r'^=>\s*', '', tail)
        tail = re.sub(r'\s*_{3,}\s*', ' {_} ', tail)
        tail = re.sub(r'\s+([.,])', r'\1', tail).strip()
        items.append({'id': 'g8.%d' % n, 't': 'fill', 'long': True,
                      'q': '<b>%s</b> <i>(%s)</i><br>=> %s' % (m.group(1), m.group(2), tail)})
    groups.append({'id': 'g8', 'instr': 'III/ For each question, complete the new sentence so that it means the same as the given one(s) using the given words. (1.0 pt)', 'items': items})
    return {'id': 'lop11-mt1-test09', 'title': 'Test 9 – Mid-term 1', 'grade': 11, 'unit': 'MidTerm1', 'theory': '',
            'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 60, 'audio': True, 'groups': groups}]}


if __name__ == '__main__':
    b = build()
    dump(os.path.join(ROOT, 'units/mt1_test09.py'), 'SET', b)
    n = 0
    for g in b['pages'][0]['groups']:
        n += len(g['items']); print(g['id'], len(g['items']))
    print('TOTAL', n)
