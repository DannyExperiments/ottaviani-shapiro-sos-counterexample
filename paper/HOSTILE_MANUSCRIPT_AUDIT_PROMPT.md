# Hostile manuscript audit prompt

You are an adversarial referee. Read `manuscript.tex`, the compiled
`manuscript.pdf` if and only if it has been supplied,
`CLAIM_SCOPE_AND_LIMITATIONS.md`, and the source/audit provenance. Find the
first false inference or inflated conclusion; do not merely edit exposition.
If no PDF is supplied, return `PDF_AND_TEX_CONCORDANT: NOT_TESTED` rather than
inferring a build result.

Audit independently:

1. the exact meaning of `tilde#(2k,l)` and unrestricted number of SOS
   summands;
2. the literal quartic construction, the forced values `t=0,...,8`, the two
   zero radicands per slice, and the exact count `9*2^7=1152`;
3. finiteness and isolation of the real zero set;
4. the real-radical fiber decomposition;
5. the free `C[t]`-basis, regular-sequence/unmixed complete-intersection
   conclusion, and absence of hidden zero-dimensional complex components;
6. every sign interval, boundary count, epsilon inequality, root count, and
   degree bound in the even-`k` family, especially `(k,l)=(2,3)` where `M=0`;
7. the exact simplification to `((l-1)(k-1)/4)k^(l-1)`;
8. the odd-`k` transfer using `e=2 floor(k/2)` only for `k>=2`;
9. that the manuscript refutes the formula but does not determine the exact
   extremal function or prove optimality of `1152`;
10. whether any DOI, arXiv, journal, problem-page, repository, or adjacent
    theorem already contains an identical construction or stronger result.

Required output:

```text
MANUSCRIPT_VERDICT: PASS / FAIL / INCOMPLETE
FIRST_INVALID_INFERENCE: exact location or NONE
BASE_COUNTEREXAMPLE_VALID: YES / NO
EXACT_1152_COUNT_VALID: YES / NO
COMPLEX_LOCUS_ARGUMENT_VALID: YES / NO
EVEN_FAMILY_VALID: YES / NO
SCOPE_BOUNDARY_CORRECT: YES / NO
NOVELTY_LANGUAGE_SAFE: YES / NO
PDF_AND_TEX_CONCORDANT: YES / NO
REQUIRED_REPAIRS:
CONFIDENCE: HIGH / MODERATE / LOW
```
