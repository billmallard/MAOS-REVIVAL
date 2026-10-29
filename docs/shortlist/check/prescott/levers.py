"""Prescott Pusher on an Aeromomentum engine, turbo-normalised at altitude:
what moves useful load, range and cruise speed against the targets.

  python3 levers.py > levers_output.md

Basis (every input graded):
- Model: the stage 3 Prescott model (docs/shortlist/check/models/prescott-pusher.json),
  OpenVSP wetted areas, component build-up. Two drag bases, kept apart:
    "brochure basis"  k = 1.35, which reproduces the brochure's 165 KTAS at
                      7,500 ft and 75% (inside the fleet band 1.16-1.36);
    "measured basis"  k = 1.55, the middle of 1.46-1.67, the factors that
                      reproduce Kitplanes' measured 151 KTAS at 73% at sea level
                      to 7,500 ft (its altitude was not published).
- Engines (Aeromomentum, F): AM20T 260 hp take-off, 285 lb dry; AM15T 160 hp,
  215 lb dry. Continuous rating 75% (195 / 120 hp) and critical altitudes 8,000
  and 16,000 ft are OUR assumptions, as in the stage 3 check. Installed = dry x
  1.25 + 35 lb (radiator, coolant). BSFC 0.45 (E).
- Balance (E, ours): the engine sits in the tail cone about 8 ft behind the
  loaded CG, and nose ballast goes about 6 ft ahead of it, so every pound of
  engine added in the tail costs 8/6 lb of nose ballast to hold the CG where the
  O-360 had it (the Prescott's flight CG was already far aft: Wainfan; builders'
  ballast). A lighter engine earns the reverse.
- Structure delta: placeholders of 0, -100 and -200 lb until MANUFACTURING
  (AER-3784) gives its modern-rebuild estimate. Labelled ours.
- Fuel: 56.5 gal (prototype 2, P), 75 and 90 gal (E: wing leading-edge and
  integral tankage; the 15% wing's geometric volume is about 280 gal, and a
  typical usable fraction is 25-35%).
- Gross: 2,400 lb (as tested, F) and 2,700 lb (a re-derived structure designed
  for it, E).
"""
import json
import sys

HERE = "/maos-work/aero/analysis/AER-3783"
sys.path.insert(0, HERE)
import perf  # noqa: E402

M = json.load(open(f"{HERE}/models/prescott-pusher.json"))
WET = json.load(open(f"{HERE}/vsp/prescott-pusher_wet.json"))
O360_INSTALLED = 330.0
ENGINES = {"AM20T": (260.0, 285.0), "AM15T": (160.0, 215.0)}
BASES = {"brochure basis (k 1.35)": 1.35, "measured basis (k 1.55)": 1.55}
BALLAST_RATIO = 8.0 / 6.0


def installed(dry):
    return dry * 1.25 + 35.0


def empty_weight(base_empty, engine, struct_delta):
    d_eng = installed(ENGINES[engine][1]) - O360_INSTALLED
    ballast = d_eng * BALLAST_RATIO          # negative = ballast removed
    return base_empty + d_eng + ballast + struct_delta, d_eng, ballast


def case(engine, crit, k, gross, empty, fuel_gal):
    hp, _ = ENGINES[engine]
    eng = {"hp": hp, "cont_hp": 0.75 * hp, "crit_alt_ft": crit, "bsfc": 0.45}
    m = dict(M, drag_factor=k)
    P = perf.power_avail(eng, crit, 0.75)
    sp = perf.solve_speed(m, WET, eng, 0.92 * gross, crit, P)
    fuel_lb = fuel_gal * 6.0
    clb = 10 + 2 * 0.45 * (gross * crit / 0.75) / (550 * 3600)
    rng, _ = perf.cruise_range(m, WET, gross - clb, fuel_lb - clb, crit, sp["V_fts"], 0.45)
    eco = perf.solve_speed(m, WET, eng, 0.92 * gross, crit, 0.65 * P)
    if eco["ktas"] < 100.0:   # economy power below what holds level flight at this weight: the solver hit its bound
        rng_eco, eco_k = float("nan"), float("nan")
        return {"ktas": sp["ktas"], "range": rng, "eco_ktas": eco_k, "range_eco": rng_eco,
                "useful": gross - empty, "P": P}
    rng_eco, _ = perf.cruise_range(m, WET, gross - clb, fuel_lb - clb, crit, eco["V_fts"], 0.45)
    return {"ktas": sp["ktas"], "range": rng, "eco_ktas": eco["ktas"], "range_eco": rng_eco,
            "useful": gross - empty, "P": P}


