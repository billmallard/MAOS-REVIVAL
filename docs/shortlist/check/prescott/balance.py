"""Prescott Pusher re-derivation (AER-3866): MANUFACTURING's structure delta
folded in, and the aft-CG balance on the AM20T solved option by option.

  python3 balance.py > balance_output.md

Runs from the repo or the analysis workspace: it finds perf.py, the model and
the wetted areas one folder up. Every input below carries its grade:
  F  designer / factory   P  flight test, magazine, NTSB   B  builder
  E  our estimate (method stated)

What this replaces. The stage 3 levers study (levers.py) used structure
placeholders (0 / -100 / -200 lb) and guessed balance arms (engine 8 ft behind
the CG, ballast 6 ft ahead, so 1.33 lb of ballast per lb of engine). Here the
structure delta is MANUFACTURING's (AER-3784, docs/MANUFACTURING.md), and the
arms are fuselage stations measured off the designer's own 1/5-scale plan.

Stations (FS, inches; nose tip = FS 92, as the real aircraft's datum):
  Tom Prescott, "Prescott Pusher", RCM July 1986, plan 971, 3 sheets, drawn by
  the designer, with the full-scale "Prototype" dimension table (F). Article
  text: "The real aircraft has the main wheel located at fuselage station 244
  extended, and retracts to fuselage station 257.4. (The fuselage nose tip is
  station 92.)" Everything else was measured on sheet 1's fuselage side view
  rendered at 200 dpi, scaled so nose tip to spinner tip is the table's
  20.28 ft (the plan's own scale reads 0.7% short). Reading accuracy about
  +/-1 in full scale; the plan is of prototype 1 (N41PP, 1985-86), a
  stand-off-scale model, so treat every measured station as E.
    https://outerzone.co.uk/plan_details.asp?ID=14320
    plan (Wayback): http://web.archive.org/web/20240306064615/https://outerzone.co.uk/download_file.asp?planID=14320&FileType=Plan&Filename=Prescott_Pusher_oz14320.pdf
    article (Wayback): http://web.archive.org/web/20240306064616/https://outerzone.co.uk/download_file.asp?planID=14320&FileType=Supp&Filename=Prescott_Pusher_oz14320_article.pdf
  How each station was read is in README.md ("Balance study").
"""
import itertools
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.dirname(HERE)
sys.path.insert(0, CHECK)
import perf  # noqa: E402

M0 = json.load(open(os.path.join(CHECK, "models", "prescott-pusher.json")))
WET0 = json.load(open(os.path.join(CHECK, "vsp", "prescott-pusher_wet.json")))

# ---------------------------------------------------------------- geometry
# Wing per the RCM prototype table (F): span 30.00 ft, root 4.67 ft, tip
# 3.00 ft, 113 ft2; sweep 10.3 deg (model sheet, reference line not stated:
# taken as the leading edge, E). Root LE measured on the plan at FS 195.1 (E).
ROOT_LE = 195.1
CR, CT, B = 56.0, 36.0, 360.0
LAM = CT / CR
MAC = 2.0 / 3.0 * CR * (1 + LAM + LAM ** 2) / (1 + LAM)            # 46.7 in
Y_MAC = B / 6.0 * (1 + 2 * LAM) / (1 + LAM)                         # 83.5 in
MAC_LE = ROOT_LE + Y_MAC * math.tan(math.radians(10.3))             # FS 210.3


def pct(fs):
    return (fs - MAC_LE) / MAC * 100.0


def fs_of(p):
    return MAC_LE + p / 100.0 * MAC


# Designer's C.G. RANGE, drawn on the wing root of the plan's side view
# (measured FS 216.2 and 222.9). It is the model's range; we read it as the
# designer's full-scale range scaled down, which the plan does not state (E).
CG_FWD, CG_AFT = 216.2, 222.9

# Horizontal tail: RCM table (F) span 11.0 ft, root 3.33, tip 2.17, 29.3 ft2;
# root LE on the plan at FS 292.5, about 6.2 ft above the wing chord plane;
# LE sweep about 19 deg (sheet 2 planform) (E).
HT_S, HT_LE, HT_CR, HT_CT, HT_B = 29.3, 292.5, 40.0, 26.0, 132.0
lam_t = HT_CT / HT_CR
HT_MAC = 2 / 3 * HT_CR * (1 + lam_t + lam_t ** 2) / (1 + lam_t)
HT_AC = HT_LE + HT_B / 6 * (1 + 2 * lam_t) / (1 + lam_t) * math.tan(math.radians(19)) + 0.25 * HT_MAC
WING_AC = fs_of(25.0)
L_T = HT_AC - WING_AC
S_W = 113.0
V_H = HT_S * L_T / (S_W * MAC)

