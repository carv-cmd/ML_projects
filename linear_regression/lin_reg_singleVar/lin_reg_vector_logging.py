import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import logging as logs
from get_data import data


# log change in gradient over time (optional -- overwrites prev log)
logs.basicConfig(filename='lin_regs.log', filemode='w', level=logs.INFO)

# get_data import will prompt user for data file
# converted to numpy ndarray for vectorized operations
print(f'\ndataSet shape: {data.shape}\n')
x_column = int(input('Enter x_column: '))
y_column = int(input('Enter y_column: '))
x = data[:, x_column]
y = data[:, y_column]


####################################################
####################################################
x_iter = []
t_error = []
def cost_function(m, b, i):
    """
    Called from gradient_descent() after gradient summation calculation
    Passed iter(i) 'm' & 'b' params, calculates total error/cost for given params before next iter
    Gradient descent iter_num appended to 'x_iter', plot to x-axis of CF_graph
    Total error value appended to 't_error', plots to y-axis of CF_graph
    :param m: iter(i) m from gradient descent
    :param b: iter(i) b from gradient descent
    :param i: grad_des iteration
    :return: updates global list values at runtime
    """
    try:
        x_iter.append(i)
        cost = (y - (m * x + b)) ** 2
        t_error.append(cost.sum() / float(len(data)))
        logs.info(f'\n--------------------------------'
                  f'\nx_iter = [{x_iter}]'
                  f'\nt_error = [{t_error}]'
                  f'\n---------------------------------------\n')
    except NameError or ValueError:
        print('cost_function FAILED')
        pass


####################################################
####################################################
def gradient_descent(L):
    """
    Uses numpy to 'horizontally' calculate total hypothesis error for given feature vectors
    Store temp 'm_grad'/'b_grad' vars while calculating hypothesis for each data point
    Simultaneously sum errors, apply learning rate, then update thetas ('m'/'b') respectively
    :param L: 'Learning Rate' or 'step size' taken in opposite direction of gradient
    :return: optimal values of 'm' and 'b' for given data set regression line
    """
    # initialize return variables
    m, b = 0, 0
    size = len(data)

    # iteration for gradient steps. Determined by global Epoch
    for i in range(Epoch):
        logs.info(f'\n-------------------({i})-------------------\n'
                  f'm_initial = {m}\nb_initial = {b}\n------------')
        m_grad = (1/size) * x * ((b + (m * x)) - y)
        b_grad = (1/size) * (b + (m * x)) - y
        m -= L * (m_grad.sum())
        b -= L * (b_grad.sum())
        cost_function(m, b, i)
        logs.info(f'\n--------------------------------'
                  f'\n\tm_grad.sum() = {m_grad.sum()}'
                  f'\n\tb_grad.sum() = {b_grad.sum()}'
                  f'\n--------------------------------'
                  f'\n\tm_update = {m}\n\tb_update = {b}'
                  f'\n---------------------------------------\n')

    return m, b


####################################################
####################################################
L = .0001
Epoch = 10
m, b = gradient_descent(L)

x_array = np.linspace(x.min() - 2, x.max() + 2, 100)
y_prediction = b + (m * x_array)

print(f'\nOptimal Values for Thetas(m & b):\nm = {m}\nb = {b}')

###################################################
###################################################
style.use('ggplot')

fig = plt.figure(figsize=(6, 9))
gd_ax1 = fig.add_subplot(211)

cf_ax2 = fig.add_subplot(212)

fig.suptitle(f"Linear_Reg (Pure Maths Implementation)"
             f"\n(m = {round(m, 4)}) & (b = {round(b, 4)})", fontsize=12)

gd_ax1.set_title('Hypothesis Result', fontsize=10)
gd_ax1.set_xlabel('Density', fontsize=8)
gd_ax1.set_ylabel('Price', fontsize=8)
gd_ax1.plot(x, y, '.')
gd_ax1.plot(x_array, y_prediction, 'b')

cf_ax2.set_title("Cost Function", fontsize=10)
cf_ax2.set_xlabel("Iterations", fontsize=8)
cf_ax2.set_ylabel("Total Error", fontsize=8)
cf_ax2.plot(x_iter, t_error, 'b-')

if __name__ == "__main__":
    plt.tight_layout()
    plt.show()
