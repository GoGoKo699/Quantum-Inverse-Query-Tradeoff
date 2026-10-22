# Model, results, and reading route

How many calls to an unknown operation can be saved by a limited supply of calls
to its inverse? The question matters whenever reversal is available but has a
different cost from forward evolution. Counting only the total number of oracle
calls conceals this distinction.

This project studies a specified transition between two known pure states. Its
main result is an optimal tradeoff between the two directional query budgets,
in a stated large-dimension regime. The construction works for every completion
of the unknown unitary; the converse permits coherent controls and adaptive
measurements.

## The testing problem

Let $U$ be a fixed unknown unitary on $\mathbb C^d$. The pure source
$|s\rangle$ and target $|g\rangle$ are known and have available preparation
circuits. Define

```math
a=\langle g|U|s\rangle,\qquad p=|a|^2.
```

Here $a$ is a complex amplitude, $|a|$ its magnitude, and $p$ the
probability of observing the target after preparing the source and applying
$U$. Throughout,

```math
0<\varepsilon\le \frac14.
```

**Exact-zero transition testing** asks for a binary answer distinguishing

```math
H_0:\ |a|=0
\qquad\text{from}\qquad
H_1:\ |a|\ge\varepsilon.
```

**Magnitude-gap transition testing** uses the more tolerant null promise

```math
H_0:\ |a|\le\varepsilon/100
\qquad\text{from}\qquad
H_1:\ |a|\ge\varepsilon.
```

No correctness condition is imposed between the two promise regions. Success
means probability at least $2/3$ on **each promised unitary**, including all
its otherwise unspecified matrix elements. The numerical factor $100$ is a
convenient fixed separation; it is not an optimized threshold.

The target is known. Producing $|g\rangle$ by its known circuit would not answer
either testing problem: the output must determine whether the unknown operation
connects the source to that target.

## Access and resource conventions

The two query budgets are nonnegative integers:

| Resource | Convention |
|---|---|
| $F$ | Maximum total number of calls to $U$ on any execution branch. |
| $R$ | Maximum total number of calls to $U^\dagger$ on any execution branch. |
| Known state operations | Preparation/unpreparation of $s,g$, and their coherent rank-one projector tests, have explicitly charged ordinary-circuit costs. |
| Work space | Arbitrary finite ancillas are allowed in the lower bound. The construction's register and ancillary costs are given separately. |
| Measurement | Adaptive measurements and classical feedback are allowed. Outcomes and failed preparations contribute to the actual algorithm and its success probability. |
| Coherent control | The lower bound also allows controlled forward and inverse calls, charged to their respective directions. The upper algorithm needs only uncontrolled oracle calls. |

Calls on subsystems of an entangled state count in the same way as calls on an
isolated register. Parallel execution changes depth, not these totals. A
coherently selected forward and inverse operation can be implemented by a
controlled call of each type and is charged accordingly; it is not a third
free oracle.

Known operations and ancillas carry no *query* cost. This convention does not
make them physically free. [Implementation](implementation.md) supplies two
explicit circuit realizations and keeps their gate and memory costs separate.
No QRAM, free classical data loading, oracle description, reflection about an
unknown state, or cloning operation is assumed.

For the ideal query theorem, the given known-state operations are exact.
Approximating the additional encoder to a fixed total trace-distance error
preserves the bounded-error result. Noise in the unknown oracle itself is a
different model and is not included.

## The budget frontier

Write

```math
B(F,R)=F+R+FR.
```

The phrase “optimal budget frontier” has the following uniform meaning. There
are universal positive constants $c,C$, independent of $d,\varepsilon,F,R$,
such that a successful algorithm requires $B(F,R)\ge c\varepsilon^{-2}$ in
the stated lower-bound dimension regime, and any available budget pair with
$B(F,R)\ge C\varepsilon^{-2}$ admits a successful algorithm. This describes
the boundary up to multiplicative constants, not an exact constant-size
feasibility curve.

### Theorem 1: exact-zero transition testing

For every dimension and known source/target pair, a bounded-error algorithm
exists whenever

```math
B(F,R)\ge 10^5\varepsilon^{-2}.
```

For

```math
d\ge16\varepsilon^{-4},
```

every algorithm solving the exact-zero problem for all $U\in U(d)$ obeys

```math
B(F,R)\ge \frac{\varepsilon^{-2}}{4096}.
```

Thus, in this sufficient large-dimension regime, the frontier is
$F+R+FR=\Theta(\varepsilon^{-2})$. The upper constant is deliberately coarse.
Neither constant nor the dimension threshold is claimed optimal. For dimensions
where a promise set is empty, the upper statement remains true but no
nontrivial lower statement is asserted.

