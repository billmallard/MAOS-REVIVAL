"""AER-3807, third planform family: the closed wing, Ligeti Stratos layout.
A front wing, low and swept back 30 deg, and a straight rear wing, high,
joined at the tips by vertical fins that also carry yaw control (no separate
fin, no tail). This is a box (Prandtl) system with a swept lower wing, not a
Wolkovitch joined wing whose wings meet without a vertical gap. Same fixed
mission, engine, fuselage, calibration and sizing rules as planform.py, so
the results sit beside the AR sweep.

Fidelity, beyond planform.py's:
  * AVL models both wings and the tip joint; e_inv and CL_alpha include the
    two-wing interference (inviscid, full suction).
  * Weights: Raymer's GA wing equation on each wing with its own area, AR and
    lift share. The joint makes the structure redundant; its relief, and the
    rear wing's buckling penalty, are NOT modelled (E: either sign).
  * Root bending: each wing as a cantilever carrying its lift share (Schrenk);
    an upper bound, because the joint carries some of it.
  * Landing CLmax of the two-wing system 1.45 (E; plain flaps on the front
    wing, front wing designed to stall first). No vortex lift.
  * No horizontal tail: pitch control on the wings (E). The tip fins carry yaw.

  python3 joined.py            rule A (same touchdown speed)
  python3 joined.py --rule S   rule B (same area, 150 ft2)
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
import planform as pf  # noqa: E402

KT = pf.KT
CONT = pf.CONT

# Stratos proportions where known (research/stratos.md): front swept ~30 deg,
# rear straight, gap/span ~0.11 (E, read from the 2003 Reese three-view).
# AR on total projected area 7 (mission-scale; the Stratos itself is 3.8).
JW = {"id": "CW", "label": "closed wing (Stratos-style)", "AR": 7.0, "share_front": 0.5,
      "gap_b": 0.11, "sweep_f": 30.0, "sweep_r": 0.0, "taper": 0.6, "tc": 0.12,
      "CLmax": 1.45, "tail": "jw"}


def geom(p, S):
    """Projected areas of the two wings; same span b; each a straight-tapered
    panel. AR is b^2 / (S_front + S_rear)."""
    b = math.sqrt(S * p["AR"])
    s = b / 2
    out = {"S": S, "b": b}
    for k, share, sw in (("f", p["share_front"], p["sweep_f"]),
                         ("r", 1 - p["share_front"], p["sweep_r"])):
        Sk = S * share
        cr = 2 * Sk / (b * (1 + p["taper"]))
        ct = p["taper"] * cr
        mac = 2 / 3 * cr * (1 + p["taper"] + p["taper"] ** 2) / (1 + p["taper"])
        out[k] = {"S": Sk, "cr": cr, "ct": ct, "mac": mac, "AR": b * b / Sk,
                  "sweep_c4": sw}
    # the straight rear wing's leading edge sits at the front wing's tip
    # leading edge, so the vertical tip fins join them (Stratos layout)
    tf = math.tan(math.radians(p["sweep_f"]))
    out["stagger"] = 0.25 * out["f"]["cr"] + s * tf - 0.25 * out["f"]["ct"]
    out["gap"] = p["gap_b"] * b
    out["S_tips"] = 2 * out["gap"] * 0.5 * (out["f"]["ct"] + out["r"]["ct"])
    out["mac"] = (out["f"]["mac"] * out["f"]["S"] + out["r"]["mac"] * out["r"]["S"]) / S
    return out


def avl(p, S, name):
    g = geom(p, S)
    b, s = g["b"], g["b"] / 2
    f, r = g["f"], g["r"]
    tf = math.tan(math.radians(p["sweep_f"]))
    tr = math.tan(math.radians(p["sweep_r"]))
    # quarter-chord lines: front from x=0.25cr_f, rear root at stagger
    xf_tip = 0.25 * f["cr"] + s * tf - 0.25 * f["ct"]
    xr_root = g["stagger"]
    xr_tip = xr_root + s * tr
    xref = 0.5 * (0.25 * f["cr"] + xr_root + 0.25 * r["cr"])
    txt = f"""{name}
