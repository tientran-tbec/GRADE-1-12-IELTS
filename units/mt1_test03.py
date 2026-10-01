# -*- coding: utf-8 -*-
"""Test 3 – Mid-term 1 (Tiếng Anh 11 Global Success): Đề kiểm tra giữa HK1 2025-2026, đề 3 (40 câu, không có phần nghe).
Sinh bởi tools/gen_mt1_bode.py từ src/mt1/bode.txt."""

SET = {'id': 'lop11-mt1-test03',
 'title': 'Test 3 – Mid-term 1',
 'grade': 11,
 'unit': 'MidTerm1',
 'theory': '',
 'pages': [{'id': 'kiem-tra',
            'title': 'Làm bài',
            'mode': 'test',
            'minutes': 45,
            'groups': [{'id': 'g1',
                        'instr': 'Read the following advertisement and mark the letter A, B, C or D on your answer sheet to indicate the option that '
                                 'best fits each of the numbered blanks from 1 to 6.',
                        'passage': '<p><b>The Art of Persistence: Journeys of Creating Admirable Legacies</b></p><p>• Genuine persistence '
                                   'consistently transforms everyday challenges into <b>(1) ______</b> opportunities for personal growth. The highly '
                                   'dedicated <b>(2) ______</b> inspire us all tremendously.</p><p>• Young people <b>(3) ______</b> to succeed '
                                   'always achieve their ambitious dreams. Our comprehensive program gives motivated students access <b>(4) '
                                   '______</b> experienced mentors worldwide.</p><p>• You need to <b>(5) ______</b> your chin up when facing '
                                   'obstacles on your path to success. We strongly encourage learning diligently from past failures <b>(6) '
                                   '______</b> exceptional resilience over time.</p><p>• Join our workshop today and discover how persistence can '
                                   'help you create your own admirable legacy!</p>',
                        'items': [{'id': 'g1.1', 't': 'mcq', 'q': 'Blank (1)', 'o': ['value', 'valuables', 'valuable', 'valuably']},
                                  {'id': 'g1.2',
                                   't': 'mcq',
                                   'q': 'Blank (2)',
                                   'o': ['international leaders business',
                                         'business leaders international',
                                         'leaders business international',
                                         'international business leaders']},
                                  {'id': 'g1.3',
                                   't': 'mcq',
                                   'q': 'Blank (3)',
                                   'o': ['determining', 'was determined', 'determined', 'which determined']},
                                  {'id': 'g1.4', 't': 'mcq', 'q': 'Blank (4)', 'o': ['to', 'about', 'on', 'with']},
                                  {'id': 'g1.5', 't': 'mcq', 'q': 'Blank (5)', 'o': ['bring', 'keep', 'make', 'take']},
                                  {'id': 'g1.6', 't': 'mcq', 'q': 'Blank (6)', 'o': ['building', 'to build', 'to building', 'build']}]},
                       {'id': 'g2',
                        'instr': 'Read the following leaflet and mark the letter A, B, C or D on your answer sheet to indicate the option that best '
                                 'fits each of the numbered blanks from 7 to 12.',
                        'passage': '<p><b>Reuniting Families Across The Digital Divide</b></p><p>• While some families stay connected online, <b>(7) '
                                   '______</b> families need our help with technology. Our program helps elderly people <b>(8) ______</b> video '
                                   'calls with their loved ones.</p><p>• The innovation of our <b>(9) ______</b> brings families closer despite '
                                   'distance. <b>(10) ______</b> technology barriers, we connect generations through simple tools.</p><p>• The '
                                   'accessibility of our <b>(11) ______</b> makes technology easy for everyone. A <b>(12) ______</b> of our '
                                   'volunteers dedicate time to teaching basic computer skills.</p><p>• Join our free workshops every Saturday! '
                                   'Learn how to stay connected with your family members no matter where they are.</p><p>• Contact us at '
                                   '123-456-7890 or visit www.familyconnect.org.</p>',
                        'items': [{'id': 'g2.7', 't': 'mcq', 'q': 'Blank (7)', 'o': ['other', 'another', 'others', 'the others']},
                                  {'id': 'g2.8', 't': 'mcq', 'q': 'Blank (8)', 'o': ['bring about', 'set up', 'look into', 'carry out']},
                                  {'id': 'g2.9', 't': 'mcq', 'q': 'Blank (9)', 'o': ['campaign', 'venture', 'project', 'program']},
                                  {'id': 'g2.10',
                                   't': 'mcq',
                                   'q': 'Blank (10)',
                                   'o': ['In advance of', 'On account of', 'With regard to', 'In spite of']},
                                  {'id': 'g2.11', 't': 'mcq', 'q': 'Blank (11)', 'o': ['platform', 'interface', 'services', 'resources']},
                                  {'id': 'g2.12', 't': 'mcq', 'q': 'Blank (12)', 'o': ['lot', 'few', 'majority', 'number']}]},
                       {'id': 'g3',
                        'instr': 'Mark the letter A, B, C or D on your answer sheet to indicate the best arrangement of utterances or sentences to '
                                 'make a meaningful exchange or text in each of the following questions from 13 to 17.',
                        'items': [{'id': 'g3.13',
                                   't': 'mcq',
                                   'q': "a. Tom: That sounds interesting! Can I help even if I'm not very good with technology?<br>b. Sarah: Hi Tom! "
                                        'Do you want to join our digital help group? We teach older people how to use computers.<br>c. Sarah: Of '
                                        'course! Some volunteers teach, others make coffee, and you can just talk to people who feel lonely. '
                                        'Everyone has something to offer!',
                                   'o': ['b-c-a', 'a-b-c', 'b-a-c', 'c-b-a']},
                                  {'id': 'g3.14',
                                   't': 'mcq',
                                   'q': 'a. Emma: Great plan! We can also ask people what they want to learn. Some might want to use email or find '
                                        "information online.<br>b. Emma: Maybe we could teach them how to use video calls first? It's simple but "
                                        "very useful.<br>c. Carlos: That's a wonderful idea! My grandmother always asks me to help with her "
                                        "phone.<br>d. Emma: Hi Carlos! I'm thinking about starting a computer class for older people in our "
                                        'community center.<br>e. Carlos: Yes, and we should make big handouts with clear pictures for each step.',
                                   'o': ['a-b-e-c-d', 'd-a-b-e-c', 'd-c-b-e-a', 'e-b-d-c-a']},
                                  {'id': 'g3.15',
                                   't': 'mcq',
                                   'q': 'Dear Sarah,<br>a. If more buildings had places where people could gather, I believe fewer would feel '
                                        'isolated in cities.<br>b. Although cities have many people, they often feel lonely because neighbors rarely '
                                        'talk to each other.<br>c. I saw your project about buildings that help people meet, which reminded me of '
                                        'our new community garden.<br>d. Would you like to visit our garden next Saturday, even though it is small, '
                                        'to see how it brings people together?<br>e. When our building added shared spaces last month, I finally met '
                                        'the kind family who lives next door.<br>Your friend,<br>LK',
                                   'o': ['c-b-e-a-d', 'b-d-e-c-a', 'a-e-c-b-d', 'e-a-b-c-d']},
                                  {'id': 'g3.16',
                                   't': 'mcq',
                                   'q': 'a. While smart homes cost money to build, they save money because people do not need to move to expensive '
                                        'care homes, which allows them to enjoy their community longer.<br>b. When someone cannot walk easily, doors '
                                        'can open automatically and lights turn on by themselves, which means fewer accidents happen at night.<br>c. '
                                        'Although technology seems complicated, new smart homes have simple buttons or voice controls that work when '
                                        'you speak to them naturally.<br>d. Smart homes help older people stay in their houses longer, which makes '
                                        'them happier and more independent.<br>e. Many older people feel lonely, but these homes can help them talk '
                                        'to family through screens, which keeps them connected even when living alone.',
                                   'o': ['b-e-d-c-a', 'd-b-c-e-a', 'c-b-e-d-a', 'e-b-c-d-a']},
                                  {'id': 'g3.17',
                                   't': 'mcq',
                                   'q': 'a. Middle-aged people sometimes feel caught between these views because they remember the past but also '
                                        'understand new ideas, which gives them balance.<br>b. When young people see new technology and social '
                                        'changes, they feel excited about possibilities that did not exist before, which creates hope.<br>c. When '
                                        'generations listen to each other with respect, they can learn from different viewpoints, which helps '
                                        'everyone see both progress and problems more clearly.<br>d. Although both generations live in the same '
                                        'world, they look at it through different experiences, which explains their disagreement about '
                                        'progress.<br>e. Older people often think society is getting worse, which makes them worry about the future '
                                        'their grandchildren will face.',
                                   'o': ['e-c-d-b-a', 'e-d-a-b-c', 'e-c-a-d-b', 'e-b-d-a-c']}]},
                       {'id': 'g4',
                        'instr': 'Read the following passage about Accessibility as the New Urban Standard and mark the letter A, B, C or D on your '
                                 'answer sheet to indicate the option that best fits each of the numbered blanks from 18 to 22.',
                        'passage': '<p>The 15-minute city concept, which was first developed by Professor Carlos Moreno, aims to improve urban life '
                                   'by ensuring all essential services are within a short walk or bike ride. This innovative approach <b>(18) '
                                   '______</b>. If more cities had implemented this design earlier, many environmental problems would have been '
                                   'prevented. Urban planners are now creating neighborhoods where schools, shops, healthcare facilities, and parks '
                                   'can be reached without using cars.</p><p>People <b>(19) ______</b>. The elderly and families with young children '
                                   'particularly benefit from this design because they often face mobility challenges. Having studied the benefits '
                                   'of walkable neighborhoods, researchers now recommend this model for all new urban developments. The buildings '
                                   'that are being constructed in these areas often include mixed-use designs, combining residential apartments with '
                                   'ground-floor businesses.</p><p><b>(20) ______</b>, having evolved before cars became common. Modern cities, '
                                   'growing rapidly and spreading outward, lost this human-centered scale. Urban designers, recognizing this '
                                   'problem, <b>(21) ______</b>. Paris has transformed dramatically, removing parking spaces and adding bike lanes '
                                   'throughout the city.</p><p>The 15-minute city not only improves physical health by encouraging walking but also '
                                   'enhances mental wellbeing by reducing commuting stress. <b>(22) ______</b>. Children gain independence earlier '
                                   'in safe, walkable neighborhoods where they can visit friends without needing rides from parents.</p>',
                        'items': [{'id': 'g4.18',
                                   't': 'mcq',
                                   'q': 'Blank (18)',
                                   'o': ['has been questioned by many economists around the world which believe it increases housing costs',
                                         'has been adopted by many cities around the world that want to reduce traffic and pollution',
                                         'has been implemented in wealthy neighborhoods around the world whose residents demand exclusive amenities',
                                         'has been promoted by car manufacturers around the world having invested in autonomous vehicle technology']},
                                  {'id': 'g4.19',
                                   't': 'mcq',
                                   'q': 'Blank (19)',
                                   'o': ['lived in 15-minute cities had reported lower satisfaction with their quality of life and weaker '
                                         'connections to their communities',
                                         'whose homes are in 15-minute cities have complained about rising property taxes and increasing commercial '
                                         'noise in their communities',
                                         'who live in 15-minute cities report higher satisfaction with their quality of life and stronger '
                                         'connections to their communities',
                                         'will live in 15-minute cities would report uncertain satisfaction with their quality of life and minimal '
                                         'connections to their communities']},
                                  {'id': 'g4.20',
                                   't': 'mcq',
                                   'q': 'Blank (20)',
                                   'o': ['Many traditional cities were accidentally designed as 15-minute communities',
                                         'Few modern suburbs were deliberately planned as car-dependent neighborhoods',
                                         'Most industrial zones were strategically located far from residential communities',
                                         'All suburban developments were economically designed for automobile convenience']},
                                  {'id': 'g4.21',
                                   't': 'mcq',
                                   'q': 'Blank (21)',
                                   'o': ['are opposing renovating historic districts while preserving car infrastructure',
                                         'having rejected modifying suburban layouts to accommodate public transit',
                                         'which prevented transforming commercial zones to encourage pedestrian activity',
                                         'have begun retrofitting existing neighborhoods to restore walkability']},
                                  {'id': 'g4.22',
                                   't': 'mcq',
                                   'q': 'Blank (22)',
                                   'o': ['Occasional gatherings of strangers at digital platforms weaken neighborhood bonds',
                                         'Mandatory assemblies of residents at municipal buildings burden local relationships',
                                         'Regular meetings of neighbors at local shops and parks strengthen communities',
                                         'Virtual interactions of households through community apps replace physical connections']}]},
                       {'id': 'g5',
                        'instr': 'Read the following passage about A New Generational Approach to Self-Definition and mark the letter A, B, C or D '
                                 'on your answer sheet to indicate the best answer to each of the following questions from 23 to 30.',
                        'passage': '<p><small>[Paragraph 1]</small> Identity fluidity refers to the idea that personal identity can change over '
                                   "time. Today's youth reject rigid categories that previous generations accepted without question or much thought. "
                                   'They view identity as a journey rather than a destination, exploring different aspects of <b>themselves</b> '
                                   'throughout life. This applies to gender, sexuality, careers, and cultural affiliations. Young people describe '
                                   'this flexibility as liberating, giving them freedom to evolve with new experiences and personal '
                                   'growth.</p><p><small>[Paragraph 2]</small> Social media has played a key role in this shift, providing platforms '
                                   'for identity experimentation and self-discovery. Online communities connect people with similar experiences, '
                                   '<b><u>validating</u></b> unusual feelings and alternative perspectives. These spaces allow youth to try '
                                   'different personas before adopting them in real life with greater confidence. Critics say constant reinvention '
                                   'causes confusion and lack of stability. However, supporters believe identity exploration is natural human '
                                   "development that past generations couldn't express openly due to societal constraints.</p><p><small>[Paragraph "
                                   '3]</small> Schools have been slow to adapt to fluid identities and changing student needs. Traditional education '
                                   'uses fixed categories that restrict students from expressing their <b><u>authentic</u></b> selves. Progressive '
                                   'educators now incorporate flexible frameworks acknowledging identity complexity in meaningful ways. They create '
                                   'judgment-free environments where students express themselves authentically throughout their educational journey. '
                                   'This requires teachers to reconsider assumptions about learning and student development. Effective education now '
                                   'helps young people develop critical thinking for their identity journeys and future '
                                   'challenges.</p><p><small>[Paragraph 4]</small> <b><u>Workplaces are changing due to identity fluidity and '
                                   'evolving social expectations.</u></b> Companies once expected employees to fit corporate cultures but now value '
                                   'diverse perspectives and unique contributions. Many businesses have revised policies for flexible identities '
                                   'across all organizational levels. This brings in wider viewpoints and talents previously overlooked by '
                                   'traditional hiring practices. Young workers seek employers respecting their whole selves, including aspects '
                                   'previously considered irrelevant to work performance.</p>',
                        'items': [{'id': 'g5.23',
                                   't': 'mcq',
                                   'q': 'According to the passage, which of the following is NOT mentioned as an area where identity fluidity '
                                        'applies?',
                                   'o': ['gender', 'sexuality', 'religion', 'career paths']},
                                  {'id': 'g5.24',
                                   't': 'mcq',
                                   'q': 'The word “<b>themselves</b>” in paragraph 1 refers to _________.',
                                   'o': ['previous generations', "today's youth", 'rigid categories', 'personal identities']},
                                  {'id': 'g5.25',
                                   't': 'mcq',
                                   'q': 'The word “<b><u>validating</u></b>” in paragraph 2 is OPPOSITE in meaning to _________.',
                                   'o': ['confirming', 'accepting', 'dismissing', 'recognizing']},
                                  {'id': 'g5.26',
                                   't': 'mcq',
                                   'q': 'The word “<b><u>authentic</u></b>” in paragraph 3 could be best replaced by _________.',
                                   'o': ['unusual', 'modern', 'complicated', 'genuine']},
                                  {'id': 'g5.27',
                                   't': 'mcq',
                                   'q': 'Which of the following best paraphrases the underlined sentence in paragraph 4?',
                                   'o': ['Business environments adapt as identity concepts shift and society develops new norms.',
                                         'Corporate policies resist modern identity trends while maintaining traditional structures.',
                                         'Employment settings focus on productivity rather than personal identity expressions.',
                                         'Office cultures prioritize technical skills over individual identity considerations.']},
                                  {'id': 'g5.28',
                                   't': 'mcq',
                                   'q': 'Which of the following is TRUE according to the passage?',
                                   'o': ['Traditional schools readily embrace fluid identities and adapt teaching approaches.',
                                         'Previous generations openly expressed identity fluidity without societal constraints.',
                                         'Critics believe identity exploration leads to confusion and instability in individuals.',
                                         'Companies prefer employees who separate personal identity from workplace roles.']},
                                  {'id': 'g5.29',
                                   't': 'mcq',
                                   'q': 'In which paragraph does the writer mention how social media facilitates identity exploration?',
                                   'o': ['Paragraph 1', 'Paragraph 2', 'Paragraph 3', 'Paragraph 4']},
                                  {'id': 'g5.30',
                                   't': 'mcq',
                                   'q': 'In which paragraph does the writer mention how educational systems respond to identity fluidity?',
                                   'o': ['Paragraph 3', 'Paragraph 2', 'Paragraph 1', 'Paragraph 4']}]},
                       {'id': 'g6',
                        'instr': 'Read the following passage about the Teaching Musical Expression Through Programming and mark the letter A, B, C '
                                 'or D on your answer sheet to indicate the best answer to each of the following questions from 31 to 40.',
                        'passage': '<p><small>[Paragraph 1]</small> Creative coding represents an innovative approach to music education that '
                                   'combines technology with artistic expression. By teaching students to write code that generates sounds and '
                                   'music, educators have <b><u>struck gold</u></b> and opened new pathways for creativity. This bridges the gap '
                                   'between STEM subjects and arts education, making both more accessible. Students learn fundamental programming '
                                   'concepts while developing musical understanding. The process begins with simple exercises like creating basic '
                                   'tones through code. As students gain confidence, <b>they</b> progress to more complex projects such as '
                                   'interactive sound installations. This approach engages students who might not otherwise show interest in '
                                   'traditional music education.</p><p><small>[Paragraph 2]</small> The benefits extend beyond musical skills '
                                   'development. <b>[I]</b> When faced with coding challenges, they must break down complex problems into manageable '
                                   'parts. <b>[II]</b> Additionally, creative coding helps students think outside the box when approaching musical '
                                   'composition. Rather than following conventional rules, they experiment with algorithmic patterns and '
                                   'randomization techniques. <b>[III]</b> As one student remarked, "Coding music helped me kill two birds with one '
                                   'stone – I improved my programming skills while discovering new ways to express myself." '
                                   '<b>[IV]</b></p><p><small>[Paragraph 3]</small> Educational institutions worldwide are increasingly incorporating '
                                   'creative coding into their curricula. Schools in Finland, South Korea, and Australia have developed programs '
                                   'that integrate coding and music. These initiatives often utilize <b><u>accessible</u></b> platforms such as '
                                   'Sonic Pi, EarSketch, or TidalCycles. Teachers report that these tools lower the barrier to entry for both '
                                   'subjects. Students who previously struggled with traditional music theory find the visual nature of coding more '
                                   'approachable. Conversely, students intimidated by programming discover that creating music provides an engaging '
                                   'context for learning code.</p><p><small>[Paragraph 4]</small> The future looks promising as technology continues '
                                   'to evolve. <b><u>New interfaces are making it easier for beginners to create sophisticated musical projects '
                                   'through code.</u></b> Virtual reality applications now allow students to visualize sound waves and interact with '
                                   'their code. Additionally, machine learning algorithms are being incorporated into educational platforms, '
                                   'enabling students to train computers to recognize patterns in music. These advancements suggest that creative '
                                   'coding will play an increasingly important role in music education while preserving the joy of musical '
                                   'creation.</p>',
                        'items': [{'id': 'g6.31',
                                   't': 'mcq',
                                   'q': 'The phrase “<b><u>struck gold</u></b>” in paragraph 1 could be best replaced by _________.',
                                   'o': ['came across', 'lucked out', 'figured out', 'hit upon']},
                                  {'id': 'g6.32',
                                   't': 'mcq',
                                   'q': 'Where in paragraph 2 does the following sentence best fit?<br><b>Students often show improved '
                                        'problem-solving abilities and computational thinking.</b>',
                                   'o': ['[I]', '[II]', '[III]', '[IV]']},
                                  {'id': 'g6.33',
                                   't': 'mcq',
                                   'q': 'The word “<b>they</b>” in paragraph 1 refers to _________.',
                                   'o': ['students', 'educators', 'pathways', 'projects']},
                                  {'id': 'g6.34',
                                   't': 'mcq',
                                   'q': 'According to the passage, which of the following is NOT mentioned as a platform used for creative coding?',
                                   'o': ['Sonic Pi', 'CodeHarmony', 'EarSketch', 'TidalCycles']},
                                  {'id': 'g6.35',
                                   't': 'mcq',
                                   'q': 'Which of the following best summarises paragraph 3?',
                                   'o': ['Educational platforms like Sonic Pi are making music theory more accessible to students who struggle with '
                                         'traditional approaches to learning music.',
                                         'Finland, South Korea, and Australia lead the world in developing innovative curricula that combine music '
                                         'education with computer programming skills.',
                                         'Schools globally are adopting creative coding programs that use specialized platforms to make both music '
                                         'and programming more approachable to students.',
                                         'Teachers report that visual coding environments help students overcome barriers to entry when learning '
                                         'either music theory or programming concepts.']},
                                  {'id': 'g6.36',
                                   't': 'mcq',
                                   'q': 'The word “<b><u>accessible</u></b>” in paragraph 3 is OPPOSITE in meaning to _________.',
                                   'o': ['prohibitive', 'available', 'attainable', 'convenient']},
                                  {'id': 'g6.37',
                                   't': 'mcq',
                                   'q': 'Which of the following is TRUE according to the passage?',
                                   'o': ['Creative coding primarily benefits students who already excel in traditional music theory and programming '
                                         'concepts.',
                                         'Students who struggle with traditional music theory often find the visual aspects of coding more '
                                         'accessible and engaging.',
                                         'Virtual reality and machine learning are currently being used by most schools that teach creative coding '
                                         'approaches.',
                                         'Educational programs in creative coding are limited to specialized schools in Finland, South Korea, and '
                                         'Australia exclusively.']},
                                  {'id': 'g6.38',
                                   't': 'mcq',
                                   'q': 'Which of the following best paraphrases the underlined sentence in paragraph 4?',
                                   'o': ['Modern software designs are enabling experienced coders to produce intricate musical arrangements with '
                                         'less technical knowledge.',
                                         'Innovative hardware systems are allowing music students to generate basic sound patterns without learning '
                                         'programming fundamentals.',
                                         'Advanced digital platforms are encouraging professional musicians to incorporate coding elements into '
                                         'their traditional compositions.',
                                         'Recent technological tools are simplifying the process for novices to develop complex music compositions '
                                         'using programming languages.']},
                                  {'id': 'g6.39',
                                   't': 'mcq',
                                   'q': 'Which of the following can be inferred from the passage?',
                                   'o': ['Traditional music education will eventually be replaced by creative coding approaches as technology '
                                         'becomes more sophisticated and widely available.',
                                         'Students who excel in creative coding will likely pursue careers that combine both musical composition and '
                                         'software development professionally.',
                                         'Creative coding provides educational benefits by engaging different types of learners through multiple '
                                         'pathways to understanding music and programming.',
                                         'Schools in countries other than Finland, South Korea, and Australia are resistant to implementing creative '
                                         'coding in their educational curricula.']},
                                  {'id': 'g6.40',
                                   't': 'mcq',
                                   'q': 'Which of the following best summarises the passage?',
                                   'o': ['Educational institutions in Finland, South Korea, and Australia are leading global efforts to integrate '
                                         'coding platforms into traditional music theory curricula.',
                                         'Virtual reality and machine learning technologies are transforming how students interact with musical '
                                         'concepts through sophisticated coding environments.',
                                         'Creative coding is revolutionizing music education by making both programming and musical composition more '
                                         'accessible to diverse learners through technological innovation.',
                                         'Students who struggle with conventional music education benefit from alternative approaches that emphasize '
                                         'visual programming and algorithmic composition.']}]}]}]}
