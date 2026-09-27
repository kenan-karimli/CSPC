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


---

## PW1 --- Lab B: Data, Plotting, and Automation

**What the data showed:**
The observed radioactive decay dataset (`decay_observed.csv`) demonstrates a clear exponential decrease in remaining count over time.

**Comparison with analytical law:**
The observed scatter plot closely follows the smooth analytical decay curve $N(t) = N_0 e^{-\lambda t}$, confirming that the empirical data strongly matches theoretical physical predictions.

**Snakemake pipeline:**
The Snakemake workflow automates the execution of `plot.py` to regenerate `figure.png` whenever the underlying dataset or code is updated, ensuring complete computational reproducibility.ss


---

## PW2 --- Lab A: Derivatives, Noise, and Integration

**What I built:**
- Computed velocity and acceleration from noisy position measurements using `np.gradient`.
- Recovered position and velocity back using `scipy.integrate.cumulative_trapezoid`.
- Generated `motion.png` showing position, velocity, and acceleration stacked plots.

**Acceleration results:**
- Mean acceleration: -8.58 m/s²
- Standard deviation of acceleration: 28.72 m/s²

**Why acceleration is noisy:**
Numerical differentiation magnifies measurement noise because computing the rate of change between adjacent time steps divides tiny random position fluctuations by very small time intervals ($\Delta t$), making two successive derivatives swing wildly even when the position curve appears smooth.