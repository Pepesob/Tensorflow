import pandas as pd


exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]
data = pd.DataFrame(exam_data)
print(data,'\n')

"""
for i in data.itertuples():
    for j in range(1,len(i)):
        print(i[j],end=" ")
    print()
"""

for index, row in data.iterrows():
    print(row['name'],row['score'])

