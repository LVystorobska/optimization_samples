import matplotlib.pyplot as plt
from scipy import optimize
import math

def f(xvals):
    return xvals**2-xvals**3

def dichotomy_method(start_point, end_point, delta, precision):
    full_len = start_point + end_point
    middle_point = full_len/2
    len_diff = end_point - start_point
    print('Middle point:', middle_point)
    if len_diff < 2*precision:
        return middle_point
    else:
        mid_relative_left = middle_point - (delta/2)
        print('Left point:', mid_relative_left)
        mid_relative_right = middle_point + (delta/2)
        print('Right point:', mid_relative_right)
        if f(mid_relative_left)<f(mid_relative_right):
            return dichotomy_method(start_point, mid_relative_right, delta, precision)
        else:
            return dichotomy_method(mid_relative_left, end_point, delta, precision)

result = dichotomy_method(1.0, 4.0, 0.05, 0.2)
print('Result:', result)

