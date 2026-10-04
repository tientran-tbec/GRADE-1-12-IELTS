# -*- coding: utf-8 -*-
"""Vá build.py: thêm chế độ Thử thách (tt.py). Chạy một lần:  python3 patch_build_tt.py   (an toàn khi chạy lại)"""
import re, sys
s = open('build.py', encoding='utf8').read()
if 'import tt' in s:
    print('build.py đã có Thử thách'); sys.exit(0)
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("import ly\n", "import ly\nimport tt\n")
# 1) trang chủ: học sinh ở chế độ Thử thách -> chuyển sang bản đồ lộ trình (?free=1 = xem bài tự do, ẩn các bài thuộc lộ trình)
TT_JS = r'''(function(){var A=window.GNAuth,u=A&&A.user&&A.user();if(!u||u.role!=="student"||u.tt!=="thuthach")return;fetch("thuthach/index.json").then(function(r){return r.json()}).then(function(ix){var P=ix.paths||{},mine=(u.sets||[]).filter(function(s){return P[s]});if(!mine.length)return;if(!/[?&]free=1/.test(location.search)){location.replace("thuthach.html");return}[].forEach.call(document.querySelectorAll("[data-sid]"),function(n){if(P[n.getAttribute("data-sid")])n.remove()});[].forEach.call(document.querySelectorAll(".setcard"),function(c){if(!c.querySelector(".tile"))c.remove()});var h=document.getElementById("hint");if(h)h.innerHTML="<b>🚀</b>Các bài thuộc lộ trình Thử thách nằm trong <a href=\"thuthach.html\">🗺 Lộ trình của em</a>.";window.gnApply&&window.gnApply()}).catch(function(){})})();'''
rep("""<script src="engine/feedback.js?v=%s"></script></body></html>'""", """<script>%s</script><script src="engine/feedback.js?v=%s"></script></body></html>'""")
m = re.search(r"% \(INDEX_JS\.replace\('@@LBL@@', json\.dumps\(UNIT_LABELS, ensure_ascii=False\)\), BV\)\)", s)
assert m, 'không thấy câu lệnh định dạng cuối của build_index'
s = s.replace(m.group(0), "% (INDEX_JS.replace('@@LBL@@', json.dumps(UNIT_LABELS, ensure_ascii=False)), TT_INDEX_JS, BV))")
rep("def build_index(done):", "TT_INDEX_JS = r'''" + TT_JS + "'''\n\n\ndef build_index(done):")
# 2) các trang trong site/
rep("for n in ('login.html', 'admin.html', 'me.html', 'student.html'):", "for n in ('login.html', 'admin.html', 'me.html', 'student.html', 'thuthach.html'):")
rep("        open(os.path.join(ROOT, n), 'w', encoding='utf8').write(t)\n\n\nif __name__", "        t = re.sub(r'(engine/[A-Za-z_]+\\.(?:js|css))\"', r'\\1?v=' + BV + '\"', t)   # chống cache cho mọi tệp engine (chưa có ?v=)\n        open(os.path.join(ROOT, n), 'w', encoding='utf8').write(t)\n\n\nif __name__")
# 3) sinh lộ trình
rep("        build_index(done)\n", "        TT = tt.build(ROOT, done, ulabel, unum)\n        print('Thử thách ->', TT['n'], 'lộ trình,', len(TT['paths']), 'bộ bài')\n        build_index(done)\n")
open('build.py', 'w', encoding='utf8').write(s)
print('đã vá build.py')
