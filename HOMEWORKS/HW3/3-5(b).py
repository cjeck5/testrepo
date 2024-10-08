import numpy as np

def driver():
    # test functions
    f1 = lambda x: -1*np.sin(2*x) + (5*x)/4 - 3/4
    # fixed point is alpha1 = 1.4987....
    #f2 = lambda x: 3+2*np.sin(x)
    #fixed point is alpha2 = 3.09...
    Nmax = 100
    tol = 1e-10
    # test f1 '''
    x0 = 5
    [xstar,ier, count] = fixedpt(f1,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f1(xstar):',f1(xstar))
    print('Error message reads:',ier)
    print('Number of iterations is: ', count)


def fixedpt(f,x0,tol,Nmax):
    ''' x0 = initial guess'''
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    count = 0

    while (count <Nmax):
        count = count +1
        x1 = f(x0)

        if (abs(x1-x0) <tol):
            xstar = x1
            ier = 0
            return [xstar,ier, count]
        x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier, count]
driver()