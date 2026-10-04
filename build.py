# -*- coding: utf-8 -*-
"""Lớp BUILD: các hàm renderer + ghép trang HTML từ dữ liệu (units/*.py) và đáp án (units/*_dapan.py).
Chạy:  python3 build.py            (sinh toàn bộ WebBaiTap/ + index.html)
       python3 build.py lop11-u1-botro   (chỉ 1 bộ)
"""
import os, sys, json, re, html, importlib.util
import ielts
import ly
LY = {'cards': [], 'catalog': [], 'n': 0, 'labels': {}, 'order': []}   # nạp bởi ly.build() trong main
IELTS = {'cards': [], 'catalog': [], 'n': 0}   # nạp bởi ielts.build() trong main

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'WebBaiTap')
APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbyZ4UJgI763vPb4TZhKbKgxl6p-lGCQCJnZDqgCL9mHCVQpUzb4sbJGg89GLWSI-sQj/exec'   # update_links.py sẽ thay giá trị này
PAGES_URL = 'https://tientran-tbec.github.io/GRADE-1-12-IELTS/'

# (id bộ, file dữ liệu, file đáp án, thư mục lớp, thư mục unit, slug thư mục, ảnh)
REGISTRY = [
    # --- Lớp 3 ---
    ('lop3-u1-luyentap', 'units/lop3_u1_luyentap.py', 'units/lop3_u1_luyentap_dapan.py', 'Lop3', 'Unit1', 'luyentap', 'assets/lop3_u1/luyentap', ''),
    ('lop3-u1-test01', 'units/lop3_u1_test01.py', 'units/lop3_u1_test01_dapan.py', 'Lop3', 'Unit1', 'test01', 'assets/lop3_u1/test01', ''),
    ('lop3-u1-test02', 'units/lop3_u1_test02.py', 'units/lop3_u1_test02_dapan.py', 'Lop3', 'Unit1', 'test02', 'assets/lop3_u1/test02', ''),
    ('lop3-u1-test03', 'units/lop3_u1_test03.py', 'units/lop3_u1_test03_dapan.py', 'Lop3', 'Unit1', 'test03', 'assets/lop3_u1/test03', ''),
    ('lop3-u2-luyentap', 'units/lop3_u2_luyentap.py', 'units/lop3_u2_luyentap_dapan.py', 'Lop3', 'Unit2', 'luyentap', 'assets/lop3_u2/luyentap', ''),
    ('lop3-u2-test01', 'units/lop3_u2_test01.py', 'units/lop3_u2_test01_dapan.py', 'Lop3', 'Unit2', 'test01', 'assets/lop3_u2/test01', ''),
    ('lop3-u2-test02', 'units/lop3_u2_test02.py', 'units/lop3_u2_test02_dapan.py', 'Lop3', 'Unit2', 'test02', 'assets/lop3_u2/test02', ''),
    ('lop3-u2-test03', 'units/lop3_u2_test03.py', 'units/lop3_u2_test03_dapan.py', 'Lop3', 'Unit2', 'test03', 'assets/lop3_u2/test03', ''),
    ('lop3-u3-luyentap', 'units/lop3_u3_luyentap.py', 'units/lop3_u3_luyentap_dapan.py', 'Lop3', 'Unit3', 'luyentap', 'assets/lop3_u3/luyentap', ''),
    ('lop3-u3-test01', 'units/lop3_u3_test01.py', 'units/lop3_u3_test01_dapan.py', 'Lop3', 'Unit3', 'test01', 'assets/lop3_u3/test01', ''),
    ('lop3-u3-test02', 'units/lop3_u3_test02.py', 'units/lop3_u3_test02_dapan.py', 'Lop3', 'Unit3', 'test02', 'assets/lop3_u3/test02', ''),
    ('lop3-u3-test03', 'units/lop3_u3_test03.py', 'units/lop3_u3_test03_dapan.py', 'Lop3', 'Unit3', 'test03', 'assets/lop3_u3/test03', ''),
    ('lop3-u4-luyentap', 'units/lop3_u4_luyentap.py', 'units/lop3_u4_luyentap_dapan.py', 'Lop3', 'Unit4', 'luyentap', 'assets/lop3_u4/luyentap', ''),
    ('lop3-u4-test01', 'units/lop3_u4_test01.py', 'units/lop3_u4_test01_dapan.py', 'Lop3', 'Unit4', 'test01', 'assets/lop3_u4/test01', ''),
    ('lop3-u4-test02', 'units/lop3_u4_test02.py', 'units/lop3_u4_test02_dapan.py', 'Lop3', 'Unit4', 'test02', 'assets/lop3_u4/test02', ''),
    ('lop3-u4-test03', 'units/lop3_u4_test03.py', 'units/lop3_u4_test03_dapan.py', 'Lop3', 'Unit4', 'test03', 'assets/lop3_u4/test03', ''),
    ('lop3-u5-luyentap', 'units/lop3_u5_luyentap.py', 'units/lop3_u5_luyentap_dapan.py', 'Lop3', 'Unit5', 'luyentap', 'assets/lop3_u5/luyentap', ''),
    ('lop3-u5-test01', 'units/lop3_u5_test01.py', 'units/lop3_u5_test01_dapan.py', 'Lop3', 'Unit5', 'test01', 'assets/lop3_u5/test01', ''),
    ('lop3-u5-test02', 'units/lop3_u5_test02.py', 'units/lop3_u5_test02_dapan.py', 'Lop3', 'Unit5', 'test02', 'assets/lop3_u5/test02', ''),
    ('lop3-u5-test03', 'units/lop3_u5_test03.py', 'units/lop3_u5_test03_dapan.py', 'Lop3', 'Unit5', 'test03', 'assets/lop3_u5/test03', ''),
    ('lop3-u6-luyentap', 'units/lop3_u6_luyentap.py', 'units/lop3_u6_luyentap_dapan.py', 'Lop3', 'Unit6', 'luyentap', 'assets/lop3_u6/luyentap', ''),
    ('lop3-u6-test01', 'units/lop3_u6_test01.py', 'units/lop3_u6_test01_dapan.py', 'Lop3', 'Unit6', 'test01', 'assets/lop3_u6/test01', ''),
    ('lop3-u6-test02', 'units/lop3_u6_test02.py', 'units/lop3_u6_test02_dapan.py', 'Lop3', 'Unit6', 'test02', 'assets/lop3_u6/test02', ''),
    ('lop3-u6-test03', 'units/lop3_u6_test03.py', 'units/lop3_u6_test03_dapan.py', 'Lop3', 'Unit6', 'test03', 'assets/lop3_u6/test03', ''),
    ('lop3-u7-luyentap', 'units/lop3_u7_luyentap.py', 'units/lop3_u7_luyentap_dapan.py', 'Lop3', 'Unit7', 'luyentap', 'assets/lop3_u7/luyentap', ''),
    ('lop3-u7-test01', 'units/lop3_u7_test01.py', 'units/lop3_u7_test01_dapan.py', 'Lop3', 'Unit7', 'test01', 'assets/lop3_u7/test01', ''),
    ('lop3-u7-test02', 'units/lop3_u7_test02.py', 'units/lop3_u7_test02_dapan.py', 'Lop3', 'Unit7', 'test02', 'assets/lop3_u7/test02', ''),
    ('lop3-u7-test03', 'units/lop3_u7_test03.py', 'units/lop3_u7_test03_dapan.py', 'Lop3', 'Unit7', 'test03', 'assets/lop3_u7/test03', ''),
    ('lop3-u8-luyentap', 'units/lop3_u8_luyentap.py', 'units/lop3_u8_luyentap_dapan.py', 'Lop3', 'Unit8', 'luyentap', 'assets/lop3_u8/luyentap', ''),
    ('lop3-u8-test01', 'units/lop3_u8_test01.py', 'units/lop3_u8_test01_dapan.py', 'Lop3', 'Unit8', 'test01', 'assets/lop3_u8/test01', ''),
    ('lop3-u8-test02', 'units/lop3_u8_test02.py', 'units/lop3_u8_test02_dapan.py', 'Lop3', 'Unit8', 'test02', 'assets/lop3_u8/test02', ''),
    ('lop3-u8-test03', 'units/lop3_u8_test03.py', 'units/lop3_u8_test03_dapan.py', 'Lop3', 'Unit8', 'test03', 'assets/lop3_u8/test03', ''),
    ('lop3-u9-luyentap', 'units/lop3_u9_luyentap.py', 'units/lop3_u9_luyentap_dapan.py', 'Lop3', 'Unit9', 'luyentap', 'assets/lop3_u9/luyentap', ''),
    ('lop3-u9-test01', 'units/lop3_u9_test01.py', 'units/lop3_u9_test01_dapan.py', 'Lop3', 'Unit9', 'test01', 'assets/lop3_u9/test01', ''),
    ('lop3-u9-test02', 'units/lop3_u9_test02.py', 'units/lop3_u9_test02_dapan.py', 'Lop3', 'Unit9', 'test02', 'assets/lop3_u9/test02', ''),
    ('lop3-u9-test03', 'units/lop3_u9_test03.py', 'units/lop3_u9_test03_dapan.py', 'Lop3', 'Unit9', 'test03', 'assets/lop3_u9/test03', ''),
    ('lop3-u10-luyentap', 'units/lop3_u10_luyentap.py', 'units/lop3_u10_luyentap_dapan.py', 'Lop3', 'Unit10', 'luyentap', 'assets/lop3_u10/luyentap', ''),
    ('lop3-u10-test01', 'units/lop3_u10_test01.py', 'units/lop3_u10_test01_dapan.py', 'Lop3', 'Unit10', 'test01', 'assets/lop3_u10/test01', ''),
    ('lop3-u10-test02', 'units/lop3_u10_test02.py', 'units/lop3_u10_test02_dapan.py', 'Lop3', 'Unit10', 'test02', 'assets/lop3_u10/test02', ''),
    ('lop3-u10-test03', 'units/lop3_u10_test03.py', 'units/lop3_u10_test03_dapan.py', 'Lop3', 'Unit10', 'test03', 'assets/lop3_u10/test03', ''),
    ('lop3-hk1-de01', 'units/lop3_hk1_de01.py', 'units/lop3_hk1_de01_dapan.py', 'Lop3', 'CuoiKy1', 'test01', 'assets/lop3_hk1/de01', 'audio/lop3_hk1_de01.mp3'),
    ('lop3-hk1-de02', 'units/lop3_hk1_de02.py', 'units/lop3_hk1_de02_dapan.py', 'Lop3', 'CuoiKy1', 'test02', 'assets/lop3_hk1/de02', 'audio/lop3_hk1_de02.mp3'),
    ('lop3-hk1-de03', 'units/lop3_hk1_de03.py', 'units/lop3_hk1_de03_dapan.py', 'Lop3', 'CuoiKy1', 'test03', 'assets/lop3_hk1/de03', 'audio/lop3_hk1_de03.mp3'),
    ('lop3-hk1-de04', 'units/lop3_hk1_de04.py', 'units/lop3_hk1_de04_dapan.py', 'Lop3', 'CuoiKy1', 'test04', 'assets/lop3_hk1/de04', 'audio/lop3_hk1_de04.mp3'),
    ('lop3-hk1-de05', 'units/lop3_hk1_de05.py', 'units/lop3_hk1_de05_dapan.py', 'Lop3', 'CuoiKy1', 'test05', 'assets/lop3_hk1/de05', 'audio/lop3_hk1_de05.mp3'),
    # --- Lớp 10 · Unit 1 ---
    ('lop10-u1-luyentap', 'units/lop10_u1_luyentap.py', 'units/lop10_u1_luyentap_dapan.py', 'Lop10', 'Unit1', 'luyentap', 'assets/lop10_u1/luyentap', 'audio/lop10_u1_luyentap_nghe.mp3'),
    ('lop10-u1-botro', 'units/lop10_u1_botro.py', 'units/lop10_u1_botro_dapan.py', 'Lop10', 'Unit1', 'botro', 'assets/lop10_u1/botro', 'audio/lop10_u1_botro_nghe.mp3'),
    ('lop10-u1-chuyensau', 'units/lop10_u1_chuyensau.py', 'units/lop10_u1_chuyensau_dapan.py', 'Lop10', 'Unit1', 'chuyensau', 'assets/lop10_u1/chuyensau', 'audio/lop10_u1_chuyensau_nghe.mp3'),
    ('lop10-u2-luyentap', 'units/lop10_u2_luyentap.py', 'units/lop10_u2_luyentap_dapan.py', 'Lop10', 'Unit2', 'luyentap', 'assets/lop10_u2/luyentap', 'audio/lop10_u2_luyentap_nghe.mp3'),
    ('lop10-u2-botro', 'units/lop10_u2_botro.py', 'units/lop10_u2_botro_dapan.py', 'Lop10', 'Unit2', 'botro', 'assets/lop10_u2/botro', 'audio/lop10_u2_botro_nghe.mp3'),
    ('lop10-u2-chuyensau', 'units/lop10_u2_chuyensau.py', 'units/lop10_u2_chuyensau_dapan.py', 'Lop10', 'Unit2', 'chuyensau', 'assets/lop10_u2/chuyensau', 'audio/lop10_u2_chuyensau_nghe.mp3'),
    ('lop10-u3-luyentap', 'units/lop10_u3_luyentap.py', 'units/lop10_u3_luyentap_dapan.py', 'Lop10', 'Unit3', 'luyentap', 'assets/lop10_u3/luyentap', 'audio/lop10_u3_luyentap_nghe.mp3'),
    ('lop10-u3-botro', 'units/lop10_u3_botro.py', 'units/lop10_u3_botro_dapan.py', 'Lop10', 'Unit3', 'botro', 'assets/lop10_u3/botro', 'audio/lop10_u3_botro_nghe.mp3'),
    ('lop10-u3-chuyensau', 'units/lop10_u3_chuyensau.py', 'units/lop10_u3_chuyensau_dapan.py', 'Lop10', 'Unit3', 'chuyensau', 'assets/lop10_u3/chuyensau', 'audio/lop10_u3_chuyensau_nghe.mp3'),
    ('lop11-u1-botro', 'units/lop11_u1_botro.py', 'units/lop11_u1_botro_dapan.py', 'Lop11', 'Unit1', 'botro', 'assets/lop11_u1/botro', 'audio/lop11_u1_botro_nghe.mp3'),
    ('lop11-u1-4kn', 'units/lop11_u1_4kn.py', 'units/lop11_u1_4kn_dapan.py', 'Lop11', 'Unit1', '4kn', 'assets/lop11_u1/4kn', 'audio/lop11_u1_4kn_nghe.mp3'),
    ('lop11-u2-botro', 'units/lop11_u2_botro.py', 'units/lop11_u2_botro_dapan.py', 'Lop11', 'Unit2', 'botro', 'assets/lop11_u2/botro', 'audio/lop11_u2_botro_nghe.mp3'),
    ('lop11-u2-4kn', 'units/lop11_u2_4kn.py', 'units/lop11_u2_4kn_dapan.py', 'Lop11', 'Unit2', '4kn', 'assets/lop11_u2/4kn', 'audio/lop11_u2_4kn_nghe.mp3'),
    ('lop11-u3-botro', 'units/lop11_u3_botro.py', 'units/lop11_u3_botro_dapan.py', 'Lop11', 'Unit3', 'botro', 'assets/lop11_u3/botro', 'audio/lop11_u3_botro_nghe.mp3'),
    ('lop11-u3-4kn', 'units/lop11_u3_4kn.py', 'units/lop11_u3_4kn_dapan.py', 'Lop11', 'Unit3', '4kn', 'assets/lop11_u3/4kn', 'audio/lop11_u3_4kn_nghe.mp3'),
    # --- Lớp 11 · Mid-term 1 ---
    ('lop11-mt1-ontap', 'units/mt1_ontap.py', 'units/mt1_ontap_dapan.py', 'Lop11', 'MidTerm1', 'ontap', 'assets/mt1/ontap', 'audio/mt1_ontap.mp3'),
    ('lop11-mt1-test01', 'units/mt1_test01.py', 'units/mt1_test01_dapan.py', 'Lop11', 'MidTerm1', 'test01', 'assets/mt1/test01', 'audio/mt1_test01.mp3'),
    ('lop11-mt1-test02', 'units/mt1_test02.py', 'units/mt1_test02_dapan.py', 'Lop11', 'MidTerm1', 'test02', 'assets/mt1/test02', 'audio/mt1_test02.mp3'),
    ('lop11-mt1-test03', 'units/mt1_test03.py', 'units/mt1_test03_dapan.py', 'Lop11', 'MidTerm1', 'test03', 'assets/mt1/test03', 'audio/mt1_test03.mp3'),
    ('lop11-mt1-test04', 'units/mt1_test04.py', 'units/mt1_test04_dapan.py', 'Lop11', 'MidTerm1', 'test04', 'assets/mt1/test04', 'audio/mt1_test04.mp3'),
    ('lop11-mt1-test05', 'units/mt1_test05.py', 'units/mt1_test05_dapan.py', 'Lop11', 'MidTerm1', 'test05', 'assets/mt1/test05', 'audio/mt1_test05.mp3'),
    ('lop11-mt1-test06', 'units/mt1_test06.py', 'units/mt1_test06_dapan.py', 'Lop11', 'MidTerm1', 'test06', 'assets/mt1/test06', 'audio/mt1_test06.mp3'),
    ('lop11-mt1-test07', 'units/mt1_test07.py', 'units/mt1_test07_dapan.py', 'Lop11', 'MidTerm1', 'test07', 'assets/mt1/test07', 'audio/mt1_test07.mp3'),
    ('lop11-mt1-test08', 'units/mt1_test08.py', 'units/mt1_test08_dapan.py', 'Lop11', 'MidTerm1', 'test08', 'assets/mt1/test08', 'audio/mt1_test08.mp3'),
    ('lop11-mt1-test09', 'units/mt1_test09.py', 'units/mt1_test09_dapan.py', 'Lop11', 'MidTerm1', 'test09', 'assets/mt1/test09', 'audio/mt1_test09.mp3'),
    ('lop11-mt1-test10', 'units/mt1_test10.py', 'units/mt1_test10_dapan.py', 'Lop11', 'MidTerm1', 'test10', 'assets/mt1/test10', 'audio/mt1_test10.mp3'),
    ('lop11-mt1-test11', 'units/mt1_test11.py', 'units/mt1_test11_dapan.py', 'Lop11', 'MidTerm1', 'test11', 'assets/mt1/test11', 'audio/mt1_test11.mp3'),
    ('lop11-mt1-test12', 'units/mt1_test12.py', 'units/mt1_test12_dapan.py', 'Lop11', 'MidTerm1', 'test12', 'assets/mt1/test12', 'audio/mt1_test12.mp3'),
    ('lop11-mt1-test13', 'units/mt1_test13.py', 'units/mt1_test13_dapan.py', 'Lop11', 'MidTerm1', 'test13', 'assets/mt1/test13', 'audio/mt1_test13.mp3'),
]

