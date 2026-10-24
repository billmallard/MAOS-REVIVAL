# docs/shortlist — stage 3 working files

The ranking and its reasoning are in [`../SHORTLIST.md`](../SHORTLIST.md). This
folder holds what produced it.

| Path | What it is |
|---|---|
| `check/geometry/<id>.json` | Published geometry, weights, performance points, safety record and rights hints per type, each number graded (F/T/P/B/R/E) with its URL. Format in `check/geometry/SCHEMA.md`. Collected 2026-10-24 from public sources only |
| `check/models/<id>.json` | The analysis model per type: the geometry actually used, every estimate listed under `assumptions`, drag build-up inputs, published calibration points, engine and weights |
| `check/vspgen.py` | Writes and runs the OpenVSP script for a model; CompGeom wetted areas to `check/vsp/<id>_wet.json` |
| `check/perf.py` | Drag build-up, propeller, power lapse and Breguet range integration. Methods and sources in its docstring |
| `check/run_check.py` | Runs one model: calibration against published points, original-engine range and payload, the two Aeromomentum cases. Writes `check/results/<id>.json` and `.txt` |
| `check/calib.json` | The fleet drag calibration (1.29) and the three cases it comes from |
| `check/report.py` | Builds `check/results/tables.md` and the per-type `check/results/<id>_stage3.md` tables |
| `narrative.py` | AERO's stage 3 prose per type; writes the stage 3 block into each `../candidates/<id>.md` between markers |

To regenerate, see "Reproduce" at the end of `../SHORTLIST.md`, then run
`python3 docs/shortlist/narrative.py` from the repo root.
