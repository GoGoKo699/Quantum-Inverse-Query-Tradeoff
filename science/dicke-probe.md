# Dicke probes for rank-one overlap testing

This page proves a uniform one-sided upper bound for the promise

```math
\langle g|U|s\rangle=0
\qquad\text{versus}\qquad
|\langle g|U|s\rangle|\ge \varepsilon.
```

The source and target states are known, and their preparation and coherent projector circuits are charged separately from oracle queries. The construction works for every unitary completion of the transition amplitude and in every dimension. It supplies the constructive part of the [resource frontier](resource-frontier.md); the matching lower bound has the dimension assumptions stated there. See [the model](model.md) for the access conventions and [implementation](implementation.md) for gate and memory costs.

## 1. Statement of the constructive bound

Write

```math
a=\langle g|U|s\rangle,\qquad p=|a|^2,\qquad p_0=\varepsilon^2.
```

For integers $1\le R\le F$, define

```math
\Lambda=F+2R(F-R).
```

**Theorem.** If $p_0\Lambda\ge1$, there is a test using at most $F$ calls to $U$ and $R$ calls to $U^\dagger$ that has no false positive when $p=0$ and detects every $p\ge p_0$ with probability at least $1/9$. Twenty independent repetitions give success probability at least $2/3$, multiplying each query budget by at most twenty. The test uses no controlled call to either unknown oracle.

The theorem counts worst-case calls, including unsuccessful preparation attempts. The zero-inverse endpoint is ordinary sampling. Reversing the roles of $U,s,g$ and $U^\dagger,g,s$ supplies the opposite orientation of an asymmetric budget. The allocation of these constructions to arbitrary budgets is given in [the resource-frontier proof](resource-frontier.md).

## 2. Reverse queries prepare an unknown input mode

Assume initially that $p<1$, and put $c=\sqrt{1-p}$. Define

```math
|\xi\rangle=\frac{U^\dagger|g\rangle-a^*|s\rangle}{c},
\qquad
|\eta\rangle=\frac{U|s\rangle-a|g\rangle}{c}.
```

Both vectors are normalized, with $\langle s|\xi\rangle=0$ and $\langle g|\eta\rangle=0$. One attempt to prepare $\xi$ consists of preparing $g$, applying $U^\dagger$, and measuring the known projector $\Pi_s=|s\rangle\langle s|$.

- Outcome $\Pi_s$ has probability $p$ and, under the exact-zero promise, certifies the alternative. The test accepts and stops.
- The complementary outcome has probability $1-p$ and leaves exactly $|\xi\rangle$ in the register.

Perform up to $R$ attempts. The event that every attempt has the complementary outcome has probability $(1-p)^R$, and conditioned on that event the retained state is $|\xi\rangle^{\otimes R}$. Every supplied copy therefore costs one inverse query. There is no unknown-state preparation oracle, cloning operation, or classical description of $\xi$.

If $p=1$, the first attempt accepts with certainty. The formula defining $\xi$ is then unnecessary. If $p=0$, all attempts succeed with certainty, so the preparation stage never produces a false positive.

The two input modes satisfy the exact identities

```math
U|s\rangle=c|\eta\rangle+a|g\rangle,
```

```math
\begin{aligned}
U|\xi\rangle
&=\frac{|g\rangle-a^*U|s\rangle}{c}\\
&=\frac{(1-|a|^2)|g\rangle-a^*c|\eta\rangle}{c}\\
&=c|g\rangle-a^*|\eta\rangle.
\end{aligned}
```

Thus, after identifying the input basis $(s,\xi)$ with the output basis $(\eta,g)$, the restricted action is

```math
\begin{pmatrix}c&-a^*\\a&c\end{pmatrix}\in SU(2).
```

This calculation uses only unitarity. No condition on the rest of $U$ is required, and the unknown output mode $\eta$ is never prepared, identified, or used as a reflection axis.

## 3. Deterministic encoding of the supplied copies

Given the $R$ copies of $\xi$ and $F-R$ registers in $s$, prepare

```math
|D_F^R(\xi,s)\rangle
=\binom FR^{-1/2}
\sum_{\substack{b\in\{0,1\}^F\\|b|=R}}
\bigotimes_{j=1}^F
\begin{cases}
|s\rangle,&b_j=0,\\
|\xi\rangle,&b_j=1.
\end{cases}
```

Here the piecewise expression specifies the factor in each tensor-product slot. An explicit encoder proceeds as follows.

1. Prepare an $F$-qubit mask $B$ in the known uniform weight-$`R`$ state $\binom FR^{-1/2}\sum_{|b|=R}|b\rangle$.
2. Conditioned on $b$, permute the supplied data registers so that the $\xi$ copies occupy precisely the one positions of $b$. Clean up the routing workspace while retaining $B$.
3. On data slot $j$ and mask qubit $B_j$, apply the known unitary

