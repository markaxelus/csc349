import matplotlib.pyplot as plt
import numpy as np


def f(x): 
    # YOUR CODE HERE
    return ...

def fp(x): 
    # YOUR CODE HERE
    return ...

def Newton(x0, eps, imax, foo, fp):
    # YOUR CODE HERE
    return root, steps

x0 = ... # take it from the task
eps = ... # take it from the task
imax = ...  # take it from the task
root, steps = Newton(x0, eps, imax, f, fp)

fxa = f(root)
fpxa = fp(root)

real_root = ... # take it from the task
rel_err = ... # YOUR CODE HERE

x_min = ... # YOUR CODE HERE
x_max = ... # YOUR CODE HERE
tail = ... # YOUR CODE HERE

x = np.linspace(x_min - tail, x_max + tail, 1000)

plt.plot(...) # YOUR CODE HERE
plt.scatter(...) # YOUR CODE HERE

plot = plt.gca()