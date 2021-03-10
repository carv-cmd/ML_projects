import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 100, 2)
y1 = np.sin(x)
y2 = x**2 + 2*x
y3 = np.log(x)
y4 = np.log2(x**3) * 5

plt.figure(1)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
ax1.plot(x, y1, 'g')
ax2.plot(x, y2, 'y')

plt.figure(2)
plt.plot(x, y3, 'r.')

plt.figure(3)
plt.plot(x, y4, 'r.')

plt.tight_layout()
plt.show()
