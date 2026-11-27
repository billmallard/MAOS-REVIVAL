"""Cooling-drag band for the AM20T on the Aries and the Prescott (AER-6292).

  python3 cooling_band.py > cooling_band_output.md

Why. Aeromomentum publishes the AM20T as liquid-cooled ("Cooling: Liquid",
https://aeromomentum.com/am20t-230hp-300hp/, read 2026-11-27; Wayback
https://web.archive.org/web/20261127165349/https://aeromomentum.com/am20t-230hp-300hp/).
The stage 3 check carries the cooling drag of every AM20T installation by
Raymer's piston formula (Aircraft Design eq. 12.39), which is an air-cooled
correlation, times the original airframe's cooling factor (Aries 1.0,
Prescott 1.2). This replaces that one term with a radiator and an
intercooler sized for the heat the AM20T rejects in turbocharged cruise at
altitude, and reports what moves. Everything else is the stage 3 check's,
unchanged, including the drag factor k on the build-up.

Method (perf.liquid_cooling_Dq). Heat to reject:
  coolant  = coolant_frac x shaft power (oil heat included, through an
             oil-to-coolant exchanger);
  charge   = engine airflow x cp x eps_ic x (T2 - T_amb), where T2 is the
             compressor outlet temperature at the pressure ratio needed to
             hold the manifold pressure at that altitude.
Cooling air = each heat / (cp x eps_air x (hot-side temperature - T_amb)).
Drag = m_air x V x (1 - Ve/V), Ve/V = sqrt(1 - zeta), where zeta is the duct's
internal total-pressure loss in freestream dynamic pressures. That is the
momentum loss of the cooling air through the duct, standard internal-flow
bookkeeping; no reference is quoted for it here. No heat-addition thrust is
credited, so the Meredith effect is not counted; at 180-200 KTAS it is small. The liquid term replaces the Raymer term
inside the build-up, so the drag factor k multiplies it as it multiplied the
air-cooled term.

Band ends, all OUR assumptions (E), none published by Aeromomentum:
  low  (a good ducted installation): coolant 0.7 x shaft power, zeta 0.35
       (core face at about 0.2 of flight speed, exit at 0.81 of it);
  high (a poor one): coolant 1.0 x shaft power, zeta 0.90 (core face at
       about 0.3 of flight speed, exit at 0.32 of it).
Common to both: coolant 373 K (100 C) at the radiator, cooling air rising
0.5 of the inlet temperature difference, air-fuel ratio 12.5, BSFC 0.45,
1.5 atm manifold at 195 hp (proportional to power), 0.97 inlet recovery,
compressor efficiency 0.70, intercooler effectiveness 0.75. The coolant
fraction is of the order of the textbook spark-ignition energy balance, where
coolant heat is comparable to brake power; the figures are ours, not quoted.

Readings. Drag held at the stage 3 factor (the published speeds that set k
were flown on the original air-cooled engines, so there is nothing to
re-match against). Propeller efficiency at the stage 3 formula, and, for the
Prescott range margin, also at 0.75, the low end of the AER-5717 band, so the
worst case of both bands is shown together. Last, the largest duct loss zeta
at which the Prescott re-derivation's worst case still flies 1,000 nm: the
requirement a radiator duct design has to meet.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import perf  # noqa: E402
from eta_band import designs, am_rows, fmt_cell, with_eta, CASES, KT  # noqa: E402
from payload_range import SPEED_FLOOR  # noqa: E402
from run_check import AM20T  # noqa: E402

COMMON = {"coolant_K": 373.0, "eps_air": 0.5, "afr": 12.5, "bsfc": 0.45,
          "map_atm": 1.5, "P_ref_hp": 195.0, "inlet_recovery": 0.97,
          "eta_comp": 0.70, "eps_ic": 0.75}
BAND = (("stage 3 (Raymer, air-cooled)", None),
        ("liquid, low", dict(COMMON, coolant_frac=0.7, zeta=0.35)),
        ("liquid, high", dict(COMMON, coolant_frac=1.0, zeta=0.90)))


def with_cooling(m, c):
    m = json.loads(json.dumps(m))
    if c is not None:
        m["cooling_liquid"] = c
    return m


def sizing_table(m, wet):
    """Cooling term and radiator sizing at the continuous cruise point of
    each engine case, on the Aries model (the heat does not depend on the
    airframe; the drag in lb does, a little, through speed)."""
    P = print
    P("## The cooling term at continuous cruise (Aries model)\n")
    P("Heat and air are the engine's, whatever the airframe. Core face area is the cooling air over "
      "its density at 0.2 and 0.3 of flight speed, a sanity check that the duct fits a nose.\n")
    P("| Engine case | Cooling | KTAS | Coolant heat, kW | Charge-air heat, kW | Compressor PR | Cooling air, kg/s "
      "| Cooling D/q, ft2 | Cooling drag, lb | Share of total drag | Core face at 0.2 / 0.3 V, ft2 |")
    P("|---|---|---|---|---|---|---|---|---|---|---|")
    for case, h in CASES:
        eng = dict(AM20T, crit_alt_ft=h)
        Pw = perf.power_avail(eng, h, eng["cont_hp"] / eng["hp"])
        for name, c in BAND:
            mm = with_cooling(m, c)
            sp = perf.solve_speed(mm, wet, eng, 0.92 * 3150.0, h, Pw)
            cool = [d for n, d, _ in sp["items"] if n == "cooling"][0]
            rho, _, _, _ = perf.atmos(h)
            q = 0.5 * rho * sp["V_fts"] ** 2
            share = cool * q * m["drag_factor"] / sp["D_lb"]
            if c is None:
                P(f"| {case} ({h:,.0f} ft) | {name} | {sp['ktas']:.0f} | - | - | - | - | {cool:.3f} "
                  f"| {cool * q:.1f} (x k {m['drag_factor']:.2f} = {cool * q * m['drag_factor']:.1f}) "
                  f"| {share * 100:.1f}% | - |")
                continue
            ht = perf.liquid_cooling_heat(c, h, Pw)
            rho_si = rho * 515.379
            V_si = sp["V_fts"] * 0.3048
            a2, a3 = (ht["m_air"] / (rho_si * f * V_si) * 10.7639 for f in (0.2, 0.3))
            P(f"| {case} ({h:,.0f} ft) | {name} | {sp['ktas']:.0f} | {ht['q_cool'] / 1000:.0f} "
              f"| {ht['q_ic'] / 1000:.0f} | {ht['pr']:.2f} | {ht['m_air']:.2f} | {cool:.3f} "
              f"| {cool * q:.1f} (x k {m['drag_factor']:.2f} = {cool * q * m['drag_factor']:.1f}) "
              f"| {share * 100:.1f}% | {a2:.2f} / {a3:.2f} |")
    P("")


def band_rows():
    out = []
    for key, label, m, wet, gross, empty, fuel_lb, _, _ in designs():
        for eta in ((None, 0.75) if key.startswith("prescott-2700") else (None,)):
            for name, c in BAND:
                mm = with_eta(with_cooling(m, c), eta)
                out.append((key, label, eta, name, am_rows(mm, wet, gross, empty, fuel_lb)))
    return out


def print_band(rows):
    P = print
    P("## Speed, payload and range on the AM20T, cooling band\n")
    P("Each cell spans the two engine cases (critical altitude 8,000 and 16,000 ft, cruising there). "
      "Payload is lb carried 1,000 nm, **no reserve / 45 min reserve**, still air; \"cannot\" means not "
      "even an empty cabin reaches 1,000 nm on full tanks. Range is on full tanks from gross, no reserve. "
      "Drag factor held at the stage 3 value.\n")
    P("| Design | eta | Cooling | Continuous: KTAS | Continuous: payload at 1,000 nm | Continuous: range, nm "
      "| Economy 65%: KTAS | Economy: payload at 1,000 nm | Economy: range, nm |")
    P("|---|---|---|---|---|---|---|---|---|")
    for key, label, eta, name, am in rows:
        c, e = am["continuous"], am["economy 65%"]
        kt_e = fmt_cell(e, "ktas") + (" (under the floor)" if min(x["ktas"] for x in e) <= SPEED_FLOOR else "")
        kt_c = fmt_cell(c, "ktas") + (" (under the floor)" if min(x["ktas"] for x in c) <= SPEED_FLOOR else "")
        el = "stage 3 formula" if eta is None else f"{eta:.2f} fixed"
        P(f"| {label} | {el} | {name} | {kt_c} | {fmt_cell(c, 'p0')} / {fmt_cell(c, 'p45')} "
          f"| {fmt_cell(c, 'rng')} | {kt_e} | {fmt_cell(e, 'p0')} / {fmt_cell(e, 'p45')} | {fmt_cell(e, 'rng')} |")
    P("")


def print_margin(rows):
    """The Prescott re-derivation's worst full-tank range at continuous power,
    over both drag bases, both engine cases and both structure ends."""
    P = print
    P("## Prescott re-derivation: range margin at continuous power\n")
    P("Worst and best full-tank range from gross, no reserve, over both drag bases, both engine cases "
      "and both structure ends (range on full tanks does not depend on the empty weight). "
      "Margin is against the 1,000 nm target.\n")
    P("| eta | Cooling | Range, nm (worst-best) | Margin at the worst case |")
    P("|---|---|---|---|")
    groups = {}
    for key, _, eta, name, am in rows:
        if key.startswith("prescott-2700"):
            groups.setdefault((eta, name), []).extend(x["rng"] for x in am["continuous"])
    for (eta, name), rs in groups.items():
        lo, hi = min(rs), max(rs)
        mg = lo - 1000.0
        verdict = f"+{mg:,.0f} nm ({mg / 10:.1f}%)" if mg >= 0 else f"**{mg:,.0f} nm ({mg / 10:.1f}%): fails**"
        el = "stage 3 formula" if eta is None else f"{eta:.2f} fixed"
        P(f"| {el} | {name} | {lo:,.0f}-{hi:,.0f} | {verdict} |")
    P("")


def worst_range(m, wet, gross, fuel_lb, c, eta):
    """Lowest full-tank range at continuous power over the two engine cases."""
    am = am_rows(with_eta(with_cooling(m, c), eta), wet, gross, 0.0, fuel_lb)
    return min(x["rng"] for x in am["continuous"])


def print_breakeven():
    """The duct loss zeta at which the Prescott re-derivation's worst case
    (measured drag basis) just flies 1,000 nm on full tanks, per coolant
    fraction and eta."""
    P = print
    P("## Prescott re-derivation: the duct loss that still holds 1,000 nm\n")
    P("The largest zeta at which the worst case (measured drag basis, k 1.55, the worse engine case) still "
      "flies 1,000 nm on full tanks from gross, no reserve, at continuous power. Ve/V is the duct exit "
      "velocity ratio that zeta implies. A duct must do at least this well for the range target to hold.\n")
    P("| eta | Coolant heat, x shaft power | Largest zeta | Ve/V at that zeta |")
    P("|---|---|---|---|")
    key = [d for d in designs() if d[0] == "prescott-2700-light-1.55"][0]
    _, _, m, wet, gross, _, fuel_lb, _, _ = key
    for eta in (None, 0.75):
        for frac in (0.7, 1.0):
            def f(z):
                return worst_range(m, wet, gross, fuel_lb, dict(COMMON, coolant_frac=frac, zeta=z), eta)
            lo, hi = 0.05, 0.99
            if f(hi) >= 1000.0:
                P(f"| {'stage 3 formula' if eta is None else f'{eta:.2f} fixed'} | {frac:.1f} | above 0.99 | - |")
                continue
            if f(lo) < 1000.0:
                P(f"| {'stage 3 formula' if eta is None else f'{eta:.2f} fixed'} | {frac:.1f} | none (below 0.05) | - |")
                continue
            for _ in range(12):
                mid = 0.5 * (lo + hi)
                lo, hi = (mid, hi) if f(mid) >= 1000.0 else (lo, mid)
            P(f"| {'stage 3 formula' if eta is None else f'{eta:.2f} fixed'} | {frac:.1f} | {lo:.2f} "
              f"| {(1 - lo) ** 0.5:.2f} |")
    P("")


def main():
    P = print
    P("# Cooling-drag band for the liquid-cooled AM20T, Aries and Prescott (AER-6292)\n")
    P("Generated by `cooling_band.py`; method, sources and every assumption in its docstring. Every number "
      "is ours (E). Engine assumptions as in the stage 3 check: AM20T 195 hp continuous, BSFC 0.45, "
      "critical altitude 8,000 or 16,000 ft, none published by Aeromomentum. Aeromomentum does publish "
      "the cooling: liquid (read 2026-11-27).\n")
    r = json.load(open(os.path.join(HERE, "results", "bellanca-t250-aries.json")))
    m = json.load(open(os.path.join(HERE, "models", "bellanca-t250-aries.json")))
    m["drag_factor"] = r["drag_factor"]
    sizing_table(m, r["wet"])
    rows = band_rows()
    print_band(rows)
    print_margin(rows)
    print_breakeven()


if __name__ == "__main__":
    main()
