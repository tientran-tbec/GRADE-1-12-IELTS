# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g4_exam import *
for p in (1, 2, 3, 4):
    src = 'Luyen-nghe-anh-4-global-giua-HK1-Phan-%d' % p
    ex = Exam('gk1_nghe%d' % p, 'GiuaKy1', 'Giữa kỳ 1 – Luyện nghe phần %d' % p, src, slug='test%02d' % (4 + p), minutes=15, warn_at=3,
              audio=['thuvienhoclieu.com-Luyen-nghe-anh-4-global-giua-HK1-Phan-%d.mp3' % p])
    build_qn(ex, src)
    ex.save()
