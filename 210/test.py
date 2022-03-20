import numpy as np
import scipy

t_data = np.array([0.5, 1.0, 1.5, 2.0])
y_data = np.array([6.8, 3., 1.5, 0.75])

def func_nl_lsq(x, t=t_data, y=y_data):
    return x[0]*np.exp(x[1]*t) -  y
    # removed one level of []'s

scipy.optimize.least_squares(func_nl_lsq, [0, 0])
