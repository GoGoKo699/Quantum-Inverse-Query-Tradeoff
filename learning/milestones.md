# Thirty milestones for the forward/inverse query tradeoff

This map states the project's understanding targets, their dependencies, and their sources. The [tutorial](tutorial.md) follows the same sequence; the linked files in `science/` remain authoritative for theorem statements and proofs. The targets cover the scientific structure of the project without attempting to enumerate every lemma or calculation.

The single educational anchor is Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information*, 10th Anniversary Edition (2010), abbreviated **N&C** below. Section numbers refer to that edition and are verified against the [official Cambridge contents](https://assets.cambridge.org/97811070/02173/frontmatter/9781107002173_frontmatter.pdf). The [anchor bridge](anchor-bridge.md) translates its notation and foundations into this project's assumptions and arguments. Textbook pointers identify relevant foundations. The Dicke construction, signed Laurent representation, Poisson features, and Müntz argument are supplied by the project and its attributed research sources; they are not claimed to be textbook results.

## Why fourteen background milestones and sixteen narrative milestones?

The question joins three kinds of reasoning: quantum states and reversible circuits, statistical detection from collective measurements, and a universal converse based on polynomial constraints. Fourteen background milestones build those objects and connect them into the common problem framework. Their final milestone, M14, integrates the prerequisites into the two proof obligations.

The sixteen narrative milestones then follow the scientific argument. M15–M20 build the achievable mechanism and its implementations; M21–M26 build the converse and connect it to the operational promises; M27–M30 combine both into the complete budget frontier, weighted cost, and contribution. Each proof branch moves from its local mechanism to its consequences, and the final four milestones integrate the branches. The allocation reflects the need for both a constructive algorithm and a general lower bound.

| Phase | Milestones | Scientific progression |
|---|---|---|
| Background/preliminaries | M01–M14 | States and operations → coherent probes and statistical evidence → general algorithms and distinguishability → the complete problem framework |
| Narrative/innovation | M15–M30 | Unknown-mode preparation and collective detection; normalized polynomial converse and promise reductions → matching frontier and its meaning |

## Phase I — Background/preliminaries

<a id="m01"></a>

### M01 — What a transition amplitude measures

- **ID and phase:** M01 · Background/preliminaries.
- **Central question:** What physical question is encoded by $a=\langle g|U|s\rangle$?
- **Understanding target:** Explain the roles of a normalized source, an unknown unitary, and a known target; distinguish the complex amplitude $a$, its magnitude $|a|$, and the observable probability $p=|a|^2$. Relate the amplitude threshold $\varepsilon$ to the probability threshold $\varepsilon^2$.
- **Dependencies and story role:** Starting point. It fixes the experimental meaning and notation used by every subsequent target.
- **Conceptual connection:** An inner product becomes a measurable event after state preparation, evolution, and a target-projector measurement.
- **Source pointers:** N&C §§2.1.4, 2.2.1–2.2.3; [Model — The testing problem](../science/model.md#the-testing-problem).

<a id="m02"></a>

### M02 — Unitary reversibility and oracle access

- **ID and phase:** M02 · Background/preliminaries.
- **Central question:** Why does the existence of $U^\dagger$ not make inverse queries freely available?
- **Understanding target:** Distinguish a mathematical inverse from an allowed oracle operation, and distinguish knowing one transition amplitude from knowing the entire unitary. Explain why the algorithm must work for every unspecified completion of $U$ and why $F$ and $R$ count separate resources.
- **Dependencies and story role:** Uses M01. It turns a single transition experiment into a problem about restricted access to an unknown operation.
- **Conceptual connection:** Unitary evolution preserves information, while a computational access model specifies which uses of that evolution are supplied and charged.
- **Source pointers:** N&C §§2.1.6, 2.2.2, 3.2.1, 6.1.1; [Model — Access and resource conventions](../science/model.md#access-and-resource-conventions).

<a id="m03"></a>

### M03 — Known projectors and all measurement outcomes

- **ID and phase:** M03 · Background/preliminaries.
- **Central question:** How can a known state be tested without discarding the significance of the other outcome?
- **Understanding target:** Explain the two outcomes of $`\{\Pi_s,I-\Pi_s\}`$, their probabilities, and their conditional output states. Relate a nondestructive projector measurement to a coherent flag computed with the known preparation circuit, and keep the probabilities and resource costs of all branches in the description.
- **Dependencies and story role:** Uses M01–M02. It supplies the operational primitive that will produce the unknown input mode and interpret a preparation failure as evidence.
- **Conceptual connection:** A projector separates orthogonal components; coherent implementation records the same distinction in an ancilla before any measurement is made.
- **Source pointers:** N&C §§2.2.3, 2.2.5, 4.3–4.4; [Implementation §1](../science/implementation.md#1-charged-known-state-operations); [Dicke probe §2](../science/dicke-probe.md#2-reverse-queries-prepare-an-unknown-input-mode).

<a id="m04"></a>

### M04 — Composite probes and supplied copies

- **ID and phase:** M04 · Background/preliminaries.
- **Central question:** What information is supplied by several quantum copies, and what changes when those registers become entangled?
- **Understanding target:** Read tensor-product states, distinguish independent copies from a coherent superposition of arrangements, and explain why permuting supplied unknown states does not clone them. Recognize that each unknown copy needs a preparation procedure and that an oracle call on one subsystem of an entangled probe remains one call.
- **Dependencies and story role:** Uses M01–M03. It moves from one register to the many-register probes used by the construction.
- **Conceptual connection:** The tensor product permits collective information processing while preserving a precise account of where the quantum information came from.
- **Source pointers:** N&C §§1.3.5, 2.1.7, 2.2.8; [Model — Access and resource conventions](../science/model.md#access-and-resource-conventions); [Dicke probe §3](../science/dicke-probe.md#3-deterministic-encoding-of-the-supplied-copies).

<a id="m05"></a>

### M05 — Coherent control and erasing a label

- **ID and phase:** M05 · Background/preliminaries.
- **Central question:** When can a control label be removed while preserving the superposition it helped create?
- **Understanding target:** Explain reversible computation, controlled permutations, and uncomputation. Identify the distinction between erasing workspace from retained input information and undoing the desired data transformation. Recognize why an orthogonal vacuum/nonvacuum label can later be recovered coherently from the data.
- **Dependencies and story role:** Uses M03–M04. It provides the circuit logic needed for a pure encoded probe rather than a data state entangled with an unused placement record.
- **Conceptual connection:** Classical reversible logic and quantum coherence meet in the requirement that auxiliary records be cleared without revealing a branch.
- **Source pointers:** N&C §§1.4.1, 4.3, 4.5.1–4.5.3; [Implementation §3](../science/implementation.md#3-reversible-routing-with-clean-workspace).

<a id="m06"></a>

### M06 — Sampling, promises, and bounded error

- **ID and phase:** M06 · Background/preliminaries.
- **Central question:** What does it mean to decide whether a transition is absent or appreciable?
- **Understanding target:** Distinguish exact-zero testing from the magnitude-gap promise, identify the region where no answer is required, and interpret success on each promised unitary. Explain why independent trials with event probability at least $\varepsilon^2$ give an $O(\varepsilon^{-2})$ sampling upper bound and why a separate converse is needed to establish optimality.
- **Dependencies and story role:** Uses M01–M04. It gives the baseline experiment, statistical error convention, and operational target for improving on sampling.
- **Conceptual connection:** A physical event probability becomes an algorithmic decision only after the promise and the acceptable error are specified.
- **Source pointers:** N&C Appendix 1, §§2.2.4, 3.2.1; [Model — The testing problem](../science/model.md#the-testing-problem); [Dicke probe — Sampling and useful parameter ranges](../science/dicke-probe.md#sampling-and-useful-parameter-ranges).

<a id="m07"></a>

### M07 — Two-mode rotations and the cost of reversible search

- **ID and phase:** M07 · Background/preliminaries.
- **Central question:** How does coherent rotation change transition probabilities, and which oracle directions does a reflection-based procedure spend?
- **Understanding target:** Interpret a two-dimensional unitary rotation and the role of a relative phase. Connect the geometry of quantum search to repeated rotations, while recognizing that a reflection conjugated by an unknown preparation unitary uses both that unitary and its inverse. Separate the geometry from any claim that one Grover iteration is a single directional query.
- **Dependencies and story role:** Uses M02–M06. It connects familiar reversible search to the question left open by unequal directional budgets.
- **Conceptual connection:** The same two-dimensional geometry can underlie algorithms with different access costs; the circuit implementing the rotation determines those costs.
- **Source pointers:** N&C §§2.2.7, 4.2, 6.1.1–6.1.4; [Related work — Reversible and forward-only endpoints](../references/related-work.md#reversible-and-forward-only-endpoints); [Resource frontier §4](../science/resource-frontier.md#4-matching-converse-and-interpretation).

<a id="m08"></a>

### M08 — Symmetric occupations and collective observables

- **ID and phase:** M08 · Background/preliminaries.
- **Central question:** Why can many two-mode registers be described by a single occupation count and collective spin?
- **Understanding target:** Explain a fixed-weight Dicke state as an equal coherent superposition of orthogonal occupation patterns. Relate $F$ two-mode registers to the symmetric spin sector $j=F/2$, the occupation label to $m=R-F/2$, and the ladder coefficients to the number of ways to change an occupation. Understand why this is a smaller description of a symmetric state, not an assumption of indistinguishable physical particles.
- **Dependencies and story role:** Uses M04–M07. It supplies the collective language that will expose how several prepared excitations influence many probes.
- **Conceptual connection:** Permutation symmetry turns individual two-mode rotations into a structured collective count distribution.
- **Source pointers:** N&C §§2.1.3, 2.1.7–2.1.9, 4.2 for the underlying algebra; the Dicke and collective-spin derivation is local in [Dicke probe §§3–5](../science/dicke-probe.md#3-deterministic-encoding-of-the-supplied-copies); [Related work — Metrological roots](../references/related-work.md#the-collective-probe-has-established-metrological-roots).

<a id="m09"></a>

### M09 — From moments to a uniform detection guarantee

- **ID and phase:** M09 · Background/preliminaries.
- **Central question:** Why is a large local sensitivity insufficient to prove success over an entire alternative promise?
- **Understanding target:** Distinguish a Taylor expansion or local Fisher information from a lower bound on the probability of a nonzero observed count change. Explain the role of the second and fourth moments in $\Pr(Q\ne0)\ge\mathbb E[Q^2]^2/\mathbb E[Q^4]$, and why controlling both prevents rare large outcomes from carrying all the second moment.
- **Dependencies and story role:** Uses M06–M08. It connects the collective observable to the type of finite-signal statistical guarantee the theorem needs.
- **Conceptual connection:** Cauchy–Schwarz converts information about the spread and tails of a distribution into actual detection probability.
- **Source pointers:** N&C §2.1.4 and Appendix 1 for mathematical foundations; [Dicke probe §§5–6](../science/dicke-probe.md#5-exact-second-and-fourth-moments) for the moment argument; [Dicke probe §7](../science/dicke-probe.md#7-local-information-and-scope) for the local-information distinction.

<a id="m10"></a>

### M10 — Averaged states, purifications, and distinguishability

- **ID and phase:** M10 · Background/preliminaries.
- **Central question:** How can a bound on two averaged quantum states limit every possible decision measurement?
- **Understanding target:** Interpret a density operator as an ensemble description, a purification as a normalized larger-system representation, and partial trace as discarding a subsystem. Use the operational meaning of $`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$ to connect a required acceptance-probability gap to a lower bound on distinguishability; recognize its contraction under discarding information.
- **Dependencies and story role:** Uses M03–M06. It begins the converse branch with the language needed to cover arbitrary final measurements.
- **Conceptual connection:** An algorithm-independent distance between output states bounds the advantage of every particular decision rule.
- **Source pointers:** N&C §§2.4.1, 2.4.3, 2.5, 9.2.1–9.2.3; [Poisson–Müntz bound §§1, 6](../science/poisson-muntz-bound.md#1-ensemble-theorem); [Promise reductions §1](../science/promise-reductions.md#1-two-diagonal-oracle-ensembles).

<a id="m11"></a>

### M11 — Query histories as signed polynomial degrees

- **ID and phase:** M11 · Background/preliminaries.
- **Central question:** What algebraic restriction does a directional query budget impose on a general quantum algorithm?
- **Understanding target:** Explain why a diagonal forward call contributes a phase factor $z_j$ and an inverse call contributes $z_j^{-1}$. Relate the resulting vector Laurent polynomial to separate positive and negative degree budgets, and explain why retaining measurement histories preserves pointwise normalization while conditioning on a selected outcome may destroy the polynomial premise.
- **Dependencies and story role:** Uses M02, M05, and M10. It translates resource accounting into the algebraic constraint used by the universal converse.
- **Conceptual connection:** A circuit's permitted operations restrict the functional dependence of its output on the unknown oracle, even when the circuit is adaptive.
- **Source pointers:** N&C §§4.4, 6.1.1, 6.7 for the circuit and black-box framework; the signed-degree representation is derived in [Poisson–Müntz bound §2](../science/poisson-muntz-bound.md#2-why-query-algorithms-satisfy-the-laurent-premise).

<a id="m12"></a>

### M12 — Random phases, averaging, and concentration

- **ID and phase:** M12 · Background/preliminaries.
- **Central question:** How can a distribution over phases define a hard physical input family?
- **Understanding target:** Explain how independent phases produce an average transition amplitude with a computable mean and variance, how a common random bias angle changes the ensemble, and how angular averaging removes unequal Fourier powers. Distinguish conditional independence from independence after averaging the common angle, and recognize why controlled oracle calls can make relative oracle phases observable.
- **Dependencies and story role:** Uses M06–M07 and M10–M11. It joins the statistical promise to the symmetries that will simplify the lower-bound polynomial.
- **Conceptual connection:** The same phase average has two roles: constructing physically valid oracle distributions and selecting the algebraic terms that survive in the converse.
- **Source pointers:** N&C §2.2.7 and Appendix 1; [Poisson–Müntz bound §§3, 5, 7](../science/poisson-muntz-bound.md#3-exact-complex-poisson-features); [Promise reductions §1](../science/promise-reductions.md#1-two-diagonal-oracle-ensembles).

<a id="m13"></a>

### M13 — Derivative control as a lower-bound tool

- **ID and phase:** M13 · Background/preliminaries.
- **Central question:** Why can limiting how fast a bounded function changes impose a minimum query budget?
- **Understanding target:** Explain the logic of a derivative bound: a function with bounded norm and restricted exponents cannot move far from its initial value over a short interval. Distinguish ordinary polynomials from the Müntz span of nonnegative real powers, and identify Newman's inequality as an imported analytic ingredient whose exponent conditions must be checked.
- **Dependencies and story role:** Uses M10–M12. It supplies the final mathematical tool before the prerequisites are integrated into a full proof plan.
- **Conceptual connection:** Resource-limited algebraic variation becomes a limit on the distinguishability that a physical algorithm can create.
- **Source pointers:** N&C §§6.6–6.7 provide the general lower-bound perspective but do not supply this inequality. The precise statement and application are in [Poisson–Müntz bound §5](../science/poisson-muntz-bound.md#5-the-phase-average-produces-a-müntz-polynomial); the primary imported theorem is [Borwein and Erdélyi, Theorem 1.1, attributing the bound to Newman](https://people.tamu.edu/~terdelyi/papers-online/positive.pdf).

<a id="m14"></a>

### M14 — The complete problem and its two proof obligations

- **ID and phase:** M14 · Background/preliminaries.
- **Central question:** What must be established to call a directional query frontier optimal?
- **Understanding target:** Assemble the known-state testing task, worst-case directional budgets, allowed controls and ancillas, and bounded-error criterion into one problem statement. Distinguish an algorithm that works for every completion from a lower bound covering every algorithm, and distinguish both query statements from gate, memory, and runtime claims. Identify why promise type and dimension remain part of the theorem.
- **Dependencies and story role:** Integrates M01–M13. It ends the background phase with the common framework required to follow both halves of the result.
- **Conceptual connection:** The constructive and converse branches address complementary quantifiers; neither alone establishes the full tradeoff.
- **Source pointers:** N&C §§3.2.1, 4.6, 6.6–6.7; [Model — The budget frontier](../science/model.md#the-budget-frontier), [Scientific route and proof dependencies](../science/model.md#scientific-route-and-proof-dependencies), and [Boundaries of the contribution](../science/model.md#boundaries-of-the-contribution).

## Phase II — Narrative/innovation

<a id="m15"></a>

### M15 — An inverse query supplies the unknown mode

- **ID and phase:** M15 · Narrative/innovation.
- **Central question:** What useful state can one inverse call prepare when the source and target are known?
- **Understanding target:** Derive the orthogonal component $|\xi\rangle=(U^\dagger|g\rangle-a^*|s\rangle)/\sqrt{1-p}$ after the complementary source outcome. Explain why a source outcome certifies the alternative under the exact-zero promise; for the gap task it is an acceptance event whose false-positive probability is controlled later. Account for one inverse query per attempted copy and explain why $p=1$ is handled before the expression for $\xi$ is needed.
- **Dependencies and story role:** Uses M01–M04 and the integrated model M14. It begins the construction with the local physical role of scarce inverse access.
- **Conceptual connection:** A measurement branch that would be called failed state preparation becomes a successful decision event in this testing task.
- **Source pointers:** N&C §§2.2.2–2.2.5 for the underlying operations; [Dicke probe §2](../science/dicke-probe.md#2-reverse-queries-prepare-an-unknown-input-mode).

<a id="m16"></a>

### M16 — Encoding unknown copies without knowing their basis

- **ID and phase:** M16 · Narrative/innovation.
- **Central question:** How can the supplied copies of $\xi$ become a pure Dicke probe without learning or cloning $\xi$?
- **Understanding target:** Explain the sequence of a known fixed-weight mask, mask-controlled permutations, routing-work uncomputation, and coherent source-vacuum label erasure. Identify why $\xi\perp s$ and exactly $R$ supplied copies suffice to erase the placement information deterministically.
- **Dependencies and story role:** Uses M04–M05, M08, and M15. It converts the inverse-prepared local resource into the collective input state.
- **Conceptual connection:** Known orthogonality supplies the label needed for coherent encoding even though the excited mode itself has no known classical description.
- **Source pointers:** N&C §§4.3, 4.5.1–4.5.3 for controlled-circuit foundations; [Dicke probe §3](../science/dicke-probe.md#3-deterministic-encoding-of-the-supplied-copies); [Implementation §3](../science/implementation.md#3-reversible-routing-with-clean-workspace).

<a id="m17"></a>

### M17 — Every unitary completion produces the same two-mode action

- **ID and phase:** M17 · Narrative/innovation.
- **Central question:** Why does the encoded probe reduce to a two-mode experiment for every compatible unknown unitary?
- **Understanding target:** Explain how unitarity gives $U|s\rangle=c|\eta\rangle+a|g\rangle$ and $U|\xi\rangle=-a^*|\eta\rangle+c|g\rangle$, with $c=\sqrt{1-p}$. Identify the unknown output mode $\eta\perp g$ and explain why measuring the known target needs no preparation or reflection about $\eta$.
- **Dependencies and story role:** Uses M02, M07–M08, and M15–M16. It establishes that the collective experiment is valid for every completion, closing the main oracle-access concern in the construction.
- **Conceptual connection:** The inverse-prepared mode and the forward transition are linked by unitarity into one exact $SU(2)$ action.
- **Source pointers:** N&C §§2.1.6, 2.2.2, 4.2; [Dicke probe §2](../science/dicke-probe.md#2-reverse-queries-prepare-an-unknown-input-mode) and [§4](../science/dicke-probe.md#4-the-complete-count-likelihood).

<a id="m18"></a>

### M18 — The observable count likelihood

- **ID and phase:** M18 · Narrative/innovation.
- **Central question:** What measurement distinguishes a nonzero transition, and what is its exact probability law?
- **Understanding target:** Connect the complete target-count distribution to a collective rotation of the fixed-weight input. Explain why the unknown phase of $a$ does not affect count probabilities, why the exact-zero null count is exactly $R$, and why the unconditional detection probability is $1-(1-p)^R A_{F,R}(p)^2$ rather than a probability conditioned on free preparation.
- **Dependencies and story role:** Uses M03, M06, M08, and M15–M17. It turns the prepared probe into a concrete decision experiment with fully charged outcomes.
- **Conceptual connection:** Symmetry reduces a large-register measurement to a structured count likelihood, while the preparation record remains part of the statistical experiment.
- **Source pointers:** N&C §§2.2.3, 2.2.7 for measurement and phase; [Dicke probe §4](../science/dicke-probe.md#4-the-complete-count-likelihood), especially [Return amplitude and the exact decision probability](../science/dicke-probe.md#return-amplitude-and-the-exact-decision-probability).

<a id="m19"></a>

### M19 — Uniform success from the collective moments

- **ID and phase:** M19 · Narrative/innovation.
- **Central question:** How does the count experiment become a guaranteed test for every $p\ge\varepsilon^2$?
- **Understanding target:** Explain the role of $\Lambda=F+2R(F-R)$ in the exact moments and how $M_4\le5M_2^2+2M_2$ yields a constant departure probability when $\Lambda\varepsilon^2\ge1$. Combine the $p\le1/2$ moment argument with the large-$`p`$ preparation event and constant repetition. Distinguish this global guarantee from the local Fisher-information identity.
- **Dependencies and story role:** Uses M09 and M18. It completes the statistical proof of a useful block rather than relying on its small-signal sensitivity alone.
- **Conceptual connection:** The product-like collective sensitivity becomes an operational advantage only when a uniform probability bound connects it to observable evidence.
- **Source pointers:** N&C Appendix 1 for the probability framework; [Dicke probe §§5–7](../science/dicke-probe.md#5-exact-second-and-fourth-moments).

<a id="m20"></a>

### M20 — Two implementations and their distinct costs

- **ID and phase:** M20 · Narrative/innovation.
- **Central question:** What ordinary resources are required to realize the query-efficient block?
- **Understanding target:** Explain why arithmetic mask preparation and reversible sorting give a full-register encoder with overhead nearly linear in $F$ up to logarithms, and why a reservoir can emit the same probe statistics with only $R+1$ live data registers but conservative $O(FR)$ routing work. Keep $C_s,C_g$, coherent workspace, precision, geometry, and oracle costs distinct, and avoid combining the best bounds of the two circuits.
- **Dependencies and story role:** Uses M05, M14, and M16–M19. It integrates the constructive branch into a complete ideal-circuit resource account.
- **Conceptual connection:** The same query experiment can have different gate–memory tradeoffs; query optimality alone does not determine physical runtime.
- **Source pointers:** N&C §§3.2.1, 4.3, 4.5.1–4.5.4 for resource and synthesis foundations; [Implementation §§1–4](../science/implementation.md#1-charged-known-state-operations), [§6](../science/implementation.md#6-streaming-resources-and-the-implementation-choice), and [§7](../science/implementation.md#7-precision-and-total-physical-cost).

<a id="m21"></a>

### M21 — An exact purification of the hard phase ensemble

- **ID and phase:** M21 · Narrative/innovation.
- **Central question:** How are random-oracle averages represented without losing normalization or complex-phase information?
- **Understanding target:** Explain how the Poisson law's signed Fourier moments define environment feature vectors with the Gram identity $\langle e_k(w)|e_h(w)\rangle=\mathbb E[z^{h-k}]$. Connect their tensor products to a purification of a general algorithm's averaged output, with norm one inherited from pointwise normalization of the Laurent output.
- **Dependencies and story role:** Uses M10–M12 and M14. It begins the converse with the local representation that makes the hard ensemble analytically tractable.
- **Conceptual connection:** Classical phase correlations become quantum environment overlaps, allowing an ensemble calculation to use normalized pure-state geometry.
- **Source pointers:** N&C §§2.4.1, 2.4.3, 2.5 for ensemble and purification foundations; [Poisson–Müntz bound §§2–3](../science/poisson-muntz-bound.md#2-why-query-algorithms-satisfy-the-laurent-premise).

<a id="m22"></a>

### M22 — Radial contraction and phase averaging

- **ID and phase:** M22 · Narrative/innovation.
- **Central question:** How do the two signed degree budgets collapse to one controlled radial function?
- **Understanding target:** Explain why the diagonal contraction replaces unequal feature weights by a common factor while keeping its norm bounded and its difference from the physical purification controlled. Then explain why averaging the common bias angle retains only equal positive and negative powers, leaving a real polynomial of degree at most $\min(F,R)$ multiplied by $(1-x)^{(F+R)/2}$.
- **Dependencies and story role:** Uses M11–M13 and M21. It reduces the general algorithm to the one-variable object on which the analytic inequality acts.
- **Conceptual connection:** The mixed resource scale comes from the interaction between total degree and the smaller directional budget after the physically specified phase average.
- **Source pointers:** N&C §2.2.7 for the distinction between global and relative phase; the specialized argument is in [Poisson–Müntz bound §§4–5](../science/poisson-muntz-bound.md#4-a-contraction-with-a-common-radial-weight) and its access qualification in [§7](../science/poisson-muntz-bound.md#7-phase-and-access-conventions).

<a id="m23"></a>

### M23 — From Newman's inequality to an ensemble converse

- **ID and phase:** M23 · Narrative/innovation.
- **Central question:** Why can an algorithm with small mixed budget not distinguish the biased and unbiased ensembles?
- **Understanding target:** Track how the nonnegative Müntz exponents and their sum enter Newman's derivative inequality, how integration bounds a purification overlap, and how returning to normalized physical states bounds trace distance. Interpret $D=O(r\sqrt{F+R+FR})$ for bias radius $r\le1/2$ and identify the common-angle average as part of the theorem.
- **Dependencies and story role:** Uses M10, M13, and M21–M22. It completes the analytic converse for a broad class of controlled and adaptive query algorithms.
- **Conceptual connection:** A norm-limited radial function constrains how far any resource-limited algorithm can separate two physical oracle ensembles.
- **Source pointers:** N&C §§9.2.1–9.2.3 for distances; [Poisson–Müntz bound §§5–7](../science/poisson-muntz-bound.md#5-the-phase-average-produces-a-müntz-polynomial); [primary theorem attribution](../references/related-work.md#newmans-derivative-inequality).

<a id="m24"></a>

### M24 — Turning ensemble indistinguishability into the gap lower bound

- **ID and phase:** M24 · Narrative/innovation.
- **Central question:** Why must an algorithm that solves every promised instance also distinguish the two random ensembles?
- **Understanding target:** Explain how the phase-average mean and variance place most null and alternative instances on the required sides of the magnitude gap. Keep the exceptional probabilities in the unconditioned acceptance averages, and connect the resulting constant acceptance gap to the ensemble bound. Identify $d\ge10^6\varepsilon^{-2}$ as the sufficient dimension regime of this reduction.
- **Dependencies and story role:** Uses M06, M10, M12, and M23. It converts the abstract ensemble converse into an operational testing lower bound.
- **Conceptual connection:** Worst-case correctness forces average-case separation whenever the hard distributions fall mostly inside the promise sets.
- **Source pointers:** N&C Appendix 1 and §9.2.1; [Promise reductions §§1–2](../science/promise-reductions.md#1-two-diagonal-oracle-ensembles).

<a id="m25"></a>

### M25 — Repairing the null to an exactly zero overlap

- **ID and phase:** M25 · Narrative/innovation.
- **Central question:** How can a lower bound for a small random overlap become a lower bound for an exact-zero promise?
- **Understanding target:** Explain the two-dimensional output rotation that produces a nearby oracle $\widetilde U$ with exactly zero transition amplitude, and the query-by-query hybrid bound controlling the change in algorithm output. Identify why this correction defines hard inputs rather than a free algorithmic operation, and why its average cost leads to the separate sufficient regime $d\ge16\varepsilon^{-4}$.
- **Dependencies and story role:** Uses M02, M07, M10, and M23–M24. It supplies the additional argument needed for the project's exact-zero theorem.
- **Conceptual connection:** Geometric control of one matrix element and continuity of query circuits bridge the gap between approximate and exact promise sets.
- **Source pointers:** N&C §§2.2.2, 4.5.1, 9.2.1–9.2.3 for geometric and distance foundations; [Promise reductions §§3–4](../science/promise-reductions.md#3-correcting-one-matrix-element-to-exactly-zero).

<a id="m26"></a>

### M26 — Which reductions preserve the oracle task?

- **ID and phase:** M26 · Narrative/innovation.
- **Central question:** Which changes of source, target, or observable inherit the proved budget law?
- **Understanding target:** Explain how known basis changes transfer the overlap lower bounds to any fixed known source and target without changing directional query counts. Derive the maximally entangled identity $\langle\Phi_d|(I\otimes U)|\Phi_d\rangle=\mathrm{tr}(U)/d$, distinguish the oracle dimension $d$ from the probe dimension $d^2$, and identify why the trace lower bound is proved for the gap promise but the exact-zero overlap repair does not establish an exact-zero trace converse.
- **Dependencies and story role:** Uses M04, M10, and M19, M24–M25. It closes the converse branch by stating exactly which operational consequences survive the reductions.
- **Conceptual connection:** A reduction transfers a theorem only when it preserves the promised input class, access model, and counted resources in the required direction.
- **Source pointers:** N&C §§1.3.6, 2.1.7, 2.2.8, 2.5 for entangled-state foundations; [Promise reductions §§5–6](../science/promise-reductions.md#5-arbitrary-known-source-and-target-states).

<a id="m27"></a>

### M27 — Fitting useful blocks into arbitrary budgets

- **ID and phase:** M27 · Narrative/innovation.
- **Central question:** How does one successful probe block yield a theorem for every sufficiently large available budget pair?
- **Understanding target:** Explain direction exchange when inverse calls are more plentiful, sampling when the minority budget is small, and the division of both budgets among repeated blocks. Understand why a first-crossing choice with $\varepsilon^{-2}\le\Lambda<3\varepsilon^{-2}$ controls the gap-null acceptance while retaining alternative detection, and why unused budget need not be spent.
- **Dependencies and story role:** Uses M06, M14, and M18–M20. It integrates the constructive blocks into the same directional-budget variables used by the converse.
- **Conceptual connection:** Local probe performance becomes a uniform resource theorem only after rounding, repetition, and promise-aware tuning fit within the original budgets.
- **Source pointers:** N&C Appendix 1 and §3.2.1 for probability and resource foundations; [Resource frontier §§1–3](../science/resource-frontier.md#1-the-block-guarantee); [Dicke probe — Global acceptance bound](../science/dicke-probe.md#a-global-bound-on-acceptance-at-small-overlap).

<a id="m28"></a>

### M28 — The matching forward/inverse frontier

- **ID and phase:** M28 · Narrative/innovation.
- **Central question:** What does $F+R+FR=\Theta(\varepsilon^{-2})$ establish, including its endpoints and qualifications?
- **Understanding target:** Combine the available-budget upper theorem with the promise-specific lower bounds into a necessary-and-sufficient scaling statement up to universal constants. Explain the sampling endpoints, the balanced reversible regime, and the product regime between them. Retain the all-dimension upper guarantee and the distinct sufficient dimension assumptions for exact-zero and gap converses.
- **Dependencies and story role:** Integrates M19–M27. It is the first complete synthesis of the constructive and impossibility arguments.
- **Conceptual connection:** The physical cooperation between inverse-prepared excitations and forward probes matches the maximum distinguishability permitted by their signed degree budgets.
- **Source pointers:** N&C §§3.2.1, 6.6–6.7 for the meaning of complexity bounds; [Model — The budget frontier](../science/model.md#the-budget-frontier); [Resource frontier §4](../science/resource-frontier.md#4-matching-converse-and-interpretation).

<a id="m29"></a>

### M29 — Pricing scarce inverse access

- **ID and phase:** M29 · Narrative/innovation.
- **Central question:** How does the optimal strategy change when an inverse call costs $\kappa\ge1$ forward-call units?
- **Understanding target:** Explain the optimization of $F+\kappa R$ subject to the proved frontier and the resulting scale $`\Theta(\min\{\varepsilon^{-2},\sqrt\kappa/\varepsilon\})`$ in the applicable dimension regime. Interpret the crossover to ordinary sampling and distinguish weighted query optimality from a runtime claim that would also need the full encoding, storage, and readout costs.
- **Dependencies and story role:** Uses M20 and M28. It translates the abstract frontier into an operational exchange rate under a specified cost model.
- **Conceptual connection:** A directional lower bound supports a meaningful resource-price optimization because it rules out all alternative algorithms in the same model.
- **Source pointers:** N&C §3.2.1 for resource accounting; [Resource frontier §§5–6](../science/resource-frontier.md#5-when-reversal-costs-more); [Implementation §7](../science/implementation.md#7-precision-and-total-physical-cost).

<a id="m30"></a>

### M30 — The contribution as a whole and its boundary

- **ID and phase:** M30 · Narrative/innovation.
- **Central question:** What has the complete argument added to existing quantum algorithms and metrology, and where does its reasoning stop?
- **Understanding target:** Explain the combined contribution of a valid unknown-mode construction and a matching worst-case mixed-budget converse. Distinguish it from the inherited reversible/forward-only endpoint results, Dicke metrology, preparation primitives, and Newman's inequality. State the proved overlap and trace-gap tasks while recognizing that a global estimation upper algorithm, unknown-subspace amplification, exact-zero trace optimality, optimized low-dimension behavior, noise tolerance, and hardware runtime advantage require additional arguments. Distinguish the stated estimation lower-bound corollary from an estimation upper theorem.
- **Dependencies and story role:** Integrates M14 and M20–M29. It closes the narrative with the result's mechanism, optimality, interpretation, attribution, and limits in one account.
- **Conceptual connection:** The scientific significance comes from joining a lawful resource conversion to a converse with matching quantifiers; its scope is fixed by the promises and model that both proofs actually cover.
- **Source pointers:** [Model — Boundaries of the contribution](../science/model.md#boundaries-of-the-contribution); [Related work](../references/related-work.md); [Promise reductions §7](../science/promise-reductions.md#7-an-additive-accuracy-lower-bound-corollary); [Dicke probe §7](../science/dicke-probe.md#7-local-information-and-scope); [Resource frontier §§4–6](../science/resource-frontier.md#4-matching-converse-and-interpretation). N&C supplies the foundations identified above; these contribution and scope judgments depend on the project's research-level statements and comparisons.