```math
L_s=\Pi_s\otimes I+(I-\Pi_s)\otimes X.
```

Because $\xi\perp s$, the third step maps each term $|b\rangle|\chi(b)\rangle$ to $|0^F\rangle|\chi(b)\rangle$. Consequently the mask disentangles and the data are in the stated pure Dicke state. Orthogonality also makes distinct occupation patterns orthogonal, which proves the normalization.

Only supplied registers are permuted. The procedure consumes the $R$ copies and needs no postselected symmetrization. The global phase chosen for $\xi$ contributes the same factor to every term because each term has exactly $R$ excitations. A fully specified reversible routing procedure, including the order of workspace uncomputation, appears in [implementation](implementation.md#3-reversible-routing-with-clean-workspace).

## 4. The complete count likelihood

Apply $U$ to each of the $F$ data registers, then measure $\Pi_g=|g\rangle\langle g|$ separately on every register. Let $`N\in\{0,\ldots,F\}`$ be the number of positive outcomes. All output registers lie in $`\mathrm{span}\{\eta,g\}`$ and the output state is symmetric. Therefore the count-$`t`$ sector of this state is the one-dimensional space spanned by $|D_F^t(g,\eta)\rangle$.

Let $[z^t]$ denote extraction of a polynomial coefficient. Expanding the two-mode transformation gives the amplitude

```math
\boxed{\displaystyle
\beta_t(a)=
\sqrt{\frac{\binom FR}{\binom Ft}}
[z^t](c+az)^{F-R}(-a^*+cz)^R.
}
```

The normalization factor follows by representing a normalized symmetric occupation state by the monomial with denominator $\sqrt{(F-R)!R!}$ and converting the coefficient of the output monomial to the normalization $\sqrt{(F-t)!t!}$. Equivalently, direct expansion gives

```math
\beta_t(a)=
\sqrt{\frac{\binom FR}{\binom Ft}}
\sum_{u=\max(0,t-R)}^{\min(t,F-R)}
\binom{F-R}{u}\binom R{t-u}
c^{F-R+t-2u}a^u(-a^*)^{R-t+u}.
```

Here $u$ is the number of source-mode factors that become target-mode factors, and $t-u$ is the number of excitation-mode factors that remain target-mode factors. Every exponent is nonnegative over the summation range. The full conditional likelihood is

```math
\Pr(N=t\mid\text{all reverse preparations succeed})=|\beta_t(a)|^2.
```

If $`a=\sqrt p\,e^{i\phi}`$, every summand in $\beta_t$ has the common phase $e^{i(t-R)\phi}$. Its remaining factor is real. The count distribution therefore depends only on $p$.

For the collective-spin description, put

```math
j=F/2,\qquad m=R-F/2,\qquad \theta=\arcsin\sqrt p.
```

Use $J_z|j,m\rangle=m|j,m\rangle$, with $J_+$ increasing the occupation count, and $J_y=(J_+-J_-)/(2i)$. For real positive $a$, the restricted oracle action is $e^{2i\theta J_y}$ in this convention. Thus the likelihood is the square of a Wigner-$`d`$ column:

```math
\Pr(N=t\mid\text{preparation succeeds})
=\left|\langle j,t-j|e^{2i\theta J_y}|j,m\rangle\right|^2.
```

Changing the sign of $\theta$ changes some amplitude signs but leaves these probabilities unchanged.

### Return amplitude and the exact decision probability

The test accepts when $N\ne R$. For $t=R$, the likelihood formula reduces to the real return amplitude

```math
\boxed{\displaystyle
A_{F,R}(p)
=\sum_{k=0}^{\min(R,F-R)}
(-1)^k\binom Rk\binom{F-R}k
p^k(1-p)^{F/2-k}.
}
```

This form has no division by $1-p$ and extends continuously to both endpoints. For $R\le F/2$ it is also

```math
A_{F,R}(p)
=(1-p)^{(F-2R)/2}
P_R^{(0,F-2R)}(1-2p),
```

where $P_R^{(\alpha,\beta)}$ is a Jacobi polynomial. The binomial expansion of the Jacobi polynomial gives the preceding finite sum.

Including every preparation-failure acceptance event, the exact one-run detection probability is

```math
\boxed{\displaystyle
P_{\mathrm{det}}(p)
=1-(1-p)^R A_{F,R}(p)^2.
}
```

In particular,

```math
P_{\mathrm{det}}(p)\ge1-A_{F,R}(p)^2.
```

The inequality is useful because preparation failure helps detection. There is no division by the probability of successful preparation and no repeated-until-success subroutine hidden in the query budget. At $p=0$, $A_{F,R}(0)=1$ and $P_{\mathrm{det}}(0)=0$. At $p=1$ and $R\ge1$, the actual protocol accepts in its first preparation attempt and $P_{\mathrm{det}}(1)=1$.

For fixed $F,R$, expansion at zero gives

```math
A_{F,R}(p)=1-\frac{\Lambda}{2}p+O_{F,R}(p^2),
```

```math
1-A_{F,R}(p)^2=\Lambda p+O_{F,R}(p^2),\qquad
P_{\mathrm{det}}(p)=(\Lambda+R)p+O_{F,R}(p^2).
```

For example, $A_{F,1}(p)=(1-p)^{(F-2)/2}(1-Fp)$, with endpoint values understood continuously. The count-stage linear coefficient is $3F-2$. The uniform guarantee below does not rely on truncating these expansions.

## 5. Exact second and fourth moments

Let $Q=N-R$. To evaluate its moments in the input state $|j,m\rangle$, rotate the count observable backward through the collective unitary. Define

```math
Z=J_z-mI,\qquad X=J_x,\qquad
c_2=1-2p,\qquad s_2=2\sqrt{p(1-p)},\qquad b=-2pm.
```

The backward-rotated observable is

```math
Q=c_2Z+s_2X+bI.
```

The phase of $a$ can be removed for this calculation because it does not change the count likelihood. Introduce the ladder coefficients

```math
A=(F-R)(R+1),\qquad B=R(F-R+1),\qquad A+B=\Lambda,
```

```math
A_+=(F-R-1)(R+2),\qquad
B_-=(R-1)(F-R+2).
```

Write $|r\rangle=|j,m+r\rangle$ for available magnetic levels, so that $|0\rangle$ in this subsection means the initial spin state. Terms involving an unavailable level are omitted. In particular, $AA_+$ or $BB_-$ is interpreted as zero whenever the corresponding two-step ladder transition is unavailable.

The ladder identities are

```math
X|0\rangle=\frac{\sqrt A}{2}|1\rangle+\frac{\sqrt B}{2}|-1\rangle,
```

```math
X|1\rangle=\frac{\sqrt A}{2}|0\rangle+\frac{\sqrt{A_+}}{2}|2\rangle,
\qquad
X|-1\rangle=\frac{\sqrt B}{2}|0\rangle+\frac{\sqrt{B_-}}{2}|-2\rangle,
```

and $Z|r\rangle=r|r\rangle$. Hence

```math
Q|0\rangle=b|0\rangle
+\frac{s_2\sqrt A}{2}|1\rangle
+\frac{s_2\sqrt B}{2}|-1\rangle.
```

Orthogonality of these levels yields the exact second moment

```math
\boxed{\displaystyle
M_2=\mathbb E[Q^2]
=b^2+\frac{s_2^2\Lambda}{4}
=4m^2p^2+\Lambda p(1-p).
}
```

A second application of $Q$ gives, with all coefficients displayed,

```math
\begin{aligned}
Q^2|0\rangle
={}&M_2|0\rangle\\
&+\frac{s_2\sqrt A}{2}(2b+c_2)|1\rangle
+\frac{s_2\sqrt B}{2}(2b-c_2)|-1\rangle\\
&+\frac{s_2^2\sqrt{AA_+}}{4}|2\rangle
+\frac{s_2^2\sqrt{BB_-}}{4}|-2\rangle.
\end{aligned}
```

Squaring its norm proves the exact fourth-moment identity

```math
\boxed{\displaystyle
M_4=\mathbb E[Q^4]
=M_2^2
+\frac{s_2^2}{4}\left[A(2b+c_2)^2+B(2b-c_2)^2\right]
+\frac{s_2^4}{16}(AA_++BB_-).
}
```

### Bounding the fourth moment

Set $v=s_2^2\Lambda/4$, so $M_2=b^2+v$. For existing ladder transitions,

```math
A_+\le2A,\qquad B_-\le2B.
```

The same bound applies after omitting unavailable terms, and therefore

```math
AA_++BB_-\le2(A^2+B^2)\le2\Lambda^2.
```

Also,

```math
(2b\pm c_2)^2\le8b^2+2c_2^2\le8b^2+2.
```

The middle term of $M_4$ is consequently at most

```math
8b^2v+2v\le2(b^2+v)^2+2M_2=2M_2^2+2M_2,
```

where $8b^2v\le2(b^2+v)^2$ follows from $2(b^2-v)^2\ge0$. Its last term is at most

```math
\frac{s_2^4}{16}\,2\Lambda^2=2v^2\le2M_2^2.
```

Adding the three terms gives

```math
\boxed{M_4\le5M_2^2+2M_2.}
```

## 6. Uniform detection over the entire alternative

Cauchy–Schwarz applied to the classical count distribution gives

```math
M_2=\mathbb E[Q^2\mathbf1_{Q\ne0}]
\le\sqrt{M_4\Pr(Q\ne0)}.
```

Whenever $M_2>0$,

```math
\Pr(Q\ne0)
\ge\frac{M_2^2}{M_4}
\ge\frac{M_2}{5M_2+2}.
```

If $p_0\le p\le1/2$ and $p_0\Lambda\ge1$, then

```math
M_2\ge\Lambda p(1-p)\ge\frac{\Lambda p_0}{2}\ge\frac12.
```

The last lower bound on the departure probability is increasing in $M_2$, so it is at least $1/9$. The exact formula for $P_{\mathrm{det}}$ shows that the unconditional detection probability is at least this conditional count-stage probability.

If $p\ge1/2$, the first reverse preparation accepts with probability $p\ge1/2$. This includes $p=1$, where no excitation state is defined. These two cases establish the theorem for every $p\ge p_0$, without an upper promise such as $p=O(p_0)$.

Under the null, preparation never accepts and the output has exactly $R$ target excitations, so there are no false positives in the ideal circuit. Repeating with fresh registers and accepting if any run accepts gives alternative error at most $(8/9)^{20}<1/3$.

### Sampling and useful parameter ranges

For $R=0$, prepare $s$, query $U$, and test $\Pi_g$ independently $F$ times. The detection probability is $1-(1-p)^F$. Taking $F\ge\lceil\log(3)/p_0\rceil$ gives success at least $2/3$.

For $1\le R\le F/2$,

```math
F(R+1)\le\Lambda\le2F(R+1).
```

Thus the useful mixed-budget regime requires $F(R+1)=\Omega(p_0^{-1})$. If more inverse queries are available than the construction needs, it is permissible to leave them unused. If inverse calls are the more plentiful direction, interchange $U,s,g$ with $U^\dagger,g,s$; the tested amplitude is conjugated and its magnitude is unchanged.

### A global bound on acceptance at small overlap

The same experiment has a useful upper bound for every $p\in[0,1]$. Let $H=2J_y$ in the initial spin state. The ladder coefficients give $\langle H^2\rangle=A+B=\Lambda$. The spectral distribution of $H$ in this state is symmetric, so the return amplitude is real and equals $\langle\cos(\theta H)\rangle$. Alternatively, its reality follows directly from the finite return-amplitude sum. Therefore

```math
1-A_{F,R}(p)^2
\le2\bigl(1-A_{F,R}(p)\bigr)
=2\langle1-\cos(\theta H)\rangle
\le\theta^2\langle H^2\rangle
=\theta^2\Lambda.
```

Here $1-\cos x\le x^2/2$ is applied to each eigenvalue of $H$. Since $\arcsin\sqrt p\le(\pi/2)\sqrt p$, and since $\Lambda\ge F\ge R$,

```math
\begin{aligned}
P_{\mathrm{det}}(p)
&=\bigl[1-(1-p)^R\bigr]
+(1-p)^R\bigl[1-A_{F,R}(p)^2\bigr]\\
&\le Rp+\frac{\pi^2}{4}\Lambda p\\
&\le\left(1+\frac{\pi^2}{4}\right)\Lambda p.
\end{aligned}
```

This upper bound supplies the small-overlap acceptance control used for [tuning a block for the tolerant promise](resource-frontier.md#2-tuning-a-block-without-overshooting-the-gap). It is a global inequality, independent of a small-$`p`$ expansion.

## 7. Local information and scope

For completeness, the conditional count likelihood also has a local Fisher-information identity. After removing the count-dependent phase, let $w_t(\theta)$ be its real rotation amplitudes. Normalization and the generator give

```math
\sum_t\left(\frac{dw_t}{d\theta}\right)^2
=\|2J_y|j,m\rangle\|^2=\Lambda.
```

Away from zero-probability points, or by continuous extension through them,

```math
\mathcal I_\theta
=\sum_t\frac{(\partial_\theta w_t^2)^2}{w_t^2}
=4\Lambda,\qquad
\mathcal I_p=\frac{\Lambda}{p(1-p)}.
```

This is an identity for the conditional count experiment. It does not supply a globally valid amplitude-estimation procedure: different parameters can have ambiguous likelihoods, and the endpoints require separate statistical treatment. The proved task here is zero-versus-nonzero rank-one overlap detection. Amplification into an unknown good subspace is also outside this theorem.

The collective-spin mechanism is established quantum metrology; generalized Holland–Burnett probes with unequal excitation populations appear, for example, in [Thekkadath et al., *Quantum-enhanced interferometry with large heralded photon-number states*](https://arxiv.org/abs/2006.08449v2). The oracle construction above specifies how the otherwise unknown mode is obtained and encoded with separately counted forward and inverse calls. See [related work](../references/related-work.md) for the comparison with prior access and metrology results.

The [numerical verification](../verification/README.md) checks selected finite-dimensional likelihoods and moment identities. The algebraic argument above supplies the uniform guarantee.
