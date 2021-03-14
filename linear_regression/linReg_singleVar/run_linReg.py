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
wait_function()
L = .0001
Epoch = 10
m_iter, b_iter = gradient_descent(L, Epoch)
print(f"\nOptimal Values for Theta's (Iterative Solution):\nm = {m_iter}\nb = {b_iter}\n")

# Linear Regression Model ~~ Matrix Formulation
wait_function()
thetas = matrix_ops()
b_mat, m_mat = thetas[0, :], thetas[1, :]
print(f"\nOptimal Values for Theta's (Matrix Formulation):\nm = {m_mat}\nb = {b_mat}\n")


####################################################
####################################################
# Generate a set of sample X values
x_array = np.linspace(x.min() - 2, x.max() + 2, 100)

# Generate Y values for iter and matrix predictions respectively
iter_prediction = b_iter + (m_iter * x_array)
matrix_prediction = b_mat + (m_iter * x_array)

####################################################
####################################################
if __name__ == "__main__":
    style.use('ggplot')

    plt.suptitle(f"Linear Regression Models")
    plt.xlabel('Density', fontsize=8)
    plt.ylabel('Price', fontsize=8)

    plt.plot(x, y, 'b.')
    plt.plot(x_array, iter_prediction, 'b')
    plt.plot(x_array, matrix_prediction, color='#38a832')

    plt.tight_layout()
    plt.show()
