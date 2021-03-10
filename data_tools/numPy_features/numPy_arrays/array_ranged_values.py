import numpy as np
import math

# Standard numpy array created manually
x = np.array([2, 3, 5, 7, 11, 13, 17])
y = ((x/2) + (x/2))**2
print(y)

# 1-1000 in steps of 10
a = np.arange(1, 100, 10)
b = np.log10(a)
print(b)

# 1-1000 w/ 47 values evenly distributed within it
o = np.linspace(1, 1000, 47)
p = np.sqrt(o)
print(p)

