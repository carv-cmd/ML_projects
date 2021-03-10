import numpy as np
import matplotlib.pyplot as plt
import math


interest_rate = np.arange(.2, 100.2, .2)
numerator = math.log(2)
denom = np.log(1 + interest_rate/100)
time_to_double = numerator / denom

print(interest_rate)
print(time_to_double)

plt.plot(interest_rate, time_to_double, 'y-')
plt.show()
