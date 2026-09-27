"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    # Verify that calling simulate with a negative decay rate raises a ValueError
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


def test_matches_law():
    N0 = 10000
    lam = 0.4
    dt = 0.05
    steps = 200
    
    # Run multiple simulations with different seeds
    runs = [simulate(N0, lam, dt=dt, steps=steps, seed=s) for s in range(200)]
    
    # Calculate the average atom count across all runs at the final time step
    avg_final_N = np.mean([run[-1] for run in runs])
    
    # Analytical decay law: N(t) = N0 * exp(-lam * t)
    t_final = dt * steps
    expected = N0 * np.exp(-lam * t_final)
    
    # Compare average simulation result with analytical value using pytest.approx
    assert avg_final_N == pytest.approx(expected, rel=0.05)