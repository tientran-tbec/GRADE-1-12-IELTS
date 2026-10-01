"""Chuyển đổi 1 lần: Đề ôn tập giữa HK1 Anh 11 Global 25-26 Đề 7 (src/mt1/d7.txt) -> units/mt1_test06.py (khung câu hỏi).
Đáp án + giải thích: units/mt1_test06_dapan.py (soạn tay). Audio: audio/mt1_test06.mp3 (ffmpeg, mono 64kbps; nguồn RAW/...De-7.mp3)."""
import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from mt1_common import *

L = load_src('d7')
END = find(L, r'ĐÁP ÁN ĐỀ ÔN GIỮA')
EX = L[:END]


def seg(a, b=None):
    i = find(EX, a)
    return EX[i:find(EX, b, i + 1)] if b else EX[i:]


def stem_of(blk):
    out = []
    for t in blk:
        if re.match(r'^A\.', t):
            break
        out.append(re.split(r'\s+A\.\s+True', t)[0])
    return ' '.join(out).strip()


def build():
    groups = []
    # --- Listening
    b1 = blocks(seg(r'^<b>I\.Listen', r'^<b>II\. Listen'))
    b2 = blocks(seg(r'^<b>II\. Listen', r'PART 2: LEXICO'))
    assert sorted(b1) == [1, 2, 3, 4] and sorted(b2) == [5, 6, 7, 8]
    groups.append({'id': 'g1', 'instr': 'PART 1: LISTENING. I. Listen to a speech and decide whether the following statements are true (T) or false (F). You will listen TWICE.',
                   'items': [{'id': 'g1.%d' % n, 't': 'tf', 'q': stem_of(b1[n])} for n in sorted(b1)]})
    items = []
    for n in sorted(b2):
        q = re.sub(r'\s*_{3,}\s*', ' {_}', ' '.join(b2[n]))
        q = re.sub(r'\s+([.,])', r'\1', q).strip()
        q = re.sub(r'\{_\}(?=[A-Za-z])', '{_} ', q)      # nguồn dính chữ: "_____of the power plant"
        items.append({'id': 'g2.%d' % n, 't': 'fill', 'q': q, 'hint': 'ONE WORD'})
    groups.append({'id': 'g2', 'instr': 'II. Listen to a talk about Bjarke Ingels and his company’s architectural projects and complete each of the sentences with ONE WORD. You will listen TWICE.',
                   'items': items})
    # --- Lexico-grammar
    lg = blocks(seg(r'^<b>I\. Write the letter', r'^<b>II/ Read'))
    assert sorted(lg) == list(range(9, 20)), sorted(lg)
    groups.append({'id': 'g3', 'instr': 'PART 2: LEXICO-GRAMMAR. I. Write the letter A, B, C, or D on your answer sheet to indicate the correct answer to each of the following questions.',
                   'items': [mcq_item('g3', n, lg[n]) for n in sorted(lg)]})
    # --- Cloze (advertisement)
    cl_seg = seg(r'^Our vision is', r'^<b>PART 3')
    pi = [i for i, l in enumerate(cl_seg) if re.match(r'^<b>Question', l)][0]
    para = ' '.join(cl(l) for l in cl_seg[:pi] if cl(l))
    para = re.sub(r'\((\d\d)\)\s*_+\s*', r'<b>(\1) ______</b> ', para)
    para = re.sub(r'([a-z])\.(?=[A-Z(<])', r'\1. ', para)
    para = re.sub(r'\.(<b>)', r'. \1', para)
    para = re.sub(r'(______</b>) (?=[a-z])', r'\1 ', para)
    para = re.sub(r'\s+([.,])', r'\1', para)
    cz = blocks(cl_seg[pi:])
    assert sorted(cz) == list(range(20, 25)), sorted(cz)
    groups.append({'id': 'g4', 'instr': 'II. Read the following advertisement and mark the letter A, B, C and D on your answer sheet to indicate the option that best fits each of the numbered blanks.',
                   'passage': '<p>%s</p>' % para,
                   'items': [dict(mcq_item('g4', n, cz[n]), q='Blank (%d)' % n) for n in sorted(cz)]})
    # --- Reading
    rd_seg = seg(r'^The concept of parental', r'^<b>PART 4')
    rq = [i for i, l in enumerate(rd_seg) if re.match(r'^<b>Question', l)][0]
    paras = []
    for l in rd_seg[:rq]:
        t = l.replace('⟦', '').replace('⟧', '').replace('\t', ' ').strip()
        t = re.sub(r'\s+', ' ', t)
        if t:
            paras.append(t)
    assert len(paras) == 5, paras
    paras[2] = paras[2].replace('<b>them</b>', '<b><u>them</u></b>')
    paras[3] = paras[3].replace('<b>authoritarian</b>', '<b><u>authoritarian</u></b>')
    rd = blocks(rd_seg[rq:])
    assert sorted(rd) == list(range(25, 30)), sorted(rd)
    items = []
    for n in sorted(rd):
        it = mcq_item('g5', n, rd[n])
        it['q'] = it['q'].replace('The word them', 'The word “<u>them</u>”').replace('The word authoritarian', 'The word “<u>authoritarian</u>”')
        it['q'] = it['q'].replace('NOT mentioned', '<b>NOT mentioned</b>')
        items.append(it)
    groups.append({'id': 'g5', 'instr': 'PART 3: READING. Read the following passage and mark the letter A, B, C, or D to indicate the answer to each of the questions.',
                   'passage': ''.join('<p>%s</p>' % p for p in paras), 'items': items})
    # --- Sắp xếp
    ar = blocks(seg(r'^<b>I/ Mark', r'^<b>II\. Supply'))
    assert sorted(ar) == [30, 31, 32]
    items = []
    for n in sorted(ar):
        blk = ar[n]
        k = max(i for i, t in enumerate(blk) if re.match(r'^[A-D]\.\s*[a-e]\s*[–-]', t))
        sents = [re.sub(r'^([A-E])\.', lambda m: m.group(1).lower() + '.', t) for t in blk[:k]]
        opts = [re.sub(r'\s*[–-]\s*', ' – ', o) for o in split_opts(' '.join(blk[k:]))]
        assert len(opts) == 4 and len(sents) in (4, 5), (n, sents, opts)
        items.append({'id': 'g6.%d' % n, 't': 'mcq', 'q': '<br>'.join(sents), 'o': opts})
    groups.append({'id': 'g6', 'instr': 'PART 4: WRITING. I. Mark the letter A, B, C or D on your answer sheet to indicate the best arrangement of utterances or sentences to make a meaningful exchange or text in each of the following questions.',
                   'items': items})
    # --- Dạng đúng của từ
    wb = blocks(seg(r'^<b>II\. Supply', r'^<b>III/For'))
    assert sorted(wb) == list(range(33, 38)), sorted(wb)
    items = []
    for n in sorted(wb):
        s = ' '.join(wb[n])
        m = re.match(r'^(.*?)\s*\(([A-Za-z /]+)\)\s*$', s)
        q = re.sub(r'\s*_{3,}\s*', ' {_} ', m.group(1)).strip()
        q = re.sub(r'\s+([.,])', r'\1', q)
        if n == 37:
            q += '.'                                    # nguồn thiếu dấu chấm cuối câu
        items.append({'id': 'g7.%d' % n, 't': 'fill', 'q': q, 'hint': re.sub(r'\s*/\s*', ' / ', m.group(2).strip())})
    groups.append({'id': 'g7', 'instr': 'II. Supply the correct form or tense of the given verb in each of the following questions to make meaningful sentences. (1.0 pt)', 'items': items})
    # --- Viết lại câu
    wr = blocks(seg(r'^<b>III/For'))
    assert sorted(wr) == list(range(38, 42)), sorted(wr)
    HINT = {38: ('first', 'This is the'), 39: (None, 'She has'), 40: ('using a modal verb', 'Students'), 41: ('using a modal verb', 'You')}
    items = []
    for n in sorted(wr):
        stem = wr[n][0]
        if n == 39:
            stem = 'The last time she saw her grandparents was in 2019'     # nguồn đề bị cụt năm "2019"
        stem = re.sub(r'\s*\((using a modal verb)\)\.?$', '', stem).rstrip('.')
        h, pre = HINT[n]
        q = '<b>%s</b>%s<br>→ %s {_}' % (stem, (' <i>(%s)</i>' % h) if h else '', pre)
        items.append({'id': 'g8.%d' % n, 't': 'fill', 'long': True, 'q': q})
    groups.append({'id': 'g8', 'instr': 'III. For each question, complete the new sentence so that it means the same as the given one(s) using given words. (1.0 pt)', 'items': items})
    return {'id': 'lop11-mt1-test06', 'title': 'Test 6 – Mid-term 1', 'grade': 11, 'unit': 'MidTerm1', 'theory': '',
            'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 60, 'audio': True, 'groups': groups}]}


if __name__ == '__main__':
    b = build()
    dump(os.path.join(ROOT, 'units/mt1_test06.py'), 'SET', b)
    n = 0
    for g in b['pages'][0]['groups']:
        n += len(g['items']); print(g['id'], len(g['items']))
    print('TOTAL', n)
