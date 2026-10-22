# Understanding the forward–inverse query tradeoff

How can a few uses of an operation in reverse help us test what it does
in the forward direction? This project answers that question for a specific
task: detect whether a fixed unknown unitary has a nonzero transition between
two known pure states.

The selected educational anchor is **Nielsen and Chuang, *Quantum Computation
and Quantum Information*, 10th Anniversary Edition (2010)**. The
[anchor bridge](anchor-bridge.md) identifies the relevant sections and translates
their notation. The [30-milestone map](milestones.md) specifies the project's
understanding targets. This explanation follows its settled 14-foundation,
16-narrative structure; the linked science pages contain the complete proofs.

| Part of this explanation | Milestones | Main connection |
|---|---|---|
| 1–3: the objects and proof framework | M01–M14 | Quantum operations, query resources, and distinguishability |
| 4–5: preparing and reading the probe | M15–M19 | An inverse query supplies a mode for collective interference |
| 6: implementing the construction | M20 | Query savings and circuit costs are separate resources |
| 7: proving an obstruction | M21–M25 | General algorithms become constrained polynomials |
| 8–10: transfers and synthesis | M26–M30 | Promise, dimension, budget, and attribution boundaries |

## 1. A transition, a probability, and two kinds of access

**M01–M06.** A pure state is represented by a unit vector. The notation
$|s\rangle$ names a prepared source state; $|g\rangle$ names the target state.
A unitary $U$ transforms a state while preserving inner products. Its inverse
is $U^\dagger$. Knowing that this inverse exists does not give an algorithm
free access to it: the two directions can have different budgets and costs.

The complex number

```math
a=\langle g|U|s\rangle
```

is the transition amplitude. Its magnitude $|a|$ is a nonnegative number.
Preparing $s$, applying $U$, and testing for $g$ gives the target outcome with
probability

```math
p=|a|^2.
```

These quantities must stay distinct. A promised magnitude of at least
$\varepsilon$ means a probability of at least $\varepsilon^2$, not
$\varepsilon$. For example, magnitude $1/10$ means probability $1/100$.

The basic question is whether $a=0$ or $|a|\ge\varepsilon$. Inputs between
these cases need not be classified. The companion magnitude-gap task permits
$|a|\le\varepsilon/100$ in the low case. Both are decision tasks; neither asks
for a numerical estimate of every possible value of $a$.

