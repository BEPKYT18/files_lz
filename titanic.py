import pyarrow.parquet as pq
import pandas as pd
import matplotlib.pyplot as plt
import csv
data = pd.read_parquet("titanic.parquet", engine="pyarrow")

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
  

print(result)