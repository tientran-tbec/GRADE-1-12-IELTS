# -*- coding: utf-8 -*-
"""Sinh bởi tools/gen_lop4_hsg.py"""

SET = {'grade': 4,
 'id': 'lop4-hsg-a',
 'pages': [{'groups': [{'id': 'v1',
                        'instr': 'Unit 1 – My friends: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v1.1', 'o': ['America', 'Australia', 'Britain', 'Japan'], 'q': 'I want to visit Disneyland in _______.', 't': 'mcq'},
                                  {'id': 'v1.2', 'o': ['America', 'Australia', 'Britain', 'Japan'], 'q': 'Kangaroos hop around in _______.', 't': 'mcq'},
                                  {'id': 'v1.3', 'o': ['America', 'Australia', 'Britain', 'Japan'], 'q': 'The Queen lives in a palace in _______.', 't': 'mcq'},
                                  {'id': 'v1.4', 'o': ['America', 'Australia', 'Britain', 'Japan'], 'q': 'Sushi is a delicious dish from _______.', 't': 'mcq'},
                                  {'id': 'v1.5',
                                   'o': ['America', 'Australia', 'Britain', 'Malaysia'],
                                   'q': 'The Petronas Towers, one of the tallest twin towers, are in _______.',
                                   't': 'mcq'},
                                  {'id': 'v1.6',
                                   'o': ['Singapore', 'Thailand', 'Vietnam', 'Japan'],
                                   'q': 'The Merlion is a famous statue in _______.',
                                   't': 'mcq'},
                                  {'id': 'v1.7',
                                   'o': ['Singapore', 'Thailand', 'Vietnam', 'Japan'],
                                   'q': 'Pho, a tasty noodle soup, is a traditional dish from _______.',
                                   't': 'mcq'},
                                  {'id': 'v1.8',
                                   'o': ['America', 'Australia', 'Britain', 'Japan'],
                                   'q': 'Beautiful beaches and the Great Barrier Reef can be found in _______.',
                                   't': 'mcq'}]},
                       {'id': 'v2',
                        'instr': 'Unit 2 – Time and daily routines: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v2.1', 'o': ["o'clock", 'fifteen', 'get up', 'go'], 'q': 'School starts at eight ___________.', 't': 'mcq'},
                                  {'id': 'v2.2',
                                   'o': ['go to school', 'have breakfast', 'go to bed', 'at'],
                                   'q': "I eat my morning meal, it's called ___________.",
                                   't': 'mcq'},
                                  {'id': 'v2.3', 'o': ["o'clock", 'go to school', 'fifteen', 'at'], 'q': 'Lunchtime is around twelve ___________.', 't': 'mcq'},
                                  {'id': 'v2.4',
                                   'o': ['get up', 'have breakfast', 'go to school', 'go to bed'],
                                   'q': 'In the evening, I ____ ____ and sleep.',
                                   't': 'mcq'}]},
                       {'id': 'v3',
                        'instr': 'Unit 3 – My week: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v3.1', 'o': ['Tuesday', 'Wednesday', 'Sunday'], 'q': 'The day after Monday is _______.', 't': 'mcq'},
                                  {'id': 'v3.2', 'o': ['study at school', 'listen to music', 'Thursday'], 'q': 'I like to _______ on the weekend.', 't': 'mcq'},
                                  {'id': 'v3.3', 'o': ['Saturday', 'Monday', 'Wednesday'], 'q': 'After Sunday comes _______.', 't': 'mcq'},
                                  {'id': 'v3.4', 'o': ['Thursday', 'Friday', 'study at school'], 'q': '_______ is the day before Saturday.', 't': 'mcq'}]},
                       {'id': 'v4',
                        'instr': 'Unit 4 – My birthday party: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v4.1', 'o': ['May', 'January', 'party'], 'q': '_______ is the first month of the year.', 't': 'mcq'},
                                  {'id': 'v4.2', 'o': ['water', 'chips', 'jam'], 'q': 'I like to have sandwiches with _______ on them.', 't': 'mcq'},
                                  {'id': 'v4.3', 'o': ['Juice', 'Jam', 'Lemonade'], 'q': '_______ is a sweet spread we put on bread or toast.', 't': 'mcq'}]},
                       {'id': 'v5',
                        'instr': 'Unit 5 – Things we can do: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v5.1',
                                   'o': ['can', 'play the piano', 'swim'],
                                   'q': 'Mom said I _______ have some ice cream after dinner.',
                                   't': 'mcq'},
                                  {'id': 'v5.2',
                                   'o': ['cook', 'ride a horse', 'roller skate'],
                                   'q': 'After eating, I like to _______ and have fun at the park.',
                                   't': 'mcq'},
                                  {'id': 'v5.3',
                                   'o': ['play the piano', 'ride a bike', 'swim'],
                                   'q': 'I can _______ in the pool because I learned how.',
                                   't': 'mcq'},
                                  {'id': 'v5.4',
                                   'o': ['ride a bike', 'play the guitar', 'cook'],
                                   'q': 'Mom can _______ a delicious meal for dinner.',
                                   't': 'mcq'},
                                  {'id': 'v5.5',
                                   'o': ['ride a horse', 'roller skate', 'ride'],
                                   'q': 'I want to _______ a bike without training wheels soon.',
                                   't': 'mcq'},
                                  {'id': 'v5.6', 'o': ['but', 'play the piano', 'can'], 'q': 'I like ice cream, _______ I also like cake.', 't': 'mcq'}]},
                       {'id': 'v6',
                        'instr': 'Unit 6 – Our school facilities: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v6.1',
                                   'o': ['city', 'mountains', 'village'],
                                   'q': 'People in the _______ often have big farms and grow their own food.',
                                   't': 'mcq'},
                                  {'id': 'v6.2',
                                   'o': ['computer room', 'town', 'playground'],
                                   'q': 'I like to play in the _______ after school with my friends.',
                                   't': 'mcq'},
                                  {'id': 'v6.3',
                                   'o': ['village', 'computer room', 'city'],
                                   'q': 'Our school has a special room with lots of computers called the _______.',
                                   't': 'mcq'},
                                  {'id': 'v6.4',
                                   'o': ['village', 'mountains', 'city'],
                                   'q': 'We live in a small _______ where everyone knows each other.',
                                   't': 'mcq'},
                                  {'id': 'v6.5',
                                   'o': ['garden', 'mountains', 'town'],
                                   'q': 'When we go on vacation, we like to visit the _______ and see the beautiful scenery.',
                                   't': 'mcq'}]},
                       {'id': 'v7',
                        'instr': 'Unit 7 – Our timetables: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v7.1',
                                   'o': ['art', 'history and geography', 'science'],
                                   'q': 'I like to draw and color in _______ class.',
                                   't': 'mcq'},
                                  {'id': 'v7.2',
                                   'o': ['maths', 'history and geography', 'Vietnamese'],
                                   'q': 'In _______ class, we learn about the world and different countries.',
                                   't': 'mcq'},
                                  {'id': 'v7.3',
                                   'o': ['music', 'English', 'science'],
                                   'q': 'I enjoy singing and playing instruments in _______ class.',
                                   't': 'mcq'},
                                  {'id': 'v7.4',
                                   'o': ['maths', 'history and geography', 'art'],
                                   'q': 'Numbers and calculations are taught in _______ class.',
                                   't': 'mcq'},
                                  {'id': 'v7.5',
                                   'o': ['science', 'Vietnamese', 'music'],
                                   'q': 'In _______ class, we learn about plants, animals, and the environment.',
                                   't': 'mcq'},
                                  {'id': 'v7.6',
                                   'o': ['history and geography', 'music', 'art'],
                                   'q': 'I learn about the past and different events in _______ class.',
                                   't': 'mcq'}]}],
            'id': 'tu-vung',
            'mode': 'practice',
            'title': 'Từ vựng – Unit 1–7'},
           {'groups': [{'id': 'v8',
                        'instr': 'Unit 8 – My favourite subjects: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v8.1',
                                   'o': ['IT (information technology)', 'PE (physical education)', 'English teacher'],
                                   'q': 'We learn about computers and technology in _______ class.',
                                   't': 'mcq'},
                                  {'id': 'v8.2',
                                   'o': ['maths teacher', 'IT (information technology)', 'PE (physical education)'],
                                   'q': 'My favorite subject is math, and the teacher is the _______.',
                                   't': 'mcq'},
                                  {'id': 'v8.3',
                                   'o': ['English teacher', 'because', 'playground'],
                                   'q': 'I have PE (physical education) class, and we play sports like soccer and run around in the _______.',
                                   't': 'mcq'},
                                  {'id': 'v8.4',
                                   'o': ['maths teacher', 'IT (information technology)', 'English teacher'],
                                   'q': 'The person who teaches us about the English language is called the _______.',
                                   't': 'mcq'},
                                  {'id': 'v8.5',
                                   'o': ['PE (physical education)', 'maths teacher', 'because'],
                                   'q': 'We exercise and do fun activities in _______ class.',
                                   't': 'mcq'},
                                  {'id': 'v8.6',
                                   'o': ['why', 'because', 'IT (information technology)'],
                                   'q': 'I like to ask _______ and understand more about things.',
                                   't': 'mcq'}]},
                       {'id': 'v9',
                        'instr': 'Unit 9 – Our sports day: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v9.1',
                                   'o': ['sports day', 'October', 'December'],
                                   'q': 'We have a special event called _______ at school where we play games and have fun.',
                                   't': 'mcq'},
                                  {'id': 'v9.2', 'o': ['July', 'November', 'August'], 'q': '_______ comes after October.', 't': 'mcq'},
                                  {'id': 'v9.3', 'o': ['July', 'November', 'December'], 'q': 'Christmas is in _______.', 't': 'mcq'},
                                  {'id': 'v9.4',
                                   'o': ['June', 'December', 'January'],
                                   'q': 'I get gifts and celebrate the Lunar New Year in _______.',
                                   't': 'mcq'},
                                  {'id': 'v9.5',
                                   'o': ['July', 'sports day', 'September'],
                                   'q': '_______ is the month when school usually starts again after a break.',
                                   't': 'mcq'}]},
                       {'id': 'v10',
                        'instr': 'Unit 10 – Our summer holidays: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v10.1', 'o': ['beach', 'campsite', 'Tokyo'], 'q': 'We built a sandcastle at the _______.', 't': 'mcq'},
                                  {'id': 'v10.2',
                                   'o': ['beach', 'Bangkok', 'campsite'],
                                   'q': 'We saw tall buildings and busy streets when we visited _______.',
                                   't': 'mcq'},
                                  {'id': 'v10.3',
                                   'o': ['Sydney', 'beach', 'countryside'],
                                   'q': 'We had a picnic in the _______ and enjoyed the fresh air.',
                                   't': 'mcq'},
                                  {'id': 'v10.4', 'o': ['Tokyo', 'beach', 'countryside'], 'q': 'We went to the _______ zoo and saw many animals.', 't': 'mcq'},
                                  {'id': 'v10.5',
                                   'o': ['on; yesterday', 'at; last', 'in; yesterday'],
                                   'q': 'I played with my friends _______ the park _______ afternoon.',
                                   't': 'mcq'}]},
                       {'id': 'v11',
                        'instr': 'Unit 11 – My home: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v11.1',
                                   'o': ['at; on', 'in; on', 'on; in'],
                                   'q': "My friend's house is _______ Hoang Hoa Tham _______ the city.",
                                   't': 'mcq'},
                                  {'id': 'v11.2',
                                   'o': ['busy; noisy', 'quiet; big', 'in; on'],
                                   'q': "The city center has many tall buildings, and it's always _______ and _______.",
                                   't': 'mcq'}]},
                       {'id': 'v12',
                        'instr': 'Unit 12 – Jobs: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v12.1', 'o': ['actor', 'farmer', 'policeman'], 'q': 'Spider-Man is a superhero and also an _______.', 't': 'mcq'},
                                  {'id': 'v12.2',
                                   'o': ['nurse', 'factory', 'farming'],
                                   'q': 'Mom helps sick people get better, and she is a _______.',
                                   't': 'mcq'},
                                  {'id': 'v12.3',
                                   'o': ['actor', 'policeman', 'farmer'],
                                   'q': 'A person who helps keep the town safe and catches bad guys is a _______.',
                                   't': 'mcq'},
                                  {'id': 'v12.4',
                                   'o': ['hospital', 'farm', 'nursing home'],
                                   'q': 'We grow vegetables and raise animals on a _______.',
                                   't': 'mcq'},
                                  {'id': 'v12.5',
                                   'o': ['nurse', 'factory', 'nursing home'],
                                   'q': 'People who work in a _______ take care of elderly individuals.',
                                   't': 'mcq'},
                                  {'id': 'v12.6', 'o': ['actor', 'farmer', 'policeman'], 'q': 'Batman is a famous movie _______.', 't': 'mcq'},
                                  {'id': 'v12.7',
                                   'o': ['hospital', 'factory', 'farm'],
                                   'q': 'A person who takes care of sick people in a _______ is a nurse.',
                                   't': 'mcq'}]},
                       {'id': 'v13',
                        'instr': 'Unit 13 – Appearance: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v13.1',
                                   'o': ['big', 'tall', 'short'],
                                   'q': 'My friend is very _______ and can easily reach high shelves.',
                                   't': 'mcq'},
                                  {'id': 'v13.2', 'o': ['eyes; face', 'hair; eyes', 'face; hair'], 'q': 'I have blue _______ and a happy _______.', 't': 'mcq'},
                                  {'id': 'v13.3', 'o': ['round', 'long', 'short'], 'q': 'The cat has a _______ tail, not a short one.', 't': 'mcq'},
                                  {'id': 'v13.4', 'o': ['round', 'tall', 'big'], 'q': 'The boy has a _______ face with a cute smile.', 't': 'mcq'}]},
                       {'id': 'v14',
                        'instr': 'Unit 14 – Daily activities: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v14.1', 'o': ['afternoon', 'evening', 'noon'], 'q': 'We have lunch at _______ every day.', 't': 'mcq'},
                                  {'id': 'v14.2',
                                   'o': ['morning', 'evening', 'afternoon'],
                                   'q': 'We usually have dinner in the _______ when the sun is setting.',
                                   't': 'mcq'},
                                  {'id': 'v14.3',
                                   'o': ['afternoon', 'evening', 'morning'],
                                   'q': 'Grandma likes to tell stories in the _______ before bedtime.',
                                   't': 'mcq'},
                                  {'id': 'v14.4',
                                   'o': ['clean the floor', 'wash the clothes', 'wash the dishes'],
                                   'q': 'After breakfast, I help Mom _______ by putting the dirty clothes in the washing machine.',
                                   't': 'mcq'},
                                  {'id': 'v14.5',
                                   'o': ['noon', 'afternoon', 'morning'],
                                   'q': 'We eat lunch at _______ and take a short nap afterward.',
                                   't': 'mcq'}]}],
            'id': 'tu-vung-2',
            'mode': 'practice',
            'title': 'Từ vựng – Unit 8–14'},
           {'groups': [{'id': 'v15',
                        'instr': 'Unit 15 – My family’s weekends: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v15.1',
                                   'o': ['cinema', 'shopping centre', 'sports centre'],
                                   'q': 'On weekends, we like to go to the _______ and watch exciting movies.',
                                   't': 'mcq'},
                                  {'id': 'v15.2',
                                   'o': ['sports centre', 'cinema', 'swimming pool'],
                                   'q': 'My favorite place to swim is the _______.',
                                   't': 'mcq'},
                                  {'id': 'v15.3',
                                   'o': ['shopping centre', 'cinema', 'sports centre'],
                                   'q': 'We buy toys and clothes at the _______.',
                                   't': 'mcq'},
                                  {'id': 'v15.4',
                                   'o': ['shopping centre', 'sports centre', 'cinema'],
                                   'q': 'In the _______, we can watch athletes play different sports.',
                                   't': 'mcq'},
                                  {'id': 'v15.5',
                                   'o': ['play tennis', 'do yoga', 'cook meals'],
                                   'q': 'Mom teaches me how to _______ in the kitchen.',
                                   't': 'mcq'},
                                  {'id': 'v15.6',
                                   'o': ['shopping centre', 'sports centre', 'swimming pool'],
                                   'q': 'On a hot day, we love to cool off by going to the _______.',
                                   't': 'mcq'},
                                  {'id': 'v15.7',
                                   'o': ['watch films', 'play tennis', 'do yoga'],
                                   'q': 'Dad and I like to have fun and play a game of _______ at the local sports facility.',
                                   't': 'mcq'}]},
                       {'id': 'v16',
                        'instr': 'Unit 16 – Weather: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v16.1', 'o': ['cloudy', 'rainy', 'sunny'], 'q': "When the sky is full of clouds, we say it's _______.", 't': 'mcq'},
                                  {'id': 'v16.2',
                                   'o': ['cloudy', 'sunny', 'windy'],
                                   'q': "If it's not raining and the sun is shining, it's a _______ day.",
                                   't': 'mcq'},
                                  {'id': 'v16.3',
                                   'o': ['bakery', 'bookshop', 'food stall'],
                                   'q': 'We buy fresh bread from the _______ in the morning.',
                                   't': 'mcq'},
                                  {'id': 'v16.4',
                                   'o': ['water park', 'supermarket', 'bakery'],
                                   'q': 'We can buy fruits and vegetables at the _______.',
                                   't': 'mcq'},
                                  {'id': 'v16.5',
                                   'o': ['rainy', 'windy', 'sunny'],
                                   'q': 'On a _______ day, we can go to the water park and have lots of fun.',
                                   't': 'mcq'},
                                  {'id': 'v16.6',
                                   'o': ['bakery', 'bookshop', 'supermarket'],
                                   'q': 'The place where we can find books is called a _______.',
                                   't': 'mcq'},
                                  {'id': 'v16.7',
                                   'o': ['bakery', 'food stall', 'water park'],
                                   'q': 'We eat delicious noodles at the _______ in the market.',
                                   't': 'mcq'},
                                  {'id': 'v16.8',
                                   'o': ['supermarket', 'water park', 'bookshop'],
                                   'q': 'The _______ is a great place to buy snacks, toys, and groceries.',
                                   't': 'mcq'}]},
                       {'id': 'v17',
                        'instr': 'Unit 17 – In the city: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v17.1',
                                   'o': ['turn round', 'turn left', 'go straight'],
                                   'q': 'If you need to change direction completely, you _______.',
                                   't': 'mcq'}]},
                       {'id': 'v18',
                        'instr': 'Unit 18 – At the shopping centre: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v18.1',
                                   'o': ['gift shop', 'T-shirt', 'skirt'],
                                   'q': 'The _______ is where we can buy presents for our friends.',
                                   't': 'mcq'},
                                  {'id': 'v18.2', 'o': ['near', 'opposite', 'between'], 'q': 'The park is _______ the school and the library.', 't': 'mcq'},
                                  {'id': 'v18.3', 'o': ['gift shop', 'thousand', 'skirt'], 'q': 'Mom gave me ten _______ to buy ice cream.', 't': 'mcq'}]},
                       {'id': 'v19',
                        'instr': 'Unit 19 – The animal world: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v19.1', 'o': ['roar', 'sing', 'dance'], 'q': 'The lion can _______ in the jungle.', 't': 'mcq'},
                                  {'id': 'v19.2',
                                   'o': ['sings', 'roars', 'runs'],
                                   'q': "The lion _______ when it's happy or wants to communicate.",
                                   't': 'mcq'}]},
                       {'id': 'v20',
                        'instr': 'Unit 20 – At summer camp: Choose the correct option. (Chọn đáp án đúng.)',
                        'items': [{'id': 'v20.1',
                                   'o': ['play card games', 'tell a story', 'put up a tent'],
                                   'q': 'Before bedtime, we often _______ to each other inside the tent.',
                                   't': 'mcq'},
                                  {'id': 'v20.2',
                                   'o': ['build a campfire', 'take a photo', 'sing songs'],
                                   'q': 'When we see a beautiful view, we like to _______ to capture the moment.',
                                   't': 'mcq'},
                                  {'id': 'v20.3',
                                   'o': ['tell a story', 'put up a tent', 'play card games'],
                                   'q': 'To have a cozy sleeping area, we need to _______ first.',
                                   't': 'mcq'}]}],
            'id': 'tu-vung-3',
            'mode': 'practice',
            'title': 'Từ vựng – Unit 15–20'},
           {'groups': [{'id': 'r1',
                        'instr': 'Unit 1 – My friends: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r1.1',
                                   'o': ['Cute kangaroos', 'The Great Barrier Reef', 'Tall buildings and the Statue of Liberty'],
                                   'q': 'What is America known for?',
                                   't': 'mcq'},
                                  {'id': 'r1.2', 'o': ['English', 'Japanese', 'Malay'], 'q': 'What language do people speak in Japan?', 't': 'mcq'},
                                  {'id': 'r1.3',
                                   'o': ['The Petronas Towers', 'The Merlion', 'Golden temples'],
                                   'q': 'What is a famous symbol in Singapore?',
                                   't': 'mcq'},
                                  {'id': 'r1.4', 'o': ['Ao dai', 'Kimono', 'Sari'], 'q': 'What is the traditional costume in Viet Nam?', 't': 'mcq'},
                                  {'id': 'r1.5', 'q': 'Australia is known for its delicious sushi.', 't': 'tf'},
                                  {'id': 'r1.6', 'q': 'People in Singapore speak only English.', 't': 'tf'},
                                  {'id': 'r1.7', 'q': 'The Petronas Towers are located in Japan.', 't': 'tf'},
                                  {'id': 'r1.8', 'q': 'The traditional costume in Viet Nam is called kimono.', 't': 'tf'}],
                        'passage': "<h4>Amazing Countries</h4><p>The world is a big, colorful place with many countries to explore. Let's talk about some of "
                                   "them!</p><p>America is a land far, far away. It's known for its tall buildings, famous landmarks, and the Statue of "
                                   "Liberty. People in America speak English, just like us.</p><p>Australia is where cute kangaroos hop around. It's also "
                                   'known for the Great Barrier Reef, a colorful underwater world. In Australia, people speak English, too.</p><p>Britain is a '
                                   'country with a queen and a royal palace. The double-decker buses and red telephone booths make it unique. People in '
                                   'Britain also speak English.</p><p>Japan is a land of cherry blossoms and sushi. The bullet trains are super fast, and '
                                   'there are beautiful temples to explore. In Japan, people speak Japanese.</p><p>Malaysia is a tropical paradise with lush '
                                   'rainforests and delicious food. The Petronas Towers in Kuala Lumpur are really tall! People in Malaysia speak '
                                   'Malay.</p><p>Singapore is a tiny city-state with modern buildings and beautiful gardens. The Merlion, a mythical creature, '
                                   'is a famous symbol. People in Singapore speak English, Malay, Chinese, and Tamil.</p><p>Thailand is known for its golden '
                                   'temples and spicy food. The elephants in Thailand are friendly and playful. People in Thailand speak Thai.</p><p>And then '
                                   "there's our country, Viet Nam! We have beautiful landscapes, from mountains to beaches. The traditional ao dai is our "
                                   'special costume. In Viet Nam, we speak Vietnamese.</p><p>Every country is like a different page in a giant book, and each '
                                   'page tells a unique and wonderful story!</p>'},
                       {'id': 'r2',
                        'instr': 'Unit 2 – Time and daily routines: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm '
                                 'bài.)',
                        'items': [{'id': 'r2.1',
                                   'o': ["6 o'clock", "7 o'clock", "8 o'clock"],
                                   'q': 'What time does the narrator get up in the morning?',
                                   't': 'mcq'},
                                  {'id': 'r2.2', 'o': ["3 o'clock", "6 o'clock", "8 o'clock"], 'q': 'When does the narrator go to school?', 't': 'mcq'},
                                  {'id': 'r2.3',
                                   'o': ['Vegetables and rice', 'Cereal with milk and orange juice', 'A piece of chicken'],
                                   'q': 'What does the narrator have for breakfast?',
                                   't': 'mcq'},
                                  {'id': 'r2.4', 'o': ["7 o'clock", "8 o'clock", "9 o'clock"], 'q': 'What time does the narrator go to bed?', 't': 'mcq'},
                                  {'id': 'r2.5', 'q': "The narrator goes to school at 6 o'clock in the evening.", 't': 'tf'},
                                  {'id': 'r2.6', 'q': "The narrator has a healthy dinner at 6 o'clock in the evening.", 't': 'tf'},
                                  {'id': 'r2.7', 'q': 'Before sleeping, the narrator likes to play with toys.', 't': 'tf'},
                                  {'id': 'r2.8', 'q': "The narrator gets up at 8 o'clock in the morning.", 't': 'tf'}],
                        'passage': "<h4>My Daily Routine</h4><p>Every day, I have a routine that helps me stay happy and healthy. Let's explore a typical day "
                                   "in my life!</p><p>I get up at 7 o'clock in the morning. It's time to start a new day! I wash my face, brush my teeth, and "
                                   "get ready for the adventures ahead.</p><p>After getting ready, it's time to have breakfast. I enjoy a bowl of cereal with "
                                   "milk and a glass of orange juice. Yummy!</p><p>At 8 o'clock, I go to school. I learn new things, play with my friends, and "
                                   'have a lot of fun. School is like a second home, full of laughter and learning.</p><p>When the school day is over at 3 '
                                   "o'clock, I come home and have a little break. I might play with my toys or read a book.</p><p>At 6 o'clock in the evening, "
                                   "it's time for dinner. I eat vegetables, rice, and sometimes a piece of chicken. A healthy dinner keeps me strong and "
                                   "energetic.</p><p>After dinner, it's time to wind down. I go to bed at 8 o'clock. Before sleeping, I like to read a bedtime "
                                   "story or listen to a lullaby.</p><p>And that's a day in my life! I follow this routine every day to make sure I have a "
                                   'happy and balanced life.</p>'},
                       {'id': 'r3',
                        'instr': 'Unit 3 – My week: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r3.1',
                                   'o': ['Sleep in a little bit', 'Listen to music', 'Solve puzzles'],
                                   'q': 'What do we do on Wednesday?',
                                   't': 'mcq'},
                                  {'id': 'r3.2', 'o': ['Thursday', 'Wednesday', 'Sunday'], 'q': 'Which day is right in the middle of the week?', 't': 'mcq'},
                                  {'id': 'r3.3',
                                   'o': ['The start of the school week', 'The last day of the school week', 'Special family time'],
                                   'q': 'What is Friday known for?',
                                   't': 'mcq'},
                                  {'id': 'r3.4', 'q': 'Tuesday is a day for sleeping in a little bit.', 't': 'tf'},
                                  {'id': 'r3.5', 'q': 'Thursday is the last day of the school week.', 't': 'tf'},
                                  {'id': 'r3.6', 'q': 'Saturday and Sunday are the best days for special family time.', 't': 'tf'},
                                  {'id': 'r3.7', 'q': 'Wednesday is the day when we go to the park and have a picnic.', 't': 'tf'}],
                        'passage': '<h4>A Week of Fun</h4><p>Every week has seven days, and each day is different and exciting!</p><p>Monday is the start of '
                                   'the week. We wake up, eat a yummy breakfast, and get ready for a new adventure.</p><p>On Tuesday, we go to school and '
                                   'learn many interesting things. We study at school and have fun with our friends.</p><p>Wednesday is right in the middle of '
                                   "the week. It's a day to listen to music and enjoy some tunes that make us happy.</p><p>Thursday is when we continue our "
                                   "learning at school. We read stories, solve puzzles, and discover new things.</p><p>Finally, it's Friday! The last day of "
                                   'the school week. We are happy because the weekend is coming, and we can have more time to play and relax.</p><p>Saturday '
                                   'and Sunday are the best days. We can sleep in a little bit and have special family time. On these days, we might go to the '
                                   "park, have a picnic, or play games together.</p><p>Every day of the week is special, and it's a mix of learning, fun, and "
                                   'family time!</p>'},
                       {'id': 'r4',
                        'instr': 'Unit 4 – My birthday party: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r4.1',
                                   'o': ['Warm days', 'Love and exchanging cards', 'Outdoor activities'],
                                   'q': 'What is February known for?',
                                   't': 'mcq'},
                                  {'id': 'r4.2',
                                   'o': ['Celebrate birthdays', 'Have picnics under the sun', 'Enjoy nature as flowers bloom'],
                                   'q': 'What do people often do in March?',
                                   't': 'mcq'},
                                  {'id': 'r4.3',
                                   'o': ['A special day with cake, balloons, and laughter', 'A day for picnics', 'A month with cozy jackets'],
                                   'q': 'What is a birthday?',
                                   't': 'mcq'},
                                  {'id': 'r4.4', 'o': ['Flowers', 'Fruits', 'Chips'], 'q': 'What is jam made from?', 't': 'mcq'},
                                  {'id': 'r4.5', 'q': 'January is described as a month with warm days.', 't': 'tf'},
                                  {'id': 'r4.6', 'q': 'April is when people celebrate birthdays.', 't': 'tf'},
                                  {'id': 'r4.7', 'q': 'Chips are mentioned as a sweet treat in the passage.', 't': 'tf'},
                                  {'id': 'r4.8', 'q': 'Lemonade is described as tangy and perfect for a sunny day.', 't': 'tf'}],
                        'passage': "<h4>Fun Months and Yummy Treats</h4><p>In Vietnam, there are twelve months in a year, and each month is special. Let's "
                                   "talk about some of them!</p><p>January is when it's a bit chilly, and we wear cozy jackets. It's the start of the year, "
                                   "and we celebrate new beginnings.</p><p>February is extra special because it's the month of love. People exchange cards and "
                                   'gifts to show how much they care.</p><p>March is when the flowers start to bloom, and the world becomes colorful again. '
                                   "It's a lovely time to enjoy nature.</p><p>April brings warmer days, and we often have picnics under the sun. The grass is "
                                   "green, and the sky is blue.</p><p>May is when it gets a bit hot, and we start looking forward to the summer break. It's a "
                                   'time for fun and outdoor activities.</p><p>One exciting day for each person is their birthday! On our birthdays, we have a '
                                   "party with friends and family. There's cake, balloons, and lots of laughter.</p><p>When we feel a little hungry, we might "
                                   'snack on some tasty treats. Chips are crunchy and salty, and they make a great snack while watching cartoons.</p><p>For a '
                                   "sweet treat, we have jam. It's made from fruits, and we spread it on bread or crackers. Yum!</p><p>When it's hot outside, "
                                   'we love to sip on refreshing drinks. Juice is fruity and cool, while lemonade is tangy and perfect for a sunny '
                                   "day.</p><p>Of course, we also need to drink plenty of water to stay healthy. It's like giving our bodies a big, refreshing "
                                   'hug.</p>'},
                       {'id': 'r5',
                        'instr': 'Unit 5 – Things we can do: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r5.1',
                                   'o': ['Ride a bike', 'Play the piano', 'Cook with mom'],
                                   'q': 'What does the narrator do in the kitchen?',
                                   't': 'mcq'},
                                  {'id': 'r5.2', 'o': ['Can', 'But', 'Swim'], 'q': 'What does the narrator use to connect two ideas?', 't': 'mcq'},
                                  {'id': 'r5.3',
                                   'o': ['Ride a horse', 'Roller skate', 'Cook meals'],
                                   'q': 'What does the narrator do on sunny days around the neighborhood?',
                                   't': 'mcq'},
                                  {'id': 'r5.4', 'q': 'The narrator can ride a bike and feels like flying on wheels.', 't': 'tf'},
                                  {'id': 'r5.5', 'q': 'The narrator plays the piano with dad.', 't': 'tf'},
                                  {'id': 'r5.6', 'q': 'Roller skating is described as a splashy adventure in the pool.', 't': 'tf'},
                                  {'id': 'r5.7', 'q': 'The word "but" is used to connect two ideas in the passage.', 't': 'tf'}],
                        'passage': '<h4>Fun and Skills</h4><p>I am a little kid, and there are so many things I can do! I can ride a bike, and it feels like '
                                   'flying on wheels. Zoom, zoom!</p><p>In the kitchen, I watch my mom cook delicious meals. Sometimes, she lets me help stir '
                                   "and mix. It's like being a chef in our own home.</p><p>After dinner, I love to play the piano. I press the keys, and it "
                                   "makes beautiful music. It's like having a mini concert in our living room.</p><p>Another instrument I enjoy is the guitar. "
                                   'I like to play the guitar with my dad. We strum the strings and make happy tunes together.</p><p>On sunny days, I grab my '
                                   'roller skates, and off I go! I love to roller skate around the neighborhood, feeling the wind on my face.</p><p>When we '
                                   "visit the countryside, I get to ride a horse. It's a big, gentle animal, and it's so much fun going for a ride.</p><p>In "
                                   "the summer, my friends and I go to the pool, and we all swim together. It's a splashy adventure, and we pretend to be "
                                   "little fish.</p><p>Sometimes, I use the word but to connect two ideas. For example, I want to play outside, but it's "
                                   'raining. So, I find something fun to do indoors.</p><p>There are so many things I can do, and every day is full of '
                                   'exciting adventures!</p>'}],
            'id': 'doc-hieu',
            'mode': 'practice',
            'title': 'Đọc hiểu – Unit 1–5'},
           {'groups': [{'id': 'r6',
                        'instr': 'Unit 6 – Our school facilities: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r6.1',
                                   'o': ['Small and quiet', 'Big and busy with tall buildings', 'Covered with green trees'],
                                   'q': 'What is a city like?',
                                   't': 'mcq'},
                                  {'id': 'r6.2',
                                   'o': ['Tall peaks and climbing spots', 'Friendly neighbors and parks', 'Shops and restaurants'],
                                   'q': 'What can you find in a town?',
                                   't': 'mcq'},
                                  {'id': 'r6.3',
                                   'o': ['Smaller than a town, with fewer houses',
                                         'Bigger than a city, with tall buildings',
                                         'Busy with lots of cars and people'],
                                   'q': 'What is a village like?',
                                   't': 'mcq'},
                                  {'id': 'r6.4',
                                   'o': ['Learn how to use computers and play educational games',
                                         'Grow flowers and vegetables',
                                         'See beautiful views from tall peaks'],
                                   'q': 'What do you do in the computer room at school?',
                                   't': 'mcq'},
                                  {'id': 'r6.5', 'q': 'Mountains are covered with green trees.', 't': 'tf'},
                                  {'id': 'r6.6', 'q': 'Villages have many shops and restaurants.', 't': 'tf'},
                                  {'id': 'r6.7', 'q': 'The computer room at school is where you play with swings and slides.', 't': 'tf'},
                                  {'id': 'r6.8', 'q': 'Gardens are places where you can enjoy nature and grow flowers or vegetables.', 't': 'tf'}],
                        'passage': '<h4>Places Around Us</h4><p>In Vietnam, there are many different places that are fun to explore. One type of place is the '
                                   'city. Cities are big and busy with tall buildings, cars, and lots of people. People in the city go to work, and there are '
                                   'many shops and restaurants.</p><p>Another type of place is the mountains. Mountains are huge and have tall peaks. They are '
                                   'covered with green trees, and some people love to climb them to see the beautiful views.</p><p>A town is a smaller place '
                                   'than a city. It has houses, schools, and parks. Towns are not as busy as cities, and you can often find friendly neighbors '
                                   'who say hello.</p><p>A village is even smaller than a town. Villages have fewer houses, and everyone knows each other. '
                                   'Sometimes, you might see animals like chickens and cows in a village.</p><p>At school, we have a special room called the '
                                   "computer room. In the computer room, we learn how to use computers and play educational games. It's a cool place to "
                                   'discover new things on the screen!</p><p>In our homes, we might have a little garden where we grow flowers or vegetables. '
                                   'Gardens are colorful and peaceful places where we can enjoy nature.</p><p>Lastly, we have a place called the playground. '
                                   "Playgrounds are filled with swings, slides, and fun things to play on. It's a happy place where we can run, jump, and have "
                                   'lots of fun with our friends.</p>'},
                       {'id': 'r7',
                        'instr': 'Unit 7 – Our timetables: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r7.1',
                                   'o': ['Play with numbers', 'Use colors and shapes to make drawings', 'Explore nature'],
                                   'q': 'What do we do in art class?',
                                   't': 'mcq'},
                                  {'id': 'r7.2',
                                   'o': ['Count numbers', 'Read and speak in a different language', 'Create beautiful drawings'],
                                   'q': 'In English class, what do we learn to do?',
                                   't': 'mcq'},
                                  {'id': 'r7.3',
                                   'o': ['Learning about numbers', 'Discovering the past and different places', 'Playing with blocks'],
                                   'q': 'What is history and geography about?',
                                   't': 'mcq'},
                                  {'id': 'r7.4',
                                   'o': ['Using colors and shapes', 'Exploring nature', 'Numbers and counting'],
                                   'q': 'What is maths all about?',
                                   't': 'mcq'},
                                  {'id': 'r7.5', 'q': 'In art class, we play simple instruments.', 't': 'tf'},
                                  {'id': 'r7.6', 'q': 'In music class, we listen to melodies and enjoy the rhythm.', 't': 'tf'},
                                  {'id': 'r7.7', 'q': 'In science, we learn about plants, animals, and the stars.', 't': 'tf'},
                                  {'id': 'r7.8', 'q': 'Vietnamese class is about learning a different language.', 't': 'tf'}],
                        'passage': '<h4>My School Subjects</h4><p>I go to school to learn many interesting things. One subject is art, where we use colors and '
                                   'shapes to create beautiful drawings. I love making pictures of animals and trees.</p><p>In English class, we learn to read '
                                   "and speak in a different language. It's like discovering a whole new world of words! The teacher helps us say sentences "
                                   'and tell stories in English.</p><p>Another subject is history and geography. We learn about the past and different places '
                                   "on the map. It's exciting to know about ancient times and faraway lands.</p><p>Maths is all about numbers and counting. We "
                                   "play with blocks and solve puzzles to become little math wizards. It's like a fun game with numbers!</p><p>In music class, "
                                   'we listen to melodies and sometimes play simple instruments. We sing along and enjoy the rhythm. Music makes us '
                                   'happy!</p><p>Science is a subject where we explore the wonders of nature. We look at plants, animals, and learn about the '
                                   "stars in the sky. It's like being a little scientist discovering the world.</p><p>Lastly, we have Vietnamese class where "
                                   "we learn to read and write in our own language. It's important to know about our culture and speak our language with "
                                   'pride.</p>'},
                       {'id': 'r8',
                        'instr': 'Unit 8 – My favourite subjects: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r8.1',
                                   'o': ['How to run and jump', 'How to use computers and technology', 'How to speak English'],
                                   'q': 'What do we learn in IT (information technology)?',
                                   't': 'mcq'},
                                  {'id': 'r8.2',
                                   'o': ['Learning to type', 'Moving and playing games', 'Solving puzzles'],
                                   'q': 'What is PE (physical education) all about?',
                                   't': 'mcq'},
                                  {'id': 'r8.3',
                                   'o': ['Maths teacher', 'IT teacher', 'English teacher'],
                                   'q': 'Who teaches us how to say words in English?',
                                   't': 'mcq'},
                                  {'id': 'r8.4', 'q': 'In PE, we learn how to use computers.', 't': 'tf'},
                                  {'id': 'r8.5', 'q': 'The maths teacher helps us count numbers and solve puzzles.', 't': 'tf'},
                                  {'id': 'r8.6', 'q': 'The passage mentions the word "why" as a way to ask about the reason for something.', 't': 'tf'},
                                  {'id': 'r8.7', 'q': 'The IT teacher teaches us how to speak English.', 't': 'tf'}],
                        'passage': '<h4>Fun School Days</h4><p>At school, we have different subjects to learn. One of them is IT (information technology), '
                                   "where we use computers and learn cool things about technology. The teacher shows us how to click and type, and it's like a "
                                   'fun game.</p><p>We also have PE (physical education), which is all about moving and playing games. We run, jump, and '
                                   'sometimes even play with colorful balls. PE is our time to be active and have fun.</p><p>In our classroom, we have special '
                                   'teachers. The English teacher teaches us how to say words in English, and we practice talking in a new language. The maths '
                                   'teacher helps us solve puzzles and count numbers. They make learning fun!</p><p>Sometimes, we ask why things are the way '
                                   'they are. When we want to know the reason, we use the word because. For example, if we ask, "Why is the sky blue?" we '
                                   'might hear, "Because the sunlight scatters in the air, making it look blue."</p>'},
                       {'id': 'r9',
                        'instr': 'Unit 9 – Our sports day: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r9.1',
                                   'o': ['July', 'June', 'August'],
                                   'q': 'What month is it when the weather is warm, and we wear shorts?',
                                   't': 'mcq'},
                                  {'id': 'r9.2',
                                   'o': ['October', 'November', 'December'],
                                   'q': 'In which month do the leaves on trees change colors?',
                                   't': 'mcq'},
                                  {'id': 'r9.3', 'o': ['June', 'November', 'December'], 'q': 'When is sports day usually celebrated in school?', 't': 'mcq'},
                                  {'id': 'r9.4',
                                   'o': ['Winter jackets', 'Sports clothes', 'School uniforms'],
                                   'q': 'What do we wear on sports day?',
                                   't': 'mcq'},
                                  {'id': 'r9.5', 'q': "In August, it's the perfect time for snow.", 't': 'tf'},
                                  {'id': 'r9.6', 'q': 'The leaves on trees change colors in December.', 't': 'tf'},
                                  {'id': 'r9.7', 'q': 'Sports day is a day where we play games and run races with friends.', 't': 'tf'}],
                        'passage': "<h4>Fun Months and Sports Day</h4><p>In Vietnam, we have many months in a year. There's June, when the weather is warm, "
                                   'and we wear our favorite shorts. Then comes July, where the sun shines brightly, and we sometimes play in the water to '
                                   "stay cool. After that is August, and it's the perfect time for yummy ice cream.</p><p>As we move to September, the air "
                                   'starts feeling a little cooler, and we might wear light jackets. In October, the leaves on trees change colors, and it '
                                   'looks like a beautiful painting. November brings even cooler days, and we might see some rain. Finally, in December, '
                                   "there's a festive feeling in the air as we get ready for the holidays.</p><p>One special day in school is called sports "
                                   'day. It usually happens in November, and we get to play fun games and run races with our friends. We wear sports clothes '
                                   "and cheer for our classmates. It's a day full of laughter and happy moments.</p>"},
                       {'id': 'r10',
                        'instr': 'Unit 10 – Our summer holidays: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r10.1',
                                   'o': ['Campsite', 'Countryside', 'Beach'],
                                   'q': 'Where did the family play with sand and splash in the water?',
                                   't': 'mcq'},
                                  {'id': 'r10.2',
                                   'o': ['Set up a tent and told stories', 'Climbed a big bridge', 'Ate yummy sushi'],
                                   'q': 'What did the family do at the campsite?',
                                   't': 'mcq'},
                                  {'id': 'r10.3', 'o': ['Tokyo', 'Sydney', 'Bangkok'], 'q': 'In which city did the family ride in a tuk-tuk?', 't': 'mcq'},
                                  {'id': 'r10.4',
                                   'o': ['Sydney Harbour Bridge', 'Tall buildings', 'Shrines'],
                                   'q': 'What did the family climb in Sydney?',
                                   't': 'mcq'},
                                  {'id': 'r10.5',
                                   'o': ['Dancing robots', 'Soft sand', 'Quiet countryside'],
                                   'q': 'What did the family see in Tokyo?',
                                   't': 'mcq'},
                                  {'id': 'r10.6', 'q': 'The beach had hard sand.', 't': 'tf'},
                                  {'id': 'r10.7', 'q': 'The family had a fire at the campsite.', 't': 'tf'},
                                  {'id': 'r10.8', 'q': 'In Sydney, the family climbed tall buildings.', 't': 'tf'},
                                  {'id': 'r10.9', 'q': 'Tokyo is described as a city with old and new things.', 't': 'tf'},
                                  {'id': 'r10.10', 'q': 'Each place the family visited was special.', 't': 'tf'}],
                        'passage': '<h4>Our Fun Trip</h4><p>Yesterday, my family and I had a fun trip. First, we went to a nice beach. The sand was soft, and '
                                   'the water made a happy sound. We played with sand and splashed in the water. It was so much fun!</p><p>After the beach, we '
                                   'went to a quiet place called a campsite in the countryside. We set up a tent and told stories. We even had a fire to make '
                                   'yummy marshmallows. It was a special night.</p><p>Today, we visited big cities. We went to Bangkok with tall buildings and '
                                   'yummy food. We rode in a tuk-tuk and had so much fun. Then, we flew to Sydney and saw big things like the Opera House. We '
                                   "climbed a big bridge, and the view was amazing.</p><p>Our last stop is Tokyo. It's a cool city with old and new things. We "
                                   'went to shrines, ate yummy sushi, and saw robots dancing. Each place was different, but they were all special.</p>'}],
            'id': 'doc-hieu-2',
            'mode': 'practice',
            'title': 'Đọc hiểu – Unit 6–10'},
           {'groups': [{'id': 'r11',
                        'instr': 'Unit 11 – My home: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r11.1',
                                   'o': ['On the road', 'At the end of the street', 'In the city'],
                                   'q': 'Where does the narrator catch the school bus?',
                                   't': 'mcq'},
                                  {'id': 'r11.2',
                                   'o': ['Small and dull', 'Big and colorful', 'Busy and noisy'],
                                   'q': 'How are the houses on Happy Street described?',
                                   't': 'mcq'},
                                  {'id': 'r11.3',
                                   'o': ['Busy noises', 'Birds singing', 'Laughter and joy'],
                                   'q': 'What does the narrator hear in the morning on Happy Street?',
                                   't': 'mcq'},
                                  {'id': 'r11.4',
                                   'o': ['Ride bikes and draw chalk pictures', 'Make a lot of noise', 'Play quiet games indoors'],
                                   'q': 'What do the narrator and their friends do on the street?',
                                   't': 'mcq'},
                                  {'id': 'r11.5',
                                   'o': ['Noisy and busy', 'Calm and peaceful', 'Colorful and chaotic'],
                                   'q': 'What is Happy Street like on the weekends?',
                                   't': 'mcq'},
                                  {'id': 'r11.6', 'q': "The narrator's house is on a busy street.", 't': 'tf'},
                                  {'id': 'r11.7', 'q': 'Happy Street is noisy in the morning.', 't': 'tf'},
                                  {'id': 'r11.8', 'q': 'The narrator and their friends sometimes draw chalk pictures on the pavement.', 't': 'tf'},
                                  {'id': 'r11.9', 'q': 'The houses on Happy Street have dull gardens.', 't': 'tf'},
                                  {'id': 'r11.10', 'q': "The narrator feels lucky to live on Happy Street because it's calm and peaceful.", 't': 'tf'}],
                        'passage': '<h4>My Home on Happy Street</h4><p>I live on Happy Street, a cheerful and colorful place. Our house is on a quiet road, '
                                   'away from the busy noises of the city. The houses on Happy Street are big and have bright colors that make me smile every '
                                   'day.</p><p>In the morning, I walk to the end of the street to catch the school bus. Happy Street is always quiet in the '
                                   "morning, and I can hear birds singing in the trees. It's a peaceful start to my day.</p><p>After school, my friends and I "
                                   'play games on the street. Sometimes, we ride our bikes, and other times, we draw colorful chalk pictures on the pavement. '
                                   "Happy Street is never noisy; instead, it's filled with laughter and joy.</p><p>On the weekends, my family and I go for a "
                                   'walk down our road. We enjoy the fresh air and talk about our week. The houses on Happy Street have pretty gardens, and '
                                   'sometimes we see neighbors planting flowers or watering their plants.</p><p>I feel lucky to live on Happy Street because '
                                   "it's not only a place with big houses but also a place where everything is calm and peaceful.</p>"},
                       {'id': 'r12',
                        'instr': 'Unit 12 – Jobs: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r12.1', 'o': ['John', 'Sarah', 'Emily', 'Mark'], 'q': 'Who grows tasty fruits and veggies on the farm?', 't': 'mcq'},
                                  {'id': 'r12.2', 'o': ['John', 'Sarah', 'Emily', 'Mark'], 'q': 'Who helps sick people in the hospital?', 't': 'mcq'},
                                  {'id': 'r12.3',
                                   'o': ['Acts in movies', 'Grows fruits and veggies', 'Helps people in the hospital', 'Keeps everyone safe as a policeman'],
                                   'q': 'What does Alex, the friendly person, do in the town?',
                                   't': 'mcq'},
                                  {'id': 'r12.4',
                                   'o': ['Nursing home', 'Factory', 'Hospital', 'City office'],
                                   'q': 'Where does Mark do his important job with papers?',
                                   't': 'mcq'},
                                  {'id': 'r12.5',
                                   'o': ['Tasty fruits and veggies', 'Fun toys for kids', 'Movies', 'Important papers'],
                                   'q': 'What do the workers in the factory make?',
                                   't': 'mcq'}],
                        'passage': '<p>Once upon a time in a little town, there were friends with cool jobs. John was like a superhero in movies, making '
                                   'people happy. Sarah worked on a farm, growing tasty fruits and veggies. Emily was like a doctor, helping sick people in '
                                   'the hospital. Mark had an office job in the city, doing important papers.</p><p>One day, there was a small problem, and '
                                   'Alex, the friendly policeman, came to help and keep everyone safe. In a big factory, workers made fun toys for kids to '
                                   'play with.</p><p>As the town grew, they made a cozy home for older friends called a nursing home, where they could be '
                                   'happy. Everyone in the town had a special job to make it a fantastic place!</p>'},
                       {'id': 'r13',
                        'instr': 'Unit 13 – Appearance: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r13.1',
                                   'o': ['Big and bright', 'Small and dark', 'Round and dull'],
                                   'q': "What did the girl's eyes look like?",
                                   't': 'mcq'},
                                  {'id': 'r13.2', 'o': ['Long', 'Short', 'Slim'], 'q': "How did the girl's arms appear?", 't': 'mcq'},
                                  {'id': 'r13.3',
                                   'o': ['Her big smile', 'Her round face', 'Her tall stature'],
                                   'q': 'What made everyone around her happy?',
                                   't': 'mcq'},
                                  {'id': 'r13.4',
                                   'o': ['They were the same height.', 'The narrator was tall.', 'The new friend was tall.'],
                                   'q': 'What did the narrator notice about their height compared to the new friend?',
                                   't': 'mcq'},
                                  {'id': 'r13.5', 'q': 'The new friend had short, straight hair.', 't': 'tf'},
                                  {'id': 'r13.6', 'q': "The girl's laugh echoed through the air.", 't': 'tf'},
                                  {'id': 'r13.7', 'q': "The narrator and the new friend couldn't be friends because they were different.", 't': 'tf'},
                                  {'id': 'r13.8', 'q': 'The important thing for the narrator was having fun and being kind to each other.', 't': 'tf'}],
                        'passage': '<h4>My New Friend</h4><p>One sunny day, I went to the playground to play with my friends. As I arrived, I saw a girl with '
                                   'big, bright eyes and a round face. She had short, curly hair that bounced when she ran. I thought she looked friendly, so '
                                   'I decided to go and say hi.</p><p>When I reached her, I noticed she was a bit tall for her age, and her arms were long '
                                   'when she reached out to shake my hand. I introduced myself, and she smiled, showing her slim fingers.</p><p>We played '
                                   'together for a while, and I learned more about my new friend. She liked to run and jump, and she had a laugh that echoed '
                                   'through the air. Her big smile made everyone around her happy.</p><p>As we played, I realized that even though we were '
                                   "different – she was tall, and I was short – we could still be great friends. It didn't matter if our hair was curly or "
                                   'straight, or if our eyes were big or small. What mattered most was having fun and being kind to each other.</p>'},
                       {'id': 'r14',
                        'instr': 'Unit 14 – Daily activities: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r14.1',
                                   'o': ['Vacuum cleaner', 'Broom and dustpan', 'Mop'],
                                   'q': 'What did they use to clean the floor?',
                                   't': 'mcq'},
                                  {'id': 'r14.2',
                                   'o': ['Cook dinner', 'Wash the clothes', 'Clean the floor'],
                                   'q': 'What did the narrator help with in the laundry area?',
                                   't': 'mcq'},
                                  {'id': 'r14.3', 'o': ['Morning', 'Afternoon', 'Evening'], 'q': 'When did they sit down to rest and talk?', 't': 'mcq'},
                                  {'id': 'r14.4', 'q': 'The narrator helped Mom wash the dishes in the morning.', 't': 'tf'},
                                  {'id': 'r14.5', 'q': 'Bubbles made the dishes clean, and the narrator played with the soapy water.', 't': 'tf'},
                                  {'id': 'r14.6', 'q': 'The narrator used a mop to clean the floor.', 't': 'tf'},
                                  {'id': 'r14.7', 'q': 'Mom and the narrator washed the clothes in the evening.', 't': 'tf'},
                                  {'id': 'r14.8', 'q': 'The narrator felt sad after doing chores with Mom.', 't': 'tf'}],
                        'passage': '<h4>Fun Chores with Mom</h4><p>In the morning, I woke up, and the sun was shining in the sky. Mom and I decided to do some '
                                   'fun chores together. First, we went to the kitchen, and I helped Mom wash the dishes. Bubbles made the dishes all clean, '
                                   'and I giggled as I played with the soapy water.</p><p>After we finished, Mom said, "Let\'s make our home even more '
                                   'sparkly!" So, we grabbed a broom and a dustpan to clean the floor. We danced around, sweeping away the dust, and it felt '
                                   'like a little party in our living room.</p><p>In the afternoon, we took a break to have lunch, and then we decided to do '
                                   'more chores. Mom showed me how to help with the cooking. I got to mix ingredients and flip pancakes. The smell of yummy '
                                   'food filled our kitchen.</p><p>As the day went on, we had more things to do. Mom gathered the clothes, and we went to the '
                                   'laundry area to wash the clothes. I helped put them in the machine, and Mom pressed the buttons. The machine made a funny '
                                   'sound, and I laughed.</p><p>By the time the evening came, we had done lots of things together. Mom and I sat down to rest, '
                                   'and she said, "Thank you for helping me today." I felt happy because doing chores with Mom was like having a little '
                                   'adventure at home.</p>'},
                       {'id': 'r15',
                        'instr': 'Unit 15 – My family’s weekends: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r15.1',
                                   'o': ['Sports centre', 'Cinema', 'Shopping centre'],
                                   'q': 'Where did the family go first on their fun day out?',
                                   't': 'mcq'},
                                  {'id': 'r15.2',
                                   'o': ['Cook meals', 'Play tennis', 'Do yoga'],
                                   'q': 'What activity did Mom and Dad do at the sports centre?',
                                   't': 'mcq'},
                                  {'id': 'r15.3',
                                   'o': ['Cooking meals', 'Playing tennis', 'Swimming in the pool'],
                                   'q': 'How did the family cool off on the warm day?',
                                   't': 'mcq'},
                                  {'id': 'r15.4',
                                   'o': ['Watch films', 'Cook meals', 'Do yoga'],
                                   'q': 'What did the family do to relax in the afternoon?',
                                   't': 'mcq'},
                                  {'id': 'r15.5', 'q': 'The family watched a short movie at the shopping centre.', 't': 'tf'},
                                  {'id': 'r15.6', 'q': 'Mom and Dad played tennis at the swimming pool.', 't': 'tf'},
                                  {'id': 'r15.7', 'q': 'The family did yoga to relax in the afternoon.', 't': 'tf'},
                                  {'id': 'r15.8', 'q': 'The family ended their day by going to the shopping centre.', 't': 'tf'},
                                  {'id': 'r15.9', 'q': 'The family returned home with frowns on their faces.', 't': 'tf'}],
                        'passage': '<h4>A Fun Day Out</h4><p>One sunny day, my family and I planned a fun day out. We started by going to the big shopping '
                                   'centre in the middle of the city. It was filled with stores selling toys, clothes, and tasty snacks. We even had the '
                                   'chance to watch a short movie at the cinema inside the shopping centre.</p><p>After exploring the shopping centre, we '
                                   'decided to head to the nearby sports centre. There, we found a variety of activities to try. Mom and Dad played a friendly '
                                   "game of tennis while my sister and I enjoyed playing in the kids' area.</p><p>Feeling energized, we made our way to the "
                                   'swimming pool. The cool water was inviting, and we had a blast splashing around and playing games. It was a perfect way to '
                                   'cool off on a warm day.</p><p>As the afternoon sun began to set, we wanted to do something relaxing. Mom suggested we go '
                                   "to a place where we could do yoga. We found a cozy spot, and with Mom's guidance, we stretched and posed in different "
                                   'ways. It was a peaceful and calming experience.</p><p>After our yoga session, we decided to end our day by going back to '
                                   'the cinema to watch films. We picked a funny animated movie and enjoyed popcorn while laughing at the silly characters on '
                                   'the big screen.</p><p>It was a fantastic day filled with shopping, sports, swimming, yoga, and movies. We returned home '
                                   'with smiles on our faces, looking forward to more family adventures.</p>'}],
            'id': 'doc-hieu-3',
            'mode': 'practice',
            'title': 'Đọc hiểu – Unit 11–15'},
           {'groups': [{'id': 'r16',
                        'instr': 'Unit 16 – Weather: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r16.1',
                                   'o': ['Bakery', 'Weather', 'Supermarket'],
                                   'q': 'What was the first thing the friends checked in the morning?',
                                   't': 'mcq'},
                                  {'id': 'r16.2',
                                   'o': ['It was windy outside.', 'They wanted to buy fresh bread.', 'The weather became rainy.'],
                                   'q': 'Why did the friends stop at the bakery?',
                                   't': 'mcq'},
                                  {'id': 'r16.3',
                                   'o': ['Fresh bread', 'Toys', 'Fruits and vegetables'],
                                   'q': 'What did the friends buy at the supermarket?',
                                   't': 'mcq'},
                                  {'id': 'r16.4', 'o': ['Water park', 'Bakery', 'Supermarket'], 'q': 'Where did the friends go to cool off?', 't': 'mcq'},
                                  {'id': 'r16.5',
                                   'o': ['Played in the water park', 'Visited a bookshop', 'Ran to a food stall'],
                                   'q': 'What did they do when it started raining?',
                                   't': 'mcq'},
                                  {'id': 'r16.6', 'q': 'The friends woke up to a cloudy day.', 't': 'tf'},
                                  {'id': 'r16.7', 'q': 'The bakery had the smell of fresh bread.', 't': 'tf'},
                                  {'id': 'r16.8', 'q': 'The friends went to the water park when it became windy.', 't': 'tf'},
                                  {'id': 'r16.9', 'q': 'The friends ran to a food stall to escape the rain.', 't': 'tf'},
                                  {'id': 'r16.10',
                                   'q': 'Despite the rain, the day out with friends was filled with laughter and exciting adventures.',
                                   't': 'tf'}],
                        'passage': '<h4>A Day Out with Friends</h4><p>One weekend, my friends and I planned a day out in our neighborhood. We woke up early, '
                                   'and the first thing we did was look outside to check the weather. The sky was clear, and the sun was shining, so we knew '
                                   'it was going to be a sunny day.</p><p>Excitedly, we decided to start our adventure by going to the local supermarket. On '
                                   'the way there, we passed by a delightful bakery with the sweet aroma of fresh bread. Even though we were eager to reach '
                                   "the supermarket, we couldn't resist stopping by to buy some tasty pastries.</p><p>After filling our bags with snacks, we "
                                   'continued on our journey to the supermarket. Once there, we explored the aisles, picking out fruits, vegetables, and other '
                                   'goodies for a picnic later.</p><p>As we left the supermarket, we noticed the sky becoming a bit cloudy. Despite the change '
                                   'in the weather, we were determined to make the most of our day. We decided to visit the nearby water park to cool '
                                   'off.</p><p>At the water park, we splashed and played in the refreshing water. Suddenly, the wind picked up, making it a '
                                   "bit windy. We didn't mind, though – it added more fun to our water adventures.</p><p>Later in the day, we visited a small "
                                   'bookshop to find a story to read. As we left the bookshop, we felt a few raindrops. It was becoming rainy! We quickly ran '
                                   'to a cozy food stall to enjoy some warm noodles while the rain fell outside.</p><p>Despite the unexpected rain, our day '
                                   'out with friends was filled with laughter, delicious treats, and exciting adventures.</p>'},
                       {'id': 'r17',
                        'instr': 'Unit 17 – In the city: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r17.1', 'o': ['Turn left', 'Go straight', 'Turn right'], 'q': 'How did the friends get to the park?', 't': 'mcq'},
                                  {'id': 'r17.2', 'o': ['Turn left', 'Turn round', 'Turn right'], 'q': 'How did they reach the pond?', 't': 'mcq'},
                                  {'id': 'r17.3',
                                   'o': ['Turn round', 'Turn left', 'Turn right'],
                                   'q': 'What did Mom tell them to do when it was time to go home?',
                                   't': 'mcq'},
                                  {'id': 'r17.4', 'q': 'The friends had to turn right at the big tree to reach the park.', 't': 'tf'},
                                  {'id': 'r17.5', 'q': 'The sign on the path said, "Go straight to the Ice Cream Shop!"', 't': 'tf'},
                                  {'id': 'r17.6', 'q': 'The playground was on the path after turning left.', 't': 'tf'},
                                  {'id': 'r17.7', 'q': 'The pond was located after turning left at the end of the path.', 't': 'tf'}],
                        'passage': '<h4>A Day in the Park</h4><p>One sunny afternoon, my friends and I decided to go to the park to play. To get there, we had '
                                   'to walk from our house. Mom told us to go straight until we reached the big tree, then we needed to turn left.</p><p>As we '
                                   'walked, we saw a funny sign that said, "Ice Cream Shop to the left!" We giggled and thought about having ice cream later. '
                                   "Continuing on, we reached the big tree, and Mom's instructions were clear - it was time to turn left.</p><p>Now, we were "
                                   'on a new path surrounded by beautiful flowers. We walked and skipped, feeling excited about our adventure. Suddenly, we '
                                   'saw a big playground up ahead. Mom had told us that the park was just straight ahead after turning left.</p><p>At the '
                                   'playground, we played on the swings, the slide, and climbed on the jungle gym. After having so much fun, we decided to '
                                   'explore more. Mom had said that if we wanted to go to the pond, we should turn right at the end of the '
                                   "path.</p><p>Following Mom's advice, we turned right and found a lovely pond with ducks swimming. We fed the ducks and "
                                   'enjoyed the peaceful scene. When it was time to go home, Mom told us to turn round and go back the way we came.</p><p>Our '
                                   "day in the park was full of adventures, and we were happy to have found our way around with Mom's directions.</p>"},
                       {'id': 'r18',
                        'instr': 'Unit 18 – At the shopping centre: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm '
                                 'bài.)',
                        'items': [{'id': 'r18.1',
                                   'o': ['Behind the entrance', 'Near the entrance', 'Opposite the entrance'],
                                   'q': 'Where was the gift shop located in the market?',
                                   't': 'mcq'},
                                  {'id': 'r18.2',
                                   'o': ['Near the apples', 'Between two other skirts', 'Opposite the entrance'],
                                   'q': 'Where did the family find the skirt?',
                                   't': 'mcq'},
                                  {'id': 'r18.3',
                                   'o': ['Behind the fish section', 'Near the apples', 'Opposite the entrance'],
                                   'q': 'Where did the family find the ripe bananas?',
                                   't': 'mcq'},
                                  {'id': 'r18.4',
                                   'o': ['Near the shoe shop', 'Behind the fish and meat section', 'Opposite the entrance'],
                                   'q': 'Where was the rice stall located?',
                                   't': 'mcq'},
                                  {'id': 'r18.5',
                                   'o': ['Between the shoe shop and the hat shop', 'Behind the fish section', 'Opposite the entrance'],
                                   'q': 'Where did the family find the T-shirt?',
                                   't': 'mcq'},
                                  {'id': 'r18.6', 'q': 'The skirt was displayed between two other skirts.', 't': 'tf'},
                                  {'id': 'r18.7', 'q': 'The T-shirt stall was opposite the shoe shop.', 't': 'tf'},
                                  {'id': 'r18.8', 'q': 'The family found ripe bananas near the fish section.', 't': 'tf'}],
                        'passage': '<h4>A Day at the Market</h4><p>One sunny morning, my family and I went to the market to buy some things. The market was a '
                                   'busy place with stalls selling fruits, vegetables, and clothes. As we walked in, we saw a colorful gift shop filled with '
                                   'toys and candies. It was right opposite the entrance.</p><p>Our first stop was the clothing section. I found a lovely pink '
                                   'skirt that I wanted to wear for a special occasion. The skirt was displayed on a rack between two other skirts of '
                                   'different colors. Mom bought it for me, and I was so happy!</p><p>Next, we went to the food section where there were '
                                   'fruits and vegetables. I saw a bunch of ripe bananas near the apples. Mom decided to buy both for a delicious fruit '
                                   'salad.</p><p>Dad needed to buy some rice, so we went to the rice stall. The rice stall was behind the fish and meat '
                                   'section. Dad chose a big bag of rice, and we also got some fresh fish for dinner.</p><p>At the end of our shopping trip, '
                                   'we found a small stall selling T-shirts. It was between the shoe shop and the hat shop. I liked a green T-shirt with a '
                                   'funny cartoon on it. Mom bought it for me as a surprise.</p><p>It was a fun day at the market, and we found everything we '
                                   'needed!</p>'},
                       {'id': 'r19',
                        'instr': 'Unit 19 – The animal world: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r19.1', 'o': ['Lion', 'Giraffe', 'Hippo'], 'q': 'What animal did the family see with a long neck?', 't': 'mcq'},
                                  {'id': 'r19.2', 'o': ['Roar', 'Sing', 'Dance'], 'q': 'What sound did the lion make in the zoo?', 't': 'mcq'},
                                  {'id': 'r19.3', 'o': ['In a tree', 'Near the water', 'On a rock'], 'q': 'Where did the crocodile like to sit?', 't': 'mcq'},
                                  {'id': 'r19.4', 'o': ['Slowly', 'Quickly', 'Merrily'], 'q': 'How did the hippo swim in the water?', 't': 'mcq'},
                                  {'id': 'r19.5',
                                   'o': ['Roar', 'Dance', 'Sing'],
                                   'q': 'What did the monkey and parrot do together in the special area?',
                                   't': 'mcq'},
                                  {'id': 'r19.6', 'q': 'The giraffe had short legs and a short neck.', 't': 'tf'},
                                  {'id': 'r19.7', 'q': 'The lion in the zoo danced with the parrot.', 't': 'tf'},
                                  {'id': 'r19.8', 'q': 'The crocodile made a soft roar near the water.', 't': 'tf'},
                                  {'id': 'r19.9', 'q': 'The hippo walked around the zoo.', 't': 'tf'},
                                  {'id': 'r19.10', 'q': "The birds in the bird section were silent and didn't sing.", 't': 'tf'}],
                        'passage': '<h4>A Day at the Zoo</h4><p>One sunny day, my family and I visited the zoo to see many animals. We saw a big, tall giraffe '
                                   'with a long neck. It walked merrily and looked at us with its big eyes. Next, we saw a lion in a cage. The lion made a '
                                   'loud roar, and we all giggled.</p><p>Nearby, there was a pond with a lazy crocodile inside. The crocodile liked to sit '
                                   'near the water and roar softly. We saw a playful hippo splashing in the water. It made us laugh as it swam '
                                   'quickly.</p><p>In the zoo, there was a special area where animals could dance. We watched a monkey and a parrot dancing '
                                   'together, moving beautifully to the music. It was so much fun!</p><p>Before leaving the zoo, we visited the bird section. '
                                   'Some birds liked to sing loudly, making the place lively. We imitated the birds and sang along merrily.</p>'}],
            'id': 'doc-hieu-4',
            'mode': 'practice',
            'title': 'Đọc hiểu – Unit 16–19'},
           {'groups': [{'id': 'r20',
                        'instr': 'Unit 20 – At summer camp: Read the passage, then choose the correct answer / True or False. (Đọc đoạn văn và làm bài.)',
                        'items': [{'id': 'r20.1',
                                   'o': ['Build a campfire', 'Put up a tent', 'Take a photo'],
                                   'q': 'What did the family set up first at the campsite?',
                                   't': 'mcq'},
                                  {'id': 'r20.2',
                                   'o': ['Sing songs', 'Build a campfire', 'Play card games'],
                                   'q': 'What did they do after putting up the tent?',
                                   't': 'mcq'},
                                  {'id': 'r20.3',
                                   'o': ['Take a photo', 'Tell stories', 'Play card games'],
                                   'q': 'What did they do around the campfire at night?',
                                   't': 'mcq'},
                                  {'id': 'r20.4',
                                   'o': ['Telling stories', 'Building a campfire', 'Singing songs'],
                                   'q': 'How did they add joy to the camping experience?',
                                   't': 'mcq'},
                                  {'id': 'r20.5',
                                   'o': ['Play card games', 'Take a photo', 'Build a campfire'],
                                   'q': 'What did they do inside the tent before going to bed?',
                                   't': 'mcq'},
                                  {'id': 'r20.6', 'q': 'The family went on a camping adventure in the city.', 't': 'tf'},
                                  {'id': 'r20.7', 'q': 'Setting up the tent was a bit tricky, but they managed to do it with teamwork.', 't': 'tf'},
                                  {'id': 'r20.8', 'q': "They made delicious s'mores by roasting marshmallows over the campfire.", 't': 'tf'},
                                  {'id': 'r20.9', 'q': 'The family woke up to the sound of birds chirping in the morning.', 't': 'tf'}],
                        'passage': '<h4>A Fun Camping Adventure</h4><p>One sunny day, my family and I decided to go on a camping adventure in the beautiful '
                                   'countryside. We packed our bags with everything we needed - a tent, sleeping bags, snacks, and more. As we arrived at the '
                                   'campsite, we saw a perfect spot near a sparkling river.</p><p>First, we decided to put up a tent. It was a bit tricky, but '
                                   'with teamwork, we managed to set it up. Inside the tent, we arranged our sleeping bags and pillows, creating a cozy space '
                                   'for the night.</p><p>After setting up the tent, it was time to have some fun. We gathered around and started to build a '
                                   'campfire. Dad taught us how to arrange the logs and light the fire safely. Once the flames flickered, we roasted '
                                   "marshmallows and made delicious s'mores.</p><p>As the night sky covered us with a blanket of stars, we sat around the "
                                   'campfire and told stories. Each family member took turns sharing exciting tales. The crackling fire added a magical touch '
                                   'to our storytelling.</p><p>To add more joy to our camping experience, we decided to sing songs. Mom played the guitar, and '
                                   'we sang our favorite tunes. The sound of laughter and music echoed through the peaceful night.</p><p>Before heading to '
                                   'bed, we played card games inside the tent. The soft glow of our lanterns illuminated the cards, and we giggled as we tried '
                                   'to outsmart each other in the games.</p><p>In the morning, we woke up to the sound of birds chirping and the fresh scent '
                                   'of nature. We decided to capture the memories by taking a family photo. We set up the camera, posed with big smiles, and '
                                   'took a photo to remember our wonderful camping adventure.</p><p>Our camping trip was filled with laughter, stories, and '
                                   'new experiences. It was a day of building memories that we would cherish forever.</p>'}],
            'id': 'doc-hieu-5',
            'mode': 'practice',
            'title': 'Đọc hiểu – Unit 20'}],
 'theory': '<h3>Từ vựng theo Unit (HSG – Bài tập bồi dưỡng)</h3><h3>Unit 1: My friends</h3><table class="tb"><tr><td><b>America (n)</b></td><td>nước Hoa '
           'Kì</td></tr><tr><td><b>Australia (n)</b></td><td>nước Ô-xtơ-rây-li-a</td></tr><tr><td><b>Britain (n)</b></td><td>nước '
           'Anh</td></tr><tr><td><b>Japan (n)</b></td><td>nước Nhật</td></tr><tr><td><b>Malaysia (n)</b></td><td>nước '
           'Ma-lay-xi-a</td></tr><tr><td><b>Singapore (n)</b></td><td>nước Xin-ga-po</td></tr><tr><td><b>Thailand (n)</b></td><td>nước Thái '
           'Lan</td></tr><tr><td><b>Viet Nam (n)</b></td><td>nước Việt Nam</td></tr></table><h3>Unit 2: Time and daily routines</h3><table '
           'class="tb"><tr><td><b>at (pre)</b></td><td>ở</td></tr><tr><td><b>fifteen (n)</b></td><td>số 15</td></tr><tr><td><b>forty-five (n)</b></td><td>số '
           '45</td></tr><tr><td><b>o’clock (n)</b></td><td>giờ (dùng sau giờ chẵn, ví dụ: 8 giờ: eight o’clock)</td></tr><tr><td><b>thirty (n)</b></td><td>số '
           '30</td></tr><tr><td><b>get up (v)</b></td><td>thức dậy</td></tr><tr><td><b>go (to bed) (v)</b></td><td>đi (ngủ)</td></tr><tr><td><b>go (to school) '
           '(v)</b></td><td>đi (học)</td></tr><tr><td><b>have (breakfast) (v)</b></td><td>dùng (bữa sáng)</td></tr></table><h3>Unit 3: My week</h3><table '
           'class="tb"><tr><td><b>Monday (n)</b></td><td>thứ Hai</td></tr><tr><td><b>Tuesday (n)</b></td><td>thứ Ba</td></tr><tr><td><b>Wednesday '
           '(n)</b></td><td>thứ Tư</td></tr><tr><td><b>Thursday (n)</b></td><td>thứ Năm</td></tr><tr><td><b>Friday (n)</b></td><td>thứ '
           'Sáu</td></tr><tr><td><b>Saturday (n)</b></td><td>thứ Bảy</td></tr><tr><td><b>Sunday (n)</b></td><td>Chủ nhật</td></tr><tr><td><b>listen to music '
           '(v. phr)</b></td><td>nghe nhạc</td></tr><tr><td><b>study at school (v. phr)</b></td><td>học, nghiên cứu ở trường</td></tr></table><h3>Unit 4: My '
           'birthday party</h3><table class="tb"><tr><td><b>January (n)</b></td><td>tháng Một</td></tr><tr><td><b>February (n)</b></td><td>tháng '
           'Hai</td></tr><tr><td><b>March (n)</b></td><td>tháng Ba</td></tr><tr><td><b>April (n)</b></td><td>tháng Tư</td></tr><tr><td><b>May '
           '(n)</b></td><td>tháng Năm</td></tr><tr><td><b>birthday (n)</b></td><td>ngày sinh</td></tr><tr><td><b>chips (n)</b></td><td>khoai tây '
           'rán</td></tr><tr><td><b>grape (n)</b></td><td>quả nho</td></tr><tr><td><b>jam (n)</b></td><td>mứt</td></tr><tr><td><b>juice (n)</b></td><td>nước '
           'ép</td></tr><tr><td><b>lemonade (n)</b></td><td>nước chanh</td></tr><tr><td><b>party (n)</b></td><td>buổi tiệc</td></tr><tr><td><b>water '
           '(n)</b></td><td>nước</td></tr></table><h3>Unit 5: Things we can do</h3><table class="tb"><tr><td><b>can (modal verb)</b></td><td>có thể, biết (làm '
           'gì)</td></tr><tr><td><b>cook (v)</b></td><td>nấu ăn</td></tr><tr><td><b>play the piano (v. phr)</b></td><td>chơi đàn '
           'piano</td></tr><tr><td><b>play the guitar (v. phr)</b></td><td>chơi đàn ghi-ta</td></tr><tr><td><b>ride (a bike) (v)</b></td><td>đạp '
           'xe</td></tr><tr><td><b>ride (a horse) (v)</b></td><td>cưỡi ngựa</td></tr><tr><td><b>roller skate (v)</b></td><td>trượt pa '
           'tanh</td></tr><tr><td><b>swim (v)</b></td><td>bơi</td></tr><tr><td><b>but (con)</b></td><td>nhưng</td></tr></table><h3>Unit 6: Our school '
           'facilities</h3><table class="tb"><tr><td><b>city (n)</b></td><td>thành phố</td></tr><tr><td><b>mountains (n)</b></td><td>vùng '
           'núi</td></tr><tr><td><b>town (n)</b></td><td>thị trấn</td></tr><tr><td><b>village (n)</b></td><td>ngôi làng</td></tr><tr><td><b>computer room (n. '
           'phr.)</b></td><td>phòng máy tính</td></tr><tr><td><b>garden (n)</b></td><td>vườn</td></tr><tr><td><b>playground (n)</b></td><td>sân '
           'chơi</td></tr></table><h3>Unit 7: Our timetables</h3><table class="tb"><tr><td><b>art (n)</b></td><td>môn Mĩ thuật</td></tr><tr><td><b>English '
           '(n)</b></td><td>môn Tiếng Anh</td></tr><tr><td><b>history and geography (n. phr.)</b></td><td>môn Lịch sử và Địa lí</td></tr><tr><td><b>maths '
           '(n)</b></td><td>môn Toán, toán học</td></tr><tr><td><b>music (n)</b></td><td>môn Âm nhạc</td></tr><tr><td><b>science (n)</b></td><td>môn Khoa '
           'học</td></tr><tr><td><b>Vietnamese (n)</b></td><td>môn Tiếng Việt</td></tr></table><h3>Unit 8: My favourite subjects</h3><table '
           'class="tb"><tr><td><b>IT (information technology) (n)</b></td><td>môn Tin học, môn Công nghệ thông tin</td></tr><tr><td><b>PE (physical '
           'education)(n)</b></td><td>môn Thể dục, môn Giáo dục thể chất</td></tr><tr><td><b>English teacher (n. phr.)</b></td><td>giáo viên (dạy Tiếng '
           'Anh)</td></tr><tr><td><b>maths teacher (n. phr.)</b></td><td>giáo viên (dạy Toán)</td></tr><tr><td><b>because (con)</b></td><td>bởi '
           'vì</td></tr><tr><td><b>why (adv)</b></td><td>tại sao</td></tr></table><h3>Unit 9: Our sports day</h3><table class="tb"><tr><td><b>June '
           '(n)</b></td><td>tháng Sáu</td></tr><tr><td><b>July (n)</b></td><td>tháng Bảy</td></tr><tr><td><b>August (n)</b></td><td>tháng '
           'Tám</td></tr><tr><td><b>September (n)</b></td><td>tháng Chín</td></tr><tr><td><b>October (n)</b></td><td>tháng Mười</td></tr><tr><td><b>November '
           '(n)</b></td><td>tháng Mười Một</td></tr><tr><td><b>December (n)</b></td><td>tháng Mười hai</td></tr><tr><td><b>sports day (n)</b></td><td>ngày hội '
           'thể thao</td></tr></table><h3>Unit 10: Our summer holidays</h3><table class="tb"><tr><td><b>beach (n)</b></td><td>bãi '
           'biển</td></tr><tr><td><b>campsite (n)</b></td><td>địa điểm cắm trại</td></tr><tr><td><b>countryside (n)</b></td><td>nông thôn, vùng '
           'quê</td></tr><tr><td><b>Bangkok (n)</b></td><td>Băng Cốc (thủ đô của nước Thái Lan)</td></tr><tr><td><b>Sydney (n)</b></td><td>Xít-ni (thành phố '
           'của nước Ô-xtơ-rây-li-a)</td></tr><tr><td><b>Tokyo (n)</b></td><td>Tô-ki-ô (thủ đô của nước Nhật)</td></tr><tr><td><b>last '
           '(adj)</b></td><td>trước, lần trước</td></tr><tr><td><b>yesterday (adv)</b></td><td>ngày hôm qua</td></tr><tr><td><b>at, on, in (+ place) '
           '(pre)</b></td><td>ở (+ địa điểm)</td></tr></table><h3>Unit 11: My home</h3><table class="tb"><tr><td><b>road (n)</b></td><td>con đường, đường '
           'phố</td></tr><tr><td><b>street (n)</b></td><td>phố, đường phố</td></tr><tr><td><b>big (adj)</b></td><td>to, lớn (kích '
           'thước)</td></tr><tr><td><b>busy (adj)</b></td><td>bận rộn, nhộn nhịp</td></tr><tr><td><b>live (v)</b></td><td>sống</td></tr><tr><td><b>noisy '
           '(adj)</b></td><td>ồn ào, om sòm, huyên náo</td></tr><tr><td><b>quiet (adj)</b></td><td>yên tĩnh, tĩnh mịch</td></tr><tr><td><b>at, in (+ name of '
           'the street / road) (pre)</b></td><td>ở, tại</td></tr></table><h3>Unit 12: Jobs</h3><table class="tb"><tr><td><b>actor (n)</b></td><td>diễn viên '
           '(nam)</td></tr><tr><td><b>farmer (n)</b></td><td>nông dân</td></tr><tr><td><b>nurse (n)</b></td><td>y tá, điều dưỡng '
           'viên</td></tr><tr><td><b>office worker (n)</b></td><td>nhân viên văn phòng</td></tr><tr><td><b>policeman (n)</b></td><td>cảnh sát '
           '(nam)</td></tr><tr><td><b>factory (n)</b></td><td>nhà máy</td></tr><tr><td><b>farm (n)</b></td><td>trang trại</td></tr><tr><td><b>hospital '
           '(n)</b></td><td>bệnh viện</td></tr><tr><td><b>nursing home (n)</b></td><td>viện điều dưỡng</td></tr></table><h3>Unit 13: Appearance</h3><table '
           'class="tb"><tr><td><b>big (adj)</b></td><td>to, lớn (kích thước)</td></tr><tr><td><b>short (adj)</b></td><td>thấp, ngắn</td></tr><tr><td><b>slim '
           '(adj)</b></td><td>mảnh mai</td></tr><tr><td><b>tall (adj)</b></td><td>cao</td></tr><tr><td><b>eyes (n)</b></td><td>mắt</td></tr><tr><td><b>face '
           '(n)</b></td><td>khuôn mặt</td></tr><tr><td><b>hair (n)</b></td><td>tóc</td></tr><tr><td><b>long (adj)</b></td><td>dài</td></tr><tr><td><b>round '
           '(adj)</b></td><td>tròn</td></tr></table><h3>Unit 14: Daily activities</h3><table class="tb"><tr><td><b>afternoon (n)</b></td><td>buổi '
           'chiều</td></tr><tr><td><b>evening (n)</b></td><td>buổi tối</td></tr><tr><td><b>morning (n)</b></td><td>buổi sáng</td></tr><tr><td><b>noon '
           '(n)</b></td><td>buổi trưa</td></tr><tr><td><b>clean (the floor) (v)</b></td><td>lau (sàn nhà)</td></tr><tr><td><b>help with the cooking (v. '
           'phr.)</b></td><td>giúp đỡ việc nấu ăn</td></tr><tr><td><b>wash (the clothes) (v)</b></td><td>giặt (quần áo)</td></tr><tr><td><b>wash (the dishes) '
           '(v)</b></td><td>rửa (bát đĩa)</td></tr></table><h3>Unit 15: My family’s weekends</h3><table class="tb"><tr><td><b>cinema (n)</b></td><td>rạp chiếu '
           'phim</td></tr><tr><td><b>shopping centre (n)</b></td><td>trung tâm mua sắm</td></tr><tr><td><b>sports centre (n)</b></td><td>trung tâm thể '
           'thao</td></tr><tr><td><b>swimming pool (n)</b></td><td>bể bơi</td></tr><tr><td><b>cook meals (v. phr.)</b></td><td>nấu ăn</td></tr><tr><td><b>do '
           'yoga (v. phr.)</b></td><td>tập yoga</td></tr><tr><td><b>play tennis (v. phr.)</b></td><td>chơi quần vợt</td></tr><tr><td><b>watch films (v. '
           'phr.)</b></td><td>xem phim</td></tr></table><h3>Unit 16: Weather</h3><table class="tb"><tr><td><b>cloudy (adj)</b></td><td>có mây, nhiều '
           'mây</td></tr><tr><td><b>rainy (adj)</b></td><td>có mưa</td></tr><tr><td><b>sunny (adj)</b></td><td>có nắng</td></tr><tr><td><b>weather '
           '(n)</b></td><td>thời tiết</td></tr><tr><td><b>windy (adj)</b></td><td>có gió</td></tr><tr><td><b>bakery (n)</b></td><td>hiệu bánh '
           'mì</td></tr><tr><td><b>bookshop (n)</b></td><td>hiệu sách</td></tr><tr><td><b>food stall (n)</b></td><td>quầy hàng thực '
           'phẩm</td></tr><tr><td><b>water park (n)</b></td><td>công viên nước</td></tr><tr><td><b>supermarket (n)</b></td><td>siêu '
           'thị</td></tr></table><h3>Unit 17: In the city</h3><table class="tb"><tr><td><b>get (to) (v)</b></td><td>đến (địa điểm)</td></tr><tr><td><b>go '
           'straight (v. phr.)</b></td><td>đi thẳng</td></tr><tr><td><b>left (n)</b></td><td>bên trái</td></tr><tr><td><b>right (n)</b></td><td>bên '
           'phải</td></tr><tr><td><b>stop (v)</b></td><td>dừng lại</td></tr><tr><td><b>turn (v)</b></td><td>rẽ</td></tr><tr><td><b>turn left (v. '
           'phr.)</b></td><td>rẽ trái</td></tr><tr><td><b>turn right (v. phr.)</b></td><td>rẽ phải</td></tr><tr><td><b>turn round (v. phr.)</b></td><td>quay '
           'lại, đổi hướng ngược lại</td></tr></table><h3>Unit 18: At the shopping centre</h3><table class="tb"><tr><td><b>behind (pre)</b></td><td>đằng '
           'sau</td></tr><tr><td><b>between (pre)</b></td><td>ở giữa</td></tr><tr><td><b>near (pre)</b></td><td>ở gần</td></tr><tr><td><b>opposite '
           '(pre)</b></td><td>đối diện</td></tr><tr><td><b>gift shop (n)</b></td><td>cửa hàng quà tặng</td></tr><tr><td><b>skirt '
           '(n)</b></td><td>Váy</td></tr><tr><td><b>dong (n)</b></td><td>đồng (đơn vị tiền tệ của Việt Nam)</td></tr><tr><td><b>thousand '
           '(n)</b></td><td>Nghìn</td></tr><tr><td><b>T-shirt (n)</b></td><td>áo thun</td></tr></table><h3>Unit 19: The animal world</h3><table '
           'class="tb"><tr><td><b>beautifully (adv)</b></td><td>đẹp đẽ</td></tr><tr><td><b>crocodile (n)</b></td><td>cá sấu Châu Phi, cá '
           'sấu</td></tr><tr><td><b>Dance</b></td><td>nhảy, múa</td></tr><tr><td><b>giraffe (n)</b></td><td>hươu cao cổ</td></tr><tr><td><b>hippo '
           '(n)</b></td><td>hà mã, lợn nước</td></tr><tr><td><b>lion (n)</b></td><td>con sư tử</td></tr><tr><td><b>loudly (adv)</b></td><td>ầm ĩ, inh '
           'ỏi</td></tr><tr><td><b>merrily (adv)</b></td><td>vui, vui vẻ</td></tr><tr><td><b>quickly (adv)</b></td><td>Nhanh</td></tr><tr><td><b>roar '
           '(v)</b></td><td>gầm, rống lên (hổ, sư tử …)</td></tr><tr><td><b>run (v)</b></td><td>chạy</td></tr><tr><td><b>sing '
           '(v)</b></td><td>hát</td></tr></table><h3>Unit 20: At summer camp</h3><table class="tb"><tr><td><b>build a campfire (v. phr.)</b></td><td>đốt lửa '
           'trại</td></tr><tr><td><b>play card games (v. phr.)</b></td><td>chơi bài</td></tr><tr><td><b>put up a tent (v. phr.)</b></td><td>dựng, cắm trại, '
           'lều</td></tr><tr><td><b>sing songs (v. phr.)</b></td><td>hát</td></tr><tr><td><b>take a photo (v. phr.)</b></td><td>chụp '
           'ảnh</td></tr><tr><td><b>tell a story (v. phr.)</b></td><td>kể chuyện</td></tr></table>',
 'title': 'HSG – Bài tập bồi dưỡng',
 'unit': 'HSG'}
