import numpy as np
import matplotlib.pyplot as plt


def simp(a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's Rule")

    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)

    integral *= h / 3
    return integral


# Function
def f(x):
    return np.sin(x)


# Exact value of the integral
exact_value = 2.0

# Different step sizes
n_val = [10, 20, 40, 80, 160, 320]
errors = []

for n in n_val:
    num = simp(0, np.pi, n)
    error = abs(num - exact_value)
    errors.append(error)

# Plot: Error vs Number of Intervals
plt.figure()
plt.plot(n_val, errors, marker='o')
plt.xlabel("Number of Intervals (n)")
plt.ylabel("Absolute Error")
plt.title("Error Convergence of Simpson's Rule")
plt.grid(True)
plt.show()
