import pandas as pd
from ex2 import data


data.sort_values(by=['name','score'], ascending=[False, True], inplace=True)
print(data)
