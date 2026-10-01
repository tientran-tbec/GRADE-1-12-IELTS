# -*- coding: utf-8 -*-
"""Dữ liệu nội dung SET (sinh từ file Word bằng tools/gen_units.py rồi có thể chỉnh tay).
Đáp án + giải thích: xem file *_dapan.py cùng tên."""

SET = {'id': 'lop11-mt1-test06',
 'title': 'Test 6 – Mid-term 1',
 'grade': 11,
 'unit': 'MidTerm1',
 'theory': '',
 'pages': [{'id': 'kiem-tra',
            'title': 'Làm bài',
            'mode': 'test',
            'minutes': 60,
            'audio': True,
            'groups': [{'id': 'g1',
                        'instr': 'PART 1: LISTENING. I. Listen to a speech and decide whether the following statements are true (T) or false (F). '
                                 'You will listen TWICE.',
                        'items': [{'id': 'g1.1', 't': 'tf', 'q': 'Your diet may significantly affect your mood and sense of wellness.'},
                                  {'id': 'g1.2',
                                   't': 'tf',
                                   'q': 'Processed meats, packaged meals, takeout food, and sugary snacks are popular in Western meals.'},
                                  {'id': 'g1.3',
                                   't': 'tf',
                                   'q': 'Increasing the amount of sugar may help to improve mood and lower your risk for mental health problems.'},
                                  {'id': 'g1.4',
                                   't': 'tf',
                                   'q': 'You will have to completely eliminate the foods you enjoy to have a healthy diet.'}]},
                       {'id': 'g2',
                        'instr': 'II. Listen to a talk about Bjarke Ingels and his company’s architectural projects and complete each of the '
                                 'sentences with ONE WORD. You will listen TWICE.',
                        'items': [{'id': 'g2.5',
                                   't': 'fill',
                                   'q': 'Architectural projects designed by Bjarke Ingels Group are believed to shape the {_}.',
                                   'hint': 'ONE WORD'},
                                  {'id': 'g2.6',
                                   't': 'fill',
                                   'q': 'In Copenhagen, Bjarke Ingels Group built houses made of {_}.',
                                   'hint': 'ONE WORD'},
                                  {'id': 'g2.7',
                                   't': 'fill',
                                   'q': 'The power plant in Copenhagen is believed to be the cleanest as it doesn’t produce any {_}.',
                                   'hint': 'ONE WORD'},
                                  {'id': 'g2.8',
                                   't': 'fill',
                                   'q': 'People can even go skiing on the sloping {_} of the power plant.',
                                   'hint': 'ONE WORD'}]},
                       {'id': 'g3',
                        'instr': 'PART 2: LEXICO-GRAMMAR. I. Write the letter A, B, C, or D on your answer sheet to indicate the correct answer to '
                                 'each of the following questions.',
                        'items': [{'id': 'g3.9',
                                   't': 'mcq',
                                   'q': 'Some of the tasks required considerable physical ______.',
                                   'o': ['strength', 'coordination', 'endurance', 'flexibility']},
                                  {'id': 'g3.10',
                                   't': 'mcq',
                                   'q': 'There have been great advances in the ______ of cancer.',
                                   'o': ['treatment', 'prevention', 'diagnosis', 'research']},
                                  {'id': 'g3.11',
                                   't': 'mcq',
                                   'q': 'Peter has decided to ______ football at the end of this season.',
                                   'o': ['give up', 'take over', 'sign up for', 'drop in']},
                                  {'id': 'g3.12',
                                   't': 'mcq',
                                   'q': 'Widespread gardening provides an opportunity for exercise, sunlight and ______ food for people in Okinawa, '
                                        'Japan.',
                                   'o': ['nutritiously', 'nutrient', 'nutritious', 'nutrition']},
                                  {'id': 'g3.13',
                                   't': 'mcq',
                                   'q': 'He is a doctor and expects his son to follow in his ______.',
                                   'o': ['footwear', 'footwork', 'foot movements', 'footsteps']},
                                  {'id': 'g3.14',
                                   't': 'mcq',
                                   'q': 'We need to seriously consider all the different ______ about the issue.',
                                   'o': ['views', 'sights', 'pictures', 'games']},
                                  {'id': 'g3.15',
                                   't': 'mcq',
                                   'q': 'I was stuck in a(n) ______ for an hour yesterday.',
                                   'o': ['traffic jam', 'parking lot', 'subway', 'street light']},
                                  {'id': 'g3.16',
                                   't': 'mcq',
                                   'q': 'The boy has impressed his doctors ______ his courage and determination.',
                                   'o': ['in', 'for', 'with', 'by']},
                                  {'id': 'g3.17',
                                   't': 'mcq',
                                   'q': 'Jane ______ to be a nurse when she grows up.',
                                   'o': ['is wanting', 'was wanting', 'wants', 'want']},
                                  {'id': 'g3.18',
                                   't': 'mcq',
                                   'q': 'You ______ eat more vegetables if you want to stay healthy.',
                                   'o': ['shouldn’t', 'mustn’t', 'don’t have to', 'should']},
                                  {'id': 'g3.19',
                                   't': 'mcq',
                                   'q': 'Unworthy buildings should be demolished to make room ______ modern construction.',
                                   'o': ['of', 'to', 'for', 'at']}]},
                       {'id': 'g4',
                        'instr': 'II. Read the following advertisement and mark the letter A, B, C and D on your answer sheet to indicate the option '
                                 'that best fits each of the numbered blanks.',
                        'passage': '<p>Our vision is to encourage <b>(20) ______</b> in every aspect of urban life, from renewable energy systems to '
                                   'smart public transport. Each citizen is encouraged to <b>(21) ______</b> responsibility for protecting the '
                                   'environment and reducing waste. <b>(22) ______</b> building in the city is powered by clean energy and '
                                   'surrounded by green spaces that keep the air fresh and cool. All public areas are equipped <b>(23) ______</b> '
                                   'modern sensors that ensure safety and energy efficiency 24 hours a day. Be part of <b>(24) ______</b> project '
                                   'development urban that represents the future of smart living.</p>',
                        'items': [{'id': 'g4.20', 't': 'mcq', 'q': 'Blank (20)', 'o': ['innovate', 'innovative', 'innovation', 'innovatively']},
                                  {'id': 'g4.21', 't': 'mcq', 'q': 'Blank (21)', 'o': ['make', 'take', 'do', 'get']},
                                  {'id': 'g4.22', 't': 'mcq', 'q': 'Blank (22)', 'o': ['another', 'all', 'every', 'each']},
                                  {'id': 'g4.23', 't': 'mcq', 'q': 'Blank (23)', 'o': ['in', 'on', 'with', 'from']},
                                  {'id': 'g4.24',
                                   't': 'mcq',
                                   'q': 'Blank (24)',
                                   'o': ['development urban project',
                                         'urban project development',
                                         'project urban development',
                                         'project development urban']}]},
                       {'id': 'g5',
                        'instr': 'PART 3: READING. Read the following passage and mark the letter A, B, C, or D to indicate the answer to each of '
                                 'the questions.',
                        'passage': '<p>The concept of parental authority has changed. Today, no parent can take their children’s respect for '
                                   'granted: authority has to be earned. Several studies have shown the following problems.</p><p><b>Trust: </b>A '
                                   'lot of young people say their parents don’t trust them. Some of them have no privacy: their parents read all '
                                   'their emails, and enter their rooms without knocking. All of these actions demonstrate lack of respect. '
                                   'Consequently, these teenagers have little respect for their parents.</p><p><b>Communication: </b>Hardly any '
                                   'teens discuss their problems with their parents. That’s because very few teens feel their parents really listen '
                                   'to <b><u>them</u></b>. Instead, most parents tend to fire off an immediate response to their kids’ first '
                                   'sentence.</p><p><b>Freedom: </b>Interestingly, most rebels come from very <b><u>authoritarian</u></b> homes '
                                   'where kids have very little freedom. Teens need fewer rules, but they have to be clear and unchangeable. Also, '
                                   'if the mother and father don’t agree about discipline, teens have less respect for both parents. They also need '
                                   'a lot of support and a little freedom to take their own decisions. None of them enjoy just listening to '
                                   'adults.</p><p><b>Role models: </b>Teens don’t have much respect for their parents if neither of them actually '
                                   'does things that they expect their children to do. Like everybody, teens appreciate people who practise what '
                                   'they preach.</p>',
                        'items': [{'id': 'g5.25',
                                   't': 'mcq',
                                   'q': 'The word “<u>them</u>” in paragraph 3 refers to ______.',
                                   'o': ['their problems', 'the teens', 'their parents', 'the studies']},
                                  {'id': 'g5.26',
                                   't': 'mcq',
                                   'q': 'Which of the following is <b>NOT mentioned</b> as a cause of teenagers losing respect for their parents?',
                                   'o': ['Parents’ lack of trust and respect',
                                         'Parents’ failure to listen to their children',
                                         'Parents disagreeing about discipline',
                                         'Parents not helping their children with homework']},
                                  {'id': 'g5.27',
                                   't': 'mcq',
                                   'q': 'The word “<u>authoritarian</u>” in paragraph 4 is closest in meaning to ______.',
                                   'o': ['generous', 'strict', 'friendly', 'careless']},
                                  {'id': 'g5.28',
                                   't': 'mcq',
                                   'q': 'The main idea of the passage is ______.',
                                   'o': ['how parents can improve communication in their home',
                                         'the reasons why teens rebel against the parents’ authority',
                                         'what parents should or shouldn’t do to gain the children’s respect',
                                         'how the concept of parental authority has developed throughout history']},
                                  {'id': 'g5.29',
                                   't': 'mcq',
                                   'q': 'Teens don’t have much respect for their parents when ______.',
                                   'o': ['teens expect people to practise what they preach',
                                         'their parents agree about discipline for their children',
                                         'their parents don’t set a good example to their children',
                                         'their parents fire off an immediate response to them']}]},
                       {'id': 'g6',
                        'instr': 'PART 4: WRITING. I. Mark the letter A, B, C or D on your answer sheet to indicate the best arrangement of '
                                 'utterances or sentences to make a meaningful exchange or text in each of the following questions.',
                        'items': [{'id': 'g6.30',
                                   't': 'mcq',
                                   'q': 'a. Sure, I’d love to help! I know how to use TikTok. We can make a short video together.<br>b. That’s '
                                        'great! Thank you so much. It’s hard for me to understand how young people use social media these '
                                        'days.<br>c. Hi, Grandpa! You look a bit confused. Do you need any help with your phone?<br>d. Oh, hi dear. '
                                        'I’m trying to upload a family photo, but I don’t know how to do it.',
                                   'o': ['a – b – c – d', 'c – d – a – b', 'd – c – b – a', 'b – d – a – c']},
                                  {'id': 'g6.31',
                                   't': 'mcq',
                                   'q': 'a. Besides, parents should listen carefully and try to understand their children’s opinions.<br>b. As a '
                                        'result, they can find better ways to solve problems together instead of arguing.<br>c. In conclusion, both '
                                        'parents and teenagers need respect and communication to close the generation gap.<br>d. First, parents '
                                        'should spend more time talking with their teenagers to know their feelings.<br>e. Conflicts between parents '
                                        'and teenagers can be reduced if both sides learn to communicate more effectively.',
                                   'o': ['e – d – a – b – c', 'e – a – d – b – c', 'e – d – b – a – c', 'a – d – b – e – c']},
                                  {'id': 'g6.32',
                                   't': 'mcq',
                                   'q': 'a. These cities will use advanced technology to save energy and protect the environment.<br>b. Life in '
                                        'cities of the future is expected to be more comfortable and convenient.<br>c. Many smart devices will help '
                                        'people control their homes and transport easily.<br>d. However, people still need to learn how to live '
                                        'sustainably.<br>e. In conclusion, future cities will bring great benefits if humans use technology wisely.',
                                   'o': ['b – a – c – d – e', 'a – b – c – d – e', 'b – c – a – d – e', 'c – b – a – d – e']}]},
                       {'id': 'g7',
                        'instr': 'II. Supply the correct form or tense of the given verb in each of the following questions to make meaningful '
                                 'sentences. (1.0 pt)',
                        'items': [{'id': 'g7.33',
                                   't': 'fill',
                                   'q': 'Despite having a very busy schedule, she remains {_} and enthusiastic whenever she takes part in volunteer '
                                        'activities.',
                                   'hint': 'ENERGY'},
                                  {'id': 'g7.34',
                                   't': 'fill',
                                   'q': 'The teacher made a very strong {_} on the new students by showing kindness and understanding from the very '
                                        'first day.',
                                   'hint': 'IMPRESS'},
                                  {'id': 'g7.35', 't': 'fill', 'q': 'She always {_} happy whenever she talks about her family.', 'hint': 'look'},
                                  {'id': 'g7.36',
                                   't': 'fill',
                                   'q': 'She {_} a lot of experience in teaching since she started working at this international school.',
                                   'hint': 'gain'},
                                  {'id': 'g7.37', 't': 'fill', 'q': 'Students {_} their uniforms when they come to school.', 'hint': 'must / wear'}]},
                       {'id': 'g8',
                        'instr': 'III. For each question, complete the new sentence so that it means the same as the given one(s) using given words. '
                                 '(1.0 pt)',
                        'items': [{'id': 'g8.38',
                                   't': 'fill',
                                   'long': True,
                                   'q': '<b>She has never visited Ha Long Bay before</b> <i>(first)</i><br>→ This is the {_}'},
                                  {'id': 'g8.39',
                                   't': 'fill',
                                   'long': True,
                                   'q': '<b>The last time she saw her grandparents was in 2019</b><br>→ She has {_}'},
                                  {'id': 'g8.40',
                                   't': 'fill',
                                   'long': True,
                                   'q': '<b>It’s against the school rules for students to leave the campus during class time</b> <i>(using a modal '
                                        'verb)</i><br>→ Students {_}'},
                                  {'id': 'g8.41',
                                   't': 'fill',
                                   'long': True,
                                   'q': '<b>It would be better for you to talk to your parents when you have problems at school</b> <i>(using a '
                                        'modal verb)</i><br>→ You {_}'}]}]}]}
