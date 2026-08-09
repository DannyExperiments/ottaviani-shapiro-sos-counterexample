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
`RELEASE_ASSET_SHA256SUMS.txt` records all five release-asset hashes.
The builder synthesizes an internal bundle manifest, checksum ledger, and
replay README and is checked by the repository verification workflow.

The repository remains private until its owner changes visibility. Public
default-branch CI, badge activation, branch-protection verification, the
immutable tag/release, DOI publication, and anonymous public-page checks remain
post-visibility gates. The staged assets do not themselves assert that those
gates have passed.
