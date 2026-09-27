"""
Speed comparison between pure-Python loop and vectorised NumPy simulation.
"""

import time
from decay import simulate, simulate_loop

N0 = 200_000
lam = 0.4

# Time pure-Python loop version
t0 = time.perf_counter()
simulate_loop(N0, lam)
t1 = time.perf_counter()
t_loop = t1 - t0

# Time vectorised NumPy version
t0 = time.perf_counter()
simulate(N0, lam)
t1 = time.perf_counter()
t_numpy = t1 - t0

# Calculate speed-up factor
speedup = t_loop / t_numpy

# Output results
print(f"simulate_loop time : {t_loop:.4f} s")
print(f"simulate (NumPy) time: {t_numpy:.4f} s")
print(f"NumPy version is {speedup:.1f}x faster.")