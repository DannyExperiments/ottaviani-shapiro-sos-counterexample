# Source-level QA

- TeX brace stack: balanced.
- `begin{document}` / `end{document}`: exactly one each.
- Abstract: four sentences, within the six-sentence limit.
- Author entry: none.
- Paper and margin settings: `amsart`, `a4paper`, one inch.
- Claim-scope scan: the conjectural formula is refuted; the exact extremal
  function and optimality of `1152` are explicitly excluded.
- Exact verifier replay: base count and audited family arithmetic both pass;
  see `VERIFIER_REPLAY_LOG.txt`.
- Private-data scan: no user name, username, email, home path, token, cookie,
  credential, wallet material, or private key detected.
- Frozen PDF SHA-256:
  `3622e8746ce08f94d4d42a6b0acb5628c10945c2afe2c8c7d03a35f42ba026a4`.
- PDF scope comparison, metadata, text privacy, embedded-font, and visual
  preflight: `PASS`; see `PDF_PREFLIGHT.md`.
