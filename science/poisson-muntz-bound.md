# A Poisson–Müntz bound for mixed forward and inverse queries

The following theorem bounds how well an algorithm with separate forward and inverse budgets can distinguish two random diagonal-oracle ensembles. Its assumptions are a Laurent degree restriction and pointwise normalization. These assumptions cover coherent controls, arbitrary ancillas, adaptive measurements, and early stopping with every outcome retained.

The operational consequences for overlap and normalized-trace testing are proved in [Promise reductions](promise-reductions.md). Query and error conventions are specified in [Model](model.md).

## 1. Ensemble theorem

For a multi-index $h\in\mathbb Z^N$, write

```math
h_{+,j}=\max\{h_j,0\},\qquad
h_{-,j}=\max\{-h_j,0\},\qquad
z^h=\prod_{j=1}^N z_j^{h_j}.
```

Let

```math
|\Psi(z)\rangle=\sum_h |v_h\rangle z^h
```

be a finite Laurent polynomial with coefficients in an arbitrary Hilbert space. Suppose

```math
\|\Psi(z)\|=1\quad\text{for every }z\in\mathbb T^N,
\qquad
|h_+|_1\le F,\quad |h_-|_1\le R
\tag{1}
```

whenever $v_h\ne0$, where $F,R$ are nonnegative integers. Set

```math
M=F+R,\qquad L=\min\{F,R\},\qquad B=F+R+FR.
```

For $|w|<1$, let $\mu_w$ be the product distribution of $N$ independent phases, each having density

```math
d\nu_w(e^{it})
 =\frac{1-|w|^2}{|e^{it}-w|^2}\,\frac{dt}{2\pi}.
\tag{2}
```

Define

```math
\rho_w=\mathbb E_{z\sim\mu_w}
 |\Psi(z)\rangle\langle\Psi(z)|,
\qquad
\overline\rho_r=\int_0^{2\pi}\rho_{re^{i\theta}}\,
 \frac{d\theta}{2\pi},
\quad 0\le r<1.
\tag{3}
```

Thus $\rho_0$ is the output averaged over independent uniform phases. To draw the alternative, first choose one common angle $\theta$ uniformly and then draw the $N$ phases independently conditional on the mean $re^{i\theta}$. The coordinates need not be independent after that angle is averaged out.

**Theorem 1.** With normalized trace distance

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1,
```

the ensembles in (3) satisfy

```math
\boxed{
D(\overline\rho_r,\rho_0)
 \le
 \min\!\left\{1,\,
 \sqrt{\bigl[11(L+1)(M+L)+M\bigr]
             \log\frac1{1-r^2}}\right\}.
}
\tag{4}
```

If $M=0$, the two states are identical and the right-hand side is zero. For $0\le r\le1/2$, a convenient consequence is

```math
D(\overline\rho_r,\rho_0)^2
 \le \frac{184}{3}\,B r^2.
\tag{5}
```

For $0<r\le1/2$, trace distance at least $0<\gamma\le1$ requires

```math
B\ge\frac{3\gamma^2}{184r^2}.
\tag{6}
```

The theorem concerns the phase-averaged alternative in (3). The common-angle average is an explicit part of the hard distribution, including when controlled oracle calls are available.

## 2. Why query algorithms satisfy the Laurent premise

Consider the diagonal oracle

```math
U_z=\sum_{j=1}^N z_j|j\rangle\langle j|.
```

A forward call multiplies a query-register basis component by one $z_j$; an inverse call multiplies it by $z_j^{-1}$. A controlled call also has components on which the oracle is inactive. Oracle-independent isometries form linear combinations of the existing coefficient vectors and introduce no new powers of $z$.

Starting from an oracle-independent state, induction over the calls therefore gives a vector Laurent polynomial. Each monomial arises from a query history. If a history makes $f$ forward and $r'$ inverse calls, then its final exponent satisfies

```math
|h_+|_1\le f,\qquad |h_-|_1\le r'.
```

Cancellation between opposite powers can only decrease these two quantities. Consequently, worst-case budgets of at most $F$ forward and $R$ inverse calls give (1).

For an adaptive algorithm, purify its initial randomness and its operations, retain the measurement outcomes in history registers, and control subsequent operations on those registers. A stopped history can be padded by inactive query slots. Every retained history still obeys the same two budgets, and the complete purified output has norm one for every oracle. The same reasoning covers a stronger query model that coherently selects a forward, inverse, or inactive block, provided the directional budgets hold on each supported query history.

The algorithm's actual output is obtained by tracing out some of these registers. A trace-distance bound for the retained output thus also bounds its accessible output. A normalized state conditioned on a chosen measurement outcome is not used in this proof: normalization after conditioning can divide the Laurent polynomial by an oracle-dependent quantity. The outcome flag and all other outcomes remain in $\Psi$.

No homogeneity assumption is made. In particular, controlled calls and early stopping can produce monomials with different total signed degrees.

## 3. Exact complex Poisson features

The single-coordinate moments of (2) are

```math
m_w(n):=\mathbb E_{\nu_w}[z^n]
 =
 \begin{cases}
 w^n,&n\ge0,\\
 \overline w^{-n},&n<0.
 \end{cases}
