"""Chuyển đổi 1 lần: Đề ôn tập giữa HK1 Anh 11 Global – ĐỀ 2 (src/mt1/d2.txt, 72 dòng, đủ 35 câu) -> units/mt1_test11.py.
Đề ngắn về số dòng nhưng ĐỦ các phần: nghe 10, âm 4, từ vựng/ngữ pháp 6, từ loại 3, chia động từ 3, viết lại 4, điền đoạn 5 (= 35 câu).
Audio: audio/mt1_test11.mp3 = Part-2 (Singapore, Q1-5) + 3 giây im lặng + Part-1 (generation gap, Q6-10)
(trong thư mục Word hai file bị đặt ngược thứ tự: Part-1 là bài nói về generation gap, Part-2 là Singapore).
Dữ liệu viết tay từ nguồn (đã sửa lỗi gõ); đáp án ở units/mt1_test11_dapan.py (Word không có khoá -> tự giải + Whisper)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import gen_units as G

SRC = open(os.path.join(G.ROOT, 'src/mt1/d2.txt'), encoding='utf8').read()
assert 'Singapore' in SRC and 'THE END' in SRC


def M(i, q, o):
    return {'id': i, 't': 'mcq', 'q': q, 'o': o}


def F(i, q, **kw):
    d = {'id': i, 't': 'fill', 'q': q}
    d.update(kw)
    return d


def T(i, q):
    return {'id': i, 't': 'tf', 'q': q}


SING = ('<p>Singapore is leading the way in smart city technology. Recently it has been recognized as the smartest city in the world. '
        "Singapore's Smart Nation program has introduced a <b>(1) ______</b> of smart technologies in both its public and private sectors.</p>"
        '<p>To help with transport efficiency, public <b>(2) ______</b> is being used in a trial to support transport planning. '
        'Data from fare cards to <b>(3) ______</b> in more than 5,000 vehicles, and the real-time tracking of buses, is analysed. '
        'The trial has achieved an impressive result with a 92% reduction in <b>(4) ______</b>.</p>'
        '<p>Contactless payment technology has been introduced to control the movements and payments of the 7.5 million passengers '
        'who use public transport each day. As a result, commuters can pay using contactless cards or mobile wallets, '
        'making their <b>(5) ______</b> even more convenient.</p>')

CLOZE = ("<p>It's important to include fruit and vegetables in your daily diet. Most of us can <b>(31) ______</b> from eating a lot of fruit and vegetables, "
         'together with a balanced and healthy diet, and an active lifestyle. With their vitamins and minerals, they can definitely keep you in good health. '
         'Fruit and vegetables can also protect you against some infectious <b>(32) ______</b>.</p>'
         "<p>It's best to buy and eat fruits and vegetables when they are in <b>(33) ______</b>, when they are being produced in the area and ready to eat. "
         'Freshness and quality are the most important when choosing fruits and vegetables.</p>'
         '<p>You <b>(34) ______</b> eat at least five serves of vegetables and two serves of fruit per day. '
         'If possible, include different colours and kinds of fruits and vegetables for your daily diet.</p>'
         '<p>In case you do not really <b>(35) ______</b> eating fruit and vegetables, start slowly with those you do like. '
         'You can be creative with the way to prepare or cook them to disguise them in sauces, minced meals and curries.</p>')

groups = [
    {'id': 'g1', 'instr': 'Listen to a talk about Singapore – one of the smartest cities in the world. Complete each blank with no more than two words.',
     'passage': SING, 'items': [F('g1.%d' % n, 'Blank (%d): {_}' % n) for n in range(1, 6)]},
    {'id': 'g2', 'instr': 'Listen to a school student talking about how to deal with the generation gap. Decide whether the statements are true or false.',
     'items': [
         T('g2.6', 'Older people and little children should be cared for in different ways.'),
         T('g2.7', 'Community care centres help old people with their storytelling skills.'),
         T('g2.8', 'Young people can help old people with their storytelling skills.'),
         T('g2.9', 'Helping old people can make young students more confident.'),
         T('g2.10', 'Some young people enjoy personal stories about the war of the older.'),
     ]},
    {'id': 'g3', 'instr': 'Choose the word whose underlined part is pronounced differently from the other three.',
     'items': [M('g3.11', '', ['nat<u>ure</u>', 'mat<u>ure</u>', 'cult<u>ure</u>', 'post<u>ure</u>']),
               M('g3.12', '', ['ex<u>a</u>mine', 'fin<u>a</u>ncial', 'priv<u>a</u>cy', 'inter<u>a</u>ct'])]},
    {'id': 'g4', 'instr': 'Choose the word whose stress pattern is different from the other three.',
     'items': [M('g4.13', '', ['sensor', 'muscle', 'fitness', 'adapt']),
               M('g4.14', '', ['properly', 'curious', 'bacteria', 'nutrient'])]},
    {'id': 'g5', 'instr': 'Choose the best option to complete the sentences.',
     'items': [
         M('g5.15', 'Many young people keep ______ by working out at the gym.', ['healthy', 'thin', 'fit', 'safe']),
         M('g5.16', 'Parents and children often ______ over small things.',
           ['come into conflicts', 'follow in their footsteps', 'bridge the generation gap', 'increase their life expectancy']),
         M('g5.17', 'Public transport is believed to be the ______ to the air pollution in big cities.', ['cause', 'key', 'explanation', 'treatment']),
         M('g5.18', "A: Let's join our green activities at school this Sunday? - B: That ______.",
           ['sounds greatly', 'sounds great', 'looks great', 'looks greatly']),
         M('g5.19', 'A: Can I borrow your mobile phone for a moment, please? - B: ______.',
           ["I'm sorry but that's not possible. I am expecting a call from a relative.", "I must say that it's not impossible.",
            'Feel free to use it. I am searching for information on the internet.', 'Sounds impossible. I need it.']),
         M('g5.20', 'I think you ______ respect the elderly.', ['must', 'should', "shouldn't", "mustn't"]),
     ]},
    {'id': 'g6', 'instr': 'Put the word in brackets into the correct form to complete the following sentences.',
     'items': [
         F('g6.21', "Living with an extended family enhances children's {_} with other people. <b>(INTERACT)</b>"),
         F('g6.22', "Moving out of their parents' house after getting married is considered {_} in Vietnamese culture. <b>(TRADITION)</b>"),
         F('g6.23', 'I watch {_} programmes on the internet every day to pick up knowledge to have a healthy lifestyle. <b>(FIT)</b>'),
     ]},
    {'id': 'g7', 'instr': 'Supply the correct form of the verbs below.',
     'items': [
         F('g7.24', "At present, many people {_} <b>(remain)</b> single throughout their life. They don't want to get married."),
         F('g7.25', 'How many goals {_} <b>(your team / score)</b> in the first half?'),
         F('g7.26', 'She {_} <b>(want)</b> to be a police officer since she was a child.'),
     ]},
    {'id': 'g8', 'instr': 'Rewrite the following sentences without changing their meaning.',
     'items': [
         F('g8.27', 'Younger people need to show their respect to the seniors.<br>It is necessary {_}', long=True),
         F('g8.28', "We haven't seen our uncle for a long time.<br>It has {_}", long=True),
         F('g8.29', 'Young people tend to be more creative than old people.<br>Young people are more {_}', long=True),
         F('g8.30', 'Differences in thinking can cause conflicts between parents and children.<br>Conflicts between {_}', long=True),
     ]},
    {'id': 'g9', 'instr': 'Read the text about eating healthily and choose the best option to complete it.',
     'passage': CLOZE,
     'items': [
         M('g9.31', 'Blank (31)', ['suffer', 'advantage', 'benefit', 'develop']),
         M('g9.32', 'Blank (32)', ['diseases', 'enemies', 'problems', 'cancers']),
         M('g9.33', 'Blank (33)', ['store', 'time', 'season', 'demand']),
         M('g9.34', 'Blank (34)', ['can', 'should', 'have to', 'will']),
         M('g9.35', 'Blank (35)', ['look forward to', 'look at', 'look in', 'look for']),
     ]},
]

S = {'id': 'lop11-mt1-test11', 'title': 'Test 11 – Mid-term 1', 'grade': 11, 'unit': 'MidTerm1', 'theory': '',
     'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 45, 'audio': True, 'groups': groups}]}

if __name__ == '__main__':
    G.dump(os.path.join(G.ROOT, 'units/mt1_test11.py'), 'SET', S)
    print('TOTAL', sum(len(g['items']) for g in groups))
