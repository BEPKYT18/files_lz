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

df=pd.DataFrame(list(war.items()), columns=['Слово', 'Частота встречи, раз'])

print(df)

print(k)