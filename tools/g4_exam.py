# -*- coding: utf-8 -*-
"""Thư viện dựng đề kiểm tra Lớp 4 từ docx (ảnh đã tách bởi g4_hl.dump -> /home/claude/g4/exi/<tên>/imgNN.png).
Dùng: ex = Exam('gk1_de1', 'GiuaKy1', 'Giữa kỳ 1 – Đề 1', 'GiuaKy1_de1', slug='test01', src='De-kiem-tra-giua-HK1-Anh-4-Global-De-1', minutes=15)
      ex.mcq_words(...); ex.mcq_pics(...); ... ; ex.save()
Mỗi lần save() ghi units/lop4_<tag>.py + _dapan.py, ảnh vào assets/lop4_<tag>/, âm thanh vào audio/lop4_<tag>.mp3 và thêm vào units/registry_lop4_ex.py."""
import os, re, pprint, subprocess, json
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMGROOT = '/home/claude/g4/exi'
MP3 = '/home/claude/g4/mp3'
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
REGFILE = os.path.join(ROOT, 'units/registry_lop4_ex.json')


def L(i, n=5):
    return 'ABCDEFGH'[i]


def letters_to_idx(s):
    return 'ABCDEFGH'.index(s.upper())


def parse_keys(s):
    """'1. B 2. C 3. A' / '1.B 2.C' / '1 jam 2 Australia' / '(1) America (2) cake' -> {1:'B',...}"""
    s = s.replace('\n', ' ')
    parts = re.split(r'(?:^|\s)\(?(\d+)[\.\)]?\s*(?=\S)', ' ' + s)
    out = {}
    for i in range(1, len(parts) - 1, 2):
        out[int(parts[i])] = parts[i + 1].strip().rstrip('.;,') if False else parts[i + 1].strip()
    return out


