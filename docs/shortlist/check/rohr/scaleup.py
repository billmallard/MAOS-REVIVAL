"""Rohr 2-175 scale-up study: the 2-175's configuration (low delta wing, engine
buried in the fuselage, shrouded pusher fan in the tail, folding wing and fin)
taken to four seats on an Aeromomentum AM20T, against the survey's targets and its speed floor.

Fidelity: conceptual. Drag is a component build-up (perf.py, Raymer/Hoerner)
on analytic wetted areas, not OpenVSP; induced drag uses an Oswald factor for a
low-aspect-ratio delta; the fan is a ducted actuator disk (momentum theory)
with stated loss factors; weights are a component estimate calibrated on
published composite four-seaters. Every input below is graded in its comment.
Nothing here claims stability, spin or flutter behaviour.

  python3 scaleup.py            prints the study tables (markdown)
"""
import math
import sys

sys.path.insert(0, "/maos-work/aero/analysis/AER-3783")
import perf  # noqa: E402

KT = 1.68781

# --- Aeromomentum AM20T, as in the stage 3 check (SHORTLIST.md) -------------
# 260 hp published take-off rating (F); 195 hp continuous and the 8,000 /
# 16,000 ft critical altitudes are OUR assumptions (Aeromomentum publishes
# neither); BSFC 0.45 lb/hp/h (E).
AM20T = {"hp": 260.0, "cont_hp": 195.0, "bsfc": 0.45, "dry_lb": 285.0}
ENGINE_CASES = {"AM-low": 8000.0, "AM-high": 16000.0}


def ducted_fan_eff(T_lb, h_ft, V, D_fan, sigma=1.0, hub=0.30, k_loss=0.86):
    """Ducted fan, momentum theory. sigma = exit area / fan disk area.
    Thrust (fan + duct) T = mdot (Ve - V), mdot = rho * sigma * A * Ve.
    Ideal efficiency 2V/(V+Ve); k_loss covers blade profile, tip clearance,
    stator and duct internal losses (E: 0.86, between McCormick's open-prop
    0.85 and the 0.88-0.90 claimed for well-designed fan-stator stages).
    Returns (eta, eta_ideal, Ve)."""
    rho = perf.atmos(h_ft)[0]
    A = math.pi * D_fan ** 2 / 4 * (1 - hub ** 2) * sigma
    # rho A Ve^2 - rho A V Ve - T = 0
    Ve = (V + math.sqrt(V * V + 4 * T_lb / (rho * A))) / 2
    eta_i = 2 * V / (V + Ve)
    return eta_i * k_loss, eta_i, Ve


def build_model(p):
    """Analytic geometry for a delta-wing, buried-engine, ducted-fan airplane.
    p: dict of design parameters. Returns a perf.py model with 'swet' per
    component, plus derived geometry for the report."""
    S, AR = p["S"], p["AR"]
    b = math.sqrt(S * AR)
    taper = p.get("taper", 0.15)            # cropped delta
    cr = 2 * S / (b * (1 + taper))
    ct = taper * cr
    mac = 2 / 3 * cr * (1 + taper + taper ** 2) / (1 + taper)
    # Exposed wing: the fuselage covers the root over its width.
    wf = p["fus_width"]
    c_at_wf = cr - (cr - ct) * wf / b
    S_exp = S - wf * (cr + c_at_wf) / 2
    sw_wing = 2 * S_exp * (1 + 0.2 * p["tc"])  # Raymer eq. 7.9 form, t/c < 0.05 term dropped
    # Fuselage forebody (cabin) as a body of revolution equivalent; the aft
    # body is the duct shroud, counted separately.
    L, dmax = p["fus_len"], p["fus_dmax"]
    sw_fus = math.pi * dmax * L * (1 - 2 / (L / dmax)) ** (2 / 3) * (1 + 1 / (L / dmax) ** 2)  # Raymer body-of-revolution estimate
    # Duct: outer shroud (in freestream) and inner wall (at the jet velocity,
    # handled by scaling its wetted area by (Ve/V)^2 inside the solver).
    Dd, Ld = p["fan_D"] * 1.08, p["duct_len"]
    sw_duct_out = math.pi * Dd * Ld
    sw_duct_in = math.pi * p["fan_D"] * Ld
    fin_S = p["fin_S"]
    sw_fin = 2 * fin_S * 1.02
    comps = [
        {"name": "Wing", "kind": "surface", "swet": sw_wing, "lref": mac, "tc": p["tc"],
         "xc": 0.35, "sweep_tc": p["sweep_tc"], "xtr": p.get("xtr_wing", 0.25), "Q": 1.0},
        {"name": "Fuselage", "kind": "body", "swet": sw_fus, "lref": L, "dmax": dmax,
         "xtr": 0.05, "Q": 1.0},
        {"name": "Duct shroud (outer)", "kind": "nacelle", "swet": sw_duct_out, "lref": Ld,
         "dmax": Dd, "xtr": 0.0, "Q": 1.1},
        {"name": "Fin", "kind": "surface", "swet": sw_fin, "lref": math.sqrt(fin_S), "tc": 0.10,
         "xc": 0.3, "sweep_tc": 35, "xtr": 0.15, "Q": 1.05},
    ]
    m = {
        "components": comps,
        "fixed_Dq": [["fixed gear, faired", p.get("gear_Dq", 0.55)]],
        # Liquid-cooled, ducted radiator: Raymer 12.39 x factor (E). The
        # 2-175 drew cooling air through the fan duct; a radiator in the duct
        # inflow is the same idea.
        "cooling_factor": p.get("cooling_factor", 0.7),
        "excrescence_frac": 0.06,
        "lifting": [{"S": S, "AR": AR, "share": 1.0, "e": p.get("e", oswald_delta(AR))}],
        "prop": {"diameter_ft": p["fan_D"]},
        # Stage 3 calibration: raw build-ups read 1.16-1.36 low against the
        # three types with measured data (SHORTLIST.md); every result here is
        # run at both ends of that band.
        "drag_factor": p.get("drag_factor", 1.25),
    }
    geo = {"b": b, "cr": cr, "ct": ct, "mac": mac, "S_exp": S_exp, "sw_wing": sw_wing,
           "sw_fus": sw_fus, "sw_duct_out": sw_duct_out, "sw_duct_in": sw_duct_in,
           "sw_fin": sw_fin}
    return m, geo


