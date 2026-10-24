"""How aspect ratio changes wing part sizes, spar depth, root loads and the fit
against home-shop tool envelopes. Input to AERO's planform study (AER-3807).

  python3 planform_parts.py            -> markdown tables
  python3 planform_parts.py --json     -> planform_parts.json

Desk scaling, not a structural design. Every assumption is stated in ASSUME
and in the printed notes. Method:
  span b = sqrt(AR * S); root chord from linear taper: c_r = 2 S / (b (1 + lambda))
  root thickness t_r = (t/c) * c_r; spar cap separation h = 0.85 * t_r (E)
  semi-span lift at ultimate load L = n_ult * W / 2 (wing carries it all; no
  canard share, no inertia relief: both make this conservative)
  spanwise centre of lift by Schrenk's approximation: the mean of the elliptic
  centroid (4/(3 pi)) * b/2 and the planform-area centroid
  (1 + 2 lambda) / (3 (1 + lambda)) * b/2
  root bending moment M = L * y_bar; cap force F = M / h; cap area A = F / sigma
Mold sizes: one-piece wing skin mold length = b + 1 ft of flange; two-piece
panel = b/2 - 2 ft (fuselage half-width) + 1 ft; width = c_r + 1 ft; female
upper-skin mold depth = 0.6 t_r + 3 in (E). Router tiles = panels of the bed
needed to cover the mold footprint; printer tiles = printer footprints needed
to cover it (plug or mold printed in pieces and bonded).
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

ASSUME = {
    "W_lb": 3000,            # 4 seats, ~1,000 lb useful, ~2,000 lb empty (E)
    "S_ft2": 130,            # Defiant 133, Cozy class; low-AR designs often carry more area (see S_delta)
    "S_delta_ft2": 180,      # a delta at the same mission usually needs more area (E)
    "n_ult": 5.7,            # normal category 3.8 limit x 1.5
    "h_over_t": 0.85,        # cap centroid separation / root thickness (E)
    "sigma_cap_psi": 80000,  # pultruded carbon cap, ultimate design compression with knockdowns (E)
    "router_bed_in": [48, 96],
    "router_z_in": [6.0, 12.0],  # budget gantry (~6 in) and the Avid PRO4896 12 in Z option (avidcnc.com, read 2026-10-24); tool stick-out eats some of it
    "printer_xy_in": 31.5,   # 800 mm class large-format FDM
}

# label, AR, taper ratio, root t/c, which area
POINTS = [
    ("High AR 10", 10, 0.5, 0.15, "S_ft2"),
    ("High AR 8", 8, 0.5, 0.15, "S_ft2"),
    ("Moderate AR 6.5", 6.5, 0.45, 0.15, "S_ft2"),
    ("Low AR 4", 4, 0.3, 0.12, "S_ft2"),
    ("Cropped delta AR 3", 3, 0.1, 0.10, "S_delta_ft2"),
    ("Delta AR 2", 2, 0.0, 0.08, "S_delta_ft2"),
]


def point(label, AR, lam, tc, skey, a=ASSUME):
    S = a[skey]
    b = math.sqrt(AR * S)
    cr = 2 * S / (b * (1 + lam))
    ct = lam * cr
    tr_in = tc * cr * 12
    h_in = a["h_over_t"] * tr_in
    L = a["n_ult"] * a["W_lb"] / 2
    y_ell = 4 / (3 * math.pi) * b / 2
    y_area = (1 + 2 * lam) / (3 * (1 + lam)) * b / 2
    y = 0.5 * (y_ell + y_area)
    M = L * y * 12                     # in-lb
    F = M / h_in                       # lb
    A = F / a["sigma_cap_psi"]         # in2
    one_L = (b + 1) * 12
    two_L = (b / 2 - 2 + 1) * 12
    width = (cr + 1) * 12
    depth = 0.6 * tr_in + 3
    bx, by = a["router_bed_in"]

    def tiles(Ln, Wd, tx, ty):
        return math.ceil(Ln / ty) * math.ceil(Wd / tx)
    return {
        "label": label, "AR": AR, "taper": lam, "t_c": tc, "S_ft2": S,
        "span_ft": round(b, 1), "root_chord_ft": round(cr, 2), "tip_chord_ft": round(ct, 2),
        "root_thickness_in": round(tr_in, 1), "spar_depth_in": round(h_in, 1),
        "root_moment_kin_lb": round(M / 1000), "cap_force_klb": round(F / 1000, 1),
        "cap_area_in2": round(A, 2),
        "mold_one_piece_ft": round(one_L / 12, 1), "mold_two_piece_ft": round(two_L / 12, 1),
        "mold_width_ft": round(width / 12, 1), "mold_depth_in": round(depth, 1),
        "router_tiles_two_piece": tiles(two_L, width, bx, by),
        "fits_z_6": depth <= a["router_z_in"][0],
        "fits_z_12": depth <= a["router_z_in"][1],
        "printer_tiles_two_piece": tiles(two_L, width, a["printer_xy_in"], a["printer_xy_in"]),
    }


def main():
    rows = [point(*p) for p in POINTS]
    if "--json" in sys.argv:
        json.dump({"assume": ASSUME, "points": rows}, open(os.path.join(HERE, "planform_parts.json"), "w"), indent=1)
        return
    print("| Point | AR | Area, ft2 | Span, ft | Root chord, ft | Root depth, in | Spar depth, in | "
          "Root moment (ult), 1,000 in-lb | Cap force (ult), 1,000 lb | Carbon cap area, in2 |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['label']} | {r['AR']} | {r['S_ft2']} | {r['span_ft']} | {r['root_chord_ft']} | "
              f"{r['root_thickness_in']} | {r['spar_depth_in']} | {r['root_moment_kin_lb']:,} | "
              f"{r['cap_force_klb']} | {r['cap_area_in2']} |")
    print()
    print("| Point | Skin mold, one-piece wing, ft | Skin mold, two-piece panel, ft | Mold width, ft | "
          "Female mold depth, in | 4x8 router tiles per panel mold | Within 6 in Z? | Within 12 in Z? | 800 mm printer tiles per panel mold |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['label']} | {r['mold_one_piece_ft']} | {r['mold_two_piece_ft']} | {r['mold_width_ft']} | "
              f"{r['mold_depth_in']} | {r['router_tiles_two_piece']} | {'yes' if r['fits_z_6'] else 'no'} | {'yes' if r['fits_z_12'] else 'no'} | "
              f"{r['printer_tiles_two_piece']} |")


if __name__ == "__main__":
    main()
