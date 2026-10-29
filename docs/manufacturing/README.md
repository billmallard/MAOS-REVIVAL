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

# Build plans (AER-3868)

`build_plans.py` holds the part-count build-up per assembly (with the make/buy
split), the tooling lines and the kit-run crossover for the Aries and both
Prescott routes. `build_plans.json` is its `--json` output. The tables in
`docs/candidates/*-manufacturing.md` come from it.

    python3 build_plans.py          # print the tables
    python3 build_plans.py --json   # rewrite build_plans.json

`price-check-2026-10-25.md` holds the dated public prices for tooling board,
print bureaus and cutting services that the plans use.