0.25
0 0 0.0
{S:.4f} {g['mac']:.4f} {b:.4f}
{xref:.4f} 0.0 0.0
0.0
SURFACE
Front
12 1.0 24 -2.0
YDUPLICATE
0.0
SECTION
0.0 0.0 0.0 {f['cr']:.4f} 0.0
NACA
2412
SECTION
{xf_tip:.4f} {s:.4f} 0.0 {f['ct']:.4f} 0.0
NACA
2412
SURFACE
Rear
12 1.0 24 -2.0
YDUPLICATE
0.0
SECTION
{xr_root:.4f} 0.0 {g['gap']:.4f} {r['cr']:.4f} 0.0
NACA
2412
SECTION
{xr_tip:.4f} {s:.4f} {g['gap']:.4f} {r['ct']:.4f} 0.0
NACA
2412
SURFACE
Tipfin
8 1.0 8 -2.0
YDUPLICATE
0.0
SECTION
{xf_tip:.4f} {s:.4f} 0.0 {f['ct']:.4f} 0.0
SECTION
{xr_tip:.4f} {s:.4f} {g['gap']:.4f} {r['ct']:.4f} 0.0
"""
    open(os.path.join(HERE, "avl", name + ".avl"), "w").write(txt)
    res = {}
    for a in (0.0, 4.0):
        lp = os.path.join(HERE, "avl", f"{name}_a{a:g}.ft")
        if os.path.exists(lp):
            os.remove(lp)
        subprocess.run(["maos", "avl", f"{CONT}/avl/{name}.avl"],
                       input=f"oper\na a {a}\nx\nft\n{CONT}/avl/{name}_a{a:g}.ft\n\nquit\n",
                       capture_output=True, text=True)
        t = open(lp).read()
        res[a] = {k: float(re.search(rf"{k}\s*=\s*([-\d.Ee+]+)", t).group(1))
                  for k in ("CLtot", "CDind", "e")}
    cla = (res[4.0]["CLtot"] - res[0.0]["CLtot"]) / math.radians(4.0)
    return {"CLa": cla, "alpha0_deg": math.degrees(-res[0.0]["CLtot"] / cla),
            "e_inv": res[4.0]["e"], "geom": g, "xf_tip": xf_tip, "xr_root": xr_root,
            "xr_tip": xr_tip}


def weights(p, g, W0):
    Ww = 0.0
    for k, share in (("f", p["share_front"]), ("r", 1 - p["share_front"])):
        w = g[k]
        q = 0.5 * perf.atmos(pf.CRUISE_ALT)[0] * (pf.V_GUST_KEAS * KT / math.sqrt(perf.atmos(pf.CRUISE_ALT)[3])) ** 2
        Lc4 = math.radians(abs(p["sweep_f"] if k == "f" else p["sweep_r"]))
        Ww += (0.036 * w["S"] ** 0.758 * (pf.FUEL_LB / 2) ** 0.0035
               * (w["AR"] / math.cos(Lc4) ** 2) ** 0.6 * q ** 0.006 * p["taper"] ** 0.04
               * (100 * p["tc"] / math.cos(Lc4)) ** -0.3 * (pf.NZ_ULT * W0 * share) ** 0.49) * 0.85
    Sv = g["S_tips"]  # the tip fins are the vertical surfaces
    Lv = math.radians(10.0)
    Wv = (0.073 * (pf.NZ_ULT * W0) ** 0.376 * q ** 0.122 * Sv ** 0.873
          * (100 * 0.10 / math.cos(Lv)) ** -0.49 * (1.5 / math.cos(Lv) ** 2) ** 0.357
          * 0.5 ** 0.039) * 0.83
    return Ww, Wv, Sv


def usable_cl(p, a, g):
    AR_ge = pf.ge_ar(p["AR"], g["b"])
    k_ge = pf.helmbold(AR_ge, 0.0) / pf.helmbold(p["AR"], 0.0)
    CL_att = a["CLa"] * k_ge * math.radians(pf.ALPHA_LIM - a["alpha0_deg"]) + 0.30  # plain flaps, front wing (E)
    return CL_att, min(CL_att, p["CLmax"]), k_ge


class JPlane(pf.Plane):
    def __init__(self, p, S, a, wet):
        self.p, self.a, self.wet = p, a, wet
        self.g = geom(p, S)
        self.g["sweep_le"] = p["sweep_f"]
        g = self.g
        Sv = g["S_tips"]
        self.Sh, self.Sv = 0.0, Sv
        comps = [
            {"name": "Front", "kind": "surface", "lref": g["f"]["mac"], "tc": p["tc"], "xc": 0.30,
             "sweep_tc": abs(p["sweep_f"]), "xtr": 0.25, "Q": 1.0},
            {"name": "Rear", "kind": "surface", "lref": g["r"]["mac"], "tc": p["tc"], "xc": 0.30,
             "sweep_tc": abs(p["sweep_r"]), "xtr": 0.25, "Q": 1.10},  # tip joint, rear-to-fuselage junction (E)
            {"name": "Fuselage", "kind": "body", "lref": pf.FUS["length"], "dmax": pf.FUS_DMAX,
             "xtr": 0.05, "Q": 1.0},
            {"name": "Tipfin", "kind": "surface", "lref": 0.5 * (g["f"]["ct"] + g["r"]["ct"]),
             "tc": 0.10, "xc": 0.3, "sweep_tc": 10, "xtr": 0.15, "Q": 1.10},  # wing junctions at both ends (E)
        ]
        self.m = {"components": comps, "fixed_Dq": [["retractable gear, doors", pf.GEAR_DQ]],
                  "cooling_factor": 0.8, "excrescence_frac": 0.05, "drag_factor": pf.CDF,
                  "lifting": [], "prop": pf.PROP}

    def K(self, CL, CD0):
        A = self.p["AR"]
        s_f = 1 - 2 * (pf.FUS["width"] / self.g["b"]) ** 2
        e = 1 / (1 / (self.a["e_inv"] * s_f) + 0.38 * CD0 * math.pi * A)
        return 1 / (math.pi * A * e)


def vsp(p, a, S, rule):
    g = a["geom"]
    L = pf.FUS["length"]
    x0 = 0.18 * L
    surfaces = [
        {"name": "Front", "span": g["b"], "croot": g["f"]["cr"], "ctip": g["f"]["ct"],
         "tc_root": p["tc"], "tc_tip": p["tc"],
         "sweep": math.degrees(math.atan2(a["xf_tip"], g["b"] / 2)), "x": x0, "z": -1.2},
        {"name": "Rear", "span": g["b"], "croot": g["r"]["cr"], "ctip": g["r"]["ct"],
         "tc_root": p["tc"], "tc_tip": p["tc"],
         "sweep": 0.0, "x": x0 + a["xr_root"], "z": -1.2 + g["gap"]},
        {"name": "Tipfin", "span": g["gap"], "croot": g["f"]["ct"], "ctip": g["r"]["ct"],
         "tc_root": 0.10, "tc_tip": 0.10, "vertical": True, "sym": True,
         "sweep": math.degrees(math.atan2(a["xr_tip"] - a["xf_tip"], g["gap"])),
         "x": x0 + a["xf_tip"], "y": g["b"] / 2, "z": -1.2},
    ]
    return pf._run_vsp({"id": f"jw_{rule}", "fuselage": pf.FUS, "surfaces": surfaces})


def evaluate(p, rule, W_fixed):
    W0, S = 2700.0, 150.0
    a = avl(p, S, f"jw_{rule}")
    for _ in range(30):
        g = geom(p, S)
        if rule == "V":
            S = 2 * W0 / (pf.RHO0 * (pf.V_TD * KT) ** 2 * usable_cl(p, a, g)[1])
        else:
            S = 150.0
        g = geom(p, S)
        Ww, Wv, Sv = weights(p, g, W0)
        W0n = W_fixed + Ww + Wv + pf.USEFUL
        if abs(W0n - W0) < 0.2:
            W0 = W0n
            break
        W0 = W0n
    a = avl(p, S, f"jw_{rule}")
    g = a["geom"]
    wet = vsp(p, a, S, rule)
    pl = JPlane(p, S, a, wet)
    Ww, Wv, Sv = weights(p, g, W0)
    Wmid = W0 - pf.FUEL_LB / 2
    Vc = pl.speed_at_power(Wmid, pf.CRUISE_ALT, pf.CRUISE_HP)
    Dc, CLc, CD0c, CDic = pl.drag(Wmid, pf.CRUISE_ALT, Vc, pf.CRUISE_HP)
    roc_sl = pl.roc(W0, 0.0, pf.TO_HP)
    roc_cr = pl.roc(W0, pf.CRUISE_ALT, pf.CRUISE_HP)
    h = pf.CRUISE_ALT
    while h < 35000:
        P = perf.power_avail({"hp": pf.CRUISE_HP, "crit_alt_ft": pf.CRIT_ALT}, h, 1.0)
        if pl.roc(W0, h, P)[0] < 100:
            break
        h += 500
    Wres = W0 - pf.FUEL_LB + pf.BSFC * 120 * 0.75
    res = pl.min_power(Wres, pf.CRUISE_ALT)
    LD, V_LD = pl.best_LD(Wmid)
    LDg, V_LDg = pl.best_LD(W0 - 100, pf.STOPPED_PROP_DQ)
    rng0 = pl.cruise_range(W0, pf.CRUISE_ALT, pf.CRUISE_HP, 0)
    rng45 = pl.cruise_range(W0, pf.CRUISE_ALT, pf.CRUISE_HP, 45)
    lr, v_lr = pl.long_range(W0, pf.CRUISE_ALT)
    CL_att, CLu, k_ge = usable_cl(p, a, g)
    V_td = math.sqrt(2 * W0 / (pf.RHO0 * S * CLu)) / KT
    Vapp = 1.3 * V_td * KT
    CLapp = W0 / (0.5 * pf.RHO0 * Vapp ** 2 * S)
    CD0app = pl.cd0(0.0, Vapp, 0) + (1.5 + 0.02 * S) / S + pf.STOPPED_PROP_DQ / S
    LDapp = CLapp / (CD0app + pl.K(CLapp, CD0app) * CLapp ** 2)
    rho_c = perf.atmos(pf.CRUISE_ALT)[0]
    WS = Wmid / S
    mu_g = 2 * WS / (rho_c * g["mac"] * a["CLa"] * 32.174)
    Kg = 0.88 * mu_g / (5.3 + mu_g)
    dn = Kg * pf.UDE * pf.V_GUST_KEAS * a["CLa"] / (498 * WS)
    # each wing a cantilever with its lift share: upper bound
    Mf = pf.NZ_ULT * W0 * p["share_front"] / 2 * pf.schrenk_ybar(g["b"], p["taper"]) * g["b"]
    hf = p["tc"] * g["f"]["cr"] * 0.95
    height = 1.0 + pf.FUS["height"] + 0.5  # rear wing on top of the fuselage, no fin (E)
    semi = g["b"] / 2
    plug = (max(semi, g["f"]["cr"]), min(semi, g["f"]["cr"]))
    return {
        "id": p["id"], "label": p["label"], "rule": rule, "AR": p["AR"], "S": S, "b": g["b"],
        "cr_f": g["f"]["cr"], "cr_r": g["r"]["cr"], "ct": g["f"]["ct"], "gap": g["gap"],
        "stagger": g["stagger"], "W0": W0, "empty": W0 - pf.USEFUL, "W_wing": Ww, "W_tail": Wv,
        "WS": W0 / S, "wet": {k: v["wet_ft2"] for k, v in wet.items()},
        "wet_total": sum(v["wet_ft2"] for v in wet.values()), "e_inv": a["e_inv"],
        "CLa": a["CLa"], "CD0": CD0c, "Dq_par": CD0c * S, "Vc": Vc / KT,
        "ind_share_cruise": CDic / (CD0c + CDic), "ind_share_climb": roc_sl[2],
        "ind_share_res": res[2], "res_keas": res[1], "res_gph": pf.BSFC * res[0] / 6,
        "LDmax": LD, "V_LDmax": V_LD, "roc_sl": roc_sl[0], "roc_cr": roc_cr[0],
        "ceiling": h, "range0": rng0, "range45": rng45, "range_lr": lr, "v_lr": v_lr,
        "CLu": CLu, "V_td": V_td, "LD_app": LDapp, "sink_app": Vapp / LDapp * 60,
        "LD_glide": LDg, "V_glide": V_LDg, "mu_g": mu_g, "Kg": Kg, "dn_gust": dn,
        "dn_per_10fps": dn / pf.UDE * 10, "M_root_front": Mf, "h_spar_in": hf * 12,
        "F_cap_front": Mf / (0.9 * hf), "height": height, "length": pf.FUS["length"],
        "plug": plug, "panel_fold": max(0.0, (g["b"] - 8.5) / 2),
    }


def _main():
    if "--calib" in sys.argv:
        r = calib_stratos()
        rows = json.load(open(os.path.join(HERE, "results", "calib.json")))
        rows = [x for x in rows if x["id"] != "stratos"] + [r]
        json.dump(rows, open(os.path.join(HERE, "results", "calib.json"), "w"), indent=1)
        print(r)
        return
    rule = "S" if "--rule" in sys.argv and sys.argv[sys.argv.index("--rule") + 1] == "S" else "V"
    Wf = pf.calibrate_fixed()
    r = evaluate(JW, rule, Wf)
    json.dump(r, open(os.path.join(HERE, "results", f"joined_{rule}.json"), "w"), indent=1)
    print(json.dumps({k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items()}, indent=0))


def calib_stratos():
    """The Stratos itself: span 5.36 m, area 7.525 m2 (mean of 7.52/7.53), gross
    188 kg (F, Jane's via Wikipedia / 1000aircraftphotos). Layout as JW with
    AR 3.82, gap/span 0.11 (E, Reese three-view). Pratt on the sweep's basis."""
    b, S, W = 5.36 / 0.3048, 7.525 / 0.3048 ** 2, 188 / 0.45359
    p = dict(JW, AR=b * b / S)
    a = avl(p, S, "cal_stratos")
    g = a["geom"]
    rho = perf.atmos(pf.CRUISE_ALT)[0]
    WS = W / S
    mu = 2 * WS / (rho * g["mac"] * a["CLa"] * 32.174)
    Kg = 0.88 * mu / (5.3 + mu)
    dn = Kg * pf.UDE * pf.V_GUST_KEAS * a["CLa"] / (498 * WS)
    r = {"id": "stratos", "label": "Ligeti Stratos (closed wing)", "AR": p["AR"], "S": S, "b": b,
         "W": round(W), "WS": WS, "CLa": a["CLa"], "mac": g["mac"], "e_inv": a["e_inv"], "mu": mu,
         "Kg": Kg, "dn": dn,
         "note": "b 5.36 m, S 7.52-7.53 m2, gross 188 kg (F, Jane's 1987-88 via Wikipedia); front swept 30 deg, gap/span 0.11 E (Reese 3-view)"}
    return r


if __name__ == "__main__":
    _main()
