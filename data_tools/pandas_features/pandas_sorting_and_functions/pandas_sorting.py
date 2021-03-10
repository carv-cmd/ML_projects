import pandas as pd
import numpy as np


data = {
    'SSN': [1116, 1112, 1111, 1113, 1115, 1114],
    'name': ['Benjamin', 'Marie&Kid', 'FatJew', 'JewBitch', 'Mims', 'FatJew'],
    'age': [23, 22, 41, 57, 17, 41],
    'height': [72, 58, 50, 78, 58, 54],
    'gender': ['m', 'f', 'f', 'm', 'f', 'f']
}

df = pd.DataFrame(data)
df.set_index('SSN', inplace=True)
print(f"\nInitial DataFrame:\n {df}\n")

dfi = df.sort_index()
print(f"\nSorted (Index) DataFrame:\n {dfi}\n")

dfv = df.sort_values(by=['name', 'age', 'height'])
print(f"\nSorted (Value/Column) DataFrame:\n {dfv}\n")

