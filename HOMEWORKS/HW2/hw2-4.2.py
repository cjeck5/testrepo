import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0, 2*np.pi, np.pi/30)

for i in range(1,10):
    R = i
    dr = 0.05
    f = 2 + i
    p = np.random.uniform(0,2)

    x_t = R*(1 + dr * np.sin(f * theta + p)) * np.cos(theta)
    y_t = R*(1 + dr * np.sin(f * theta + p)) * np.sin(theta)
    plt.plot(x_t,y_t)

plt.show()