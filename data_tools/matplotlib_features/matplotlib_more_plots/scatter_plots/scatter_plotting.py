import numpy as np
import matplotlib.pyplot as plt
import random


# x = np.random.rand(50)
# y = np.random.rand(50)
# plt.title('Absolutely Pointless Data')
# plt.ylabel('MORE NUMBERS')
# plt.xlabel('Numbers')
# plt.scatter(x, y)

a = [random.randint(15, 225) for weight in range(50)]
b = [random.randint(48, 72) for height in range(50)]
plt.title('Fat MF Tracker')
plt.xlabel('Weight(pounds)')
plt.ylabel('Height(inches)')
plt.scatter(a, b, c='red', marker='x')

plt.tight_layout()
plt.show()

