# Aristotle request: exact Ottaviani--Shapiro counterexample

Formalize in Lean the following explicit theorem. Do not formalize the
general family in this request.

Use variables `t,x_0,...,x_8 : Real` and define

```text
q_0 = x_0^2 + t(t-8),
q_i = x_i^2 - (t-i+1)(t-i), 1<=i<=8,
P   = sum_(i=0)^8 q_i^2.
```

Prove:

1. `P=0` iff every `q_i=0`.
2. Every zero has `t in {0,1,...,8}`.
3. For each such `t`, exactly two of the nine radicands are zero and seven
   are positive.
4. The real zero set is finite with cardinality `9*2^7=1152`.
5. `1152>2^10`.

Deliver a complete pinned Lean project. Do not use `sorry`, `admit`, unsafe
shortcuts, unapproved axioms, or theorem-shaped placeholders. Include a clean
build log, no-placeholder scan, `#print axioms` output for the headline
theorem, and a statement-equivalence note comparing the formal theorem with
the specification above.

If the cardinality proof is too large, return the strongest fully compiling
dependency theorem and identify the exact first missing lemma. Do not report
a dashboard state as a completed formalization.
