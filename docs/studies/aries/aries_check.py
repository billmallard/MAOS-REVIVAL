"""AER-3867: Bellanca T-250 Aries, deep independent check of the range result.

Builds on the stage 3 shortlist check (docs/shortlist/check/): same drag
build-up, propeller and range methods (perf.py), same OpenVSP wetted areas,
same Aeromomentum assumptions (run_check.AM20T). What this study adds:

  1. Calibration on every measured speed found: AOPA Pilot (Mar 1977, two
     points) and Flying (Apr 1977, four points), both on the prototype. The
     AOPA cruise point's density altitude comes from its OAT and IAS/TAS pair;
     part-throttle power comes from the Lycoming O-540-A chart. A weight and
     power bracket, because neither magazine states the cruise weight. The
     one production-airframe report (N77CT ferry, 2013) is a pessimistic bound.
  2. Jane's 1979-80 geometry: tailplane span 12 ft 6 in, constant chord 5 ft
     6 in (confirming the chord stage 3 derived from span and area).
  3. A front-side level-flight solver (scan down from high speed, then
     bisect) in place of plain bisection, which can return the back-side
     root at low power.
  4. Range at three loadings (full fuel at MTOW; 1,000 lb payload at MTOW;
     1,000 lb useful load, i.e. empty + 1,000 lb), at continuous power, 65% of
     take-off power, best-range speed and the stage 3 "economy" setting, with
     no reserve and with 45 min, on both assumed engine bases.
  5. What closes the gap: fuel volume, take-off weight, cruise power, and
     individual drag items, each as a change in range.
  6. A sensitivity table: every geometry and calibration input moved across
     its credible range, with the drag factor re-calibrated each time.
  7. A range integrator that flies the final partial fuel step (stage 3's
     drops it), so no-reserve and 45 min ranges are both exact.

Run from the repo root:  python3 docs/studies/aries/aries_check.py
Writes docs/studies/aries/results.json and docs/studies/aries/tables.md.
"""
import copy
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.normpath(os.path.join(HERE, "..", "..", "shortlist", "check"))
sys.path.insert(0, CHECK)
import perf  # noqa: E402
import run_check  # noqa: E402

FT_PER_KT = 1.68781
DENS = 6.0  # lb/gal, as in the shortlist check

# ---------------------------------------------------------------------------
# A drag change applied AFTER the calibration factor. A seal or a better duct
# removes a real, estimated amount of drag; scaling it by the calibration
# factor would credit it with drag it never had.
_parasite = perf.parasite_Dq


def parasite_post(m, wet, h_ft, V_fts, P_hp):
    total, items = _parasite(m, wet, h_ft, V_fts, P_hp)
    d = m.get("delta_Dq_post", 0.0)
    if d:
        items = items + [("drag change (after calibration)", d, "closer item")]
    return total + d, items


perf.parasite_Dq = parasite_post


# perf.cruise_range burns fuel in whole steps and drops the last partial one,
# which understates range by up to one step (5 lb, about 14 nm at 160 KTAS).
# This study's version flies the final fraction, as perf.fuel_for already
# does. The shared stage 3 module is left unchanged.
def cruise_range_frac(m, wet, W0, fuel_lb, h_ft, V_fts, bsfc, nprops=1,
                      reserve_min=0.0, step=10.0):
    W, burned, dist, t = W0, 0.0, 0.0, 0.0
    while True:
        P, _ = perf.power_required(m, wet, W, h_ft, V_fts, nprops)
        ff = bsfc * P  # lb/h
        avail = fuel_lb - burned - ff * reserve_min / 60.0
        if avail <= 0:
            break
        s = min(step, avail)
        dt = s / ff
        dist += V_fts / FT_PER_KT * dt
        t += dt
        burned += s
        W -= s
        if s < step:
            break
    return dist, t


perf.cruise_range = cruise_range_frac

HTAIL_AREA = 12.5 * 2.55


# ---------------------------------------------------------------------------
def load():
    m = json.load(open(os.path.join(CHECK, "models", "bellanca-t250-aries.json")))
    wet = json.load(open(os.path.join(CHECK, "vsp", "bellanca-t250-aries_wet.json")))
    # Jane's 1979-80 (F): "Tailplane span 3-81 m (12 ft 6 in)". Stage 3 used
    # 11.0 ft x 2.55 ft. Chord kept (E), so the stabilator is 31.9 ft2; its
    # wetted area is scaled from the stage 3 OpenVSP result by area ratio.
    wet["HTail"]["wet_ft2"] *= HTAIL_AREA / 28.05
    m["assumptions"].append("AER-3867: stabilator span 12.5 ft (F, Jane's 1979-80), chord 2.55 ft kept (E): 31.9 ft2; "
                            "wing chord 5 ft 6 in constant (F, Jane's) confirms the 5.43 ft used to close 170 ft2.")
    return m, wet


def density_altitude(pa_ft, oat_c):
    """Density altitude from pressure altitude and OAT (ISA troposphere)."""
    p = (1 - 6.8756e-6 * pa_ft) ** 5.2559
    sig = p / ((oat_c + 273.15) / 288.15)
    return (1 - sig ** (1 / 4.2559)) / 6.8756e-6, sig


