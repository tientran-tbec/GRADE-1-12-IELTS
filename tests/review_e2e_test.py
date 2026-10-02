# -*- coding: utf-8 -*-
"""Cấp toàn quyền cho GV; xem lại bài làm + chi tiết vi phạm; trang tổng kết học sinh. Phục vụ site qua http để fetch trang đề."""
import os, subprocess, time, json, re, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT, WEB = 8797, 8798
srv = subprocess.Popen(['node', os.path.join(ROOT, 'tests/gas_server.js'), str(PORT)], stdout=subprocess.PIPE); srv.stdout.readline()
web = subprocess.Popen(['python3', '-m', 'http.server', str(WEB), '--bind', '127.0.0.1'], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
res = []
def chk(n, ok): res.append(bool(ok)); print('OK  ' if ok else 'FAIL', n)
def raw(d):
    r = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=json.dumps(d).encode(), method='POST'); return urllib.request.urlopen(r).read().decode()
def api(d): return json.loads(raw(d))
def route(r):
    req = r.request
    if req.method == 'OPTIONS': r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'}); return
    rq = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=req.post_data.encode() if req.post_data else None, method=req.method)
    r.fulfill(status=200, body=urllib.request.urlopen(rq).read(), headers={'access-control-allow-origin': '*', 'content-type': 'text/plain'})
U = lambda p: 'http://127.0.0.1:%d/%s' % (WEB, p)
def quiz_of(path):
    s = open(os.path.join(ROOT, path), encoding='utf8').read(); i = s.index('window.QUIZ=') + 12; d = 0
    for j in range(i, len(s)):
        if s[j] == '{': d += 1
        elif s[j] == '}':
            d -= 1
            if d == 0: return json.loads(s[i:j + 1])
