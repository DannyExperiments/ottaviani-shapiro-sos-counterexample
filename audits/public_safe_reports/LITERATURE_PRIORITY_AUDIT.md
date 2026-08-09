# Independent literature and priority audit: POLY-2200006

**Execution cutoff:** 2026-08-09T02:42:52Z (2026-08-09T09:42:52+07:00)  
**Audit lane:** live Internet literature and historical-priority search  
**Mathematical correctness:** not adjudicated in this report  
**Priority conclusion:** apparently new relative to the sources searched; moderate confidence

## 1. Executive determination

No earlier published or publicly posted source was found that contains either:

1. the explicit quartic sum-of-squares construction in ten variables with exactly
   `1152` isolated real zeros, refuting the proposed value `2^10=1024` at
   `(k,l)=(2,10)`; or
2. a theorem or construction implying the audited even-degree lower bound

   ```text
   tilde#(2k,l) >= ((l-1)(k-1)/4) k^(l-1)
   ```

   for even `k>=2` and `l>=3`.

The original statement and attribution are verified. The closest prior art gives
the baseline sum-of-squares construction with `k^l` zeros (in equivalent
homogeneous notation) and general amplification mechanisms, but no base example
beating that baseline and no collision with the displayed construction or family.

The defensible classification at the cutoff is therefore:

```text
ORIGINAL_STATEMENT_VERIFIED: YES
IDENTICAL_PRIOR_RESULT_FOUND: NO
STRONGER_PRIOR_RESULT_FOUND: NO
EXACT_CONSTRUCTION_COLLISION_FOUND: NO
BASE_COUNTEREXAMPLE_PRIORITY: APPARENTLY_NEW
LOWER_BOUND_FAMILY_PRIORITY: APPARENTLY_NEW
NOVELTY_CONFIDENCE: MODERATE
ABSOLUTE_PRIORITY_CLAIM: NO
```

This is a negative-search conclusion, not proof of absolute historical priority.

## 2. Exact result placed under audit

For integers `k,l>=1`, let `tilde#(2k,l)` denote the maximum possible number of
isolated real zeros of a polynomial in `l` real variables that is a finite sum of
squares of real polynomials of degree at most `k`.

The audited candidate contains the following two claims only.

### 2.1 Explicit quartic counterexample

Use variables `t,x_0,...,x_8` and define

```text
q_0 = x_0^2 + t(t-8),
q_i = x_i^2 - (t-i+1)(t-i),  1<=i<=8,
P   = sum_(i=0)^8 q_i^2.
```

Its claimed real zero set has exactly

```text
9 * 2^7 = 1152
```

points. Consequently,

```text
tilde#(4,10) >= 1152 > 1024 = 2^10.
```

### 2.2 Even-degree lower-bound family

For even `k>=2` and `l>=3`, the audited family claims

```text
tilde#(2k,l) >= ((l-1)(k-1)/4) k^(l-1).
```

This exceeds the conjectured value `k^l` whenever

```text
(l-1)(k-1) > 4k.
```

### 2.3 Explicitly excluded scope

This audit does **not** evaluate or claim:

- the exact value of `tilde#(4,10)`;
- a matching upper bound;
- the exact extremal function in Problem 3;
- classification of extremizers; or
- a second named open-problem solution.

The result under review refutes Conjecture 4 and supplies a lower-bound family. It
does not settle the broader exact-maximum Problem 3.

## 3. Original source and attribution

The original source located is:

- Boris Shapiro, “Problems Around Polynomials: The Good, The Bad and The Ugly…,”
  *Arnold Mathematical Journal* **1** (2015), 91–99.
