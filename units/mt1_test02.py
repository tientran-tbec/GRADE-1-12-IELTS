# -*- coding: utf-8 -*-
"""Test 2 – Mid-term 1 (Tiếng Anh 11 Global Success): Đề kiểm tra giữa HK1 2025-2026, đề 2 (40 câu, không có phần nghe).
Sinh bởi tools/gen_mt1_bode.py từ src/mt1/bode.txt."""

SET = {'id': 'lop11-mt1-test02',
 'title': 'Test 2 – Mid-term 1',
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
                        'passage': '<p><b>Mindful Longevity: The Forgotten Connection Between Mental Peace and Physical Health</b></p><p>• The '
                                   '<b>(1) ______</b> community has been increasingly vocal about longevity research. <b>(2) ______</b> recommend '
                                   'daily meditation practices.</p><p>• People <b>(3) ______</b> mindfulness regularly experience fewer '
                                   'stress-related illnesses. Our program gives participants access <b>(4) ______</b> experienced mentors.</p><p>• '
                                   'When it comes to mental health, <b>(5) ______</b> is better than cure. <b>(6) ______</b> to balance your mental '
                                   'and physical health is the key to longevity.</p><p>• Join our Mindful Longevity workshop today and discover how '
                                   'mental peace contributes to a longer, healthier life!</p>',
                        'items': [{'id': 'g1.1', 't': 'mcq', 'q': 'Blank (1)', 'o': ['science', 'scientist', 'scientific', 'scientifically']},
                                  {'id': 'g1.2',
                                   't': 'mcq',
                                   'q': 'Blank (2)',
                                   'o': ['Health modern experts', 'Modern health experts', 'Modern experts health', 'Experts health modern']},
                                  {'id': 'g1.3', 't': 'mcq', 'q': 'Blank (3)', 'o': ['was practiced', 'practicing', 'which practiced', 'practiced']},
                                  {'id': 'g1.4', 't': 'mcq', 'q': 'Blank (4)', 'o': ['to', 'with', 'for', 'about']},
                                  {'id': 'g1.5', 't': 'mcq', 'q': 'Blank (5)', 'o': ['awareness', 'treatment', 'meditation', 'prevention']},
                                  {'id': 'g1.6', 't': 'mcq', 'q': 'Blank (6)', 'o': ['To learning', 'Learn', 'Learning', 'To learn']}]},
                       {'id': 'g2',
                        'instr': 'Read the following leaflet and mark the letter A, B, C or D on your answer sheet to indicate the option that best '
                                 'fits each of the numbered blanks from 7 to 12.',
                        'passage': '<p><b>Resonance 2025: Where Every Note Matters</b></p><p>• Join us at Resonance 2025, while <b>(7) ______</b> '
                                   'are hosting ordinary music events. Our talented musicians will <b>(8) ______</b> the festival with a spectacular '
                                   'performance.</p><p>• The <b>(9) ______</b> of our songs will touch your heart. <b>(10) ______</b> the weather, '
                                   'the concert will continue as planned.</p><p>• The <b>(11) ______</b> between different instruments creates a '
                                   "magical atmosphere. <b>(12) ______</b> of tickets are still available for early booking.</p><p>• Don't miss this "
                                   'amazing music festival! Come and experience the power of music at Resonance 2025, where every note truly '
                                   'matters.</p><p>• <b>Date:</b> August 15-17, 2025</p><p>• <b>Location:</b> City Music Hall</p><p>• '
                                   '<b>Tickets:</b> $25 - $75</p><p>• Book now at www.resonance2025.com or call 555-123-4567.</p>',
                        'items': [{'id': 'g2.7', 't': 'mcq', 'q': 'Blank (7)', 'o': ['others', 'another', 'other', 'the others']},
                                  {'id': 'g2.8', 't': 'mcq', 'q': 'Blank (8)', 'o': ['start up', 'bring on', 'take over', 'kick off']},
                                  {'id': 'g2.9', 't': 'mcq', 'q': 'Blank (9)', 'o': ['rhythm', 'melody', 'lyrics', 'tempo']},
                                  {'id': 'g2.10', 't': 'mcq', 'q': 'Blank (10)', 'o': ['Contrary to', 'Apart from', 'Regardless of', 'Along with']},
                                  {'id': 'g2.11', 't': 'mcq', 'q': 'Blank (11)', 'o': ['connection', 'balance', 'interaction', 'harmony']},
                                  {'id': 'g2.12', 't': 'mcq', 'q': 'Blank (12)', 'o': ['Plenty', 'Lots', 'Some', 'A number']}]},
                       {'id': 'g3',
                        'instr': 'Mark the letter A, B, C or D on your answer sheet to indicate the best arrangement of utterances or sentences to '
                                 'make a meaningful exchange or text in each of the following questions from 13 to 17.',
                        'items': [{'id': 'g3.13',
                                   't': 'mcq',
                                   'q': 'a. Jack: My brother can teach you! He plays guitar every day after school.<br>b. Emma: Wow! Look at this '
                                        'beautiful guitar. I want to learn how to play it.<br>c. Emma: Really? That would be amazing! Can we meet '
                                        'him this weekend?',
                                   'o': ['c-a-b', 'a-b-c', 'b-a-c', 'c-b-a']},
                                  {'id': 'g3.14',
                                   't': 'mcq',
                                   'q': 'a. Jenny: We can buy a cake from the bakery near my house, and we can order pizza from the restaurant '
                                        'downtown.<br>b. Jenny: I would love to help you, but I need to know what kind of party you want.<br>c. '
                                        'Mike: That sounds perfect, and we should also invite our friends from school to make it more fun!<br>d. '
                                        'Mike: I want to have a birthday party next week, and I hope you can help me plan it.<br>e. Mike: I like '
                                        'chocolate cake and pizza, so I want to have both at my party.',
                                   'o': ['b-d-a-e-c', 'd-b-e-a-c', 'd-b-c-a-e', 'e-b-a-c-d']},
                                  {'id': 'g3.15',
                                   't': 'mcq',
                                   'q': "Dear Uncle John,<br>a. When we talked last month, I felt sad because we couldn't understand each other's "
                                        'points of view.<br>b. Even though politics can be difficult to discuss, I know that we both want what is '
                                        'best for our family and our country.<br>c. I am writing because I miss our family dinners, which were '
                                        'always full of laughter and stories.<br>d. Although we have different ideas about politics, I believe that '
                                        'our family love is more important than any disagreement we might have.<br>e. I hope that we can meet soon '
                                        'for coffee, where we can listen to each other with open hearts and minds.<br>With love,<br>LK',
                                   'o': ['a-e-d-c-b', 'e-a-d-c-b', 'd-a-b-e-c', 'c-d-a-e-b']},
                                  {'id': 'g3.16',
                                   't': 'mcq',
                                   'q': 'a. Many people think that we need to buy more things to be happy, which is not always true.<br>b. Growing '
                                        'food in community gardens is good because it brings people together while giving us healthy vegetables to '
                                        'eat.<br>c. When we fix our old things instead of buying new ones, we help our planet and save money at the '
                                        'same time.<br>d. If we focus on what truly makes us happy, such as spending time with loved ones and '
                                        'enjoying nature, we might find that we need less stuff than we thought.<br>e. Although big companies want '
                                        'us to keep shopping, we can find joy in sharing what we already have with friends and family.',
                                   'o': ['a-e-c-b-d', 'e-b-c-a-d', 'c-b-a-e-d', 'b-c-a-e-d']},
                                  {'id': 'g3.17',
                                   't': 'mcq',
                                   'q': 'a. The piano pieces that computers write sometimes fool listeners, who cannot tell if a human or machine '
                                        'created the melody.<br>b. Computers can make music now, which surprises many people who think only humans '
                                        'can be creative.<br>c. Although some musicians worry that machines will take their jobs, many artists use '
                                        'computer tools to help them make new kinds of music.<br>d. If we learn to work together with smart music '
                                        'programs, we might discover amazing new sounds that no one has ever heard before.<br>e. When special '
                                        'programs follow rules that composers create, they can write songs that sound beautiful and interesting.',
                                   'o': ['b-c-d-e-a', 'b-e-c-a-d', 'b-a-e-c-d', 'b-d-a-c-e']}]},
                       {'id': 'g4',
                        'instr': 'Read the following passage about When to Turn Off the Screens and mark the letter A, B, C or D on your answer '
                                 'sheet to indicate the option that best fits each of the numbered blanks from 18 to 22.',
                        'passage': '<p>In 2025, many families struggle with screen time rules. Children often spend hours on tablets and phones, '
                                   'which worries parents around the world. If parents had established clear boundaries earlier, <b>(18) ______</b>. '
                                   'The devices that connect us to friends and information can also disconnect us from the people sitting next to '
                                   'us. Family dinners should be screen-free times; <b>(19) ______.</b> Children need outdoor play for healthy '
                                   'development, but many prefer virtual worlds to real ones. Parents wanting to set good examples and <b>(20) '
                                   '______</b>.</p><p>Experts suggest creating "tech-free zones" in homes where no devices are allowed. The bedroom '
                                   'should be one such zone to improve sleep quality. Some families now use special boxes that lock away all phones '
                                   'during dinner or family game nights. <b>(21) ______.</b> Children learn by watching adults, so parents must '
                                   'model healthy digital habits. When parents put down their phones to play board games or take walks, children see '
                                   'that real-life connections matter. Many schools now teach digital wellness classes to help young people '
                                   "understand how technology affects their brains and emotions.</p><p>The challenge for 2025 families isn't about "
                                   'removing technology completely but finding the right balance. Technology brings many benefits when used wisely, '
                                   'but face-to-face time remains essential for emotional development and family bonding. Research shows that '
                                   'families <b>(22) ______</b>. Finding this balance requires ongoing conversations and adjustments as children '
                                   'grow and technology evolves.</p>',
                        'items': [{'id': 'g4.18',
                                   't': 'mcq',
                                   'q': 'Blank (18)',
                                   'o': ['which connects families to online resources',
                                         'whom children learn digital habits from',
                                         'this problem would not be so difficult now',
                                         'having established clear rules earlier']},
                                  {'id': 'g4.19',
                                   't': 'mcq',
                                   'q': 'Blank (19)',
                                   'o': ['however, many parents check work emails during meals',
                                         'therefore, screens improve family communication skills',
                                         'consequently, technology enhances mealtime conversations',
                                         'thus, digital devices strengthen parent-child relationships']},
                                  {'id': 'g4.20',
                                   't': 'mcq',
                                   'q': 'Blank (20)',
                                   'o': ['having rejected all forms of digital technology',
                                         'encouraging unlimited screen time for development',
                                         'who promote online games instead of outdoor play',
                                         'create healthy habits must first examine their own screen use']},
                                  {'id': 'g4.21',
                                   't': 'mcq',
                                   'q': 'Blank (21)',
                                   'o': ['Such digital devices prevent children from developing social skills',
                                         'These simple tools help create important boundaries in a digital world',
                                         'Modern technology eliminates the need for face-to-face interaction',
                                         'Screen time should replace traditional family bonding activities']},
                                  {'id': 'g4.22',
                                   't': 'mcq',
                                   'q': 'Blank (22)',
                                   'o': ['which encourage constant digital engagement develop healthier family bonds',
                                         'will ban technology completely had experienced more family conflicts',
                                         'had promoted unlimited screen time are seeing improved social skills',
                                         'who set clear screen time limits report better communication and stronger relationships']}]},
                       {'id': 'g5',
                        'instr': 'Read the following passage about The Silent Crisis Beneath the Waves and mark the letter A, B, C or D on your '
                                 'answer sheet to indicate the best answer to each of the following questions from 23 to 30.',
                        'passage': '<p><small>[Paragraph 1]</small> Ocean acidification is a problem that happens when the sea absorbs too much '
                                   "carbon dioxide from the air. This process makes the water more acidic, which means the ocean's pH level drops. "
                                   'Since the Industrial Revolution began, ocean pH has <b><u>fallen</u></b> by about 0.1 units, representing a 30% '
                                   'increase in acidity. This change might seem small, but it has big effects on marine '
                                   'life.</p><p><small>[Paragraph 2]</small> The main victims of ocean acidification are coral reefs and shellfish. '
                                   'These animals need calcium carbonate to build their shells and skeletons. In acidic water, calcium carbonate '
                                   '<b><u>dissolves</u></b> easily, making it hard for these creatures to grow. Scientists have observed that '
                                   'shellfish now have thinner shells. Coral reefs, which provide homes for thousands of species, are growing slowly '
                                   'and becoming fragile. Without action, we could lose 90% of coral reefs by 2050.</p><p><small>[Paragraph '
                                   '3]</small> Ocean acidification also affects the food chain. Tiny creatures called pteropods, or "sea '
                                   'butterflies," are an important food for many fish, including salmon. As <b>their</b> shells become damaged, '
                                   'pteropod populations decrease. This impacts fish that eat them, and eventually humans who depend on these fish '
                                   'for food. Fishing communities are already noticing changes in fish populations and sizes, affecting their '
                                   'livelihoods.</p><p><small>[Paragraph 4]</small> We can take steps to address this problem. <b><u>Reducing carbon '
                                   'dioxide emissions is the most effective solution.</u></b> Using renewable energy helps decrease carbon dioxide '
                                   'released into the atmosphere. Protecting coastal habitats like seagrass beds, which remove carbon dioxide from '
                                   'water, is another strategy. Scientists are developing methods to help species adapt to changing conditions. By '
                                   'working together, we can slow ocean acidification and protect marine ecosystems for future generations.</p>',
                        'items': [{'id': 'g5.23',
                                   't': 'mcq',
                                   'q': 'According to the passage, which of the following is NOT mentioned as an effect of ocean acidification?',
                                   'o': ['Damage to coral reefs',
                                         'Thinner shells in shellfish',
                                         'Increased ocean temperature',
                                         'Changes in fish populations']},
                                  {'id': 'g5.24',
                                   't': 'mcq',
                                   'q': 'The word “<b><u>fallen</u></b>” in paragraph 1 is OPPOSITE in meaning to _________.',
                                   'o': ['risen', 'decreased', 'dropped', 'lowered']},
                                  {'id': 'g5.25',
                                   't': 'mcq',
                                   'q': 'The word “<b><u>dissolves</u></b>” in paragraph 2 could be best replaced by _________.',
                                   'o': ['hardens', 'melts', 'forms', 'grows']},
                                  {'id': 'g5.26',
                                   't': 'mcq',
                                   'q': 'The word “<b>their</b>” in paragraph 3 refers to _________.',
                                   'o': ['pteropods', 'fish', 'salmon', 'humans']},
                                  {'id': 'g5.27',
                                   't': 'mcq',
                                   'q': 'Which of the following best summarises paragraph 4?',
                                   'o': ['Renewable energy is the only way to solve the ocean acidification crisis.',
                                         'Scientists cannot agree on how to address the problem of acidification.',
                                         'Coastal habitats are more important than reducing carbon emissions.',
                                         'Solutions to ocean acidification require global cooperation and action.']},
                                  {'id': 'g5.28',
                                   't': 'mcq',
                                   'q': 'Which of the following is TRUE according to the passage?',
                                   'o': ['Ocean pH has decreased by 30% since the Industrial Revolution began.',
                                         'All coral reefs will completely disappear from oceans by the year 2050.',
                                         'Ocean pH has fallen by 0.1 units, showing a 30% increase in acidity.',
                                         'Pteropods are the only significant food source for salmon populations.']},
                                  {'id': 'g5.29',
                                   't': 'mcq',
                                   'q': 'In which paragraph does the writer mention the effects of acidification on shellfish and coral reefs?',
                                   'o': ['Paragraph 1', 'Paragraph 2', 'Paragraph 3', 'Paragraph 4']},
                                  {'id': 'g5.30',
                                   't': 'mcq',
                                   'q': 'In which paragraph does the writer describe how acidification affects the marine food chain?',
                                   'o': ['Paragraph 3', 'Paragraph 2', 'Paragraph 4', 'Paragraph 1']}]},
                       {'id': 'g6',
                        'instr': 'Read the following passage about the Understanding the Psychological Response to Emerging Sound Patterns and mark '
                                 'the letter A, B, C or D on your answer sheet to indicate the best answer to each of the following questions from '
                                 '31 to 40.',
                        'passage': '<p><small>[Paragraph 1]</small> Psychoacoustics examines how humans perceive and respond to sound. This field '
                                   'sits at the crossroads of psychology and acoustics, revealing how our brains make sense of the world through our '
                                   'ears. When researchers first delved into this area, they <b><u>were all ears</u></b> about discovering the '
                                   'relationship between sound waves and psychological experiences. Studies show that our brains process different '
                                   'sound characteristics—like pitch, loudness, and timbre—simultaneously. Even subtle changes in sound patterns can '
                                   'trigger strong emotional responses, explaining why certain music pieces can bring tears while others energize '
                                   'us.</p><p><small>[Paragraph 2]</small> Sound perception varies among individuals based on factors like age, '
                                   'culture, and personal experience. <b>[I]</b> Children typically hear higher frequencies better than adults, '
                                   'which explains why some high-pitched sounds are only audible to younger people. <b>[II]</b> Cultural background '
                                   'shapes how we interpret sounds; what sounds pleasant in one culture might be jarring in another. <b>[III]</b> '
                                   'Our brains are remarkably adaptable when processing sound, allowing us to filter background noise during '
                                   'conversations—known as the "cocktail party effect." <b>[IV]</b></p><p><small>[Paragraph 3]</small> The practical '
                                   'applications of psychoacoustics extend into many areas. Sound designers use these principles to create immersive '
                                   'experiences in movies and games. In healthcare, understanding sound <b><u>perception</u></b> helps develop '
                                   'better hearing aids that process sound to match individual hearing patterns. Architects apply psychoacoustic '
                                   'principles when designing concert halls to create optimal acoustic environments. Even product manufacturers '
                                   'consider how <b>their</b> products sound—from the click of a luxury car door to smartphone notifications—knowing '
                                   'these sounds influence consumer perception.</p><p><small>[Paragraph 4]</small> As technology advances, '
                                   'psychoacoustics continues to evolve. <b><u>Virtual reality developers are creating more realistic 3D audio '
                                   'experiences that mimic how sounds naturally reach our ears.</u></b> Scientists are exploring how sound affects '
                                   'cognitive performance, finding that certain patterns can enhance or impair concentration. Some researchers are '
                                   'investigating therapeutic applications, using specific frequencies to reduce stress or improve sleep. '
                                   'Understanding our psychological response to sound remains crucial as our world becomes increasingly filled with '
                                   'artificial sounds, helping us design healthier sonic environments.</p>',
                        'items': [{'id': 'g6.31',
                                   't': 'mcq',
                                   'q': 'The phrase “<b><u>were all ears</u></b>” in paragraph 1 could be best replaced by _________.',
                                   'o': ['look up', 'listen in', 'take in', 'tune out']},
                                  {'id': 'g6.32',
                                   't': 'mcq',
                                   'q': 'Where in paragraph 2 does the following sentence best fit?<br><b>This ability helps us focus on important '
                                        'sounds while ignoring distractions.</b>',
                                   'o': ['[I]', '[II]', '[III]', '[IV]']},
                                  {'id': 'g6.33',
                                   't': 'mcq',
                                   'q': 'According to the passage, which of the following is NOT mentioned as a factor affecting sound perception?',
                                   'o': ['age', 'educational level', 'cultural background', 'personal experience']},
                                  {'id': 'g6.34',
                                   't': 'mcq',
                                   'q': 'Which of the following best summarises paragraph 3?',
                                   'o': ['Psychoacoustics has diverse practical applications across multiple industries.',
                                         'Sound designers rely on psychoacoustics more than healthcare professionals.',
                                         'Product manufacturers prioritize sound quality over visual product design.',
                                         'Architects must study psychoacoustics to create successful concert venues.']},
                                  {'id': 'g6.35',
                                   't': 'mcq',
                                   'q': 'The word “<b><u>perception</u></b>” in paragraph 3 is OPPOSITE in meaning to _________.',
                                   'o': ['awareness', 'sensation', 'ignorance', 'reception']},
                                  {'id': 'g6.36',
                                   't': 'mcq',
                                   'q': 'The word “<b>their</b>” in paragraph 3 refers to _________.',
                                   'o': ['sounds', 'consumers', 'architects', 'manufacturers']},
                                  {'id': 'g6.37',
                                   't': 'mcq',
                                   'q': 'Which of the following best paraphrases the underlined sentence in paragraph 4?',
                                   'o': ['Creators of virtual reality are designing audio that accurately simulates natural sound reception.',
                                         'Virtual reality experts are researching how human ears process three-dimensional sound waves.',
                                         'Developers are testing new technologies to enhance the volume of sounds in virtual environments.',
                                         'Virtual reality companies are competing to produce the most complex audio systems available.']},
                                  {'id': 'g6.38',
                                   't': 'mcq',
                                   'q': 'Which of the following is TRUE according to the passage?',
                                   'o': ['All cultures interpret sound patterns in similar ways regardless of background.',
                                         'Children typically hear higher frequencies better than most adult listeners.',
                                         'Sound designers are the primary beneficiaries of psychoacoustic research.',
                                         'Virtual reality cannot accurately replicate how sounds reach human ears.']},
                                  {'id': 'g6.39',
                                   't': 'mcq',
                                   'q': 'Which of the following can be inferred from the passage?',
                                   'o': ['Sound perception research will eventually eliminate all unwanted noise pollution.',
                                         'Most people are unaware of how significantly sound affects their daily experiences.',
                                         'Future hearing aids may incorporate more sophisticated psychoacoustic principles.',
                                         'Virtual reality will replace traditional methods of studying human sound perception.']},
                                  {'id': 'g6.40',
                                   't': 'mcq',
                                   'q': 'Which of the following best summarises the passage?',
                                   'o': ['Therapeutic applications of sound frequencies represent the future of medical treatments.',
                                         'Cultural differences in sound perception create challenges for international sound design.',
                                         'Virtual reality developers are leading innovations in three-dimensional audio experiences.',
                                         'Psychoacoustics studies how humans perceive sound and has applications across various fields.']}]}]}]}
