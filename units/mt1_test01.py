# -*- coding: utf-8 -*-
"""Test 1 – Mid-term 1 (Tiếng Anh 11 Global Success): Đề kiểm tra giữa HK1 2025-2026, đề 1 (40 câu, không có phần nghe).
Sinh bởi tools/gen_mt1_bode.py từ src/mt1/bode.txt."""

SET = {'id': 'lop11-mt1-test01',
 'title': 'Test 1 – Mid-term 1',
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
                        'passage': '<p><b>Climate-Positive Cities: Where Buildings Clean the Air You Breathe</b></p><p>• Breathe deeply in our '
                                   '<b>(1) ______</b>. Powerful green technology transforms ordinary buildings into living air purifiers.</p><p>• '
                                   'Families <b>(2) ______</b> in climate-positive neighborhoods enjoy 40% cleaner air. Our architects explain '
                                   'benefits <b>(3) ______</b> communities.</p><p>• Our buildings are state-of-the<b>-(4) ______</b> in '
                                   'environmental engineering. Children enjoy <b>(5) ______</b> outside without worrying about air quality.</p><p>• '
                                   'Imagine waking up to birdsong instead of traffic noise. Picture your children running through green spaces with '
                                   "clean lungs. Our climate-positive buildings don't just reduce pollution—they <b>(6) ______</b> remove "
                                   'it!</p><p>• Visit www.cleanercities.com today to discover how your city can become a paradise where buildings '
                                   'help you breathe better.</p>',
                        'items': [{'id': 'g1.1',
                                   't': 'mcq',
                                   'q': 'Blank (1)',
                                   'o': ['green revolutionary cities',
                                         'cities revolutionary green',
                                         'revolutionary green cities',
                                         'revolutionary cities green']},
                                  {'id': 'g1.2', 't': 'mcq', 'q': 'Blank (2)', 'o': ['which lived', 'lived', 'living', 'was lived']},
                                  {'id': 'g1.3', 't': 'mcq', 'q': 'Blank (3)', 'o': ['about', 'to', 'for', 'on']},
                                  {'id': 'g1.4', 't': 'mcq', 'q': 'Blank (4)', 'o': ['art', 'tech', 'line', 'edge']},
                                  {'id': 'g1.5', 't': 'mcq', 'q': 'Blank (5)', 'o': ['to play', 'to playing', 'play', 'playing']},
                                  {'id': 'g1.6', 't': 'mcq', 'q': 'Blank (6)', 'o': ['activity', 'actively', 'activeness', 'active']}]},
                       {'id': 'g2',
                        'instr': 'Read the following leaflet and mark the letter A, B, C or D on your answer sheet to indicate the option that best '
                                 'fits each of the numbered blanks from 7 to 12.',
                        'passage': '<p><b>The Only Tech That Grandma AND Her Grandkids Fight Over</b></p><p><b>The TabletPro X3: Family Fun for All '
                                   'Ages!</b></p><p>• We need <b>(7) ______</b> tablet for our excited family members tomorrow. Grandma can <b>(8) '
                                   '______</b> our simple, colorful design right away without any help.</p><p>• The beautiful <b>(9) ______</b> is '
                                   'large and clear for everyone in the house. You can enjoy exciting games <b>(10) ______</b> your advanced age or '
                                   'technical skills.</p><p>• The powerful <b>(11) ______</b> battery lasts all day without charging even with heavy '
                                   'use. <b>(12) ______</b> of educational apps for both learning and entertainment are available now.</p><p>• '
                                   '<b>Why families love our TabletPro X3:</b></p><p>• Easy to use for ages 5 to 65</p><p>• Big, bright '
                                   'screen</p><p>• Long battery life</p><p>• Games, videos, and books all in one place</p><p>• Special family '
                                   'sharing features</p><p>• Call us today at 123-456-7890 or visit www.tabletpro.com to order yours!</p><p>• '
                                   '<b>Special discount:</b> Buy one for Grandma, get 20% off a second for the grandkids!</p>',
                        'items': [{'id': 'g2.7', 't': 'mcq', 'q': 'Blank (7)', 'o': ['the others', 'another', 'other', 'others']},
                                  {'id': 'g2.8', 't': 'mcq', 'q': 'Blank (8)', 'o': ['pick up', 'work out', 'take in', 'figure out']},
                                  {'id': 'g2.9', 't': 'mcq', 'q': 'Blank (9)', 'o': ['touchscreen', 'display', 'monitor', 'interface']},
                                  {'id': 'g2.10',
                                   't': 'mcq',
                                   'q': 'Blank (10)',
                                   'o': ['as compared with', 'in addition to', 'in spite of', 'with regard to']},
                                  {'id': 'g2.11', 't': 'mcq', 'q': 'Blank (11)', 'o': ['alkaline', 'nickel', 'zinc', 'lithium']},
                                  {'id': 'g2.12', 't': 'mcq', 'q': 'Blank (12)', 'o': ['Lots', 'Dozens', 'Hundreds', 'Plenty']}]},
                       {'id': 'g3',
                        'instr': 'Mark the letter A, B, C or D on your answer sheet to indicate the best arrangement of utterances or sentences to '
                                 'make a meaningful exchange or text in each of the following questions from 13 to 17.',
                        'items': [{'id': 'g3.13',
                                   't': 'mcq',
                                   'q': "a. Child: Wow! We both got ice cream, but you picked a different flavor. Let's taste each other's!<br>b. "
                                        'Child: Grandma, can I have chocolate ice cream with sprinkles, please?<br>c. Grandma: Of course, sweetie! '
                                        'And I will try the strawberry one today.',
                                   'o': ['b-c-a', 'a-b-c', 'c-b-a', 'a-c-b']},
                                  {'id': 'g3.14',
                                   't': 'mcq',
                                   'q': 'a. Miguel: I can help you water them, and we can watch them grow together.<br>b. Lily: I planted some seeds '
                                        'yesterday, and they need water every day.<br>c. Miguel: My grandmother grows tomatoes at home, and she says '
                                        'plants are like friends.<br>d. Lily: The teacher said they will become beautiful flowers, but we must be '
                                        "patient.<br>e. Lily: I'm excited to see the first leaves appear, and I will draw pictures of our garden in "
                                        'my notebook!',
                                   'o': ['a-c-b-d-e', 'b-a-e-c-d', 'b-a-d-c-e', 'c-d-b-e-a']},
                                  {'id': 'g3.15',
                                   't': 'mcq',
                                   'q': 'Dear Sam,<br>a. Although some people think gardening is difficult, I find it very relaxing.<br>b. When we '
                                        "grow food in our neighborhood, we don't need trucks to bring it from far away.<br>c. I am writing because "
                                        'our community garden is growing so many vegetables that we can eat fresh food every day.<br>d. If you visit '
                                        'next weekend, we can pick vegetables together for a delicious lunch since you mentioned wanting to learn '
                                        'about gardening.<br>e. My family enjoys the tomatoes that we planted together in spring, while my mother '
                                        'loves the fresh herbs.<br>Your friend,<br>LK',
                                   'o': ['b-e-c-a-d', 'c-b-e-a-d', 'a-d-e-c-b', 'e-c-a-b-d']},
                                  {'id': 'g3.16',
                                   't': 'mcq',
                                   'q': 'a. Many children learn about important ideas when they listen to songs that talk about friendship and '
                                        'kindness, which helps them understand how to be good people.<br>b. When John Lennon wrote "Imagine," he '
                                        'wanted us to dream of a world where everyone is equal, which inspired many young people.<br>c. Although '
                                        'some musicians only sing about love or fun, artists like Nina Simone used their beautiful voices to speak '
                                        'about problems in society that needed to change.<br>d. Bob Marley sang songs about peace that made people '
                                        'think about how we can live together without fighting.<br>e. Michael Jackson created music videos that '
                                        'showed people from different backgrounds dancing together, while his songs talked about making the world '
                                        'better.',
                                   'o': ['d-b-e-c-a', 'b-c-e-d-a', 'c-d-e-b-a', 'e-b-c-d-a']},
                                  {'id': 'g3.17',
                                   't': 'mcq',
                                   'q': 'a. When architects design new homes, they use traditional patterns from Africa and Asia that make the '
                                        'houses both beautiful and comfortable.<br>b. Modern buildings in 2025 mix ideas from many countries, which '
                                        'makes cities look interesting and colorful.<br>c. Although some people prefer simple buildings, many '
                                        'families enjoy living in homes that have special spaces where they can cook food from their home '
                                        'countries.<br>d. The most popular parks have small buildings where people can meet friends, which helps '
                                        "neighbors from different cultures learn about each other's traditions.<br>e. Schools and libraries now have "
                                        'big windows that let in natural light, while their roofs collect rainwater for plants and trees around '
                                        'them.',
                                   'o': ['b-e-c-a-d', 'b-d-a-e-c', 'b-c-d-a-e', 'b-a-e-c-d']}]},
                       {'id': 'g4',
                        'instr': 'Read the following passage about Household Solutions and mark the letter A, B, C or D on your answer sheet to '
                                 'indicate the option that best fits each of the numbered blanks from 18 to 22.',
                        'passage': '<p>Water scarcity affects many regions around the world today. Families can make small changes at home to save '
                                   'this precious resource. If everyone participated in conservation efforts, millions of gallons of water would be '
                                   'saved each year. Installing low-flow showerheads and faucet aerators reduces water usage without affecting '
                                   'performance. These simple devices <b>(18) ______</b>. Collecting rainwater, which falls freely from the sky, '
                                   'provides an excellent alternative for garden irrigation. Rain barrels, <b>(19) ______</b>, are used to capture '
                                   'this valuable resource. The water that is collected can be used for plants, washing cars, or cleaning outdoor '
                                   'spaces. This practice not only conserves tap water but also reduces stormwater runoff.</p><p>Fixing leaky pipes '
                                   'is essential; <b>(20) ______</b>. A single dripping faucet wastes gallons daily; similarly, a running toilet can '
                                   'waste hundreds of gallons weekly. <b>(21) ______</b>. Children who learn conservation habits early will carry '
                                   'these practices into adulthood. Parents should teach their children to turn off faucets while brushing their '
                                   'teeth and to take shorter showers. Schools that incorporate water conservation into their curriculum help create '
                                   'a generation of environmentally conscious citizens. Homeowners invest in modern water recycling systems and save '
                                   'money through reduced monthly bills. Having installed these efficient systems, <b>(22) ______</b>. The '
                                   'technology for water recycling has improved dramatically in recent years, making these solutions more accessible '
                                   'to average families.</p>',
                        'items': [{'id': 'g4.18',
                                   't': 'mcq',
                                   'q': 'Blank (18)',
                                   'o': ['will reduce energy consumption and improve the quality of indoor air circulation',
                                         'which experts recommend for gardens and they help during seasonal drought periods',
                                         'can be purchased at most hardware stores and installed easily by homeowners',
                                         'having considered the environmental impact and choosing based on customer reviews']},
                                  {'id': 'g4.19',
                                   't': 'mcq',
                                   'q': 'Blank (19)',
                                   'o': ['had collected rainwater since the drought began',
                                         'design prevents mosquitoes from breeding inside',
                                         'which many households now connect to downspouts',
                                         'where people will store excess water for gardens']},
                                  {'id': 'g4.20',
                                   't': 'mcq',
                                   'q': 'Blank (20)',
                                   'o': ['however, planting drought-resistant flowers can beautify outdoor spaces',
                                         'moreover, checking toilets for silent leaks can prevent significant waste',
                                         'therefore, installing solar panels can reduce monthly electricity bills',
                                         'meanwhile, recycling plastic containers can decrease landfill pollution']},
                                  {'id': 'g4.21',
                                   't': 'mcq',
                                   'q': 'Blank (21)',
                                   'o': ['Regular maintenance prevents these problems and saves money on water bills',
                                         'Proper insulation reduces energy loss and improves comfort during winter',
                                         'Digital monitoring tracks electricity usage and alerts users to power surges',
                                         'Organic gardening eliminates chemical runoff and produces healthier food']},
                                  {'id': 'g4.22',
                                   't': 'mcq',
                                   'q': 'Blank (22)',
                                   'o': ['recycling materials found in older buildings during renovation projects',
                                         'having planted native trees increasing biodiversity around properties',
                                         'designed to maximize natural lighting reducing electricity consumption',
                                         'homeowners also contribute to environmental protection in their communities']}]},
                       {'id': 'g5',
                        'instr': 'Read the following passage about The Evolutionary Path Across Generations and mark the letter A, B, C or D on your '
                                 'answer sheet to indicate the best answer to each of the following questions from 23 to 30.',
                        'passage': '<p><small>[Paragraph 1]</small> The relationship between humans and technology has transformed over the past '
                                   'century. In the early 1900s, many viewed new inventions with <b><u>suspicion</u></b>. The introduction of '
                                   'telephones, radios, and televisions met resistance from older generations who preferred traditional methods. '
                                   'This technophobia was evident among rural communities where access to new devices was limited. Despite '
                                   'hesitation, these technologies became accepted as their benefits became apparent.</p><p><small>[Paragraph '
                                   '2]</small> By the 1980s, personal computers entered homes and workplaces, marking a shift in technological '
                                   'adoption. Children born during this period grew up alongside evolving technology, making them more adaptable. '
                                   'Unlike <b>their</b> grandparents, these individuals embraced technology with enthusiasm. Schools started '
                                   'incorporating computer literacy, recognizing its importance. This generation served as a bridge between the '
                                   "tech-resistant older population and tech-native youth.</p><p><small>[Paragraph 3]</small> Today's youth, called "
                                   '"digital natives," have never known a world without smartphones and instant information. Their relationship with '
                                   'technology differs from previous generations as they integrate digital tools into their lives. Studies show '
                                   'children as young as two can navigate touchscreens with <b><u>proficiency</u></b>. However, this integration has '
                                   'raised concerns about dependency. Parents now face the challenge of teaching responsible technology use while '
                                   'acknowledging its essential role.</p><p><small>[Paragraph 4]</small> <b><u>Looking ahead, the evolution from '
                                   'technophobia to tech-dependence raises questions about adaptation.</u></b> As AI and virtual reality become '
                                   'sophisticated, our relationship with technology will transform. Some experts predict the distinction between '
                                   'digital and physical experiences will blur. While older generations may struggle with technological changes, '
                                   'younger people view these as natural progression. This generational difference highlights how our relationship '
                                   'with technology reflects our willingness to adapt.</p>',
                        'items': [{'id': 'g5.23',
                                   't': 'mcq',
                                   'q': 'According to the passage, all of the following were met with resistance in the early 1900s EXCEPT?',
                                   'o': ['telephones', 'automobiles', 'radios', 'televisions']},
                                  {'id': 'g5.24',
                                   't': 'mcq',
                                   'q': 'The word “<b><u>suspicion</u></b>” in paragraph 1 is OPPOSITE in meaning to _________.',
                                   'o': ['concern', 'awareness', 'trust', 'observation']},
                                  {'id': 'g5.25',
                                   't': 'mcq',
                                   'q': 'The word “<b>their</b>” in paragraph 2 refers to _________.',
                                   'o': ['Children born during this period', 'Personal computers', 'Homes and workplaces', 'Technologies']},
                                  {'id': 'g5.26',
                                   't': 'mcq',
                                   'q': 'The word “<b><u>proficiency</u></b>” in paragraph 3 could be best replaced by _________.',
                                   'o': ['interest', 'skill', 'frequency', 'difficulty']},
                                  {'id': 'g5.27',
                                   't': 'mcq',
                                   'q': 'Which of the following best paraphrases the underlined sentence in paragraph 4?',
                                   'o': ['Future shifts in how we use technology may bring about new health concerns for society.',
                                         'The next generation will likely develop better methods to address technology-related fears.',
                                         'Advanced innovations may eventually eliminate the gap between those who fear and use technology.',
                                         'Moving forward, our changing relationship with technology poses questions about human adaptability.']},
                                  {'id': 'g5.28',
                                   't': 'mcq',
                                   'q': 'Which of the following is TRUE according to the passage?',
                                   'o': ['Rural communities completely rejected all technological advancements throughout the twentieth century.',
                                         'Schools initially discouraged computer literacy until digital devices became widespread in most homes.',
                                         'Experts universally agree that technology dependency poses significant threats to social development.',
                                         'Children born in the 1980s served as a bridge between tech-resistant older people and tech-native youth.']},
                                  {'id': 'g5.29',
                                   't': 'mcq',
                                   'q': 'In which paragraph does the writer describe early attitudes toward technological innovations?',
                                   'o': ['Paragraph 1', 'Paragraph 2', 'Paragraph 3', 'Paragraph 4']},
                                  {'id': 'g5.30',
                                   't': 'mcq',
                                   'q': 'In which paragraph does the writer describe which generation is described as a "bridge" between '
                                        'tech-resistant and tech-native populations?',
                                   'o': ['Paragraph 3', 'Paragraph 1', 'Paragraph 2', 'Paragraph 4']}]},
                       {'id': 'g6',
                        'instr': 'Read the following passage about the Integrating Nature into Concrete Jungles and mark the letter A, B, C or D on '
                                 'your answer sheet to indicate the best answer to each of the following questions from 31 to 40.',
                        'passage': '<p><small>[Paragraph 1]</small> Urban forests are green spaces that bring nature back to concrete environments. '
                                   'As cities expand, striking a balance between development and nature becomes essential. For decades, urban '
                                   "developers <b><u>couldn't see the forest for the trees</u></b>, focusing on individual buildings while missing "
                                   'the bigger picture of environmental health. Now many city planners are incorporating more greenery in their '
                                   'designs. Urban forests include neighborhood parks, tree-lined streets, community gardens, or larger protected '
                                   'areas within city limits. These spaces serve as islands of nature amid buildings and roads. Without <b>them</b>, '
                                   'cities would be merely concrete and steel—materials that trap heat and worsen the urban heat island '
                                   'effect.</p><p><small>[Paragraph 2]</small> Urban forests offer significant benefits to city dwellers. <b>[I]</b> '
                                   'They improve air quality by filtering pollutants and producing oxygen while capturing carbon dioxide that '
                                   'contributes to climate change. <b>[II]</b> These green spaces provide important health benefits, as studies show '
                                   'they reduce stress and improve mental wellbeing. <b>[III]</b> Additionally, these areas support biodiversity by '
                                   'providing habitat for birds, insects, and small animals while creating community gathering spaces where social '
                                   'bonds flourish. <b>[IV]</b></p><p><small>[Paragraph 3]</small> Creating urban forests faces numerous challenges '
                                   'despite their advantages. Space limitations plague densely populated cities where land is expensive and '
                                   'development competition is fierce. Green projects often receive less funding <b><u>priority</u></b> than '
                                   'infrastructure. Ongoing maintenance presents concerns since plants require regular care in harsh urban '
                                   'conditions. Climate change adds pressure through extreme weather events that threaten plant survival. Water '
                                   'management becomes critical in regions experiencing drought or irregular rainfall. However, solutions like green '
                                   'roofs and pocket parks help integrate nature into limited spaces.</p><p><small>[Paragraph 4]</small> <b><u>The '
                                   'future of urban forests lies in revolutionary approaches to city greening.</u></b> Biophilic architecture '
                                   'integrates living systems directly into buildings, with structures designed to host diverse ecosystems. Smart '
                                   'forests equipped with sensors monitor health, pollution levels, and biodiversity in real-time. Edible urban '
                                   'forests produce food while improving ecology, transforming cities into productive landscapes. Climate-resilient '
                                   'forest systems using predictive modeling select species that will thrive despite changing conditions. Floating '
                                   'forests on urban waterways create new habitats while filtering water.</p>',
                        'items': [{'id': 'g6.31',
                                   't': 'mcq',
                                   'q': "The phrase “<b><u>couldn't see the forest for the trees</u></b>” in paragraph 1 could be best replaced by "
                                        '_________.',
                                   'o': ['looked down on', 'missed out on', 'gave up on', 'looked up to']},
                                  {'id': 'g6.32',
                                   't': 'mcq',
                                   'q': 'The word “<b>them</b>” in paragraph 1 refers to _________.',
                                   'o': ['Urban forests', 'Buildings and roads', 'Islands of nature', 'Concrete and steel']},
                                  {'id': 'g6.33',
                                   't': 'mcq',
                                   'q': 'Where in paragraph 2 does the following sentence best fit?<br><b>People living near parks tend to be more '
                                        'physically active, preventing various health problems.</b>',
                                   'o': ['[I]', '[II]', '[III]', '[IV]']},
                                  {'id': 'g6.34',
                                   't': 'mcq',
                                   'q': 'According to the passage, all of the following are benefits of urban forests EXCEPT?',
                                   'o': ['They improve air quality by filtering pollutants',
                                         'They provide habitats for wildlife and support biodiversity',
                                         'They create community gathering spaces where social bonds flourish',
                                         'They increase property values in surrounding neighborhoods']},
                                  {'id': 'g6.35',
                                   't': 'mcq',
                                   'q': 'Which of the following best summarises paragraph 3?',
                                   'o': ['Urban planners have identified suitable designs for overcoming space constraints while neglecting '
                                         'maintenance needs, funding limitations, and climate concerns that challenge the implementation of urban '
                                         'forests in modern city environments.',
                                         'Despite their ecological benefits, urban forests face implementation challenges including space '
                                         'constraints, funding priorities, maintenance requirements, climate threats, and water management issues, '
                                         'though solutions like green roofs exist.',
                                         'The primary obstacle to urban forest development is inadequate funding allocation, while secondary '
                                         'concerns include design limitations, public opposition, temperature fluctuations, and technological '
                                         'barriers in monitoring ecosystem health.',
                                         'Research demonstrates that urban forests struggle to survive in artificial environments due to '
                                         'insufficient planning, chemical pollutants, incompatible architectural designs, and resident misuse '
                                         'despite educational community campaigns.']},
                                  {'id': 'g6.36',
                                   't': 'mcq',
                                   'q': 'The word “<b><u>priority</u></b>” in paragraph 3 is OPPOSITE in meaning to _________.',
                                   'o': ['afterthought', 'preference', 'significance', 'urgency']},
                                  {'id': 'g6.37',
                                   't': 'mcq',
                                   'q': 'Which of the following best paraphrases the underlined sentence in paragraph 4?',
                                   'o': ['Urban forests will gradually evolve through conventional environmental planning methods that cities have '
                                         'traditionally used for landscape development projects.',
                                         'The preservation of existing green spaces requires immediate action rather than waiting for technological '
                                         'advances in urban landscape architecture.',
                                         'Innovative techniques for introducing vegetation will transform how urban forests develop and function '
                                         'within metropolitan environments in coming years.',
                                         'City planners must balance traditional conservation strategies with experimental designs to maintain '
                                         'current forest areas against urban encroachment.']},
                                  {'id': 'g6.38',
                                   't': 'mcq',
                                   'q': 'Which of the following is TRUE according to the passage?',
                                   'o': ['Urban developers have historically prioritized environmental health considerations over individual '
                                         'building projects when planning city layouts and infrastructural development.',
                                         'Smart technology integrated into urban green spaces enables real-time monitoring of ecosystem health '
                                         'factors including pollution levels and biodiversity measurements.',
                                         'Urban forests require minimal maintenance as the plant species selected for these environments have '
                                         'naturally evolved to thrive in harsh conditions without human intervention.',
                                         'Floating forests represent an outdated approach to urban greening that has been largely abandoned due to '
                                         'water contamination concerns and navigational difficulties.']},
                                  {'id': 'g6.39',
                                   't': 'mcq',
                                   'q': 'Which of the following can be inferred from the passage?',
                                   'o': ['Most city residents actively oppose urban forest initiatives due to concerns about increased insect '
                                         'populations, maintenance costs, and the reduction of available parking spaces.',
                                         'Traditional parks with minimal technology integration will remain the preferred approach to urban greening '
                                         'because they require less specialized maintenance than newer biophilic architectural designs.',
                                         'Despite documented benefits, urban forests will likely decrease in coming decades as economic pressures '
                                         'force cities to prioritize revenue-generating developments over environmental considerations.',
                                         'As technology advances and climate concerns intensify, urban planners will increasingly integrate natural '
                                         'elements with built environments rather than treating them as separate domains.']},
                                  {'id': 'g6.40',
                                   't': 'mcq',
                                   'q': 'Which of the following best summarises the passage?',
                                   'o': ['Urban forests represent essential green spaces that benefit city environments and residents in multiple '
                                         'ways, though their implementation faces challenges that innovative approaches like biophilic design and '
                                         'smart technology aim to overcome.',
                                         'Urban forests have historically been neglected by city planners but offer numerous health benefits to '
                                         'residents despite requiring extensive maintenance that most municipalities cannot financially sustain '
                                         'without significant federal infrastructure funding.',
                                         'The rapid expansion of concrete urban environments has created urgent ecological crises that traditional '
                                         'conservation methods cannot address, necessitating revolutionary architectural innovations before '
                                         'irreversible environmental damage occurs.',
                                         'Modern cities suffer from excessive pollution and social disconnection that urban forests might '
                                         'theoretically alleviate, but practical implementation barriers make sustainable green space development '
                                         'largely unrealistic for most metropolitan areas.']}]}]}]}
