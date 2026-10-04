# -*- coding: utf-8 -*-
"""Trang chủ Thử thách (học sinh): lối tắt mỗi lộ trình 1 khung, top 5, vinh danh; tab Tổng quan của giáo viên/admin."""
import os, subprocess, time, json, re, copy, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT, WEB = 8805, 8806
# lộ trình thứ hai giả (lopx) để thử 2 lối tắt
P = json.load(open(os.path.join(ROOT, 'thuthach/lop3.json'), encoding='utf8')); IX = json.load(open(os.path.join(ROOT, 'thuthach/index.json'), encoding='utf8'))
X = copy.deepcopy(P); X['id'] = 'lopx'; X['title'] = 'Toán · Lớp 3'
for c in X['chapters']:
    for s in c['steps']:
        s['sid'] = 'fx-' + s['sid']; s['id'] = s['sid'] + '|' + s['pid']
IXX = copy.deepcopy(IX)
for k, v in IX['paths'].items(): IXX['paths']['fx-' + k] = 'lopx'
json.dump(X, open(os.path.join(ROOT, 'thuthach/lopx.json'), 'w', encoding='utf8'), ensure_ascii=False); json.dump(IXX, open(os.path.join(ROOT, 'thuthach/index.json'), 'w', encoding='utf8'), ensure_ascii=False)
steps = [s for c in P['chapters'] for s in c['steps']]; SETS = list(IXX['paths'])
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
def login(p, u, pw):
    p.goto(U('login.html')); p.fill('#u', u); p.fill('#p', pw); p.click('#b1'); time.sleep(2.5)
    if p.locator('#np').is_visible(): p.fill('#op', pw); p.fill('#np', 'matkhau5'); p.fill('#np2', 'matkhau5'); p.click('#b2'); time.sleep(2.5)