try:
    exec(open(os.path.join(ROOT, 'units/registry_lop4.py'), encoding='utf8').read(), globals())
    REGISTRY += ENTRIES
except FileNotFoundError:
    pass
import json as _json, glob as _glob
for _f in sorted(_glob.glob(os.path.join(ROOT, 'units/reg/*.json'))):
    REGISTRY.append(tuple(_json.load(open(_f, encoding='utf8'))))


def load_py(path, attr):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return None
    spec = importlib.util.spec_from_file_location('m_' + os.path.basename(p)[:-3], p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return getattr(m, attr, None)


def load_answers(path):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return {}, {}
    spec = importlib.util.spec_from_file_location('ans_' + os.path.basename(p)[:-3], p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return getattr(m, 'ANS', {}), getattr(m, 'EXPLANATIONS', {})


# ------------------------------------------------------------------ renderers
def esc_attr(s):
    return html.escape(str(s), quote=True)


def radio_item(it, plain=False, short=True):
    """Trắc nghiệm 1 đáp án (mcq)."""
    opts = it['o']
    cols = ' cols' if (len(opts) <= 4 and all(len(re.sub(r'<[^>]+>', '', o)) <= 22 for o in opts)) else ''
    out = ['<div class="opts%s">' % cols]
    for i, o in enumerate(opts):
        L = 'ABCDEFGHIJ'[i]
        if it.get('plain'):
            out.append('<label class="opt"><input type="radio" name="%s" value="%s"><span>%s</span></label>' % (esc_attr(it['id']), esc_attr(o), o))
        else:
            out.append('<label class="opt"><input type="radio" name="%s" value="%s"><span><b>%s.</b> %s</span></label>' % (esc_attr(it['id']), L, L, o))
    out.append('</div>')
    return ''.join(out)


def tf_item(it):
    vals = [('T', 'True'), ('F', 'False')] + ([('NG', 'Not given')] if it['t'] == 'tfng' else [])
    out = ['<div class="opts cols">']
    for v, lab in vals:
        out.append('<label class="opt"><input type="radio" name="%s" value="%s"><span>%s</span></label>' % (esc_attr(it['id']), v, lab))
    out.append('</div>')
    return ''.join(out)


LONG_GROUPS = {'vg8', 'kt-rw', 'wr1', 'wr2', 'vg9', 'vg10', 'vg11', 'kt-cue'}   # nhóm viết lại câu: dùng ô nhiều dòng, kéo giãn được


def text_item(it, test_mode):
    """Điền từ: thay mỗi {_} bằng ô nhập."""
    q = it['q']
    n = q.count('{_}')
    if n == 0:
        q = q + ' {_}'
        n = 1
    k = [0]

    long_ = bool(it.get('long')) or it['id'].split('.')[0] in LONG_GROUPS or it['id'].startswith('wr')

    def rep(_):
        i = k[0]
        k[0] += 1
        if long_:
            return '<br><textarea class="blank long" rows="3" data-id="%s" data-i="%d" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Viết câu hoàn chỉnh của bạn tại đây…" aria-label="ô viết %d"></textarea>' % (esc_attr(it['id']), i, i + 1)
        return '<input class="blank" type="text" data-id="%s" data-i="%d" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="ô điền %d">' % (esc_attr(it['id']), i, i + 1)
    s = re.sub(r'\{_\}', rep, q)
    extra = ''
    if it.get('hint'):
        extra += '<span class="hint">(%s)</span>' % html.escape(it['hint'])
    if it.get('nwords'):
        extra += '<span class="hint">(%d từ)</span>' % it['nwords']
    btn = '' if test_mode else ' <button class="btn sm chk" type="button">Kiểm tra</button>'
    return '<div class="stem">%s %s%s</div>' % (s, extra, btn)


def match_item(it, test_mode, imgbase):
    """Nối: mỗi dòng bên trái có 1 ô chọn đáp án bên phải. ANS = {'blanks': [[đáp án 1], [đáp án 2], ...]}."""
    rows = []
    for i, L in enumerate(it['left']):
        if isinstance(L, dict):
            lab = ('<img class="mpic" src="%s/%s" alt="">' % (imgbase, L['img']) if L.get('img') else '') + html.escape(L.get('t', ''))
        else:
            lab = L
        opts = '<option value="">— chọn —</option>' + ''.join('<option value="%s">%s</option>' % (esc_attr(o), html.escape(o)) for o in it['o'])
        rows.append('<div class="mrow"><span class="ml">%s</span><span class="ma">→</span><select class="blank" data-id="%s" data-i="%d" aria-label="chọn %d">%s</select></div>'
                    % (lab, esc_attr(it['id']), i, i + 1, opts))
    btn = '' if test_mode else '<p><button class="btn sm chk" type="button">Kiểm tra</button></p>'
    return ('<div class="stem">%s</div>' % it['q'] if it.get('q') else '') + '<div class="match">%s</div>%s' % (''.join(rows), btn)


def order_item(it, test_mode):
    """Bấm từ xếp câu. words = các từ (đã xáo sẵn); ANS = câu đúng (chuỗi hoặc list chấp nhận)."""
    chips = ''.join('<button type="button" class="chip" data-w="%s">%s</button>' % (esc_attr(w), html.escape(w)) for w in it['words'])
    btn = '' if test_mode else ' <button class="btn sm chk" type="button">Kiểm tra</button>'
    return ('<div class="stem">%s</div>' % it['q'] if it.get('q') else '') + (
        '<div class="ord"><div class="ord-ans" aria-label="câu của bạn"></div><div class="ord-bank">%s</div>'
        '<input type="hidden" class="blank" data-id="%s" data-i="0"><button type="button" class="btn sm ghost ord-clear">Xoá hết</button>%s</div>'
        % (chips, esc_attr(it['id']), btn))


def open_item(it, test_mode):
    btn = '' if test_mode else '<p><button class="btn sm chk" type="button">Xem đáp án mẫu</button></p>'
    return '<textarea class="open" rows="9" placeholder="Viết câu trả lời của bạn tại đây…"></textarea>' + btn


def bank_box(words):
    return '<div class="bank"><b>Từ/cụm từ cho sẵn:</b>%s</div>' % ''.join('<span class="w">%s</span>' % html.escape(w) for w in words)


def audio_player(src, max_plays=0):
    mp = ' Số lần nghe tối đa: %d.' % max_plays if max_plays else ''
    return ('<div class="audio"><audio id="audio" controls preload="metadata" src="%s"></audio>'
            '<div class="plays" id="plays">Đã nghe: 0%s lần.%s</div></div>' % (esc_attr(src), ('/%d' % max_plays) if max_plays else '', mp))


def qgroup_open(g):
    s = '<section class="card group" id="g-%s">' % esc_attr(g['id'])
    if g.get('instr'):
        s += '<div class="instr">%s</div>' % html.escape(g['instr'])
    return s


def qgroup_close():
    return '</section>'


def render_item(it, num, test_mode, imgbase):
    t = it['t']
    body = ''
    if it.get('say'):   # nút nghe: trình duyệt đọc to (không cần file mp3)
        body += '<button type="button" class="say" data-say="%s">🔊 Nghe</button> ' % esc_attr(it['say'])
    if it.get('img'):
        body += '<img class="pic%s" src="%s/%s" alt="Hình minh hoạ câu %s">' % (' wide' if it.get('wide') else '', imgbase, it['img'], num)
    if t == 'mcq':
        if it.get('q'):
            body += '<div class="stem">%s</div>' % it['q']
        body += radio_item(it)
    elif t in ('tf', 'tfng'):
        body += '<div class="stem">%s</div>' % it['q'] + tf_item(it)
    elif t == 'fill':
        body += text_item(it, test_mode)
    elif t == 'match':
        body += match_item(it, test_mode, imgbase)
    elif t == 'order':
        body += order_item(it, test_mode)
    elif t == 'open':
        body += '<div class="stem">%s</div>' % it['q'] + open_item(it, test_mode)
    if t in ('match', 'order'):
        t = 'fill'
    return ('<div class="q" data-id="%s" data-t="%s"><div class="qn">%s</div><div class="qb">%s<div class="exp" data-for="%s" hidden></div></div></div>'
            % (esc_attr(it['id']), t, num, body, esc_attr(it['id'])))


# ------------------------------------------------------------------ ghép trang
def nav_tabs(S, cur_id, slug):
    items = ([('ly-thuyet', 'Lý thuyết')] if S.get('theory') else []) + [(p['id'], p['title']) for p in S['pages']]
    return '<nav class="tabs">%s<a href="../../../../index.html">⌂ Trang chủ</a></nav>' % ''.join(
        '<a href="%s.html"%s>%s</a>' % (i, ' class="cur"' if i == cur_id else '', html.escape(t)) for i, t in items)


def json_script(obj):
    return json.dumps(obj, ensure_ascii=False).replace('</', '<\\/')


import time as _t
BV = str(int(_t.time()))   # chống cache trình duyệt/GitHub Pages cho engine
AUTH_HEAD = '<script>window.GN_URL="%s";window.GN_ROOT="%s";</script><script src="%sengine/auth.js?v='+BV+'"></script><script>GNAuth.require()</script>'


def page_shell(title, sub, body, extra_head='', badge='', h1=None, sid=''):
    return _page_shell(title, sub, body, extra_head, badge, h1, sid).replace('@@V@@', BV)


def _page_shell(title, sub, body, extra_head='', badge='', h1=None, sid=''):
    return ('<!doctype html>\n<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><link rel="stylesheet" href="../../../../engine/engine.css?v=@@V@@">%s%s</head><body>'
            '<header class="top"><div class="wrap">%s<h1>%s</h1><div class="sub">%s</div>%%NAV%%</div></header>%s'
            '<script>GNAuth.chip(".top .wrap");GNAuth.verify();</script>%s</body></html>'
            % (html.escape(title), AUTH_HEAD % (APPS_SCRIPT_URL, '../../../../', '../../../../') + ('<script>GNAuth.requireSet(%s)</script>' % json.dumps(sid) if sid else ''), extra_head, badge, html.escape(h1 or title), html.escape(sub), body,
               ('<script>window.GN_SET=%s</script><script src="../../../../engine/feedback.js?v=@@V@@"></script>' % json.dumps(sid)) if sid else ''))


def build_theory_page(S, slug):
    body = '<div class="wrap"><div class="card theory">%s</div></div>' % S['theory']
    s = page_shell('Lý thuyết – ' + S['title'], 'Từ vựng, phát âm, ngữ pháp trọng tâm của Unit', body, badge='<span class="badge">Lý thuyết</span>', h1='Lý thuyết', sid=S['id'])
    return s.replace('%NAV%', nav_tabs(S, 'ly-thuyet', slug))


def build_quiz_page(S, P, ANS, EXP, slug, imgbase, audio_src):
    test_mode = P['mode'] == 'test'
    order, items_meta = [], {}
    body = ['<div class="wrap">']
    if P.get('pending'):
        body.append('<div class="pending"><b>Lưu ý:</b> Phần này đang chờ cập nhật transcript và đáp án. Bạn có thể xem câu hỏi, nhưng chưa tính điểm.</div>')
    if test_mode:
        body.append('<div class="card rules"><b>📋 Quy định làm bài</b><ul><li>Thời gian: <b>%d phút</b>. Còn 10 phút hệ thống nhắc; hết giờ có thêm 5 phút gia hạn rồi tự động nộp.</li><li>Bài làm ở chế độ <b>toàn màn hình</b>. Chuyển tab, mất focus, thoát toàn màn hình đều bị ghi nhận và báo cho giáo viên.</li><li>Không dùng chuột phải, sao chép/dán, phím tắt. Đáp án và giải thích chi tiết hiển thị sau khi nộp bài.</li></ul></div>' % P['minutes'])
    body.append('<div class="result" id="result" hidden></div>')
    if P.get('audio'):
        body.append(audio_player(audio_src, P.get('audio_max_plays', 0)))
    for g in P['groups']:
        body.append(qgroup_open(g))
        if g.get('note'):
            body.append('<div class="theory">%s</div>' % g['note'])
        if g.get('passage'):
            body.append('<div class="passage">%s</div>' % g['passage'])
        if g.get('bank'):
            body.append(bank_box(g['bank']))
        for idx, it in enumerate(g['items'], 1):
            if g['id'] in LONG_GROUPS and it['t'] == 'fill':
                it['long'] = True
            num = int(it['id'].split('.')[-1]) if test_mode else idx
            body.append(render_item(it, num, test_mode, imgbase))
            order.append(it['id'])
            items_meta[it['id']] = {'t': 'fill' if it['t'] in ('match', 'order') else it['t'], 'g': g['id']}
        body.append(qgroup_close())
    body.append('</div>')
    # thanh dưới
    bar = ('<div class="bar"><div class="prog"><i id="progBar"></i></div><div class="in">%s<span class="stat grow" id="stat"></span>%s%s</div></div>'
           % ('<span class="timer" id="timer">--:--</span>' if test_mode else '',
              '' if P.get('pending') else '<button class="btn ghost" id="reset" type="button">Làm lại</button>',
              '' if P.get('pending') else '<button class="btn" id="submit" type="button">%s</button>' % ('Nộp bài' if test_mode else 'Nộp kết quả')))
    modal = ('<div class="modal" id="startModal"><div class="box"><h3>%s</h3><p>Nhập thông tin để hệ thống ghi nhận kết quả.</p>'
             '<label>Họ và tên<input type="text" id="stName" autocomplete="name"></label>'
             '<label>Lớp<input type="text" id="stClass"></label><div id="stErr" style="color:var(--bad)"></div>'
             '<button class="btn" id="startBtn" type="button">%s</button> %s</div></div>'
             % ('Bắt đầu làm bài kiểm tra' if test_mode else 'Bắt đầu luyện tập', 'Bắt đầu làm bài' if test_mode else 'Bắt đầu',
                '' if test_mode else '<button class="btn ghost" id="skipBtn" type="button">Luyện tập không ghi tên</button>'))
    warn = '<div class="modal" id="warnModal" hidden><div class="box"><h3>Nhắc giờ</h3><p id="warnText"></p><button class="btn" id="warnOk" type="button">Đã hiểu</button></div></div><div class="toast" id="toast" hidden></div>'
    if test_mode:
        warn += ('<div class="modal" id="timeUpModal" hidden><div class="box"><h3>⏰ Đã hết giờ làm bài</h3><p>Bạn có thêm <b>5 phút</b> để hoàn tất. Hết 5 phút bài sẽ tự động nộp.</p>'
                 '<button class="btn" id="timeUpSubmit" type="button">Nộp bài ngay</button> <button class="btn ghost" id="timeUpBack" type="button">Làm tiếp</button></div></div>'
                 '<div class="modal fsov" id="fsOverlay" hidden><div class="box"><h3>⚠ Bạn đã thoát toàn màn hình</h3><p>Hành vi này đã được ghi nhận. Hãy quay lại chế độ toàn màn hình để tiếp tục làm bài.</p>'
                 '<button class="btn" id="fsBack" type="button">Vào toàn màn hình</button></div></div>')
    cfg = {'setId': S['id'], 'pageId': P['id'], 'mode': P['mode'], 'minutes': P.get('minutes', 0), 'warnAt': P.get('warn_at', 10 if test_mode else 0),
           'url': APPS_SCRIPT_URL, 'audioMaxPlays': P.get('audio_max_plays', 0), 'lockSeek': bool(P.get('lock_seek')),
           'order': order, 'items': items_meta,
           'ANS': {i: ANS[i] for i in order if i in ANS}, 'EXP': {i: EXP[i] for i in order if i in EXP}}
    scripts = '<script>window.QUIZ=%s;</script><script src="../../../../engine/engine.js?v=@@V@@"></script><script src="../../../../engine/tools.js?v=@@V@@"></script>' % json_script(cfg)
    badge = '<span class="badge%s">%s</span>' % (' test' if test_mode else '', 'Kiểm tra' if test_mode else 'Luyện tập')
    sub = '%s  ·  %d câu' % (S['title'], len(order))
    s = page_shell(P['title'] + ' – ' + S['title'], sub, ''.join(body) + bar + modal + warn + scripts, badge=badge, h1=P['title'], sid=S['id'])
    return s.replace('%NAV%', nav_tabs(S, P['id'], slug))


def apply_fixes(sid, S, ANS, EXP):
    """Áp dụng units/fixes.py (sửa đáp án/đề/giải thích sau khi sinh dữ liệu). Báo lỗi nếu id không tồn tại."""
    FX = (load_py('units/fixes.py', 'FIXES') or {}).get(sid, {})
    if not FX:
        return
    items = {it['id']: it for P in S['pages'] for g in P['groups'] for it in g['items']}
    for iid, f in FX.items():
        if iid not in items:
            raise SystemExit('fixes.py: %s không có câu %s' % (sid, iid))
        it = items[iid]
        if 'ans' in f:
            ANS[iid] = f['ans']
        if 'exp' in f:
            EXP[iid] = f['exp']
        if 'exp_add' in f:
            EXP[iid] = (EXP.get(iid, '') + ' ' + f['exp_add']).strip()
        if 'q' in f:
            it['q'] = f['q']
        for k, txt in (f.get('o') or {}).items():
            it['o'][k] = txt
    print('  [fixes] %s: %d câu đã sửa' % (sid, len(FX)))


def build_set(entry):
    sid, data_p, ans_p, gdir, udir, slug, imgdir, audio = entry
    S = load_py(data_p, 'SET')
    if S is None:
        return None, []   # bộ chưa soạn xong → bỏ qua
    ANS, EXP = load_answers(ans_p)
    apply_fixes(sid, S, ANS, EXP)
    d = os.path.join(OUT, gdir, udir, slug)
    os.makedirs(d, exist_ok=True)
    imgbase = '../../../../' + imgdir
    audio_src = '../../../../' + audio
    pages = []
    if S.get('theory'):
        with open(os.path.join(d, 'ly-thuyet.html'), 'w', encoding='utf8') as f:
            f.write(build_theory_page(S, slug))
    for P in S['pages']:
        with open(os.path.join(d, P['id'] + '.html'), 'w', encoding='utf8') as f:
            f.write(build_quiz_page(S, P, ANS, EXP, slug, imgbase, audio_src))
        pages.append((P['id'], P['title'], P['mode'], sum(len(g['items']) for g in P['groups'])))
    return S, pages


INDEX_CSS = """
:root{--bg:#f5f4ff;--card:#fff;--ink:#1f2140;--mut:#6b6f8d;--line:#e6e4f7;--pri:#6c4cf5;--pri2:#ff5fa2;--test:#e8590c;--sb:#ffffff}
@media(prefers-color-scheme:dark){:root{--bg:#14152a;--card:#1d1f3a;--ink:#eceefb;--mut:#a3a7c9;--line:#2c2f55;--sb:#191b34}}
[hidden]{display:none!important}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.top{position:sticky;top:0;z-index:30;background:linear-gradient(90deg,var(--pri),var(--pri2));color:#fff;display:flex;align-items:center;gap:12px;padding:10px 16px}
.top h1{font-size:17px;margin:0;flex:1}.top button{background:rgba(255,255,255,.2);border:0;color:#fff;border-radius:10px;padding:8px 12px;font-size:15px;cursor:pointer}
.locked{display:none!important}.expired{opacity:.5;pointer-events:none;filter:grayscale(.6)}.duem{color:#b45309;font-weight:600}.menu{display:none}.gn-chip{display:flex;align-items:center;gap:12px;flex-wrap:wrap;font-size:14px}.gn-chip small{opacity:.8}.gn-chip a{color:#fff;margin-left:10px;text-decoration:underline;text-underline-offset:3px;white-space:nowrap}
.layout{display:grid;grid-template-columns:270px 1fr;min-height:calc(100vh - 52px)}
.sb{background:var(--sb);border-right:1px solid var(--line);padding:18px 16px;position:sticky;top:52px;height:calc(100vh - 52px);overflow:auto}
.sb h4{margin:18px 0 8px;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--mut)}.sb h4:first-child{margin-top:0}
.sb input[type=search]{width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--ink);font-size:15px}
.fl{display:flex;flex-direction:column;gap:4px}
.f{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:9px 12px;border-radius:10px;border:0;background:none;color:var(--ink);font-size:15px;text-align:left;cursor:pointer}
.f:hover{background:var(--bg)}.f.on{background:linear-gradient(90deg,var(--pri),var(--pri2));color:#fff;font-weight:600}
.f small{opacity:.75;font-size:12px}.f[disabled]{opacity:.4;cursor:not-allowed}
.seg{display:flex;gap:6px;flex-wrap:wrap}.seg .f{border:1px solid var(--line);padding:7px 11px;flex:1;justify-content:center}.seg .f.on{border-color:transparent}.seg.kinds{display:grid;grid-template-columns:1fr 1fr}.seg.kinds .f{white-space:nowrap;padding:7px 8px}
.reset{margin-top:18px;width:100%;padding:9px;border:1px dashed var(--line);border-radius:10px;background:none;color:var(--mut);cursor:pointer}
main{padding:22px 24px 60px;max-width:1100px;width:100%}
.bar{display:flex;align-items:baseline;gap:12px;margin-bottom:14px;flex-wrap:wrap}.bar h2{margin:0;font-size:22px}.bar span{color:var(--mut)}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:16px 18px;margin-bottom:16px;box-shadow:0 2px 10px rgba(80,60,200,.05)}
.settitle{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:12px}.settitle h3{margin:0;font-size:17px}
.chip{background:var(--bg);color:var(--pri);border:1px solid var(--line);border-radius:999px;padding:3px 10px;font-size:12px;font-weight:600}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.tile{display:flex;flex-direction:column;gap:2px;padding:12px;border-radius:14px;border:1px solid var(--line);text-decoration:none;color:var(--ink);background:var(--bg);transition:.15s}
.tile:hover{transform:translateY(-2px);border-color:var(--pri);box-shadow:0 6px 16px rgba(108,76,245,.18)}
.tile .ic{font-size:22px}.tile b{font-size:14.5px}.tile small{color:var(--mut);font-size:12px}
.tile.t-test{background:rgba(232,89,12,.08);border-color:rgba(232,89,12,.35)}.tile.t-test b{color:var(--test)}
.empty{text-align:center;padding:50px 10px;color:var(--mut)}
.foot{text-align:center;color:var(--mut);font-size:13px;margin-top:30px}
.tree{display:flex;flex-direction:column;gap:2px}
.tb{display:flex;align-items:center;gap:6px;width:100%;border:0;background:none;color:var(--ink);font-size:15px;text-align:left;cursor:pointer;border-radius:10px;padding:9px 10px}
.tb:hover{background:var(--bg)}.tb[disabled]{opacity:.4;cursor:not-allowed}.tb small{margin-left:auto;opacity:.7;font-size:12px}
.tb i{font-style:normal;display:inline-block;width:14px;font-size:11px;transition:.15s;opacity:.7}
.tg.open>.tb i,.ts.open>.tb i{transform:rotate(90deg)}
.tb.l1{font-weight:600}.tb.cur{color:var(--pri)}
.tk{margin-left:12px;padding-left:8px;border-left:2px solid var(--line);display:flex;flex-direction:column;gap:2px}
.tb.l2{font-size:14.5px}.tb.l3{font-size:14px;padding:7px 10px}
.tb.on{background:linear-gradient(90deg,var(--pri),var(--pri2));color:#fff;font-weight:600}
.sb details{margin-top:16px}.sb summary{cursor:pointer;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--mut);font-weight:600}
.hint{text-align:center;padding:70px 10px;color:var(--mut);font-size:16px}.hint b{display:block;font-size:34px;margin-bottom:6px}
body.nosb .sb,body.nosb .menu{display:none}body.nosb .layout{grid-template-columns:1fr}
.scrim{display:none}
@media(max-width:820px){
 .menu{display:inline-block}.layout{grid-template-columns:1fr}
 .sb{position:fixed;left:0;top:52px;bottom:0;width:290px;max-width:86vw;height:auto;z-index:40;transform:translateX(-102%);transition:.2s;box-shadow:4px 0 20px rgba(0,0,0,.25)}
 body.open .sb{transform:none}body.open .scrim{display:block;position:fixed;inset:52px 0 0 0;background:rgba(0,0,0,.4);z-index:35}
 main{padding:16px 16px 50px}.tiles{grid-template-columns:repeat(2,1fr)}
}
"""

INDEX_JS = """
(function(){
var LBL=@@LBL@@;
var st={g:'',s:'',u:'',l:'',k:'',m:'',q:''};
try{var sv=JSON.parse(localStorage.getItem('gn_idx2')||'{}');for(var k in st)if(sv[k]!==undefined)st[k]=sv[k]}catch(e){}
var cards=[].slice.call(document.querySelectorAll('.setcard'));
cards.forEach(function(c){if(!c.dataset.s)c.dataset.s=(c.dataset.g==='IELTS'?c.dataset.u:'Tiếng Anh')});
function save(){try{localStorage.setItem('gn_idx2',JSON.stringify(st))}catch(e){}}
function norm(s){return (s||'').toLowerCase()}
function $(i){return document.getElementById(i)}
function all(sel,root){return [].slice.call((root||document).querySelectorAll(sel))}
function dueMark(el,sid,stu){
  var d=GNAuth.due(sid),ex=stu&&GNAuth.overdue(sid),m=el.querySelector('.duem');
  if(!d){if(m)m.remove();el.classList.remove('expired');return}
  if(!m){m=document.createElement('span');m.className='duem';(el.querySelector('small')||el.querySelector('.settitle')||el).appendChild(m)}
  var p=d.split('-');m.textContent=(ex?' · Hết hạn ':' · Hạn ')+p[2]+'/'+p[1];el.classList.toggle('expired',!!ex);
}
var STU=false,VIS=[];
function has(g,s,u,l){return VIS.some(function(c){return c.dataset.g===g&&(!s||c.dataset.s===s)&&(!u||c.dataset.u===u)&&(!l||c.dataset.k===l)})}
function lockAll(){
  var u=window.GNAuth&&GNAuth.user();STU=!!(u&&u.role==='student');
  cards.forEach(function(c){
    var tl=all('.tile[data-sid]',c);
    if(tl.length){var any=false;tl.forEach(function(t){var lk=STU&&!GNAuth.assigned(t.dataset.sid);t.classList.toggle('locked',lk);if(!lk){any=true;dueMark(t,t.dataset.sid,STU)}});c.classList.toggle('locked',!any)}
    else{var lk2=!!(STU&&c.dataset.sid&&!GNAuth.assigned(c.dataset.sid));c.classList.toggle('locked',lk2);if(!lk2&&c.dataset.sid)dueMark(c,c.dataset.sid,STU)}
  });
  VIS=cards.filter(function(c){return !c.classList.contains('locked')});
  /* cây thư mục: học sinh chỉ thấy lớp / môn / bài đã được giao; giáo viên & admin thấy đủ */
  all('.tg').forEach(function(el){
    var g=el.dataset.g,n=VIS.filter(function(c){return c.dataset.g===g&&c.dataset.k!=='soon'}).length,b=el.firstElementChild,sm=b.querySelector('small');
    if(el.dataset.n!=='0'&&sm)sm.textContent=n?n+' bộ':'chưa giao';
    el.hidden=STU&&!n;
  });
  all('.ts').forEach(function(el){
    var g=el.dataset.g,s=el.dataset.s,n=VIS.filter(function(c){return c.dataset.g===g&&c.dataset.s===s&&c.dataset.k!=='soon'}).length;
    el.hidden=STU&&!n;
    var b=el.firstElementChild,sm=b.querySelector('small');if(sm&&el.dataset.n!=='0')sm.textContent=n?'':'chưa giao';
  });
  all('.tb.l3').forEach(function(b){
    b.hidden=STU&&!(b.dataset.lv==='l'?has(b.dataset.g,b.dataset.s,'',b.dataset.l):has(b.dataset.g,b.dataset.s,b.dataset.u));
  });
  var none=STU&&!VIS.length;
  document.body.classList.toggle('nosb',none);
  var nb=$('nobai');if(nb)nb.hidden=!none;
}
function pickAuto(){
  /* chỉ có 1 lớp / 1 môn khả dụng thì tự mở sẵn cho gọn */
  if(!st.g){var gs=all('.tg').filter(function(e){return !e.hidden&&e.dataset.n!=='0'});if(gs.length===1)st.g=gs[0].dataset.g}
  if(st.g&&!st.s){var ss=all('.ts').filter(function(e){return e.dataset.g===st.g&&!e.hidden&&e.dataset.n!=='0'});if(ss.length===1)st.s=ss[0].dataset.s}
}
function apply(){
  lockAll();
  var tg=st.g&&document.querySelector('.tg[data-g="'+st.g+'"]');
  if(st.g&&(!tg||tg.hidden||tg.dataset.n==='0')){st.g=st.s=st.u=st.l='';}
  var ts=st.s&&document.querySelector('.ts[data-g="'+st.g+'"][data-s="'+st.s+'"]');
  if(st.s&&(!ts||ts.hidden||ts.dataset.n==='0')){st.s=st.u=st.l=''}
  pickAuto();
  var leaf=!!(st.g&&st.s&&(st.u||st.l));
  var q=norm(st.q);var showAll=!!q||leaf;
  var shown=0;
  cards.forEach(function(c){
    if(c.classList.contains('locked')||!showAll){c.hidden=true;return}
    var ok=(!st.g||c.dataset.g===st.g)&&(!st.s||c.dataset.s===st.s)&&(!st.u||c.dataset.u===st.u)&&(!st.l||c.dataset.k===st.l)&&(!st.k||c.dataset.k===st.k)&&(!q||norm(c.textContent).indexOf(q)>=0);
    c.hidden=!ok;
    all('.tile',c).forEach(function(t){
      var tm=t.dataset.m||'';t.hidden=!!(t.classList.contains('locked')||(st.m&&tm!==st.m));
    });
    if(ok&&st.m&&!c.querySelector('.tile:not([hidden])'))c.hidden=true;
    if(!c.hidden)shown++;
  });
  var nbv=$('nobai')&&!$('nobai').hidden;
  $('empty').hidden=!showAll||shown>0||nbv;
  $('hint').hidden=showAll||nbv;
  $('cnt').textContent=showAll?shown+' bộ bài':'';
  /* trạng thái mở / chọn trong cây */
  all('.tg').forEach(function(el){var o=el.dataset.g===st.g;el.classList.toggle('open',o);el.lastElementChild.hidden=!o||el.dataset.n==='0';el.firstElementChild.classList.toggle('cur',o)});
  all('.ts').forEach(function(el){var o=el.dataset.g===st.g&&el.dataset.s===st.s;el.classList.toggle('open',o);el.lastElementChild.hidden=!o||el.dataset.n==='0';el.firstElementChild.classList.toggle('cur',o)});
  all('.tb.l3').forEach(function(b){var on=b.dataset.g===st.g&&b.dataset.s===st.s&&(b.dataset.lv==='l'?b.dataset.l===st.l:(b.dataset.u===st.u&&!st.l));b.classList.toggle('on',on)});
  all('.f[data-f]').forEach(function(b){b.classList.toggle('on',(st[b.dataset.f]||'')===b.dataset.v)});
  var t=[];if(st.g)t.push(st.g==='IELTS'?'IELTS':'Lớp '+st.g);if(st.s&&st.g)t.push(st.s);
  if(st.u)t.push(LBL[st.u]||(/^[0-9]+$/.test(st.u)?'Unit '+st.u:/^Review[0-9]$/.test(st.u)?'Review '+st.u.slice(6):st.u));
  if(st.l){var lb=document.querySelector('.tb.l3[data-l="'+st.l+'"]');if(lb)t.push(lb.firstChild.textContent.trim())}
  $('ttl').textContent=leaf?t.join(' · '):(q?'Kết quả tìm kiếm':'Chọn bài học');
  save();
}
document.addEventListener('click',function(e){
  var b=e.target.closest&&e.target.closest('.f[data-f]');
  if(b&&!b.disabled){st[b.dataset.f]=b.dataset.v;apply();return}
  var t=e.target.closest&&e.target.closest('.tb');
  if(t&&!t.disabled){
    var lv=t.dataset.lv;
    if(lv==='g'){var same=st.g===t.dataset.g;st.g=same?'':t.dataset.g;st.s=st.u=st.l=st.k=''}
    else if(lv==='s'){var same2=st.s===t.dataset.s&&st.g===t.dataset.g;st.g=t.dataset.g;st.s=same2?'':t.dataset.s;st.u=st.l=st.k=''}
    else if(lv==='u'){st.g=t.dataset.g;st.s=t.dataset.s;st.u=t.dataset.u;st.l=''}
    else if(lv==='l'){st.g=t.dataset.g;st.s=t.dataset.s;st.u='';st.l=t.dataset.l}
    apply();
    if((lv==='u'||lv==='l')&&window.innerWidth<=820)document.body.classList.remove('open');
    return;
  }
  if(e.target.id==='reset'){st={g:'',s:'',u:'',l:'',k:'',m:'',q:''};$('q').value='';apply()}
  if(e.target.closest&&(e.target.closest('.menu')||e.target.classList.contains('scrim')))document.body.classList.toggle('open');
});
$('q').addEventListener('input',function(e){st.q=e.target.value;apply()});
$('q').value=st.q||'';
window.gnApply=apply;
apply();
})();
"""


def unum(udir):
    return udir[4:] if udir.startswith('Unit') else udir


UNIT_LABELS = {'MidTerm1': 'Mid-term 1', 'CuoiKy1': 'Cuối kỳ 1', 'GiuaKy1': 'Giữa kỳ 1', 'GiuaKy2': 'Giữa kỳ 2', 'CuoiKy2': 'Cuối kỳ 2', 'Start': 'Bài mở đầu',
               'OnHK1': 'Ôn tập HK1', 'OnHK2': 'Ôn tập HK2', 'DeCuongHK1': 'Đề cương HK1', 'DeCuongHK2': 'Đề cương HK2', 'HSG': 'Học sinh giỏi'}
UNIT_ORDER = ['Start', 'Review1', 'GiuaKy1', 'MidTerm1', 'Review2', 'CuoiKy1', 'OnHK1', 'DeCuongHK1', 'Review3', 'GiuaKy2', 'Review4', 'CuoiKy2', 'OnHK2', 'DeCuongHK2', 'HSG']
# nhóm đề riêng (không có bài luyện tập) xếp ngay sau mục nào: (lớp, thư mục) -> (thư mục mốc, thứ tự phụ)
AFTER = {('Lop3', 'CuoiKy1'): ('Unit10', 6), ('Lop4', 'GiuaKy1'): ('Review1', 6), ('Lop4', 'CuoiKy1'): ('Review2', 6), ('Lop4', 'OnHK1'): ('Review2', 7), ('Lop4', 'DeCuongHK1'): ('Review2', 8),
         ('Lop4', 'GiuaKy2'): ('Review3', 6), ('Lop4', 'CuoiKy2'): ('Review4', 6), ('Lop4', 'OnHK2'): ('Review4', 7), ('Lop4', 'DeCuongHK2'): ('Review4', 8), ('Lop4', 'HSG'): ('Review4', 9)}


def ulabel(u):
    if u in UNIT_LABELS: return UNIT_LABELS[u]
    m = re.match(r'^Review(\d)$', u)
    return ('Review ' + m.group(1)) if m else 'Unit ' + u


SUBJECTS = ['Tiếng Anh', 'Toán', 'Hóa', 'Lý', 'Sinh', 'Tin', 'Văn', 'Sử']
GRADE_SUBJECTS = {'11': SUBJECTS}   # lớp nào có nhiều môn; lớp khác chỉ có Tiếng Anh
SUBJECT_BY_SET = {}                 # mã bộ bài -> môn (không khai báo = Tiếng Anh). Thêm môn mới: khai báo ở đây
IELTS_SKILLS = [('Reading', [('full', 'Full Test'), ('dang', 'Theo dạng bài')]), ('Listening', None), ('Writing', None), ('Speaking', None)]


def subj(sid):
    if sid.startswith('ly11-'): return 'Lý'
    return SUBJECT_BY_SET.get(sid, 'Tiếng Anh')


def build_tree(done):
    def ukey(u):
        return (0 if u.isdigit() else 1, int(u) if u.isdigit() else (UNIT_ORDER.index(u) if u in UNIT_ORDER else 99))
    units = {}
    for e, S, _ in done:
        units.setdefault((e[3][3:], subj(S['id'])), set()).add(unum(e[4]))
    o = ['<nav class="tree" id="tree">']
    for g in range(1, 13):
        gs = str(g)
        n = sum(1 for e, S, _ in done if e[3][3:] == gs) + (LY['n'] if gs == '11' else 0)
        if not n:
            o.append('<div class="tg" data-g="%s" data-n="0"><button class="tb l1" disabled>Lớp %d <small>sắp có</small></button><div class="tk" hidden></div></div>' % (gs, g))
            continue
        o.append('<div class="tg" data-g="%s"><button class="tb l1" data-lv="g" data-g="%s"><i>▸</i>Lớp %d <small>%d bộ</small></button><div class="tk" hidden>' % (gs, gs, g, n))
        for sb in GRADE_SUBJECTS.get(gs, ['Tiếng Anh']):
            us = sorted(units.get((gs, sb), []), key=ukey)
            if gs == '11' and sb == 'Lý' and LY['cards']:
                o.append('<div class="ts" data-g="11" data-s="Lý"><button class="tb l2" data-lv="s" data-g="11" data-s="Lý"><i>▸</i>Lý<small></small></button><div class="tk" hidden>')
                for u in LY['order']:
                    o.append('<button class="tb l3" data-lv="u" data-g="11" data-s="Lý" data-u="%s">%s</button>' % (u, html.escape(LY['labels'].get(u, u))))
                o.append('</div></div>')
                continue
            if not us:
                o.append('<div class="ts" data-g="%s" data-s="%s" data-n="0"><button class="tb l2" disabled>%s <small>sắp có</small></button><div class="tk" hidden></div></div>' % (gs, sb, html.escape(sb)))
                continue
            o.append('<div class="ts" data-g="%s" data-s="%s"><button class="tb l2" data-lv="s" data-g="%s" data-s="%s"><i>▸</i>%s<small></small></button><div class="tk" hidden>' % (gs, sb, gs, sb, html.escape(sb)))
            for u in us:
                o.append('<button class="tb l3" data-lv="u" data-g="%s" data-s="%s" data-u="%s">%s</button>' % (gs, sb, u, ulabel(u)))
            o.append('</div></div>')
        o.append('</div></div>')
    if IELTS['cards']:
        o.append('<div class="tg" data-g="IELTS"><button class="tb l1" data-lv="g" data-g="IELTS"><i>▸</i>IELTS <small></small></button><div class="tk" hidden>')
        for sk, leaves in IELTS_SKILLS:
            if leaves:
                o.append('<div class="ts" data-g="IELTS" data-s="%s"><button class="tb l2" data-lv="s" data-g="IELTS" data-s="%s"><i>▸</i>%s<small></small></button><div class="tk" hidden>' % (sk, sk, sk))
                for l, lb in leaves:
                    o.append('<button class="tb l3" data-lv="l" data-g="IELTS" data-s="%s" data-l="%s">%s</button>' % (sk, l, lb))
                o.append('</div></div>')
            else:
                o.append('<div class="ts" data-g="IELTS" data-s="%s" data-n="0"><button class="tb l2" disabled>%s <small>sắp có</small></button><div class="tk" hidden></div></div>' % (sk, sk))
        o.append('</div></div>')
    o.append('</nav>')
    return ''.join(o)


def build_index(done):
    grades = sorted({e[3][3:] for e, _, _ in done}, key=int)
    units = sorted({(e[3][3:], unum(e[4])) for e, _, _ in done}, key=lambda x: (int(x[0]), 0 if x[1].isdigit() else 1, int(x[1]) if x[1].isdigit() else (UNIT_ORDER.index(x[1]) if x[1] in UNIT_ORDER else 99)))
    def cnt(fn):
        return sum(1 for e, _, _ in done if fn(e))
    o = ['<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
         '<title>GRADE 1-12-IELTS</title><style>%s</style>%s</head><body>' % (INDEX_CSS, AUTH_HEAD % (APPS_SCRIPT_URL, '', '')),
         '<div class="top"><button class="menu" aria-label="Mở bộ lọc">☰ Bộ lọc</button><h1>GRADE 1-12-IELTS</h1><span id="chip"></span></div>',
         '<div class="layout"><aside class="sb">',
         '<h4>Tìm kiếm</h4><input id="q" type="search" placeholder="Tên unit, kỹ năng…">',
         '<h4>Lớp học</h4>', build_tree(done)]
    o.append('<details><summary>Lọc thêm</summary><h4>Loại bài tập</h4><div class="seg kinds"><button class="f" data-f="k" data-v="">Tất cả</button>'
             '<button class="f" data-f="k" data-v="luyentap">Luyện tập</button><button class="f" data-f="k" data-v="botro">Bổ trợ</button><button class="f" data-f="k" data-v="chuyensau">Chuyên sâu</button><button class="f" data-f="k" data-v="4kn">4 kỹ năng</button>'
             '<button class="f" data-f="k" data-v="ontap">Ôn tập</button><button class="f" data-f="k" data-v="test">Đề kiểm tra</button>'
             '</div>'
             '<h4>Hình thức</h4><div class="seg"><button class="f" data-f="m" data-v="">Tất cả</button>'
             '<button class="f" data-f="m" data-v="prac">Luyện tập</button><button class="f" data-f="m" data-v="test">Kiểm tra</button></div>'
             '</details><button class="reset" id="reset">↺ Xoá lựa chọn</button></aside><div class="scrim"></div><main>'
             '<div class="bar"><h2 id="ttl">Chọn bài học</h2><span id="cnt"></span></div><div class="hint" id="hint"><b>📂</b>Chọn <u>Lớp</u> → <u>Môn học</u> → <u>Bài</u> ở cột bên trái để xem nội dung</div>')
    icons = {'phat-am': '🔊', 'tu-vung': '🔤', 'tu-vung-ngu-phap': '🔤', 'ngu-phap': '🧩', 'nghe': '🎧', 'noi': '🗣️', 'doc': '📖', 'viet': '✍️', 'kiem-tra': '📝', 'phat-am': '🔊', 'loi-sai': '🔍', 'dien-tu': '🧩', 'doc-hieu': '📖', 'noi-giao-tiep': '🗣️'}
    tests = [x for x in done if x[0][5].startswith('test')]
    cards = []   # (vị trí, html) — đề kiểm tra của Unit nào xếp ngay sau Unit đó
    last_pos = {}
    for pos, (entry, S, pages) in enumerate([x for x in done if not x[0][5].startswith('test')]):
        gdir, udir, slug = entry[3], entry[4], entry[5]
        mark_o = len(o)
        g, u = gdir[3:], unum(udir)
        kind = 'test' if slug.startswith('test') else ('luyentap' if slug.startswith('luyentap') else slug)
        o.append('<section class="card setcard" data-g="%s" data-s="%s" data-u="%s" data-k="%s" data-sid="%s"><div class="settitle"><span class="chip">Lớp %s · %s</span><h3>%s</h3></div><div class="tiles">'
                 % (g, subj(S['id']), u, kind, S['id'], g, ulabel(u), html.escape(S['title'])))
        if S.get('theory'):
            o.append('<a class="tile" data-m="prac" href="WebBaiTap/%s/%s/%s/ly-thuyet.html"><span class="ic">📘</span><b>Lý thuyết</b><small>Từ vựng · ngữ pháp</small></a>' % (gdir, udir, slug))
        for pid, title, mode, n in pages:
            o.append('<a class="tile %s" data-m="%s" href="WebBaiTap/%s/%s/%s/%s.html"><span class="ic">%s</span><b>%s</b><small>%d câu%s</small></a>'
                     % ('t-test' if mode == 'test' else '', 'test' if mode == 'test' else 'prac', gdir, udir, slug, pid, icons.get(pid, '✏️'), html.escape(title), n, ' · có tính giờ' if mode == 'test' else ''))
        o.append('</div></section>')
        cards.append((pos * 10, ''.join(o[mark_o:]))); del o[mark_o:]; last_pos[(gdir, udir)] = pos * 10
    groups = []   # các đề riêng gom theo (lớp, Unit/Mid-term) — mỗi nhóm một thẻ
    for x in tests:
        key = (x[0][3], x[0][4])
        for gr in groups:
            if gr[0] == key:
                gr[1].append(x); break
        else:
            groups.append((key, [x]))
    for (gdir, udir), tl in groups:
        g, u = gdir[3:], unum(udir)
        mark_o = len(o)
        ttl = 'Đề kiểm tra Mid-term 1 (%d test)' % len(tl) if udir == 'MidTerm1' else 'Đề kiểm tra %s (%d đề)' % (ulabel(u), len(tl))
        o.append('<section class="card setcard" data-g="%s" data-s="%s" data-u="%s" data-k="test"><div class="settitle"><span class="chip">Lớp %s · %s</span><h3>%s</h3></div><div class="tiles">' % (g, subj(tl[0][1]['id']), u, g, ulabel(u), ttl))
        for entry, S, pages in tl:
            pid, title, mode, n = pages[0]
            P0 = S['pages'][0]
            num = S['title'].split('–')[0].strip()
            if udir != 'MidTerm1': num = 'Đề ' + S['title'].split()[-1]
            o.append('<a class="tile t-test" data-m="test" data-sid="%s" href="WebBaiTap/%s/%s/%s/%s.html"><span class="ic">%s</span><b>%s</b><small>%d câu · %d phút%s</small></a>'
                     % (S['id'], entry[3], entry[4], entry[5], pid, '🎧' if P0.get('audio') else '📝', html.escape(num), n, P0.get('minutes', 0), ' · có nghe' if P0.get('audio') else ''))
        o.append('</div></section>')
        pp = last_pos.get((gdir, udir))
        if pp is not None:
            pos_t = pp + 5
        elif (gdir, udir) in AFTER:
            anc, off = AFTER[(gdir, udir)]
            pos_t = last_pos.get((gdir, anc), 10**6) + off
        else:
            pos_t = 10**6
        cards.append((pos_t, ''.join(o[mark_o:]))); del o[mark_o:]
    for _, h in sorted(cards, key=lambda c: c[0]):
        o.append(h)
    o.extend(LY['cards'])
    o.extend(IELTS['cards'])
    o.append('<div class="empty" id="nobai" hidden>Chưa có bài nào được giao cho lớp của bạn. Hãy nhờ giáo viên giao bài.</div><div class="empty" id="denied" hidden>Bài đó chưa được giao cho lớp của bạn.</div><div class="empty" id="empty" hidden>Không có bộ bài phù hợp. Hãy bấm “Xoá lựa chọn”.</div>'
             '<div class="foot">Học sinh làm bài trên điện thoại hoặc máy tính · Kết quả ghi tự động về giáo viên</div></main></div>'
             '<script>GNAuth.chip("#chip");</script><script>%s</script><script>GNAuth.verify(function(){window.gnApply&&gnApply()});if(/denied=1/.test(location.search)){var d=document.getElementById("denied");if(d)d.hidden=false}</script><script src="engine/feedback.js?v=%s"></script></body></html>' % (INDEX_JS.replace('@@LBL@@', json.dumps(UNIT_LABELS, ensure_ascii=False)), BV))
    open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf8').write(''.join(o))
    build_site_pages(done)


def catalog(done):
    out = []
    for e, S, pages in done:
        slug = e[5]
        out.append({'id': S['id'], 'title': S['title'], 'grade': int(e[3][3:]), 'unit': ulabel(unum(e[4])), 'kind': 'test' if slug.startswith('test') else slug})
    return out + LY['catalog'] + IELTS['catalog']


def build_site_pages(done=None):
    """site/*.html (đăng nhập, quản trị, điểm của tôi) → thư mục gốc, gắn link Apps Script."""
    pages = {e[0]: 'WebBaiTap/%s/%s/%s' % (e[3], e[4], e[5]) for e in REGISTRY}   # mã bộ bài -> thư mục trang (để xem lại bài làm)
    for n in ('login.html', 'admin.html', 'me.html', 'student.html'):
        t = open(os.path.join(ROOT, 'site', n), encoding='utf8').read().replace('%PAGES%', json.dumps(pages)).replace('engine/review.js"', 'engine/review.js?v=' + BV + '"').replace('engine/auth.js"', 'engine/auth.js?v=' + BV + '"').replace('engine/feedback.js"', 'engine/feedback.js?v=' + BV + '"').replace('engine/app.css"', 'engine/app.css?v=' + BV + '"').replace('%GN_URL%', APPS_SCRIPT_URL).replace('%CATALOG%', json.dumps(catalog(done or []), ensure_ascii=False))
        open(os.path.join(ROOT, n), 'w', encoding='utf8').write(t)


if __name__ == '__main__':
    want = sys.argv[1:]
    done = []
    for e in REGISTRY:
        if want and e[0] not in want:
            continue
        S, pages = build_set(e)
        if S is None:
            continue
        done.append((e, S, pages))
        print(e[0], '->', len(pages), 'trang,', sum(p[3] for p in pages), 'câu')
    if not want:
        LY.update(ly.build(ROOT, APPS_SCRIPT_URL, AUTH_HEAD, BV))
        UNIT_LABELS.update(LY['labels'])
        print('Vật lí 11 ->', LY['n'], 'bộ,', len(LY['cards']), 'thẻ')
        IELTS.update(ielts.build(ROOT, APPS_SCRIPT_URL, AUTH_HEAD, BV))
        print('IELTS Reading ->', IELTS['n'], 'bộ,', len(IELTS['cards']), 'thẻ')
        build_index(done)
