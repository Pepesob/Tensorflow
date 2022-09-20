import pandas as pd


data = pd.DataFrame([[1, 4, 7], [2, 5, 8], [3, 6, 9]],columns=['col1', 'col2', 'col3'])
print(data)
data.columns = ['Column1','Column2','Column3']
print(data)
