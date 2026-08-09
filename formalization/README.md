# Formalization status

No theorem in this repository is currently kernel checked. The included
materials are a feasibility/dependency analysis and a request packet, not a
Lean or Aristotle certificate.

The preferred first target is the exact quartic witness theorem:

1. the displayed `P` is a degree-four sum of nine squares;
2. `P=0` has exactly 1152 real solutions; and
3. `1152>2^10`.

The general even-degree family should be attempted only after the exact
witness is scope-matched and rebuilt without placeholders.

No formalization badge is authorized at this stage.

The Aristotle request ZIP retains its original assembly timestamps. Those
timestamps are nonsemantic: the archive bytes are covered by the repository
checksum ledger, and no deterministic packet generator exists in this
candidate. The archive was therefore not repacked merely to normalize ZIP
metadata.
