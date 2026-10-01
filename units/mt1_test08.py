# -*- coding: utf-8 -*-
"""Dữ liệu nội dung SET (sinh từ file Word bằng tools/gen_units.py rồi có thể chỉnh tay).
Đáp án + giải thích: xem file *_dapan.py cùng tên."""

SET = {'id': 'lop11-mt1-test08',
 'title': 'Test 8 – Mid-term 1',
 'grade': 11,
 'unit': 'MidTerm1',
 'theory': '',
 'pages': [{'id': 'kiem-tra',
            'title': 'Làm bài',
            'mode': 'test',
            'minutes': 45,
            'audio': True,
            'groups': [{'id': 'g1',
                        'instr': 'PART 1. You will listen to Grace and Tom talking about exams and decide whether the statements are true or false. '
                                 'You will listen TWICE.',
                        'items': [{'id': 'g1.1', 't': 'tf', 'q': "Tom doesn't usually get good grades at school."},
                                  {'id': 'g1.2', 't': 'tf', 'q': "Grace thinks Tom will get sick if he doesn't relax."},
                                  {'id': 'g1.3', 't': 'tf', 'q': 'Tom admits that he feels confident and relaxed during exams.'},
                                  {'id': 'g1.4', 't': 'tf', 'q': "Grace doesn't get stressed about exams."}]},
                       {'id': 'g2',
                        'instr': 'PART 2. You will hear a lecture about climate changes. Listen and choose the correct answer A, B, C, or D to each '
                                 'of the following questions. You will hear the recording TWICE.',
                        'items': [{'id': 'g2.5',
                                   't': 'mcq',
                                   'q': 'A slight ______ in some of the colder parts of the world may improve conditions for agriculture.',
                                   'o': ['emission increase', 'emission decrease', 'temperature decrease', 'temperature increase']},
                                  {'id': 'g2.6',
                                   't': 'mcq',
                                   'q': 'The developed and industrialized world is responsible for ______ of all carbon dioxide emissions.',
                                   'o': ['a quarter', 'a half', 'three-fourths', 'two-thirds']},
                                  {'id': 'g2.7',
                                   't': 'mcq',
                                   'q': 'Which countries are expected to suffer the most from rising sea levels?',
                                   'o': ['European and North American countries',
                                         'Industrialized countries with large populations',
                                         'Poorer countries like Bangladesh',
                                         'Countries with less agriculture']},
                                  {'id': 'g2.8',
                                   't': 'mcq',
                                   'q': 'What could lead to hundreds of millions of climate refugees?',
                                   'o': ['The effect of deforestation',
                                         'The effect of drowning coastlines',
                                         'The effect of carbon dioxide emission',
                                         'The effect of tropical storms']}]},
                       {'id': 'g3',
                        'instr': 'Mark the letter A, B, C or D on your answer sheet to indicate the correct answer to each of the following '
                                 'questions.',
                        'items': [{'id': 'g3.9',
                                   't': 'mcq',
                                   'q': 'The government has introduced policies to improve citizens’ life ______ by enhancing healthcare and '
                                        'education.',
                                   'o': ['expectancy', 'expectational', 'expectation', 'expecting']},
                                  {'id': 'g3.10',
                                   't': 'mcq',
                                   'q': 'In traditional societies, young people ______ follow their parents’ advice when choosing a career.',
                                   'o': ['must', 'had to', 'were to', 'should']},
                                  {'id': 'g3.11',
                                   't': 'mcq',
                                   'q': 'My grandfather ______ work in the fields from dawn till dusk when he was young.',
                                   'o': ['used to', 'has to', 'had to', 'is used to']},
                                  {'id': 'g3.12',
                                   't': 'mcq',
                                   'q': 'In order to cope with global challenges, humans must quickly ______ to technological change.',
                                   'o': ['adapt', 'adopt', 'accept', 'attach']},
                                  {'id': 'g3.13',
                                   't': 'mcq',
                                   'q': 'Many megacities are facing serious ______ issues due to population growth and limited space.',
                                   'o': ['housing', 'households', 'home', 'inhabitant']},
                                  {'id': 'g3.14',
                                   't': 'mcq',
                                   'q': 'The newly renovated museum looks so ______ that everyone wants to take photos there.',
                                   'o': ['beautifully', 'beautify', 'beauty', 'beautiful']},
                                  {'id': 'g3.15',
                                   't': 'mcq',
                                   'q': 'Citizens ______ separate their household waste properly to reduce environmental pollution.',
                                   'o': ['need to', 'might', 'can', 'may not']},
                                  {'id': 'g3.16',
                                   't': 'mcq',
                                   'q': 'Reading the product’s ______ helps customers avoid items with harmful chemicals.',
                                   'o': ['composition', 'ingredient', 'label', 'description']},
                                  {'id': 'g3.17',
                                   't': 'mcq',
                                   'q': 'Future cities aim to be more ______ by combining innovation with environmental protection.',
                                   'o': ['sustainable', 'industrial', 'economic', 'temporary']},
                                  {'id': 'g3.18',
                                   't': 'mcq',
                                   'q': 'I firmly ______ that education is the key to bridging differences among generations.',
                                   'o': ['am believing', 'believe', 'beliefs', 'have believed']},
                                  {'id': 'g3.19',
                                   't': 'mcq',
                                   'q': 'Heavy ______ during rush hours causes serious delays in the city centre every day.',
                                   'o': ['traffic congestion', 'traffic lights', 'traffic jam', 'street noise']}]},
                       {'id': 'g4',
                        'instr': 'Read the following passage and mark the letter A, B, C or D on your answer sheet to choose the word or phrase that '
                                 'best fits each other numbered blanks.',
                        'passage': '<h4>BLUE DRAGON CHILDREN’S FOUNDATION</h4><p>Homeless people are a tragic sign in the cities of almost every '
                                   'country in the world, but the ones in the most difficult situation are the street children. No one knows the '
                                   'exact <b>(20) ______</b> of homeless children because they often fear and avoid authorities. Some have run away '
                                   'from home <b>(21) ______</b> family problems, while others have been forced to leave home because their parents '
                                   "simply didn't have enough money to support them. They struggle to <b>(22) ______</b> ends meet by shining shoes "
                                   "or selling small items like chewing gum. Blue Dragon Children's Foundation is a non-profit organisation which "
                                   'was founded by Michael Brosowski and Pham Sy Chung in 2004. It focuses on helping streets kids and rescuing '
                                   'children from slavery and human trafficking of social workers in Vietnam. Blue Dragon has worked <b>(23) '
                                   '______</b> to offer a variety of services which are led by a team of social workers, psychologists, teachers and '
                                   'lawyers. The charity provides children in need with shelters, nutritious meals and healthcare as well as helps '
                                   'them return to their families. It also makes sure that children can stay in school and receive a proper <b>(24) '
                                   '______</b> by supporting them with tuition fees and living expenses. Blue Dragon believes that every child '
                                   'deserves exceptional care so that they can have a better chance in life.</p>',
                        'items': [{'id': 'g4.20', 't': 'mcq', 'q': 'Blank (20)', 'o': ['plenty', 'amount', 'level', 'numbers']},
                                  {'id': 'g4.21', 't': 'mcq', 'q': 'Blank (21)', 'o': ['despite', 'although', 'as a result', 'because of']},
                                  {'id': 'g4.22', 't': 'mcq', 'q': 'Blank (22)', 'o': ['do', 'make', 'take', 'give']},
                                  {'id': 'g4.23', 't': 'mcq', 'q': 'Blank (23)', 'o': ['continuous', 'endless', 'limitless', 'nonstop']},
                                  {'id': 'g4.24', 't': 'mcq', 'q': 'Blank (24)', 'o': ['education', 'educated', 'educational', 'educating']}]},
                       {'id': 'g5',
                        'instr': 'Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each of the '
                                 'questions below.',
                        'passage': '<p>In today’s fast-paced world, maintaining a healthy lifestyle has become increasingly important. It means '
                                   'making conscious choices about what we eat, how often we exercise, and how well we sleep. By building healthy '
                                   'habits, we can prevent diseases, improve both physical and mental health, and enjoy life to the fullest.</p><p>A '
                                   'balanced diet provides the foundation for good health. Consuming fruits, vegetables, whole grains, lean '
                                   'proteins, and healthy fats gives the body essential nutrients. On the other hand, eating too much processed '
                                   'food, sugary drinks, or saturated fat may lead to obesity, heart disease, and other serious '
                                   'illnesses.</p><p>Regular exercise is another key factor. It strengthens muscles and bones, supports '
                                   'cardiovascular health, and lowers the risk of chronic conditions. Exercise also boosts mental well-being by '
                                   'releasing endorphins, natural chemicals that reduce stress and improve mood. Health experts recommend at least '
                                   '30 minutes of moderate-intensity physical activity each day.</p><p>Adequate sleep is equally vital. Getting 7–8 '
                                   'hours of quality rest improves memory, concentration, and emotional balance. Keeping a <b>consistent</b> sleep '
                                   'schedule, avoiding caffeine, and limiting electronic use before bed can help achieve better sleep.</p><p>In '
                                   'conclusion, a healthy lifestyle relies on three essential elements: a nutritious diet, regular exercise, and '
                                   'sufficient rest. By making small but consistent improvements, we can strengthen both body and mind, reduce '
                                   'health risks, and lead a happier and more fulfilling life. It is essential to prioritise healthy habits and make '
                                   '<b><u>them</u></b> a part of our daily routine.</p><p class="src"><i>(Adapted from Havard Health: Staying '
                                   'healthy)</i></p>',
                        'items': [{'id': 'g5.25',
                                   't': 'mcq',
                                   'q': 'What is the main idea of the passage?',
                                   'o': ['How to Have a Healthy Lifestyle',
                                         'The Importance of Exercises',
                                         'Our Daily Routine',
                                         'The Well-being of the Brain']},
                                  {'id': 'g5.26',
                                   't': 'mcq',
                                   'q': 'According to the passage, people should avoid ______ before bedtime to have a good sleep.',
                                   'o': ['processed food', 'caffeine', 'whole grains', 'endorphins']},
                                  {'id': 'g5.27',
                                   't': 'mcq',
                                   'q': 'The word “<u>them</u>” in the last paragraph is referred to ______.',
                                   'o': ['regular exercises', 'chronic diseases', 'small changes', 'healthy habits']},
                                  {'id': 'g5.28',
                                   't': 'mcq',
                                   'q': 'The word “consistent” in paragraph 4 is OPPOSITE in meaning to ______',
                                   'o': ['changeable', 'regular', 'positive', 'beneficial']},
                                  {'id': 'g5.29',
                                   't': 'mcq',
                                   'q': 'Which of the following is NOT mentioned according to the passage?',
                                   'o': ['Adults are advised to exercise moderately for 30 minutes every day.',
                                         'Adequate sleep can help enhance memory.',
                                         'People should drink more than two litres of water every day.',
                                         'Visiting the doctor regularly for health check-ups.']}]},
                       {'id': 'g6',
                        'instr': 'Mark the letter A, B, C, or D on your answer sheet to indicate the correct arrangement of the sentences to make a '
                                 'meaningful paragraph/letter in each of the following questions.',
                        'items': [{'id': 'g6.30',
                                   't': 'mcq',
                                   'q': 'a. Lan: I usually go jogging every morning to keep fit.<br>b. Nam: That’s great! I also try to eat more '
                                        'vegetables and drink enough water.<br>c. Nam: How do you stay healthy every day?',
                                   'o': ['a – b – c', 'c – a – b', 'b – c – a', 'a – c – b']},
                                  {'id': 'g6.31',
                                   't': 'mcq',
                                   'q': 'a. I’ve just joined a new health club in our town.<br>b. Hi Anna!<br>c. I think it would be fun and healthy '
                                        'if you joined with me.<br>d. Let’s go together this weekend!<br>e. They have great fitness classes and a '
                                        'friendly environment.',
                                   'o': ['b – c – a – e – d', 'b – a – c – e – d', 'b – a – e – c – d', 'a – b – c – e – d']},
                                  {'id': 'g6.32',
                                   't': 'mcq',
                                   'q': 'a. First, technology makes transportation faster and easier, so people can save time.<br>b. Finally, '
                                        'citizens can access better healthcare, education, and safety services through digital platforms.<br>c. '
                                        'Living in a smart city brings many benefits to people’s daily lives.<br>d. In conclusion, smart cities '
                                        'bring comfort, efficiency, and a higher quality of life.<br>e. Moreover, smart systems help reduce '
                                        'pollution and keep the environment cleaner.',
                                   'o': ['c – a – e – b – d', 'a – e – c – b – d', 'c – a – b – e – d', 'a – e – b – c – d']}]},
                       {'id': 'g7',
                        'instr': 'Supply the correct form or tense of the given verb in each of the following questions to make meaningful '
                                 'sentences. (1.0 pt)',
                        'items': [{'id': 'g7.33',
                                   't': 'fill',
                                   'q': 'Students in smart cities are expected to be more {_} in using technology for learning.',
                                   'hint': 'SKILL'},
                                  {'id': 'g7.34',
                                   't': 'fill',
                                   'q': 'The {_} communication between family members can lead to more understanding and happiness.',
                                   'hint': 'EFFECT'},
                                  {'id': 'g7.35',
                                   't': 'fill',
                                   'q': 'Since the project started, our group {_} many ideas to make the city greener.',
                                   'hint': 'PROPOSE'},
                                  {'id': 'g7.36',
                                   't': 'fill',
                                   'q': 'There are often heated {_} between friends about which major to choose at university.',
                                   'hint': 'ARGUE'},
                                  {'id': 'g7.37',
                                   't': 'fill',
                                   'q': 'My teacher advised me to {_} my goals before making any important decision.',
                                   'hint': 'CONSIDER'}]},
                       {'id': 'g8',
                        'instr': 'Finish each of the following sentences in such a way that it means the same as the original sentence printed '
                                 'before it.',
                        'items': [{'id': 'g8.38',
                                   't': 'fill',
                                   'long': True,
                                   'q': '<b>It is important for young people to communicate with their parents to bridge the generation gap.</b> '
                                        '<i>(use a modal verb)</i><br>→ {_}'},
                                  {'id': 'g8.39',
                                   't': 'fill',
                                   'long': True,
                                   'q': "<b>I haven't visited my grandparents for two weeks.</b> <i>(use 'since')</i><br>→ {_}"},
                                  {'id': 'g8.40',
                                   't': 'fill',
                                   'long': True,
                                   'q': '<b>We started learning about smart cities last month, and we are still studying the topic.</b> <i>(use '
                                        "'present perfect tense')</i><br>→ {_}"},
                                  {'id': 'g8.41',
                                   't': 'fill',
                                   'long': True,
                                   'q': '<b>We are not allowed to use our mobile phones during the movie screening.</b> <i>(use a modal '
                                        'verb)</i><br>→ {_}'}]}]}]}
