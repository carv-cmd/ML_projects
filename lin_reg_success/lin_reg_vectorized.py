import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import logging as logs

# log change in gradient over time (optional -- overwrites prev log)
logs.basicConfig(filename='lin_regs.log', filemode='w', level=logs.INFO)

# pandas.read() to pull external data
# convert to numpy ndarray for vectorized operations
data = pd.read_csv('../linear_sets_csv/data.csv', delimiter=',').to_numpy()
x = data[:, 0]
y = data[:, 1]


####################################################
####################################################
def gradient_descent(L):
    """
    Uses numpy to horizontally calc total hypothesis error for given feature vectors
    Store temp 'm_grad'/'b_grad' vars while calculating hypothesis for each data point
    Simultaneously sum errors, apply learning rate, then update thetas ('m'/'b') respectively 
    :param L: 'Learning Rate' or 'step size' taken in opposite direction of gradient
    :return: optimal values of 'm' and 'b' for given data set regression line
    """
    # initialize return variables
    m = 0
    b = 0
    # iteration for gradient steps. Determined by global Epoch
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
# Need to fine tune as the learning rate just looks wrong, but mostly works so idk..
L = .000001
Epoch = 1000
m, b = gradient_descent(L)

print(f'\nOptimal Thetas:\nm = {m}\nb = {b}')
print(f'\ndata_x_Min = {x.min()}\ndata_x_Max = {x.max()}\n')

userX = float(input(f'Input a density for pricing estimate: '))
model_prediction = round(b + (m * userX), 8)
print(f'Estimated Price: {model_prediction}')

y_prediction = b + (m * x)

###################################################
###################################################
style.use('ggplot')

plt.title(f"Linear Regression\nm = {m}\nb = {b}")
plt.xlabel('Density')
plt.ylabel('Price')

plt.plot(x, y, '.')
plt.plot(userX, model_prediction, 'b.')

plt.plot(x, y_prediction, 'r')

plt.tight_layout()
plt.show()
