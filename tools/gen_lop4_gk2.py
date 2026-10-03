# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g4_exam import *
P = 'thuvienhoclieu.com-Nghe-De-kiem-tra-giua-HK2-Anh-4-Global-De-%d.mp3'


def mk(n, minutes=15):
    src = 'De-kiem-tra-giua-HK2-Anh-4-Global-De-%d' % n
    d = Dump(src)
    ex = Exam('gk2_de%d' % n, 'GiuaKy2', 'Giữa kỳ 2 – Đề %d' % n, src, slug='test%02d' % n, minutes=minutes, warn_at=3, audio=[P % n])
    return d, d.sec(), d.keys(), ex


PT = {3: {2: {'q': 'Nghe: Khi nào bạn rửa bát? (When do you wash the dishes?)', 'o': ['In the afternoon', 'In the morning', 'In the evening']}},
      5: {3: {'q': 'Nghe: Khi nào cô ấy chơi tennis? (When does she play tennis?)', 'o': ['In the morning', 'In the afternoon', 'In the evening']}}}
for n in (1, 3, 4, 5):
    d, S, K, ex = mk(n)
    std_family(ex, d, S, K, pic_text=PT.get(n))
    ex.save()


# ================= ĐỀ 2: phần IV có khung từ
d, S, K, ex = mk(2)
std_family.__globals__  # noqa
kI = keyletters(K['I']['lines']); kII = keyletters(K['II']['lines']); kIII = keyletters(K['III']['lines'])
rw = rows_words(S['I']['lines'])
ex.mcq_words('l1', 'I. Listen to the sounds and circle the correct words (nghe âm, chọn từ có âm đó).', rw, [kI[i + 1] for i in range(4)], q='Nghe âm và chọn từ có âm đó.')
rp = rows_pics(S['II']['lines'])
ex.mcq_pics('l2', 'II. Listen and circle the correct pictures (nghe và chọn tranh đúng).', rp, [kII[i + 1] for i in range(4)])
rq = rows_q(S['III']['lines'])
ex.mcq_text('r1', 'III. Circle the correct answers (nhìn tranh, chọn câu đúng).', rq, [kIII[i + 1] for i in range(4)])
ex.fill('r2', 'IV. Fill in the blanks. There is ONE extra word (chọn từ trong khung, thừa 1 từ).',
        [('Susan: What does your dad look like? John: He has short, black {_}.', ['hair'], 'img24', 'hair = tóc.'),
         ('Susan: Is he {_}? John: Yes, he is. And he is thin.', ['tall'], 'img24', 'tall = cao.'),
         ('Susan: Can you describe your mum? John: She has {_}, brown hair.', ['long'], 'img25', 'long hair = tóc dài.'),
         ('Susan: Is she big? John: No, she isn’t. She’s {_}.', ['slim'], 'img25', 'slim = mảnh mai, thon thả.')],
        bank=['long', 'big', 'tall', 'hair', 'slim'])
ex.save()

# ================= ĐỀ 6 (24-25)
src6 = 'De-kiem-tra-giua-hoc-ky-2-Tieng-Anh-4-Global-24-25-De-6-'
ex = Exam('gk2_de6', 'GiuaKy2', 'Giữa kỳ 2 – Đề 6', src6, slug='test06', minutes=35, warn_at=5, audio=['thuvienhoclieu.com-Nghe-De-kiem-tra-giua-hoc-ky-2-Tieng-Anh-4-Global-24-25-De-6.mp3'])
ex.mcq_text('l1', 'A. Listening. Listen and choose the correct answers to complete sentences (nghe, chọn đáp án hoàn thành câu).', [
    (None, '1. I ____ in the morning.', ['have breakfast', 'take a shower', 'do morning exercise']),
    (None, '2. You ____ in the evening.', ['have dinner', 'take a bath', 'watch TV']),
    (None, '3. She goes home at ____.', ['half past three', 'six o’clock', 'three o’clock']),
    (None, '4. Tom ____ at 5 p.m.', ['take a bath', 'takes a shower', 'takes a bath']),
    (None, '5. You ____ in the afternoon.', ['go to school', 'go home', 'get dressed'])], ['B', 'A', 'C', 'C', 'B'])
ex.mcq_text('v1', 'B. Vocabulary & Grammar. I. Odd one out (chọn từ khác loại).', [
    (None, '1. Chọn từ khác loại:', ['hotel', 'accountant', 'fireman', 'engineer']),
    (None, '2. Chọn từ khác loại:', ['chicken', 'bread', 'lemonade', 'fish']),
    (None, '3. Chọn từ khác loại:', ['strong', 'slim', 'young', 'live']),
    (None, '4. Chọn từ khác loại:', ['come', 'smart', 'join', 'hear']),
    (None, '5. Chọn từ khác loại:', ['get up', 'have breakfast', 'go home', 'routine'])], ['A', 'C', 'D', 'B', 'D'],
    exps=['hotel là nơi chốn; 3 từ còn lại là nghề nghiệp.', 'lemonade là đồ uống; còn lại là đồ ăn.', 'live là động từ; còn lại là tính từ.',
          'smart là tính từ; còn lại là động từ.', 'routine là danh từ; còn lại là cụm động từ.'])
