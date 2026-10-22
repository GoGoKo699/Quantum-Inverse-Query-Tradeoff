# From Nielsen–Chuang to the inverse-query tradeoff

The single educational anchor for this project is **Michael A. Nielsen and Isaac L. Chuang, _Quantum Computation and Quantum Information_, 10th Anniversary Edition (Cambridge University Press, 2010)**. Use it for the state, circuit, measurement, and distinguishability language needed to read the project. The [30-milestone map](milestones.md) determines the project's learning route; the book's chapter order does not replace that map.

The [publisher's book page](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE) and [official contents and front matter](https://assets.cambridge.org/97811070/02173/frontmatter/9781107002173_frontmatter.pdf) verify the source and section numbers below. The front matter identifies the 2010 anniversary edition, version 16 dated July 2025. Page numbers below are printed book pages, not PDF page numbers. The public front matter is a contents reference; it is not the complete book.

Read the selected passages when their concepts become useful. There is no whole-book prerequisite. The repository supplies the additional derivations connecting these foundations to its theorem, while the primary papers cited in the scientific account supply attribution and the explicitly imported analytic inequality. They are not additional educational anchors.

## 1. Selected passages and their role

The topic descriptions in this table are guide labels, rather than new or altered textbook section titles.

| Project need | Precise anchor passages | Where the idea is used here |
|---|---|---|
| Vectors, amplitudes, adjoints, and products of registers | §§2.1.2, 2.1.4, 2.1.6–2.1.7; pp. 63, 65, 69–71 | Read $\langle g\rvert U\lvert s\rangle$, reverse an operation, and distinguish one register from many copies. |
| States, dynamics, and measured probabilities | §§2.2.1–2.2.3 and 2.2.5–2.2.6; pp. 80–90 | Convert an amplitude into a probability; implement the two-outcome source and target tests. |
| Global phase and composite systems | §§2.2.7–2.2.8; p. 93 | Understand why magnitude testing ignores one phase but a controlled oracle can make relative phases observable. |
| Mixtures, reduced states, purification, and environments | §§2.4.1, 2.4.3, 2.5, and 8.2.2; pp. 99, 105, 109, 357 | Represent randomized hard instances and retain measurement records without conditioning on a preferred outcome. |
| Resource counting and controlled circuits | §3.2.1; §§4.2–4.4 and 4.6; pp. 136, 174–185, 202 | Separate oracle budgets from known gates, and turn a known-state test into a coherent flag operation. |
| Exact gates and approximation | §§4.5.1–4.5.4; pp. 189–198 | Recognize the difference between an ideal query theorem and finite-precision synthesis of its additional encoder. |
| Search geometry, counting, and oracle limits | §§6.1.1, 6.1.3–6.1.4, 6.3, and 6.6–6.7; pp. 248, 252–253, 261, 269–271 | Understand the reversible benchmark, then identify why separately pricing the two directions asks a different resource question. |
| Distinguishability and fidelity | §§9.2.1–9.2.3; pp. 403–415 | Turn a bounded-error decision requirement into a necessary separation between output states. |
| Classical probability | Appendix 1; p. 608 | Interpret repetitions, conditioning, moments, and the concentration steps in the promise reductions. |

For a quick first pass, combine the states-and-measurement passages with the search geometry and then read [Model](../science/model.md). Return to purification and state distance before the converse. The more detailed circuit passages become useful when reading [Implementation](../science/implementation.md).

## 2. Translate the notation before comparing statements

| Symbol or idea | Meaning in this repository | Consequence for reading |
|---|---|---|
| $\lvert s\rangle,\lvert g\rangle$ | Known normalized source and target states | Their circuits are supplied known operations; their being known does not reveal what $U$ does. |
| $a=\langle g\rvert U\lvert s\rangle$ | A generally complex amplitude | The promise concerns its magnitude $\lvert a\rvert$. |
| $p=\lvert a\rvert^2$ | Transition probability | A magnitude threshold $\varepsilon$ corresponds to probability $\varepsilon^2$. |
| $F,R$ | Total forward and inverse query budgets | The letter $F$ here is a query count, not a fidelity. Lower-case $f,r$ may instead denote the budgets of one probe block. |
| $d$ and $n$ | Oracle dimension and $n=\lceil\log_2d\rceil$ qubits per encoded register | An experiment using many registers does not change the dimension of the queried oracle. |
| $D(\rho,\sigma)$ | $\tfrac12\lVert\rho-\sigma\rVert_1$ | Every event probability changes by at most $D$. |
| $\xi,\eta$ | Unknown orthogonal input and output directions defined from $U,s,g$ | Their use in a proof does not grant circuits that prepare or reflect about them. |
| $w=re^{i\theta}$ in the converse | The complex mean of a phase distribution | This lower-case $r$ is a bias radius, not an inverse query count. The proof explicitly uses $r=2\varepsilon$ in the promise reduction. |

The converse works directly with the overlap $A$ of two normalized purifications. Its pure-state distance formula is

```math
D\bigl(|\psi\rangle\langle\psi|,|\phi\rangle\langle\phi|\bigr)
=\sqrt{1-|\langle\psi|\phi\rangle|^2}.
```

This removes ambiguity between root-fidelity and squared-fidelity conventions: the modulus of the overlap and its square are different quantities. Likewise, the scalar polynomial called $p(x)$ in the converse has a local meaning there; it is not the transition probability $p$. Below it is written $P_{\rm rad}(x)$ to keep the two roles distinct.

## 3. The essential change in access assumptions

A known circuit can be reversed by reversing its gate sequence and taking adjoints. This applies to the supplied source and target circuits $S,G$. It does not give an algorithm the inverse of a black box merely because the box implements a unitary. Here a call to $U^\dagger$ is a separately supplied and separately counted resource.

The familiar two-dimensional search picture is a useful starting point. For example, a reflection about a state prepared by an unknown oracle has the form

```math
I-2U|s\rangle\langle s|U^\dagger
=U\bigl(I-2|s\rangle\langle s|\bigr)U^\dagger.
```

Implementing this expression through the oracle spends one call in each direction. Calling the entire expression one iteration does not remove either cost. The project asks how far one can move along the resource boundary when the total inverse supply is much smaller than the forward supply. The search geometry in the anchor motivates this question; the general reversible amplitude-amplification benchmark is attributed to [Brassard, Høyer, Mosca, and Tapp](https://arxiv.org/abs/quant-ph/0005055) in [Related work](../references/related-work.md).

Known-state tests remain available. For instance, the circuit $S$ converts a test of the all-zero state into a test of $\Pi_s=|s\rangle\langle s|$. Keeping the result coherent gives

```math
L_s=\Pi_s\otimes I+(I-\Pi_s)\otimes X.
```

This operation labels source and non-source components without identifying which unknown state lies in the orthogonal subspace. Its known-gate cost is charged through $C_s$ in [Implementation](../science/implementation.md). The corresponding target operation is charged through $C_g$.

The explicit upper algorithm uses no controlled call to the unknown oracle. The lower bound allows such calls so that its obstruction applies to a larger algorithm class. A coherent choice between forward and inverse actions is charged in both directions under the [model's conventions](../science/model.md#access-and-resource-conventions). Parallel calls still contribute individually to the total budgets.

## 4. From single-register geometry to the collective probe

The first local step requires only inner products, projection, and unitarity. For $p<1$, define

```math
|\xi\rangle=
\frac{U^\dagger|g\rangle-a^*|s\rangle}{\sqrt{1-p}},
\qquad
|\eta\rangle=
\frac{U|s\rangle-a|g\rangle}{\sqrt{1-p}}.
```

Then $\xi\perp s$, $\eta\perp g$, and

```math
\begin{aligned}
U|s\rangle&=\sqrt{1-p}|\eta\rangle+a|g\rangle,\\
U|\xi\rangle&=-a^*|\eta\rangle+\sqrt{1-p}|g\rangle.
\end{aligned}
```

These identities locate a two-dimensional input/output action even when the full oracle has very large dimension. They do not provide a classical description of either unknown direction.

One inverse call on $g$, followed by the source projection, either triggers immediate acceptance or supplies one copy of $\xi$. Acceptance certifies the alternative under the exact-zero promise; in the magnitude-gap task, the allocation proof controls its probability on the small null. The copy-producing event has probability $1-p$. Obtaining $R$ retained copies through $R$ attempts therefore has probability $(1-p)^R$. The algorithm counts all attempts, including the events that stop it. No discarded branch is supplied for free.

The next step is a collective state of $F$ registers with exactly $R$ occupations of $\xi$ and $F-R$ of $s$. A classical random choice of the occupied positions would produce a mixture. The probe instead maintains their coherent superposition. The [encoding construction](../science/implementation.md) prepares a known binary occupation mask, routes the existing copies under that mask, and erases the mask using the source/non-source labels. It moves the supplied unknown states; it does not clone them.

The target count is exactly $R$ when $p=0$. Its response away from zero has the collective scale

```math
\Lambda(F,R)=F+2R(F-R).
```

The unequal-occupation enhancement has established interferometric precedents, documented in [Related work](../references/related-work.md#the-collective-probe-has-established-metrological-roots). The project additionally needs a lawful preparation of the unknown mode and a uniform decision guarantee. The [Dicke-probe proof](../science/dicke-probe.md) supplies the exact count likelihood and a second/fourth-moment bound that detects every alternative above threshold. A local sensitivity calculation near $p=0$ would not establish that whole-promise statement.

Finally, the [allocation proof](../science/resource-frontier.md) tunes the block scale, repeats it a constant number of times, and treats both one-direction sampling endpoints. This is the step that turns a successful block into a statement about every sufficiently large available pair $(F,R)$.

## 5. From state distance to the universal converse

The anchor's purification and distance material explains how the converse is interpreted. The additional query-specific and approximation-theoretic reductions are proved locally in [Poisson–Müntz bound](../science/poisson-muntz-bound.md).

### Preserve the full algorithm

For a diagonal oracle with phases $z_1,\ldots,z_d$, a forward call inserts a factor $z_j$ and an inverse call inserts $z_j^{-1}$. Therefore a purified algorithm has a vector Laurent expansion

```math
|\Psi(z)\rangle=\sum_h |v_h\rangle z^h,
\qquad |h_+|_1\le F,\qquad |h_-|_1\le R.
```

The vector has norm one for every choice of phases. Random coins, measurement outcomes, and stopped branches can be retained in ancillary registers. Conditioning on one preferred outcome and normalizing it would generally divide by an oracle-dependent quantity and lose the polynomial structure. This is why the proof keeps every outcome.

### Build comparable purifications

The hard alternative uses phases with a specified complex mean $w$. Explicit feature vectors reproduce their Poisson moments as inner products. Tensoring these features produces a normalized purification $\Phi_w$ of the algorithm's averaged output. This is a concrete application of purification: an algebraic Gram identity specifies the environment, and pointwise normalization of $\Psi$ guarantees normalization of the resulting state.

A diagonal contraction then replaces the different environment-support factors with a common radial factor. The auxiliary comparison vector $\chi_w$ need not be normalized. The proof bounds its norm and its distance from $\Phi_w$, and returns to normalized purifications before using trace distance. It does not regard the contraction as a free physical preparation procedure.

### Average the common phase, then use the two degree budgets

Set $M=F+R$ and $L=\min(F,R)$. Averaging a term $`w^a\overline w^{\,b}`$ over the common phase of $w$ kills it unless $a=b$. The resulting real scalar function has the form

```math
q(x)=(1-x)^{M/2}P_{\rm rad}(x),
\qquad \deg P_{\rm rad}\le L,
\qquad q(0)=1,\quad |q(x)|\le1.
```

This is the point at which both budgets matter: matching a positive and a negative power cannot occur more than $\min(F,R)$ times. The common-angle average is part of the chosen hard ensemble. For controlled queries it cannot simply be removed by saying that global phase is unobservable; relative phases between an active and an inactive branch can be measured.

With $y=1-x$, the function belongs to the real span of the powers

```math
y^{M/2},\ y^{M/2+1},\ \ldots,\ y^{M/2+L}.
```

These powers form a Müntz space. **Newman's derivative inequality is the external analytic ingredient.** The exact version used is Theorem 1.1 in [Borwein and Erdélyi's author-hosted manuscript](https://people.tamu.edu/~terdelyi/papers-online/positive.pdf), with distinct nonnegative exponents. This theorem is not supplied by the selected textbook, and the research proof states its hypotheses and its use explicitly.

Its exponent sum is

```math
\sum_{j=0}^{L}\left(\frac M2+j\right)
=\frac{(L+1)(M+L)}2.
```

Integrating the derivative bound controls the purification overlap. Contractivity under partial trace then yields a bound of order

```math
D=O\!\left(r\sqrt{F+R+FR}\right)
\qquad (0\le r\le1/2).
```

The exact constants and normalized-state steps appear in the canonical proof. This estimate limits how differently any permitted algorithm can respond to the two ensembles; it is not restricted to the Dicke construction.

### Convert an ensemble statement into a promise theorem

The diagonal-family transition amplitude is the average of the oracle phases. Elementary second moments show that the two ensembles usually lie in the appropriate magnitude-gap regions. Any algorithm correct on every promised input must therefore separate their average outputs by a constant amount. The preceding trace-distance upper bound forces a large enough $F+R+FR$.

For an exact-zero null, merely being close to zero is insufficient. The [promise-reduction proof](../science/promise-reductions.md) defines a nearby unitary whose specified transition amplitude is exactly zero and bounds the algorithm's change by a query hybrid. This separate correction accounts for the different sufficient dimension condition.

## 6. What the bridge does and does not establish

The [model page](../science/model.md) remains the authority for the claims. For $0<\varepsilon\le1/4$, it combines a universal sufficient budget $F+R+FR\ge10^5\varepsilon^{-2}$ with the necessary budget $F+R+FR\ge\varepsilon^{-2}/4096$ under these sufficient dimension conditions:

| Task | Dimension needed for the stated converse |
|---|---|
| Zero rank-one transition versus magnitude at least $\varepsilon$ | $d\ge16\varepsilon^{-4}$ |
| Rank-one magnitude at most $\varepsilon/100$ versus at least $\varepsilon$ | $d\ge10^6\varepsilon^{-2}$ |
| Normalized-trace magnitude with the same fixed-ratio gap | $d\ge10^6\varepsilon^{-2}$ |

All corresponding upper constructions work in every dimension. The dimension thresholds and numerical constants are sufficient rather than optimized. The normalized-trace upper reduction uses a known maximally entangled state and the identity

```math
\langle\Phi_d|(I\otimes U)|\Phi_d\rangle
=\frac{\mathrm{Tr}(U)}d.
```

Here $d$ is the oracle dimension, although the entangled probe lives in dimension $d^2$. The proved trace converse has a magnitude gap. Correcting one transition matrix element to zero does not set the trace to zero, so the exact-zero transition converse does not establish an exact-zero trace converse.

The project's complete matching result is for testing. The promise reductions also give an additive-estimation **lower-bound** consequence; no matching general additive-estimation algorithm follows from the detection construction. Likewise, knowing the target state does not turn this into a procedure for outputting an unknown good state.

The primary circuit and metrology references credit ingredients beyond the anchor: known occupation-mask preparation, sorting primitives, and unequal-occupation sensitivity. The Poisson-feature reduction, the promise transfers, and the budget allocation are developed in the repository, with Newman's inequality as a stated external dependency. The [literature comparison](../references/related-work.md) records these distinctions rather than assigning another textbook.

Finally, the [verification scripts](../verification/README.md) check finite instances of the likelihood, moment, and Poisson-feature identities. These checks help detect algebraic or implementation mistakes; the all-input theorems rest on the analytical proofs. The scripts do not synthesize or numerically test the sorting-network and streaming encoders; their correctness and cost bounds are analytical. The stated oracle-cost advantage also leaves known-gate work, coherent memory, connectivity, and oracle noise to the explicit resource discussion. Reading the anchor's circuit model does not convert those costs into a hardware performance guarantee.
