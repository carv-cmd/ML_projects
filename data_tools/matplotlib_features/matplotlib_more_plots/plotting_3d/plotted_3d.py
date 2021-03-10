import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


ax = plt.axes(projection="3d")


def z_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2))


x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

x, y = np.meshgrid(x, y)
Z = z_function(x, y)

ax.plot_surface(x, y, Z)

plt.tight_layout()
plt.show()
