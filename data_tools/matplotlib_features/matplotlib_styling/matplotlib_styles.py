import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Setup Functions
x = np.arange(1, 30, 0.2)
y1 = np.log(x)
y2 = np.sin(x)
y3 = np.cos(x)
y4 = np.tan(x)

# Initialize Plot Styling
style.use('fivethirtyeight')
plt.suptitle('Mathematical Functions')

# Define Plots
ax1 = plt.subplot(221)
plt.title('Natural Log Function')
plt.xlabel('X Values (1-100)')
plt.ylabel('Natural Log of X')
ax1.plot(x, y1)

ax2 = plt.subplot(222)
plt.title('Sin Function')
plt.xlabel('X Values (1-100)')
plt.ylabel('Sin of X')
ax2.plot(x, y2)

ax3 = plt.subplot(223)
plt.title('Cos Function')
plt.xlabel('X Values (1-100)')
plt.ylabel('Cos of X')
ax3.plot(x, y3)

ax4 = plt.subplot(224)
plt.title('Tan Function')
plt.xlabel('X Values (1-100)')
plt.ylabel('Tan of X')
ax4.plot(x, y4)

# Account for Overflow and Show Plots 
plt.tight_layout()
plt.show()


