import pandas as pd
from ex2 import data
import numpy as np


data = data.loc[data['score'].isnull(),:]
print(data)