### Theorem 2: magnitude-gap transition testing

The same upper bound holds in every dimension. The same necessary inequality
$B(F,R)\ge\varepsilon^{-2}/4096$ holds under the sufficient condition

```math
d\ge10^6\varepsilon^{-2}.
```

The exact-zero and magnitude-gap lower bounds use different reductions.
Their dimension requirements must not be interchanged.

### Corollary: normalized-trace magnitude

For an unknown $d$-dimensional unitary, define
$\tau(U)=\operatorname{Tr}(U)/d$. The magnitude-gap problem

```math
|\tau(U)|\le\varepsilon/100
\quad\text{versus}\quad
|\tau(U)|\ge\varepsilon
```

has the same budget frontier when $d\ge10^6\varepsilon^{-2}$. Its upper
bound uses the known maximally entangled state

```math
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{j=1}^d |j,j\rangle,
\qquad
\langle\Phi_d|(I\otimes U)|\Phi_d\rangle
=\frac{\operatorname{Tr}(U)}d.
```

One call to $I\otimes U$ is one call to $U$, and similarly for the inverse.
Here the lower-bound dimension $d$ is that of the queried oracle, not the
dimension $d^2$ of the two-register probe.

The exact-zero construction gives an upper bound for exact-zero trace testing
as well. The matching exact-zero **trace** lower bound is not established:
the rank-two repair used for transition amplitudes does not preserve or set
the trace.

## Why a product of budgets appears

An inverse call on the known target produces a state with a component
orthogonal to the known source. After projecting onto that orthogonal
component, it supplies one copy of an otherwise unknown input direction.
Coherent permutations place several such copies among many source registers
in a symmetric state. Forward calls then mix these two directions.

The resulting target count is exactly fixed under the zero null hypothesis.
For a block with $f$ forward calls and $r\le f/2$ inverse preparations,
the count's sensitivity is governed by

```math
\Lambda(f,r)=f+2r(f-r).
```

For $r\ll f$, each extra inverse preparation increases the useful scale by
order $f$. A uniform second/fourth-moment argument turns this sensitivity
into a detection guarantee over the whole alternative promise. Local Fisher
information alone would not supply that guarantee.

The converse starts from a diagonal-oracle ensemble. A general algorithm is
a vector Laurent polynomial with positive and negative degree budgets
$F,R$. A Poisson-phase purification, followed by a common-phase average,
reduces its distinguishability to a one-variable Müntz polynomial. Newman's
classical derivative inequality then gives the same mixed scale. Concentration
and a separate unitary repair connect this ensemble calculation to the
testing promises.

## Scientific route and proof dependencies

| Question | Authoritative page |
|---|---|
| What is the problem, and which theorem applies? | This page |
| How are inverse calls converted into a collective probe? | [Dicke probe and uniform detection](dicke-probe.md) |
| How is the unknown-mode encoding actually implemented? | [Implementation and ordinary resources](implementation.md) |
| Why can no general algorithm improve the scale? | [Poisson–Müntz distinguishability bound](poisson-muntz-bound.md) |
| How does that bound imply the two promises and the trace corollary? | [Promise reductions](promise-reductions.md) |
| How does a block yield arbitrary budgets and weighted costs? | [Resource frontier](resource-frontier.md) |
| Which ingredients and results are inherited? | [Related work](../references/related-work.md) |
| Which finite identities have executable checks? | [Verification](../verification/README.md) |

The upper half of Theorems 1–2 follows from the Dicke probe and the allocation
argument in the resource-frontier page. Their lower halves follow from the
Poisson–Müntz bound and the respective promise reductions. The trace corollary
uses the gap reduction directly. All these are analytical claims; the finite
numerical checks support selected identities and conventions.

## Boundaries of the contribution

These are detection theorems for a known rank-one transition, with a separate
normalized-trace gap corollary. They do not by themselves provide global
additive-precision amplitude estimation or amplification into an unknown
good subspace. Those tasks require additional arguments.

The stated dimension regimes matter. Existing dimension-dependent
inverse-free estimation results can improve on sampling in fixed dimension;
the [literature comparison](../references/related-work.md) explains this
without changing the large-dimension theorem.

The weighted-cost consequence counts oracle uses with specified prices.
Ordinary gates, coherent storage, geometry, and errors may dominate an
implementation. The two explicit encoder options expose these costs; no
hardware speedup or fault-tolerance theorem follows from query optimality alone.
