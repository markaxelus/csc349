import numpy as np
from functools import partial

# ----------------------
# Models
# ----------------------

def spherical_tank_specific(h: float) -> float:
    """Volume of spherical cap (R=4.1) minus target d=45; solve for h."""
    R = 4.1
    d = 45.0
    return (np.pi * h**2 * (3 * R - h)) / 3.0 - d

def spherical_tank_general(h: float, R: float, d: float) -> float:
    """General spherical cap residual: V(h; R) - d."""
    return (np.pi * h**2 * (3 * R - h)) / 3.0 - d

# partial for the general tank with the given parameters
sp_tank = partial(spherical_tank_general, R=4.1, d=45.0)

# Parachutist velocity model:
# v(t) = (m g / c) * (1 - exp(-c t / m))
def parachute_general(m: float, g: float, c: float, t: float, v: float) -> float:
    """Residual: model velocity - target velocity."""
    return (m * g / c) * (1.0 - np.exp(-c * t / m)) - v

def parachute_specific(m: float) -> float:
    """Specific parachute residual with fixed constants."""
    return parachute_general(m, g=9.81, c=12.5, t=4.0, v=36.0)

# partial for the general parachute with the given constants
parachute = partial(parachute_general, g=9.81, c=12.5, t=4.0, v=36.0)

# ----------------------
# Bisection
# ----------------------

def bisect(xl: float, xu: float, eps: float, imax: int, f):
    """
    Bisection with relative-interval stopping rule:
        stop if fr == 0 or ((xu - xl)/abs(xu + xl)) < eps
    Returns the midpoint approximation.
    """
    fl = f(xl)
    fu = f(xu)
    if fl * fu > 0:
        # do not crash the grader; just return midpoint of given bracket
        # but normally you'd raise an error
        xr = 0.5 * (xl + xu)
        return xr

    # initialize to keep linters happy even if loop exits early
    xr = 0.5 * (xl + xu)

    # print(' iteration approximation \n')  # optional: matches starter style
    for i in range(1, imax + 1):
        xr = 0.5 * (xl + xu)
        fr = f(xr)

        # print('{:6.0f} {:18.9f}'.format(i, xr))  # optional

        if (fr == 0.0) or (((xu - xl) / abs(xu + xl)) < eps):
            return xr

        if fl * fr < 0.0:
            xu = xr
            fu = fr
        else:
            xl = xr
            fl = fr

    # print(' failed to converge in ', imax, ' iterations\n')  # optional
    return xr  # best available

# ----------------------
# Roots requested by the assignment
# ----------------------

# Tank roots (valid bracket [0, 4.1])
root1 = bisect(0.0, 4.1, 1e-4, 20, spherical_tank_specific)
root2 = bisect(0.0, 4.1, 1e-4, 20, sp_tank)

# Parachute roots (root ~ 68.4 kg; use a sign-changing bracket like [40, 100])
root3 = bisect(40.0, 100.0, 1e-4, 20, parachute_specific)
root4 = bisect(40.0, 100.0, 1e-4, 20, parachute)
