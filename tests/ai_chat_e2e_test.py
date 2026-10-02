# -*- coding: utf-8 -*-
"""Khung Hỏi · Góp ý ở mọi trang (kể cả trang chủ), gửi tin hiện ngay, trợ lý AI (khoá khi đang làm kiểm tra), tab Trợ lý AI của admin."""
import os, subprocess, time, json, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT, WEB = 8787, 8788
srv = subprocess.Popen(['node', os.path.join(ROOT, 'tests/gas_server.js'), str(PORT)], stdout=subprocess.PIPE, env=dict(os.environ, AI_FAKE='1')); srv.stdout.readline()
web = subprocess.Popen(['python3', '-m', 'http.server', str(WEB), '--bind', '127.0.0.1'], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
res = []
def chk(n, ok): res.append(bool(ok)); print('OK  ' if ok else 'FAIL', n)
def api(d):
    r = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=json.dumps(d).encode(), method='POST'); return json.loads(urllib.request.urlopen(r).read())
def route(r):
    req = r.request
    if req.method == 'OPTIONS': r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'}); return
    resp = r.fetch(url='http://127.0.0.1:%d/exec' % PORT, method=req.method, headers={'content-type': 'text/plain'}, post_data=req.post_data)
    r.fulfill(status=200, body=resp.body(), headers={'access-control-allow-origin': '*', 'content-type': 'text/plain'})
