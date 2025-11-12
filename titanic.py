import pyarrow.parquet as pq
import pandas as pd
import matplotlib.pyplot as plt
import csv
data = pd.read_parquet("titanic.parquet", engine="pyarrow")
t=0
data.to_csv("titanic.csv", index=False)

result={}

with open('titanic.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        if row[2] not in result:
            result[row[2]]={row[1]:1}
        elif row[2] in result:
            if row[1] not in result[row[2]]:
                result[row[2]][row[1]]=1
            elif row[1] in result[row[2]]:
                result[row[2]][row[1]]+=1
        t+=1
        
tclass=list(result.keys())

live={}
die={}
stat=[]

for i in range(len(result)):
    live[tclass[i]]=result[tclass[i]]['1']/t*100
    die[tclass[i]]=result[tclass[i]]['0']/t*100
    

   

plt.bar(range(len(live)), list(live.values()),color='blue', align='center')
plt.xticks(range(len(live)), list(live.keys()))
plt.show()
plt.bar(range(len(live)), list(live.values()),color='orange', align='center')
plt.xticks(range(len(live)), list(live.keys()))
plt.show()