\tag{7}
```

For example, expand the two factors of

```math
\frac{1-|w|^2}{(1-we^{-it})(1-\overline w e^{it})}
```

as absolutely convergent geometric series. Integrating $e^{int}$ selects their matching Fourier coefficient and gives (7). Product independence then gives

```math
\mathbb E_{\mu_w}[z^{h-k}]
 =\prod_{j=1}^N m_w(h_j-k_j).
\tag{8}
```

Let $c=\sqrt{1-|w|^2}$. In an environment with orthonormal basis indexed by the integers, define

```math
|e_0(w)\rangle=|0\rangle,
```

and, for $a\ge1$,

```math
\begin{aligned}
|e_a(w)\rangle
 &=w^a|0\rangle+
 c\sum_{\ell=1}^a w^{a-\ell}|+\ell\rangle,\\
|e_{-a}(w)\rangle
 &=\overline w^{\,a}|0\rangle+
 c\sum_{\ell=1}^a\overline w^{\,a-\ell}|-\ell\rangle.
\end{aligned}
\tag{9}
```

Use the convention that the inner product is conjugate-linear in its first argument. The precise Gram identity is

```math
\boxed{\langle e_k(w)|e_h(w)\rangle=m_w(h-k).}
\tag{10}
```

Here is a verification of every sign case. If $0\le k\le h$, then

```math
\begin{aligned}
\langle e_k|e_h\rangle
 &=w^{h-k}
 \left[|w|^{2k}
       +(1-|w|^2)\sum_{t=0}^{k-1}|w|^{2t}\right]\\
 &=w^{h-k}.
\end{aligned}
```

An empty sum at $k=0$ is zero. If $k=-b\le h=-a\le0$, with $b\ge a$, the same finite sum gives

```math
\langle e_{-b}|e_{-a}\rangle
 =w^{b-a}
 \left[|w|^{2a}
       +(1-|w|^2)\sum_{t=0}^{a-1}|w|^{2t}\right]
 =w^{b-a}=w^{h-k}.
```

If $k\le0\le h$, the positive and negative rays meet only at the vacuum, so their vacuum terms give $w^{-k}w^h=w^{h-k}$. Finally, $h<k$ follows by conjugate symmetry. These computations include $w=0$, with the usual polynomial convention $w^0=1$.

Tensor the features over all coordinates:

```math
|E_h(w)\rangle=\bigotimes_{j=1}^N|e_{h_j}(w)\rangle,
\qquad
|\Phi_w\rangle=\sum_h |v_h\rangle\otimes|E_h(w)\rangle.
\tag{11}
```

Equations (8) and (10) imply

```math
\begin{aligned}
\mathrm{Tr}_{E}|\Phi_w\rangle\langle\Phi_w|
 &=\sum_{h,k}|v_h\rangle\langle v_k|
       \langle E_k(w)|E_h(w)\rangle\\
 &=\sum_{h,k}|v_h\rangle\langle v_k|\,
       \mathbb E_{\mu_w}[z^{h-k}]
 =\rho_w.
\end{aligned}
\tag{12}
```

The order of $k,h$ in this Gram matrix is essential for a nonreal $w$. Since $\Psi(z)$ has norm one pointwise, $\mathrm{Tr}\rho_w=1$, and therefore

```math
\|\Phi_w\|=1.
\tag{13}
```

## 4. A contraction with a common radial weight

For signed multi-indices $\ell,h$, write $\ell\preceq h$ when every $\ell_j$ lies on the integer segment from $0$ to $h_j$. Thus it has the same sign as $h_j$, unless it is zero, and satisfies $|\ell_j|\le|h_j|$. Let

```math
s(\ell)=|\{j:\ell_j\ne0\}|.
```

Expanding (11) in the environment basis gives

```math
|\Phi_w\rangle
 =\sum_\ell c^{s(\ell)}
 |P_\ell(w,\overline w)\rangle\otimes|\ell\rangle,
