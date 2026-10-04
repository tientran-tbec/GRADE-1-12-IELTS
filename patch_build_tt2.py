# -*- coding: utf-8 -*-
"""Vá build.py lần 2: học sinh Thử thách vào 'tt_home.html' (trang chủ lối tắt + bảng vinh danh) thay vì thẳng bản đồ. Chạy một lần (an toàn khi chạy lại)."""
import sys
s = open('build.py', encoding='utf8').read()
if 'tt_home.html' in s:
    print('build.py đã vá tt_home'); sys.exit(0)
a = 'location.replace("thuthach.html");return}'
assert s.count(a) == 1, s.count(a)
s = s.replace(a, 'location.replace("tt_home.html");return}')
b = 'nằm trong <a href=\\"thuthach.html\\">🗺 Lộ trình của em</a>'
assert s.count(b) == 1, s.count(b)
s = s.replace(b, 'nằm trong <a href=\\"tt_home.html\\">🏠 Trang chủ Thử thách</a>')
c = "'student.html', 'thuthach.html')"
assert s.count(c) == 1, s.count(c)
s = s.replace(c, "'student.html', 'thuthach.html', 'tt_home.html')")
open('build.py', 'w', encoding='utf8').write(s)
print('đã vá build.py (tt_home)')
