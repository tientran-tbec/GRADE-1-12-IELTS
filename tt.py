# -*- coding: utf-8 -*-
"""Chế độ THỬ THÁCH: sinh lộ trình học tuần tự từ các bộ bài đã build.
Gọi từ build.py:  tt.build(ROOT, done, ulabel, unum)  ->  {'paths': {mã_bộ_bài: mã_lộ_trình}, 'n': số lộ trình}
Ghi ra  thuthach/index.json  (bộ bài -> lộ trình)  và  thuthach/<mã>.json  (các chương, bước).
Mỗi bước: id = '<mã bộ>|<trang>', kind = theory | practice | test.  Thứ tự: trong mỗi Unit: Lý thuyết -> các trang luyện tập (đúng thứ tự thanh tab) -> các đề kiểm tra.
Muốn thêm lộ trình cho lớp/môn khác: thêm một dòng vào PATHS."""
import os, json, re

# id, tiêu đề, thư mục lớp (gdir), môn, ngưỡng mặc định
PATHS = [
    {'id': 'lop3', 'title': 'Tiếng Anh · Lớp 3', 'gdir': 'Lop3', 'subject': 'Tiếng Anh', 'grade': '3'},
    # 'order': thứ tự các chương (khoá theo unum); mục không có trong order (đề giữa/cuối kỳ, ôn tập, HSG…) KHÔNG nằm trong lộ trình -> học sinh vẫn làm tự do
    {'id': 'lop4', 'title': 'Tiếng Anh · Lớp 4', 'gdir': 'Lop4', 'subject': 'Tiếng Anh', 'grade': '4',
     'order': ['Start'] + [str(i) for i in range(1, 6)] + ['Review1'] + [str(i) for i in range(6, 11)] + ['Review2']
              + [str(i) for i in range(11, 16)] + ['Review3'] + [str(i) for i in range(16, 21)] + ['Review4']},
]
DEFAULTS = {'theory_min': 2, 'practice_pass': 80, 'test_pass': 75}   # phút đọc lý thuyết, % qua bài luyện tập, % qua bài kiểm tra


def _ukey(u):
    return (0, int(u)) if u.isdigit() else (1, u)


def build(root, done, ulabel, unum):
    out_dir = os.path.join(root, 'thuthach')
    os.makedirs(out_dir, exist_ok=True)
    for f in os.listdir(out_dir):
        if f.endswith('.json'):
            try: os.remove(os.path.join(out_dir, f))
            except OSError: pass
    index, n = {}, 0
    for P in PATHS:
        units = {}
        for e, S, pages in done:
            if e[3] != P['gdir']:
                continue
            units.setdefault(unum(e[4]), []).append((e, S, pages))
        chapters = []
        keys = sorted(units, key=_ukey)
        if P.get('order'):
            keys = [k for k in P['order'] if k in units]
        for u in keys:
            steps = []
            lt = [x for x in units[u] if not x[0][5].startswith('test')]
            ts = sorted([x for x in units[u] if x[0][5].startswith('test')], key=lambda x: x[0][5])
            title = None
            for e, S, pages in lt:
                sid, gdir, udir, slug = e[0], e[3], e[4], e[5]
                title = title or re.split(r'\s*[:–-]\s*Luyện tập', S['title'])[0].strip()
                base = 'WebBaiTap/%s/%s/%s/' % (gdir, udir, slug)
                if S.get('theory'):
                    steps.append({'id': sid + '|ly-thuyet', 'sid': sid, 'pid': 'ly-thuyet', 'kind': 'theory', 'title': 'Lý thuyết', 'url': base + 'ly-thuyet.html', 'n': 0})
                for pid, ptitle, mode, cnt in pages:
                    steps.append({'id': sid + '|' + pid, 'sid': sid, 'pid': pid, 'kind': 'test' if mode == 'test' else 'practice', 'title': ptitle, 'url': base + pid + '.html', 'n': cnt})
                index[sid] = P['id']
            for k, (e, S, pages) in enumerate(ts, 1):
                sid, gdir, udir, slug = e[0], e[3], e[4], e[5]
                base = 'WebBaiTap/%s/%s/%s/' % (gdir, udir, slug)
                for pid, ptitle, mode, cnt in pages:
                    steps.append({'id': sid + '|' + pid, 'sid': sid, 'pid': pid, 'kind': 'test', 'title': 'Kiểm tra %d' % k, 'url': base + pid + '.html', 'n': cnt})
                index[sid] = P['id']
            if steps:
                chapters.append({'id': 'u' + u, 'title': title or ulabel(u), 'steps': steps})
        if not chapters:
            continue
        doc = {'id': P['id'], 'title': P['title'], 'subject': P['subject'], 'grade': P['grade'], 'defaults': DEFAULTS, 'chapters': chapters}
        with open(os.path.join(out_dir, P['id'] + '.json'), 'w', encoding='utf8') as f:
            json.dump(doc, f, ensure_ascii=False, separators=(',', ':'))
        n += 1
    with open(os.path.join(out_dir, 'index.json'), 'w', encoding='utf8') as f:
        json.dump({'paths': index, 'defaults': DEFAULTS}, f, ensure_ascii=False, separators=(',', ':'))
    return {'paths': index, 'n': n}
