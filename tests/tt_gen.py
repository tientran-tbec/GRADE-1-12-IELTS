"""Dựng danh sách `done` giả từ các trang lớp 3 đã build (chỉ để kiểm thử khi không có nguồn units) rồi chạy tt.build."""
import os, sys, re, json, html as H
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); os.chdir(ROOT)
import tt
def unum(u): return u[4:] if u.startswith('Unit') else u
def ulabel(u): return 'Unit ' + u
done = []
base = os.path.join(ROOT, 'WebBaiTap', 'Lop3')
for udir in sorted(os.listdir(base)):
    for slug in sorted(os.listdir(os.path.join(base, udir))):
        d = os.path.join(base, udir, slug); files = sorted(os.listdir(d))
        first = open(os.path.join(d, files[0]), encoding='utf8').read()
        sid = re.search(r'window\.QUIZ=\{"setId": "([^"]+)"', first) or re.search(r'requireSet\("([^"]+)"', first)
        sid = sid.group(1)
        tabs = re.findall(r'<a href="([^"]+)\.html"(?: class="cur")?>([^<]+)</a>', re.search(r'<nav class="tabs">(.*?)</nav>', first).group(1))
        pages = []; theory = False
        for pid, title in tabs:
            if pid.startswith('..'): continue
            if pid == 'ly-thuyet': theory = True; continue
            t = open(os.path.join(d, pid + '.html'), encoding='utf8').read()
            m = re.search(r'window\.QUIZ=(\{.*?\});', t); q = json.loads(m.group(1)) if m else {}
            pages.append((pid, H.unescape(title), 'test' if q.get('mode') == 'test' else 'practice', len(q.get('order', []))))
        if not tabs:  # đề kiểm tra: một trang
            pid = files[0][:-5]; m = re.search(r'window\.QUIZ=(\{.*?\});', first); q = json.loads(m.group(1))
            pages = [(pid, 'Kiểm tra', 'test', len(q['order']))]
        title = re.search(r'<div class="sub">([^<]+)', first); title = H.unescape(title.group(1)) if title else sid
        S = {'id': sid, 'title': title.split('  ·')[0], 'theory': theory}
        done.append(((sid, '', '', 'Lop3', udir, slug), S, pages))
print(len(done), 'bộ lớp 3')
r = tt.build(ROOT, done, ulabel, unum); print(r['n'], 'lộ trình', len(r['paths']), 'bộ')
# trang đăng nhập / quản trị / điểm của tôi / bản đồ (chỉ để thử): thay giữ chỗ như build.build_site_pages
for n in ('login.html', 'admin.html', 'me.html', 'student.html', 'thuthach.html', 'tt_home.html'):
    f = os.path.join(ROOT, 'site', n)
    if not os.path.exists(f): continue
    t = open(f, encoding='utf8').read().replace('%GN_URL%', 'https://script.google.com/macros/s/TEST/exec').replace('%PAGES%', '{}').replace('%CATALOG%', '[]')
    t = re.sub(r'(engine/[A-Za-z_]+\.(?:js|css))"', r'\1?v=1"', t)
    open(os.path.join(ROOT, n), 'w', encoding='utf8').write(t)
