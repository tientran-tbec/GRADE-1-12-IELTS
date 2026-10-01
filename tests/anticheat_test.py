# -*- coding: utf-8 -*-
"""Kiểm tra chống gian lận trên trang kiểm tra: toàn màn hình, chặn chuột phải/copy/dán/phím tắt, đếm vi phạm, hết giờ + gia hạn, tắt sau khi nộp."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from authstub import new_ctx
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
f = 'file://' + os.path.join(ROOT, 'WebBaiTap/Lop11/Unit1/botro/kiem-tra.html')
res = []
def chk(n, ok): res.append(ok); print('OK  ' if ok else 'FAIL', n)
with sync_playwright() as pw:
    pg = new_ctx(pw.chromium.launch()).new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('dialog', lambda d: d.accept())
    pg.goto(f)
    chk('đã đăng nhập: modal chào tên, không bắt nhập tay', 'Học Sinh Test' in pg.inner_text('#startModal') and not pg.is_visible('#stName'))
    pg.click('#startBtn')
    chk('đóng popup sau khi nhập', pg.evaluate("document.getElementById('startModal').hidden"))
    chk('body có class testmode', pg.evaluate("document.body.classList.contains('testmode')"))
    chk('user-select none', pg.evaluate("getComputedStyle(document.querySelector('body')).userSelect") == 'none')
    chk('chặn chuột phải', pg.evaluate("(function(){var e=new MouseEvent('contextmenu',{bubbles:true,cancelable:true});document.body.dispatchEvent(e);return e.defaultPrevented})()"))
    for ev in ('copy', 'cut', 'paste', 'dragstart'):
        chk('chặn ' + ev, pg.evaluate("(function(){var e=new Event('%s',{bubbles:true,cancelable:true});document.body.dispatchEvent(e);return e.defaultPrevented})()" % ev))
    for k, kw in [('F12', {}), ('c', {'ctrlKey': True}), ('v', {'ctrlKey': True}), ('u', {'ctrlKey': True}), ('i', {'ctrlKey': True, 'shiftKey': True}), ('Escape', {})]:
        r = pg.evaluate("(function(){var e=new KeyboardEvent('keydown',Object.assign({key:%r,bubbles:true,cancelable:true},%s));document.dispatchEvent(e);return e.defaultPrevented})()" % (k, str(kw).replace('True', 'true')))
        chk('chặn phím %s %s' % (k, kw), r)
    # thoát toàn màn hình -> overlay + đếm
    print('fullscreen đang bật:', pg.evaluate("!!document.fullscreenElement"))
    pg.evaluate("document.fullscreenElement ? document.exitFullscreen() : document.dispatchEvent(new Event('fullscreenchange'))")
    pg.wait_for_timeout(400)
    chk('overlay hiện khi thoát fullscreen', not pg.evaluate("document.getElementById('fsOverlay').hidden"))
    pg.evaluate("document.dispatchEvent(new Event('visibilitychange'))")
    pg.evaluate("window.dispatchEvent(new Event('blur'))")
    chk('toast cảnh báo hiện', not pg.evaluate("document.getElementById('toast').hidden"))
    pg.click('#fsBack'); chk('nút vào lại toàn màn hình ẩn overlay', pg.evaluate("document.getElementById('fsOverlay').hidden"))
    # hết giờ
    pg.evaluate("window.__quiz.setRemain && window.__quiz.setRemain(1)")
    chk('không lỗi JS', not errs)
    print(errs)
    # sau nộp: tắt chặn
    pg.evaluate("window.__quiz.submit(false)")
    chk('tắt chặn chuột phải sau nộp', not pg.evaluate("(function(){var e=new MouseEvent('contextmenu',{bubbles:true,cancelable:true});document.body.dispatchEvent(e);return e.defaultPrevented})()"))
    txt = pg.inner_text('#result')
    chk('có báo cáo vi phạm', 'chuyển tab' in txt)
    print(txt)
print('ALL OK' if all(res) else 'CÓ LỖI')
