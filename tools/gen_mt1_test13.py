"""Chuyển đổi 1 lần: Đề ôn tập giữa HK1 Anh 11 Global – ĐỀ 4 (src/mt1/d4.txt, 115 dòng, đủ 37 câu) -> units/mt1_test13.py.
Đề ngắn về số dòng nhưng ĐỦ các phần: nghe 10, âm 4, từ vựng/ngữ pháp 6, đọc 6, chia động từ 3 (5 ô), từ loại 4, viết lại 4 (= 37 câu).
Audio: audio/mt1_test13.mp3 = Part-1 (interview) + 3 giây im lặng + Part-2 (viewpoints), ffmpeg mono 64kbps.
Dữ liệu viết tay từ nguồn (đã sửa lỗi gõ); đáp án ở units/mt1_test13_dapan.py (Word không có khoá -> tự giải + Whisper)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import gen_units as G

SRC = open(os.path.join(G.ROOT, 'src/mt1/d4.txt'), encoding='utf8').read()
assert 'PHẦN TỰ LUẬN' in SRC and 'The best time to exercise' in SRC


def M(i, q, o):
    return {'id': i, 't': 'mcq', 'q': q, 'o': o}


def F(i, q, **kw):
    d = {'id': i, 't': 'fill', 'q': q}
    d.update(kw)
    return d


FORM = ('<p>According to the pessimistic viewpoint, our future cities will not be safe and <b>(6) ______</b> places to live in. '
        'Governments have no <b>(7) ______</b> ways to control pollution, which will continue to be a serious problem in the future. '
        'Moreover, cities will become <b>(8) ______</b>, which means there will be more waste and heavier traffic.</p>'
        '<p>According to the optimistic viewpoint, city dwellers will have a better life thanks to advances in technology and <b>(9) ______</b>. '
        'Furthermore, the environmental problems will be solved. Renewable energy sources will gradually replace <b>(10) ______</b> in the next twenty years.</p>')

READ = ('<h4>The best time to exercise</h4>'
        "<p>We all know the importance of exercise as a healthy habit. But what's the best time to exercise? Research has shown that morning, afternoon, or evening workouts have their own benefits. "
        'When you work out in the morning, you burn more fat. In fact, those who start their exercise routine on an empty stomach can burn about 20 per cent more body fat than those exercising later in the day. '
        'Morning exercise also helps many people sleep better at night.</p>'
        '<p>Afternoon or evening workouts can also bring benefits. Remember that your temperature is the highest between 2 p.m. and 6 p.m. This temperature helps increase your muscle strength and endurance. '
        'In the afternoon or evening, your reaction time is at its quickest, while your heart rate and blood pressure are the lowest. '
        'Exercising at this time decreases your chances of injury while improving your performance. '
        'So, depending on your schedule and preferences, you can choose the best time to work out.</p>')

groups = [
    {'id': 'g1', 'instr': 'PHẦN NGHE (2.0 pts) – Part 1: Listen and choose the correct information.',
     'items': [
         M('g1.1', 'What is the interview mainly about?',
           ['Advantages of living in a smart city.', 'Problems of living in a smart city.', 'Attractions of urban lifestyles.', 'Comforts of urban lifestyles.']),
         M('g1.2', 'How are cameras and sensors used in a smart city?',
           ['To collect information about city dwellers and their activities.', 'To collect information about the government and some companies.',
            "To improve city dwellers' safety and security.", 'To show the problems the police.']),
         M('g1.3', 'What do the government and some companies have?',
           ['So much information about city life', 'So much information about night life', 'So much private information about city residents', 'So much information about crimes.']),
         M('g1.4', 'Why does it take Miss Stevens a long time to get familiar with all the smart devices at home?',
           ['She has some friends to help.', "She doesn't have any neighborhood friends for help.", 'She gets some support from neighbors.', 'She does not know how to use smart devices.']),
         M('g1.5', 'Why does Ms Stevens feel lonely?',
           ["Because she doesn't interact with many people.", "Because she can't use the smart devices.", "Because she doesn't like her neighbourhood.", "Because she doesn't go out."]),
     ]},
    {'id': 'g2', 'instr': 'Part 2: Listen and complete the form below. No more than two words for each answer.', 'passage': FORM,
     'items': [F('g2.%d' % n, 'Blank (%d): {_}' % n) for n in range(6, 11)]},
    {'id': 'g3', 'instr': 'PHẦN TRẮC NGHIỆM – I. Write the letter A, B, C, or D to indicate the word whose underlined part differs from the other three in pronunciation. (0.5 pt)',
     'items': [M('g3.11', '', ['pr<u>i</u>vate', 'publ<u>i</u>c', 'c<u>i</u>ty', '<u>i</u>nteract']),
               M('g3.12', '', ['<u>s</u>olar', 'infra<u>s</u>tructure', 'de<u>s</u>igner', 'focu<u>s</u>'])]},
    {'id': 'g4', 'instr': 'II. Write the letter A, B, C, or D to indicate the word that differs from the other three in the position of primary stress. (0.5 pt)',
     'items': [M('g4.13', '', ['apartment', 'emission', 'location', 'harmony']),
               M('g4.14', '', ['article', 'privacy', 'quality', 'solution'])]},
    {'id': 'g5', 'instr': 'III. Write the letter A, B, C, or D to indicate the correct answer to each of the following questions. (1.5 pts)',
     'items': [
         M('g5.15', 'Have you been ______ by the doctor yet?', ['fixed', 'examined', 'investigated', 'repaired']),
         M('g5.16', 'Life ______ for smokers is shorter than for people who don\'t smoke.', ['strength', 'expectation', 'expectancy', 'routine']),
         M('g5.17', 'There are agreed rules in each family that its members ______ follow.', ["don't have to", 'must', "mustn't", 'had to']),
         M('g5.18', "My father ______ of going on a diet. He's put on weight recently.", ['thinks', 'is thinking', 'thought', 'has thought']),
         M('g5.19', 'Your store needs a bold sign that will catch the ______ of anyone walking down the street. That may help to sell more products.',
           ['eye', 'peek', 'flash', 'glimpse']),
         M('g5.20', 'The government ______ the infrastructure of big cities to boost the economy recently.', ['has improved', 'improved', 'should improve', 'improves']),
     ]},
    {'id': 'g6', 'instr': 'IV. Read the following passage and mark the letter A, B, C or D to indicate the correct answer to each of the questions. (1.5 pts)',
     'passage': READ,
     'items': [
         M('g6.21', 'What is the text mainly about?',
           ['Workouts at different times and their benefits.', 'Drawbacks of afternoon workouts.', 'Advantages of evening workouts.', 'Benefits of morning workouts and injuries.']),
         M('g6.22', 'Which of the following is a benefit of a morning workout?',
           ['You put on weight.', 'You gain more body fat.', "You have a better night's sleep.", 'You have an empty stomach.']),
         M('g6.23', "The word 'endurance' in paragraph 2 means ______.",
           ["the ability to see problems and solve them quickly without others' support",
            'the ability to continue doing something painful or difficult for a long period of time',
            'the ability to work both on your own and in a group', 'the ability to live a balanced life']),
         M('g6.24', 'Which of the following is a benefit of an afternoon or evening workout?',
           ['Your body temperature is the lowest.', 'Your reaction time is slow.', 'Your heart rate and blood pressure are the highest.', 'You can avoid the risk of injury.']),
         M('g6.25', "The word 'its' in paragraph 2 refers to ______.", ['afternoon', 'evening', 'reaction time', 'heart rate']),
         M('g6.26', "The phrase 'blood pressure' in paragraph 2 means ______.",
           ['a measure of the force with which blood flows through the body', 'the number of times the heart beats per minute',
            'the pressure on your chest', 'the stress that can cause heart problems']),
     ]},
    {'id': 'g7', 'instr': 'PHẦN TỰ LUẬN – I. Complete the sentences using the correct forms of the verbs in brackets. (1 pt) '
                          '(Ở câu 27 và 28, điền cả hai chỗ trống quanh động từ: trợ động từ và dạng đúng của động từ.)',
     'items': [
         F('g7.27', '{_} scientists <b>(discover)</b> {_} a new cancer drug yet?'),
         F('g7.28', 'I {_} <b>(buy)</b> {_} all the ingredients. Can you help me cook the dish now?'),
         F('g7.29', 'John {_} <b>(build)</b> muscles since he {_} <b>(start)</b> working out at the gym. He looks really fit now.'),
     ]},
    {'id': 'g8', 'instr': 'II. Supply the correct form of the given word in each of the following questions to make meaningful sentences. (1.0 pt)',
     'items': [
         F('g8.30', "This is a 'green city' designed to reduce its {_} impact on the environment. <b>(NEGATE)</b>"),
         F('g8.31', 'AI technologies, such as cameras and smart sensors, will be installed to help the city operate more {_}. <b>(EFFICIENCY)</b>'),
         F('g8.32', 'My grandparents hold {_} views about male jobs and gender roles. <b>(TRADITION)</b>'),
         F('g8.33', 'He is receiving {_} for his health problem. <b>(TREAT)</b>'),
     ]},
    {'id': 'g9', 'instr': 'III. For each question, complete the new sentence so that it means the same as the given one(s). (2 pts)',
     'items': [
         F('g9.34', 'It is not a good idea for women to leave their jobs after getting married. <b>(should not)</b><br>Women {_} married.', long=True),
         F('g9.35', 'It is important for all family members to follow the family house rules. <b>(must)</b><br>All family members {_}.', long=True),
         F('g9.36', 'It has been a long time since we last called each other.<br>We haven\'t {_}.', long=True),
         F('g9.37', 'When did you start the treatment?<br>How long {_}?', long=True),
     ]},
]

S = {'id': 'lop11-mt1-test13', 'title': 'Test 13 – Mid-term 1', 'grade': 11, 'unit': 'MidTerm1', 'theory': '',
     'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 45, 'audio': True, 'groups': groups}]}

if __name__ == '__main__':
    G.dump(os.path.join(G.ROOT, 'units/mt1_test13.py'), 'SET', S)
    print('TOTAL', sum(len(g['items']) for g in groups))
