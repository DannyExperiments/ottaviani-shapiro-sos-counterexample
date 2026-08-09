# Lean target (not yet implemented)

Target environment: choose and pin the current stable Lean 4 and a matching
mathlib revision at implementation time.

Required public theorem scope:

```text
There is an explicit degree-four SOS polynomial in ten real variables whose
real zero set has cardinality 1152; hence the conjectured bound 2^10 is
violated.
```

Acceptance requirements: clean rebuild, no placeholders, no unexpected
axioms, exact statement-equivalence report, and a CI workflow. Until those
requirements pass, do not add a Lean badge.

