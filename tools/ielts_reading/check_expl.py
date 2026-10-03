import json,re,sys,html
def nz(s):
    s=html.unescape(re.sub(r'<.*?>',' ',s))
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('–','-').replace('—','-').replace('…','...')
    return re.sub(r'\s+',' ',s).strip().lower()
def needed(d):
    keys=[];
    for g in d['groups']:
        if g['type']=='mcq_multi':
            for it in g['items']: keys.append('q'+''.join(map(str,it['ns'])))
    multi={n for g in d['groups'] if g['type']=='mcq_multi' for it in g['items'] for n in it['ns']}
    for k in d['answers']:
        if int(k) not in multi: keys.append(k)
    return keys
def check(no):
    d=json.load(open(f'json/final2/t{no:02d}.json'))
    try: e=json.load(open(f'json/expl2/t{no:02d}.json'))
    except Exception as ex: return [f'cannot read: {ex}']
    errs=[]
    ptxt=nz(' '.join(x['html'] for p in d['passages'] for x in p['paras']))
    # also allow quote in question text for completeness? no: passage only
    for k in needed(d):
        v=e.get(k)
        if not v: errs.append(f'missing {k}'); continue
        for f in ('quote','en','vi'):
            if not v.get(f,'').strip(): errs.append(f'{k} empty {f}')
        if len(v.get('en',''))<120 or len(v.get('vi',''))<120: errs.append(f'{k} too short')
        q=v.get('quote','')
        parts=[x for x in re.split(r'\s*(?:\.\.\.|…|\[…\]|\|)\s*',q) if len(x.strip())>8]
        for part in parts:
            if nz(part).strip(' .,"\'') not in ptxt: errs.append(f'{k} quote not in passage: {part[:60]}'); break
    return errs
if __name__=='__main__':
    for a in sys.argv[1:]:
        r=check(int(a)); print(a,'OK' if not r else r[:12], '' if len(r)<=12 else f'(+{len(r)-12} more)')