\tag{14}
```

where

```math
|P_\ell(w,\overline w)\rangle
 =\sum_{h:\,\ell\preceq h}
 |v_h\rangle\,
 w^{\,|h_+|_1-|\ell_+|_1}
 \overline w^{\,|h_-|_1-|\ell_-|_1}.
\tag{15}
```

All exponents in (15) are nonnegative. Each polynomial has degree at most $F$ in $w$ and at most $R$ in $\overline w$, and every contributing environment index satisfies

```math
s(\ell)\le|\ell_+|_1+|\ell_-|_1\le M.
\tag{16}
```

Define the auxiliary vector

```math
|\chi_w\rangle
 =c^M\sum_\ell |P_\ell(w,\overline w)\rangle
                   \otimes|\ell\rangle.
\tag{17}
```

On the finite environment subspace occurring in (14), let $B_w$ be diagonal with

```math
B_w|\ell\rangle=c^{M-s(\ell)}|\ell\rangle.
```

Then

```math
|\chi_w\rangle=(I\otimes B_w)|\Phi_w\rangle.
```

Every diagonal entry belongs to $[c^M,1]$. Hence

```math
\boxed{
\|\chi_w\|\le1,\qquad
\|\Phi_w-\chi_w\|\le1-c^M,\qquad
\chi_0=\Phi_0.
}
\tag{18}
```

The norm bound follows from $`\|B_w\|\le1`$; the difference bound follows from
$`\|I-B_w\|\le1-c^M`$ on that subspace and (13). At $w=0$, $c=1$, so the contraction is the identity.

The vector $\chi_w$ is an auxiliary comparison vector. Its role is to bound an overlap with the normalized purification $\Phi_w$.

## 5. The phase average produces a Müntz polynomial

For $0\le x<1$, put

```math
q(x)=\int_0^{2\pi}
 \mathrm{Re}\langle\Phi_0|
       \chi_{\sqrt{x}e^{i\theta}}\rangle
 \,\frac{d\theta}{2\pi}.
\tag{19}
```

Equations (13) and (18) give

```math
q(0)=1,\qquad |q(x)|\le1.
\tag{20}
```

A monomial $`w^a\overline w^{\,b}`$ becomes

```math
x^{(a+b)/2}e^{i(a-b)\theta}.
```

Its angular average is zero unless $a=b$, when it is $x^a$. The bidegree restriction in (15) therefore implies

```math
q(x)=(1-x)^{M/2}p(x),
\qquad p\in\mathbb R[x],\quad \deg p\le L.
\tag{21}
```

Taking the real part in (19) makes the surviving coefficients real. For $M>0$, (21) extends continuously to $x=1$, where it equals zero; thus $|q(x)|\le1$ on the closed interval as well. The case $M=0$ has already been separated.

Set $y=1-x$ and

```math
Q(y)=q(1-y)=y^{M/2}p(1-y).
\tag{22}
```

Expanding the ordinary polynomial $p(1-y)$ shows that

```math
Q\in\mathrm{span}_{\mathbb R}
 \{y^{M/2},y^{M/2+1},\ldots,y^{M/2+L}\}.
```

These are $L+1$ distinct nonnegative exponents, whose sum is

```math
S=\sum_{j=0}^L\left(\frac M2+j\right)
 =\frac{(L+1)(M+L)}2.
\tag{23}
```

**Classical inequality used.** Newman's inequality states that for distinct nonnegative real exponents $\lambda_0,\ldots,\lambda_n$ and a real polynomial in their Müntz span,

```math
\|yQ'(y)\|_{[0,1]}
 \le11\left(\sum_{j=0}^n\lambda_j\right)
       \|Q\|_{[0,1]}.
\tag{24}
```

This is the upper bound in Theorem 1.1 of Borwein and Erdélyi's author-hosted paper, which attributes the result to Newman [1,2]. The relevant theorem permits a positive smallest exponent; the additional hypotheses in that paper's separate positive-interval theorem are not needed here.

Using $`\|Q\|_{[0,1]}\le1`$ and (23), for $0\le x<1$ we obtain

```math
|q'(x)|=|Q'(1-x)|
 \le\frac{11S}{1-x}.
```

Integration from $0$ to $r^2$, together with $q(0)=1$, gives

```math
1-q(r^2)
 \le11S\log\frac1{1-r^2}.
