import json,re,html,os
APPS="https://script.google.com/macros/s/AKfycbyfZgrcZfOw-g5nCLlQ5QyLCCADuct8QRxW31SG8F3IZfkgL0x_3LOoPWBHRFRNiXA1/exec"
S_FULL=open('a/Test1_Reading.html',encoding='utf8').read()
S_ONE=open('d/Test1_Passage1_TFNG.html',encoding='utf8').read()
# patch engine: select may accept array of answers
S_FULL=S_FULL.replace("ok = (val === ANS[n]);\n        var sel","ok = Array.isArray(ANS[n]) ? ANS[n].indexOf(val)!==-1 : (val === ANS[n]);\n        var sel")
def _radio(t):
    t=t.replace("ok = (val === ANS[n]);\n        document.querySelectorAll('input[name=\"q'+n+'\"]')","ok = Array.isArray(ANS[n]) ? ANS[n].indexOf(val)!==-1 : (val === ANS[n]);\n        document.querySelectorAll('input[name=\"q'+n+'\"]')")
    t=t.replace("if(inp.value === ANS[n]) label.classList.add('correct');","if(Array.isArray(ANS[n]) ? ANS[n].indexOf(inp.value)!==-1 : inp.value === ANS[n]) label.classList.add('correct');")
    return t
