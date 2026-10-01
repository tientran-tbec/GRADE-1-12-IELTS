"""Chuyển đổi 1 lần: Đề kiểm tra giữa HK1 Anh 11 (Đề 5) src/mt1/d5.txt -> units/mt1_test04.py (khung câu hỏi).
Đáp án + giải thích: units/mt1_test04_dapan.py (soạn tay, đối chiếu khoá ⟦…⟧ trong phần ĐÁP ÁN của Word).
Hàm build_test() dùng chung cho gen_mt1_test05.py."""
import re, sys, os, pprint
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import parse_mcq, cl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def keepu(s):
    s = re.sub(r'<u>(\s*)</u>', r'\1', s)
    s = re.sub(r'<u>(\s*)(.*?)(\s*)</u>', r'\1<u>\2</u>\3', s)       # bỏ khoảng trắng nằm trong thẻ gạch chân
    s = re.sub(r'</u>(\s*)<u>', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def load_question_part(src, fixes):
    raw = open(os.path.join(ROOT, src), encoding='utf8').read()
    raw = re.sub(r'<b>C\s*\.\s*</b>', '<b>C.</b>', raw)      # nguồn: "C ." làm mất phương án C
    raw = re.sub(r'<u>[\s\xa0]{5,}</u>', '______', raw)             # chỗ trống bị gạch chân rỗng (Q7 Đề 5)
    raw = re.sub(r'<u>[ \xa0]{1,4}</u>', ' ', raw)                 # khoảng trắng gạch chân ngắn -> dấu cách (cl() sẽ xoá mất)
    for a, b in fixes:
        raw = raw.replace(a, b)
    L = raw.split('\n')
    a = next(i for i, l in enumerate(L) if 'Mark the letter' in l)
    b = next(i for i, l in enumerate(L) if re.search(r'ĐÁP ÁN|LỜI GIẢI', l))
    return L[a:b]


def build_test(src, fixes, tid, title, img_dir, minutes, split_img, arrange):
    """split_img: {số câu đầu nhóm: tên ảnh}; arrange: tập số câu sắp xếp câu (stem xuống dòng)."""
    ev = parse_mcq(load_question_part(src, fixes), expect=1)
    groups, cur = [], None
    for kind, v in ev:
        if kind == 'instr':
            cur = {'id': 'g%d' % (len(groups) + 1), 'instr': v, 'items': []}
            groups.append(cur)
        elif kind == 'para':
            cur.setdefault('_p', []).append(v)
        else:
            cur['items'].append(v)
    out = []
    for g in groups:
        paras = g.pop('_p', [])
        pas = ''
        for p in paras:
            p = keepu(p)
            p = re.sub(r'\((\d+)\)\s*_*', r'<b>(\1) ______</b> ', p)
            p = re.sub(r'\s+([.,?!;:])', r'\1', re.sub(r'\s+', ' ', p)).strip()
            pas += '<p>%s</p>' % p
        g['passage'] = pas
        items = []
        for it in g.pop('items'):
            n = it['n']
            q = keepu(it['q'])
            if n in arrange:
                q = re.sub(r'\s+(?=[a-g][.)]\s)', '<br>', ' ' + q).strip().strip('<br>')
                q = q.replace('<br>', '<br>')
            if not q and g['passage']:
                q = 'Blank (%d)' % n
            q = re.sub(r'_{3,}', '______', q)
            o = [keepu(x) for x in it['o']]
            if n in arrange:
                o = [x.rstrip('.').strip() for x in o]
            assert len(o) == 4, (n, o)
            items.append({'id': '%s.%d' % (g['id'], n), 't': 'mcq', 'q': q, 'o': o})
        g['items'] = items
        out.append(g)
    # tách nhóm có ảnh (thông báo/quảng cáo) thành các nhóm con
    final = []
    for g in out:
        firsts = [it for it in g['items'] if int(it['id'].split('.')[-1]) in split_img]
        if not firsts:
            final.append(g)
            continue
        idx = [g['items'].index(it) for it in firsts] + [len(g['items'])]
        for k, (a, b) in enumerate(zip(idx, idx[1:])):
            n0 = int(g['items'][a]['id'].split('.')[-1])
            sub = {'id': g['id'] if k == 0 else g['id'] + 'b', 'instr': g['instr'] if k == 0 else
                   'Thông báo/quảng cáo thứ hai: chọn đáp án đúng cho các chỗ trống (13)–(15) (tiếp tục đề bài trên).',
                   'passage': '<p><img src="../../../../%s/%s" alt="Văn bản có chỗ trống" style="max-width:100%%;height:auto"></p>' % (img_dir, split_img[n0]),
                   'items': g['items'][a:b]}
            for it in sub['items']:
                it['id'] = '%s.%s' % (sub['id'], it['id'].split('.')[-1])
                if it['q'] == '':
                    it['q'] = 'Blank (%s)' % it['id'].split('.')[-1]
            final.append(sub)
    S = {'id': 'lop11-mt1-' + tid, 'title': title, 'grade': 11, 'unit': 'MidTerm1', 'theory': '',
         'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': minutes, 'groups': final}]}
    return S


def dump(path, S):
    s = '# -*- coding: utf-8 -*-\n"""Dữ liệu nội dung SET (sinh từ file Word bằng tools/gen_mt1_%s.py rồi có thể chỉnh tay).\nĐáp án + giải thích: xem file *_dapan.py cùng tên."""\n\nSET = ' % os.path.basename(path)[4:10]
    s += pprint.pformat(S, width=150, sort_dicts=False) + '\n'
    open(path, 'w', encoding='utf8').write(s)


FIXES = [
    ('closet in meaning', 'closest in meaning'),
    (' high blood pressure, arthritis,', ' arthritis,'),         # Q18-23: lặp "high blood pressure" (khoá Word đã bỏ)
]

if __name__ == '__main__':
    S = build_test('src/mt1/d5.txt', FIXES, 'test04', 'Test 4 – Mid-term 1', 'assets/mt1/test04', 45,
                   {10: 'image1.png', 13: 'image2.png'}, {16, 17})
    dump(os.path.join(ROOT, 'units/mt1_test04.py'), S)
    n = 0
    for g in S['pages'][0]['groups']:
        n += len(g['items'])
        print(g['id'], len(g['items']), [it['id'] for it in g['items']][:1], g['instr'][:50])
    print('TOTAL', n)
