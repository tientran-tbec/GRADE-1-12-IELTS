# -*- coding: utf-8 -*-
"""Môn Vật lí lớp 11 (Kết nối tri thức): sinh trang bài tập từ ngân hàng câu hỏi đã thẩm định (ly_src/bank_final.json).
Loại câu: trắc nghiệm 4 lựa chọn (mcq), đúng/sai 4 ý (tf4), trả lời ngắn (short, đáp số), tự luận (essay: AI gợi ý điểm + giáo viên duyệt).
Trang chạy bằng engine/physics.js (bản mở rộng của engine.js) + KaTeX (engine/katex/). Công thức LaTeX để nguyên trong $...$, KaTeX vẽ ở trình duyệt.
Cách dùng từ build.py: ly.build(ROOT, APPS_SCRIPT_URL, AUTH_HEAD, BV) -> {'cards','catalog','n','labels','order'}"""
import os, re, json, html, glob, shutil

GRADE_DIR, SUBJ_DIR = 'Lop11', 'Ly'
OUT_REL = os.path.join('WebBaiTap', GRADE_DIR, SUBJ_DIR)
ROOT_REL = '../../../'

BAI = {0: 'Tổng hợp', 1: 'Mô tả dao động', 2: 'Mô tả dao động (đồ thị, độ lệch pha)', 3: 'Vận tốc, gia tốc trong dao động điều hoà',
       4: 'Bài tập về dao động điều hoà', 5: 'Động năng, thế năng, sự chuyển hoá năng lượng', 6: 'Dao động tắt dần, cưỡng bức, cộng hưởng',
       7: 'Bài tập về sự chuyển hoá năng lượng', 8: 'Mô tả sóng', 9: 'Sóng ngang, sóng dọc, truyền năng lượng', 10: 'Thực hành đo tần số sóng âm',
       11: 'Sóng điện từ', 12: 'Giao thoa sóng', 13: 'Sóng dừng', 14: 'Bài tập về sóng', 15: 'Thực hành đo tốc độ truyền âm'}
KINDS = [('mcq', 'tn', 'Trắc nghiệm', '☑️', 20), ('tf4', 'ds', 'Đúng / Sai', '✅', 8), ('short', 'tln', 'Trả lời ngắn', '🔢', 12), ('essay', 'tl', 'Tự luận', '✍️', 6)]
LEVEL = {'NB': 0, 'TH': 1, 'VD': 2, 'VDC': 3}
EXAMS = [  # (tiền tố tên đề, mã bộ, mã nhóm (data-u), nhãn nhóm, tiêu đề thẻ)
    ('Đề kiểm tra giữa HK1 25-26', 'kt', 'LyKT', 'Kiểm tra giữa HK1 (25-26)', 'Đề kiểm tra giữa HK1 25-26'),
    ('Đề ôn tập giữa HK1 25-26', 'on', 'LyOn', 'Ôn tập giữa HK1 (25-26)', 'Đề ôn tập giữa HK1 25-26'),
    ('Đề ôn tập giữa HK1 KNTT', 'kntt', 'LyKNTT', 'Ôn tập giữa HK1 KNTT', 'Đề ôn tập giữa HK1 KNTT'),
]
UNIT_LABELS = {'LyKT': 'Kiểm tra giữa HK1 (25-26)', 'LyOn': 'Ôn tập giữa HK1 (25-26)', 'LyKNTT': 'Ôn tập giữa HK1 KNTT'}
for _b, _t in BAI.items():
    UNIT_LABELS['LyBai%02d' % _b] = 'Bài %d · %s' % (_b, _t) if _b else 'Tổng hợp'
LABEL_ORDER = ['LyBai%02d' % i for i in range(1, 16)] + ['LyBai00', 'LyKT', 'LyOn', 'LyKNTT']


def _natural(s):
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', str(s))]


def fmt(s):
    """Văn bản đề/lời giải → HTML (giữ nguyên $...$ cho KaTeX)."""
    if s is None:
        return ''
    s = html.escape(str(s), quote=False)
    s = re.sub(r'\*\*([^*\n]+)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\[\[IMG:([^\]]+)\]\]', lambda m: '<img class="pic wide" loading="lazy" alt="Hình minh hoạ" src="@@IMG:%s@@">' % m.group(1), s)
    return s.replace('\n', '<br>')


