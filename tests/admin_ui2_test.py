# -*- coding: utf-8 -*-
"""Giao diện quản trị: giờ VN, GV nhiều lớp, bộ lọc Lớp, giao bài theo học sinh."""
import os, subprocess, time, json, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8796
srv = subprocess.Popen(['node', os.path.join(ROOT, 'tests/gas_server.js'), str(PORT)], stdout=subprocess.PIPE); srv.stdout.readline()
res = []
def chk(n, ok): res.append(bool(ok)); print('OK  ' if ok else 'FAIL', n)
def api(d):
    return json.loads(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=json.dumps(d).encode(), method='POST')).read())
def route(r):
    q = r.request
    if q.method == 'OPTIONS': r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'}); return
    rq = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=q.post_data.encode() if q.post_data else None, method=q.method)
    r.fulfill(status=200, body=urllib.request.urlopen(rq).read(), headers={'access-control-allow-origin': '*', 'content-type': 'text/plain'})
U = lambda p: 'file://' + os.path.join(ROOT, p)
try:
    A = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'})['token']
    for c, g in (('11A', 11), ('11B', 11), ('10A', 10), ('IE1', 'IELTS')): api({'action': 'adm_class_save', 'token': A, 'cls': {'id': c, 'name': 'Lớp ' + c, 'grade': g}})
    t1 = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Cô Lan', 'role': 'teacher'}})['user']['username']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': '10A', 'name': 'Lớp 10A', 'grade': 10, 'teacher': t1}})
    stu = {}
    for n in ('Hs Một', 'Hs Hai', 'Hs Ba'):
        r = api({'action': 'adm_user_save', 'token': A, 'user': {'name': n, 'classes': ['11A'], 'password': 'hs1234'}}); stu[n] = (r['user']['username'], r['password'])
    with sync_playwright() as pw:
        br = pw.chromium.launch(); c = br.new_context(viewport={'width': 1300, 'height': 900}); c.route('**/script.google.com/**', route)
        p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e)))
        p.goto(U('login.html')); p.fill('#u', 'admin'); p.fill('#p', 'Admin@123'); p.click('#b1'); p.wait_for_url('**/admin.html*'); p.wait_for_selector('#tabs button')
        chk('GNAuth.t: ISO → giờ VN dd/MM/yyyy HH:mm:ss', p.evaluate("GNAuth.t('2026-10-01T11:32:19.000Z')") == '01/10/2026 18:32:19' and p.evaluate("GNAuth.t('05/10/2026 08:00:00')") == '05/10/2026 08:00:00')
        # GV nhiều lớp
        p.click('#tabs button[data-t=teachers]'); p.wait_for_selector('#tbT button[data-a=tcls]'); p.click('#tbT button[data-a=tcls]'); p.wait_for_selector('#tcl')
        [p.check('#tcl input[value="%s"]' % x) for x in ('11A', '11B')]; chk('modal lớp phụ trách liệt kê đủ 4 lớp', p.eval_on_selector_all('#tcl input', 'e=>e.length') == 4)
        p.click('#tcs'); p.wait_for_function("document.getElementById('tbT').innerText.includes('11B')", timeout=8000)
        chk('GV hiện lớp phụ trách "10A, 11A, 11B"', all(x in p.inner_text('#tbT') for x in ('10A', '11A', '11B')))
        # bộ lọc lớp
        p.click('#tabs button[data-t=classes]'); p.wait_for_selector('#tbC tr')
        rows = lambda: p.eval_on_selector_all('#tbC tr', 'e=>e.map(x=>x.innerText)')
        chk('lớp: 4 dòng, hiện số lớp "4/4"', len(rows()) == 4 and '4/4' in p.inner_text('#cfc'))
        p.select_option('#cfg', '11'); chk('lọc khối 11 → 2 lớp', len(rows()) == 2)
        p.select_option('#cfg', 'IELTS'); chk('lọc khối IELTS → 1 lớp', len(rows()) == 1 and 'IE1' in rows()[0])
        p.select_option('#cfg', ''); p.select_option('#cft', '__none'); chk('lọc chưa có GV → IE1 + (11A? không)', 'IE1' in ' '.join(rows()) and '10A' not in ' '.join(rows()))
        p.select_option('#cft', t1); chk('lọc theo GV Cô Lan → 3 lớp (10A, 11A, 11B)', len(rows()) == 3)
        p.select_option('#cft', ''); p.select_option('#cfs', 'nostu'); chk('lọc chưa có học sinh → 10A, 11B, IE1', len(rows()) == 3 and '11A' not in ' '.join([r.split('\t')[0] for r in rows()]))
        p.select_option('#cfs', ''); p.fill('#cfq', '11'); chk('tìm "11" → 2 lớp', len(rows()) == 2); p.fill('#cfq', 'zzz'); chk('không khớp → thông báo', 'Không có lớp nào khớp' in p.inner_text('#tbC')); p.fill('#cfq', '')
        # sửa lớp nhiều GV
        t2 = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Thầy Bình', 'role': 'teacher'}})['user']['username']
        p.reload(); p.wait_for_selector('#tabs button'); p.click('#tabs button[data-t=classes]'); p.wait_for_selector('#tbC tr')
        p.click('#tbC tr:has-text("11A") button[data-a=edit]'); p.wait_for_selector('#ctc input')
        p.check('#ctc input[value="%s"]' % t2); p.click('#cf2 button:not(#cx)'); time.sleep(0.6)
        cl = {c['id']: c for c in api({'action': 'adm_classes', 'token': A})['classes']}
        chk('lớp 11A có 2 GV', set(cl['11A']['teacher'].split(',')) == {t1, t2})
        # giao bài theo học sinh
        p.click('#tabs button[data-t=assign]'); p.select_option('#acls', '11A'); p.wait_for_selector('#alist input[data-s]')
        p.check('#alist input[data-s="lop11-u1-botro"]'); p.check('#alist input[data-s="lop11-u2-botro"]')
        p.click('#alist button[data-u="lop11-u1-botro"]'); p.wait_for_selector('#psl')
        p.check('#psl input[value="%s"]' % stu['Hs Một'][0]); p.click('#pss'); time.sleep(0.2)
        chk('nút hiện "👥 1 HS"', '1 HS' in p.inner_text('#alist button[data-u="lop11-u1-botro"]') and 'Cả lớp' in p.inner_text('#alist button[data-u="lop11-u2-botro"]'))
        p.click('#asave'); time.sleep(0.6)
        got = api({'action': 'adm_assign_get', 'token': A, 'cls': '11A'})
        chk('đã lưu: u1 chỉ cho Hs Một, u2 cả lớp', got['users'] == {'lop11-u1-botro': [stu['Hs Một'][0]]} and set(got['sets']) == {'lop11-u1-botro', 'lop11-u2-botro'})
        lg = lambda n: api({'action': 'auth_login', 'username': stu[n][0], 'password': stu[n][1], 'device': 'd' + n})['user']['sets']
        chk('Hs Một thấy cả 2 bộ, Hs Hai chỉ thấy bộ cả lớp', set(lg('Hs Một')) == {'lop11-u1-botro', 'lop11-u2-botro'} and lg('Hs Hai') == ['lop11-u2-botro'])
        # mở lại tab giao bài vẫn giữ lựa chọn
        p.reload(); p.wait_for_selector('#tabs button'); p.click('#tabs button[data-t=assign]'); p.select_option('#acls', '11A'); p.wait_for_selector('#alist button[data-u]')
        chk('mở lại vẫn hiện "1 HS"', '1 HS' in p.inner_text('#alist button[data-u="lop11-u1-botro"]'))
        chk('không lỗi JS', not errs)
finally:
    srv.kill()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI')
raise SystemExit(0 if all(res) else 1)
