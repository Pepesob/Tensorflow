import numpy as np
import pandas as pd
from ex2 import data


new = {'name' : "Suresh", 'attempts': 1, 'qualify': "yes",'score': 15.5}
new = pd.Series(new).to_frame().T
new.set_index(np.array(['k']),inplace=True)
data = pd.concat([data,new],ignore_index=False)
print(data,'\n')
data.drop(index='k',inplace=True)
print(data)
