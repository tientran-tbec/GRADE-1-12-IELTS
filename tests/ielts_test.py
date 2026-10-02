# -*- coding: utf-8 -*-
"""IELTS Reading trong web tổng: lớp IELTS, giao bài, khoá bài chưa giao, bỏ ô nhập tên, ghi kết quả/nhật ký theo tài khoản, admin làm thử không ghi."""
import os, subprocess, time, json, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8793
srv = subprocess.Popen(['node', os.path.join(ROOT, 'tests/gas_server.js'), str(PORT)], stdout=subprocess.PIPE); srv.stdout.readline()
res = []
def chk(n, ok): res.append(bool(ok)); print('OK  ' if ok else 'FAIL', n)
def api(d):
    r = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=json.dumps(d).encode(), method='POST')
    return json.loads(urllib.request.urlopen(r).read())
def dump(): return json.loads(urllib.request.urlopen('http://127.0.0.1:%d/dump' % PORT).read())
def route(r):
    req = r.request
    if req.method == 'OPTIONS': r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'}); return
    rq = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=req.post_data.encode() if req.post_data else None, method=req.method)
    r.fulfill(status=200, body=urllib.request.urlopen(rq).read(), headers={'access-control-allow-origin': '*', 'content-type': 'text/plain'})
U = lambda p: 'file://' + os.path.join(ROOT, p)
try:
    A = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'})['token']
    chk('tạo lớp IELTS', api({'action': 'adm_class_save', 'token': A, 'cls': {'id': 'IELTS1', 'name': 'Lớp IELTS 1', 'grade': 'IELTS'}})['ok'])
    r = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Lê Thị An', 'cls': 'IELTS1', 'password': 'hs1234'}}); un = r['user']['username']
    chk('tạo HS lớp IELTS', r['ok'])
    chk('giao 2 bộ IELTS', api({'action': 'adm_assign_save', 'token': A, 'cls': 'IELTS1', 'sets': ['ielts-rd-test01', 'ielts-rd-completion']})['ok'])
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        def newpage():
            c = br.new_context(viewport={'width': 1200, 'height': 900}); c.route('**/script.google.com/**', route)
            p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e))); p.on('dialog', lambda d: d.accept()); return p, errs
        pg, errs = newpage()
        pg.goto(U('login.html')); pg.fill('#u', un); pg.fill('#p', 'hs1234'); pg.click('#b1')
        # lần đầu bị bắt đổi MK
        pg.wait_for_selector('#np', timeout=5000); pg.fill('#op', 'hs1234'); pg.fill('#np', 'matkhau9'); pg.fill('#np2', 'matkhau9'); pg.click('#b2'); pg.wait_for_url('**/index.html*')
        pg.wait_for_selector('.setcard:not([hidden])'); time.sleep(0.3)
        vis = pg.eval_on_selector_all('.setcard:not([hidden]) .tile:not([hidden])', 'els=>els.map(e=>e.getAttribute("href"))')
        chk('HS IELTS chỉ thấy Test 1 + Completion', vis and all(('Test1_Reading' in h) or ('/Completion/' in h) for h in vis) and any('Test1_Reading' in h for h in vis) and any('/Completion/' in h for h in vis))
        chk('HS không thấy thẻ "sắp có"', 'Sắp có' not in pg.inner_text('main'))
        # Full Test 1
        pg.goto(U('WebBaiTap/IELTS/Reading/FullTest/Test1_Reading.html')); pg.wait_for_selector('#nameOverlay button')
        chk('Full Test: không có ô nhập tên/lớp', not pg.is_visible('#stuName') and not pg.is_visible('#stuClass'))
        chk('Full Test: lời chào đúng tên', 'Lê Thị An' in pg.inner_text('#nameOverlay'))
        pg.click('#nameOverlay button'); time.sleep(0.4)
        chk('Full Test: bắt đầu không báo lỗi', pg.inner_text('#nameErr').strip() == '' and not pg.is_visible('#nameOverlay'))
        pg.click('#submitBtn'); pg.click('.btn-confirm'); pg.wait_for_selector('button[onclick="closeResult()"]', state='visible'); time.sleep(1)
        rows = dump().get('Lop1-12_KetQua', [])
        last = rows[-1] if rows else []
        chk('Full Test: kết quả ghi đúng bộ/tài khoản', len(rows) >= 2 and last[4] == 'ielts-rd-test01' and last[5] == 'Test1_Reading' and last[17] == un and last[2] == 'Lê Thị An' and last[3] == 'IELTS1' and last[8] == 40)
        chk('Full Test: ghi chế độ ielts-reading + Band', last[6] == 'ielts-reading' and 'Band' in str(last[16]))
        # bài chưa giao
        pg.goto(U('WebBaiTap/IELTS/Reading/FullTest/Test2_Reading.html')); pg.wait_for_url('**/index.html?denied=1*'); chk('Test 2 chưa giao → bị đẩy về index', True)
        # Completion
        pg.goto(U('WebBaiTap/IELTS/Reading/TheoDang/Completion/Test1_Passage1_Completion.html')); pg.wait_for_selector('#nameOverlay button')
        chk('Completion: không có ô nhập', not pg.is_visible('#stuName'))
        pg.click('#nameOverlay button'); time.sleep(0.6)
        pg.click('#submitBtn'); pg.click('.btn-confirm'); pg.wait_for_selector('button[onclick="closeResult()"]', state='visible'); time.sleep(1.2)
        d = dump(); rows = d.get('Lop1-12_KetQua', []); last = rows[-1]
        chk('Completion: kết quả ghi đúng bộ/trang', last[4] == 'ielts-rd-completion' and last[5] == 'Test1_Passage1_Completion' and last[17] == un)
        ev = [x for x in d.get('Lop1-12_NhatKy', []) if str(x[1]).startswith('IELTS')]
        chk('Completion: nhật ký sự kiện (enter/submit) theo tài khoản', any('enter' in x[1] for x in ev) and any('submit' in x[1] for x in ev) and all(x[-1] == un for x in ev))
        chk('HS: không lỗi JS', not errs)
        # admin làm thử: không ghi
        n0 = sum(len(v) for v in d.values())
        pa, errs2 = newpage()
        pa.goto(U('login.html')); pa.fill('#u', 'admin'); pa.fill('#p', 'Admin@123'); pa.click('#b1'); pa.wait_for_url('**/admin.html*')
        pa.goto(U('WebBaiTap/IELTS/Reading/FullTest/Test2_Reading.html')); pa.wait_for_selector('#nameOverlay button')
        chk('admin: vào được bài chưa giao, không ô nhập', not pa.is_visible('#stuName') and 'làm thử' in pa.inner_text('#nameOverlay'))
        pa.click('#nameOverlay button'); time.sleep(0.4); pa.click('#submitBtn'); pa.click('.btn-confirm'); time.sleep(1.2)
        chk('admin làm thử không ghi dữ liệu', sum(len(v) for v in dump().values()) == n0)
        chk('admin: không lỗi JS', not errs2)
        # trang chủ admin thấy "sắp có"
        pa.goto(U('index.html')); pa.wait_for_selector('.setcard'); time.sleep(0.3)
        chk('admin thấy mục IELTS đủ 4 kỹ năng', all(k in pa.inner_text('main') for k in ['Reading', 'Listening', 'Writing', 'Speaking']))
finally:
    srv.kill()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI')
raise SystemExit(0 if all(res) else 1)
