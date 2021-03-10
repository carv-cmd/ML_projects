import pandas as pd
import matplotlib.pyplot as plt

t1 = 'Morning'
t2 = 'Night'

sample1 = pd.Series([8, 45, 57, 78], ['ph', 'hydroxide', 'calcium', 'salinity'])
sample1.name = t1
s1 = sample1.sort_index()


sample2 = pd.Series([10, 29, 45, 12], ['ph', 'hydroxide', 'calcium', 'salinity'])
sample2.name = t2
s2 = sample2.sort_index()

print(sample1)
print(sample2)


def squared(x):
    return x*2


s1.apply(squared)
s2.apply(squared)

print(s1)
print(s2)


