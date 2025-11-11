import re
import docx
import pandas as pd
from collections import Counter
k=0
doc=docx.Document('lion.docx')
fullText = []

for para in doc.paragraphs:
    fullText.append(para.text)
 
fullText=' '.join(fullText).lower()
fullText = re.findall('[a-zа-яё]+', fullText, flags=re.IGNORECASE)

war={}



for i in range(len(fullText)):
    if fullText[i] in war:
        war[fullText[i]]+=1
    else:
        war[fullText[i]]=1 

#print(war)

ks=[]
tms=[]
prs=[]

for key in war.keys():
    ks.append(key)
    tms.append(war[key])
    prs.append(int(war[key])/len(war)*100)

data = {
'Слово' : ks,
'Частота встречи, раз' : tms,
'Частота встречи в %' : prs
}

print(pd.DataFrame(data))


