import pandas as pd
from ex2 import data


color = ['Red','Blue','Orange','Red','White','White','Blue','Green','Green','Red']
"""
color_data = pd.DataFrame(color,index=[chr(97+i) for i in range(len(color))])
color_data.rename(columns={0:'color'},inplace=True)
data = pd.concat([data, color_data],axis=1)
"""

data['color'] = color
print(data)
