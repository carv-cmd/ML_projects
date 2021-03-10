import pandas as pd

names = {
    'SSN': [2, 5, 7, 8],
    'name': ['Alice', 'Bob', 'Eve', 'Ben']
}

ages = {
    'SSN': [2, 1, 3, 8],
    'age': [20, 19, 17, 23]
}

df1 = pd.DataFrame(names)
df2 = pd.DataFrame(ages)

merge_outer = pd.merge(df1, df2, on='SSN', how='outer')
merge_outer.set_index('SSN', inplace=True)

merge_left = pd.merge(df1, df2, on='SSN', how='left')
merge_left.set_index('SSN', inplace=True)

merge_right = pd.merge(df1, df2, on='SSN', how='right')
merge_right.set_index('SSN', inplace=True)

merge_inner = pd.merge(df1, df2, on='SSN', how='inner')
merge_inner.set_index('SSN', inplace=True)

print(f'Dataframe 1:\n{df1}\nDataframe 2:\n{df2}\n')

print(f'\nMerge Outer:\n{merge_outer}\n')
print(f'\nMerge Left:\n{merge_left}\n')
print(f'\nMerge Right:\n{merge_right}\n')
print(f'\nMerge Inner:\n{merge_inner}\n')
