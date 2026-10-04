# -*- coding: utf-8 -*-
"""Chế độ THỬ THÁCH: sinh lộ trình học tuần tự từ các bộ bài đã build.
Gọi từ build.py:  tt.build(ROOT, done, ulabel, unum, LY, IELTS)  ->  {'paths': {mã_bộ_bài: mã_lộ_trình}, 'n': số lộ trình}
Ghi ra  thuthach/index.json  (bộ bài -> lộ trình)  và  thuthach/<mã>.json  (các chương, bước).
Mỗi bước: id = '<mã bộ>|<trang>', kind = theory | practice | test.
Lộ trình theo Unit: trong mỗi Unit: (Lý thuyết -> các trang luyện tập) của từng bộ theo 'sets_order', rồi các đề kiểm tra.
Muốn thêm lộ trình cho lớp/môn khác: thêm một dòng vào PATHS (hoặc EXTRA cho nguồn đặc biệt như Lý, IELTS)."""
import os, json, re

DEFAULTS = {'theory_min': 2, 'practice_pass': 80, 'test_pass': 75}   # phút đọc lý thuyết, % qua bài luyện tập, % qua bài kiểm tra
SLUG_LABEL = {'luyentap': 'Luyện tập', 'botro': 'Bổ trợ', 'chuyensau': 'Chuyên sâu', '4kn': '4 kỹ năng', 'ontap': 'Ôn tập'}
UNITS = [str(i) for i in range(1, 21)]

# id, tiêu đề, thư mục lớp (gdir), môn
# 'order': thứ tự các chương (khoá theo unum); mục không có trong order (đề giữa/cuối kỳ, HSG…) KHÔNG nằm trong lộ trình -> vẫn làm tự do
# 'sets_order': thứ tự các bộ trong một Unit;  'titles': tên chương riêng;  'defaults': ngưỡng riêng cho lộ trình
PATHS = [
    {'id': 'lop3', 'title': 'Tiếng Anh · Lớp 3', 'gdir': 'Lop3', 'subject': 'Tiếng Anh', 'grade': '3'},
    {'id': 'lop4', 'title': 'Tiếng Anh · Lớp 4', 'gdir': 'Lop4', 'subject': 'Tiếng Anh', 'grade': '4',
     'order': ['Start'] + [str(i) for i in range(1, 6)] + ['Review1'] + [str(i) for i in range(6, 11)] + ['Review2']
              + [str(i) for i in range(11, 16)] + ['Review3'] + [str(i) for i in range(16, 21)] + ['Review4']},
    {'id': 'lop10', 'title': 'Tiếng Anh · Lớp 10', 'gdir': 'Lop10', 'subject': 'Tiếng Anh', 'grade': '10',
     'order': ['1', '2', '3'], 'sets_order': ['luyentap', 'botro', 'chuyensau']},
    {'id': 'lop11', 'title': 'Tiếng Anh · Lớp 11', 'gdir': 'Lop11', 'subject': 'Tiếng Anh', 'grade': '11',
     'order': ['1', '2', '3', 'MidTerm1'], 'sets_order': ['4kn', 'botro', 'ontap'], 'titles': {'MidTerm1': 'Mid-term 1 · Ôn tập & đề thi thử'}},
]
IELTS_DEFAULTS = {'theory_min': 2, 'practice_pass': 60, 'test_pass': 60}   # IELTS Reading khó hơn: qua bài từ 60% (giáo viên chỉnh được)


def _ukey(u):
    return (0, int(u)) if u.isdigit() else (1, u)


def _chap_title(S):
    return re.split(r'\s*[:–-]\s*Luyện tập|\s*:\s*Bài tập', S['title'])[0].strip()


def _build_units(P, done, ulabel, unum):
    units = {}
    for e, S, pages in done:
        if e[3] != P['gdir']:
            continue
        units.setdefault(unum(e[4]), []).append((e, S, pages))
    keys = sorted(units, key=_ukey)
    if P.get('order'):
        keys = [k for k in P['order'] if k in units]
    so = P.get('sets_order') or []
    chapters, index = [], {}
    for u in keys:
        steps = []
        lt = [x for x in units[u] if not x[0][5].startswith('test')]
        lt.sort(key=lambda x: so.index(x[0][5]) if x[0][5] in so else len(so))
        ts = sorted([x for x in units[u] if x[0][5].startswith('test')], key=lambda x: x[0][5])
        title = None
        multi = len(lt) > 1
        for e, S, pages in lt:
            sid, gdir, udir, slug = e[0], e[3], e[4], e[5]
            title = title or _chap_title(S)
            base = 'WebBaiTap/%s/%s/%s/' % (gdir, udir, slug)
            pre = (SLUG_LABEL.get(slug, slug) + ' · ') if multi else ''
            if S.get('theory'):
                steps.append({'id': sid + '|ly-thuyet', 'sid': sid, 'pid': 'ly-thuyet', 'kind': 'theory', 'title': 'Lý thuyết' + ((' · ' + SLUG_LABEL.get(slug, slug)) if multi else ''), 'url': base + 'ly-thuyet.html', 'n': 0})
            for pid, ptitle, mode, cnt in pages:
                steps.append({'id': sid + '|' + pid, 'sid': sid, 'pid': pid, 'kind': 'test' if mode == 'test' else 'practice', 'title': pre + ptitle, 'url': base + pid + '.html', 'n': cnt})
            index[sid] = P['id']
        for k, (e, S, pages) in enumerate(ts, 1):
            sid, gdir, udir, slug = e[0], e[3], e[4], e[5]
            base = 'WebBaiTap/%s/%s/%s/' % (gdir, udir, slug)
            for pid, ptitle, mode, cnt in pages:
                steps.append({'id': sid + '|' + pid, 'sid': sid, 'pid': pid, 'kind': 'test', 'title': 'Kiểm tra %d' % k, 'url': base + pid + '.html', 'n': cnt})
            index[sid] = P['id']
        if steps:
            chapters.append({'id': 'u' + u, 'title': (P.get('titles') or {}).get(u) or title or ulabel(u), 'steps': steps})
    return chapters, index


