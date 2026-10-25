"""Wheeler Express: the stall-and-yaw problem in numbers, and what each fix
costs. Conceptual fidelity; every input graded in its comment.

  python3 tail_study.py    prints markdown tables

1. Directional stability, Cn_beta, built up from the fuselage (destabilising)
   and the fin (stabilising) as a function of fin area, because no fin
   dimensions are published for any Express variant. Methods: Raymer, Aircraft
   Design 6th ed., eq. 16.47 (fuselage), eq. 12.6 (fin lift slope, Helmbold
   form with sweep) and the DATCOM sidewash term as given by Raymer eq. 16.48.
2. Stall speeds: the CAFE Foundation's measured 1 g stalls (P) against the kit
   maker's published figures (F), scaled to weight and bank angle.
3. Cruise cost of each fix: the stage 3 Express model (calibrated drag factor,
   AM20T at the assumed 195 hp continuous, 8,000 ft), with the added wetted
   area of each fix put through the same component build-up.
Nothing here claims spin or post-stall behaviour; those are the record's.
"""
import json
import math
import sys

sys.path.insert(0, "/maos-work/aero/analysis/AER-3783")
import perf  # noqa: E402

M = json.load(open("/maos-work/aero/analysis/AER-3783/models/express-2000.json"))
WET = json.load(open("/maos-work/aero/analysis/AER-3783/vsp/express-2000_wet.json"))
RES = json.load(open("/maos-work/aero/analysis/AER-3783/results/express-2000.json"))

# --- geometry (CAFE, P, unless marked) ---------------------------------------
S, b = 130.29, 31.0                      # wing area ft2, span ft (CAFE)
L, W, H = 25.67, 3.9, 4.1                # fuselage length (CAFE, P); width, height (E, stage 3 model)
VOL = 0.55 * L * W * H                   # E: fuselage volume, prismatic coefficient 0.55 for a tapering composite fuselage
LV = 14.0                                # E: fin quarter-chord to CG, from the 25.67 ft length; no tail arm is published
FIN_AR, FIN_SWEEP = 1.5, 35.0            # E: effective aspect ratio (geometric about 1.0-1.2 plus end-plate from the stab) and "highly swept" (CAFE) leading edge


def fin_lift_slope(A=FIN_AR, sweep=FIN_SWEEP):
    """Raymer eq. 12.6, M ~ 0.2, airfoil efficiency 0.95. Per radian."""
    beta2 = 1 - 0.2 ** 2
    t = math.tan(math.radians(sweep)) ** 2
    return 2 * math.pi * A / (2 + math.sqrt(4 + A * A * beta2 / 0.95 ** 2 * (1 + t / beta2)))


def cnb_fuselage():
    """Raymer eq. 16.47: Cn_beta_fus = -1.3 Vol/(S b) (D_f/W_f), per radian."""
    return -1.3 * VOL / (S * b) * (H / W)


def cnb_fin(Sv, sidewash=1.0):
    """Fin contribution, per radian. 'sidewash' is eta_v (1 + d sigma/d beta);
    DATCOM/Raymer 16.48 gives about 0.9-1.1 for a low wing with a mid tail."""
    return fin_lift_slope() * Sv * LV / (S * b) * sidewash


def stability_table():
    out = ["| Fin area, ft2 | Vertical tail volume Vv | Cn_beta fin, /deg | Cn_beta total (fuselage + fin), /deg | Reading |",
           "|---|---|---|---|---|"]
    fus = cnb_fuselage()
    for Sv in (10, 12, 14, 16, 18, 20, 22, 24, 26):
        f = cnb_fin(Sv)
        tot = (fus + f) * math.pi / 180
        Vv = Sv * LV / (S * b)
        if tot < 0.0004:
            r = "near neutral or unstable"
        elif tot < 0.0010:
            r = "weak"
        elif tot < 0.0016:
            r = "typical light single"
        else:
            r = "strong"
        out.append(f"| {Sv} | {Vv:.3f} | {f*math.pi/180:.5f} | {tot:.5f} | {r} |")
    return out, fus