try:
    A = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'})['token']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': 'RV', 'name': 'Lớp RV', 'grade': 10}})
    gv = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Cô Toàn', 'role': 'teacher', 'password': 'gv1234'}})['user']['username']
    hs = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Em Nộp Bài', 'classes': ['RV'], 'password': 'hs1234'}})['user']['username']
    api({'action': 'adm_assign_save', 'token': A, 'cls': 'RV', 'sets': ['lop10-u1-luyentap']})
    Q = quiz_of('WebBaiTap/Lop10/Unit1/luyentap/kiem-tra-15.html')
    a1 = Q['ANS']['t15.1']; a1 = a1[0] if isinstance(a1, list) else a1; wrong = next(x for x in 'ABCD' if x != (Q['ANS']['t15.2'] if not isinstance(Q['ANS']['t15.2'], list) else Q['ANS']['t15.2'][0]))
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        def newpage(w=1300):
            c = br.new_context(viewport={'width': w, 'height': 900}); c.route('**/script.google.com/**', route)
            p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e))); p.on('dialog', lambda d: d.accept()); return p, errs
        def login(p, u, pw_, newpw=None):
            p.goto(U('login.html')); p.fill('#u', u); p.fill('#p', pw_); p.click('#b1')
            if newpw: p.wait_for_selector('#np'); p.fill('#op', pw_); p.fill('#np', newpw); p.fill('#np2', newpw); p.click('#b2')
            p.wait_for_url('**/*.html*', timeout=8000); time.sleep(0.6)
        # HS nộp bài (qua trang thật để lấy token, sau đó gửi kết quả có sự kiện vi phạm)
        ps, e0 = newpage(); login(ps, hs, 'hs1234', 'matkhau5'); tok = ps.evaluate("JSON.parse(localStorage.getItem('gn_auth')).token")
        out = raw({'action': 'grade_save_result', 'token': tok, 'set_id': 'lop10-u1-luyentap', 'page_id': 'kiem-tra-15', 'mode': 'test', 'score': 1, 'total': 10, 'pct': 10, 'score10': 1, 'time_spent': 400,
                   'tab_switch': 1, 'blur': 0, 'fullscreen_exit': 0, 'answers': {'t15.1': a1, 't15.2': wrong}, 'events': [{'ev': 'enter', 't': 0}, {'ev': 'tab_hidden', 't': 31}, {'ev': 'paste', 't': 55}, {'ev': 'shortcut', 't': 70, 'x': 'Ctrl+C'}]})
        chk('HS nộp bài có sự kiện vi phạm', out == 'ok')
        # --- admin: cấp toàn quyền 1 nút
        pa, e1 = newpage(); login(pa, 'admin', 'Admin@123'); pa.goto(U('admin.html')); pa.wait_for_selector('#tabs button')
        pa.click('#tabs button[data-t=teachers]'); pa.wait_for_selector('#tbT button[data-a=tfull]')
        chk('hàng GV có nút "Cấp toàn quyền"', 'Cấp toàn quyền' in pa.inner_text('#tbT'))
        pa.click('#tbT button[data-a=tfull]'); pa.wait_for_function("document.querySelector('#tbT').innerText.indexOf('Thu hồi toàn quyền')>=0")
        chk('cấp toàn quyền: nút đổi thành Thu hồi + hiện đủ quyền', 'Thu hồi toàn quyền' in pa.inner_text('#tbT') and 'Quản lý lớp' in pa.inner_text('#tbT'))
        pt, e2 = newpage(); login(pt, gv, 'gv1234', 'gvmoi123'); pt.goto(U('admin.html')); pt.wait_for_selector('#tabs button'); pt.wait_for_timeout(1500)
        tabs = pt.inner_text('#tabs'); chk('GV toàn quyền thấy tab Giáo viên + Giao bài', 'Giáo viên' in tabs and 'Giao bài' in tabs)
        pt.click('#tabs button[data-t=teachers]'); chk('GV toàn quyền thấy nút Quyền / Lớp phụ trách của giáo viên', pt.locator('#tbT button[data-a=tperm]').count() >= 1 and pt.locator('#addT:visible').count() == 1)
        # --- xem kết quả + xem bài + vi phạm
        pt.click('#tabs button[data-t=results]'); pt.wait_for_selector('#tbR button[data-v]')
        chk('bảng kết quả có nút Xem bài + cảnh báo bấm được + tên là liên kết', pt.locator('#tbR button[data-v]').count() == 1 and pt.locator('#tbR button[title*="vi phạm"]').count() == 1 and pt.locator('#tbR a[href*="student.html"]').count() == 1)
        pt.click('#tbR button[data-v]'); pt.wait_for_selector('#gnrvb tr'); pt.wait_for_timeout(300)
        m = pt.inner_text('.gnrv-b')
        chk('xem bài: dựng lại đề + câu trả lời HS + đáp án đúng', 'Đúng: 1' in m and 'Sai: 1' in m and pt.locator('#gnrvb tr[data-r=ok]').count() == 1 and pt.locator('#gnrvb tr[data-r=no]').count() == 1)
        chk('xem bài: hiển thị chi tiết vi phạm theo mốc thời gian', '0:31' in m and 'Chuyển sang tab' in m and '0:55' in m and 'Cố dán nội dung' in m and 'Ctrl+C' in m)
        if os.environ.get('SHOT'): pt.emulate_media(color_scheme='dark'); pt.screenshot(path=os.environ['SHOT'] + '/review.png')
        pt.check('#gnrvf'); chk('lọc chỉ câu sai/bỏ trống', pt.locator('#gnrvb tr:not([hidden])[data-r=ok]').count() == 0 and pt.locator('#gnrvb tr:not([hidden])[data-r=no]').count() == 1)
        pt.click('#gnrvx'); chk('đóng cửa sổ xem bài', pt.locator('#gnrv').count() == 0)
        pt.click('#tbR button[title*="vi phạm"]'); pt.wait_for_selector('.gnrv-ev'); chk('bấm cảnh báo mở chi tiết vi phạm', 'Vi phạm ghi nhận' in pt.inner_text('.gnrv-b')); pt.click('#gnrvx')
        # --- trang tổng kết học sinh
        pt.click('#tbR a[href*="student.html"]'); pt.wait_for_selector('#tbR tr td:nth-child(2)'); pt.wait_for_timeout(500)
        chk('trang tổng kết: tên + lớp + thống kê', 'Em Nộp Bài' in pt.inner_text('#head') and 'RV' in pt.inner_text('#head') and pt.locator('#stats .card').count() == 6)
        chk('tổng kết: bài được giao + lần nộp', 'Kiểm tra 15' in pt.inner_text('#tbA') or 'luyện tập' in pt.inner_text('#tbA') or 'lop10-u1-luyentap' in pt.inner_text('#tbA'))
        chk('tổng kết: cảnh báo cộng dồn = 1 lần', pt.locator('#stats .card').nth(4).inner_text().startswith('1'))
        if os.environ.get('SHOT'): pt.screenshot(path=os.environ['SHOT'] + '/summary.png', full_page=True)
        pt.click('#tbR button[data-v]'); pt.wait_for_selector('#gnrvb tr'); chk('từ tổng kết xem lại được bài làm', 'Đúng: 1' in pt.inner_text('.gnrv-b')); pt.click('#gnrvx')
        # --- GV thường (không phụ trách lớp) không xem được
        gv2 = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Cô Khác', 'role': 'teacher', 'password': 'gv1234'}})['user']['username']
        p2, e3 = newpage(); login(p2, gv2, 'gv1234', 'gvmoi456'); p2.goto(U('student.html?u=' + hs)); p2.wait_for_selector('#head .err'); chk('GV ngoài lớp không mở được trang tổng kết', 'không thuộc lớp' in p2.inner_text('#head'))
        errs = e0 + e1 + e2 + e3
        chk('không lỗi JS', not errs)
        if errs: print(errs[:3])
        br.close()
finally:
    srv.terminate(); web.terminate()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI: %d/%d' % (res.count(False), len(res)))
raise SystemExit(0 if all(res) else 1)
