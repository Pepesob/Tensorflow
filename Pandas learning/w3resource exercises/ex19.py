import pandas as pd
from ex2 import data


"""
data.drop(labels='attempts',axis=1,inplace=True)
"""

data.pop('attempts')
print(data)
