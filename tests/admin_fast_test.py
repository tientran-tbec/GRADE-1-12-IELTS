# -*- coding: utf-8 -*-
"""Máy chủ giả lập chậm 1,5 giây: trang quản trị lần 2 phải hiện dữ liệu ngay (bản lưu), thao tác khoá/mở khoá đổi giao diện ngay."""
import os, subprocess, time, json, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT, WEB = 8789, 8790
srv = subprocess.Popen(['node', os.path.join(ROOT, 'tests/gas_server.js'), str(PORT)], stdout=subprocess.PIPE, env=dict(os.environ, DELAY_MS='0')); srv.stdout.readline()
web = subprocess.Popen(['python3', '-m', 'http.server', str(WEB), '--bind', '127.0.0.1'], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
res = []; DELAY = [0]
def chk(n, ok): res.append(bool(ok)); print('OK  ' if ok else 'FAIL', n)
def api(d):
    r = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=json.dumps(d).encode(), method='POST'); return json.loads(urllib.request.urlopen(r).read())
def route(r):
    req = r.request
    if req.method == 'OPTIONS': r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'}); return
    resp = r.fetch(url='http://127.0.0.1:%d/exec' % PORT, method=req.method, headers={'content-type': 'text/plain'}, post_data=req.post_data)
    r.fulfill(status=200, body=resp.body(), headers={'access-control-allow-origin': '*', 'content-type': 'text/plain'})
U = lambda p: 'http://127.0.0.1:%d/%s' % (WEB, p)
try:
    LG = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'}); A = LG['token']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': 'FA', 'name': 'FA', 'grade': 10}})
    for i in range(6): api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Hoc Sinh %d' % i, 'classes': ['FA'], 'password': 'hs1234'}})
    with sync_playwright() as pw:
        br = pw.chromium.launch(); c = br.new_context(viewport={'width': 1300, 'height': 800}); c.route('**/script.google.com/**', route)
        p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e))); p.on('dialog', lambda d: d.accept())
        c.add_init_script("localStorage.setItem('gn_auth', %s)" % json.dumps(json.dumps({'token': LG['token'], 'user': LG['user']})))
        urllib.request.urlopen('http://127.0.0.1:%d/delay?ms=1500' % PORT)
        t0 = time.time(); p.goto(U('admin.html')); p.wait_for_selector('#tbS a[href*="student.html"]'); t1 = time.time() - t0
        chk('lần đầu (máy chủ chậm 1,5s): hiện bảng sau %.1fs' % t1, t1 >= 1.4)
        time.sleep(3)
        t0 = time.time(); p.goto(U('admin.html')); p.wait_for_selector('#tbS a[href*="student.html"]'); t2 = time.time() - t0
        chk('lần sau: hiện bảng NGAY từ bản lưu (%.2fs)' % t2, t2 < 1.0)
        time.sleep(3)
        # khoá tài khoản: giao diện đổi ngay dù máy chủ chậm
        p.wait_for_selector('#tbS button[data-a=tog]')
        t0 = time.time(); p.click('#tbS tr:nth-child(1) button[data-a=tog]'); p.wait_for_function("document.querySelector('#tbS tr:nth-child(1)').innerText.indexOf('Đã khoá')>=0 || document.querySelector('#tbS tr:nth-child(1)').innerText.indexOf('Hoạt động')<0"); t3 = time.time() - t0
        chk('bấm Khoá: giao diện đổi ngay (%.2fs)' % t3, t3 < 0.6)
        time.sleep(3.5)
        chk('sau khi lưu ngầm, trạng thái giữ nguyên (đã khoá)', 'Đã khoá' in p.inner_text('#tbS tr:nth-child(1)'))
        # lọc / tìm kiếm chạy tại chỗ
        t0 = time.time(); p.fill('#fq', 'Hoc Sinh 3'); p.wait_for_function("document.querySelectorAll('#tbS tr').length===1"); chk('tìm kiếm tại chỗ (%.2fs)' % (time.time() - t0), time.time() - t0 < 0.5)
        chk('không lỗi JS', not errs)
        if errs: print(errs[:3])
        br.close()
finally:
    srv.terminate(); web.terminate()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI: %d/%d' % (res.count(False), len(res)))
raise SystemExit(0 if all(res) else 1)
