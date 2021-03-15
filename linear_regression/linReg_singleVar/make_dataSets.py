from sklearn.datasets import make_regression
import pandas as pd
import logging as logs

logs.basicConfig(filename='dataSets.log', filemode='w', level=logs.INFO)

n = 500

x, y = make_regression(n_samples=n, n_features=1, noise=75)

x = x.reshape(n)
y = y.reshape(n)

data = (pd.DataFrame([x, y]).to_numpy()).transpose()

logs.info(f'\n----------------DataSetsGenerated----------------'
          f'\n{data}')

if __name__ == "__main__":
    print(data)
