"""AER-3807 planform sweep: one four-seat pusher mission, six wings from
aspect ratio 10 down to a 2.0 delta. Everything except the wing (and the tail
it needs) is held fixed, so the differences are the planform's.

Run:  python3 planform.py            -> results/sweep.json + results/sweep.md
      python3 planform.py --rule S   -> same-wing-area sensitivity

Methods, named in every table (fidelity in brackets):
  Span efficiency, lift slope  AVL 3.x vortex lattice, wing alone [inviscid,
                               attached flow, full leading-edge suction]
  Lift-dependent viscous drag  Kroo (2001, "Drag due to lift", Annu. Rev.
                               Fluid Mech. 33): e = 1/(1/(e_inv s) + 0.38 CD0 pi A)
                               [empirical]
  Delta leading-edge suction   Raymer 6th ed. sec. 12.6: K = S K100 + (1-S)/CLa,
                               S falling with CL (our schedule, grade E)
  Vortex lift                  Polhamus suction analogy (NASA TN D-3767), used
                               only in the stall/landing bracket
  Wetted area                  OpenVSP CompGeom on a parametric model
                               [+/-3% surfaces, +/-10% fuselage]
  Parasite drag                Raymer component build-up via AER-3783 perf.py,
                               x1.29 survey fleet calibration (calib.json)
  Weights                      Raymer eqs. 15.46-15.48 (GA wing, tails) with
                               composite factors 0.85/0.83 (Raymer table 15.4)
  Propeller                    McCormick actuator disk x 0.85 x install 0.90
  Range                        stepwise constant-power cruise (perf.py)
  Gust                         Pratt formula, 14 CFR 23.341 as it stood
                               before amendment 23-64 (2017), Ude 50 ft/s at Vc
  Root bending                 Schrenk spanload at 3.8 g limit x 1.5
  Ground effect                McCormick (Aerodynamics, Aeronautics and Flight
                               Mechanics) phi = (16h/b)^2/(1+(16h/b)^2) on AR
"""
import json
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/maos-work/aero/analysis/AER-3783")
sys.path.insert(0, HERE)
import perf  # noqa: E402
import vspgen  # noqa: E402
import avlgen  # noqa: E402

KT = 1.68781
RHO0 = 0.0023769
CONT = "/workspace/analysis/AER-3807"

# ---- the fixed mission and airframe -------------------------------------
USEFUL = 1000.0          # lb, Bill's useful-load target
FUEL_GAL = 75.0          # US gal usable, all points (E: 1,000 nm + 45 min at ~10 gph)
FUEL_LB = FUEL_GAL * 6.0
CRUISE_ALT = 12000.0     # ft; 180 KTAS here is 150 KEAS
CRUISE_HP = 195.0        # 75% of AM20T 260 hp take-off rating (F); continuous rating ours (E)
TO_HP = 260.0            # AM20T published (F), aeromomentum.com/am20t-230hp-300hp/
CRIT_ALT = 12000.0       # turbo-normalized to here: ASSUMED (Aeromomentum publishes none)
BSFC = 0.45
NZ_ULT = 3.8 * 1.5       # normal category limit x 1.5
V_TD = 61.0              # kt, sizing touchdown/stall speed (Part 23 legacy 61 kt single-engine stall)
ALPHA_LIM = 14.0         # deg, usable landing attitude, all points (E; tail/prop clearance)
H_WING = 3.0             # ft, wing quarter-MAC height above ground at touchdown (E)
FUS = {"length": 22.0, "width": 4.0, "height": 4.4, "profile": "pusher_tail"}
FUS_DMAX = 4.2
PROP = {"diameter_ft": 6.0, "install": 0.90}
GEAR_DQ = 0.10           # retractable, doors and gaps (E); 1.5 ft2 more extended
STOPPED_PROP_DQ = 1.0    # ft2, stopped fixed-pitch 6 ft prop (E; none if feathered)
CDF = 1.29               # survey fleet drag factor (AER-3783 calib.json)
if "--cdf" in sys.argv:  # sensitivity: measured pushers need 1.35-1.72 (AER-3783)
    CDF = float(sys.argv[sys.argv.index("--cdf") + 1])
UDE = 50.0               # ft/s, design gust at Vc
V_GUST_KEAS = 150.0      # same equivalent speed for every point

