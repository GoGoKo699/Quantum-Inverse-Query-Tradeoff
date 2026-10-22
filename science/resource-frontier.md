# From a probe to the complete resource frontier

The [Dicke probe](dicke-probe.md) supplies a block with a sensitivity scale
containing a product of forward and inverse calls. This page proves that
the block covers arbitrary available budget pairs, handles both sampling
endpoints, and derives the cost of expensive reversal.

The model, promises, and theorem statements are in [Model and results](model.md).
All constants below are universal and deliberately unoptimized.

## 1. The block guarantee

For integers $f\ge1$ and $0\le r\le f/2$, let

```math
\Lambda(f,r)=f+2r(f-r).
```

A block uses at most $f$ forward and $r$ inverse calls. It accepts a nonzero
transition when an inverse preparation projects onto the source, or when the
final target count differs from $r$. With $p=|\langle g|U|s\rangle|^2$,
the [probe proof](dicke-probe.md) establishes:

```math
\begin{aligned}
p=0 &\quad\Longrightarrow\quad P_{\rm det}(p)=0,\\
p\ge\varepsilon^2,\ \Lambda(f,r)\varepsilon^2\ge1
&\quad\Longrightarrow\quad P_{\rm det}(p)\ge\frac19,\\
0\le p\le1 &\quad\Longrightarrow\quad
P_{\rm det}(p)\le
\left(r+\frac{\pi^2}{4}\Lambda(f,r)\right)p
\le K\Lambda(f,r)p,
\end{aligned}
```

where $K=1+\pi^2/4<3.468$. For $r=0$, the block is simply $f$
independent source-to-target trials, with
$P_{\rm det}=1-(1-p)^f$; the displayed inequalities remain valid.

The alternative guarantee is uniform, including large transition
probabilities. It does not assume that the local small-$`p`$ expansion remains
accurate away from zero.

## 2. Tuning a block without overshooting the gap

Let $T=\varepsilon^{-2}\ge16$. Suppose an available block
$(f,k)$, $0\le k\le f/2$, satisfies $\Lambda(f,k)\ge T$.
There is a sub-block $(u,v)$ using no more resources in either direction
such that

```math
T\le\Lambda(u,v)<3T.
```

To see this, first increase $(u,v)$ along
$(1,0),(2,0),\ldots,(f,0)$, and then along
$(f,1),\ldots,(f,k)$. The sensitivity increases throughout.
Along the first part it increases by one. Along the second part,

```math
\Lambda(f,v+1)-\Lambda(f,v)=2(f-2v-1)\le2f
\le2\Lambda(f,v).
```

Every step therefore increases $\Lambda$ by at most a factor of three.
The first crossing of $T$, starting from $1<T$, has the required bound.
Equivalently, if $f\ge T$, take $(u,v)=(\lceil T\rceil,0)$;
otherwise take $u=f$ and the smallest $v\le k$ that crosses $T$.

Run 20 independent copies of this tuned block and accept if any accepts.
For the alternative, its miss probability is at most

```math
\left(\frac89\right)^{20}<0.095.
```

For the magnitude-gap null, $p\le\varepsilon^2/10^4$, the union bound gives

```math
P_{\rm false\ positive}\le
20K(3T)\frac{\varepsilon^2}{10^4}
=\frac{60K}{10^4}<0.021.
```

For the exact-zero null this probability is zero in the ideal circuit.
Thus both promises have a substantial margin beyond success $2/3$.
An overall implementation trace-distance error at most $1/100$ changes
any decision probability by at most $1/100$, preserving that margin.

## 3. Allocating arbitrary directional budgets

Let $F,R$ be the available budgets and set

```math
q=\max(F,R),\qquad r=\min(F,R),\qquad B=q+r+qr.
```

Assume $B\ge10^5T$. If the more abundant direction is $U^\dagger$,
apply the construction to $V=U^\dagger$, with source $g$ and target $s$.
Its amplitude is $a^*$, so the testing promise is unchanged. This exchanges
the two directional costs without requiring an additional oracle.

### A small minority budget

If $r<40$, then

```math
B=q(r+1)+r\le q(r+2)\le41q.
```

Consequently $q\ge10^5T/41$, more than enough for
$N=\lceil2T\rceil$ ordinary trials in the abundant direction.
Under the alternative their miss probability is at most $e^{-2}$.
Under the gap null their false-positive probability is at most

```math
N\frac{\varepsilon^2}{10^4}
\le\frac{2+1/16}{10^4}<0.001.
```

This includes both one-direction endpoints. The minority budget need not be
spent merely because it is available.

### Both budgets at least 40

Set

```math
f=\left\lfloor\frac q{20}\right\rfloor,\qquad
k=\min\left\{
\left\lfloor\frac r{20}\right\rfloor,\
\left\lfloor\frac f2\right\rfloor
\right\}.
```