# Neutral point (E). AVL, wing + T-tail as flat lifting surfaces from the
# stations above (prescott_np.avl, AER-3866): Xnp 3.159 ft aft of the root LE,
# FS 233.0, 48.6% MAC. Hand check: 25% + eta V_H (a_t/a)(1 - de/da) with
# a_t 3.9, a 5.07, de/da 0.34 (DATCOM, T-tail) = 49.6%. Fuselage: Raymer
# eq. 16.25, K_fus 0.015 (0.010-0.020) for a wing at 53% of the length, gives
# -10.7% (-7 to -14). Pusher propeller normal force, power on: about +1%.
NP_WT = pct(ROOT_LE + 3.159 * 12)
NP_FUS = -10.7
NP_PROP = 1.0
NP = NP_WT + NP_FUS + NP_PROP
# Stick-free: elevator float takes 20-30% off the tail term (E, typical).
NP_FREE = NP - 0.25 * (NP_WT - 25.0)

# ---------------------------------------------------------------- stations
FS = {
    "front": 180.0,     # front occupants (E): ahead of the spar, behind F-3
    "rear": 220.0,      # rear occupants on the carry-through (P: AOPA86), E
    "bag": 238.0,       # baggage bay behind the rear seats, ahead of F-4 (FS 249)
    "fuel": 212.0,      # leading-edge tanks, 56.5 gal (E)
    "fuel90": 214.0,    # 90 gal reaches further out the swept LE (E)
    "ballast": 100.0,   # nose battery bay (P: battery in the nose, SA86)
    "nosebay": 110.0,   # nose bay where the oil cooler went (P: AOPA86)
    "panel": 160.0,
    "engine": 296.0,    # engine CG: prop flange ~FS 310 behind a 12 in extension,
                        # Lycoming CG ~14 in ahead of its flange; F-5 at FS 279 (E)
    "tailcone": 285.0,  # radiator and duct in the cone (E)
    "wing": fs_of(40.0),
    "tail": HT_AC,
    "main": 244.0,      # F, RCM86 (prototype 1); prototype 2 moved them ~8 in fwd (P)
    "nose_gear": 142.4,
}
H_CG, H_THRUST, H_DRAG, PROP_R, PROP_FS = 36.0, 55.0, 40.0, 32.5, 322.0
# Heights above ground (E): plan side view at the model's gear height; the
# full-scale gear was kept as short as the 65 in propeller allowed (AZ, TP07).

# ---------------------------------------------------------------- weights
O360 = 330.0                    # installed O-360 (E, stage 3)
AM20T_ENGINE = 285.0 * 1.25     # 356 lb: engine, PSRU, turbo, mount, exhaust (E)
AM20T_RAD = 35.0                # radiator, coolant, plumbing (E, stage 3)
RAD_NOSE_LINES = 6.0            # longer coolant lines to a nose radiator (E)
OCC = 170.0                     # standard occupant (Part 23 convention)

# MANUFACTURING's rebuild deltas (docs/MANUFACTURING.md, AER-3784), split to
# where the weight sits (the split is ours, E). Light and heavy ends.
MFG = {
    "light": {"start": 1550.0, "items": [
        ("shell, forward 60%", -42.0, 170.0), ("shell, aft 40%", -28.0, 270.0),
        ("wing to molded carbon", -60.0, None), ("tail to carbon", -15.0, None),
        ("panel to EFIS", -30.0, 160.0), ("EFI backup battery", 5.0, 100.0),
        ("radiator duct / baffles out", -5.0, 285.0)],
        "growth_2700": 30.0},
    "heavy": {"start": 1661.0, "items": [
        ("shell, forward 60%", -15.0, 170.0), ("shell, aft 40%", -10.0, 270.0),
        ("wing to molded carbon", -20.0, None), ("tail to carbon", -5.0, None),
        ("panel to EFIS", -10.0, 160.0), ("EFI backup battery", 10.0, 100.0),
        ("radiator duct", 15.0, 285.0)],
        "growth_2700": 85.0},
}
# The heavy end starts from the one weighed builder aircraft (N747P, 1,661 lb
# with paint, interior, avionics "and ballast for c.g.", SA91, P). Its 111 lb
# over the factory figure is placed at the baseline empty CG (neutral), so if
# part of it was ballast the heavy end double-counts a little: conservative.

