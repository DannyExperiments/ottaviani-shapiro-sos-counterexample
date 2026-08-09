# A counterexample to the Ottaviani--Shapiro isolated-zero conjecture

<!--
Activate these badges only after the repository is public and all three named
workflows pass on its default branch:

[![Verify public evidence](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/verify.yml/badge.svg)](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/verify.yml)
[![Verifier replay](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/replay.yml/badge.svg)](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/replay.yml)
[![PDF build](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/pdf.yml/badge.svg)](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/pdf.yml)

No Lean badge is authorized: no scope-matched theorem is kernel checked.
The PDF has passed private page-by-page visual preflight, but its badge remains
hidden until the workflow passes on the public default branch.
-->

This repository gives a negative answer to the universal equality conjectured
by Ottaviani and Shapiro for isolated real zeros of nonnegative sums of
squares. It exhibits a quartic sum of squares in ten variables with exactly
`1152` isolated real zeros, exceeding the conjectured value `2^10=1024`.

The proof, designated manuscript source, frozen three-page PDF, public-safe
audit reports, and deterministic replay bundle are included below. The result
refutes Conjecture 4; it does **not** determine the exact maximum in Problem 3.

## Original problem

For integers `k,l>=1`, let `tilde#(2k,l)` be the maximum number of isolated
real zeros of a real nonnegative polynomial in `l` variables, of degree at
most `2k`, which is a finite sum of squares of real polynomials of degree at
most `k`. Problem 3 and Conjecture 4 in Boris Shapiro's 2015 paper record the
bounds

```text
k^l <= tilde#(2k,l) <= (2k-1)^l
```

and conjecture `tilde#(2k,l)=k^l`. The problem is attributed there to
Giorgio Ottaviani and Boris Shapiro.

Authoritative source: Boris Shapiro, *Problems Around Polynomials: The Good,
The Bad and The Ugly...*, Arnold Mathematical Journal 1 (2015), 91--99,
[DOI 10.1007/s40598-015-0008-4](https://doi.org/10.1007/s40598-015-0008-4),
[arXiv:1503.05295](https://arxiv.org/abs/1503.05295).

## Counterexample

In variables `t,x_0,...,x_8`, define

```text
q_0 = x_0^2 + t(t-8),
q_i = x_i^2 - (t-i+1)(t-i),   1<=i<=8,
P   = q_0^2 + q_1^2 + ... + q_8^2.
```

Then `P` is a nonnegative quartic SOS. Its real zeros have
`t in {0,1,...,8}`. On each `t`-slice exactly two radicands vanish and the
other seven have two independent sign choices. Hence

```text
# Z_R(P) = 9*2^7 = 1152 > 2^10 = 1024.
```

The real zero set is finite, so all 1152 zeros are isolated. Therefore

```text
tilde#(4,10) >= 1152 > 2^10,
```

which refutes the conjectured universal equality.

## Stronger audited family

The same canonical proof gives, for every even `k>=2` and `l>=3`,

```text
tilde#(2k,l) >= ((l-1)(k-1)/4) k^(l-1).
```

It violates `tilde#(2k,l)=k^l` exactly when
`(l-1)(k-1)>4k`. This is a lower-bound construction. It does **not**
determine the exact extremal function, prove `tilde#(4,10)=1152`, or classify
extremizers.

[Problem and proof](proof/PROBLEM_AND_PROOF.md) ·
[Paper (PDF)](paper/manuscript.pdf) ·
[Designated manuscript TeX](paper/manuscript.tex) ·
[Release notes](release/RELEASE_NOTES_v1.0.0.md) ·
[Reproduce](REPRODUCIBILITY.md) ·
[Citation metadata](CITATION.cff) ·
[Mathematical audit](audits/public_safe_reports/MATHEMATICAL_AUDIT.md) ·
[Live literature/priority audit](audits/public_safe_reports/LITERATURE_PRIORITY_AUDIT.md) ·
[Architecture/terminology priority audit](audits/public_safe_reports/PRIORITY_AUDIT_ARCHITECTURE_2026-08-09.md) ·
[Formalization status](formalization/README.md) ·
[Claim/evidence matrix](CLAIMS_EVIDENCE_MATRIX.md) ·
[Deterministic evidence bundle](release/EVIDENCE_BUNDLE.zip)

The paper is directly readable above. Workflow badges remain hidden until all
three workflows pass on the public default branch. A release link and DOI badge
will be added only after the immutable release and DOI deposits exist.

## Verification status

| Gate | Current status |
|---|---|
| Symbolic counterexample | Audited; exact count `1152` |
| Exact replay scripts | Present; corroborating, not load-bearing |
| General lower-bound family | Audited after boundary repairs |
| Exact extremal maximum | Open |
| Literature/priority | `PRIORITY_AUDIT_PASS_QUALIFIED`: apparently new after documented search through 2026-08-09, moderate confidence; generic/product-grid/SOS ingredients are prior art; absolute priority unclaimed. Three independent lanes are frozen. |
| Human specialist review | Not obtained |
| Lean/Aristotle | No kernel-checked formalization yet; request packet only |
| Manuscript source | Designated source; source QA and hostile source-level audit `PASS` |
| Manuscript PDF | Frozen 3-page A4 artifact rebuilt by PR CI; SHA-256 `32dd500a3a58a944387cb2cd73dcd0aa446d40a993733bbe3e9ddef8e19cb110`; visual preflight `PASS` |

## Authorship and disclosure

The citation name follows the repository owner's established convention,
`DannyExperiments`. AI systems assisted discovery, proof development,
mathematical and literature auditing, and repository assembly. No AI system is
proposed as an author. See [AI_DISCLOSURE.md](AI_DISCLOSURE.md).