def _build_ly(LY):
    """Vật lí 11: mỗi bài = 1 chương: Lý thuyết -> trắc nghiệm -> đúng/sai -> trả lời ngắn (bỏ tự luận: chấm bằng AI, không tính %)."""
    chapters, index = [], {}
    base = 'WebBaiTap/%s/%s/' % tuple(LY.get('dirs') or ('Lop11', 'Ly'))
    for b in sorted(LY.get('tt') or [], key=lambda b: (b['bai'] == 0, b['bai'])):
        steps = []
        if b['theory']:
            pid = 'b%02d-ly-thuyet' % b['bai']
            steps.append({'id': b['sid'] + '|' + pid, 'sid': b['sid'], 'pid': pid, 'kind': 'theory', 'title': 'Lý thuyết', 'url': base + pid + '.html', 'n': 0})
        for pid, label, kind, cnt in b['pages']:
            part = pid.rsplit('-', 1)[1]
            multi = len([p for p in b['pages'] if p[2] == kind]) > 1
            steps.append({'id': b['sid'] + '|' + pid, 'sid': b['sid'], 'pid': pid, 'kind': 'practice', 'title': label + ((' ' + part) if multi else ''), 'url': base + pid + '.html', 'n': cnt})
        if steps:
            index[b['sid']] = 'lop11-ly'
            chapters.append({'id': 'ly%02d' % b['bai'], 'title': b['title'], 'steps': steps})
    return chapters, index


def _build_ielts(IE):
    """IELTS Reading: Theo dạng bài (từng dạng) rồi Full Test."""
    chapters, index = [], {}
    t = IE.get('tt') or {}
    for d in t.get('dang', []):
        steps = []
        for pid, title, url, q in d['pages']:
            steps.append({'id': d['sid'] + '|' + pid, 'sid': d['sid'], 'pid': pid, 'kind': 'practice', 'title': title, 'url': url, 'n': q})
        if steps:
            index[d['sid']] = 'ielts-reading'
            chapters.append({'id': 'd-' + d['code'], 'title': 'Dạng bài: ' + d['label'], 'steps': steps})
    steps = []
    for sid, pid, title, url, q in t.get('full', []):
        steps.append({'id': sid + '|' + pid, 'sid': sid, 'pid': pid, 'kind': 'test', 'title': title, 'url': url, 'n': q})
        index[sid] = 'ielts-reading'
    if steps:
        chapters.append({'id': 'full', 'title': 'Full Test (40 câu · 60 phút)', 'steps': steps})
    return chapters, index


def build(root, done, ulabel, unum, LY=None, IELTS=None):
    out_dir = os.path.join(root, 'thuthach')
    os.makedirs(out_dir, exist_ok=True)
    for f in os.listdir(out_dir):
        if f.endswith('.json'):
            try: os.remove(os.path.join(out_dir, f))
            except OSError: pass
    index, n = {}, 0
    docs = []
    for P in PATHS:
        ch, ix = _build_units(P, done, ulabel, unum)
        if ch: docs.append(({'id': P['id'], 'title': P['title'], 'subject': P['subject'], 'grade': P['grade'], 'defaults': dict(DEFAULTS, **(P.get('defaults') or {})), 'chapters': ch}, ix))
    if LY and LY.get('tt'):
        ch, ix = _build_ly(LY)
        if ch: docs.append(({'id': 'lop11-ly', 'title': 'Vật lí · Lớp 11', 'subject': 'Lý', 'grade': '11', 'defaults': dict(DEFAULTS), 'chapters': ch}, ix))
    if IELTS and IELTS.get('tt'):
        ch, ix = _build_ielts(IELTS)
        if ch: docs.append(({'id': 'ielts-reading', 'title': 'IELTS · Reading', 'subject': 'IELTS', 'grade': 'IELTS', 'defaults': dict(IELTS_DEFAULTS), 'chapters': ch}, ix))
    for doc, ix in docs:
        with open(os.path.join(out_dir, doc['id'] + '.json'), 'w', encoding='utf8') as f:
            json.dump(doc, f, ensure_ascii=False, separators=(',', ':'))
        index.update(ix); n += 1
    with open(os.path.join(out_dir, 'index.json'), 'w', encoding='utf8') as f:
        json.dump({'paths': index, 'defaults': DEFAULTS}, f, ensure_ascii=False, separators=(',', ':'))
    return {'paths': index, 'n': n}
