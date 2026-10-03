# -*- coding: utf-8 -*-
"""Lớp 4 – Global Success: sinh Unit 1–20, Review 1–4, Bài mở đầu từ file Word 'Bài tập Anh 4 Global' (có phần KEY tô vàng).
Chạy: python3 tools/gen_lop4.py [thư_mục_chứa_docx]   (mặc định /mnt/user-data/uploads/04. GRADE 1-12/GRADE 04)
Mỗi bộ: luyện tập (trắc nghiệm, nối + hội thoại, đọc hiểu, sắp xếp câu, [nghe]) + 3 đề kiểm tra 20 câu (rút từ ngân hàng câu)."""
import os, re, sys, glob, json, zlib, random, pprint
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import g4_hl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = sys.argv[1] if len(sys.argv) > 1 else '/mnt/user-data/uploads/04. GRADE 1-12/GRADE 04'
TITLES = {1: 'My friends', 2: 'Time and daily routines', 3: 'My week', 4: 'My birthday party', 5: 'Things we can do', 6: 'Our school facilities', 7: 'Our timetable',
          8: 'My favourite subjects', 9: 'Our sports day', 10: 'Our summer holidays', 11: 'My home', 12: 'Jobs', 13: 'Appearance', 14: 'Daily activities',
          15: "My family's weekends", 16: 'Weather', 17: 'In the city', 18: 'At the shopping centre', 19: 'The animal world', 20: 'At summer camp'}
WARN = []
ORDER = ['Start'] + ['Unit%d' % n for n in range(1, 6)] + ['Review1'] + ['Unit%d' % n for n in range(6, 11)] + ['Review2'] + ['Unit%d' % n for n in range(11, 16)] + ['Review3'] + ['Unit%d' % n for n in range(16, 21)] + ['Review4']

# ------------------------------------------------------------------ đọc & tách bài
HEAD = re.compile(r'^⟦?(\d)\.\s+(Choose|Read|Reorder|Match|Fill|Look|Complete|Write|Circle|Tick|Find|Put|Listen|Rearrange)\b')


