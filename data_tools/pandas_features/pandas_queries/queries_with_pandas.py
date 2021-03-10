import pandas as pd


df = pd.read_csv('people.csv', delimiter=',')
df.set_index('SSN', inplace=True)

print(f"{df.loc[df['Age'] < 25]}\n")

print(f"{df.loc[(df['Age'] > 21) & (df['Weight'] < 150)]}\n")

print(f"{df.loc[(df['Age'] > 21) & (df['Weight'] < 150)]['Name']}\n")

