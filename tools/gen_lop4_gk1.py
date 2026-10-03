# -*- coding: utf-8 -*-
"""Lớp 4 – Giữa kỳ 1: Đề 1–4 (thuvienhoclieu.com) + 4 phần luyện nghe. Bỏ phần Speaking (nếu có)."""
import sys, re
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from g4_exam import *

PHON = 'Nghe âm và chọn từ có âm đó.'


def gk1(n, audio, drop_listen=False):
    src = 'De-kiem-tra-giua-HK1-Anh-4-Global-De-%d' % n
    d = Dump(src)
    S, K = d.sec(), d.keys()
    ex = Exam('gk1_de%d' % n, 'GiuaKy1', 'Giữa kỳ 1 – Đề %d' % n, src, slug='test%02d' % n, minutes=15, warn_at=3, audio=audio)
    return d, S, K, ex


# ============ ĐỀ 1 (đã có file nghe)
def de1():
    d, S, K, ex = gk1(1, ['gk1_de1_t1.mp3', 'gk1_de1_t2.mp3'])
    kI = keyletters(K['I']['lines']); kII = keyletters(K['II']['lines'])
    ex.mcq_words('l1', 'I. Listen to the sounds and circle the correct words (nghe âm, chọn từ đúng).', rows_words(S['I']['lines']), [kI[i] for i in range(1, 5)], q='Nghe và chọn từ em nghe được.')
    ex.mcq_pics('l2', 'II. Listen and tick the correct pictures (nghe và chọn tranh đúng).', rows_pics(S['II']['lines']), [kII[i] for i in range(1, 5)])
    rq = rows_q(S['III']['lines']); kk = keyletters(K['III']['lines'])
    ex.mcq_text('r1', 'III. Circle the correct answers (nhìn tranh, chọn câu đúng).', rq, [kk[i] for i in range(1, 5)])
    ps = ' '.join(l for l in S['IV']['lines'])
    fills = ['America', 'cake', 'chips', 'milk']
    pics = imgs(ps)
    ex.fill('r2', 'IV. Fill in the blanks (nhìn tranh, điền từ vào chỗ trống).',
            [('Chỗ trống (%d): {_}' % (i + 1), [a], pics[i]) for i, a in enumerate(fills)], passage=passage(ps))
    ex.save()


# ============ ĐỀ 2
def de2():
    d, S, K, ex = gk1(2, ['thuvienhoclieu.com-De-kiem-tra-giua-HK1-Anh-4-Global-De-2-TASK-1.mp3', 'thuvienhoclieu.com-De-kiem-tra-giua-HK1-Anh-4-Global-De-2-TASK-2.mp3'])
    ex.mcq_words('l1', 'I. Listen and circle the correct words (nghe và chọn từ đúng).', rows_words(S['I']['lines']), ['C', 'A', 'C', 'A'], q='Nghe và chọn từ em nghe được.')
    ex.mcq_pics('l2', 'II. Listen and tick the correct pictures (nghe và chọn tranh đúng).', rows_pics(S['II']['lines']), ['C', 'A', 'B', 'C'])
    ex.mcq_text('r1', 'III. Read and circle the correct sentences (nhìn tranh, chọn câu đúng).', rows_q(S['III']['lines']), ['A', 'C', 'C', 'A'])
    ps = ' '.join(S['IV']['lines']); pics = imgs(ps)
    ex.fill('r2', 'IV. Fill in the blanks (nhìn tranh, điền từ vào chỗ trống).',
            [('Chỗ trống (%d): {_}' % (i + 1), [a], pics[i]) for i, a in enumerate(['roller skate', 'play the guitar', 'play the piano', 'ride a bike'])], passage=passage(ps))
    ex.save()