class Exam:
    def __init__(self, tag, unit, title, src, slug='test01', minutes=40, warn_at=5, audio=None, max_plays=3, kind='test'):
        self.tag, self.unit, self.title, self.slug = tag, unit, title, slug
        self.src = os.path.join(IMGROOT, src)
        self.minutes, self.warn_at, self.max_plays = minutes, warn_at, max_plays
        self.audio_src = audio  # list tên mp3 (trong MP3/) hoặc None
        self.groups, self.ANS, self.EXP, self.k = [], {}, {}, 0
        self.out = os.path.join(ROOT, 'assets/lop4_%s' % tag)
        os.makedirs(self.out, exist_ok=True)
        self.notes = []

    # ------------------------------------------------------------ ảnh
    def load(self, name):
        if isinstance(name, Image.Image): return name
        p = os.path.join(self.src, name if name.endswith('.png') else name + '.png')
        return Image.open(p).convert('RGB')

    @staticmethod
    def fit(im, w, h):
        s = min(w / im.width, h / im.height, 3.0)
        return im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)

    def cell(self, names, w, h, border=True):
        names = [names] if isinstance(names, (str, Image.Image)) else names
        c = Image.new('RGB', (w, h), 'white')
        k = len(names)
        for i, nm in enumerate(names):
            im = self.fit(self.load(nm), w // k - 6, h - 8)
            c.paste(im, (i * (w // k) + (w // k - im.width) // 2, (h - im.height) // 2))
        if border: ImageDraw.Draw(c).rectangle([0, 0, w - 1, h - 1], outline=(190, 190, 190))
        return c

    def strip(self, items, labels, out, w=170, h=140):
        gap = 12
        W = len(items) * w + (len(items) - 1) * gap
        S = Image.new('RGB', (W, h + 34), 'white')
        d = ImageDraw.Draw(S)
        for i, (nm, lb) in enumerate(zip(items, labels)):
            x = i * (w + gap)
            S.paste(self.cell(nm, w, h), (x, 0))
            tw = d.textlength(lb, font=FONT)
            d.text((x + (w - tw) / 2, h + 4), lb, fill=(20, 20, 20), font=FONT)
        S.save(os.path.join(self.out, out), optimize=True)
        return out

    def single(self, names, out, w=200, h=150):
        self.cell(names, w, h).save(os.path.join(self.out, out), optimize=True)
        return out

    def asset(self, out):
        return '../../../../assets/lop4_%s/%s' % (self.tag, out)

    # ------------------------------------------------------------ nhóm
    def add(self, gid, instr, items, passage=None, bank=None):
        out = []
        for it, a, e in items:
            self.k += 1
            it = dict(it)
            it['id'] = '%s.%d' % (gid, self.k)
            out.append(it)
            self.ANS[it['id']] = a
            self.EXP[it['id']] = e
        g = {'id': gid, 'instr': instr, 'items': out}
        if passage: g['passage'] = passage
        if bank: g['bank'] = bank
        self.groups.append(g)

    # ------ trắc nghiệm chọn từ (text)
    def mcq_words(self, gid, instr, rows, keys, q='Chọn từ đúng.', exps=None):
        """rows: [[optA,optB,optC]]; keys: ['B','C',...] hoặc chuỗi 'BCAB'"""
        items = []
        for i, (opts, kk) in enumerate(zip(rows, keys)):
            a = opts[letters_to_idx(kk)]
            items.append(({'t': 'mcq', 'q': q, 'o': list(opts)}, kk.upper(), (exps[i] if exps else 'Đáp án: %s. %s' % (kk.upper(), a))))
        self.add(gid, instr, items)

    # ------ trắc nghiệm chọn tranh A/B/C
    def mcq_pics(self, gid, instr, rows, keys, q='Nghe và chọn tranh đúng.', w=150, h=125, exps=None):
        """rows: [[img1,img2,img3]] (tên ảnh)"""
        items = []
        for i, (pics, kk) in enumerate(zip(rows, keys), 1):
            if isinstance(pics, dict):   # tranh mất dấu hiệu phân biệt -> chuyển thành câu chữ
                items.append(({'t': 'mcq', 'q': pics['q'], 'o': pics['o']}, kk.upper(), 'Đáp án: %s. %s' % (kk.upper(), pics['o'][letters_to_idx(kk)])))
                continue
            nm = self.strip(pics, [L(j) for j in range(len(pics))], '%s_%d.png' % (gid, i), w=w, h=h)
            items.append(({'t': 'mcq', 'plain': True, 'wide': True, 'img': nm, 'q': q, 'o': [L(j) for j in range(len(pics))]}, kk.upper(),
                          (exps[i - 1] if exps else 'Đáp án %s (theo đáp án của đề). Nghe lại file âm thanh và đối chiếu với tranh.' % kk.upper())))
        self.add(gid, instr, items)

    # ------ câu hỏi (có ảnh) + các đáp án chữ
    def mcq_text(self, gid, instr, rows, keys, w=210, h=150, exps=None):
        """rows: [(imgs|None, câu hỏi, [opt...])]; keys: letters"""
        items = []
        for i, ((imgs, qq, opts), kk) in enumerate(zip(rows, keys), 1):
            it = {'t': 'mcq', 'q': qq, 'o': list(opts)}
            if imgs:
                it['img'] = self.single(imgs, '%s_%d.png' % (gid, i), w=w, h=h)
            a = opts[letters_to_idx(kk)]
            items.append((it, kk.upper(), (exps[i - 1] if exps else 'Đáp án: %s. %s' % (kk.upper(), a))))
        self.add(gid, instr, items)

    # ------ điền từ
    def fill(self, gid, instr, rows, passage=None, bank=None):
        """rows: [(q có {_}, [đáp án chấp nhận], img|None|list, giải thích|None)]"""
        items = []
        for i, r in enumerate(rows, 1):
            q, a, im = r[0], r[1], (r[2] if len(r) > 2 else None)
            e = r[3] if len(r) > 3 and r[3] else 'Đáp án: %s' % a[0]
            it = {'t': 'fill', 'q': q}
            if im:
                it['img'] = self.single(im, '%s_%d.png' % (gid, i), w=170, h=130)
            items.append((it, a if isinstance(a, list) else [a], e))
        self.add(gid, instr, items, passage=passage, bank=bank)

    # ------ True / False
    def tf(self, gid, instr, rows, passage=None):
        """rows: [(câu, 'T'|'F', img|None, giải thích|None)]"""
        items = []
        for i, r in enumerate(rows, 1):
            q, a = r[0], r[1]
            im = r[2] if len(r) > 2 else None
            e = r[3] if len(r) > 3 and r[3] else ('Đáp án: %s (theo đáp án của đề).' % ('True' if a == 'T' else 'False'))
            it = {'t': 'tf', 'q': q}
            if im:
                it['img'] = self.single(im, '%s_%d.png' % (gid, i), w=200, h=150)
            items.append((it, a, e))
        self.add(gid, instr, items, passage=passage)

    # ------ sắp xếp từ
    def order(self, gid, instr, rows):
        items = [({'t': 'order', 'q': 'Sắp xếp thành câu đúng:', 'words': w}, [s], 'Câu đúng: ' + s) for w, s in rows]
        self.add(gid, instr, items)

    # ------ nối / chọn (select)
    def match(self, gid, instr, left, opts, keys, exp='', picture=None):
        """left: [{'t':..}|{'img':..}], opts: list, keys: list đáp án cho từng left"""
        it = {'t': 'match', 'q': 'Nối (chọn đáp án đúng cho từng dòng):', 'left': left, 'o': opts}
        self.add(gid, instr, [(it, {'blanks': [[x] for x in keys]}, exp)], passage=picture)

    # ------ nghe & đánh số (a-d) -> mỗi tranh một câu
    def number_pics(self, gid, instr, pics, labels, keys, nums=None, only=None):
        """pics: ảnh các tranh a,b,c,d; keys: số thứ tự nghe thấy cho từng tranh; only: nhãn cần hỏi (bỏ tranh ví dụ); nums: các số lựa chọn"""
        nm = self.strip(pics, labels, '%s.png' % gid, w=150, h=125)
        n = len(pics)
        items = []
        for lb, kk in zip(labels, keys):
            if only and lb not in only: continue
            items.append(({'t': 'mcq', 'plain': True, 'q': 'Tranh %s là câu số mấy trong bài nghe?' % lb, 'o': nums or [str(i) for i in range(1, n + 1)]}, str(kk),
                          'Tranh %s ứng với câu %s (theo đáp án của đề).' % (lb, kk)))
        self.add(gid, instr, items, passage='<img class="wide" src="%s" alt="Tranh">' % self.asset(nm))

    # ------------------------------------------------------------ xuất
    def save(self):
        total = sum(len(g['items']) for g in self.groups)
        page = {'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': self.minutes, 'warn_at': self.warn_at, 'groups': self.groups}
        audio_rel = ''
        if self.audio_src:
            audio_rel = 'audio/lop4_%s.mp3' % self.tag
            self.make_audio(os.path.join(ROOT, audio_rel))
            page['audio'] = True
            page['audio_max_plays'] = self.max_plays
        S = {'id': 'lop4-%s' % self.tag.replace('_', '-'), 'title': self.title, 'grade': 4, 'unit': self.unit, 'theory': '', 'pages': [page]}
        base = 'units/lop4_%s' % self.tag
        for path, name, obj in ((base + '.py', 'SET', S), (base + '_dapan.py', 'ANS', self.ANS)):
            with open(os.path.join(ROOT, path), 'w', encoding='utf8') as f:
                f.write('# -*- coding: utf-8 -*-\n"""Sinh bởi tools/g4_exam.py"""\n\n%s = %s\n' % (name, pprint.pformat(obj, width=160)))
        with open(os.path.join(ROOT, base + '_dapan.py'), 'a', encoding='utf8') as f:
            f.write('\nEXPLANATIONS = %s\n' % pprint.pformat(self.EXP, width=160))
        os.makedirs(os.path.join(ROOT, 'units/reg'), exist_ok=True)
        json.dump([S['id'], base + '.py', base + '_dapan.py', 'Lop4', self.unit, self.slug, 'assets/lop4_%s' % self.tag, audio_rel],
                  open(os.path.join(ROOT, 'units/reg/%s.json' % self.tag), 'w', encoding='utf8'), ensure_ascii=False)
        print('%-22s %3d câu  %s' % (self.tag, total, ' | '.join(self.notes)))
        return total

    def make_audio(self, dst):
        files = [os.path.join(MP3, f) for f in self.audio_src]
        for f in files:
            assert os.path.exists(f), f
        lst = dst + '.lst'
        sil = '/tmp/sil1.mp3'
        if not os.path.exists(sil):
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'anullsrc=r=22050:cl=mono', '-t', '2', '-ac', '1', '-ab', '48k', sil], check=True)
        parts = []
        for i, f in enumerate(files):
            if i: parts.append(sil)
            parts.append(f)
        # re-encode từng phần cho đồng nhất rồi nối
        tmp = []
        for i, f in enumerate(parts):
            t = '/tmp/_g4part_%d.mp3' % i
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f, '-vn', '-ac', '1', '-ab', '48k', '-ar', '22050', t], check=True)
            tmp.append(t)
        with open(lst, 'w') as fh:
            for t in tmp: fh.write("file '%s'\n" % t)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', dst], check=True)
        os.remove(lst)


