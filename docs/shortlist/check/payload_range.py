"""Payload-range on the AM20T for every shortlisted design (AER-3900).

  python3 payload_range.py > payload_range_output.md

Bill's ruling (2026-10-25): useful load and range are targets to report against, and
there is no joint pass/fail on the two. This reports the tradeoff instead: the
payload (occupants and baggage) each design carries over 600, 800, 1,000 and
1,200 nm, with no reserve and with a 45 min reserve.

Basis: nothing new is assumed. Every input is the stage 3 check's, unchanged:
- Models, wetted areas and drag factors: results/<id>.json (run_check.py), so
  each design uses the same calibrated drag as the SHORTLIST results table.
- Engine: AM20T, 195 hp assumed continuous, critical altitude 8,000 ft
  (AM-low) or 16,000 ft (AM-high), cruise at that altitude, BSFC 0.45; all OUR
  assumptions, as in run_check.py. Empty weight is the headline one (no credit
  for a lighter engine).
- Economy is 65% of the continuous power, as in run_check.py.
- Prescott re-derivation: 2,700 lb, 90 gal, MANUFACTURING's light and heavy
  structure ends, balance option B (radiator to the nose, residual nose
  ballast), both drag bases, taken from prescott/balance.py unchanged.
- Bede BD-4C (AER-4145, reference): factory weights, 51 gal and the 80 gal
  option, fleet drag factor (Bede publishes no altitude or power with its
  speeds). The BD-19 publishes no geometry of its own and shares the BD-4C's
  wing, gear, weights and performance table, so the BD-4C rows stand in for it.

Method (perf.py): constant-altitude, constant-speed cruise integrated in fuel
steps, taxi and climb allowance as in run_check.py, no descent credit, the
reserve flown at end-of-cruise power. While the tanks have room, the airplane
leaves at gross and fuel is traded for payload. Past the full-tank point it
leaves below gross with full tanks, and payload is solved so the fuel just
covers the distance. "cannot" means not even an empty cabin reaches it on full
tanks. No seat or baggage-bay cap is applied: a payload above the cabin's
capacity is weight available, not people.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "prescott"))
import perf  # noqa: E402
from run_check import AM20T, climb_allowance  # noqa: E402

DISTS = (600.0, 800.0, 1000.0, 1200.0)
RESERVES = (0.0, 45.0)
CASES = (("AM-low", 8000.0), ("AM-high", 16000.0))
SHORTLIST = {"bellanca-t250-aries": "Bellanca T-250 Aries", "express-2000": "Wheeler Express",
             "lancair-iv-p": "Lancair IV-P", "meyers-200d": "Meyers 200D",
             "mooney-301": "Mooney 301", "cozy-mkiv": "Cozy MKIV (reference)",
             # reference designs added on AER-4145; the BD-19 has no geometry of its own
             # published, so the BD-4C model stands in for it (see its dossier)
             "bede-bd-4c": "Bede BD-4C (reference; BD-19 proxy)",
             "bede-bd-4c-80gal": "Bede BD-4C, 80 gal option (reference)"}
SPEED_FLOOR = 160.0   # KTAS: the one floor left in the brief (Bill, 2026-10-25)


def payload(m, wet, gross, empty, fuel_lb, h, V, bsfc, d, resv):
    """Payload (lb) that flies d nm, or None."""
    clb = climb_allowance(gross, h, bsfc=bsfc)
    f = perf.fuel_for(m, wet, gross - clb, d, h, V, bsfc, 1, resv)
    if f <= fuel_lb - clb:
        p = gross - clb - empty - f
        return p if p >= 0 else None
    # tank-limited: full tanks, take-off weight below gross
    def fits(p):
        W = empty + p + fuel_lb
        c = climb_allowance(W, h, bsfc=bsfc)
        return perf.fuel_for(m, wet, W - c, d, h, V, bsfc, 1, resv) <= fuel_lb - c
    hi = gross - empty - fuel_lb
    if hi < 0 or not fits(0.0):
        return None
    lo = 0.0
    for _ in range(30):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if fits(mid) else (lo, mid)
    return lo


def full_tank_range(m, wet, gross, fuel_lb, h, V, bsfc, resv):
    clb = climb_allowance(gross, h, bsfc=bsfc)
    rng, _ = perf.cruise_range(m, wet, gross - clb, fuel_lb - clb, h, V, bsfc, 1, resv)
    return rng


def compute(m, wet, gross, empty, fuel_lb, bsfc=0.45):
    """One record per (power, engine case): KTAS, payload per distance and
    reserve, and the full-tank point."""
    out = []
    for power, frac in (("continuous", 1.0), ("economy 65%", 0.65)):
        for case, h in CASES:
            eng = dict(AM20T, crit_alt_ft=h)
            P = perf.power_avail(eng, h, eng["cont_hp"] / eng["hp"]) * frac
            sp = perf.solve_speed(m, wet, eng, 0.92 * gross, h, P)
            rec = {"power": power, "case": case, "alt_ft": h, "hp": P}
            if sp["ktas"] < 100.0:   # below level-flight power: the solver hit its bound
                rec["ktas"] = None
                out.append(rec)
                continue
            V = sp["V_fts"]
            rec["ktas"] = sp["ktas"]
            rec["payload"] = {f"{d:.0f}": [payload(m, wet, gross, empty, fuel_lb, h, V, bsfc, d, r)
                                            for r in RESERVES] for d in DISTS}
            rec["full_tank_payload"] = gross - empty - fuel_lb
            rec["full_tank_range"] = [full_tank_range(m, wet, gross, fuel_lb, h, V, bsfc, r)
                                      for r in RESERVES]
            out.append(rec)
    return out


def rows(label, recs):
    out = []
    for r in recs:
        pw = f"{r['power']}, {r['alt_ft']/1000:.0f}k"
        if r["ktas"] is None:
            out.append(f"| {label} | {pw} | no level-flight solution | | | | | |")
            continue
        cells = [f"{f0(a)} / {f0(b)}" for a, b in (r["payload"][f"{d:.0f}"] for d in DISTS)]
        ftp = r["full_tank_payload"]
        ft = r["full_tank_range"]
        kt = f"{r['ktas']:.0f}" + (" (under the 160 floor)" if r["ktas"] <= SPEED_FLOOR else "")
        out.append(f"| {label} | {pw} | {kt} | " + " | ".join(cells)
                   + f" | {f0(ftp) if ftp >= 0 else 'tanks exceed useful load'}: {ft[0]:,.0f} / {ft[1]:,.0f} |")
    return out


def span(xs, fmt="{:,.0f}"):
    """Low-high over a set of values; None (cannot) sorts lowest."""
    vals = [x for x in xs if x is not None]
    if not vals:
        return "cannot"
    lo = "cannot" if len(vals) < len(xs) else fmt.format(min(vals))
    hi = fmt.format(max(vals))
    return hi if lo == hi else f"{lo}-{hi}"


def condensed(label, recsets, power):
    """One row: every engine case (and every drag basis in recsets) spanned."""
    rs = [r for recs in recsets for r in recs if r["power"] == power and r["ktas"] is not None]
    if not rs:
        return f"| {label} | {power} | no level-flight solution | | | | | |"
    cells = []
    for d in DISTS:
        k = f"{d:.0f}"
        cells.append(span([r["payload"][k][0] for r in rs]) + " / " + span([r["payload"][k][1] for r in rs]))
    kt = span([r["ktas"] for r in rs])
    if min(r["ktas"] for r in rs) <= SPEED_FLOOR:
        kt += " (under the 160 floor at the low end)" if max(r["ktas"] for r in rs) > SPEED_FLOOR else " (under the 160 floor)"
    return (f"| {label} | {power} | {kt} | " + " | ".join(cells)
            + f" | {span([r['full_tank_range'][0] for r in rs])} |")


def f0(x):
    return "cannot" if x is None else f"{x:,.0f}"


HDR = ("| Design | Power, cruise alt | KTAS | 600 nm | 800 nm | 1,000 nm | 1,200 nm | "
       "Full tanks from gross: payload, lb: range, nm |\n|---|---|---|---|---|---|---|---|")
CHDR = ("| Design | Power | KTAS | 600 nm | 800 nm | 1,000 nm | 1,200 nm | "
        "Range on full tanks from gross, no reserve, nm |\n|---|---|---|---|---|---|---|---|")


def main():
    data = {}
    for i in SHORTLIST:
        r = json.load(open(os.path.join(HERE, "results", i + ".json")))
        m = json.load(open(os.path.join(HERE, "models", i + ".json")))
        m["drag_factor"] = r["drag_factor"]
        gross = m["weights"]["mtow"]
        empty = r["am"]["AM-low"]["empty"]
        fuel = m["fuel_usable_gal"] * m.get("fuel_density", 6.0)
        label = SHORTLIST[i] + f" ({gross:,} lb, {empty:,.0f} lb empty, "
        label += f"{m['fuel_usable_gal']:g} gal, k {r['drag_factor']:.2f})"
        data[i] = {"label": label, "sets": {"": compute(m, r["wet"], gross, empty, fuel)}}

    import balance as B  # prescott/balance.py: model_for, rebuilt_empty, cg
    for gross, gal in ((2400.0, 56.5), (2700.0, 90.0)):
        for end in ("light", "heavy"):
            # option B exactly as balance.py's performance table sizes it:
            # radiator to the nose, avionics forward, residual nose ballast
            items = B.rebuilt_empty(end, gross, "nose") + [(-15.0, B.FS["panel"]), (15.0, B.FS["nosebay"])]
            ffs = B.FS["fuel"] if gross == 2400.0 else B.FS["fuel90"]
            ew = sum(w for w, _ in items) + B.ballast_for(items, gross, gal, ffs)
            key = f"prescott-{gross:.0f}-{end}"
            data[key] = {"label": f"Prescott Pusher, {gross:,.0f} lb, {gal:g} gal, {end} end ({ew:,.0f} lb empty)",
                         "sets": {}}
            for bn, k in B.BASES.items():
                m, wet = B.model_for(gross, k)
                data[key]["sets"][f"{bn.split(' (')[0]} (k {k:.2f})"] = compute(m, wet, gross, ew, gal * 6.0)
    json.dump(data, open(os.path.join(HERE, "results", "payload_range.json"), "w"), indent=1, default=float)

    P = print
    P("# Payload-range on the AM20T (AER-3900)\n")
    P("Generated by `payload_range.py` (data in `results/payload_range.json`). Every number is "
      "ours (E). Each distance cell is payload in lb with **no reserve / 45 min reserve**, "
      "still air. \"cannot\" means not even an empty cabin reaches that distance on full tanks. "
      "The engine assumptions are the stage 3 check's (195 hp continuous, critical altitude "
      "8,000 or 16,000 ft and cruise there, BSFC 0.45, economy 65% of continuous), none "
      "published by Aeromomentum. No seat or baggage cap is applied. Cruise above 160 KTAS "
      "is still a floor: a row marked under it buys its payload-range with speed the brief "
      "does not allow.\n")
    P("## Condensed: each cell spans both engine cases (and, for the Prescott, both drag bases)\n")
    P(CHDR)
    for key, d in data.items():
        for power in ("continuous", "economy 65%"):
            P(condensed(d["label"], list(d["sets"].values()), power))
    P("")
    P("## Shortlist, stage 3 models (fleet or own drag factor, headline empty weight)\n")
    P(HDR)
    for i in SHORTLIST:
        for line in rows(data[i]["label"], data[i]["sets"][""]):
            P(line)
    P("")
    P("## Prescott Pusher\n")
    P("As built (2,400 lb, 56.5 gal) and re-derived (2,700 lb, 90 gal, wing and tail 12.5% "
      "larger), balance option B (radiator to the nose, residual nose ballast), on both drag bases "
      "(prescott/balance.py). Light and heavy are MANUFACTURING's two structure ends.\n")
    P(HDR)
    for key, d in data.items():
        if not key.startswith("prescott-"):
            continue
        for bn, recs in d["sets"].items():
            for line in rows(f"{d['label']}, {bn}", recs):
                P(line)
    P("")


if __name__ == "__main__":
    main()
