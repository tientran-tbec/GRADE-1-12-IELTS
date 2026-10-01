"""Chuyển đổi 1 lần: Đề ôn tập giữa HK1 Anh 11 Global – ĐỀ 1 (dòng 1–163 của src/mt1/d1.txt; d1.txt là cả bộ 10 đề,
Đề 1 chỉ gồm phần đầu) -> units/mt1_test10.py.  Đề rất ngắn nên dữ liệu được viết tay từ nguồn (đã sửa lỗi gõ).
Audio: audio/mt1_test10.mp3 = Part-1 + 3 giây im lặng + Part-2 (ffmpeg, mono 64kbps).
Đáp án + giải thích: units/mt1_test10_dapan.py (khoá Word chỉ có ở Q1–5 phần nghe; phần còn lại tự giải, phần nghe đối chiếu Whisper)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import gen_units as G

SRC = open(os.path.join(G.ROOT, 'src/mt1/d1.txt'), encoding='utf8').read().split('\n')[:165]
assert 'ĐỀ 1' in SRC[3] and 'ĐỀ' in open(os.path.join(G.ROOT, 'src/mt1/d1.txt'), encoding='utf8').read().split('\n')[168]


def M(i, q, o):
    return {'id': i, 't': 'mcq', 'q': q, 'o': o}


def F(i, q, **kw):
    d = {'id': i, 't': 'fill', 'q': q}
    d.update(kw)
    return d


TBL = ('<table class="th"><tr><th colspan="2"><p>School play</p></th></tr>'
       '<tr><td><p>Date:</p></td><td><p>20th December</p></td></tr>'
       '<tr><td><p>Last day to buy tickets:</p></td><td><p><b>(6) ______</b></p></td></tr>'
       '<tr><td><p>Guests pay:</p></td><td><p><b>(7) £ ______</b></p></td></tr>'
       '<tr><td><p>Help needed to make:</p></td><td><p><b>(8) ______</b></p></td></tr>'
       '<tr><td><p>Teacher to talk to:</p></td><td><p><b>(9) Mr ______</b></p></td></tr>'
       '<tr><td><p>Things to sell:</p></td><td><p><b>(10) ______</b> &amp; ice cream</p></td></tr></table>')

READ = ('<p>In American, although most men still do less housework than their wives, that gap has been halved since the 1960s. '
        'Today, 41 per cent of couples say they share childcare equally, compared with 25 percent in 1985. '
        "Men's greater involvement at home is good for their relationships with their spouses, and also good for their children. "
        'Hands-on fathers make better parents than men who let their wives do all the nurturing and childcare. '
        'They raise sons who are more expressive and daughters who are more likely to do well in school - especially in math and science.</p>'
        '<p>In 1900, life expectancy in the United States was 47 years, and only four per cent of the population was 65 or older. '
        'Today, life expectancy is 76 years, and by 2025, it is estimated about 20 per cent of the U.S. population will be 65 or older. '
        'For the first time, a generation of adults must plan for the needs of both their parents and their children. '
        'Most Americans are responding with remarkable grace. One in four households gives the <b>equivalent</b> of a full day a week or more '
        'in unpaid care to an aging relative, and more than half say they expect to do so in the next 10 years. '
        'Older people are less likely to be impoverished or incapacitated by illness than in the past, '
        'and have more opportunity to develop a relationship with their grandchildren.</p>'
        '<p>Even some of the choices that worry people the most are turning out to be <b>manageable</b>. '
        'Divorce rates are likely to remain high, and in many cases marital breakdown causes serious problems for both adults and kids. '
        'Yet when parents minimize conflict, family bonds can be maintained. And many families are doing <b>this</b>. '
        'More non-custodial parents are staying in touch with their children. Child-support receipts are rising. '
        'A lower proportion of children from divorced families are exhibiting problems than in earlier decades. '
        "And stepfamilies are learning to maximize children's access to supportive adults rather than cutting them off from one side of the family.</p>")

groups = [
    {'id': 'g1', 'instr': 'PHẦN NGHE – Questions 1-5: For each question, choose the correct answer. You will listen twice. '
                          'You will hear Zoe talking to her friend, Pete, about a birthday party she is planning.',
     'items': [
         M('g1.1', "Why doesn't Zoe know how many guests will come to her party?",
           ["She hasn't sent the invitations yet.", "She hasn't decided who she wants to invite.", 'No one has received an invitation yet.']),
         M('g1.2', 'Guests will probably eat', ['simple food.', 'their own food.', 'pizza and chips.']),
         M('g1.3', 'Who has Zoe invited?', ['all her classmates', 'a small number of friends', "some people she doesn't know well"]),
         M('g1.4', "If the weather's good, Zoe", ['will have a barbecue in the garden.', 'will have her party in the garden.',
                                                  'will offer her friends some food outside.']),
         M('g1.5', "What will some of Zoe's friends do?", ['They will bring music CDs.', 'They will play musical instruments.',
                                                           'They will buy her a CD player.']),
     ]},
    {'id': 'g2', 'instr': 'PHẦN NGHE – Questions 6-10: For each question, write the correct answer in the gap. Write one word or a number or '
                          'a date or a time. You will hear a teacher talking to students about a school play. You will listen twice.',
     'passage': TBL,
     'items': [F('g2.%d' % n, 'Blank (%d): {_}' % n) for n in range(6, 11)]},
    {'id': 'g3', 'instr': 'PHẦN TRẮC NGHIỆM – I. Write the letter A, B, C, or D to indicate the word whose underlined part differs from the other three '
                          'in pronunciation in each of the following questions. (0.5 pt)',
     'items': [M('g3.11', '', ['dw<u>e</u>ller', 's<u>e</u>nsor', '<u>e</u>nergy', 'r<u>e</u>duce']),
               M('g3.12', '', ['c<u>o</u>ntrol', 'ec<u>o</u>nomic', 'c<u>o</u>nfidence', 'c<u>o</u>ndition'])]},
    {'id': 'g4', 'instr': 'II. Write the letter A, B, C, or D to indicate the word that differs from the other three in the position of primary stress '
                          'in each of the following questions. (0.5 pt)',
     'items': [M('g4.13', '', ['feature', 'sustain', 'predict', 'produce']),
               M('g4.14', '', ['permission', 'difference', 'argument', 'cultural'])]},
    {'id': 'g5', 'instr': 'III. Write the letter A, B, C, or D to indicate the correct answer to each of the following questions. (1.5 pts)',
     'items': [
         M('g5.15', "All students ______ complete their homework before going to class because it's a rule.", ['ought to', 'have to', 'must', 'should']),
         M('g5.16', "Parents can't always respond effectively to aggressive ______ of their children.", ['generation', 'thought', 'behaviour', 'roles']),
         M('g5.17', "To decide the winner of the competition, the examiners ______ candidates' dishes now.", ['taste', 'tasted', 'are tasting', 'was tasting']),
         M('g5.18', 'With better transportation, more people will be able to move around easily, and it will reduce traffic ______.',
           ['noise', 'pollution', 'congestion', 'transport']),
         M('g5.19', 'A smart city is a modern urban area that uses ______ technologies to provide services, solve problems, and support people better.',
           ['a great deal of', 'a range of', 'the number of', 'the amount of']),
         M('g5.20', 'All food products should carry a list of ______ on the packet.', ['areas', 'parts', 'ingredients', 'chemicals']),
     ]},
    {'id': 'g6', 'instr': 'IV. Read the following passage and mark the letter A, B, C or D to indicate the correct answer to each of the questions. (2.0 pts)',
     'passage': READ,
     'items': [
         M('g6.21', 'Which of the following can be the most suitable heading for paragraph 1?',
           ["Men's involvement at home", "Benefits of men's involvement at home", "Drawbacks of men's involvement at home", 'Children studying math and science']),
         M('g6.22', 'Nowadays, ______ of men help take care of children.', ['50%', '41%', '25%', '20%']),
         M('g6.23', 'According to the writer, old people in the USA ______.',
           ['are experiencing a shorter life expectancy', 'receive less care from their children than they used to',
            'have better relationships with their children and grandchildren', 'may live in worse living conditions']),
         M('g6.24', 'Which of the following is NOT true about divorce rates in the USA?',
           ['They will still be high.', 'They can cause problems for both parents and children.',
            'More problems are caused by children from divorced families.', 'Children are encouraged to meet their separate parents.']),
         M('g6.25', 'The word "<b>equivalent</b>" in paragraph 2 is closest in meaning to ______.', ['comparable', 'opposed', 'dissimilar', 'contrasting']),
         M('g6.26', 'The word "<b>manageable</b>" in paragraph 3 is closest in meaning to ______.', ['difficult', 'challenging', 'demanding', 'easy']),
         M('g6.27', 'The word "<b>this</b>" in paragraph 3 refers to ______.',
           ['getting divorced', 'minimizing conflict', 'causing problems to kids', 'maintaining bonds']),
         M('g6.28', 'According to the writer, the future of American family life can be ______.', ['positive', 'negative', 'unchanged', 'unpredictable']),
     ]},
    {'id': 'g7', 'instr': 'PHẦN TỰ LUẬN – I. Supply the correct form of the given word in each of the following questions to make meaningful sentences. (1.0 pt)',
     'items': [
         F('g7.29', "Spending more time outdoors can boost the body's {_} and ability to function well. <b>(STRONG)</b>"),
         F('g7.30', 'They may also be more sustainable, with green spaces and {_} energy sources. <b>(NEW)</b>'),
         F('g7.31', 'The {_} friendly products are designed not to harm the natural environment. <b>(ENVIRONMENT)</b>'),
         F('g7.32', '{_} is the fact of a country or city having too many people living in it. <b>(POPULATE)</b>'),
     ]},
    {'id': 'g8', 'instr': 'II. Fill in the blank with a suitable preposition. (1.0 pt)',
     'items': [
         F('g8.33', "I knew what food tasted good, but I didn't know what was good {_} my body."),
         F('g8.34', "Her parents' opinions make no difference {_} her decisions."),
         F('g8.35', "We're taking {_} new staff at the moment."),
         F('g8.36', 'Was it really fair {_} the elder sister to ask her to do all the housework?'),
     ]},
    {'id': 'g9', 'instr': 'III. For each question, complete the new sentence so that it means the same as the given one(s). (1.5 pts)',
     'items': [
         F('g9.37', 'John has worked for this electronics firm since 1999.<br>John started {_}', long=True),
         F('g9.38', "John doesn't get permission to use that computer.<br>John {_}", long=True),
         F('g9.39', 'What do you think about living in a smart city?<br>What is your {_}?', long=True),
     ]},
]

S = {'id': 'lop11-mt1-test10', 'title': 'Test 10 – Mid-term 1', 'grade': 11, 'unit': 'MidTerm1', 'theory': '',
     'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 45, 'audio': True, 'groups': groups}]}

if __name__ == '__main__':
    G.dump(os.path.join(G.ROOT, 'units/mt1_test10.py'), 'SET', S)
    print('TOTAL', sum(len(g['items']) for g in groups))
