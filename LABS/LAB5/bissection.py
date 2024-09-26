# import libraries
import numpy as np

def driver():
# use routines
    f = lambda x: np.exp(x**2 + 7*x - 30)
    f_prime = lambda x: (2*x + 7)*np.exp(x**2 + 7*x - 30)
    f_double_prime = lambda x: (4*x**2 + 28*x + 51)*np.exp(x**2 + 7*x - 30)
    a = 2
    b = 4.5
    # f = lambda x: np.sin(x)
    # a = 0.1
    # b = np.pi+0.1
    tol = 1e-7
    [astar,ier] = bisection(f,f_prime,f_double_prime,a,b,tol)
    print('For bissection')
    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))
    # define routines
    
    p0 = 4.5
    Nmax = 100
    [p,pstar,info,it] = newton(f,f_prime,p0,tol,Nmax)
    print('For newton:')
    print('the approximate root is', '%16.16e' % pstar)
    print('the error message reads:', '%d' % info)
    print('Number of iterations:', '%d' % it)

    [astar, ier] = hybrid(f, f_prime, f_double_prime,a,b,tol,p0,Nmax)
    print('The approximate root is:', astar)
    print('The error message reads:', ier)


def bisection(f,f_prime, f_double_prime ,a,b,tol):
    # Inputs:
    # f,a,b - function and endpoints of initial interval
    # tol - bisection stops when interval length < tol
    # Returns:
    # astar - approximation of root
    # ier - error message
    # - ier = 1 => Failed
    # - ier = 0 == success
    # first verify there is a root we can find in the interval
    fa = f(a)
    fb = f(b)
    if (fa*fb>0):
        ier = 1
        astar = a
        return [astar, ier]
# verify end points are not a root
    if (fa == 0):
        astar = a
        ier =0
        return [astar, ier]
    if (fb ==0):
        astar = b
        ier = 0
        return [astar, ier]
    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
        fd = f(d)
        f_primex = f_prime(d)
        f_double_primex = f_double_prime(d)
        converge_test = abs((fd*f_double_primex)/(f_primex)**2)

        if(converge_test < 1):
            astar = d
            ier = 0
        if (fd ==0):
            astar = d
            ier = 0
            return [astar, ier]
        
        d = 0.5*(a+b)
        count = count +1
# print('abs(d-a) = ', abs(d-a))
    astar = d
    ier = 0
    return [astar, ier]


def newton(f,fp,p0,tol,Nmax):
    """
    Newton iteration.
    Inputs:
    f,fp - function and derivative
    p0 - initial guess for root
    tol - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
    Returns:
    p - an array of the iterates
    pstar - the last iterate
    info - success message
    - 0 if we met tol
    - 1 if we hit Nmax iterations (fail)
    """
    p = np.zeros(Nmax+1)
    p[0] = p0
    for it in range(Nmax):
        p1 = p0-f(p0)/fp(p0)
        p[it+1] = p1
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [p,pstar,info,it]
        p0 = p1
    pstar = p1
    info = 1
    return [p,pstar,info,it]

def hybrid(f,f_prime, f_double_prime,a,b,tol,p0,Nmax):
    fa = f(a)
    fb = f(b)
    if (fa*fb>0):
        ier = 1
        astar = a
        return [astar, ier]
# verify end points are not a root
    if (fa == 0):
        astar = a
        ier =0
        return [astar, ier]
    if (fb ==0):
        astar = b
        ier = 0
        return [astar, ier]
    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
        fd = f(d)
        f_primex = f_prime(d)
        f_double_primex = f_double_prime(d)
        converge_test = abs((fd*f_double_primex)/(f_primex)**2)

        if(converge_test < 1):
            p0 = d
            [p,pstar,info,it] = newton(f,f_prime,f_double_prime,tol,p0,Nmax)
            astar = pstar
            ier = 0
            return [astar, ier]
        
        if (fd ==0):
            astar = d
            ier = 0
            return [astar, ier]
        
        d = 0.5*(a+b)
        count = count +1
# print('abs(d-a) = ', abs(d-a))
    astar = d
    ier = 0
    return [astar, ier]

driver()