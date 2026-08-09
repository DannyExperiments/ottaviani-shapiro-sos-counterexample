# Status

## Mathematical scope

The explicit quartic SOS counterexample and its exact `1152`-point count have
passed independent hostile mathematical review after three scoped repairs:

1. complex-component purity is derived from a finite-free, unmixed
   complete-intersection argument;
2. the family parameter is stated as `M>=0`, including `(k,l)=(2,3)`;
3. largest-even transfer is restricted to `k>=2` (odd `k>=3`).

The conjectured equality is refuted. The exact maximum remains open.

## Priority

A documented search through 2026-08-09 found no earlier identical
`(k,l)=(2,10)` construction, exact count `1152`, or theorem implying the
displayed family. All three independent priority lanes are frozen. Their
qualified determination is:

> **PRIORITY_AUDIT_PASS_QUALIFIED:** apparently new after documented search
> through 2026-08-09, moderate confidence; generic/product-grid/SOS ingredients
> are prior art; absolute priority unclaimed.

The candidate refutes Conjecture 4 only. It does not determine the exact
maximum requested by Problem 3.

## Verification categories

- **Proof:** symbolic and self-contained.
- **Scripts:** exact corroborating count and family-incidence replay; not the
  proof.
- **Formalization:** not yet kernel checked. A feasibility report and request
  packet are included.
- **Manuscript:** `paper/manuscript.tex` is the designated source and
  `paper/manuscript.pdf` is the frozen three-page A4 artifact. Its SHA-256 is
  `32dd500a3a58a944387cb2cd73dcd0aa446d40a993733bbe3e9ddef8e19cb110`.
  Source QA, scope comparison, PDF metadata checks, text privacy extraction,
  embedded-font checks, and page-by-page visual preflight pass. The exact PDF
  was rebuilt successfully on the release-hardening PR at commit
  `7c2eb4031131923f98fe4779f17a6d6578fea1ea`. The public default-branch PDF
  workflow then passed at main commit
  `78a6a49461df990abf01a8d5089fcd074002fd36` in run `31296200849`, job
  `93201578150`; artifact `9033026233` has API-recorded digest
  `sha256:a796fa661318c52403d61e62450f8228123dd622e5c0c2c2ab62248bfc0a68ac`,
  and artifact parity passed. All three workflow badges and targets were
  anonymously tested and report passing.
- **Peer review:** no human specialist report has been obtained.
- **Publication:** the repository is public, but no immutable versioned GitHub
  release, journal acceptance, or DOI is asserted.

## Release state

`PUBLIC_MAIN_CI_PASS_RELEASE_PENDING`, `MANUSCRIPT_PASS`, and
`PRIORITY_AUDIT_PASS_QUALIFIED`.

Authorship (`DannyExperiments`), the AI disclosure, and the all-rights-reserved
no-license status are finalized for this release. Public visibility,
public-default-branch CI, and badge activation are complete. Default-branch
protection, an immutable `v1.0.0` release, DOI publication, and external
notices remain separate gates.
