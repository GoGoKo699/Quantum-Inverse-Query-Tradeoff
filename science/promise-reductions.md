# From the ensemble bound to overlap and trace promises

Let $U$ be an unknown unitary on a $d$-dimensional register, and let $|s\rangle,|g\rangle$ be fixed known normalized states. Write

```math
a(U)=\langle g|U|s\rangle,\qquad
B=F+R+FR,\qquad M=F+R.
```

Here $F,R$ are nonnegative integer bounds on the **total** numbers of forward and inverse queries on every run. They may depend on $d$ and the promised threshold. The lower bounds allow coherent controls, arbitrary ancillas, intermediate measurements, adaptation, and early stopping under the conventions in [Model](model.md).

A test is required to be correct with probability at least $2/3$ for **each** unitary satisfying either side of its promise. No condition is imposed on its answer in the interval between the two sides of a gap promise. The threshold $\varepsilon$ below is an amplitude threshold; the corresponding transition-probability threshold is $\varepsilon^2$.

The three operational consequences proved on this page are:

| Task | Promise | Sufficient dimension for the lower bound |
|---|---|---|
| Exact-zero rank-one overlap | $a=0$ versus $\lvert a\rvert\ge\varepsilon$ | $d\ge16\varepsilon^{-4}$ |
| Tolerant rank-one overlap | $\lvert a\rvert\le\varepsilon/100$ versus $\lvert a\rvert\ge\varepsilon$ | $d\ge10^6\varepsilon^{-2}$ |
| Normalized-trace magnitude | $\lvert\mathrm{tr}(U)/d\rvert\le\varepsilon/100$ versus $\lvert\mathrm{tr}(U)/d\rvert\ge\varepsilon$ | $d\ge10^6\varepsilon^{-2}$ |

For all three rows, if $0<\varepsilon\le1/4$, every such test satisfies

```math
{\displaystyle
\boxed{F+R+FR\ge\frac{1}{4096\varepsilon^2}.}
}
\tag{1}
```

The dimension conditions are sufficient conditions for these proofs. The query constructions in [Dicke probes](dicke-probe.md) and the budget allocation in [Resource frontier](resource-frontier.md) give the corresponding upper bounds in every dimension.

## 1. Two diagonal-oracle ensembles

First use the known uniform state

```math
|u_d\rangle=\frac1{\sqrt d}\sum_{j=1}^d|j\rangle
```

as both source and target, and choose

```math
U_z=\mathrm{diag}(z_1,\ldots,z_d).
```

Then

```math
{\displaystyle
a(U_z)=\langle u_d|U_z|u_d\rangle
       =\frac1d\sum_{j=1}^d z_j.
}
\tag{2}
```

In the null ensemble, the $z_j$ are independent uniform phases. In the alternative, draw $\theta$ uniformly and, conditional on it, draw the $z_j$ independently from the Poisson law with mean

```math
w=2\varepsilon e^{i\theta}.
```

