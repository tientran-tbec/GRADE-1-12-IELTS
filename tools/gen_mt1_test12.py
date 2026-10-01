"""Chuyển đổi 1 lần: Đề ôn tập giữa HK1 Anh 11 Global – ĐỀ 3 (src/mt1/d3.txt, 83 dòng, đủ 32 câu) -> units/mt1_test12.py.
Đề ngắn về số dòng nhưng ĐỦ các phần: nghe 10 (điền 5 + trắc nghiệm 5), âm 4, đọc 4, ngữ pháp 4, từ loại 6, viết lại 4 (= 32 câu).
Audio: audio/mt1_test12.mp3 = Part-1 (viewpoints) + 3 giây im lặng + Part-2 (history of cities), ffmpeg mono 64kbps.
Dữ liệu viết tay từ nguồn (đã sửa lỗi gõ); đáp án ở units/mt1_test12_dapan.py (Word không có khoá -> tự giải + Whisper)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import gen_units as G

SRC = open(os.path.join(G.ROOT, 'src/mt1/d3.txt'), encoding='utf8').read()
assert 'pessimistic' in SRC and 'Tự luận' in SRC


def M(i, q, o):
    return {'id': i, 't': 'mcq', 'q': q, 'o': o}


def F(i, q, **kw):
    d = {'id': i, 't': 'fill', 'q': q}
    d.update(kw)
    return d


LIS = ('<p>According to the pessimistic viewpoint, our future cities will not be safe and <b>(1) ______</b> places to live in. '
       'Governments have no <b>(2) ______</b> ways to control pollution, which will continue to be a serious problem in the future. '
       'Moreover, cities will become <b>(3) ______</b>, which means there will be more waste and heavier traffic.</p>'
       '<p>According to the optimistic viewpoint, city dwellers will have a better life thanks to advances in technology and <b>(4) ______</b>. '
       'Furthermore, the environmental problems will be solved. <b>(5) ______</b> energy sources will gradually replace fossil fuels in the next twenty years.</p>')

READ = ('<p>The family dynamic evolves as a teen matures, and can test the parent-teen relationship. With both sides feeling mixed emotions, this time can be challenging.</p>'
        '<p>Puberty brings lots of emotions for teens, and is a time of readjustment for the whole family. Parents have a huge influence on a young child\'s values and interests, '
        'and so it can often feel hard for them to separate from their teen, who wants to develop their own identity and to have new freedoms. '
        '<b><u>This</u></b> may lead to conflict, as both parents and teens need time to figure out how to adapt the relationship.</p>'
        '<p>As teens get older, it is important for them to take on responsibilities. This highlights the valuable contribution each family member makes to a home, '
        'and teaches teens about what it\'s like to be an adult. Setting clear rules about routine and home life helps teens to know what\'s expected of them—even if they do complain or resist. '
        'Expectations go both ways, however, and so constant communication and flexibility when necessary will help avoid conflict.</p>'
        '<p>It is important for parents and teens to overcome life\'s many distractions in order to spend quality time together. '
        'For parents, maintaining a close relationship with a teen who is preprogrammed to separate from them can be tricky, but it helps to be present and <b><u>willing</u></b>. '
        'Talking about the things that are going well is as helpful as discussing areas of conflict.</p>')

groups = [
    {'id': 'g1', 'instr': 'I/ Listening (2 points) – Listen and complete the summaries of the two viewpoints.', 'passage': LIS,
     'items': [F('g1.%d' % n, 'Blank (%d): {_}' % n) for n in range(1, 6)]},
    {'id': 'g2', 'instr': 'Ex 2: Listen to the recording and choose the correct answer A, B, C or D.',
     'items': [
         M('g2.6', 'One hundred years ago, what percentage of the human population lived in cities?', ['10%', '20%', '40%', '80%']),
         M('g2.7', 'What led to the development of the first semi-permanent settlements?',
           ['Changes in the global climate', 'An increase in fresh water supplies', 'Improvements in healthcare', 'Advancements in agriculture']),
         M('g2.8', 'Which of these technologies developed because of the desire to trade with other cities?', ['Tractors', 'City walls', 'Roads', 'Aqueducts']),
         M('g2.9', 'Why did people first move into cities?', ['Jobs', 'Fun', 'Safety', 'More farmland']),
         M('g2.10', 'The global population is expected to peak at ______ billion.', ['7', '6', '9', '10']),
     ]},
    {'id': 'g3', 'instr': 'II/ Trắc nghiệm (3 points) – Circle A, B, C or D to indicate the word whose underlined part differs from the other three in pronunciation.',
     'items': [M('g3.11', '', ['m<u>u</u>scle', 's<u>u</u>ffer', 'yogh<u>u</u>rt', 'instr<u>u</u>ct']),
               M('g3.12', '', ['fr<u>e</u>sh', 'di<u>e</u>t', 'fl<u>e</u>sh', '<u>e</u>xercise'])]},
    {'id': 'g4', 'instr': 'Circle A, B, C, or D to indicate the word that differs from the other three in the position of the primary stress.',
     'items': [M('g4.13', '', ['asleep', 'avoid', 'formal', 'remind']),
               M('g4.14', '', ['robot', 'sensor', 'impress', 'urban'])]},
    {'id': 'g5', 'instr': 'Ex 3. Read the following text and choose the best answer.', 'passage': READ,
     'items': [
         M('g5.15', 'What is the main idea of the passage?', ['Puberty of teenagers', "Teens' romantic relationship", 'Parent-teen relationship', "Teens' responsibilities"]),
         M('g5.16', 'The word "<b>this</b>" in paragraph 2 refers to:',
           ['Puberty brings lots of emotions for teens', "Parents have a huge influence on a young child's values and interests",
            'Both parents and teens need time to adapt the relationship', 'Parents cannot separate from their teens who want to be free']),
         M('g5.17', 'The word "<b>willing</b>" is CLOSEST in meaning to', ['shocked', 'ready', 'strict', 'sympathetic']),
         M('g5.18', 'Which of the following is <b>NOT TRUE</b> about the solution as teens get older?',
           ['Complain and resist', 'Communicate constantly', 'Set rules about routine and home life', 'Ask teens to take on responsibilities']),
     ]},
    {'id': 'g6', 'instr': 'Ex 4. Circle A, B, C or D to indicate the correct answer to each of the following questions.',
     'items': [
         M('g6.19', 'I have never played badminton before. This is the first time I ______ to play it.', ['try', 'tried', 'have tried', 'am trying']),
         M('g6.20', 'We ______ eat as much fruit as possible in order to get enough vitamins for our bodies.', ['had better', 'should', 'ought to', 'All are correct']),
         M('g6.21', 'Your parents appear ______ with you, but also very fair.', ['strictly', 'strict', 'strictness', 'open-minded']),
         M('g6.22', 'At present, I ______ calm.', ['remain', 'remained', 'is remaining', 'was remaining']),
     ]},
    {'id': 'g7', 'instr': 'III/ Tự luận (5 points) – Ex 1. Complete the following sentences with the correct forms of the words in capitals.',
     'items': [
         F('g7.23', 'Raw meat and poultry may contain harmful {_}. <b>(BACTERIUM)</b>'),
         F('g7.24', 'Food with a lot of sugar is not very good for your skin, so you should cut down on {_} desserts and drinks. <b>(SUGAR)</b>'),
         F('g7.25', 'Many important {_} documents were destroyed when the library was burned. <b>(HISTORY)</b>'),
         F('g7.26', '{_} is one of the common characteristics of Generation Y. <b>(CURIOUS)</b>'),
         F('g7.27', 'Environmentalists say there is a high risk of {_} from the landfill site. <b>(POLLUTE)</b>'),
         F('g7.28', 'The disease spread quickly among the poor slum {_} of the city. <b>(DWELL)</b>'),
     ]},
    {'id': 'g8', 'instr': 'Ex 2. Rewrite the following sentences as long as the meaning is unchanged.',
     'items': [
         F('g8.29', "Why don't we go camping this summer?<br>How about {_}?", long=True),
         F('g8.30', 'It is forbidden for students to cheat in the exam.<br>Students {_}.', long=True),
         F('g8.31', "He hasn't played basketball for 6 months.<br>The last time {_}.", long=True),
         F('g8.32', 'It was such a dirty beach that I decided not to stay.<br>The beach {_}.', long=True),
     ]},
]

S = {'id': 'lop11-mt1-test12', 'title': 'Test 12 – Mid-term 1', 'grade': 11, 'unit': 'MidTerm1', 'theory': '',
     'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 45, 'audio': True, 'groups': groups}]}

if __name__ == '__main__':
    G.dump(os.path.join(G.ROOT, 'units/mt1_test12.py'), 'SET', S)
    print('TOTAL', sum(len(g['items']) for g in groups))