def clean(s):
    s = s.replace('⟦', '').replace('⟧', '')
    s = re.sub(r'\s+([.,?!;:])', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def split_opts(text):
    """'a. x b. y ⟦c. z⟧' -> (['x','y','z'], idx_đáp_án|None). Đáp án = lựa chọn chứa nhiều ký tự tô vàng nhất."""
    t, hl, on = [], [], False
    for ch in text:
        if ch == '⟦': on = True; continue
        if ch == '⟧': on = False; continue
        t.append(ch); hl.append(on)
    t = ''.join(t)
    pos, start = [], 0
    for k in range(7):
        L = chr(97 + k)
        mm = re.compile(r'(?:^|\s)[%s%s]\s?[.:]\s' % (L, L.upper())).search(t, start)
        if not mm:
            break
        pos.append((mm.start(), mm.end()))
        start = mm.end()
    opts, best, ans = [], 0, None
    for i, (s_, e_) in enumerate(pos):
        end = pos[i + 1][0] if i + 1 < len(pos) else len(t)
        opts.append(clean(t[e_:end]))
        c = sum(1 for j in range(s_, end) if hl[j] and t[j].strip())
        if c > best: best, ans = c, i
    return opts, ans


def parse_mcq(lines, name):
    qs, cur = [], None
    for ln in lines:
        m = re.match(r'^⟦?(\d+)\.\s+(?![a-g]\.\s)(.*)$', ln)
        if m and not re.match(r'^KEY', ln):
            cur = {'n': int(m.group(1)), 'q': clean(m.group(2)), 'o': ''}
            qs.append(cur)
        elif cur is not None:
            cur['o'] += ' ' + ln
    out = []
    for q in qs:
        opts, a = split_opts(q['o'].strip())
        if not opts or a is None:
            WARN.append('%s: câu %s không đọc được đáp án (%r)' % (name, q['n'], q['o'][:60]))
            continue
        out.append({'n': q['n'], 'q': q['q'], 'o': opts, 'a': a})
    return out


def keymap(lines):
    for ln in lines:
        if re.match(r'^⟦?KEY', ln):
            return {int(a): b.lower() for a, b in re.findall(r'(\d+)\.\s*([a-gA-GTF])\b', ln.replace('⟦', '').replace('⟧', ''))}
    return {}


def parse_match(lines, name):
    rows = [l for l in lines if l.startswith('|')]
    if len(rows) < 2:
        WARN.append(name + ': không thấy bảng nối'); return None
    cells = [c.strip() for c in rows[1].strip('|').split('|')]
    A = [re.sub(r'^\d+\.\s*', '', clean(x)) for x in cells[0].split('¦')]
    B = [re.sub(r'^[a-g]\.\s*', '', clean(x)) for x in cells[1].split('¦')]
    km = keymap(lines)
    left, ans = [], []
    for i, a in enumerate(A, 1):
        L = km.get(i)
        if not L:
            WARN.append('%s: nối %d thiếu đáp án' % (name, i)); continue
        left.append(a); ans.append(B[ord(L) - 97])
    return {'left': left, 'opts': B, 'ans': ans}


def parse_dialog(lines, name):
    km = keymap(lines)
    body = [l for l in lines if not re.match(r'^⟦?KEY', l)]
    inline = [l for l in body if re.match(r'^\d+\.\s+⟦?[a-g]\.\s', l)]
    blanks = {}
    if inline:                                   # mỗi chỗ trống có 3 lựa chọn riêng
        passage = [l for l in body if l not in inline]
        for l in inline:
            n = int(re.match(r'^(\d+)\.', l).group(1))
            o, a = split_opts(re.sub(r'^\d+\.\s+', '', l))
            if a is None: WARN.append('%s: chỗ trống %d thiếu đáp án' % (name, n)); continue
            blanks[n] = (o, a)
    else:
        bank_i = [i for i, l in enumerate(body) if re.match(r'^[⟦]?a\.\s.*\sb\.\s', l)]
        if not bank_i:
            WARN.append(name + ': không thấy khung từ'); return None
        bank, _ = split_opts(body[bank_i[0]])
        passage = body[:bank_i[0]] + body[bank_i[0] + 1:]
        for n in sorted(set(int(x) for x in re.findall(r'\((\d+)\)', ' '.join(passage)))):
            L = km.get(n)
            if not L: WARN.append('%s: chỗ trống %d thiếu đáp án' % (name, n)); continue
            blanks[n] = (bank, ord(L) - 97)
    txt = []
    for l in passage:
        txt.append(re.sub(r'\((\d+)\)\s*_+', r'<b>(\1)&nbsp;______</b>', clean(l)))
    ctx = {}
    full = ' '.join(clean(l) for l in passage)
    for n in blanks:
        for l in passage:
            if re.search(r'\(%d\)' % n, l):
                ctx[n] = re.sub(r'\(%d\)\s*_+' % n, '_____', clean(l)); break
    return {'html': '<br>'.join(txt), 'blanks': blanks, 'ctx': ctx}


def parse_reading(lines, head, name):
    body = [l for l in lines]
    km = keymap(body)
    tab = [l for l in body if l.startswith('|')]
    first_q = next((i for i, l in enumerate(body) if re.match(r'^1\.\s', l) or l.startswith('|')), len(body))
    passage = '<br>'.join(clean(l) for l in body[:first_q] if not re.match(r'^⟦?KEY', l))
    if tab and re.search(r'True|tick T', head):
        cells = [c.strip() for c in tab[1].strip('|').split('|')]
        sts = [re.sub(r'^\d+\.\s*', '', clean(x)) for x in cells[0].split('¦')]
        items = []
        for i, s in enumerate(sts, 1):
            v = km.get(i)
            if v not in ('t', 'f'): WARN.append('%s: ý %d thiếu T/F' % (name, i)); continue
            items.append({'q': s, 'a': v.upper()})
        return {'passage': passage, 'tf': items}
    return {'passage': passage, 'mcq': parse_mcq(body[first_q:], name)}


def parse_file(path, name):
    lines = g4_hl.dump(path)
    ki = next((i for i, l in enumerate(lines) if 'KEY' in l and 'ĐÁP ÁN' in l), None)
    if ki is None:
        WARN.append(name + ': không có phần KEY'); return None
    gi = next((i for i, l in enumerate(lines[:ki]) if l.strip().startswith('Ghi nhớ')), None)
    theory = lines[gi:ki] if gi is not None else []
    if not theory:                                  # có file để Ghi nhớ sau phần KEY
        gj = next((i for i, l in enumerate(lines[ki:], ki) if l.strip().startswith('Ghi nhớ')), None)
        theory = lines[gj:] if gj is not None else []
    key = lines[ki + 1:]
    gj = next((i for i, l in enumerate(key) if l.strip().startswith('Ghi nhớ')), None)
    if gj is not None: key = key[:gj]
    # tách bài
    heads, exp = [], 1
    for i, l in enumerate(key):
        m = HEAD.match(l)
        if m and int(m.group(1)) == exp:
            heads.append((i, clean(l))); exp += 1
    ex = []
    for k, (i, h) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(key)
        body = key[i + 1:end]
        if k + 1 == len(heads):                      # phần cuối bài + lý thuyết (không có chữ 'Ghi nhớ') dính sau bài cuối
            cut = next((j for j, l in enumerate(body) if l.startswith('|') or re.match(r'^\d+\.\s.*[Cc]ách', l)), None)
            if cut is not None:
                if not theory: theory = ['Ghi nhớ'] + body[cut:]
                body = body[:cut]
        ex.append((h, body))
    return {'ex': ex, 'theory': theory}


def build_unit(P, name):
    """P: kết quả parse_file -> dict các phần"""
    U = {'mcq1': [], 'mcq2': [], 'match': None, 'dialog': None, 'read': None, 'order': []}
    for h, body in P['ex']:
        hl = h.lower()
        if 'reorder' in hl or 'rearrange' in hl:
            U['order'] = parse_mcq(body, name + ' ex-sắp xếp')
        elif 'match' in hl:
            U['match'] = parse_match(body, name + ' ex-nối')
        elif 'dialogue' in hl:
            U['dialog'] = parse_dialog(body, name + ' ex-hội thoại')
        elif 'text' in hl:
            U['read'] = parse_reading(body, h, name + ' ex-đọc')
        elif 'complete each blank' in hl or 'to complete' in hl or 'điền' in hl.split('(')[-1]:
            U['mcq2'] = parse_mcq(body, name + ' ex2')
        elif 'choose the correct option' in hl:
            U['mcq1'] = parse_mcq(body, name + ' ex1') if not U['mcq1'] else U['mcq1']
    return U



# ------------------------------------------------------------------ bài nghe (Luyện nghe Unit 1-10)
def parse_listen(path, name):
    lines = g4_hl.dump(path)
    ki = next((i for i, l in enumerate(lines) if 'ĐÁP ÁN' in l), None)
    if ki is None:
        WARN.append(name + ': nghe không có ĐÁP ÁN'); return []
    L = lines[ki + 1:]
    blocks, cur = [], None
    for l in L:
        m = re.match(r'^Question\s+(\d+)\.?\s*(.*)$', l)
        if m:
            cur = {'n': int(m.group(1)), 'head': m.group(2), 'lines': []}; blocks.append(cur)
        elif cur is not None and not re.match(r'^LISTEN AND', l):
            cur['lines'].append(l)
    items = []
    for b in blocks:
        head = re.sub(r'^Number\s+\d+\s*:\s*', '', b['head']).strip()
        body = b['lines']
        optl = [l for l in body if re.match(r'^⟦?[A-C]\.\s', l)]
        if optl:
            txt = ' '.join(optl)
            txt = re.sub(r'(⟦?)([A-C])\.\s', lambda m: m.group(1) + m.group(2).lower() + '. ', txt)
            o, a = split_opts(txt)
            if a is None or len(o) < 2:
                WARN.append('%s: nghe câu %d thiếu đáp án' % (name, b['n'])); continue
            if len(o) == 2 and o[0].upper() == 'TRUE' and o[1].upper() == 'FALSE':
                items.append({'n': b['n'], 't': 'tf', 'q': clean(head), 'a': 'T' if a == 0 else 'F'})
            else:
                pre = clean(' '.join(l for l in body if l not in optl))
                items.append({'n': b['n'], 't': 'mcq', 'q': clean((head + ' ' + pre).strip()) or 'Nghe và chọn đáp án đúng.', 'o': o, 'a': a})
        else:
            txt = ' '.join([head] + body)
            m = re.search(r'⟦([^⟧]+)⟧', txt)
            if not m:
                WARN.append('%s: nghe câu %d (điền) thiếu đáp án tô vàng' % (name, b['n'])); continue
            ans = clean(m.group(1)).rstrip('.')
            q = clean(txt.replace(m.group(0), ' {_} ')); q = re.sub(r'[….]{2,}', '', q)
            items.append({'n': b['n'], 't': 'fill', 'q': q, 'a': ans})
    return items


def listen_page(s, items, audio_note=True):
    its = []
    for it in items:
        i = 'n.%d' % it['n']
        if it['t'] == 'mcq':
            d = s.mcq(i, 'Câu %d. %s' % (it['n'], it['q']), it['o'], it['a'])
        elif it['t'] == 'tf':
            d = s.tf(i, 'Câu %d. %s' % (it['n'], it['q']), it['a'])
        else:
            s.ANS[i] = [it['a']]; s.EXP[i] = 'Đáp án: ' + it['a']
            d = {'id': i, 't': 'fill', 'q': 'Câu %d. %s' % (it['n'], it['q'])}
        its.append(d)
    return {'id': 'nghe', 'title': 'Luyện nghe', 'mode': 'practice', 'audio': True, 'groups': [{'id': 'n', 'instr': 'Nghe file âm thanh và làm các câu theo số thứ tự trong bài nghe.', 'items': its}]}

# ------------------------------------------------------------------ SET
def theory_html(lines):
    out, tb = [], []
    def flush():
        nonlocal tb
        if tb:
            rows = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c.replace(' ¦ ', '<br>') for c in r) for r in tb)
            out.append('<table class="tb">%s</table>' % rows); tb = []
    for l in lines:
        if l.startswith('|'):
            tb.append([clean(c) for c in l.strip('|').split('|')])
        else:
            flush()
            t = clean(l)
            if t and t != 'Ghi nhớ': out.append('<p>%s</p>' % t)
    flush()
    return '<h3>Ghi nhớ</h3>' + ''.join(out) if out else ''


