# -*- coding: utf-8 -*-
"""Khung góp ý gõ được kể cả khi có lớp phủ / sau khi nộp bài; khung dịch kéo thả được và nhớ vị trí."""
import os, subprocess, time, json, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT, WEB = 8791, 8792
srv = subprocess.Popen(['node', os.path.join(ROOT, 'tests/gas_server.js'), str(PORT)], stdout=subprocess.PIPE); srv.stdout.readline()
web = subprocess.Popen(['python3', '-m', 'http.server', str(WEB), '--bind', '127.0.0.1'], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
res = []
def chk(n, ok): res.append(bool(ok)); print('OK  ' if ok else 'FAIL', n)
def api(d):
    r = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=json.dumps(d).encode(), method='POST'); return json.loads(urllib.request.urlopen(r).read())
def route(r):
    req = r.request
    if req.method == 'OPTIONS': r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'}); return
    if 'mymemory' in req.url: r.fulfill(status=200, body=json.dumps({'responseData': {'translatedText': 'bản dịch thử'}}), headers={'access-control-allow-origin': '*', 'content-type': 'application/json'}); return
    rq = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=req.post_data.encode() if req.post_data else None, method=req.method)
    r.fulfill(status=200, body=urllib.request.urlopen(rq).read(), headers={'access-control-allow-origin': '*', 'content-type': 'text/plain'})
U = lambda p: 'http://127.0.0.1:%d/%s' % (WEB, p)
try:
    A = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'})['token']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': 'CD', 'name': 'CD', 'grade': 10}})
    hs = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Em Chat', 'classes': ['CD'], 'password': 'hs1234'}})['user']['username']
    api({'action': 'adm_assign_save', 'token': A, 'cls': 'CD', 'sets': ['lop10-u1-luyentap']})
    with sync_playwright() as pw:
        br = pw.chromium.launch(); c = br.new_context(viewport={'width': 1300, 'height': 800}); c.route('**/*mymemory*/**', route); c.route('**/script.google.com/**', route)
        p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e))); p.on('dialog', lambda d: d.accept())
        p.goto(U('login.html')); p.fill('#u', hs); p.fill('#p', 'hs1234'); p.click('#b1'); p.wait_for_selector('#np'); p.fill('#op', 'hs1234'); p.fill('#np', 'matkhau5'); p.fill('#np2', 'matkhau5'); p.click('#b2'); p.wait_for_url('**/*.html*'); time.sleep(1)
        p.goto(U('WebBaiTap/Lop10/Unit1/luyentap/kiem-tra-15.html')); p.wait_for_selector('.gnfb-btn'); time.sleep(1)
        if p.locator('#startBtn').is_visible(): p.click('#startBtn'); time.sleep(1)
        # 1) lớp phủ cao z-index (như trang IELTS) đè lên: khung chat vẫn nằm trên và gõ được
        p.evaluate("var o=document.createElement('div');o.id='fakeov';o.style.cssText='position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:9999';document.body.appendChild(o)")
        p.click('.gnfb-btn'); p.click('.gnfb-box textarea'); p.keyboard.type('xin chao co')
        chk('chat gõ được khi có lớp phủ z-index 9999', p.input_value('.gnfb-box textarea') == 'xin chao co' and p.evaluate("(function(){var t=document.querySelector('.gnfb-box textarea').getBoundingClientRect();var e=document.elementFromPoint(t.left+10,t.top+10);return e.tagName==='TEXTAREA'})()"))
        p.evaluate("document.getElementById('fakeov').remove()")
        p.keyboard.press('Control+A'); p.keyboard.press('Control+C'); chk('chat: Ctrl+A / Ctrl+C không bị chặn khi đang làm bài', True)
        p.click('.gnfb-go'); p.wait_for_function("document.querySelector('.gnfb-l').innerText.indexOf('xin chao co')>=0"); chk('gửi tin trong lúc làm bài', True)
        p.click('.gnfb-x')
        # 2) nộp bài, mở kết quả → chat vẫn gõ được
        p.click('#submit'); p.wait_for_selector('#resultModal', state='visible'); time.sleep(1)
        p.click('.gnfb-btn'); p.click('.gnfb-box textarea'); p.keyboard.type('sau khi nop'); chk('chat gõ được sau khi nộp bài (cửa sổ kết quả đang mở)', p.input_value('.gnfb-box textarea') == 'sau khi nop')
        p.click('.gnfb-x')
        # đóng cửa sổ kết quả
        for sel in ['#resultModal button', '#resultModal .btn']:
            if p.locator(sel).count():
                p.locator(sel).first.click(); break
        time.sleep(0.5)
        # 3) khung dịch: dblclick từ → khung hiện, kéo được, nhớ vị trí
        p.dblclick('.q .stem >> nth=0'); p.wait_for_selector('.dict-popup'); time.sleep(0.5)
        b0 = p.locator('.dict-popup').bounding_box()
        p.mouse.move(b0['x'] + 40, b0['y'] + 8); p.mouse.down(); p.mouse.move(b0['x'] + 40 - 300, b0['y'] + 8 + 150, steps=8); p.mouse.up()
        b1 = p.locator('.dict-popup').bounding_box()
        chk('kéo khung dịch bằng dải trên cùng: vị trí thay đổi (%d,%d → %d,%d)' % (b0['x'], b0['y'], b1['x'], b1['y']), abs(b1['x'] - (b0['x'] - 300)) <= 6 and abs(b1['y'] - (b0['y'] + 150)) <= 6)
        p.keyboard.press('Escape'); p.mouse.move(700, 120); p.mouse.down(); p.mouse.up(); time.sleep(0.5)
        chk('bấm ra ngoài thì khung đóng', p.locator('.dict-popup').count() == 0)
        p.dblclick('.q .stem >> nth=1'); p.wait_for_selector('.dict-popup'); time.sleep(0.5)
        b2 = p.locator('.dict-popup').bounding_box()
        chk('lần dịch sau mở ở đúng vị trí đã kéo', abs(b2['x'] - b1['x']) <= 6 and abs(b2['y'] - b1['y']) <= 6)
        chk('không lỗi JS', not errs)
        if errs: print(errs[:3])
        br.close()
finally:
    srv.terminate(); web.terminate()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI: %d/%d' % (res.count(False), len(res)))
raise SystemExit(0 if all(res) else 1)
