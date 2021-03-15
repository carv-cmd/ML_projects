import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from make_dataSets import data


# get_data import will prompt user for data file
# converted to numpy ndarray for vectorized operations
num_rows = np.shape(data)[0]
num_col = np.shape(data)[1]


####################################################
####################################################
def matrix_ops():
    # Columns parsed, offset due to the requirement of (x0 == 1 for all)
    x0 = np.ones(num_rows, dtype=int)
    # Parse data for processing store initially in x(i's) variables
    x1 = data[:, 0]

    # Generate feature matrix and its transpose
    matrix_x = np.array([x0, x1])
    transpose_x = np.transpose(matrix_x)

    # Calculate inner product (X'X) then determine inverse of (X'X)^-1
    m_dot_t = matrix_x.dot(transpose_x)
    mdt_inverse = np.linalg.inv(m_dot_t)

    # Prep Y column vector for X'Y operation
    y = data[:, 1].reshape((num_rows, 1))

    transpose_xy = matrix_x.dot(y)

    # Inner Product of "(X'X)^-1' and "transpose_xy"
    theta = mdt_inverse.dot(transpose_xy)

    # print(f''
    #       f'\nMatrixX: (shape: {matrix_x.shape})\n{matrix_x}\n'
    #       f'\nTransposeX: (shape: {transpose_x.shape})\n{transpose_x}\n'
    #       f'\nm_dot_t:\n{m_dot_t}\n'
    #       f'\nmdt_inverse:\n{mdt_inverse}\n'
    #       f'\ny: (shape: {y.shape})\n{y}\n'
    #       f'\ntranspose_xy: (shape: {transpose_xy.shape})\n{transpose_xy}\n'
    #       f'\nOptimal Values for Theta0/1:\n{theta}')

    return theta


###################################################
###################################################
if __name__ == "__main__":
    xf = data[:, 0]
    yf = data[:, 1]
    thetas = matrix_ops()
    b, m = thetas[0, :], thetas[1, :]

    print(f'\ntheta_0 (b) = {thetas[0, :]}\n'
          f'\ntheta_1 (m) = {thetas[1, :]}\n')

    x_array = np.linspace(data[:, 0].min() - 2, data[:, 0].max() + 2, 100)
    y_prediction = b + (m * x_array)

    print(f'\nOptimal Values for Thetas(m & b):\nm = {m}\nb = {b}')

    style.use('ggplot')
    plt.figure(figsize=(12, 8))
    plt.suptitle(f"Linear_Reg (Pure Maths Implementation)"
                 f"\n(m = {m}) & (b = {b})", fontsize=12)

    plt.title('Hypothesis Result', fontsize=10)
    plt.xlabel('Density', fontsize=8)
    plt.ylabel('Price', fontsize=8)
    plt.plot(xf, yf, '.')
    plt.plot(x_array, y_prediction, 'b')

    plt.tight_layout()
    plt.show()