# ================================================================ đọc dump
class Dump:
    """Đọc <IMGROOT>/<src>.txt; tách thành các phần theo tiêu đề La Mã (I., II.…) ở thân đề và ở đáp án."""

    def __init__(self, src):
        self.lines = [l.replace('⟦', '').replace('⟧', '') for l in open(os.path.join(IMGROOT, src + '.txt'), encoding='utf8').read().split('\n')]
        ki = next((i for i, l in enumerate(self.lines) if re.match(r'^\s*(ANSWER KEY|KEYS?|ĐÁP ÁN|KEY)\b', l.strip(), re.I)), len(self.lines))
        self.body, self.key = self.lines[:ki], self.lines[ki + 1:]

    @staticmethod
    def split(lines, pat=r'^([IVX]+)\.\s*(.*)$'):
        secs, cur = {}, None
        for l in lines:
            m = re.match(pat, l.strip())
            if m:
                cur = m.group(1); secs[cur] = {'head': m.group(2), 'lines': []}
            elif cur:
                secs[cur]['lines'].append(l)
        return secs

    def sec(self):
        return self.split(self.body)

    def keys(self):
        return self.split(self.key)


def passage(text, hint=True):
    """text: văn bản có '(n) [img:x] ______' -> HTML <p>"""
    t = re.sub(r'\((\d+)\)\s*(?:\[img:\w+\]\s*)?[_\.…]+', lambda m: '<b>(%s) ______</b>' % m.group(1), text)
    t = re.sub(r'\[img:\w+\]', '', t)
    return '<p>' + t.strip() + '</p>'


