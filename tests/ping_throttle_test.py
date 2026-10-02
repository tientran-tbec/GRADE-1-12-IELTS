# -*- coding: utf-8 -*-
"""Học sinh chuyển trang liên tục: chỉ hỏi máy chủ (auth_ping) tối đa 1 lần / 2 phút; giáo viên luôn hỏi."""
import os, subprocess, time, json, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT, WEB = 8793, 8794
srv = subprocess.Popen(['node', os.path.join(ROOT, 'tests/gas_server.js'), str(PORT)], stdout=subprocess.PIPE); srv.stdout.readline()
web = subprocess.Popen(['python3', '-m', 'http.server', str(WEB), '--bind', '127.0.0.1'], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
res = []
def chk(n, ok): res.append(bool(ok)); print('OK  ' if ok else 'FAIL', n)
def api(d):
    r = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=json.dumps(d).encode(), method='POST'); return json.loads(urllib.request.urlopen(r).read())
calls = []
def route(r):
    req = r.request
    if req.method == 'OPTIONS': r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'}); return
    if req.post_data and '"auth_ping"' in req.post_data: calls.append(1)
    rq = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=req.post_data.encode() if req.post_data else None, method=req.method)
    r.fulfill(status=200, body=urllib.request.urlopen(rq).read(), headers={'access-control-allow-origin': '*', 'content-type': 'text/plain'})
U = lambda p: 'http://127.0.0.1:%d/%s' % (WEB, p)
try:
    A = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'})['token']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': 'PT', 'name': 'PT', 'grade': 10}})
    hs = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Em Ping', 'classes': ['PT'], 'password': 'hs1234'}})['user']['username']
    with sync_playwright() as pw:
        br = pw.chromium.launch(); c = br.new_context(); c.route('**/script.google.com/**', route); p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e)))
        p.goto(U('login.html')); p.fill('#u', hs); p.fill('#p', 'hs1234'); p.click('#b1'); p.wait_for_selector('#np'); p.fill('#op', 'hs1234'); p.fill('#np', 'matkhau5'); p.fill('#np2', 'matkhau5'); p.click('#b2'); p.wait_for_url('**/*.html*'); time.sleep(1)
        time.sleep(4); calls.clear()
        per = []
        for pg in ('index.html', 'me.html', 'index.html', 'me.html'):
            n0 = len(calls); p.goto(U(pg)); time.sleep(1); per.append(len(calls) - n0)
        chk('HS chuyển 4 trang trong vài giây: từ trang thứ 2 trở đi không hỏi máy chủ nữa (%s)' % per, sum(per[1:]) == 0)
        chk('không lỗi JS', not errs)
        br.close()
finally:
    srv.terminate(); web.terminate()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI'); raise SystemExit(0 if all(res) else 1)
