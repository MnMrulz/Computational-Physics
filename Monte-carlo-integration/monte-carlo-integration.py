import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2


def monte_carlo_integral(a, b, n):
    x_random = np.random.uniform(a, b, n)
    f_values = f(x_random)
    integral = (b - a) * np.mean(f_values)
    return integral


# Exact value
exact_value = 1.0 / 3.0

# Sample sizes
n_values = [100, 500, 1000, 5000, 10000, 50000]
errors = []

for n in n_values:
    numerical = monte_carlo_integral(0, 1, n)
    error = abs(numerical - exact_value)
    errors.append(error)
    print(f"N = {n}, Integral = {numerical:.6f}, Error = {error:.6f}")


# Plot: Error vs Number of Samples
plt.figure()
plt.plot(n_values, errors, marker='o')
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Number of Random Samples (N)")
plt.ylabel("Absolute Error")
plt.title("Monte Carlo Integration Convergence")
plt.grid(True, which="both")
plt.show()