\tag{25}
```

## 6. Return to normalized physical states

For fixed $r$, write $c=\sqrt{1-r^2}$. We need a purification of the angle-averaged alternative and a compatible purification of the null.

A finite angle register suffices. By (14)–(15), every component of $\Phi_{re^{i\theta}}$ is a trigonometric polynomial with frequencies of absolute value at most $M$. Its outer product has frequencies of absolute value at most $2M$. Choose $K=2M+1$ and $\theta_j=2\pi j/K$, $j=0,\ldots,K-1$. Averaging over these angles annihilates every nonconstant frequency in that range, so it equals the continuous angular average. Define the unit vectors

```math
\begin{aligned}
|\Omega_r\rangle
 &=K^{-1/2}\sum_{j=0}^{K-1}|j\rangle
                  |\Phi_{re^{i\theta_j}}\rangle,\\
|\Omega_0\rangle
 &=K^{-1/2}\sum_{j=0}^{K-1}|j\rangle|\Phi_0\rangle.
\end{aligned}
\tag{26}
```

Tracing out the angle register and feature environment yields
$\overline\rho_r$ and $\rho_0$, respectively. Their overlap is

```math
A=\langle\Omega_0|\Omega_r\rangle
 =\int_0^{2\pi}
   \langle\Phi_0|\Phi_{re^{i\theta}}\rangle
   \,\frac{d\theta}{2\pi}.
\tag{27}
```

The equality with the integral follows from the same finite-frequency calculation.

At each angle, (18) bounds the change in this overlap caused by replacing $\Phi_w$ with $\chi_w$. Consequently

```math
\mathrm{Re}A
 \ge q(r^2)-(1-c^M).
\tag{28}
```

Let

```math
\ell_r=\log\frac1{1-r^2}.
```

Then $c^M=e^{-M\ell_r/2}$, and $1-e^{-t}\le t$ gives

```math
1-c^M\le\frac M2\ell_r.
```

Combining this with (25) and (28),

```math
1-\mathrm{Re}A
 \le\left(11S+\frac M2\right)\ell_r.
\tag{29}
```

Trace distance is contractive under partial trace. The normalized trace distance between two unit pure states with overlap $A$ is
$\sqrt{1-|A|^2}$, as follows by diagonalizing their difference on their two-dimensional span. Moreover,

```math
1-|A|^2\le2(1-\mathrm{Re}A),
```

because the difference between the right and left sides is $|1-A|^2$. Thus

```math
\begin{aligned}
D(\overline\rho_r,\rho_0)^2
 &\le1-|A|^2\\
 &\le2(1-\mathrm{Re}A)\\
 &\le(22S+M)\ell_r\\
 &=\bigl[11(L+1)(M+L)+M\bigr]\ell_r.
\end{aligned}
```

Together with $D\le1$, this proves (4).

For the advertised simplification, note that

```math
M(L+1)=B+L^2,\qquad
L^2\le FR,\qquad M+L\le2M.
```

Therefore

```math
11(L+1)(M+L)+M
 \le44B+B\le46B.
\tag{30}
```

For $r\le1/2$,

```math
\log\frac1{1-r^2}
 \le\frac{r^2}{1-r^2}\le\frac43r^2.
\tag{31}
```

Equations (30) and (31) prove (5), and rearranging (5) proves (6). The constants are deliberately conservative.

## 7. Phase and access conventions

For a circuit with a fixed number of unconditional forward and inverse calls, replacing $U$ by $e^{i\theta}U$ multiplies the complete output vector by one overall phase. Its output density operator is therefore unchanged. This observation can identify the fixed-direction and phase-averaged ensembles for that restricted circuit class.

For controlled calls, relative phases between active and inactive branches can be observable. The proof above explicitly averages the bias angle and does not identify those two ensembles in the controlled model. This still gives a valid worst-case hard distribution for the phase-insensitive overlap-magnitude promises in [Promise reductions](promise-reductions.md).

## References and reproducible checks

1. Peter Borwein and Tamás Erdélyi, *Newman's inequality for Müntz polynomials on positive intervals*, Theorem 1.1. [Author-hosted primary text](https://people.tamu.edu/~terdelyi/papers-online/positive.pdf).
2. D. J. Newman, *Derivative bounds for Müntz polynomials*, **Journal of Approximation Theory 18** (1976), 360–362; bibliographic entry 6 in [1].

The standard-library script [check_poisson_features.py](../verification/check_poisson_features.py) checks nonreal signed Gram matrices, circuit-generated normalized Laurent examples, purification orientation, the contraction bounds, and exact finite angular averages. It can be run from the repository root with:

~~~sh
python3 verification/check_poisson_features.py
~~~

These finite checks exercise the conventions and algebra used above. The theorem follows from the analytic proof.
