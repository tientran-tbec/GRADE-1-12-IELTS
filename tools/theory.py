"""Chuyển vùng 'lý thuyết' (có bảng) từ file trích xuất sang HTML sạch."""
import re, html


def _parse(lines, i):
    nodes = []
    while i < len(lines):
        s = lines[i].strip()
        if s == '<TABLE>':
            tbl, i = _table(lines, i + 1)
            nodes.append(tbl)
        elif s in ('<ROW>', '<CELL>', '</TABLE>'):
            return nodes, i
        else:
            nodes.append(lines[i])
            i += 1
    return nodes, i


def _table(lines, i):
    rows = []
    while i < len(lines):
        s = lines[i].strip()
        if s == '</TABLE>':
            return ('T', rows), i + 1
        if s == '<ROW>':
            rows.append([])
            i += 1
        elif s == '<CELL>':
            nodes, i = _parse(lines, i + 1)
            rows[-1].append(nodes)
        else:
            i += 1
    return ('T', rows), i


def _inline(s, imgdir):
    s = s.replace('\xa0', ' ').replace('\t', ' ').replace('﻿', '')
    s = re.sub(r'\[TICK\]', '', s)
    s = re.sub(r'\[IMG:([^\]]+)\]', lambda m: '<img src="%s/%s" alt="">' % (imgdir, m.group(1)) if imgdir else '', s)
    s = s.replace('⟦', '<mark>').replace('⟧', '</mark>')
    s = re.sub(r'<mark>\s*</mark>', '', s)
    s = re.sub(r'</u>(\s*)<u>', r'\1', s)
    s = re.sub(r'</b>(\s*)<b>', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def _render(nodes, imgdir):
    out = []
    for n in nodes:
        if isinstance(n, tuple):
            rows = n[1]
            out.append('<table class="th">')
            for r, row in enumerate(rows):
                out.append('<tr>')
                for c in row:
                    inner = _render(c, imgdir)
                    tag = 'th' if (r == 0 and len(rows) > 1 and not re.search(r'<table', inner)) else 'td'
                    out.append('<%s>%s</%s>' % (tag, inner, tag))
                out.append('</tr>')
            out.append('</table>')
        else:
            t = _inline(n, imgdir)
            if t and not re.fullmatch(r'(<[^>]+>|\s)*', t):
                out.append('<p>%s</p>' % t)
    return ''.join(out)


def theory_html(lines, imgdir=''):
    nodes, _ = _parse(lines, 0)
    return _render(nodes, imgdir)
