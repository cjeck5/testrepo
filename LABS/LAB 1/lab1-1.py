import numpy as np
import matplotlib.pyplot as plt

#EXCERCISE 3.2

x = np.linspace(0,5,6) #lines 5 and 6 are used to practice initialzing domains using linspace and arange.
y = np.arange(0,5,6)
print('the first three entires of x are',x[0:3])

w = 10**(-np.linspace(1,10,10)) #w defines the values of 10^-x where x are the values 1 to 10, with 10 steps.


x2 = np.linspace(1,10,10)
s = 3*w 
plt.plot(x2,w) #plots the values of w over the domain (x2)
plt.plot(x2,s)

plt.xlabel('x')
plt.ylabel('w')
plt.show()