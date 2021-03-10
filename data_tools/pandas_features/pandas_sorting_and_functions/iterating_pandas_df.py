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

print(f"Initial DataFrame: {df}\n")

print('\nIterating Over Complete Data Frame')
for key1, value1 in df.iteritems():
    print(f"{key1} for {value1}\n")

print('\nIterating Over a Specific Column')
for key2, value2 in df['name'].iteritems():
    print(f"Index ID: {key2}:: Mapped to: {value2}/n")

print('\nIterating Over a Specific Row')
for row in df.iterrows():
    print(f'{row}\n')

