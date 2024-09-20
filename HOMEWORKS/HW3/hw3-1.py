# import libraries
import numpy as np
def driver():
    f = lambda x: (x**3 + x - 4)
    a = 1
    b = 4
    tol = 1e-3
    [astar,ier,count] = bisection(f,a,b,tol)
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))
    print('count = ', count)

def bisection(f,a,b,tol):
    fa = f(a)
    fb = f(b)
    count = 1


    if (fa*fb>0):
        ier = 1
        astar = a
        return [astar, ier, count]
    if (fa == 0):
        astar = a
        ier =0
        return [astar, ier, count]
    if (fb ==0):
        astar = b
        ier = 0
        return [astar, ier, count]
    count = 0
    d = 0.5*(a+b)

    while (abs(d-a)> tol):
        fd = f(d)
        if (fd ==0):
            astar = d
            ier = 0
            return [astar, ier, count]
        if (fa*fd<0):
            b = d
        else:
            a = d
            fa = fd
        d = 0.5*(a+b)
        count = count + 1
    astar = d
    ier = 0
    return [astar, ier, count]
driver()