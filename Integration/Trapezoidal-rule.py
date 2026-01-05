import numpy as np
import matplotlib.pyplot as plt


def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        x = a + i * h
        integral += f(x)

    integral *= h
    return integral


# Function
def f(x):
    return x**2


# Exact value of the integral
evalue = 1 / 3

# Different step sizes
n_val = [10, 20, 50, 100, 200, 500, 1000]
errors = []

for n in n_val:
    num = trapezoidal_rule(0, 1, n)
    error = abs(num - evalue)
    errors.append(error)


# Plot: Error vs Number of Intervals
plt.figure()
plt.plot(n_val, errors, marker='o')
plt.xlabel("Number of Intervals (n)")
plt.ylabel("Absolute Error")
plt.title("Error Convergence of Trapezoidal Rule")
plt.grid(True)
plt.show()