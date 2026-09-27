# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
    conda env create -f PW<n>/Lab\ <X>/environment.yml
    conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- Unit tests in `test_decay.py` verifying exponential decay physics, initial conditions, and negative rate validation.
- Performance benchmarking script (`speed.py`) comparing pure-Python loops against vectorised NumPy implementations.

**Speed comparison (loop vs NumPy):**
- loop   : 1.9497 s
- numpy  : 0.0002 s
- speed-up: 11577.2 x faster

**Tests:** all passing? yes

**Conclusion:**
- Vectorised NumPy binomial operations (`rng.binomial`) significantly outperform pure-Python atom-by-atom loops by eliminating interpreter overhead and inner loops.
- All three unit tests passed successfully, proving that vectorisation maintains statistical physical accuracy against the analytical law $N(t) = N_0 e^{-\lambda t}$.
- Environment setup via Conda ensures seamless cross-machine execution and reproducibility.

**Reproducibility Test (Stretch Goal):**
- Tested with partner repository clone: The environment built seamlessly using `environment.yml` and all tests passed via `pytest -v` without requiring code modifications.