def theory_html(body):
    out, ul = [], False
    for ln in str(body or '').split('\n'):
        m = re.match(r'^\s*[-•*]\s+(.*)$', ln)
        if m:
            if not ul: out.append('<ul>'); ul = True
            out.append('<li>%s</li>' % fmt(m.group(1)))
        else:
            if ul: out.append('</ul>'); ul = False
            if ln.strip(): out.append('<p>%s</p>' % fmt(ln))
    if ul: out.append('</ul>')
    return ''.join(out)


def json_script(o):
    return json.dumps(o, ensure_ascii=False).replace('</', '<\\/')


def qnum(ref):
    m = re.search(r'Câu\s*(\d+)', ref or '')
    return int(m.group(1)) if m else 999


def render_item(it, num):
    uid, k = it['uid'], it['kind']
    b = '<div class="stem">%s</div>' % fmt(it['q'])
    if k == 'mcq':
        b += '<div class="opts cols">' + ''.join(
            '<label class="opt"><input type="radio" name="%s" value="%s"><span><b>%s.</b> %s</span></label>' % (html.escape(uid), 'ABCD'[i], 'ABCD'[i], fmt(o))
            for i, o in enumerate(it['opts'])) + '</div>'
    elif k == 'tf4':
        rows = ''
        for i, st in enumerate(it['stems']):
            n = html.escape(uid) + '_' + str(i)
            rows += ('<div class="tfr" data-i="%d"><div class="st"><b>%s)</b> %s</div><div class="tfo">'
                     '<label class="opt"><input type="radio" name="%s" value="T"><span>Đúng</span></label>'
                     '<label class="opt"><input type="radio" name="%s" value="F"><span>Sai</span></label></div></div>') % (i, 'abcd'[i], fmt(st), n, n)
        b += '<div class="tf4">%s</div><button type="button" class="btn sm chk">Kiểm tra</button>' % rows
    elif k == 'short':
        b += ('<div class="num"><input type="text" class="blank numin" inputmode="decimal" autocomplete="off" placeholder="Nhập đáp số">%s'
              ' <button type="button" class="btn sm chk">Kiểm tra</button></div>') % ((' <span class="hint">%s</span>' % html.escape(it['unit'])) if it.get('unit') else '')
    elif k == 'essay':
        syms = ''.join('<button type="button" data-s="%s">%s</button>' % (html.escape(s), html.escape(s)) for s in ['π', 'ω', 'φ', 'λ', 'Δ', 'α', 'Σ', '√', '²', '³', '°', '×', '·', '→', '≈', '≤', '≥', '±'])
        b += ('<div class="sym" title="Chèn ký hiệu">%s</div><textarea class="open ly-essay" placeholder="Trình bày lời giải: viết công thức, thay số, kết quả kèm đơn vị…"></textarea>'
              '<div class="essay-actions"><button type="button" class="btn sm esub">Nộp để AI gợi ý điểm</button> <button type="button" class="btn sm ghost eshow">Xem lời giải mẫu</button></div>'
              '<div class="essay-res" hidden></div>') % syms
    meta = ''
    if it.get('level'):
        meta = '<div class="qmeta">%s</div>' % html.escape({'NB': 'Nhận biết', 'TH': 'Thông hiểu', 'VD': 'Vận dụng', 'VDC': 'Vận dụng cao'}.get(it['level'], it['level']))
    return ('<div class="q" data-id="%s" data-t="%s"><div class="qn">%s</div><div class="qb">%s%s<div class="exp" data-for="%s" hidden></div></div></div>'
            % (html.escape(uid), k, num, meta + b, '', html.escape(uid)))


def item_cfg(it):
    k = it['kind']
    c = {'t': k, 'bai': it.get('bai'), 'sol': fmt(it.get('sol'))}
    if k == 'essay':
        c.update(max=it.get('total') or 1.0, final=it.get('final') or '', rubric=it.get('rubric') or [])
    else:
        c.update(ans=it['ans'])
        if k == 'short':
            c.update(tol=it.get('tol'), alts=it.get('alts') or [], unit=it.get('unit') or '')
    return c