# The sweep. tail: "conv" = horizontal + vertical tail by volume coefficient;
# "fin" = tailless, fin only (Rohr 2-175 style).
POINTS = [
    {"id": "AR10", "AR": 10.0, "taper": 0.45, "tail": "conv", "airfoil": "2415",
     "label": "high AR, glider-like"},
    {"id": "AR8", "AR": 8.0, "taper": 0.50, "tail": "conv", "airfoil": "2415",
     "label": "high AR, conventional GA"},
    {"id": "AR6.5", "AR": 6.5, "taper": 0.60, "tail": "conv", "airfoil": "2415",
     "label": "moderate AR"},
    {"id": "AR4", "AR": 4.0, "taper": 0.70, "tail": "conv", "airfoil": "2415",
     "label": "low AR, straight wing"},
    {"id": "D3", "AR": 3.0, "taper": 0.15, "tail": "fin", "airfoil": "0014",
     "label": "cropped delta (Rohr-style)"},
    {"id": "D2", "AR": 2.0, "taper": 0.10, "tail": "fin", "airfoil": "0014",
     "label": "delta (Dyke-style)"},
]
TC = {"conv": (0.14, 0.12), "fin": (0.10, 0.10)}  # root, tip t/c (E: GA practice; deltas thinner on long chords)


def sweep_le(p):
    """Straight wings: quarter-chord unswept. Deltas: straight trailing edge."""
    A, lam = p["AR"], p["taper"]
    if p["tail"] == "fin":
        return math.degrees(math.atan(4 * (1 - lam) / (A * (1 + lam))))
    return math.degrees(math.atan((1 - lam) / (A * (1 + lam))))


def sweep_x(p, x_frac):
    """Sweep of the x/c = x_frac line (deg)."""
    A, lam = p["AR"], p["taper"]
    t = math.tan(math.radians(sweep_le(p)))
    return math.degrees(math.atan(t - 4 * x_frac * (1 - lam) / (A * (1 + lam))))


def geom(p, S):
    b = math.sqrt(S * p["AR"])
    cr = 2 * S / (b * (1 + p["taper"]))
    ct = p["taper"] * cr
    mac = 2 / 3 * cr * (1 + p["taper"] + p["taper"] ** 2) / (1 + p["taper"])
    return {"S": S, "b": b, "cr": cr, "ct": ct, "mac": mac,
            "sweep_le": sweep_le(p), "sweep_c4": sweep_x(p, 0.25)}


def tails(p, g):
    """Tail areas by volume coefficient (Raymer table 6.4, GA single:
    Vh 0.70, Vv 0.04). Arms from a 22 ft pusher fuselage (E). Tailless fin:
    Vv 0.05 on a 6 ft arm (E; a delta's MAC sits far aft)."""
    if p["tail"] == "conv":
        Sh = 0.70 * g["S"] * g["mac"] / 11.0
        Sv = 0.04 * g["S"] * g["b"] / 10.5
    else:
        # Tailless delta: fin at the trailing edge, arm 0.45 root chord from
        # the CG; Vv 0.03 because a swept wing adds its own weathercock
        # stability (E, ours; check against the calibration fins).
        Sh = 0.0
        Sv = 0.03 * g["S"] * g["b"] / (0.45 * g["cr"])
    return Sh, Sv


def weights(p, g, W0):
    q = 0.5 * perf.atmos(CRUISE_ALT)[0] * (V_GUST_KEAS * KT / math.sqrt(perf.atmos(CRUISE_ALT)[3])) ** 2
    Lc4 = math.radians(g["sweep_c4"])
    tc = 0.5 * sum(TC[p["tail"]])
    Ww = (0.036 * g["S"] ** 0.758 * FUEL_LB ** 0.0035 * (p["AR"] / math.cos(Lc4) ** 2) ** 0.6
          * q ** 0.006 * p["taper"] ** 0.04 * (100 * tc / math.cos(Lc4)) ** -0.3
          * (NZ_ULT * W0) ** 0.49) * 0.85
    Sh, Sv = tails(p, g)
    Wh = 0.0
    if Sh > 0:
        Wh = (0.016 * (NZ_ULT * W0) ** 0.414 * q ** 0.168 * Sh ** 0.896
              * (100 * 0.10) ** -0.12 * 4.5 ** 0.043 * 0.6 ** -0.02) * 0.83
    Lv = math.radians(35.0)
    Wv = (0.073 * (NZ_ULT * W0) ** 0.376 * q ** 0.122 * Sv ** 0.873
          * (100 * 0.10 / math.cos(Lv)) ** -0.49 * (1.5 / math.cos(Lv) ** 2) ** 0.357
          * 0.5 ** 0.039) * 0.83
    return Ww, Wh, Wv