# ============ ĐỀ 3
def de3():
    d, S, K, ex = gk1(3, ['thuvienhoclieu.com-Nghe-De-kiem-tra-giua-HK1-Anh-4-Global-De-3-TASK-1.mp3', 'thuvienhoclieu.com-Nghe-De-kiem-tra-giua-HK1-Anh-4-Global-De-3-TASK-2.mp3'])
    ex.mcq_words('l1', 'I. Listen and circle the correct words (nghe và chọn từ đúng).', rows_words(S['I']['lines']), ['C', 'A', 'A', 'C'], q='Nghe và chọn từ em nghe được.')
    # II: nghe, ✓ / ✗ với 4 tranh
    pics = imgs(' '.join(S['II']['lines']))[1:5]
    ex.tf('l2', 'II. Listen and put a ✓ (True) or ✗ (False) (nghe, tranh có khớp với câu nghe được không?).',
          [('Tranh %d: nội dung bài nghe có khớp với tranh không?' % (i + 1), t, pics[i]) for i, t in enumerate(['T', 'F', 'F', 'T'])])
    rq = rows_q(S['III']['lines'])
    keys3 = ['When’s your birthday?', 'Can he cook?', 'What do you want to drink?', 'What do you do on Sundays?']
    rows = []
    for (im, q, opts), kq in zip(rq, keys3):
        rows.append((im, 'Chọn câu hỏi phù hợp với câu trả lời: ' + q.replace('–', '').replace('___________________?', '____?').strip(), opts))
    ex.mcq_text('r1', 'III. Tick the correct questions (chọn câu hỏi đúng).', rows, [('A' if o[0] == k else 'B') for (_, _, o), k in zip(rq, keys3)])
    ps = ' '.join(S['IV']['lines']); pp = imgs(ps)
    ex.fill('r2', 'IV. Fill in the blanks (nhìn tranh, điền từ vào chỗ trống).',
            [('Chỗ trống (%d): {_}' % (i + 1), [a] if a != 'play football' else ['play football'], pp[i]) for i, a in enumerate(['Singapore', 'play football', 'chips', 'lemonade'])], passage=passage(ps))
    ex.save()


# ============ ĐỀ 4
def de4():
    d, S, K, ex = gk1(4, ['thuvienhoclieu.com-Nghe-De-kiem-tra-giua-HK1-Anh-4-Global-De-4-TASK-1.mp3', 'thuvienhoclieu.com-Nghe-De-kiem-tra-giua-HK1-Anh-4-Global-De-4-TASK-2.mp3'])
    ex.mcq_words('l1', 'I. Listen and circle the correct words (nghe và chọn từ đúng).', rows_words(S['I']['lines']), ['B', 'C', 'B', 'A'], q='Nghe và chọn từ em nghe được.')
    pics = imgs(' '.join(S['II']['lines']))[:5]   # tranh a–e (câu ví dụ: a = 1)
    ex.number_pics('l2', 'II. Listen and number the pictures (nghe và đánh số tranh; tranh a là ví dụ = 1).', pics, list('abcde'), ['1', '4', '5', '2', '3'],
                   nums=['2', '3', '4', '5'], only=list('bcde'))
    rq = rows_q(S['III']['lines'])
    ans = ['I go to bed at nine o’clock.', 'I do housework.', 'I want some grapes.', 'No, she can’t.']
    ex.mcq_text('r1', 'III. Read and tick the correct sentences (nhìn tranh, chọn câu đúng).',
                [(im, q, o) for (im, q, o) in rq], ['A' if o[0] == a else 'B' for (_, _, o), a in zip(rq, ans)])
    ps = ' '.join(S['IV']['lines']); pp = imgs(ps)
    ex.fill('r2', 'IV. Fill in the blanks (nhìn tranh, điền từ vào chỗ trống).',
            [('Chỗ trống (%d): {_}' % (i + 1), [a], pp[i]) for i, a in enumerate(['get up', 'have breakfast', 'jam', 'milk'])], passage=passage(ps))
    ex.save()


if __name__ == '__main__':
    de1(); de2(); de3(); de4()
