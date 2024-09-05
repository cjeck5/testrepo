import numpy as np
import numpy.linalg as la
import math
def driver():
    n = 2
    x = np.linspace(0,np.pi,n)
# this is a function handle. You can use it to define
# functions instead of using a subroutine like you
# have to in a true low level language.
    y = np.array([1,0])
    w = np.array([0,1])
# evaluate the dot product of y and w
    dp = dotProduct(y,w,n)
# print the output
    print('the dot product is : ', dp)
    return

def dotProduct(x,y,n):
# Computes the dot product of the n x 1 vectors x and y
    dp = 0.
    for j in range(n):
        dp = dp + x[j]*y[j]
    return dp

driver()