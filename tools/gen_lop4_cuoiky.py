# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from g4_exam import *
for hk, uname, ltxt in ((1, 'CuoiKy1', 'Cuối kỳ 1'), (2, 'CuoiKy2', 'Cuối kỳ 2')):
    for n in (1, 2, 3, 4):
        src = 'De-kiem-tra-cuoi-HK%d-Anh-4-Global-De-%d' % (hk, n)
        d = Dump(src)
        aud = 'thuvienhoclieu.com-Nghe-De-kiem-tra-cuoi-HK%d-Anh-4-Global-De-%d.mp3' % (hk, n)
        auds = [aud]
        ex = Exam('ck%d_de%d' % (hk, n), uname, '%s – Đề %d' % (ltxt, n), src, slug='test%02d' % n, minutes=35, warn_at=5, audio=auds)
        std_cuoi(ex, d, d.sec(), d.keys())
        ex.save()
