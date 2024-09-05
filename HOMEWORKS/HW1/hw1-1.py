import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(1.920, 2.080, .001)
y = (x-2)**9
plt.plot(x,y)
plt.show()