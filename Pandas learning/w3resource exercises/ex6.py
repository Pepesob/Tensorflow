import pandas as pd
from ex2 import data


index = [1,3,5,6]
index = [chr(index[i]+96) for i in range(len(index))]

data = data.loc[index, ['name','score']]
print(data)
