# -*- coding: utf-8 -*-
"""Lớp BUILD: các hàm renderer + ghép trang HTML từ dữ liệu (units/*.py) và đáp án (units/*_dapan.py).
Chạy:  python3 build.py            (sinh toàn bộ WebBaiTap/ + index.html)
       python3 build.py lop11-u1-botro   (chỉ 1 bộ)
"""
import os, sys, json, re, html, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'WebBaiTap')
APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbyfZgrcZfOw-g5nCLlQ5QyLCCADuct8QRxW31SG8F3IZfkgL0x_3LOoPWBHRFRNiXA1/exec'   # update_links.py sẽ thay giá trị này
PAGES_URL = 'https://tientran-tbec.github.io/GRADE-6-12/'

# (id bộ, file dữ liệu, file đáp án, thư mục lớp, thư mục unit, slug thư mục, ảnh)
REGISTRY = [
    ('lop11-u1-botro', 'units/lop11_u1_botro.py', 'units/lop11_u1_botro_dapan.py', 'Lop11', 'Unit1', 'botro', 'assets/lop11_u1/botro', 'audio/lop11_u1_botro_nghe.mp3'),
    ('lop11-u1-4kn', 'units/lop11_u1_4kn.py', 'units/lop11_u1_4kn_dapan.py', 'Lop11', 'Unit1', '4kn', 'assets/lop11_u1/4kn', 'audio/lop11_u1_4kn_nghe.mp3'),
]