def shuffled(words, seed):
    w = list(words)
    for k in range(30):
        random.Random(seed + k).shuffle(w)
        if w != list(words): break
    return w


class Sets:
    def __init__(s, tag, title, U, theory, grade=4, unit=None, listen=None):
        s.tag, s.title, s.U, s.theory, s.grade, s.unit, s.listen = tag, title, U, theory, grade, unit if unit is not None else tag, listen
        s.ANS, s.EXP = {}, {}

    def mcq(s, i, q, o, a, e=None, passage=None):
        s.ANS[i] = o[a]; s.EXP[i] = e or ('Đáp án: ' + o[a])
        return {'id': i, 't': 'mcq', 'plain': True, 'q': q, 'o': list(o)}

    def order(s, i, sentence):
        words = sentence.split()
        s.ANS[i] = [sentence]; s.EXP[i] = 'Câu đúng: ' + sentence
        return {'id': i, 't': 'order', 'q': 'Sắp xếp thành câu đúng:', 'words': shuffled(words, zlib.crc32(i.encode()))}

    def match_item(s, i, M):
        s.ANS[i] = {'blanks': [[a] for a in M['ans']]}
        s.EXP[i] = '; '.join('%s → %s' % (l, a) for l, a in zip(M['left'], M['ans']))
        return {'id': i, 't': 'match', 'q': 'Nối câu ở cột A với câu phù hợp ở cột B:', 'left': M['left'], 'o': M['opts']}

    def tf(s, i, q, a):
        s.ANS[i] = a; s.EXP[i] = 'Đáp án: ' + ('True (Đúng)' if a == 'T' else 'False (Sai)')
        return {'id': i, 't': 'tf', 'q': q}

    def practice(s):
        U, pages = s.U, []
        gs, n = [], 0
        for key, gid, ins in (('mcq1', 'a', 'Choose the correct option. (Chọn đáp án đúng.)'), ('mcq2', 'b', 'Choose the correct option to complete each blank. (Chọn đáp án để hoàn thành câu.)')):
            if U[key]:
                gs.append({'id': gid, 'instr': ins, 'items': [s.mcq('%s.%d' % (gid, k), q['q'], q['o'], q['a']) for k, q in enumerate(U[key], 1)]})
        if gs: pages.append({'id': 'trac-nghiem', 'title': 'Trắc nghiệm', 'mode': 'practice', 'groups': gs})
        gs = []
        if U['match']:
            gs.append({'id': 'c', 'instr': 'Read and match each sentence in A with the appropriate sentence in B. (Nối câu.)', 'items': [s.match_item('c.1', U['match'])]})
        if U['dialog']:
            D = U['dialog']
            gs.append({'id': 'd', 'instr': 'Read the dialogue and choose the correct option to complete each blank. (Chọn từ điền vào chỗ trống.)', 'passage': D['html'],
                       'items': [s.mcq('d.%d' % k, 'Chỗ trống (%d):' % k, o, a) for k, (o, a) in sorted(D['blanks'].items())]})
        if gs: pages.append({'id': 'noi-hoi-thoai', 'title': 'Nối & hội thoại', 'mode': 'practice', 'groups': gs})
        R = U['read']
        if R and (R.get('tf') or R.get('mcq')):
            if R.get('tf'):
                its = [s.tf('e.%d' % k, x['q'], x['a']) for k, x in enumerate(R['tf'], 1)]; ins = 'Read the text and tick T (True) or F (False). (Đọc và chọn Đúng/Sai.)'
            else:
                its = [s.mcq('e.%d' % k, x['q'], x['o'], x['a']) for k, x in enumerate(R['mcq'], 1)]; ins = 'Read the text and choose the correct answers. (Đọc và chọn đáp án đúng.)'
            pages.append({'id': 'doc-hieu', 'title': 'Đọc hiểu', 'mode': 'practice', 'groups': [{'id': 'e', 'instr': ins, 'passage': R['passage'], 'items': its}]})
        if U['order']:
            its = [s.order('f.%d' % k, clean(q['o'][q['a']])) for k, q in enumerate(U['order'], 1)]
            pages.append({'id': 'sap-xep-cau', 'title': 'Sắp xếp câu', 'mode': 'practice', 'groups': [{'id': 'f', 'instr': 'Reorder the words to make meaningful sentences. (Bấm các từ để xếp thành câu.)', 'items': its}]})
        if s.listen: pages.append(s.listen(s))
        return {'id': 'lop4-%s-luyentap' % s.tag, 'title': '%s: Luyện tập' % s.title, 'grade': s.grade, 'unit': s.unit, 'theory': s.theory, 'pages': pages}

    def pool(s):
        """ngân hàng câu 1 đáp án để ghép đề: list các hàm (id)->item"""
        U, P = s.U, []
        mk = []
        for key in ('mcq1', 'mcq2'):
            mk.append([(lambda i, q=q: s.mcq(i, q['q'], q['o'], q['a'])) for q in U[key]])
        if U['match']:
            M = U['match']
            mk.append([(lambda i, l=l, a=a: s.mcq(i, l, M['opts'], M['opts'].index(a))) for l, a in zip(M['left'], M['ans'])])
        if U['dialog']:
            D = U['dialog']
            mk.append([(lambda i, k=k, o=o, a=a: s.mcq(i, 'Chọn từ cho chỗ trống: ' + D['ctx'].get(k, '(%d)' % k), o, a)) for k, (o, a) in sorted(D['blanks'].items())])
        if U['order']:
            mk.append([(lambda i, q=q: s.order(i, clean(q['o'][q['a']]))) for q in U['order']])
        # xen kẽ các nhóm để mỗi đề có đủ dạng
        out, k = [], 0
        while any(mk):
            for g in mk:
                if k < len(g): out.append(g[k])
            k += 1
            if k > 30: break
        return out

    def tests(s):
        L = s.pool(); res = []
        for t in range(3):
            s.ANS, s.EXP = {}, {}
            items = []
            for j in range(min(20, len(L))):
                items.append(L[(t * 14 + j) % len(L)]('t1.%d' % (j + 1)))
            res.append(({'id': 'lop4-%s-test%02d' % (s.tag, t + 1), 'title': '%s: Kiểm tra %d' % (s.title, t + 1), 'grade': s.grade, 'unit': s.unit, 'theory': '',
                        'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 15, 'warn_at': 2,
                                   'groups': [{'id': 't1', 'instr': 'Làm %d câu. Nộp bài để xem điểm và đáp án.' % len(items), 'items': items}]}]}, s.ANS, s.EXP))
        return res


