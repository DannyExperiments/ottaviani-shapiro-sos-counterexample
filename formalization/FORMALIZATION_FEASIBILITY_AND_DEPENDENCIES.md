# Formalization feasibility and dependencies

## Assessment

```text
BASE_COUNTEREXAMPLE_FEASIBILITY: HIGH
EXACT_1152_CARDINALITY_FEASIBILITY: MODERATE_TO_HIGH
REAL_RADICAL_DECOMPOSITION_FEASIBILITY: MODERATE
FINITE_FREE_COMPLEX_LOCUS_FEASIBILITY: MODERATE
GENERAL_EVEN_FAMILY_FEASIBILITY: MODERATE
CURRENT_KERNEL_VERIFICATION: NONE
```

The headline counterexample is unusually suitable for formalization because
it is finite, explicit, and reduces to real inequalities, a nine-element
finite index set, and exact cardinality arithmetic. The proof does not need a
computer algebra system or an imported classification theorem.

## Minimal material kernel

The first scope-matched theorem should define the nine radicands

```text
a_0(t)=t(8-t),
a_i(t)=(t-i+1)(t-i), 1<=i<=8,
```

and the zero set of `P=sum q_i^2`. It should prove an equivalence between
zeros and a finite disjoint union indexed by `j in Fin 9`, where two
coordinates are zero and seven independently choose a square root sign. From
that equivalence, prove cardinality `9*2^7=1152` and the strict inequality
against `2^10`.

## Dependency order

1. `sq_nonneg` and `sum_eq_zero_iff_of_nonneg` for `P=0 iff all q_i=0`.
2. Interval sign lemmas for `(t-i+1)(t-i)`.
3. Finite-disjunction theorem `t=0 or ... or t=8`.
4. Root-cardinality lemma: `x^2=a` has one real solution when `a=0` and two
   when `a>0`.
5. Product-cardinality lemma for seven independent sign coordinates.
6. Disjointness of the nine `t`-fibers.
7. Exact arithmetic `9*2^7=1152>2^10`.

## Lean plan

- Pin Lean and mathlib before implementation.
- Prefer `Fin 9`, `Finset`, and finite sets over hand-expanded tuples.
- Represent the zero set as a `Set` first; introduce a `Fintype` only after
  the explicit equivalence is proved.
- Avoid `Real.sqrt` where possible by using a two-root lemma; if square roots
  are used, isolate the positivity hypotheses.
- The public theorem must be rebuilt with no `sorry`, `admit`, unsafe code,
  or theorem-shaped axioms; record `#print axioms`.

## Aristotle plan

Submit the exact base theorem and dependency map only. If the full 1152-count
request times out, split at the finite-fiber decomposition and cardinality
product lemma. A dashboard state or returned archive is not evidence until
downloaded, inspected, rebuilt, and scope-matched.

## Deferred targets

The real-radical and finite-free complex-locus claims are mathematically
valuable but not required to refute the conjecture. The general family also
adds substantial polynomial root-separation machinery. They should not delay
the base formalization or be conflated with it.

