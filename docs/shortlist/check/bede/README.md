# Bede BD-4C / BD-19 reference check (AER-4145)

The Bede BD-4C and BD-19 are reference designs beside the Cozy MKIV, not
candidates. Their dossiers are `docs/candidates/bede-bd-4c.md` and
`docs/candidates/bede-bd-19.md`.

- `../models/bede-bd-4c.json` and `../models/bede-bd-4c-80gal.json`: the
  stage 3 model, on Bede's published geometry, with 51 and 80 gal. The BD-19
  publishes no geometry, so it has no model of its own; the BD-4C model
  stands in for it.
- `bede_check.py`: Bede publishes speeds without an altitude, so no point can
  calibrate the model. The script asks what the fleet-calibrated model says
  about those speeds and about the published range. It runs the sensitivity
  to what the model had to assume, and gives useful load on the AM20T at
  every empty weight on record. It also tests the builder-reported N2468Z
  points, and the AM20T on that airplane's as-first-flown drag. Output:
  `bede_check_output.md`.

Every number is ours (E). The sources and their grades are in the dossiers.

## Reproduce

```sh
cp -r docs/shortlist/check /maos-work/aero/analysis/AER-3783    # copy by read/write on the network share; see SHORTLIST.md
cd /maos-work/aero/analysis/AER-3783
python3 run_check.py models/bede-bd-4c.json > results/bede-bd-4c.txt
python3 run_check.py models/bede-bd-4c-80gal.json > results/bede-bd-4c-80gal.txt
python3 report.py
python3 payload_range.py > payload_range_output.md
python3 axes/axes.py > axes/axes_output.md
python3 bede/bede_check.py > bede/bede_check_output.md
```
