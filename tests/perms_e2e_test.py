# -*- coding: utf-8 -*-
"""Quyền cấp thêm cho GV + chức vụ HS (trưởng/phó nhóm): giao diện thật + backend = code.gs (mock Node)."""
import os, subprocess, time, json, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8796
srv = subprocess.Popen(['node', os.path.join(ROOT, 'tests/gas_server.js'), str(PORT)], stdout=subprocess.PIPE); srv.stdout.readline()
res = []
def chk(n, ok): res.append(bool(ok)); print('OK  ' if ok else 'FAIL', n)
def api(d):
    r = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=json.dumps(d).encode(), method='POST')
    return json.loads(urllib.request.urlopen(r).read())
def route(r):
    req = r.request
    if req.method == 'OPTIONS': r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'}); return
    rq = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=req.post_data.encode() if req.post_data else None, method=req.method)
    r.fulfill(status=200, body=urllib.request.urlopen(rq).read(), headers={'access-control-allow-origin': '*', 'content-type': 'text/plain'})
U = lambda p: 'file://' + os.path.join(ROOT, p)
try:
    A = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'})['token']
    for c in ('QA', 'QB'): api({'action': 'adm_class_save', 'token': A, 'cls': {'id': c, 'name': 'Lớp ' + c, 'grade': 11}})
    gv = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Cô Quyền', 'role': 'teacher', 'password': 'gv1234'}})['user']['username']
    api({'action': 'adm_teacher_classes', 'token': A, 'username': gv, 'classes': ['QA']})
    mk = lambda n: api({'action': 'adm_user_save', 'token': A, 'user': {'name': n, 'classes': ['QA'], 'password': 'hs1234'}})['user']['username']
    h1, h2, h3 = mk('Học Một'), mk('Học Hai'), mk('Học Ba')
    api({'action': 'adm_assign_save', 'token': A, 'cls': 'QA', 'sets': ['lop11-u1-botro', 'lop11-u1-4kn']})
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        def newpage(w=1200):
            c = br.new_context(viewport={'width': w, 'height': 900}); c.route('**/script.google.com/**', route)
            p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e))); p.on('dialog', lambda d: d.accept()); return p, errs
        def login(p, u, pw_, newpw=None):
            p.goto(U('login.html')); p.fill('#u', u); p.fill('#p', pw_); p.click('#b1')
            if newpw:
                p.wait_for_selector('#np'); p.fill('#op', pw_); p.fill('#np', newpw); p.fill('#np2', newpw); p.click('#b2')
            p.wait_for_url('**/*.html*', timeout=8000); time.sleep(0.6)
        # --- GV mặc định: không có tab Giao bài, không thấy nút thêm lớp
        pt, e1 = newpage(); login(pt, gv, 'gv1234', 'gvmoi123'); pt.goto(U('admin.html')); pt.wait_for_selector('#tabs button')
        tabs = pt.inner_text('#tabs'); chk('GV mặc định không có tab Giao bài', 'Giao bài' not in tabs and 'Học sinh' in tabs)
        pt.click('#tabs button[data-t=classes]'); chk('GV mặc định không có nút Thêm lớp / Sửa / Giao bài', pt.is_hidden('#addC') and 'Sửa' not in pt.inner_text('#tbC'))
        # --- admin cấp quyền qua giao diện
        pa, e2 = newpage(); login(pa, 'admin', 'Admin@123'); pa.goto(U('admin.html')); pa.wait_for_selector('#tabs button')
        pa.click('#tabs button[data-t=teachers]'); pa.wait_for_selector('#tbT button[data-a=tperm]'); pa.click('#tbT button[data-a=tperm]')
        pa.wait_for_selector('#tpl input'); chk('hộp quyền GV có 6 mục (gồm Toàn quyền)', pa.locator('#tpl input').count() == 6)
        pa.check('#tpl input[value=assign]'); pa.check('#tpl input[value=classes]'); pa.click('#tps'); pa.wait_for_function("document.querySelector('#tbT').innerText.indexOf('Giao bài')>=0")
        chk('bảng GV hiện quyền đã cấp', 'Quản lý lớp' in pa.inner_text('#tbT'))
        # --- GV đăng nhập lại -> có tab Giao bài + nút thêm lớp
        pt.reload(); pt.wait_for_selector('#tabs button'); pt.wait_for_timeout(2500); pt.wait_for_selector('#tabs button')
        chk('GV có quyền → thấy tab Giao bài', 'Giao bài' in pt.inner_text('#tabs'))
        pt.click('#tabs button[data-t=classes]'); chk('GV có quyền quản lý lớp → có nút Thêm lớp, Sửa', pt.is_visible('#addC') and 'Sửa' in pt.inner_text('#tbC'))
        # --- admin phong trưởng nhóm / phó nhóm qua giao diện
        pa.click('#tabs button[data-t=students]'); pa.wait_for_selector('#tbS button[data-a=rank]')
        def rank(name, val):
            row = pa.locator('#tbS tr', has_text=name); row.locator('button[data-a=rank]').click(); pa.wait_for_selector('#rpl input')
            pa.select_option('select[data-rc=QA]', val)
            pa.wait_for_timeout(100); n = pa.locator('#rpl input:checked').count(); pa.click('#rps'); pa.wait_for_function("!document.querySelector('#rpl')"); return n
        n1 = rank('Học Một', 'T'); n2 = rank('Học Hai', 'P')
        chk('chọn Trưởng nhóm tự tích 4 quyền, Phó nhóm 2 quyền', n1 == 4 and n2 == 2)
        chk('bảng HS hiện chức vụ', 'Trưởng nhóm' in pa.inner_text('#tbS') and 'Phó nhóm' in pa.inner_text('#tbS'))
        # --- học sinh thường: không có khu Nhóm
        ps, e3 = newpage(); login(ps, h3, 'hs1234', 'matkhau3'); ps.goto(U('me.html')); ps.wait_for_selector('#tb'); time.sleep(0.5)
        chk('HS thường không thấy khu Nhóm của tôi', ps.is_hidden('#nhom'))
        # --- học sinh 2 làm bài để có dữ liệu tiến độ
        tk = api({'action': 'auth_login', 'username': h3, 'password': 'matkhau3', 'device': 'x3'})
        # (login trên thiết bị khác bị chặn → dùng token trang ps)
        tok3 = ps.evaluate("JSON.parse(localStorage.getItem('gn_auth')).token")
        urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=json.dumps({'action': 'grade_save_result', 'token': tok3, 'set_id': 'lop11-u1-botro', 'page_id': 'doc', 'mode': 'practice', 'score': 7, 'total': 10, 'pct': 70, 'score10': 7}).encode(), method='POST')).read()
        # --- trưởng nhóm
        pl, e4 = newpage(); login(pl, h1, 'hs1234', 'matkhau1'); pl.goto(U('me.html')); pl.wait_for_selector('#nhom:not([hidden])'); pl.wait_for_selector('#nb tr td:nth-child(2)')
        chk('trưởng nhóm thấy khu Nhóm của tôi + 3 bạn', pl.is_visible('#nhom') and pl.locator('#nb tr').count() == 3)
        txt = pl.inner_text('#nb'); chk('bảng tiến độ: HS Ba đã nộp (có điểm 7), HS khác chưa nộp', '7' in pl.locator('#nb tr', has_text='Học Ba').inner_text() and 'chưa nộp' in pl.locator('#nb tr', has_text='Học Hai').inner_text())
        chk('trưởng nhóm có khung nhắc nộp + góp ý nhóm', pl.is_visible('#nrem') and pl.is_visible('#nfb'))
        pl.select_option('#nset', 'lop11-u1-botro'); pl.fill('#nnote', 'Nộp trước thứ 6'); pl.click('#nsend')
        pl.wait_for_timeout(800)
        pl.fill('#nfbt', 'Cả lớp xin lùi hạn'); pl.click('#nfbs'); pl.wait_for_selector('#nfbm div'); chk('trưởng nhóm gửi góp ý thay nhóm', 'lùi hạn' in pl.inner_text('#nfbm'))
        # --- phó nhóm: không có góp ý nhóm / không điểm
        pp, e5 = newpage(); login(pp, h2, 'hs1234', 'matkhau2'); pp.goto(U('me.html')); pp.wait_for_selector('#nhom:not([hidden])'); pp.wait_for_selector('#nb tr td:nth-child(2)')
        chk('phó nhóm không có khung góp ý nhóm', pp.is_hidden('#nfb') and pp.is_visible('#nrem'))
        chk('phó nhóm không thấy điểm (chỉ ✓ n trang)', '· 7' not in pp.locator('#nb tr', has_text='Học Ba').inner_text())
        # --- HS 3 thấy lời nhắc
        pp.wait_for_selector('#nhac:not([hidden])'); chk('HS chưa nộp được nhắc: thẻ Nhắc nhở có lời nhắn', 'Nộp trước thứ 6' in pp.inner_text('#nhacl') and 'Trưởng nhóm' in pp.inner_text('#nhacl'))
        ps.goto(U('me.html')); ps.wait_for_selector('#tb'); time.sleep(0.5); chk('HS đã nộp không bị nhắc', ps.is_hidden('#nhac'))
        # --- GV thấy góp ý của nhóm (lớp phụ trách)
        pt.click('#tabs button[data-t=fb]'); pt.wait_for_selector('.fbi'); chk('GV thấy góp ý thay nhóm', 'Góp ý của nhóm' in pt.inner_text('#fbl'))
        chk('không lỗi JS', not (e1 + e2 + e3 + e4 + e5))
        if e1 + e2 + e3 + e4 + e5: print((e1 + e2 + e3 + e4 + e5)[:3])
        br.close()
finally:
    srv.terminate()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI: %d/%d' % (res.count(False), len(res)))
raise SystemExit(0 if all(res) else 1)