U = lambda p: 'http://127.0.0.1:%d/%s' % (WEB, p)
def setdelay(ms): urllib.request.urlopen('http://127.0.0.1:%d/delay?ms=%d' % (PORT, ms))
try:
    LA = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'}); A = LA['token']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': 'AI', 'name': 'AI', 'grade': 10}})
    hs = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Em Hỏi AI', 'classes': ['AI'], 'password': 'hs1234'}})['user']['username']
    api({'action': 'adm_assign_save', 'token': A, 'cls': 'AI', 'sets': ['lop10-u1-luyentap', 'ielts-rd-test02']})
    LH = api({'action': 'auth_login', 'username': hs, 'password': 'hs1234', 'device': 'h'})
    # mật khẩu tạm → đổi để dùng được token
    api({'action': 'auth_change_password', 'token': LH['token'], 'old_password': 'hs1234', 'new_password': 'matkhau5'})
    LH = api({'action': 'auth_login', 'username': hs, 'password': 'matkhau5', 'device': 'h'})
    with sync_playwright() as pw:
        br = pw.chromium.launch(); errs = []
        def newctx(L):
            c = br.new_context(viewport={'width': 1300, 'height': 850}); c.route('**/script.google.com/**', route)
            c.add_init_script("localStorage.removeItem('gn_ping'); localStorage.setItem('gn_auth', %s)" % json.dumps(json.dumps({'token': L['token'], 'user': L['user']})))
            p = c.new_page(); p.on('pageerror', lambda e: errs.append(str(e))); p.on('dialog', lambda d: d.accept()); return p
        p = newctx(LH)
        # --- nút ở trang chủ + menu
        p.goto(U('index.html')); p.wait_for_selector('.gnfb-btn')
        chk('trang chủ có nút "Hỏi · Góp ý" nổi', p.is_visible('.gnfb-btn') and 'Góp ý' in p.inner_text('.gnfb-btn'))
        chk('thanh menu có liên kết "💬 Góp ý" rõ chữ', 'Góp ý' in p.inner_text('.gn-links'))
        # --- gửi tin hiện ngay dù máy chủ chậm
        setdelay(1500)
        p.click('.gnfb-btn'); p.click('.gnfb-box textarea'); p.keyboard.type('Cô ơi cho em hỏi bài tập về nhà')
        t0 = time.time(); p.click('.gnfb-go'); p.wait_for_function("document.querySelector('.gnfb-l').innerText.indexOf('Cô ơi cho em hỏi')>=0"); dt = time.time() - t0
        chk('bấm Gửi: tin hiện ngay (%.2fs) với trạng thái đang gửi' % dt, dt < 0.5 and 'đang gửi' in p.inner_text('.gnfb-l'))
        p.wait_for_function("document.querySelector('.gnfb-l').innerText.indexOf('đang gửi')<0", timeout=8000)
        chk('sau khi máy chủ nhận: bỏ trạng thái đang gửi, không nhân đôi tin', p.inner_text('.gnfb-l').count('Cô ơi cho em hỏi') == 1)
        setdelay(0)
        inbox = json.dumps(api({'action': 'fb_inbox', 'token': A}), ensure_ascii=False)
        chk('admin thấy góp ý chung trong hộp thư', 'general' in inbox and 'Cô ơi' in inbox)
        # --- chưa được cấp quyền AI: chỉ góp ý
        chk('chưa cấp quyền: không có tab AI, nút chỉ ghi "Góp ý"', not p.is_visible('.gnfb-tabs') and p.inner_text('.gnfb-btn').strip().startswith('💬 Góp ý') and 'Hỏi' not in p.inner_text('.gnfb-btn'))
        chk('chưa cấp quyền: máy chủ từ chối ai_chat', 'chưa được giáo viên cấp quyền' in api({'action': 'ai_chat', 'token': LH['token'], 'text': 'x'}).get('error', ''))
        api({'action': 'adm_user_ai', 'token': A, 'usernames': [hs], 'on': True})
        (p.evaluate("localStorage.removeItem('gn_ping')"), p.reload()); p.wait_for_selector('.gnfb-btn'); p.wait_for_function("document.querySelector('.gnfb-btn').innerText.indexOf('Hỏi')>=0", timeout=8000)
        p.click('.gnfb-btn') if not p.is_visible('.gnfb-box') else None
        chk('được cấp quyền: hiện 2 tab (Giáo viên + Trợ lý AI)', p.is_visible('.gnfb-tabs') and p.is_visible('.gnfb-tabs button[data-t=a]') and p.is_visible('.gnfb-tabs button[data-t=t]'))
        # --- AI
        p.click('.gnfb-tabs button[data-t=a]'); p.wait_for_function("document.querySelector('.gnfb-sub').innerText.indexOf('Còn')>=0")
        chk('tab AI hiện số lượt còn lại', 'Còn 50' in p.inner_text('.gnfb-sub'))
        setdelay(1200)
        p.click('.gnfb-box textarea'); p.keyboard.type('Giải thích thì hiện tại hoàn thành'); t0 = time.time(); p.click('.gnfb-go')
        p.wait_for_function("document.querySelector('.gnfb-l').innerText.indexOf('Giải thích thì')>=0"); chk('câu hỏi AI hiện ngay + báo đang trả lời (%.2fs)' % (time.time() - t0), time.time() - t0 < 0.5 and 'đang trả lời' in p.inner_text('.gnfb-l'))
        p.wait_for_function("document.querySelector('.gnfb-l').innerText.indexOf('AI trả lời')>=0", timeout=8000); setdelay(0)
        chk('trợ lý AI trả lời + đếm lượt (còn 49)', 'Còn 49' in p.inner_text('.gnfb-sub') and 'Trợ lý AI' in p.inner_text('.gnfb-l'))
        (p.evaluate("localStorage.removeItem('gn_ping')"), p.reload()); p.wait_for_selector('.gnfb-btn'); p.click('.gnfb-btn'); p.click('.gnfb-tabs button[data-t=a]'); time.sleep(0.5)
        chk('tải lại trang: cuộc trò chuyện AI còn nguyên', 'Giải thích thì' in p.inner_text('.gnfb-l'))
        # --- khoá khi đang làm kiểm tra, mở sau khi nộp
        p.goto(U('WebBaiTap/Lop10/Unit1/luyentap/kiem-tra-15.html')); p.wait_for_selector('.gnfb-btn')
        if p.locator('#startBtn').is_visible(): p.click('#startBtn'); time.sleep(1)
        p.click('.gnfb-btn'); p.click('.gnfb-tabs button[data-t=a]'); time.sleep(0.5)
        p.wait_for_function("document.querySelector('.gnfb-sub').innerText.indexOf('chỉ mở')>=0")
        chk('đang làm kiểm tra: AI bị khoá', 'chỉ mở sau khi bạn nộp bài' in p.inner_text('.gnfb-sub') and p.is_disabled('.gnfb-box textarea'))
        p.click('.gnfb-x'); p.click('#submit'); p.wait_for_selector('#resultModal', state='visible'); time.sleep(1)
        p.click('.gnfb-btn'); p.click('.gnfb-tabs button[data-t=a]'); time.sleep(0.5)
        p.wait_for_function("document.querySelector('.gnfb-sub').innerText.indexOf('chỉ mở')<0")
        chk('nộp bài xong: AI mở lại', not p.is_disabled('.gnfb-box textarea'))
        p.click('.gnfb-box textarea'); p.keyboard.type('Giải thích chi tiết câu 1 giúp mình'); p.click('.gnfb-go')
        p.wait_for_function("document.querySelector('.gnfb-l').innerText.indexOf('|ctx=')>=0", timeout=8000)
        import re as _re
        m_ = _re.search(r'\|ctx=(\d+)', p.inner_text('.gnfb-l')); chk('AI nhận được nội dung trang bài (ctx=%s ký tự)' % (m_.group(1) if m_ else '?'), m_ and int(m_.group(1)) > 1500)
        p.goto(U('WebBaiTap/Lop10/Unit1/luyentap/' + os.listdir(os.path.join(ROOT, 'WebBaiTap/Lop10/Unit1/luyentap'))[0])); p.wait_for_selector('.gnfb-btn')
        if p.locator('#submit').count():
            p.click('.gnfb-btn'); p.click('.gnfb-tabs button[data-t=a]'); time.sleep(0.5)
            chk('trang luyện tập chưa nộp: AI cũng khoá', p.is_disabled('.gnfb-box textarea'))
        p.goto(U('WebBaiTap/IELTS/Reading/FullTest/Test2_Reading.html')); p.wait_for_selector('.gnfb-btn')
        p.click('.gnfb-btn'); p.click('.gnfb-tabs button[data-t=a]'); time.sleep(0.5)
        chk('IELTS chưa nộp bài: AI khoá', p.is_disabled('.gnfb-box textarea') and 'chỉ mở sau khi' in p.inner_text('.gnfb-sub'))
        p.evaluate("document.getElementById('submitBtn').click()"); time.sleep(2)
        p.evaluate("document.querySelectorAll('button').forEach(function(b){ if(/Nộp|Xác nhận|Đồng ý|OK/i.test(b.textContent) && b.offsetParent && b.id!=='submitBtn' && !b.closest('.gnfb-box')) b.click() })"); time.sleep(1.5)
        (None if p.is_visible('.gnfb-box') else p.click('.gnfb-btn')); p.click('.gnfb-tabs button[data-t=a]'); time.sleep(0.6)
        chk('IELTS nộp bài xong: AI mở', not p.is_disabled('.gnfb-box textarea'))
        # --- admin
        pa = newctx(LA); pa.goto(U('admin.html#ai')); pa.wait_for_selector('#tbAI tr'); time.sleep(0.8)
        chk('admin: tab Trợ lý AI báo đã có khoá + nhật ký có câu hỏi', 'Đã có khoá' in pa.inner_text('#aiSt') and 'Giải thích thì hiện tại hoàn thành' in pa.inner_text('#tbAI') and 'sk-test' not in pa.content())
        pa.fill('#aiLim', '5'); pa.click('#aiSave'); pa.wait_for_function("document.querySelector('#msg').innerText.indexOf('Đã lưu')>=0")
        chk('admin lưu giới hạn 5 lượt', api({'action': 'adm_ai_get', 'token': A})['limit'] == 5)
        api({'action': 'adm_user_ai', 'token': A, 'usernames': [hs], 'on': False})
        pa.evaluate("Object.keys(localStorage).filter(function(k){return k.indexOf('gn_adm_')===0}).forEach(function(k){localStorage.removeItem(k)})"); pa.goto(U('admin.html#students')); pa.reload(); pa.wait_for_selector('#tbS button[data-a=ai]'); pa.click('#tbS button[data-a=ai]')
        pa.wait_for_function("document.querySelector('#tbS').innerText.indexOf('AI')>=0 && document.querySelector('#tbS button[data-a=ai]').innerText.indexOf('Thu AI')>=0")
        time.sleep(0.8); chk('admin bấm "Cấp AI" ở danh sách học sinh → máy chủ ghi nhận', any(u['username'] == hs and u.get('ai') for u in api({'action': 'adm_users', 'token': A, 'role': 'student'})['users']))
        pa.click('#aiRevoke'); pa.wait_for_function("document.querySelector('#tbS button[data-a=ai]').innerText.indexOf('Cấp AI')>=0"); time.sleep(0.8)
        chk('nút "Thu AI" hàng loạt thu quyền', not any(u['username'] == hs and u.get('ai') for u in api({'action': 'adm_users', 'token': A, 'role': 'student'})['users']))
        pt = newctx(api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a2'}))
        chk('không lỗi JS', not errs)
        if errs: print(errs[:3])
        br.close()
finally:
    srv.terminate(); web.terminate()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI: %d/%d' % (res.count(False), len(res)))
raise SystemExit(0 if all(res) else 1)
