# -*- coding: utf-8 -*-
"""Trang Vật lí 11: KaTeX, trắc nghiệm, đúng/sai, trả lời ngắn, tự luận + AI gợi ý, GV duyệt, khung AI kéo to, đề kiểm tra."""
import os, subprocess, time, json, re, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT, WEB = 8793, 8794
srv = subprocess.Popen(['node', os.path.join(ROOT, 'tests/ly_server.js'), str(PORT)], stdout=subprocess.PIPE); srv.stdout.readline()
web = subprocess.Popen(['python3', '-m', 'http.server', str(WEB), '--bind', '127.0.0.1'], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
res = []
def chk(n, ok): res.append(bool(ok)); print('OK  ' if ok else 'FAIL', n)
def api(d):
    r = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=json.dumps(d).encode(), method='POST'); return json.loads(urllib.request.urlopen(r).read())
def get(path): return json.loads(urllib.request.urlopen('http://127.0.0.1:%d%s' % (PORT, path)).read())
def route(r):
    req = r.request
    if req.method == 'OPTIONS': r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'}); return
    rq = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=req.post_data.encode() if req.post_data else None, method=req.method)
    r.fulfill(status=200, body=urllib.request.urlopen(rq).read(), headers={'access-control-allow-origin': '*', 'content-type': 'text/plain'})