def ge_ar(AR, b):
    x = (16 * H_WING / b) ** 2
    return AR * (1 + x) / x


def helmbold(AR, sweep_half_deg, M=0.1):
    """Raymer eq. 12.6, eta 0.95, F 1.0, per rad: used only to scale AVL's
    slope into ground effect (ratio of in- to out-of-ground values)."""
    b2 = 1 - M * M
    t = math.tan(math.radians(sweep_half_deg)) ** 2
    return 2 * math.pi * AR / (2 + math.sqrt(4 + AR * AR * b2 / 0.95 ** 2 * (1 + t / b2)))


def usable_cl(p, a, g):
    """Landing CL: limited by the attitude, not CLmax, on low-AR wings.
    Straight wings: single-slotted flaps, CLmax 1.9 (E, GA practice),
    dCL_flap 0.55 at the attitude. Tailless deltas: no flaps (elevons trim
    up), dCL 0. In ground effect. Returns (CL_att, CLmax, CL_usable, vortex
    CL increment at the attitude by Polhamus with Kv = pi, deltas only)."""
    AR_ge = ge_ar(p["AR"], g["b"])
    hal = sweep_x(p, 0.5)
    k_ge = helmbold(AR_ge, hal) / helmbold(p["AR"], hal)
    al = math.radians(ALPHA_LIM - a["alpha0_deg"])
    if p["tail"] == "conv":
        CL_att = a["CLa"] * k_ge * al + 0.55
        CLmax = 1.9
        dv = 0.0
    else:
        CL_att = a["CLa"] * k_ge * al
        CLmax = 1.35  # E: rounded-LE cropped delta, attached-flow max before vortex break
        a_r = math.radians(ALPHA_LIM)
        dv = math.pi * math.cos(a_r) * math.sin(a_r) ** 2
    return CL_att, CLmax, min(CL_att, CLmax), dv, k_ge


def suction_S(CL):
    """Leading-edge suction fraction for a rounded-LE delta (E, ours, after
    the shape of Raymer fig. 12.37): 0.93 to CL 0.25, 0.70 at 0.8, 0.5 at 1.2."""
    if CL <= 0.25:
        return 0.93
    if CL <= 0.8:
        return 0.93 - (CL - 0.25) / 0.55 * 0.23
    return max(0.5, 0.70 - (CL - 0.8) / 0.4 * 0.2)


