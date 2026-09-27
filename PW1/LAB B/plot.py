"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     # decay constant, given

# TODO 1: Read decay_observed.csv into arrays t and observed (skip the header row)
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# TODO 2: Set N0 to the first observed value and build analytical = N0 * exp(-LAMBDA * t)
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: Make a 1x2 subplot with SHARED x and y axes[cite: 19]
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

# Left panel: scatter of the observed data[cite: 19]
ax1.scatter(t, observed, color="blue", label="Observed", s=15)
ax1.set_title("Observed data")
ax1.set_xlabel("Time (t)")
ax1.set_ylabel("Count N(t)")
ax1.grid(True)

# Right panel: line plot of the analytical curve[cite: 19]
ax2.plot(t, analytical, color="red", label="Analytical")
ax2.set_title("Analytical")
ax2.set_xlabel("Time (t)")
ax2.grid(True)

plt.tight_layout()

# TODO 4: Save the figure as figure.png[cite: 19]
plt.savefig("figure.png")
print("figure.png generated successfully.")
