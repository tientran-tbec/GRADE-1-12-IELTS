# -*- coding: utf-8 -*-
"""Tạo thư mục firebase/public từ trang đã build, đổi link Apps Script cũ sang API Firebase.
Không đụng vào bản đang chạy trên GitHub Pages (chỉ sao chép + thay chữ trong bản sao).
Dùng:  python make_public.py [--audio] [--api URL]"""
import os, re, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.abspath(os.path.join(HERE, '..', 'public'))
API = 'https://asia-southeast1-lms-learning-36841.cloudfunctions.net/api'
args = sys.argv[1:]
if '--api' in args: API = args[args.index('--api') + 1]
with_audio = '--audio' in args
DIRS = ['WebBaiTap', 'assets', 'engine', 'thuthach'] + (['audio'] if with_audio else [])
OLD = re.compile(r'https://script\.google\.com/macros/s/[A-Za-z0-9_-]+/exec')
TEXT = ('.html', '.js', '.json', '.css', '.txt')
if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
n_files = n_rep = 0
def put(src, dst):
    global n_files, n_rep
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if src.lower().endswith(TEXT):
        t = open(src, encoding='utf-8', errors='surrogateescape').read()
        t2, k = OLD.subn(API, t)
        n_rep += k
        open(dst, 'w', encoding='utf-8', errors='surrogateescape', newline='').write(t2)
    else:
        shutil.copyfile(src, dst)
    n_files += 1
for f in sorted(os.listdir(ROOT)):
    if f.lower().endswith('.html') and os.path.isfile(os.path.join(ROOT, f)): put(os.path.join(ROOT, f), os.path.join(OUT, f))
for d in DIRS:
    base = os.path.join(ROOT, d)
    if not os.path.isdir(base): print('[bỏ qua] không có', d); continue
    for dp, _, fs in os.walk(base):
        for f in fs:
            s = os.path.join(dp, f); put(s, os.path.join(OUT, os.path.relpath(s, ROOT)))
left = 0
for dp, _, fs in os.walk(OUT):
    for f in fs:
        if f.lower().endswith(TEXT) and 'script.google.com/macros' in open(os.path.join(dp, f), encoding='utf-8', errors='ignore').read(): left += 1
print('Đã tạo %s: %d file, thay %d link, còn sót link cũ ở %d file%s' % (OUT, n_files, n_rep, left, '' if with_audio else ' (không kèm audio)'))
