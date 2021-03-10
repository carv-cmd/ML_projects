import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 172, 8
x = mu + sigma * np.random.randn(10000)

plt.hist(x, 100, facecolor='blue', density=True)


plt.title('Distribution of Students Heights')
plt.xlabel('Heights')
plt.ylabel('Percentage of Students')
plt.text(140, 0.045, 'mu=172 & sigma=8')
plt.grid(True)
plt.show()
