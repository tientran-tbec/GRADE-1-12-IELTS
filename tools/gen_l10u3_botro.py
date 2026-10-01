"""Chuyển đổi 1 lần: Word Lớp 10 Unit 3 – Music (Bài tập bổ trợ) -> units/lop10_u3_botro.py (khung câu hỏi).
Nguồn src/l10u3/bt_c.txt: nửa đầu (đến dòng 'ĐÁP ÁN') = đề; nửa sau = khoá (⟦…⟧ tô màu).
Đáp án + giải thích: units/lop10_u3_botro_dapan.py (đối chiếu khoá Word và tự giải độc lập)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parse_src import parse_mcq, cl
import gen_units as G
from gen_units import mk_mcq, keepu, dump

ROOT = G.ROOT
RAW = open(os.path.join(ROOT, 'src/l10u3/bt_c.txt'), encoding='utf8').read().split('\n')
END = next(i for i, l in enumerate(RAW) if 'ĐÁP ÁN' in l)
BR = [re.sub(r'(Question \d+:\s*</b>)(\S)', r'\1 \2', l) for l in (x.replace('<b>A .</b>', '<b>A.</b>') for x in RAW[:END])]   # nguồn thiếu dấu cách sau 'Question 26:</b>'


def fnd(pat, start=1):
    for i in range(start - 1, len(BR)):
        if re.search(pat, BR[i]):
            return i + 1
    raise KeyError(pat)


def rng(a, b):
    return BR[a - 1:b]


def items_of(ev):
    return [v for k, v in ev if k == 'item']


def fixblank(s):
    s = re.sub(r'\s*_{3,}\s*', ' ______ ', s)
    s = re.sub(r'\s+([.,?!;:])', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def mcq(gid, lines, expect=1):
    its = items_of(parse_mcq(lines, expect=expect))
    out = mk_mcq(gid, its)
    for it in out:
        it['q'] = fixblank(it['q'])
        assert len(it['o']) == 4, it
    return out


def vocab():
    a = fnd(r'A\. VOCABULARY'); b = fnd(r'B\. GRAMMAR')
    L = [cl(l) for l in rng(a + 1, b - 1)]
    L = [l for l in L if l]
    i = 4  # bỏ tiêu đề bảng
    out = []
    while i < len(L):
        m = re.match(r'^(\d+)\.\s*(.+)$', L[i])
        assert m, L[i]
        w = m.group(2).strip(); ty = L[i + 1]; ipa = L[i + 2]; j = i + 3; vi = []
        while j < len(L) and not re.match(r'^\d+\.\s', L[j]):
            vi.append(L[j]); j += 1
        out.append((w, ty.strip('()'), ipa, ' '.join(vi)))
        i = j
    assert len(out) == 69, len(out)
    return out


def theory():
    h = '<p><b>A. VOCABULARY</b> (Từ vựng)</p><table class="th"><tr><th>Word</th><th>Type</th><th>Pronunciation</th><th>Meaning</th></tr>'
    for w, ty, ipa, vi in vocab():
        h += '<tr><td>%s</td><td>(%s)</td><td>%s</td><td>%s</td></tr>' % (w, ty, ipa, vi)
    h += '</table><p><b>B. GRAMMAR</b> (Ngữ pháp)</p>'
    h += '<p><b>I. COMPOUND SENTENCES (Câu ghép)</b></p>'
    h += ('<p><b>Câu ghép</b> là câu gồm 2 hoặc nhiều <b>mệnh đề độc lập</b>, nối với nhau bằng liên từ (conjunction): '
          '<b>Mệnh đề + LIÊN TỪ + Mệnh đề</b>. Các liên từ thường gặp (FANBOYS):</p>'
          '<table class="th"><tr><th>Liên từ</th><th>Nghĩa</th><th>Cách dùng</th></tr>'
          '<tr><td><b>F</b>or</td><td>bởi vì</td><td>chỉ nguyên nhân</td></tr>'
          '<tr><td><b>A</b>nd</td><td>và</td><td>thêm ý</td></tr>'
          '<tr><td><b>N</b>or</td><td>cũng không</td><td>bổ sung một ý phủ định (đảo ngữ sau nor)</td></tr>'
          '<tr><td><b>B</b>ut</td><td>nhưng</td><td>chỉ sự trái ngược</td></tr>'
          '<tr><td><b>O</b>r</td><td>hoặc</td><td>chỉ sự lựa chọn</td></tr>'
          '<tr><td><b>Y</b>et</td><td>nhưng (vẫn)</td><td>chỉ ý trái ngược, bất ngờ</td></tr>'
          '<tr><td><b>S</b>o</td><td>vì vậy</td><td>chỉ kết quả</td></tr></table>'
          '<p><b>Ví dụ:</b></p>'
          '<p>- Her family planned to travel this summer, <b>but</b> the father was sick.</p>'
          '<p>- Nam’s house is very old, <b>so</b> he is going to move to a new apartment.</p>'
          '<p>- My son wants to have a puppy for his birthday, <b>for</b> dogs are very cute.</p>'
          '<p>- My brother is a doctor, <b>and</b> my sister is a nurse.</p>'
          '<p>- We don’t go out, <b>nor</b> do we want to do anything on the weekend.</p>'
          '<p>- You should call her back, <b>or</b> she will come here to talk to you.</p>'
          '<p>- My children don’t like vegetables, <b>yet</b> they eat them anyway.</p>')
    h += '<p><b>II. TO-INFINITIVE AND BARE INFINITIVE (Động từ To V0 và V0)</b></p>'

    def tbl(words, cols=4):
        rows = ''
        for k in range(0, len(words), cols):
            rows += '<tr>' + ''.join('<td>%s</td>' % w for w in words[k:k + cols]) + '</tr>' * 0 + '</tr>'
        return '<table class="th">%s</table>' % rows
    v1 = ['afford (đủ khả năng)', 'agree (đồng ý)', 'appear (xuất hiện)', 'arrange (sắp xếp)', 'decide (quyết định)', 'demand (yêu cầu)',
          'deserve (xứng đáng)', 'expect (mong đợi)', 'fail (thất bại)', 'hesitate (do dự)', 'hope (hi vọng)', 'learn (học)',
          'manage (xoay sở)', 'mean (có ý định)', 'need (cần)', 'offer (đề nghị)', 'plan (lên kế hoạch)', 'prepare (chuẩn bị)',
          'pretend (giả vờ)', 'promise (hứa)', 'refuse (từ chối)', 'seem (dường như)', 'threaten (đe doạ)', 'volunteer (tình nguyện)',
          'wait (đợi)', 'want (muốn)', 'wish (mong)', 'would like (muốn)', 'would love (yêu thích)', '']
    v2 = ['advise (khuyên)', 'allow (cho phép)', 'invite (mời)', 'ask (yêu cầu)', 'permit (cho phép)', 'challenge (thách thức)',
          'persuade (thuyết phục)', 'convince (thuyết phục)', 'remind (nhắc nhở)', 'dare (dám)', 'require (đòi hỏi)', 'encourage (khuyến khích)',
          'teach (dạy)', 'expect (mong đợi)', 'tell (bảo)', 'urge (thúc giục)', 'force (buộc)', 'want (muốn)', 'hire (thuê)', 'warn (cảnh báo)']
    h += '<p><b>1. Động từ + TO V0 (V + to V0)</b></p>' + tbl(v1)
    h += ('<p><b>Ví dụ:</b> Maria <b>decided to continue</b> her education after a gap year. / He <b>manages to fix</b> his daughter’s bicycle. / '
          'Most women <b>expect to get</b> more help with the housework from their husbands. / I’m <b>planning to take</b> my children to the new amusement park this weekend.</p>')
    h += '<p><b>2. Động từ + tân ngữ + TO V0 (V + O + to V0)</b></p>' + tbl(v2)
    h += ('<p><b>Ví dụ:</b> He somehow persuades <u>his parents</u> <b>to buy</b> him a motorbike. / I’ve warned <u>you</u> many times <b>not to leave</b> the front door unlocked. / '
          'His parents encourage <u>him</u> <b>to take part</b> in the competition.</p>')
    h += ('<p><b>3. Động từ + tân ngữ + V0 (V + O + V0)</b></p><table class="th"><tr><th>Cấu trúc</th><th>Nghĩa</th></tr>'
          '<tr><td><b>make + O + V0</b></td><td>khiến/bắt ai làm gì</td></tr>'
          '<tr><td><b>let + O + V0</b></td><td>để cho ai làm gì</td></tr>'
          '<tr><td><b>help + O + (to) V0</b></td><td>giúp ai làm gì</td></tr>'
          '<tr><td><b>Let’s + V0</b></td><td>chúng ta hãy</td></tr>'
          '<tr><td><b>see / hear / smell / feel / notice / watch + O + V0</b></td><td>thấy/nghe… ai làm gì (chứng kiến toàn bộ hành động)</td></tr></table>'
          '<p><b>Ví dụ:</b> I heard <u>him</u> <b>open</b> the window last night. / Our teacher made <u>us</u> <b>apologise</b> for our rudeness. / '
          'Lucy helps <u>me</u> <b>(to) do</b> my homework. / Mary’s parents let <u>her</u> <b>go</b> to the movie with her friends. / <b>Let’s go</b> out for dinner!</p>')
    return h


def build():
    pages = []
    H = {}
    cur = 1
    for k, pat in [('e1', r'^<b>E1:'), ('e2', r'^<b>E2:'), ('e3', r'^<b>E3:'), ('e4', r'^<b>E4:'), ('e4b', r'^<b>E4: Make'),
                   ('e5', r'^<b>E5:'), ('sp', r'IV-SPEAKING'), ('e6', r'^<b>E6:'), ('e7', r'^<b>E7:'), ('e8', r'^<b>E8:'), ('e9', r'^<b>E9:')]:
        cur = fnd(pat, cur + (1 if k == 'e4b' else 0)) if k != 'e4' else fnd(pat, cur)
        H[k] = cur
    H['e4b'] = fnd(r'^<b>E4: Make', H['e4'] + 1)
    H['end'] = len(BR) + 1

    # ---- phát âm / trọng âm (Word: E1 trọng âm, E2 phát âm)
    ph1 = mcq('ph1', rng(H['e1'] + 1, H['e2'] - 1)); assert len(ph1) == 13
    ph2 = mcq('ph2', rng(H['e2'] + 1, fnd(r'II-VOCABULARY') - 1)); assert len(ph2) == 10
    pages.append({'id': 'phat-am', 'title': 'Phát âm & trọng âm', 'mode': 'practice', 'groups': [
        {'id': 'ph1', 'instr': 'E1: Mark the letter A, B, C, or D to indicate the word that differs from the other three in the position of the primary stress in each of the following questions.', 'items': ph1},
        {'id': 'ph2', 'instr': 'E2: Mark the letter A, B, C or D to indicate the word whose underlined part differs from the other three in pronunciation in each of the following questions.', 'items': ph2}]})

    # ---- từ vựng & ngữ pháp
    vg1 = mcq('vg1', rng(H['e3'] + 1, H['e4'] - 1)); assert len(vg1) == 64
    vg1[16]['q'] = 'Fantasia Barrino, the winner of American Idol’s season 3 in 2004, released her ______ Free Yourself which earned three Grammy Award nominations.'
    for k in (21, 22):                               # bỏ gạch chân thừa ở chỗ trống
        vg1[k]['q'] = fixblank(vg1[k]['q'].replace('<u>', '').replace('</u>', ''))
    vg1[26]['q'] = vg1[26]['q'].replace('<u>', '').replace('</u>', '').replace('the ______', 'the ______ ')
    vg1[26]['q'] = fixblank(vg1[26]['q'])
    vg1[26]['q'] = vg1[26]['q'].replace('We’re seeking for', 'We’re seeking')
    vg1[44]['q'] = fixblank(vg1[44]['q'].replace('wonders he should', 'wonders whether he should'))
    vg2 = mcq('vg2', rng(H['e4'] + 1, H['e4b'] - 1)); assert len(vg2) == 61
    vg2[3]['q'] = vg2[3]['q'].replace(' from at least', ' from someone at least')
    vg2[36]['q'] = fixblank(vg2[36]['q'].replace('<u>', '').replace('</u>', ''))
    vg2[36]['o'] = [keepu(re.sub(r'</?u>', '', x)) for x in vg2[36]['o']]
    vg2[27]['q'] = fixblank(vg2[27]['q'])
    vg3 = []
    for l in rng(H['e4b'] + 1, H['e5'] - 1):
        m = re.match(r'^Question (\d+):\s*(.*?)\s*\((\w+)\)\s*$', cl(l))
        if m:
            q = m.group(2).strip()
            q = q.replace('yesterday She', 'yesterday. She').replace('The party', 'The party')
            q = q.replace('will probably be invited to join the band,', 'will probably be invited to join the band.')
            vg3.append({'id': 'vg3.%d' % (len(vg3) + 1), 't': 'fill', 'long': True,
                        'q': '<b>Nối hai câu bằng liên từ (%s):</b> %s<br>{_}' % (m.group(3), q)})
    assert len(vg3) == 8
    pages.append({'id': 'tu-vung-ngu-phap', 'title': 'Từ vựng & Ngữ pháp', 'mode': 'practice', 'groups': [
        {'id': 'vg1', 'instr': 'E3: Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.', 'items': vg1},
        {'id': 'vg2', 'instr': 'E4: Mark the letter A, B, C or D to indicate the correct answer to each of the following questions.', 'items': vg2},
        {'id': 'vg3', 'instr': 'E4 (bài 2 – nguồn đánh trùng nhãn E4): Make compound sentences using the conjunctions in brackets.', 'items': vg3}]})

    # ---- nghe
    stm = []
    for l in rng(H['e5'] + 1, H['sp'] - 1):
        m = re.match(r'^\s*(\d)\.\s*(.*)$', cl(l))
        if m:
            stm.append({'id': 'li1.%s' % m.group(1), 't': 'tf', 'q': m.group(2).strip().replace('June 11,2003', 'June 11, 2003').replace('Simon Fuller', 'Simon Fuller.').replace('star World', 'Star World') .rstrip('.') + '.'})
    assert len(stm) == 5
    pages.append({'id': 'nghe', 'title': 'Nghe', 'mode': 'practice', 'audio': 'botro_nghe.mp3', 'groups': [
        {'id': 'li1', 'instr': 'E5: Listen to the information about American Idol and decide whether the statements are True (T) or False (F).', 'items': stm}]})

    # ---- nói
    cues = ''.join('<li>%s</li>' % re.sub(r'^\d\.\s*', '', cl(l)) for l in rng(fnd(r'^<b>Give your answer using', H['sp']) + 1, H['e6'] - 2) if cl(l))
    q = ('Talk about a TV music show that you like. You can use the following questions as cues: '
         '<ul><li>What is it?</li><li>How do you know it?</li><li>What is it like?</li><li>Why do you like it?</li></ul>'
         '<b>Useful vocabulary:</b> The Voice of Vietnam, Vietnam Idol, The X Factor, The Remix; through the Internet / TV / friends / magazines; popular, new, interesting, celebrities’ appearance; focusing on voice, relaxing, professional performances.<br>'
         '<b>Useful structures:</b> Among many TV music shows … / I am a big fan of … / One of my favourite TV music shows is … / I like … most. / I know this programme through … / '
         'I watched the show for the first time on … / In this programme, … / There are some reasons why I like the show. / Firstly, … Secondly, … In addition, …<br>'
         '<b>Give your answer using the following cues (speak for 1–2 minutes):</b><ol>%s</ol>' % cues)
    pages.append({'id': 'noi', 'title': 'Nói', 'mode': 'practice', 'groups': [
        {'id': 'sp1', 'instr': 'IV – Speaking: Talk about a TV music show that you like. (nói – đối chiếu bài mẫu)', 'items': [{'id': 'sp1.1', 't': 'open', 'q': q}]}]})

    # ---- đọc
    def para(lines):
        out = []
        for l in lines:
            t = keepu(cl(l))
            if t:
                t = re.sub(r'<b>\((\d+)\)</b>\s*_+', r'<b>(\1) ______</b>', t)
                t = re.sub(r'\((\d+)\)\s*_+', r'<b>(\1) ______</b>', t) if '<b>(' not in t else t
                out.append('<p>%s</p>' % t)
        return ''.join(out)
    k6 = fnd(r'^<b>Question 1: </b>\s*What is TRUE', H['e6'])
    p6 = para(rng(H['e6'] + 1, k6 - 1))
    re1 = []
    L6 = rng(k6, H['e7'] - 1)
    stems = [i for i, l in enumerate(L6) if l.startswith('<b>Question')]
    for n, i in enumerate(stems):
        j = stems[n + 1] if n + 1 < len(stems) else len(L6)
        blk = L6[i:j]
        m = re.match(r'^<b>Question \d+:\s*</b>(.*)$', blk[0]); stem = cl(m.group(1))
        opt = ' '.join(cl(x) for x in blk[1:])
        from parse_src import split_opts
        o = split_opts(opt)
        assert len(o) == 4, (stem, o)
        re1.append({'id': 're1.%d' % (n + 1), 't': 'mcq', 'q': stem, 'o': [x.strip() for x in o]})
    assert len(re1) == 5
    k7 = fnd(r'^<b>Question 1: A\.', H['e7'])
    p7 = para(rng(H['e7'] + 1, k7 - 1)).replace('new while R&amp;B', 'new white R&amp;B').replace('new while R&B', 'new white R&B').replace('new eroup', 'new group')
    p7 = re.sub(r'(\(\d+\) ______</b>)(\w)', r'\1 \2', p7)
    re2 = mcq('re2', rng(k7, H['e8'] - 2 if False else fnd(r'VI-WRITING') - 1)); assert len(re2) == 13
    for i, it in enumerate(re2, 1):
        it['q'] = 'Blank (%d)' % i
    pages.append({'id': 'doc', 'title': 'Đọc hiểu', 'mode': 'practice', 'groups': [
        {'id': 're1', 'instr': 'E6: Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each of the questions.', 'passage': p6, 'items': re1},
        {'id': 're2', 'instr': 'E7: Read the following passage and mark the letter A, B, C, or D to indicate the correct word or phrase that best fits each of the numbered blanks.', 'passage': p7, 'items': re2}]})

    # ---- viết
    wr1 = []
    for l in rng(H['e8'] + 1, H['e9'] - 1):
        m = re.match(r'^Question (\d):\s*(.*?)\s*$', cl(l))
        if m:
            wr1.append({'id': 'wr1.%s' % m.group(1), 't': 'fill', 'long': True,
                        'q': '<b>Từ gợi ý:</b> %s<br>Câu hoàn chỉnh: {_}' % m.group(2).strip()})
    assert len(wr1) == 5
    wr2 = [{'id': 'wr2.1', 't': 'open', 'q': 'You have an English friend and want to tell him / her about your favourite singer. Write an email (120 – 150 words) to tell him / her about it. Use the following questions as cues:'
            '<ul><li>What is his / her name?</li><li>What type of music does he / she sing?</li><li>What type of people listen to his / her songs?</li><li>Why do you admire him / her?</li></ul>'
            '<i>To: … / Subject: … / Dear …, … / Best wishes,</i>'}]
    pages.append({'id': 'viet', 'title': 'Viết', 'mode': 'practice', 'groups': [
        {'id': 'wr1', 'instr': 'E8: Complete each of the following sentences using the cues given. You can change the cues and use other words in addition to the cues to complete the sentences.', 'items': wr1},
        {'id': 'wr2', 'instr': 'E9: You have an English friend and want to tell him / her about your favourite singer. Write an email (120 – 150 words). (tự luận – xem bài mẫu)', 'items': wr2}]})
    return {'id': 'lop10-u3-botro', 'title': 'Unit 3 – Music: Bài tập bổ trợ', 'grade': 10, 'unit': 3, 'theory': theory(), 'pages': pages}


if __name__ == '__main__':
    b = build()
    dump(os.path.join(ROOT, 'units/lop10_u3_botro.py'), 'SET', b)
    tot = 0
    for p in b['pages']:
        n = sum(len(g['items']) for g in p['groups']); tot += n
        print(p['id'], n, [(g['id'], len(g['items'])) for g in p['groups']])
    print('TOTAL', tot)
