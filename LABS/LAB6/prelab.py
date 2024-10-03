import numpy as np

def f(x):
    return np.cos(x)

def forward_difference(f, s, h):
    return (f(s + h) - f(s)) / h

# Centered difference approximation
def centered_difference(f, s, h):
    return (f(s + h) - f(s - h)) / (2 * h)

h_vals = 0.01*2.0**(-np.arange(0,10))

s = np.pi / 2

for h in h_vals:
    forward_approx = forward_difference(f,s,h)
    centered_approx = centered_difference(f,s,h)
    print('forward approx is:', forward_approx)
    print('centered approx is:', centered_approx)