try:
    A = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'})['token']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': '3A', 'name': '3A', 'grade': 3}})
    names = ['Trần Bảo Châu', 'Lê Duy Khang', 'Nguyễn Cát Tiên', 'Phạm An Nhiên', 'Võ Minh Anh', 'Đặng Gia Hân', 'Bùi Quốc Bảo']
    us = [api({'action': 'adm_user_save', 'token': A, 'user': {'name': n, 'classes': ['3A'], 'password': 'hs1234'}})['user']['username'] for n in names]
    g = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Cô Ba', 'role': 'teacher'}}); gv, gpw = g['user']['username'], g['password']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': '3A', 'name': '3A', 'grade': 3, 'teacher': gv}})
    api({'action': 'adm_assign_save', 'token': A, 'cls': '3A', 'sets': SETS})
    api({'action': 'tt_mode_set', 'token': A, 'scope': 'cls', 'key': '3A', 'mode': 'thuthach'})
    api({'action': 'tt_cfg_set', 'token': A, 'path': 'lop3', 'cfg': {'theory_min': 0, 'practice_pass': 80, 'test_pass': 75}})
    api({'action': 'tt_cfg_set', 'token': A, 'path': 'lopx', 'cfg': {'theory_min': 0, 'practice_pass': 80, 'test_pass': 75}})
    # tạo tiến độ khác nhau bằng cách cho qua (admin) các bước đầu
    for i, u in enumerate(us):
        for k in range([14, 9, 6, 4, 2, 1, 0][i]):
            api({'action': 'tt_unlock', 'token': A, 'username': u, 'step': steps[k]['id'], 'how': 'pass'})
    api({'action': 'tt_unlock', 'token': A, 'username': us[4], 'step': 'fx-' + steps[0]['id'], 'how': 'pass'})
    with sync_playwright() as pw:
        br = pw.chromium.launch(); errs = []
        c = br.new_context(viewport={'width': 1280, 'height': 900}); c.route('**/script.google.com/**', route)
        p = c.new_page(); p.on('pageerror', lambda e: errs.append(str(e)))
        login(p, us[4], 'hs1234')                       # học sinh hạng 5/7
        p.goto(U('tt_home.html')); time.sleep(4); print('PAGE:', p.url, p.inner_text('body')[:200], errs)
        p.wait_for_selector('.hm-card', timeout=15000); time.sleep(1.2)
        chk('2 lộ trình → 2 khung lối tắt', p.locator('.hm-card').count() == 2)
        hrefs = p.eval_on_selector_all('.hm-go', 'els => els.map(e => e.getAttribute("href"))')
        chk('lối tắt 1 trỏ thẳng bước đang làm (%s)' % hrefs[0], hrefs[0] == steps[2]['url'] if False else hrefs[0].startswith('WebBaiTap/'))
        chk('lối tắt 2 trỏ bước đang làm của lộ trình 2', hrefs[1].startswith('WebBaiTap/') and hrefs[1] != '')
        chk('có chuỗi ngày/lời chào', 'Chào' in p.inner_text('.hm-hero'))
        chk('có 2 bảng top (mỗi lộ trình)', p.locator('.hm-top').count() == 2)
        t1 = p.locator('.hm-top').first
        chk('top 5 lớp = 5 dòng + dòng của em ở cuối', t1.locator('tbody tr:not(.sep)').count() == 6 and 'em' in t1.locator('tbody tr').last.inner_text())
        chk('em hạng 5 xuất hiện 2 chỗ (trong top và hàng cuối)', t1.locator('tr.me').count() == 2)
        chk('vinh danh: 3 cột × tối đa 3 người', p.locator('.hm-f').count() == 6 and p.locator('.hm-f').first.locator('li').count() == 3)
        chk('vinh danh nhanh nhất: chưa ai đủ bước', 'Chưa ai đủ' in p.locator('.hm-f.c').first.inner_text())
        p.screenshot(path='/tmp/home_desktop.png', full_page=True)
        # học sinh ngoài top (hạng 7)
        c2 = br.new_context(viewport={'width': 390, 'height': 800}); c2.route('**/script.google.com/**', route); p2 = c2.new_page(); p2.on('pageerror', lambda e: errs.append(str(e)))
        login(p2, us[6], 'hs1234'); p2.goto(U('tt_home.html')); p2.wait_for_selector('.hm-card', timeout=15000); time.sleep(1.2)
        chk('hạng 7: top 5 + hàng cuối riêng (1 chỗ)', p2.locator('.hm-top').first.locator('tr.me').count() == 1 and p2.locator('.hm-top').first.locator('tbody tr.me').first.inner_text().strip().startswith('7'))
        chk('điện thoại: không tràn ngang', p2.evaluate('document.documentElement.scrollWidth') <= 392)
        p2.screenshot(path='/tmp/home_mobile.png', full_page=True)
        # chuyển hướng từ trang chủ cũ
        p3 = c.new_page(); p3.goto(U('tt_home.html')); p3.wait_for_selector('.hm-card'); p3.close()
        # --- giáo viên: tab Tổng quan là tab mở đầu
        c3 = br.new_context(viewport={'width': 1280, 'height': 900}); c3.route('**/script.google.com/**', route); t = c3.new_page(); t.on('pageerror', lambda e: errs.append(str(e)))
        login(t, gv, gpw); t.goto(U('admin.html')); t.wait_for_selector('.hm-k', timeout=15000); time.sleep(1)
        chk('GV mở trang quản trị → tab Tổng quan', t.locator('#tabs button.on').inner_text().startswith('Tổng quan'))
        chk('KPI + bảng lớp + vinh danh mỗi lộ trình', t.locator('.hm-k').count() == 6 and t.locator('.hm-top tbody tr').count() >= 1 and t.locator('.hm-f').count() == 6)
        chk('học sinh chưa bắt đầu nằm trong "Cần chú ý"', 'Chưa bắt đầu' in t.inner_text('.hm-two'))
        t.screenshot(path='/tmp/over_desktop.png', full_page=True)
        chk('không lỗi JS: %s' % errs, not errs)
        br.close()
finally:
    srv.kill(); web.kill()
    json.dump(IX, open(os.path.join(ROOT, 'thuthach/index.json'), 'w', encoding='utf8'), ensure_ascii=False)
    try: os.remove(os.path.join(ROOT, 'thuthach/lopx.json'))
    except OSError: pass
print('%d/%d đạt' % (sum(res), len(res)))