class Plane:
    def __init__(self, p, S, a, wet):
        self.p, self.a, self.wet = p, a, wet
        self.g = geom(p, S)
        Sh, Sv = tails(p, self.g)
        self.Sh, self.Sv = Sh, Sv
        g = self.g
        comps = [
            {"name": "Wing", "kind": "surface", "lref": g["mac"], "tc": 0.5 * sum(TC[p["tail"]]), "xc": 0.30,
             "sweep_tc": sweep_x(p, 0.3), "xtr": 0.25, "Q": 1.0},
            {"name": "Fuselage", "kind": "body", "lref": FUS["length"], "dmax": FUS_DMAX,
             "xtr": 0.05, "Q": 1.0},
            {"name": "Vtail", "kind": "surface", "lref": math.sqrt(Sv / 1.5), "tc": 0.10,
             "xc": 0.3, "sweep_tc": 30, "xtr": 0.15, "Q": 1.05},
        ]
        if Sh > 0:
            comps.append({"name": "Htail", "kind": "surface", "lref": math.sqrt(Sh / 4.5),
                          "tc": 0.10, "xc": 0.3, "sweep_tc": 5, "xtr": 0.15, "Q": 1.05})
        self.m = {"components": comps, "fixed_Dq": [["retractable gear, doors", GEAR_DQ]],
                  "cooling_factor": 0.8, "excrescence_frac": 0.05, "drag_factor": CDF,
                  "lifting": [], "prop": PROP}

    def cd0(self, h, V, P):
        dq, _ = perf.parasite_Dq(self.m, self.wet, h, V, P)
        return dq / self.g["S"]

    def K(self, CL, CD0):
        """Induced-drag factor CDi = K CL^2."""
        A = self.p["AR"]
        s_f = 1 - 2 * (FUS["width"] / self.g["b"]) ** 2
        e = 1 / (1 / (self.a["e_inv"] * s_f) + 0.38 * CD0 * math.pi * A)
        Kk = 1 / (math.pi * A * e)
        if self.p["tail"] == "fin":
            S = suction_S(CL)
            Kd = S * Kk + (1 - S) / self.a["CLa"]
            return max(Kk, Kd)
        return Kk

    def drag(self, W, h, V, P, extra_dq=0.0):
        rho = perf.atmos(h)[0]
        q = 0.5 * rho * V * V
        CL = W / (q * self.g["S"])
        CD0 = self.cd0(h, V, P) + extra_dq / self.g["S"]
        CDi = self.K(CL, CD0) * CL * CL
        return q * self.g["S"] * (CD0 + CDi), CL, CD0, CDi

    def eta(self, T, h, V):
        return perf.prop_eff(self.m, T, h, V)[0]

    def speed_at_power(self, W, h, P):
        """High-speed (front-side) root of eta P = D V: scan down from 600
        ft/s to the first speed with positive excess power, then bisect.
        Plain bisection over the whole range can land on the back-side root."""
        def excess(V):
            D = self.drag(W, h, V, P)[0]
            return self.eta(D, h, V) * P * 550 - D * V
        hi = 600.0
        while hi > 80.0 and excess(hi - 5.0) <= 0:
            hi -= 5.0
        lo = hi - 5.0
        if excess(lo) <= 0:
            raise ValueError(f"no level-flight speed at W={W:.0f} lb, h={h:.0f} ft, P={P:.0f} hp")
        for _ in range(40):
            V = 0.5 * (lo + hi)
            D = self.drag(W, h, V, P)[0]
            if self.eta(D, h, V) * P * 550 > D * V:
                lo = V
            else:
                hi = V
        return 0.5 * (lo + hi)

    def power_req(self, W, h, V):
        P = 150.0
        for _ in range(25):
            D = self.drag(W, h, V, P)[0]
            P = D * V / (self.eta(D, h, V) * 550)
        return P

    def roc(self, W, h, P_avail):
        """Best rate of climb (fpm) and its speed (KEAS), and the induced
        share of drag there."""
        best = (-1e9, 0, 0)
        sig = perf.atmos(h)[3]
        for keas in range(60, 160):
            V = keas * KT / math.sqrt(sig)
            D, CL, CD0, CDi = self.drag(W, h, V, P_avail)
            Pex = self.eta(D, h, V) * P_avail * 550 - D * V
            r = Pex / W * 60
            if r > best[0]:
                best = (r, keas, CDi / (CD0 + CDi))
        return best

    def best_LD(self, W, extra_dq=0.0):
        best = (0, 0)
        for keas in range(55, 200):
            V = keas * KT
            D = self.drag(W, 0.0, V, 120.0, extra_dq)[0]
            if W / D > best[0]:
                best = (W / D, keas)
        return best

    def min_power(self, W, h):
        """Max-endurance (min power) speed: the 45 min reserve leg."""
        sig = perf.atmos(h)[3]
        best = (1e9, 0, 0)
        for keas in range(55, 170):
            V = keas * KT / math.sqrt(sig)
            P = self.power_req(W, h, V)
            if P < best[0]:
                D, CL, CD0, CDi = self.drag(W, h, V, P)
                best = (P, keas, CDi / (CD0 + CDi))
        return best

    def cruise_range(self, W0, h, P, reserve_min=0.0):
        ff = BSFC * P
        usable = FUEL_LB - ff * reserve_min / 60.0
        W, burned, dist = W0, 0.0, 0.0
        while burned + 10 <= usable:
            V = self.speed_at_power(W - 5, h, P)
            dist += V / KT * (10 / ff)
            burned += 10
            W -= 10
        return dist

    def long_range(self, W0, h):
        """Best-range cruise (max V/P at each weight) - the upper bound on range."""
        sig = perf.atmos(h)[3]
        W, burned, dist = W0, 0.0, 0.0
        while burned + 20 <= FUEL_LB:
            best = (0, 0, 0)
            for keas in range(70, 190, 2):
                V = keas * KT / math.sqrt(sig)
                P = self.power_req(W - 10, h, V)
                if V / P > best[0]:
                    best = (V / P, V, P)
            _, V, P = best
            dist += V / KT * (20 / (BSFC * P))
            burned += 20
            W -= 20
        return dist, best[1] / KT


