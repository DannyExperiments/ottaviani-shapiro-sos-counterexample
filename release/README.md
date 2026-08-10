# Release staging

No immutable release exists yet. This directory contains the deterministic
public-safe assets and final `v1.0.0` release notes.

The planned immutable release asset set is:

- `ottaviani-shapiro-sos-counterexample-v1.0.0.pdf` — exact frozen three-page PDF;
- `ottaviani-shapiro-sos-counterexample-v1.0.0.tex` — designated source;
- `references.bib` — manuscript bibliography;
- `CITATION.cff` — versioned citation metadata; and
- `ottaviani-shapiro-sos-counterexample-public-evidence-v1.0.0.zip` —
  deterministic sanitized evidence subset.

`EVIDENCE_BUNDLE.sha256` records the archive hash.
`RELEASE_ASSET_SHA256SUMS.txt` records all five release-asset hashes. Exact
renamed copies and their checksum ledger are assembled under
`release/staging/v1.0.0/`; this local directory is staging evidence, not a tag
or published GitHub release.
The builder synthesizes an internal bundle manifest, checksum ledger, and
replay README and is checked by the repository verification workflow.

The repository is public. All three default-branch workflows pass, and the
repository, Actions page, badge images, and badge targets were anonymously
tested. Default-branch protection and repository release immutability were
live-verified on 2026-08-10. The immutable tag/release, DOI publication, and
external notice remain pending. The staged assets do not themselves assert that
those later gates have passed.
