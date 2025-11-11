import tabulate
import re
import docx
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
k=0
doc=docx.Document('lion.docx')
fullText = []

for para in doc.paragraphs:
    fullText.append(para.text)
 
fullText=' '.join(e for e in fullText if e.isalnum()).lower()
Text = re.findall('[a-zа-яё]+', fullText, flags=re.IGNORECASE)

war={}



for i in range(len(Text)):
    if Text[i] in war:
        war[Text[i]]+=1
    else:
        war[Text[i]]=1 

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

print(tabulate.tabulate(data, headers='data.keys', tablefmt='fancy_grid'))

patt='[0-9,a-z]'


letters=''.join(e for e in fullText if e.isalnum())

letters= re.sub(patt, '', letters)
letters=list(letters)
print(letters)

stat={}

for i in range(len(letters)):
    if letters[i] in war:
        stat[letters[i]]+=1
    else:
        stat[letters[i]]=1 

#plt.hist(stat.keys, color = 'blue', edgecolor = 'black',
         #bin=int(180/5))