def gagg_ferrar(sig):
    return sig - (1 - sig) / 7.55


def excess(m, wet, W, h, P, V):
    rho = perf.atmos(h)[0]
    Dq_p, _ = perf.parasite_Dq(m, wet, h, V, P)
    D = 0.5 * rho * V * V * (Dq_p + perf.induced_Dq(m, W, h, V))
    eta, _ = perf.prop_eff(m, D, h, V)
    return eta * P * 550 - D * V


def speed_front(m, wet, W, h, P):
    """Front-side root of eta*P = D*V: scan down from 450 ft/s (267 kt) to the
    first speed with positive excess power, then bisect in that bracket."""
    V = 450.0
    if excess(m, wet, W, h, P, V) > 0:
        raise ValueError("faster than the scan ceiling")
    while V > 120.0:
        if excess(m, wet, W, h, P, V - 2.0) > 0:
            lo, hi = V - 2.0, V
            for _ in range(30):
                mid = 0.5 * (lo + hi)
                lo, hi = (mid, hi) if excess(m, wet, W, h, P, mid) > 0 else (lo, mid)
            return 0.5 * (lo + hi)
        V -= 2.0
    raise ValueError(f"no level flight at {P:.0f} hp, {h:.0f} ft, {W:.0f} lb")


def k_match(m, wet, W, h, P, ktas):
    """Drag factor that makes the build-up fly ktas at P."""
    mm = copy.deepcopy(m)
    lo, hi = 0.5, 3.0
    for _ in range(30):
        mm["drag_factor"] = 0.5 * (lo + hi)
        v = speed_front(mm, wet, W, h, P) / FT_PER_KT
        lo, hi = (mm["drag_factor"], hi) if v > ktas else (lo, mm["drag_factor"])
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# AOPA Pilot flight check, March 1977, prototype N51AG (grade P):
# https://aeroresourcesinc.com/uploads/197703-1977%20Bellanca%20Aries%20T-250.pdf
# Cruise: 6,500 ft, OAT 50 F, 22.5 inHg full throttle / 2,300 rpm, "73%" by
# AOPA's calculation, 185 mph IAS, 208 mph TAS, "partially loaded".
# Full throttle: 1,000 ft, 2,575 rpm, 215 mph IAS, 217 mph TAS, choppy air.
DA_CRUISE, SIG_CRUISE = density_altitude(6500, 10.0)       # OAT 50 F = 10 C
DA_FT1000 = (1 - ((215 / 217) ** 2) ** (1 / 4.2559)) / 6.8756e-6  # from IAS/TAS
TEMP_CORR = math.sqrt((15 - 1.98 * 6.5 + 273.15) / (10 + 273.15))  # Lycoming: hp ~ 1/sqrt(T)


def lyc_pct_2300(mp_in, pa_ft):
    """Percent of rated power for the O-540-A at 2,300 rpm (grade E, ours).
    Sea-level slope read off Lycoming Operator's Manual 60297-10, Fig. 3-2
    (part-throttle curve, O-540-A): 65% at about 21.2 inHg, about 2.7% per
    inch. Altitude correction 1.0% per 1,000 ft, anchored on AOPA's own "73%"
    for 22.5 inHg / 2,300 rpm at 6,500 ft; Collins's "nearly 75-percent" at
    22.8 inHg checks it. ISA temperature (Flying gives no OAT)."""
    return (65.0 + 2.7 * (mp_in - 21.2)) * (1 + 0.010 * pa_ft / 1000.0)


def cal_points(w_cruise=None, hp_cruise=None, da_cruise=None, w_ft=None, w_flying=None,
               hp_scale=1.0):
    """Measured points (grade P), all on the prototype N51AG with the
    carbureted O-540. Flying, Apr 1977, R. L. Collins (Google Books volume
    wKfgQo2Zw3MC): 4,500 ft, 23 in / 2,300, 163 KIAS, 175 KTAS; 6,500 ft,
    21.5 in / 2,300, 173 KTAS; 22.8 in / 2,300, 181 KTAS ("nearly 75-percent
    power", altitude not stated); two-way VOR run at 6,000 ft pressure
    altitude, 177.6 kt, "probably a shade below 75 percent". OAT not given:
    ISA. Weights: neither magazine gives the cruise weight. AOPA "partially
    loaded" -> 0.9 MTOW; Flying "300 pounds below gross weight for our
    initial flight" -> 2,850 lb (E for the cruise runs)."""
    mtow = 3150
    wf = w_flying or 2850.0
    return [
        {"name": "AOPA cruise, 6,500 ft, 22.5 in / 2,300", "ktas": 208 / 1.15078,
         "alt": da_cruise if da_cruise is not None else DA_CRUISE,
         "hp": (hp_cruise if hp_cruise is not None else 0.73 * 250 * TEMP_CORR) * hp_scale,
         "W": w_cruise or 0.9 * mtow},
        {"name": "AOPA full throttle, 1,000 ft, 2,575", "ktas": 217 / 1.15078, "alt": DA_FT1000,
         "hp": 250 * gagg_ferrar(perf.atmos(DA_FT1000)[3]),
         "W": w_ft or 0.9 * mtow},
        {"name": "Flying, 4,500 ft, 23 in / 2,300 (163 KIAS)", "ktas": 175.0, "alt": 4500.0,
         "hp": 2.5 * lyc_pct_2300(23.0, 4500) * hp_scale, "W": wf},
        {"name": "Flying, 6,500 ft, 21.5 in / 2,300", "ktas": 173.0, "alt": 6500.0,
         "hp": 2.5 * lyc_pct_2300(21.5, 6500) * hp_scale, "W": wf},
        {"name": "Flying, 22.8 in / 2,300, altitude not stated (6,500 ft taken)", "ktas": 181.0,
         "alt": 6500.0, "hp": 2.5 * lyc_pct_2300(22.8, 6500) * hp_scale, "W": wf},
        {"name": "Flying, two-way VOR run, 6,000 ft, 'a shade below 75%' (73% taken)", "ktas": 177.6,
         "alt": 6000.0, "hp": 0.73 * 250 * hp_scale, "W": wf},
    ]


