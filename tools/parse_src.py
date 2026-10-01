"""Phân tích file trích xuất (src/*_c.txt) thành khung câu hỏi trắc nghiệm (JSON) để kiểm tra.
Chỉ dùng để chuyển đổi 1 lần: kết quả ghi ra units/*.py rồi chỉnh tay."""
import re, json, sys

START = re.compile(r'^\s*(?:Question\s+)?(\d{1,2})\s*[.:]?\s+(.*)$|^\s*(?:Question\s+)?(\d{1,2})\s*[.:]\s*$')
OPT_LINE = re.compile(r'^\s*A\.\s')


def cl(s):
    s = s.replace('⟦', '').replace('⟧', '')
    s = re.sub(r'\[(?:IMG|TICK)[^\]]*\]', '', s)
    s = s.replace('\t', ' ').replace('\xa0', ' ').replace('﻿', '').replace('​', '')
    s = re.sub(r'</?b>', '', s)
    s = re.sub(r'<u>\s*</u>', '', s)
    s = re.sub(r'</u>(\s*)<u>', r'\1', s) if False else s
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def split_opts(t):
    parts = re.split(r'(?:^|\s)([A-D])\.\s*', t)
    # parts: ['', 'A', 'text', 'B', 'text'...]
    opts = []
    i = 1
    while i < len(parts) - 1:
        opts.append(parts[i + 1].strip())
        i += 2
    return opts


INSTR = re.compile(r'^(Mark the letter|Read the following|Circle A|Find the mistakes|Complete the second|Choose the|Listen)', re.I)


def parse_mcq(lines, expect=None):
    """Trả về danh sách sự kiện: ('instr',txt) ('para',txt) ('item',{n,q,o})."""
    ev, cur = [], None
    last_n = [0]

    def fin():
        nonlocal cur
        if cur:
            opt_txt = ' '.join(cur['opt'])
            o = split_opts(opt_txt) if opt_txt else []
            ev.append(('item', {'n': cur['n'], 'q': ' '.join(cur['stem']).strip(), 'o': o}))
            last_n[0] = cur['n']
            cur = None

    for ln in lines:
        t = cl(ln)
        if not t:
            continue
        if INSTR.match(t) and not (cur and cur['opt'] and re.match(r'^[A-D]\.', t)):
            fin(); ev.append(('instr', t)); continue
        plain = re.sub(r'</?b>', '', ln).replace('⟦', '').replace('⟧', '').replace('\t', ' ')
        m = START.match(plain)
        is_item = False
        if m:
            n = int(m.group(1) or m.group(3))
            rest = (m.group(2) or '').strip()
            ref = cur['n'] if cur else last_n[0]
            is_item = (ref > 0 and 0 < n - ref <= 6) or (ref == 0 and expect is None and n == 1) or (expect is not None and ref == 0 and n == expect)
        if is_item:
            fin()
            rest = cl(rest)
            cur = {'n': n, 'stem': [], 'opt': []}
            if OPT_LINE.match(rest):
                cur['opt'].append(rest)
            elif rest:
                cur['stem'].append(rest)
        elif cur is None:
            ev.append(('para', t))
        else:
            nopt = len(re.findall(r'(?:^|\s)[A-D]\.\s', ' '.join(cur['opt'])))
            if cur['opt'] and nopt >= 4 and not re.match(r'^[A-D]\.\s', t):
                fin(); ev.append(('para', t))
            elif cur['opt'] or OPT_LINE.match(t):
                cur['opt'].append(t)
            else:
                cur['stem'].append(t)
    fin()
    return ev


def find(lines, pat, start=0):
    for i in range(start, len(lines)):
        if re.search(pat, lines[i]):
            return i
    raise KeyError(pat)


if __name__ == '__main__':
    raw = open(sys.argv[1]).read().split('\n')
    a, b = int(sys.argv[2]), int(sys.argv[3])
    ev = parse_mcq(raw[a - 1:b])
    print(json.dumps(ev, ensure_ascii=False, indent=1)[:6000])
