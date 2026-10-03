# -*- coding: utf-8 -*-
"""Nhóm on1c: Ôn thi HK1 – Đề 9, 10, 11, 12 (định dạng 'Question n.', KEYS ở cuối)."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g4_exam import *

VI = [('tick or cross', 'nghe và chọn tick/cross'), ('circle', 'nghe và khoanh'), ('listen and tick', 'nghe và chọn tranh'),
      ('listen and number', 'nghe và đánh số'), ('listen and write', 'nghe và chọn đúng/sai'), ('reorder', 'sắp xếp từ thành câu'),
      ('best option', 'chọn đáp án đúng'), ('true or false', 'đúng hay sai'), ('read and decide', 'đọc và chọn đúng/sai'),
      ('yes/ no', 'đọc và chọn Yes/No'), ('choose a', 'đọc và chọn đáp án đúng')]


def vi_instr(h):
    h = h.strip().rstrip('.')
    for k, v in VI:
        if k in h.lower():
            return '%s (%s)' % (h, v)
    return h


def parse_exam(src):
    raw = open(os.path.join(IMGROOT, src + '.txt'), encoding='utf8').read().replace('⟦', '').replace('⟧', '').split('\n')
    cut = next(i for i, l in enumerate(raw) if re.match(r'^\s*(ĐÁP ÁN|KEYS?)\b', l.strip(), re.I))
    body, ans = raw[:cut], raw[cut + 1:]
    keys, sent = {}, {}
    for l in ans:
        l = re.sub(r'img\d+\.png.*$', '', l).strip()
        if not l: continue
        if '|' in l:
            for n, k in re.findall(r'(\d+)\.\s*([A-D])\b', l): keys[int(n)] = k
        else:
            m = re.match(r'^(\d+)\.\s+(.+)$', l)
            if m: sent[int(m.group(1))] = m.group(2).strip()
    secs, cur, q = [], None, None
    for l in body:
        t = l.strip()
        if not t or t.startswith('MÔN') or t.startswith('ĐỀ ÔN') or t == '→': continue
        m = re.match(r'^Question\s+(\d+)\.\s*(.*)$', t)
        if m:
            q = {'n': int(m.group(1)), 'text': m.group(2).replace('→', '').strip(), 'opts': []}
            cur['qs'].append(q); continue
        if re.match(r'^[A-D]\.\s', t) and q is not None:
            for pt in re.split(r'\s+(?=[A-D]\.\s)', t):
                o = re.sub(r'^[A-D]\.\s*', '', pt).strip()
                q['opts'].append(o)
            continue
        im = re.fullmatch(r'(\[img:\w+\]\s*)+', t)
        if im:
            cur['img'] += imgs(t); continue
        if cur is None or cur['qs']:
            cur = {'head': t, 'img': [], 'pas': [], 'qs': []}; secs.append(cur); q = None
        else:
            cur['pas'].append(t)
    return secs, keys, sent


def lab(o):
    m = re.fullmatch(r'(?:tick |picture )?([a-d])', o.strip(), re.I)
    if m: return 'Tranh ' + m.group(1).lower()
    return {'tick': 'Tick (✓)', 'cross': 'Cross (✗)'}.get(o.strip().lower(), o.strip())


def build(ex, src, fixes=None, optfix=None):
    fixes = fixes or {}
    secs, keys, sent = parse_exam(src)
    for gi, s in enumerate(secs, 1):
        items, last = [], 0
        for q in s['qs']:
            n, txt = q['n'], fixes.get(q['n'], q['text'])
            m = re.fullmatch(r'Number\s*(\d+)', txt)
            if m:
                k = int(m.group(1))
                if k <= last: k = last + 1
                last = k
                txt = 'Nghe câu số %d.' % k
            elif re.fullmatch(r'Picture\s+([a-d])', txt):
                txt = 'Nghe và xét tranh %s.' % txt[-1]
            if q['opts']:
                opts = [o for o in q['opts'] if o not in ('_', '')]
                if optfix and n in optfix: opts = optfix[n]
                kk = keys[n]
                low = sorted(o.lower() for o in opts)
                if low == ['false', 'true']:
                    it = {'t': 'tf', 'q': txt}
                    a = 'T' if opts['ABCD'.index(kk)].lower() == 'true' else 'F'
                    items.append((it, a, 'Đáp án: %s (theo đáp án của đề).' % ('True' if a == 'T' else 'False')))
                else:
                    opts = [lab(o) for o in opts]
                    if not txt: txt = 'Chọn đáp án đúng.'
                    items.append(({'t': 'mcq', 'q': txt, 'o': opts}, kk, 'Đáp án: %s. %s' % (kk, opts['ABCD'.index(kk)])))
            else:
                a = sent[n]
                words = [w.strip() for w in txt.split('/') if w.strip()]
                items.append(({'t': 'order', 'q': 'Sắp xếp thành câu đúng:', 'words': words}, [a], 'Câu đúng: ' + a))
        pas = ''
        if s['img']:
            nm = ex.single(s['img'], 'p%d.png' % gi, w=700, h=230)
            pas += '<img class="wide" src="%s" alt="Hình">' % ex.asset(nm)
        if s['pas']:
            pas += '<p>' + ' '.join(s['pas']) + '</p>'
        ex.add('q%d' % gi, vi_instr(s['head']), items, passage=pas or None)


for n in (9, 10, 11, 12):
    src = 'De-on-thi-HK1-Anh-4-Global-De-%d' % n
    ex = Exam('on1_de%d' % n, 'OnHK1', 'Ôn HK1 – Đề %d' % n, src, slug='test%02d' % n, minutes=35, warn_at=5,
              audio=['thuvienhoclieu.com-Nghe-De-on-thi-HK1-Anh-4-Global-De-%d.mp3' % n])
    fixes, optfix = {}, {}
    if n == 12:
        fixes[8] = 'Picture d'
        ex.notes.append('Q8 đề ghi "Picture a" (trùng Q5) -> hiểu là tranh d')
    if n == 10:
        optfix[30] = ['I want some jam.', 'I want some juice.', 'I want some grapes.']
        ex.notes.append('Q6 đề ghi "Number 1" -> số 2; Q28 bỏ đáp án D "_"; Q30 sửa "som jam" -> "some jam"')
    build(ex, src, fixes, optfix)
    ex.save()
