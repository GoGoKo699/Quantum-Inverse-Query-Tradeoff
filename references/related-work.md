# Relation to prior work

The result in this repository is a resource theorem for a specific decision task: testing a known rank-one transition amplitude with separately counted forward and inverse queries. The [model](../science/model.md) and [resource frontier](../science/resource-frontier.md) state its dimension and promise requirements. This page identifies the established ingredients and the additional argument supplied here.

References were checked against the primary versions listed below on 22 October 2026. These comparisons delimit the contribution; they are not a claim that every relevant publication has been exhaustively screened. Bibliographic records are in [bibliography.bib](bibliography.bib).

## What is inherited, and what is proved here

| Ingredient | Established source or mechanism | Role of this repository |
|---|---|---|
| Quadratic improvement with reversible oracle access | Amplitude amplification and estimation | Resolve the resources between the zero-inverse and comparable-direction endpoints. |
| Forward-only obstruction in high dimension | Tang–Wright; subsequent time-reversal lower bounds | Preserve the two directional degree budgets throughout a matching converse. |
| Collective sensitivity from unequal occupations | Dicke states and generalized Holland–Burnett interferometry | Prepare the unknown oracle-defined mode using charged inverse calls and encode it using known-state tests. |
| Efficient preparation of a known occupation mask | Kaye–Mosca and later Dicke-state circuits | Route existing unknown-state copies under that mask and erase its label coherently. |
| Derivative control for sparse real powers | Newman's inequality for Müntz polynomials | Derive the required radial polynomial from a normalized query state through Poisson features and phase averaging. |

The claimed combination is the upper construction together with the universal lower bound yielding the budget boundary

```math
F+R+FR=\Theta(\varepsilon^{-2})
```

in the specified worst-case dimension regimes. The expression for Dicke-state sensitivity, the existence of entangled parallel probes, and the classical derivative inequality are not new claims. Neither is the general importance of inverse access.

## Reversible and forward-only endpoints