S_FULL=_radio(S_FULL); S_ONE=_radio(S_ONE)
S_ONE=S_ONE.replace("ok = (val === ANS[n]);\n        var sel","ok = Array.isArray(ANS[n]) ? ANS[n].indexOf(val)!==-1 : (val === ANS[n]);\n        var sel")
NUMW={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen','20':'twenty','30':'thirty','40':'forty','50':'fifty','100':'hundred'}
WN={v:k for k,v in NUMW.items()}
def variants(a):
    if isinstance(a,str): a=[a]
    out=[]
    def add(x):
        x=re.sub(r'\s+',' ',x).strip()
        if x and x.lower() not in [y.lower() for y in out]: out.append(x)
    for b in a:
        b=html.unescape(re.sub('<.*?>','',str(b)))
        cands=[b]
        if '(' in b:
            cands.append(re.sub(r'\([^)]*\)','',b))      # bỏ phần trong ngoặc
            cands.append(re.sub(r'[()]','',b))            # giữ nội dung
        for c in cands:
            add(c)
            add(c.replace('-',' '));  add(c.replace('–','-'))
            if re.match(r'^(a|an|the) ',c,re.I): add(re.sub(r'^(a|an|the) ','',c,flags=re.I))
            w=c.lower()
            if w in WN: add(WN[w])
            if w in NUMW: add(NUMW[w])
            if re.match(r'^\d{1,3}(,\d{3})+$',c): add(c.replace(',',''))
    return out
def bl(x): return html.escape(x)
def ph_text(n): return f'<b class="qnum-inline">{n}</b><input type="text" class="qtext" id="q{n}" autocomplete="off"><span id="hint-q{n}"></span>'
def sel_opts(opts,first='--',label_text=False):
    s=f'<option value="">{first}</option>'
    for k,t in opts:
        s+=f'<option value="{k}">{k}. {t}</option>' if label_text and t else f'<option value="{k}">{k}</option>'
    return s
def ph_sel(n,opts,label_text=False):
    return f'<b class="qnum-inline">{n}</b><select class="qselect" id="q{n}">{sel_opts(opts,"--",label_text)}</select><span id="hint-q{n}"></span>'
def letters(rng):
    m=re.match(r'\s*([A-Za-z])\s*[-–—]\s*([A-Za-z])',rng or '')
    if not m: return list('ABCDEFGH')
    a,b=ord(m.group(1).upper()),ord(m.group(2).upper()); return [chr(c) for c in range(a,b+1)]
def render_group(g,d):
    a,b=g['q']
    h='Questions %d–%d'%(a,b) if a!=b else 'Question %d'%a
    o=[f'<div class="qgroup">\n<h3>{h}</h3>']
    for l in g.get('lines',[]): o.append(f'<div class="instr">{l}</div>')
    units=[];ans={};cbg=[]
    t=g['type']
    A=d['answers']
    if t in('tfng','ynng'):
        for it in g['items']:
            n=it['n']
            o.append(f'<div class="qitem"><span class="qnum">{n}.</span> {it["q"]}<span id="hint-q{n}"></span><br>')
            for lab in g['labels']:
                o.append(f'<label class="opt-row"><input type="radio" name="q{n}" value="{lab}"> {lab}</label>')
            o.append('</div>'); units.append({'type':'radio','n':n}); ans[str(n)]=A[str(n)]
    elif t=='mcq':
        for it in g['items']:
            n=it['n']
            o.append(f'<div class="qitem"><span class="qnum">{n}.</span> {it["q"]}<span id="hint-q{n}"></span><br>')
            for op in it['opts']:
                txt=f'{op["k"]}.  {op["t"]}' if op.get('t') else op['k']
                o.append(f'<label class="opt-row"><input type="radio" name="q{n}" value="{op["k"]}"> {txt}</label>')
            o.append('</div>'); units.append({'type':'radio','n':n}); v=A[str(n)]; ans[str(n)]=v if isinstance(v,str) or len(v)>1 else v[0]
    elif t=='mcq_multi':
        for it in g['items']:
            ns=it['ns']; name='q'+''.join(map(str,ns)); mx=it.get('max') or len(ns)
            lab=f'Q{ns[0]}-{ns[-1]}.' if len(ns)>1 else f'Q{ns[0]}.'
            o.append(f'<div class="qitem"><span class="qnum">{lab}</span> {it["q"]}<br>')
            for op in it['opts']:
                txt=f'{op["k"]}.  {op["t"]}' if op.get('t') else op['k']
                o.append(f'<label class="opt-row"><input type="checkbox" name="{name}" value="{op["k"]}"> {txt}</label>')
            o.append('</div>')
            units.append({'type':'checkboxGroup','group':name,'members':ns,'max':len(ns)}); cbg.append({'name':name,'max':len(ns)})
            ans[name]=[A[str(n)] if not isinstance(A[str(n)],list) else A[str(n)][0] for n in ns]
    elif t=='match':
        opts=g.get('options') or []
        kind=g.get('kind')
        if opts:
            o.append('<div class="headinglist"><b>%s</b><br>'%(g.get('options_title') or 'List'))
            for op in opts: o.append(f'<div>{op["k"]}.  {op["t"]}</div>')
            o.append('</div>')
            ol=[(op['k'],op['t']) for op in opts]
        else:
            ol=[(c,'') for c in letters(g.get('range'))]
        for it in g['items']:
            n=it['n']; q=it.get('q','')
            val=A[str(n)]; val=val[0] if isinstance(val,list) and len(val)==1 else val
            if '{{%d}}'%n in q:
                sel=ph_sel(n,ol,kind=='heading')
                o.append(f'<div class="qitem">{q.replace("{{%d}}"%n,sel)}</div>')
            else:
                sel=f'<select class="qselect" id="q{n}">{sel_opts(ol,"-- chọn --",kind=="heading")}</select>'
                o.append(f'<div class="qitem"><span class="qnum">{n}.</span> {q} {sel}</div>')
            units.append({'type':'select','n':n}); ans[str(n)]=val
    elif t=='completion':
        body=g.get('body','')
        bank=g.get('bank') or []
        if bank:
            o.append('<div class="wordbank">'+''.join(f'<span>{x["k"]}  {x["t"]}</span>' for x in bank)+'</div>')
            bol=[(x['k'],x['t']) for x in bank]
        def rep(m):
            n=int(m.group(1))
            if bank:
                units.append({'type':'select','n':n}); v=A[str(n)]; ans[str(n)]=v if isinstance(v,str) or len(v)>1 else v[0]
                return ph_sel(n,bol,True)
            units.append({'type':'text','n':n}); ans[str(n)]=variants(A[str(n)])
            return ph_text(n)
        body2=re.sub(r'\{\{(\d+)\}\}',rep,body)
        cls='summarybox' if g.get('kind') in('summary','bank','sentence','short') else 'notebox'
        ttl=f'<span class="stitle">{g["title"]}</span>' if g.get('title') else ''
        o.append(f'<div class="{cls}">{ttl}{body2}</div>')
    else:
        o.append(f'<div class="notebox">{g.get("body","")}</div>')
    o.append('</div>')
    return '\n'.join(o),units,ans,cbg
def passage_panel(p,idx,active):
    o=[f'<div class="passage-panel tab-content{" active" if active else ""}" id="passage-{idx}">']
    if p.get('title'): o.append(f'<div class="passage-title">{p["title"]}</div>')
    if p.get('instr'): o.append(f'<div class="passage-instr">{p["instr"]}</div>')
    for x in p['paras']:
        if x.get('sub'): o.append(f'<p><span class="subheading">{x["html"]}</span></p>')
        elif x.get('label'): o.append(f'<p><span class="subheading">{x["label"]}</span>\t{x["html"]}</p>')
        else: o.append(f'<p>{x["html"]}</p>')
    return '\n'.join(o)+'\n'
def ans_text(v):
    if isinstance(v,list):
        if len(v)==1: return v[0]
        return v[0]+' (hoặc '+', '.join(v[1:3])+')' if (all(len(x)<=3 for x in v) or all(x in('TRUE','FALSE','NOT GIVEN','YES','NO') for x in v)) else v[0]
    return v
def explain_panel(idx,keys,expl,d):
    o=[f'<div class="explain-panel" id="explainPanel-{idx}"><h3>📘 Giải thích chi tiết đáp án</h3>']
    for k in keys:
        e=expl.get(k)
        if not e: continue
        if k.startswith('q'):
            ns=[]
            for g in d['groups']:
                if g['type']=='mcq_multi':
                    for it in g['items']:
                        if 'q'+''.join(map(str,it['ns']))==k: ns=it['ns']
            lab=f'Câu {ns[0]}-{ns[-1]}.'; at=', '.join(str(d['answers'][str(n)] if not isinstance(d['answers'][str(n)],list) else d['answers'][str(n)][0]) for n in ns)
        else:
            lab=f'Câu {k}.'; at=ans_text(d['answers'][k])
        q=e['quote'].replace('&','&amp;').replace('<','&lt;')
        en=html.escape(e['en'],quote=False); vi=html.escape(e['vi'],quote=False)
        o.append(f'<div class="explain-item"><b class="eq">{lab}</b> Đáp án đúng: <span class="eans">{html.escape(at,quote=False)}</span><span class="equote">&ldquo;{q}&rdquo;</span><span class="etext etext-en"><b class="elang">EN:</b> {en}</span><span class="etext etext-vi"><b class="elang">VI:</b> {vi}</span></div>')
    o.append('</div>')
    return ''.join(o)
def qkeys(groups,d):
    ks=[]
    for g in groups:
        if g['type']=='mcq_multi':
            for it in g['items']: ks.append('q'+''.join(map(str,it['ns'])))
        elif g['type']=='completion':
            ks+= [str(int(x)) for x in re.findall(r'\{\{(\d+)\}\}',g['body'])]
        else:
            ks+= [str(it['n']) for it in g['items']]
    return ks
def data_block(no,total,pc,ans,units,cbg,extra=''):
    return ('var TEST_NUM = %d;\nvar TOTAL_QUESTIONS = %d;\nvar PASSAGE_COUNTS = %s;\n%svar APPS_SCRIPT_URL = "%s";\nvar ANS = %s;\nvar UNITS = %s;\nvar CHECKBOX_GROUPS = %s;\n'
        %(no,total,json.dumps(pc),extra,APPS,json.dumps(ans,ensure_ascii=False),json.dumps(units,ensure_ascii=False),json.dumps(cbg)))
DATA_RE=re.compile(r'var TEST_NUM = .*?var CHECKBOX_GROUPS = [^\n]*\n',re.S)
def full_html(d,expl):
    no=d['no']; s=S_FULL
    i=s.find('<div id="examArea">'); head=s[:i]; j=s.find('<button id="submitBtn"'); tail=s[j:]
    head=head.replace('IELTS Reading Test 1','IELTS Reading Test %d'%no)
    head=head.replace('thời gian: 60 phút, 40 câu hỏi','thời gian: 60 phút, %d câu hỏi'%d['total'])
    body=['<div id="examArea">']
    units=[];ans={};cbg=[]
    for pi in range(3):
        gs=[g for g in d['groups'] if g['p']==pi+1]
        body.append('  '+passage_panel(d['passages'][pi],pi,pi==0)+'  </div>')
        if pi==0: body.append('  <div id="divider"></div>')
        body.append(f'  <div class="question-panel tab-content{" active" if pi==0 else ""}" id="questions-{pi}">')
        for g in gs:
            h,u,a,c=render_group(g,d); body.append(h); units+=u; ans.update(a); cbg+=c
        body.append(explain_panel(pi,qkeys(gs,d),expl,d))
        body.append('  </div>')
    body.append('</div>\n\n')
    tail=DATA_RE.sub(lambda m:data_block(no,d['total'],d['pc'],ans,units,cbg),tail,count=1)
    return head+'\n'.join(body)+tail
TYPES={'Completion':('COMPLETION',{'completion'}),'Matching':('MATCHING',{'match'}),'MCQ':('MULTIPLE CHOICE',{'mcq','mcq_multi'}),'TFNG':('TRUE / FALSE / NOT GIVEN',{'tfng'}),'YNNG':('YES / NO / NOT GIVEN',{'ynng'})}
FOLDERS={'Completion':'Completion','Matching':'Matching','MCQ':'MultipleChoice','TFNG':'TrueFalseNotGiven','YNNG':'YesNoNotGiven'}
def one_html(d,pi,tkey,expl):
    no=d['no']; qt,types=TYPES[tkey]
    gs=[g for g in d['groups'] if g['p']==pi+1 and g['type'] in types]
    if not gs: return None
    p=d['passages'][pi]
    src=f"Test {no} — Passage {pi+1}"+(f": {re.sub('<.*?>','',p['title'])}" if p.get('title') else '')
    s=S_ONE; i=s.find('<div id="examArea">'); head=s[:i]; j=s.find('<button id="submitBtn"'); tail=s[j:]
    units=[];ans={};cbg=[];parts=[]
    for g in gs:
        h,u,a,c=render_group(g,d); parts.append(h); units+=u; ans.update(a); cbg+=c
    k=sum(g['q'][1]-g['q'][0]+1 for g in gs)
    # head replacements
    oldsrc="Test 1 — Passage 1: THE IMPORTANCE OF CHILDREN'S PLAY"
    head=head.replace(oldsrc,src).replace("<title>"+src+"</title>","<title>"+src+"</title>")
    head=re.sub(r'(thời gian: 30 phút, )\d+( câu)',lambda m:m.group(1)+str(k)+m.group(2),head)
    head=re.sub(r'(<span class="qtype-badge">)[^<]*',lambda m:m.group(1)+qt,head)
    head=head.replace("THE IMPORTANCE OF CHILDREN&#39;S PLAY",src)
    body=['<div id="examArea">','  '+passage_panel(p,0,True)+'  </div>','  <div class="question-panel tab-content active" id="questions-0">']
    body+=parts; body.append(explain_panel(0,qkeys(gs,d),expl,d)); body.append('  </div>'); body.append('</div>\n\n')
    extra='var QTYPE = %s;\nvar TEST_SOURCE = %s;\n'%(json.dumps(qt,ensure_ascii=False),json.dumps(src,ensure_ascii=False))
    tail=DATA_RE.sub(lambda m:data_block(no,k,[k],ans,units,cbg,extra),tail,count=1)
    return head+'\n'.join(body)+tail
def load_final(no):
    d=json.load(open(f'json/final2/t{no:02d}.json'))
    try: e=json.load(open(f'json/expl2/t{no:02d}.json'))
    except: e={}
    return d,e