These are exactly the ensembles in [Theorem 1 of the Poisson–Müntz bound](poisson-muntz-bound.md#1-ensemble-theorem), with $N=d$ and $r=2\varepsilon\le1/2$.

Let $\rho_{\mathrm H}$ be the algorithm's average output on the uniform-phase null and $\rho_{\mathrm P}$ its average output on the alternative. The ensemble bound gives

```math
{\displaystyle
\begin{aligned}
D(\rho_{\mathrm P},\rho_{\mathrm H})^2
 &\le
 \bigl[11(L+1)(M+L)+M\bigr]
       \log\frac1{1-4\varepsilon^2}\\
 &\le\frac{736}{3}\,B\varepsilon^2,
 \qquad L=\min\{F,R\}.
\end{aligned}
}
\tag{3}
```

For the second inequality, use the coefficient bound $46B$ and

```math
\log\frac1{1-4\varepsilon^2}
 \le\frac{4\varepsilon^2}{1-4\varepsilon^2}
 \le\frac{16}{3}\varepsilon^2.
```

Independence gives the exact null second moment

```math
{\displaystyle
\mathbb E_{\mathrm H}|a|^2
 =\frac1{d^2}\sum_{j,k}
        \mathbb E[z_j\overline z_k]
 =\frac1d.
}
\tag{4}
```

For the alternative, conditional on $\theta$,

```math
{\displaystyle
\mathbb E_{\mathrm P}[a\mid\theta]=w,\qquad
\mathbb E_{\mathrm P}[|a-w|^2\mid\theta]
 =\frac{1-|w|^2}{d}
 =\frac{1-4\varepsilon^2}{d}\le\frac1d.
}
\tag{5}
```

The covariance cross terms vanish because the centered phases are conditionally independent. Averaging (5) over $\theta$ preserves the bound.

For any final acceptance effect $0\le T\le I$,

```math
{\displaystyle
|\mathrm{tr}(T\rho)-\mathrm{tr}(T\sigma)|
 \le D(\rho,\sigma).
}
\tag{6}
```

We will combine required acceptance gaps with the upper bound (3).

## 2. The tolerant overlap promise

**Theorem 2.** Fix $0<\varepsilon\le1/4$, an integer dimension
$d\ge10^6\varepsilon^{-2}$, and any known normalized source and target states. Every test correct with probability at least $2/3$ on

```math
{\displaystyle
H_0:\ |a(U)|\le\varepsilon/100,
\qquad
H_1:\ |a(U)|\ge\varepsilon
}
\tag{7}
```

satisfies (1).

We first prove the result for the uniform source and target. By (4) and Markov's inequality,

```math
{\displaystyle
\delta_0:=
 \Pr_{\mathrm H}\{|a|>\varepsilon/100\}
 \le\frac{10^4}{d\varepsilon^2}.
}
\tag{8}
```

If $|a|<\varepsilon$ under the alternative, the reverse triangle inequality and $|w|=2\varepsilon$ imply $|a-w|>\varepsilon$. Applying Markov's inequality to $|a-w|^2$ in (5) gives

```math
{\displaystyle
\delta_1:=
 \Pr_{\mathrm P}\{|a|<\varepsilon\}
 \le\frac1{d\varepsilon^2}.
}
\tag{9}
```

Thus

```math
{\displaystyle
\delta_0\le10^{-2},\qquad \delta_1\le10^{-6}.
}
\tag{10}
```

Let acceptance mean the answer $H_1$. On the null good event, acceptance is at most $1/3$, and on the null bad event it is at most one. On the alternative good event, acceptance is at least $2/3$, and on its bad event it is at least zero. Hence

```math
\begin{aligned}
\Pr_{\mathrm H}(\mathrm{accept})
 &\le\frac13(1-\delta_0)+\delta_0
 =\frac13+\frac23\delta_0,\\
\Pr_{\mathrm P}(\mathrm{accept})
 &\ge\frac23(1-\delta_1).
\end{aligned}
```

Equations (6) and (10) imply

```math
{\displaystyle
D(\rho_{\mathrm P},\rho_{\mathrm H})
 \ge\frac13-\frac23(\delta_0+\delta_1)
 \ge0.326666>\frac8{25}.
}
\tag{11}
```

This uses the original unconditioned ensembles, so no conditional-distribution normalization enters the proof.

If $B<1/(4096\varepsilon^2)$, equation (3) would instead give

```math
{\displaystyle
D(\rho_{\mathrm P},\rho_{\mathrm H})^2
 <\frac{736}{3\cdot4096}
 =\frac{23}{384}<\frac1{16},
}
\tag{12}
```

and therefore $D<1/4$, contradicting (11). This proves (1) for the uniform pair. Section 5 below transfers it to every fixed known pair $s,g$.

## 3. Correcting one matrix element to exactly zero

The uniform-phase null in (4) has a small random overlap. To obtain an exact-zero promise, correct each null oracle by a unitary rotation supported on at most two output directions.

**Lemma 3.** For $d\ge2$, every unitary $U$ and every normalized pair $s,g$ admit a unitary $\widetilde U$ such that

```math
{\displaystyle
\langle g|\widetilde U|s\rangle=0,\qquad
\|\widetilde U-U\|\le2|\langle g|U|s\rangle|.
}
\tag{13}
```

The same norm bound holds for their inverses.

**Proof.** Let

```math
|\psi\rangle=U|s\rangle,\qquad
a=\langle g|\psi\rangle,\qquad
c=\sqrt{1-|a|^2}.
```

If $a=0$, take $\widetilde U=U$. If $0<|a|<1$, define the unit vector

```math
|\eta\rangle=\frac{|\psi\rangle-a|g\rangle}{c},
\qquad \langle g|\eta\rangle=0.
```

On the ordered orthonormal basis $(\eta,g)$, define

```math
{\displaystyle
V=
\begin{pmatrix}
c&\overline a\\
-a&c
\end{pmatrix},
}
\tag{14}
```

and let $V$ be the identity on the orthogonal complement. The identity
$c^2+|a|^2=1$ shows $V^\dagger V=I$. The coordinates of $\psi$ in this basis are $(c,a)$, so

```math
V\begin{pmatrix}c\\a\end{pmatrix}
 =\begin{pmatrix}1\\0\end{pmatrix}.
```

Thus $V\psi=\eta$ and $\langle g|VU|s\rangle=0$.

The two nontrivial eigenvalues of $V$ are $c\pm i|a|$. Consequently

```math
{\displaystyle
\begin{aligned}
\|V-I\|
 &=\sqrt{2-2c}\\
 &=|a|\sqrt{\frac{2}{1+c}}
 \le\sqrt2\,|a|\le2|a|.
\end{aligned}
}
\tag{15}
```

Set $\widetilde U=VU$. Right multiplication by a unitary preserves the operator norm, so (13) follows.

If $|a|=1$, choose any unit vector $\eta\perp g$, which exists because $d\ge2$, and use the matrix (14) with $c=0$. Since $\psi=a g$, it still maps $\psi$ to $\eta$, and (15) still holds. Finally,

```math
\|\widetilde U^\dagger-U^\dagger\|
 =\|\widetilde U-U\|.
```

This proves the lemma in all cases. $\square$

Only the output vectors $\eta,g$ are required to be orthogonal. The lemma applies without change when the supplied source and target coincide.

### Hybrid bound, including controlled and adaptive calls

For any fixed pair of unitaries $U,\widetilde U$, an algorithm using at most $q$ query slots satisfies

```math
{\displaystyle
D(\rho(U),\rho(\widetilde U))
 \le q\|U-\widetilde U\|.
}
\tag{16}
```

To see this, purify the algorithm and replace one oracle call at a time. At a forward slot, the Euclidean distance between the two resulting state vectors increases by at most $`\|U-\widetilde U\|`$. At an inverse slot the same bound holds because
$`\|U^\dagger-\widetilde U^\dagger\|=\|U-\widetilde U\|`$.
All intervening isometries preserve vector distances. The triangle inequality gives a final vector-distance bound of $`q\|U-\widetilde U\|`$.

For unit vectors, normalized trace distance between their density matrices is at most their Euclidean distance, and partial trace cannot increase trace distance. This proves (16) for the actual output. A controlled call has a block-diagonal difference with zero in its inactive block and $U-\widetilde U$ in its active block, so its norm is unchanged. A selector with forward, inverse, and inactive blocks is bounded in the same way. Keeping measurement records and padding stopped histories by inactive slots proves the adaptive statement.

For budgets $F,R$, use $q\le M=F+R$. Applying (13) in (16) gives

```math
{\displaystyle
D(\rho(U),\rho(\widetilde U))
 \le2M|a(U)|.
}
\tag{17}
```

## 4. The exact-zero overlap promise

**Theorem 4.** Fix $0<\varepsilon\le1/4$, an integer dimension
$d\ge16\varepsilon^{-4}$, and any known normalized source and target states. Every test correct with probability at least $2/3$ on

```math
{\displaystyle
H_0:\ a(U)=0,\qquad
H_1:\ |a(U)|\ge\varepsilon
}
\tag{18}
```

satisfies (1).

Again begin with the uniform source and target. Draw $U_z$ from the uniform-phase null and apply Lemma 3 to define $\widetilde U_z$. Every corrected oracle has exactly zero overlap. Denote the average algorithm output on this corrected null by $\rho_{\mathrm Z}$.

Convexity of trace distance, (17), (4), and Cauchy–Schwarz give

```math
{\displaystyle
\begin{aligned}
D(\rho_{\mathrm H},\rho_{\mathrm Z})
 &\le\mathbb E_{\mathrm H}
       D(\rho(U_z),\rho(\widetilde U_z))\\
 &\le2M\,\mathbb E_{\mathrm H}|a(U_z)|\\
 &\le2M\sqrt{\mathbb E_{\mathrm H}|a(U_z)|^2}
 =\frac{2M}{\sqrt d}.
\end{aligned}
}
\tag{19}
```

The corrected oracle is a valid member of the arbitrary-unitary input class. The correcting rotation is used to define a hard input distribution; it is not an operation the algorithm is asked to implement.

Correctness on the corrected null implies
$\Pr_{\mathrm Z}(\mathrm{accept})\le1/3$.
Equations (6) and (19) then give

```math
\Pr_{\mathrm H}(\mathrm{accept})
 \le\frac13+\frac{2M}{\sqrt d}.
```

The alternative satisfies the promised lower threshold except with probability $\delta_1\le1/(d\varepsilon^2)$, by (9). Its acceptance probability is at least
$\frac23(1-\delta_1)$. Therefore

```math
{\displaystyle
D(\rho_{\mathrm P},\rho_{\mathrm H})
 \ge\frac13-\frac{2}{3d\varepsilon^2}
              -\frac{2M}{\sqrt d}.
}
\tag{20}
```

Suppose, for contradiction, that
$B<1/(4096\varepsilon^2)$.
Since $M\le B$ and $d\ge16\varepsilon^{-4}$,

```math
\frac{2M}{\sqrt d}<\frac1{8192}.
```

Also,

```math
\frac{2}{3d\varepsilon^2}
 \le\frac{\varepsilon^2}{24}
 \le\frac1{384},
```

where the last step uses $\varepsilon\le1/4$. Thus (20) gives the explicit required separation

```math
{\displaystyle
D(\rho_{\mathrm P},\rho_{\mathrm H})
 >
 \frac13-\frac1{384}-\frac1{8192}
 =\frac{8125}{24576}>\frac14.
}
\tag{21}
```

The Poisson–Müntz bound gives $D<1/4$ under the same small-budget assumption, exactly as in (12). This contradiction proves (1). Section 5 transfers the result to arbitrary known source and target states. $\square$

In probability-threshold notation $p_0=\varepsilon^2$, the theorem states a necessary budget $B\ge1/(4096p_0)$ when $0<p_0\le1/16$ and $d\ge16p_0^{-2}$.

## 5. Arbitrary known source and target states

Fix any normalized known pair $s,g$ in the same dimension. Choose known unitaries $A,C$ satisfying

```math
A|s\rangle=|u_d\rangle,\qquad
C|u_d\rangle=|g\rangle.
```

Given any oracle $U$ from the uniform-pair construction, define

```math
U'=CUA.
```

Then

```math
{\displaystyle
\langle g|U'|s\rangle
 =\langle u_d|U|u_d\rangle.
}
\tag{22}
```

One query to $U'$ is simulated using one forward query to $U$, with known gates $A,C$. One query to $U'^\dagger=A^\dagger U^\dagger C^\dagger$ uses one inverse query. The same statement holds for controlled calls because all basis-change gates are known.

An algorithm for the pair $s,g$ would therefore solve the uniform-pair problem with identical directional query counts and success probability. This proves both overlap lower bounds for every fixed known pair. These reductions count oracle calls; the cost of implementing known-state gates is a separate resource in [Implementation](implementation.md).

## 6. Normalized-trace magnitude

Let

```math
\tau(U)=\frac{\mathrm{tr}(U)}d.
```

For the diagonal hard family in (2),

```math
{\displaystyle
\tau(U_z)=\frac1d\sum_{j=1}^d z_j
        =\langle u_d|U_z|u_d\rangle.
}
\tag{23}
```

A test for normalized-trace magnitude on arbitrary $d$-dimensional unitaries must in particular work on this diagonal family. Equations (3)–(12) therefore apply directly to such a test, with arbitrary ancillas and controls already allowed.

**Corollary 5.** For $0<\varepsilon\le1/4$ and
$d\ge10^6\varepsilon^{-2}$, every test correct with probability at least $2/3$ on

```math
{\displaystyle
|\tau(U)|\le\varepsilon/100
\quad\text{versus}\quad
|\tau(U)|\ge\varepsilon
}
\tag{24}
```

satisfies (1).

For the corresponding upper construction, use the known maximally entangled state

```math
|\Phi_d\rangle
 =\frac1{\sqrt d}\sum_{j=1}^d|j\rangle|j\rangle.
```

Its overlap under the oracle on the second register is

```math
{\displaystyle
\langle\Phi_d|(I\otimes U)|\Phi_d\rangle
 =\frac1d\sum_{j=1}^d\langle j|U|j\rangle
 =\tau(U).
}
\tag{25}
```

Each forward or inverse call to $I\otimes U$ uses one corresponding call to $U$. The known-state Dicke test, with the fixed-ratio gap analysis in [Resource frontier](resource-frontier.md), therefore applies to normalized trace with the same directional query budgets. For $d=2^n$, the known source, target, and projector in (25) are implemented by Bell-state preparation and its inverse; their gates and the two-register workspace are part of the ordinary resource accounting.

The normalized-trace lower bound proved here has the gap promise (24). Lemma 3 removes one specified matrix element of a unitary; it does not impose $\mathrm{tr}(\widetilde U)=0$. The maximally entangled identity supplies an upper reduction, but a lower bound over all unitaries on a larger register cannot be transferred merely by restricting to the special form $I\otimes U$.

## 7. An additive-accuracy lower-bound corollary

For completeness, the tolerant testing result also gives a precisely quantified estimation lower bound. Suppose an algorithm returns a real estimate $\widehat b$ with

```math
\Pr\{|\widehat b-|a(U)||\le\eta\}\ge2/3
```

for every $U$. Set $\varepsilon=4\eta$. On the successful estimation event, the threshold test $\widehat b\ge\varepsilon/2$ correctly distinguishes (7), because

```math
\varepsilon/100+\eta<\varepsilon/2<\varepsilon-\eta.
```

Thus, for $0<\eta\le1/16$ and $d\ge62500\eta^{-2}$,

```math
{\displaystyle
F+R+FR\ge\frac1{65536\eta^2}.
}
\tag{26}
```

The same conclusion holds for additive estimation of $|\tau(U)|$, using (24). An estimate of the complex amplitude or normalized trace within complex absolute error $\eta$ also yields such a magnitude estimate by the reverse triangle inequality. Equation (26) is a lower-bound consequence of the testing reduction.

## Proof dependencies

The ensemble comparison, including the only external analytic inequality used here, is proved in [Poisson–Müntz bound](poisson-muntz-bound.md). The bounded-error upper tests and their likelihood estimates are proved in [Dicke probes](dicke-probe.md). The conversion from individual blocks to statements about total asymmetric budgets is given in [Resource frontier](resource-frontier.md).
