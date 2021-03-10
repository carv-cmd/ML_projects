import pandas as pd
import numpy as np


data = {
    'SSN': [1111, 1112, 1113, 1114, 1115],
    'name': ['Benjamin', 'Marie + Kid', 'FatJew', 'JewBitch', 'Mims'],
    'age': [23, 22, 41, 57, 17],
    'height': [72, 58, 50, 78, 58],
    'gender': ['m', 'f', 'f', 'm', 'f']
}

df = pd.DataFrame(data)
df.set_index('SSN', inplace=True)

print(df['height'].apply(np.log))
print(df['height'].apply(lambda x: x**2))