Let $F$ count all calls to $U$ and $R$ all calls to $U^\dagger$, including
preparation attempts and repetitions. The budgets apply on every execution
branch. Known source and target preparation circuits, their coherent
projector tests, memory, and ordinary gates are additional resources.
The [access model](../science/model.md#access-and-resource-conventions)
specifies precisely what is supplied.

Ordinary sampling illustrates one endpoint. With $F$ independent forward
experiments, the probability of seeing at least one target is
$1-(1-p)^F$. Therefore $F$ of order $\varepsilon^{-2}$ suffices in the
exact-zero task. Inverse sampling gives the other endpoint because
$|\langle s|U^\dagger|g\rangle|^2=p$.

## 2. From rotations to collective counts

**M07–M09.** Nielsen and Chuang's search geometry explains how coherent
rotations can make a small transition easier to detect when both oracle
directions are available. In this project, the relevant issue is how much of
that improvement survives when inverse calls are scarce.

A product of independent experiments is only one possible probe. A *symmetric
occupation state* coherently combines the different placements of a fixed
number of excitations among several registers. With two orthogonal states
$s$ and $\xi$, the smallest example is

```math
|D_2^1(\xi,s)\rangle
=\frac{|s\rangle|\xi\rangle+|\xi\rangle|s\rangle}{\sqrt2}.
```

The two summands are added as amplitudes before measurement. If a separate
register still labels which placement occurred, discarding that register
instead produces a mixture and loses the interference needed here.

For a probe block with $1\le R\le F$, there are $F$ registers containing
$R$ excitations. Its sensitivity scale is

```math
\Lambda=F+2R(F-R).
```

The endpoint $R=0$ uses sampling. Section 9 explains how these block budgets
are chosen within arbitrary available budgets.

The collective-spin interpretation treats the count as an angular-momentum
coordinate. The formula is an established symmetric-state effect; the project
must additionally show how to prepare its unknown excitation mode with
exactly the charged oracle resources.

A sensitivity at $p=0$ is also insufficient for a decision theorem. The test
must work for **every** promised $p\ge\varepsilon^2$. Oscillating return
probabilities make a small-parameter expansion unreliable away from zero.
The proof instead controls the second and fourth moments of the full count
distribution. Section 5 explains how those moments give a uniform guarantee.

## 3. The framework for a universal lower bound

**M10–M14.** An upper bound exhibits one successful algorithm. A lower bound
must cover every allowed algorithm, including ancillas, controls, and adaptive
measurements.

A density operator describes the state available to an observer, including
mixtures obtained by averaging an unknown oracle. For two such states,

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1
```

is their trace distance. Here the trace norm adds the singular values of a
matrix. Operationally, no event in a measurement can have probabilities
differing by more than $D$. A test that accepts one case with probability at
least $2/3$ and the other with probability at most $1/3$ therefore needs
trace distance at least $1/3$.

The converse chooses diagonal oracles whose entries are phases $z_j$ on the
unit circle. Every forward query can introduce a factor $z_j$; every inverse
query can introduce $z_j^{-1}$. Retaining all work registers and measurement
records represents the final state by a normalized vector Laurent polynomial:
a polynomial that may have positive and negative powers. The total positive
degree is at most $F$ and the total negative degree at most $R$.

This directional accounting is more informative than using only $F+R$.
The proof compares an unbiased phase ensemble with a weakly biased one,
randomizing a common bias angle as part of the chosen hard ensemble.
This randomization preserves the magnitude promise. With controlled queries,
relative oracle phases can be observable, so the average cannot simply be
dropped as an unobservable global phase. A classical polynomial derivative
bound then limits the change in the algorithm's output.

The background phase now closes into a single architecture: construct a probe
whose output separates the promises, and prove that any budget-limited
algorithm has too little output distinguishability below the same scale.
The exact statements and dependencies are in
[the model](../science/model.md#scientific-route-and-proof-dependencies).

## 4. An inverse query supplies the missing mode

**M15–M17.** Apply $U^\dagger$ to $g$ and test the known source projector
$\Pi_s=|s\rangle\langle s|$. There are two useful outcomes:

- The source outcome occurs with probability $p$. Under the exact-zero
  promise this already proves the alternative, so the algorithm accepts.
- The complementary outcome occurs with probability $1-p$. For $p<1$ it
  leaves the normalized state

```math
|\xi\rangle=
\frac{U^\dagger|g\rangle-a^*|s\rangle}{\sqrt{1-p}},
\qquad \langle s|\xi\rangle=0.
```

The star means complex conjugation. The algorithm does not calculate $a$ or
prepare this formula from classical data: the measurement physically leaves
the displayed state. Each copy costs one inverse call. For $p=1$ the first
outcome is certain, so the denominator is never needed.

After $R$ complementary outcomes, the algorithm holds $R$ copies of $\xi$.
A known uniform occupation mask controls permutations of those supplied
copies among $F-R$ source registers. To erase the mask coherently, test
whether each register is orthogonal to the known state $s$ and XOR that bit
into the corresponding mask qubit. Every placement then resets the mask to
zero. The data retain their coherent sum.

This works because the known test distinguishes $s$ from its orthogonal
complement without identifying the unknown vector $\xi$. It does not clone
$\xi$ or require a reflection about $\xi$. The
[encoder proof](../science/dicke-probe.md#3-deterministic-encoding-of-the-supplied-copies)
gives the normalized state and the workspace cleanup.

Define an output mode
$|\eta\rangle=(U|s\rangle-a|g\rangle)/\sqrt{1-p}$, orthogonal to $g$.
Writing $c=\sqrt{1-p}$, unitarity gives

```math
U|s\rangle=c|\eta\rangle+a|g\rangle,\qquad
U|\xi\rangle=-a^*|\eta\rangle+c|g\rangle.
```

Thus the unknown unitary acts as a two-mode rotation on the prepared inputs,
whatever it does on the rest of the space. The algorithm only measures the
known target $g$; it never needs to identify $\eta$.

## 5. A complete three-query example, then the uniform guarantee

**M18–M19.** Use one inverse call to attempt the preparation above. If it
accepts, stop. Otherwise encode $|D_2^1(\xi,s)\rangle$, apply $U$ to both
registers, and count the number $N$ of target outcomes. This uses at most
two forward calls and one inverse call.

Expanding the two-mode identities gives the following exact distribution
*conditional on the complementary preparation outcome*:

| Target count $N$ | Probability | Decision |
|---|---|---|
| $0$ | $2p(1-p)$ | Accept the alternative |
| $1$ | $(1-2p)^2$ | Do not accept |
| $2$ | $2p(1-p)$ | Accept the alternative |

The probabilities add to one. When $p=0$, exactly one target always appears,
so any other count certifies the alternative. The conditional acceptance
probability is $4p(1-p)$. Including the first preparation event gives

```math
\begin{aligned}
P_{\mathrm{det}}(p)
&=p+(1-p)\,4p(1-p)\\
&=1-(1-p)(1-2p)^2\\
&=5p-8p^2+4p^3.
\end{aligned}
```

For small $p$, its leading term is $5p$; three independent sampling calls
would give $1-(1-p)^3=3p+O(p^2)$. This is a concrete interference advantage
for this comparison. It is not yet a bounded-error algorithm for every small
$\varepsilon$. In this example $\Lambda=4$, while the general guarantee needs
$\Lambda\varepsilon^2\ge1$.

For a general block with $1\le R\le F$, the exact-zero null count is
exactly $R$. Put $Q=N-R$ and let
$M_2=\mathbb E(Q^2)$ and $M_4=\mathbb E(Q^4)$ refer to the conditional count
distribution. The exact calculations prove

```math
M_2\ge\Lambda p(1-p),\qquad
M_4\le5M_2^2+2M_2.
```

Cauchy–Schwarz applied on the event $Q\ne0$ gives
$M_2^2\le M_4\Pr(Q\ne0)$. Hence

```math
\Pr(Q\ne0)\ge\frac{M_2}{5M_2+2}.
```

If $\Lambda\varepsilon^2\ge1$ and
$\varepsilon^2\le p\le1/2$, then $M_2\ge1/2$ and this lower bound is
at least $1/9$. Including the preparation events can only improve the
unconditional detection probability. For $p\ge1/2$, the first inverse
preparation attempt already accepts with probability at least $1/2$.
This covers the whole alternative. Twenty independent repetitions make the
miss probability at most $(8/9)^{20}<1/3$.

The complete likelihood, moment identities, and a global upper bound on
false acceptance in the magnitude-gap task are proved in
[the Dicke-probe page](../science/dicke-probe.md).

## 6. Query counts and physical implementation

**M20.** A query is a use of the unknown oracle. Preparing known registers,
performing controlled permutations, retaining coherence, and measuring still
cost resources.

The full-register implementation prepares a known weight-$`R`$ bit mask and
uses reversible sorting to route the supplied copies. Its data register count
is $F$ before sorting-network padding and less than $2F$ with padding;
the mask and routing workspaces are additional. A streaming implementation
holds $R$ reservoir registers and one output register, emits one piece of the
probe at a time, and measures it after its forward query. Future operations
act on the remaining reservoir, so the early output measurements preserve
the intended joint statistics.

These are different circuits. The streaming construction's smaller live-data
memory has a different gate cost; it cannot be combined with the full-register
gate bound as though both belonged to one implementation. The detailed
[resource table](../science/implementation.md#6-streaming-resources-and-the-implementation-choice)
includes known preparation costs and precision. The decision proof also
reserves a finite error allowance for approximate known operations.

## 7. Why every algorithm faces the same scale

**M21–M25.** The lower bound's central task is to compare the output states of
general algorithms under two distributions of phase oracles.

The Poisson distribution on the unit circle supplies a controlled bias:
for a phase $z$ with complex bias $w$, its moments satisfy
$\mathbb E(z^n)=w^n$ for $n\ge0$, with the negative moments given by complex
conjugation. An explicit environment construction turns these moments into
inner products of feature vectors. Applied to all oracle coordinates, it
gives normalized purifications of the averaged algorithm outputs.

Purification is the textbook idea of representing a mixed state as part of a
larger pure state. The particular Poisson feature vectors and their signs are
derived locally in [the converse proof](../science/poisson-muntz-bound.md#3-exact-complex-poisson-features);
they are not supplied by the anchor.

Set $M=F+R$ and $L=\min(F,R)$. A carefully bounded contraction on the
environment makes the components share a radial factor. Averaging the common
phase then produces a scalar function

```math
q(x)=(1-x)^{M/2}p_L(x),\qquad
\deg p_L\le L,\qquad q(0)=1,\qquad |q(x)|\le1.
```

Here $x$ is the squared ensemble bias, not the transition probability of an
individual oracle, and $p_L$ is a polynomial, not the probability $p$ used
above. The two symbols occur in different roles. The contraction's error
must be added back when returning to normalized physical states.

After changing variable to $y=1-x$, the expression is a sum of powers with
exponents $M/2,M/2+1,\ldots,M/2+L$: a Müntz polynomial. Newman's classical
derivative inequality limits how quickly this bounded function can change.
The relevant sum of exponents is

```math
\frac{(L+1)(M+L)}2.
```

This is where separate positive and negative query degrees produce a product
scale. The full proof translates the derivative estimate back into a trace
distance bounded by a constant times
$r\sqrt{F+R+FR}$ for ensemble bias magnitude $r\le1/2$.
If the budgets are too small at $r$ of order $\varepsilon$, the two output
ensembles remain too close for successful testing.

An ensemble theorem alone is not yet the promised-input theorem. The phases
are independent conditional on the common bias, and their mean concentrates
near that bias. That places most
unbiased samples in the small-magnitude case and most biased samples in the
large-magnitude case, producing the magnitude-gap lower bound when
$d\ge10^6\varepsilon^{-2}$.

For the exact-zero task, a typical unbiased sample has a small residual
amplitude rather than exactly zero. A separate rank-two output rotation
repairs that one matrix element. A hybrid argument bounds how much the
repair can change any algorithm's state. This extra step yields the
sufficient condition $d\ge16\varepsilon^{-4}$.
The [promise-reduction proof](../science/promise-reductions.md) keeps these
two routes and their constants separate.

## 8. Which changes of task preserve the result?

**M26.** Known changes of basis transfer the construction and lower bound
to arbitrary known source and target states without adding oracle calls.
Their ordinary circuit cost still belongs in the implementation account.

For a normalized trace, prepare a known maximally entangled state

```math
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{j=1}^d|j\rangle|j\rangle.
```

Then

```math
\langle\Phi_d|(I\otimes U)|\Phi_d\rangle
=\frac{\mathrm{Tr}(U)}d.
```

A call to $I\otimes U$ uses one call to the original $d$-dimensional oracle;
the other register is an ancilla. This supplies a trace-testing upper bound.
The diagonal hard ensembles also give the magnitude-gap trace lower bound.

The exact-zero matrix-element repair does **not** preserve the normalized
trace in the required way. Consequently the project does not claim a
matching exact-zero trace lower bound. The distinction is part of the
theorem's scope, not a notation change that can be ignored.

## 9. From useful blocks to the full budget frontier

**M27–M29.** A good probe block does not automatically fit every supplied
pair of budgets. The allocation proof uses sampling when the smaller budget
is tiny. Otherwise it chooses an orientation, reserves calls for repetitions,
and tunes a smaller probe so that

```math
\varepsilon^{-2}\le\Lambda<3\varepsilon^{-2}.
```

The upper bound is useful for the magnitude-gap task: tuning prevents a block
from being excessively sensitive to the allowed small null amplitude.
Both preparation events and count events contribute to its error analysis.

Write $B=F+R+FR$. In the stated dimension regimes, the full result is

```math
B\ge\frac{\varepsilon^{-2}}{4096}\quad\text{necessary},
\qquad
B\ge10^5\varepsilon^{-2}\quad\text{sufficient}.
```

The constants are deliberately separated; the claim is an optimal scaling
up to universal factors, not an exact threshold at $B=\varepsilon^{-2}$.
The constructive sufficient bound works in every dimension. The matching
necessity has the promise-specific dimension assumptions from Section 7.

When inverse calls cost $\kappa\ge1$ times as much as forward calls, the cost
is $C_\kappa=F+\kappa R$. Optimizing along this frontier gives

```math
C_{\kappa,\mathrm{opt}}
=\Theta\!\left(\min\left\{\varepsilon^{-2},
\frac{\sqrt\kappa}{\varepsilon}\right\}\right).
```

For $\kappa=1$ the scale is $\varepsilon^{-1}$. For intermediate inverse
costs, one uses more forward than inverse calls. Once
$\kappa$ reaches order $\varepsilon^{-2}$, ordinary sampling attains the
optimal order without paying for inverse access.
The [resource-frontier proof](../science/resource-frontier.md) includes
integer budgets, repetitions, both promise errors, and the weighted-cost
lower bound.

## 10. The whole contribution and its evidence

**M30.** The result joins two complementary facts. A charged inverse query can
supply an unknown orthogonal mode; coherent routing then turns several such
copies into a useful collective probe. Conversely, a general algorithm's
separately bounded Laurent degrees constrain its ability to distinguish
appropriately chosen oracle ensembles. These arguments meet at
$F+R+FR=\Theta(\varepsilon^{-2})$ in the sufficient dimension regimes.

The [related-work account](../references/related-work.md) attributes the
existing collective-spin sensitivity, amplitude-amplification endpoints,
state-preparation ingredients, and Newman inequality. The project's
contribution is the assembled and proved mixed-budget testing frontier with
its access, promise, dimension, and implementation requirements.

The [finite verification suite](../verification/README.md) checks explicit
count distributions, second and fourth moments, Poisson feature Gram
identities, and normalization/contraction conventions. Passing these finite
checks supports the algebraic implementations; the analytical arguments
establish the universal statements.

The account gives a detection result and an estimation lower-bound corollary,
not a matching general additive-estimation algorithm. It does not establish
optimal dimension thresholds or a hardware runtime advantage. These
boundaries tell a reader where the proved result ends and where another
argument would be required.

Return to the [milestone map](milestones.md), consult the
[Nielsen–Chuang bridge](anchor-bridge.md), or go directly to the
[canonical statements](../science/model.md).
