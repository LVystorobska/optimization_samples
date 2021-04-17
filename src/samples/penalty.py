import numpy as np
from scipy import optimize 
import math


def check_stop_condition_func(penalty_func, point, general_function, cut_function, penalty_param, precision):
    return penalty_func(point, general_function, cut_function, penalty_param) <= precision

def penalty_function(point, general_function, cut_function, penalty_param):
    cut_func_value = 0
    if cut_function is not None and cut_function(point) > 0:
        cut_func_value = cut_function(point)**2
    return (penalty_param/2.)*(((general_function(point)**2) if general_function is not None else 0)+cut_func_value)

def gen_func(point):
    return 0.

def cut_func(point):
    return 0. if (point - 1.) <= 0 else 1000000000.

def init_function(point):
    return point**2. - 4.*point

def derived_penalty_x_search_by_param(penalty_param):
    return (4. + penalty_param)/(2. + penalty_param)

def penalty_optimize(point, init_func, penalty_param, general_function, cut_function, penalty_func, step_delta, precision):

    def penalty(point):
        return init_func(point) + penalty_func(point, general_function, cut_function, penalty_param)
    point_next = optimize.fminbound(penalty, -10., 10)
    if check_stop_condition_func(penalty_func, point_next, general_function, cut_function, penalty_param, precision):
        print('Result finction value: ', penalty(point_next))
        return point_next
    else:
        return penalty_optimize(derived_penalty_x_search_by_param(penalty_param), init_func, (penalty_param*step_delta), general_function, cut_function, penalty_func, step_delta, precision)


result = penalty_optimize(10.,init_function, 1., gen_func, cut_func, penalty_function, 5., 0.01)
print('Result:', result)
