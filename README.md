# Quantum Inverse Query Tradeoff

**How much forward-query work can a limited number of inverse queries save?**

For a fixed unknown unitary $U$, this project studies whether a transition
between known pure states has zero amplitude or magnitude at least
$\varepsilon$. Counting $F$ calls to $U$ and $R$ calls to
$U^\dagger$ separately, the optimal budget boundary is

```math
\boxed{F+R+FR=\Theta(\varepsilon^{-2})}
```

in the sufficient large-dimension regimes below. The constructive algorithm
works in every dimension. The matching converse allows controlled queries,
ancillas, and adaptive measurements.

## Results and scope

Let $a=\langle g|U|s\rangle$, with known preparable source $s$ and target
$g$, and let $0<\varepsilon\le1/4$. Success is at least $2/3$ on every
promised unitary.

| Testing task | Promise | Sufficient dimension for the matching lower bound |
|---|---|---|
| Exact-zero transition | $a=0$ versus $\lvert a\rvert\ge\varepsilon$ | $d\ge16\varepsilon^{-4}$ |
| Transition magnitude gap | $\lvert a\rvert\le\varepsilon/100$ versus $\lvert a\rvert\ge\varepsilon$ | $d\ge10^6\varepsilon^{-2}$ |
| Normalized-trace magnitude gap | Replace $a$ by $\operatorname{Tr}(U)/d$ in the preceding row | $d\ge10^6\varepsilon^{-2}$ |

The frontier means necessity and sufficiency up to universal constants:
the proofs give the necessary bound
$F+R+FR\ge\varepsilon^{-2}/4096$, and a deliberately conservative sufficient
bound $F+R+FR\ge10^5\varepsilon^{-2}$. The dimension thresholds are
sufficient and are not claimed optimal.

If an inverse call costs $\kappa\ge1$ times a forward call, the optimal
weighted query cost is

```math
C_{\kappa,\mathrm{opt}}
=\Theta\!\left(
\min\left\{\varepsilon^{-2},
\frac{\sqrt\kappa}{\varepsilon}\right\}
\right).
```

See [the model and exact statements](science/model.md) and
[the complete budget-allocation and cost proof](science/resource-frontier.md).

## How the two bounds meet

An inverse call on the known target can prepare a copy of an unknown direction
orthogonal to the source. A failed preparation is itself a charged detection
event. Known-state tests and controlled permutations place the successful
copies among source registers in a symmetric Dicke state. After the forward
calls, counting target outcomes detects a departure from the null's fixed
count. Exact second and fourth moments make this guarantee uniform over the
whole alternative promise.

The converse represents a general query algorithm by a normalized vector
Laurent polynomial. A Poisson-phase purification and an average over its
common phase produce a radial Müntz polynomial. Newman's classical derivative
inequality bounds how quickly the output ensembles can separate. Concentration
and a separate rank-two unitary correction give the two testing promises.

The collective-spin gain, reversible amplitude-amplification endpoints, and
Newman inequality are established ingredients. The
[related-work account](references/related-work.md) identifies them and explains
the additional mixed-budget construction and converse.

## Read the science

| Start with this question | Read |
|---|---|
| What is proved, under which access assumptions? | [Model and results](science/model.md) |
| How is the probe prepared, and what is measured? | [Dicke probe](science/dicke-probe.md) |
| What do routing, known-state operations, and memory cost? | [Implementation](science/implementation.md) |
| Why is the mixed-budget scale unavoidable? | [Poisson–Müntz bound](science/poisson-muntz-bound.md) |
| Where do the dimension and promise restrictions enter? | [Promise reductions](science/promise-reductions.md) |
| How do arbitrary budgets and expensive inverses behave? | [Resource frontier](science/resource-frontier.md) |
| Which earlier results are used or compared? | [Related work](references/related-work.md) · [Bibliography](references/bibliography.bib) |
| How can the finite checks be reproduced? | [Verification](verification/README.md) |

## Reproduce the checks

With Python 3.12, run from the repository root:

```sh
python3 -m pip install -r requirements.txt
python3 verification/run_all.py
```

The suite checks small full-unitary count distributions, spin-moment identities,
complex Poisson features, and the purification/contraction conventions.
[Verification](verification/README.md) records the tested environment, counts,
tolerances, and expected output. These are finite numerical checks; the universal
claims rest on the analytical proofs.

## Consequential boundaries

The result concerns detection of a **known rank-one transition**. It does not
supply a global additive-precision amplitude-estimation algorithm or
amplification into an unknown good subspace. The matching trace lower bound
has a magnitude-gap promise; the exact-zero matrix-element repair does not
establish an exact-zero trace converse.

The dimension requirements prevent a claim of a uniform forward-only
obstruction in fixed dimension. Ordinary preparation, encoding, coherent
memory, and readout costs are stated separately. The full-register and
streaming implementations offer different gate/memory choices; their best
individual bounds are not simultaneous. Weighted query optimality alone
does not establish a hardware runtime advantage.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
