# -*- coding: utf-8 -*-
"""Lớp 4 – nhóm HSG (unit 'HSG').
  hsg_a  'HSG – Bài tập bồi dưỡng'  (slug luyentap_a) từ Bai-tap-boi-duong-HSG-Tieng-Anh-4-Global.txt
         Tài liệu KHÔNG có phần đáp án/tô vàng -> chỉ giữ câu mà đáp án suy ra chắc chắn từ chính đoạn văn / từ vựng trong tài liệu
         (đáp án do người dựng suy ra, ghi ở bảng A_VOCAB / A_READ / A_TF bên dưới; câu mơ hồ hoặc đề lỗi bị bỏ).
         Bỏ hẳn phần Reorder (không có đáp án, các cụm từ bị cắt lộn xộn).
  hsg_b1..hsg_b5  'HSG – Bộ đề ôn thi – Đề N' (slug test01..test05) từ Bo-de-on-thi-HSG-Tieng-Anh-4-co-dap-an.txt (có ANSWER KEY).
Chạy: python3 tools/gen_lop4_hsg.py"""
import os, re, sys, json, pprint
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g4_exam import Exam, ROOT, IMGROOT

SRC_A = 'Bai-tap-boi-duong-HSG-Tieng-Anh-4-Global'
SRC_B = 'Bo-de-on-thi-HSG-Tieng-Anh-4-co-dap-an'
NOTES = []

# =====================================================================================================
# PHẦN A – Bài tập bồi dưỡng (không có key: đáp án suy ra từ đoạn văn)
# =====================================================================================================
# Trắc nghiệm từ vựng (chỉ câu chỉ có MỘT đáp án hợp lý)
A_VOCAB = {
    1: {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'D', 6: 'A', 7: 'C', 8: 'B'},
    2: {2: 'A', 4: 'B', 7: 'A', 8: 'D'},
    3: {2: 'A', 3: 'B', 5: 'B', 8: 'B'},
    4: {3: 'B', 4: 'C', 7: 'B'},
    5: {2: 'A', 3: 'C', 4: 'C', 6: 'C', 7: 'C', 8: 'A'},
    6: {1: 'C', 2: 'C', 3: 'B', 4: 'A', 7: 'B'},
    7: {1: 'A', 2: 'B', 3: 'A', 5: 'A', 6: 'A', 7: 'A'},
    8: {1: 'A', 2: 'A', 3: 'C', 4: 'C', 5: 'A', 6: 'A'},
    9: {2: 'A', 3: 'B', 4: 'C', 6: 'C', 7: 'C'},
    10: {1: 'A', 3: 'B', 4: 'C', 6: 'A', 7: 'C'},
    11: {2: 'C', 3: 'A'},
    12: {1: 'A', 3: 'A', 4: 'B', 5: 'B', 6: 'C', 7: 'A', 8: 'A'},
    13: {1: 'B', 2: 'A', 4: 'B', 6: 'A'},
    14: {1: 'C', 4: 'B', 5: 'B', 6: 'B', 8: 'A'},
    15: {1: 'A', 3: 'C', 4: 'A', 5: 'B', 6: 'C', 7: 'C', 8: 'B'},
    16: {1: 'A', 2: 'B', 3: 'A', 4: 'B', 5: 'C', 6: 'B', 7: 'B', 8: 'A'},
    17: {8: 'A'},
    18: {2: 'A', 3: 'C', 6: 'B'},
    19: {1: 'A', 6: 'B'},
    20: {4: 'B', 5: 'B', 6: 'B'},
}
# Trắc nghiệm đọc hiểu (đáp án nằm trong đoạn văn)
A_READ = {
    1: {1: 'C', 2: 'B', 3: 'B', 4: 'A'},
    2: {1: 'B', 2: 'C', 3: 'B', 4: 'B'},
    3: {2: 'B', 3: 'B', 4: 'B'},
    4: {1: 'B', 2: 'C', 3: 'A', 4: 'B'},
    5: {1: 'C', 3: 'B', 4: 'B'},
    6: {1: 'B', 2: 'B', 3: 'A', 4: 'A'},
    7: {1: 'B', 2: 'B', 3: 'B', 4: 'C'},
    8: {1: 'B', 2: 'B', 3: 'C'},
    9: {1: 'B', 2: 'A', 3: 'B', 4: 'B'},
    10: {1: 'C', 2: 'A', 3: 'C', 4: 'A', 5: 'A'},
    11: {1: 'B', 2: 'B', 3: 'B', 4: 'A', 5: 'B'},
    12: {1: 'B', 2: 'C', 3: 'D', 4: 'D', 5: 'B'},
    13: {1: 'A', 3: 'A', 4: 'A', 5: 'C'},
    14: {2: 'B', 4: 'B', 5: 'C'},
    15: {1: 'C', 3: 'B', 4: 'C', 5: 'C'},
    16: {1: 'B', 2: 'B', 3: 'C', 4: 'A', 5: 'C'},
    17: {1: 'B', 4: 'C', 5: 'A'},
    18: {1: 'C', 2: 'B', 3: 'B', 4: 'B', 5: 'A'},
    19: {1: 'B', 2: 'A', 3: 'B', 4: 'B', 5: 'B'},
    20: {1: 'B', 2: 'B', 3: 'B', 4: 'C', 5: 'A'},
}
# Đúng/Sai (đáp án suy ra từ đoạn văn)
A_TF = {
    1: {1: 'F', 2: 'F', 3: 'F', 4: 'F'},
    2: {1: 'F', 2: 'T', 3: 'F', 4: 'F'},
    3: {1: 'F', 2: 'F', 3: 'T', 4: 'F'},
    4: {1: 'F', 2: 'F', 3: 'F', 4: 'T'},
    5: {1: 'T', 2: 'F', 3: 'F', 4: 'T'},
    6: {1: 'T', 2: 'F', 3: 'F', 4: 'T'},
    7: {1: 'F', 2: 'T', 3: 'T', 4: 'F'},
    8: {1: 'F', 2: 'T', 3: 'T', 4: 'F'},
    9: {1: 'F', 2: 'F', 3: 'T'},
    10: {1: 'F', 2: 'T', 3: 'F', 4: 'T', 5: 'T'},
    11: {1: 'F', 2: 'F', 3: 'T', 4: 'F', 5: 'T'},
    13: {1: 'F', 2: 'T', 3: 'F', 5: 'T'},
    14: {1: 'T', 2: 'T', 3: 'F', 4: 'F', 5: 'F'},
    15: {1: 'T', 2: 'F', 3: 'T', 4: 'F', 5: 'F'},
    16: {1: 'F', 2: 'T', 3: 'F', 4: 'T', 5: 'T'},
    17: {1: 'F', 2: 'F', 3: 'T', 4: 'F'},
    18: {2: 'T', 4: 'F', 5: 'F'},
    19: {1: 'F', 2: 'F', 3: 'T', 4: 'F', 5: 'F'},
    20: {1: 'F', 2: 'T', 3: 'T', 4: 'T'},
}
FIXMEAN = [('historyand', 'history and'), ('dụcthể', 'dục thể'), ('nghệthông', 'nghệ thông'), ('nướcÔ', 'nước Ô'), ('nướcThái', 'nước Thái'), ('nướcNhật', 'nước Nhật')]


