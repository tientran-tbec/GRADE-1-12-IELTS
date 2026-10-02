# -*- coding: utf-8 -*-
"""Sinh dữ liệu Lớp 3 (Unit 1-2) -> units/lop3_uN_{luyentap,test01}.py + _dapan.py ; copy hình từ docx đã bung (/tmp/m1, /tmp/m2)."""
import os, sys, shutil, pprint, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_lop3_more as more
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANS, EXP = {}, {}

def mcq(i, q, o, a, e, img=None, plain=True, say=None):
    ANS[i] = a; EXP[i] = e
    d = {'id': i, 't': 'mcq', 'q': q, 'o': o, 'plain': True}
    if say: d['say'] = say
    if img: d['img'] = img
    return d

def fill(i, q, a, e, hint=None, img=None, say=None):
    ANS[i] = a if isinstance(a, dict) else (a if isinstance(a, list) else [a]); EXP[i] = e
    d = {'id': i, 't': 'fill', 'q': q}
    if say: d['say'] = say
    if hint: d['hint'] = hint
    if img: d['img'] = img
    return d

def match(i, q, left, o, a, e):
    ANS[i] = {'blanks': [[x] for x in a]}; EXP[i] = e
    return {'id': i, 't': 'match', 'q': q, 'left': left, 'o': o}

def order(i, q, sentence, e, extra=None, seed=1):
    ws = sentence.split()
    sh = ws[:]
    random.Random(seed).shuffle(sh)
    if sh == ws: sh = ws[::-1]
    ANS[i] = [sentence] + (extra or []); EXP[i] = e
    return {'id': i, 't': 'order', 'q': q, 'words': sh}

def copyimgs(src, dst, names):
    os.makedirs(os.path.join(R, dst), exist_ok=True)
    for n in names:
        shutil.copy(os.path.join(src, n), os.path.join(R, dst, n))

def write(name, S):
    with open(os.path.join(R, 'units/%s.py' % name), 'w', encoding='utf-8') as f:
        f.write('# -*- coding: utf-8 -*-\n"""Lớp 3 – Global Success. Sinh bởi tools/gen_lop3.py; nguồn: Bài tập chuyên sâu Tiếng Anh 3."""\n\nSET = ' + pprint.pformat(S, width=140) + '\n')
    with open(os.path.join(R, 'units/%s_dapan.py' % name), 'w', encoding='utf-8') as f:
        f.write('# -*- coding: utf-8 -*-\n"""Đáp án + giải thích (Lớp 3)."""\n\nANS = ' + pprint.pformat(ANS, width=140) + '\n\nEXPLANATIONS = ' + pprint.pformat(EXP, width=140) + '\n\nGHI_CHU_RA_SOAT = []\n')
    ANS.clear(); EXP.clear()

def table(rows, head):
    return '<table class="th"><tr>%s</tr>%s</table>' % (''.join('<th>%s</th>' % h for h in head), ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows))

