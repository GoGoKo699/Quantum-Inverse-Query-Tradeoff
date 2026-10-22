# Implementation and complete resource accounting

The [Dicke-probe test](dicke-probe.md) uses $R$ inverse calls to supply an unknown mode and $F$ forward calls to probe it collectively. This page specifies two implementations of its oracle-independent encoder. The full-register implementation stores all $F$ data registers and has gate overhead nearly linear in $F$, up to logarithms. The streaming implementation stores $R+1$ data registers and has a conservative $O(FR)$ routing overhead. These are separate resource options.

Throughout, $1\le R\le F$, $n=\lceil\log_2 d\rceil$, and $\delta$ denotes the allowed encoding error in trace distance. An arbitrary $d$-dimensional register can be embedded in $n$ qubits; known circuits preserve the intended subspace. All-to-all known-gate connectivity is assumed for the displayed circuit counts. Architecture-specific movement and connectivity costs must be added for a particular device.

## 1. Charged known-state operations

Let known circuits $S$ and $G$ satisfy

```math
S|0^n\rangle=|s\rangle,\qquad G|0^n\rangle=|g\rangle.
```

Let $C_s$ bound the elementary-gate cost of a source preparation or unpreparation and of one coherent source-projector test, and define $C_g$ similarly. These costs can be obtained from the preparation circuits: conjugate an all-zero test by $S$ or $G$. With clean reusable workspace, an all-zero test costs $O(n)$ known gates, so a convention such as $C_s=O(\mathrm{cost}(S)+n)$ and $C_g=O(\mathrm{cost}(G)+n)$ suffices.

For example, the coherent source test is

```math
L_s=\Pi_s\otimes I+(I-\Pi_s)\otimes X,
\qquad \Pi_s=|s\rangle\langle s|.
```

Measuring its flag realizes the nondestructive two-outcome projection used in reverse preparation. Keeping its flag coherent labels a register as vacuum or nonvacuum. A phase on the known nonvacuum subspace is implemented by the same basis change and a controlled phase. None of these operations requires knowing the orthogonal vector $\xi$.

Each inverse-preparation attempt prepares $g$, applies $U^\dagger$, and tests $\Pi_s$. The test accepts and stops if the source outcome occurs. Thus a run uses at most $R$ inverse calls; on the branch that continues, those calls have supplied exactly $R$ copies of

```math
|\xi\rangle=\frac{U^\dagger|g\rangle-a^*|s\rangle}{\sqrt{1-|a|^2}},
\qquad \xi\perp s.
```

The other $F-R$ data registers are prepared in $s$. Final readout uses $F$ known target-projector tests. Across preparation, encoding labels, and readout, these known-state operations cost $O(F(C_s+C_g))$ gates. Their reusable internal workspace must also be counted; denote a sufficient bound by $W_{\mathrm{known}}$ qubits. Internal workspace required by a physical implementation of $U$ or $U^\dagger$ is an additional resource of those oracles.

## 2. Preparing the known occupation mask

The full-register encoder starts with the known state

```math
|D_F^R\rangle_B
=\binom FR^{-1/2}\sum_{|b|=R}|b\rangle.
```

This mask concerns ordinary qubits. It contains no classical description of $\xi$. A sequential construction keeps a binary counter $r$ for the number of ones still to be placed. Initially $r=R$. With $\ell$ unfilled positions left, use the conditional rotation

```math
|r\rangle|0\rangle
\longmapsto
|r\rangle\left(
\sqrt{\frac{\ell-r}{\ell}}|0\rangle
+\sqrt{\frac r\ell}|1\rangle
\right),
```

then decrement $r$ if the emitted bit is one. The cases $r=0$ and $r=\ell$ are deterministic and can be implemented exactly. In the other cases, compute the rotation angle reversibly from $r,\ell$, apply the rotation, and uncompute the angle workspace **before** changing $r$.

For a length-$`F`$ bit string of weight $R$, multiplying the squared conditional amplitudes gives

```math
\frac{R!\,(F-R)!}{F!}=\binom FR^{-1}.
```

All amplitudes are positive. At the end $r=0$ in every branch, so the counter disentangles and the mask is the required pure state.