def cl(s):
    s = s.replace('⟦', '').replace('⟧', '').replace('¦', ' ')
    for a, b in FIXMEAN: s = s.replace(a, b)
    s = re.sub(r'\s+([.,?!;:])', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def parse_a():
    lines = [l.rstrip() for l in open(os.path.join(IMGROOT, SRC_A + '.txt'), encoding='utf8').read().split('\n')]
    units, cur = {}, None
    for l in lines:
        m = re.match(r'^⟦?Unit (\d+):\s*(.*?)⟧?$', l.strip())
        if m:
            cur = units.setdefault(int(m.group(1)), {'title': m.group(2), 'lines': []}); continue
        if cur is not None: cur['lines'].append(l)
    out = {}
    for n, U in units.items():
        st, voc, vq, pas, rq, tq, cq = 'vocab', [], [], [], [], [], None
        title = ''
        for l in U['lines']:
            t = l.strip()
            if not t or t.startswith('…'): continue
            if t.startswith('|'):
                if st == 'vocab' and not t.startswith('| WORD'):
                    c = [x.strip() for x in t.strip('|').split(' | ')]
                    voc.append((cl(c[0]), cl(c[-1])))
                continue
            if re.match(r'^Reorder', t): st = 'reorder'; continue
            m = re.match(r'^Read the passage:\s*(.*)$', t)
            if m: st = 'passage'; title = m.group(1).strip(); continue
            if re.match(r'^Multiple[ -]Choice Questions', t): st = 'mcq'; cq = None; continue
            if re.match(r'^(True/False Questions|Choose True or False)', t): st = 'tf'; cq = None; continue
            if st == 'reorder':
                if not re.match(r'^\d+\.', t):          # đoạn văn nằm lẫn sau mục Reorder (Unit 12, 20)
                    if not pas and len(t) < 40: title = t
                    else: pas.append(t)
                continue
            if st == 'passage': pas.append(t); continue
            if st in ('vocab', 'mcq', 'tf'):
                mq = re.match(r'^(\d+)\.\s*(.*)$', t)
                mo = re.match(r'^([a-d])\.\s*(.*)$', t)
                if mq and not mo:
                    q = {'n': int(mq.group(1)), 'q': re.sub(r'^True/False:\s*', '', mq.group(2)), 'o': []}
                    cq = q
                    {'vocab': vq, 'mcq': rq, 'tf': tq}[st].append(q)
                elif mo and cq is not None:
                    cq['o'].append(cl(mo.group(2)))
        out[n] = {'title': U['title'], 'vocab': voc, 'vq': vq, 'passage': pas, 'ptitle': title, 'rq': rq, 'tq': tq}
    return out


def build_a():
    D = parse_a()
    assert sorted(D) == list(range(1, 21)), sorted(D)
    ANS, EXP = {}, {}

    def mcq_item(iid, q, opts, key):
        ANS[iid] = key; EXP[iid] = 'Đáp án: %s. %s' % (key, opts['ABCD'.index(key)])
        return {'id': iid, 't': 'mcq', 'q': cl(q), 'o': opts}
    vgroups, rgroups, theory = [], [], ['<h3>Từ vựng theo Unit (HSG – Bài tập bồi dưỡng)</h3>']
    for n in range(1, 21):
        U = D[n]
        theory.append('<h3>Unit %d: %s</h3><table class="tb">%s</table>' % (n, U['title'], ''.join('<tr><td><b>%s</b></td><td>%s</td></tr>' % (w, m) for w, m in U['vocab'])))
        # từ vựng
        its = []
        for q in U['vq']:
            k = A_VOCAB.get(n, {}).get(q['n'])
            if not k: NOTES.append('A U%d từ vựng câu %d: bỏ (mơ hồ/đề lỗi)' % (n, q['n'])); continue
            assert len(q['o']) >= 'ABCD'.index(k) + 1, (n, q['n'])
            its.append(mcq_item('v%d.%d' % (n, len(its) + 1), q['q'], q['o'], k))
        if its: vgroups.append((n, {'id': 'v%d' % n, 'instr': 'Unit %d – %s: Choose the correct option. (Chọn đáp án đúng.)' % (n, U['title']), 'items': its}))
        # đọc hiểu
        its = []
        for q in U['rq']:
            k = A_READ.get(n, {}).get(q['n'])
            if not k: NOTES.append('A U%d đọc hiểu câu %d: bỏ (đề lỗi/mơ hồ)' % (n, q['n'])); continue
            assert len(q['o']) >= 'ABCD'.index(k) + 1, (n, q['n'], 'read')
            its.append(mcq_item('r%d.%d' % (n, len(its) + 1), q['q'], q['o'], k))
        for q in U['tq']:
            k = A_TF.get(n, {}).get(q['n'])
            if not k: NOTES.append('A U%d T/F câu %d: bỏ (mơ hồ)' % (n, q['n'])); continue
            iid = 'r%d.%d' % (n, len(its) + 1)
            ANS[iid] = k; EXP[iid] = 'Đáp án: %s (căn cứ đoạn văn).' % ('True (Đúng)' if k == 'T' else 'False (Sai)')
            its.append({'id': iid, 't': 'tf', 'q': cl(q['q'])})
        if its:
            ps = U['passage']
            assert ps, n
            html = ('<h4>%s</h4>' % cl(U['ptitle']) if U['ptitle'] else '') + ''.join('<p>%s</p>' % cl(p) for p in ps)
            rgroups.append((n, {'id': 'r%d' % n, 'instr': 'Unit %d – %s: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)' % (n, U['title']), 'passage': html, 'items': its}))

    def paginate(groups, pid, label, limit=40):
        pages, cur, cnt = [], [], 0
        for n, g in groups:
            if cur and cnt + len(g['items']) > limit: pages.append(cur); cur, cnt = [], 0
            cur.append((n, g)); cnt += len(g['items'])
        if cur: pages.append(cur)
        res = []
        for i, pg in enumerate(pages):
            a, b = pg[0][0], pg[-1][0]
            res.append({'id': pid if i == 0 else '%s-%d' % (pid, i + 1), 'title': '%s – Unit %s' % (label, (str(a) if a == b else '%d–%d' % (a, b))), 'mode': 'practice', 'groups': [g for _, g in pg]})
        return res
    pages = paginate(vgroups, 'tu-vung', 'Từ vựng') + paginate(rgroups, 'doc-hieu', 'Đọc hiểu')
    S = {'id': 'lop4-hsg-a', 'title': 'HSG – Bài tập bồi dưỡng', 'grade': 4, 'unit': 'HSG', 'theory': ''.join(theory), 'pages': pages}
    write_set('hsg_a', S, ANS, EXP, 'luyentap_a')
    tot = sum(len(g['items']) for p in pages for g in p['groups'])
    print('hsg_a: %d câu, %d trang: %s' % (tot, len(pages), ' | '.join('%s=%d' % (p['id'], sum(len(g['items']) for g in p['groups'])) for p in pages)))


def write_set(tag, S, ANS, EXP, slug):
    base = 'units/lop4_%s' % tag
    os.makedirs(os.path.join(ROOT, 'assets/lop4_%s' % tag), exist_ok=True)
    for path, name, obj in ((base + '.py', 'SET', S), (base + '_dapan.py', 'ANS', ANS)):
        with open(os.path.join(ROOT, path), 'w', encoding='utf8') as f:
            f.write('# -*- coding: utf-8 -*-\n"""Sinh bởi tools/gen_lop4_hsg.py"""\n\n%s = %s\n' % (name, pprint.pformat(obj, width=160)))
    with open(os.path.join(ROOT, base + '_dapan.py'), 'a', encoding='utf8') as f:
        f.write('\nEXPLANATIONS = %s\n' % pprint.pformat(EXP, width=160))
    os.makedirs(os.path.join(ROOT, 'units/reg'), exist_ok=True)
    json.dump([S['id'], base + '.py', base + '_dapan.py', 'Lop4', 'HSG', slug, 'assets/lop4_%s' % tag, ''],
              open(os.path.join(ROOT, 'units/reg/%s.json' % tag), 'w', encoding='utf8'), ensure_ascii=False)


# =====================================================================================================
# PHẦN B – Bộ đề ôn thi (có ANSWER KEY trong tài liệu)
# =====================================================================================================
U_ = lambda w, a: w.replace('[', '<u>').replace(']', '</u>')   # [ea] -> <u>ea</u>

PRON_Q = 'Chọn từ có phần gạch chân phát âm khác các từ còn lại.'
ODD_Q = 'Chọn từ khác loại.'

# mỗi đề: dict các phần
EXAMS = {}

EXAMS[1] = dict(
    odd=([['seven', 'nice', 'nine', 'two'], ['when', 'happy', 'what', 'how'], ['eggs', 'apple', 'chairs', 'books'], ['is', 'are', 'am', 'were'], ['teacher', 'doctor', 'pilot', 'cooker']], 'BBBDD'),
    pron=([['h[ea]d', 'pl[ea]se', 'h[ea]vy', 'm[ea]sure'], ['n[o]tebook', 'gl[o]ves', 's[o]me', '[o]ther'], ['n[ow]', 'h[ow]', 'am[ou]nt', 'bl[ow]'],
           ['disapp[ea]r', 'w[ea]r', 'y[ea]r', 'd[ea]r'], ['h[a]te', 'p[a]n', 'c[a]rrot', 'm[a]tter']], 'BADBA'),
    grammar=([('He _______ dinner for his family last night.', ['cook', 'cooks', 'cooked', 'cooking']), ('He _______ cooking new recipes.', ['enjoys', 'enjoy', 'enjoyed', 'is enjoying']),
              ('He _______ coffee at the moment.', ['is drinking', 'drink', 'drinks', 'drank']), ('I _______ to school every day.', ['walks', 'walk', 'walked', 'am walking']),
              ('The birds _______ in the morning.', ['chirp', 'chirps', 'are chirping', 'chirped']), ('The sun _______ in the west.', ['sets', 'is setting', 'set', 'had set']),
              ('They _______ the zoo last weekend.', ['are visiting', 'visit', 'visited', 'visits']), ('We usually _______ pancakes for breakfast on Sundays.', ['are having', 'have', 'had', 'has']),
              ('She _______ shopping for groceries yesterday.', ['go', 'goes', 'went', 'is going']), ('He is currently _______ for his exams.', ['studying', 'study', 'studies', 'studied'])], 'CAABAACBCA'),
    verbs=[('I {_} (play) soccer after school.', ['play']), ('She {_} (read) books every night.', ['reads']), ('We {_} (go) swimming on Saturdays.', ['go']),
           ('She {_} (not read) a book right now.', ['isn’t reading']), ('We {_} (not swim) at the pool today.', ['aren’t swimming']), ('I {_} (not play) soccer yesterday.', ['didn’t play']),
           ('She {_} (not read) a book last night.', ['didn’t read']), ('{_} he {_} (listen) to music in his room yesterday?', ['Did', 'listen']),
           ('{_} they {_} (play) basketball after school yesterday?', ['Did', 'play']), ('We {_} (go) to the park last Saturday.', ['went'])],
    match=(['What is your favorite subject in school?', 'Where did you go on your last vacation?', 'When is your birthday?', 'Do you like to read science fiction books?', 'Are you going to the party tonight?'],
           ['My birthday is on July 15th.', 'My favorite subject is science.', 'Yes, I am.', 'I went to Florida with my family. We visited Disney World and had a lot of fun!', 'No, I don’t.'], 'BDAEC'),
    fix=[('The sun are shining brightly.', 'The sun is shining brightly.', 'are → is'), ('Birds chirps in the morning.', 'Birds chirp in the morning.', 'chirps → chirp'),
         ('I love play with my toys.', 'I love playing with my toys.', 'play → playing'), ('My dog like to chase its tail.', 'My dog likes to chase its tail.', 'like → likes'),
         ('We goes to school to learn.', 'We go to school to learn.', 'goes → go')],
    reading=dict(kind='cloze', bank=['upon', 'Children', 'taught', 'kingdom', 'named'],
                 passage='Once (1) ______ a time, there was a magical kingdom where animals and humans lived harmoniously. In this kingdom, a wise old owl (2) ______ Oliver was known for his knowledge and kindness. Every day, he would sit perched on a tall oak tree, offering advice and guidance to anyone who sought it. (3) ______ from all corners of the kingdom would gather around Oliver, eager to hear his stories and wisdom. With his gentle hoots and soothing voice, Oliver (4) ______ the young ones valuable lessons about friendship, bravery, and the importance of kindness. And so, the (5) ______ flourished under the watchful eyes and wise words of their beloved owl, Oliver.',
                 ans=['upon', 'named', 'Children', 'taught', 'kingdom']),
    order=[(['The', 'Independence', 'Declaration', 'of', 'declared', 'freedom.'], 'The Declaration of Independence declared freedom.'), (['evokes', 'Music', 'in', 'emotions', 'us.'], 'Music evokes emotions in us.'),
           (['shake', 'the', 'Earthquakes', 'ground.'], 'Earthquakes shake the ground.'), (['are', 'Cells', 'living', 'tiny', 'things.'], 'Cells are tiny living things.'),
           (['The', 'around', 'the', 'goes', 'Earth', 'Sun.'], 'The Earth goes around the Sun.')],
    rewrite=[('My sister walks to the supermarket.', 'My sister goes …', 'My sister goes to the supermarket on foot.'), ('There are many flowers in our garden.', 'Our garden …', 'Our garden has many flowers.'),
             ('Does your father cycle to work?', 'Does your father get …', 'Does your father get to work by bike?'), ('The garden is behind Nam’s classroom.', 'Nam’s classroom …', 'Nam’s classroom is in front of the garden.'),
             ('Tom drives to work every morning.', 'Tom travels …', 'Tom travels to work by car every morning.')])

EXAMS[2] = dict(
    odd=([['morning', 'dancing', 'evening', 'afternoon'], ['see', 'watch', 'meet', 'how'], ['Vietnamese', 'Australia', 'America', 'Canada'], ['he', 'your', 'they', 'we'], ['grandpa', 'doctor', 'mother', 'cousin']], 'BDABB'),
    pron=([['nerv[ou]s', 'sc[ou]t', 'h[ou]sehold', 'm[ou]se'], ['favor[i]te', 'f[i]nd', 'outs[i]de', 'l[i]brary'], ['l[a]st', 't[a]ste', 'f[a]st', 't[a]sk'],
           ['f[u]ture', 's[u]mmer', 'n[u]mber', 'dr[u]m'], ['t[i]me', 'k[i]nd', 'b[i]rd', 'n[i]ce']], 'AABAC'),
    grammar=([('He __________ a documentary about nature.', ['is watching', 'watch', 'watches', 'watched']), ('He usually __________ for a run in the evening.', ['goes', 'is going', 'went', 'go']),
              ('I __________ a workshop next month.', ['am attending', 'attend', 'attends', 'attended']), ('I __________ in the park every morning.', ['am jogging', 'jog', 'jogs', 'jogged']),
              ('She always __________ in the shower.', ['is singing', 'sing', 'sings', 'sang']), ('She __________ a novel at the moment.', ['is reading', 'read', 'reads', 'have read']),
              ('She __________ for her exams this week.', ['study', 'studies', 'studied', 'is studying']), ('She often __________ long walks in the park.', ['taked', 'takes', 'take', 'is taking']),
              ('She __________ a marathon last month.', ['is running', 'run', 'runs', 'ran']), ('He __________ television right now.', ['watch', 'watches', 'is watching', 'watched'])], 'AAABCADBDC'),
    verbs=[('Birds {_} (not sing) in the winter.', ['don’t sing']), ('Cats {_} (not sleep) in the morning.', ['don’t sleep']), ('He {_} (swim) in the pool right now.', ['is swimming']),
           ('{_} we {_} (visit) grandma this weekend?', ['Are', 'visiting']), ('Birds {_} (sing) in the trees yesterday.', ['sang']), ('Cats {_} (sleep) on the couch last night.', ['slept']),
           ('{_} she {_} (dance) ballet in the studio yesterday?', ['Did', 'dance']), ('{_} he {_} (walk) to school this morning?', ['Is', 'walking']),
           ('My mom {_} (not cook) dinner tonight.', ['isn’t cooking']), ('{_} the Earth {_} (orbit) the Sun?', ['Does', 'orbit'])],
    match=(['What’s the weather like today?', 'What nationality is Hoa?', 'Where’s Ha Noi?', 'Do you like English?', 'Where do you live?'],
           ['She’s Vietnamese.', 'Yes, I really like it.', 'I live in Ha Noi.', 'It’s rainy.', 'It’s in north Viet Nam.'], 'DAEBC'),
    fix=[('I plays soccer after school.', 'I play soccer after school.', 'plays → play'), ('She is reading books every night.', 'She reads books every night.', 'is reading → reads'),
         ('She reads a book right now.', 'She is reading a book right now.', 'reads → is reading'), ('I play soccer yesterday.', 'I played soccer yesterday.', 'play → played')],
    fix_dropped='VI.3 (“I play soccer after school.” câu gốc đã đúng nhưng key ghi “am playing”)',
    reading=dict(kind='mcq2', passage='Once upon a time, a young girl named Lily lived in a small village nestled between rolling hills. Lily had a special gift – she could communicate with animals. Every morning, she would wake up to the cheerful chirping of birds outside her window, and they would tell her tales of their adventures in the forest. With a heart full of kindness, Lily would spend her days tending to injured animals, nursing them back to health with gentle care. Her bond with the creatures of the forest was unbreakable, and they became her closest friends. Together, they roamed the woods, exploring hidden trails and discovering the wonders of nature. In the eyes of Lily, every creature, big or small, held a story waiting to be heard, and she cherished each moment spent in their company.',
                 qs=[('What was special about Lily in the story?', ['Lily could communicate with animals.', 'Lily could communicate with gifts.'], 'A'),
                     ('How did Lily spend her days in the village?', ['Lily spent her days buying animals.', 'Lily spent her days tending to injured animals.'], 'B'),
                     ('What did the birds do for Lily every morning?', ['The birds outside her window told Lily tales of their adventures.', 'The birds outside her door told Lily tales of their adventures.'], 'A'),
                     ('Describe Lily’s relationship with the animals of the forest.', ['Lily had an unbreakable bond with the animals of the forest, becoming her closest friends.', 'With a heart full of kindness, Lily would spend her days tending to injured animals, nursing them back to health with gentle care.'], 'A'),
                     ('How did Lily view every creature she encountered?', ['Lily had a special gift – she could communicate with animals.', 'Lily believed that every creature had a story waiting to be heard and cherished each moment with them.'], 'B')]),
    order=[(['doesn\'t', 'She', 'books', 'every', 'read', 'night.'], 'She doesn\'t read books every night.'), (['We', 'swimming', 'at', 'are', 'pool', 'the', 'today.'], 'We are swimming at the pool today.'),
           (['He', 'is', 'walking', 'to', 'school', 'this', 'morning.'], 'He is walking to school this morning.'), (['She', 'read', 'a', 'book', 'last', 'night.'], 'She read a book last night.'),
           (['We', 'swam', 'at', 'the', 'pool', 'last', 'weekend.'], 'We swam at the pool last weekend.')],
    rewrite=[('There are four people in her family.', 'Her family …', 'Her family has four people.'), ('My house is behind the hotel.', 'The hotel …', 'The hotel is in front of my house.'),
             ('Does your class have twenty-five students?', 'Are …', 'Are there twenty-five students in your class?'), ('He goes to work at seven-fifteen.', 'He goes to work at a …', 'He goes to work at a quarter past seven.'),
             ('The drugstore is to the right of the bakery.', 'The bakery …', 'The bakery is to the left of the drugstore.')])

EXAMS[3] = dict(
    odd=([['art', 'maths', 'subject', 'science'], ['when', 'why', 'watch', 'how'], ['June', 'August', 'weather', 'December'], ['book', 'pen', 'rubber', 'house'], ['teacher', 'daughter', 'sister', 'aunt']], 'CCCDA'),
    pron=([['h[ar]d', 'c[ar]ry', 'c[ar]d', 'y[ar]d'], None, ['w[e]ll', 'g[e]t', 's[e]nd', 'pr[e]tty'], ['w[ea]ther', 'r[ea]dy', 'm[ea]n', 'h[ea]d'], ['br[ea]k', 'm[ea]n', 'pl[ea]se', 'm[ea]t']], 'BXDCA'),
    pron_dropped='II.2 (m[y]/bab[y]/sp[y]/cr[y]: key ghi A nhưng từ khác biệt là baby -> key sai)',
    grammar=([('She _________ yoga regularly.', ['practice', 'practices', 'is practicing', 'practiced']), ('She _________ English at the local school.', ['teaches', 'teach', 'is teaching', 'teached']),
              ('The sun _________ early in the morning.', ['rise', 'is rising', 'rises', 'rised']), ('They _________ a vacation next month.', ['plan', 'plans', 'are planning', 'planned']),
              ('They _________ a concert last Friday.', ['attend', 'attends', 'are attending', 'attended']), ('We _________ hiking in the mountains.', ['enjoy', 'enjoys', 'are enjoying', 'enjoyed']),
              ('We _________ dinner at 7 p.m.', ['ate', 'are eating', 'eats', 'eat']), ('We usually _________ a walk after dinner.', ['are taking', 'take', 'takes', 'taked']),
              ('We _________ a movie at home last night.', ['watch', 'watches', 'are watching', 'watched']), ('We _________ the theater tomorrow night.', ['go to', 'goes to', 'are going to', 'went to'])], 'BACCDADBDC'),
    verbs=[('{_} she {_} (read) a book right now?', ['Is', 'reading']), ('{_} we {_} (swim) at the pool today?', ['Are', 'swimming']), ('{_} they {_} (watch) movies on Fridays?', ['Do', 'watch']),
           ('{_} the Sun {_} (rise) in the east?', ['Does', 'rise']), ('We {_} (not visit) grandma next week.', ['aren’t visiting']), ('He {_} (walk) to school last morning.', ['walked']),
           ('We {_} (not go) to the park tomorrow.', ['aren’t going']), ('{_} they {_} (play) video games together last weekend?', ['Did', 'play'])],
    verbs_dropped='IV.1-2 (câu gốc “She (brush) … last night / He (listen) … yesterday” khẳng định nhưng key ghi didn’t brush / didn’t listen -> key lệch đề)',
    match=(['How old is your brother?', 'Where is Hakim from?', 'What are they doing?', 'Nice to meet you, Son.', 'Are they your friends?'],
           ['They’re doing their homework.', 'It’s nice to meet you, too, Ha.', 'He\'s six.', 'Yes, they’re.', 'He’s from Malaysia.'], 'CEABD'),
    fix=[('He walk to school in the morning.', 'He walks to school in the morning.', 'walk → walks'), ('They watched movies on Fridays.', 'They watch movies on Fridays.', 'watched → watch'),
         ('He walks to school this morning.', 'He is walking to school this morning.', 'walks → is walking'), ('They watch a movie tonight.', 'They are watching a movie tonight.', 'watch → are watching'),
         ('The Sun shines brightly yesterday.', 'The Sun shone brightly yesterday.', 'shines → shone')],
    reading=dict(kind='open', passage='Hogwarts is a very special school: it is a school for young witches and wizards. It is located near a lake in Scotland, but its students come from Scotland, England, Ireland and Wales. School begins on September 1, and students all get on a special train in London to go to school together. Hogwarts is a boarding school, so students have classes and live at the school. They have to wear robes as their uniform. Each student has an owl for a pet. The owls also carry letters from families. All students play a sport called “quidditch”, a kind of flying soccer. Players try to hit the ball with a stick while mounting their flying brooms.',
                 qs=[('Who goes to Hogwarts School?', 'Young witches and wizards'), ('How do students get to school on their first day?', 'By train'), ('What do the students wear for their uniforms?', 'Robes'),
                     ('What do owls do for the students?', 'Carry letters from families'), ('What do players use to hit the ball in a quidditch?', 'A stick')]),
    order=[(['We', 'don\'t', 'go', 'swimming', 'on', 'Saturdays.'], 'We don\'t go swimming on Saturdays.'), (['He', 'doesn\'t', 'walk', 'to', 'school', 'in', 'the', 'morning.'], 'He doesn\'t walk to school in the morning.'),
           (['Am', 'I', 'playing', 'soccer', 'after', 'school?'], 'Am I playing soccer after school?'), (['Is', 'she', 'reading', 'a', 'book', 'right', 'now?'], 'Is she reading a book right now?'),
           (['They', 'didn\'t', 'watch', 'a', 'movie', 'last', 'Friday.'], 'They didn\'t watch a movie last Friday.')],
    rewrite=[('My room is smaller than your room.', 'Your room …', 'Your room is bigger than my room.'), ('No house in the street is older than this house.', 'This house …', 'This house is the oldest in the street.'),
             ('Quang is 1.75 meters tall. Vinh is 1.65 meters tall.', 'Vinh is …', 'Vinh is shorter than Quang.'), ('Hang is the fattest girl in my class.', 'No girl …', 'No girl in my class is fatter than Hang.'),
             ('The Red River is 1,200 kilometers long. The Nile River is 6,437 kilometers long.', 'The Nile River is much …', 'The Nile River is much longer than the Red River.')])

EXAMS[4] = dict(
    odd=([None, ['badminton', 'volleyball', 'kites', 'tennis'], ['has', 'sing', 'play', 'swim'], ['nice', 'big', 'read', 'old'], ['dog', 'cat', 'fish', 'pig']], 'XCACC'),
    odd_dropped='I.1 (seventh/fifteenth/nineth/second đều là số thứ tự, key ghi B không có cơ sở)',
    pron=([['l[u]cky', 'p[u]nish', 'p[u]ll', 'h[u]ngry'], ['pl[a]net', 'ch[a]racter', 'h[a]ppy', 'classm[a]te'], ['l[e]tter', 'tw[e]lve', 'p[e]rson', 's[e]ntence'], None, ['[th]at', '[th]ank', '[th]ief', '[th]in']], 'CDCXA'),
    pron_dropped='II.4 (h[u]mor/m[u]sic/c[u]cumber/s[u]n: key ghi A nhưng từ khác biệt là sun -> key sai)',
    grammar=([('They _________ the museum last weekend.', ['visit', 'visited', 'visits', 'are visiting']), ('We often _________ to the gym together.', ['are going', 'go', 'went', 'goes']),
              ('The flowers _________ in the spring.', ['bloom', 'blooms', 'are blooming', 'bloomed']), ('The cat usually _________ on the sofa.', ['is sleeping', 'sleep', 'sleeps', 'slept']),
              ('The sun _________ in a spectacular display.', ['is setting', 'set', 'are setting', 'sets']), ('The sun _________ in the east.', ['is rising', 'rised', 'rise', 'rises']),
              ('They _________ to Europe last year.', ['traveled', 'are traveling', 'travel', 'travels']), ('We _________ a concert tomorrow.', ['are going to', 'went to', 'go to', 'goes to']),
              ('I _________ a new language online.', ['learns', 'learn', 'am learning', 'learns']), ('He enjoys _________ video games in his free time.', ['played', 'playing', 'play', 'plays'])], 'BBACDDAACB'),
    verbs=[('Flowers {_} (bloom) in the garden last spring.', ['bloomed']), ('The Earth {_} (rotate) on its axis yesterday.', ['rotated']), ('He {_} (not walk) to school this morning.', ['isn’t walking']),
           ('They {_} (not watch) a movie tonight.', ['aren’t watching']), ('{_} she {_} (dance) ballet on Tuesdays?', ['Does', 'dance']), ('{_} he {_} (swim) in the pool in summer?', ['Does', 'swim']),
           ('They {_} (play) video games on weekends.', ['play']), ('My mom {_} (cook) dinner every evening.', ['cooks']), ('{_} cats {_} (sleep) on the couch last night?', ['Did', 'sleep']),
           ('{_} dogs {_} (bark) loudly yesterday?', ['Did', 'bark'])],
    match=(['Good night, children.', 'Do you have any pets?', 'What nationality are you?', 'What day is it today?', 'Where are you from?'],
           ['Yes. I have three chickens.', 'It’s the first of October.', 'Good night, Dad and Mom.', 'I’m from England.', 'I’m Korean.'], 'CAEBD'),
    fix=[('Does I play soccer after school?', 'Do I play soccer after school?', 'Does → Do'), ('Does she reads books every night?', 'Does she read books every night?', 'reads → read'),
         ('I don’t play soccer yesterday.', 'I didn’t play soccer yesterday.', 'don’t → didn’t'), ('She doesn’t read a book last night.', 'She didn’t read a book last night.', 'doesn’t → didn’t'),
         ('We are not visit grandma next week.', 'We are not visiting grandma next week.', 'visit → visiting')],
    reading=dict(kind='tf', passage='I have many good classmates, but my best friends are Vy and Thảo. Vy sits next to me, and Thảo sits in front of us. Both of them are very smart and creative. Vy is good at English, and Thảo is best at maths. They help me a lot with my study. During break time, we often play many games together. Our favourite is hide and seek. Thảo and I like science, so we join the school\'s science club. Vy likes dancing, so she is in the dance club. Vy often performs in front of the whole school at the beginning of each month, and we love watching her. I think I\'m very lucky to have two best friends!',
                 qs=[('Mai is mainly talking about her school activities.', 'F'), ('Mai, Vy and Thảo sit at the same table.', 'F'), ('They don\'t have any favourite game.', 'F'),
                     ('Mai\'s friends help her to study.', 'T'), ('Vy is not in the same club as Mai and Thảo.', 'T')]),
    order=[(['She', 'books', 'read', 'every', 'doesn\'t', 'night.'], 'She doesn\'t read books every night.'), (['swimming', 'We', 'on', 'go', 'don\'t', 'Saturdays.'], 'We don\'t go swimming on Saturdays.'),
           (['are', 'Birds', 'not', 'the', 'in', 'singing', 'winter.'], 'Birds are not singing in the winter.'), (['Cats', 'sleeping', 'not', 'are', 'outside.'], 'Cats are not sleeping outside.'),
           (['play', 'Did', 'soccer', 'I', 'yesterday?'], 'Did I play soccer yesterday?')],
    rewrite=[('How many classes are there in your school?', 'How many classes does …', 'How many classes does your school have?'), ('That classroom is small.', 'That is a …', 'That is a small classroom.'),
             ('Peter is Mary’s brother.', 'Mary …', 'Mary is Peter\'s sister.'), ('My house has four floors.', 'There …', 'There are four floors in my house.'),
             ('Mr. and Mrs. Black have a son, John.', 'John is …', 'John is the son of Mr. and Mrs. Black.')])

EXAMS[5] = dict(
    odd=([['kite', 'cook', 'sing', 'listen'], ['read', 'happy', 'young', 'beautiful'], ['egg', 'apple', 'pen', 'books'], ['window', 'wall', 'door', 'bus'], ['May', 'July', 'Monday', 'January']], 'AADDC'),
    pron=([['r[ou]gh', 's[u]m', '[u]tter', '[u]nion'], ['n[oo]n', 't[oo]l', 'bl[oo]d', 'sp[oo]n'], ['[ch]emist', '[ch]icken', '[ch]urch', 'cen[t]ury'], ['th[ou]ght', 't[ou]gh', 't[au]ght', 'b[ou]ght'],
           ['pl[ea]sure', 'h[ea]t', 'm[ea]t', 'f[ee]d']], 'DCABA'),
    grammar=([('He _________ television right now.', ['is watching', 'watch', 'watches', 'watched']), ('He _________ basketball with his friends yesterday.', ['play', 'plays', 'is playing', 'played']),
              ('He _________ the newspaper every morning.', ['read', 'reads', 'is reading', 'have read']), ('He _________ his parents last weekend.', ['is visiting', 'visit', 'visited', 'visits']),
              ('_________ do you like monkeys? Because they\'re funny.', ['What', 'When', 'Why', 'Who']), ('Would you _________ some milk? Yes, please.', ['like', 'liking', 'to like', 'liked']),
              ('_________ your favorite drink, Mai? – It\'s orange juice.', ['What', 'What’s', 'When', 'How']), ('_________ do they look like? They\'re tall and slim.', ['What', 'What’s', 'Why', 'How']),
              ('_________ is stronger? Kevin is stronger.', ['Why', 'When', 'Who', 'What']), ('_________ are you doing, Linda?', ['Why', 'Who', 'Where', 'What'])], 'ADBCCABACD'),
    verbs=[('She {_} (brush) her teeth before bed last night.', ['brushed']), ('He {_} (listen) to music in his room yesterday.', ['listened']), ('She {_} (not dance) ballet in the gym next week.', ['isn’t dancing']),
           ('He {_} (not swim) in the pool right now.', ['isn’t swimming']), ('My mom {_} (not cook) breakfast in the evening.', ['doesn’t cook']), ('We {_} (not visit) the park at night.', ['don’t visit']),
           ('{_} they {_} (watch) a movie tonight?', ['Are', 'watching']), ('They {_} (not play) video games together last weekend.', ['didn’t play']), ('We {_} (go) swimming on Saturdays.', ['go']),
           ('He {_} (walk) to school in the morning.', ['walks'])],
    match=(['What do you do at the weekend?', 'What does Alex do on Sunday mornings?', 'What is the date today?', 'What is Hakim’s nationality?', 'How many months are there in a year?'],
           ['He goes to school on Sunday mornings.', 'Today is Thursday.', 'I go shopping with my mother.', 'There are twelve months.', 'He is Malaysian.'], 'CABED'),
    fix=[('The Sun isn\'t rise in the west.', 'The Sun doesn\'t rise in the west.', 'isn’t → doesn’t'), ('Birds aren’t sing in the winter.', 'Birds don\'t sing in the winter.', 'aren’t → don’t'),
         ('We visit grandma this weekend.', 'We are visiting grandma this weekend.', 'visit → are visiting'), ('Does he listen to music in his room yesterday?', 'Did he listen to music in his room yesterday?', 'Does → Did'),
         ('Do they play basketball after school yesterday?', 'Did they play basketball after school yesterday?', 'Do → Did')],
    reading=dict(kind='open', passage='These are my friends from Camp Wannabe. In the first picture, you can see Ian and Anne. They are from Ireland. I like them a lot. They’re really nice, and I had a lot of fun with them at the camp. In the second picture, you can see a boy from Poland. His name is Tomas. He’s a very honest boy, and he’s learning English, just like me! He likes playing ice hockey a lot. The girl in the third picture is Kim. She lives in Australia with her family, but her aunt lives in England. I don’t see her because she lives far away, but we chat on the Internet.',
                 qs=[('Who is in the first picture from Camp Wannabe?', 'Ian and Anne from Ireland.'), ('What can you say about Ian and Anne?', 'They are really nice, and I had a lot of fun with them at the camp.'),
                     ('Who is in the second picture and where is he from?', 'Tomas from Poland.'), ('What do we know about Tomas?', 'He is a very honest boy and enjoys playing ice hockey.'),
                     ('Who is the girl in the third picture and where is she from?', 'The girl is Kim, and she lives in Australia with her family.')]),
    order=[(['Do', 'go', 'we', 'on', 'swimming', 'Saturdays?'], 'Do we go swimming on Saturdays?'), (['walk', 'Does', 'in', 'he', 'the', 'school', 'to', 'morning?'], 'Does he walk to school in the morning?'),
           (['in', 'He', 'right', 'is', 'the', 'pool', 'swimming', 'now.'], 'He is swimming in the pool right now.'), (['a', 'They', 'watch', 'last', 'didn\'t', 'movie', 'Friday.'], 'They didn\'t watch a movie last Friday.'),
           (['didn\'t', 'The', 'brightly', 'shine', 'Sun', 'yesterday.'], 'The Sun didn\'t shine brightly yesterday.')],
    rewrite=[('Mr. Ba rides his motorbike to work every day.', 'Mr. Ba gets …', 'Mr. Ba gets to work by motorbike every day.'), ('My school has six hundred students.', 'There …', 'There are six hundred students in my school.'),
             ('Julia is Jack’s sister.', 'Jack …', 'Jack\'s sister is Julia.'), ('The supermarket is behind the bank.', 'The bank …', 'The bank is in front of the supermarket.'),
             ('The children are walking to school now.', 'The children are going to …', 'The children are going to school on foot now.')])


def build_b(n):
    E = EXAMS[n]
    tag = 'hsg_b%d' % n
    ex = Exam(tag, 'HSG', 'HSG – Bộ đề ôn thi – Đề %d' % n, 'x', slug='test%02d' % n, minutes=40, warn_at=5)
    # I. odd one out
    rows, keys = E['odd']
    rr, kk = [], ''
    for r, k in zip(rows, keys):
        if r is None or k == 'X': continue
        rr.append(r); kk += k
    ex.mcq_words('a', 'I. Circle the odd one out. (Chọn từ khác loại.)', rr, kk, q=ODD_Q)
    # II. pronunciation
    rows, keys = E['pron']
    rr, kk = [], ''
    for r, k in zip(rows, keys):
        if r is None or k == 'X': continue
        rr.append([U_(w, 0) for w in r]); kk += k
    ex.mcq_words('b', 'II. Circle the word which has the underlined part pronounced differently from the others. (Chọn từ có phần gạch chân phát âm khác.)', rr, kk, q=PRON_Q)
    # III. grammar MCQ
    qs, keys = E['grammar']
    items = []
    for (q, o), k in zip(qs, keys):
        items.append(({'t': 'mcq', 'q': q, 'o': o}, k, 'Đáp án: %s. %s' % (k, o['ABCD'.index(k)])))
    ex.add('c', 'III. Circle the word or phrase that best completes the sentence. (Chọn từ/cụm từ đúng.)', items)
    # IV. verb forms
    items = []
    for q, a in E['verbs']:
        ans = {'blanks': [[x] for x in a]}
        items.append(({'t': 'fill', 'q': q}, ans, 'Đáp án: ' + ' / '.join(a)))
    ex.add('d', 'IV. Put the verbs in brackets into the correct form. (Chia động từ trong ngoặc.)', items)
    # V. match
    left, opts, keys = E['match']
    ex.match('e', 'V. Match the questions with the answers. (Nối câu hỏi với câu trả lời.)', [{'t': l} for l in left], opts, [opts['ABCDE'.index(k)] for k in keys],
             exp='; '.join('%d–%s' % (i + 1, k) for i, k in enumerate(keys)) + ' (theo đáp án của đề).')
    # VI. find and correct
    items = []
    for wrong, right, note in E['fix']:
        items.append(({'t': 'fill', 'q': 'Câu sai: <i>%s</i><br>Viết lại câu đúng: {_}' % wrong}, [right], 'Sửa lỗi: %s. Câu đúng: %s' % (note, right)))
    ex.add('wrfix', 'VI. Find and correct the mistakes in each sentence. (Tìm lỗi sai và viết lại câu đúng.)', items)
    # VII. reading
    R = E['reading']
    pas = '<p>%s</p>' % R['passage']
    if R['kind'] == 'cloze':
        ex.fill('f', 'VII. Read the passage. Then, fill in the blanks with suitable words in the box. (Điền từ trong khung vào chỗ trống.)',
                [('Chỗ trống (%d): {_}' % (i + 1), [a], None, 'Đáp án: %s' % a) for i, a in enumerate(R['ans'])], passage=pas, bank=R['bank'])
    elif R['kind'] == 'mcq2':
        items = []
        for q, o, k in R['qs']:
            items.append(({'t': 'mcq', 'q': q, 'o': o}, k, 'Đáp án: %s. %s' % (k, o['AB'.index(k)])))
        ex.add('f', 'VII. Read the passage and circle the correct answers. (Đọc đoạn văn và chọn đáp án đúng.)', items, passage=pas)
    elif R['kind'] == 'tf':
        ex.tf('f', 'VII. Read the passage. Decide whether the sentences are true (T) or false (F). (Đọc đoạn văn, chọn True/False.)', [(q, a) for q, a in R['qs']], passage=pas)
    else:   # open: đáp án mẫu theo key của đề (không chấm điểm)
        items = [({'t': 'open', 'q': q}, None, 'Đáp án mẫu (theo đáp án của đề): <b>%s</b>' % a) for q, a in R['qs']]
        ex.add('f', 'VII. Read the passage and answer the questions. (Đọc đoạn văn và trả lời câu hỏi – đối chiếu đáp án mẫu sau khi nộp.)', items, passage=pas)
    # VIII. reorder
    for w, s in E['order']:
        assert sorted(' '.join(w).lower().split()) == sorted(s.lower().split()), (n, w, s)
    ex.order('g', 'VIII. Reorder the words to make correct sentences. (Sắp xếp từ thành câu đúng.)', E['order'])
    # IX. rewrite (mở -> đáp án mẫu)
    items = [({'t': 'open', 'q': 'Viết lại câu sao cho nghĩa không đổi:<br><i>%s</i><br><b>%s</b>' % (a, b)}, None, 'Đáp án mẫu (theo đáp án của đề): <b>%s</b>' % c) for a, b, c in E['rewrite']]
    ex.add('h', 'IX. Rewrite the following sentences in such another way which has the same meaning as the first one. (Viết lại câu – đối chiếu đáp án mẫu sau khi nộp.)', items)
    for iid in [k for k, v in ex.ANS.items() if v is None]: del ex.ANS[iid]   # câu mở: không chấm
    for key in ('fix_dropped', 'pron_dropped', 'odd_dropped', 'verbs_dropped'):
        if E.get(key): ex.notes.append('bỏ ' + E[key])
    ex.notes.append('mục mở (VII/IX): đáp án mẫu, không chấm')
    ex.save()
    NOTES.extend('B%d: %s' % (n, x) for x in ex.notes)


if __name__ == '__main__':
    build_a()
    for i in range(1, 6): build_b(i)
    print('\n'.join(NOTES))