GROSS = (2400.0, 2700.0)
FUEL_GAL = {2400.0: 56.5, 2700.0: 90.0}
BASES = {"brochure basis (k 1.35)": 1.35, "measured basis (k 1.55)": 1.55}
CRITS = (8000.0, 16000.0)

# Fixed reference empty CG: the O-360 airplane at the factory's 1,550 lb is
# taken to sit exactly on the designer's aft limit in its most-aft standard
# loading, with no ballast. That is the design as drawn; builders found it
# needed ballast (N747P; "we narrowed the CG envelope"), so this is the
# kindest reading of the original, and every option below is a delta from it.


def loadings(empty_w, gross, fuel_gal, fuel_fs):
    """Standard loadings (E): 1-2 front, 0-2 rear, 0/50/100 lb baggage, fuel
    from a 45 min reserve (8 gal at the AM20T's ~10 gph) to full, capped at
    gross. Returns list of (name, [(w, fs), ...])."""
    out = []
    for nf, nr, bag in itertools.product((1, 2), (0, 1, 2), (0.0, 50.0, 100.0)):
        people = OCC * (nf + nr) + bag
        for fl in ("reserve", "full"):
            fuel = 8.0 * 6.0 if fl == "reserve" else min(fuel_gal * 6.0, gross - empty_w - people)
            if fuel < 48.0 or empty_w + people + fuel > gross + 0.1:
                continue
            out.append((f"{nf} front, {nr} rear, {bag:.0f} lb bags, {fl} fuel",
                        [(OCC * nf, FS["front"]), (OCC * nr, FS["rear"]), (bag, FS["bag"]),
                         (fuel, fuel_fs)]))
    return out


def cg(items):
    w = sum(a for a, _ in items)
    return w, sum(a * x for a, x in items) / w


def envelope(empty_items, gross, fuel_gal, fuel_fs, shift=0.0):
    ew, ex = cg(empty_items)
    res = []
    for name, load in loadings(ew, gross, fuel_gal, fuel_fs):
        load = [(w, x - shift if x in (FS["front"],) else x) for w, x in load]
        w, x = cg(empty_items + load)
        res.append((x, name, w))
    res.sort()
    return ew, ex, res[0], res[-1]


def baseline_empty_cg():
    """Solve the O-360 empty CG that puts the most-aft loading on the aft limit."""
    lo, hi = 150.0, 300.0
    for _ in range(60):
        x = 0.5 * (lo + hi)
        _, _, _, aft = envelope([(1550.0, x)], 2400.0, 56.5, FS["fuel"])
        if aft[0] > CG_AFT:
            hi = x
        else:
            lo = x
    return 0.5 * (lo + hi)


X_E0 = baseline_empty_cg()


def rebuilt_empty(end, gross, radiator):
    """Empty-weight item list for the AM20T rebuild. radiator: 'tail' or 'nose'."""
    d = MFG[end]
    items = [(1550.0, X_E0)]
    if d["start"] > 1550.0:
        items.append((d["start"] - 1550.0, X_E0))
    for name, w, x in d["items"]:
        if x is None:
            x = FS["wing"] if name.startswith("wing") else FS["tail"]
        items.append((w, x))
    items.append((AM20T_ENGINE - O360, FS["engine"]))
    if radiator == "tail":
        items.append((AM20T_RAD, FS["tailcone"]))
    else:
        items.append((AM20T_RAD + RAD_NOSE_LINES, FS["nosebay"]))
    if gross > 2400.0:
        g = d["growth_2700"]
        items += [(0.85 * g, 230.0), (0.15 * g, FS["tail"])]
    return items


def ballast_for(items, gross, fuel_gal, fuel_fs, limit=CG_AFT, at=None, shift=0.0):
    at = FS["ballast"] if at is None else at
    lo, hi = 0.0, 400.0
    _, _, _, aft = envelope(items, gross, fuel_gal, fuel_fs, shift)
    if aft[0] <= limit:
        return 0.0
    for _ in range(50):
        b = 0.5 * (lo + hi)
        _, _, _, aft = envelope(items + [(b, at)], gross, fuel_gal, fuel_fs, shift)
        if aft[0] > limit:
            lo = b
        else:
            hi = b
    return hi