PART_TITLES = {'mcq': ('PHẦN I. Câu trắc nghiệm nhiều phương án lựa chọn', 'Mỗi câu có 4 phương án, chỉ chọn một đáp án đúng (0,25 điểm).'),
               'tf4': ('PHẦN II. Câu trắc nghiệm đúng sai', 'Trong mỗi ý a), b), c), d) chọn Đúng hoặc Sai. Đúng 1 ý: 0,1 · 2 ý: 0,25 · 3 ý: 0,5 · 4 ý: 1,0 điểm.'),
               'short': ('PHẦN III. Câu trắc nghiệm trả lời ngắn', 'Điền đáp số (có thể dùng dấu phẩy hoặc dấu chấm thập phân). Mỗi câu 0,25 điểm.'),
               'essay': ('PHẦN IV. Tự luận', 'Viết lời giải đầy đủ. Bấm “Nộp để AI gợi ý điểm”: AI chấm gợi ý theo biểu điểm, giáo viên sẽ duyệt điểm chính thức.')}


def shell(title, sub, body, sid, mode, auth_head, apps_url, bv, nav='', cfg=None, h1=None, theory=False):
    ah = auth_head % (apps_url, ROOT_REL, ROOT_REL)
    scripts = ''
    if cfg is not None:
        scripts = ('<script>window.QUIZ=%s;</script><script src="%sengine/katex/katex.min.js"></script><script src="%sengine/katex/auto-render.min.js"></script>'
                   '<script src="%sengine/physics.js?v=%s"></script>') % (json_script(cfg), ROOT_REL, ROOT_REL, ROOT_REL, bv)
    elif theory:
        scripts = ('<script src="%sengine/katex/katex.min.js"></script><script src="%sengine/katex/auto-render.min.js"></script>'
                   '<script src="%sengine/physics.js?v=%s"></script>') % (ROOT_REL, ROOT_REL, ROOT_REL, bv)
    return ('<!doctype html>\n<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title>'
            '<link rel="stylesheet" href="%sengine/engine.css?v=%s"><link rel="stylesheet" href="%sengine/katex/katex.min.css"><link rel="stylesheet" href="%sengine/physics.css?v=%s">'
            '%s<script>GNAuth.requireSet(%s)</script></head><body class="ly"><header class="top"><div class="wrap"><span class="badge%s">%s</span><h1>%s</h1><div class="sub">%s</div>%s</div></header>%s'
            '<script>GNAuth.chip(".top .wrap");GNAuth.verify();</script><script>window.GN_SET=%s;window.GN_LY={set:%s,mode:%s}</script>%s'
            '<script src="%sengine/feedback.js?v=%s"></script></body></html>'
            % (html.escape(title), ROOT_REL, bv, ROOT_REL, ROOT_REL, bv, ah, json.dumps(sid), ' test' if mode == 'test' else '',
               'Kiểm tra' if mode == 'test' else ('Lý thuyết' if theory else 'Luyện tập'), html.escape(h1 or title), html.escape(sub), nav, body,
               json.dumps(sid), json.dumps(sid), json.dumps(mode), scripts, ROOT_REL, bv))


