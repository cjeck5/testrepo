import numpy as np

def EvalLine(x0,x1,fx0,fx1, alpha):
    if x1 == x0:
        print('Error: x0 and x1 must be different values')
        return
    
    f_alpha = fx0 + ((fx1-fx0)/(x1-x0))*(alpha-x0)
    return f_alpha