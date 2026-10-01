"""Chuyển đổi 1 lần: Đề kiểm tra giữa HK1 Anh 11 (Đề 6) src/mt1/d6.txt -> units/mt1_test05.py (khung câu hỏi).
Dùng build_test() của gen_mt1_test04.py. Đáp án + giải thích: units/mt1_test05_dapan.py."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_mt1_test04 import build_test, dump, FIXES, ROOT

FIXES6 = [f for f in FIXES if 'high blood pressure' not in f[0]] + [
    ('signicantly', 'significantly'),        # nguồn gõ sai (Q11 D)
    (', wich also', ', which also'),         # Q17 a
    ('Last but on least', 'Last but not least'),   # Q17 b
]

if __name__ == '__main__':
    S = build_test('src/mt1/d6.txt', FIXES6, 'test05', 'Test 5 – Mid-term 1', 'assets/mt1/test05', 45,
                   {10: 'image1.png', 13: 'image2.png'}, {16, 17})
    dump(os.path.join(ROOT, 'units/mt1_test05.py'), S)
    n = 0
    for g in S['pages'][0]['groups']:
        n += len(g['items'])
        print(g['id'], len(g['items']), [it['id'] for it in g['items']][:1], g['instr'][:50])
    print('TOTAL', n)
