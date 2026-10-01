# -*- coding: utf-8 -*-
"""Smoke test: mở từng trang bài tập, điền ĐÁP ÁN ĐÚNG, nộp, kiểm tra 100% & không lỗi JS / file thiếu."""
import glob, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages = sorted(p for p in glob.glob(os.path.join(ROOT, 'WebBaiTap', '**', '*.html'), recursive=True) if not p.endswith('ly-thuyet.html'))
bad = 0
with sync_playwright() as pw:
    br = pw.chromium.launch()
    from authstub import new_ctx
    ctx = new_ctx(br)
    for f in pages:
        pg = ctx.new_page(); errs = []
        pg.on('pageerror', lambda e: errs.append('JS: %s' % e))
        pg.on('requestfailed', lambda r: errs.append('FAIL: %s' % r.url[-60:]) if not (r.url.endswith('.mp3') or 'script.google.com' in r.url or 'googleusercontent' in r.url) else None)
        pg.on('response', lambda r: errs.append('HTTP %d: %s' % (r.status, r.url[-60:])) if r.status >= 400 else None)
        pg.goto('file://' + f)
        info = pg.evaluate('window.QUIZ ? {mode:window.QUIZ.mode, n:window.QUIZ.order.length} : null')
        rel = os.path.relpath(f, ROOT)
        if not info:
            print('SKIP (không phải trang quiz):', rel); pg.close(); continue
        for u in pg.evaluate('Array.from(document.querySelectorAll("audio source,audio")).map(function(a){return a.getAttribute("src")||""}).filter(Boolean)'):
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), u))): errs.append('MISSING audio ' + u)
        pg.click('#startBtn')
        items = pg.evaluate('Object.keys(window.QUIZ.ANS)')
        for iid in items:
            a = pg.evaluate('window.QUIZ.ANS["%s"]' % iid); t = pg.evaluate('window.QUIZ.items["%s"].t' % iid)
            sel = '.q[data-id="%s"]' % iid
            if isinstance(a, list) and t != 'fill': a = a[0]   # nhiều đáp án chấp nhận → thử đáp án đầu
            if t in ('mcq', 'tf', 'tfng'):
                pg.eval_on_selector('%s input[value="%s"]' % (sel, a), 'e=>e.click()')
            elif t == 'fill':
                bl = a['blanks'] if isinstance(a, dict) else ([[a]] if isinstance(a, str) else [a])
                inputs = pg.query_selector_all(sel + ' [class~=blank]')
                for i, inp in enumerate(inputs):
                    if inp.is_disabled(): continue
                    inp.fill(bl[i][0])
                    if i == len(inputs) - 1: inp.press('Enter')
        if info['mode'] == 'test':
            pg.click('#submit')
        t = pg.evaluate('window.__quiz.tally()')
        # kiểm tra mọi câu có giải thích
        noexp = pg.evaluate('Object.keys(window.QUIZ.ANS).filter(function(k){return !window.QUIZ.EXP[k]})')
        ok = t['ok'] == t['total'] and not errs and not noexp
        bad += 0 if ok else 1
        print(('OK  ' if ok else 'FAIL'), rel, info['mode'], t, ('missing-exp=%s' % noexp if noexp else ''), errs[:3])
        if t['ok'] != t['total']:
            wrong = pg.evaluate('window.QUIZ.order.filter(function(k){return window.QUIZ.ANS[k]!==undefined && window.QUIZ.items[k].t!=="open" && !window.__quiz.isCorrect(k)})')
            print('   sai:', wrong[:20])
        pg.close()
    br.close()
sys.exit(1 if bad else 0)
