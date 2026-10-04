# -*- coding: utf-8 -*-
"""Chế độ Thử thách trên trình duyệt: bản đồ lộ trình, khoá trang, khoá tab, đồng hồ lý thuyết, báo kết quả sau nộp, chuyển hướng."""
import os, subprocess, time, json, re, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT, WEB = 8801, 8802
srv = subprocess.Popen(['node', os.path.join(ROOT, 'tests/tt_server.js'), str(PORT)], stdout=subprocess.PIPE); srv.stdout.readline()
web = subprocess.Popen(['python3', '-m', 'http.server', str(WEB), '--bind', '127.0.0.1'], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
res = []
def chk(n, ok): res.append(bool(ok)); print('OK  ' if ok else 'FAIL', n)
def api(d):
    r = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=json.dumps(d).encode(), method='POST'); return json.loads(urllib.request.urlopen(r).read())
def route(r):
    req = r.request
    if req.method == 'OPTIONS': r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'}); return
    rq = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=req.post_data.encode() if req.post_data else None, method=req.method)
    r.fulfill(status=200, body=urllib.request.urlopen(rq).read(), headers={'access-control-allow-origin': '*', 'content-type': 'text/plain'})
U = lambda p: 'http://127.0.0.1:%d/%s' % (WEB, p)
P = json.load(open(os.path.join(ROOT, 'thuthach/lop3.json'), encoding='utf8')); steps = [s for c in P['chapters'] for s in c['steps']]
SETS = list(json.load(open(os.path.join(ROOT, 'thuthach/index.json'), encoding='utf8'))['paths'])
FILL = """() => { const Q = window.QUIZ; Q.order.forEach(id => { const q = document.querySelector('.q[data-id="'+id+'"]'); if(!q) return; const a = Q.ANS[id];
  const rad = q.querySelectorAll('input[type=radio]'); if (rad.length) { const v = Array.isArray(a) ? a[0] : a; const r = [...rad].find(x => x.value === v); if (r) r.click(); return; }
  const bl = q.querySelectorAll('.blank'); const arr = (a && a.blanks) ? a.blanks.map(x => Array.isArray(x) ? x[0] : x) : [Array.isArray(a) ? a[0] : a];
  bl.forEach((b, i) => { b.value = arr[i] !== undefined ? arr[i] : arr[0]; b.dispatchEvent(new Event('input', {bubbles:true})); b.dispatchEvent(new Event('change', {bubbles:true})); }); }); }"""