- DOI: [10.1007/s40598-015-0008-4](https://doi.org/10.1007/s40598-015-0008-4)
- arXiv: [1503.05295](https://arxiv.org/abs/1503.05295)
- journal HTML: [Arnold Mathematical Journal article](https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/14-08/)
- author-hosted PDF: [ProblemsWithPolynomials.pdf](https://staff.math.su.se/shapiro/ProblemSolving/ProblemsWithPolynomials.pdf)

Problem 3 asks for the maximum number of isolated real zeros of the relevant sums
of squares. Conjecture 4 records the proposed equality `tilde#(2k,l)=k^l` and is
attributed to Giorgio Ottaviani and Boris Shapiro. The candidate's use of the name
“Ottaviani–Shapiro conjecture” and its target formula are source-faithful.

Crossref independently confirms the publication metadata and DOI:

- [Crossref work record](https://api.crossref.org/works/10.1007/s40598-015-0008-4)

## 4. Search coverage and method

The search was conducted independently of the proof audit and was aimed at both
exact formula collisions and equivalent prior theorems. It covered the following
routes through the stated cutoff.

| Route | Coverage performed |
|---|---|
| DOI and bibliographic metadata | Crossref DOI record and query searches; DOI resolution |
| Preprints | arXiv exact-phrase, title, abstract, author, and concept searches |
| Citation graph | OpenAlex citing works; Semantic Scholar metadata comparison |
| Journals | primary journal pages and DOI landing pages for the original and closest prior art |
| Author pages | current public publication/problem pages for Shapiro, Ottaviani, and Reznick |
| Proceedings and theses | Crossref type-filtered queries and OpenAlex dissertation searches |
| Problem/comment sites | exact searches over MathOverflow, Mathematics Stack Exchange, and indexed problem pages |
| Construction collision | exact strings, coefficients, zero count, threshold inequality, and formula fragments |
| Web repositories | indexed GitHub/web searches for the literal construction and count |

Representative exact searches included:

```text
"1152" "isolated real zeros" polynomial
"x_0^2" "t(t-8)" polynomial
"9*2^7" "sum of squares" polynomial zeros
"((l-1)(k-1)/4)" polynomial zeros
"(l-1)(k-1)>4k"
"Problem 3" "isolated zeros" "sums of squares"
"Conjecture 4" "isolated real zeros" polynomial
site:github.com "t(t-8)" "x_0^2"
site:mathoverflow.net "isolated real zeros" "sum of squares"
```

No relevant exact collision was returned.

## 5. Citation-network audit of the 2015 source

The live metadata services disagree on raw citation counts, which is itself a
reason not to treat any one index as complete:

- [Crossref](https://api.crossref.org/works/10.1007/s40598-015-0008-4) reported
  eight referencing records.
- [OpenAlex](https://api.openalex.org/works/https://doi.org/10.1007/s40598-015-0008-4)
  reported ten citing works and identified the source as `W2105159206`.
- Semantic Scholar's API metadata reported four citations during this audit.

The ten OpenAlex citing records were retrieved with:

- [OpenAlex citing-works query](https://api.openalex.org/works?filter=cites:W2105159206&per-page=200&select=id,doi,display_name,publication_year,primary_location)

The returned works concern other problems from Shapiro's compendium, including
univariate real-zero questions, Casas–Alvero/Abel–Goncharov problems, Newton-type
inequalities, critical points, and equilibrium configurations. None states or
implies the target sum-of-squares isolated-zero counterexample or lower-bound
family. Two representative inspected records are:

- [On the number of real zeros of polynomials of even degree](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/on-the-number-of-real-zeros-of-polynomials-of-even-degree/44FBEA3BF475A8745201AAA7533F69D7), addressing a different Shapiro conjecture.
- [Upper bounds for the number of isolated critical points via Thom–Milnor theory](https://arxiv.org/abs/2307.00312), addressing critical points rather than zeros of sums of squares.

No direct-citation record inspected resolved Conjecture 4.

## 6. Closest prior art

### 6.1 Choi–Lam–Reznick: finite zeros of positive semidefinite forms

The closest foundational source is:

- M.-D. Choi, T.-Y. Lam, and B. Reznick, “Real Zeros of Positive Semidefinite
  Forms. I,” *Mathematische Zeitschrift* **171** (1980), 1–26.
- DOI: [10.1007/BF01215051](https://doi.org/10.1007/BF01215051)
- archival record: [EuDML](https://eudml.org/doc/172919)

That paper studies homogeneous/projective maxima `B_{n,m}` and `B'_{n,m}` for
positive-semidefinite and sum-of-squares forms with finitely many real projective
zeros. Its Proposition 4.1 gives the standard sum-of-squares baseline construction

```text
sum_(i=1)^(n-1) product_(j=1)^r (x_i-j x_n)^2,
```

with `r^(n-1)` projective real zeros when the degree is `2r`. Under the standard
affine/projective translation, this is the predecessor of the baseline `k^l`; it
does not beat the baseline and does not contain the `1152` construction.

Proposition 4.2 supplies multiplicative/Chebyshev-style amplification mechanisms,
but no base witness or theorem was found there that yields either audited claim.

Reznick's public bibliography was also inspected:

- [Bruce Reznick publications](https://reznick.web.illinois.edu/reznickrpubs.html)

The related proceedings article
[Sums of squares of real polynomials](https://doi.org/10.1090/pspum/058.2/1327293)
does not supply a collision with the candidate result in its retrievable metadata
and available text.

### 6.2 Dressler: later status of SOS finite-zero maxima

- Mareike Dressler, “Real Zeros of SONC Polynomials,”
  arXiv [1909.06707](https://arxiv.org/abs/1909.06707),
  DOI [10.1016/j.jpaa.2020.106602](https://doi.org/10.1016/j.jpaa.2020.106602).

Dressler's abstract explicitly describes the analogous maxima for nonnegative and
SOS homogeneous forms as generally open, while solving the SONC analogue. This is
strong evidence that the broader SOS extremal problem was not already closed by a
standard theorem. It is not evidence of absolute novelty and it predates the
candidate construction.

### 6.3 Adjacent but non-colliding SOS literature

The following neighboring sources were checked and found to address different
questions:

- Giorgio Ottaviani, Philipp Reichenbach, and others on generic identifiability of
  SOS decompositions: [arXiv:2402.05189](https://arxiv.org/abs/2402.05189),
  DOI [10.1016/j.jalgebra.2024.07.052](https://doi.org/10.1016/j.jalgebra.2024.07.052).
- Degrees of varieties of sums-of-squares decompositions:
  [arXiv:2206.07473](https://arxiv.org/abs/2206.07473),
  DOI [10.1016/j.jpaa.2024.107638](https://doi.org/10.1016/j.jpaa.2024.107638).
- Biquadratic forms and sums of squares:
  DOI [10.1080/00927872.2013.865052](https://doi.org/10.1080/00927872.2013.865052).
- Noncoercive sums of squares:
  DOI [10.1016/j.jpaa.2009.05.012](https://doi.org/10.1016/j.jpaa.2009.05.012).
- A modern survey with a different focus:
  [Sums of Squares: A Real Projective Story](https://arxiv.org/abs/2101.05773).

None gives the target isolated-real-zero count, polynomial, or lower-bound family.

## 7. arXiv audit

Exact and concept searches included combinations of:

```text
"isolated zeros" AND "sums of squares"
"isolated real zeros"
"nonnegative polynomials" AND "isolated zeros"
"sum of squares" AND "real zeros"
```

The exact phrase search for “isolated zeros” and “sums of squares” returned only
an unrelated recent paper on odd powers. The broader searches recovered Dressler's
SONC paper and other non-colliding records, but no identical construction,
refutation, or family.

This was a metadata/abstract and retrievable-full-text search, not a theorem-by-
theorem inspection of every arXiv PDF containing generic SOS terminology.

## 8. Author-page audit

The following current public pages were inspected:

- [Boris Shapiro articles](https://staff.math.su.se/shapiro/Articles/)
- [Boris Shapiro problem-solving page](https://staff.math.su.se/shapiro/ProblemSolving/)
- [Giorgio Ottaviani publications](https://people.dimai.unifi.it/ottaviani/public.html)
- [Bruce Reznick publications](https://reznick.web.illinois.edu/reznickrpubs.html)

No listed publication or publicly linked manuscript was found containing the
candidate construction or lower-bound family. The continued presence of the 2015
problem PDF is not by itself proof that the conjecture remains open; it is only
corroborative source evidence.

## 9. Proceedings, theses, and problem-discussion audit

Crossref searches were filtered over `proceedings-article`, `dissertation`,
`journal-article`, and `posted-content` for combinations of isolated real zeros,
sums of squares, nonnegative polynomials, and the exact numerical/formula strings.
OpenAlex dissertation searches were run with both exact and broadened terminology.
No matching thesis or proceedings result was found.

Exact searches of indexed MathOverflow, Mathematics Stack Exchange, problem pages,
and web repositories found no public solution or matching construction. One
MathOverflow result concerning multivariate polynomials with prescribed real zeros
was inspected and is unrelated:

- [Multivariate polynomials with given real zeros](https://mathoverflow.net/questions/430566/multivariate-polynomials-with-given-real-zeros)

The public zbMATH serial page records the original article as `Zbl 1321.26032`:

- [zbMATH serial record](https://zbmath.org/serials/8523)

No exact resolution was found in the publicly accessible citation/related-record
surface.

## 10. Exact-construction collision assessment

No indexed source was found containing any of the following in the relevant
mathematical setting:

- the paired factors `t(t-8)` and `(t-i+1)(t-i)`;
- a `9*2^7=1152` count for a quartic SOS in ten variables;
- the displayed coefficient `((l-1)(k-1)/4)k^(l-1)`; or
- the violation threshold `(l-1)(k-1)>4k`.

This significantly lowers the probability of an exact public collision. It does
not exclude equivalent constructions written in transformed coordinates or under
different notation.

## 11. Separate priority adjudications

### 11.1 Explicit `(k,l)=(2,10)` witness

**Classification:** APPARENTLY_NEW  
**Confidence:** MODERATE

No identical witness, equivalent numerical count, or stronger published theorem
implying that witness was found. The 1980 baseline construction is strictly weaker
for this purpose.

### 11.2 Even-degree lower-bound family

**Classification:** APPARENTLY_NEW  
**Confidence:** MODERATE

No source was found stating or implying the exact family
`((l-1)(k-1)/4)k^(l-1)`. The literature contains baseline constructions and
general amplification ideas, but no located combination yields this family
without the candidate's new base/sign-slice construction.

### 11.3 Problem 3

**Classification:** NOT SOLVED BY THE AUDITED CLAIMS

Problem 3 asks for the exact maximum. The candidate supplies lower bounds and a
counterexample to Conjecture 4, but not an exact maximum. No release text should
describe it as solving Problem 3.

## 12. Remaining source and priority gaps

1. Full subscription MathSciNet reviews and cited-by networks were unavailable.
2. Full subscription-level zbMATH citation and review functionality was not
   available beyond public pages.
3. GitHub's authenticated code-search API returned HTTP 401 without a token; only
   web-indexed repository searches were used.
4. Citation services disagree on citation counts, demonstrating incomplete or
   non-identical indexing.
5. Search engines and bibliographic databases can miss unindexed proceedings,
   accepted-but-unpublished papers, non-English literature, and formulae embedded
   only in scanned PDFs.
6. Equivalent constructions may be presented after affine/projective coordinate
   changes or in homogeneous notation without the searched strings.
7. No direct inquiry was sent to Ottaviani, Shapiro, Reznick, Dressler, journal
   editors, or specialists in real algebraic geometry.
8. Private manuscripts, correspondence, seminar notes, and work posted after the
   exact cutoff cannot be excluded.

These gaps prevent a high-confidence or absolute-priority verdict.

## 13. Public-safe wording

Recommended status sentence:

> A documented literature search completed on 9 August 2026 found no earlier
> published or publicly posted identical construction, nor a result found to
> imply the stated even-degree lower-bound family. The construction and family
> are therefore apparently new relative to the sources searched. This is a
> negative-search conclusion, not an absolute historical-priority claim.

Recommended headline:

> An explicit counterexample to the Ottaviani–Shapiro all-positive formula, with
> an even-degree lower-bound family.

Wording to avoid:

- “the first counterexample”;
- “we solve Problem 3”;
- “the exact value is 1152”;
- “complete classification”;
- “second named solve”; or
- any assertion of peer review or full formal verification.

## 14. Final machine-readable adjudication

```text
AUDIT_CUTOFF_UTC: 2026-08-09T02:42:52Z
AUDIT_CUTOFF_LOCAL: 2026-08-09T09:42:52+07:00
AUDIT_TYPE: LIVE_INTERNET_LITERATURE_AND_PRIORITY
PROOF_CORRECTNESS_AUDITED_HERE: NO
ORIGINAL_STATEMENT_VERIFIED: YES
ORIGINAL_ATTRIBUTION_VERIFIED: YES
IDENTICAL_PRIOR_RESULT_FOUND: NO
STRONGER_PRIOR_RESULT_FOUND: NO
EXACT_FORMULA_COLLISION_FOUND: NO
EXACT_CONSTRUCTION_COLLISION_FOUND: NO
BASE_COUNTEREXAMPLE_PRIORITY: APPARENTLY_NEW
LOWER_BOUND_FAMILY_PRIORITY: APPARENTLY_NEW
NOVELTY_CONFIDENCE: MODERATE
CONJECTURE_4_REFUTATION_SCOPE: YES
PROBLEM_3_EXACT_MAXIMUM_SCOPE: NO
SECOND_NAMED_SOLVE_CLAIM: NO
ABSOLUTE_HISTORICAL_PRIORITY_CLAIM: NO
FIRST_INVALID_PRIORITY_INFERENCE: NONE WITHIN THE QUALIFIED WORDING
```