# ===================================================== UNIT 1 · HELLO
def unit1():
    S1, S2 = '/tmp/m1/word/media', ''
    imgs = ['image%d.png' % n for n in (6, 7, 8, 9, 10, 12, 13, 14, 15)] + ['image16.jpeg']
    copyimgs(S1, 'assets/lop3_u1/luyentap', imgs)
    theory = ('<h3>Từ vựng</h3>' + table([
        ['hi / hello', 'xin chào'], ['goodbye / bye', 'tạm biệt'], ['fine', 'khỏe'], ['thank you / thanks', 'cảm ơn'],
        ['nice to meet you', 'rất vui được gặp bạn'], ['name', 'tên'], ['school', 'trường học'], ['class', 'lớp học']], ['English', 'Tiếng Việt']) +
        '<h3>Mẫu câu</h3><ul>'
        '<li><b>Hello. / Hi.</b> – Xin chào. (<i>Hi</i> thân mật hơn, dùng với bạn bè.)</li>'
        '<li><b>I\'m + tên.</b> – Mình là … &nbsp; <i>I\'m Mai.</i></li>'
        '<li><b>How are you?</b> – Bạn có khỏe không? &rarr; <b>I\'m fine, thank you. / Fine, thanks.</b> – Mình khỏe, cảm ơn.</li>'
        '<li><b>Nice to meet you.</b> – Rất vui được gặp bạn. &rarr; <b>Nice to meet you, too.</b></li>'
        '<li><b>Goodbye. / Bye.</b> – Tạm biệt. &rarr; <b>Bye. See you later.</b> – Hẹn gặp lại.</li></ul>')
    p1 = {'id': 'tu-vung', 'title': 'Từ vựng', 'mode': 'practice', 'groups': [
        {'id': 'm1', 'instr': 'Nối từ tiếng Anh với nghĩa tiếng Việt. (Chọn nghĩa ở ô bên phải.)', 'items': [
            match('m1.1', '', ['hello', 'goodbye', 'thank you', 'fine', 'name', 'school'], ['tạm biệt', 'cảm ơn', 'trường học', 'xin chào', 'khỏe', 'tên'],
                  ['xin chào', 'tạm biệt', 'cảm ơn', 'khỏe', 'tên', 'trường học'], 'hello = xin chào, goodbye = tạm biệt, thank you = cảm ơn, fine = khỏe, name = tên, school = trường học.')]},
        {'id': 'a', 'instr': 'Task 1. Nhìn hình và chọn từ đúng.', 'items': [
            mcq('a.1', '', ['How are you?', 'hello', "I'm Nam"], 'hello', 'Các bạn đang vẫy tay chào nhau → hello.', 'image6.png'),
            mcq('a.2', '', ['goodbye', 'name', 'how'], 'goodbye', 'Mẹ và bé vẫy tay chia tay → goodbye.', 'image7.png'),
            mcq('a.3', '', ['I', 'thank you', 'you'], 'thank you', 'Bạn nhỏ đưa quà / nói cảm ơn → thank you.', 'image8.png'),
            mcq('a.4', '', ['nice', 'are', 'hi'], 'hi', 'Chú chim cánh cụt vẫy chào → hi.', 'image9.png'),
            mcq('a.5', '', ['fine', 'bye', 'thank you'], 'fine', 'Ngón tay OK nghĩa là khỏe → fine.', 'image10.png')]},
        {'id': 'b', 'instr': 'Task 2. Chọn từ khác loại.', 'items': [
            mcq('b.1', '', ['hi', 'hello', 'bye'], 'bye', 'hi, hello là lời chào; bye là lời tạm biệt.'),
            mcq('b.2', '', ['how', 'Peter', 'Tony'], 'how', 'Peter, Tony là tên người; how là từ để hỏi.'),
            mcq('b.3', '', ['pink', 'yellow', 'ten'], 'ten', 'pink, yellow là màu sắc; ten là số.'),
            mcq('b.4', '', ['bye', 'goodbye', 'hello'], 'hello', 'bye, goodbye là tạm biệt; hello là chào.'),
            mcq('b.5', '', ['thanks', 'bye', 'thank you'], 'bye', 'thanks, thank you đều là cảm ơn; bye là tạm biệt.')]},
        {'id': 'c', 'instr': 'Task 3. Nhìn hình, sắp xếp lại chữ cái và viết từ đúng.', 'items': [
            fill('c.1', 'hlole → {_}', 'hello', 'h-e-l-l-o = hello.', img='image12.png'),
            fill('c.2', 'ih → {_}', 'hi', 'h-i = hi.', img='image13.png'),
            fill('c.3', 'hankts → {_}', 'thanks', 't-h-a-n-k-s = thanks.', img='image14.png'),
            fill('c.4', 'eyb → {_}', 'bye', 'b-y-e = bye.', img='image15.png'),
            fill('c.5', 'ouy → {_}', 'you', 'y-o-u = you.', img='image16.jpeg')]}]}
    p2 = {'id': 'mau-cau', 'title': 'Mẫu câu', 'mode': 'practice', 'groups': [
        {'id': 'd', 'instr': 'Task 4. Nối câu hỏi / lời nói (cột A) với câu trả lời (cột B).', 'items': [
            match('d.1', '', ['How are you?', 'Hi! I\'m Mai.', 'Goodbye!', 'Hello. I am Thuy.', 'Nice to meet you!'],
                  ['Hi!', 'Bye. See you later.', 'Hello!', 'Nice to meet you, too!', 'Fine, thanks.'],
                  ['Fine, thanks.', 'Hello!', 'Bye. See you later.', 'Hi!', 'Nice to meet you, too!'],
                  'How are you? – Fine, thanks. | Hi! I\'m Mai. – Hello! | Goodbye! – Bye. See you later. | Hello. – Hi! | Nice to meet you! – Nice to meet you, too!')]},
        {'id': 'e', 'instr': 'Task 5. Hoàn thành đoạn hội thoại bằng các từ: Hello – How – fine – you – thanks.', 'bank': ['Hello', 'How', 'fine', 'you', 'thanks'], 'items': [
            fill('e.1', 'Quan: Hi, Tony.<br>Tony: {_}, Quan and Phong.', 'Hello', 'Chào lại: Hello.'),
            fill('e.2', 'Quan: {_} are you?', 'How', 'How are you? = Bạn khỏe không?'),
            fill('e.3', "Tony: I'm {_}, thanks. And you?", 'fine', "I'm fine, thanks. = Mình khỏe, cảm ơn."),
            fill('e.4', 'Quan: I\'m fine. Thank {_}.', 'you', 'Thank you = cảm ơn bạn.'),
            fill('e.5', 'Tony: And how are you, Phong?<br>Phong: Fine, {_}.', 'thanks', 'Fine, thanks. = Khỏe, cảm ơn.')]},
        {'id': 'f', 'instr': 'Task 6. Bấm các từ để xếp thành câu đúng.', 'items': [
            order('f.1', '', 'Hello, Quan. I\'m Phong.', 'Chào Quan rồi giới thiệu: Hello, Quan. I\'m Phong.', seed=3),
            order('f.2', '', 'I\'m fine, thanks.', 'I\'m fine, thanks. = Mình khỏe, cảm ơn.', seed=5),
            order('f.3', '', 'How are you?', 'Câu hỏi thăm sức khoẻ: How are you?', seed=2),
            order('f.4', '', 'Nice to meet you, too.', 'Đáp lại: Nice to meet you, too.', seed=7),
            order('f.5', '', 'Goodbye, Miss Hoa.', 'Goodbye, Miss Hoa. = Tạm biệt cô Hoa.', seed=4)]}]}
    S = {'id': 'lop3-u1-luyentap', 'title': 'Unit 1 – Hello: Luyện tập', 'grade': 3, 'unit': 1, 'theory': theory, 'pages': [p1, p2] + more.u1_pages(sys.modules[__name__])}
    write('lop3_u1_luyentap', S)
    for k, specs in enumerate(more.u1_tests(sys.modules[__name__]), 1):
        items = more.seq(sys.modules[__name__], specs)
        T = {'id': 'lop3-u1-test%02d' % k, 'title': 'Unit 1 – Hello: Kiểm tra %d' % k, 'grade': 3, 'unit': 1, 'theory': '',
             'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 15, 'warn_at': 2, 'groups': [{'id': 't1', 'instr': 'Làm %d câu. Nộp bài để xem điểm và đáp án.' % len(items), 'items': items}]}]}
        write('lop3_u1_test%02d' % k, T)

# ===================================================== UNIT 2 · WHAT'S YOUR NAME?
def unit2():
    S2 = '/tmp/m2/word/media'
    copyimgs(S2, 'assets/lop3_u2/luyentap', ['image7.jpeg', 'image8.jpeg', 'image9.jpeg', 'image10.jpeg', 'image11.jpeg', 'image26.png', 'image28.png', 'image30.png', 'image31.png'])
    theory = ('<h3>Từ vựng</h3>' + table([['what', 'cái gì'], ["what's (= what is)", 'là cái gì'], ['your', 'của bạn'], ['my', 'của tôi / của mình'], ['name', 'tên'], ['how', 'như thế nào'], ['spell', 'đánh vần']], ['English', 'Tiếng Việt']) +
        '<h3>Mẫu câu</h3><ul>'
        '<li><b>What\'s your name?</b> – Tên bạn là gì? &rarr; <b>My name\'s Quynh.</b> / <b>I\'m Quynh.</b></li>'
        '<li><b>What\'s his / her name?</b> – Tên bạn ấy là gì? &rarr; <b>His / Her name\'s Mai.</b></li>'
        '<li><b>How do you spell your name?</b> – Bạn đánh vần tên thế nào? &rarr; <b>L-I-N-D-A.</b></li></ul>')
    p1 = {'id': 'tu-vung', 'title': 'Từ vựng', 'mode': 'practice', 'groups': [
        {'id': 'm1', 'instr': 'Nối từ tiếng Anh với nghĩa tiếng Việt.', 'items': [
            match('m1.1', '', ['what', 'your', 'my', 'name', 'spell', 'how'], ['tên', 'như thế nào', 'cái gì', 'đánh vần', 'của tôi', 'của bạn'],
                  ['cái gì', 'của bạn', 'của tôi', 'tên', 'đánh vần', 'như thế nào'], 'what = cái gì, your = của bạn, my = của tôi, name = tên, spell = đánh vần, how = như thế nào.')]},
        {'id': 'a', 'instr': 'Task 1. Chọn từ khác loại.', 'items': [
            mcq('a.1', '', ['Hi', 'bye', 'hello'], 'bye', 'Hi, hello là chào; bye là tạm biệt.'),
            mcq('a.2', '', ['how', 'Peter', 'Linda'], 'how', 'Peter, Linda là tên; how là từ để hỏi.'),
            mcq('a.3', '', ['Bye', 'goodbye', 'name'], 'name', 'Bye, goodbye là tạm biệt; name là tên.'),
            mcq('a.4', '', ['what', 'how', 'hi'], 'hi', 'what, how là từ để hỏi; hi là lời chào.'),
            mcq('a.5', '', ['Tony', 'Peter', 'fine'], 'fine', 'Tony, Peter là tên người; fine là khỏe.')]},
        {'id': 'b', 'instr': 'Task 2. Nhìn hình, sắp xếp chữ cái và viết từ đúng.', 'items': [
            fill('b.1', 'trePe → {_}', 'Peter', 'P-e-t-e-r = Peter.', img='image7.jpeg'),
            fill('b.2', 'Lnadi → {_}', 'Linda', 'L-i-n-d-a = Linda.', img='image8.jpeg'),
            fill('b.3', 'begodyo → {_}', 'goodbye', 'g-o-o-d-b-y-e = goodbye.', img='image9.jpeg'),
            fill('b.4', 'neam → {_}', 'name', 'n-a-m-e = name.', img='image10.jpeg'),
            fill('b.5', 'plsel → {_}', 'spell', 's-p-e-l-l = spell.', img='image11.jpeg')]}]}
    p2 = {'id': 'mau-cau', 'title': 'Mẫu câu', 'mode': 'practice', 'groups': [
        {'id': 'c', 'instr': 'Task 3. Nối câu (cột A) với câu đáp (cột B).', 'items': [
            match('c.1', '', ['Hello. I\'m Mary.', 'What\'s your name?', 'How do you spell your name?', 'How are you?', 'My name\'s Nam. Nice to meet you.'],
                  ['I\'m fine, thank you.', 'N-A-M.', 'My name\'s Tony.', 'Hi, Mary. I\'m Phuong.', 'My name\'s Ha. Nice to meet you, too.'],
                  ['Hi, Mary. I\'m Phuong.', 'My name\'s Tony.', 'N-A-M.', 'I\'m fine, thank you.', 'My name\'s Ha. Nice to meet you, too.'],
                  'Chào – chào lại; hỏi tên – nói tên; hỏi cách đánh vần – đánh vần; hỏi thăm – trả lời khỏe; làm quen – đáp lại.')]},
        {'id': 'd', 'instr': 'Task 4. Hoàn thành đoạn hội thoại bằng các từ: names – how – nice – hi – What\'s – Linda.', 'bank': ['hi', "What's", 'Linda', 'name', 'nice', 'How'], 'items': [
            fill('d.1', "Linda: Hi, I'm Linda. {_} your name?", "What's", "What's your name? = Tên bạn là gì?"),
            fill('d.2', 'Mai: Hello, my {_} Mai.', ["name's", 'name is'], "my name's / my name is = tên mình là."),
            fill('d.3', 'Mai: Nice to meet you, {_}.', 'Linda', 'Gọi tên bạn đang nói chuyện: Linda.'),
            fill('d.4', 'Linda: {_} to meet you, too.', 'Nice', 'Nice to meet you, too.'),
            fill('d.5', 'Mai: {_} do you spell your name?', 'How', 'How do you spell your name?')]},
        {'id': 'e', 'instr': 'Task 5. Chọn từ đúng điền vào chỗ trống.', 'items': [
            fill('e.1', '{_} your name?', "What's", "What's your name?"),
            fill('e.2', "{_} name's Tim.", 'My', "My name's Tim."),
            fill('e.3', '{_} do you spell your name?', 'How', 'How do you spell your name?'),
            fill('e.4', 'My {_} is Mary.', 'name', 'My name is Mary.'),
            fill('e.5', 'How {_} you?', 'are', 'How are you?'),
            fill('e.6', 'Nice {_} meet you.', 'to', 'Nice to meet you.')]},
        {'id': 'f', 'instr': 'Task 6. Bấm các từ để xếp thành câu đúng.', 'items': [
            order('f.1', '', 'What is your name?', 'What is your name? = Tên bạn là gì?', seed=2),
            order('f.2', '', 'My name is Mary.', 'My name is Mary.', seed=3),
            order('f.3', '', 'I am Linda.', 'I am Linda. = Mình là Linda.', seed=1),
            order('f.4', '', 'How do you spell your name?', 'How do you spell your name?', seed=5),
            order('f.5', '', 'Her name is Mai.', 'Her name is Mai. = Tên bạn ấy là Mai.', seed=4)]}]}
    p3 = {'id': 'doc-viet', 'title': 'Đọc – Viết', 'mode': 'practice', 'groups': [
        {'id': 'g', 'instr': 'Task 7. Nhìn hình và viết: What is his / her name? – He / She is …', 'items': [
            fill('g.1', 'What is his name? – He is {_}.', 'Tommy', 'He is Tommy.', img='image26.png'),
            fill('g.2', 'What is her name? – She is {_}.', 'Bella', 'She is Bella.', img='image28.png'),
            fill('g.3', 'What is her name? – She is {_}.', 'Lola', 'She is Lola.', img='image30.png'),
            fill('g.4', 'What is her name? – She is {_}.', 'Lily', 'She is Lily.', img='image31.png')]},
        {'id': 'h', 'instr': 'Task 8. Chọn đáp án đúng.', 'items': [
            mcq('h.1', 'How ___ you, Mai?', ['am', 'is', 'are', 'it'], 'are', 'Chủ ngữ you → are: How are you?'),
            mcq('h.2', 'Goodbye. ___ you later.', ['How', 'See', 'Nice', 'are'], 'See', 'See you later. = Hẹn gặp lại.'),
            mcq('h.3', '___, I am Linda.', ['Hello', 'Good-bye', 'Bye', 'See you'], 'Hello', 'Giới thiệu bản thân → Hello.'),
            mcq('h.4', 'Goodbye. See you ___.', ['soon', 'late', 'do', 'am'], 'soon', 'See you soon. = Hẹn sớm gặp lại.'),
            mcq('h.5', '___ her name?', ['Hello', 'Goodbye', 'What', "What's"], "What's", "What's her name? = Tên bạn ấy là gì?")]}]}
    S = {'id': 'lop3-u2-luyentap', 'title': "Unit 2 – What's your name?: Luyện tập", 'grade': 3, 'unit': 2, 'theory': theory, 'pages': [p1, p2, p3] + more.u2_pages(sys.modules[__name__])}
    write('lop3_u2_luyentap', S)
    for k, specs in enumerate(more.u2_tests(sys.modules[__name__]), 1):
        items = more.seq(sys.modules[__name__], specs)
        T = {'id': 'lop3-u2-test%02d' % k, 'title': "Unit 2 – What's your name?: Kiểm tra %d" % k, 'grade': 3, 'unit': 2, 'theory': '',
             'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 15, 'warn_at': 2, 'groups': [{'id': 't1', 'instr': 'Làm %d câu. Nộp bài để xem điểm và đáp án.' % len(items), 'items': items}]}]}
        write('lop3_u2_test%02d' % k, T)

if __name__ == '__main__':
    unit1(); unit2(); print('ok')