U = lambda p: 'http://127.0.0.1:%d/%s' % (WEB, p)
B = json.load(open(os.path.join(ROOT, 'ly_src/bank_final.json'), encoding='utf8'))
try:
    A = api({'action': 'auth_login', 'username': 'admin', 'password': 'Admin@123', 'device': 'a'})['token']
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': '11L', 'name': '11L', 'grade': 11}})
    hs = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Em Ly', 'classes': ['11L'], 'password': 'hs1234'}})['user']['username']
    sets = ['ly11-b01', 'ly11-kt-de1']
    api({'action': 'adm_assign_save', 'token': A, 'cls': '11L', 'sets': sets})
    api({'action': 'adm_user_ai', 'token': A, 'usernames': [hs], 'on': True})
    with sync_playwright() as pw:
        br = pw.chromium.launch(); c = br.new_context(viewport={'width': 1300, 'height': 850}); c.route('**/script.google.com/**', route)
        p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e))); p.on('dialog', lambda d: d.accept())
        p.goto(U('login.html')); p.fill('#u', hs); p.fill('#p', 'hs1234'); p.click('#b1'); p.wait_for_selector('#np'); p.fill('#op', 'hs1234'); p.fill('#np', 'matkhau5'); p.fill('#np2', 'matkhau5'); p.click('#b2'); p.wait_for_url('**/*.html*'); time.sleep(1)
        # ---- trắc nghiệm
        p.goto(U('WebBaiTap/Lop11/Ly/b01-tn-1.html')); p.wait_for_selector('.q'); time.sleep(1.5)
        chk('KaTeX vẽ công thức', p.locator('.katex').count() > 5)
        chk('không còn ký tự $ thô trong đề', '$' not in p.inner_text('.q >> nth=0'))
        it = [i for i in B['items'] if i['kind'] == 'mcq' and (i['bai'] or 0) == 1]
        p.locator('.q >> nth=0 >> label.opt >> nth=0').click(); time.sleep(0.5)
        chk('mcq: chọn xong hiện đáp án + lời giải', p.locator('.q >> nth=0 >> .exp').is_visible() and p.locator('.q >> nth=0 >> .exp .ans').inner_text().startswith(('✔', '✘')))
        chk('mcq: lời giải có công thức KaTeX', p.locator('.q >> nth=0 >> .exp .katex').count() >= 0)
        # đáp án đúng bằng khóa: tìm câu đầu và bấm đúng
        uid0 = p.locator('.q >> nth=1').get_attribute('data-id'); key1 = [i for i in B['items'] if i['uid'] == uid0][0]['ans']
        p.locator('.q >> nth=1 >> input[value="%s"]' % key1).check(force=True); time.sleep(0.4)
        chk('mcq: chọn đúng khóa → ✔', p.locator('.q >> nth=1 >> .exp .ans').inner_text().startswith('✔'))
        # ---- hỏi AI theo câu
        chk('có nút 🤖 AI giải bài', p.locator('.qtools button').count() > 10)
        p.locator('.q >> nth=2 >> .qtools button[data-k=solve]').click(); time.sleep(0.5)
        p.wait_for_function("document.querySelector('.gnfb-l').innerText.indexOf('Lời giải')>=0", timeout=15000)
        chk('AI chat mở & trả lời có công thức KaTeX', p.locator('.gnfb-m.ai .katex').count() >= 1)
        last = get('/last'); chk('AI nhận prompt vật lí + nội dung trang có BÀI LÀM CỦA HỌC SINH', 'BÀI LÀM CỦA HỌC SINH' in last['sys'] and 'ctx=có-bài-làm' in p.inner_text('.gnfb-l'))
        # ---- kéo to khung AI
        b0 = p.locator('.gnfb-box').bounding_box()
        g = p.locator('.gnfb-g[data-d=bl]').bounding_box()
        p.mouse.move(g['x'] + 8, g['y'] + 8); p.mouse.down(); p.mouse.move(g['x'] + 8 - 260, g['y'] + 8 + 20, steps=8); p.mouse.up()
        b1 = p.locator('.gnfb-box').bounding_box()
        chk('kéo góc dưới-trái: khung to ra (%d→%d rộng)' % (b0['width'], b1['width']), b1['width'] > b0['width'] + 200 and abs((b1['x'] + b1['width']) - (b0['x'] + b0['width'])) < 3)
        g = p.locator('.gnfb-g[data-d=tl]').bounding_box()
        p.mouse.move(g['x'] + 5, g['y'] + 5); p.mouse.down(); p.mouse.move(g['x'] + 5 - 50, g['y'] + 5 - 0, steps=4); p.mouse.up()
        sz = p.evaluate("localStorage.getItem('gn_fb_geo')"); chk('kích thước được nhớ', sz and json.loads(sz)['w'] > 500)
        p.click('.gnfb-x'); p.reload(); p.wait_for_selector('.gnfb-btn'); p.click('.gnfb-btn'); time.sleep(0.5)
        b2 = p.locator('.gnfb-box').bounding_box(); chk('tải lại trang: khung vẫn giữ cỡ to', abs(b2['width'] - json.loads(sz)['w']) < 3)
        p.click('.gnfb-mx'); time.sleep(0.3); b3 = p.locator('.gnfb-box').bounding_box(); chk('nút ⛶ phóng to gần hết màn hình', b3['height'] > 780 and b3['width'] > 900)
        p.click('.gnfb-mx'); time.sleep(0.3); b4 = p.locator('.gnfb-box').bounding_box(); chk('bấm lại thì thu về cỡ cũ', abs(b4['width'] - b2['width']) < 4)
        p.click('.gnfb-x')
        # ---- đúng / sai
        p.goto(U('WebBaiTap/Lop11/Ly/b01-ds-1.html')); p.wait_for_selector('.q'); time.sleep(1)
        uid = p.locator('.q >> nth=0').get_attribute('data-id'); a = [i for i in B['items'] if i['uid'] == uid][0]['ans']
        for i, ch in enumerate(a):
            p.locator('.q >> nth=0 >> label.opt:has(input[name="%s_%d"][value="%s"])' % (uid, i, ch)).click()
        p.locator('.q >> nth=0 >> button.chk').click(); time.sleep(0.5)
        chk('tf4: chọn đúng cả 4 ý → 1 điểm', '1 điểm' in p.locator('.q >> nth=0 >> .exp .ans').inner_text() and p.locator('.q >> nth=0 >> .tfr.right').count() == 4)
        uid = p.locator('.q >> nth=1').get_attribute('data-id'); a = [i for i in B['items'] if i['uid'] == uid][0]['ans']
        for i, ch in enumerate(a):
            want = ch if i < 2 else ('F' if ch == 'T' else 'T')
            p.locator('.q >> nth=1 >> label.opt:has(input[name="%s_%d"][value="%s"])' % (uid, i, want)).click()
        p.locator('.q >> nth=1 >> button.chk').click(); time.sleep(0.5)
        chk('tf4: đúng 2/4 ý → 0,25 điểm', '0,25 điểm' in p.locator('.q >> nth=1 >> .exp .ans').inner_text())
        # ---- trả lời ngắn
        p.goto(U('WebBaiTap/Lop11/Ly/b01-tln-1.html')); p.wait_for_selector('.q'); time.sleep(1)
        uid = p.locator('.q >> nth=0').get_attribute('data-id'); s = [i for i in B['items'] if i['uid'] == uid][0]
        p.fill('.q >> nth=0 >> input.numin', s['ans'] + ' ' + (s.get('unit') or '')); p.locator('.q >> nth=0 >> button.chk').click(); time.sleep(0.4)
        chk('short: nhập đáp án đúng (kèm đơn vị) → ✔ [%s]' % s['ans'], p.locator('.q >> nth=0 >> .exp .ans').inner_text().startswith('✔'))
        p.fill('.q >> nth=1 >> input.numin', '123456'); p.locator('.q >> nth=1 >> button.chk').click(); time.sleep(0.4)
        chk('short: sai → ✘', p.locator('.q >> nth=1 >> .exp .ans').inner_text().startswith('✘'))
        v = p.evaluate("[__quiz.numOk('0,07',{ans:'0,07',tol:0.03}), __quiz.numOk('0.0712',{ans:'0,07',tol:0.03}), __quiz.numOk('0,08',{ans:'0,07',tol:0.03}), __quiz.numOk('5',{ans:'5',tol:'exact'}), __quiz.numOk('5,01',{ans:'5',tol:'exact'}), __quiz.numOk('−25 cm/s',{ans:'-25',tol:0.01}), __quiz.numOk('2,5×10^-3',{ans:'0,0025',tol:0.01})]")
        chk('short: so sánh số (dấu phẩy/chấm, đơn vị, sai số, mũ 10)', v == [True, True, False, True, False, True, True])
        # ---- tự luận
        p.goto(U('WebBaiTap/Lop11/Ly/b01-tl-1.html')); p.wait_for_selector('.q'); time.sleep(1)
        p.fill('.q >> nth=0 >> textarea', 'x = A cos(wt + phi), thay số được x = 5 cm.')
        p.locator('.q >> nth=0 >> .sym button >> nth=0').click(); chk('chèn ký hiệu π', 'π' in p.input_value('.q >> nth=0 >> textarea'))
        p.locator('.q >> nth=0 >> .esub').click(); p.wait_for_selector('.q >> nth=0 >> .ea b', timeout=20000)
        chk('tự luận: hiện điểm AI gợi ý + chờ GV duyệt', 'AI gợi ý' in p.inner_text('.q >> nth=0 >> .essay-res') and 'giáo viên sẽ duyệt' in p.inner_text('.q >> nth=0 >> .essay-res'))
        chk('tự luận: hiện lời giải mẫu sau khi nộp', p.locator('.q >> nth=0 >> .exp').is_visible())
        rows = get('/dump').get('TuLuan', []); chk('tự luận: lưu vào tab TuLuan', len(rows) == 2 and rows[1][3] == hs)
        # GV duyệt
        gvr = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Co Ly', 'role': 'teacher'}}); gv, gpw = gvr['user']['username'], gvr['password']
        api({'action': 'adm_class_save', 'token': A, 'cls': {'id': '11L', 'name': '11L', 'grade': 11, 'teacher': gv}})
        T = api({'action': 'auth_login', 'username': gv, 'password': gpw, 'device': 'gv'})['token']
        lst = api({'action': 'ly_essay_list', 'token': T})['rows']; chk('GV thấy bài của lớp mình', len(lst) == 1)
        api({'action': 'ly_essay_review', 'token': T, 'id': lst[0]['id'], 'score': '0,5', 'comment': 'Cần ghi đơn vị.'})
        p.reload(); p.wait_for_selector('.q'); time.sleep(2)
        chk('tải lại trang: HS thấy điểm chính thức GV + bài đã nộp', 'Giáo viên đã chấm: 0,5' in p.inner_text('.q >> nth=0 >> .essay-res') and 'x = A cos' in p.input_value('.q >> nth=0 >> textarea'))
        # ---- đề kiểm tra
        p.goto(U('WebBaiTap/Lop11/Ly/kt-de1.html')); p.wait_for_selector('#startBtn'); time.sleep(1)
        p.click('#startBtn'); time.sleep(1.2)
        chk('đề kiểm tra: có đồng hồ', p.locator('#timer').is_visible() and ':' in p.inner_text('#timer'))
        p.click('.gnfb-btn'); time.sleep(0.5); p.click('.gnfb-tabs button[data-t=a]'); time.sleep(0.5)
        chk('đề kiểm tra: AI khoá khi đang làm', p.locator('.gnfb-box textarea').is_disabled())
        p.click('.gnfb-x')
        chk('đề kiểm tra: nút hỏi AI theo câu bị khoá', p.locator('.qtools button >> nth=0').is_disabled())
        p.locator('.q >> nth=0 >> label.opt >> nth=1').click(); p.locator('.q >> nth=1 >> label.opt >> nth=2').click()
        p.click('#lySubmit'); p.wait_for_selector('#resultModal', state='visible', timeout=20000); time.sleep(2)
        chk('đề kiểm tra: nộp bài → có điểm', '/' in p.inner_text('#resultBox .big'))
        sheet = get('/dump'); rr = sheet.get('Lop1-12_KetQua', []); chk('đề kiểm tra: kết quả được lưu', len(rr) >= 2 and rr[-1][4] == 'ly11-kt-de1')
        p.locator('#resultClose').click(); time.sleep(0.3)
        chk('sau nộp: nút hỏi AI mở', not p.locator('.qtools button >> nth=0').is_disabled())
        chk('đề kiểm tra: không lỗi JS', not errs)
        if errs: print(errs[:4])
        br.close()
finally:
    srv.terminate(); web.terminate()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI: %d/%d' % (res.count(False), len(res)))
raise SystemExit(0 if all(res) else 1)
