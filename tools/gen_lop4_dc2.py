# -*- coding: utf-8 -*-
"""Lớp 4 – Đề cương ôn tập HK2 (unit 'DeCuongHK2'): 5 tài liệu -> 5 bộ luyện tập (lý thuyết + bài tập có đáp án).
Chạy: python3 tools/gen_lop4_dc2.py [a b c d e]
  dc2_a  De-cuong-on-tap-HK2-Tieng-Anh-4-Global-24-25      (lý thuyết Unit 11-20 + 25 bài tập có KEY)
  dc2_b  De-cuong-on-tap-HK2-Tieng-Anh-4-nam-24-25         (Revision 1-2: phần đọc-viết; phần nghe không có KEY nên bỏ)
  dc2_c  De-cuong-on-tap-HK2-Tieng-Anh-4-nam-25-26         (bài tập theo Unit 11-20, KHÔNG có KEY trong tài liệu -> chỉ giữ câu có đáp án duy nhất)
  dc2_d  De-cuong-on-tap-cuoi-HK2-Tieng-Anh-4-Global-24-25 (chỉ từ vựng + mẫu câu -> tự sinh trắc nghiệm từ chính tài liệu)
  dc2_e  De-cuong-on-tap-giua-HK2-Tieng-Anh-4-Global-24-25- (giữa kỳ 2: lý thuyết Unit 11-15 + 14 bài tập có KEY)
Dump docx được đọc trực tiếp từ docx gốc (có đánh dấu chỗ trống gạch chân '_____' mà dump cũ làm mất)."""
import os, re, sys, json, pprint, random, zlib, html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import g4_hl
from docx.oxml.ns import qn
from g4_exam import Exam, ROOT

DOCX = '/home/claude/g4/ex/thuvienhoclieu.com-%s.docx'
UNIT = 'DeCuongHK2'
TITLES = {11: 'My home', 12: 'Jobs', 13: 'Appearance', 14: 'Daily activities', 15: "My family's weekends", 16: 'Weather', 17: 'In the city',
          18: 'At the shopping centre', 19: 'The animal world', 20: 'At summer camp'}


# ================================================================ dump docx (giữ chỗ trống gạch chân)
def _para_text(p):
    out, cur = [], None
    for r in p.iter(qn('w:r')):
        rpr = r.find(qn('w:rPr'))
        u = rpr is not None and rpr.find(qn('w:u')) is not None and rpr.find(qn('w:u')).get(qn('w:val')) != 'none'
        t = ''.join(x.text or '' for x in r.iter(qn('w:t')))
        if r.find(qn('w:tab')) is not None: t = ('_____ ' if u else '\t') + t
        elif u and t and not t.strip(): t = '_____'
        if not t: continue
        hl = g4_hl.run_hl(r)
        if hl and not cur: out.append('⟦')
        if not hl and cur: out.append('⟧')
        cur = hl; out.append(t)
    if cur: out.append('⟧')
    s = ''.join(out).replace('\xa0', ' ')
    s = s.replace('⟧⟦', '').replace('⟦ ', ' ⟦').replace(' ⟧', '⟧ ')
    s = re.sub(r'[ \t]+', ' ', s).strip()
    s = re.sub(r'(_____ ?)+', '_____ ', s).strip()
    return s


def dump(name):
    old = g4_hl.para_text
    g4_hl.para_text = _para_text
    try:
        L = g4_hl.dump(DOCX % name)
    finally:
        g4_hl.para_text = old
    return [l.replace('⟦', '').replace('⟧', '') for l in L]


