import numpy as np
import matplotlib.pyplot as plt

# 1. Read trajectory.csv into arrays time, x, and y
data = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)
t = data[:, 0]
x = data[:, 1]
y = data[:, 2]

# 2. Compute velocity components using np.gradient
vx = np.gradient(x, t)
vy = np.gradient(y, t)

# 3. Compute speed: sqrt(vx^2 + vy^2)
speed = np.sqrt(vx**2 + vy**2)

# 4. Plot 2D path (y vs x) and speed over time
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left panel: 2D Path (x vs y)
ax1.plot(x, y, 'b.-', label="Path (x vs y)")
ax1.set_xlabel("x position (m)")
ax1.set_ylabel("y position (m)")
ax1.set_title("2D Trajectory Path")
ax1.grid(True)
ax1.legend()

# Right panel: Speed over time
ax2.plot(t, speed, 'r-', label=r"Speed $\sqrt{v_x^2 + v_y^2}$")
ax2.set_xlabel("Time t (s)")
ax2.set_ylabel("Speed (m/s)")
ax2.set_title("Speed over Time")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig("trajectory.png")
print("trajectory.png generated successfully.")