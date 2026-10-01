# -*- coding: utf-8 -*-
"""Chuyển đổi 1 lần: src/mt1/bode.txt (Bộ đề kiểm tra giữa HK1 Anh 11 Global 2025-26, 3 đề x 40 câu)
 -> units/mt1_test01..03.py (SET) + units/mt1_test01..03_dapan.py (ANS + EXPLANATIONS).
Cấu trúc nguồn: [bảng tiêu đề 'ĐỀ n'] [phần đề] 'ĐÁP ÁN' [bản có khoá ⟦…⟧ + Giải thích] [Tạm dịch bài đọc] [bảng 'Từ vựng' - bỏ qua].
Chạy:  python tools/gen_mt1_bode.py"""
import re, os, sys, pprint

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = open(os.path.join(ROOT, 'src/mt1/bode.txt'), encoding='utf8').read()
L = RAW.split('\n')

# ---- ranh giới 3 đề (xác định bằng tiêu đề 'ĐỀ n' trong bảng đầu mỗi đề)
HEAD = [i for i, l in enumerate(L) if re.search(r'ĐỀ\s*(</b><b>)?\s*\d\s*</b>', l) and '⟦' in l and 'KIỂM TRA' not in l]
ANSK = [i for i, l in enumerate(L) if l.strip() == '⟦<b>ĐÁP ÁN</b>⟧']
VOC = [i for i, l in enumerate(L) if re.match(r'^⟦<b>Từ Vựng', l)]
assert len(HEAD) == len(ANSK) == len(VOC) == 3, (HEAD, ANSK, VOC)


def region(k):
    h = HEAD[k]
    s = next(i for i in range(h, len(L)) if L[i].startswith('</TABLE>')) + 1
    return L[s:ANSK[k]], L[ANSK[k] + 1:VOC[k]]


