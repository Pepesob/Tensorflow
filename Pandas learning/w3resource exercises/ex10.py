import pandas as pd
from ex2 import data


data = data.loc[(15<=data['score']) & (data['score']<=20)]
print(data)
