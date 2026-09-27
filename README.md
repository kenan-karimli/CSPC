# PW1 --- Lab A: Radioactive Decay Simulation

## Test Results
Running `pytest -v` confirms that all 3 unit tests pass:
- `test_starts_at_N0`: PASSED (verifies $N(0) = N_0$)
- `test_rejects_negative_rate`: PASSED (verifies `ValueError` for negative decay rates)
- `test_matches_law`: PASSED (verifies average simulation results match the analytical law $N(t) = N_0 e^{-\lambda t}$)

## Speed Comparison (`speed.py`)
Benchmark results for $N_0 = 200,000$ atoms over 200 time steps:

- **Pure-Python Loop (`simulate_loop`)**: `1.9497 s`
- **Vectorised NumPy (`simulate`)**: `0.0002 s`
- **Speed-up Factor**: NumPy version is **11577.2x** faster.

## Conclusion
The simulation accurately models physical exponential decay according to $N(t) = N_0 e^{-\lambda t}$. The pure-Python implementation requires nested loops over every individual surviving atom at each time step, scaling $O(N \times \text{steps})$. By leveraging NumPy's vectorised binomial sampling (`rng.binomial`), the inner atom loop is eliminated, achieving an impressive speed-up (>11,000x) while preserving identical physical dynamics and numerical accuracy.