def oswald_delta(AR):
    """Span efficiency for a low-aspect-ratio cropped delta with a round
    leading edge at cruise CL: about 0.80 at AR 2-3 rising toward 0.85 at AR
    4 (E; Raymer fig. 12.? leading-edge suction 85-90%, Hoerner ch. 7)."""
    return min(0.85, 0.74 + 0.03 * AR)


def duct_inner_Dq(p, geo, h_ft, V, Ve):
    """Inner duct wall friction, at the duct velocity (mean of fan and exit,
    taken as Ve for sigma=1), referenced to freestream q."""
    rho, T, a, _ = perf.atmos(h_ft)
    nu = perf.mu(T) / rho
    Re = Ve * p["duct_len"] / nu
    cf = perf.cf_turb(Re, Ve / a)
    return cf * geo["sw_duct_in"] * (Ve / V) ** 2 * 1.15  # 15% for struts, stator, gaps (E)


def solve(p, W, h_ft, P_hp):
    """Speed where eta * P = D * V, with duct inner friction coupled to Ve."""
    m, geo = build_model(p)
    rho = perf.atmos(h_ft)[0]
    lo, hi = 100.0, 600.0
    for _ in range(80):
        V = 0.5 * (lo + hi)
        Dq_p, _ = perf.parasite_Dq(m, {}, h_ft, V, P_hp)
        Dq_i = perf.induced_Dq(m, W, h_ft, V)
        D0 = 0.5 * rho * V * V * (Dq_p + Dq_i)
        # iterate the duct inner drag with Ve
        D = D0
        for _ in range(6):
            eta, eta_i, Ve = ducted_fan_eff(D, h_ft, V, p["fan_D"])
            D = D0 + 0.5 * rho * V * V * duct_inner_Dq(p, geo, h_ft, V, Ve)
        if eta * P_hp * 550 > D * V:
            lo = V
        else:
            hi = V
    V = 0.5 * (lo + hi)
    Dq_p, items = perf.parasite_Dq(m, {}, h_ft, V, P_hp)
    Dq_i = perf.induced_Dq(m, W, h_ft, V)
    D0 = 0.5 * rho * V * V * (Dq_p + Dq_i)
    D = D0
    for _ in range(6):
        eta, eta_i, Ve = ducted_fan_eff(D, h_ft, V, p["fan_D"])
        Dq_in = duct_inner_Dq(p, geo, h_ft, V, Ve)
        D = D0 + 0.5 * rho * V * V * Dq_in
    q = 0.5 * rho * V * V
    return {"ktas": V / KT, "V": V, "D": D, "eta": eta, "eta_i": eta_i, "Ve": Ve,
            "Dq_par": Dq_p + Dq_in, "Dq_ind": Dq_i, "CL": W / (q * p["S"]),
            "LD": W / D, "items": items + [("duct inner wall", Dq_in, "at jet velocity")],
            "geo": geo}


