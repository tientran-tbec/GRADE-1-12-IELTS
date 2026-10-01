"""Chuyển đổi 1 lần: Đề ôn tập giữa HK1 Anh 11 Global 25-26 Đề 8 (src/mt1/d8.txt) -> units/mt1_test07.py (khung câu hỏi).
Nguồn đề 8 trình bày rất lộn xộn (mất nhãn A., gõ sai, số câu đánh lại từ 1 ở mỗi phần) nên câu hỏi/phương án được gõ lại tay
ở đây (đối chiếu từng câu với src/mt1/d8.txt); đoạn đọc hiểu lấy trực tiếp từ nguồn. Số câu được đánh liên tục 1..38.
Đáp án + giải thích: units/mt1_test07_dapan.py. Audio: audio/mt1_test07.mp3 (ffmpeg, mono 64kbps; cắt bỏ Part 1 'clothes shop' dư ở đầu file RAW ...De-8.mp3)."""
import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from mt1_common import *

L = load_src('d8')
END = find(L, r'<b>\s*ĐÁP ÁN')
EX = L[:END]


def mc(gid, n, q, o):
    return {'id': '%s.%d' % (gid, n), 't': 'mcq', 'q': q, 'o': o}


def build():
    groups = []
    # --- Listening (1-5)
    groups.append({'id': 'g1', 'instr': 'I. LISTENING. You will hear some information about a cinema. Listen and complete each space with ONE word or number. You will hear the recording TWICE.',
                   'passage': '<p><b>CINEMA</b></p><p>Name of cinema: <b>North London Arts Cinema</b></p>',
                   'items': [{'id': 'g1.1', 't': 'fill', 'q': "Next week's film: Midnight {_}"},
                             {'id': 'g1.2', 't': 'fill', 'q': 'From: {_} to Thursday.'},
                             {'id': 'g1.3', 't': 'fill', 'q': 'Ticket costs: £ {_}'},
                             {'id': 'g1.4', 't': 'fill', 'q': 'Nearest car park: in {_} Street.'},
                             {'id': 'g1.5', 't': 'fill', 'q': 'A walk from the cinema: {_} minutes'}]})
    # --- Lexico-grammar (6-16)
    groups.append({'id': 'g2', 'instr': 'II. LEXICAL-GRAMMAR. Mark the letter A, B, C, or D on your answer sheet to indicate the correct answer to each of the following questions.',
                   'items': [
        mc('g2', 6, 'To build your ______, you can try lift weights.', ['health', 'treatment', 'habit', 'muscles']),
        mc('g2', 7, 'It’s also important to eat a ______ diet with lots of fruits, vegetables, and protein.', ['electronic', 'balanced', 'regular', 'nutrients']),
        mc('g2', 8, 'The doctors advised viewers to exercise ______.', ['nicely', 'fit', 'regularly', 'infectiously']),
        mc('g2', 9, 'Gen Zers are very ______ as they always come up with new ideas or things.', ['experienced', 'curious', 'creative', 'traditional']),
        mc('g2', 10, 'Linda ______ in this city since she left school.', ['lived', 'lives', 'had lived', 'has lived']),
        mc('g2', 11, 'With the help of technology, people can grow vegetables in the roof garden of ______ buildings.', ['high-standard', 'high-quality', 'high-rise', 'high-level']),
        mc('g2', 12, 'All the students ______ obey the school rules.', ['mustn’t', 'have to', 'should', 'must']),
        mc('g2', 13, 'He ______ his grandparents last week.', ['visited', 'visits', 'has visited', 'is visiting']),
        mc('g2', 14, 'Peter ______ his essay on travelling.', ['just finished', 'just has finished', 'have just finished', 'has just finished']),
        mc('g2', 15, 'You ______ tidy up your bedroom. No one can clean it for you.', ['don’t have to', 'mustn’t', 'must', 'shouldn’t']),
        mc('g2', 16, 'Please be quiet! I ______.', ['think', 'am thinking', 'thought', 'thinks'])]})
    # --- Cloze (17-21)
    i0 = find(EX, r'Green Living')
    txt = ' '.join(cl(l) for l in EX[i0:i0 + 3] if cl(l))
    txt = txt.replace('Green Living: A Better Tomorrow', '').strip()
    txt = re.sub(r'\((\d)\)\s*_+\s*', r'<b>(\1) ______</b> ', txt)
    txt = txt.replace('eco – friendly', 'eco-friendly').replace('single – use', 'single-use')
    txt = re.sub(r'\s+([.,!])', r'\1', txt)
    txt = re.sub(r'(______</b>) (?=[a-z])', r'\1 ', txt)
    txt = txt.replace('efforts <b>(4)', 'efforts <b>(4)')
    txt = re.sub(r'\s+', ' ', txt)
    sp = txt.index('By going green')
    groups.append({'id': 'g3', 'instr': 'Read the following advertisement and mark the letter A, B, C or D on your answer sheet to indicate the option that best fits each of the numbered blanks from 1 to 5.',
                   'passage': '<h4>Green Living: A Better Tomorrow</h4><p>%s</p><p>%s</p>' % (txt[:sp].strip(), txt[sp:].strip()),
                   'items': [dict(mc('g3', 17, 'Blank (1)', ['Living', 'To live', 'Lived', 'Live'])),
                             mc('g3', 18, 'Blank (2)', ['simple habits daily', 'daily simple habits', 'habits simple daily', 'simple daily habits']),
                             mc('g3', 19, 'Blank (3)', ['boring', 'bored', 'boringly', 'boredom']),
                             mc('g3', 20, 'Blank (4)', ['with', 'on', 'of', 'to']),
                             mc('g3', 21, 'Blank (5)', ['make', 'have', 'book', 'do'])]})
    # --- Reading (22-26)
    r0 = find(EX, r'^Most human diets')
    rq = find(EX, r'^<b>Question 1:</b> We can infer')
    paras = []
    for l in EX[r0:rq]:
        t = re.sub(r'\s+', ' ', l.replace('⟦', '').replace('⟧', '').replace('\t', ' ')).strip()
        if t:
            paras.append(t.replace('conies', 'comes'))      # nguồn gõ sai: "conies"
    assert len(paras) == 3, len(paras)
    paras[2] = paras[2].replace('<b><u>They</u></b>', '<b><u>They</u></b>')
    groups.append({'id': 'g4', 'instr': 'III. READING. Read the following passage and mark the letter A, B, C, or D to indicate the correct answer to each of the questions.',
                   'passage': ''.join('<p>%s</p>' % p for p in paras),
                   'items': [
        mc('g4', 22, 'We can infer from the passage that all of the following statements about fats are TRUE <b>EXCEPT</b> ______.',
           ['alcohol is not a common source of dietary energy', 'fats provide energy for the body', 'economics influences the distribution of calorie intake', 'poor people eat more fatty foods']),
        mc('g4', 23, 'The word “<b><u>They</u></b>” in paragraph 3 refers to ______.', ['Abnormalities', 'Systems', 'Rats', 'Fatty acids']),
        mc('g4', 24, 'According to the author of the passage, which of the following is TRUE for rats when they are fed a fat-free diet?',
           ['They lose body hair.', 'They have more babies.', 'They require less care.', 'They stop growing.']),
        mc('g4', 25, 'The word “<b><u>essential</u></b>” in paragraph 3 is CLOSEST in meaning to ______.', ['curious', 'necessary', 'sustainable', 'liveable']),
        mc('g4', 26, 'This passage probably appeared in which of the following?', ['A newspaper', 'A cookbook', 'A women’s magazine', 'A book on basic nutrition'])]})
    # --- Sắp xếp (27-29)
    a1 = ['a. Sarah: Hi Mike! It’s so good to see you. How have you been?',
          'b. Sarah: Same here. I’ve been trying to balance work and exercise. Actually, I just started taking yoga classes.',
          'c. Mike: Hey Sarah! I’m doing well, thanks. Just been really busy with work lately. How about you?']
    a2 = ['a. John: Happy birthday, Emma! I have a gift for you.', 'b. Emma: Wow! A beautiful blue scarf!', 'c. Emma: Hi John! Welcome to my birthday party!',
          'd. Emma: Thank you! What is it?', 'e. John: Open it and see!']
    a3 = ['a. Second, English is an international means of communication. Take Media, commercials, electronic gadgets catalogues, the internet, most TV programmes and movies.',
          'b. Are not these drives enough to make learning English imperative for us all?',
          'c. First, speaking English is a competency that attracts most employers worldwide. For example, people who speak English have more chances to get a good job wherever in the world than others.',
          'd. Learning English is important for my career for three reasons.',
          'e. Third, English is the key to many fresh resources and information. If you speak English, you can get the information fresh ahead of millions of people.']
    groups.append({'id': 'g5', 'instr': 'IV. WRITING. Mark the letter A, B, C, or D on your answer sheet to indicate the correct arrangement of the sentences to make a meaningful dialogue/paragraph in each of the following questions.',
                   'items': [mc('g5', 27, '<br>'.join(a1), ['c – b – a', 'a – b – c', 'a – c – b', 'c – a – b']),
                             mc('g5', 28, '<br>'.join(a2), ['c – a – d – e – b', 'a – d – e – b – c', 'e – a – c – d – b', 'c – a – b – d – e']),
                             mc('g5', 29, '<br>'.join(a3), ['c – a – e – b – d', 'a – d – b – e – c', 'd – b – c – a – e', 'd – c – a – e – b'])]})
    # --- Dạng đúng của từ (30-34)
    groups.append({'id': 'g6', 'instr': 'Supply the correct form of the given word/verb in each of the following questions to make meaningful sentences.',
                   'items': [{'id': 'g6.30', 't': 'fill', 'q': 'People from different generations may sometimes get into {_} over viewpoints.', 'hint': 'ARGUE'},
                             {'id': 'g6.31', 't': 'fill', 'q': 'Hung is a {_} thinker. He always tries to look into things from different aspects and contributes to work out a better solution.', 'hint': 'CRITIC'},
                             {'id': 'g6.32', 't': 'fill', 'q': 'John and Mary {_} each other since they were at high school.', 'hint': 'LOVE'},
                             {'id': 'g6.33', 't': 'fill', 'q': 'You should not {_} up late to play computer games.', 'hint': 'STAY'},
                             {'id': 'g6.34', 't': 'fill', 'q': 'The little boy looks {_} because he gets good grades in the exam.', 'hint': 'HAPPY'}]})
    # --- Viết lại câu (35-38)
    def rw(n, stem, hint, pre):
        return {'id': 'g7.%d' % n, 't': 'fill', 'long': True, 'q': '<b>%s</b> <i>(%s)</i><br>→ %s {_}' % (stem, hint, pre)}
    groups.append({'id': 'g7', 'instr': 'PART 5: WRITING (2.0 PTS). For each question, complete the new sentence so that it means the same as the given one(s) using given words.',
                   'items': [rw(35, 'Jack and Jean started to learn how to drive 2 weeks ago.', 'have', 'Jack'),
                             rw(36, 'It is a good idea for parents to try to understand their teenage children.', 'should', 'Parents'),
                             rw(37, 'He quit smoking in 2020.', 'hasn’t', 'He'),
                             rw(38, 'Every staff isn’t allowed to smoke or eat in the office.', 'mustn’t', 'Every staff')]})
    return {'id': 'lop11-mt1-test07', 'title': 'Test 7 – Mid-term 1', 'grade': 11, 'unit': 'MidTerm1', 'theory': '',
            'pages': [{'id': 'kiem-tra', 'title': 'Làm bài', 'mode': 'test', 'minutes': 45, 'audio': True, 'groups': groups}]}


if __name__ == '__main__':
    b = build()
    dump(os.path.join(ROOT, 'units/mt1_test07.py'), 'SET', b)
    n = 0
    for g in b['pages'][0]['groups']:
        n += len(g['items']); print(g['id'], len(g['items']))
    print('TOTAL', n)
