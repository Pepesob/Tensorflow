import pandas as pd
from ex2 import data


data = data.loc[(data.loc[:,'attempts']<2) & (data.loc[:,'score']>15)]
print(data)
