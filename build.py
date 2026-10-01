# -*- coding: utf-8 -*-
"""Lớp BUILD: các hàm renderer + ghép trang HTML từ dữ liệu (units/*.py) và đáp án (units/*_dapan.py).
Chạy:  python3 build.py            (sinh toàn bộ WebBaiTap/ + index.html)
       python3 build.py lop11-u1-botro   (chỉ 1 bộ)
"""
import os, sys, json, re, html, importlib.util

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'WebBaiTap')
APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbyZ4UJgI763vPb4TZhKbKgxl6p-lGCQCJnZDqgCL9mHCVQpUzb4sbJGg89GLWSI-sQj/exec'   # update_links.py sẽ thay giá trị này
PAGES_URL = 'https://tientran-tbec.github.io/GRADE-1-12-IELTS/'

# (id bộ, file dữ liệu, file đáp án, thư mục lớp, thư mục unit, slug thư mục, ảnh)
REGISTRY = [
    ('lop11-u1-botro', 'units/lop11_u1_botro.py', 'units/lop11_u1_botro_dapan.py', 'Lop11', 'Unit1', 'botro', 'assets/lop11_u1/botro', 'audio/lop11_u1_botro_nghe.mp3'),
    ('lop11-u1-4kn', 'units/lop11_u1_4kn.py', 'units/lop11_u1_4kn_dapan.py', 'Lop11', 'Unit1', '4kn', 'assets/lop11_u1/4kn', 'audio/lop11_u1_4kn_nghe.mp3'),
    ('lop11-u2-botro', 'units/lop11_u2_botro.py', 'units/lop11_u2_botro_dapan.py', 'Lop11', 'Unit2', 'botro', 'assets/lop11_u2/botro', 'audio/lop11_u2_botro_nghe.mp3'),
    ('lop11-u2-4kn', 'units/lop11_u2_4kn.py', 'units/lop11_u2_4kn_dapan.py', 'Lop11', 'Unit2', '4kn', 'assets/lop11_u2/4kn', 'audio/lop11_u2_4kn_nghe.mp3'),
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
        L = 'ABCDEFGHIJ'[i]
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


LONG_GROUPS = {'vg8', 'kt-rw', 'wr1', 'wr2', 'vg9', 'vg10', 'vg11', 'kt-cue'}   # nhóm viết lại câu: dùng ô nhiều dòng, kéo giãn được


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


INDEX_CSS = """
:root{--bg:#f5f4ff;--card:#fff;--ink:#1f2140;--mut:#6b6f8d;--line:#e6e4f7;--pri:#6c4cf5;--pri2:#ff5fa2;--test:#e8590c;--sb:#ffffff}
@media(prefers-color-scheme:dark){:root{--bg:#14152a;--card:#1d1f3a;--ink:#eceefb;--mut:#a3a7c9;--line:#2c2f55;--sb:#191b34}}
[hidden]{display:none!important}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.top{position:sticky;top:0;z-index:30;background:linear-gradient(90deg,var(--pri),var(--pri2));color:#fff;display:flex;align-items:center;gap:12px;padding:10px 16px}
.top h1{font-size:17px;margin:0;flex:1}.top button{background:rgba(255,255,255,.2);border:0;color:#fff;border-radius:10px;padding:8px 12px;font-size:15px;cursor:pointer}
.menu{display:none}
.layout{display:grid;grid-template-columns:270px 1fr;min-height:calc(100vh - 52px)}
.sb{background:var(--sb);border-right:1px solid var(--line);padding:18px 16px;position:sticky;top:52px;height:calc(100vh - 52px);overflow:auto}
.sb h4{margin:18px 0 8px;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--mut)}.sb h4:first-child{margin-top:0}
.sb input[type=search]{width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--ink);font-size:15px}
.fl{display:flex;flex-direction:column;gap:4px}
.f{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:9px 12px;border-radius:10px;border:0;background:none;color:var(--ink);font-size:15px;text-align:left;cursor:pointer}
.f:hover{background:var(--bg)}.f.on{background:linear-gradient(90deg,var(--pri),var(--pri2));color:#fff;font-weight:600}
.f small{opacity:.75;font-size:12px}.f[disabled]{opacity:.4;cursor:not-allowed}
.seg{display:flex;gap:6px;flex-wrap:wrap}.seg .f{border:1px solid var(--line);padding:7px 11px;flex:1;justify-content:center}.seg .f.on{border-color:transparent}
.reset{margin-top:18px;width:100%;padding:9px;border:1px dashed var(--line);border-radius:10px;background:none;color:var(--mut);cursor:pointer}
main{padding:22px 24px 60px;max-width:1100px;width:100%}
.bar{display:flex;align-items:baseline;gap:12px;margin-bottom:14px;flex-wrap:wrap}.bar h2{margin:0;font-size:22px}.bar span{color:var(--mut)}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:16px 18px;margin-bottom:16px;box-shadow:0 2px 10px rgba(80,60,200,.05)}
.settitle{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:12px}.settitle h3{margin:0;font-size:17px}
.chip{background:var(--bg);color:var(--pri);border:1px solid var(--line);border-radius:999px;padding:3px 10px;font-size:12px;font-weight:600}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.tile{display:flex;flex-direction:column;gap:2px;padding:12px;border-radius:14px;border:1px solid var(--line);text-decoration:none;color:var(--ink);background:var(--bg);transition:.15s}
.tile:hover{transform:translateY(-2px);border-color:var(--pri);box-shadow:0 6px 16px rgba(108,76,245,.18)}
.tile .ic{font-size:22px}.tile b{font-size:14.5px}.tile small{color:var(--mut);font-size:12px}
.tile.t-test{background:rgba(232,89,12,.08);border-color:rgba(232,89,12,.35)}.tile.t-test b{color:var(--test)}
.empty{text-align:center;padding:50px 10px;color:var(--mut)}
.foot{text-align:center;color:var(--mut);font-size:13px;margin-top:30px}
.scrim{display:none}
@media(max-width:820px){
 .menu{display:inline-block}.layout{grid-template-columns:1fr}
 .sb{position:fixed;left:0;top:52px;bottom:0;width:290px;max-width:86vw;height:auto;z-index:40;transform:translateX(-102%);transition:.2s;box-shadow:4px 0 20px rgba(0,0,0,.25)}
 body.open .sb{transform:none}body.open .scrim{display:block;position:fixed;inset:52px 0 0 0;background:rgba(0,0,0,.4);z-index:35}
 main{padding:16px 16px 50px}.tiles{grid-template-columns:repeat(2,1fr)}
}
"""

INDEX_JS = """
(function(){
var st={g:'',u:'',k:'',m:'',q:''};
try{var sv=JSON.parse(localStorage.getItem('gn_idx')||'{}');for(var k in st)if(sv[k]!==undefined)st[k]=sv[k]}catch(e){}
var cards=[].slice.call(document.querySelectorAll('.setcard'));
function save(){try{localStorage.setItem('gn_idx',JSON.stringify(st))}catch(e){}}
function norm(s){return (s||'').toLowerCase()}
function apply(){
  var shown=0;
  cards.forEach(function(c){
    var ok=(!st.g||c.dataset.g===st.g)&&(!st.u||c.dataset.u===st.u)&&(!st.k||c.dataset.k===st.k)&&(!st.q||norm(c.textContent).indexOf(norm(st.q))>=0);
    c.hidden=!ok;
    [].forEach.call(c.querySelectorAll('.tile'),function(t){
      var tm=t.dataset.m||'';t.hidden=!!(st.m&&tm!==st.m);
    });
    if(ok&&st.m&&!c.querySelector('.tile:not([hidden])'))c.hidden=true;
    if(!c.hidden)shown++;
  });
  document.getElementById('empty').hidden=shown>0;
  document.getElementById('cnt').textContent=shown+' bộ bài';
  [].forEach.call(document.querySelectorAll('.f[data-f]'),function(b){b.classList.toggle('on',(st[b.dataset.f]||'')===b.dataset.v)});
  var t=[];if(st.g)t.push('Lớp '+st.g);if(st.u)t.push('Unit '+st.u);
  document.getElementById('ttl').textContent=t.length?t.join(' · '):'Tất cả bài học';
  save();
}
document.addEventListener('click',function(e){
  var b=e.target.closest&&e.target.closest('.f[data-f]');
  if(b&&!b.disabled){st[b.dataset.f]=b.dataset.v;if(b.dataset.f==='g'){st.u=''}apply();if(window.innerWidth<=820)document.body.classList.remove('open');return}
  if(e.target.id==='reset'){st={g:'',u:'',k:'',m:'',q:''};document.getElementById('q').value='';apply()}
  if(e.target.closest&&(e.target.closest('.menu')||e.target.classList.contains('scrim')))document.body.classList.toggle('open');
  if(b&&window.innerWidth<=820)document.body.classList.remove('open');
});
document.getElementById('q').addEventListener('input',function(e){st.q=e.target.value;apply()});
document.getElementById('q').value=st.q||'';
apply();
})();
"""


def build_index(done):
    grades = sorted({e[3][3:] for e, _, _ in done}, key=int)
    units = sorted({(e[3][3:], e[4][4:]) for e, _, _ in done}, key=lambda x: (int(x[0]), int(x[1])))
    def cnt(fn):
        return sum(1 for e, _, _ in done if fn(e))
    o = ['<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
         '<title>Bài luyện tập & đề kiểm tra</title><style>%s</style></head><body>' % INDEX_CSS,
         '<div class="top"><button class="menu" aria-label="Mở bộ lọc">☰ Bộ lọc</button><h1>GNOMIO · Lớp 1–12</h1></div>',
         '<div class="layout"><aside class="sb">',
         '<h4>Tìm kiếm</h4><input id="q" type="search" placeholder="Tên unit, kỹ năng…">',
         '<h4>Lớp</h4><div class="fl"><button class="f" data-f="g" data-v="">Tất cả lớp</button>']
    for g in range(1, 13):
        n = cnt(lambda e, g=g: e[3][3:] == str(g))
        if n:
            o.append('<button class="f" data-f="g" data-v="%d">Lớp %d <small>%d bộ</small></button>' % (g, g, n))
        else:
            o.append('<button class="f" disabled>Lớp %d <small>sắp có</small></button>' % g)
    o.append('</div><h4>Unit</h4><div class="fl"><button class="f" data-f="u" data-v="">Tất cả unit</button>')
    for g, u in units:
        o.append('<button class="f" data-f="u" data-v="%s">Lớp %s · Unit %s</button>' % (u, g, u))
    o.append('</div><h4>Loại bài tập</h4><div class="seg"><button class="f" data-f="k" data-v="">Tất cả</button>'
             '<button class="f" data-f="k" data-v="botro">Bổ trợ</button><button class="f" data-f="k" data-v="4kn">4 kỹ năng</button></div>'
             '<h4>Hình thức</h4><div class="seg"><button class="f" data-f="m" data-v="">Tất cả</button>'
             '<button class="f" data-f="m" data-v="prac">Luyện tập</button><button class="f" data-f="m" data-v="test">Kiểm tra</button></div>'
             '<button class="reset" id="reset">↺ Xoá bộ lọc</button></aside><div class="scrim"></div><main>'
             '<div class="bar"><h2 id="ttl">Tất cả bài học</h2><span id="cnt"></span></div>')
    icons = {'phat-am': '🔊', 'tu-vung': '🔤', 'tu-vung-ngu-phap': '🔤', 'ngu-phap': '🧩', 'nghe': '🎧', 'noi': '🗣️', 'doc': '📖', 'viet': '✍️', 'kiem-tra': '📝'}
    for entry, S, pages in done:
        gdir, udir, slug = entry[3], entry[4], entry[5]
        g, u = gdir[3:], udir[4:]
        o.append('<section class="card setcard" data-g="%s" data-u="%s" data-k="%s"><div class="settitle"><span class="chip">Lớp %s · Unit %s</span><h3>%s</h3></div><div class="tiles">'
                 % (g, u, slug, g, u, html.escape(S['title'])))
        o.append('<a class="tile" data-m="prac" href="WebBaiTap/%s/%s/%s/ly-thuyet.html"><span class="ic">📘</span><b>Lý thuyết</b><small>Từ vựng · ngữ pháp</small></a>' % (gdir, udir, slug))
        for pid, title, mode, n in pages:
            o.append('<a class="tile %s" data-m="%s" href="WebBaiTap/%s/%s/%s/%s.html"><span class="ic">%s</span><b>%s</b><small>%d câu%s</small></a>'
                     % ('t-test' if mode == 'test' else '', 'test' if mode == 'test' else 'prac', gdir, udir, slug, pid, icons.get(pid, '✏️'), html.escape(title), n, ' · có tính giờ' if mode == 'test' else ''))
        o.append('</div></section>')
    o.append('<div class="empty" id="empty" hidden>Không có bộ bài phù hợp. Hãy bấm “Xoá bộ lọc”.</div>'
             '<div class="foot">Học sinh làm bài trên điện thoại hoặc máy tính · Kết quả ghi tự động về giáo viên</div></main></div>'
             '<script>%s</script></body></html>' % INDEX_JS)
    open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf8').write(''.join(o))


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