def cells(line):
    """'| a | b ¦ c |' -> [['a'], ['b','c']]"""
    return [[x.strip() for x in c.split('¦')] for c in line.strip().strip('|').split(' | ')]


def imgs(s):
    return re.findall(r'\[img:(\w+)\]', s)


# ---- bảng -> hàng
def _skip_example(c0):
    return bool(re.match(r'^(e\.?g\.?|example)', c0.strip(), re.I))


def rows_words(lines):
    """'| 1. | A. jam | B. yes | C. grapes |' -> [[jam,yes,grapes]] (bỏ ví dụ)"""
    out = []
    for l in lines:
        if not l.startswith('|'): continue
        c = cells(l)
        if _skip_example(c[0][0]): continue
        opts = [re.sub(r'^[A-D]\.\s*', '', x[0]).strip() for x in c[1:]]
        if len(opts) >= 2 and re.match(r'^\d', c[0][0]): out.append(opts)
    return out


def rows_pics(lines):
    """'| 1. | A. [img] | B. [img] | C. [img] |' -> [[img,img,img]] (bỏ ví dụ)"""
    out = []
    for l in lines:
        if not l.startswith('|'): continue
        c = cells(l)
        if _skip_example(c[0][0]): continue
        if not re.match(r'^\d', c[0][0]): continue
        pics = []
        for x in c[1:]:
            im = list(dict.fromkeys(imgs(' '.join(x))))
            if im: pics.append(im if len(im) > 1 else im[0])
        if pics: out.append(pics)
    return out


def rows_q(lines, tick=False):
    """'| 1. | [imgs] | câu hỏi ¦ A. a ¦ B. b ¦ C. c |' -> [(imgs, câu hỏi, [opts])]"""
    out = []
    for l in lines:
        if not l.startswith('|'): continue
        c = cells(l)
        if _skip_example(c[0][0]): continue
        if not re.match(r'^\d', c[0][0]): continue
        if len(c) < 2: continue
        last = c[-1]
        im = [i for x in c[1:-1] for i in imgs(' '.join(x))]
        isopt = lambda x: re.match(r'^(?:[A-D]\.|⬜|🗹)', x.strip())
        q = ' '.join([last[0]] + [x for x in last[1:] if not isopt(x)])
        opts = [re.sub(r'^(?:[A-D]\.|⬜|🗹)\s*', '', x).strip() for x in last[1:] if isopt(x)]
        out.append((im, q, opts))
    return out


def keyletters(lines):
    """tìm 'n. X' trong dòng (A-D / a-d / T / F)"""
    txt = ' '.join(lines)
    return {int(n): v for n, v in re.findall(r'(\d+)\s*[\.\)]?\s*([A-Ea-e]|TRUE|FALSE|True|False|T|F)(?=\s|$|\.)', txt)}


