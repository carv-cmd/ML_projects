import pandas as pd


data = {
    'SSN': [1111, 1112, 1113, 1114, 1115],
    'name': ['Benjamin', 'Marie + Kid', 'FatJew', 'JewBitch', 'Mims'],
    'age': [23, 22, 41, 57, 17],
    'height': [72, 58, 50, 78, 58],
    'gender': ['m', 'f', 'f', 'm', 'f']
}

df = pd.DataFrame(data)
df.set_index('SSN', inplace=True)

print(f"MEAN: {df['height'].mean()}\n")
print(f"MEDIAN: {df['height'].median()}\n")
print(f"MOST: {df['height'].mode()}\n")
print(f"standard Deviation: {df['height'].std()}\n")

print(f"Maximum Value: {df['height'].max()}\n")
print(f"Minimum Value: {df['height'].min()}\n")

print(f"DataFrame Complete Summary:\n {df.describe()}\n")
print(f"DataFrame Column Summary:\n {df['height'].describe()}")
