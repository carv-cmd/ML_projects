import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from get_data import data


# get_data import will prompt user for data file
# converted to numpy ndarray for vectorized operations
num_rows = np.shape(data)[0]
num_col = np.shape(data)[1]

# Columns parsed, offset due to the requirement of (x0 == 1 for all)
x0 = np.ones(num_rows, dtype=int)

# Parse data for processing store initially in x(i's) variables
x1, y = data[:, 0], data[:, 1]

# Create feature matrix
matrix_X = np.array([x0, x1])
transpose_X = np.transpose(matrix_X)

print(f'\nMatrixX:\n{matrix_X}\nTransposeX\n{transpose_X}\n'
      f'\nMatrixX.shape:{matrix_X.shape}\n'
      f'\nTransposeX.shape:{transpose_X.shape}')

m_dot_t = matrix_X.dot(transpose_X)

mdt_inverse = np.linalg.inv(m_dot_t)

transpose_XY = transpose_X.dot(np.array(y))

print(f'\nm_dot_t:\n{m_dot_t}\n'
      f'\nmdt_inverse:\n{mdt_inverse}\n'
      f'\ntransposeY:\n{transpose_XY}')

####################################################
####################################################
x_iter = []
t_error = []


def cost_function(m, b, i):
    """
    Called from gradient_descent() after summation and gradients calculations
    Passed iter(i) 'm' & 'b' params, calculates total error/cost for given params before next iter
    Gradient descent iter_num appended to 'x_iter', plots to x-axis of CF_graph
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
    # iteration for gradient steps. Determined by global Epoch
    size = len(data)
    for i in range(Epoch):
        m_grad = (1/size) * x * ((b + (m * x)) - y)
        b_grad = (1/size) * (b + (m * x)) - y
        m -= L * (m_grad.sum())
        b -= L * (b_grad.sum())
        cost_function(m, b, i)
    return m, b


####################################################
####################################################
L = .0001
Epoch = 10
# m, b = gradient_descent(L)

# x_array = np.linspace(x.min() - 2, x.max() + 2, 100)
# y_prediction = b + (m * x_array)
#
# print(f'\nOptimal Values for Thetas(m & b):\nm = {m}\nb = {b}')
#
# ###################################################
# ###################################################
# style.use('ggplot')
#
# fig = plt.figure(figsize=(6, 9))
# gd_ax1 = fig.add_subplot(211)
#
# cf_ax2 = fig.add_subplot(212)
#
# fig.suptitle(f"Linear_Reg (Pure Maths Implementation)"
#              f"\n(m = {round(m, 4)}) & (b = {round(b, 4)})", fontsize=12)
#
# gd_ax1.set_title('Hypothesis Result', fontsize=10)
# gd_ax1.set_xlabel('Density', fontsize=8)
# gd_ax1.set_ylabel('Price', fontsize=8)
# gd_ax1.plot(x, y, '.')
# gd_ax1.plot(x_array, y_prediction, 'b')
#
# cf_ax2.set_title("Cost Function", fontsize=10)
# cf_ax2.set_xlabel("Iterations", fontsize=8)
# cf_ax2.set_ylabel("Total Error", fontsize=8)
# cf_ax2.plot(x_iter, t_error, 'b-')

# if __name__ == "__main__":
#     plt.tight_layout()
#     plt.show()