# ================================================================ định dạng "Question n."
def parse_qn(src):
    """Đọc <src>.txt dạng 'Question n.' có bản đáp án (đáp án = đoạn tô ⟦⟧). Trả về list block:
    {'head':..., 'img': [..], 'qs': [{'n','text','opts':[..],'key':'A'|None,'hl':[...]}]}"""
    raw = open(os.path.join(IMGROOT, src + '.txt'), encoding='utf8').read().split('\n')
    cut = next((i for i, l in enumerate(raw) if re.match(r'^\s*⟦?\s*(ĐÁP ÁN|KEYS?)\b', l.strip(), re.I)), None)
    body, ans = (raw[:cut], raw[cut + 1:]) if cut is not None else (raw, [])

    def parse(lines, keep):
        blocks, cur, q = [], None, None
        for l in lines:
            t = l.strip()
            if not t: continue
            plain = t.replace('⟦', '').replace('⟧', '')
            m = re.match(r'^Question\s+(\d+)\.?\s*(.*)$', plain)
            if m and not re.match(r'^Question\s+\d+\.', plain) and not re.sub(r'\[img:\w+\]', '', m.group(2)).strip():
                # 'Question 13 [img:..]' = dòng tiêu đề ảnh của câu 13
                cur = {'head': cur['head'] if cur else '', 'img': imgs(plain), 'qs': []}; blocks.append(cur); q = None
                continue
            if m:
                q = {'n': int(m.group(1)), 'text': m.group(2).strip(), 'opts': [], 'key': None, 'hl': [], 'raw': t}
                if cur is None:
                    cur = {'head': '', 'img': [], 'qs': []}; blocks.append(cur)
                # ảnh nằm cùng dòng 'Question 13 [img:..]'
                cur['img'] += imgs(plain)
                q['text'] = re.sub(r'\[img:\w+\]', '', q['text']).strip()
                cur['qs'].append(q)
                # phần tô trong dòng câu hỏi
                continue
            if re.match(r'^Question\s+\d+\s*\[img', plain):
                continue
            om = re.match(r'^(?:\[img:[^\]]*\]\s*)?(⟦)?\s*([A-D])\.\s*(.*)$', t)
            if om and q is not None and cur['qs'] and cur['qs'][-1] is q:
                # có thể nhiều đáp án trên một dòng
                parts = re.split(r'\s+(?=⟦?[A-D]\.\s)', re.sub(r'^\[img:[^\]]*\]\s*', '', t))
                for pt in parts:
                    mm = re.match(r'^(⟦)?\s*([A-D])\.\s*(.*?)\s*(⟧)?$', pt)
                    if not mm: continue
                    q['opts'].append(mm.group(3).replace('⟦', '').replace('⟧', '').strip())
                    if mm.group(1) or mm.group(4):
                        q['key'] = mm.group(2)
                continue
            if imgs(plain) and not re.match(r'^[A-D]\.', plain) and (q is None or not q['text'] or True) and re.fullmatch(r'(\[img:\w+\]\s*)+', plain):
                if cur is None or (cur['qs'] and keep):
                    cur = {'head': cur['head'] if cur else '', 'img': [], 'qs': []}; blocks.append(cur)
                cur['img'] += imgs(plain); q = None
                continue
            if plain.upper() == plain and len(plain) < 40 and not re.match(r'^[A-D]\.', plain) and not plain.startswith('|'):
                cur = {'head': plain, 'img': [], 'qs': []}; blocks.append(cur); q = None
                continue
            if q is not None and not q['opts']:
                q['text'] = (q['text'] + ' ' + plain).strip()
                for h in re.findall(r'⟦([^⟧]*)⟧', t): q['hl'].append(h.strip())
                continue
        return [b for b in blocks if b['qs']]
    B = parse(body, True)
    A = parse(ans, True) if ans else []
    amap = {q['n']: q for b in A for q in b['qs']}
    for b in B:
        for q in b['qs']:
            a = amap.get(q['n'])
            if a:
                q['key'] = a['key']
                q['hl'] = a['hl'] + re.findall(r'⟦([^⟧]*)⟧', a['raw'])
    return B


