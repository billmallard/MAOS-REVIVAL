"""Run the independent check for one or more models.

  python3 run_check.py models/<id>.json [...]   -> results/<id>.json + .md

Per model:
  1. OpenVSP CompGeom wetted areas (vspgen.py).
  2. Calibration against every published cruise point that states altitude
     and power: our KTAS at that power, and our fuel flow at that KTAS.
  3. Original engine: still-air range on usable fuel at the published
     cruise setting; payload at 1,000 nm (no reserve, 45 min).
  4. Aeromomentum AM20T, two bracketing engine cases (see AM_CASES): speed
     at the continuous power, and payload at 1,000 nm.
"""
import json
import math
import os
import sys

import perf
import vspgen

HERE = os.path.dirname(os.path.abspath(__file__))

# Aeromomentum AM20T: 260 hp at 5,800 rpm, 285 lb dry, liquid-cooled (grade F,
# https://aeromomentum.com/am20t-230hp-300hp/, read 2026-10-24). Aeromomentum
# publishes NO continuous rating, NO critical altitude and NO fuel
# consumption. Every number below the first line is OUR ASSUMPTION.
AM20T = {"hp": 260.0, "dry_lb": 285.0,
         "installed_lb": 285.0 * 1.25 + 35.0,  # Aeromomentum's ~25% install note (AM13T page) + 35 lb radiator/coolant/plumbing (E, ours)
         "cont_hp": 195.0,               # ASSUMED: 75% of take-off rating, the GA cruise convention
         "bsfc": 0.45}                   # ASSUMED: same as the stage 1 screen estimate
AM_CASES = {
    "AM-low": dict(AM20T, crit_alt_ft=8000.0),    # ASSUMED critical altitude, pessimistic
    "AM-high": dict(AM20T, crit_alt_ft=16000.0),  # ASSUMED critical altitude, optimistic
}
CRUISE_ALTS = {"AM-low": 8000.0, "AM-high": 16000.0}
FT_PER_KT = 1.68781


def climb_allowance(W, h, eta=0.75, bsfc=0.45):
    """Taxi/takeoff 10 lb plus twice the ideal potential-energy fuel for the
    climb (Gudmundsson-style allowance; climb is run rich and slow)."""
    ideal = bsfc * (W * h / eta) / (550.0 * 3600.0)
    return 10.0 + 2.0 * ideal


