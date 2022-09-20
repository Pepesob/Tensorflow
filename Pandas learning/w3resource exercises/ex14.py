import pandas as pd
from ex2 import data


data = data.loc[:,'score'].mean(skipna=True)
print(data)
