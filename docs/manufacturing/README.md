# Stage 4 rebuild weights

`rebuild_weights.json` holds, per design, the starting empty weight (with its
source and grade), each rebuild item as a signed light/heavy delta in lb with
its basis and grade, and the engine-swap change from our per-variant engine
check. `weights.py` sums them into the ranges used in `docs/MANUFACTURING.md`
and in each dossier's stage 4 section; `results.json` is its `--json` output.

    python3 weights.py          # print the tables
    python3 weights.py --json   # rewrite results.json

Everything here is a desk estimate (AER-3784, 2026-10-24). The method and the
laminate arithmetic behind the composite items are in `docs/MANUFACTURING.md`.
