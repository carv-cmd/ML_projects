from matrix_formulation import *
from lin_reg_vectorized import *


def wait_function():
    """ Waits for user input to proceed """
    while True:
        user_input = str(input("Press ENTER to continue... "))
        if user_input != '':
            break
        return


####################################################
####################################################
# Linear Regression Model ~~ Iterative Implementation
# wait_function()
L = .0001
Epoch = 10
m_iter, b_iter = gradient_descent(L, Epoch)
print(f"\nOptimal Values for Theta's (Iterative Solution):\nm = {m_iter}\nb = {b_iter}\n")

# Linear Regression Model ~~ Matrix Formulation
# wait_function()
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
# wait_function()

####################################################
####################################################
if __name__ == "__main__":
    style.use('ggplot')

    fig = plt.figure(figsize=(9, 6))
    fig.suptitle(f"Linear Regression Models")
    is_ax1 = fig.add_subplot(221)
    mf_ax2 = fig.add_subplot(222)
    cf_ax3 = fig.add_subplot(212)

    is_ax1.set_title('Iterative Solution')
    is_ax1.set_xlabel('Density', fontsize=8)
    is_ax1.set_ylabel('Price', fontsize=8)
    is_ax1.plot(x, y, 'b.')
    is_ax1.plot(x_array, iter_prediction, 'r')

    mf_ax2.set_title('Matrix Formulation')
    mf_ax2.set_xlabel('Density', fontsize=8)
    mf_ax2.set_ylabel('Price', fontsize=8)
    mf_ax2.plot(x, y, 'b.')
    mf_ax2.plot(x_array, matrix_prediction, 'r')

    cf_ax3.set_title('Iterative Cost Function')
    cf_ax3.set_xlabel('Iterations', fontsize=8)
    cf_ax3.set_ylabel('Total Error', fontsize=8)
    cf_ax3.plot(x_iter, t_error, 'b-')

    plt.tight_layout()
    plt.show()
