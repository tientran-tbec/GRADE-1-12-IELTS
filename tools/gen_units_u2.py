"""Chuyển đổi 1 lần: Word Unit 2 -> units/lop11_u2_botro.py (khung câu hỏi). Đáp án ở *_dapan.py (soạn tay)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import parse_mcq, cl
from theory import theory_html
import gen_units as G
from gen_units import mk_mcq, fill_numbered, groups_from_events, passage_group, keepu, dump

ROOT = G.ROOT
BR = open(os.path.join(ROOT, 'src/u2/botro.txt')).read().replace('16.<u> </u>', '16. ').split('\n')


def rng(a, b):
    return BR[a - 1:b]


def items_of(ev):
    return [v for k, v in ev if k == 'item']


def err3(gid, lines, start=1, prefix=None):
    """câu tìm lỗi dạng (A) <u>..</u> (B) <u>..</u> ..."""
    out = []
    for ln in lines:
        t = cl(ln)
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if not m:
            continue
        n = int(m.group(1)); s = m.group(2)
        s = re.sub(r'</u>\s*<u>', ' ', s)
        segs = []

        def rep(mm):
            segs.append(mm.group(2).strip())
            return '<u>%s</u><sup>%s</sup>' % (mm.group(2).strip(), mm.group(1))
        s2 = re.sub(r'\(([A-D])\)\s*<u>(.*?)</u>', rep, s)
        out.append({'id': '%s.%d' % (gid, n if prefix else len(out) + start), 't': 'mcq', 'q': keepu(s2), 'o': segs})
    return out


def build():
    th_a = next(i for i, l in enumerate(BR) if 'PART I. VOCABULARY' in l)
    th_b = next(i for i, l in enumerate(BR) if 'A. PHONETIC' in l)
    theory = theory_html(BR[th_a:th_b], '')
    pages = []

    # ---- Phonetic
    ex1 = ''.join('<li>%s</li>' % cl(l)[cl(l).index(' ') + 1:] for l in rng(477, 486))
    note = ('<p class="note"><b>Quy tắc dạng yếu / dạng mạnh:</b> trợ động từ, dạng rút gọn (<i>\'re, \'s, \'ve, don\'t, haven\'t…</i>) '
            'đọc <b>yếu</b> khi đứng giữa câu và đọc <b>mạnh</b> khi đứng cuối câu trả lời ngắn hoặc cần nhấn mạnh. '
            'Hãy gạch chân dạng yếu, gạch đôi dạng mạnh rồi luyện đọc theo cặp (không chấm điểm).</p><ol class="ex">%s</ol>' % ex1)
    ph2 = parse_mcq(rng(488, 497)); ph3 = parse_mcq(rng(499, 508))
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'ph1', 'instr': 'Exercise 1: Underline the weak form and double underline the strong form of the contracted forms in the following sentences. Then practise them with your partner (luyện đọc – không chấm điểm).', 'note': note, 'items': []},
        {'id': 'ph2', 'instr': 'Exercise 2: Mark the letter A, B, C, or D to indicate the word whose underlined part differs from the other three in pronunciation.', 'items': mk_mcq('ph2', items_of(ph2))},
        {'id': 'ph3', 'instr': 'Exercise 3: Mark the letter A, B, C, or D to indicate the word that differs from the other three in the position of primary stress.', 'items': mk_mcq('ph3', items_of(ph3))},
    ]})

    # ---- Vocabulary & grammar
    vg1 = fill_numbered('vg1', rng(519, 528))
    vg2 = mk_mcq('vg2', items_of(parse_mcq(rng(530, 609))))
    vg2[4]['o'][3] = 'quarrel'            # nguồn bị cắt "qua"
    vg2[6]['o'] = ['distance', 'gap', 'space', 'All are correct']  # nguồn bị cắt "All are co"
    vg3 = fill_numbered('vg3', rng(611, 616))
    for it in vg3:
        it['q'] = it['q'].replace('{_}', '{_}')
    vg4_src = [
        ('In a library, students ______ borrow up to six books.', ['may', 'must']),
        ('In an exam, students ______ answer all the questions.', ['must', "mustn't"]),
        ('To ride a motorbike, students ______ be over 16 years old.', ['must', 'have to']),
        ('In a hotel, guests ______ use the exit only in an emergency.', ['must', 'have to']),
        ('In a park, you ______ walk on the grass.', ['must', "mustn't"]),
        ('On a bus, you ______ talk to the driver.', ['must', "mustn't"]),
    ]
    vg4 = [{'id': 'vg4.%d' % i, 't': 'mcq', 'q': q, 'o': o, 'plain': True} for i, (q, o) in enumerate(vg4_src, 1)]
    vg5 = mk_mcq('vg5', items_of(parse_mcq(rng(625, 644))))
    vg6 = mk_mcq('vg6', items_of(parse_mcq(rng(646, 665))))
    vg7 = err3('vg7', rng(667, 676))
    vg8_src = [
        ('You ______ eat anything you don\'t like.', ["don't have to", 'must']),
        ("If you don't want to have a sore throat, you ______ to drink too much iced water.", ["don't have to", "oughtn't"]),
        ('Flight attendants ______ take care of passengers on the plane.', ['have to', "mustn't"]),
        ('During the lesson, students ______ leave class without the teacher\'s permission.', ["don't have to", "mustn't"]),
        ('Her mother cooks for her, so she herself ______ cook.', ["doesn't have to", "mustn't"]),
        ('Smokers ______ smoke in public places. This is stated in a new law.', ["don't have to", "mustn't"]),
        ('Drinks are free for today. It means that you ______ pay money for drinks today.', ["don't have to", "mustn't"]),
        ('Kelvin won the lottery last year, so he ______ work now.', ["doesn't have to", "mustn't"]),
        ('According to the company regulations, staff ______ finish their work with highest efficiency.', ['have to', 'must']),
        ('To be healthy, we ______ eat healthful food and do the exercise regularly.', ["mustn't", 'ought to']),
    ]
    vg8 = [{'id': 'vg8.%d' % i, 't': 'mcq', 'q': q, 'o': o, 'plain': True} for i, (q, o) in enumerate(vg8_src, 1)]

    def rw(gid, rows):
        return [{'id': '%s.%d' % (gid, i), 't': 'fill', 'q': '%s <b>(%s)</b><br>%s {_}' % (s1, w, stem)} for i, (s1, w, stem) in enumerate(rows, 1)]
    vg9 = rw('vg9', [
        ('If I were you, I would spend more time talking with my children.', 'should', 'You'),
        ("John doesn't get permission to use that computer.", "mustn't", 'John'),
        ('It is necessary that people who work here leave by 6 p.m.', 'must', 'People who work here'),
        ("Every staff isn't allowed to smoke or eat in the office.", "mustn't", 'Every staff'),
        ('It is forbidden for students to cheat in the exam.', "mustn't", 'Students'),
        ('Ms. Ly is in charge of cleaning the floor every day.', 'has to', 'Ms. Ly'),
        ('You are not allowed to take photographs in the museum.', "mustn't", 'You'),
        ('It is not necessary for Jack to call Ben today.', "doesn't have to", 'Jack'),
    ])
    vg10 = rw('vg10', [
        ('I will tell you my secret, but you tell anyone.', "mustn't", 'I will tell you'),
        ('You spend too much time playing computer games. You stop that.', 'must', 'You spend'),
        ('We wear helmets when we ride a motorbike.', 'have to', 'We'),
        ('I book the tickets in advance.', "don't have to", 'I'),
        ('Alia, you say rude words like that.', "mustn't", 'Alia, you'),
        ('We play table tennis. We can play chess instead.', "don't have to", 'We'),
        ('Children put their hands into sockets. That is very dangerous.', "mustn't", 'Children'),
        ('Doctors sometimes work at the weekends and on national holidays.', 'have to', 'Doctors sometimes'),
    ])
    vg11 = rw('vg11', [
        ("It's necessary for you to finish your homework before going to bed.", 'must', 'You'),
        ("It isn't necessary for you to bring food and drink for lunch.", 'have to', 'You'),
        ('Fishing is not allowed in this park.', 'must', 'You'),
        ('Every receptionist in our hotel is obliged to wear a uniform.', 'have to', 'Every receptionist'),
        ("It's forbidden to sell cigarettes to children.", 'must not', 'Shops'),
        ("It's obligatory for every employee to keep the company's information secret.", 'have to', 'Every employee'),
    ])
    pages.append({'id': 'tu-vung-ngu-phap', 'title': 'Từ vựng & Ngữ pháp', 'mode': 'practice', 'groups': [
        {'id': 'vg1', 'instr': 'Exercise 1: Complete the sentences with the words given.',
         'bank': ['choice', 'culture', 'historical', 'influence', 'lifestyle', 'social', 'suit', 'traditional', 'view', 'characteristics'], 'items': vg1},
        {'id': 'vg2', 'instr': 'Exercise 2: Mark the letter A, B, C, or D to indicate the correct answer to each of the following questions.', 'items': vg2},
        {'id': 'vg3', 'instr': 'Exercise 3: Complete the sentences with should or shouldn\'t.', 'items': vg3},
        {'id': 'vg4', 'instr': 'Exercise 4: Choose the correct modal verb to complete the sentences.', 'items': vg4},
        {'id': 'vg5', 'instr': 'Exercise 5: Mark the letter A, B, C, or D to indicate the word(s) CLOSEST in meaning to the underlined word(s).', 'items': vg5},
        {'id': 'vg6', 'instr': 'Exercise 6: Mark the letter A, B, C, or D to indicate the word(s) OPPOSITE in meaning to the underlined word(s).', 'items': vg6},
        {'id': 'vg7', 'instr': 'Exercise 7: Mark the letter A, B, C, or D to indicate the underlined part that needs correction.', 'items': vg7},
        {'id': 'vg8', 'instr': 'Exercise 8: Choose the correct modal verb (loại bỏ phương án sai – "cross out the wrong part").', 'items': vg8},
        {'id': 'vg9', 'instr': 'Exercise 9: Rewrite each sentence using the word(s) in the brackets, without changing its meaning.', 'items': vg9},
        {'id': 'vg10', 'instr': 'Exercise 10: Rewrite the sentences and add the given modal verb at the appropriate position (viết phần còn lại của câu).', 'items': vg10},
        {'id': 'vg11', 'instr': 'Exercise 11: Rewrite the sentences with the same meaning, using the given words and the correct form of the modal verbs in brackets.', 'items': vg11},
    ]})

    # ---- Listening
    def tf(gid, qs):
        return [{'id': '%s.%d' % (gid, i), 't': 'tf', 'q': q} for i, q in enumerate(qs, 1)]
    li1 = tf('li1', ["Linda's parents are pleased with her choice of clothes.", "Tom shares Linda's opinion on clothes.",
                     'Linda wants to look more fashionable.', "Tom's parents don't let him play computer games.",
                     'Playing computer games is a form of relaxation for Tom.'])
    li2 = tf('li2', ['Parents sometimes find it hard to talk to their teenage children.', 'Teenagers always like talking about their school work.',
                     'Teenagers hate questions that aim to check up on them.', 'Parents should push their teenage children to talk about school, work and future plans, if necessary.',
                     'Parents should watch for danger signs in some teenagers who may smoke or try using drugs or alcohol.'])
    pages.append({'id': 'nghe', 'title': 'Nghe', 'mode': 'practice', 'audio': 'bt_nghe.mp3', 'groups': [
        {'id': 'li1', 'instr': 'Exercise 1: Listen to the conversation. Decide if the following sentences are true (T) or false (F).', 'items': li1},
        {'id': 'li2', 'instr': 'Exercise 2: Listen to the recording about relationship problems between parents and teenage children. Decide whether the following statements are true (T) or false (F) according to the speaker.', 'items': li2},
    ]})

    # ---- Speaking
    sp1_q = ["My parents don't let me do what I want.", 'My parents want me to follow in their footsteps.', 'Do you help with housework?',
             'Is there any generation gap in your family?', 'How can I make my own decisions?', 'Are there any ways to avoid conflicts and arguments in the family?',
             "My parents don't allow me to play computer games!", 'My mother dressed badly and had an ugly hairstyle yesterday, Dad.',
             'Who do you talk with when you have problems?', 'Should I tell my parents before I make important decisions?']
    sp1_o = [['I think you have supportive parents.', 'I think they should respect your privacy.'],
             ["They walk fast - you can't catch them up.", 'I think you have your own dreams of job.'],
             ['Certainly. All of us share the chores.', "My parents say I don't study enough."],
             ['No. I live in a nuclear family.', 'No. My parents are very understanding.'],
             ['You try to explain them to your parents.', 'Your parents will respect your privacy.'],
             ['You should set the family rules.', "There are only trivial things. Don't worry."],
             ['You can do it when you finish homework.', "You needn't ask their permission."],
             ["She looked younger and nicer, didn't she?", 'No. They were popular 20 years ago.'],
             ['Only serious problems.', 'My mum, of course.'],
             ["Of course. It's a must.", "Certainly. You're mature enough."]]
    sp1 = [{'id': 'sp1.%d' % i, 't': 'mcq', 'q': '<b>A:</b> %s<br><b>B:</b> ______' % q, 'o': o} for i, (q, o) in enumerate(zip(sp1_q, sp1_o), 1)]
    resp = [cl(l)[3:].strip() for l in rng(976, 982) if re.match(r'^<b>[A-G]\.</b>', l)]
    resp = []
    for l in rng(976, 984):
        m = re.match(r'^<b>([A-G])\.</b>\s*(.*)$', l)
        if m:
            resp.append(cl(m.group(2)))
    assert len(resp) == 7, resp
    conv = ('<p><b>Sam:</b> Nick, what fights are there between a teenager and the parents?</p><p><b>Nick:</b> (1) ______</p>'
            '<p><b>Sam:</b> Right. Our parents often make decisions about everything in our lives.</p>'
            '<p><b>Nick:</b> It\'s a good thing because small kids need this kind of protection and assistance. (2) ______</p>'
            '<p><b>Sam:</b> I agree with you. When we grow up, we can make our own decisions. Our parents aren\'t used to the new situation yet. They only know us as the kid who had everything decided and didn\'t mind.</p>'
            '<p><b>Nick:</b> (3) ______. We want to cover our walls with new posters but they don\'t understand why we don\'t like the childish wallpaper anymore.</p>'
            '<p><b>Sam:</b> Clashes like these small things are very common between teens and parents.</p><p><b>Nick:</b> (4) ______</p>'
            '<p><b>Sam:</b> That\'s right. And parents also get angry because they disagree with the teen decisions.</p><p><b>Nick:</b> (5) ______</p>')
    bank_html = '<div class="note"><b>Responses:</b><ol type="A">%s</ol></div>' % ''.join('<li>%s</li>' % r for r in resp)
    conv = bank_html + conv
    sp2 = [{'id': 'sp2.%d' % i, 't': 'mcq', 'q': 'Chỗ trống (%d) – chọn A–G' % i, 'o': list('ABCDEFG'), 'plain': True} for i in range(1, 6)]
    sp3 = mk_mcq('sp3', items_of(parse_mcq(rng(1036, 1072))))
    pages.append({'id': 'noi', 'title': 'Nói (hội thoại)', 'mode': 'practice', 'groups': [
        {'id': 'sp1', 'instr': 'Exercise 1: Choose the correct response. Then practice the short exchanges in pairs.', 'items': sp1},
        {'id': 'sp2', 'instr': 'Exercise 2: Complete the conversation about fights between teenagers and their parents, using the responses (A–G) given. There are two extra ones.', 'passage': conv, 'items': sp2},
        {'id': 'sp3', 'instr': 'Exercise 3: Circle A, B, C, or D to indicate the correct response to each of the following exchanges.', 'items': sp3},
    ]})

    # ---- Reading
    P = lambda a, b: ''.join('<p>%s</p>' % keepu(cl(l)) for l in rng(a, b) if cl(l))
    re1a = passage_group('re1a', 'Exercise 1a: Read the passage and choose the word or phrase that best fits each numbered blank (1–5).', parse_mcq(rng(1079, 1083), expect=1))
    for _g in (re1a,):
        for _i, _it in enumerate(_g['items'], 1):
            _it['q'] = 'Blank (%d)' % _i
    re1a['passage'] = '<h4>Generation Gap</h4>' + P(1077, 1078)
    re1b = passage_group('re1b', 'Exercise 1b: Read the passage and choose the word or phrase that best fits each numbered blank (1–5).', parse_mcq(rng(1085, 1089), expect=1))
    for _i, _it in enumerate(re1b['items'], 1):
        _it['q'] = 'Blank (%d)' % _i
    re1b['passage'] = '<h4>Peer Pressure</h4>' + P(1084, 1084)
    re2a = passage_group('re2a', 'Exercise 2a: Read the passage and choose the correct answer to each question (1–5).', parse_mcq(rng(1093, 1108), expect=1))
    re2a['passage'] = P(1091, 1092)
    re2b = passage_group('re2b', 'Exercise 2b: Read the passage and choose the correct answer to each question (1–5).', parse_mcq(rng(1112, 1129), expect=1))
    re2b['passage'] = P(1109, 1111)
    re2c = passage_group('re2c', 'Exercise 2c: Read the passage and choose the correct answer to each question (1–5).', parse_mcq(rng(1138, 1160), expect=1))
    re2c['passage'] = '<h4>Dating Customs Around the World</h4>' + P(1132, 1137)
    re3_st = [re.sub(r'\s*_{3,}\s*$', '', re.sub(r'^\d+\.\s*', '', cl(l))) for l in rng(1166, 1171)]
    re3 = {'id': 're3', 'instr': 'Exercise 3: Read the passage, and then decide whether the statements are true (T) or false (F).', 'passage': P(1162, 1165),
           'items': [{'id': 're3.%d' % i, 't': 'tf', 'q': q} for i, q in enumerate(re3_st, 1)]}
    re4_q = [re.sub(r'^\d+\.\s*', '', cl(l)) for l in rng(1177, 1189) if re.match(r'^\d+\.', cl(l))]
    re4 = {'id': 're4', 'instr': 'Exercise 4: Read the passage about family rules, and then answer the questions (tự luận – đối chiếu đáp án mẫu).', 'passage': '<h4>Family rules</h4>' + P(1173, 1176),
           'items': [{'id': 're4.%d' % i, 't': 'open', 'q': q} for i, q in enumerate(re4_q, 1)]}
    pages.append({'id': 'doc', 'title': 'Đọc hiểu', 'mode': 'practice', 'groups': [re1a, re1b, re2a, re2b, re2c, re3, re4]})

    # ---- Writing
    halves = [re.sub(r'^\d+\.\s*', '', cl(l)) for l in rng(1194, 1198)]
    ends = []
    for l in rng(1199, 1203):
        m = re.match(r'^_+\s*<b>[A-E]\.</b>\s*(.*)$', l.replace('\t', ' ').strip())
        ends.append(cl(m.group(1)))
    wr1 = [{'id': 'wr1.%d' % i, 't': 'mcq', 'q': h + ' ______', 'o': ends} for i, h in enumerate(halves, 1)]
    ph = []
    for l in rng(1205, 1210):
        m = re.match(r'^<b>([A-F])\.</b>\s*(.*)$', l)
        ph.append(cl(m.group(2)))
    assert len(ph) == 6
    essay = cl(BR[1210]) + ' ' + cl(BR[1211]) + ' ' + cl(BR[1212])
    essay = re.sub(r'\((\d)\)\s*_+', r'<b>(\1) ______</b>', ' '.join(cl(l) for l in rng(1211, 1213)))
    essay = '<div class="note"><b>Phrases:</b><ol type="A">%s</ol></div><p>%s</p>' % (''.join('<li>%s</li>' % x for x in ph), essay)
    wr2 = [{'id': 'wr2.%d' % i, 't': 'mcq', 'q': 'Chỗ trống (%d) – chọn A–F' % i, 'o': list('ABCDEF'), 'plain': True} for i in range(1, 7)]
    pages.append({'id': 'viet', 'title': 'Viết', 'mode': 'practice', 'groups': [
        {'id': 'wr1', 'instr': 'Exercise 1: Match the first halves to the second ones to make meaningful sentences.', 'items': wr1},
        {'id': 'wr2', 'instr': "Exercise 2: Complete the opinion essay about limiting teenagers' screen time with the phrases given.", 'passage': essay, 'items': wr2},
        {'id': 'wr3', 'instr': "Exercise 3: Write an opinion essay (120–150 words) about limiting teenagers' screen time (tự luận – xem bài mẫu).",
         'items': [{'id': 'wr3.1', 't': 'open', 'q': "Write an opinion essay (120–150 words) limiting teenagers' screen time."}]},
    ]})

    # ---- Test (50 câu)
    ev = parse_mcq(rng(1236, 1326))
    groups = groups_from_events('kt', ev)
    for g in groups:
        for it in g['items']:
            it.pop('_n', None)
    last = max(int(it['id'].split('.')[1]) for g in groups for it in g['items'])
    assert last == 34, last
    e = err3('kt', rng(1328, 1333), prefix=True)
    for it in e:
        n = int(it['id'].split('.')[1])
        it['id'] = 'kt.%d' % (n)
    groups.append({'id': 'kt-er', 'instr': 'Find the mistakes in the following sentences and correct them (mark the underlined part that needs correction).', 'passage': '', 'items': e})
    rwi = []
    for a, b in [(1335, 1336), (1337, 1338), (1339, 1340), (1341, 1342), (1343, 1344)]:
        t = cl(BR[a - 1]); m = re.match(r'^(\d+)\.\s*(.*)$', t)
        rwi.append({'id': 'kt.%s' % m.group(1), 't': 'fill', 'q': m.group(2) + '<br>' + cl(BR[b - 1]) + ' {_}'})
    groups.append({'id': 'kt-rw', 'instr': 'Complete the second sentence so that it has the same meaning as the first one.', 'passage': '', 'items': rwi})
    cue = []
    for k in range(1347, 1367):
        t = cl(BR[k - 1])
        m = re.match(r'^(\d+)\.\s*(.*)$', t)
        if m:
            cue.append({'id': 'kt.%s' % m.group(1), 't': 'fill', 'q': m.group(2) + '<br>Viết thành câu hoàn chỉnh: {_}'})
    assert len(cue) == 5, len(cue)
    groups.append({'id': 'kt-cue', 'instr': 'Write the tips for limiting teenagers\' screen time. You can add some more necessary words, but you have to use all the words given.', 'passage': '<h4>Tip for Limiting Screen Time</h4>', 'items': cue})
    pages.append({'id': 'kiem-tra', 'title': 'Bài kiểm tra Unit 2 (50 câu)', 'mode': 'test', 'minutes': 50, 'groups': groups})

    return {'id': 'lop11-u2-botro', 'title': 'Unit 2 – The generation gap: Bài tập bổ trợ', 'grade': 11, 'unit': 2, 'theory': theory, 'pages': pages}


KR = open(os.path.join(ROOT, 'src/u2/4kn.txt')).read().split('\n')


def kr(a, b):
    return KR[a - 1:b]


def KP(a, b):
    return ''.join('<p>%s</p>' % keepu(cl(l)) for l in kr(a, b) if cl(l) and not cl(l).startswith('Source:'))


def build_4kn():
    th_b = next(i for i, l in enumerate(KR) if 'B. THỰC' in l)
    theory = theory_html(KR[:th_b], '')
    pages = []
    ev1 = parse_mcq(kr(974, 983), expect=1); ev2 = parse_mcq(kr(986, 995), expect=1)
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'pr1', 'instr': 'Task 1. Find the word whose underlined part differs from the other three in pronunciation.', 'items': mk_mcq('pr1', items_of(ev1))},
        {'id': 'pr2', 'instr': 'Task 2. Find the word that differs from the other three in the position of stress.', 'items': mk_mcq('pr2', items_of(ev2))},
    ]})
    defs = []
    for l in kr(1003, 1050):
        t = cl(l)
        m = re.match(r'^([a-j])\.\s*(.*)$', t)
        if m:
            defs.append((m.group(1), m.group(2)))
    terms = []
    for l in kr(1003, 1050):
        m = re.match(r'^\s*(\d+)\.\s*(.*)$', cl(l))
        if m and int(m.group(1)) <= 10 and not re.match(r'^[a-j]\.', cl(l)):
            terms.append(m.group(2))
    assert len(defs) == 10 and len(terms) == 10, (len(defs), len(terms))
    dl = '<div class="note"><ol type="a">%s</ol></div>' % ''.join('<li>%s</li>' % d for _, d in defs)
    vo1 = [{'id': 'vo1.%d' % i, 't': 'mcq', 'q': '<b>%s</b> – chọn a–j' % t, 'o': [x for x, _ in defs], 'plain': True} for i, t in enumerate(terms, 1)]
    vo2 = fill_numbered('vo2', kr(1054, 1063))
    vo3 = mk_mcq('vo3', items_of(parse_mcq(kr(1066, 1085), expect=1)))
    vo4 = mk_mcq('vo4', items_of(parse_mcq(kr(1088, 1097), expect=1)))
    vo5 = G.plain_fill('vo5', kr(1099, 1108))
    vo6_src = [('The new generation has the potential to ______ great things with their skills and determination.', ['achieve', 'allow']),
               ('The older generation should not ______ their beliefs and ideas upon the younger generation.', ['force', 'upset']),
               ('The younger generation prioritises ______ opportunities such as higher study.', ['technological', 'educational']),
               ("It is important for teenagers to ask for their parents' ______ before going out late.", ['career', 'permission']),
               ('Unhealthy eating habits and lack of physical activity can contribute to weight ______ in children.', ['gain', 'control'])]
    vo6 = [{'id': 'vo6.%d' % i, 't': 'mcq', 'q': q, 'o': o, 'plain': True} for i, (q, o) in enumerate(vo6_src, 1)]
    pages.append({'id': 'tu-vung', 'title': 'Từ vựng', 'mode': 'practice', 'groups': [
        {'id': 'vo1', 'instr': 'Task 1. Match the words on the left with their meanings on the right (chọn chữ cái a–j).', 'passage': dl, 'items': vo1},
        {'id': 'vo2', 'instr': 'Task 2. Complete the following sentences with suitable words from Task 1.', 'bank': terms[:], 'items': vo2},
        {'id': 'vo3', 'instr': 'Task 3. Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.', 'items': vo3},
        {'id': 'vo4', 'instr': 'Task 4. Choose the word(s) OPPOSITE in meaning to the underlined word(s) in each of the following questions.', 'items': vo4},
        {'id': 'vo5', 'instr': 'Task 5. Complete the sentences using the correct form of the words in brackets.', 'items': vo5},
        {'id': 'vo6', 'instr': 'Task 6. Choose the correct word or phrase to complete the sentences.', 'items': vo6},
    ]})
    gr1_src = [("Children ______ recognize the importance of family traditions and cultural values, even if they may seem outdated in the modern world.", ['must', "mustn't"]),
               ('Grandparents ______ learn how to use smartphones or social media to stay connected with their grandchildren.', ["shouldn't", 'should']),
               ('Children ______ respect old people because they have lots of life experiences.', ['have to', "don't have to"]),
               ('Parents ______ force their children to follow their jobs; instead, they should give advice and let their children choose their own careers.', ["mustn't", "don't have to"]),
               ("Older generations ______ rely on physical newspapers or books for information, but today's youth don't have to, thanks to the internet.", ['must', 'had to']),
               ("Teenagers ______ appreciate the efforts their parents make for them, even if they don't always agree.", ['must', "mustn't"]),
               ("Teenagers ______ listen to their parents' advice and guidance, as they can help them overcome difficult situations.", ['should', "shouldn't"]),
               ('In previous generations, women had to follow specific gender roles, but today they ______ limit their dreams and can pursue any career they like.', ["don't have to", "mustn't"])]
    gr1 = [{'id': 'gr1.%d' % i, 't': 'mcq', 'q': q, 'o': o, 'plain': True} for i, (q, o) in enumerate(gr1_src, 1)]
    gr2 = mk_mcq('gr2', items_of(parse_mcq(kr(1129, 1138), expect=1)))
    gr3 = []
    for ln in (1141, 1143, 1145, 1147, 1149):
        t = cl(KR[ln - 1]); m = re.match(r'^(\d+)\.\s*(.*)$', t); s = m.group(2)
        segs = re.findall(r'<u>(.*?)</u>', s)
        assert len(segs) == 4, segs
        it = iter('ABCD')
        s2 = re.sub(r'<u>(.*?)</u>', lambda mm: '<u>%s</u><sup>%s</sup>' % (mm.group(1), next(it)), s)
        gr3.append({'id': 'gr3.%s' % m.group(1), 't': 'mcq', 'q': keepu(s2), 'o': [x.strip() for x in segs]})
    pages.append({'id': 'ngu-phap', 'title': 'Ngữ pháp', 'mode': 'practice', 'groups': [
        {'id': 'gr1', 'instr': 'Task 1. Choose the appropriate modal verb.', 'items': gr1},
        {'id': 'gr2', 'instr': 'Task 2. Choose the correct answers.', 'items': gr2},
        {'id': 'gr3', 'instr': 'Task 3. Mark the letter A, B, C or D to indicate the mistake in each of the following sentences (rồi tự sửa lại cho đúng).', 'items': gr3},
    ]})
    re1 = {'id': 're1', 'instr': 'Task 1. Read the following passage and mark the letter A, B, C or D to indicate the correct word that best fits each of the numbered blanks.',
           'passage': KP(1154, 1157), 'items': mk_mcq('re1', items_of(parse_mcq(kr(1159, 1168), expect=1)))}
    for i, it in enumerate(re1['items'], 1):
        it['q'] = 'Blank (%d)' % i
    re2 = {'id': 're2', 'instr': 'Task 2. Read the following passage and choose the correct answer to each of the questions.', 'passage': KP(1171, 1175),
           'items': mk_mcq('re2', items_of(parse_mcq(kr(1177, 1192), expect=1)))}
    st = [re.sub(r'^\W*\d+\.\s*', '', cl(l)) for l in kr(1199, 1203)]
    re3 = {'id': 're3', 'instr': 'Task 3. Read the passage and decide whether the following statements are true (T), false (F) or not given (NG).', 'passage': KP(1195, 1198),
           'items': [{'id': 're3.%d' % i, 't': 'tfng', 'q': q} for i, q in enumerate(st, 1)]}
    pages.append({'id': 'doc', 'title': 'Đọc hiểu', 'mode': 'practice', 'groups': [re1, re2, re3]})
    wr1 = []
    for i, ln in enumerate((1207, 1209, 1211, 1213, 1215), 1):
        t = cl(KR[ln - 1]); m = re.match(r'^(.*?)\s*\((\d+) words\)$', t)
        wr1.append({'id': 'wr1.%d' % i, 't': 'fill', 'q': 'Từ cho sẵn: <i>%s</i><br>Câu hoàn chỉnh: {_}' % m.group(1), 'nwords': int(m.group(2))})
    wr2 = mk_mcq('wr2', items_of(parse_mcq(kr(1219, 1243), expect=1)))
    pages.append({'id': 'viet', 'title': 'Viết', 'mode': 'practice', 'groups': [
        {'id': 'wr1', 'instr': 'Task 1. Reorder the given words and phrases to form meaningful sentences.', 'items': wr1},
        {'id': 'wr2', 'instr': 'Task 2. Mark the letter A, B, C or D to indicate the sentence that is closest in meaning to each of the given sentences.', 'items': wr2},
        {'id': 'wr3', 'instr': 'Task 3. Write a paragraph (120–150 words) about this topic: "Parents should control their children\'s activities on social media. Do you agree or disagree with this statement?" (tự luận – xem bài mẫu).',
         'items': [{'id': 'wr3.1', 't': 'open', 'q': "Parents should control their children's activities on social media. Do you agree or disagree?"}]},
    ]})
    pages.append({'id': 'noi', 'title': 'Nói', 'mode': 'practice', 'groups': [
        {'id': 'sp1', 'instr': 'Task 1. Answer the following questions (luyện nói – đối chiếu câu trả lời mẫu).', 'items': [
            {'id': 'sp1.1', 't': 'open', 'q': 'How often do you spend time talking with your parents?'},
            {'id': 'sp1.2', 't': 'open', 'q': 'What are some differences in beliefs between you and your parents?'}]},
        {'id': 'sp2', 'instr': 'Task 2. Describe a time when you had a difficulty related to the generation gap in 2–3 minutes.', 'items': [
            {'id': 'sp2.1', 't': 'open', 'q': 'Describe a time when you had a difficulty related to the generation gap.'}]},
    ]})
    li1 = [{'id': 'li1.%d' % i, 't': 'mcq', 'q': 'Conflict: <b>%s</b> – speaker nào?' % c, 'o': ['Speaker A', 'Speaker B', 'Speaker C']}
           for i, c in enumerate(['Money management', 'Independence and control', 'Communication and understanding'], 1)]
    li2 = [{'id': 'li2.%d' % i, 't': 'tf', 'q': q} for i, q in enumerate([
        'Conflict with parents is common for everyone, including well-behaved individuals.',
        'Conflict with parents can lead to unhappiness and stress for both parties involved.',
        'Conflict with parents only impacts mental health.',
        "Teenagers should consider the reasons for their arguments with their parents and be in their parents' opinion.",
        'Teenagers should communicate with their parents instead of staying silent.'], 1)]
    pages.append({'id': 'nghe', 'title': 'Nghe', 'mode': 'practice', 'audio': 'kn_nghe.mp3', 'groups': [
        {'id': 'li1', 'instr': 'Task 1. Listen to three people talking about their conflict with their parents and decide which speaker mentions each conflict. You can listen to each recording TWICE.', 'items': li1},
        {'id': 'li2', 'instr': 'Task 2. Listen to a talk about teenagers\' conflict with their parents and decide if the following statements are true (T) or false (F).', 'items': li2},
    ]})
    ev_t = parse_mcq([l for l in kr(1321, 1494) if not cl(l).startswith('Source:')], expect=1)
    tg = groups_from_events('kt', ev_t)
    for g in tg:
        for it in g['items']:
            it.pop('_n', None)
    for g in tg:
        for it in g['items']:
            if it['id'] in ('kt.20', 'kt.21'):
                it['q'] = re.sub(r'\s+(Boy:|Father:|A:|B:)', r'<br><b>\1</b>', it['q'])
    pages.append({'id': 'kiem-tra', 'title': 'Bài kiểm tra Unit 2 (50 câu)', 'mode': 'test', 'minutes': 50, 'groups': tg})
    return {'id': 'lop11-u2-4kn', 'title': 'Unit 2 – The generation gap: Bài tập 4 kỹ năng', 'grade': 11, 'unit': 2, 'theory': theory, 'pages': pages}


if __name__ == '__main__':
    k = build_4kn()
    dump(os.path.join(ROOT, 'units/lop11_u2_4kn.py'), 'SET', k)
    for p in k['pages']:
        n = sum(len(g['items']) for g in p['groups'])
        print(p['id'], n, [(g['id'], len(g['items'])) for g in p['groups']])
    b = build()
    dump(os.path.join(ROOT, 'units/lop11_u2_botro.py'), 'SET', b)
    tot = 0
    for p in b['pages']:
        n = sum(len(g['items']) for g in p['groups']); tot += n
        print(p['id'], n, [(g['id'], len(g['items'])) for g in p['groups']])
    print('TOTAL', tot)