Then $f\ge q/40$ and $f\ge2$. Also
$\lfloor r/20\rfloor\ge r/40$ and
$\lfloor f/2\rfloor\ge f/3\ge q/120\ge r/120$;
hence $k\ge r/120$. Since $k\le f/2$,

```math
\Lambda(f,k)\ge fk\ge\frac{qr}{4800}
\ge\frac{B}{14400}>T.
```

The last non-strict inequality uses $q+r+qr\le3qr$ for positive
integer budgets. Tune this block as in Section 2, and repeat it 20 times.
The total calls obey $20f\le q$ and $20k\le r$, so the entire algorithm
fits the original budgets. The resulting success bounds prove the uniform
upper statements of [Theorems 1–2](model.md#the-budget-frontier).

The constant $10^5$ makes the quantifier “every sufficiently large budget
pair” explicit. It is not an estimate of a practically necessary constant.

## 4. Matching converse and interpretation

The [Poisson–Müntz bound](poisson-muntz-bound.md) and
[promise reductions](promise-reductions.md) establish the necessity of

```math
F+R+FR\ge\frac{\varepsilon^{-2}}{4096}
```

in the respective dimension regimes. Combined with the construction, this
gives the following scaling picture.

| Available inverse budget | Forward scale sufficient and necessary up to constants |
|---|---|
| $R=0$ | $F=\Theta(\varepsilon^{-2})$ |
| $1\lesssim R\lesssim\varepsilon^{-1}$ | $F=\Theta(\varepsilon^{-2}/(R+1))$ |
| $F$ and $R$ of the same order | $F,R=\Theta(\varepsilon^{-1})$ |
| $F=0$ | $R=\Theta(\varepsilon^{-2})$, by the reversed testing problem |

The middle row describes the boundary with $R$ fixed in the displayed
range and leaves the same universal constant freedom as the theorem. Near
the inverse-only endpoint it is clearer to use the full expression
$F+R+FR$, or exchange the direction labels.

The product term has an operational origin: inverse preparations supply
unknown excitations that can cooperate with many forward probes. It cannot
be inferred merely by treating a Grover iteration as one query, because a
Grover iteration already spends calls in both directions. The known
collective-spin sensitivity is attributed in
[Related work](../references/related-work.md).

## 5. When reversal costs more

Suppose a forward call costs one unit and an inverse call costs
$\kappa\ge1$ units. Define the weighted query cost

```math
C_\kappa=F+\kappa R.
```

In a dimension regime where the matching lower bound holds, optimizing this
cost gives

```math
C_{\kappa,\mathrm{opt}}
=\Theta\!\left(
\min\left\{\varepsilon^{-2},
\frac{\sqrt\kappa}{\varepsilon}\right\}
\right).
```

**Lower bound.** For any nonnegative budgets,

```math
F+R+FR\le C_\kappa+\frac{C_\kappa^2}{4\kappa}.
```

The first term uses $\kappa\ge1$; the second follows by maximizing
$F(\kappa R)$ at fixed $F+\kappa R$.
With $c=1/4096$, necessity of $B\ge cT$ implies

```math
C_\kappa\ge
2\kappa\left(\sqrt{1+\frac{cT}{\kappa}}-1\right)
=\Omega\!\left(\min\{T,\sqrt{\kappa T}\}\right).
```

**Upper bound.** If $1\le\kappa\le T$, choose budgets proportional to

```math
F\asymp\sqrt{\kappa T},\qquad
R\asymp\sqrt{\frac T\kappa}.
```

For a completely explicit use of the preceding theorem, take 320 times
the ceiling of each quantity. Their product is at least $102400T$,
and their weighted cost is $O(\sqrt{\kappa T})$. The rounding cost
remains of this order because $1\le\kappa\le T$. If $\kappa>T$,
use $\lceil2T\rceil$ forward trials and no inverse calls.

Thus inverse access is useful in the query-cost model while its price is
below order $\varepsilon^{-2}$. Within that range the optimal cost
increases as $\sqrt\kappa$. The theorem gives a scaling crossover,
not a sharp constant-price threshold.

## 6. From queries to implementation

The result above weights oracle calls only. Its physical interpretation
requires the known-state circuits, coherent memory, routing, and readout
in [Implementation](implementation.md).

For $n=\lceil\log_2 d\rceil$, the full-register construction keeps $f$
data registers and has known-gate overhead nearly linear in $f$, up to
logarithms and the known-state circuit costs. The streaming construction
keeps $r+1$ live data registers but uses a conservative $O(fr)$ number
of routing operations. These are distinct implementations. Their best
individual gate and memory bounds cannot be combined into a single
unproved resource estimate.

A system in which long coherent storage, distant controlled swaps, or precise
inverse implementation is costly may have a different elapsed-time optimum.
The query law identifies the best possible directional exchange rate in the
specified oracle model; a hardware comparison must price its other resources.
