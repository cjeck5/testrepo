import numpy as np

def driver():
    # test functions
    f1 = lambda x: (10/(x+4))**(1/2)
    # fixed point is alpha1 = 1.4987....
    #f2 = lambda x: 3+2*np.sin(x)
    #fixed point is alpha2 = 3.09...
    Nmax = 100
    tol = 1e-10
    # test f1 '''
    x0 = 1.50
    [xstar,ier, approx_vec, count] = fixedpt(f1,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f1(xstar):',f1(xstar))
    print('Error message reads:',ier)
    print('Approximations vector for f1:\n', approx_vec)
    print('Number of iterations is: ', count)

    approx_vec = approx_vec[:-1]
    compute_order(approx_vec, xstar)

    #test f2 '''
    #x0 = 1.50
    #[xstar,ier, approx_vec, count] = fixedpt(f2,x0,tol,Nmax)
    #print('the approximate fixed point is:',xstar)
    #print('f2(xstar):',f2(xstar))
    #print('Error message reads:',ier)
    #print('Approximations vector for f2:', approx_vec)
    #print('Number of iterations is: ', count)
    # define routines


def aitkens(x):
    xn = x[:-2]
    xn1 = x[1:-1]
    xn2 = x[2:]
    return xn - (xn1-xn)**2/(xn2-2*xn1+xn)

def compute_order(x, xstar):

    diff1 = np.abs(x[1::] - xstar)
    diff2 = np.abs(x[0:-1] - xstar)

    fit = np.polyfit(np.log(diff2.flatten()), np.log(diff1.flatten()), 1)
    _lambda = np.exp(fit[1])
    alpha = fit[0]
    print(f"lambda is {_lambda}")
    print(f"alpha is {alpha}")
    return fit

def fixedpt(f,x0,tol,Nmax):
    ''' x0 = initial guess'''
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    count = 0
    approx_vec = np.zeros((Nmax, 1))

    while (count <Nmax):
        count = count +1
        x1 = f(x0)
        
        approx_vec[count - 1] = x1

        if (abs(x1-x0) <tol):
            xstar = x1
            ier = 0
            approx_vec = approx_vec[:count]
            return [xstar,ier, approx_vec, count]
        x0 = x1

    xstar = x1
    ier = 1
    approx_vec = approx_vec[:count]
    return [xstar, ier, approx_vec, count]
driver()