def build_qn(ex, src, keys=None, hint=True, fill_blank=r'[…\.]{3,}|_{3,}'):
    """Dựng nhóm từ parse_qn. keys: dict n->đáp án (ghi đè). Trả về số câu."""
    B0 = parse_qn(src)
    B = []
    for b in B0:   # gộp các khối liền nhau cùng tiêu đề và không có ảnh riêng
        if B and not b['img'] and b['head'] == B[-1]['head'] and not B[-1]['img']:
            B[-1]['qs'] += b['qs']
        else:
            B.append(b)
    gi = 0
    for b in B:
        gi += 1
        items = []
        head = b['head'].title() if b['head'] else 'Questions'
        vi = {'LISTEN AND CHOOSE': 'nghe và chọn đáp án đúng', 'LISTEN AND WRITE': 'nghe và điền từ',
              'LISTEN AND TICK': 'nghe và chọn', 'LISTEN AND NUMBER': 'nghe và đánh số'}.get(b['head'], '')
        instr = head + (' (%s)' % vi if vi else '')
        pas = None
        if b['img']:
            nm = ex.single(b['img'], 'p%d.png' % gi, w=560 if len(b['img']) == 1 else 700, h=230)
            pas = '<img class="wide" src="%s" alt="Hình">' % ex.asset(nm)
        for q in b['qs']:
            n = q['n']
            key = (keys or {}).get(n, q['key'])
            if q['opts']:
                txt = q['text']
                txt = re.sub(r'^Number\s*(\d+)$', r'Nghe câu số \1.', txt) if re.match(r'^Number\s*\d+$', txt) else txt
                if not txt: txt = 'Nghe và chọn đáp án đúng.'
                if key is None:
                    ex.notes.append('Q%d thiếu đáp án' % n); continue
                opts = q['opts']
                items.append(({'t': 'mcq', 'q': txt, 'o': opts}, key, 'Đáp án: %s. %s' % (key, opts['ABCD'.index(key)])))
            else:
                hl = (keys or {}).get(n) or q['hl']
                if not hl:
                    ex.notes.append('Q%d thiếu đáp án điền' % n); continue
                hl = hl if isinstance(hl, list) else [hl]
                t = re.sub(r'⟦[^⟧]*⟧', '…', q['text'])
                if not re.findall(fill_blank, t):
                    t = re.sub(r'\s*\.?\s*$', ' ……………', t.rstrip()) if not t.rstrip().endswith('?') else t + ' ……………'
                if len(re.findall(fill_blank, t)) != 1:
                    ex.notes.append('Q%d: số ô trống lạ (%d)' % (n, len(re.findall(fill_blank, t)))); 
                t = re.sub(fill_blank, '{_}', t, count=1)
                t = re.sub(r'\s*…{3,}', '', t) if '{_}' in t else t
                t = re.sub(r'(\{_\})\s+\.(?=\s|$)', r'\1', t)
                t = re.sub(r'(\{_\})\s+([?.])', r'\1\2', t)
                items.append(({'t': 'fill', 'q': t}, [hl[0].strip(' .')], 'Đáp án: %s' % hl[0].strip(' .')))
        if items:
            ex.add('q%d' % gi, instr, items, passage=pas)
    return ex.k


def blank_answers(lines):
    """'(1) hair (2) tall' / nhiều dòng -> ['hair','tall']"""
    txt = ' '.join(l.strip() for l in lines)
    parts = re.split(r'\(\d+\)\s*', txt)[1:]
    return [p.strip().rstrip('.;,').strip() for p in parts]


def _hd(h):
    return re.sub(r'\s*\(\s*[\d,\.]+\s*points?\s*\)\s*$', '', h).strip()


def std_family(ex, d, S, K, listen=True, ivq='IV', words_q='Nghe âm và chọn từ có âm đó.', pic_text=None):
    """Họ đề I (âm) – II (tranh) – III (câu hỏi có tranh) – IV (điền từ theo tranh). Trả về dict các ghi chú."""
    if listen:
        kI = keyletters(K['I']['lines']); kII = keyletters(K['II']['lines'])
        rw = rows_words(S['I']['lines'])
        ex.mcq_words('l1', 'I. ' + _hd(S['I']['head']) + ' (nghe âm, chọn từ có âm đó).', rw, [kI[i + 1] for i in range(len(rw))], q=words_q)
        rp = rows_pics(S['II']['lines'])
        for i, v in (pic_text or {}).items(): rp[i - 1] = v
        ex.mcq_pics('l2', 'II. ' + _hd(S['II']['head']) + ' (nghe và chọn tranh đúng).', rp, [kII[i + 1] for i in range(len(rp))])
    rq = rows_q(S['III']['lines']); kIII = keyletters(K['III']['lines'])
    ex.mcq_text('r1', 'III. ' + _hd(S['III']['head']) + ' (nhìn tranh, chọn câu đúng).', rq, [kIII[i + 1] for i in range(len(rq))])
    ps = ' '.join(S[ivq]['lines']); pp = list(dict.fromkeys(imgs(ps)))
    ans = blank_answers(K[ivq]['lines'])
    if len(pp) != len(ans):
        ex.notes.append('IV: %d ảnh vs %d đáp án' % (len(pp), len(ans)))
        pp = (pp + [None] * len(ans))[:len(ans)]
    ex.fill('r2', 'IV. ' + _hd(S[ivq]['head']) + ' (nhìn tranh, điền từ vào chỗ trống).',
            [('Chỗ trống (%d): {_}' % (i + 1), [a], pp[i]) for i, a in enumerate(ans)], passage=passage(ps))


# ================================================================ họ đề Cuối kỳ (I nghe-số, II nối, III nghe-điền, IV chọn, V viết câu hỏi, VI T/F, VII điền, VIII viết/sắp xếp)
def _variants(s):
    s = s.strip()
    out = [s]
    if '(' in s:
        out.append(re.sub(r'\s*\([^)]*\)', '', s).strip())
        out.append(re.sub(r'[()]', '', s).strip())
    return list(dict.fromkeys(out))