# Production airframe N77CT (s/n 0004), ferry flight Dec 2013 (grade B):
# "only able to get about 190MPH TAS instead of the 208MPH TAS promised by the
# manual" (TheWebWingman, Wayback feed capture 20140509072721). Altitude and
# power not stated; the post mentions an IFR leg at 8,000 ft. Engine repaired
# with components of unknown time (sale listing, 2014), compressions 70-78/80.
FERRY = {"name": "N77CT ferry 2013, ~190 mph; 8,000 ft and 70% assumed", "ktas": 190 / 1.15078,
         "alt": 8000.0, "hp": 0.70 * 250, "W": 2900.0}


def calibrate(m, wet, pts):
    ks = [k_match(m, wet, p["W"], p["alt"], p["hp"], p["ktas"]) for p in pts]
    return ks, sum(ks) / len(ks)


# ---------------------------------------------------------------------------
def engine(case, cont_hp=195.0, bsfc=0.45):
    e = dict(run_check.AM20T, cont_hp=cont_hp, bsfc=bsfc)
    e["crit_alt_ft"] = {"AM-low": 8000.0, "AM-high": 16000.0}[case]
    return e


CRUISE_ALT = {"AM-low": 8000.0, "AM-high": 16000.0}


def fly(m, wet, eng, h, V, W0, fuel_lb, reserve_min):
    """Climb allowance, then constant-speed cruise. Returns nm."""
    clb = run_check.climb_allowance(W0, h, bsfc=eng["bsfc"])
    if fuel_lb <= clb:
        return 0.0
    nm, _ = perf.cruise_range(m, wet, W0 - clb, fuel_lb - clb, h, V, eng["bsfc"],
                              1, reserve_min, step=5.0)
    return nm


def setting_speed(m, wet, eng, h, P, mtow):
    return speed_front(m, wet, 0.92 * mtow, h, P)


def best_range_speed(m, wet, eng, h, W0, fuel_lb, reserve_min):
    best = (0, None)
    for kt in range(110, 200, 2):
        nm = fly(m, wet, eng, h, kt * FT_PER_KT, W0, fuel_lb, reserve_min)
        if nm > best[0]:
            best = (nm, kt)
    return best[1], best[0]


def power_at(m, wet, W, h, V):
    P, _ = perf.power_required(m, wet, W, h, V)
    return P


def loadings(mtow, empty, fuel_max):
    """name -> (takeoff weight, fuel lb, payload lb)."""
    return {
        "A full fuel at MTOW": (mtow, fuel_max, mtow - empty - fuel_max),
        "B 1,000 lb payload at MTOW": (mtow, min(fuel_max, mtow - empty - 1000.0), 1000.0),
        "C 1,000 lb useful (empty + 1,000 lb), full fuel":
            (empty + 1000.0, fuel_max, 1000.0 - fuel_max),
    }


def payload_range(m, wet, eng, h, V, mtow, empty, fuel_max, reserve_min):
    """Max payload that flies 1,000 nm (MTOW-limited), and the fuel it needs."""
    clb = run_check.climb_allowance(mtow, h, bsfc=eng["bsfc"])
    f = perf.fuel_for(m, wet, mtow - clb, 1000.0, h, V, eng["bsfc"], 1, reserve_min) + clb
    return (None if f > fuel_max else mtow - empty - f), f


def speed_for_range(m, wet, eng, h, W0, fuel_lb, reserve_min, target=1000.0):
    """Fastest constant speed that still makes target nm. Not capped at the
    speed the engine can reach: callers compare with the continuous-power
    speed (every use in this study falls below it; aries_closers.py caps)."""
    for kt in range(220, 100, -1):
        if fly(m, wet, eng, h, kt * FT_PER_KT, W0, fuel_lb, reserve_min) >= target:
            return kt
    return None


