import os,json,re
from docgen import *
from webgen import load_final
OUT='out2/PACK/ielts_src/reading/TaiLieu_Word'
T=[load_final(n)[0] for n in range(1,50)]
N=len(T)
os.makedirs(OUT+'/TungTest',exist_ok=True); os.makedirs(OUT+'/TheoDang',exist_ok=True)
# per-test
for d in T:
    doc=new_doc()
    P(doc,f'IELTS READING — TEST {d["no"]}',18,bold=True,align='c',color=BLUE)
    P(doc,f'Thời gian: 60 phút · {d["total"]} câu · DATA GNOMIO 2026',10.5,align='c')
    P(doc,'')
    add_test(doc,d)
    doc.save(f'{OUT}/TungTest/IELTS_Reading_Test_{d["no"]:02d}.docx')
# full
doc=new_doc()
P(doc,f'IELTS READING — TỔNG HỢP {N} TEST',22,bold=True,align='c',color=BLUE)
P(doc,f'Test 1 – Test {N} · DATA GNOMIO 2026',11,align='c')
P(doc,'Mỗi test gồm 3 passage, câu hỏi và bảng đáp án ngay sau test.',10.5,align='c')
for k,d in enumerate(T):
    pagebreak(doc) if k else P(doc,'')
    P(doc,f'TEST {d["no"]}',20,bold=True,align='c',color=BLUE)
    add_test(doc,d)
doc.save(f'{OUT}/IELTS_Reading_Full_{N}_Test.docx')
# by type
TY=[('Dang1_Completion','DẠNG 1 — COMPLETION (Hoàn thành câu / ghi chú / bảng / tóm tắt)','Gồm: Sentence Completion, Note/Summary/Table Completion, Summary Completion (word list).',{'completion'}),
('Dang2_Matching','DẠNG 2 — MATCHING (Nối thông tin)','Gồm: Matching Headings, Matching Information/Paragraphs, Matching Features/People, Matching Sentence Endings.',{'match'}),
('Dang3_TrueFalseNotGiven','DẠNG 3 — TRUE / FALSE / NOT GIVEN',None,{'tfng'}),
('Dang4_YesNoNotGiven','DẠNG 4 — YES / NO / NOT GIVEN',None,{'ynng'}),
('Dang5_MultipleChoice','DẠNG 5 — MULTIPLE CHOICE (Trắc nghiệm)','Gồm Multiple Choice (1 đáp án) và Multiple Choice (chọn TWO/THREE đáp án).',{'mcq','mcq_multi'})]
for fn,title,sub,types in TY:
    doc=new_doc()
    P(doc,title,18,bold=True,align='c',color=BLUE)
    if sub: P(doc,sub,10.5)
    P(doc,f'Tổng hợp từ {N} đề IELTS Reading (Test 1 - Test {N}) — DATA GNOMIO 2026',10.5,bold=True)
    P(doc,'')
    rows=[]
    for d in T:
        for pi in range(3):
            gs=[g for g in d['groups'] if g['p']==pi+1 and g['type'] in types]
            if not gs: continue
            passage(doc,d['no'],pi,d)
            for g in gs: group(doc,g,d)
            P(doc,'')
        for n,a in key_rows(d,types): rows.append((d['no'],n,a))
    pagebreak(doc)
    P(doc,'ĐÁP ÁN — ANSWER KEY',16,bold=True,align='c',color=BLUE)
    key_table(doc,rows,True)
    doc.save(f'{OUT}/TheoDang/IELTS_{fn}.docx')
    print(fn,len(rows))
