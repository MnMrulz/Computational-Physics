# I have solved the !D harmonic Oscillator with the help of rk4 method here

import numpy as np
import matplotlib.pyplot as plt


def derivatives(x, v, omega):
    dxdt = v
    dvdt = -omega**2 * x
    return dxdt, dvdt


# Parameters
omega = 1.0
dt = 0.01
t_max = 20

# Initial conditions
x = 1.0
v = 0.0

# Time array
t_values = np.arange(0, t_max, dt)

# Storage arrays
x_values = []
v_values = []

# RK4 integration
for t in t_values:
    x_values.append(x)
    v_values.append(v)

    k1_x, k1_v = derivatives(x, v, omega)

    k2_x, k2_v = derivatives(
        x + 0.5 * dt * k1_x,
        v + 0.5 * dt * k1_v,
        omega
    )

    k3_x, k3_v = derivatives(
        x + 0.5 * dt * k2_x,
        v + 0.5 * dt * k2_v,
        omega
    )

    k4_x, k4_v = derivatives(
        x + dt * k3_x,
        v + dt * k3_v,
        omega
    )

    x += (dt / 6) * (k1_x + 2*k2_x + 2*k3_x + k4_x)
    v += (dt / 6) * (k1_v + 2*k2_v + 2*k3_v + k4_v)


# ---- Plot 1: x(t) ----
plt.figure()
plt.plot(t_values, x_values)
plt.xlabel("Time")
plt.ylabel("Position x(t)")
plt.title("Harmonic Oscillator")
plt.grid(True)
plt.show()

# ---- Plot 2: Phase Space ----
plt.figure()
plt.plot(x_values, v_values)
plt.xlabel("Position x")
plt.ylabel("Velocity v")
plt.title("Phase Space")
plt.grid(True)
plt.show()
