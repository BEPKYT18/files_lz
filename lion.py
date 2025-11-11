import docx
import pandas as pd
from collections import Counter
k=0
doc=docx.Document('lion.docx')
fullText = []
for para in doc.paragraphs:
    fullText.append(para.text)

fullText=' '.join(fullText).lower()

words = fullText.split (' ') 

war={}

for i in words:
    if i in war:
        war[i]+=1
    else:
        war[i]=1
    k+=1


df=pd.DataFrame(list(war.items()), columns=['Слово', 'Частота встречи, раз'])

print(df)

print(k)