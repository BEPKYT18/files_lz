import docx
import pandas as pd
from collections import Counter

doc=docx.Document('lion.docx')
fullText = []
for para in doc.paragraphs:
    fullText.append(para.text)

fullText=' '.join(fullText)

words = fullText.split (' ') 

war={}

for i in words:
    if i in war:
        war[i]+=1
    else:
        war[i]=1
    
print(war)