def mark(ok):
    return "pass" if ok else "fail"


def tmark(ok):
    """Useful load and range are targets (Bill, 2026-10-25): met or short."""
    return "met" if ok else "short"


def main():
    out = []
    out.append("### A. Engine swap alone (published 1,550 lb empty, 2,400 lb gross, 56.5 gal)\n")
    out.append("| Engine, critical altitude | Basis | Empty incl. ballast, lb | Useful load | KTAS at continuous power | Range at continuous, nm | Economy KTAS / range, nm |")
    out.append("|---|---|---|---|---|---|---|")
    for e in ENGINES:
        emp, de, bal = empty_weight(1550.0, e, 0.0)
        for crit in (8000.0, 16000.0):
            for bn, k in BASES.items():
                r = case(e, crit, k, 2400.0, emp, 56.5)
                out.append(f"| {e}, {crit/1000:.0f}k ft | {bn} | {emp:,.0f} ({de:+.0f} engine, {bal:+.0f} ballast) | {r['useful']:,.0f} | "
                           f"{r['ktas']:.0f} | {r['range']:,.0f} | {r['eco_ktas']:.0f} / {r['range_eco']:,.0f} |")
    out.append("")
    out.append("### B. The levers together: AM20T, 16,000 ft critical altitude (the optimistic engine case)\n")
    out.append("Targets: useful load 1,000 lb; range 1,000 nm (still air, no reserve, full fuel, at continuous power, and at economy in brackets); cruise above 160 KTAS (180 preferred).\n")
    out.append("| Gross, lb | Structure delta, lb | Fuel, gal | Basis | Useful load | KTAS | Range, nm (economy) | Load / range targets, speed floor |")
    out.append("|---|---|---|---|---|---|---|---|")
    for gross in (2400.0, 2700.0):
        for sd in (0.0, -100.0, -200.0):
            for fuel in (56.5, 75.0, 90.0):
                emp, _, _ = empty_weight(1550.0, "AM20T", sd)
                if gross > 2400:
                    emp += 0.10 * (gross - 2400)      # E: structure grows about 10% of the added gross
                if emp + fuel * 6.0 > gross:
                    continue
                for bn, k in BASES.items():
                    r = case("AM20T", 16000.0, k, gross, emp, fuel)
                    fl = (f"{tmark(r['useful'] >= 1000)} / {tmark(r['range'] >= 1000)}"
                          f"{' (eco ' + tmark(r['range_eco'] >= 1000) + ')' if r['range'] < 1000 and r['range_eco'] == r['range_eco'] else ''} / "
                          f"{mark(r['ktas'] > 160)}{'+' if r['ktas'] >= 180 else ''}")
                    out.append(f"| {gross:,.0f} | {sd:+.0f} | {fuel:g} | {bn.split(' (')[0]} | {r['useful']:,.0f} | {r['ktas']:.0f} | "
                               f"{r['range']:,.0f} ({'no level-flight solution at 65%' if r['range_eco'] != r['range_eco'] else format(r['range_eco'], ',.0f')}) | {fl} |")
    out.append("")
    out.append("### C. Same, AM15T (lighter in the tail), 16,000 ft\n")
    out.append("| Gross, lb | Structure delta, lb | Fuel, gal | Basis | Useful load | KTAS | Range, nm (economy) | Load / range targets, speed floor |")
    out.append("|---|---|---|---|---|---|---|---|")
    for gross in (2400.0, 2700.0):
        for sd in (0.0, -200.0):
            for fuel in (56.5, 90.0):
                emp, _, _ = empty_weight(1550.0, "AM15T", sd)
                if gross > 2400:
                    emp += 0.10 * (gross - 2400)
                for bn, k in BASES.items():
                    r = case("AM15T", 16000.0, k, gross, emp, fuel)
                    fl = (f"{tmark(r['useful'] >= 1000)} / {tmark(r['range'] >= 1000)}"
                          f"{' (eco ' + tmark(r['range_eco'] >= 1000) + ')' if r['range'] < 1000 and r['range_eco'] == r['range_eco'] else ''} / "
                          f"{mark(r['ktas'] > 160)}{'+' if r['ktas'] >= 180 else ''}")
                    out.append(f"| {gross:,.0f} | {sd:+.0f} | {fuel:g} | {bn.split(' (')[0]} | {r['useful']:,.0f} | {r['ktas']:.0f} | "
                               f"{r['range']:,.0f} ({'no level-flight solution at 65%' if r['range_eco'] != r['range_eco'] else format(r['range_eco'], ',.0f')}) | {fl} |")
    print("\n".join(out))


if __name__ == "__main__":
    main()
