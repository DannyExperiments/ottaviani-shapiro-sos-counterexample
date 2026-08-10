# Release record and frozen staging

Immutable GitHub Version 1.0.0 was published on 2026-08-10 from commit
`b778a50ee4d9ec0ad217dcf7ab23a9ce1b020eba`:

<https://github.com/DannyExperiments/ottaviani-shapiro-sos-counterexample/releases/tag/v1.0.0>

The release is archived at version DOI `10.5281/zenodo.21875290`; concept DOI
`10.5281/zenodo.21875289` represents all Zenodo versions.

The planned immutable release asset set is:

- `ottaviani-shapiro-sos-counterexample-v1.0.0.pdf` — exact frozen three-page PDF;
- `ottaviani-shapiro-sos-counterexample-v1.0.0.tex` — designated source;
- `references.bib` — manuscript bibliography;
- `CITATION.cff` — versioned citation metadata; and
- `ottaviani-shapiro-sos-counterexample-public-evidence-v1.0.0.zip` —
  deterministic sanitized evidence subset.

`EVIDENCE_BUNDLE.sha256` records the archive hash.
`RELEASE_ASSET_SHA256SUMS.txt` records all five release-asset hashes. Exact
renamed copies and their checksum ledger are preserved under
`release/staging/v1.0.0/`. They are frozen evidence of the immutable tag and
must not be regenerated from later current-main metadata. In particular, the
staged `CITATION.cff` is the released asset; the root `CITATION.cff` contains
the later DOI metadata and actual 2026-08-10 release date.
The builder synthesized an internal bundle manifest, checksum ledger, and
replay README. The repository verification workflow now pins the exact
published archive and asset-ledger hashes.

The repository is public. All three default-branch workflows pass, and the
repository, Actions page, badge images, and badge targets were anonymously
tested. Default-branch protection and repository release immutability were
live-verified on 2026-08-10. The immutable tag/release and DOI publication are
complete. External notice remains pending and requires separate approval.
