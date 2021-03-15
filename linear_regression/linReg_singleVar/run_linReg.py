from linReg_iterative import *
from linReg_matrixOps import *
from save_agent import save_function


####################################################
####################################################
# Linear Regression Model ~~ Iterative Implementation
L = .0001
Epoch = 10
m_iter, b_iter = gradient_descent(L, Epoch)
print(f"\nOptimal Values for Theta's (Iterative Solution):\nm = {m_iter}\nb = {b_iter}\n")

# Linear Regression Model ~~ Matrix Formulation
thetas = matrix_ops()
b_mat, m_mat = thetas[0, :], thetas[1, :]
print(f"\nOptimal Values for Theta's (Matrix Formulation):\nm = {m_mat}\nb = {b_mat}\n")


####################################################
####################################################
# Generate a set of sample X values
x_array = np.linspace(x.min() - 2, x.max() + 2, 100)

# Generate Y values for iter and matrix predictions respectively
iter_prediction = b_iter + (m_iter * x_array)
matrix_prediction = b_mat + (m_mat * x_array)

####################################################
####################################################
if __name__ == "__main__":
    style.use('ggplot')

    fig = plt.figure(figsize=(12, 9))
    fig.suptitle(f"Linear Regression Models"
                 f"\nTrainingSet Size: {n}", fontsize=10)
    is_ax1 = fig.add_subplot(221)
    mf_ax2 = fig.add_subplot(222)
    cf_ax3 = fig.add_subplot(212)

    is_ax1.set_title('Iterative Solution')
    is_ax1.set_xlabel('Density', fontsize=6)
    is_ax1.set_ylabel('Price', fontsize=6)
    is_ax1.scatter(x, y, c='blue', marker='.')
    is_ax1.plot(x_array, iter_prediction, 'r')

    mf_ax2.set_title('Matrix Formulation')
    mf_ax2.set_xlabel('Density', fontsize=6)
    mf_ax2.set_ylabel('Price', fontsize=6)
    mf_ax2.scatter(x, y, c='blue', marker='.')
    mf_ax2.plot(x_array, matrix_prediction, 'r')

    cf_ax3.set_title('Iterative Cost Function')
    cf_ax3.set_xlabel('Iterations', fontsize=6)
    cf_ax3.set_ylabel('Total Error', fontsize=6)
    cf_ax3.plot(x_iter, t_error, 'b..')

    plt.tight_layout()
    plt.show()

    save_function()