def max_LD(p, W, h_ft):
    """Best L/D and its speed, at a nominal power for the cooling term."""
    best = (0, 0)
    for kt in range(80, 220, 2):
        V = kt * KT
        m, geo = build_model(p)
        rho = perf.atmos(h_ft)[0]
        Dq_p, _ = perf.parasite_Dq(m, {}, h_ft, V, 120)
        Dq_i = perf.induced_Dq(m, W, h_ft, V)
        D = 0.5 * rho * V * V * (Dq_p + Dq_i)
        if W / D > best[0]:
            best = (W / D, kt)
    return best


def range_nm(p, W0, fuel_lb, h_ft, P_hp, bsfc, reserve_min=0.0):
    """Constant-altitude, constant-power cruise range (a slight speed-up as
    weight falls), stepped in 10 lb of fuel."""
    W, burned, dist = W0, 0.0, 0.0
    ff = bsfc * P_hp
    usable = fuel_lb - ff * reserve_min / 60
    while burned + 10 <= usable:
        r = solve(p, W - 5, h_ft, P_hp)
        dt = 10 / ff
        dist += r["ktas"] * dt
        burned += 10
        W -= 10
    return dist


def stall_kt(W, S, CLmax):
    return math.sqrt(2 * W / (0.0023769 * S * CLmax)) / KT


# --- the four-seat design point ------------------------------------------------
# Weights. Empty-weight fraction calibrated on the two composite four-seaters
# with weighed aircraft in this survey: Cozy MKIV 1,179/2,050 = 0.575 and
# Wheeler Express 1,994/3,200 = 0.62 (CAFE, P). We take 0.60, plus 100 lb for
# what the 2-175 layout adds: duct and stator, fan, extension shaft and
# couplings, wing and fin fold mechanisms (E, ours: about 60-70 lb propulsor,
# 30-40 lb folding).
EF, LAYOUT_LB = 0.60, 100.0
FUEL_GAL = 105.0           # E: sized for 1,000 nm at continuous power plus climb and 45 min (see report)


def weights(W0):
    empty = EF * W0 + LAYOUT_LB
    return {"W0": W0, "empty": empty, "useful": W0 - empty,
            "payload_full_fuel": W0 - empty - FUEL_GAL * 6.0}


def design(S, AR, fan_D, k=1.25, W0=2900.0):
    """Four-seat layout: cabin 46 in wide (2+2), forebody to the duct 17 ft,
    fuselage max diameter 4.4 ft (E); duct length 0.95 x fan D; fin 18 ft2
    (folding, as on the 2-175). Wing t/c 0.12 (the 2-175's sparless foam-core
    skin needs depth), quarter-chord sweep 35 deg for a cropped delta."""
    return {"S": S, "AR": AR, "tc": 0.12, "sweep_tc": 35, "fus_width": 4.0, "fus_len": 17.0,
            "fus_dmax": 4.4, "fan_D": fan_D, "duct_len": 0.95 * fan_D, "fin_S": 18.0,
            "drag_factor": k, "W0": W0}


def evaluate(p, h_ft):
    W0 = p["W0"]
    P = perf.power_avail({"hp": 260.0, "cont_hp": 195.0, "crit_alt_ft": h_ft}, h_ft, 0.75)
    r = solve(p, 0.92 * W0, h_ft, P)
    ld, v_ld = max_LD(p, 0.92 * W0, h_ft)
    clb = 10 + 2 * 0.45 * (W0 * h_ft / 0.75) / (550 * 3600)
    rng = range_nm(p, W0 - clb, FUEL_GAL * 6.0 - clb, h_ft, P, 0.45)
    return {"ktas": r["ktas"], "eta": r["eta"], "eta_i": r["eta_i"], "CL": r["CL"], "LD": r["LD"],
            "LDmax": ld, "V_LDmax": v_ld, "range": rng, "b": r["geo"]["b"], "cr": r["geo"]["cr"],
            "Dq_par": r["Dq_par"], "Dq_ind": r["Dq_ind"]}


def lift_slope(AR, sweep_tc=35.0, M=0.15):
    """Raymer eq. 12.6 (Helmbold form with sweep), per radian, F = 1.0 (no
    fuselage lift credit), airfoil efficiency 0.95."""
    b2 = 1 - M * M
    t = math.tan(math.radians(sweep_tc)) ** 2
    return 2 * math.pi * AR / (2 + math.sqrt(4 + AR * AR * b2 / 0.95 ** 2 * (1 + t / b2)))


