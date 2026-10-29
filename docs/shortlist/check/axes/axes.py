"""Deep-dive axes (brief, 2026-10-24): storage, home-shop construction, safety
(glide) and ride comfort (gust response), per shortlisted design, from the same
models and calibrated drag factors as the stage 3 performance check.

  python3 axes.py > axes_output.md

Methods and their limits:
  Lift-curve slope   Raymer, Aircraft Design 6th ed., eq. 12.6 (Helmbold form
                     with sweep), M from the reference speed, airfoil efficiency
                     0.95, fuselage lift factor 1.07 (Raymer's F for a typical
                     GA fuselage/span ratio). Low-AR deltas take the same form;
                     it does not include vortex lift (conservative for gusts).
  Gust response      Pratt-Walker formula as in 14 CFR 23 (pre-Amendment 64)
                     and Raymer eq. 14.? : dn = Kg rho0 Ude Ve a / (2 W/S),
                     mu = 2 (W/S) / (rho c a g), Kg = 0.88 mu / (5.3 + mu).
                     Ude 30 ft/s, at a common reference of 150 KEAS and
                     8,000 ft, at MTOW, so designs compare like for like. A
                     lower dn is a smoother ride.
  Glide              Best L/D from the calibrated drag build-up at 0.92 MTOW,
                     8,000 ft, with the cooling term at idle power. It does NOT
                     include windmilling or stopped-propeller drag, so real
                     engine-out glide is worse, by more for large fixed props.
  Storage            T-hangar door width taken as 40 ft (E: common nested
                     T-hangar doors run about 38-42 ft; the owner's own hangar
                     governs). Span from the model.
  Construction       Largest single part (half wing) and root spar depth
                     (t/c x root chord), which set mold and jig sizes. What a
                     home shop can make is MANUFACTURING's (AER-3784).
"""
import json
import math
import sys

HERE = "/maos-work/aero/analysis/AER-3783"
sys.path.insert(0, HERE)
import perf  # noqa: E402

KT = 1.68781
DESIGNS = [("bellanca-t250-aries", "Bellanca T-250 Aries"), ("prescott-pusher", "Prescott Pusher"), ("express-2000", "Wheeler Express"),
           ("lancair-iv-p", "Lancair IV-P"), ("meyers-200d", "Meyers 200D"),
           ("mooney-301", "Mooney 301"), ("cozy-mkiv", "Cozy MKIV (reference)"),
           ("bede-bd-4c", "Bede BD-4C (reference; the BD-19 uses its wing)")]
EXTRA = []  # (id, name) added when a model exists, e.g. the Prescott


def lift_slope(AR, sweep=0.0, M=0.25, F=1.07):
    b2 = 1 - M * M
    t = math.tan(math.radians(sweep)) ** 2
    return 2 * math.pi * AR / (2 + math.sqrt(4 + AR * AR * b2 / 0.95 ** 2 * (1 + t / b2))) * F


def gust_dn(WS, a, cbar, Ve_kt=150.0, h=8000.0, Ude=30.0):
    rho = perf.atmos(h)[0]
    mu = 2 * WS / (rho * cbar * a * perf.G0)
    Kg = 0.88 * mu / (5.3 + mu)
    return Kg * 0.0023769 * Ude * Ve_kt * KT * a / (2 * WS), mu, Kg


def wing_of(m):
    w = [s for s in m["surfaces"] if s["name"].lower().startswith("wing")][0]
    lift = m["lifting"][0] if len(m["lifting"]) == 1 else max(m["lifting"], key=lambda s: s["S"])
    return w, lift


def row(i, name):
    m = json.load(open(f"{HERE}/models/{i}.json"))
    r = json.load(open(f"{HERE}/results/{i}.json"))
    wet = r["wet"]
    w, lift = wing_of(m)
    S = lift["S"]
    AR = lift["AR"]
    b = math.sqrt(S * AR)
    cbar = S / b
    WS = m["weights"]["mtow"] / S
    sweep = w.get("sweep", 0.0)
    a = lift_slope(AR, sweep)
    dn, mu, Kg = gust_dn(WS, a, cbar)
    mm = dict(m, drag_factor=r["drag_factor"])
    W = 0.92 * m["weights"]["mtow"]
    best = (0, 0)
    for kt in range(70, 200):
        V = kt * KT
        Dq, _ = perf.parasite_Dq(mm, wet, 8000.0, V, 15.0)
        Dq += perf.induced_Dq(mm, W, 8000.0, V)
        LD = W / (0.5 * perf.atmos(8000.0)[0] * V * V * Dq)
        if LD > best[0]:
            best = (LD, kt)
    spar = w["tc_root"] * w["croot"] * 12
    half = b / 2
    return {"id": i, "name": name, "AR": AR, "S": S, "b": b, "WS": WS, "a": a, "mu": mu,
            "Kg": Kg, "dn": dn, "LD": best[0], "V_LD": best[1], "spar_in": spar,
            "half_span": half, "croot": w["croot"], "fits_40": b <= 40.0}


def main(extra=()):
    rows = [row(i, n) for i, n in list(DESIGNS) + list(extra)]
    print("| Design | AR | Span, ft | Fits a 40 ft T-hangar door | Wing loading, lb/ft2 | Lift slope, /rad | "
          "Gust dn per 30 ft/s at 150 KEAS, 8,000 ft | Best L/D (prop drag excluded), at KTAS | "
          "Half-wing length / root chord, ft | Root spar depth, in |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for x in rows:
        print(f"| {x['name']} | {x['AR']:.1f} | {x['b']:.1f} | {'yes' if x['fits_40'] else 'no'} | "
              f"{x['WS']:.1f} | {x['a']:.2f} | {x['dn']:.2f} | {x['LD']:.1f} at {x['V_LD']} | "
              f"{x['half_span']:.1f} / {x['croot']:.1f} | {x['spar_in']:.1f} |")
    json.dump(rows, open(f"{HERE}/axes/axes.json", "w"), indent=1)


if __name__ == "__main__":
    extra = [tuple(a.split("=", 1)) for a in sys.argv[1:]]
    main(extra)