def page_html(sid, pid, title, sub, items, mode, minutes, nav, auth_head, apps_url, bv, h1=None):
    test = mode == 'test'
    order, meta, parts = [], {}, []
    if test:
        parts.append('<div class="card rules"><b>📋 Quy định làm bài</b><ul><li>Thời gian: <b>%d phút</b>. Còn 10 phút hệ thống nhắc; hết giờ có thêm 5 phút gia hạn rồi tự động nộp.</li>'
                     '<li>Bài làm ở chế độ <b>toàn màn hình</b>. Chuyển tab, mất focus, thoát toàn màn hình đều bị ghi nhận và báo cho giáo viên.</li>'
                     '<li>Không dùng chuột phải, sao chép/dán, phím tắt. Trợ lý AI chỉ mở sau khi nộp bài. Phần tự luận: AI gợi ý điểm, giáo viên duyệt điểm chính thức.</li></ul></div>' % minutes)
    parts.append('<div class="result" id="result" hidden></div>')
    n = 0
    for kind in ('mcq', 'tf4', 'short', 'essay'):
        its = [x for x in items if x['kind'] == kind]
        if not its:
            continue
        t, ins = PART_TITLES[kind]
        parts.append('<section class="card group"><h3>%s</h3><div class="instr">%s</div>' % (t, html.escape(ins)))
        for i, it in enumerate(its, 1):
            parts.append(render_item(it, i))
            order.append(it['uid']); meta[it['uid']] = item_cfg(it)
        parts.append('</section>')
    bar = ('<div class="bar"><div class="prog"><i id="progBar"></i></div><div class="in">%s<span class="stat grow" id="stat"></span>'
           '<button class="btn ghost" id="reset" type="button">Làm lại</button><button class="btn" id="lySubmit" type="button">%s</button></div></div>'
           % ('<span class="timer" id="timer">--:--</span>' if test else '', 'Nộp bài' if test else 'Nộp kết quả'))
    modal = ('<div class="modal" id="startModal"><div class="box"><h3>%s</h3><p>Nhập thông tin để hệ thống ghi nhận kết quả.</p>'
             '<label>Họ và tên<input type="text" id="stName" autocomplete="name"></label><label>Lớp<input type="text" id="stClass"></label><div id="stErr" style="color:var(--bad)"></div>'
             '<button class="btn" id="startBtn" type="button">%s</button> %s</div></div>'
             % ('Bắt đầu làm bài kiểm tra' if test else 'Bắt đầu luyện tập', 'Bắt đầu làm bài' if test else 'Bắt đầu',
                '' if test else '<button class="btn ghost" id="skipBtn" type="button">Luyện tập không ghi tên</button>'))
    warn = '<div class="modal" id="warnModal" hidden><div class="box"><h3>Nhắc giờ</h3><p id="warnText"></p><button class="btn" id="warnOk" type="button">Đã hiểu</button></div></div><div class="toast" id="toast" hidden></div>'
    if test:
        warn += ('<div class="modal" id="timeUpModal" hidden><div class="box"><h3>⏰ Đã hết giờ làm bài</h3><p>Bạn có thêm <b>5 phút</b> để hoàn tất. Hết 5 phút bài sẽ tự động nộp.</p>'
                 '<button class="btn" id="timeUpSubmit" type="button">Nộp bài ngay</button> <button class="btn ghost" id="timeUpBack" type="button">Làm tiếp</button></div></div>'
                 '<div class="modal fsov" id="fsOverlay" hidden><div class="box"><h3>⚠ Bạn đã thoát toàn màn hình</h3><p>Hành vi này đã được ghi nhận. Hãy quay lại chế độ toàn màn hình để tiếp tục làm bài.</p>'
                 '<button class="btn" id="fsBack" type="button">Vào toàn màn hình</button></div></div>')
    cfg = {'setId': sid, 'pageId': pid, 'mode': mode, 'minutes': minutes, 'warnAt': 10 if test else 0, 'url': '@@URL@@', 'order': order, 'items': meta, 'ly': True}
    body = '<div class="wrap">' + ''.join(parts) + '</div>' + bar + modal + warn
    cfg['url'] = apps_url
    return shell(title + ' – Vật lí 11', sub, body, sid, mode, auth_head, apps_url, bv, nav=nav, cfg=cfg, h1=h1 or title)


