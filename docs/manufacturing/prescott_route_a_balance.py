"""Prescott build plan, route A (metal wing and tail) on AERO's balance script.

Route A is AERO's balance.py with the carbon wing and tail deltas taken out of
MANUFACTURING's rebuild list; everything else (datum, stations, option B's
radiator split and routed coolant run, the constant-speed propeller) is the
committed script. Prints option B's lead, empty weight and useful load for
both routes at 2,700 lb with 90 gal, on balance.py's headline datum.

Run from the repository root:  python3 docs/manufacturing/prescott_route_a_balance.py
"""
import copy
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shortlist", "check", "prescott"))
import balance as b  # noqa: E402

GROSS = 2700.0


def option_b(label):
    rows = b.solve_options(b.HEADLINE, gross=GROSS, fuel_gal=90.0)
    for end in ("light", "heavy"):
        r = rows[("O2", end)]
        print(f"| {label} | {end} | {r[6]:.1f} | {r[1]:.1f} | {GROSS - r[1]:.1f} | FS {r[3]:.2f} |")


print(f"Datum: {b.HEADLINE}; {GROSS:,.0f} lb, 90 gal; option B (masses forward)\n")
print("| Route | End | Nose lead, lb | Empty, lb | Useful load, lb | Most-aft CG |")
print("|---|---|---|---|---|---|")
option_b("B (carbon wing and tail, as committed)")
mfg = copy.deepcopy(b.MFG)
for end in b.MFG:
    b.MFG[end]["items"] = [i for i in mfg[end]["items"] if "carbon" not in i[0]]
option_b("A (metal wing and tail)")
