"""Hàm dùng chung cho tools/gen_mt1_test08.py, 09 (đọc src/mt1/dN.txt)."""
import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import cl, split_opts
from gen_units import dump, ROOT


def load_src(name, fixes=()):
    raw = open(os.path.join(ROOT, 'src/mt1/%s.txt' % name), encoding='utf8').read()
    for a, b in fixes:
        assert a in raw, a
        raw = raw.replace(a, b)
    return raw.split('\n')


def find(L, pat, start=0):
    for i in range(start, len(L)):
        if re.search(pat, L[i]):
            return i
    raise KeyError(pat)


def blocks(lines):
    """cắt dòng thành các khối 'Question N' -> {n: [dòng đã cl()]}"""
    out, cur = {}, None
    for ln in lines:
        t = cl(ln)
        m = re.match(r'^Question\s+(\d+)\s*[.:]?\s*(.*)$', t)
        if m:
            cur = int(m.group(1))
            out[cur] = [m.group(2)] if m.group(2) else []
        elif cur is not None and t:
            out[cur].append(t)
    return out


def mcq_item(gid, n, blk):
    """khối: dòng stem..., rồi các dòng phương án (bắt đầu 'A.'). Trả về item mcq"""
    k = next((i for i, t in enumerate(blk) if re.match(r'^A\s*[.\-–]', t) or re.match(r'^A\.', t)), None)
    stem = ' '.join(blk[:k]) if k is not None else ' '.join(blk)
    opts = split_opts(' '.join(blk[k:]))
    return {'id': '%s.%d' % (gid, n), 't': 'mcq', 'q': fix_blank(stem), 'o': opts}


def fix_blank(s):
    s = re.sub(r'\s*_{3,}\s*', ' ______ ', s)
    s = re.sub(r'\s+([.,?!;:])', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()
