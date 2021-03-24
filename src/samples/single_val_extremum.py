import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import math


def f(xvals):
    #return math.pow(xvals, 4) + math.exp(xvals)
    return 4*math.pow(xvals, 3) - math.exp(-xvals)
f2 = np.vectorize(f)
x = np.arange(-1, 2, 0.01)
plt.plot(x, f2(x))
plt.show()


# Global optimization
# grid = (-1, 2, 0.01)
# xmin_global = optimize.brute(f, (grid, ))
# print("Global minima found %s" % xmin_global)

# Constrain optimization
xmin_local = optimize.fminbound(f, -1, 2)
print("Local minimum found %s" % xmin_local)