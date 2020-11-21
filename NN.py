import numpy as np
import pandas as pd

arqPath = "diamonds.csv"

data = pd.read_csv(arqPath, index_col = 0)

print(data)

print(data['price'])

data['volume'] = data['x'] * data['y'] * data['z']

print(data['volume'])

#data.sort()

data.head()

data.tail(3)