# ------------------------------------------------------- performance (perf.py)
def model_for(gross, k, stretch_in=0.0, grow_area=True):
    """The stage 3 Prescott model; at 2,700 lb the wing and tail grow 12.5% at
    the same aspect ratio (MANUFACTURING's weight assumes that, to hold the
    stall speed), and a fuselage stretch adds length and wetted area."""
    m = json.loads(json.dumps(M0))
    wet = json.loads(json.dumps(WET0))
    m["drag_factor"] = k
    f = gross / 2400.0 if (grow_area and gross > 2400.0) else 1.0
    if f != 1.0:
        s = math.sqrt(f)
        m["Sref"] *= f
        m["lifting"][0]["S"] *= f
        for c in m["components"]:
            if c["name"] in ("Wing", "HTail"):
                c["lref"] *= s
        wet["Wing"]["wet_ft2"] *= f
        wet["HTail"]["wet_ft2"] *= f
    if stretch_in:
        fus = [c for c in m["components"] if c["name"] == "Fuselage"][0]
        fus["lref"] += stretch_in / 12.0
        wet["Fuselage"]["wet_ft2"] += 1.03 * stretch_in   # cabin perimeter ~12.3 ft (E)
    return m, wet


def perf_case(gross, empty, fuel_gal, k, crit, stretch_in=0.0):
    m, wet = model_for(gross, k, stretch_in)
    hp = 260.0
    eng = {"hp": hp, "cont_hp": 0.75 * hp, "crit_alt_ft": crit, "bsfc": 0.45}
    P = perf.power_avail(eng, crit, 0.75)
    sp = perf.solve_speed(m, wet, eng, 0.92 * gross, crit, P)
    fuel_lb = fuel_gal * 6.0
    clb = 10 + 2 * 0.45 * (gross * crit / 0.75) / (550 * 3600)
    rng, _ = perf.cruise_range(m, wet, gross - clb, fuel_lb - clb, crit, sp["V_fts"], 0.45)
    pl45, _ = perf.payload_at(m, wet, gross - clb, empty, 1000.0, crit, sp["V_fts"], 0.45,
                              fuel_lb - clb, 1, 45.0)
    return {"ktas": sp["ktas"], "range": rng, "useful": gross - empty,
            "full_fuel_payload": gross - empty - fuel_lb, "pl1000_45": pl45}


# ------------------------------------------------------------ rotation (E)
def rotation(gross, x_cg, x_mg, hp, eta_to, v_h_scale=1.0):
    """Speed ratio V/Vs(TO) at which full nose-up elevator just balances the
    moments about the main-wheel contact point, and the ratio at which the
    wing lifts the airplane off flat at ground attitude. Quasi-static, out of
    ground effect for the tail. Inputs (E): CLmax with take-off flap 1.6;
    ground-roll CL 0.5; wing Cm_ac -0.12; tail CL at full up elevator -1.0,
    eta 0.95; ground-roll CD 0.06."""
    rho = 0.0023769
    S = S_W * (gross / 2400.0)
    c = MAC * math.sqrt(gross / 2400.0)
    vs = math.sqrt(2 * gross / (rho * S * 1.6))
    st = HT_S * (gross / 2400.0) * v_h_scale
    x_t = HT_AC
    for r in [1.0 + 0.005 * i for i in range(0, 200)]:
        V = r * vs
        q = 0.5 * rho * V * V
        L = q * S * 0.5
        T = eta_to * hp * 550.0 / V
        D = q * S * 0.06
        # Nose-down about the wheels: weight at the CG, thrust on the high
        # thrust line, the wing's pitching moment. Nose-up: wing lift at its
        # AC (ahead of the wheels) and drag above the ground.
        need = gross * (x_mg - x_cg) + T * H_THRUST + q * S * c * 0.12 \
            - D * H_DRAG - L * (x_mg - WING_AC)
        have = 0.95 * q * st * 1.0 * (x_t - x_mg)
        if have >= need:
            return r, math.sqrt(1.6 / 0.5)
    return float("nan"), math.sqrt(1.6 / 0.5)


def prop_strike_deg(x_mg):
    return math.degrees(math.atan((H_THRUST - PROP_R) / (PROP_FS - x_mg)))


def tipback_deg(x_mg, x_cg):
    return math.degrees(math.atan((x_mg - x_cg) / H_CG))


# ------------------------------------------------------------------ report
def fmt(x, d=0):
    return f"{x:,.{d}f}"


