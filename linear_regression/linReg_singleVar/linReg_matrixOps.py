import numpy as np
from make_dataSets import train_set, logs, plt, n
from matplotlib import style
from save_agent import save_function

# make_dataSets generates random linear regression test sets
# converted to numpy ndarray for vectorized operations
train_set = train_set.to_numpy()
num_rows = np.shape(train_set)[0]
num_col = np.shape(train_set)[1]


####################################################
####################################################
def matrix_ops():
    """
    Steps taken to perform calculation listed below:
    1a). Columns parsed, offset due to the requirement of (x0 == 1 for all)
    1b). Parse data for processing store initially in x(i's) variables
    2a). Generate the feature matrix. (2b) As well as its transpose.
    3a). Calculate inner product (X'X). (3b). Then determine inverse of (X'X)^-1
    4). Reshape Y into column vector for X'Y operation
    5). Perform X'Y operation and store in transpose_xy variable
    6). Inner Product of mdt_inverse:"(X'X)^-1" and transpose_xy:"X'Y"
    """
    x0 = np.ones(num_rows, dtype=int)  # (1a)
    x1 = train_set[:, 0]  # (1b)

    matrix_x = np.array([x0, x1])  # (2a)
    transpose_x = np.transpose(matrix_x)  # (2b)

    m_dot_t = matrix_x.dot(transpose_x)  # (3a)
    mdt_inverse = np.linalg.inv(m_dot_t)  # (3b)

    y = train_set[:, 1].reshape((num_rows, 1))  # (4)

    transpose_xy = matrix_x.dot(y)  # (5)

    theta = mdt_inverse.dot(transpose_xy)  # (6)

    # logs.info(f'\n*********** MatrixResults ***********'
    #           f'\nMatrixX: (shape: {matrix_x.shape})'
    #           f'\nTransposeX: (shape: {transpose_x.shape})\n'
    #           f'\nm_dot_t:\n{m_dot_t}\n'
    #           f'\nmdt_inverse:\n{mdt_inverse}\n'
    #           f'\ntranspose_xy: (shape: {transpose_xy.shape})\n{transpose_xy}\n'
    #           f'\nOptimal Values for Theta0/1:\n{theta}')

    return theta


###################################################
###################################################
if __name__ == "__main__":
    xf = train_set[:, 0]
    yf = train_set[:, 1]
    thetas = matrix_ops()
    b, m = thetas[0, :], thetas[1, :]

    x_array = np.linspace(train_set[:, 0].min(), train_set[:, 0].max(), 100)
    y_prediction = b + (m * x_array)

    print(f'\nOptimal Values for Thetas(m & b):\nm = {m}\nb = {b}')

    style.use('ggplot')
    plt.figure()
    plt.suptitle(f"LinReg Model (Matrix Formulation)"
                 f"Input Size: {n}"
                 f"\n(m = {m}) & (b = {b})", fontsize=12)

    plt.title('Hypothesis Result', fontsize=10)
    plt.xlabel('Density', fontsize=8)
    plt.ylabel('Price', fontsize=8)
    plt.scatter(xf, yf, c='red', marker='.')
    plt.plot(x_array, y_prediction, 'b')

    plt.tight_layout()
    plt.show()

    save_function()
