import os,shutil,json
from webgen import *
OUT='out2/PACK'
FT=OUT+'/ielts_src/reading/FullTest'; TD=OUT+'/ielts_src/reading/TheoDang'
os.makedirs(FT,exist_ok=True)
cnt={}
for no in range(11,50):
    d,e=load_final(no)
    open(f'{FT}/Test{no}_Reading.html','w',encoding='utf8').write(full_html(d,e))
    for tk,fo in FOLDERS.items():
        for pi in range(3):
            h=one_html(d,pi,tk,e)
            if h:
                os.makedirs(f'{TD}/{fo}',exist_ok=True)
                open(f'{TD}/{fo}/Test{no}_Passage{pi+1}_{tk}.html','w',encoding='utf8').write(h)
                cnt[fo]=cnt.get(fo,0)+1
print(cnt,sum(cnt.values()))