def dump(path, name, obj):
    with open(os.path.join(ROOT, path), 'w', encoding='utf8') as f:
        f.write('# -*- coding: utf-8 -*-\n"""Sinh bởi tools/gen_lop4.py"""\n\n%s = %s\n' % (name, pprint.pformat(obj, width=160)))


def write_set(S, ANS, EXP, stem):
    dump('units/%s.py' % stem, 'SET', S)
    dump('units/%s_dapan.py' % stem, 'ANS', ANS)
    with open(os.path.join(ROOT, 'units/%s_dapan.py' % stem), 'a', encoding='utf8') as f:
        f.write('\nEXPLANATIONS = %s\n' % pprint.pformat(EXP, width=160))


def find_src(pattern):
    r = sorted(glob.glob(os.path.join(SRC, pattern)))
    return r[0] if r else None


def main(only=None):
    jobs = [('start', 'Bài mở đầu', 'Start', '*Bai-mo-dau.docx', None)]
    for n in range(1, 21):
        jobs.append(('u%d' % n, 'Unit %d – %s' % (n, TITLES[n]), 'Unit%d' % n, '*Bai-tap-Anh-4-Global-Unit-%d-*.docx' % n, n))
    for n in range(1, 5):
        jobs.append(('r%d' % n, 'Review %d' % n, 'Review%d' % n, '*Global-Review-%d.docx' % n, None))
    reg = []
    for tag, title, udir, pat, n in jobs:
        if only and tag not in only: continue
        path = find_src(pat if 'Bai-mo-dau' not in pat else '*Bai-mo-dau.docx')
        if not path:
            print('thiếu file', pat); continue
        P = parse_file(path, tag)
        if not P: continue
        U = build_unit(P, tag)
        listen, audio = None, ''
        if n and n <= 10:
            lp = find_src('*Luyen-nghe-anh-4-global-Unit-%d-*.docx' % n)
            mp = find_src('*Luyen-nghe-anh-4-global-Unit-%d-*.mp3' % n)
            if lp and mp:
                LI = parse_listen(lp, tag)
                if LI:
                    listen = (lambda s_, LI=LI: listen_page(s_, LI))
                    audio = 'audio/lop4_u%d_nghe.mp3' % n
                    dst = os.path.join(ROOT, audio)
                    if not os.path.exists(dst):
                        os.system('ffmpeg -loglevel error -y -i "%s" -ac 1 -ab 48k -ar 22050 "%s"' % (mp, dst))
        G = Sets(tag, title, U, theory_html(P['theory']), unit=n if n else udir, listen=listen)
        S = G.practice()
        write_set(S, G.ANS, G.EXP, 'lop4_%s_luyentap' % tag)
        reg.append(("lop4-%s-luyentap" % tag, 'units/lop4_%s_luyentap.py' % tag, 'units/lop4_%s_luyentap_dapan.py' % tag, 'Lop4', udir, 'luyentap', 'assets/lop4_%s/luyentap' % tag, audio))
        G2 = Sets(tag, title, U, '', unit=n if n else udir)
        for t, (T, TA, TE) in enumerate(G2.tests(), 1):
            write_set(T, TA, TE, 'lop4_%s_test%02d' % (tag, t))
            reg.append(('lop4-%s-test%02d' % (tag, t), 'units/lop4_%s_test%02d.py' % (tag, t), 'units/lop4_%s_test%02d_dapan.py' % (tag, t), 'Lop4', udir, 'test%02d' % t, 'assets/lop4_%s/test%02d' % (tag, t), ''))
        cnt = lambda k: len(U[k]) if isinstance(U[k], list) else (1 if U[k] else 0)
        print(tag, 'mcq1=%d mcq2=%d match=%s dlg=%s read=%s order=%d' % (len(U['mcq1']), len(U['mcq2']), bool(U['match']), (len(U['dialog']['blanks']) if U['dialog'] else 0), (len((U['read'] or {}).get('tf') or (U['read'] or {}).get('mcq') or [])), len(U['order'])))
    for w in WARN: print('CẢNH BÁO', w)
    return reg


if __name__ == '__main__':
    reg = main(set(sys.argv[2:]) or None) if len(sys.argv) > 2 else main()
    # ghi đăng ký (gộp vào build.py qua units/registry_lop4.py)
    old = {}
    rp = os.path.join(ROOT, 'units/registry_lop4.py')
    if os.path.exists(rp):
        ns = {}; exec(open(rp, encoding='utf8').read(), ns)
        old = {e[0]: e for e in ns['ENTRIES']}
    for e in reg: old[e[0]] = e
    with open(rp, 'w', encoding='utf8') as f:
        f.write('# -*- coding: utf-8 -*-\n"""Danh sách đăng ký Lớp 4 (sinh tự động)."""\nENTRIES = [\n')
        for e in sorted(old.values(), key=lambda x: (ORDER.index(x[4]) if x[4] in ORDER else 999, x[0])): f.write('    %r,\n' % (e,))
        f.write(']\n')