def build(root, apps_url, auth_head, bv):
    src = os.path.join(root, 'ly_src')
    bank_p = os.path.join(src, 'bank_final.json')
    if not os.path.exists(bank_p):
        return {'cards': [], 'catalog': [], 'n': 0, 'labels': {}, 'order': []}
    B = json.load(open(bank_p, encoding='utf8'))
    items, theory = B['items'], B['theory']
    out = os.path.join(root, OUT_REL)
    if os.path.isdir(out):
        for f in glob.glob(os.path.join(out, '*.html')) + glob.glob(os.path.join(out, '*.json')):
            os.remove(f)
    os.makedirs(os.path.join(out, 'img'), exist_ok=True)
    imgs = {}
    for f in os.listdir(os.path.join(src, 'img')):
        imgs[os.path.splitext(f)[0]] = f
    used = set()

    def finish(t):   # gắn đường dẫn ảnh thật
        def r(m):
            n = m.group(1)
            if n not in imgs:
                return 'missing.png'
            used.add(imgs[n]); return 'img/' + imgs[n]
        return re.sub(r'@@IMG:([^@]+)@@', r, t)

    def write(name, t):
        open(os.path.join(out, name), 'w', encoding='utf8').write(finish(t))

    cards, cat, npages = [], [], 0
    icon_of = {k: ic for k, _, _, ic, _ in KINDS}
    # ---------- theo từng bài ----------
    for bai in sorted({i['bai'] or 0 for i in items}):
        its = [i for i in items if (i['bai'] or 0) == bai]
        th = [t for t in theory if (t['bai'] or 0) == bai]
        sid = 'ly11-b%02d' % bai
        udir = 'LyBai%02d' % bai
        pages = []   # (pid, label, kind, chunk items)
        for kind, code, label, ic, size in KINDS:
            ks = sorted([i for i in its if i['kind'] == kind], key=lambda x: (LEVEL.get(x.get('level'), 1), _natural(x['uid'])))
            for ci in range(0, len(ks), size):
                pages.append(('b%02d-%s-%d' % (bai, code, ci // size + 1), label, kind, ks[ci:ci + size]))
        if not pages and not th:
            continue
        has_th = bool(th)

        def nav_for(cur):
            kinds_first = {}
            for pid, label, kind, ch in pages:
                kinds_first.setdefault(kind, (pid, label))
            tabs = []
            if has_th:
                tabs.append(('b%02d-ly-thuyet' % bai, 'Lý thuyết', cur == 'b%02d-ly-thuyet' % bai))
            curkind = next((p[2] for p in pages if p[0] == cur), None)
            for kind, code, label, ic, size in KINDS:
                if kind in kinds_first:
                    tabs.append((kinds_first[kind][0], label, kind == curkind))
            h = '<nav class="tabs">%s<a href="%sindex.html">⌂ Trang chủ</a></nav>' % (''.join('<a href="%s.html"%s>%s</a>' % (p, ' class="cur"' if c else '', html.escape(l)) for p, l, c in tabs), ROOT_REL)
            sib = [p for p in pages if p[2] == curkind]
            if curkind and len(sib) > 1:
                h += '<nav class="tabs sub">%s</nav>' % ''.join('<a href="%s.html"%s>%s</a>' % (p[0], ' class="cur"' if p[0] == cur else '', p[0].rsplit('-', 1)[1]) for p in sib)
            return h
        if has_th:
            body = '<div class="wrap"><div class="card theory">%s</div></div>' % ''.join('<h3>%s</h3>%s' % (html.escape(t.get('title') or ''), theory_html(t.get('body'))) for t in th)
            write('b%02d-ly-thuyet.html' % bai, shell('Lý thuyết – Bài %d – Vật lí 11' % bai, 'Bài %d · %s' % (bai, BAI.get(bai, '')), body, sid, 'prac', auth_head, apps_url, bv, nav=nav_for('b%02d-ly-thuyet' % bai), h1='Lý thuyết', theory=True))
            npages += 1
        tiles = []
        if has_th:
            tiles.append('<a class="tile t-theory" data-m="prac" href="WebBaiTap/%s/%s/b%02d-ly-thuyet.html"><span class="ic">📘</span><b>Lý thuyết</b><small>Tóm tắt</small></a>' % (GRADE_DIR, SUBJ_DIR, bai))
        for pid, label, kind, ch in pages:
            part = pid.rsplit('-', 1)[1]
            total = len([p for p in pages if p[2] == kind])
            title = 'Bài %d · %s%s' % (bai, label, (' · phần %s' % part) if total > 1 else '')
            write(pid + '.html', page_html(sid, pid, title, 'Bài %d · %s  ·  %d câu' % (bai, BAI.get(bai, ''), len(ch)), ch, 'prac', 0, nav_for(pid), auth_head, apps_url, bv))
            npages += 1
            tiles.append('<a class="tile" data-m="prac" data-sid="%s" href="WebBaiTap/%s/%s/%s.html"><span class="ic">%s</span><b>%s%s</b><small>%d câu</small></a>'
                         % (sid, GRADE_DIR, SUBJ_DIR, pid, icon_of[kind], html.escape(label), (' ' + part) if total > 1 else '', len(ch)))
        ttl = 'Bài %d · %s' % (bai, BAI.get(bai, '')) if bai else 'Ôn tập tổng hợp'
        cards.append('<section class="card setcard" data-g="11" data-s="Lý" data-u="%s" data-k="luyentap" data-sid="%s"><div class="settitle"><span class="chip">Lớp 11 · Vật lí</span><h3>%s</h3></div><div class="tiles">%s</div></section>'
                     % (udir, sid, html.escape(ttl), ''.join(tiles)))
        cat.append({'id': sid, 'title': 'Vật lí 11 · ' + ttl, 'grade': 11, 'unit': UNIT_LABELS[udir], 'kind': 'luyentap'})
    # ---------- đề thi ----------
    byexam = {}
    for it in items:
        for e in it['exams']:
            byexam.setdefault(e['name'], []).append((qnum(e['ref']), it))
    for prefix, code, udir, ulabel, ctitle in EXAMS:
        names = sorted([n for n in byexam if n.startswith(prefix)], key=lambda n: _natural(n.split('–')[-1]))
        tiles = []
        for nm in names:
            de = nm.split('–')[-1].strip()                       # "Đề 3"
            num = re.sub(r'^Đề\s*', '', de)
            sid, pid = 'ly11-%s-de%s' % (code, num), '%s-de%s' % (code, num)
            kord = {'mcq': 0, 'tf4': 1, 'short': 2, 'essay': 3}
            its = [it for _, it in sorted(byexam[nm], key=lambda x: (kord[x[1]['kind']], x[0], x[1]['uid']))]
            ne = len([i for i in its if i['kind'] == 'essay'])
            minutes = 45 + 10 * ne if ne else 45
            write(pid + '.html', page_html(sid, pid, '%s – %s' % (ctitle, de), '%s  ·  %d câu  ·  %d phút' % (ulabel, len(its), minutes), its, 'test', minutes,
                                           '<nav class="tabs"><a href="%sindex.html">⌂ Trang chủ</a></nav>' % ROOT_REL, auth_head, apps_url, bv, h1='%s – %s' % (ctitle, de)))
            npages += 1
            tiles.append('<a class="tile t-test" data-m="test" data-sid="%s" href="WebBaiTap/%s/%s/%s.html"><span class="ic">📝</span><b>%s</b><small>%d câu · %d phút</small></a>' % (sid, GRADE_DIR, SUBJ_DIR, pid, html.escape(de), len(its), minutes))
            cat.append({'id': sid, 'title': 'Vật lí 11 · %s – %s' % (ctitle, de), 'grade': 11, 'unit': ulabel, 'kind': 'test'})
        if tiles:
            cards.append('<section class="card setcard" data-g="11" data-s="Lý" data-u="%s" data-k="test"><div class="settitle"><span class="chip">Lớp 11 · Vật lí</span><h3>%s (%d đề)</h3></div><div class="tiles">%s</div></section>'
                         % (udir, html.escape(ctitle), len(tiles), ''.join(tiles)))
    # ---------- khoá tự luận (cho máy chủ chấm AI) ----------
    key = {}
    for it in items:
        if it['kind'] == 'essay':
            q = re.sub(r'\[\[IMG:[^\]]+\]\]', '[hình minh hoạ]', it['q'])
            key[it['uid']] = {'q': q, 'max': it.get('total') or 1.0, 'final': it.get('final') or '', 'sol': it.get('sol') or '', 'rubric': it.get('rubric') or [], 'keywords': it.get('keywords') or []}
    json.dump(key, open(os.path.join(out, 'essay_key.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
    # ---------- ảnh ----------
    for f in used:
        shutil.copy2(os.path.join(src, 'img', f), os.path.join(out, 'img', f))
    for f in os.listdir(os.path.join(out, 'img')):
        if f not in used:
            os.remove(os.path.join(out, 'img', f))
    return {'cards': cards, 'catalog': cat, 'n': len(cat), 'pages': npages, 'labels': UNIT_LABELS, 'order': LABEL_ORDER}
