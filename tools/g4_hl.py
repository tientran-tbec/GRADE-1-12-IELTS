# -*- coding: utf-8 -*-
"""docx -> text có đánh dấu chỗ tô vàng bằng ⟦ ⟧ (đáp án trong phần KEY). Duyệt đoạn + bảng theo thứ tự."""
import docx, re, sys
from docx.oxml.ns import qn

def run_hl(r):
    rpr = r.find(qn('w:rPr'))
    if rpr is None: return False
    shd = rpr.find(qn('w:shd'))
    if shd is not None and shd.get(qn('w:fill')) not in (None, 'auto', 'FFFFFF', 'ffffff'): return True
    h = rpr.find(qn('w:highlight'))
    if h is not None and h.get(qn('w:val')) not in (None, 'none'): return True
    return False

IMG = None   # {'rels': {rId: part}, 'dir': path, 'n': counter, 'seen': {rId: name}}
A_NS = 'http://schemas.openxmlformats.org/drawingml/2006/main'
R_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'


def _img_tokens(r):
    """các ảnh nằm trong run r -> chuỗi ' [img:NN] '"""
    if IMG is None: return ''
    out = ''
    ids = [b.get('{%s}embed' % R_NS) for b in r.iter('{%s}blip' % A_NS)]
    ids += [b.get('{urn:schemas-microsoft-com:office:office}relid') or b.get('{%s}id' % R_NS) for b in r.iter('{urn:schemas-microsoft-com:vml}imagedata')]
    for rid in ids:
        if not rid or rid not in IMG['rels']: continue
        if rid not in IMG['seen']:
            IMG['n'] += 1
            nm = 'img%02d' % IMG['n']
            IMG['seen'][rid] = nm
            try:
                from PIL import Image
                import io
                im = Image.open(io.BytesIO(IMG['rels'][rid].blob)); im.load()
                if im.mode in ('RGBA', 'LA', 'P'):
                    im = im.convert('RGBA'); bg = Image.new('RGBA', im.size, 'white'); bg.alpha_composite(im); im = bg
                im.convert('RGB').save('%s/%s.png' % (IMG['dir'], nm))
            except Exception as e:
                IMG['seen'][rid] = nm + '(lỗi)'
        out += ' [img:%s] ' % IMG['seen'][rid]
    return out


def para_text(p):
    out = []
    cur = None
    for r in p.iter(qn('w:r')):
        t = ''.join(x.text or '' for x in r.iter(qn('w:t')))
        if r.find(qn('w:tab')) is not None: t = '\t' + t
        t += _img_tokens(r)
        if not t: continue
        hl = run_hl(r)
        if hl and cur is False or not hl and cur is True or cur is None:
            pass
        if hl and not cur: out.append('⟦')
        if not hl and cur: out.append('⟧')
        cur = hl
        out.append(t)
    if cur: out.append('⟧')
    s = ''.join(out).replace('\xa0', ' ')
    s = s.replace('⟧⟦', '').replace('⟦ ', ' ⟦').replace(' ⟧', '⟧ ')
    return re.sub(r'[ \t]+', ' ', s).strip()

def dump(path, imgdir=None):
    """imgdir: nếu có, lưu ảnh (nền trắng) vào đó dưới tên img01.png… và chèn [img:imgNN] vào đúng vị trí trong văn bản."""
    global IMG
    d = docx.Document(path)
    if imgdir:
        import os
        os.makedirs(imgdir, exist_ok=True)
        IMG = {'rels': {rid: rel.target_part for rid, rel in d.part.rels.items() if 'image' in rel.reltype}, 'dir': imgdir, 'n': 0, 'seen': {}}
    else:
        IMG = None
    lines = []
    for el in d.element.body.iterchildren():
        if el.tag == qn('w:p'):
            t = para_text(el)
            if t: lines.append(t)
        elif el.tag == qn('w:tbl'):
            for tr in el.iter(qn('w:tr')):
                cells = []
                for tc in tr.findall(qn('w:tc')):
                    cells.append(' ¦ '.join(x for x in (para_text(p) for p in tc.iter(qn('w:p'))) if x))
                lines.append('| ' + ' | '.join(cells) + ' |')
    return lines

if __name__ == '__main__':
    print('\n'.join(dump(sys.argv[1])))
