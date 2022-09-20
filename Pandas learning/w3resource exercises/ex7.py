import pandas as pd
from ex2 import data


data = data.loc[data['attempts'] > 2,:]
print(data)
