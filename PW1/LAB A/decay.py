"""
Radioactive decay simulation.

A sample starts with N0 atoms. Each atom decays at random: in a short
time step dt it decays with probability lam*dt, independently of the others.
No one can predict which atom decays when, yet the average over the whole
sample follows the exact law  N(t) = N0 * exp(-lam * t).

Two versions are provided so you can compare their speed:
  - simulate_loop : a pure-Python loop over every atom (slow)
  - simulate      : a vectorised NumPy version (fast)
Both return an array of the atom count at each time step.
"""

import numpy as np


def simulate_loop(N0, lam, dt=0.05, steps=200, seed=0):
    """Radioactive decay, pure-Python loop version (slow)."""
    if lam < 0:
        raise ValueError("lam must be >= 0")
    rng = np.random.default_rng(seed)
    N = N0
    counts = [N0]
    for _ in range(steps):
        decayed = 0
        for _ in range(N):                  # loop over every surviving atom
            if rng.random() < lam * dt:
                decayed += 1
        N -= decayed
        counts.append(N)
    return np.array(counts)


def simulate(N0, lam, dt=0.05, steps=200, seed=0):
    """Radioactive decay, vectorised NumPy version (fast)."""
    if lam < 0:
        raise ValueError("lam must be >= 0")
    rng = np.random.default_rng(seed)
    N = N0
    counts = [N0]
    for _ in range(steps):
        decayed = rng.binomial(N, lam * dt)  # decide all atoms at once
        N -= decayed
        counts.append(N)
    return np.array(counts)
