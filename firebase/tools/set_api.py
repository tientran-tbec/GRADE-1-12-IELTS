# -*- coding: utf-8 -*-
"""Đổi APPS_SCRIPT_URL trong build.py. Dùng: python set_api.py <URL> [đường_dẫn_build.py]"""
import os, re, sys
url = sys.argv[1]
b = sys.argv[2] if len(sys.argv) > 2 else os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'build.py'))
t = open(b, encoding='utf-8').read()
t2, n = re.subn(r"APPS_SCRIPT_URL = '[^']*'", "APPS_SCRIPT_URL = '%s'" % url, t, count=1)
if not n: print('[LOI] không thấy APPS_SCRIPT_URL trong', b); sys.exit(1)
open(b, 'w', encoding='utf-8', newline='').write(t2)
print('[OK] APPS_SCRIPT_URL ->', url)
