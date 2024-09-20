import numpy as np
import matplotlib.pyplot as plt
import math

t = np.arange(0,np.pi,np.pi/30)
y = np.cos(t)

S = np.sum(t*y)

print("The sum is: " + str(S))


theta = np.arange(0, 2*np.pi, np.pi/30)
R = 1.2
dr = 0.1
f = 15
p = 0

x_t = R*(1 + dr * np.sin(f * theta + p)) * np.cos(theta)
y_t = R*(1 + dr * np.sin(f * theta + p)) * np.sin(theta)

plt.plot(x_t, y_t)
plt.axis('equal')
plt.show()