# ---- chuẩn hoá văn bản
def tx(s):
    """giữ <b>,<u>; bỏ ⟦⟧, tab, nbsp, ký tự rác; gộp khoảng trắng"""
    s = s.replace('⟦', '').replace('⟧', '').replace('\t', ' ').replace('\xa0', ' ').replace('﻿', '').replace('​', '').replace('­', '')
    s = re.sub(r'\[(?:IMG|TICK)[^\]]*\]', '', s)
    s = re.sub(r'</b>(\s*)<b>', r'\1', s)
    s = re.sub(r'</u>(\s*)<u>', r'\1', s)
    s = re.sub(r'<(b|u)>\s*</\1>', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def plain(s):
    return re.sub(r'\s+', ' ', re.sub(r'</?[bu]>', '', tx(s))).strip()


def fixblank(s):
    return re.sub(r'\((\d+)\)\s*_{2,}', r'(\1) ______', s)


INSTR = re.compile(r'^(Read |Mark the letter)')
QSTART = re.compile(r'^Question\s+(\d+)\s*:\s*(.*)$')


def opts_split(t):
    parts = re.split(r'(?:^|\s)([A-D])\.\s*', t)
    o, i = [], 1
    while i < len(parts) - 1:
        o.append(parts[i + 1].strip())
        i += 2
    return o


# ---- phần đề
def parse_exam(lines):
    groups, g, q = [], None, None

    def endq():
        nonlocal q
        if q:
            g['qs'].append(q)
            q = None
    for ln in lines:
        t = plain(ln)
        if not t:
            continue
        if INSTR.match(t) and q is None or INSTR.match(t) and q is not None and not re.match(r'^[A-D]\.', t):
            endq()
            g = {'instr': t, 'para': [], 'qs': []}
            groups.append(g)
            continue
        m = QSTART.match(t)
        if m:
            endq()
            q = {'n': int(m.group(1)), 'stem': [], 'opt': []}
            rest = tx(re.sub(r'^\s*(<b>)?\s*Question\s+\d+\s*:\s*(</b>)?', '', ln.replace('⟦', '').replace('⟧', ''), count=1))
            # dòng 'Question n:A. ...' -> phần còn lại bắt đầu bằng phương án
            if re.match(r'^(<b>)?A\.\s', rest) or re.match(r'^A\.', plain(rest)):
                q['opt'].append(rest)
            elif plain(rest):
                q['stem'].append(rest)
            continue
        tp = t
        if q is not None:
            if q['opt'] or re.match(r'^[A-D]\.\s', tp):
                q['opt'].append(tx(ln))
            else:
                q['stem'].append(tx(ln))
        else:
            g['para'].append(tx(ln))
    endq()
    return groups


def mk_options(q):
    t = ' '.join(plain(x) for x in q['opt'])
    o = opts_split(t)
    return o


# ---- phần đáp án
def parse_answers(lines):
    """-> {n: {'key': 'A', 'exp_lines': [...], 'opts': [...]}}"""
    blocks, cur = {}, None
    for ln in lines:
        t = plain(ln)
        if not t:
            continue
        m = QSTART.match(t)
        if m:
            cur = {'n': int(m.group(1)), 'lines': [ln]}
            blocks[cur['n']] = cur
            continue
        if INSTR.match(t) or t.startswith('Tạm Dịch Bài Đọc'):
            cur = None
            continue
        if cur is not None:
            cur['lines'].append(ln)
    out = {}
    for n, b in blocks.items():
        ls = b['lines']
        gi = next((i for i, l in enumerate(ls) if re.search(r'Giải\s*[Tt]hích', l)), None)
        pre = ls[:gi] if gi is not None else ls
        marks = []
        for l in pre:
            for mm in re.finditer(r'⟦(.*?)⟧', l):
                s = plain(mm.group(1))
                mo = re.match(r'^([A-D])\.', s)
                if mo:
                    marks.append(mo.group(1))
        out[n] = {'marks': marks, 'exp': ls[gi:] if gi is not None else [], 'has_exp': gi is not None}
    return out


def cut(s, n):
    s = s.strip()
    if len(s) <= n:
        return s
    c = s[:n]
    k = max(c.rfind('. '), c.rfind('; '), c.rfind(', '))
    if k > n * 0.5:
        c = c[:k + 1]
    return c.rstrip(' ,;') + '…'


def build_exp(info, key, opts):
    if isinstance(key, list):
        key = key[0]
    """gộp giải thích Word -> HTML ngắn gọn"""
    out = []
    ex = info['exp']
    for i, ln in enumerate(ex):
        t = plain(ln)
        if not t:
            continue
        if i == 0:
            m = re.match(r'^Giải\s*[Tt]hích\s*:?\s*(.*)$', t)
            rest = m.group(1) if m else t
            if rest.startswith('Kiến thức'):
                out.append('<b>%s</b>' % rest)
            continue
        m = re.match(r'^([A-D])\.\s*(.*?)\s*[–-]\s*(ĐÚNG|SAI|Đúng|Sai)\b\s*[:\-–]?\s*(.*)$', t)
        if m:
            L_, otx, verdict, why = m.groups()
            if verdict.upper() == 'ĐÚNG':
                out.append('<b>%s. %s</b> – ĐÚNG: %s' % (L_, otx, cut(why, 650)))
            else:
                out.append('%s. SAI: %s' % (L_, cut(why, 190)))
            continue
        m = re.match(r'^([A-D])\.\s', t)
        if m:        # bản dịch tiếng Việt của phương án: chỉ giữ phương án đúng
            if m.group(1) == key:
                out.append('<i>Dịch đáp án đúng:</i> ' + cut(t, 300))
            continue
        if t.startswith('Tạm dịch'):
            out.append('<b>Tạm dịch:</b> ' + cut(re.sub(r'^Tạm dịch\s*:?\s*', '', t), 600))
            continue
        out.append(cut(t, 260))
    return '<br>'.join(out)


def paras_html(para):
    ps = []
    for p in para:
        p = fixblank(p)
        p = re.sub(r'^[⮚❖✔]\s*', '• ', p)
        p = p.replace('<b>• ', '• <b>')
        if ps and p[:1].islower() and not p.startswith('•'):
            ps[-1] += ' ' + p
        else:
            ps.append(p)
    return ''.join('<p>%s</p>' % p for p in ps)


def numbered_paras(para):
    """đoạn văn đọc hiểu: gắn nhãn Paragraph k (để các câu hỏi 'in paragraph k' dễ theo dõi)"""
    ps = [fixblank(p) for p in para]
    return ''.join('<p><small>[Paragraph %d]</small> %s</p>' % (i, p) for i, p in enumerate(ps, 1))


# ---- sửa lỗi nguồn / đáp án (điền sau khi rà soát): {test: {'src': [(old,new)], 'key': {n: (letter, note)}}}
FIX = {}
exec(open(os.path.join(ROOT, 'tools/mt1_bode_fixes.py'), encoding='utf8').read()) if os.path.exists(os.path.join(ROOT, 'tools/mt1_bode_fixes.py')) else None


def main():
    for k in range(3):
        tn = k + 1
        fx = FIX.get(tn, {})
        ex_lines, an_lines = region(k)
        for a, b in fx.get('src', []):
            ex_lines = [l.replace(a, b) for l in ex_lines]
            an_lines = [l.replace(a, b) for l in an_lines]
        groups = parse_exam(ex_lines)
        ans = parse_answers(an_lines)
        gl, ANS, EXPL, notes, warn = [], {}, {}, list(fx.get('notes', [])), []
        nq = 0
        for gi, g in enumerate(groups, 1):
            gid = 'g%d' % gi
            qs = g['qs']
            lo, hi = qs[0]['n'], qs[-1]['n']
            is_cloze = bool(g['para']) and any('(%d)' % qs[0]['n'] in plain(p) or '(%d)' % (qs[0]['n'] - 0) in p for p in g['para'])
            has_blank = any(re.search(r'\(\d+\)\s*_', p) for p in g['para'])
            grp = {'id': gid, 'instr': fixblank(g['instr'])}
            if g['para']:
                grp['passage'] = paras_html(g['para']) if has_blank or lo <= 12 else numbered_paras(g['para'])
            items = []
            for q in g['qs']:
                n = q['n']
                nq += 1
                if n != nq:
                    warn.append('số câu nhảy: %d != %d' % (n, nq))
                o = mk_options(q)
                if len(o) != 4:
                    warn.append('Q%d: %d phương án' % (n, len(o)))
                stem = '<br>'.join(re.sub(r'^<b>([a-e])\.\s*</b>\s*', r'\1. ', x) for x in q['stem'])
                if has_blank and not stem:
                    stem = 'Blank (%d)' % n
                it = {'id': '%s.%d' % (gid, n), 't': 'mcq', 'q': stem, 'o': o}
                items.append(it)
                info = ans.get(n)
                if not info:
                    warn.append('Q%d: không có khối đáp án' % n); continue
                marks = info['marks']
                if len(marks) != 1:
                    warn.append('Q%d: khoá Word %s' % (n, marks))
                key = marks[0] if marks else None
                if n in fx.get('key', {}):
                    key, why = fx['key'][n]
                # đối chiếu khoá với dòng ĐÚNG trong giải thích
                good = re.findall(r'^([A-D])\.[^\n]*?[–-]\s*(?:ĐÚNG|Đúng)', '\n'.join(plain(x) for x in info['exp']), re.M)
                if isinstance(key, str) and good and good[0] != key and n not in fx.get('key', {}):
                    warn.append('Q%d: khoá tô %s nhưng giải thích ĐÚNG %s' % (n, key, good))
                if not info['has_exp']:
                    warn.append('Q%d: thiếu giải thích' % n)
                ANS[it['id']] = key
                EXPL[it['id']] = build_exp(info, key, o)
                if isinstance(key, list):
                    EXPL[it['id']] += '<br><b>Lưu ý:</b> ' + why
            grp['items'] = items
            gl.append(grp)
        SET = {'id': 'lop11-mt1-test%02d' % tn, 'title': 'Test %d – Mid-term 1' % tn, 'grade': 11, 'unit': 'MidTerm1', 'theory': '',
               'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 45, 'groups': gl}]}
        hdr = '# -*- coding: utf-8 -*-\n'
        open(os.path.join(ROOT, 'units/mt1_test%02d.py' % tn), 'w', encoding='utf8').write(
            hdr + '"""Test %d – Mid-term 1 (Tiếng Anh 11 Global Success): Đề kiểm tra giữa HK1 2025-2026, đề %d (40 câu, không có phần nghe).\nSinh bởi tools/gen_mt1_bode.py từ src/mt1/bode.txt."""\n\nSET = ' % (tn, tn)
            + pprint.pformat(SET, width=150, sort_dicts=False) + '\n')
        open(os.path.join(ROOT, 'units/mt1_test%02d_dapan.py' % tn), 'w', encoding='utf8').write(
            hdr + '"""Đáp án + giải thích – Test %d Mid-term 1. Khoá lấy từ phần ĐÁP ÁN (tô ⟦⟧) của file Word, đối chiếu lại độc lập;\ngiải thích rút gọn từ lời giải tiếng Việt trong Word."""\n\nGHI_CHU_RA_SOAT = %s\n\nANS = %s\n\nEXPLANATIONS = %s\n'
            % (tn, pprint.pformat(notes, width=150), pprint.pformat(ANS, width=150, sort_dicts=False), pprint.pformat(EXPL, width=150, sort_dicts=False)))
        print('Test %d: %d nhóm, %d câu, cảnh báo: %s' % (tn, len(gl), nq, warn))


if __name__ == '__main__':
    main()
