# -*- coding: utf-8 -*-
"""Bài bổ sung Lớp 3 – Unit 1, 2 (trang Nghe, Chính tả, Mẫu câu 2, Đọc hiểu + bộ 3 đề kiểm tra mỗi Unit)."""

def tf(i, q, a, e):
    import sys
    ANS, EXP = sys.modules['__main__'].ANS, sys.modules['__main__'].EXP
    ANS[i] = a; EXP[i] = e
    return {'id': i, 't': 'tf', 'q': q}

def pg(id_, title, groups):
    return {'id': id_, 'title': title, 'mode': 'practice', 'groups': groups}

def seq(g, specs, start=1, prefix='t1.'):
    """specs: danh sách (tên hàm, tham số...) → item với id t1.N liên tiếp."""
    out = []
    for n, sp in enumerate(specs, start):
        k, *a = sp
        out.append(getattr(g, k)(prefix + str(n), *a))
    return out

# ---------------------------------------------------------------- UNIT 1
def u1_pages(g):
    mcq, fill, order, match = g.mcq, g.fill, g.order, g.match
    def listen_words(pref, words, pool):
        res = []
        for n, w in enumerate(words, 1):
            opts = [w] + [x for x in pool if x != w][:2]
            opts = sorted(opts, key=lambda x: (hash(x + pref) % 7, x))
            res.append(mcq('%s.%d' % (pref, n), 'Bấm 🔊 và chọn từ em nghe được.', opts, w, 'Từ được đọc là: %s.' % w, say=w))
        return res
    pool = ['hello', 'hi', 'bye', 'goodbye', 'fine', 'thank you', 'how', 'you', 'name']
    nghe = pg('nghe', 'Nghe', [
        {'id': 'n1', 'instr': 'Nghe 1. Bấm 🔊 (có thể nghe lại nhiều lần) và chọn từ em nghe được.', 'items': listen_words('n1', ['hello', 'goodbye', 'fine', 'thank you', 'hi', 'bye'], pool)},
        {'id': 'n2', 'instr': 'Nghe 2. Nghe câu và chọn câu trả lời phù hợp.', 'items': [
            mcq('n2.1', 'Em nghe: câu hỏi', ["I'm fine, thank you.", 'Goodbye.', "I'm Nam."], "I'm fine, thank you.", 'Câu hỏi là "How are you?" → trả lời I\'m fine, thank you.', say='How are you?'),
            mcq('n2.2', 'Em nghe: lời tạm biệt', ['Bye, Mai.', 'Hello.', 'Fine, thanks.'], 'Bye, Mai.', 'Nghe "Goodbye, Nam." → đáp lại Bye.', say='Goodbye, Nam.'),
            mcq('n2.3', 'Em nghe: lời làm quen', ['Nice to meet you, too.', 'Goodbye.', 'How are you?'], 'Nice to meet you, too.', 'Nghe "Nice to meet you." → đáp Nice to meet you, too.', say='Nice to meet you.'),
            mcq('n2.4', 'Em nghe: lời chào', ["Hi, Tony. I'm Linda.", "I'm fine.", 'Bye.'], "Hi, Tony. I'm Linda.", 'Được chào Hello thì chào lại.', say="Hello, I'm Tony."),
            mcq('n2.5', 'Em nghe: lời cảm ơn', ['Fine, thanks.', 'Hello.', 'Bye.'], 'Fine, thanks.', 'Nghe "I\'m fine, thank you." → bạn ấy đang trả lời "How are you?".', say="I'm fine, thank you.")]},
        {'id': 'n3', 'instr': 'Nghe 3. Nghe và viết lại từ.', 'items': [
            fill('n3.1', '{_}', 'hello', 'hello', say='hello'), fill('n3.2', '{_}', 'goodbye', 'goodbye', say='goodbye'),
            fill('n3.3', '{_}', 'thanks', 'thanks = cảm ơn', say='thanks'), fill('n3.4', '{_}', 'fine', 'fine', say='fine'), fill('n3.5', '{_}', 'bye', 'bye', say='bye')]},
        {'id': 'n4', 'instr': 'Nghe 4. Nghe và viết lại cả câu.', 'items': [
            fill('n4.1', '{_}', 'How are you?', 'How are you?', say='How are you?'),
            fill('n4.2', '{_}', ["I'm fine, thanks.", "I'm fine, thank you."], "I'm fine, thanks.", say="I'm fine, thanks."),
            fill('n4.3', '{_}', 'Goodbye, Mai.', 'Goodbye, Mai.', say='Goodbye, Mai.')]}])
    chinhta = pg('chinh-ta', 'Chính tả', [
        {'id': 'c1', 'instr': 'Điền chữ cái còn thiếu.', 'items': [
            fill('c1.1', 'th{_}nk you', 'a', 'thank you'), fill('c1.2', 'ho{_}', 'w', 'how'), fill('c1.3', 'y{_}u', 'o', 'you'),
            fill('c1.4', 'h{_}', 'i', 'hi'), fill('c1.5', 'goo{_}bye', 'd', 'goodbye'), fill('c1.6', 'h{_}llo', 'e', 'hello'), fill('c1.7', 'f{_}ne', 'i', 'fine')]},
        {'id': 'c2', 'instr': 'Sắp xếp lại chữ cái thành từ đúng.', 'items': [
            fill('c2.1', 'oyu → {_}', 'you', 'you'), fill('c2.2', 'lehol → {_}', 'hello', 'hello'), fill('c2.3', 'doog bey → {_}', ['good bye', 'goodbye'], 'good bye = goodbye'),
            fill('c2.4', 'nefi → {_}', 'fine', 'fine'), fill('c2.5', 'ohw → {_}', 'how', 'how'), fill('c2.6', 'kthna uoy → {_}', 'thank you', 'thank you')]}])
    bosung = pg('mau-cau-2', 'Mẫu câu 2', [
        {'id': 'e2', 'instr': 'Điền từ thích hợp vào chỗ trống.', 'items': [
            fill('e2.1', "Hi, I'm Ben.<br>Hello, Ben. {_} Mai.", "I'm", "I'm Mai. = Mình là Mai."),
            fill('e2.2', "How are you? – I'm fine, {_}.", ['thank you', 'thanks'], 'I\'m fine, thank you.'),
            fill('e2.3', '{_}, Miss Nga.<br>Goodbye, Nam.', ['Goodbye', 'Bye'], 'Goodbye / Bye = tạm biệt.'),
            fill('e2.4', "{_}, I'm Lucy.<br>Hi, Lucy. I'm Minh.", ['Hello', 'Hi'], 'Mở đầu bằng lời chào.'),
            fill('e2.5', 'How are {_}, Ben? – I\'m fine, thank you.', 'you', 'How are you?'),
            fill('e2.6', '{_}, Nam. I\'m Lan.', ['Hi', 'Hello'], 'Chào rồi giới thiệu.'),
            fill('e2.7', "I'm fine, {_} you.", 'thank', 'thank you'),
            fill('e2.8', 'Hi, Mai. {_} are you? – Fine, thanks.', 'How', 'How are you?')]},
        {'id': 'f2', 'instr': 'Chọn từ đúng để hoàn thành đoạn hội thoại.', 'items': [
            mcq('f2.1', 'Nga: Hello, Hoa. How are ___?', ['you', 'I', 'fine'], 'you', 'How are you?'),
            mcq('f2.2', "Hoa: Hi, Nga. I'm ___, thanks. And you?", ['fine', 'hello', 'bye'], 'fine', "I'm fine, thanks."),
            mcq('f2.3', "Nga: ___ fine, thank you. Goodbye, Hoa.", ["I'm", 'How', 'Hi'], "I'm", "I'm fine."),
            mcq('f2.4', 'Hoa: ___, Nga.', ['Bye', 'How', 'Fine'], 'Bye', 'Đáp lại lời tạm biệt.')]},
        {'id': 'g2', 'instr': 'Bấm các từ để xếp thành câu đúng.', 'items': [
            order('g2.1', '', "Hi, Mai. I'm Minh.", "Hi, Mai. I'm Minh. = Chào Mai. Mình là Minh.", seed=2),
            order('g2.2', '', 'Goodbye, Minh.', 'Goodbye, Minh.', seed=5),
            order('g2.3', '', 'How are you, Lan?', 'How are you, Lan?', seed=3),
            order('g2.4', '', "I'm fine, thanks.", "I'm fine, thanks.", seed=8),
            order('g2.5', '', 'Bye. See you later.', 'Bye. See you later. = Tạm biệt. Hẹn gặp lại.', seed=4),
            order('g2.6', '', 'Goodbye. See you next week, Bill.', 'See you next week = Hẹn gặp lại tuần sau.', seed=6)]}])
    doc = pg('doc-hieu', 'Đọc hiểu', [
        {'id': 'r1', 'instr': 'Sắp xếp hội thoại: chọn số thứ tự (câu đầu tiên là số 0: "Nam: Hello, I\'m Nam.").', 'items': [
            match('r1.1', '', ["Quan: Hi, Nam. I'm Quan.", "Nam: How are you, Quan?", "Quan: I'm fine, thanks. And you?", "Nam: I'm fine, too. Thank you."], ['1', '2', '3', '4'],
                  ['1', '2', '3', '4'], "Thứ tự: 0 Nam: Hello, I'm Nam. → 1 Quan: Hi, Nam. I'm Quan. → 2 Nam: How are you, Quan? → 3 Quan: I'm fine... → 4 Nam: I'm fine, too.")]},
        {'id': 'r2', 'instr': 'Đọc và chọn True (Đúng) hoặc False (Sai).', 'passage': "<p>Hello. I'm Mai. I'm fine, thank you.</p>", 'items': [
            tf('r2.1', 'Her name is Mai.', 'T', 'I\'m Mai → tên bạn ấy là Mai.'), tf('r2.2', 'She says goodbye.', 'F', 'Bạn ấy chào (Hello), chưa tạm biệt.'), tf('r2.3', 'Mai is fine.', 'T', "I'm fine → Mai khỏe.")]},
        {'id': 'r3', 'instr': 'Đọc hội thoại và chọn True hoặc False.', 'passage': "<p><b>Nam:</b> Hi, Lan. How are you?<br><b>Lan:</b> I'm fine, thanks. And you?<br><b>Nam:</b> I'm fine, too. Goodbye, Lan.<br><b>Lan:</b> Bye, Nam.</p>", 'items': [
            tf('r3.1', 'Nam asks "How are you?"', 'T', 'Nam hỏi Lan: How are you?'), tf('r3.2', 'Lan is not fine.', 'F', "Lan nói I'm fine."), tf('r3.3', 'They say goodbye.', 'T', 'Cả hai đều tạm biệt.'), tf('r3.4', "Lan says \"Hello\" at the end.", 'F', 'Cuối hội thoại Lan nói Bye.')]}])
    return [nghe, chinhta, bosung, doc]

