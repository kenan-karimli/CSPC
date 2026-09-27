"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)[cite: 17]
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)[cite: 17]
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?[cite: 17]
v = np.gradient(y, t)
a = np.gradient(v, t)
mean_a = np.mean(a)
print(f"Mean acceleration: {mean_a:.2f} m/s^2")
print(f"Standard deviation of acceleration: {a.std():.2f} m/s^2")


# TODO 3: integrate a back up to recover velocity and position[cite: 17]
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)[cite: 17]
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration[cite: 17]
#         vs time. Mark the true -9.81 line on the acceleration panel.[cite: 17]
#         Save it as motion.png[cite: 17]
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Position panel
ax1.plot(t, y, 'b.', label="Measured position")
ax1.plot(t, y_rec, 'r--', label="Recovered position")
ax1.set_ylabel("Position y (m)")
ax1.set_title("Free-fall Motion Analysis")
ax1.legend()
ax1.grid(True)

# Velocity panel
ax2.plot(t, v, 'b-', label="Velocity (derived)")
ax2.plot(t, v_rec, 'r--', label="Recovered velocity")
ax2.set_ylabel("Velocity v (m/s)")
ax2.legend()
ax2.grid(True)

# Acceleration panel
ax3.plot(t, a, 'b-', label="Acceleration (derived)")
ax3.axhline(-9.81, color='g', linestyle='--', label="True -9.81 m/s²")
ax3.set_xlabel("Time t (s)")
ax3.set_ylabel("Acceleration a (m/s²)")
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.savefig("motion.png")
print("motion.png generated successfully.")

