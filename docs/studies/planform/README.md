# Planform study: inputs, scripts and results

The study itself is [`../planform.md`](../planform.md). This folder holds what
produced it, so every number can be regenerated rather than trusted.

The scripts drive the `maos` tool containers (AVL, OpenVSP), which see
`/maos-work/aero/analysis` as `/workspace/analysis`. Copy this folder to
`/maos-work/aero/analysis/AER-3807` and run, in order:

```
python3 planform.py            # rule A, same touchdown speed -> results/sweep_V.json
python3 planform.py --rule S   # rule B, same wing area      -> results/sweep_S.json
python3 calib.py               # real designs                 -> results/calib.json
python3 report.py --doc        # results/tables.md and ../planform.md
```

Each sweep run writes one AVL deck per point (`avl/pf_<point>_<rule>.avl`, with
force reports at alpha 0 and 4 deg) and one OpenVSP script per point
(`vsp/pf_<point>_<rule>.vspscript`, CompGeom wetted areas in `_wet.json`).
`perf.py` and `vspgen.py` are copied unchanged from the stage 3 check
(AER-3783). A full rule run takes about two minutes.