def _run_vsp(m):
    sp = os.path.join(HERE, "vsp", m["id"] + ".vspscript")
    vspgen.CONTAINER = CONT
    open(sp, "w").write(vspgen.build_script(m))
    r = subprocess.run(["maos", "vspscript", "-script", f"{CONT}/vsp/{m['id']}.vspscript"],
                       capture_output=True, text=True)
    comps = {}
    for line in (r.stdout + r.stderr).splitlines():
        mm = re.search(r"WET\|([^|]+)\|([-\d.eE+]+)\|([-\d.eE+]+)", line)
        if mm:
            comps[mm.group(1).strip()] = {"theo_ft2": float(mm.group(2)),
                                          "wet_ft2": float(mm.group(3))}
    if not comps:
        sys.exit("CompGeom produced no output:\n" + r.stdout[-1500:] + r.stderr[-1500:])
    json.dump(comps, open(os.path.join(HERE, "vsp", m["id"] + "_wet.json"), "w"), indent=1)
    return comps


def size(p, rule, W_fixed, S_fixed=150.0):
    """Iterate W0 and S. rule 'V': S for V_TD at W0 with the usable landing
    CL; rule 'S': S fixed. AVL is re-run on the final planform."""
    W0, S = 2900.0, 150.0
    a = avlgen.run(f"pf_{p['id']}_{rule}{'' if CDF == 1.29 else '_cdf'}", S, p["AR"], p["taper"], sweep_le(p), p["airfoil"])
    for _ in range(30):
        g = geom(p, S)
        if rule == "V":
            CLu = usable_cl(p, a, g)[2]
            S = 2 * W0 / (RHO0 * (V_TD * KT) ** 2 * CLu)
        else:
            S = S_fixed
        g = geom(p, S)
        Ww, Wh, Wv = weights(p, g, W0)
        W0n = W_fixed + Ww + Wh + Wv + USEFUL
        if abs(W0n - W0) < 0.2:
            W0 = W0n
            break
        W0 = W0n
    a = avlgen.run(f"pf_{p['id']}_{rule}{'' if CDF == 1.29 else '_cdf'}", S, p["AR"], p["taper"], sweep_le(p), p["airfoil"])
    return W0, S, a


def schrenk_ybar(b, taper):
    """Spanwise lift centroid of a semi-span, Schrenk average of planform and
    ellipse, as a fraction of b."""
    y_trap = (1 + 2 * taper) / (6 * (1 + taper))
    y_ell = 4 / (6 * math.pi)
    return 0.5 * (y_trap + y_ell)