def gal_for(m, wet, eng, h, V, mtow, reserve_min, target=1000.0):
    """Usable fuel (gal) to fly target nm from MTOW."""
    clb = run_check.climb_allowance(mtow, h, bsfc=eng["bsfc"])
    f = perf.fuel_for(m, wet, mtow - clb, target, h, V, eng["bsfc"], 1, reserve_min) + clb
    return f / DENS


# ---------------------------------------------------------------------------
def perturb(m, wet, key, val):
    """Return (m, wet) with one input moved. Wetted areas of the tails and
    fuselage scale analytically (area ratio; perimeter ratio), not by a new
    OpenVSP run: adequate for a sensitivity, stated as such."""
    m, wet = copy.deepcopy(m), copy.deepcopy(wet)
    if key == "htail_area":       # base HTAIL_AREA (12.5 x 2.55)
        wet["HTail"]["wet_ft2"] *= val / HTAIL_AREA
    elif key == "fin_area":       # base 15 ft2
        wet["Fin"]["wet_ft2"] *= val / 15.0
    elif key in ("fus_width", "fus_height"):
        w = val if key == "fus_width" else 4.0
        hgt = val if key == "fus_height" else 4.4
        wet["Fuselage"]["wet_ft2"] *= (w + hgt) / 8.4
        for c in m["components"]:
            if c["name"] == "Fuselage":
                c["dmax"] = math.sqrt(w * hgt)
    elif key == "xtr_wing":
        for c in m["components"]:
            if c["name"] == "Wing":
                c["xtr"] = val
    elif key == "tc_wing":
        for c in m["components"]:
            if c["name"] == "Wing":
                c["tc"] = val
    elif key == "excrescence":
        m["excrescence_frac"] = val
    elif key == "cooling":
        m["cooling_factor"] = val
    elif key == "prop_install":
        m["prop"]["install"] = val
    else:
        raise KeyError(key)
    return m, wet


def headline(m, wet, k, eng_case, cont_hp=195.0, bsfc=0.45, mtow=3150, fuel_gal=76):
    mm = copy.deepcopy(m)
    mm["drag_factor"] = k
    eng = engine(eng_case, cont_hp, bsfc)
    h = CRUISE_ALT[eng_case]
    P = perf.power_avail(eng, h, eng["cont_hp"] / eng["hp"])
    V = setting_speed(mm, wet, eng, h, P, mtow)
    r45 = fly(mm, wet, eng, h, V, mtow, fuel_gal * DENS, 45.0)
    r0 = fly(mm, wet, eng, h, V, mtow, fuel_gal * DENS, 0.0)
    return V / FT_PER_KT, r0, r45