for i, nm in enumerate(['img01', 'img02', 'img03', 'img04', 'img05'], 1):
    ex.single(nm, 'm%d.png' % i, w=190, h=140)
ex.match('v2', 'II. Match (nhìn tranh, chọn từ đúng).', [{'img': 'm%d.png' % i} for i in range(1, 6)], ['interview', 'party', 'vegetables', 'farmer', 'Christmas'],
         ['vegetables', 'farmer', 'party', 'Christmas', 'interview'], 'Tranh 1: rau củ (vegetables); 2: nông dân (farmer); 3: bữa tiệc (party); 4: lễ Giáng sinh (Christmas); 5: phỏng vấn (interview).')
ex.mcq_text('v3', 'III. Choose the correct answer (chọn đáp án đúng).', [
    (None, '1. ____ does he work? – He works in a hospital.', ['What', 'When', 'Where']),
    (None, '2. I like beef. It’s my favourite ____.', ['drink', 'milk', 'food']),
    (None, '3. What ____ they look like?', ['do', 'are', 'does']),
    (None, '4. How ____ is this bag?', ['much', 'many', 'lot of']),
    (None, '5. Would you like ____ water?', ['many', 'some', 'for'])], ['C', 'C', 'A', 'A', 'B'],
    exps=['Hỏi nơi chốn → Where.', 'beef là thức ăn → food.', 'they → do.', 'Hỏi giá → How much.', 'Would you like some + N?'])
P6 = ('My brother’s name is Dat. He is 10 and he studies at Cambridge Primary School. He often gets up at six o’clock in the morning. He usually has breakfast at six thirty. '
      'Then, he goes to school by bus. He has got Maths and Science in the morning and his class starts at seven o’clock. He studies to eleven o’clock. He and his friends have lunch in the canteen. '
      'He learns English and History in the afternoon. His class finishes at five p.m. He is at home at five thirty and helps mom to clear the table and cook the dinner. He watches TV, then goes to bed at 11 p.m.')
ex.fill('v4', 'IV. Read the passage and complete the sentences (đọc đoạn văn, hoàn thành câu).', [
    ('Dat studies at {_}.', ['Cambridge Primary School', 'Cambridge primary school'], None, 'He studies at Cambridge Primary School.'),
    ('He {_} at six o’clock in the morning.', ['often gets up'], None, 'He often gets up at six o’clock in the morning.'),
    ('His class starts at {_}.', ['seven o’clock', "seven o'clock", 'seven'], None, 'His class starts at seven o’clock.'),
    ('He has lunch in {_}.', ['the canteen', 'canteen'], None, 'He has lunch in the canteen.'),
    ('He {_} at 11 p.m.', ['goes to bed'], None, 'He goes to bed at 11 p.m.')], passage='<p>' + P6 + '</p>')
ex.mcq_text('v5', 'V. Read and choose the correct words (chọn từ đúng).', [
    (None, '1. This is my uncle. He is ____ worker.', ['a', 'an']),
    (None, '2. ____ you like some orange juice? – No, thanks.', ['Do', 'Would']),
    (None, '3. ____ does he do at Tet? – He cleans the house.', ['What', 'Where']),
    (None, '4. ____ is your favourite food? – Pork.', ['What', 'How']),
    (None, '5. What does ____ mother look like?', ['he', 'his'])], ['A', 'B', 'A', 'A', 'B'],
    exps=['worker bắt đầu bằng phụ âm → a.', 'Would you like …? là lời mời.', 'Hỏi hoạt động → What.', 'What is your favourite food?', 'his mother = mẹ của anh ấy.'])
ex.save()

# ================= ĐỀ 7 (24-25)
src7 = 'De-kiem-tra-giua-hoc-ky-2-Tieng-Anh-4-Global-24-25-De-7'
ex = Exam('gk2_de7', 'GiuaKy2', 'Giữa kỳ 2 – Đề 7', src7, slug='test07', minutes=35, warn_at=5, audio=['thuvienhoclieu.com-Nghe-De-kiem-tra-giua-hoc-ky-2-Tieng-Anh-4-Global-24-25-De-7.mp3'])
L7 = ('Today I go to the market with my (1) . We buy fruits and vegetables. First we go to the fruits (2) . Here we buy apples, bananas, watermelons, oranges and (3) . '
      'After that, we go to the vegetable mall. Mum buys cabbage, (4) . Next, we buy some snacks and soft drinks such as biscuits, yogurts, (5) and pancake. We also buy rice, noodles and bread before we go home.')
