import numpy as np
from get_data import data

# logs.basicConfig(filename='multi_lin_reg.log', filemode='w', level=logs.INFO)

####################################################
####################################################
# DataSet imported from get_data, shape stored for ones/zeros arrays
num_rows = np.shape(data)[0]
num_col = np.shape(data)[1]

# Columns parsed, offset due to the requirement of (x0 == 1 for all)
x0 = np.ones(num_rows)
x1, x2, x3, x4 = data[:, 0], data[:, 1], data[:, 2], data[:, 3]
x1_u, x2_u, x3_u, x4_u = x1.mean(), x2.mean(), x3.mean(), x4.mean()
x1_std, x2_std, x3_std, x4_std = x1.std(), x2.std(), x3.std(), x4.std()

# Scale features using the mean normalization method
x1 = (x1 - x1_u) / x1_std
x2 = (x2 - x2_u) / x2_std
x3 = (x3 - x3_u) / x3_std
x4 = (x4 - x4_u) / x4_std

# Actual Y values from data set
Y = data[:, 4]

####################################################
####################################################
iteration = []
total_error = []


def cost_function(t, i):
    """
    Called from gradient_descent() after summation and gradients calculations
    Passed t[num_col] params, calculates total error/cost for given params before next iter
    Gradient descent iter_num appended to 'x_iter', plots to x-axis of CF_graph
    Total error value appended to 't_error', plots to y-axis of CF_graph
    :param t: current hypothesis variables
    :param i: grad_des iteration
    :return: updates global list values at runtime
    """
    try:
        iteration.append(i)
        cost = (Y - ((x0 * t[0]) + (x1 * t[1]) + (x2 * t[2]) + (x3 * t[3]) - (x4 * t[4]))) ** 2
        total_error.append(cost.sum() / float(len(data)))
        # logs.info(f'\n-----------Cost-Function-----------'
        #           f'\nIteration:\n{iteration}'
        #           f'\nTotal_Error\n{total_error}\n')
    except NameError or ValueError:
        print("Cost_Function FAILED!")
        pass


####################################################
####################################################
def gradient_descent(L, Epoch):
    """
    Much like single variable regression with the obvious multivariate twist
    Uses numpy to 'horizontally' calculate total hypothesis error for given feature vectors
    Better to use pure matrix data structures and operations?
    Store temp t_gradient vars while calculating hypothesis for each data point
    Simultaneously sum errors, apply learning rate, then update thetas respectively
    :return: optimal hypothesis values of the regression line for the given dataSet
    """
    t = np.zeros(num_col)
    n = float(len(data))
    for irx in range(Epoch):
        # logs.info(f'\n-----------Iteration({irx})-----------'
        #           f'\ntheta_initials = {t}'
        #           f'\n-----------------------')
        x4_grad = (1/n) * x4 * (((x1 * t[1]) + (x2 * t[2]) + (x3 * t[3]) - (x4 * t[4])) - Y)
        x3_grad = (1/n) * x3 * (((x1 * t[1]) + (x2 * t[2]) + (x3 * t[3]) - (x4 * t[4])) - Y)
        x2_grad = (1/n) * x2 * (((x1 * t[1]) + (x2 * t[2]) + (x3 * t[3]) - (x4 * t[4])) - Y)
        x1_grad = (1/n) * x1 * (((x1 * t[1]) + (x2 * t[2]) + (x3 * t[3]) - (x4 * t[4])) - Y)
        x0_grad = (1/n) * (((x1 * t[1]) + (x2 * t[2]) + (x3 * t[3]) - (x4 * t[4])) - Y)

        t[4] -= L * x4_grad.sum()
        t[3] -= L * x3_grad.sum()
        t[2] -= L * x2_grad.sum()
        t[1] -= L * x1_grad.sum()
        t[0] -= L * x0_grad.sum()

        cost_function(t, irx)

    return t


####################################################
####################################################
def print_thetas():
    print(f'\nOptimal Prediction Vars Given\nLearning_Rate:({L}) && Epoch:({Epoch})'
          f'\nop[0](holder):{op[0]}'
          f'\nop[1](size):  {op[1]}'
          f'\nop[2](rooms): {op[2]}'
          f'\nop[3](floors):{op[3]}'
          f'\nop[4](yr_old):{op[4]}\n')


####################################################
####################################################
# L: 'step size' that will be taken in opposite direction of gradient
# Epoch: number of iterations for which gradient descent should run
if __name__ == "__main__":
    L = .0003
    Epoch = 18000
    op = gradient_descent(L, Epoch)
    print_thetas()