def evaluate(p, rule, W_fixed):
    W0, S, a = size(p, rule, W_fixed)
    g = geom(p, S)
    Sh, Sv = tails(p, g)
    wet = _run_vsp({"id": f"pf_{p['id']}_{rule}{'' if CDF == 1.29 else '_cdf'}", "fuselage": FUS,
                    "surfaces": _surfaces(p, g, Sh, Sv)})
    pl = Plane(p, S, a, wet)
    Ww, Wh, Wv = weights(p, g, W0)
    empty = W0 - USEFUL
    Wmid = W0 - FUEL_LB / 2
    Vc = pl.speed_at_power(Wmid, CRUISE_ALT, CRUISE_HP)
    Dc, CLc, CD0c, CDic = pl.drag(Wmid, CRUISE_ALT, Vc, CRUISE_HP)
    roc_sl = pl.roc(W0, 0.0, TO_HP)
    roc_cr = pl.roc(W0, CRUISE_ALT, CRUISE_HP)
    # service ceiling (100 fpm) on continuous power, Gagg-Ferrar above CRIT_ALT
    h = CRUISE_ALT
    while h < 35000:
        P = perf.power_avail({"hp": CRUISE_HP, "crit_alt_ft": CRIT_ALT}, h, 1.0)
        if pl.roc(W0, h, P)[0] < 100:
            break
        h += 500
    ceiling = h
    Wres = W0 - FUEL_LB + BSFC * 120 * 0.75  # end of cruise, reserve fuel still aboard (approx)
    res = pl.min_power(Wres, CRUISE_ALT)
    LD, V_LD = pl.best_LD(Wmid)
    LDg, V_LDg = pl.best_LD(W0 - 100, STOPPED_PROP_DQ)
    rng0 = pl.cruise_range(W0, CRUISE_ALT, CRUISE_HP, 0)
    rng45 = pl.cruise_range(W0, CRUISE_ALT, CRUISE_HP, 45)
    lr, v_lr = pl.long_range(W0, CRUISE_ALT)
    # landing
    CL_att, CLmax, CLu, dv, k_ge = usable_cl(p, a, g)
    V_td = math.sqrt(2 * W0 / (RHO0 * S * CLu)) / KT
    V_td_vort = math.sqrt(2 * W0 / (RHO0 * S * (CLu + dv))) / KT if dv else V_td
    alpha_stall_free = a["alpha0_deg"] + math.degrees(
        (CLmax - (0.55 if p["tail"] == "conv" else 0)) / a["CLa"])
    # power-off approach at 1.3 x V_td, gear and flaps down: L/D and sink
    Vapp = 1.3 * V_td * KT
    CLapp = W0 / (0.5 * RHO0 * Vapp ** 2 * S)
    CD0app = pl.cd0(0.0, Vapp, 0) + (1.5 + (0.03 * S if p["tail"] == "conv" else 0)) / S \
        + STOPPED_PROP_DQ / S
    CDapp = CD0app + pl.K(CLapp, CD0app) * CLapp ** 2
    LDapp = CLapp / CDapp
    sink_app = Vapp / LDapp * 60
    # gust (Pratt), at 150 KEAS, cruise altitude density, mid weight
    rho_c = perf.atmos(CRUISE_ALT)[0]
    WS = Wmid / S
    mu_g = 2 * WS / (rho_c * g["mac"] * a["CLa"] * 32.174)
    Kg = 0.88 * mu_g / (5.3 + mu_g)
    dn = Kg * UDE * V_GUST_KEAS * a["CLa"] / (498 * WS)
    dn_sharp = UDE * V_GUST_KEAS * a["CLa"] / (498 * WS)
    # structure: root bending at ultimate, Schrenk, wing weight relief ignored
    M_root = NZ_ULT * W0 / 2 * schrenk_ybar(g["b"], p["taper"]) * g["b"]
    h_spar = TC[p["tail"]][0] * g["cr"] * 0.95
    F_cap = M_root / (0.9 * h_spar)
    # storage
    fin_h = math.sqrt(1.5 * Sv)
    height = 1.0 + FUS["height"] + fin_h * 0.85  # gear + fuselage + fin above top (E)
    length = max(FUS["length"], 0.8 + g["cr"] + 1.0) if p["tail"] == "fin" else FUS["length"]
    return {
        "id": p["id"], "label": p["label"], "rule": rule, "AR": p["AR"], "taper": p["taper"],
        "tail": p["tail"], "S": S, "b": g["b"], "cr": g["cr"], "ct": g["ct"], "mac": g["mac"],
        "sweep_le": g["sweep_le"], "sweep_c4": g["sweep_c4"], "Sh": Sh, "Sv": Sv,
        "W0": W0, "empty": empty, "W_wing": Ww, "W_tail": Wh + Wv, "WS": W0 / S,
        "wet": {k: v["wet_ft2"] for k, v in wet.items()},
        "wet_total": sum(v["wet_ft2"] for v in wet.values()),
        "e_inv": a["e_inv"], "CLa": a["CLa"], "alpha0": a["alpha0_deg"],
        "e_cruise": CLc ** 2 / (math.pi * p["AR"] * CDic),
        "CD0": CD0c, "Dq_par": CD0c * S, "Vc": Vc / KT, "CLc": CLc,
        "ind_share_cruise": CDic / (CD0c + CDic), "LD_cruise": Wmid / Dc,
        "roc_sl": roc_sl[0], "vy_sl": roc_sl[1], "ind_share_climb": roc_sl[2],
        "roc_cr": roc_cr[0], "ceiling": ceiling,
        "res_hp": res[0], "res_keas": res[1], "ind_share_res": res[2],
        "res_gph": BSFC * res[0] / 6.0,
        "LDmax": LD, "V_LDmax": V_LD, "LD_glide": LDg, "V_glide": V_LDg,
        "range0": rng0, "range45": rng45, "range_lr": lr, "v_lr": v_lr,
        "CL_att": CL_att, "CLmax": CLmax, "CLu": CLu, "k_ge": k_ge, "V_td": V_td,
        "V_td_vortex": V_td_vort, "alpha_stall_free": alpha_stall_free,
        "V_app": Vapp / KT, "CL_app": CLapp, "LD_app": LDapp, "sink_app": sink_app,
        "mu_g": mu_g, "Kg": Kg, "dn_gust": dn, "dn_sharp": dn_sharp,
        "dn_per_10fps": dn / UDE * 10,
        "M_root": M_root, "h_spar_in": h_spar * 12, "F_cap": F_cap,
        "height": height, "length": length, "fin_h": fin_h,
    }


