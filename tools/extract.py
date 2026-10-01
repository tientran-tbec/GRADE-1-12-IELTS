"""Trích văn bản từ docx, giữ đánh dấu: ⟦…⟧ = highlight/đỏ, <u>, <b>, [IMG:file], [TICK]."""
import docx, sys, re
from docx.table import Table
from docx.text.paragraph import Paragraph
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'


def run_txt(r, doc):
    t = r.text
    # images / ticks inside the run
    extra = ''
    for el in r._r.iter():
        if el.tag == A + 'blip':
            rid = el.get(R + 'embed')
            if rid and rid in doc.part.rels:
                extra += '[IMG:%s]' % doc.part.rels[rid].target_ref.split('/')[-1]
        if el.tag == W + 'sym' and el.get(W + 'char', '').upper().endswith('FC'):
            extra += '[TICK]'
    if not t:
        return extra
    f = r.font
    hl = bool(f.highlight_color)
    rpr = r._r.rPr
    if rpr is not None and rpr.find(W + 'shd') is not None:
        hl = True
    col = ''
    try:
        if f.color is not None and f.color.type is not None and f.color.rgb is not None:
            col = str(f.color.rgb)
    except Exception:
        pass
    red = col in ('FF0000', 'C00000', 'EE0000')
    s = t
    if r.underline:
        s = '<u>' + s + '</u>'
    if r.bold and t.strip():
        s = '<b>' + s + '</b>'
    if hl or red:
        s = '⟦' + s + '⟧'
    return s + extra


def para_txt(p, doc):
    out = ''.join(run_txt(r, doc) for r in p.runs)
    for a, b in (('</b><b>', ''), ('</u><u>', ''), ('⟧⟦', '')):
        out = out.replace(a, b)
    return out


def walk(el, doc, lines, depth=0):
    for ch in el.iterchildren():
        if ch.tag == W + 'p':
            lines.append('  ' * depth + para_txt(Paragraph(ch, doc), doc))
        elif ch.tag == W + 'tbl':
            t = Table(ch, doc)
            lines.append('  ' * depth + '<TABLE>')
            for row in t.rows:
                lines.append('  ' * depth + ' <ROW>')
                seen = set()
                for c in row.cells:
                    if id(c._tc) in seen:
                        continue
                    seen.add(id(c._tc))
                    lines.append('  ' * depth + '  <CELL>')
                    walk(c._tc, doc, lines, depth + 2)
            lines.append('  ' * depth + '</TABLE>')
        elif ch.tag == W + 'sdt':
            c = ch.find(W + 'sdtContent')
            if c is not None:
                walk(c, doc, lines, depth)


if __name__ == '__main__':
    d = docx.Document(sys.argv[1])
    L = []
    walk(d.element.body, d, L)
    open(sys.argv[2], 'w').write('\n'.join(L))
    print(len(L))