def u1_tests(g):
    M = lambda *a: ('mcq',) + a
    F = lambda *a: ('fill',) + a
    O = lambda sent, e=None: ('order', '', sent, e or sent)
    X = lambda *a: ('match',) + a
    t1 = [M('___, I\'m Tony.', ['Hello', 'Fine', 'Bye'], 'Hello', 'Giới thiệu bắt đầu bằng lời chào.'),
          M('— How are you? — ___', ["I'm fine, thank you.", "I'm Mai.", 'Goodbye.'], "I'm fine, thank you.", 'Hỏi thăm → trả lời khỏe.'),
          M('— Goodbye, Nam. — ___', ['Bye, Mai.', 'Hello.', 'Fine.'], 'Bye, Mai.', 'Tạm biệt thì đáp Bye.'),
          M('— Nice to meet you. — ___', ['Nice to meet you, too.', 'Bye.', 'How are you?'], 'Nice to meet you, too.', 'Đáp lại làm quen.'),
          M('Chọn từ khác loại:', ['bye', 'goodbye', 'hello'], 'hello', 'bye, goodbye = tạm biệt; hello = chào.'),
          F('Hello, I\'m Mai. Nice to meet {_}.', 'you', 'Nice to meet you.'), F('How {_} you?', 'are', 'How are you?'),
          F("I'm {_}, thanks.", 'fine', "I'm fine, thanks."), F('Goodbye. See you {_}.', 'later', 'See you later.'), F('eyb → {_}', 'bye', 'bye'),
          O('Hello, Miss Hoa.', 'Hello, Miss Hoa.'), O("I'm fine, thanks.", "I'm fine, thanks."), O('How are you?', 'How are you?'),
          X('Nối:', ['How are you?', 'Goodbye!', 'Nice to meet you!', 'Hello!'], ['Hello!', 'Fine, thanks.', 'Nice to meet you, too!', 'Bye. See you later.'],
            ['Fine, thanks.', 'Bye. See you later.', 'Nice to meet you, too!', 'Hello!'], 'Mỗi câu nói có một câu đáp.'),
          O('Goodbye, Miss Hoa.', 'Goodbye, Miss Hoa.'),
          M('Chọn từ nghĩa "cảm ơn":', ['thank you', 'fine', 'bye'], 'thank you', 'thank you = cảm ơn.'),
          M('Chọn từ nghĩa "xin chào":', ['bye', 'goodbye', 'hi'], 'hi', 'hi = xin chào.'),
          M('Hi, Mai. ___ are you?', ['How', 'What', "I'm"], 'How', 'How are you?'),
          F('Thank {_}.', 'you', 'Thank you.'), F('lehol → {_}', 'hello', 'hello')]
    t2 = [M('Chọn từ nghĩa "tạm biệt":', ['hello', 'goodbye', 'hi'], 'goodbye', 'goodbye = tạm biệt.'),
          M('Chọn từ nghĩa "khỏe":', ['fine', 'name', 'how'], 'fine', 'fine = khỏe.'),
          M('Bye. ___ you later.', ['See', 'Fine', 'How'], 'See', 'See you later.'),
          M('— Hello, I\'m Nam. — ___', ["Hi, Nam. I'm Lan.", 'Fine, thanks.', 'Bye.'], "Hi, Nam. I'm Lan.", 'Chào lại và giới thiệu.'),
          M('Chọn từ khác loại:', ['hi', 'hello', 'thanks'], 'thanks', 'hi, hello = chào; thanks = cảm ơn.'),
          F('Thank {_}, Mai.', 'you', 'Thank you.'), F("{_} fine, thanks.", "I'm", "I'm fine."), F('Hi! How {_} you?', 'are', 'How are you?'),
          F('Nice to {_} you.', 'meet', 'Nice to meet you.'), F('nefi → {_}', 'fine', 'fine'),
          O('Goodbye, Minh.', 'Goodbye, Minh.'), O("Hi, Mai. I'm Minh.", "Hi, Mai. I'm Minh."), O('Bye. See you later.', 'Bye. See you later.'),
          X('Nối từ với nghĩa:', ['hello', 'goodbye', 'thank you', 'fine'], ['cảm ơn', 'khỏe', 'tạm biệt', 'xin chào'], ['xin chào', 'tạm biệt', 'cảm ơn', 'khỏe'], 'hello = xin chào; goodbye = tạm biệt; thank you = cảm ơn; fine = khỏe.'),
          O('Thank you, Ben.', 'Thank you, Ben.'),
          M('— Thank you. — ___', ['Thanks.', 'Hello.', 'How are you?'], 'Thanks.', 'Cảm ơn nhau.'),
          M('Hello, ___ Linda.', ["I'm", 'How', 'Bye'], "I'm", "Hello, I'm Linda."),
          M('How ___ you, Ben?', ['are', 'am', 'is'], 'are', 'you → are.'),
          F('ohw → {_}', 'how', 'how'), F('G{_}odbye', 'o', 'goodbye')]
    t3 = [M('Bấm 🔊 và chọn từ em nghe được.', ['hello', 'goodbye', 'fine'], 'goodbye', 'Từ được đọc là goodbye.', None, True, 'goodbye'),
          M('Bấm 🔊, nghe câu hỏi rồi chọn câu trả lời.', ["I'm fine, thanks.", 'Bye.', "I'm Tony."], "I'm fine, thanks.", 'Hỏi thăm → trả lời khỏe.', None, True, 'How are you?'),
          M('— Hi, I\'m Mai. — ___', ["Hello, Mai. I'm Nam.", 'Fine, thanks.', 'Goodbye.'], "Hello, Mai. I'm Nam.", 'Chào lại.'),
          M('Chọn từ khác loại:', ['bye', 'goodbye', 'hi'], 'hi', 'bye, goodbye = tạm biệt.'),
          M('Nice to meet ___.', ['you', 'fine', 'bye'], 'you', 'Nice to meet you.'),
          F('Good{_}! (chào buổi sáng)', 'morning', 'Good morning = chào buổi sáng.'), F("I'm fine, thank {_}.", 'you', 'thank you'),
          F('See you {_}.', 'later', 'See you later.'), F('{_} are you?', 'How', 'How are you?'), F('kthna uoy → {_}', 'thank you', 'thank you'),
          O('How are you, Lan?', 'How are you, Lan?'), O('Hello, Quan.', 'Hello, Quan.'), O("I'm Phong.", "I'm Phong."),
          X('Nối:', ['Hello!', 'Goodbye!', 'How are you?', 'Nice to meet you!'], ['Fine, thanks.', 'Nice to meet you, too!', 'Hi!', 'Bye.'], ['Hi!', 'Bye.', 'Fine, thanks.', 'Nice to meet you, too!'], 'Mỗi câu nói có một câu đáp.'),
          O('Goodbye, Miss Hoa.', 'Goodbye, Miss Hoa.'),
          M('Chọn từ nghĩa "chào" (thân mật):', ['hi', 'thanks', 'fine'], 'hi', 'hi = chào.'),
          M('— Good___! (chúc ngủ ngon)', ['night', 'fine', 'how'], 'night', 'Good night.'),
          M('I\'m ___, thank you.', ['fine', 'bye', 'hello'], 'fine', "I'm fine."),
          M('Hello, I\'m Nam. ___ to meet you.', ['Nice', 'Fine', 'Bye'], 'Nice', 'Nice to meet you.'),
          F('lehol → {_}', 'hello', 'hello'), F('G{_}odbye', 'o', 'goodbye')]
    return [t1, t2, t3]

