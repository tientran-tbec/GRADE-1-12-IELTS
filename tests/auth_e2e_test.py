# -*- coding: utf-8 -*-
"""E2E đăng nhập/quản lý: admin → lớp → giáo viên → học sinh → đổi MK → làm bài → xem điểm. Backend = code.gs chạy trong Node (mock)."""
import os, re, subprocess, time, json, urllib.request
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8791
srv = subprocess.Popen(['node', os.path.join(ROOT, 'tests/gas_server.js'), str(PORT)], stdout=subprocess.PIPE)
srv.stdout.readline()
res = []
def chk(n, ok): res.append(bool(ok)); print('OK  ' if ok else 'FAIL', n)
def route(r):
    req = r.request
    if req.method == 'OPTIONS': r.fulfill(status=204, headers={'access-control-allow-origin': '*', 'access-control-allow-headers': '*'}); return
    data = req.post_data.encode() if req.post_data else None
    rq = urllib.request.Request('http://127.0.0.1:%d/exec' % PORT, data=data, method=req.method)
    body = urllib.request.urlopen(rq).read()
    r.fulfill(status=200, body=body, headers={'access-control-allow-origin': '*', 'content-type': 'text/plain'})
U = lambda p: 'file://' + os.path.join(ROOT, p)
try:
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        def newpage(w=1200):
            c = br.new_context(viewport={'width': w, 'height': 900}); c.route('**/script.google.com/**', route)
            p = c.new_page(); errs = []; p.on('pageerror', lambda e: errs.append(str(e))); p.on('dialog', lambda d: d.accept()); return p, errs
        # 1) chưa đăng nhập → bị chuyển về login
        pg, errs = newpage()
        pg.goto(U('index.html')); pg.wait_for_url('**/login.html*'); chk('chưa đăng nhập: index → login', 'login.html' in pg.url)
        pg.goto(U('WebBaiTap/Lop11/Unit1/botro/doc.html')); pg.wait_for_url('**/login.html*'); chk('chưa đăng nhập: bài tập → login', 'login.html' in pg.url and 'next=' in pg.url)
        pg.goto(U('login.html')); pg.fill('#u', 'admin'); pg.fill('#p', 'sai'); pg.click('#b1'); pg.wait_for_function("document.getElementById('e1').textContent.length>0")
        chk('sai mật khẩu báo lỗi', 'Sai tài khoản' in pg.inner_text('#e1'))
        # 2) admin
        pg.fill('#p', 'Admin@123'); pg.click('#b1'); pg.wait_for_url('**/admin.html*'); chk('admin vào admin.html', True)
        pg.wait_for_selector('#tabs button')
        chk('admin có tab Giáo viên', 'Giáo viên' in pg.inner_text('#tabs'))
        pg.goto(U('WebBaiTap/Lop11/MidTerm1/test01/kiem-tra.html')); pg.wait_for_selector('#startBtn')
        
        chk('admin: không có ô nhập tên/lớp', not pg.is_visible('#stName') and not pg.is_visible('#stClass'))
        pg.click('#startBtn'); time.sleep(0.4)
        chk('admin: bấm bắt đầu không báo lỗi nhập tên/lớp', pg.inner_text('#stErr').strip() == '' and not pg.is_visible('#startModal'))
        pg.goto(U('WebBaiTap/Lop11/Unit1/botro/doc.html')); time.sleep(0.6)
        chk('admin: bài luyện tập vào thẳng, không hỏi', not pg.is_visible('#startModal'))
        pg.goto(U('admin.html')); pg.wait_for_selector('#tabs button')
        pg.click('#tabs button[data-t=classes]'); pg.click('#addC')
        pg.fill('#cid', '11A1'); pg.fill('#cnm', 'Lớp 11A1'); pg.fill('#cgr', '11'); pg.click('#cf2 button:not(#cx)'); pg.wait_for_selector('#tbC tr td b')
        chk('tạo lớp 11A1', '11A1' in pg.inner_text('#tbC'))
        pg.click('#tabs button[data-t=teachers]'); pg.click('#addT'); pg.fill('#uname', 'Nguyễn Thị Hoa'); pg.fill('#upw', 'gv1234'); pg.click('#uf button:not(#ux)')
        pg.wait_for_selector('#cOk'); chk('tạo GV hoa nt hiện mật khẩu', 'hoant' in pg.inner_text('#mbox') and 'gv1234' in pg.inner_text('#mbox')); pg.click('#cOk')
        pg.click('#tabs button[data-t=classes]'); pg.click('#tbC button[data-a=edit]'); pg.select_option('#ctc', 'hoant'); pg.click('#cf2 button:not(#cx)'); pg.wait_for_selector('#tbC td')
        pg.wait_for_function("document.querySelector('#tbC').innerText.includes('hoant')"); chk('gán GV cho lớp', True)
        pg.click('#tabs button[data-t=students]'); pg.click('#impS'); pg.select_option('#icls', '11A1')
        pg.fill('#itxt', 'Trần Văn An\nLê Thị Bình'); pg.click('#ig'); pg.wait_for_selector('#cOk')
        creds = pg.inner_text('#mbox'); chk('import 2 học sinh', 'antv' in creds and 'binhlt' in creds)
        pw_an = re.search(r'antv\s+(\S{6})', creds).group(1); pg.click('#cOk')
        chk('bảng học sinh có 2 dòng', pg.locator('#tbS tr').count() == 2)
        # 2b) giao bài cho lớp 11A1: chỉ Test 1 + Unit 1 bổ trợ
        pg.click('#tabs button[data-t=classes]'); pg.click('#tbC button[data-a=asg]'); pg.wait_for_selector('#alist input[data-s]')
        chk('giao bài: chỉ liệt kê bài khối 11', pg.locator('#alist input[data-s]').count() > 0)
        pg.check('#alist input[data-s="lop11-mt1-test01"]'); pg.check('#alist input[data-s="lop11-u1-botro"]'); pg.click('#asave')
        pg.wait_for_function("document.getElementById('msg').textContent.includes('Đã lưu giao bài')"); chk('lưu giao bài', True)
        # 3) đăng xuất
        pg.click('[data-gn=out]'); pg.wait_for_url('**/login.html*'); chk('đăng xuất', True)
        # 4) học sinh: đăng nhập lần đầu bắt đổi MK
        pg.fill('#u', 'antv'); pg.fill('#p', pw_an); pg.click('#b1'); pg.wait_for_selector('#fChange:not([hidden])')
        # thiết bị thứ 2 (context khác = localStorage khác) bị chặn
        pgx, ex = newpage(); pgx.goto(U('login.html')); pgx.fill('#u', 'antv'); pgx.fill('#p', pw_an); pgx.click('#b1')
        pgx.wait_for_function("document.getElementById('e1').textContent.length>0"); chk('thiết bị thứ 2 bị chặn', 'thiết bị khác' in pgx.inner_text('#e1'))
        chk('HS lần đầu bị bắt đổi MK', not pg.is_visible('#skip'))
        pg.fill('#op', pw_an); pg.fill('#np', 'matkhau9'); pg.fill('#np2', 'matkhau9'); pg.click('#b2'); pg.wait_for_url('**/index.html*'); chk('đổi MK → vào trang chủ', True)
        pg.wait_for_selector('.setcard:not([hidden])'); time.sleep(0.3)
        vis = pg.eval_on_selector_all('.setcard:not([hidden]) .tile:not([hidden])', 'els=>els.map(e=>e.getAttribute("href"))')
        chk('HS chỉ thấy bài được giao (Unit 1 bổ trợ + Test 1)', len(vis) > 0 and all(('Unit1/botro' in h) or ('test01' in h) for h in vis) and any('test01' in h for h in vis))
        chk('chip hiện tên + lớp', 'Trần Văn An' in pg.inner_text('.gn-chip') and '11A1' in pg.inner_text('.gn-chip'))
        chk('HS không có link Quản trị', 'Quản trị' not in pg.inner_text('.gn-chip'))
        pg.goto(U('admin.html')); pg.wait_for_url('**/index.html*'); chk('HS vào admin.html → bị đẩy về index', True)
        pg.goto(U('WebBaiTap/Lop11/Unit2/botro/doc.html')); pg.wait_for_url('**/index.html?denied=1*'); chk('HS vào bài chưa giao → bị đẩy về index', True)
        # 5) HS làm bài kiểm tra → server ghi theo danh tính token
        pg.goto(U('WebBaiTap/Lop11/MidTerm1/test01/kiem-tra.html')); pg.wait_for_selector('#startBtn')
        chk('modal chào đúng tên, không có ô nhập', 'Trần Văn An' in pg.inner_text('#startModal') and not pg.is_visible('#stName'))
        pg.click('#startBtn'); time.sleep(0.5)
        ans = pg.evaluate('window.QUIZ.ANS'); items = pg.evaluate('window.QUIZ.items')
        k = 0
        for iid, a in ans.items():
            if items[iid]['t'] == 'mcq':
                if isinstance(a, list): a = a[0]
                pg.eval_on_selector('.q[data-id="%s"] input[value="%s"]' % (iid, a), 'e=>e.click()'); k += 1
                if k >= 10: break
        pg.click('#submit'); pg.wait_for_selector('#resultModal', state='visible'); time.sleep(1)
        dump = json.loads(urllib.request.urlopen('http://127.0.0.1:%d/dump' % PORT).read())
        kq = dump.get('Lop1-12_KetQua', [])
        chk('server có dòng kết quả với tài khoản + tên + lớp từ token', len(kq) >= 2 and kq[-1][2] == 'Trần Văn An' and kq[-1][3] == '11A1' and kq[-1][-1] == 'antv')
        # 6) Điểm của tôi
        pg.goto(U('me.html')); pg.wait_for_selector('#tb tr td'); time.sleep(0.5)
        chk('Điểm của tôi có kết quả', 'lop11-mt1-test01' in pg.inner_text('#tb'))
        # 7) giáo viên: chỉ thấy lớp mình, kết quả HS
        pg2, e2 = newpage()
        pg2.goto(U('login.html')); pg2.fill('#u', 'hoant'); pg2.fill('#p', 'gv1234'); pg2.click('#b1'); pg2.wait_for_selector('#fChange:not([hidden])')
        pg2.fill('#op', 'gv1234'); pg2.fill('#np', 'gvmoi99'); pg2.fill('#np2', 'gvmoi99'); pg2.click('#b2'); pg2.wait_for_url('**/admin.html*')
        pg2.wait_for_selector('#tabs button'); chk('GV không có tab Giáo viên', 'Giáo viên' not in pg2.inner_text('#tabs'))
        pg2.wait_for_function("document.querySelectorAll('#tbS tr').length>=2"); chk('GV thấy 2 HS lớp mình', pg2.locator('#tbS tr').count() == 2)
        pg2.click('#tabs button[data-t=results]'); pg2.wait_for_selector('#tbR tr td'); time.sleep(0.5)
        chk('GV thấy kết quả của HS', 'Trần Văn An' in pg2.inner_text('#tbR'))
        # GV sửa thông tin HS trực tiếp trên web
        pg2.click('#tabs button[data-t=students]'); pg2.click('#tbS tr:has-text("antv") button[data-a=edit]'); pg2.fill('#uname', 'Trần Văn Ân'); pg2.click('#uf button:not(#ux)'); pg2.wait_for_function("document.getElementById('modal').hidden")
        pg2.wait_for_function("document.querySelector('#tbS').innerText.includes('Trần Văn Ân')"); chk('GV sửa tên HS trên web', True)
        chk('HS đang online hiện nhãn + nút đăng xuất thiết bị', 'Đang đăng nhập' in pg2.inner_text('#tbS'))
        pg2.click('#tbS tr:has-text("Trần Văn Ân") button[data-a=kick]'); pg2.wait_for_function("!document.querySelector('#tbS').innerText.includes('Đang đăng nhập')"); chk('GV đăng xuất thiết bị HS', True)
        pg.reload(); pg.wait_for_function("location.href.includes('login.html')"); chk('HS bị kick → trang tự về đăng nhập', 'msg=' in pg.url)
        pg2.click('#tabs button[data-t=students]'); pg2.click('#tbS button[data-a=reset] >> nth=0'); pg2.wait_for_selector('#cOk'); chk('GV đặt lại MK HS', len(re.findall(r'\b[a-z2-9]{6}\b', pg2.inner_text('#mbox'))) > 0); pg2.click('#cOk')
        chk('không lỗi JS', not errs and not e2)
        br.close()
finally:
    srv.terminate()
print('ALL OK' if all(res) else 'CÓ LỖI', len(res), 'kiểm tra')
raise SystemExit(0 if all(res) else 1)
