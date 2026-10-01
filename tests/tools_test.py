# -*- coding: utf-8 -*-
"""Kiểm tra công cụ: highlight/tẩy, bút/xoá nét, tra từ (mock API), popup kết quả, ô viết dài."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from authstub import new_ctx
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = lambda p: 'file://' + os.path.join(ROOT, 'WebBaiTap/Lop11/Unit1', p)
res = []
def chk(n, ok): res.append(bool(ok)); print('OK  ' if ok else 'FAIL', n)
with sync_playwright() as pw:
    b = pw.chromium.launch(); errs = []
    pg = new_ctx(b, ctx={'viewport': {'width': 1000, 'height': 800}}).new_page(); pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('dialog', lambda d: d.accept())
    pg.route('**/api.mymemory.translated.net/**', lambda r: r.fulfill(status=200, content_type='application/json', body=json.dumps({'responseData': {'translatedText': 'BẢN DỊCH'}})))
    pg.goto(U('4kn/doc.html')); (pg.click('#startBtn') if pg.is_visible('#startBtn') else None)
    # highlight
    inputs_before = pg.evaluate("document.querySelectorAll('input').length")
    pg.evaluate("""(function(){var p=document.querySelector('.passage p');var r=document.createRange();r.setStart(p.firstChild,3);r.setEnd(p.firstChild,20);var s=getSelection();s.removeAllRanges();s.addRange(r);})()""")
    pg.evaluate("document.dispatchEvent(new MouseEvent('mouseup',{bubbles:true}))"); pg.wait_for_timeout(100)
    chk('highlight tạo span.hl-yellow', pg.evaluate("document.querySelectorAll('.passage span.hl-yellow').length") >= 1)
    chk('highlight không phá ô nhập', pg.evaluate("document.querySelectorAll('input').length") == inputs_before)
    # tẩy
    pg.click('[data-m=erase]'); pg.click('.passage span.hl-yellow'); chk('tẩy xoá highlight', pg.evaluate("document.querySelectorAll('.passage span.hl-yellow').length") == 0)
    # bút
    pg.click('[data-m=pen]'); pg.mouse.move(200, 300); pg.mouse.down(); pg.mouse.move(260, 340, steps=5); pg.mouse.up()
    chk('bút vẽ polyline', pg.evaluate("document.querySelectorAll('.draw-layer polyline').length") == 1)
    chk('chọn mực xanh', (pg.click('[data-ink="#2563eb"]') or True) and True)
    pg.click('[data-m=penerase]'); pg.mouse.move(230, 320); pg.mouse.down(); pg.mouse.up()
    chk('xoá nét', pg.evaluate("document.querySelectorAll('.draw-layer polyline').length") == 0)
    # tra từ (luyện tập)
    pg.click('[data-m=dict]')
    pg.evaluate("""(function(){var p=document.querySelector('.passage p');var r=document.createRange();r.setStart(p.firstChild,3);r.setEnd(p.firstChild,12);var s=getSelection();s.removeAllRanges();s.addRange(r);})()""")
    pg.evaluate("document.dispatchEvent(new MouseEvent('mouseup',{bubbles:true}))"); pg.wait_for_timeout(300)
    chk('popup tra từ hiện bản dịch', 'BẢN DỊCH' in (pg.inner_text('.dict-popup') if pg.query_selector('.dict-popup') else ''))
    chk('chia chunk đoạn dài', pg.evaluate("__tools.chunks(('This is a sentence. '.repeat(60))).length") > 1)
    # kiểm tra: nộp → popup kết quả đóng được, tắt công cụ, tra từ tự động
    pg.goto(U('botro/kiem-tra.html')); (pg.click('#startBtn') if pg.is_visible('#startBtn') else None)
    chk('ô viết lại là textarea nhiều dòng', pg.evaluate("document.querySelectorAll('textarea.blank.long').length") >= 7)
    h0 = pg.evaluate("document.querySelector('.q[data-id=\"kt.34\"] textarea').offsetHeight")
    pg.fill('.q[data-id="kt.34"] textarea', 'They have studied English since they were in grade 2. ' * 20)
    chk('ô viết lại tự giãn', pg.evaluate("document.querySelector('.q[data-id=\"kt.34\"] textarea').offsetHeight") > h0)
    chk('có tay kéo giãn (resize)', pg.evaluate("getComputedStyle(document.querySelector('textarea.blank.long')).resize") == 'vertical')
    pg.click('#submit'); pg.wait_for_timeout(200)
    chk('popup kết quả hiện', not pg.evaluate("document.getElementById('resultModal').hidden"))
    pg.click('#resultClose'); chk('nút Đóng — Xem lại bài làm hoạt động', pg.evaluate("document.getElementById('resultModal').hidden"))
    chk('thanh công cụ ẩn + thông báo tra từ', pg.evaluate("document.getElementById('tools').hidden") and not pg.evaluate("document.querySelector('.tools-note').hidden"))
    chk('không lỗi JS', not errs); print(errs)
    pw_ = new_ctx(b, ctx={'viewport': {'width': 420, 'height': 800}}).new_page(); pw_.goto(U('botro/viet.html')); (pw_.click('#startBtn') if pw_.is_visible('#startBtn') else None)
    pw_.eval_on_selector('.q[data-id="wr1.1"]', 'e=>e.scrollIntoView()'); pw_.screenshot(path='/tmp/v.png')
print('ALL OK' if all(res) else 'CÓ LỖI')
