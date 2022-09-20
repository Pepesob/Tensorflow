import pandas as pd
from ex2 import data


data['qualify'].replace({'yes':True,'no':False},inplace=True)
print(data)
