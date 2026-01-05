# I ae used the equation f(x)=cos(x)−x here and solved using Bisection method, Secant method, and Newton-Rahpson method

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.cos(x) - x


def df(x):
    return -np.sin(x) - 1


def bisection(a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        raise ValueError("Bisection method requires opposite signs")

    while abs(b - a) > tol:
        c = 0.5 * (a + b)
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return 0.5 * (a + b)


def newton_raphson(x0, tol=1e-6):
    x = x0
    while abs(f(x)) > tol:
        x = x - f(x) / df(x)
    return x


def secant(x0, x1, tol=1e-6):
    while abs(x1 - x0) > tol:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
    return x1


# Initial guesses
root_bisection = bisection(0, 1)
root_newton = newton_raphson(0.5)
root_secant = secant(0, 1)

print("Root (Bisection) =", root_bisection)
print("Root (Newton-Raphson) =", root_newton)
print("Root (Secant) =", root_secant)