def cl(s):
    s = (s or '').replace('⟦', '').replace('⟧', '').replace(' ¦ ', ' ').replace('¦', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def cells(line):
    return [cl(c) for c in line.strip().strip('|').split(' | ')]


def blank_html(s):
    s = re.sub(r'(?:_+\s*)+', '______ ', s)
    s = re.sub(r'\s+([.,?!])', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


# ================================================================ lý thuyết HTML
def theory_html(lines, unit_head=True):
    """lines: dòng dump (đoạn + bảng). 'UNIT n' -> <h3>; dòng thường -> <p><b>; bảng liên tiếp -> table.tb"""
    out, tb = [], []

    def flush():
        nonlocal tb
        if tb:
            rows = ''
            for r in tb:
                r = list(r)
                while r and not r[-1]: r.pop()
                if not r: continue
                if len(r) == 1:
                    rows += '<tr><td colspan="3"><b>%s</b></td></tr>' % _html.escape(r[0]) if r[0].lower().startswith('example') else '<tr><td colspan="3">%s</td></tr>' % _html.escape(r[0])
                else:
                    rows += '<tr>%s</tr>' % ''.join('<td>%s</td>' % _html.escape(c) for c in r)
            out.append('<table class="tb">%s</table>' % rows); tb = []
    for l in lines:
        if l.startswith('|'):
            tb.append(cells(l))
            continue
        flush()
        t = cl(l)
        if not t: continue
        m = re.match(r'^UNIT\s*(\d+)$', t, re.I)
        if m:
            n = int(m.group(1))
            out.append('<h3>Unit %d%s</h3>' % (n, (' – ' + TITLES[n]) if n in TITLES else ''))
        elif t.lower().startswith('lưu ý'):
            out.append('<p><i>%s</i></p>' % _html.escape(t))
        else:
            out.append('<p><b>%s</b></p>' % _html.escape(t))
    flush()
    return ''.join(out)


# ================================================================ bộ dựng "luyện tập"
class Practice:
    """Dùng Exam để lấy ex.add / ex.ANS / ex.EXP, tự dựng trang mode 'practice'."""

    def __init__(self, tag, title, src_name, slug):
        self.ex = Exam(tag, UNIT, title, src_name, slug=slug)
        self.tag, self.title, self.slug = tag, title, slug
        self.pages, self.theory = [], ''
        self._start = 0

    def begin(self):
        self._start = len(self.ex.groups)

    def end(self, pid, title):
        gs = self.ex.groups[self._start:]
        if gs: self.pages.append({'id': pid, 'title': title, 'mode': 'practice', 'groups': gs})
        return len(gs)

    # --- các dạng câu
    def mcq(self, gid, instr, rows, passage=None):
        """rows: [(q, [opts], 'A'|idx, exp|None)]"""
        items = []
        for q, o, k, e in rows:
            kk = 'ABCDEFGH'[k] if isinstance(k, int) else k.upper()
            items.append(({'t': 'mcq', 'q': blank_html(q), 'o': list(o)}, kk, e or 'Đáp án: %s. %s' % (kk, o['ABCDEFGH'.index(kk)])))
        self.ex.add(gid, instr, items, passage=passage)

    def fill(self, gid, instr, rows, passage=None, bank=None):
        """rows: [(q có {_}, [đáp án], exp|None)]"""
        items = []
        for q, a, e in rows:
            a = a if isinstance(a, list) else [a]
            items.append(({'t': 'fill', 'q': q}, a, e or 'Đáp án: %s' % a[0]))
        self.ex.add(gid, instr, items, passage=passage, bank=bank)

    def tf(self, gid, instr, rows, passage=None):
        items = [({'t': 'tf', 'q': q}, a, e or 'Đáp án: %s.' % ('True (Đúng)' if a == 'T' else 'False (Sai)')) for q, a, e in rows]
        self.ex.add(gid, instr, items, passage=passage)

    def order(self, gid, instr, sentences):
        items = []
        for s in sentences:
            s = re.sub(r'\s+', ' ', s).strip()
            w = s.split()
            seed = zlib.crc32(s.encode('utf8'))
            sh = w
            for k in range(40):
                sh = list(w); random.Random(seed + k).shuffle(sh)
                if sh != w: break
            items.append(({'t': 'order', 'q': 'Sắp xếp thành câu đúng:', 'words': sh}, [s], 'Câu đúng: ' + s))
        self.ex.add(gid, instr, items)

    def match(self, gid, instr, left, opts, keys, exp):
        it = {'t': 'match', 'q': 'Nối (chọn đáp án đúng cho từng dòng):', 'left': [{'t': x} for x in left], 'o': list(opts)}
        self.ex.add(gid, instr, [(it, {'blanks': [[k] for k in keys]}, exp)])

    def open(self, gid, instr, rows, passage=None):
        """rows: [(q, đáp án mẫu)] -> câu mở (không chấm), chỉ hiện đáp án mẫu"""
        items = [({'t': 'open', 'q': q}, None, 'Đáp án mẫu: ' + a) for q, a in rows]
        self.ex.add(gid, instr, items, passage=passage)
        for it in self.ex.groups[-1]['items']: self.ex.ANS.pop(it['id'], None)

    # --- xuất
    def save(self, notes=()):
        ex = self.ex
        total = sum(len(g['items']) for p in self.pages for g in p['groups'])
        sid = 'lop4-%s' % self.tag.replace('_', '-')
        S = {'id': sid, 'title': self.title, 'grade': 4, 'unit': UNIT, 'theory': self.theory, 'pages': self.pages}
        base = 'units/lop4_%s' % self.tag
        for path, name, obj in ((base + '.py', 'SET', S), (base + '_dapan.py', 'ANS', ex.ANS)):
            with open(os.path.join(ROOT, path), 'w', encoding='utf8') as f:
                f.write('# -*- coding: utf-8 -*-\n"""Sinh bởi tools/gen_lop4_dc2.py"""\n\n%s = %s\n' % (name, pprint.pformat(obj, width=160)))
        with open(os.path.join(ROOT, base + '_dapan.py'), 'a', encoding='utf8') as f:
            f.write('\nEXPLANATIONS = %s\n' % pprint.pformat(ex.EXP, width=160))
        os.makedirs(os.path.join(ROOT, 'units/reg'), exist_ok=True)
        json.dump([sid, base + '.py', base + '_dapan.py', 'Lop4', UNIT, self.slug, 'assets/lop4_%s' % self.tag, ''],
                  open(os.path.join(ROOT, 'units/reg/%s.json' % self.tag), 'w', encoding='utf8'), ensure_ascii=False)
        d = os.path.join(ROOT, 'assets/lop4_%s' % self.tag)
        if os.path.isdir(d) and not os.listdir(d): os.rmdir(d)
        print('%-8s %3d câu / %d trang  %s' % (self.tag, total, len(self.pages), ' | '.join(list(ex.notes) + list(notes))))
        return total


# ================================================================ parser bài tập dạng "Exercise n"
def split_exercises(lines):
    """-> (exs, keylines): exs = {n: (head, [lines])} theo thứ tự; phần KEY tách riêng"""
    ki = next((i for i, l in enumerate(lines) if l.strip() == 'KEY'), len(lines))
    body, key = lines[:ki], lines[ki + 1:]
    exs, cur = {}, None
    for l in body:
        m = re.match(r'^Exercise\s+(\d+)\s*[:\.]\s*(.*)$', l.strip())
        if m:
            cur = int(m.group(1)); exs[cur] = [m.group(2).strip(), []]
        elif cur is not None:
            exs[cur][1].append(l)
    return exs, key


def parse_key(keylines):
    """-> {n: {'cells': [giá trị theo thứ tự], 'lines': [dòng chữ]}}"""
    txt = '\n'.join(keylines)
    parts = re.split(r'Exercise\s+(\d+)', txt)
    out = {}
    for i in range(1, len(parts) - 1, 2):
        n = int(parts[i]); body = parts[i + 1]
        cs, ls = [], []
        for l in body.split('\n'):
            l = l.strip()
            if not l: continue
            if l.startswith('|'):
                for c in l.strip('|').split('|'):
                    c = re.sub(r'^\d+\.\s*', '', cl(c))
                    if c: cs.append(c)
            else:
                ls.append(re.sub(r'^\d+\.\s*', '', cl(l)))
        out[n] = {'cells': cs, 'lines': ls}
    return out


def mcq_rows(lines):
    """'| 1. | q |..' + '|  | A. x | B. y |' -> [(q, [opts])]  (bỏ lựa chọn rỗng / ảnh)"""
    out, q = [], None
    for l in lines:
        if not l.startswith('|'): continue
        c = cells(l)
        if re.match(r'^\d+\.$', c[0]) and len(c) > 1 and c[1]:
            q = c[1]
        elif q is not None and c[0] == '' and any(re.match(r'^[A-D]\.', x) for x in c):
            opts = []
            for x in c[1:]:
                m = re.match(r'^([A-D])\.\s*(.*)$', x)
                if m and m.group(2) and not m.group(2).startswith('[img'): opts.append(m.group(2).strip())
            out.append((q, opts)); q = None
    return out


def match_rows(lines):
    """'| 1. | Q |  | A. | ans |' -> (lefts, opts)"""
    L, O = [], []
    for l in lines:
        if not l.startswith('|'): continue
        c = [x for x in cells(l)]
        m = re.match(r'^(\d+)\.$', c[0])
        if m and len(c) >= 3 and not re.match(r'^\d+\.$', c[1]):
            L.append(c[1])
            # đáp án nằm ở hai ô cuối: 'A.' , 'text'
            for i, x in enumerate(c):
                if re.match(r'^[A-E]\.$', x) and i + 1 < len(c): O.append(c[i + 1])
    return L, O


def order_items(lines):
    return [cells(l)[1] for l in lines if l.startswith('|') and re.match(r'^\d+\.$', cells(l)[0]) and '/' in l]


def letters(cs):
    return [c.strip().upper() for c in cs]


# ================================================================ A & E: họ "Exercise n" có KEY
TYPO = {'togehter': 'together', 'wather': 'water'}
# đáp án trong KEY của đề cương sai (đã đối chiếu ngữ pháp) -> sửa, ghi vào notes
MCQ_FIX = {(6, 1): ('A', 'Đề cương ghi D (Done) nhưng "___ you have a brother?" cần trợ động từ Do.'),
           (6, 6): ('B', 'Đề cương ghi A (big) nhưng người nặng 36 kg là "slim" (mảnh khảnh).'),
           (9, 4): ('A', 'Đề cương ghi B (does) nhưng chủ ngữ "I" đi với do.'),
           (9, 5): ('B', 'Đề cương ghi A (read) nhưng "My family" là chủ ngữ số ít → reads (như câu "My family watches TV").')}
EX7_FIX = {6: 'are'}   # "My grandfather and grandmother ___ old": KEY ghi "is" nhưng chủ ngữ số nhiều
EX8_ANS = [  # câu sửa đúng (KEY chỉ ghi phần sửa) – 8 sửa lại "are => slim" thành "is"
    (['Today is Monday.'], 'Bỏ "on": Today is Monday (trước thứ trong tuần ở câu "Today is…" không dùng on).'),
    (['He has long hair.'], 'Bỏ "a": hair là danh từ không đếm được.'),
    (['She has a small face.'], 'have → has (chủ ngữ she).'),
    (['What does your mother look like?'], 'do → does (chủ ngữ your mother).'),
    (['My father has a round face.'], 'an → a (round bắt đầu bằng phụ âm).'),
    (['My little sister has big eyes.'], 'have → has (chủ ngữ my little sister).'),
    (['My mother has beautiful hands.'], 'hand → hands (bộ phận cơ thể có hai cái dùng số nhiều).'),
    (['My grandfather is slim.'], 'are → is (chủ ngữ số ít). KEY ghi "are => slim" là sai chính tả của đề cương.'),
    (['Do you have a sister?'], 'does → do (chủ ngữ you).'),
    (["No, I don't. I have a brother."], 'do → don\'t (trả lời phủ định).')]


def build_family(P, lines, pages_plan, notes, which):
    """lines: dump docx; pages_plan: [(pid, title, [số bài])]"""
    exs, key = split_exercises(lines)
    K = parse_key(key)
    ex = P.ex
    stub = {}

    def mcq_block(n):
        h, ls = exs[n]
        rows = mcq_rows(ls)
        ks = letters(K[n]['cells'])
        assert len(rows) == len(ks) == 10, (n, len(rows), len(ks))
        out = []
        for i, ((q, o), k) in enumerate(zip(rows, ks), 1):
            e = None
            if '_' not in q:   # docx để chỗ trống bằng khoảng trắng (không gạch chân)
                q = {'What does look like?': 'What does _____ look like?', 'you have a brother?': '_____ you have a brother?'}[q]
            if (n, i) in MCQ_FIX:
                k, why = MCQ_FIX[(n, i)]
                e = 'Đáp án: %s. %s. %s' % (k, o['ABCD'.index(k)], why)
                notes.append('%s Ex%d.%d: sửa key' % (which, n, i))
            out.append((q, o, k, e))
        P.mcq('e%d' % n, 'Exercise %d. Read and circle the best answer. (Chọn đáp án đúng nhất.)' % n, out)

    def match_block(n):
        h, ls = exs[n]
        L, O = match_rows(ls)
        ks = letters(K[n]['cells'])
        assert len(L) == len(ks) == len(O) == 5, (n, L, O, ks)
        keys = [O['ABCDE'.index(k)] for k in ks]
        P.match('e%d' % n, 'Exercise %d. Match each question with a suitable answer. (Nối câu hỏi với câu trả lời phù hợp.)' % n, L, O, keys,
                '; '.join('%d – %s' % (i, k) for i, k in enumerate(ks, 1)) + '. ' + ' | '.join('%s → %s' % (l, a) for l, a in zip(L, keys)))

    def order_block(n, skip_fill=None):
        h, ls = exs[n]
        its = order_items(ls)
        sents = [TYPO_FIX(s) for s in K[n]['lines']]
        if n == 11:   # KEY thiếu câu 4 (đã có đủ từ trong đề: Do you wash your clothes in the afternoon?)
            assert len(sents) == 4 and len(its) == 5
            sents.insert(3, 'Do you wash your clothes in the afternoon?')
            notes.append('%s Ex11.4: KEY thiếu, tự ghép từ đề' % which)
        assert len(sents) == len(its), (n, len(sents), len(its))
        P.order('e%d' % n, 'Exercise %d. Reorder the words to make sentences. (Sắp xếp từ thành câu.)' % n, sents)

    def TYPO_FIX(s):
        for a, b in TYPO.items(): s = s.replace(a, b)
        return s

    def ex7():
        h, ls = exs[7]
        qs = [cells(l)[1] for l in ls if l.startswith('|') and re.match(r'^\d+\.$', cells(l)[0])]
        ans = [a.lower() if i else a for i, a in enumerate(K[7]['cells'])]
        ans = [a.lower() for a in K[7]['cells']]
        assert len(qs) == len(ans) == 6
        rows = []
        for i, (q, a) in enumerate(zip(qs, ans), 1):
            q = re.sub(r'(?:\s*_{2,})+\s*', ' {_} ', q); q = re.sub(r'\s+([.,?!])', r'\1', q).strip()
            e = None
            if i in EX7_FIX:
                e = 'Đáp án: %s (chủ ngữ số nhiều). Đề cương ghi "%s".' % (EX7_FIX[i], a); a = EX7_FIX[i]
                notes.append('%s Ex7.%d: sửa key' % (which, i))
            rows.append((q, [a], e))
        P.fill('e7', 'Exercise 7. Complete these sentences by filling in the blank. (Điền từ vào chỗ trống.)', rows)

    def ex8():
        h, ls = exs[8]
        sents = [cells(l)[1] for l in ls if l.startswith('|') and re.match(r'^\d+\.$', cells(l)[0])]
        assert len(sents) == 10
        rows = [('Tìm lỗi sai và viết lại câu đúng: <i>%s</i><br>{_}' % s, a, 'Câu đúng: %s %s' % (a[0], e)) for s, (a, e) in zip(sents, EX8_ANS)]
        P.fill('e8', 'Exercise 8. Find mistakes in each sentence and correct them. (Tìm lỗi sai và viết lại cả câu cho đúng.)', rows)

    def ex10():
        h, ls = exs[10]
        sent = {}
        for l in ls:
            if not l.startswith('|'): continue
            c = [x for x in cells(l) if x]
            c = [x for x in c if not re.match(r'^_+$', x)]
            if len(c) >= 2:
                sent[c[0].rstrip(':').strip()] = c[1]
        seq = letters(K[10]['cells'])   # thứ tự đúng
        assert sorted(seq) == sorted(sent), (seq, sent)
        pas = '<p>' + '</p><p>'.join('<b>%s:</b> %s' % (k, sent[k]) for k in sorted(sent)) + '</p>'
        items = []
        for k in sorted(sent):
            pos = seq.index(k) + 1
            items.append(({'t': 'mcq', 'plain': True, 'q': 'Câu %s đứng ở vị trí thứ mấy trong đoạn hội thoại?' % k, 'o': ['1', '2', '3', '4', '5', '6']}, str(pos),
                          'Thứ tự đúng: %s. Câu %s ở vị trí %d.' % (' – '.join(seq), k, pos)))
        ex.add('e10', 'Exercise 10. Read and number the sentences in the correct order. (Đọc và đánh số thứ tự câu trong hội thoại.)', items, passage=pas)

    def tf_block(n):
        h, ls = exs[n]
        txt = ' '.join(cl(l) for l in ls if not l.startswith('|'))
        sts = [cells(l)[1] for l in ls if l.startswith('|') and re.match(r'^\d+\.$', cells(l)[0])]
        ks = letters(K[n]['cells'])
        assert len(sts) == len(ks)
        P.tf('e%d' % n, 'Exercise %d. Read and decide whether these sentences are True (T) or False (F). (Đọc đoạn văn, True hay False?)' % n,
             [(s, k, None) for s, k in zip(sts, ks)], passage='<p>%s</p>' % _html.escape(txt))

    def open_block(n):
        h, ls = exs[n]
        txt = ' '.join(cl(l) for l in ls if not l.startswith('|'))
        qs = [cells(l)[1] for l in ls if l.startswith('|') and re.match(r'^\d+\.$', cells(l)[0])]
        ans = [a.replace('Mr.Long', 'Mr. Long') for a in K[n]['lines']]
        assert len(qs) == len(ans) == 5
        P.open('e%d' % n, 'Exercise %d. Read the passage and answer the questions. (Đọc đoạn văn và trả lời câu hỏi – tự viết, xem đáp án mẫu.)' % n,
               [(q, a) for q, a in zip(qs, ans)], passage='<p>%s</p>' % _html.escape(txt))
        notes.append('%s Ex%d: đề ghi T/F nhưng thực chất là câu hỏi -> dạng mở' % (which, n))

    for pid, title, nums in pages_plan:
        P.begin()
        for n in nums:
            h = exs[n][0].lower()
            if n == 7: ex7()
            elif n == 8: ex8()
            elif n == 10: ex10()
            elif 'match' in h: match_block(n)
            elif 'circle' in h: mcq_block(n)
            elif 'reorder' in h: order_block(n)
            elif 'true (t)' in h and n == 19: tf_block(n)
            elif 'true (t)' in h: open_block(n)
            else: raise Exception('chưa xử lý Exercise %d: %s' % (n, h))
        P.end(pid, title)


def theory_lines(lines, insert_unit19=False):
    ci = next(i for i, l in enumerate(lines) if l.startswith('ÔN BÀI TẬP'))
    th = [l for l in lines[:ci] if not re.match(r'^(ĐỀ CƯƠNG|ÔN LÝ THUYẾT)', l.strip())]
    if insert_unit19:
        j = next(i for i, l in enumerate(th) if 'What are these animals?' in l and l.startswith('| Để hỏi'))
        th.insert(j, 'UNIT 19')
    return [l.replace('Các hỏi về', 'Cách hỏi về') for l in th]


def build_a():
    name = 'De-cuong-on-tap-HK2-Tieng-Anh-4-Global-24-25'
    P = Practice('dc2_a', 'Đề cương HK2 (24-25) A – Global: Unit 11–20', name, 'luyentap_a')
    L = dump(name)
    P.theory = '<h3>Đề cương ôn tập Tiếng Anh lớp 4 – Kì 2 (Global Success)</h3>' + theory_html(theory_lines(L, True))
    notes = []
    build_family(P, L, [('unit-11-12', 'Unit 11–12', [1, 2, 3, 4, 5]), ('unit-13', 'Unit 13: Appearance', [6, 7, 8]), ('unit-14', 'Unit 14: Daily activities', [9, 10, 11]),
                        ('unit-15-16', 'Unit 15–16', [12, 13, 14, 15, 16, 17]), ('unit-17-19', 'Unit 17–19', [18, 19, 20, 21, 22]), ('unit-20', 'Unit 20: At summer camp', [23, 24, 25])], notes, 'A')
    return P.save(notes)


def build_e():
    name = 'De-cuong-on-tap-giua-HK2-Tieng-Anh-4-Global-24-25-'
    P = Practice('dc2_e', 'Đề cương HK2 (24-25) E – Giữa kì 2: Unit 11–15', name, 'luyentap_e')
    L = dump(name)
    P.theory = '<h3>Đề cương ôn tập Tiếng Anh lớp 4 – Giữa kì 2</h3>' + theory_html(theory_lines(L))
    notes = []
    build_family(P, L, [('unit-11-12', 'Unit 11–12', [1, 2, 3, 4, 5]), ('unit-13', 'Unit 13: Appearance', [6, 7, 8]), ('unit-14', 'Unit 14: Daily activities', [9, 10, 11]),
                        ('unit-15', 'Unit 15: My family\'s weekends', [12, 13, 14])], notes, 'E')
    return P.save(notes)


# ================================================================ C: bài tập theo Unit (đề cương 25-26) – tài liệu KHÔNG có KEY
def unit_blocks(lines):
    """-> {unit: {bài: [dòng]}}"""
    out, u, b = {}, None, None
    for l in lines:
        t = re.sub(r'(?<=[a-z])[A-Z]\b', lambda m: m.group().lower(), cl(l))   # 'postcarD' -> 'postcard' (lỗi định dạng của docx)
        m = re.match(r'^\W*UNIT\s+(\d+)\s*:', t)
        if m:
            u = int(m.group(1)); out[u] = {}; b = None; continue
        m = re.match(r'^\W*B[àa]i\s+(\d+)\s*:', t)
        if m and u:
            b = int(m.group(1)); out[u][b] = []; continue
        if u and b and t:
            out[u][b].append(t)
    return out


def split_abc(text):
    """'stem A. x B. y C. z' -> (stem, [x,y,z])"""
    text = text.replace(' ', ' ')
    pos, start = [], 0
    for L in 'ABC':
        m = re.compile(r'(?:^|(?<=[\s\?\.:!]))%s\.\s' % L).search(text, start)
        if not m: return text, []
        pos.append((m.start(), m.end())); start = m.end()
    stem = text[:pos[0][0]].strip()
    opts = [text[e:(pos[i + 1][0] if i + 1 < 3 else len(text))].strip() for i, (s_, e) in enumerate(pos)]
    return stem, opts


def words_ok(doc_line, sentence):
    """kiểm tra từ trong đề (a / b / c) trùng với câu đáp án của mình"""
    d = doc_line.split('👉')[0]
    toks = [x.strip() for x in d.split('/') if x.strip()]
    norm = lambda s: sorted(re.sub(r"[^\w' ]", '', s.replace('’', "'").lower()).split())
    return norm(' '.join(toks)) == norm(sentence)


# key (do mình giải – tài liệu không có đáp án). None = bỏ câu (đáp án không duy nhất / đề lỗi)
C_DATA = {
    11: {'mcq': 'CB-BA', 'mcqskip': {3: 'on a ___ street: big/busy đều hợp lý'},
         'order': ['I live at Hai Ba Trung Street.', 'This is a noisy street.', 'There is a big school.', 'He lives on Hoang Van Thu Road.', 'The street is very quiet.'],
         'fill': [['live'], ['at'], ['road'], ['busy'], ['quiet']],
         'b5': [['live'], ['busy', 'big'], ['noisy'], ['quiet'], ['road', 'street']]},
    12: {'mcq': 'BACBA', 'match': ['C', 'E', 'A', 'D', 'B'],
         'fill': [['farmer'], ['actor'], ['policeman'], ['hospital'], ['factory']],
         'order': ['She is a nurse.', 'My brother works in a factory.', 'My dad is a policeman.', None, None],
         'b5': 'BCABC'},
    13: {'mcq': 'B-CAB', 'match': ['B', 'C', 'E', 'D', 'A'],
         'fill': [['tall'], ['big'], ['hair'], ['short'], ['round']],
         'order': ['She has a round face.', 'He has long hair.', 'Her eyes are big.', 'She is very slim.', 'My brother is short.'],
         'b5': 'BBACC'},
    14: {'mcq': 'BCCAA', 'match': ['C', 'A', 'B', 'E', 'D'],
         'fill': [['morning'], ['noon'], ['wash'], ['help'], ['clean']],
         'order': ['I get up early in the morning.', 'I help dad with the cooking.', 'She always washes the dishes.', 'They clean the floor.', 'I go shopping in the afternoon.'],
         'b5': [['morning'], ['help with the cooking'], ['noon'], ['wash the clothes'], ['evening'], ['clean the floor'], ['wash the dishes']]},
    15: {'mcq': 'CBABA', 'match': {1: 'E', 3: 'B', 4: 'D', 5: 'A'},
         'fill': [['shopping centre'], ['play tennis'], ['cook meals'], ['do yoga'], ['cinema']],
         'order': ['I often go to the cinema.', 'They do yoga in the morning.', 'We always cook meals for dinner.', 'I play tennis at the sports centre.', 'We go to the swimming pool.']},
    16: {'mcq': 'BCABB', 'match': ['B', 'C', 'A', 'D', 'E'],
         'fill': [['windy'], ['supermarket'], ['food stall'], ['cloudy'], ['water park']],
         'order': ['I go to the bakery every morning.', 'The weather is sunny today.', 'I buy books at the bookshop.', 'It is very windy today.', 'We eat noodles at the food stall.'],
         'b5': {1: ['cloudy'], 2: ['bookshop'], 4: ['supermarket'], 5: ['food stall']}},
    17: {'mcq': 'A-BAB', 'match': ['C', 'A', 'D', 'B', 'E'],
         'fill': [['turn'], ['get'], ['go straight'], ['stop'], ['right']],
         'order': ['Go straight and turn left.', 'Turn right at the bookstore.', 'Stop at the red light.', 'I want to get to the zoo.', 'You can turn round.'],
         'b5': ['Go straight, go straight, turn right, stop, get to the zoo.', 'Go straight, turn left, go straight, turn round, get to the bakery.',
                'Go straight, go straight, turn right, turn left, stop.', 'Go straight, turn left, go straight, turn right, get to the hospital.',
                'Turn right, go straight, stop, turn round, get to the supermarket.']},
    18: {'mcq': 'BBABC', 'match': ['B', 'A', 'C', 'D', 'E'],
         'fill': [['gift shop'], ['opposite', 'behind'], ['skirt'], ['behind', 'opposite'], ['thousand']],
         'order': [None, 'How much is the skirt?', 'I want to buy that T-shirt.', 'The gift shop is near the school.', 'It costs one thousand dong.'],
         'b5': [['thousand'], ['opposite'], ['between']]},
    19: {'mcq': 'BCBAC', 'match': ['B', 'C', 'A', 'D', 'E'],
         'fill': [['roar'], ['beautifully', 'loudly'], ['giraffe'], ['crocodile'], ['loudly', 'beautifully']],
         'order': ['The lion roared loudly.', 'Hippos can run quickly.', 'The bird sang beautifully.', 'The children are dancing merrily.', 'We saw the crocodile.']},
    20: {'mcq': 'BABBC', 'match': ['C', 'D', 'B', 'A', 'E'],
         'fill': [['sing songs', 'play card games', 'tell a story'], ['build a campfire'], ['play card games', 'sing songs', 'tell a story'], ['put up a tent'], ['tell a story', 'sing songs', 'play card games']],
         'order': ['They put up a tent.', 'We played card games.', 'I took a photo of the mountain.', 'They sang songs around the campfire.', 'He told a funny story.'],
         'b5': [['We take a photo of the mountains.', 'We took a photo of the mountains.'], ['My brother plays card games by himself.'], ['They put up a tent next to the river.'],
                ['We sat by the fire and told a story.', 'We sat by the fire and tell a story.'], ['Every night, we sing songs around the campfire.']]},
}



C_BANK = {  # khung từ (đề U12 ghi 'farm' nhưng câu cần 'farmer')
    11: ['busy', 'quiet', 'road', 'live', 'at'], 12: ['hospital', 'actor', 'farmer', 'policeman', 'factory'],
    13: ['short', 'big', 'hair', 'tall', 'round'], 14: ['morning', 'noon', 'help with the cooking', 'wash', 'clean'],
    15: ['do yoga', 'shopping centre', 'cook meals', 'cinema', 'play tennis'], 16: ['windy', 'supermarket', 'food stall', 'cloudy', 'water park'],
    17: ['turn', 'get', 'stop', 'right', 'go straight'], 18: ['skirt', 'opposite', 'thousand', 'gift shop', 'behind'],
    19: ['loudly', 'roar', 'giraffe', 'beautifully', 'crocodile'], 20: ['sing songs', 'play card games', 'tell a story', 'build a campfire', 'put up a tent']}
C_TITLE = {11: 'Unit 11: My home', 12: 'Unit 12: Jobs', 13: 'Unit 13: Appearance', 14: 'Unit 14: Daily activities', 15: "Unit 15: My family's weekends",
           16: 'Unit 16: Weather', 17: 'Unit 17: In the city', 18: 'Unit 18: At the shopping centre', 19: 'Unit 19: The animal world', 20: 'Unit 20: At summer camp'}


def slots(q):
    q = re.sub(r'(?:_+\s*)+', ' {_} ', q)
    q = re.sub(r'\s+([.,?!])', r'\1', q)
    return re.sub(r'\s+', ' ', q).strip()


def build_c():
    name = 'De-cuong-on-tap-HK2-Tieng-Anh-4-nam-25-26'
    P = Practice('dc2_c', 'Đề cương HK2 (25-26) C – Bài tập theo Unit 11–20', name, 'luyentap_c')
    B = unit_blocks(dump(name))
    notes = ['tài liệu không có KEY: đáp án do soạn giả tự giải, chỉ giữ câu có đáp án duy nhất']
    th = []
    for u in range(11, 21):
        D, blk = C_DATA[u], B[u]
        P.begin()
        # ---- Bài 1: trắc nghiệm A/B/C
        qs = [split_abc(l) for l in blk[1] if split_abc(l)[1]]
        assert len(qs) == 5 and len(D['mcq']) == 5, (u, len(qs))
        rows = []
        for (stem, o), k in zip(qs, D['mcq']):
            if k == '-':
                notes.append('U%d b1: bỏ "%s" (đáp án không duy nhất)' % (u, stem[:35])); continue
            e = 'Đáp án: %s. %s. Theo mẫu câu của đề cương: I live in + tên phố (on cũng có thể dùng trong tiếng Anh thực tế).' % (k, o['ABC'.index(k)]) if stem.startswith('I live') else None
            rows.append((stem, o, k, e))
        P.mcq('u%dmcq' % u, 'Bài 1. Multiple Choice – chọn đáp án đúng A, B hoặc C.', rows)
        # ---- Bài 2: nối
        if 'match' in D:
            lefts, opts = [], []
            for l in blk[2]:
                if not l.startswith('|'): continue
                c = [x.strip() for x in l.strip('|').split('|')]
                if re.match(r'^\d+\.', c[0]): lefts.append(re.sub(r'^\d+\.\s*', '', c[0]))
                if re.match(r'^[A-Ea-e]\.', c[1]): opts.append(re.sub(r'^[A-Ea-e]\.\s*', '', c[1]))
            assert len(lefts) == len(opts) == 5, (u, lefts, opts)
            mk = D['match']
            idx = list(range(1, 6)) if isinstance(mk, list) else sorted(mk)
            kk = mk if isinstance(mk, list) else [mk[i] for i in idx]
            for i in range(1, 6):
                if i not in idx: notes.append('U%d b2: bỏ dòng "%s" (2 đáp án hợp lý)' % (u, lefts[i - 1]))
            th.append('<h3>%s</h3><table class="tb">%s</table>' % (C_TITLE[u], ''.join('<tr><td><b>%s</b></td><td>%s</td></tr>' % (_html.escape(lefts[i - 1]), _html.escape(opts['ABCDE'.index(k.upper())])) for i, k in zip(idx, kk))))
            P.match('u%dmatch' % u, 'Bài 2. Match – nối từ/cụm từ với nghĩa hoặc nơi phù hợp.', [lefts[i - 1] for i in idx], opts,
                    [opts['ABCDE'.index(k.upper())] for k in kk], '; '.join('%s → %s' % (lefts[i - 1], opts['ABCDE'.index(k.upper())]) for i, k in zip(idx, kk)))
        # ---- Bài 3 / 4: điền từ & sắp xếp (U11 đảo thứ tự)
        bf, bo = (4, 3) if u == 11 else (3, 4)
        qlines = [l for l in blk[bf] if '_' in l]
        assert len(qlines) == 5 == len(D['fill']), (u, qlines)
        P.fill('u%dfill' % u, 'Bài %d. Fill in the blanks – điền từ thích hợp vào chỗ trống.' % bf,
               [(slots(q), a, None) for q, a in zip(qlines, D['fill'])], bank=C_BANK[u])
        olines = [l for l in blk[bo] if '/' in l]
        assert len(olines) == 5 == len(D['order']), (u, olines)
        sents = []
        for ol, s_ in zip(olines, D['order']):
            if s_ is None:
                notes.append('U%d b%d: bỏ "%s" (đề thiếu/thừa từ)' % (u, bo, ol.split('👉')[0].strip())); continue
            for s1 in ([s_] if isinstance(s_, str) else s_[:1]):
                if not words_ok(ol, s1): notes.append('U%d b%d: từ trong đề khác đáp án "%s"' % (u, bo, s1))
            sents.append(s_)
        P.order('u%dorder' % u, 'Bài %d. Reorder the words – sắp xếp các từ thành câu đúng.' % bo, sents)
        # ---- Bài 5: theo từng unit
        b5 = blk.get(5, [])
        if u == 11:
            txt = b5[2]
            blanks = re.findall(r'\((\d+)\)', txt)
            pas = '<p>' + re.sub(r'\((\d+)\)\s*(?:_+\s*)+', lambda m: '<b>(%s) ______</b> ' % m.group(1), txt) + '</p>'
            P.fill('u11b5', 'Bài 5. Read and Complete – điền từ trong khung vào chỗ trống (có 1 từ thừa): road, street, live, quiet, busy, noisy, big.',
                   [('Chỗ trống (%d): {_}' % (i + 1), a, None) for i, a in enumerate(D['b5'])], passage=pas, bank=['road', 'street', 'live', 'quiet', 'busy', 'noisy', 'big'])
        elif u in (12, 13):
            pas = '<p>%s</p>' % _html.escape(b5[0])
            rows = []
            for l, k in zip(b5[1:], D['b5']):
                stem, o = split_abc(l)
                rows.append((stem, o, k, None))
            P.mcq('u%db5' % u, 'Bài 5. Read & Choose – đọc đoạn văn và chọn đáp án đúng.', rows, passage=pas)
        elif u == 14:
            txt = b5[2]
            pas = re.sub(r'\((\d+)\)\s*(?:_+\s*)+', lambda m: '<b>(%s) ______</b> ' % m.group(1), txt)
            pas = '<p>' + re.sub(r'(?<=[\.\?!])\s*(Nam|Mai):', r'<br>\1:', pas) + '</p>'
            P.fill('u14b5', 'Bài 5. Fill in the Blanks – hoàn thành hội thoại bằng các cụm trong khung.',
                   [('Chỗ trống (%d): {_}' % (i + 1), a, None) for i, a in enumerate(D['b5'])], passage=pas,
                   bank=['morning', 'noon', 'evening', 'clean the floor', 'wash the clothes', 'wash the dishes', 'help with the cooking'])
        elif u == 15:
            notes.append('U15 b5: bỏ (kế hoạch cuối tuần – câu trả lời tự do)')
        elif u == 16:
            ml = [l for l in b5 if '👉' in l]
            rows = []
            for i, l in enumerate(ml, 1):
                if i in D['b5']:
                    rows.append(('Tìm từ sai và sửa lại: <i>%s</i><br>Từ đúng: {_}' % l.split('👉')[0].strip(), D['b5'][i], None))
                else:
                    notes.append('U16 b5: bỏ câu %d (đáp án không rõ)' % i)
            P.fill('u16b5', "Bài 5. Spot the Mistake – tìm từ sai trong câu và viết từ đúng (gợi ý: cloudy, bookshop, supermarket, food stall, windy).", rows,
                   bank=['cloudy', 'bookshop', 'supermarket', 'food stall', 'windy'])
        elif u == 17:
            ml = [l.split('👉')[0].strip() for l in b5 if '👉' in l]
            P.open('u17b5', 'Bài 5. Secret Code – giải mã chỉ dẫn (GS = go straight, TL = turn left, TR = turn right, ST = stop, TT = turn round, GT = get to). Tự viết, xem đáp án mẫu.',
                   [(m, a) for m, a in zip(ml, D['b5'])])
        elif u == 18:
            txt = ' '.join(b5[2:4])
            pas = '<p>' + _html.escape(re.sub(r'_+\s*', '…… ', txt)) + '</p>'
            fl = [l for l in b5 if l.startswith('The ') and '_' in l and ('standing' in l or 'between' in l or l.startswith('The price'))]
            fl = [l for l in b5[5:] if 'pink' not in l and 'white' not in l]
            assert len(fl) == 3 == len(D['b5']), fl
            P.fill('u18b5', 'Bài 5. Read and Complete – đọc đoạn văn rồi điền từ vào chỗ trống (khung từ: T-shirt, skirt, thousand).',
                   [(slots(q), a, None) for q, a in zip(fl, D['b5'])], passage=pas)
            notes.append('U18 b5: bỏ 2 câu pink/white (skirt–T-shirt hoán đổi được)')
        elif u == 19:
            notes.append('U19 b5: bỏ (hội thoại có 8 chỗ trống, 7 từ -> đáp án không duy nhất)')
        elif u == 20:
            ml = [l.split('→')[0].strip() for l in b5 if '→' in l]
            P.fill('u20b5', 'Bài 5. Find the Mistake – tìm lỗi sai và viết lại cả câu cho đúng.',
                   [('Sửa lỗi sai: <i>%s</i><br>{_}' % m, a, 'Câu đúng: %s' % a[0]) for m, a in zip(ml, D['b5'])])
        P.end('unit-%d' % u, C_TITLE[u])
    P.theory = ('<h3>Đề cương ôn tập HK2 năm học 2025–2026 – Tiếng Anh 4</h3><p>Tài liệu chỉ gồm bài tập theo từng Unit. Bảng dưới là từ vựng/cụm từ cùng nghĩa hoặc mô tả lấy từ Bài 2 (Match) của mỗi Unit.</p>'
                '<h3>Unit 11: My home</h3><p>Từ cần nhớ: road, street, big, busy, quiet, noisy, live, at, in.</p>' + ''.join(th))
    return P.save(notes)

# ================================================================ B: Revision 1–2 (phần đọc–viết; phần nghe không có KEY/script nên bỏ)
def build_b():
    name = 'De-cuong-on-tap-HK2-Tieng-Anh-4-nam-24-25'
    P = Practice('dc2_b', 'Đề cương HK2 (24-25) B – Revision 1–2 (đọc–viết)', name, 'luyentap_b')
    L = [cl(l) for l in dump(name)]
    notes = ['bỏ phần Listening (Rev.1: 3 task, Rev.2: 2 task) vì không có KEY/audio script; mp3 De-1/De-2 chưa dùng', 'bỏ Rev.1 Reading T/F (câu dựa vào tranh, không có KEY), Rev.2 Reading Task 1 (nối tranh) và Task 4 (viết đoạn văn)']
    txt = '\n'.join(L)
    r1, r2 = txt.split('REVISION 2')

    def passage_of(part, start_pat):
        m = re.search(start_pat + r'\s*\n(.+)', part)
        return m.group(1).strip()

    def cloze(part, bank_line_pat):
        m = re.search(r'Task 3\. Read and complete[^\n]*\n(?:\[img[^\n]*\n)?[^\n]*\n(.+)', part)
        return m.group(1).strip()
    # ---------- Revision 1
    P.begin()
    pas1 = passage_of(r1, r'Task 2\. Read and answer[^\n]*')
    P.fill('r1t2', 'Revision 1 – Task 2. Read and answer. Use ONE WORD and/or A NUMBER for each gap. (Đọc và trả lời.)', [
        ('What is the weather like today?<br>Answer: {_}', ['sunny'], 'Đáp án: sunny (Today is a sunny day).'),
        ('Where’s the shopping centre? – It’s opposite the {_}.', ['cinema'], 'Đáp án: cinema (It is opposite the cinema).'),
        ('What does Lan want to buy?<br>Answer: {_}', ['a book', 'book'], 'Đáp án: a book (Lan wants to buy a book about giraffes).'),
        ('What animals does Lan like?<br>Answer: {_}', ['giraffes', 'giraffe'], 'Đáp án: giraffes.'),
        ('How much is the T-shirt?<br>Answer: {_}', ['seventy thousand', '70,000', '70.000', '70000', 'seventy thousand dong', '70,000 dong'], 'Đáp án: seventy thousand (dong) = 70,000 dong.')],
        passage='<p>%s</p>' % _html.escape(pas1))
    c1 = passage_of(r1, r'campsite thirty thousand rainy go straight rain water park')
    c1 = re.sub(r'\((\d)\)\s*(?:_+\s*)+', lambda m: '<b>(%s) ______</b> ' % m.group(1), c1)
    P.fill('r1t3', 'Revision 1 – Task 3. Read and complete. There is ONE extra option. (Điền từ trong khung, có 1 từ thừa.)',
           [('Chỗ trống (%d): {_}' % (i + 1), [a], None) for i, a in enumerate(['rainy', 'water park', 'campsite', 'go straight', 'thirty thousand'])],
           passage='<p>%s</p>' % c1, bank=['campsite', 'thirty thousand', 'rainy', 'go straight', 'rain', 'water park'])
    P.order('r1t4', 'Revision 1 – Task 4. Rearrange the words to make complete sentences. (Sắp xếp từ thành câu.)',
            ['The boys and the girls are playing tug of war.', 'The giraffes have long necks, and they can run quite fast.', 'The boys and the girls are putting up tents.', 'The students are playing tug of war.'])
    notes.append('Rev.1 Task 4: bỏ câu 3 ("the playing cards tent. The students in game are" – đề thiếu/thừa từ); câu sắp xếp tự ghép từ các từ trong đề')
    P.end('revision-1', 'Revision 1')
    # ---------- Revision 2
    P.begin()
    pas2 = passage_of(r2, r'Task 2\. Read and answer[^\n]*')
    P.fill('r2t2', 'Revision 2 – Task 2. Read and answer. Use ONE WORD and/or A NUMBER for each gap. (Đọc và trả lời.)', [
        ('What was the weather like yesterday?<br>Answer: {_}', ['sunny'], 'Đáp án: sunny (Yesterday, it was sunny).'),
        ('Where is the bookshop? – It is {_} Phong’s house.', ['near'], 'Đáp án: near (the bookshop near Phong’s house).'),
        ('What does Minh want to buy?<br>Answer: {_}', ['a book', 'book'], 'Đáp án: a book (a book about crocodiles).'),
        ('What animals does Minh like?<br>Answer: {_}', ['crocodiles', 'crocodile'], 'Đáp án: crocodiles.'),
        ('How much is the comic?<br>Answer: {_}', ['twenty thousand', '20,000', '20.000', '20000', 'twenty thousand dong', '20,000 dong'], 'Đáp án: twenty thousand (dong) = 20,000 dong.')],
        passage='<p>%s</p>' % _html.escape(pas2))
    c2 = passage_of(r2, r'50,000 bakery sun bookshop go straight sunny')
    c2 = re.sub(r'\((\d)\)\s*(?:_+\s*)+', lambda m: '<b>(%s) ______</b> ' % m.group(1), c2)
    P.fill('r2t3', 'Revision 2 – Task 3. Read and complete. There is ONE extra option. (Điền từ trong khung, có 1 từ thừa.)',
           [('Chỗ trống (%d): {_}' % (i + 1), a, None) for i, a in enumerate([['sunny'], ['bakery'], ['go straight'], ['bookshop'], ['50,000', '50.000', '50000', 'fifty thousand']])],
           passage='<p>%s</p>' % c2, bank=['50,000', 'bakery', 'sun', 'bookshop', 'go straight', 'sunny'])
    P.end('revision-2', 'Revision 2')
    P.theory = ''
    return P.save(notes)


# ================================================================ D: đề cương cuối HK2 (chỉ từ vựng + mẫu câu) -> tự sinh trắc nghiệm
def fix_d(s):
    s = s.replace('suuny', 'sunny').replace('foodstall', 'food stall')
    return re.sub(r'\s+', ' ', s).strip()


def slashfix(s):
    return re.sub(r'\s*/\s*', '/', fix_d(s))


def parse_d(lines):
    units, cur = [], None
    for l in lines:
        if not l.startswith('|'): continue
        c = [x.strip() for x in l.strip('|').split(' | ')]
        m = re.match(r'^Unit\s+(\d+)\s*:\s*(.*)$', c[0])
        if m:
            cur = {'n': int(m.group(1)), 'title': m.group(2).strip(), 'vocab': [], 'gram': [], 'gram_raw': []}; units.append(cur); continue
        if cur and c[0] == 'Vocabulary':
            for it in c[1].split(' ¦ '):
                it = re.sub(r'^\d+\.\s*', '', it.strip())
                if ':' in it:
                    en, vi = it.split(':', 1)
                    cur['vocab'].append((fix_d(en), fix_d(vi)))
        elif cur and c[0] == 'Grammar':
            els = []
            for it in c[1].split(' ¦ '):
                it = re.sub(r'^[^\w\-À-ỹ]+', '', it.strip())
                parts = re.split(r'\s+(?=B:)', it)
                els += parts
            heading, pending = None, None
            for it in els:
                it = re.sub(r'^[^\w\-À-ỹ]+', '', it.strip())
                if re.match(r'^(\d+\.\s*)?Hỏi', it):
                    heading = re.sub(r'^\d+\.\s*', '', it); cur['gram_raw'].append(('h', fix_d(heading))); continue
                t = re.sub(r'^(-|A:|B:)\s*', '', it).strip()
                t = slashfix(t)
                if t.endswith('?'): pending = t; cur['gram_raw'].append(('q', t))
                else:
                    cur['gram_raw'].append(('a', t))
                    if pending: cur['gram'].append((pending, t)); pending = None
    return units


def build_d():
    name = 'De-cuong-on-tap-cuoi-HK2-Tieng-Anh-4-Global-24-25'
    P = Practice('dc2_d', 'Đề cương HK2 (24-25) D – Cuối kì 2: từ vựng & mẫu câu', name, 'luyentap_d')
    L = dump(name)
    U = parse_d(L)
    notes = ['tài liệu chỉ có từ vựng + mẫu câu (không có bài tập): trắc nghiệm tự sinh từ chính tài liệu, nhiễu lấy từ các mục khác trong tài liệu', 'sửa chính tả trong tài liệu: suuny→sunny, foodstall→food stall']
    # ----- lý thuyết
    th = ['<h3>Đề cương ôn tập Tiếng Anh khối 4 – Kì 2 (Global Success) – Năm học 2024–2025</h3>']
    for u in U:
        th.append('<h3>Unit %d: %s</h3>' % (u['n'], _html.escape(u['title'])))
        th.append('<table class="tb"><tr><td><b>Từ vựng</b></td><td><b>Nghĩa</b></td></tr>%s</table>' % ''.join('<tr><td>%s</td><td>%s</td></tr>' % (_html.escape(a), _html.escape(b)) for a, b in u['vocab']))
        g = ['<p><b>Mẫu câu</b></p><ul>']
        for kind, t in u['gram_raw']:
            if kind == 'h': g.append('</ul><p>%s</p><ul>' % _html.escape(t))
            else: g.append('<li>%s</li>' % _html.escape(t))
        g.append('</ul>')
        th.append(''.join(g).replace('<ul></ul>', '').replace('<ul></ul>', ''))
    P.theory = ''.join(th)
    # ----- trắc nghiệm từ vựng
    allv = [(u['n'], en, vi) for u in U for en, vi in u['vocab']]
    rng = random.Random(20250)

    def pick(pool, correct, k=3, same=None):
        cand = [x for x in pool if x != correct]
        pri = [x for x in cand if same and x in same]
        rest = [x for x in cand if x not in pri]
        rng.shuffle(pri); rng.shuffle(rest)
        return (pri + rest)[:k]

    def mc(q, correct, pool, same):
        opts = pick(pool, correct, 3, same) + [correct]
        rng.shuffle(opts)
        return (q, opts, opts.index(correct), None)
    en_vi, vi_en = [], []
    for u in U:
        same_vi = [vi for _, vi in u['vocab']]; same_en = [en for en, _ in u['vocab']]
        all_vi = [v for _, _, v in allv]; all_en = [e for _, e, _ in allv]
        en_vi.append((u['n'], [mc('<b>%s</b> nghĩa là gì?' % _html.escape(en), vi, all_vi, same_vi) for en, vi in u['vocab']]))
        vi_en.append((u['n'], [mc('Từ/cụm từ nào có nghĩa là: <b>%s</b>?' % _html.escape(vi), en, all_en, same_en) for en, vi in u['vocab']]))

    def paginate(seq, label, pid, maxn=40):
        page, cnt, units = [], 0, []
        pages = []
        for n, rows in seq:
            if cnt + len(rows) > maxn and page:
                pages.append((page, units)); page, cnt, units = [], 0, []
            page.append((n, rows)); cnt += len(rows); units.append(n)
        if page: pages.append((page, units))
        for k, (pg, us) in enumerate(pages, 1):
            P.begin()
            for n, rows in pg:
                P.mcq('%s%d' % (pid, n), 'Unit %d – %s' % (n, 'chọn nghĩa tiếng Việt đúng' if pid == 'ev' else 'chọn từ/cụm từ tiếng Anh đúng'), rows)
            P.end('%s%d' % (pid, k), '%s (Unit %d–%d)' % (label, us[0], us[-1]) if us[0] != us[-1] else '%s (Unit %d)' % (label, us[0]))
    paginate(en_vi, 'Từ vựng Anh → Việt', 'ev')
    paginate(vi_en, 'Từ vựng Việt → Anh', 've')
    # ----- mẫu câu: chọn câu trả lời / câu hỏi phù hợp
    allq = [(u['n'], q, a) for u in U for q, a in u['gram']]
    P.begin()
    gq = []
    for n, q, a in allq:
        okp = [x[2] for x in allq if x[1] != q]   # bỏ các đáp án của chính câu hỏi này (vd. 2 đáp án cho What does he/she look like?)
        gq.append((n, mc('Câu trả lời phù hợp cho: <b>%s</b>' % _html.escape(q), a, okp, [x for x in okp if x in [y[2] for y in allq if y[0] == n]])))
    for n in sorted(set(x[0] for x in gq)):
        P.mcq('gq%d' % n, 'Unit %d – chọn câu trả lời phù hợp' % n, [r for m, r in gq if m == n])
    P.end('mau-cau-tra-loi', 'Mẫu câu: chọn câu trả lời')
    P.begin()
    gh = []
    for n, q, a in allq:
        okq = [x[1] for x in allq if x[1] != q]
        gh.append((n, mc('Câu hỏi phù hợp cho câu trả lời: <b>%s</b>' % _html.escape(a), q, okq, [x for x in okq if x in [y[1] for y in allq if y[0] == n]])))
    for n in sorted(set(x[0] for x in gh)):
        P.mcq('gh%d' % n, 'Unit %d – chọn câu hỏi phù hợp' % n, [r for m, r in gh if m == n])
    P.end('mau-cau-hoi', 'Mẫu câu: chọn câu hỏi')
    return P.save(notes)


if __name__ == '__main__':
    todo = set(sys.argv[1:]) or set('abcde')
    for k in 'abcde':
        if k in todo and 'build_' + k in globals(): globals()['build_' + k]()
