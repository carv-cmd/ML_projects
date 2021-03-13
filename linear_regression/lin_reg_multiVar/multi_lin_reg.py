import numpy as np
from get_data import data
import logging as logs

logs.basicConfig(filename='multi_lin_reg.log', filemode='w', level=logs.INFO)

####################################################
####################################################
# DataSet imported from get_data, shape stored for ones/zeros arrays
num_rows = np.shape(data)[0]
num_col = np.shape(data)[1]
print(f'num_col: {num_col}')

# Parse data for processing store initially in x(i's) variables
# Store mean and standard deviation subsequent calculation
x1, x2, x3, x4 = data[:, 0], data[:, 1], data[:, 2], data[:, 3]
# x1_u, x2_u, x3_u, x4_u = x1.mean(), x2.mean(), x3.mean(), x4.mean()
# x1_std, x2_std, x3_std, x4_std = x1.std(), x2.std(), x3.std(), x4.std()
#
# # Scale features using the mean normalization method (element-to-element)
# # Update initial x(i's) to normalized values
# x1 = (x1 - x1_u) / x1_std
# x2 = (x2 - x2_u) / x2_std
# x3 = (x3 - x3_u) / x3_std
# x4 = (x4 - x4_u) / x4_std

# Columns parsed, offset due to the requirement of (x0 == 1 for all)
x0 = np.ones(num_rows, dtype=int)

# # Actual Y values from data set
y_val = np.reshape(np.array(data[:, 4]), (num_rows, 1))

# Generate feature "matrix" data structure
features = np.array([x0, x1, x2, x3, x4])

print(f'\nFeatures Transposed and Scaled by Mean Normalization:'
      f'\n{features}\n\nY_Values:\n{y_val}\n'
      f'\nFeatures:{type(features)}, {features.shape}'
      f'\ny_values:{type(y_val)}, {y_val.shape}')

####################################################
####################################################
iteration = []
total_error = []


def cost_function(parameters, i):
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
        cost = (y_val - np.dot(features, parameters)) ** 2
        print(cost)
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
    parameters = np.reshape(np.ones(num_col), (num_col, 1))
    # prediction = np.zeros(num_col)
    n = float(len(data))
    for irx in range(Epoch):
        pass

        # temp = (1/n) * L * (features.dot(parameters) - y_val)

        print(f'\nParameters:\n{parameters}'
              f'\nfeatures.shape = {features.shape}'
              f'\nparameters.shape = {parameters.shape}')
        #
        # logs.info(f'\n-----------Iteration({irx})-----------'
        #           f'\nInitial Prediction:\n{parameters}'
        #           f'\n-----------------------')

        # prediction = prediction - temp
        # cost_function(prediction, irx)

    # return t



# ####################################################
# ####################################################
# def print_thetas():
#     print(f'\nOptimal Prediction Vars Given\nLearning_Rate:({L}) && Epoch:({Epoch})'
#           f'\nop[0](holder):{op[0]}'
#           f'\nop[1](size):  {op[1]}'
#           f'\nop[2](rooms): {op[2]}'
#           f'\nop[3](floors):{op[3]}'
#           f'\nop[4](yr_old):{op[4]}\n')
#
#
####################################################
####################################################
# L: 'step size' that will be taken in opposite direction of gradient
# Epoch: number of iterations for which gradient descent should run
if __name__ == "__main__":
    L = .0003
    Epoch = 1
    op = gradient_descent(L, Epoch)
    # print_thetas()