def stall_table():
    """CAFE 1997, N360EZ, CAS (P): clean 77.2 mph at 2,865 lb; full flap 67.2
    mph at 2,863 lb. Kit maker (F): Vs1 55-58 kt, Vso 50-55 kt."""
    vs_clean = 77.2 / 1.15078
    vs_flap = 67.2 / 1.15078
    rows = ["| Weight, lb | Bank | Clean stall, KCAS (CAFE basis) | Full-flap stall, KCAS (CAFE basis) | Kit-maker Vs1 scaled, kt |",
            "|---|---|---|---|---|"]
    for Wt in (2865, 3200):
        k = math.sqrt(Wt / 2865)
        for bank in (0, 30, 45, 60):
            n = 1 / math.cos(math.radians(bank))
            f = math.sqrt(n) * k
            rows.append(f"| {Wt:,} | {bank} deg | {vs_clean*f:.0f} | {vs_flap*f:.0f} | {55*f:.0f}-{58*f:.0f} |")
    return rows, vs_clean, vs_flap


def cruise_cost():
    """KTAS at 195 hp and 8,000 ft (AM-low case) for each fix, at the stage 3
    calibrated drag factor. Added wetted area is put on a component with the
    same Reynolds-number treatment as the existing tail."""
    eng = {"hp": 260.0, "cont_hp": 195.0, "bsfc": 0.45, "crit_alt_ft": 8000.0}
    m = json.loads(json.dumps(M))
    m["drag_factor"] = RES["drag_factor"]
    W = 0.92 * m["weights"]["mtow"]

    def speed(extra):
        mm = json.loads(json.dumps(m))
        for name, swet, lref, tc in extra:
            mm["components"].append({"name": name, "kind": "surface", "swet": swet, "lref": lref,
                                     "tc": tc, "xc": 0.3, "xtr": 0.1, "Q": 1.08})
        return perf.solve_speed(mm, WET, eng, W, 8000.0, 195.0)["ktas"]

    base = speed([])
    fin_wet = WET["Fin"]["wet_ft2"]
    ht_wet = WET["HTail"]["wet_ft2"]
    cases = [
        ("Baseline (stage 3 model; fin 12 ft2 is our estimate)", []),
        ("Fin enlarged to 20 ft2 (+8 ft2 planform)", [("fin add", 2 * 8 * 1.02, 3.2, 0.10)]),
        ("Fin enlarged to 24 ft2 (+12 ft2)", [("fin add", 2 * 12 * 1.02, 3.4, 0.10)]),
        ("Dorsal fin, about 3 ft2", [("dorsal", 2 * 3 * 1.02, 4.0, 0.06)]),
        ("Ventral fin, about 3 ft2", [("ventral", 2 * 3 * 1.02, 2.5, 0.08)]),
        ("S-90 style tail: 40% more tail wetted area (CAFE; NTSB)", [("tail add", 0.40 * (fin_wet + ht_wet), 2.8, 0.09)]),
        ("S-90 tail plus dorsal and ventral", [("tail add", 0.40 * (fin_wet + ht_wet), 2.8, 0.09),
                                             ("dorsal", 6.1, 4.0, 0.06), ("ventral", 6.1, 2.5, 0.08)]),
    ]
    rows = ["| Fix | KTAS at 195 hp, 8,000 ft | Change |", "|---|---|---|"]
    for name, extra in cases:
        v = speed(extra)
        rows.append(f"| {name} | {v:.1f} | {v - base:+.1f} kt |")
    return rows, base


if __name__ == "__main__":
    t, fus = stability_table()
    print(f"Fin lift slope {fin_lift_slope():.2f} /rad; fuselage Cn_beta {fus:.4f} /rad "
          f"({fus*math.pi/180:.5f} /deg); fuselage volume {VOL:.0f} ft3 (E)\n")
    print("\n".join(t))
    print()
    s, vc, vf = stall_table()
    print(f"CAFE clean {vc:.1f} KCAS, full flap {vf:.1f} KCAS\n")
    print("\n".join(s))
    print()
    c, base = cruise_cost()
    print("\n".join(c))
