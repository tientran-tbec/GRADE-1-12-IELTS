# -*- coding: utf-8 -*-
"""Sinh Lớp 3 – Unit 3, 4, 5 (Global Success) từ dữ liệu gọn: python tools/gen_lop3_units.py"""
import os, sys, zlib, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_lop3 as g

def tf(i, q, a, e):
    g.ANS[i] = a; g.EXP[i] = e
    return {'id': i, 't': 'tf', 'q': q}

def big(e): return '<span class="emo">%s</span>' % e
def det(items, key): return sorted(items, key=lambda x: (zlib.crc32((x + key).encode()), x))
def scramble(w, seed):
    ls = list(w)
    for k in range(20):
        random.Random(seed + k).shuffle(ls)
        if ''.join(ls) != w: break
    return ''.join(ls)

def pg(id_, title, groups): return {'id': id_, 'title': title, 'mode': 'practice', 'groups': groups}

class Gen:
    def __init__(s, D): s.D = D; s.words = [v for v in D['vocab'] if ' ' not in v[0] and v[0].isalpha() and len(v[0]) >= 3]; s.pics = [v for v in D['vocab'] if v[2]]
    # ----- thành phần dùng chung (mỗi hàm tạo 1 item với id cho trước)
    def pic(s, i, v):
        others = [x[0] for x in s.pics if x[0] != v[0]]
        opts = det([v[0]] + det(others, i)[:2], i)
        return g.mcq(i, big(v[2]), opts, v[0], '%s = %s (%s)' % (v[0], v[1], v[2]))
    def mean(s, i, v):
        others = [x[1] for x in s.D['vocab'] if x[1] != v[1]]
        opts = det([v[1]] + det(others, i)[:2], i)
        return g.mcq(i, 'Nghĩa của "%s" là:' % v[0], opts, v[1], '%s = %s' % (v[0], v[1]))
    def unscr(s, i, w): return g.fill(i, '%s → {_}' % scramble(w, zlib.crc32(i.encode())), w, w)
    def miss(s, i, w):
        k = len(w) // 2
        return g.fill(i, '%s{_}%s' % (w[:k], w[k + 1:]), w[k], w)
    def listen_word(s, i, v):
        others = [x[0] for x in s.words if x[0] != v[0]]
        opts = det([v[0]] + det(others, i)[:2], i)
        return g.mcq(i, 'Bấm 🔊 và chọn từ em nghe được.', opts, v[0], 'Từ được đọc là: %s.' % v[0], say=v[0])
    def listen_qa(s, i, qa, pool):
        q, a = qa
        opts = det([a] + det([x[1] for x in pool if x[1] != a], i)[:2], i)
        return g.mcq(i, 'Bấm 🔊, nghe và chọn câu trả lời phù hợp.', opts, a, '%s → %s' % (q, a), say=q)
    def qa_match(s, i, qas, e='Mỗi câu hỏi có một câu đáp tương ứng.'):
        left = [x[0] for x in qas]; right = det([x[1] for x in qas], i)
        return g.match(i, '', left, right, [x[1] for x in qas], e)
    def practice(s):
        D = s.D; n = D['n']; V = D['vocab']; qa = D['qa']
        # ---- trang Từ vựng
        grp = [{'id': 'm1', 'instr': 'Nối từ tiếng Anh với nghĩa tiếng Việt.', 'items': [
            g.match('m1.1', '', [v[0] for v in V[:6]], det([v[1] for v in V[:6]], 'm1'), [v[1] for v in V[:6]], '; '.join('%s = %s' % (v[0], v[1]) for v in V[:6]))]}]
        if len(V) > 6:
            grp[0]['items'].append(g.match('m1.2', '', [v[0] for v in V[6:]], det([v[1] for v in V[6:]], 'm2'), [v[1] for v in V[6:]], '; '.join('%s = %s' % (v[0], v[1]) for v in V[6:])))
        grp.append({'id': 'a', 'instr': 'Nhìn hình và chọn từ đúng.', 'items': [s.pic('a.%d' % (k + 1), v) for k, v in enumerate(s.pics)]})
        grp.append({'id': 'b', 'instr': 'Chọn từ khác loại.', 'items': [g.mcq('b.%d' % (k + 1), '', o, a, e) for k, (o, a, e) in enumerate(D['odd'])]})
        p_tv = pg('tu-vung', 'Từ vựng', grp)
        # ---- Chính tả
        p_ct = pg('chinh-ta', 'Chính tả', [
            {'id': 'c1', 'instr': 'Điền chữ cái còn thiếu.', 'items': [s.miss('c1.%d' % (k + 1), v[0]) for k, v in enumerate(s.words)]},
            {'id': 'c2', 'instr': 'Sắp xếp lại chữ cái thành từ đúng.', 'items': [s.unscr('c2.%d' % (k + 1), v[0]) for k, v in enumerate(s.words)]}])
        # ---- Mẫu câu
        p_mc = pg('mau-cau', 'Mẫu câu', [
            {'id': 'd', 'instr': 'Nối câu hỏi / lời nói (cột A) với câu trả lời (cột B).', 'items': [s.qa_match('d.1', qa)]},
            {'id': 'e', 'instr': 'Điền từ thích hợp vào chỗ trống.', 'items': [g.fill('e.%d' % (k + 1), q, a, e) for k, (q, a, e) in enumerate(D['fills'][:8])]},
            {'id': 'f', 'instr': 'Bấm các từ để xếp thành câu đúng.', 'items': [g.order('f.%d' % (k + 1), '', t, t, seed=k + n) for k, t in enumerate(D['sents'][:6])]}])
        p_mc2 = pg('mau-cau-2', 'Mẫu câu 2', [
            {'id': 'e2', 'instr': 'Chọn đáp án đúng.', 'items': [g.mcq('e2.%d' % (k + 1), q, o, a, e) for k, (q, o, a, e) in enumerate(D['mcq'])]},
            {'id': 'f2', 'instr': 'Điền từ thích hợp vào chỗ trống.', 'items': [g.fill('f2.%d' % (k + 1), q, a, e) for k, (q, a, e) in enumerate(D['fills'][8:])]},
            {'id': 'g2', 'instr': 'Bấm các từ để xếp thành câu đúng.', 'items': [g.order('g2.%d' % (k + 1), '', t, t, seed=k + n + 9) for k, t in enumerate(D['sents'][6:])]}])
        # ---- Nghe
        p_ng = pg('nghe', 'Nghe', [
            {'id': 'n1', 'instr': 'Nghe 1. Bấm 🔊 (nghe lại được nhiều lần) và chọn từ em nghe được.', 'items': [s.listen_word('n1.%d' % (k + 1), v) for k, v in enumerate(s.words[:6])]},
            {'id': 'n2', 'instr': 'Nghe 2. Nghe câu và chọn câu trả lời phù hợp.', 'items': [s.listen_qa('n2.%d' % (k + 1), x, qa) for k, x in enumerate(qa)]},
            {'id': 'n3', 'instr': 'Nghe 3. Nghe và viết lại từ.', 'items': [g.fill('n3.%d' % (k + 1), '{_}', v[0], v[0], say=v[0]) for k, v in enumerate(s.words[:5])]},
            {'id': 'n4', 'instr': 'Nghe 4. Nghe và viết lại cả câu.', 'items': [g.fill('n4.%d' % (k + 1), '{_}', t, t, say=t) for k, t in enumerate(D['sents'][:3])]}])
        # ---- Đọc hiểu
        rd = [{'id': 'r1', 'instr': 'Sắp xếp hội thoại: chọn số thứ tự (câu đầu tiên là số 0: "%s").' % D['dlg'][0],
               'items': [g.match('r1.1', '', D['dlg'][1:], ['1', '2', '3', '4'], ['1', '2', '3', '4'], 'Thứ tự đúng: ' + ' → '.join(D['dlg']))]}]
        for pi, (txt, tfs) in enumerate(D['read'], 2):
            rd.append({'id': 'r%d' % pi, 'instr': 'Đọc và chọn True (Đúng) hoặc False (Sai).', 'passage': txt, 'items': [tf('r%d.%d' % (pi, k + 1), q, a, e) for k, (q, a, e) in enumerate(tfs)]})
        p_rd = pg('doc-hieu', 'Đọc hiểu', rd)
        theory = ('<h3>Từ vựng</h3>' + g.table([[v[0] + (' ' + v[2] if v[2] else ''), v[1]] for v in V], ['English', 'Tiếng Việt']) + '<h3>Mẫu câu</h3>' + D['pattern'])
        return {'id': 'lop3-u%d-luyentap' % n, 'title': 'Unit %d – %s: Luyện tập' % (n, D['title']), 'grade': 3, 'unit': n, 'theory': theory,
                'pages': [p_tv, p_mc, p_mc2, p_ng, p_ct, p_rd]}
    def test(s, k):
        D = s.D; n = D['n']; ctr = [0]
        def nid(): ctr[0] += 1; return 't1.%d' % ctr[0]
        def cyc(lst, cnt): return [lst[(k * cnt + j) % len(lst)] for j in range(cnt)]
        it = []
        for q, o, a, e in cyc(D['mcq'], 4): it.append(g.mcq(nid(), q, o, a, e))
        for v in cyc(s.pics, 2): it.append(s.pic(nid(), v))
        o, a, e = cyc(D['odd'], 1)[0]; it.append(g.mcq(nid(), 'Chọn từ khác loại:', o, a, e))
        for v in cyc(D['vocab'], 2): it.append(s.mean(nid(), v))
        it.append(s.listen_qa(nid(), D['qa'][k % len(D['qa'])], D['qa']))
        for q, a, e in cyc(D['fills'], 4): it.append(g.fill(nid(), q, a, e))
        it.append(s.unscr(nid(), cyc(s.words, 1)[0][0]))
        for t in cyc(D['sents'], 4): it.append(g.order(nid(), '', t, t, seed=k * 7 + len(it)))
        qs = D['qa'][k:] + D['qa'][:k]; it.append(g.match(nid(), 'Nối:', [x[0] for x in qs[:4]], det([x[1] for x in qs[:4]], 'T%d' % k), [x[1] for x in qs[:4]], 'Mỗi câu hỏi có một câu đáp tương ứng.'))
        return {'id': 'lop3-u%d-test%02d' % (n, k + 1), 'title': 'Unit %d – %s: Kiểm tra %d' % (n, D['title'], k + 1), 'grade': 3, 'unit': n, 'theory': '',
                'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 15, 'warn_at': 2, 'groups': [{'id': 't1', 'instr': 'Làm %d câu. Nộp bài để xem điểm và đáp án.' % len(it), 'items': it}]}]}
    def run(s):
        n = s.D['n']
        g.write('lop3_u%d_luyentap' % n, s.practice())
        for k in range(3): g.write('lop3_u%d_test%02d' % (n, k + 1), s.test(k))

from gen_lop3_data import UNITS
if __name__ == '__main__':
    for D in UNITS: Gen(D).run()
    print('ok')
