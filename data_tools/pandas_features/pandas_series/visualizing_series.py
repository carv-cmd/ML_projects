import pandas as pd
import matplotlib.pyplot as plt


s1 = pd.Series([1, 2, 3, 4, 7, 5, 1, 2], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

plt.figure(1)
s1.plot()

plt.figure(2)
s1.plot.pie()

plt.show()
