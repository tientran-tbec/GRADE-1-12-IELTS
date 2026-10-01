# -*- coding: utf-8 -*-
"""Mở cả 84 trang IELTS Reading (đăng nhập giả lập): không lỗi JS, hộp bắt đầu không có ô nhập, bấm Bắt đầu chạy được."""
import os, glob, sys, time
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from authstub import new_ctx
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = sorted(glob.glob(os.path.join(ROOT, 'WebBaiTap/IELTS/Reading/**/*.html'), recursive=True))
bad = []
with sync_playwright() as pw:
    br = pw.chromium.launch(); c = new_ctx(br, role='teacher', cls='IELTS1'); c.route('**/script.google.com/**', lambda r: r.fulfill(status=200, body='ok', headers={'access-control-allow-origin': '*'}))
    c.route('**/api.mymemory.translated.net/**', lambda r: r.abort())
    pg = c.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    for f in files:
        errs.clear()
        pg.goto('file://' + f); pg.wait_for_selector('#nameOverlay button', timeout=8000)
        ok = not pg.is_visible('#stuName') and 'GN_RD' in pg.content() and pg.evaluate('!!window.GN_RD && !!window.GNAuth')
        pg.click('#nameOverlay button'); time.sleep(0.15)
        ok = ok and not pg.is_visible('#nameOverlay') and not errs
        if not ok: bad.append((os.path.relpath(f, ROOT), list(errs)))
print(len(files), 'trang;', 'LỖI:' if bad else 'tất cả OK', bad[:5])
raise SystemExit(1 if bad else 0)