def landing(S, AR, W=2900.0, alpha_land=14.0, alpha0=-2.0, dCL_flap=0.25):
    """Touchdown speed when lift is limited by the landing attitude, not by
    CLmax: a low-aspect-ratio wing reaches its CLmax only at an angle of attack
    the gear and the pilot's view do not allow. alpha_land 14 deg (E: tail
    clearance and view on a conventional-gear-height airplane); alpha0 -2 deg
    (E, cambered section); dCL_flap 0.25 (E: plain trailing-edge flaps on the
    inboard half of a cropped delta, trimmed). Returns (CL usable, V kt)."""
    CL = lift_slope(AR) * math.radians(alpha_land - alpha0) + dCL_flap
    V = math.sqrt(2 * W / (0.0023769 * S * CL)) / KT
    return CL, V


# --- the 2-175 as built: a sanity check on its design target --------------------
# Fraser's late 3-view (F): span 20 ft, wing 180 ft2, fin 16 ft2, elevons
# 22.8 ft2, gross 1,450 lb; tailless cropped delta, TE unswept, tip chord about
# 4.1 ft, root about 14.7 ft at the centreline (our scaling, E), so taper 0.28 and
# LE sweep about 47 deg. Nose to duct exit about 18.7 ft (E); duct NACA 23015,
# 40.25 in ID, 2.75 ft long; fan 40 in (F, Rohr sketch). Engine 150 hp
# (TWITT). Design target: cruise 152 kt at 10,000 ft (Rohr memo, 8 May 1974, F).
BASE = {"S": 180.0, "AR": 20.0 ** 2 / 180.0, "taper": 0.28, "tc": 0.12, "sweep_tc": 40,
        "fus_width": 3.6, "fus_len": 15.8, "fus_dmax": 3.8, "fan_D": 40.0 / 12, "duct_len": 2.75,
        "fin_S": 16.0, "gear_Dq": 0.45, "W0": 1450.0}


def base_check(k):
    p = dict(BASE, drag_factor=k)
    eng = {"hp": 150.0, "crit_alt_ft": 0.0}
    P = perf.power_avail(eng, 10000.0, 1.0)            # full throttle, normally aspirated
    r = solve(p, 0.95 * 1450, 10000.0, P)
    # power the 152 kt target needs
    lo, hi = 40.0, 400.0
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        v = solve(p, 0.95 * 1450, 10000.0, mid)["ktas"]
        lo, hi = (lo, mid) if v > 152 else (mid, hi)
    return P, r, 0.5 * (lo + hi)


def cg_check(S=210.0, AR=3.0, taper=0.28, W0=2900.0, fuel_gal=105.0):
    """First-cut weight and balance for the four-seat layout, nose datum, ft.
    Positions and masses are ours (E). Returns rows and the CG and neutral-point
    figures in % MAC."""
    b = math.sqrt(S * AR)
    cr = 2 * S / (b * (1 + taper))
    ct = taper * cr
    mac = 2 / 3 * cr * (1 + taper + taper ** 2) / (1 + taper)
    ymac = b / 6 * (1 + 2 * taper) / (1 + taper)
    tanLE = (cr - ct) / (b / 2)                         # TE unswept, as on the 2-175
    x_rootLE = 4.5                                      # E: wing root LE at the cabin's front
    x_mac_le = x_rootLE + tanLE * ymac
    x_ac = x_mac_le + 0.25 * mac
    empty = EF * W0 + LAYOUT_LB
    engine = 285 * 1.25 + 35                            # AM20T installed (stage 3 basis)
    prop = 65.0                                         # fan, duct, stator, shaft (E)
    wing = 0.18 * W0                                    # E
    rest = empty - engine - prop - wing
    items = [("structure, systems, gear (rest of empty)", rest, x_rootLE + 0.45 * cr),
             ("wing", wing, x_mac_le + 0.40 * mac),
             ("AM20T installed, behind the rear seats", engine, 12.8),
             ("fan, duct, stator, shaft", prop, 16.6)]
    loads = {"front seats": (2 * 190, 6.3), "rear seats": (2 * 170, 9.3),
             "fuel (wing)": (fuel_gal * 6, x_mac_le + 0.35 * mac), "baggage": (60, 11.0)}
    cases = {"empty": [], "pilot, 1/3 fuel": [("pilot", 190, 6.3), ("fuel", fuel_gal * 2, loads["fuel (wing)"][1])],
             "two front, full fuel": [("front", 380, 6.3), ("fuel", fuel_gal * 6, loads["fuel (wing)"][1])],
             "four aboard, fuel to gross": None}
    rows = []
    for name, add in cases.items():
        it = list(items)
        if add is None:
            pay = 380 + 340 + 60
            fuel = W0 - empty - pay
            it += [("front", 380, 6.3), ("rear", 340, 9.3), ("bag", 60, 11.0), ("fuel", fuel, loads["fuel (wing)"][1])]
        else:
            it += add
        W = sum(m for _, m, _ in it)
        x = sum(m * xx for _, m, xx in it) / W
        rows.append((name, W, x, (x - x_mac_le) / mac * 100))
    return rows, {"mac": mac, "x_mac_le": x_mac_le, "x_ac": x_ac, "b": b, "cr": cr}