The conditional-probability method is an established preparation primitive: [Kaye and Mosca, *Quantum Networks for Generating Arbitrary Quantum States*, Sections 2–4](https://arxiv.org/pdf/quant-ph/0407102), give reversible arithmetic preparation and specialize it to symmetric states. [Aktar et al., *A Divide-and-Conquer Approach to Dicke State Preparation*, Table 1](https://arxiv.org/pdf/2112.12435v2), records its $O(F\mathrm{polylog}(F/\delta))$ gate bound.

To obtain total error at most $\delta$, it suffices to approximate each of the $F$ conditional rotations to operator-norm error $O(\delta/F)$. Reversible division, square root, and angle evaluation at $b=O(\log(F/\delta))$ bits of precision have polynomial cost in $b$. The telescoping bound on a product of unitaries then gives $O(\delta)$ total state error. A conservative resource bound is

```math
O\!\left(F\mathrm{poly}(\log(F/\delta))\right)
\quad\text{gates},\qquad
\mathrm{poly}(\log(F/\delta))
\quad\text{reusable arithmetic qubits}.
```

The conditional probabilities and angles are computed by circuits. There is no QRAM lookup or uncharged table of amplitudes.

## 3. Reversible routing with clean workspace

Initially put the $R$ supplied $\xi$ registers first and the $F-R$ vacuum registers afterward:

```math
|\chi_0\rangle_D=|\xi\rangle^{\otimes R}|s\rangle^{\otimes(F-R)}.
```

For each mask $b$, the encoder must move these data into the corresponding occupation pattern and erase every register recording the permutation. A fixed sorting network provides an explicit procedure.

### 3.1 Compute a permutation while leaving the mask untouched

Create workspace records

```math
K_j=(1-b_j,j),\qquad j=1,\ldots,F.
```

The mask is used only as a control during this computation. Sort the records lexicographically with a fixed network, recording one comparison bit for every comparator. The index $j$ breaks ties and makes the records distinct. The sorted list begins with the original positions of the $R$ one bits, followed by the original positions of the zero bits.

A reversible comparator first computes whether a swap is needed into a clean bit and then conditionally swaps the two records. All these bits are retained. Denote the resulting sorted records and comparison bits by $W(b)$.

Use, for example, a [Batcher sorting network](https://doi.org/10.1145/1468075.1468121) with $O(F\log^2F)$ comparators. A non-power-of-two length can be padded to fewer than $2F$ wires using fixed sentinel records and vacuum data. Padding changes only constants. The extra data registers end in the known vacuum and receive no oracle queries; only the original $F$ slots are probed and measured. Reversible sorting networks are also an established quantum primitive; see [Liu, Childs and Gottesman, *Low-depth quantum symmetrization*, Section II](https://arxiv.org/pdf/2411.04019v2).

### 3.2 Reverse-route the data

Starting with $\chi_0$ in sorted order, traverse the comparison bits in the reverse network order. For each bit, perform the corresponding controlled swap on the two **data** registers. This applies the inverse of the permutation that sorted the records. The $R$ initial excitations are therefore placed in the original one positions of $b$.

After this step the joint state is

```math
\binom FR^{-1/2}\sum_{|b|=R}
|b\rangle_B|W(b)\rangle_W|\chi(b)\rangle_D.
```

Each data swap consists of $n$ controlled qubit swaps. The permutation acts on the supplied unknown states themselves and is valid for every normalized $\xi\perp s$.

### 3.3 Uncompute comparisons and records from the retained mask

Apply the inverse of the entire record-computation and sorting circuit to $B,W$, acting only on those registers. For each comparator in reverse order, its retained bit first unswaps the workspace records; the comparison is then recomputed from those restored records and XORed into the retained bit, clearing it. Finally, erase the original records $K_j=(1-b_j,j)$ using the still untouched mask and the known indices.

This restores $W$ to zero while preserving the routed data:

```math
\binom FR^{-1/2}\sum_{|b|=R}
|b\rangle_B|0\rangle_W|\chi(b)\rangle_D.
```

The order matters: the comparison controls are used to reverse-route the data before they are erased, and the inverse workspace circuit has no action on the data registers.

### 3.4 Erase the mask using the known vacuum test

Apply $L_s$ to data slot $j$ and mask bit $B_j$ for all $j$. The nonvacuum label of $|\chi(b)\rangle$ is exactly $b$, so the mask becomes $0^F$. The final joint state is

```math
|0^F\rangle_B|0\rangle_W|D_F^R(\xi,s)\rangle_D.
```

Every coherent record of the placement has been removed. This is a deterministic encoder on the promised input copies, with approximate accuracy only where finite-precision known rotations are explicitly used.

## 4. Full-register gate and memory bounds

Each comparator operates on $O(\log F)$ record bits. Computing and uncomputing the records costs $O(F\log^3F)$ known gates, and routing the data costs $O(Fn\log^2F)$. Their combined bound is

```math
O\!\left(F\log^2F\,(n+\log F)\right).
```

There are $F$ mask qubits, $O(F\log F)$ record bits, and $O(F\log^2F)$ retained comparison bits. Adding arithmetic workspace and the data registers gives the per-run bounds

```math
\boxed{\displaystyle
G_{\mathrm{full}}
=O\!\left(
F\mathrm{poly}(\log(F/\delta))
+F\log^2F\,(n+\log F)
+F(C_s+C_g)
\right),
}
```

```math
\boxed{\displaystyle
Q_{\mathrm{full}}
=O\!\left(
Fn+F\log^2F+\mathrm{poly}(\log(F/\delta))
\right)+W_{\mathrm{known}}.
}
```

Here logarithmic factors may be read as at least one for small $F$. The $R$ inverse-prepared copies are included among the $F$ data registers. A simpler quadratic-size sorting or selection circuit also gives a polynomial encoder; it is unnecessary for the stronger bound displayed above.

The oracle calls can be sequential. Simultaneous access to $F$ oracle devices is not assumed, although the full-register implementation does retain all $F$ probe registers coherently until they are processed. The count can be accumulated classically with $O(\log F)$ bits and $O(F\log F)$ bit operations after the individual measurements. A reversible counter is also possible and is absorbed by the displayed logarithmic overhead.

## 5. A streaming encoder with $R+1$ live data registers

The full Dicke state can instead be emitted one slot at a time. Keep $R$ reservoir registers, a counter $k$, and one output register initialized in $s$. With $\ell$ outputs remaining, the reservoir invariant is support on

```math
|k\rangle_K|\xi\rangle^{\otimes k}|s\rangle^{\otimes(R-k)},
\qquad 0\le k\le\min(R,\ell).
```

The reservoir and counter may be entangled with previously emitted outputs. Initially $k=R$ and $\ell=F$. The desired emission map is

```math
\begin{aligned}
&|k\rangle|\xi\rangle^{\otimes k}|s\rangle^{\otimes(R-k)}|s\rangle_{\mathrm{out}}\\
\longmapsto{}&
\sqrt{\frac{\ell-k}{\ell}}
|k\rangle|\xi\rangle^{\otimes k}|s\rangle^{\otimes(R-k)}|s\rangle_{\mathrm{out}}\\
&+\sqrt{\frac k\ell}
|k-1\rangle|\xi\rangle^{\otimes(k-1)}|s\rangle^{\otimes(R-k+1)}|\xi\rangle_{\mathrm{out}}.
\end{aligned}
```

The second term is omitted for $k=0$. Repeating for $\ell=F,F-1,\ldots,1$ assigns squared amplitude $R!(F-R)!/F!$ to each weight-$`R`$ output pattern. The counter ends at zero and every reservoir slot ends in $s$, so the reservoir disentangles. With the outputs retained, this is precisely $|D_F^R(\xi,s)\rangle$.

### 5.1 Implementing one emission

For each $j=1,\ldots,R$, coherently test $k=j$. Under that equality control, apply

```math
e^{i\theta_{j,\ell}\mathrm{SWAP}}
\quad\text{to reservoir slot }j\text{ and the output},
\qquad
\sin\theta_{j,\ell}=\sqrt{j/\ell},
```

for valid $j\le\ell$; impossible counter values need no specified nontrivial action. Keep $k$ unchanged throughout this selection loop and erase each equality-control work bit before changing it. Only the operation with $j=k$ acts nontrivially on any branch.

For $k=j\ge1$, the selected reservoir slot is $\xi$, and

```math
e^{i\theta\mathrm{SWAP}}|\xi\rangle|s\rangle
=\cos\theta|\xi\rangle|s\rangle
+i\sin\theta|s\rangle|\xi\rangle.
```

Apply $\Pi_s-i(I-\Pi_s)$ to the output to make both coefficients real and positive. Compute the output's nonvacuum flag, decrement $k$ under that flag, and uncompute the flag from the unchanged output register. In the excitation branch, reservoir slot $j=k$ has become $s$ and the counter has decreased to $k-1$; in the vacuum branch neither changes. This proves the reservoir invariant and implements the displayed emission map.

The boundary $k=\ell$ emits an excitation deterministically and can be implemented by an exact swap with the appropriate phase correction. The boundary $k=0$ emits a vacuum. No measurement in an unknown basis is used.

### 5.2 Register-SWAP exponentials

The exponential of an entire-register SWAP is a known operation. Since $\mathrm{SWAP}$ has eigenvalues $\pm1$, an ancilla initialized to zero can coherently record the eigenvalue using a Hadamard, a controlled register-SWAP, and another Hadamard. Apply the phase $e^{i\theta}$ for eigenvalue $+1$ and $e^{-i\theta}$ for eigenvalue $-1$, then reverse the extraction circuit.

This realizes $e^{i\theta\mathrm{SWAP}}$ and clears the ancilla. It requires two controlled register-SWAP networks, or $O(n)$ controlled qubit swaps, plus a one-qubit phase and its control. The counter equality test and rotation precision add logarithmic or polynomial-logarithmic overhead. Looping over all $R$ possible reservoir slots is an explicit implementation of the selection; no random-access memory assumption is needed.

### 5.3 Querying and measuring emitted registers

Immediately after emitting a register, apply $U$, measure the known projector $\Pi_g$, and update a classical count. Every later emission acts only on the reservoir, counter, and fresh output registers. Those later operations commute with a query and measurement on a previously emitted register, so performing that readout early gives the same joint count distribution as retaining all outputs and reading them at the end.

The measured output register can then be discarded or reset and reused. This produces the same test and likelihood as the full-register implementation while keeping only $R+1$ live data registers. It still uses at most $R$ inverse preparations and $F$ forward probes, with early preparation acceptance already charged.

## 6. Streaming resources and the implementation choice

For total encoding error $\delta$, allocate precision conservatively across the $O(FR)$ selected-slot operations. The explicit loop above gives

```math
\boxed{\displaystyle
G_{\mathrm{stream}}
=O\!\left(
FR\,[n+\mathrm{poly}(\log(FR/\delta))]
+F(C_s+C_g)
\right),
}
```

```math
\boxed{\displaystyle
Q_{\mathrm{stream}}
=O\!\left(
(R+1)n+\log(R+1)
+\mathrm{poly}(\log(FR/\delta))
\right)+W_{\mathrm{known}}.
}
```

The additive known-state term includes source preparation for fresh outputs, the nonvacuum phase and flags, and target readout. A classical count uses another $O(\log F)$ bits.

| Resource per run | Full-register encoder | Streaming encoder |
|---|---|---|
| Forward and inverse oracle calls | At most $F$ and $R$ | At most $F$ and $R$ |
| Live data qubits | $Fn$ without padding; fewer than $2Fn$ with the stated padded network | $(R+1)n$ |
| Known routing work | $`O(F\log^2F\,(n+\log F))`$ | Conservative $`O(FR\,[n+\mathrm{polylog}(FR/\delta)])`$ including rotation work |
| Other preparation and readout | $O(F\mathrm{polylog}(F/\delta)+F(C_s+C_g))$ | $O(F(C_s+C_g))$ beyond the displayed emission work |
| Coherent control workspace | $O(F\log^2F+\mathrm{polylog}(F/\delta))$ | $O(\log(R+1)+\mathrm{polylog}(FR/\delta))$ |

The full-register gate bound and the streaming memory bound refer to different circuits. The construction above does not establish both bounds simultaneously. The reservoir loop is a conservative implementation; a smaller streaming routing cost would require an additional algorithm.

## 7. Precision and total physical cost

The ideal-query theorem assumes exact known operations. If the prepared probe differs from the ideal probe by trace distance at most $\delta$, subsequent ideal oracle calls and measurements cannot increase that distance, and every event probability changes by at most $\delta$.

For the 20-block test in [Resource frontier](resource-frontier.md#2-tuning-a-block-without-overshooting-the-gap), allocate at most $1/2000$ error to each complete block. A hybrid bound gives at most $20/2000=1/100$ change in any final decision probability. The ideal alternative miss probability is below $0.095$ and the gap-null acceptance probability is below $0.021$, so this total error preserves success greater than $2/3$ on both promises. When known preparation or measurement instruments are also approximated, their errors must be included in this complete-block budget; a lower bound on alternative acceptance alone would not control false positives.

If only the interior mask rotations are approximated while deterministic boundary transitions, routing, and source/target tests are exact, the mask remains supported on weight $R$. In that implementation the exact-zero null still produces count $R$ with certainty. More general errors in the known-state projectors can also create false positives and should be included in the chosen total error budget.

If a forward oracle costs $C_U$ and an inverse oracle costs $C_{U^\dagger}$, the per-run gate-weighted accounting is

```math
F C_U+R C_{U^\dagger}+G_{\mathrm{full}}
\quad\text{or}\quad
F C_U+R C_{U^\dagger}+G_{\mathrm{stream}},
```

with the corresponding coherent storage, hardware routing, and oracle-internal workspaces. The [weighted query frontier](resource-frontier.md) optimizes the first two terms. Whether that query saving yields a lower physical runtime depends on their size relative to the stated encoding, readout, and memory costs. No noise-tolerance or architecture-independent runtime advantage follows from the query law alone.
