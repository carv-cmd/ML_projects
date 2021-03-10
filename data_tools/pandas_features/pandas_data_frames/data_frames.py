import pandas as pd
import matplotlib.pyplot as plt

data = {
    'SSN': [1111, 1112, 1113, 1114],
    'name': ['Benjamin', 'Marie + Kid', 'FatJewBitch', 'BigNoseKike'],
    'age': [23, 22, 41, 57],
    'height': [72, 58, 50, 78],
    'weight': [160, 140, 315, 210],
    'gender': ['m', 'f', 'f', 'm']
}

df = pd.DataFrame(data)
df.set_index('SSN', inplace=True)

print(df)

##############################################################################
##############################################################################
# DataFrame Attributes and Functions
# print(df.head(2))
# print(df.tail(2))

# print(df.ndim)
# print(df.shape)
# print(df.size)
# print(df.dtypes)
# print(df.T)

# print(df['name'].iloc[1])
# print(df.iloc[2])
# print(df.iloc[0: 2])

##############################################################################
##############################################################################
df.plot.bar()
plt.show()