def run(path):
    m = json.load(open(path))
    wet = vspgen.run(path)
    n = m.get("nprops", 1)
    res = {"id": m["id"], "name": m["name"], "wet": wet, "calibration": [],
           "assumptions": m.get("assumptions", [])}
    dens = m.get("fuel_density", 6.0)
    fuel_lb = m["fuel_usable_gal"] * dens
    mtow = m["weights"]["mtow"]
    empty = m["weights"]["empty"]
    orig = m["engine"]

    # --- 2. calibration (raw build-up, drag_factor 1.0)
    kglob = m.get("drag_factor", None)
    m["drag_factor"] = 1.0
    for p in m.get("published", []):
        if p.get("alt_ft") is None or p.get("hp") is None:
            continue
        W = p.get("weight_lb") or 0.9 * mtow
        r = perf.solve_speed(m, wet, orig, W, p["alt_ft"], p["hp"], n)
        row = {"pub": p, "W": W, "our_ktas": r["ktas"],
               "d_ktas_pct": (r["ktas"] / p["ktas"] - 1) * 100 if p.get("ktas") else None,
               "eta": r["eta"], "LD": r["LD"], "Dq_par": r["Dq_par"],
               "Dq_ind": r["Dq_ind"]}
        if p.get("ktas"):
            P, _ = perf.power_required(m, wet, W, p["alt_ft"], p["ktas"] * FT_PER_KT, n)
            row["our_hp_at_pub_ktas"] = P
            row["our_gph_at_pub_ktas"] = orig["bsfc"] * P / dens
            lo, hi = 0.5, 3.0
            for _ in range(40):
                m["drag_factor"] = 0.5 * (lo + hi)
                v = perf.solve_speed(m, wet, orig, W, p["alt_ft"], p["hp"], n)["ktas"]
                lo, hi = (m["drag_factor"], hi) if v > p["ktas"] else (lo, m["drag_factor"])
            row["k_match"] = 0.5 * (lo + hi)
            m["drag_factor"] = 1.0
        res["calibration"].append(row)
    own = [c["k_match"] for c in res["calibration"]
           if c.get("k_match") and c["pub"].get("grade") in ("P", "R")
           and c["pub"].get("use_for_k", True)]
    res["k_own"] = sum(own) / len(own) if own else None
    kfleet = json.load(open(os.path.join(HERE, "calib.json")))["k_global"]
    res["k_fleet"] = kfleet
    if kglob is None:
        if own:
            kglob = max(res["k_own"], kfleet)
            res["k_alt"] = min(res["k_own"], kfleet)
            res["k_basis"] = ("own published points" if kglob == res["k_own"]
                              else "fleet calibration (own points read cleaner than the fleet)")
        else:
            kglob = kfleet
            res["k_alt"] = 1.16
            res["k_basis"] = "fleet calibration (no published point with known power)"
    else:
        res["k_alt"] = kglob
        res["k_basis"] = "set in model"
    m["drag_factor"] = kglob
    res["drag_factor"] = kglob

    # drag breakdown at the reference condition (first calibration point, or AM-low)
    ref = m.get("ref_condition")
    if ref is None and res["calibration"]:
        c0 = res["calibration"][0]
        ref = {"alt_ft": c0["pub"]["alt_ft"], "hp": c0["pub"]["hp"], "W": c0["W"]}
    r = perf.solve_speed(m, wet, orig, ref["W"], ref["alt_ft"], ref["hp"], n)
    Sref = m["Sref"]
    res["breakdown"] = {"cond": ref, "ktas": r["ktas"],
                        "items": [(a, b, c) for a, b, c in r["items"]],
                        "Dq_par": r["Dq_par"], "Dq_ind": r["Dq_ind"],
                        "CD0": r["Dq_par"] / Sref, "eta": r["eta"], "LD": r["LD"]}

    # --- 3. original engine, published cruise setting
    oc = m["orig_cruise"]  # {"alt_ft", "hp"} -- the setting the published range uses
    W0 = mtow
    sp = perf.solve_speed(m, wet, orig, 0.92 * mtow, oc["alt_ft"], oc["hp"], n)
    V = sp["V_fts"]
    clb = climb_allowance(W0, oc["alt_ft"], bsfc=orig["bsfc"])
    rng, hrs = perf.cruise_range(m, wet, W0 - clb, fuel_lb - clb, oc["alt_ft"], V,
                                 orig["bsfc"], n)
    out = {"alt_ft": oc["alt_ft"], "hp": oc["hp"], "ktas": sp["ktas"],
           "range_nm_noreserve_fullfuel_mtow": rng, "hours": hrs,
           "climb_allowance_lb": clb}
    for resv in (0.0, 45.0):
        pl, f = perf.payload_at(m, wet, mtow - clb, empty, 1000.0, oc["alt_ft"], V,
                                orig["bsfc"], fuel_lb - clb, n, resv)
        out[f"payload_1000_{int(resv)}"] = None if pl is None else pl
        out[f"fuel_1000_{int(resv)}_lb"] = f + clb
    res["orig"] = out

    # --- 4. AM20T cases
    base = dict(AM20T)
    if "am_engine" in m:  # e.g. 2x AM15T for a twin
        ae = m["am_engine"]
        base.update(hp=ae["hp"], dry_lb=ae["dry_lb"], installed_lb=ae["dry_lb"] * 1.25 + 35.0,
                    cont_hp=0.75 * ae["hp"], model=ae["model"])
    else:
        base["model"] = "AM20T"
    ne = m.get("n_engines", 1)
    dmass = base["installed_lb"] * ne - m["orig_installed_lb"]
    res["am_model"] = f"{ne}x {base['model']}" if ne > 1 else base["model"]
    res["am_dmass_lb"] = dmass
    res["am"] = {}
    for case, crit in (("AM-low", 8000.0), ("AM-high", 16000.0)):
        eng = dict(base, crit_alt_ft=crit)
        h = CRUISE_ALTS[case]
        P = perf.power_avail(eng, h, eng["cont_hp"] / eng["hp"]) * ne
        # headline: no credit for a lighter engine (CG ballast assumed to eat it);
        # the full saving is taken only in the optimistic bound below
        e_am = empty + max(dmass, 0.0)
        e_opt = empty + dmass
        sp = perf.solve_speed(m, wet, eng, 0.92 * mtow, h, P, n)
        V = sp["V_fts"]
        clb = climb_allowance(mtow, h, bsfc=eng["bsfc"])
        rng, hrs = perf.cruise_range(m, wet, mtow - clb, fuel_lb - clb, h, V,
                                     eng["bsfc"], n)
        o = {"alt_ft": h, "hp": P, "ktas": sp["ktas"], "empty": e_am,
             "useful": mtow - e_am, "useful_opt": mtow - e_opt, "range_nm_fullfuel": rng,
             "gph": eng["bsfc"] * P / dens}
        for resv in (0.0, 45.0):
            pl, f = perf.payload_at(m, wet, mtow - clb, e_am, 1000.0, h, V,
                                    eng["bsfc"], fuel_lb - clb, n, resv)
            o[f"payload_1000_{int(resv)}"] = pl
            o[f"fuel_1000_{int(resv)}_lb"] = f + clb
        # economy: 65% of continuous for comparison
        sp2 = perf.solve_speed(m, wet, eng, 0.92 * mtow, h, 0.65 * P, n)
        for resv in (0.0, 45.0):
            pl, f = perf.payload_at(m, wet, mtow - clb, e_am, 1000.0, h,
                                    sp2["V_fts"], eng["bsfc"], fuel_lb - clb, n, resv)
            o[f"eco_payload_1000_{int(resv)}"] = pl
        o["eco_ktas"] = sp2["ktas"]
        # optimistic bound: the other calibration factor
        m["drag_factor"] = res["k_alt"]
        spo = perf.solve_speed(m, wet, eng, 0.92 * mtow, h, P, n)
        plo, _ = perf.payload_at(m, wet, mtow - clb, e_opt, 1000.0, h, spo["V_fts"],
                                 eng["bsfc"], fuel_lb - clb, n, 45.0)
        m["drag_factor"] = kglob
        o["opt_ktas"] = spo["ktas"]
        o["opt_payload_1000_45"] = plo
        res["am"][case] = o

    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    json.dump(res, open(os.path.join(HERE, "results", m["id"] + ".json"), "w"),
              indent=1, default=float)
    return res


