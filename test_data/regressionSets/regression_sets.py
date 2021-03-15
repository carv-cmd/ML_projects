from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

n = 500

x, y = make_regression(n_samples=n, n_features=1, noise=75)

x = x.reshape(n)
y = y.reshape(n)

print(f'\nx: x.shape:{x.shape}\n{x}\n'
      f'\ny: y.shape:{y.shape}\n{y}')

data = (pd.DataFrame([x, y]).to_numpy()).transpose()



