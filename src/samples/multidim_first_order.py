import numpy as np
from scipy import optimize 
import math

def check_stop_condition_func(current_xvector, past_xvector, fdef, precision):
    return (fdef(past_xvector) - fdef(current_xvector)) < (precision*(1 - math.fabs(fdef(current_xvector))))

def check_stop_condition_variable(x_current, x_past, precision):
    return (np.linalg.norm((x_past-x_current))) < (math.sqrt(precision)*(1 - np.linalg.norm((x_current))))

def check_stop_condition_ratio(current_xvector, fdef, fdef_deriv, precision):
    return (np.linalg.norm(fdef_deriv(current_xvector))) <= (math.pow(precision,1./3.)*(1 - math.fabs(fdef(current_xvector))))


def init_func(xarr):
    return xarr.item(0)**2+25*xarr.item(1)**2

def init_func_deriv_numpy(xarr):
    return [xarr.item(0)*2, 50*xarr.item(1)]


def get_step(f):
    return optimize.fminbound(f, 0.0, 1.0)

def optim_first_order(func, func_deriv, init_xarr, precision):

    def step_func(beta):
        return (init_xarr[0] - beta*func_deriv(init_xarr)[0])**2 + 25*(init_xarr[1] - beta*func_deriv(init_xarr)[1])**2
    
    step = get_step(step_func)
    x_derived=np.array([step*func_deriv(init_xarr)[0], step*func_deriv(init_xarr)[1]])
    next_xarr = init_xarr - x_derived

    if check_stop_condition_func(next_xarr, init_xarr, func, precision) and check_stop_condition_variable(next_xarr, init_xarr, precision) and check_stop_condition_ratio(next_xarr, func, func_deriv, precision):
        print('BY CONDITION 1')
        return next_xarr
    elif (next_xarr == init_xarr).all():
        print('BY CONDITION 2')
        return next_xarr
    else:
        return optim_first_order(func, func_deriv, next_xarr, precision)


x_current=np.array([1.0, 1.0])

result = optim_first_order(init_func, init_func_deriv_numpy, x_current, 0.01)
print('Result:', result)