try:
    A = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'})['token']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': '3A', 'name': '3A', 'grade': 3}})
    hs = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Em Bé Ba', 'classes': ['3A'], 'password': 'hs1234'}})['user']['username']
    hs2 = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Bạn Bốn', 'classes': ['3A'], 'password': 'hs1234'}})['user']['username']
    api({'action': 'adm_assign_save', 'token': A, 'cls': '3A', 'sets': SETS})
    api({'action': 'tt_mode_set', 'token': A, 'scope': 'cls', 'key': '3A', 'mode': 'thuthach'})
    api({'action': 'tt_cfg_set', 'token': A, 'path': 'lop3', 'cfg': {'theory_min': 0.1, 'practice_pass': 80, 'test_pass': 75}})
    with sync_playwright() as pw:
        br = pw.chromium.launch(); c = br.new_context(viewport={'width': 1300, 'height': 900}); c.route('**/script.google.com/**', route)
        p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e))); p.on('dialog', lambda d: d.accept())
        p.goto(U('login.html')); p.fill('#u', hs); p.fill('#p', 'hs1234'); p.click('#b1'); p.wait_for_selector('#np'); p.fill('#op', 'hs1234'); p.fill('#np', 'matkhau5'); p.fill('#np2', 'matkhau5'); p.click('#b2'); time.sleep(2)
        # --- bản đồ
        p.goto(U('thuthach.html')); p.wait_for_selector('.nd', timeout=15000); time.sleep(0.8)
        chk('bản đồ vẽ đủ %d bước' % len(steps), p.locator('.nd').count() == len(steps))
        chk('chỉ bước đầu là "current", còn lại khoá', p.locator('.nd.current').count() == 1 and p.locator('.nd.locked').count() == len(steps) - 1)
        chk('bước đầu là lý thuyết (📘)', 'Lý thuyết' in p.inner_text('.nd.current'))
        chk('cột % bên phải: 0%', '0%' in p.inner_text('.ring'))
        p.locator('.nd.locked >> nth=0').click(); time.sleep(0.3)
        chk('bấm bước khoá: báo 🔒', p.locator('.tt-toast').count() == 1 and p.url.endswith('thuthach.html'))
        # --- vào thẳng trang bước khoá -> bị đưa về lộ trình
        tv = steps[1]['url']; p.goto(U(tv)); p.wait_for_url(re.compile('thuthach.html\\?locked='), timeout=15000)
        chk('mở thẳng trang bị khoá → về lộ trình + cảnh báo', 'chưa mở' in p.inner_text('.ttbanner'))
        # --- lý thuyết
        p.locator('.nd.current').click(); p.wait_for_selector('.tt-bar', timeout=15000)
        chk('trang lý thuyết có đồng hồ đọc bài', 'Đọc bài' in p.inner_text('.tt-bar') and p.locator('.tt-hud').count() == 1)
        chk('thanh tab: các trang sau bị 🔒', p.locator('nav.tabs a.tt-lock').count() >= 5)
        p.wait_for_selector('.tt-bar .tt-btn', timeout=25000)
        chk('đọc đủ giờ → hiện nút làm tiếp', 'Hoàn thành' in p.inner_text('.tt-bar'))
        p.click('.tt-bar .tt-btn'); p.wait_for_selector('.q', timeout=15000); time.sleep(0.8)
        chk('sang bước 2 (mở khoá)', steps[1]['pid'] in p.url)
        chk('tab trang sau vẫn khoá, tab Lý thuyết ✓', p.locator('nav.tabs a.tt-lock').count() >= 4 and p.locator('nav.tabs a.tt-done').count() >= 1)
        # --- nộp bài trắng: chưa đạt
        p.click('#submit'); p.wait_for_selector('.tt-res.fail', timeout=15000)
        chk('nộp trắng: báo chưa đạt ≥80%', '80%' in p.inner_text('.tt-res.fail >> nth=0') and p.locator('.tt-res [data-tt=again]').count() >= 1)
        st = api({'action': 'auth_login', 'username': hs, 'password': 'matkhau5', 'device': 'zz'})
        # --- làm đúng
        p.reload(); p.wait_for_selector('.q'); time.sleep(0.8); p.evaluate(FILL); time.sleep(0.4); p.click('#submit'); p.wait_for_selector('.tt-res.pass', timeout=20000)
        txt = p.inner_text('.tt-res.pass >> nth=0'); chk('làm đúng: báo qua bài + sao', 'Tuyệt vời' in txt and '⭐' in txt)
        chk('báo bước tiếp theo đã mở', steps[2]['title'] in txt)
        p.locator('#resultBox .tt-res.pass .tt-btn >> nth=0').click(); p.wait_for_selector('.q', timeout=15000)
        chk('"Làm tiếp" dẫn sang bước 3', steps[2]['pid'] in p.url)
        # --- bản đồ sau khi tiến bộ
        p.goto(U('thuthach.html')); p.wait_for_selector('.nd'); time.sleep(0.8)
        chk('bản đồ: 2 bước xong', p.locator('.nd.done').count() == 2 and p.locator('.nd.current').count() == 1)
        pc = int(re.search(r'(\d+)%', p.inner_text('.ring')).group(1)); chk('cột %% = %d%% (2 trên %d bước)' % (pc, len(steps)), pc == round(200 / len(steps)))
        chk('có huy hiệu & nhiệm vụ tiếp theo', p.locator('.bd').count() >= 6 and 'Nhiệm vụ tiếp theo' in p.inner_text('#side'))
        chk('bảng các bạn trong lớp', p.locator('#boardBox:not([hidden])').count() == 1 and p.locator('.board tr.me').count() == 1)
        # --- trang gốc luyện tập của bước đã xong vẫn mở được
        p.goto(U(steps[1]['url'])); p.wait_for_selector('.q'); time.sleep(0.8)
        chk('bước đã xong mở lại được, có nhãn Đã qua', p.locator('.tt-chip').count() == 1)
        # --- học sinh Tự do không bị ảnh hưởng
        api({'action': 'tt_mode_set', 'token': A, 'scope': 'user', 'key': hs2, 'mode': 'tudo'})
        c2 = br.new_context(viewport={'width': 1300, 'height': 900}); c2.route('**/script.google.com/**', route); q = c2.new_page(); q.on('pageerror', lambda e: errs.append(str(e)))
        q.goto(U('login.html')); q.fill('#u', hs2); q.fill('#p', 'hs1234'); q.click('#b1'); q.wait_for_selector('#np'); q.fill('#op', 'hs1234'); q.fill('#np', 'matkhau5'); q.fill('#np2', 'matkhau5'); q.click('#b2'); time.sleep(2)
        q.goto(U(steps[7]['url'])); q.wait_for_selector('#startBtn, .q', timeout=15000); time.sleep(1)
        chk('học sinh chế độ Tự do mở thẳng bước xa được, không có thanh lộ trình', q.locator('.tt-hud').count() == 0 and 'thuthach' not in q.url)
        chk('không lỗi JS', not errs)
        if errs: print(errs[:4])
        br.close()
finally:
    srv.terminate(); web.terminate()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI: %d/%d' % (res.count(False), len(res)))
raise SystemExit(0 if all(res) else 1)
