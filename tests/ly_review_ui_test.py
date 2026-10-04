# -*- coding: utf-8 -*-
"""Màn hình GV duyệt tự luận Lý (admin.html tab 'Tự luận Lý') + mục 'Tự luận Vật lí' trong me.html."""
import os, subprocess, time, json, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT, WEB = 8795, 8796
srv = subprocess.Popen(['node', os.path.join(ROOT, 'tests/ly_server.js'), str(PORT)], stdout=subprocess.PIPE); srv.stdout.readline()
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
KEY = json.load(open(os.path.join(ROOT, 'WebBaiTap/Lop11/Ly/essay_key.json'), encoding='utf8')); uid = sorted(KEY)[0]
try:
    A = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'})['token']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': '11L', 'name': '11L', 'grade': 11}})
    hs = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Em Ly', 'classes': ['11L'], 'password': 'hs1234'}})['user']['username']
    gvr = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Co Ly', 'role': 'teacher'}}); gv, gpw = gvr['user']['username'], gvr['password']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': '11L', 'name': '11L', 'grade': 11, 'teacher': gv}})
    api({'action': 'adm_assign_save', 'token': A, 'cls': '11L', 'sets': ['ly11-b01']})
    H = api({'action': 'auth_login', 'username': hs, 'password': 'hs1234', 'device': 'h'})
    r = api({'action': 'ly_essay', 'token': H['token'], 'uid': uid, 'set_id': 'ly11-b01', 'page_id': 'b01-tl-1', 'mode': 'prac', 'answer': 'Bài làm thử của em: x = 5 cm, v = 10 cm/s.'})
    chk('HS nộp tự luận (%s)' % uid, r.get('ok')); api({'action': 'auth_logout', 'token': H['token']})
    with sync_playwright() as pw:
        br = pw.chromium.launch(); c = br.new_context(viewport={'width': 1300, 'height': 850}); c.route('**/script.google.com/**', route)
        p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e)))
        # GV
        p.goto(U('login.html')); p.fill('#u', gv); p.fill('#p', gpw); p.click('#b1'); time.sleep(2.5)
        if p.locator('#np').is_visible(): p.fill('#op', gpw); p.fill('#np', 'matkhau5'); p.fill('#np2', 'matkhau5'); p.click('#b2'); time.sleep(1.5)
        p.goto(U('admin.html#essay')); p.wait_for_selector('.ey', timeout=15000)
        chk('GV thấy bài chờ duyệt', p.locator('.ey').count() == 1 and 'Em Ly' in p.inner_text('.ey'))
        chk('hiện bài làm của học sinh', 'x = 5 cm' in p.inner_text('.ey .ans'))
        p.click('.ey summary'); time.sleep(1)
        chk('mở đề + lời giải mẫu + biểu điểm', 'Lời giải mẫu' in p.inner_text('.ey details') and 'Biểu điểm' in p.inner_text('.ey details'))
        chk('KaTeX vẽ công thức trong đề', p.locator('.ey .katex').count() >= 1)
        chk('hiện điểm AI gợi ý', 'AI gợi ý' in p.inner_text('.ey .ai'))
        p.click('.eyuse'); chk('Dùng điểm AI điền vào ô', p.input_value('.eysc') != '')
        p.fill('.eysc', '0.75'); p.fill('.eycm', 'Thiếu đơn vị.'); p.click('.eyok'); p.wait_for_function("document.querySelector('.eymsg').innerText.indexOf('Đã lưu')>=0")
        chk('Duyệt: thẻ chuyển Đã duyệt', 'Đã duyệt' in p.inner_text('.ey .bar'))
        p.select_option('#eys', 'pending'); time.sleep(1.2)
        chk('lọc Chờ duyệt: hết bài', p.locator('.ey').count() == 0)
        # HS
        c2 = br.new_context(viewport={'width': 1300, 'height': 850}); c2.route('**/script.google.com/**', route); q = c2.new_page(); q.on('pageerror', lambda e: errs.append(str(e)))
        q.goto(U('login.html')); q.fill('#u', hs); q.fill('#p', 'hs1234'); q.click('#b1'); time.sleep(2.5)
        if q.locator('#np').is_visible(): q.fill('#op', 'hs1234'); q.fill('#np', 'matkhau5'); q.fill('#np2', 'matkhau5'); q.click('#b2'); time.sleep(1.5)
        q.goto(U('me.html')); q.wait_for_selector('#lyes:not([hidden])', timeout=15000)
        t = q.inner_text('#lyes'); chk('Điểm của tôi: thấy điểm GV + nhận xét', '0,75' in t and 'Thiếu đơn vị' in t and 'Đã duyệt' in t)
        chk('không lỗi JS', not errs)
        if errs: print(errs[:4])
        br.close()
finally:
    srv.terminate(); web.terminate()
print('ALL OK %d' % len(res) if all(res) else 'CÓ LỖI %d/%d' % (res.count(False), len(res)))
raise SystemExit(0 if all(res) else 1)
