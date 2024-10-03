import numpy as np
import math
import time
from numpy.linalg import inv
from numpy.linalg import norm

def driver():
    x0 = np.array([1,0])
    Nmax = 100
    tol = 1e-10
    t = time.time()
    for j in range(20):
        [xstar,ier,its] = SlackerNewton(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Slacker Newton: the error message reads:',ier)
    print('Slacker Newton: took this many seconds:',elapsed/20)
    print('Slacker: number of iterations is:',its)

    t = time.time()
    for j in range(20):
        [xstar,ier,its] = LazyNewton(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Lazy Newton: the error message reads:',ier)
    print('Lazy Newton: took this many seconds:',elapsed/20)
    print('Lazy Newton: number of iterations is:',its)

def evalF(x):
    F = np.zeros(2)
    F[0] = 4*x[0]**2 + x[1]**2 - 4
    F[1] = x[0] + x[1] - np.sin(x[0] - x[1])
    return F

def evalJ(x):
    J = np.zeros((2,2))
    J[0,0] = 8 *x[0]
    J[0,1] = 2 * x[1]
    J[1,0] = 1 - np.cos(x[0] - x[1])
    J[1,1] = 1 + np.cos(x[0]-x[1])
    return J

def SlackerNewton(x0,tol,Nmax, delta = 1e-4):
    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''
    J = evalJ(x0)
    Jinv = inv(J)
    #delta is our criteria for the iteration diff being too large

    for its in range(Nmax):
        F = evalF(x0)
        x1 = x0 - Jinv.dot(F)

        if(norm(x1-x0) > delta):
            J = evalJ(x1)
            Jinv = inv(J)

        if (norm(x1-x0) < tol):
            xstar = x1
            ier = 0
            return[xstar, ier,its]
        x0 = x1
        
    xstar = x1
    ier = 1
    return[xstar,ier,its]

def LazyNewton(x0,tol,Nmax):
    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''
    J = evalJ(x0)
    Jinv = inv(J)
    for its in range(Nmax):
        F = evalF(x0)
        x1 = x0 - Jinv.dot(F)
        if (norm(x1-x0) < tol):
            xstar = x1
            ier =0
            return[xstar, ier,its]
        x0 = x1

    xstar = x1
    ier = 1
    return[xstar,ier,its]

driver()