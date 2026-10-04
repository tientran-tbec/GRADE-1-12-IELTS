# -*- coding: utf-8 -*-
"""Tab Thử thách ở trang quản trị: chế độ lớp / học sinh, tiến độ, mở khoá, cấu hình luật."""
import os, subprocess, time, json, re, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT, WEB = 8803, 8804
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
P = json.load(open(os.path.join(ROOT, 'thuthach/lop3.json'), encoding='utf8')); steps = [s for c in P['chapters'] for s in c['steps']]
SETS = list(json.load(open(os.path.join(ROOT, 'thuthach/index.json'), encoding='utf8'))['paths'])
def login(p, u, pw):
    p.goto(U('login.html')); p.fill('#u', u); p.fill('#p', pw); p.click('#b1'); time.sleep(2.5)
    if p.locator('#np').is_visible(): p.fill('#op', pw); p.fill('#np', 'matkhau5'); p.fill('#np2', 'matkhau5'); p.click('#b2'); time.sleep(2.5)
try:
    A = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'})['token']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': '3A', 'name': '3A', 'grade': 3}})
    g = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Co Ba', 'role': 'teacher'}}); gv, gpw = g['user']['username'], g['password']
    g2 = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Co Tu', 'role': 'teacher'}}); gv2, gpw2 = g2['user']['username'], g2['password']
    api({'action': 'adm_teacher_perms', 'token': A, 'username': gv, 'perms': ['mode']})
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': '3A', 'name': '3A', 'grade': 3, 'teacher': gv + ',' + gv2}})
    hs = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Em Bé Ba', 'classes': ['3A'], 'password': 'hs1234'}})['user']['username']
    api({'action': 'adm_assign_save', 'token': A, 'cls': '3A', 'sets': SETS})
    with sync_playwright() as pw:
        br = pw.chromium.launch(); c = br.new_context(viewport={'width': 1300, 'height': 900}); c.route('**/script.google.com/**', route)
        p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e))); p.on('dialog', lambda d: d.accept())
        login(p, gv, gpw)
        p.goto(U('admin.html#tt')); p.wait_for_selector('#ttc option', state='attached', timeout=15000); time.sleep(1)
        chk('GV có quyền mode thấy tab Thử thách', p.locator('#tabs button[data-t=tt]').count() == 1)
        chk('liệt kê học sinh của lớp', 'Em Bé Ba' in p.inner_text('#ttl'))
        p.select_option('#ttm', 'thuthach'); p.wait_for_function("document.querySelector('#ttmsg').innerText.indexOf('Đã lưu')>=0", timeout=10000); time.sleep(0.8)
        st = api({'action': 'auth_login', 'username': hs, 'password': 'hs1234', 'device': 'x'})
        chk('đặt lớp = Thử thách → học sinh nhận user.tt', st['user']['tt'] == 'thuthach'); api({'action': 'auth_logout', 'token': st['token']})
        chk('bảng hiện tiến độ 0/%d' % len(steps), ('0/%d' % len(steps)) in p.inner_text('#ttl'))
        p.select_option('.ttus', 'tudo'); time.sleep(1.2)
        L = api({'action': 'auth_login', 'username': hs, 'password': 'hs1234', 'device': 'y'}); chk('đặt riêng học sinh = Tự do', L['user']['tt'] == 'tudo'); api({'action': 'auth_logout', 'token': L['token']})
        p.select_option('.ttus', ''); time.sleep(1.2)
        # học sinh nộp vài bước qua API để có tiến độ
        H = api({'action': 'auth_login', 'username': hs, 'password': 'hs1234', 'device': 'z'})
        api({'action': 'tt_cfg_set', 'token': A, 'path': 'lop3', 'cfg': {'theory_min': 0, 'practice_pass': 80, 'test_pass': 75}})
        api({'action': 'tt_theory', 'token': H['token'], 'step': steps[0]['id'], 'event': 'start'}); api({'action': 'tt_theory', 'token': H['token'], 'step': steps[0]['id'], 'event': 'done'})
        urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=json.dumps({'action': 'grade_save_result', 'token': H['token'], 'set_id': steps[1]['sid'], 'page_id': steps[1]['pid'], 'mode': 'practice', 'score': 6, 'total': 10, 'pct': 60, 'score10': 6}).encode(), method='POST')).read()
        api({'action': 'auth_logout', 'token': H['token']})
        p.click('#ttr'); time.sleep(1.5)
        chk('tiến độ cập nhật: 1/%d, đang ở Từ vựng' % len(steps), ('1/%d' % len(steps)) in p.inner_text('#ttl') and 'Từ vựng' in p.inner_text('#ttl'))
        p.click('[data-det]'); p.wait_for_selector('#ttd table', timeout=10000)
        chk('chi tiết: bước Từ vựng "chưa đạt (tốt nhất 60%)"', 'chưa đạt (tốt nhất 60%)' in p.inner_text('#ttd'))
        p.locator('#ttd [data-act=pass] >> nth=0').click(); p.wait_for_function("document.querySelector('#ttd').innerText.indexOf('Giáo viên cho qua')>=0", timeout=10000)
        chk('GV cho qua → "Giáo viên cho qua"', 'Giáo viên cho qua' in p.inner_text('#ttd'))
        chk('tiến độ lớp tăng lên 2', ('2/%d' % len(steps)) in p.inner_text('#ttl'))
        p.locator('#ttd [data-act=revoke]').click(); time.sleep(1.2); chk('thu hồi quyền cho qua', 'Giáo viên cho qua' not in p.inner_text('#ttd'))
        # đặt lại nhiều bước (chọn) + hoàn tác
        p.locator('#ttd [data-act=pass] >> nth=0').click(); p.wait_for_function("document.querySelector('#ttd').innerText.indexOf('Giáo viên cho qua')>=0", timeout=10000); time.sleep(0.6)
        chk('có ô tick từng bước + chọn tất cả', p.locator('#ttd .ttck').count() == len(steps) and p.locator('#ttd .ttall').count() == 1 and p.locator('#ttrs').is_disabled())
        p.locator('#ttd .ttck').nth(0).check(); p.locator('#ttd .ttck').nth(1).check()
        chk('nút “Đặt lại bước đã chọn (2)”', p.locator('#ttrs').is_enabled() and p.inner_text('#ttsn') == '2')
        p.click('#ttrs'); p.wait_for_function("document.querySelector('#ttmsg').innerText.indexOf('Đã đặt lại 2')>=0", timeout=10000); time.sleep(1.0)
        chk('sau khi đặt lại: tiến độ 0/%d' % len(steps), ('0/%d' % len(steps)) in p.inner_text('#ttl'))
        chk('lịch sử có nút Hoàn tác', p.locator('#tth [data-undo]').count() >= 1)
        p.click('#tth [data-undo]'); p.wait_for_function("document.querySelector('#ttmsg').innerText.indexOf('Đã hoàn tác')>=0", timeout=10000); time.sleep(1.0)
        chk('hoàn tác → tiến độ lại 2/%d' % len(steps), ('2/%d' % len(steps)) in p.inner_text('#ttl'))
        p.click('#ttra'); p.wait_for_function("document.querySelector('#ttmsg').innerText.indexOf('Đã đặt lại')>=0", timeout=10000); time.sleep(1.0)
        chk('đặt lại tất cả → 0/%d' % len(steps), ('0/%d' % len(steps)) in p.inner_text('#ttl'))
        p.locator('#tth [data-undo]').first.click(); time.sleep(0.5); p.wait_for_function("document.querySelector('#ttmsg').innerText.indexOf('Đã hoàn tác')>=0", timeout=10000); time.sleep(1.5)
        chk('hoàn tác lần đặt lại tất cả', ('2/%d' % len(steps)) in p.inner_text('#ttl'))
        with p.expect_download(timeout=8000) as dl: p.click('#ttex')
        chk('tải bảng Excel (CSV) của lớp', dl.value.suggested_filename.endswith('.csv'))
        p.locator('#ttd [data-act=revoke]').first.click(); time.sleep(1.0)
        # cấu hình luật
        p.fill('#ttg input[data-k=practice_pass]', '70'); p.click('#ttg summary'); p.locator('#ttg input[data-skip]').nth(2).check(); p.click('#ttcs'); p.wait_for_function("document.querySelector('#ttcm').innerText.indexOf('Đã lưu')>=0", timeout=10000)
        cf = api({'action': 'tt_mode_get', 'token': A})['cfg']['lop3']; chk('lưu luật: ngưỡng 70, bỏ qua 1 bước', cf['practice_pass'] == 70 and len(cf['skip']) == 1)
        # GV không quyền mode
        c2 = br.new_context(viewport={'width': 1300, 'height': 900}); c2.route('**/script.google.com/**', route); q = c2.new_page(); q.on('pageerror', lambda e: errs.append(str(e)))
        login(q, gv2, gpw2); q.goto(U('admin.html#tt')); q.wait_for_selector('#ttc option', state='attached', timeout=15000); time.sleep(1)
        chk('GV không quyền: xem được tiến độ nhưng không đổi chế độ', q.locator('#ttm').is_disabled() and q.locator('.ttus').first.is_disabled() and 'Em Bé Ba' in q.inner_text('#ttl') and q.locator('#ttg').is_hidden())
        chk('không lỗi JS', not errs)
        if errs: print(errs[:4])
        br.close()
finally:
    srv.terminate(); web.terminate()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI: %d/%d' % (res.count(False), len(res)))
raise SystemExit(0 if all(res) else 1)