def main():
    m, wet = load()
    mtow, empty, fuel_max = 3150.0, 1850.0, 76 * DENS
    out = {"inputs": {"DA_cruise_ft": DA_CRUISE, "sigma_cruise": SIG_CRUISE,
                      "DA_fullthrottle_ft": DA_FT1000, "temp_corr": TEMP_CORR}}

    # --- 1. calibration
    m1 = copy.deepcopy(m)
    m1["drag_factor"] = 1.0
    stage3 = [{"name": "AOPA cruise (stage 3 basis)", "ktas": 180.7, "alt": 6500, "hp": 182.5, "W": 2835},
              {"name": "AOPA full throttle (stage 3 basis)", "ktas": 188.6, "alt": 1000, "hp": 242, "W": 2835}]
    pts = cal_points()
    cal = []
    for p in stage3 + pts + [FERRY]:
        V = speed_front(m1, wet, p["W"], p["alt"], p["hp"]) / FT_PER_KT
        cal.append(dict(p, raw_ktas=V, k=k_match(m1, wet, p["W"], p["alt"], p["hp"], p["ktas"])))
    ks_new = [c["k"] for c in cal[2:2 + len(pts)]]
    k_own = sum(ks_new) / len(ks_new)
    k_fleet = json.load(open(os.path.join(CHECK, "calib.json")))["k_global"]
    k = max(k_own, k_fleet)
    k_ferry = cal[-1]["k"]
    # bracket: cruise weight 2,600-3,150 lb on every point; power -5% / +5% on
    # every part-throttle point; AOPA cruise density altitude 6,500-7,900 ft
    brk = {}
    for lab, kw in [("all weights 2,600", dict(w_cruise=2600, w_ft=2600, w_flying=2600)),
                    ("all weights 3,150", dict(w_cruise=3150, w_ft=3150, w_flying=3150)),
                    ("part-throttle power -5%", dict(hp_scale=0.95)),
                    ("part-throttle power +5%", dict(hp_scale=1.05)),
                    ("AOPA DA 6,500", dict(da_cruise=6500)), ("AOPA DA 7,900", dict(da_cruise=7900))]:
        brk[lab] = calibrate(m1, wet, cal_points(**kw))[1]
    out["calibration"] = {"points": cal, "k_own": k_own, "k_fleet": k_fleet, "k": k,
                          "k_ferry": k_ferry, "bracket_mean_k": brk}

    m["drag_factor"] = k
    # factory figures (F, altitude not stated): what altitude makes them true?
    fac = []
    for lab, ktas, hp in [("factory 75% (208 mph)", 180.7, 187.5), ("factory 65% (200 mph)", 173.8, 162.5)]:
        found = None
        for h in range(0, 16001, 250):
            if 250 * gagg_ferrar(perf.atmos(h)[3]) < hp:
                break
            if speed_front(m, wet, 0.9 * mtow, h, hp) / FT_PER_KT >= ktas:
                found = h
        fac.append({"label": lab, "ktas": ktas, "hp": hp,
                    "highest_alt_ft_that_reaches_it": found,
                    "ktas_at_7500": speed_front(m, wet, 0.9 * mtow, 7500, hp) / FT_PER_KT})
    out["factory_check"] = fac
    # factory ranges (Jane's 1979-80: four occupants, max fuel, 45 min reserve
    # at 45% power) -> implied BSFC, no climb allowance, on 76 (TCDS) and 72
    # (Jane's) gal usable. The 55% speed is not published: our model's.
    V55 = speed_front(m, wet, 0.9 * mtow, 8000, 137.5) / FT_PER_KT
    out["factory_range_flow"] = []
    for lab, nm, ktas, hp in [("75%: 860 nm", 860, 180.7, 187.5), ("65%: 946 nm", 946, 173.8, 162.5),
                              ("55%: 1,016 nm (speed: ours at 8,000 ft)", 1016, V55, 137.5)]:
        hphr = hp * nm / ktas + 0.45 * 250 * 0.75
        out["factory_range_flow"].append({"label": lab, "nm": nm, "ktas": ktas, "hp": hp,
                                          "bsfc76": 76 * DENS / hphr, "bsfc72": 72 * DENS / hphr})
    # original O-540 at 75/65/55%, BSFC 0.45, climb allowance, our model
    o540 = {"hp": 250.0, "crit_alt_ft": 0.0, "bsfc": 0.45}
    out["orig_factory_compare"] = []
    for lab, hp, pub in [("75%", 187.5, 860), ("65%", 162.5, 946), ("55%", 137.5, 1016)]:
        h = 6500 if hp > 180 else 8000
        Vx = speed_front(m, wet, 0.92 * mtow, h, hp)
        out["orig_factory_compare"].append({"label": lab, "alt": h, "ktas": Vx / FT_PER_KT, "pub": pub,
                                            "nm45": fly(m, wet, o540, h, Vx, mtow, fuel_max, 45)})

    # --- 2. range matrix
    mat = {}
    for case in ("AM-low", "AM-high"):
        eng = engine(case)
        h = CRUISE_ALT[case]
        Pc = perf.power_avail(eng, h, eng["cont_hp"] / eng["hp"])
        settings = {"continuous (195 hp, 75% of 260)": Pc,
                    "65% of take-off (169 hp)": 0.65 * 260,
                    "stage 3 'economy' (127 hp = 65% of 195)": 0.65 * Pc}
        rows = []
        for sname, P in settings.items():
            V = setting_speed(m, wet, eng, h, P, mtow)
            for lname, (W0, fuel, pay) in loadings(mtow, empty, fuel_max).items():
                rows.append({"setting": sname, "hp": P, "ktas": V / FT_PER_KT,
                             "kcas": V / FT_PER_KT * math.sqrt(perf.atmos(h)[3]),
                             "loading": lname, "W0": W0, "fuel_gal": fuel / DENS, "payload": pay,
                             "nm0": fly(m, wet, eng, h, V, W0, fuel, 0.0),
                             "nm45": fly(m, wet, eng, h, V, W0, fuel, 45.0)})
            pr0, _ = payload_range(m, wet, eng, h, V, mtow, empty, fuel_max, 0.0)
            pr45, f45 = payload_range(m, wet, eng, h, V, mtow, empty, fuel_max, 45.0)
            rows.append({"setting": sname, "hp": P, "ktas": V / FT_PER_KT, "loading": "payload at 1,000 nm",
                         "pay0": pr0, "pay45": pr45, "fuel45_gal": f45 / DENS})
        for lname, (W0, fuel, pay) in loadings(mtow, empty, fuel_max).items():
            for resv in (0.0, 45.0):
                kt, nm = best_range_speed(m, wet, eng, h, W0, fuel, resv)
                rows.append({"setting": "best-range speed", "loading": lname, "reserve": resv,
                             "ktas": kt, "hp": power_at(m, wet, 0.92 * W0, h, kt * FT_PER_KT),
                             "nm": nm})
        fastest = {}
        for lname, (W0, fuel, pay) in loadings(mtow, empty, fuel_max).items():
            for resv in (0.0, 45.0):
                kt = speed_for_range(m, wet, eng, h, W0, fuel, resv)
                fastest[f"{lname} | {int(resv)} min"] = None if kt is None else {
                    "ktas": kt, "hp": power_at(m, wet, 0.92 * W0, h, kt * FT_PER_KT)}
        mat[case] = {"rows": rows, "fastest_for_1000": fastest, "Pc": Pc}
    out["matrix"] = mat

    # --- 3. closers (continuous power, full fuel at MTOW, 45 min)
    clos = {}
    for case in ("AM-low", "AM-high"):
        eng = engine(case)
        h = CRUISE_ALT[case]
        Pc = mat[case]["Pc"]
        V = setting_speed(m, wet, eng, h, Pc, mtow)
        base45 = fly(m, wet, eng, h, V, mtow, fuel_max, 45.0)
        base0 = fly(m, wet, eng, h, V, mtow, fuel_max, 0.0)
        c = {"base": {"ktas": V / FT_PER_KT, "nm45": base45, "nm0": base0}}
        c["fuel_gal_needed_45"] = gal_for(m, wet, eng, h, V, mtow, 45.0)
        c["fuel_gal_needed_0"] = gal_for(m, wet, eng, h, V, mtow, 0.0)
        need = None
        for dW in range(0, 801, 10):
            W0 = mtow + dW
            Vw = setting_speed(m, wet, eng, h, Pc, W0)
            clb = run_check.climb_allowance(W0, h, bsfc=eng["bsfc"])
            f = perf.fuel_for(m, wet, W0 - clb, 1000.0, h, Vw, eng["bsfc"], 1, 45.0) + clb
            if W0 - empty - f >= 1000.0:
                need = {"dW": dW, "fuel_gal": f / DENS, "ktas": Vw / FT_PER_KT}
                break
        c["mtow_for_1000lb_payload_45"] = need
        items = []
        for lab, edit in [
            ("Radiator in a designed duct: cooling drag -40%", ("cool", 0.60)),
            ("Gap seals on ailerons, flaps, stabilator, rudder", ("post", -0.03)),
            ("Leakage sealing, root fillet, gear-door and wheel-well seals", ("post", -0.03)),
            ("Laminar run on the wing 0.25 -> 0.40 chord (smooth bonded skin)", ("xtr", 0.40)),
            ("Modern propeller, +3% efficiency", ("prop", 1.03)),
        ]:
            mm, ww = copy.deepcopy(m), wet
            if edit[0] == "cool":
                mm["cooling_factor"] = edit[1]
            elif edit[0] == "post":
                mm["delta_Dq_post"] = edit[1]
            elif edit[0] == "xtr":
                mm, ww = perturb(m, wet, "xtr_wing", edit[1])
                mm["drag_factor"] = k
            elif edit[0] == "prop":
                mm["prop"]["install"] = edit[1]
            Vi = setting_speed(mm, ww, eng, h, Pc, mtow)
            items.append({"label": lab, "ktas": Vi / FT_PER_KT,
                          "nm45": fly(mm, ww, eng, h, Vi, mtow, fuel_max, 45.0)})
        mm, ww = perturb(m, wet, "xtr_wing", 0.40)
        mm["drag_factor"] = k
        mm["cooling_factor"] = 0.60
        mm["delta_Dq_post"] = -0.06
        mm["prop"]["install"] = 1.03
        Vi = setting_speed(mm, ww, eng, h, Pc, mtow)
        items.append({"label": "All five together", "ktas": Vi / FT_PER_KT,
                      "nm45": fly(mm, ww, eng, h, Vi, mtow, fuel_max, 45.0)})
        for b in (0.42, 0.48):
            e2 = engine(case, bsfc=b)
            items.append({"label": f"BSFC {b} instead of 0.45 (engine; not published)",
                          "ktas": V / FT_PER_KT, "nm45": fly(m, wet, e2, h, V, mtow, fuel_max, 45.0)})
        c["items"] = items
        clos[case] = c
    out["closers"] = clos

    # --- 4. sensitivity: move one input, re-calibrate, report headline
    base_m, base_wet = load()
    base_m["drag_factor"] = 1.0
    sens = []

    def run_one(mm, ww, pts_kw=None, cont=195.0, bsfc=0.45):
        mm = copy.deepcopy(mm)
        mm["drag_factor"] = 1.0
        _, kk = calibrate(mm, ww, cal_points(**(pts_kw or {})))
        r = {case: headline(mm, ww, kk, case, cont, bsfc) for case in ("AM-low", "AM-high")}
        return kk, r

    k0, r0 = run_one(base_m, base_wet)
    sens.append({"input": "baseline", "k": k0, "res": r0})
    cases = [
        ("Stabilator area 31.9 ft2 (span F, Jane's; chord E)", "htail_area", [24.0, 40.0]),
        ("Fin area 15 ft2 (E, volume coefficient)", "fin_area", [10.5, 19.5]),
        ("Fuselage max width 4.0 ft (E)", "fus_width", [3.7, 4.3]),
        ("Fuselage max height 4.4 ft (E)", "fus_height", [4.1, 4.7]),
        ("Wing laminar run 0.25 c (E)", "xtr_wing", [0.10, 0.40]),
        ("Wing t/c 0.12 (F/B, '600412')", "tc_wing", [0.10, 0.15]),
        ("Leakage and protuberance 5% (E)", "excrescence", [0.03, 0.10]),
        ("Cooling drag factor 1.0 (E)", "cooling", [0.6, 1.4]),
        ("Propeller installation factor 1.00 (E)", "prop_install", [0.97, 1.03]),
    ]
    for lab, key, vals in cases:
        for v in vals:
            mm, ww = perturb(base_m, base_wet, key, v)
            kk, r = run_one(mm, ww)
            mm["drag_factor"] = k0
            rn = {case: headline(mm, ww, k0, case) for case in ("AM-low", "AM-high")}
            sens.append({"input": lab, "value": v, "k": kk, "res": r, "res_uncal": rn})
    for lab, kw in [("Test weight at every measured point (E: 2,835 AOPA, 2,850 Flying)",
                     [dict(w_cruise=2600, w_ft=2600, w_flying=2600), dict(w_cruise=3150, w_ft=3150, w_flying=3150)]),
                    ("Power at every part-throttle point (E, Lycoming chart)", [dict(hp_scale=0.95), dict(hp_scale=1.05)]),
                    ("AOPA cruise density altitude 7,400 ft (ours, from IAS/TAS and OAT)",
                     [dict(da_cruise=6500), dict(da_cruise=7900)])]:
        for v in kw:
            kk, r = run_one(base_m, base_wet, pts_kw=v)
            sens.append({"input": lab, "value": v, "k": kk, "res": r})
    for lab, kwv in [("AM20T continuous power 195 hp (assumed)", [("cont", 180.0), ("cont", 210.0)]),
                     ("AM20T BSFC 0.45 lb/hp/h (assumed)", [("bsfc", 0.42), ("bsfc", 0.50)])]:
        for kind, v in kwv:
            r = {case: headline(base_m, base_wet, k0, case, v if kind == "cont" else 195.0,
                                v if kind == "bsfc" else 0.45) for case in ("AM-low", "AM-high")}
            sens.append({"input": lab, "value": v, "k": k0, "res": r})
    r = {case: headline(base_m, base_wet, k_ferry, case) for case in ("AM-low", "AM-high")}
    sens.append({"input": "Drag factor from the N77CT ferry report (B, conditions assumed)",
                 "value": round(k_ferry, 3), "k": k_ferry, "res": r})
    out["sensitivity"] = sens

    json.dump(out, open(os.path.join(HERE, "results.json"), "w"), indent=1, default=float)
    write_tables(out)
    return out


