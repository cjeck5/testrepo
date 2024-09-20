import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-10,10,1000)
y = x - 4 * np.sin(2*x)-3

plt.plot(x,y)
plt.axhline(0, color = 'black', linewidth = 0.5)
plt.axvline(0, color = 'black', linewidth = 0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()