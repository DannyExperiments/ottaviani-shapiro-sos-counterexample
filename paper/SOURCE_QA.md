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
- PDF status is recorded separately in `BUILD_LOG.txt` and `BUILD_STATUS.md`.
