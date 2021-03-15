import logging as logs
from sklearn.datasets import make_regression
import pandas as pd
import matplotlib.pyplot as plt

# logs.basicConfig(filename='dataSets.log', filemode='w', level=logs.INFO)


####################################################
def plotter():
    plt.suptitle(f'Generated Data Set: Size:{n}'
                 f'\nClose window for save prompt', fontsize=10)
    plt.xlabel('x_values', fontsize=8)
    plt.ylabel('y_values', fontsize=8)

    plt.scatter(x_gen, y_gen, c='red', marker='.')

    plt.tight_layout()

    plt.show()


####################################################
####################################################
n = int(input("\nEnter Size(n) of training examples: "))
# noisy = int(input("\nDesired Noise of dataSet: "))
noisy = 30

x_gen, y_gen = make_regression(n_samples=n, n_features=1, noise=noisy)

x_gen = x_gen.reshape(n)
y_gen = y_gen.reshape(n)
x_gen *= 500
y_gen *= 500

train_set = pd.DataFrame([x_gen, y_gen]).transpose()

# logs.info(f'\n----------------DataSetGenerated----------------'
#           f'\nData Attributes:'
#           f'\ntrain_set.size: {train_set.size}'
#           f'\ntrain_set.shape: {train_set.shape}\n'
#           f'\n{train_set}\n')

####################################################
####################################################
if __name__ == "__main__":
    plotter()

