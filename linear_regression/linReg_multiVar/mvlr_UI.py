# User Input for Multivariate Linear Regression Model
import matplotlib.pyplot as plt
from matplotlib import style
# from multi_lin_reg import *


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
def prediction():
    size = int(input('Enter Size (sq/ft): '))
    rooms = int(input('Enter Number of Rooms: '))
    floors = int(input('Enter Number of Floors: '))
    year = int(input('Enter Year Built: '))
    price = op[0] + (size * op[1]) + (rooms * op[2]) + (floors * op[3]) - (year * op[4])
    print(f'\nPredicted Sale Price: ${price}')


####################################################
####################################################
if __name__ == "__main__":
    # L = float(input("Value for LearningRate: "))
    # Epoch = int(input("Value for Epoch: "))
    L = .00003
    Epoch = 20000
    op = gradient_descent(L, Epoch)
    print_thetas()
    # prediction()

####################################################
####################################################
style.use('ggplot')
plt.suptitle('Multivariate Linear Regression', fontsize=14)
plt.title('Cost Function', fontsize=12)
plt.ylabel('Total Error')
plt.xlabel('Iterations')

plt.plot(iteration, total_error, 'b-')

plt.tight_layout()
plt.show()