ex.fill('l1', 'A. Listening. Listen and complete (nghe và điền từ).', [('Chỗ trống (%d): {_}' % (i + 1), [a], None, 'Đáp án: ' + a) for i, a in enumerate(['mother', 'store', 'grapes', 'tomatoes', 'milk'])], passage=passage(L7))
ex.mcq_text('v1', 'B. Vocabulary & Grammar. I. Odd one out (chọn từ khác loại).', [
    (None, '1. Chọn từ khác loại:', ['snake', 'dog', 'teacher', 'kangaroo']),
    (None, '2. Chọn từ khác loại:', ['second', 'thirteen', 'eight', 'twelve']),
    (None, '3. Chọn từ khác loại:', ['cheap', 'much', 'expensive', 'long']),
    (None, '4. Chọn từ khác loại:', ['toy store', 'bakery', 'hospital', 'near']),
    (None, '5. Chọn từ khác loại:', ['secretary', 'lawyer', 'airport', 'postman'])], ['C', 'A', 'B', 'D', 'C'],
    exps=['teacher là nghề nghiệp; còn lại là động vật.', 'second là số thứ tự; còn lại là số đếm.', 'much không phải tính từ như các từ còn lại.', 'near là tính từ; còn lại là địa điểm.', 'airport là địa điểm; còn lại là nghề nghiệp.'])
ex.mcq_text('v2', 'II. Choose the correct answer (chọn đáp án đúng).', [
    (None, '1. ____ do you have dinner? – 7 p.m.', ['What', 'Where', 'What time']),
    (None, '2. I have lunch ____ twelve o’clock.', ['at', 'to', 'with']),
    (None, '3. What ____ her brother do?', ['do', 'does', 'is']),
    (None, '4. He is ____ engineer.', ['X', 'an', 'a']),
    (None, '5. Would you like ____ milk?', ['many', 'a', 'some'])], ['C', 'A', 'B', 'B', 'C'],
    exps=['Hỏi giờ → What time.', 'at + giờ.', 'her brother → does.', 'engineer bắt đầu bằng nguyên âm → an.', 'Would you like some + N?'])
P7 = ('December is always a very busy period of time for Santa Claus. He does a lot of things. He opens and reads many (1) from children all over the world. He (2) long lists of toys and children’s names. '
      'He buys lots of (3) for the children and wraps them. He puts them on his sleigh and (4) them to the children’s (5) all around the world.')
ex.fill('v3', 'III. Read and complete the passage. Use available words (chọn từ trong khung).', [('Chỗ trống (%d): {_}' % (i + 1), [a], None, 'Đáp án: ' + a) for i, a in enumerate(['letters', 'writes', 'presents', 'brings', 'houses'])],
        passage=passage(P7), bank=['writes', 'houses', 'presents', 'letters', 'brings'])
A7 = ('Hello. My name is Anna. I come from the USA. These are my parents. My mother is Laura and she loves vegetables and fruits. She doesn\'t like beef. My father is Peter. He loves meat and he dislikes vegetables and fruits. '
      'My parents have two children: me and my little sister Nina. This is Nina. Nina is five years old. She is playing with a yo yo and eating some biscuits. She loves biscuits. Finally, I am a student at the International School. I don\'t like bananas and fish. I love pork and chicken.')
ex.fill('v4', 'IV. Read and answer questions (đọc và trả lời câu hỏi).', [
    ('Where is Anna from? – {_}', ['Anna is from the USA.', 'She is from the USA.', 'She’s from the USA.', 'From the USA.', 'The USA.', 'The USA'], None, 'Anna is from the USA.'),
    ('What’s Laura’s favourite food? – {_}', ['She likes vegetables and fruits.', 'She loves vegetables and fruits.', 'Vegetables and fruits.'], None, 'She likes vegetables and fruits.'),
    ('What’s Peter’s favourite food? – {_}', ['He likes meat.', 'He loves meat.', 'Meat.'], None, 'He likes meat.'),
    ('How many people are there in Anna’s family? – {_}', ['There are four people in Anna’s family.', 'There are four people.', 'There are four.', 'Four.'], None, 'There are four people in Anna’s family.'),
    ('What’s Anna’s favourite food? – {_}', ['She likes pork and chicken.', 'She loves pork and chicken.', 'Pork and chicken.'], None, 'She likes pork and chicken.')], passage='<p>' + A7 + '</p>')
ex.order('v5', 'V. Rearrange to make correct sentences (sắp xếp từ thành câu đúng).', [
    (['is', 'than', 'her', 'taller', 'sister.', 'Anna'], 'Anna is taller than her sister.'),
    (['wears', 'at', 'new', 'She', 'clothes', 'Tet.'], 'She wears new clothes at Tet.'),
    (['does', 'her', 'look', 'like?', 'What', 'mother'], 'What does her mother look like?'),
    (['your', 'work?', 'brother', 'Where', 'does'], 'Where does your brother work?'),
    (['day?', 'is', 'When', 'Children’s', 'the'], 'When is the Children’s day?')])
ex.save()
