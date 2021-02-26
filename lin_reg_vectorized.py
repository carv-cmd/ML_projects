# Gradient Descent w/ Matrix/Vectorized Operations
####################################################
####################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import logging as logs

logs.basicConfig(filename='lin_regs.log', filemode='w', level=logs.INFO)

data = pd.read_csv('../linear_sets_csv/data_nn_new.csv', delimiter=',').to_numpy()
# data = pd.read_csv('linear_sets_csv/data_set_githubguy.csv', delimiter=',')
x = data[:, 0]
y = data[:, 1]


def gradient_descent(L):
    # initialize return variables
    m = 0
    b = 0
    # vectorized operations. iteration for gradient steps
    size = len(data)
    for i in range(Epoch):
        logs.info(f'\n-------------------({i})-------------------\n'
                  f'm_initial = {m}\nb_initial = {b}\n------------')
        m_grad = (1/size) * x * ((b + (m * x)) - y)
        b_grad = (1/size) * (b + (m * x)) - y
        m -= L * (m_grad.sum())
        b -= L * (b_grad.sum())
        logs.info(f'\n--------------------------------'
                  f'\nm_grad.sum() = {m_grad.sum()}'
                  f'\nb_grad.sum() = {b_grad.sum()}'
                  f'\n--------------------------------'
                  f'\nm_update = {m}\nb_update = {b}'
                  f'\n---------------------------------------\n')
    return m, b


####################################################
####################################################
L = .000001
Epoch = 1000
m, b = gradient_descent(L)

print(f'Final Thetas:\nm = {m}\nb = {b}')

y_prime = b + (m * x)

###################################################
###################################################
style.use('ggplot')
plt.title(f"Linear Regression\nm = {m}\nb = {b}")
plt.xlabel('Density')
plt.ylabel('Caching Faults')

plt.plot(x, y, '.')
plt.plot(x, y_prime, 'b')

plt.tight_layout()
plt.show()

