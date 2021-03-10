import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x = np.arange(1, 36, 0.2)
y1 = np.sin(x)
y2 = np.cos(x)

style.use('fivethirtyeight')
plt.suptitle('Frequency(Hz)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.plot(x, y1, label="Sine")
plt.plot(x, y2, label="Cosine")

plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

