# A counterexample to the Ottaviani--Shapiro isolated-zero conjecture

<!--
Activate these badges only after the clean repository exists publicly and both
named workflows pass on its default branch:

[![Verify public evidence](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/verify.yml/badge.svg)](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/verify.yml)
[![Verifier replay](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/replay.yml/badge.svg)](https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/actions/workflows/replay.yml)

No Lean badge is authorized: no scope-matched theorem is kernel checked.
No PDF badge is authorized: no compiled or visually inspected PDF exists.
-->

This repository gives a negative answer to the universal equality conjectured
by Ottaviani and Shapiro for isolated real zeros of nonnegative sums of
squares. It exhibits a quartic sum of squares in ten variables with exactly
`1152` isolated real zeros, exceeding the conjectured value `2^10=1024`.

> **Prepublication status.** This is a private local public-candidate skeleton.
> The audited proof and designated private manuscript TeX are present, and
> manuscript source QA passes. No PDF exists; compile and visual preflight,
> public CI runs, human release approvals, immutable release, and DOI do not
> yet exist. The
> badge definitions are staged in a hidden comment for the intended repository
> name and must remain hidden until future public default-branch runs succeed.

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
[Designated manuscript TeX](paper/manuscript.tex) ·
[Reproduce](REPRODUCIBILITY.md) ·
[Mathematical audit](audits/public_safe_reports/MATHEMATICAL_AUDIT.md) ·
[Priority audit](audits/public_safe_reports/LITERATURE_PRIORITY_AUDIT.md) ·
[Formalization status](formalization/README.md) ·
[Claim/evidence matrix](CLAIMS_EVIDENCE_MATRIX.md)

The final paper link, PDF-build badge, release link, and DOI badge are
deliberately withheld until the manuscript and immutable public release pass
their separate gates.

## Verification status

| Gate | Current status |
|---|---|
| Symbolic counterexample | Audited; exact count `1152` |
| Exact replay scripts | Present; corroborating, not load-bearing |
| General lower-bound family | Audited after boundary repairs |
| Exact extremal maximum | Open |
| Literature/priority | Comprehensive documented negative-search audit through 2026-08-09; apparently new with moderate confidence; no absolute-priority claim |
| Human specialist review | Not obtained |
| Lean/Aristotle | No kernel-checked formalization yet; request packet only |
| Manuscript source | Designated private candidate; source QA and hostile source-level audit `PASS` |
| Manuscript PDF | Not compiled; visual preflight not run; exact Tectonic resource approval pending |

## Authorship and disclosure

The planned citation name follows the owner's established repository
convention, `DannyExperiments`; it remains subject to human approval before
release. AI systems assisted discovery, proof development, mathematical and
literature auditing, and repository assembly. No AI system is proposed as an
author. See [AI_DISCLOSURE.md](AI_DISCLOSURE.md).
