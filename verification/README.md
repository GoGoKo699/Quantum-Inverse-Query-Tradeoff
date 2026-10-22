# Reproducing the finite scientific checks

The scientific results have analytical proofs. The scripts here independently
evaluate selected finite identities that are easy to get wrong in those
proofs: normalization of the Dicke count likelihood, spin-moment factors,
complex-conjugation conventions, and the Poisson purification.

## Environment and commands

The recorded run used **Python 3.12.14**, **NumPy 2.3.5**, and **SciPy 1.17.0**.
The two numerical packages are pinned in [requirements.txt](../requirements.txt).
Both scripts use the fixed seed 20261022 and print JSON to standard output.
They do not download data or write files.

From the repository root:

```sh
python3 -m pip install -r requirements.txt
python3 verification/run_all.py
```

A successful run exits with status zero and prints a JSON object whose
top-level status is "passed". [expected_output.json](expected_output.json)
contains the complete output of the recorded run. Case counts and the asserted
tolerances are the stable checks; the last few floating-point digits may differ
with the numerical backend.

The checks can also be run separately:

```sh
python3 verification/check_dicke_probe.py
python3 verification/check_poisson_features.py
```

The Poisson script uses only Python's standard library. The Dicke script uses
NumPy tensor operations and SciPy matrix exponentiation. Run normally, without
Python's assertion-disabling optimization option.

## Dicke probe: full likelihood and count moments

[check_dicke_probe.py](check_dicke_probe.py) compares several distinct
representations of the experiment in [Dicke probes](../science/dicke-probe.md).

| Check | Instances | Recorded result |
|---|---:|---|
| Explicit unknown-mode Dicke vector, full tensor action of a sampled unitary, and every target-count probability | 80, with dimensions 3 and 4 and 2–5 forward calls | Maximum probability error $2.56\times10^{-15}$; output norm error $6.00\times10^{-15}$ |
| Probability endpoints $p=0,1$, all occupations for 1–15 forward calls | 270 | Zero count-distribution and return-probability error |
| Exact second and fourth moments from direct spin rotations | 1,092 | Maximum second-moment error $1.43\times10^{-13}$; fourth-moment error $3.28\times10^{-11}$ |
| Fourth-moment inequality and uniform departure bound on the same spin instances | 1,092 | Both inequalities passed, including departure probability at least $1/9$ |

The code asserts likelihood and state-normalization errors below $10^{-10}$,
endpoint errors below $10^{-12}$, second-moment errors below $10^{-9}$,
and fourth-moment errors below $10^{-7}$. Inequality comparisons allow
the stated floating-point tolerances in the script.

The random-unitary calculation explicitly constructs the symmetrized tensor
state and applies the entire unknown unitary to each factor. It therefore
checks that the output likelihood depends only on the specified transition,
for the instances tested. It does not numerically synthesize the sorting-network
or streaming encoders; their correctness and asymptotic costs are established
in [Implementation](../science/implementation.md).

## Poisson features: complex signs and retained query histories

[check_poisson_features.py](check_poisson_features.py) uses finite
circuit-generated Laurent polynomials, including controlled forward queries,
controlled inverse queries, and mixed-direction schedules. Known Fourier gates
mix the retained control branches; no measurement outcome is discarded.

| Check | Instances | What is compared |
|---|---:|---|
| Signed Gram identity at complex biases | 845 | Explicit feature inner products against independent Poisson moment formulas |
| Pointwise norm of six circuit-generated Laurent states | 150 | Evaluation on sampled torus phases against unit norm |
| Purification and contraction | 30 | Partial trace of explicit features against a density matrix computed directly from moments; auxiliary-vector construction against the diagonal contraction |
| Radial polynomial after phase averaging | 24 | Exact finite angular average against the surviving equal-degree terms |

All recorded identity errors are below $2.67\times10^{-15}$, against an
asserted tolerance of $2\times10^{-10}$. The script also checks the
contraction norm and difference bounds, and equality of the two purifications
at zero bias.

The finite angle count in the script is larger than the maximum Fourier
frequency, so its angular sum is exact in exact arithmetic. This is a check
of the degree and orientation conventions used in
[the Poisson–Müntz proof](../science/poisson-muntz-bound.md).

## What establishes the universal claims

| Claim | Analytical basis |
|---|---|
| Uniform detection for every alternative transition | Exact two-mode action, complete likelihood, and second/fourth-moment argument in [Dicke probes](../science/dicke-probe.md) |
| Feasibility for arbitrary directional budget pairs | Integer allocation and block tuning in [Resource frontier](../science/resource-frontier.md) |
| Distinguishability bound for every allowed algorithm | Pointwise-normalized Laurent model, explicit purification, common-phase average, and the cited Newman inequality in [Poisson–Müntz bound](../science/poisson-muntz-bound.md) |
| Exact-zero and gap lower bounds | Concentration, unitary repair, and adaptive hybrid in [Promise reductions](../science/promise-reductions.md) |
| Gate and memory costs | Explicit reversible constructions in [Implementation](../science/implementation.md) |

Passing the finite suite does not prove a universal lower bound, establish
literature priority, validate a noisy implementation, or demonstrate a hardware
runtime advantage. The reference output records a local numerical run; it is
not a claim that GitHub Actions or a physical device executed these checks.
