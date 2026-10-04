# -*- coding: utf-8 -*-
"""Vá build.py lần 3: (1) truyền dữ liệu Lý + IELTS cho tt.build; (2) học sinh Thử thách không có bài tự do thì không vào được giao diện tự do. Chạy một lần (an toàn khi chạy lại)."""
import sys
s = open('build.py', encoding='utf8').read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70])
    s = s.replace(a, b)
changed = False
if 'tt.build(ROOT, done, ulabel, unum, LY, IELTS)' not in s:
    rep('tt.build(ROOT, done, ulabel, unum)', 'tt.build(ROOT, done, ulabel, unum, LY, IELTS)'); changed = True
a = 'if(!/[?&]free=1/.test(location.search)){location.replace("tt_home.html");return}'
if a in s:
    rep(a, 'var fr=(u.sets||[]).filter(function(s){return !P[s]});if(!/[?&]free=1/.test(location.search)||!fr.length){location.replace("tt_home.html");return}'); changed = True
open('build.py', 'w', encoding='utf8').write(s)
print('đã vá build.py (lần 3)' if changed else 'build.py đã vá lần 3')