def report():
    L = []
    L.append("### 1. The 2-175 as built, through our method (sanity check on its design target)\n")
    L.append("| Drag factor | Full-throttle power at 10,000 ft | Our KTAS at 10,000 ft | Power the 152 kt target needs | Fan efficiency |")
    L.append("|---|---|---|---|---|")
    for k in (1.16, 1.36):
        P, r, Pn = base_check(k)
        L.append(f"| {k:.2f} | {P:.0f} hp | {r['ktas']:.0f} | {Pn:.0f} hp | {r['eta']:.2f} |")
    L.append("")
    L.append("### 2. Four seats on an AM20T: cruise, range and landing across planforms\n")
    L.append("Gross 2,900 lb; empty 0.60 x gross + 100 lb for the duct, fan, shaft and folds = 1,840 lb; useful 1,060 lb; 105 gal; 195 hp assumed continuous; fan 3.6 ft; drag factor 1.16-1.36 (the stage 3 band). Taper 0.28, trailing edge unswept, as on the 2-175.\n")
    L.append("| Wing, ft2 | AR | Span, ft | Wing loading, lb/ft2 | KTAS at 8,000 ft | KTAS at 16,000 ft | L/D max | Range on 105 gal at 8,000 ft, nm, still air | Touchdown at 14 deg attitude, kt |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for S in (180.0, 210.0, 240.0, 358.0):
        for AR in ((2.2, 3.0, 4.0) if S < 300 else (2.2,)):
            vals = {}
            for k in (1.36, 1.16):
                p = design(S, AR, 3.6, k)
                p["taper"] = 0.28
                e8 = evaluate(p, 8000.0)
                e16 = evaluate(p, 16000.0)
                vals[k] = (e8, e16)
            CL, Vtd = landing(S, AR)
            lo, hi = vals[1.36], vals[1.16]
            L.append(f"| {S:.0f}{' (2-175 wing loading)' if S > 300 else ''} | {AR:.1f} | {math.sqrt(S*AR):.1f} | {2900/S:.1f} | "
                     f"{lo[0]['ktas']:.0f}-{hi[0]['ktas']:.0f} | {lo[1]['ktas']:.0f}-{hi[1]['ktas']:.0f} | "
                     f"{lo[0]['LDmax']:.1f}-{hi[0]['LDmax']:.1f} | {lo[0]['range']:.0f}-{hi[0]['range']:.0f} | {Vtd:.0f} |")
    L.append("")
    L.append("### 3. Fan size at 260 hp (wing 210 ft2, AR 3.0, drag factor 1.25, 8,000 ft)\n")
    L.append("| Fan diameter, ft | Disk loading at 260 hp, hp/ft2 | KTAS | Fan efficiency (ideal) | Note |")
    L.append("|---|---|---|---|---|")
    for D in (3.33, 3.6, 4.0, 4.4):
        p = design(210.0, 3.0, D, 1.25)
        p["taper"] = 0.28
        e = evaluate(p, 8000.0)
        A = math.pi * D * D / 4 * (1 - 0.30 ** 2)
        note = "the 2-175's 40 in fan" if D < 3.4 else ("the 2-175's disk loading at 260 hp" if D > 4.3 else "")
        L.append(f"| {D:.2f} | {260/A:.0f} | {e['ktas']:.0f} | {e['eta']:.2f} ({e['eta_i']:.2f}) | {note} |")
    L.append("")
    L.append("### 4. Balance: a tailless delta with two rows of seats\n")
    rows, g = cg_check()
    L.append(f"Wing 210 ft2, AR 3.0: MAC {g['mac']:.1f} ft, its leading edge {g['x_mac_le']:.1f} ft from the nose. Positions and masses are ours (E).\n")
    L.append("| Loading | Weight, lb | CG, ft from nose | CG, % MAC |")
    L.append("|---|---|---|---|")
    for n, W, x, pct in rows:
        L.append(f"| {n} | {W:,.0f} | {x:.2f} | {pct:.0f} |")
    return "\n".join(L)


if __name__ == "__main__":
    print(report())