# ---------------------------------------------------------------- UNIT 2
def u2_pages(g):
    mcq, fill, order, match = g.mcq, g.fill, g.order, g.match
    num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    so = pg('so-dem', 'Số đếm 1–10', [
        {'id': 's1', 'instr': 'Nối số với chữ (số 1–5).', 'items': [match('s1.1', '', ['1', '2', '3', '4', '5'], ['three', 'five', 'one', 'four', 'two'], ['one', 'two', 'three', 'four', 'five'], '1 one, 2 two, 3 three, 4 four, 5 five.')]},
        {'id': 's2', 'instr': 'Nối số với chữ (số 6–10).', 'items': [match('s2.1', '', ['6', '7', '8', '9', '10'], ['nine', 'ten', 'six', 'eight', 'seven'], ['six', 'seven', 'eight', 'nine', 'ten'], '6 six, 7 seven, 8 eight, 9 nine, 10 ten.')]},
        {'id': 's3', 'instr': 'Viết số bằng chữ.', 'items': [fill('s3.%d' % (k + 1), '%d = {_}' % (k + 1), num[k], '%d = %s' % (k + 1, num[k])) for k in (0, 2, 4, 6, 8)]},
        {'id': 's4', 'instr': 'Sắp xếp lại chữ cái thành số.', 'items': [fill('s4.1', 'net → {_}', 'ten', 'ten'), fill('s4.2', 'vense → {_}', 'seven', 'seven'), fill('s4.3', 'veif → {_}', 'five', 'five'),
                                                                       fill('s4.4', 'neni → {_}', 'nine', 'nine'), fill('s4.5', 'rofu → {_}', 'four', 'four'), fill('s4.6', 'theig → {_}', 'eight', 'eight'), fill('s4.7', 'xis → {_}', 'six', 'six')]}])
    nghe = pg('nghe', 'Nghe', [
        {'id': 'n1', 'instr': 'Nghe 1. Bấm 🔊 và chọn số em nghe được.', 'items': [
            mcq('n1.%d' % (k + 1), 'Em nghe số mấy?', o, a, '%s = %s' % (w, a), say=w) for k, (w, o, a) in enumerate([('three', ['2', '3', '8'], '3'), ('seven', ['6', '7', '9'], '7'), ('ten', ['1', '10', '5'], '10'), ('eight', ['4', '8', '9'], '8'), ('five', ['5', '6', '4'], '5')])]},
        {'id': 'n2', 'instr': 'Nghe 2. Nghe câu hỏi và chọn câu trả lời.', 'items': [
            mcq('n2.1', 'Em nghe câu hỏi:', ["My name's Nam.", "I'm eight years old.", "I'm fine."], "My name's Nam.", "What's your name? → My name's…", say="What's your name?"),
            mcq('n2.2', 'Em nghe câu hỏi:', ["I'm eight years old.", "My name's Mai.", 'Goodbye.'], "I'm eight years old.", 'How old are you? → I\'m … years old.', say='How old are you?'),
            mcq('n2.3', 'Em nghe câu hỏi:', ["I'm fine, thanks.", "My name's Ben.", "I'm nine years old."], "I'm fine, thanks.", 'How are you? → I\'m fine.', say='How are you?'),
            mcq('n2.4', 'Em nghe câu:', ["Hi, Linda. I'm Tom.", "I'm ten years old.", 'Bye.'], "Hi, Linda. I'm Tom.", 'Chào lại và giới thiệu.', say="Hello, I'm Linda.")]},
        {'id': 'n3', 'instr': 'Nghe 3. Nghe và viết số bằng chữ.', 'items': [fill('n3.%d' % (k + 1), '{_}', w, w, say=w) for k, w in enumerate(['two', 'six', 'nine', 'four', 'ten'])]},
        {'id': 'n4', 'instr': 'Nghe 4. Nghe và viết lại câu.', 'items': [
            fill('n4.1', '{_}', "What's your name?", "What's your name?", say="What's your name?"),
            fill('n4.2', '{_}', 'How old are you?', 'How old are you?', say='How old are you?'),
            fill('n4.3', '{_}', ["I'm eight years old.", 'I am eight years old.'], "I'm eight years old.", say="I'm eight years old.")]}])
    chinhta = pg('chinh-ta', 'Chính tả', [
        {'id': 'c1', 'instr': 'Điền chữ cái còn thiếu.', 'items': [fill('c1.1', 'o{_}r', 'u', 'our'), fill('c1.2', 'm{_}', 'y', 'my'), fill('c1.3', 'ho{_} old', 'w', 'how old'),
                                                                   fill('c1.4', 'wh{_}t', 'a', 'what'), fill('c1.5', 'y{_}ur', 'o', 'your'), fill('c1.6', 'na{_}e', 'm', 'name')]},
        {'id': 'c2', 'instr': 'Sắp xếp lại chữ cái thành từ đúng.', 'items': [fill('c2.1', 'ym → {_}', 'my', 'my'), fill('c2.2', 'wath → {_}', 'what', 'what'), fill('c2.3', 'ruyo → {_}', 'your', 'your'),
                                                                          fill('c2.4', 'mena → {_}', 'name', 'name'), fill('c2.5', 'ruo → {_}', 'our', 'our'), fill('c2.6', 'woh lod → {_}', 'how old', 'how old')]}])
    bosung = pg('mau-cau-2', 'Mẫu câu 2 (hỏi tuổi)', [
        {'id': 'e2', 'instr': 'Điền từ thích hợp.', 'items': [
            fill('e2.1', "What's {_} name? – My name's Nam.", 'your', "What's your name?"), fill('e2.2', 'How {_} are you? – I\'m nine years old.', 'old', 'How old are you?'),
            fill('e2.3', "My name's Lan. I'm five {_} old.", 'years', 'five years old'), fill('e2.4', "What's your {_}? – My name's Mary.", 'name', "What's your name?"),
            fill('e2.5', 'How old {_} you? – I\'m ten.', 'are', 'How old are you?')]},
        {'id': 'f2', 'instr': 'Chọn đáp án đúng cho đoạn hội thoại.', 'items': [
            mcq('f2.1', "Bill: Hi. I'm Bill. What's ___ name?", ['our', 'your', 'you'], 'your', "What's your name?"),
            mcq('f2.2', 'Nam: Hello, Bill. My ___ Nam.', ["name's", 'name', 'names'], "name's", "My name's Nam."),
            mcq('f2.3', 'Bill: How ___ are you?', ['much', 'old', 'many'], 'old', 'How old are you?'),
            mcq('f2.4', 'Nam: I\'m ___ years old.', ['nice', 'fine', 'nine'], 'nine', "I'm nine years old.")]},
        {'id': 'g2', 'instr': 'Bấm các từ để xếp thành câu đúng.', 'items': [
            order('g2.1', '', "What's your name?", "What's your name?", seed=3), order('g2.2', '', 'My name is Mary.', 'My name is Mary.', seed=2),
            order('g2.3', '', 'How old are you?', 'How old are you?', seed=4), order('g2.4', '', "I'm ten years old.", "I'm ten years old.", seed=5),
            order('g2.5', '', 'Bill is seven years old.', 'Bill is seven years old.', seed=1), order('g2.6', '', 'Hello, my name is Nam.', 'Hello, my name is Nam.', seed=6),
            order('g2.7', '', 'His name is Keith.', 'His name is Keith. = Tên bạn ấy là Keith.', seed=7), order('g2.8', '', "She's eight years old.", "She's eight years old. = Bạn ấy 8 tuổi.", seed=2)]}])
    doc = pg('doc-hieu', 'Đọc hiểu', [
        {'id': 'r1', 'instr': 'Sắp xếp hội thoại: chọn số thứ tự (câu đầu tiên là số 0: "Linh: Hello, I\'m Linh.").', 'items': [
            match('r1.1', '', ["Mary: Hello, Linh. I'm Mary.", 'Mary: How old are you?', "Linh: I'm eight years old. How about you?", "Mary: I'm eight years old, too."], ['1', '2', '3', '4'], ['1', '2', '3', '4'],
                  "Thứ tự: 0 Linh: Hello, I'm Linh. → 1 Mary: Hello, Linh. I'm Mary. → 2 Mary: How old are you? → 3 Linh: I'm eight... → 4 Mary: I'm eight, too.")]},
        {'id': 'r2', 'instr': 'Đọc và chọn True hoặc False.', 'passage': "<p>Hello. My name's Linda. I'm nine years old.</p>", 'items': [
            tf('r2.1', 'Her name is Linda.', 'T', "My name's Linda."), tf('r2.2', 'She is ten years old.', 'F', 'Bạn ấy 9 tuổi (nine).'), tf('r2.3', 'Linda says hello.', 'T', 'Bài đọc mở đầu bằng Hello.')]},
        {'id': 'r3', 'instr': 'Đọc hội thoại và chọn True hoặc False.', 'passage': "<p><b>Bill:</b> Hi. I'm Bill. What's your name?<br><b>Nam:</b> Hello, Bill. My name's Nam.<br><b>Bill:</b> How old are you?<br><b>Nam:</b> I'm eight years old.</p>", 'items': [
            tf('r3.1', 'Bill asks about Nam\'s name.', 'T', "Bill hỏi What's your name?"), tf('r3.2', 'Nam is nine years old.', 'F', 'Nam 8 tuổi.'), tf('r3.3', 'Bill asks "How old are you?"', 'T', 'Bill hỏi tuổi Nam.'), tf('r3.4', "Nam's name is Bill.", 'F', 'Bill là tên của Bill; Nam là Nam.')]}])
    return [so, nghe, chinhta, bosung, doc]