def _surfaces(p, g, Sh, Sv):
    L = FUS["length"]
    out = []
    if p["tail"] == "conv":
        xw = 0.42 * L - 0.25 * g["mac"]
        bh = math.sqrt(4.5 * Sh)
        ch = Sh / bh
        out.append({"name": "Htail", "span": bh, "croot": ch * 1.2, "ctip": ch * 0.8,
                    "tc_root": 0.10, "x": L - 1.2 * ch - 0.3, "z": 0.6})
    else:
        xw = max(L - g["cr"] - 0.8, 0.5)
    out.insert(0, {"name": "Wing", "span": g["b"], "croot": g["cr"], "ctip": g["ct"],
                   "tc_root": TC[p["tail"]][0], "tc_tip": TC[p["tail"]][1], "sweep": g["sweep_le"],
                   "x": xw, "z": -1.2})
    hv = math.sqrt(1.5 * Sv)
    cv = Sv / hv
    out.append({"name": "Vtail", "span": hv, "croot": cv * 1.3, "ctip": cv * 0.7,
                "tc_root": 0.10, "vertical": True, "sym": False, "sweep": 30,
                "x": L - 1.3 * cv - 0.2, "z": 1.0})
    return out


def calibrate_fixed():
    """Fixed (non-wing, non-tail) empty weight, set so the AR 6.5 point at
    W/S ~19 comes out at an empty fraction of 0.60 (the survey's composite
    four-seat calibration: Cozy 0.575, Express 0.62, CAFE weighed)."""
    p = POINTS[2]
    g = geom(p, 2900 / 19.0)
    Ww, Wh, Wv = weights(p, g, 2900.0)
    return 0.60 * 2900.0 - Ww - Wh - Wv


if __name__ == "__main__":
    rule = "S" if "--rule" in sys.argv and sys.argv[sys.argv.index("--rule") + 1] == "S" else "V"
    Wf = calibrate_fixed()
    out = {"W_fixed": Wf, "rule": rule, "points": []}
    for p in POINTS:
        r = evaluate(p, rule, Wf)
        out["points"].append(r)
        print(f"{r['id']:6s} S {r['S']:6.1f} b {r['b']:5.1f} W0 {r['W0']:6.0f} e_inv {r['e_inv']:.3f} "
              f"CLa {r['CLa']:.2f} Vc {r['Vc']:5.1f} ind {r['ind_share_cruise']*100:4.1f}% "
              f"LD {r['LDmax']:4.1f}@{r['V_LDmax']} ROC {r['roc_sl']:5.0f} ceil {r['ceiling']:.0f} "
              f"R0 {r['range0']:5.0f} R45 {r['range45']:5.0f} LR {r['range_lr']:5.0f} "
              f"dn {r['dn_gust']:.2f} sink {r['sink_app']:.0f} Fcap {r['F_cap']:.0f}", flush=True)
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    tag = "" if CDF == 1.29 else f"_cdf{int(round(CDF * 100))}"
    json.dump(out, open(os.path.join(HERE, "results", f"sweep_{rule}{tag}.json"), "w"), indent=1)
