# Release staging

No immutable release exists yet. This directory contains the deterministic
public-safe assets and final `v1.0.0` release notes.

The planned immutable release asset set is:

- `paper/manuscript.pdf` — exact frozen three-page PDF;
- `paper/manuscript.tex` — designated source;
- `SHA256SUMS.txt` — complete repository ledger; and
- `release/EVIDENCE_BUNDLE.zip` — deterministic sanitized evidence subset.

`EVIDENCE_BUNDLE.sha256` records the archive hash.
`RELEASE_ASSET_SHA256SUMS.txt` records the PDF, TeX, and evidence-bundle hashes.
The builder synthesizes an internal bundle manifest, checksum ledger, and
replay README and is checked by the repository verification workflow.

The repository remains private until its owner changes visibility. Public
default-branch CI, badge activation, branch-protection verification, the
immutable tag/release, DOI publication, and anonymous public-page checks remain
post-visibility gates. The staged assets do not themselves assert that those
gates have passed.
