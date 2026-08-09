# Independent architecture, terminology, and priority audit: POLY-2200006

**Execution date:** 2026-08-09
**Literature cutoff:** 2026-08-09
**Audit lane:** Independent Internet-enabled architecture/terminology and priority review
**Candidate reviewed:** *Many Isolated Real Zeros of Sums of Squares*

## Executive determination

No earlier public source was located that states or implies either of the following exact candidate results:

1. a quartic polynomial in ten real variables, expressible as a sum of nine squares of quadratic polynomials, whose real zero set consists of exactly $1152$ isolated points; or
2. the uniform even-$k$ lower bound

   \[
   \widetilde{\#}(2k,\ell)
   \ge \frac{(\ell-1)(k-1)}4 k^{\ell-1}
   \qquad (k\ge 2\text{ even},\ \ell\ge 3).
   \]

The candidate's ingredients have clear predecessors: the zero set of a sum of squares is a common zero set; product grids give many isolated real points; isolated real points can lie on positive-dimensional complex varieties; and products of univariate factors are standard in sharp real-algebraic constructions. A particularly close 2007 example gives $d^2$ isolated real points on a complex curve using a sum of two squared grid polynomials. What was not located earlier is the candidate's shared-selector, interval-gating assembly that produces nine admissible slices with $2^7$ sign choices per slice, or its general even-degree amplification.

The appropriate provisional classification is therefore:

> **APPARENTLY_NEW_AFTER_DOCUMENTED_SEARCH, with MODERATE novelty confidence.**

This is not an absolute priority certificate. The conclusion is limited by the unresolved source gaps listed below.

## Mandatory scope separation

The source contains two different questions which must not be conflated.

- **Ottaviani--Shapiro Conjecture 4** asserts the universal identity
  \(
  \widetilde{\#}(2k,\ell)=k^\ell.
  \)
  If the candidate construction is mathematically valid, the explicit inequality
  \(
  \widetilde{\#}(4,10)\ge1152>1024=2^{10}
  \)
  refutes that conjecture.
- **Problem 3** asks for the exact value of \(\widetilde{\#}(2k,\ell)\). The candidate does **not** determine that extremal function. It gives neither a matching upper bound nor a classification of extremizers, and it does not prove that $1152$ is maximal when $(2k,\ell)=(4,10)$.
- The real-radical decomposition, complete-intersection description, Cartesian-product amplification, and any broader implications are subsidiary claims. They do not convert the construction into an exact solution of Problem 3.

Accordingly, a release may say that the candidate **refutes Conjecture 4** and gives a new lower-bound family, subject to the separate mathematical-validity audit. It may not say that it solves Problem 3 or determines the exact maximum.

## Candidate claims reconstructed from the manuscript

### The explicit quartic

In variables $t,x_0,\ldots,x_8$, the manuscript defines

\[
q_0=x_0^2+t(t-8),\qquad
q_i=x_i^2-(t-i+1)(t-i)\quad(1\le i\le8),
\]

and

\[
P=\sum_{i=0}^8q_i^2.
\]

Thus $P$ has degree four and is a sum of nine squares. The proposed count is organized by the selector variable $t$: real solutions occur only for $t=0,1,\ldots,8$. At each of these nine values, two radicands vanish and seven are positive, yielding $2^7$ independent sign choices. The claimed total is

\[
9\cdot2^7=1152.
\]

The manuscript additionally records that the complex common-zero scheme is one-dimensional rather than zero-dimensional: its coordinate ring is finite free of rank $2^9$ over \(\mathbb C[t]\). This correctly identifies why a zero-dimensional complex Bezout count would be the wrong comparison architecture.

### The even-degree family

For even $k=2d$, the manuscript combines a univariate $d$-well polynomial

\[
F_d(x)=\prod_{r=1}^d(x-r)^2
\]

with degree-$k$ sign-gating polynomials $A_i(t)$. The simultaneous nonnegative locus of the $A_i$ is a finite set of allowed selector values; at those values the equations

\[
F_d(x_i)=\varepsilon A_i(t)
\]

have either $d=k/2$ or $k$ real solutions. The resulting count is the displayed lower bound above. This is the exact family for which prior art was sought; merely finding earlier product-grid or SOS constructions would not be an identical result.

## Original source and status verification

Boris Shapiro's 2015 problem collection states:

- **Problem 3:** find the maximal number \(\widetilde{\#}(2k,\ell)\) of isolated zeros of a real nonnegative degree-$2k$ polynomial in \(\ell\) variables that is a sum of squares of degree-at-most-$k$ real polynomials; and
- **Conjecture 4:** \(\widetilde{\#}(2k,\ell)=k^\ell\) for every number of variables.

The official journal HTML was checked directly:

- Boris Shapiro, “Problems Around Polynomials: The Good, The Bad and The Ugly…,” *Arnold Mathematical Journal* **1** (2015), 91--99, DOI [10.1007/s40598-015-0008-4](https://doi.org/10.1007/s40598-015-0008-4).
- Official full-text HTML: [Arnold Mathematical Journal](https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/14-08/).
- Public preprint: [arXiv:1503.05295](https://arxiv.org/abs/1503.05295).

The official text distinguishes the exact maximum problem from the conjectural formula and cites the two-variable theorem \(\widetilde{\#}(2k,2)=k^2\). The candidate's scope statement is therefore source-faithful when it claims a refutation of Conjecture 4 but not a solution of Problem 3.

A current copy on Shapiro's problem seminar pages was also checked and still presents the item without an attached resolution:

- [Problems with polynomials PDF](https://staff.math.su.se/shapiro/ProblemSolving/ProblemsWithPolynomials.pdf)
- [Problems in mathematics seminar page](https://staff.math.su.se/shapiro/ProblemSolving/)

The absence of an annotation is supporting status evidence, not proof of novelty.

## Theorem-level comparison with the closest prior art

| Source | Exact result or construction | Relation to the candidate | Collision verdict |
|---|---|---|---|
| M.-D. Choi, T.-Y. Lam, B. Reznick, “Real zeros of positive semidefinite forms. I,” *Math. Z.* **171** (1980), 1--26, [DOI](https://doi.org/10.1007/BF01215051), [EuDML](https://eudml.org/doc/172919) | Establishes the relevant sharp two-variable SOS value \(\widetilde{\#}(2k,2)=k^2\), as reported in Shapiro's source, and treats real zeros of positive semidefinite forms. | Foundational extremal precedent, but it does not state an \(\ell\ge3\) selector construction, a $1152$-point quartic, or the even-$k$ family. | **No exact or stronger collision located.** |
| Y. Lu, D. J. Bates, A. J. Sommese, C. W. Wampler, “Finding All Real Points of a Complex Curve,” *Contemp. Math.* **448** (2007), 183--205, [DOI](https://doi.org/10.1090/conm/448/08665), [primary PDF](https://www3.nd.edu/~cwample1/Preprints/lbsw.pdf) | Exhibits \(\prod_{i=1}^d(x-i)^2+\prod_{i=1}^d(y-i)^2=0\), which has $d^2$ isolated real solutions lying on a complex curve. | This is the closest explicit architecture predecessor. It already demonstrates both a product grid and isolated real points on a positive-dimensional complex locus. It attains the standard $k^2$ scale in two variables and has no shared selector or interval-gated multi-slice amplification. | **Known ingredient and close architecture; not the candidate theorem.** |
| S. Barone, S. Basu, “On a real analog of Bezout inequality and the number of connected components of sign conditions,” *Proc. Lond. Math. Soc.* **112** (2016), 115--145, [DOI](https://doi.org/10.1112/plms/pdv059), [arXiv](https://arxiv.org/abs/1303.1577), [author PDF](https://www.math.purdue.edu/~sbasu/submission-12-july-2014.pdf) | Provides sharpness examples for real-Bezout-type component bounds using sums of squares of products of univariate factors in coordinate blocks; Example 1.12 realizes the predicted degree dependence. | Shows that SOS product-grid constructions for many real components are standard. Under a uniform degree-$k$ summand constraint, this comparison supplies grid-scale behavior, not the candidate's super-$k^\ell$ selector count. It does not state the $1152$ example or family bound. | **Known constructional ingredients; no theorem-level collision.** |
| R. Quarez, “On the Real Zeros of Positive Semidefinite Biquadratic Forms,” *Commun. Algebra* **43** (2015), 1317--1353, [DOI](https://doi.org/10.1080/00927872.2013.865052) | Studies real zero patterns and SOS behavior for the special class of positive semidefinite biquadratic forms. | Different polynomial class, grading, and extremal question. No implication of the affine $10$-variable construction or general family was located. | **Adjacent, not stronger.** |
| S. Kunert, C. Scheiderer, “Extreme positive ternary sextics,” *Trans. Amer. Math. Soc.* **370** (2018), 3997--4013, [DOI](https://doi.org/10.1090/tran/7076), [arXiv](https://arxiv.org/abs/1508.03816) | Classifies zero configurations and extremality phenomena for positive semidefinite ternary sextics, including non-SOS forms. | Different class and fixed low dimension; it neither gives the candidate SOS construction nor an upper/lower theorem implying it. | **Adjacent, not stronger.** |
| C. Blekherman et al., “Sums of squares and quadratic persistence on real projective varieties,” *J. Eur. Math. Soc.* **24** (2022), [DOI](https://doi.org/10.4171/JEMS/1108) | Relates sums of squares, Pythagoras numbers, and projective invariants. | Concerns SOS length and projective geometry rather than the maximum number of isolated affine real zeros. | **No collision.** |
| C. Scheiderer, “Sum of squares length of real forms,” *Math. Z.* **286** (2017), [DOI](https://doi.org/10.1007/s00209-016-1773-z) | Studies the number of squares required in SOS representations. | The candidate uses nine squares, but its result is about isolated real-zero counts. SOS length results found do not force or reproduce the candidate count. | **No collision.** |
| D. Bates, F. Bihan, F. Sottile, “Bounds on the number of real solutions to polynomial equations,” [arXiv:0706.4134](https://arxiv.org/abs/0706.4134); F. Bihan, F. Sottile, “New fewnomial upper bounds from Gale dual polynomial systems,” [arXiv:math/0609544](https://arxiv.org/abs/math/0609544) | Gives fewnomial bounds for nondegenerate real solutions of sparse polynomial systems. | The candidate points are singular common zeros and lie on positive-dimensional complex components; its supports are not in a fixed fewnomial regime yielding the claimed count. The located fewnomial theorems do not imply the candidate construction or contradict it. | **Different hypotheses; no collision.** |
| T. Le, M. Safey El Din, T. de Wolff, “Computing the real isolated points of an algebraic hypersurface,” [arXiv:2008.10331](https://arxiv.org/abs/2008.10331) | Gives algorithms for computing real isolated points. | Algorithmic detection, not an extremal count or construction. | **No collision.** |

No earlier theorem was found which, under its exact hypotheses, forces a quartic SOS in ten variables to have at least $1152$ isolated real zeros or yields the manuscript's general coefficient \((\ell-1)(k-1)/4\).

## Architecture and terminology adjudication

### What is established prior art

The following mechanisms should not be presented as individually new:

1. \(\sum_i q_i(x)^2=0\) over \(\mathbb R\) if and only if every \(q_i(x)=0\).
2. Products of univariate factors create Cartesian grids of real zeros.
3. Isolated real points may be singular points of a positive-dimensional complex variety; Lu--Bates--Sommese--Wampler give an explicit SOS grid example.
4. Sums of squares of product polynomials are standard sharpness constructions in real-algebraic component bounds; Barone--Basu provide a clear primary-source precedent.
5. Degree-sensitive real-root-count and component-count bounds are classical in real algebraic geometry, fewnomial theory, and the topology of intersections of quadrics.

### What appears distinctive in the candidate

The searched literature did not reveal the following assembly:

1. one common selector $t$ controlling all other variables;
2. adjacent quadratic sign exclusions that force \(t\in\{0,\ldots,8\}\);
3. exactly two vanishing radicands and seven positive radicands on every allowed slice;
4. \(9\cdot2^7=1152\) isolated real zeros from nine degree-two equations in ten variables, despite a one-dimensional complex common-zero locus;
5. a scalable sign-gating construction whose allowed selector values have one-active and two-active profiles and yield the uniform even-$k$ lower bound.

Useful neutral terminology for this architecture is **shared-selector slice gating** or **selector-gated product-grid construction**. No evidence was found that either phrase is established terminology; they should be used descriptively, not as claims of a named method.

The phrase **nine-slice quartic** should not be confused with **a sum of nine squares**: both happen to equal nine in the base construction, but one counts selector values and the other counts SOS summands.

## Database, citation, and identifier searches

### Crossref and DOI

The source DOI record was checked directly:

- [Crossref record for 10.1007/s40598-015-0008-4](https://api.crossref.org/works/10.1007/s40598-015-0008-4)

At the execution date, the record reported publication in 2015, twenty deposited references, and eight Crossref-recorded citing works. Exact-phrase and formula searches through Crossref produced no matching candidate construction. Broad searches were noisy and were not treated as evidence of exhaustiveness.

### OpenAlex

The source record and its cited-by graph were checked:

- [OpenAlex source record](https://api.openalex.org/works/https://doi.org/10.1007/s40598-015-0008-4)
- [OpenAlex works citing the source](https://api.openalex.org/works?filter=cites%3AW2105159206&per-page=200)

At the execution date, OpenAlex listed ten citing works. The returned titles concerned other problems in Shapiro's collection: random growth, differential-polynomial zeros, Newton inequalities, Abel--Goncharov/Casas--Alvero questions, even-degree real zeros, isolated critical points, oscillatory solutions, point-mass equilibria, critical points of entire fractions, and the Hawaii conjecture. No title or available abstract stated the SOS isolated-zero construction or an exact/stronger resolution of Problem 3 or Conjecture 4.

An exact OpenAlex search for the conjunction of “isolated real zeros” and “sum of squares” returned only unrelated SOS/nonnegativity and sublevel-volume works; no formula or architecture collision was identified.

### DataCite

The source DOI is Crossref-registered, so a missing DataCite item is expected. An exact DataCite phrase query returned no match:

- [DataCite phrase search](https://api.datacite.org/dois?query=%22isolated+real+zeros%22+%22sum+of+squares%22&page%5Bsize%5D=50)

### arXiv and indexed-web searches

The source preprint and searches using combinations of the following were checked:

- `"Ottaviani Shapiro" isolated zeros`
- `"isolated real zeros" "sum of squares"`
- `"1152" "isolated real zeros" quartic`
- `"x_0^2+t(t-8)"`
- `"x_i^2-(t-i+1)(t-i)"`
- `"9*2^7" sum of squares zeros`
- `"(l-1)(k-1)/4" sum of squares`
- `"(ell-1)(k-1)>4k"`
- `selector polynomial` / `gate polynomial` / `slice` with SOS and real zeros
- `grid polynomial` with isolated real zeros and positive-dimensional complex components

No indexed arXiv paper or public manuscript containing the candidate formulas, count, or family bound was located. Direct access to the arXiv export API was unavailable during one part of the audit because its host did not resolve; the public arXiv pages and indexed-web routes remained usable. This is recorded as a coverage limitation, not silently ignored.

## Author pages, proceedings, theses, comments, and problem sites

- Giorgio Ottaviani's [publication list](https://people.dimai.unifi.it/ottaviani/public.html) was inspected through its current entries. It includes substantial work on sums of squares, degree, and identifiability, but no item whose title or available metadata resolves this isolated-zero conjecture.
- Boris Shapiro's current problem-seminar pages were inspected as described above.
- Searches restricted to MathOverflow, GitHub, UnsolvedMath, arXiv, university repositories, theses, and conference proceedings found no posted proof, counterexample, comment, or code with the candidate formula or count.
- Formula-level searches were used because an equivalent result may omit the names Ottaviani and Shapiro.

No public comment thread announcing an earlier counterexample was located. Searchable absence is not a historical guarantee.

## Non-English searches

Targeted searches were run using terminology equivalent to “isolated real zeros” and “sum of squares” in:

- Russian: `изолированных вещественных нулей`, `сумма квадратов`;
- French: `zéros réels isolés`, `somme de carrés`;
- German: `isolierte reelle Nullstellen`, `Summe von Quadraten`;
- Italian: `zeri reali isolati`, `somma di quadrati`.

No relevant earlier construction or theorem was located. This was a terminology search, not a complete review of every non-English journal.

## Stronger-result search

The audit separately looked for results that would imply the candidate without reproducing its exact formulas:

- general lower bounds for isolated real points of affine SOS hypersurfaces;
- component bounds and sharpness examples for real varieties defined by quadrics;
- complete intersections with all or many solutions real;
- fewnomial lower and upper constructions;
- SOS-length and Pythagoras-number results;
- real-radical and singular-isolated-point constructions;
- product theorems and block amplification for zero sets.

The located generic complete-intersection and product-grid results explain the $k^\ell$-scale baseline or concern nondegenerate complex solutions. They do not yield a super-$k^\ell$ count under the candidate's uniform summand-degree constraint. No earlier stronger theorem implying the $1152$-point construction or the even-$k$ family was found.

## Unresolved source gaps

1. **Subscription citation networks.** Full MathSciNet and zbMATH review text and complete cited-by graphs were not independently exhausted.
2. **Google Scholar.** A complete, stable, exportable cited-by traversal was not available; OpenAlex and Crossref were used as reproducible substitutes, but their coverage differs.
3. **arXiv export API.** One direct API route failed to resolve. Public arXiv pages and indexed searches were checked, but a clean API dump was not obtained.
4. **Unindexed literature.** Accepted-but-unindexed articles, local proceedings, dissertations, lecture notes, and non-OCR scans may evade formula and terminology searches.
5. **Private work.** Unpublished manuscripts, correspondence, seminar handouts, and private communications cannot be excluded.
6. **Rediscovery risk.** The base construction is elementary once seen. An equivalent selector-gating example could appear under different notation in computational real algebraic geometry or an exercise without mentioning the extremal function.
7. **Cutoff-day lag.** Material posted on or near 2026-08-09 may not yet have propagated through DOI, Crossref, OpenAlex, or search indexes.
8. **Mathematical validity is a separate gate.** This priority audit reconstructs the claim and checks its literature position; it does not replace the hostile line-by-line proof audit or verifier replay.

These gaps prevent a high-confidence or absolute priority claim. They do not reveal an actual collision.

## Release-safe wording

Subject to the independent mathematical audit, the following wording is supported:

> We give an explicit quartic sum of nine squares in ten variables with $1152$ isolated real zeros, thereby refuting the Ottaviani--Shapiro conjectural identity \(\widetilde{\#}(2k,\ell)=k^\ell\). We also give a uniform even-degree lower-bound construction. A documented search through 2026-08-09 located close product-grid and real-curve precedents but no earlier statement of either result; the results are therefore described as apparently new with moderate confidence. We do not determine the exact extremal function in Problem 3 and do not claim absolute historical priority.

Unsupported wording includes “first proof,” “complete solution of Problem 3,” “exact value \(\widetilde{\#}(4,10)=1152\),” “optimal lower bound,” or “classification of extremizers.”

## Final adjudication fields

```text
ORIGINAL_STATEMENT_VERIFIED: YES
EXACT_1152_CONSTRUCTION_PRIOR_ART: NOT_LOCATED
EVEN_K_FAMILY_PRIOR_ART: NOT_LOCATED
STRONGER_EARLIER_RESULT: NOT_LOCATED
ARCHITECTURE_PRIOR_ART: KNOWN_INGREDIENTS_AND_CLOSE_GRID_PRECEDENTS
CONJECTURE_4_STATUS: REFUTED_BY_CANDIDATE_IF_MATHEMATICALLY_VALID
PROBLEM_3_EXACT_MAXIMUM_STATUS: NOT_SOLVED_BY_CANDIDATE
NOVELTY_CLASSIFICATION: APPARENTLY_NEW_AFTER_DOCUMENTED_SEARCH
NOVELTY_CONFIDENCE: MODERATE
FIRST_COLLISION: NONE
ABSOLUTE_PRIORITY_CLAIM: NO
```
