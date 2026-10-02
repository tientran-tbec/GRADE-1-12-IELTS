# -*- coding: utf-8 -*-
"""Góp ý (chat HS↔GV), HS nhiều lớp, hạn nộp, tiến độ — chạy trên giao diện thật với backend = code.gs (mock Node)."""
import os, subprocess, time, json, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8794
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
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': 'M11', 'name': 'Lớp 11 M', 'grade': 11}})
    api({'action': 'adm_class_save', 'token': A, 'cls': {'id': 'MI', 'name': 'IELTS M', 'grade': 'IELTS'}})
    r = api({'action': 'adm_user_save', 'token': A, 'user': {'name': 'Võ Hai Lớp', 'classes': ['M11', 'MI'], 'password': 'hs1234'}}); un = r['user']['username']
    chk('API: HS thuộc 2 lớp', r['ok'] and r['user']['classes'] == ['M11', 'MI'])
    api({'action': 'adm_assign_save', 'token': A, 'cls': 'M11', 'sets': ['lop11-u1-botro']})
    api({'action': 'adm_assign_save', 'token': A, 'cls': 'MI', 'sets': ['ielts-rd-test01', 'ielts-rd-completion', 'ielts-rd-matching'], 'due': {'ielts-rd-test01': '2000-01-01', 'ielts-rd-completion': '2999-12-31'}})
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        def newpage(w=1200):
            c = br.new_context(viewport={'width': w, 'height': 900}); c.route('**/script.google.com/**', route)
            p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e))); p.on('dialog', lambda d: d.accept()); return p, errs
        pg, errs = newpage()
        pg.goto(U('login.html')); pg.fill('#u', un); pg.fill('#p', 'hs1234'); pg.click('#b1')
        pg.wait_for_selector('#np'); pg.fill('#op', 'hs1234'); pg.fill('#np', 'matkhau9'); pg.fill('#np2', 'matkhau9'); pg.click('#b2'); pg.wait_for_url('**/index.html*')
        pg.wait_for_selector('.setcard:not([hidden])'); time.sleep(0.4)
        txt = pg.inner_text('main')
        chk('tiêu đề trang chủ GRADE 1-12-IELTS', 'GRADE 1-12-IELTS' in pg.inner_text('.top') and pg.title() == 'GRADE 1-12-IELTS')
        hrefs = pg.eval_on_selector_all('.setcard:not([hidden]) .tile:not([hidden])', 'els=>els.map(e=>e.getAttribute("href"))')
        chk('HS 2 lớp thấy bài cả Lớp 11 lẫn IELTS', any('Unit1/botro' in h for h in hrefs) and any('Test1_Reading' in h for h in hrefs) and any('/Completion/' in h for h in hrefs))
        chk('bài chưa giao (Test 2) không hiện', not any('Test2_Reading' in h for h in hrefs))
        exp = pg.eval_on_selector_all('.tile.expired', 'els=>els.map(e=>e.innerText)')
        chk('Test 1 quá hạn hiện "Hết hạn" + bị khoá', len(exp) == 1 and 'Hết hạn' in exp[0] and '01/01' in exp[0])
        chk('Completion còn hạn hiện "Hạn 31/12"', 'Hạn 31/12' in txt)
        # trang bị quá hạn bị chặn
        pg.goto(U('WebBaiTap/IELTS/Reading/FullTest/Test1_Reading.html')); pg.wait_for_url('**/index.html?denied=1*'); chk('mở thẳng bài quá hạn → bị đẩy về index', True)
        # góp ý trên trang luyện tập
        pg.goto(U('WebBaiTap/Lop11/Unit1/botro/doc.html')); pg.wait_for_selector('.gnfb-btn')
        chk('trang luyện tập có nút Góp ý', pg.is_visible('.gnfb-btn'))
        pg.click('.gnfb-btn'); pg.fill('.gnfb-box textarea', 'Câu 5 em thấy có 2 đáp án đúng ạ'); pg.click('.gnfb-go'); pg.wait_for_selector('.gnfb-m.me')
        chk('HS gửi góp ý, hiện trong khung chat', 'Câu 5' in pg.inner_text('.gnfb-l'))
        # trang kiểm tra IELTS Completion cũng có nút
        pg.goto(U('WebBaiTap/IELTS/Reading/TheoDang/Completion/Test1_Passage1_Completion.html')); pg.wait_for_selector('.gnfb-btn')
        chk('trang IELTS có nút Góp ý', pg.is_visible('.gnfb-btn'))
        # GV (admin) trả lời qua giao diện
        pa, errs2 = newpage()
        pa.goto(U('login.html')); pa.fill('#u', 'admin'); pa.fill('#p', 'Admin@123'); pa.click('#b1'); pa.wait_for_url('**/admin.html*')
        pa.goto(U('admin.html#gopy')); pa.wait_for_selector('.fbi')
        chk('admin thấy cuộc trò chuyện chưa đọc', pa.is_visible('.fbi b.dot') and 'Võ Hai Lớp' in pa.inner_text('#fbl'))
        pa.click('.fbi'); pa.wait_for_selector('#fbr'); chk('mở cuộc trò chuyện thấy nội dung HS', 'Câu 5' in pa.inner_text('#fbt'))
        pa.fill('#fbr', 'Cô kiểm tra lại, cảm ơn em nhé'); pa.click('#fbs'); pa.wait_for_function("document.querySelectorAll('#fbm .fbm.tc').length>=1"); chk('admin gửi trả lời', True)
        chk('hết chấm đỏ sau khi đọc', not pa.is_visible('.fbi b.dot'))
        # HS thấy trả lời
        pg.goto(U('WebBaiTap/Lop11/Unit1/botro/doc.html')); pg.wait_for_selector('.gnfb-btn'); time.sleep(1.0)
        chk('HS thấy chấm đỏ tin trả lời', pg.evaluate("document.querySelector('.gnfb-btn').classList.contains('has')"))
        pg.click('.gnfb-btn'); pg.wait_for_selector('.gnfb-m.tc')
        chk('HS đọc được trả lời của GV', 'Cô kiểm tra lại' in pg.inner_text('.gnfb-l'))
        pg.goto(U('me.html#gopy')); pg.wait_for_selector('#fbl div'); chk('me.html liệt kê góp ý của tôi', 'doc' in pg.inner_text('#fbl').lower() or 'Unit' in pg.inner_text('#fbl'))
        # admin tạo HS 2 lớp bằng giao diện + giao bài có hạn + tiến độ
        pa.click('#tabs button[data-t=students]'); pa.wait_for_selector('#addS'); pa.click('#addS')
        pa.fill('#uname', 'Đỗ Hai Lớp UI'); [pa.check('#ucls input[value="%s"]' % c) for c in ('M11', 'MI')]; pa.click('#uf button:not(#ux)')
        pa.wait_for_selector('#cOk'); pa.click('#cOk'); time.sleep(0.4)
        chk('UI: học sinh hiện 2 lớp "M11, MI"', 'M11, MI' in pa.inner_text('#tbS'))
        pa.click('#tabs button[data-t=assign]'); pa.select_option('#acls', 'MI'); pa.wait_for_selector('#alist input[data-s]')
        pa.fill('#adue', '2999-06-30'); pa.click('#adueSet')
        chk('UI: giao bài hiện ô hạn cho bộ đã chọn', pa.eval_on_selector_all('#alist input[data-d]', 'els=>els.length') >= 3)
        pa.click('#asave'); time.sleep(0.6)
        got = api({'action': 'adm_assign_get', 'token': A, 'cls': 'MI'})
        chk('UI: đã lưu hạn 30/06/2999 cho bộ đã giao', got['due'].get('ielts-rd-matching') == '2999-06-30' and got['due'].get('ielts-rd-test01') == '2999-06-30')
        pa.click('#tabs button[data-t=progress]'); pa.wait_for_selector('#tbP tr td'); chk('tab Tiến độ có học sinh', 'Võ Hai Lớp' in pa.inner_text('#tbP'))
        chk('không lỗi JS (HS + admin)', not errs and not errs2)
finally:
    srv.kill()
print('ALL OK %d kiểm tra' % len(res) if all(res) else 'CÓ LỖI')
raise SystemExit(0 if all(res) else 1)
