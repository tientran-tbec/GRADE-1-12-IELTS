# -*- coding: utf-8 -*-
"""Trang quản lý học sinh, xoá kết quả, sao lưu / khôi phục / reset (giao diện admin)."""
import os, subprocess, time, json, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT, WEB = 8795, 8796
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
try:
    A = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'})['token']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': 'MG', 'name': 'Lớp MG', 'grade': 10}})
    api({'action': 'adm_assign_save', 'token': A, 'cls': 'MG', 'sets': ['lop10-u1-luyentap']})
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': 'MG2', 'name': 'Lớp MG2', 'grade': 10}})
    gv = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Cô Thường', 'role': 'teacher', 'password': 'gv1234', 'classes': []}})['user']['username']
    api({'action': 'adm_teacher_classes', 'token': A, 'username': gv, 'classes': ['MG']})
    hs = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Em Quản Lý', 'classes': ['MG'], 'password': 'hs1234'}})['user']['username']
    with sync_playwright() as pw:
        br = pw.chromium.launch(); errs = []
        def newpage(accept_dl=False):
            c = br.new_context(viewport={'width': 1300, 'height': 900}, accept_downloads=True); c.route('**/script.google.com/**', route)
            p = c.new_page(); p.on('pageerror', lambda e: errs.append(str(e))); p.on('dialog', lambda d: d.accept()); return p
        def login(p, u, pw_, newpw=None):
            p.goto(U('login.html')); p.fill('#u', u); p.fill('#p', pw_); p.click('#b1')
            if newpw: p.wait_for_selector('#np'); p.fill('#op', pw_); p.fill('#np', newpw); p.fill('#np2', newpw); p.click('#b2')
            p.wait_for_url('**/*.html*', timeout=8000); time.sleep(0.6)
        ps = newpage(); login(ps, hs, 'hs1234', 'matkhau5'); tok = ps.evaluate("JSON.parse(localStorage.getItem('gn_auth')).token")
        for pg, sc in (('p1', 5), ('p2', 8), ('p3', 3)):
            raw({'action': 'grade_save_result', 'token': tok, 'set_id': 'lop10-u1-luyentap', 'page_id': pg, 'mode': 'test', 'score': sc, 'total': 10, 'pct': sc * 10, 'score10': sc, 'time_spent': 300, 'tab_switch': 0, 'blur': 0, 'fullscreen_exit': 0, 'answers': {}})
        pa = newpage(); login(pa, 'admin', 'Admin@123'); pa.goto(U('admin.html')); pa.wait_for_selector('#tbS tr')
        # --- tab học sinh: tên là link
        chk('tab Học sinh: tên là liên kết tới trang quản lý', pa.locator('#tbS a[href*="student.html?u="]').count() >= 1)
        pa.click('#tbS a[href*="student.html"]'); pa.wait_for_selector('#mbar button'); pa.wait_for_selector('#tbR tr td:nth-child(2)')
        chk('trang quản lý có các nút quản lý + tổng kết', pa.locator('#mbar button').count() >= 5 and 'Em Quản Lý' in pa.inner_text('#head') and pa.locator('#tbR tr').count() == 3)
        # sửa tên + lớp
        pa.click('#mbar button[data-m=edit]'); pa.fill('#en', 'Em Đã Sửa'); pa.check('#ec input[value=MG2]'); pa.click('#ef button:not(#ex)'); pa.wait_for_function("document.querySelector('#head').innerText.indexOf('Em Đã Sửa')>=0")
        chk('sửa tên + thêm lớp', 'MG2' in pa.inner_text('#head'))
        pa.click('#mbar button[data-m=rank]'); pa.select_option('select[data-rc=MG]', 'P'); pa.click('#rs'); pa.wait_for_function("document.querySelector('#head').innerText.indexOf('Phó nhóm')>=0")
        chk('đặt chức vụ phó nhóm', True)
        pa.click('#mbar button[data-m=tog]'); pa.wait_for_function("document.querySelector('#head').innerText.indexOf('Đã khoá')>=0"); chk('khoá tài khoản', True)
        pa.click('#mbar button[data-m=tog]'); pa.wait_for_function("document.querySelector('#head').innerText.indexOf('Hoạt động')>=0"); chk('mở khoá', True)
        pa.click('#mbar button[data-m=pw]'); pa.wait_for_selector('#px'); chk('đặt lại MK hiện mật khẩu mới', len(pa.inner_text('#mbox')) > 30); pa.click('#px')
        # xoá 1 kết quả
        pa.click('#tbR button[data-d]'); pa.wait_for_function("document.querySelectorAll('#tbR tr').length===2"); chk('xoá 1 kết quả trong trang học sinh', pa.locator('#tbR tr').count() == 2)
        # --- tab kết quả: chọn nhiều + xoá
        pa.goto(U('admin.html#results')); pa.wait_for_selector('#tbR .rsel')
        chk('tab Kết quả có ô chọn + nút xoá từng dòng', pa.locator('#tbR .rsel').count() == 2 and pa.locator('#tbR button[data-d]').count() == 2)
        pa.click('#tbR button[data-d]'); pa.wait_for_function("document.querySelectorAll('#tbR .rsel').length===1"); chk('xoá 1 dòng', True)
        # --- sao lưu
        pa.click('#tabs button[data-t=backup]'); pa.wait_for_selector('#bkB input')
        chk('tab Sao lưu hiện đủ các phần', pa.locator('#bkB input').count() == 8 and pa.locator('#bkX input').count() == 10)
        pa.check('#bkB input[value=results]'); pa.check('#bkB input[value=classes]')
        with pa.expect_download() as dl: pa.click('#bkGo')
        path = dl.value.path(); bk = json.load(open(path, encoding='utf8'))
        chk('file sao lưu: đúng phần đã chọn + dữ liệu', set(bk['parts']) == {'results', 'classes'} and len(bk['parts']['results']['rows']) == 1 and len(bk['parts']['classes']['rows']) >= 2)
        # --- reset kết quả (không tự sao lưu)
        pa.uncheck('#bkPre'); pa.check('#bkX input[value=results]')
        chk('nút Reset bị khoá khi chưa gõ RESET', pa.is_disabled('#bkReset'))
        pa.fill('#bkConf', 'RESET'); pa.click('#bkReset'); pa.wait_for_function("document.querySelector('#bkMsgX').innerText.indexOf('Đã xoá')>=0")
        pa.click('#tabs button[data-t=results]'); pa.click('#rgo'); pa.wait_for_function("document.querySelector('#rinfo').innerText.indexOf('0 kết quả')>=0"); chk('reset kết quả: bảng trống', pa.locator('#tbR .rsel').count() == 0)
        # --- khôi phục
        pa.click('#tabs button[data-t=backup]'); pa.set_input_files('#bkFile', path); pa.wait_for_selector('#bkR input')
        chk('chọn file: liệt kê phần có trong file', pa.locator('#bkR input').count() == 2)
        pa.uncheck('#bkR input[value=classes]'); pa.click('#bkRestore'); pa.wait_for_function("document.querySelector('#bkMsgR').innerText.indexOf('Đã khôi phục 1')>=0")
        pa.wait_for_load_state(); time.sleep(2); pa.goto(U('admin.html#results')); pa.wait_for_selector('#tbR .rsel')
        chk('khôi phục: kết quả trở lại', pa.locator('#tbR .rsel').count() == 1)
        # reset học sinh
        pa.click('#tabs button[data-t=backup]'); pa.uncheck('#bkPre'); pa.check('#bkX input[value=students]'); pa.fill('#bkConf', 'RESET'); pa.click('#bkReset'); pa.wait_for_function("document.querySelector('#bkMsgX').innerText.indexOf('students')>=0")
        pa.click('#tabs button[data-t=students]'); chk('reset học sinh: danh sách trống', pa.locator('#tbS a[href*="student.html"]').count() == 0)
        # --- GV thường: không có tab sao lưu, không có nút xoá
        pt = newpage(); login(pt, gv, 'gv1234', 'gvmoi123'); pt.goto(U('admin.html')); pt.wait_for_selector('#tabs button'); pt.wait_for_timeout(1200)
        chk('GV thường không có tab Sao lưu', 'Sao lưu' not in pt.inner_text('#tabs'))
        chk('GV thường không gọi được sao lưu/reset/xoá', not api({'action': 'adm_backup', 'token': pt.evaluate("JSON.parse(localStorage.getItem('gn_auth')).token"), 'part': 'users'})['ok'])
        chk('không lỗi JS', not errs)
        if errs: print(errs[:3])
        br.close()
finally:
    srv.terminate(); web.terminate()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI: %d/%d' % (res.count(False), len(res)))
raise SystemExit(0 if all(res) else 1)
