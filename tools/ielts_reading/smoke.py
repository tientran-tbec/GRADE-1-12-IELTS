import sys,json,re,asyncio,glob,os
from playwright.sync_api import sync_playwright
def run(files):
    res=[]
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome' if os.path.exists('/opt/pw-browsers/chromium-1194/chrome-linux/chrome') else None,args=['--no-sandbox'])
        for f in files:
            pg=b.new_page(); errs=[]
            pg.on('pageerror',lambda e:errs.append(str(e)))
            pg.goto('file://'+os.path.abspath(f)); 
            pg.fill('#stuName','Test'); pg.fill('#stuClass','X'); pg.evaluate('startExam()')
            info=pg.evaluate('({ANS:ANS,UNITS:UNITS,TOTAL:TOTAL_QUESTIONS})')
            for u in info['UNITS']:
                if u['type']=='text': 
                    v=info['ANS'][str(u['n'])]; pg.evaluate("([n,v])=>{var e=document.getElementById('q'+n);e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}));}",[u['n'],v[0]])
                elif u['type']=='select': pg.evaluate("([n,v])=>{var e=document.getElementById('q'+n);e.value=v;e.dispatchEvent(new Event('change',{bubbles:true}));}",[u['n'],(lambda a:a[0] if isinstance(a,list) else a)(info['ANS'][str(u['n'])])])
                elif u['type']=='radio':
                    v=info['ANS'][str(u['n'])]; v=v[0] if isinstance(v,list) else v
                    pg.evaluate("([n,v])=>{var e=[...document.querySelectorAll('input[name=q'+n+']')].find(x=>x.value===v); e.checked=true; e.dispatchEvent(new Event('change',{bubbles:true}));}",[u['n'],v])
                else:
                    for v in info['ANS'][u['group']]:
                        pg.evaluate("([g,v])=>{var e=[...document.querySelectorAll('input[name='+g+']')].find(x=>x.value===v); e.checked=true; e.dispatchEvent(new Event('change',{bubbles:true}));}",[u['group'],v])
            pg.evaluate('confirmSubmit()')
            t=pg.inner_text('#resultBox')
            m=re.search(r'Tổng điểm\s*(\d+)/(\d+)',t) or re.search(r'Số câu đúng\s+Tỉ lệ\s+(\d+)/(\d+)',t)
            ex=pg.evaluate("document.querySelectorAll('.explain-item').length")
            res.append((f,m and m.groups(),info['TOTAL'],ex,errs[:2]))
            pg.close()
        b.close()
    return res
if __name__=='__main__':
    for r in run(sys.argv[1:]): print(r)