def _numbered(lines):
    """gom: '1. xxx' + các dòng tiếp theo cho đến số kế -> [(n, [dòng...])]"""
    out = []
    for l in lines:
        m = re.match(r'^\s*(\d+)\s*\.\s*(.*)$', l)
        if m:
            out.append([int(m.group(1)), [m.group(2).strip()]])
        elif out and l.strip():
            out[-1][1].append(l.strip())
    return out


def _keytext(lines):
    t = ' '.join(l.strip() for l in lines)
    return re.sub(r'^\s*Key:\s*', '', t.replace('Key:', ' '))


def std_cuoi(ex, d, S, K, listen=True, tag=''):
    for r, sec in S.items():
        head = re.sub(r'\s*\(\s*[\d,\.]+\s*points?\s*\)\s*$', '', sec['head']).strip().rstrip('.')
        hl = head.lower(); lines = sec['lines']; kk = K.get(r, {'lines': []})['lines']
        if 'read and write t' in hl:   # một số đề đánh số phần đáp án lệch -> tìm theo nội dung
            kk = next((v['lines'] for v in K.values() if re.match(r'^\s*1\s*\.\s*(T|F)\b', ' '.join(v['lines']))), kk)
        if 'questions for the answers' in hl:
            kk = next((v['lines'] for v in K.values() if v['lines'] and '?' in ' '.join(v['lines'][:2]) and not re.search(r'Audio|Key', ' '.join(v['lines']))), kk)
        gid = ('g' + r).lower()
        title = '%s. %s' % (r, head)
        if 'speaking' in hl:
            ex.notes.append('bỏ Speaking'); continue
        if 'listen and number' in hl:
            if not listen: continue
            pics = imgs(' '.join(lines))[:4]
            kt = _keytext(kk)
            if re.search(r'\b[a-d]\s*\.\s*\d', kt):   # tranh -> số câu
                m = {a: int(b) for a, b in re.findall(r'([a-d])\s*\.\s*(\d)', kt)}
                inv = {v: k for k, v in m.items()}
            else:
                inv = {int(a): b for a, b in re.findall(r'(\d)\s*\.\s*([a-d])', kt)}
            nm = ex.strip(pics, list('abcd'), '%s.png' % gid, w=150, h=125)
            items = [({'t': 'mcq', 'plain': True, 'q': 'Nghe câu số %d: câu đó ứng với tranh nào?' % k, 'o': list('abcd')}, inv[k], 'Câu %d ứng với tranh %s (theo đáp án của đề).' % (k, inv[k])) for k in range(1, 5)]
            ex.add(gid, title + ' (nghe và chọn tranh cho từng câu).', items, passage='<img class="wide" src="%s" alt="Tranh a–d">' % ex.asset(nm))
        elif 'draw lines' in hl:
            if not listen: continue
            left, right = [], []
            for l in lines:
                if not l.startswith('|'): continue
                c = cells(l)
                li = imgs(c[0][0]); nm_ = re.sub(r'^\d+\.\s*|\[img:\w+\]', '', c[0][0]).strip()
                left.append((li[0] if li else None, nm_))
                ri = imgs(' '.join(c[1])) if len(c) > 1 else []
                right.append(ri[0] if ri else None)
            kd = {int(a): b for a, b in re.findall(r'(\d)\s*\.\s*([a-d])', _keytext(kk))}
            rn = ex.strip(right, list('abcd'), '%s.png' % gid, w=150, h=125)
            L = []
            for i, (im, nm_) in enumerate(left, 1):
                o = {'t': nm_}
                if im: o['img'] = ex.single(im, '%s_l%d.png' % (gid, i), w=130, h=100)
                L.append(o)
            ex.match(gid, title + ' (nghe và nối nhân vật với tranh).', L, list('abcd'), [kd[i] for i in range(1, len(left) + 1)],
                     'Đáp án theo đáp án của đề: ' + ', '.join('%d–%s' % (i, kd[i]) for i in sorted(kd)), picture='<img class="wide" src="%s" alt="Tranh a–d">' % ex.asset(rn))
        elif 'listen and complete' in hl:
            if not listen: continue
            nb = _numbered(lines)
            kt = parse_keys(_keytext(kk))
            items = []
            for n, ls in nb:
                q = '<br>'.join(re.sub(r'_{3,}', '{_}', x) for x in ls)
                items.append(({'t': 'fill', 'q': q}, [kt[n]], 'Đáp án: %s' % kt[n]))
            ex.add(gid, title + ' (nghe và điền từ).', items)
        elif 'read and choose' in hl:
            rq = rows_q(lines); k2 = keyletters(kk)
            ex.mcq_text(gid, title + ' (nhìn tranh, chọn đáp án đúng).', rq, [k2[i + 1] for i in range(len(rq))])
        elif 'questions for the answers' in hl:
            items = []
            kd = {n: ' '.join(ls) for n, ls in _numbered(kk)}
            rr = []
            for l in lines:
                if l.startswith('|'):
                    c = cells(l)
                    if re.match(r'^\d', c[0][0]):
                        im = imgs(' '.join(' '.join(x) for x in c)); last = c[-1]
                        rr.append((im, ' '.join(last[1:]) if len(last) > 1 else ''))
            for i, (im, ans_) in enumerate(rr, 1):
                it = {'t': 'fill', 'q': 'Viết câu hỏi cho câu trả lời: <i>%s</i><br>{_}' % ans_.lstrip('–- ').strip()}
                if im: it['img'] = ex.single(im, '%s_%d.png' % (gid, i), w=190, h=140)
                items.append((it, _variants(kd[i]), 'Câu hỏi đúng: %s' % kd[i]))
            ex.add(gid, title + ' (nhìn tranh, viết câu hỏi phù hợp).', items)
        elif 'read and write t' in hl:
            txt = []; st = []
            for l in lines:
                m = re.match(r'^\s*(\d+)\s*\.\s*(.*?)\s*_{3,}\s*$', l)
                if m: st.append(m.group(2).strip())
                elif not st and l.strip(): txt.append(l.strip())
            k2 = keyletters(kk)
            ex.tf(gid, title + ' (đọc đoạn văn, True hay False?).', [(s_, k2[i + 1]) for i, s_ in enumerate(st)], passage='<p>' + ' '.join(txt) + '</p>')
        elif 'fill in the blanks' in hl:
            bank = None; txt = []
            for l in lines:
                if l.startswith('|'):
                    bank = [x[0] for x in cells(l)]
                elif l.strip(): txt.append(l.strip())
            ps = ' '.join(txt); pp = list(dict.fromkeys(imgs(ps)))
            kt = _keytext(kk)
            ans = blank_answers(kk) if '(1)' in kt else [v for _, v in sorted(parse_keys(kt).items())]
            if pp and len(pp) != len(ans):
                ex.notes.append('%s: %d ảnh vs %d đáp án' % (r, len(pp), len(ans))); pp = (pp + [None] * len(ans))[:len(ans)]
            ps2 = re.sub(r'\((\d+)\)\s*(?:\[img:\w+\]\s*)?_+', lambda m: '(%s) ______' % m.group(1), ps)
            ex.fill(gid, title + ' (điền từ vào chỗ trống' + (', chọn từ trong khung' if bank else ', nhìn tranh') + ').',
                    [('Chỗ trống (%d): {_}' % (i + 1), [a], (pp[i] if pp else None)) for i, a in enumerate(ans)], passage=passage(ps2), bank=bank)
        elif 'given words' in hl:
            bank = None; qs = []
            for l in lines:
                if l.startswith('|'): bank = [x[0] for x in cells(l)]
            nb = _numbered([l for l in lines if not l.startswith('|') and not l.startswith('⭢')])
            kd = {n: ' '.join(ls) for n, ls in _numbered(kk)}
            items = [({'t': 'fill', 'q': '%s<br>→ {_}' % ls[0]}, _variants(kd[n]), 'Câu trả lời đúng: %s' % kd[n]) for n, ls in nb]
            ex.add(gid, title + ' (dùng từ cho sẵn để trả lời).', items, bank=bank)
        elif 'reorder' in hl:
            nb = _numbered(lines)
            kd = {n: ' '.join(ls) for n, ls in _numbered(kk)}
            rows = []
            for n, ls in nb:
                toks = [t.strip() for t in ' '.join(ls).replace('→', '').replace('_', '').split('/') if t.strip()]
                w = [t for t in toks if t not in ('.', '?', '!')]
                ans_ = kd[n].strip()
                if ans_ and ans_[-1] in '.?!' and ans_[-1] not in (w[-1] if w else ''):
                    last = ans_.split()[-1].rstrip('.?!')
                    for i_, t in enumerate(w):
                        if t.lower() == last.lower() and not t.endswith(ans_[-1]):
                            w[i_] = t + ans_[-1]; break
                rows.append((w, ans_))
            ex.order(gid, title + ' (sắp xếp từ thành câu đúng).', rows)
        else:
            ex.notes.append('phần lạ %s: %s' % (r, head))
