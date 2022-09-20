import pandas as pd
from ex2 import data


"""
for i,name in enumerate(data['name']):
    if name == 'James':
        data.iloc[i, 0] = 'Suresh'
        break
"""

data.loc[:,'name'].replace({'James':'Suresh'},inplace=True)

print(data)
