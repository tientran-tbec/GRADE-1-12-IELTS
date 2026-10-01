"""python tools/show.py <u3_botro> <item-id>...  -> hiện câu hỏi, phương án, đáp án và giải thích"""
import sys, os, re, importlib.util
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, R)
def load(p):
    sp = importlib.util.spec_from_file_location(os.path.basename(p)[:-3], os.path.join(R, p)); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
def show(key, ids):
    d = load('units/lop11_%s.py' % key); a = load('units/lop11_%s_dapan.py' % key)
    items = {}
    for pg in d.SET['pages']:
        for g in pg['groups']:
            for it in g['items']: items[it['id']] = (pg['id'], g, it)
    for i in ids:
        pid, g, it = items[i]
        print('=== %s [%s] %s' % (i, pid, it['t'])); print('INSTR:', re.sub('<[^>]+>', '', g.get('instr', ''))[:200]); 
        if g.get('passage') and it['t'] in ('tf', 'tfng'): print('PASSAGE:', re.sub('<[^>]+>', '', g['passage'])[:2500])
        print('Q:', it.get('q')); print('O:', it.get('o')); print('ANS:', a.ANS.get(i)); print('EXP:', a.EXPLANATIONS.get(i)); print()
if __name__ == '__main__': show(sys.argv[1], sys.argv[2:])