def u2_tests(g):
    M = lambda *a: ('mcq',) + a
    F = lambda *a: ('fill',) + a
    O = lambda sent, e=None: ('order', '', sent, e or sent)
    X = lambda *a: ('match',) + a
    t1 = [M("What's your ___?", ['name', 'fine', 'bye'], 'name', "What's your name?"), M("___ name's Nam. Nice to meet you.", ['My', 'You', 'How'], 'My', "My name's Nam."),
          M('How old ___ you?', ['am', 'is', 'are'], 'are', 'How old are you?'), M("— What's your name? — ___", ["My name's Nam.", "I'm fine.", 'Goodbye.'], "My name's Nam.", 'Hỏi tên → nói tên.'),
          M('— How old are you? — ___', ["I'm nine years old.", "My name's Mai.", 'Fine, thanks.'], "I'm nine years old.", 'Hỏi tuổi → nói tuổi.'),
          F("What's {_} name?", 'your', "What's your name?"), F("{_} name's Tim.", 'My', "My name's Tim."), F('How {_} are you?', 'old', 'How old are you?'),
          F("I'm eight {_} old.", 'years', 'eight years old'), F('wath → {_}', 'what', 'what'),
          O("What's your name?", "What's your name?"), O('My name is Linda.', 'My name is Linda.'), O('How old are you?', 'How old are you?'),
          X('Nối:', ["What's your name?", 'How old are you?', 'How are you?', "Hello. I'm Mary."], ["I'm fine, thank you.", 'Hi, Mary.', "My name's Tony.", "I'm ten years old."],
            ["My name's Tony.", "I'm ten years old.", "I'm fine, thank you.", 'Hi, Mary.'], 'Mỗi câu hỏi có một câu đáp.'),
          O("I'm ten years old.", "I'm ten years old."),
          M('Chọn từ nghĩa "của bạn":', ['your', 'my', 'name'], 'your', 'your = của bạn.'), M('Chọn từ nghĩa "của tôi":', ['your', 'my', 'what'], 'my', 'my = của tôi.'),
          M('Chọn từ khác loại:', ['six', 'ten', 'name'], 'name', 'six, ten là số.'), F('mena → {_}', 'name', 'name'), F('seven = số {_}', '7', 'seven = 7')]
    t2 = [M('Chọn từ nghĩa "tên":', ['name', 'old', 'how'], 'name', 'name = tên.'), M('Chọn từ nghĩa "cái gì":', ['what', 'my', 'your'], 'what', 'what = cái gì.'),
          M('My ___ is Linda.', ['name', 'old', 'fine'], 'name', 'My name is Linda.'), M('I\'m ten years ___.', ['old', 'name', 'fine'], 'old', 'ten years old.'),
          M('Chọn từ khác loại:', ['my', 'your', 'seven'], 'seven', 'my, your = của; seven là số.'),
          F('What\'s your {_}?', 'name', "What's your name?"), F('How old {_} you?', 'are', 'How old are you?'), F("I'm nine {_} old.", 'years', 'nine years old'),
          F('ruyo → {_}', 'your', 'your'), F('woh lod → {_}', 'how old', 'how old'),
          O('My name is Mary.', 'My name is Mary.'), O('Bill is seven years old.', 'Bill is seven years old.'), O('Hello, my name is Nam.', 'Hello, my name is Nam.'),
          X('Nối từ với nghĩa:', ['what', 'your', 'my', 'name'], ['tên', 'của tôi', 'cái gì', 'của bạn'], ['cái gì', 'của bạn', 'của tôi', 'tên'], 'what = cái gì; your = của bạn; my = của tôi; name = tên.'),
          O("What's your name?", "What's your name?"),
          M("— Hi. I'm Bill. What's your name? — ___", ["Hello, Bill. My name's Nam.", "I'm fine.", 'Bye.'], "Hello, Bill. My name's Nam.", 'Chào lại và nói tên.'),
          M('— How are you? — ___', ["I'm fine, thanks.", "I'm ten.", "My name's Ben."], "I'm fine, thanks.", 'Hỏi thăm → khỏe.'),
          M('Hello. ___ name\'s Mai.', ['My', 'You', 'Fine'], 'My', 'My name\'s Mai.'), F('Số 5 viết là: {_}', 'five', 'five'), F('theig → {_}', 'eight', 'eight')]
    t3 = [M('Bấm 🔊 và chọn số em nghe được.', ['3', '8', '10'], '8', 'Từ được đọc là eight.', None, True, 'eight'), M('Bấm 🔊, nghe câu hỏi rồi chọn câu trả lời.', ["My name's Mai.", "I'm nine.", 'Bye.'], "My name's Mai.", 'Hỏi tên → nói tên.', None, True, "What's your name?"),
          M('How ___ are you?', ['old', 'name', 'what'], 'old', 'How old are you?'), M("Hello. My name's Linda. Nice to meet ___.", ['you', 'fine', 'bye'], 'you', 'Nice to meet you.'),
          M('Chọn từ khác loại:', ['Peter', 'Linda', 'how'], 'how', 'Peter, Linda là tên người.'),
          F('{_} your name?', ["What's", 'What is'], "What's your name?"), F('My {_} is Mary.', 'name', 'My name is Mary.'), F("How old are {_}?", 'you', 'How old are you?'),
          F('Số 9 viết là: {_}', 'nine', 'nine'), F('ruo → {_}', 'our', 'our'),
          O("I'm eight years old.", "I'm eight years old."), O('Her name is Mai.', 'Her name is Mai.'), O('How old are you?', 'How old are you?'),
          X('Nối số với chữ:', ['2', '4', '6', '9'], ['six', 'nine', 'two', 'four'], ['two', 'four', 'six', 'nine'], '2 two; 4 four; 6 six; 9 nine.'),
          O('His name is Keith.', 'His name is Keith.'),
          M('— How old are you? — ___', ["I'm eight years old.", "I'm Mai.", 'Goodbye.'], "I'm eight years old.", 'Nói tuổi.'), M('Chọn từ nghĩa "bao nhiêu tuổi":', ['how old', 'what', 'name'], 'how old', 'how old = bao nhiêu tuổi.'),
          M('___ is your name? (hỏi tên)', ['What', 'How', 'Fine'], 'What', 'What is your name?'), F('mena → {_}', 'name', 'name'), F('Hello, my {_} is Mai.', 'name', 'my name is Mai.')]
    return [t1, t2, t3]