def f0(x):
    return "cannot" if x is None else f"{x:,.0f}"


def write_tables(o):
    L = ["# AER-3867 Aries deep check: generated tables",
         "",
         "Generated by `aries_check.py`; do not edit by hand. Every number is our",
         "estimate (grade E) unless the row says otherwise. AM20T continuous power",
         "195 hp, BSFC 0.45 and both critical altitudes are ASSUMED (not published).",
         ""]
    c = o["calibration"]
    i = o["inputs"]
    L += ["## 1. Calibration", "",
          f"AOPA cruise point density altitude: {i['DA_cruise_ft']:,.0f} ft (sigma {i['sigma_cruise']:.3f}) "
          f"from 6,500 ft and OAT 50 F; full-throttle point {i['DA_fullthrottle_ft']:,.0f} ft from 215 mph IAS / 217 mph TAS. "
          f"Temperature correction on AOPA's 73%: x{i['temp_corr']:.3f}.", "",
          "| Point | KTAS | Density alt, ft | hp | Weight, lb | Raw build-up KTAS | Drag factor to match |",
          "|---|---|---|---|---|---|---|"]
    for p in c["points"]:
        L.append(f"| {p['name']} | {p['ktas']:.1f} | {p['alt']:,.0f} | {p['hp']:.1f} | {p['W']:,.0f} | {p['raw_ktas']:.1f} | {p['k']:.3f} |")
    L += ["", "Rows 1-2: the stage 3 basis, kept for comparison. Rows 3-8: the measured points used (P). "
          "Last row: the N77CT ferry report (B), not used in the mean.", "",
          f"Own factor (mean of the six measured points): **{c['k_own']:.3f}**; fleet {c['k_fleet']:.2f}; "
          f"used: **{c['k']:.3f}**. Ferry report implies {c['k_ferry']:.3f}.", "",
          "Bracket on the mean factor: " +
          ", ".join(f"{a} {b:.3f}" for a, b in c["bracket_mean_k"].items()), ""]
    L += ["## 2. Factory figures (F, altitude not stated) against the calibrated model", "",
          "| Figure | KTAS | hp | Highest altitude where the model reaches it, ft | Model KTAS at 7,500 ft |",
          "|---|---|---|---|---|"]
    for r in o["factory_check"]:
        L.append(f"| {r['label']} | {r['ktas']:.1f} | {r['hp']:.1f} | {f0(r['highest_alt_ft_that_reaches_it'])} | {r['ktas_at_7500']:.1f} |")
    L += ["", "Jane's 1979-80 ranges (four occupants, max fuel, 45 min reserve at 45% power), implied BSFC with no climb allowance:", "",
          "| Factory range | KTAS | hp | Implied BSFC on 76 gal (TCDS) | on 72 gal (Jane's) |", "|---|---|---|---|---|"]
    for r in o["factory_range_flow"]:
        L.append(f"| {r['label']} | {r['ktas']:.0f} | {r['hp']:.1f} | {r['bsfc76']:.3f} | {r['bsfc72']:.3f} |")
    L += ["", "Original O-540, our model (BSFC 0.45, climb allowance, 45 min at cruise power, 76 gal):", "",
          "| Power | Altitude, ft | KTAS | nm, 45 min | Jane's, nm |", "|---|---|---|---|---|"]
    for r in o["orig_factory_compare"]:
        L.append(f"| {r['label']} | {r['alt']:,} | {r['ktas']:.0f} | {r['nm45']:.0f} | {r['pub']} |")
    L += ["", "## 3. Range on the AM20T", ""]
    for case, d in o["matrix"].items():
        L += [f"### {case} (critical altitude {'8,000' if case == 'AM-low' else '16,000'} ft, assumed; cruise at that altitude)", "",
              "| Setting | hp | KTAS | KCAS | Loading | Take-off, lb | Fuel, gal | Payload, lb | nm, no reserve | nm, 45 min |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        for r in d["rows"]:
            if "nm0" in r:
                L.append(f"| {r['setting']} | {r['hp']:.0f} | {r['ktas']:.0f} | {r['kcas']:.0f} | {r['loading']} | {r['W0']:,.0f} | "
                         f"{r['fuel_gal']:.0f} | {r['payload']:,.0f} | {r['nm0']:,.0f} | {r['nm45']:,.0f} |")
        L += ["", "| Setting | KTAS | Max payload at 1,000 nm, no reserve | with 45 min | Fuel for 1,000 nm + 45 min, gal |", "|---|---|---|---|---|"]
        for r in d["rows"]:
            if r["loading"] == "payload at 1,000 nm":
                L.append(f"| {r['setting']} | {r['ktas']:.0f} | {f0(r['pay0'])} | {f0(r['pay45'])} | {r['fuel45_gal']:.0f} |")
        L += ["", "| Best-range speed | Loading | Reserve, min | KTAS | hp | nm |", "|---|---|---|---|---|---|"]
        for r in d["rows"]:
            if r["setting"] == "best-range speed":
                L.append(f"| best range | {r['loading']} | {int(r['reserve'])} | {r['ktas']} | {r['hp']:.0f} | {r['nm']:,.0f} |")
        L += ["", "| Fastest constant speed that still makes 1,000 nm | KTAS | hp |", "|---|---|---|"]
        for kk, v in d["fastest_for_1000"].items():
            L.append(f"| {kk} | {'cannot' if v is None else v['ktas']} | {'-' if v is None else round(v['hp'])} |")
        L.append("")
    L += ["## 4. What closes the gap (continuous power, full fuel at MTOW, 45 min reserve)", ""]
    for case, cdat in o["closers"].items():
        b = cdat["base"]
        L += [f"### {case}", "",
              f"Baseline: {b['ktas']:.0f} KTAS, {b['nm0']:.0f} nm no reserve, {b['nm45']:.0f} nm with 45 min.",
              f"Usable fuel for 1,000 nm: {cdat['fuel_gal_needed_0']:.1f} gal with no reserve, "
              f"{cdat['fuel_gal_needed_45']:.1f} gal with 45 min (standard 76)."]
        n = cdat["mtow_for_1000lb_payload_45"]
        L.append("MTOW for 1,000 lb payload over 1,000 nm with 45 min: " +
                 ("not found within +800 lb" if n is None else
                  f"+{n['dW']} lb ({3150 + n['dW']:,} lb), {n['fuel_gal']:.0f} gal, {n['ktas']:.0f} KTAS"))
        L += ["", "| Item | KTAS | nm, 45 min | Change, nm |", "|---|---|---|---|"]
        for it in cdat["items"]:
            L.append(f"| {it['label']} | {it['ktas']:.0f} | {it['nm45']:,.0f} | {it['nm45'] - b['nm45']:+,.0f} |")
        L.append("")
    L += ["## 5. Sensitivity (drag factor re-calibrated on the six measured points for every row)", "",
          "Headline: continuous power, full fuel at MTOW. AM-low / AM-high.", "",
          "| Input moved | Value | Drag factor | KTAS | nm, 45 min | Change, nm (low / high) | Change if NOT re-calibrated, nm (low) |",
          "|---|---|---|---|---|---|---|"]
    b = o["sensitivity"][0]["res"]
    for s in o["sensitivity"]:
        r = s["res"]
        val = s.get("value", "-")
        if isinstance(val, dict):
            val = ", ".join(f"{a}={v:g}" for a, v in val.items())
        unc = s.get("res_uncal")
        L.append(f"| {s['input']} | {val} | {s['k']:.3f} | {r['AM-low'][0]:.0f} / {r['AM-high'][0]:.0f} | "
                 f"{r['AM-low'][2]:,.0f} / {r['AM-high'][2]:,.0f} | {r['AM-low'][2] - b['AM-low'][2]:+.0f} / {r['AM-high'][2] - b['AM-high'][2]:+.0f} | "
                 f"{'-' if unc is None else format(unc['AM-low'][2] - b['AM-low'][2], '+.0f')} |")
    open(os.path.join(HERE, "tables.md"), "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
    print(open(os.path.join(HERE, "tables.md")).read())