def main():
    out = []
    p = out.append
    p("# Prescott Pusher: balance and re-derivation (AER-3866)\n")
    p("Generated by `balance.py`. Every number is ours (E) unless a grade is given; the inputs and their sources are in the script's header and constants.\n")

    p("## 1. Geometry read off the designer's plan\n")
    p("| Item | Value | Basis |")
    p("|---|---|---|")
    p(f"| Datum | nose tip = FS 92 | F, RCM86 text |")
    p(f"| Wing root LE | FS {ROOT_LE:.1f} | E, measured on the plan |")
    p(f"| MAC | {MAC:.1f} in, LE at FS {MAC_LE:.1f} | E, from the RCM table (30 ft, 56/36 in chords) and 10.3 deg LE sweep |")
    p(f"| Designer's C.G. range (plan) | FS {CG_FWD:.1f} to {CG_AFT:.1f} = {pct(CG_FWD):.1f} to {pct(CG_AFT):.1f}% MAC | E, measured; drawn on the model plan, full-scale status not stated |")
    p(f"| Main wheels | FS 244 extended (prototype 1); about FS 236 on prototype 2 | F, RCM86; P, Kitplanes 1988 (moved ~8 in fwd) |")
    p(f"| Horizontal tail AC | FS {HT_AC:.1f}; tail arm {L_T:.1f} in ({L_T/12:.2f} ft) | E, measured |")
    p(f"| Tail volume V_H | {V_H:.2f} | E; GA singles typically 0.6-0.8 (Raymer table 6.4: 0.70) |")
    p(f"| Neutral point, wing + tail (AVL) | {NP_WT:.1f}% MAC (hand check 49.6%) | E, `prescott_np.avl` |")
    p(f"| Neutral point, with fuselage and propeller | {NP:.1f}% MAC (band {NP_WT-14+NP_PROP:.0f}-{NP_WT-7+NP_PROP:.0f}%) | E, Raymer eq. 16.25 |")
    p(f"| Stick-free neutral point | about {NP_FREE:.0f}% MAC | E, elevator float takes 20-30% of the tail term |")
    p(f"| Static margin at the aft limit, stick fixed / free | {NP-pct(CG_AFT):.0f}% / {NP_FREE-pct(CG_AFT):.0f}% MAC | E |")
    p(f"| Engine CG | FS {FS['engine']:.0f}, {FS['engine']-CG_AFT:.0f} in behind the aft limit | E |")
    p(f"| Nose ballast bay | FS {FS['ballast']:.0f}, {CG_AFT-FS['ballast']:.0f} in ahead of the aft limit | E; battery already in the nose (SA86, P) |")
    p(f"| Ballast per lb of engine weight added at the engine CG | {(FS['engine']-CG_AFT)/(CG_AFT-FS['ballast']):.2f} lb | stage 3 assumed 1.33 |")
    p(f"| Reference empty CG, O-360 at 1,550 lb | FS {X_E0:.1f} ({pct(X_E0):.0f}% MAC) | E, solved so the most-aft standard loading sits on the aft limit |")
    p("")

    p("## 2. The balance options, on the AM20T at the re-derived 2,700 lb, 90 gal\n")
    p("Each option is sized so the most-aft standard loading sits on the designer's aft limit "
      f"(FS {CG_AFT:.1f}, {pct(CG_AFT):.0f}% MAC). Light and heavy are MANUFACTURING's two ends. "
      "Added weight is what the option itself costs; useful load is at 2,700 lb gross.\n")
    p("| Option | Structure end | Added weight, lb | Empty, lb | Empty CG, FS (% MAC) | Most-aft loading, FS | Most-forward loading, FS (fwd limit {:.1f}) | Useful load, lb |".format(CG_FWD))
    p("|---|---|---|---|---|---|---|---|")
    gross, fuel_gal, ffs = 2700.0, 90.0, FS["fuel90"]
    rows = {}
    for end in ("light", "heavy"):
        base_t = rebuilt_empty(end, gross, "tail")
        base_n = rebuilt_empty(end, gross, "nose")
        # O0: no fix
        ew, ex, fwd, aft = envelope(base_t, gross, fuel_gal, ffs)
        rows[("O0", end)] = (0.0, ew, ex, aft[0], fwd[0], 0.0)
        # O1: ballast only (radiator in the tail cone)
        b = ballast_for(base_t, gross, fuel_gal, ffs)
        it = base_t + [(b, FS["ballast"])]
        ew, ex, fwd, aft = envelope(it, gross, fuel_gal, ffs)
        rows[("O1", end)] = (b, ew, ex, aft[0], fwd[0], 0.0)
        # O2: masses forward: radiator to the nose (+lines), remote avionics 15 lb
        # from the panel to the nose bay; residual ballast if any
        it = base_n + [(-15.0, FS["panel"]), (15.0, FS["nosebay"])]
        b2 = ballast_for(it, gross, fuel_gal, ffs)
        it2 = it + [(b2, FS["ballast"])]
        ew, ex, fwd, aft = envelope(it2, gross, fuel_gal, ffs)
        rows[("O2", end)] = (RAD_NOSE_LINES + b2, ew, ex, aft[0], fwd[0], 0.0, b2)
        # O3: fuselage stretch ahead of the spar (plug at FS 190): the nose,
        # panel, front seats and occupants move forward; 0.8 lb/in (E); about
        # 270 lb of empty weight sits ahead of the plug (E). Radiator stays in
        # the tail cone: each option is sized alone against the unfixed airplane.
        for dx in range(0, 37):
            ahead = 270.0
            st = base_t + [(-ahead, 150.0), (ahead, 150.0 - dx), (0.8 * dx, 190.0)]
            bb = ballast_for(st, gross, fuel_gal, ffs, shift=dx)
            if bb <= 0.0:
                break
        ew, ex, fwd, aft = envelope(st, gross, fuel_gal, ffs, shift=dx)
        rows[("O3", end)] = (0.8 * dx, ew, ex, aft[0], fwd[0], dx)
        # O4: wing (and the wing-mounted mains and fuel) moved aft; limits and
        # NP move with the wing less the tail-arm loss (0.129 in per in);
        # +10 lb of cage rework (E). Radiator in the tail cone, as for C.
        for dx in range(0, 37):
            wing_items = [(-(210.0 + 70.0), 232.0), (210.0 + 70.0, 232.0 + dx), (10.0, 215.0)]
            lim = CG_AFT + dx * (1 - 0.246 * MAC / L_T)
            ww = base_t + wing_items
            bb = ballast_for(ww, gross, fuel_gal, ffs + dx, limit=lim)
            if bb <= 0.0:
                break
        ew, ex, fwd, aft = envelope(ww, gross, fuel_gal, ffs + dx)
        rows[("O4", end)] = (10.0, ew, ex, aft[0], fwd[0], dx, lim + 0.0, CG_FWD + dx * (1 - 0.246 * MAC / L_T))
    names = {
        "O0": "No fix: AM20T, radiator in the tail cone",
        "O1": "A. Nose ballast (radiator in the tail cone)",
        "O2": "B. Masses forward: radiator and coolant to the nose bay, remote avionics forward; ballast for any rest",
        "O3": "C. Fuselage stretch ahead of the spar",
        "O4": "D. Wing moved aft with its mains and tanks",
    }
    for key in ("O0", "O1", "O2", "O3", "O4"):
        for end in ("light", "heavy"):
            r = rows[(key, end)]
            extra = ""
            if key == "O2":
                extra = f" (incl. {r[6]:.0f} lb ballast)" if r[6] > 0 else " (no ballast)"
            if key == "O3":
                extra = f" ({r[5]} in stretch)"
            if key == "O4":
                extra = f" ({r[5]} in aft; limits move to FS {r[7]:.1f}-{r[6]:.1f})"
            p(f"| {names[key]} | {end} | {r[0]:.0f}{extra} | {fmt(r[1])} | {r[2]:.1f} ({pct(r[2]):.0f}%) | "
              f"{r[3]:.1f}{' **aft of limit by ' + format(r[3]-CG_AFT, '.1f') + ' in**' if key == 'O0' and r[3] > CG_AFT + 0.05 else ''} | "
              f"{r[4]:.1f}{' (fwd of limit)' if r[4] < (r[7] if key == 'O4' else CG_FWD) - 0.05 else ''} | {fmt(gross - r[1])} |")
    p("")
    p("C and D are each sized alone against the unfixed airplane (radiator in the tail cone), so they compare with A directly. "
      f"If the original's real empty CG was aft of our reference (N747P needed ballast; its amount is unpublished), every option grows: "
      f"each inch of empty-CG error at 1,550 lb is about {1550.0/(CG_AFT-FS['ballast']):.0f} lb of nose ballast; "
      f"moving the radiator forward is worth about {(AM20T_RAD*(FS['tailcone']-FS['nosebay']))/1550.0:.1f} in of it.\n")
    p("Ballast at 2,400 lb on the AM20T, the stage 3 engine-swap case (radiator in the tail cone, 56.5 gal): "
      + ", ".join(f"{end} {ballast_for(rebuilt_empty(end, 2400.0, 'tail'), 2400.0, 56.5, FS['fuel']):.0f} lb" for end in ("light", "heavy"))
      + f"; on the published 1,550 lb airplane with only the engine swapped, "
      f"{ballast_for([(1550.0, X_E0), (AM20T_ENGINE - O360, FS['engine']), (AM20T_RAD, FS['tailcone'])], 2400.0, 56.5, FS['fuel']):.0f} lb (stage 3: 82 lb).\n")

    p("## 3. Useful load and range at the re-derived gross, both drag bases\n")
    p("AM20T at the assumed 195 hp continuous; still air, no reserve, full fuel from gross, at continuous power. "
      "Payload with full fuel = useful load - fuel. At 2,700 lb the wing and tail are 12.5% larger (MANUFACTURING's weight assumes it). "
      "Option B is the balance fix in every row except the 'no fix' and 'ballast' rows.\n")
    p("| Gross, fuel | Option | Structure end | Useful load | Payload with full fuel | Basis | KTAS, crit. alt 8k / 16k | Range, nm, 8k / 16k | Payload 1,000 nm + 45 min, 16k (info) | Floors at 16k: load / range / speed |")
    p("|---|---|---|---|---|---|---|---|---|---|")
    for gross in GROSS:
        fg = FUEL_GAL[gross]
        ffs = FS["fuel"] if gross == 2400.0 else FS["fuel90"]
        for key, label in (("O1", "A. ballast"), ("O2", "B. masses forward")):
            for end in ("light", "heavy"):
                if key == "O1":
                    items = rebuilt_empty(end, gross, "tail")
                    b = ballast_for(items, gross, fg, ffs)
                    empty = sum(w for w, _ in items) + b
                else:
                    items = rebuilt_empty(end, gross, "nose") + [(-15.0, FS["panel"]), (15.0, FS["nosebay"])]
                    b = ballast_for(items, gross, fg, ffs)
                    empty = sum(w for w, _ in items) + b
                for bn, k in BASES.items():
                    r8 = perf_case(gross, empty, fg, k, 8000.0)
                    r16 = perf_case(gross, empty, fg, k, 16000.0)
                    ok = lambda c: "pass" if c else "fail"  # noqa: E731
                    pl = "cannot" if r16["pl1000_45"] is None else fmt(r16["pl1000_45"])
                    p(f"| {gross:,.0f} lb, {fg:g} gal | {label} | {end} | {fmt(r16['useful'])} | {fmt(r16['full_fuel_payload'])} | {bn.split(' (')[0]} | "
                      f"{r8['ktas']:.0f} / {r16['ktas']:.0f} | {fmt(r8['range'])} / {fmt(r16['range'])} | {pl} | "
                      f"{ok(r16['useful'] >= 1000)} / {ok(r16['range'] >= 1000)} / {ok(r16['ktas'] > 160)}{'+' if r16['ktas'] >= 180 else ''} |")
    p("")
    # stretch drag cost
    end = "light"
    m_s = [perf_case(2700.0, 1500.0, 90.0, k, 16000.0, s) for k in (1.35, 1.55) for s in (0.0, 12.0)]
    p(f"Drag cost of a 12 in stretch (option C), 2,700 lb, 16k: {m_s[0]['ktas']-m_s[1]['ktas']:.1f} / {m_s[2]['ktas']-m_s[3]['ktas']:.1f} kt "
      f"and {m_s[0]['range']-m_s[1]['range']:.0f} / {m_s[2]['range']-m_s[3]['range']:.0f} nm (brochure / measured basis).\n")
    m_a = [perf_case(2700.0, 1500.0, 90.0, 1.35, 16000.0)]
    mm, ww = model_for(2700.0, 1.35, grow_area=False)
    eng = {"hp": 260.0, "cont_hp": 195.0, "crit_alt_ft": 16000.0, "bsfc": 0.45}
    sp = perf.solve_speed(mm, ww, eng, 0.92 * 2700.0, 16000.0, 195.0)
    p(f"Sensitivity: holding the wing and tail at today's size at 2,700 lb (stage 3's levers did) reads {sp['ktas'] - m_a[0]['ktas']:+.1f} kt faster on the brochure basis at 16k, "
      "but raises the stall speed about 6%, and MANUFACTURING's +30 to +85 lb already pays for the larger wing and tail.\n")

    p("## 4. Rotation and ground geometry (E, quasi-static)\n")
    p(f"Heights above ground (E, from the plan at the model's gear height): CG {H_CG:.0f} in, thrust line {H_THRUST:.0f} in, propeller radius {PROP_R:.1f} in (65 in prop), prop plane FS {PROP_FS:.0f}. "
      "V_rot / Vs is the speed, as a multiple of the take-off-flap stall speed, at which full up elevator can just start the rotation; "
      f"the airplane lifts off flat at ground attitude at about {math.sqrt(1.6/0.5):.2f} Vs, so a V_rot near or above that means it cannot be rotated, it jumps off.\n")
    xe_b = cg(rebuilt_empty("light", 2700.0, "nose") + [(-15.0, FS["panel"]), (15.0, FS["nosebay"])])[1]
    p(f"Tip-back of the empty airplane (option B, CG FS {xe_b:.1f}) bounds how far forward the mains can go: below about 15 deg it sits on its tail when someone steps into the back.\n")
    p("| Case | Mains, FS | CG, FS | Tipback at this CG, deg (typ. 15) | Empty-airplane tipback, deg | Prop-strike pitch about the mains, deg | V_rot / Vs |")
    p("|---|---|---|---|---|---|---|")
    cases = [
        ("O-360, 2,400 lb, aft limit, prototype 1 mains", 2400.0, CG_AFT, 244.0, 180.0, 0.55),
        ("O-360, 2,400 lb, fwd limit, prototype 1 mains", 2400.0, CG_FWD, 244.0, 180.0, 0.55),
        ("O-360, 2,400 lb, aft limit, prototype 2 mains", 2400.0, CG_AFT, 236.0, 180.0, 0.55),
        ("AM20T, 2,700 lb, aft limit, prototype 2 mains", 2700.0, CG_AFT, 236.0, 260.0, 0.60),
        ("AM20T, 2,700 lb, fwd limit, prototype 2 mains", 2700.0, CG_FWD, 236.0, 260.0, 0.60),
        ("AM20T, 2,700 lb, aft limit, mains at FS 232", 2700.0, CG_AFT, 232.0, 260.0, 0.60),
        ("AM20T, 2,700 lb, aft limit, mains FS 236, tail +30%", 2700.0, CG_AFT, 236.0, 260.0, 0.60),
        ("AM20T, 2,700 lb, fwd limit, mains FS 236, tail +30%", 2700.0, CG_FWD, 236.0, 260.0, 0.60),
    ]
    for name, g, xc, xm, hp, eta in cases:
        vs = 1.3 if "tail +30%" in name else 1.0
        r, flat = rotation(g, xc, xm, hp, eta, vs)
        p(f"| {name} | {xm:.0f} | {xc:.1f} | {tipback_deg(xm, xc):.0f} | {tipback_deg(xm, xe_b):.0f} | {prop_strike_deg(xm):.1f} | "
          f"{'above ' + format(flat, '.2f') + ' (jumps off flat)' if r != r or r >= flat else format(r, '.2f')} |")
    p("")
    # thrust-moment equivalent
    dT = (0.60 * 260 - 0.55 * 180) * 550 / (1.1 * math.sqrt(2 * 2400 / (0.0023769 * 113 * 1.6)))
    p(f"The AM20T's extra take-off thrust on the high thrust line adds about {dT*H_THRUST:,.0f} in-lb of nose-down moment at rotation, "
      f"as much as moving the CG {dT*H_THRUST/2400:.1f} in forward at 2,400 lb.\n")
    mt, wt = model_for(2700.0, 1.35)
    wt["HTail"]["wet_ft2"] *= 1.3
    base = perf_case(2700.0, 1500.0, 90.0, 1.35, 16000.0)
    eng = {"hp": 260.0, "cont_hp": 195.0, "crit_alt_ft": 16000.0, "bsfc": 0.45}
    sp30 = perf.solve_speed(mt, wt, eng, 0.92 * 2700.0, 16000.0, 195.0)
    p(f"A 30% larger horizontal tail (V_H {V_H:.2f} to {1.3*V_H:.2f}, about +{0.3*HT_S*1.125*1.0:.0f} ft2 at roughly 1 lb/ft2 in carbon, E) costs {base['ktas']-sp30['ktas']:.1f} kt at 16k on the brochure basis.\n")
    # empty airplane tipping
    for end in ("light", "heavy"):
        it = rebuilt_empty(end, 2700.0, "nose") + [(-15.0, FS["panel"]), (15.0, FS["nosebay"])]
        w, x = cg(it)
        p(f"- Empty airplane, {end} end, option B: CG FS {x:.1f}, {236.0 - x:.1f} in ahead of prototype 2's mains, {232.0 - x:.1f} in ahead of FS 232.")
    p("")
    print("\n".join(out))


if __name__ == "__main__":
    main()
