# -*- coding: utf-8 -*-
"""Nạp các trang IELTS Reading (viết sẵn) vào web tổng: bọc đăng nhập + cầu nối kết quả, sinh thẻ trang chủ & danh mục giao bài.
Nguồn: ielts_src/reading/FullTest/*.html và ielts_src/reading/TheoDang/<Dạng>/*.html (giữ nguyên nội dung, chỉ chèn <script> vào <head>/<body>)."""
import os, re, html, glob, json

TYPES = [  # (thư mục, mã bộ, tên hiển thị)
    ('Completion', 'completion', 'Completion'),
    ('Matching', 'matching', 'Matching'),
    ('MultipleChoice', 'mcq', 'Multiple Choice'),
    ('TrueFalseNotGiven', 'tfng', 'True / False / Not Given'),
    ('YesNoNotGiven', 'ynng', 'Yes / No / Not Given'),
]
SOON = [('Listening', '🎧'), ('Writing', '✍️'), ('Speaking', '🗣️')]
URL_RE = re.compile(r'https://script\.google\.com/macros/s/[A-Za-z0-9_-]+/exec')


def _natural(s):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', s)]


def _wrap(src, out, root_rel, set_id, page_id, kind, apps_url, auth_head, bv):
    t = open(src, encoding='utf8').read()
    t = URL_RE.sub(apps_url, t)
    head = (auth_head % (apps_url, root_rel, root_rel)
            + '<script>GNAuth.requireSet(%s)</script>' % json.dumps(set_id)
            + '<script>window.GN_RD=%s</script>' % json.dumps({'set': set_id, 'page': page_id, 'kind': kind})
            + '<script src="%sengine/reading_shim.js?v=%s"></script>' % (root_rel, bv))
    assert '<head>' in t and '</body>' in t, src
    t = t.replace('<head>', '<head>' + head, 1)
    t = t.replace('</body>', '<script>GNAuth.verify()</script><script src="%sengine/feedback.js?v=%s"></script></body>' % (root_rel, bv), 1)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf8').write(t)
    return t


def build(root, apps_url, auth_head, bv):
    """Trả về {'cards': [html], 'catalog': [...], 'n': số bộ} và ghi các trang vào WebBaiTap/IELTS/Reading/."""
    base = os.path.join(root, 'ielts_src', 'reading')
    out_base = os.path.join(root, 'WebBaiTap', 'IELTS', 'Reading')
    cards, cat = [], []
    # --- Full Test ---
    tiles = []
    files = sorted(glob.glob(os.path.join(base, 'FullTest', 'Test*_Reading.html')), key=lambda p: _natural(os.path.basename(p)))
    for f in files:
        n = int(re.match(r'Test(\d+)_Reading', os.path.basename(f)).group(1))
        sid, pid = 'ielts-rd-test%02d' % n, os.path.splitext(os.path.basename(f))[0]
        t = _wrap(f, os.path.join(out_base, 'FullTest', os.path.basename(f)), '../../../../', sid, pid, 'full', apps_url, auth_head, bv)
        m = re.search(r'thời gian: (\d+) phút, (\d+) câu', t)
        mins, q = (m.group(1), m.group(2)) if m else ('60', '40')
        tiles.append('<a class="tile t-test" data-m="test" data-sid="%s" href="WebBaiTap/IELTS/Reading/FullTest/%s"><span class="ic">📖</span><b>Test %d</b><small>%s câu · %s phút</small></a>' % (sid, os.path.basename(f), n, q, mins))
        cat.append({'id': sid, 'title': 'IELTS Reading · Full Test %d' % n, 'grade': 'IELTS', 'unit': 'Reading', 'kind': 'full'})
    cards.append('<section class="card setcard" data-g="IELTS" data-u="Reading" data-k="full"><div class="settitle"><span class="chip">IELTS · Reading</span><h3>Full Test (%d đề · 40 câu · 60 phút)</h3></div><div class="tiles">%s</div></section>' % (len(files), ''.join(tiles)))
    # --- Theo dạng ---
    for d, code, label in TYPES:
        sid = 'ielts-rd-' + code
        fs = sorted(glob.glob(os.path.join(base, 'TheoDang', d, '*.html')), key=lambda p: _natural(os.path.basename(p)))
        tl = []
        for f in fs:
            name = os.path.basename(f)
            m = re.match(r'Test(\d+)_Passage(\d+)_', name)
            t = _wrap(f, os.path.join(out_base, 'TheoDang', d, name), '../../../../../', sid, os.path.splitext(name)[0], d, apps_url, auth_head, bv)
            tt = re.search(r'<title>([^<]*)</title>', t)
            mm = re.search(r'thời gian: (\d+) phút, (\d+) câu', t)
            mins, q = (mm.group(1), mm.group(2)) if mm else ('30', '?')
            tl.append('<a class="tile t-test" data-m="test" data-sid="%s" title="%s" href="WebBaiTap/IELTS/Reading/TheoDang/%s/%s"><span class="ic">📖</span><b>Test %s · P%s</b><small>%s câu · %s phút</small></a>'
                      % (sid, html.escape(tt.group(1) if tt else name), d, name, m.group(1), m.group(2), q, mins))
        cards.append('<section class="card setcard" data-g="IELTS" data-u="Reading" data-k="dang"><div class="settitle"><span class="chip">IELTS · Reading</span><h3>Theo dạng bài: %s (%d trang)</h3></div><div class="tiles">%s</div></section>' % (html.escape(label), len(fs), ''.join(tl)))
        cat.append({'id': sid, 'title': 'IELTS Reading · %s (%d trang)' % (label, len(fs)), 'grade': 'IELTS', 'unit': 'Reading', 'kind': 'dang'})
    # --- Kỹ năng sắp có (chỉ admin/giáo viên thấy) ---
    for sk, ic in SOON:
        cards.append('<section class="card setcard" data-g="IELTS" data-u="%s" data-k="soon" data-sid="__soon"><div class="settitle"><span class="chip">IELTS · %s</span><h3>%s %s</h3></div><p style="color:var(--mut,#667);margin:6px 0 0">Sắp có.</p></section>' % (sk, sk, ic, sk))
    return {'cards': cards, 'catalog': cat, 'n': len(cat)}
