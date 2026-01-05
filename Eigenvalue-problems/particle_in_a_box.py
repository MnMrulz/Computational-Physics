import numpy as np
import matplotlib.pyplot as plt


# Physical parameters
L = 1.0
N = 100
dx = L / (N + 1)

x = np.linspace(dx, L - dx, N)

# Kinetic energy matrix (finite difference)
H = np.zeros((N, N))

for i in range(N):
    H[i, i] = 2.0
    if i > 0:
        H[i, i - 1] = -1.0
    if i < N - 1:
        H[i, i + 1] = -1.0

H = H / (dx**2)

eigenvalues, eigenvectors = np.linalg.eigh(H)

# First 5 energy levels
print("First five numerical energy eigenvalues:")
for i in range(5):
    print(f"n = {i+1}, E = {eigenvalues[i]:.4f}")


# Analytical energies for comparison
print("\nAnalytical energy eigenvalues:")
for n in range(1, 6):
    E_exact = (n**2) * (np.pi**2)
    print(f"n = {n}, E = {E_exact:.4f}")


# Plot first three eigenfunctions
plt.figure()

for n in range(3):
    psi = eigenvectors[:, n]
    psi = psi / np.sqrt(np.sum(psi**2) * dx)
    plt.plot(x, psi, label=f"n = {n+1}")

plt.xlabel("x")
plt.ylabel("Psi(x)")
plt.title("Eigenfunctions")
plt.legend()
plt.grid(True)
plt.show()