def load_py(path, attr):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return None
    spec = importlib.util.spec_from_file_location('m_' + os.path.basename(p)[:-3], p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return getattr(m, attr, None)


def load_answers(path):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return {}, {}
    spec = importlib.util.spec_from_file_location('ans_' + os.path.basename(p)[:-3], p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return getattr(m, 'ANS', {}), getattr(m, 'EXPLANATIONS', {})


# ------------------------------------------------------------------ renderers
def esc_attr(s):
    return html.escape(str(s), quote=True)


def radio_item(it, plain=False, short=True):
    """Trắc nghiệm 1 đáp án (mcq)."""
    opts = it['o']
    cols = ' cols' if (len(opts) <= 4 and all(len(re.sub(r'<[^>]+>', '', o)) <= 22 for o in opts)) else ''
    out = ['<div class="opts%s">' % cols]
    for i, o in enumerate(opts):
        L = 'ABCDEF'[i]
        if it.get('plain'):
            out.append('<label class="opt"><input type="radio" name="%s" value="%s"><span>%s</span></label>' % (esc_attr(it['id']), esc_attr(o), o))
        else:
            out.append('<label class="opt"><input type="radio" name="%s" value="%s"><span><b>%s.</b> %s</span></label>' % (esc_attr(it['id']), L, L, o))
    out.append('</div>')
    return ''.join(out)


def tf_item(it):
    vals = [('T', 'True'), ('F', 'False')] + ([('NG', 'Not given')] if it['t'] == 'tfng' else [])
    out = ['<div class="opts cols">']
    for v, lab in vals:
        out.append('<label class="opt"><input type="radio" name="%s" value="%s"><span>%s</span></label>' % (esc_attr(it['id']), v, lab))
    out.append('</div>')
    return ''.join(out)


LONG_GROUPS = {'vg8', 'kt-rw', 'wr1', 'wr2'}   # nhóm viết lại câu: dùng ô nhiều dòng, kéo giãn được


def text_item(it, test_mode):
    """Điền từ: thay mỗi {_} bằng ô nhập."""
    q = it['q']
    n = q.count('{_}')
    if n == 0:
        q = q + ' {_}'
        n = 1
    k = [0]

    long_ = bool(it.get('long')) or it['id'].split('.')[0] in LONG_GROUPS or it['id'].startswith('wr')

    def rep(_):
        i = k[0]
        k[0] += 1
        if long_:
            return '<br><textarea class="blank long" rows="3" data-id="%s" data-i="%d" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Viết câu hoàn chỉnh của bạn tại đây…" aria-label="ô viết %d"></textarea>' % (esc_attr(it['id']), i, i + 1)
        return '<input class="blank" type="text" data-id="%s" data-i="%d" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="ô điền %d">' % (esc_attr(it['id']), i, i + 1)
    s = re.sub(r'\{_\}', rep, q)
    extra = ''
    if it.get('hint'):
        extra += '<span class="hint">(%s)</span>' % html.escape(it['hint'])
    if it.get('nwords'):
        extra += '<span class="hint">(%d từ)</span>' % it['nwords']
    btn = '' if test_mode else ' <button class="btn sm chk" type="button">Kiểm tra</button>'
    return '<div class="stem">%s %s%s</div>' % (s, extra, btn)


def open_item(it, test_mode):
    btn = '' if test_mode else '<p><button class="btn sm chk" type="button">Xem đáp án mẫu</button></p>'
    return '<textarea class="open" rows="9" placeholder="Viết câu trả lời của bạn tại đây…"></textarea>' + btn


def bank_box(words):
    return '<div class="bank"><b>Từ/cụm từ cho sẵn:</b>%s</div>' % ''.join('<span class="w">%s</span>' % html.escape(w) for w in words)


def audio_player(src, max_plays=0):
    mp = ' Số lần nghe tối đa: %d.' % max_plays if max_plays else ''
    return ('<div class="audio"><audio id="audio" controls preload="metadata" src="%s"></audio>'
            '<div class="plays" id="plays">Đã nghe: 0%s lần.%s</div></div>' % (esc_attr(src), ('/%d' % max_plays) if max_plays else '', mp))


def qgroup_open(g):
    s = '<section class="card group" id="g-%s">' % esc_attr(g['id'])
    if g.get('instr'):
        s += '<div class="instr">%s</div>' % html.escape(g['instr'])
    return s


def qgroup_close():
    return '</section>'


def render_item(it, num, test_mode, imgbase):
    t = it['t']
    body = ''
    if it.get('img'):
        body += '<img class="pic" src="%s/%s" alt="Hình minh hoạ câu %s">' % (imgbase, it['img'], num)
    if t == 'mcq':
        if it.get('q'):
            body += '<div class="stem">%s</div>' % it['q']
        body += radio_item(it)
    elif t in ('tf', 'tfng'):
        body += '<div class="stem">%s</div>' % it['q'] + tf_item(it)
    elif t == 'fill':
        body += text_item(it, test_mode)
    elif t == 'open':
        body += '<div class="stem">%s</div>' % it['q'] + open_item(it, test_mode)
    return ('<div class="q" data-id="%s" data-t="%s"><div class="qn">%s</div><div class="qb">%s<div class="exp" data-for="%s" hidden></div></div></div>'
            % (esc_attr(it['id']), t, num, body, esc_attr(it['id'])))


# ------------------------------------------------------------------ ghép trang
def nav_tabs(S, cur_id, slug):
    items = [('ly-thuyet', 'Lý thuyết')] + [(p['id'], p['title']) for p in S['pages']]
    return '<nav class="tabs">%s<a href="../../../../index.html">⌂ Trang chủ</a></nav>' % ''.join(
        '<a href="%s.html"%s>%s</a>' % (i, ' class="cur"' if i == cur_id else '', html.escape(t)) for i, t in items)


def json_script(obj):
    return json.dumps(obj, ensure_ascii=False).replace('</', '<\\/')


def page_shell(title, sub, body, extra_head='', badge='', h1=None):
    return ('<!doctype html>\n<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><link rel="stylesheet" href="../../../../engine/engine.css">%s</head><body>'
            '<header class="top"><div class="wrap">%s<h1>%s</h1><div class="sub">%s</div>%%NAV%%</div></header>%s</body></html>'
            % (html.escape(title), extra_head, badge, html.escape(h1 or title), html.escape(sub), body))


def build_theory_page(S, slug):
    body = '<div class="wrap"><div class="card theory">%s</div></div>' % S['theory']
    s = page_shell('Lý thuyết – ' + S['title'], 'Từ vựng, phát âm, ngữ pháp trọng tâm của Unit', body, badge='<span class="badge">Lý thuyết</span>', h1='Lý thuyết')
    return s.replace('%NAV%', nav_tabs(S, 'ly-thuyet', slug))


def build_quiz_page(S, P, ANS, EXP, slug, imgbase, audio_src):
    test_mode = P['mode'] == 'test'
    order, items_meta = [], {}
    body = ['<div class="wrap">']
    if P.get('pending'):
        body.append('<div class="pending"><b>Lưu ý:</b> Phần này đang chờ cập nhật transcript và đáp án. Bạn có thể xem câu hỏi, nhưng chưa tính điểm.</div>')
    if test_mode:
        body.append('<div class="card rules"><b>📋 Quy định làm bài</b><ul><li>Thời gian: <b>%d phút</b>. Còn 10 phút hệ thống nhắc; hết giờ có thêm 5 phút gia hạn rồi tự động nộp.</li><li>Bài làm ở chế độ <b>toàn màn hình</b>. Chuyển tab, mất focus, thoát toàn màn hình đều bị ghi nhận và báo cho giáo viên.</li><li>Không dùng chuột phải, sao chép/dán, phím tắt. Đáp án và giải thích chi tiết hiển thị sau khi nộp bài.</li></ul></div>' % P['minutes'])
    body.append('<div class="result" id="result" hidden></div>')
    if P.get('audio'):
        body.append(audio_player(audio_src, P.get('audio_max_plays', 0)))
    for g in P['groups']:
        body.append(qgroup_open(g))
        if g.get('note'):
            body.append('<div class="theory">%s</div>' % g['note'])
        if g.get('passage'):
            body.append('<div class="passage">%s</div>' % g['passage'])
        if g.get('bank'):
            body.append(bank_box(g['bank']))
        for idx, it in enumerate(g['items'], 1):
            if g['id'] in LONG_GROUPS and it['t'] == 'fill':
                it['long'] = True
            num = int(it['id'].split('.')[-1]) if test_mode else idx
            body.append(render_item(it, num, test_mode, imgbase))
            order.append(it['id'])
            items_meta[it['id']] = {'t': it['t'], 'g': g['id']}
        body.append(qgroup_close())
    body.append('</div>')
    # thanh dưới
    bar = ('<div class="bar"><div class="prog"><i id="progBar"></i></div><div class="in">%s<span class="stat grow" id="stat"></span>%s%s</div></div>'
           % ('<span class="timer" id="timer">--:--</span>' if test_mode else '',
              '' if P.get('pending') else '<button class="btn ghost" id="reset" type="button">Làm lại</button>',
              '' if P.get('pending') else '<button class="btn" id="submit" type="button">%s</button>' % ('Nộp bài' if test_mode else 'Nộp kết quả')))
    modal = ('<div class="modal" id="startModal"><div class="box"><h3>%s</h3><p>Nhập thông tin để hệ thống ghi nhận kết quả.</p>'
             '<label>Họ và tên<input type="text" id="stName" autocomplete="name"></label>'
             '<label>Lớp<input type="text" id="stClass"></label><div id="stErr" style="color:var(--bad)"></div>'
             '<button class="btn" id="startBtn" type="button">%s</button> %s</div></div>'
             % ('Bắt đầu làm bài kiểm tra' if test_mode else 'Bắt đầu luyện tập', 'Bắt đầu làm bài' if test_mode else 'Bắt đầu',
                '' if test_mode else '<button class="btn ghost" id="skipBtn" type="button">Luyện tập không ghi tên</button>'))
    warn = '<div class="modal" id="warnModal" hidden><div class="box"><h3>Nhắc giờ</h3><p id="warnText"></p><button class="btn" id="warnOk" type="button">Đã hiểu</button></div></div><div class="toast" id="toast" hidden></div>'
    if test_mode:
        warn += ('<div class="modal" id="timeUpModal" hidden><div class="box"><h3>⏰ Đã hết giờ làm bài</h3><p>Bạn có thêm <b>5 phút</b> để hoàn tất. Hết 5 phút bài sẽ tự động nộp.</p>'
                 '<button class="btn" id="timeUpSubmit" type="button">Nộp bài ngay</button> <button class="btn ghost" id="timeUpBack" type="button">Làm tiếp</button></div></div>'
                 '<div class="modal fsov" id="fsOverlay" hidden><div class="box"><h3>⚠ Bạn đã thoát toàn màn hình</h3><p>Hành vi này đã được ghi nhận. Hãy quay lại chế độ toàn màn hình để tiếp tục làm bài.</p>'
                 '<button class="btn" id="fsBack" type="button">Vào toàn màn hình</button></div></div>')
    cfg = {'setId': S['id'], 'pageId': P['id'], 'mode': P['mode'], 'minutes': P.get('minutes', 0), 'warnAt': P.get('warn_at', 10 if test_mode else 0),
           'url': APPS_SCRIPT_URL, 'audioMaxPlays': P.get('audio_max_plays', 0), 'lockSeek': bool(P.get('lock_seek')),
           'order': order, 'items': items_meta,
           'ANS': {i: ANS[i] for i in order if i in ANS}, 'EXP': {i: EXP[i] for i in order if i in EXP}}
    scripts = '<script>window.QUIZ=%s;</script><script src="../../../../engine/engine.js"></script><script src="../../../../engine/tools.js"></script>' % json_script(cfg)
    badge = '<span class="badge%s">%s</span>' % (' test' if test_mode else '', 'Kiểm tra' if test_mode else 'Luyện tập')
    sub = '%s  ·  %d câu' % (S['title'], len(order))
    s = page_shell(P['title'] + ' – ' + S['title'], sub, ''.join(body) + bar + modal + warn + scripts, badge=badge, h1=P['title'])
    return s.replace('%NAV%', nav_tabs(S, P['id'], slug))


def build_set(entry):
    sid, data_p, ans_p, gdir, udir, slug, imgdir, audio = entry
    S = load_py(data_p, 'SET')
    ANS, EXP = load_answers(ans_p)
    d = os.path.join(OUT, gdir, udir, slug)
    os.makedirs(d, exist_ok=True)
    imgbase = '../../../../' + imgdir
    audio_src = '../../../../' + audio
    pages = []
    with open(os.path.join(d, 'ly-thuyet.html'), 'w', encoding='utf8') as f:
        f.write(build_theory_page(S, slug))
    for P in S['pages']:
        with open(os.path.join(d, P['id'] + '.html'), 'w', encoding='utf8') as f:
            f.write(build_quiz_page(S, P, ANS, EXP, slug, imgbase, audio_src))
        pages.append((P['id'], P['title'], P['mode'], sum(len(g['items']) for g in P['groups'])))
    return S, pages


def build_index(done):
    out = ['<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
           '<title>Bài luyện tập & đề kiểm tra</title><link rel="stylesheet" href="engine/engine.css"></head><body>'
           '<header class="hero"><div class="wrap"><div class="hero-in"><div class="hero-tag">GNOMIO · Lớp 6 – 12</div><h1>Luyện tập thông minh,<br>kiểm tra tự tin</h1>'
           '<p>Bài tập tự luyện có giải thích từng câu · Đề kiểm tra có đồng hồ & chống gian lận</p></div></div></header>'
           '<div class="wrap index">']
    for entry, S, pages in done:
        gdir, udir, slug = entry[3], entry[4], entry[5]
        out.append('<section class="card setcard"><div class="settitle"><span class="chip">Lớp %s · %s</span><h3>%s</h3></div><div class="tiles">' % (gdir[3:], udir.replace('Unit', 'Unit '), html.escape(S['title'])))
        out.append('<a class="tile t-theory" href="WebBaiTap/%s/%s/%s/ly-thuyet.html"><span class="ic">📘</span><b>Lý thuyết</b><small>Từ vựng · ngữ pháp</small></a>' % (gdir, udir, slug))
        icons = {'phat-am': '🔊', 'tu-vung': '🔤', 'tu-vung-ngu-phap': '🔤', 'ngu-phap': '🧩', 'nghe': '🎧', 'noi': '🗣️', 'doc': '📖', 'viet': '✍️', 'kiem-tra': '📝'}
        for pid, title, mode, n in pages:
            out.append('<a class="tile %s" href="WebBaiTap/%s/%s/%s/%s.html"><span class="ic">%s</span><b>%s</b><small>%d câu%s</small></a>'
                       % ('t-test' if mode == 'test' else 't-prac', gdir, udir, slug, pid, icons.get(pid, '✏️'), html.escape(title), n, ' · có tính giờ' if mode == 'test' else ''))
        out.append('</div></section>')
    out.append('<footer class="foot">Học sinh làm bài trên điện thoại hoặc máy tính · Kết quả ghi tự động về giáo viên</footer></div></body></html>')
    open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf8').write(''.join(out))


if __name__ == '__main__':
    want = sys.argv[1:]
    done = []
    for e in REGISTRY:
        if want and e[0] not in want:
            continue
        S, pages = build_set(e)
        done.append((e, S, pages))
        print(e[0], '->', len(pages), 'trang,', sum(p[3] for p in pages), 'câu')
    if not want:
        build_index(done)