def fmt(x, nd=0):
    if x is None:
        return "cannot"
    return f"{x:,.{nd}f}"


def summary(res):
    L = [f"## {res['name']}  (results at drag factor {res['drag_factor']:.2f}, {res['k_basis']})"]
    b = res["breakdown"]
    L.append(f"Reference condition {b['cond']}: {b['ktas']:.0f} KTAS, CD0 {b['CD0']:.4f}, "
             f"D/q par {b['Dq_par']:.2f} ft2, ind {b['Dq_ind']:.2f} ft2, eta {b['eta']:.3f}, L/D {b['LD']:.1f}")
    for c in res["calibration"]:
        p = c["pub"]
        s = (f"  pub {p.get('ktas')} KTAS @ {p['alt_ft']} ft, {p['hp']} hp ({p.get('grade')}) "
             f"-> ours {c['our_ktas']:.0f} KTAS")
        if c.get("d_ktas_pct") is not None:
            s += f" ({c['d_ktas_pct']:+.1f}%, k_match {c['k_match']:.2f}), power for pub speed {c['our_hp_at_pub_ktas']:.0f} hp, {c['our_gph_at_pub_ktas']:.1f} gph"
            if p.get("gph"):
                s += f" vs pub {p['gph']} gph"
        L.append(s)
    o = res["orig"]
    L.append(f"Orig engine {o['hp']} hp @ {o['alt_ft']} ft: {o['ktas']:.0f} KTAS, range {o['range_nm_noreserve_fullfuel_mtow']:.0f} nm, "
             f"payload@1000 {fmt(o['payload_1000_0'])}/{fmt(o['payload_1000_45'])}")
    L.append(f"{res['am_model']} swap delta installed mass {res['am_dmass_lb']:+.0f} lb")
    for k, a in res["am"].items():
        L.append(f"  {k}: {a['hp']:.0f} hp @ {a['alt_ft']:.0f} ft -> {a['ktas']:.0f} KTAS, UL {a['useful']:.0f}, "
                 f"range {a['range_nm_fullfuel']:.0f} nm, payload@1000 {fmt(a['payload_1000_0'])}/{fmt(a['payload_1000_45'])}; "
                 f"[opt k {res['k_alt']:.2f}: {a['opt_ktas']:.0f} KTAS, {fmt(a['opt_payload_1000_45'])}] eco {a['eco_ktas']:.0f} KTAS payload {fmt(a['eco_payload_1000_0'])}/{fmt(a['eco_payload_1000_45'])}")
    return "\n".join(L)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(summary(run(p)))