**Brassard, Høyer, Mosca, and Tapp, _Quantum Amplitude Amplification and Estimation_.** Their [original paper](https://arxiv.org/abs/quant-ph/0005055) supplies the standard reversible benchmark: a success probability of order $\varepsilon^2$ can be amplified using order $1/\varepsilon$ applications of a preparation unitary and its inverse. This establishes the balanced-direction scale. Its usual implementation repeatedly spends both directions; it does not make a supply of inverse queries reusable at no cost.

**Tang and Wright, _Amplitude amplification and estimation require inverses_, arXiv:2507.23787v2 (23 April 2026).** [Theorems 1.4–1.5 and the hard-instance construction](https://arxiv.org/html/2507.23787v2) establish the forward-only obstruction, including an amplitude-estimation lower bound of order $\min(d,\varepsilon^{-2})$ and controlled-query access. Their diagonal-phase and normalized-trace viewpoint is an important predecessor of the hard ensembles used here. The cited theorems do not state a frontier in two separate total counts. The [Poisson–Müntz bound](../science/poisson-muntz-bound.md) retains those counts and yields the product term $FR$.

**Allen, Caro, Chen, Gur, and Lowe, _The power of time reversal in Hamiltonian property testing_, arXiv:2610.04996v1 (4 October 2026).** Their [continuous-time lower-bound framework](https://arxiv.org/html/2610.04996v1) establishes advantages of time reversal for Hamiltonian property testing, also improving related inverse-free amplitude bounds and allowing fractional queries. This repository concerns a fixed unitary and integer directional query budgets. Its theorem does not imply an analogous tradeoff between positive and negative Hamiltonian evolution times.

**Wang, Carolan, and Childs, _On State Distinguishing Without Inverse Queries_, arXiv:2610.05389v1 (4 October 2026).** [Theorem 1.1](https://arxiv.org/html/2610.05389v1) proves a forward-only obstruction even when the two candidate output states are known. The same paper gives a continuous-time quantum-Zeno algorithm under a different promise on a Hamiltonian's first column. These distinctions matter: knowledge of a target does not by itself remove the discrete-query obstruction, while a discrete-query lower bound need not survive a change to continuous-time access.

## The collective probe has established metrological roots

**Thekkadath et al., _Quantum-enhanced interferometry with large heralded photon-number states_, npj Quantum Information 6, 89 (2020).** The [paper and supplement](https://arxiv.org/abs/2006.08449v2) study generalized Holland–Burnett probes with unequal input occupations. Supplementary Note 1, Eq. (S20), gives the lossless quantum Fisher information $2h_1h_2+h_1+h_2$; photon counting attains it in the lossless setting. These are direct precedents for the collective sensitivity and count readout used here.

**Ataman, _Quantum Fisher information maximization in an unbalanced interferometer_, Physical Review A 105, 012604 (2022).** [Section V, Eq. (55)](https://arxiv.org/abs/2201.05362v1) gives the balanced-interferometer expression $n+m+2nm$ for two-mode number inputs. Substituting $n=F-R$, $m=R$ produces exactly

```math
\Lambda=F+2R(F-R).
```

The rotation-angle convention in this repository differs from the optical phase convention, so its pure-state quantum Fisher information with respect to that rotation angle is $4\Lambda$. The population enhancement itself is established physics.

The additional operational step is that the second logical mode here is unknown and depends on $U^\dagger|g\rangle$. Inverse queries prepare its copies, preparation failures are counted, and known-source projectors permit their coherent placement without identifying or cloning that mode. The [Dicke-probe page](../science/dicke-probe.md) then proves a finite-promise detection guarantee from count moments; local Fisher information alone would not prove that guarantee. The seed copies are consumed by the experiment.

## Dimension-dependent inverse-free protocols

**Chen, _Inverse-free quantum state estimation with Heisenberg scaling_, arXiv:2510.25750v1 (29 October 2025).** [Corollary 1.5](https://arxiv.org/html/2510.25750v1) gives inverse-free estimation of an amplitude magnitude to additive error $\varepsilon$ using $O(\min(d^{3/2}/\varepsilon,\varepsilon^{-2}))$ queries. The construction uses entangled parallel probes. This is why the high-dimensional qualification in our converse is substantive. We do not assert an $\varepsilon^{-2}$ forward-only lower bound uniformly in dimension, nor solve the full finite-dimensional directional frontier.

**He, Li, Scully, Zhou, and Yang, _Optimal classical shadow estimation of unitary channels at Heisenberg limit_, arXiv:2606.13638v2 (29 September 2026).** The [current version](https://arxiv.org/abs/2606.13638v2) gives a parallel inverse-free channel-shadow protocol. Section 3.3, Corollary 3.3, specializes it to estimating a known-projector **probability**

```math
b(U)=\operatorname{tr}\!\left(\Pi U|0\rangle\langle0|U^\dagger\right)
```

within additive error $\delta$, with $O(\min(d^{3/2}/\delta,\delta^{-2}))$ queries after combining with sampling. Although that section calls $b(U)$ an amplitude, it is the probability, whereas this repository uses $\varepsilon$ for an amplitude magnitude. A direct application to our near-zero promise therefore uses probability error of order $\varepsilon^2$; one must not silently replace $\delta$ by $\varepsilon$. The v2 channel-shadow bound is also version sensitive: for constant effective observable size the abstract states $O(\min(d\delta^{-2},d^{3/2}\delta^{-1}))$.

## Other tradeoffs count different resources

**Giurgica-Tiron et al., _Low depth algorithms for quantum amplitude estimation_, Quantum 6, 745 (2022)** ([primary version](https://arxiv.org/abs/2012.03348v2)), and **Erle and Koczor, _Nearly Optimal Amplitude Estimation at any Depth_, arXiv:2608.24434v1 (25 August 2026)** ([primary version](https://arxiv.org/abs/2608.24434v1)), trade circuit depth against repetitions or total queries. The latter gives a uniform angle-accuracy guarantee, including near zero, with $M^2N$ of order $\varepsilon^{-2}$ up to logarithmic factors. Its Grover iterate explicitly contains both $U$ and $U^\dagger$. Repeating a short circuit spends its inverse queries again on each repetition. Consequently circuit depth and **total inverse count** cannot be identified. Near-zero overlap certification is already an application in that literature.

**Tang, Wright, and Zhandry, _Conjugate queries can help_, arXiv:2510.07622v2 (8 May 2026).** [Theorem 1.5](https://arxiv.org/html/2510.07622v2) simulates $q$ total forward/inverse state-preparation queries, averaged over a specified completion distribution, with $O(q^2/\delta)$ copies to trace-distance error $\delta$. The v2 statement explicitly notes that this distribution is supported on reflections and is not the uniform completion distribution. Its direct budget dependence is through $q=F+R$, which does not resolve $F+R+FR$. A separately chosen forward-only ensemble cannot simply be substituted into this simulator.

## Imported mathematical and circuit ingredients

### Newman's derivative inequality

The external analytic ingredient is **D. J. Newman's _Derivative bounds for Müntz polynomials_**, Journal of Approximation Theory 18 (1976), 360–362. We use the statement reproduced as Theorem 1.1 in **Borwein and Erdélyi, _Newman's inequality for Müntz polynomials on positive intervals_**, Journal of Approximation Theory 85 (1996), 132–139 ([author-hosted manuscript](https://people.tamu.edu/~terdelyi/papers-online/positive.pdf)):

```math
\|xP'(x)\|_{[0,1]}
\le 11\left(\sum_j\lambda_j\right)\|P\|_{[0,1]},
\qquad
P\in\operatorname{span}_{\mathbb R}\{x^{\lambda_j}\}.
```

Theorem 1.1 requires distinct nonnegative exponents; it does **not** require the smallest exponent to be zero. The different positive-interval theorem in the manuscript's abstract has additional hypotheses and is not the result invoked here. Our [converse](../science/poisson-muntz-bound.md) supplies the quantum-to-polynomial reduction; it does not claim a new derivative inequality.

### Known Dicke-mask preparation

**Kaye and Mosca, _Quantum Networks for Generating Arbitrary Quantum States_**, [arXiv:quant-ph/0407102v1](https://arxiv.org/abs/quant-ph/0407102v1), Sections 2–4, provide the conditional-probability state-preparation framework used for the known binary occupation mask. **Aktar, Bärtschi, Badawy, and Eidenbenz, _A Divide-and-Conquer Approach to Dicke State Preparation_**, [arXiv:2112.12435v2](https://arxiv.org/abs/2112.12435v2), Table 1, records the corresponding $O(F\operatorname{polylog}(F/\delta))$ circuit bound. This preparation handles the known mask, not arbitrary unknown quantum states. The additional routing and mask-erasure construction, and the separate full-register and streaming costs, are given in [implementation.md](../science/implementation.md).

The routing uses established sorting-network primitives: **Batcher, _Sorting networks and their applications_** ([1968 conference paper](https://doi.org/10.1145/1468075.1468121)), and the coherent sorting constructions discussed in **Liu, Childs, and Gottesman, _Low-depth quantum symmetrization_**, [arXiv:2411.04019v2](https://arxiv.org/abs/2411.04019v2), Section II. These are credited as circuit ingredients; the implementation page separately explains how the retained mask permits data routing and workspace erasure in this task.

## Boundaries of the comparison

The result is a coherent oracle theorem for scalar overlap testing. The [promise reductions](../science/promise-reductions.md) separately state the fixed-ratio normalized-trace gap theorem. They do not establish an exact-zero trace converse. This account also does not claim a general algorithm for outputting an unknown good state, full additive amplitude estimation, noisy-device advantage, or an optimal small-dimension tradeoff. Keeping those distinctions explicit is necessary both for comparison with existing results and for interpreting the contribution.
