#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DOI LINK GOOGLE SHEET / APPS SCRIPT + BUILD LAI TOAN BO WEB
------------------------------------------------------------
Cach dung (dung thu muc nay):
    python update_links.py                      -> chi build lai trang + index.html
    python update_links.py "<link Google Sheet>"  -> doi SHEET_ID trong code.gs (roi build)
    python update_links.py "<link Apps Script /exec>" -> doi APPS_SCRIPT_URL trong build.py (roi build)
    python update_links.py --sync-only          -> chi tao lai code.public.gs
Co the dan ca 2 link cung luc, thu tu khong quan trong.
"""
import sys, re, os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
GS_FILE = os.path.join(ROOT, "code.gs")
GS_PUBLIC_FILE = os.path.join(ROOT, "code.public.gs")
BUILD = os.path.join(ROOT, "build.py")
SHEET_RE = re.compile(r"docs\.google\.com/spreadsheets/d/([a-zA-Z0-9_-]+)")
SCRIPT_RE = re.compile(r"https://script\.google\.com/macros/s/[a-zA-Z0-9_-]+/exec")


def sync_public_copy():
    if os.path.exists(GS_FILE):
        open(GS_PUBLIC_FILE, "w", encoding="utf-8").write(open(GS_FILE, encoding="utf-8").read())
        print("[OK] Da dong bo code.public.gs")


def update_sheet_id(new_id):
    t = open(GS_FILE, encoding="utf-8").read()
    t, n = re.subn(r'var SHEET_ID\s*=\s*"[^"]*"', 'var SHEET_ID = "%s"' % new_id, t)
    if n:
        open(GS_FILE, "w", encoding="utf-8").write(t)
        print("[OK] Da doi SHEET_ID ->", new_id)
        sync_public_copy()
    else:
        print("[LOI] Khong thay SHEET_ID trong code.gs")


def update_url(new_url):
    t = open(BUILD, encoding="utf-8").read()
    t, n = re.subn(r"APPS_SCRIPT_URL = '[^']*'", "APPS_SCRIPT_URL = '%s'" % new_url, t, count=1)
    if n:
        open(BUILD, "w", encoding="utf-8").write(t)
        print("[OK] Da doi APPS_SCRIPT_URL ->", new_url)
    else:
        print("[LOI] Khong thay APPS_SCRIPT_URL trong build.py")


def main():
    args = sys.argv[1:]
    if args and args[0] == "--sync-only":
        sync_public_copy()
        return
    for raw in args:
        link = raw.strip().strip('"').strip("'")
        m1, m2 = SHEET_RE.search(link), SCRIPT_RE.search(link)
        if m1:
            update_sheet_id(m1.group(1))
        elif m2:
            update_url(m2.group(0))
        else:
            print("[?] Khong nhan dien duoc link:", link)
    subprocess.check_call([sys.executable, BUILD], cwd=ROOT)
    print("[OK] Da build lai web trong", ROOT)


if __name__ == "__main__":
    main()
