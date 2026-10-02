"""python tools/check_set.py <tên-module-data> ...   vd: mt1_test01
Kiểm tra: mọi câu (trừ open) có ANS + EXPLANATION; mcq có đủ phương án; fill khớp số ô; id duy nhất."""
import sys, os, re, importlib.util
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(p):
    sp = importlib.util.spec_from_file_location(os.path.basename(p)[:-3], os.path.join(R, p)); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
bad = 0
for name in sys.argv[1:]:
    d = load('units/%s.py' % name); a = load('units/%s_dapan.py' % name)
    ANS = dict(a.ANS); EXP = dict(a.EXPLANATIONS); seen = set(); n = 0; err = []
    FX = (load('units/fixes.py').FIXES.get(d.SET['id'], {})) if os.path.exists(os.path.join(R, 'units/fixes.py')) else {}
    for k, f in FX.items():
        if 'ans' in f: ANS[k] = f['ans']
        if 'exp' in f: EXP[k] = f['exp']
    for pg in d.SET['pages']:
        for g in pg['groups']:
            for it in g['items']:
                i = it['id']; n += 1
                if i in seen: err.append('trùng id ' + i)
                seen.add(i)
                if it['t'] == 'open':
                    if i not in EXP: err.append('open thiếu EXP ' + i)
                    continue
                if i not in ANS: err.append('thiếu ANS ' + i); continue
                if i not in EXP or not EXP[i]: err.append('thiếu EXP ' + i)
                x = ANS[i]
                if it['t'] == 'mcq':
                    o = it.get('o') or []
                    xs = x if isinstance(x, list) else [x]
                    for v in xs:
                        if it.get('plain'):
                            if v not in o: err.append('%s: ANS %r không là phương án' % (i, v))
                        elif not (isinstance(v, str) and len(v) == 1 and 'ABCDEFGHIJ'.find(v) in range(len(o))): err.append('%s: ANS %r ngoài %d phương án' % (i, v, len(o)))
                elif it['t'] == 'tf' and x not in ('T', 'F'): err.append('%s: tf cần T/F' % i)
                elif it['t'] == 'tfng' and x not in ('T', 'F', 'NG'): err.append('%s: tfng cần T/F/NG' % i)
                elif it['t'] == 'match':
                    bl = x['blanks'] if isinstance(x, dict) else x
                    if len(bl) != len(it['left']): err.append('%s: match %d dòng nhưng ANS %d' % (i, len(it['left']), len(bl)))
                    for z in bl:
                        if not any(v in it['o'] for v in (z if isinstance(z, list) else [z])): err.append('%s: ANS %r không thuộc o' % (i, z))
                elif it['t'] == 'order':
                    ws = sorted(' '.join(it['words']).split()); xs = x if isinstance(x, list) else [x]
                    for v in xs:
                        if sorted(v.split()) != ws: err.append('%s: ANS %r không khớp words' % (i, v))
                elif it['t'] == 'fill':
                    nb = len(re.findall(r'\{_\}', it['q']))
                    bl = x['blanks'] if isinstance(x, dict) else ([[x]] if isinstance(x, str) else [x])
                    if nb != len(bl): err.append('%s: %d ô nhưng ANS có %d' % (i, nb, len(bl)))
    print('%s: %d câu, %d lỗi' % (name, n, len(err))); [print('  ', e) for e in err[:40]]; bad += len(err)
sys.exit(1 if bad else 0)
