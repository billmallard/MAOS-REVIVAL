"""Tables for docs/studies/planform.md from results/sweep_V.json and
results/sweep_S.json. Adds the storage, folding and home-shop columns, which
are geometry only (no aerodynamics).

  python3 report.py > results/tables.md
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# Envelopes (sources in the study's "Storage" and "Home shop" sections)
T_DOOR_W, T_DOOR_H_SMALL, T_DOOR_H_STD, T_DEPTH = 40.0, 9 + 5 / 12, 12.0, 30.0  # Hayward small/standard T
CLEAR = 1.0                     # ft each side at the door (E, ours)
TRAILER_W = 8.5                 # 102 in, 23 CFR 658.15
# Home-tier envelope as confirmed by MANUFACTURING (AER-3784, PR #5,
# docs/manufacturing/planform_parts.py; prices read 2026-10-24)
ROUTER = (98.75 / 12, 49.5 / 12)  # Avid PRO4896 work area, ft
ROUTER_Z = 12.0                 # in, the PRO4896's 12 in Z option
PRINT_TILE = 800 / 304.8        # Elegoo OrangeStorm Giga, 800 x 800 x 1,000 mm, ft
MILL = (23.0, 21.0, 6.1)        # Langmuir MR-1 travels, in
GARAGE = 24.0                   # ft, two-car garage, square (E, ours)
WORK_ROOM = 2.0                 # ft each side for layup, bagging, infusion (MANUFACTURING, E)


def tiles(L, W, tile):
    a, b = tile
    return min(math.ceil(L / a) * math.ceil(W / b), math.ceil(L / b) * math.ceil(W / a))


def shop(r):
    semi = r["b"] / 2
    # half-wing skin plug: bounding box in plan view (semi-span x root chord)
    L, W = max(semi, r["cr"]), min(semi, r["cr"])
    router = tiles(L, W, ROUTER)
    printer = math.ceil(L / PRINT_TILE) * math.ceil(W / PRINT_TILE)
    fits_garage = L <= GARAGE - 2 * WORK_ROOM
    # female skin mold depth ~0.6 x root thickness + 3 in (MANUFACTURING, E)
    depth = 0.6 * r["h_spar_in"] / 0.95 + 3.0
    return {"semi": semi, "plug_L": L, "plug_W": W, "router_tiles": router,
            "print_tiles": printer, "garage": fits_garage, "mold_depth": depth,
            "z_ok": depth <= ROUTER_Z}


def storage(r):
    span_ok = r["b"] + 2 * CLEAR <= T_DOOR_W
    h = r["height"]
    # trailer: fold outboard of a centre section TRAILER_W wide
    panel = max(0.0, (r["b"] - TRAILER_W) / 2)
    if r["tail"] == "conv":
        fold = f"fold aft {panel:.1f} ft panels alongside fuselage"
    else:
        fold = f"fold up {panel:.1f} ft panels; fin folds too"
    return {"span_ok": span_ok, "h_small": h <= T_DOOR_H_SMALL, "h_std": h <= T_DOOR_H_STD,
            "panel": panel, "fold": fold, "len_ok": r["length"] <= T_DEPTH,
            "footprint": r["b"] * r["length"]}


def yn(b):
    return "yes" if b else "no"


def tables(d, title):
    P = d["points"]
    ids = [r["id"] for r in P]
    out = [f"### {title}\n"]

    def row(name, f):
        out.append(f"| {name} | " + " | ".join(f(r) for r in P) + " |")

    out.append("| | " + " | ".join(ids) + " |")
    out.append("|---|" + "---|" * len(P))
    row("Planform", lambda r: r["label"])
    row("Aspect ratio", lambda r: f"{r['AR']:.1f}")
    row("Wing area, ft2", lambda r: f"{r['S']:.0f}")
    row("Span, ft", lambda r: f"{r['b']:.1f}")
    row("Root / tip chord, ft", lambda r: f"{r['cr']:.1f} / {r['ct']:.1f}")
    row("LE sweep, deg", lambda r: f"{r['sweep_le']:.0f}")
    row("Tail", lambda r: "H + V tail" if r["tail"] == "conv" else "fin only (tailless)")
    row("Gross weight, lb", lambda r: f"{r['W0']:.0f}")
    row("Empty weight, lb", lambda r: f"{r['empty']:.0f}")
    row("Wing + tail weight, lb", lambda r: f"{r['W_wing']:.0f} + {r['W_tail']:.0f}")
    row("Wing loading, psf", lambda r: f"{r['WS']:.1f}")
    row("Wetted area total, ft2", lambda r: f"{r['wet_total']:.0f}")
    row("of which wing, ft2", lambda r: f"{r['wet']['Wing']:.0f}")
    row("AVL e_inv (inviscid)", lambda r: f"{r['e_inv']:.3f}")
    row("AVL CL_alpha, /rad (inviscid)", lambda r: f"{r['CLa']:.2f}")
    out.append("")
    out.append("**1. Performance**\n")
    out.append("| | " + " | ".join(ids) + " |")
    out.append("|---|" + "---|" * len(P))
    row("CD0 (calibrated)", lambda r: f"{r['CD0']:.4f}")
    row("Parasite D/q, ft2", lambda r: f"{r['Dq_par']:.2f}")
    row("Cruise KTAS, 12,000 ft, 195 hp", lambda r: f"{r['Vc']:.0f}")
    row("Induced share: climb (SL, Vy)", lambda r: f"{r['ind_share_climb']*100:.0f}%")
    row("Induced share: cruise", lambda r: f"{r['ind_share_cruise']*100:.0f}%")
    row("Induced share: 45 min reserve (min power)", lambda r: f"{r['ind_share_res']*100:.0f}%")
    row("Reserve leg: KEAS / gph", lambda r: f"{r['res_keas']} / {r['res_gph']:.1f}")
    row("Best L/D (KEAS)", lambda r: f"{r['LDmax']:.1f} ({r['V_LDmax']})")
    row("Rate of climb SL, 260 hp, fpm", lambda r: f"{r['roc_sl']:.0f}")
    row("Rate of climb 12,000 ft, 195 hp, fpm", lambda r: f"{r['roc_cr']:.0f}")
    row("Service ceiling, ft (100 fpm)", lambda r: f"{r['ceiling']:,.0f}")
    row("Range at 195 hp, no reserve, nm", lambda r: f"{r['range0']:.0f}")
    row("Range at 195 hp, 45 min reserve, nm", lambda r: f"{r['range45']:.0f}")
    row("Range at best-range speed, no reserve, nm (KTAS)",
        lambda r: f"{r['range_lr']:.0f} ({r['v_lr']:.0f})")
    out.append("")
    out.append("**2. Storage** (door: small T-hangar 40 ft x 9 ft 5 in, standard 40 ft x 12 ft; 1 ft clearance each side)\n")
    out.append("| | " + " | ".join(ids) + " |")
    out.append("|---|" + "---|" * len(P))
    st = [storage(r) for r in P]
    sh = [shop(r) for r in P]

    def srow(name, f, src):
        out.append(f"| {name} | " + " | ".join(f(x, r) for x, r in zip(src, P)) + " |")

    srow("Span through a 40 ft door", lambda s, r: f"{yn(s['span_ok'])} ({r['b']:.0f} ft)", st)
    srow("Height, ft (E)", lambda s, r: f"{r['height']:.1f}", st)
    srow("Under 9 ft 5 in / 12 ft door", lambda s, r: f"{yn(s['h_small'])} / {yn(s['h_std'])}", st)
    srow("Length, ft", lambda s, r: f"{r['length']:.0f}", st)
    srow("Plan footprint (span x length), ft2", lambda s, r: f"{s['footprint']:.0f}", st)
    srow("Trailer (8.5 ft wide): fold", lambda s, r: s["fold"], st)
    out.append("")
    out.append("**3. Home-shop build**\n")
    out.append("| | " + " | ".join(ids) + " |")
    out.append("|---|" + "---|" * len(P))
    srow("Half-wing plug bounding box, ft", lambda s, r: f"{s['plug_L']:.1f} x {s['plug_W']:.1f}", sh)
    srow("4x8 router sheets per plug face (Avid PRO4896)", lambda s, r: f"{s['router_tiles']}", sh)
    srow("800 mm printer tiles per plug face (OrangeStorm Giga)", lambda s, r: f"{s['print_tiles']}", sh)
    srow("Female mold depth, in / fits 12 in router Z", lambda s, r: f"{s['mold_depth']:.0f} / {yn(s['z_ok'])}", sh)
    srow("Half-wing mold fits a 24 ft garage with 2 ft working room", lambda s, r: yn(s["garage"]), sh)
    srow("Root spar depth, in", lambda s, r: f"{r['h_spar_in']:.1f}", sh)
    srow("Root bending, ultimate, ft-lb", lambda s, r: f"{r['M_root']:,.0f}", sh)
    srow("Spar cap force, ultimate, lb", lambda s, r: f"{r['F_cap']:,.0f}", sh)
    out.append("")
    out.append("**4. Safety**\n")
    out.append("| | " + " | ".join(ids) + " |")
    out.append("|---|" + "---|" * len(P))
    row("Landing CL usable (attitude 14 deg, in ground effect)", lambda r: f"{r['CLu']:.2f}")
    row("Limited by", lambda r: "CLmax" if r["CLu"] >= r["CLmax"] - 1e-6 else "attitude")
    row("Touchdown speed at gross, kt", lambda r: f"{r['V_td']:.0f}")
    row("same, with full Polhamus vortex lift, kt", lambda r: f"{r['V_td_vortex']:.0f}")
    row("Alpha for CLmax out of ground effect, deg", lambda r: f"{r['alpha_stall_free']:.0f}")
    row("Power-off approach at 1.3 V_td: L/D", lambda r: f"{r['LD_app']:.1f}")
    row("Power-off approach sink, fpm", lambda r: f"{r['sink_app']:.0f}")
    row("Engine-out glide ratio, prop stopped (KEAS)", lambda r: f"{r['LD_glide']:.1f} ({r['V_glide']})")
    out.append("")
    out.append("**5. Ride** (Pratt, 150 KEAS at 12,000 ft, mid-cruise weight)\n")
    out.append("| | " + " | ".join(ids) + " |")
    out.append("|---|" + "---|" * len(P))
    row("Wing loading, psf", lambda r: f"{r['WS']:.1f}")
    row("CL_alpha, /rad", lambda r: f"{r['CLa']:.2f}")
    row("Mass ratio mu_g / alleviation K_g", lambda r: f"{r['mu_g']:.1f} / {r['Kg']:.2f}")
    row("Delta n, 50 ft/s design gust", lambda r: f"{r['dn_gust']:.2f}")
    row("Delta n per 10 ft/s (ride)", lambda r: f"{r['dn_per_10fps']:.2f}")
    row("Sharp-edged, no alleviation, 50 ft/s", lambda r: f"{r['dn_sharp']:.2f}")
    return "\n".join(out)


def calib_table():
    rows = json.load(open(os.path.join(HERE, "results", "calib.json")))
    out = ["| Design | AR | Span, ft | Area, sq ft | Gross, lb | W/S, psf | CL_alpha, /rad (AVL) "
           "| mu_g / K_g | Delta n, 50 ft/s | Delta n per 10 ft/s | Basis |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        out.append(f"| {r['label']} | {r['AR']:.2f} | {r['b']:.1f} | {r['S']:.0f} | {r['W']:,} "
                   f"| {r['WS']:.1f} | {r['CLa']:.2f} | {r['mu']:.1f} / {r['Kg']:.2f} "
                   f"| {r['dn']:.2f} | {r['dn'] / 5:.2f} | {r['note']} |")
    out.append("| Rohr 2-175 | not determinable (area not found) | 20 (de Piolenc) or 30 (aerofiles) "
               "| not found | 1,450 | - | - | - | - | - | see below |")
    return "\n".join(out)


def closed_table():
    """The closed-wing point against three sweep points, rule A."""
    cw = json.load(open(os.path.join(HERE, "results", "joined_V.json")))
    sw = {r["id"]: r for r in json.load(open(os.path.join(HERE, "results", "sweep_V.json")))["points"]}
    cols = [("CW (closed wing)", cw), ("AR10", sw["AR10"]), ("AR6.5", sw["AR6.5"]), ("D3", sw["D3"])]
    out = ["| Rule A, same touchdown speed | " + " | ".join(c for c, _ in cols) + " |",
           "|---|" + "---|" * len(cols)]

    def row(name, f):
        out.append(f"| {name} | " + " | ".join(f(r) for _, r in cols) + " |")

    def cap(r):
        return r.get("F_cap", r.get("F_cap_front"))
    row("AR on total area / span efficiency e_inv (AVL)", lambda r: f"{r['AR']:.1f} / {r['e_inv']:.3f}")
    row("Wing area, ft2 / span, ft", lambda r: f"{r['S']:.0f} / {r['b']:.1f}")
    row("Gross weight, lb / wing loading, psf", lambda r: f"{r['W0']:.0f} / {r['WS']:.1f}")
    row("Wing + tail (or tip-fin) weight, lb", lambda r: f"{r['W_wing']:.0f} + {r['W_tail']:.0f}")
    row("Wetted area, ft2", lambda r: f"{r['wet_total']:.0f}")
    row("Cruise KTAS, 12,000 ft, 195 hp", lambda r: f"{r['Vc']:.0f}")
    row("Induced share: climb / cruise / reserve",
        lambda r: f"{r['ind_share_climb']*100:.0f}% / {r['ind_share_cruise']*100:.0f}% / {r['ind_share_res']*100:.0f}%")
    row("Best L/D (KEAS)", lambda r: f"{r['LDmax']:.1f} ({r['V_LDmax']})")
    row("Climb SL / 12,000 ft, fpm", lambda r: f"{r['roc_sl']:.0f} / {r['roc_cr']:.0f}")
    row("Service ceiling, ft", lambda r: f"{r['ceiling']:,.0f}")
    row("Range 195 hp, 0 / 45 min reserve, nm", lambda r: f"{r['range0']:.0f} / {r['range45']:.0f}")
    row("Best-range distance, nm", lambda r: f"{r['range_lr']:.0f}")
    row("Height, ft (E)", lambda r: f"{r['height']:.1f}")
    row("Trailer fold panel length, ft",
        lambda r: f"{r.get('panel_fold', max(0.0, (r['b'] - 8.5) / 2)):.1f}")
    row("Root spar depth, in", lambda r: f"{r['h_spar_in']:.1f}")
    row("Spar-cap force, ultimate, lb", lambda r: f"{cap(r):,.0f}" + (" per wing, cantilever bound" if "F_cap_front" in r else ""))
    row("Power-off approach sink, fpm", lambda r: f"{r['sink_app']:.0f}")
    row("Engine-out glide, prop stopped", lambda r: f"{r['LD_glide']:.1f}")
    row("Delta n per 10 ft/s (Pratt)", lambda r: f"{r['dn_per_10fps']:.2f}")
    return "\n".join(out)


def box_table():
    d = json.load(open(os.path.join(HERE, "results", "boxcheck.json")))
    gaps = ["0.05", "0.10", "0.15", "0.20", "0.25"]
    out = ["| Gap / span | " + " | ".join(gaps) + " |", "|---|" + "---|" * len(gaps)]
    for kind, lab in (("biplane", "Open biplane"), ("box", "Prandtl box (tip panels)"),
                      ("joined", "Joined wing, no vertical gap at the tips")):
        out.append(f"| {lab} | " + " | ".join(f"{d[f'{kind} {g}']:.3f}" for g in gaps) + " |")
    return "\n".join(out)


def cdf_table():
    """Drag-factor sensitivity: measured pushers need 1.35-1.72 (AER-3783)."""
    a = {r["id"]: r for r in json.load(open(os.path.join(HERE, "results", "sweep_V.json")))["points"]}
    b = {r["id"]: r for r in json.load(open(os.path.join(HERE, "results", "sweep_V_cdf150.json")))["points"]}
    ja = json.load(open(os.path.join(HERE, "results", "joined_V.json")))
    jb = json.load(open(os.path.join(HERE, "results", "joined_V_cdf150.json")))
    ids = list(a) + ["CW"]
    a["CW"], b["CW"] = ja, jb
    out = ["| Rule A | " + " | ".join(ids) + " |", "|---|" + "---|" * len(ids)]
    out.append("| Cruise KTAS, x1.29 / x1.5 | " + " | ".join(f"{a[i]['Vc']:.0f} / {b[i]['Vc']:.0f}" for i in ids) + " |")
    out.append("| Best L/D, x1.29 / x1.5 | " + " | ".join(f"{a[i]['LDmax']:.1f} / {b[i]['LDmax']:.1f}" for i in ids) + " |")
    out.append("| Range 195 hp no reserve, nm, x1.29 / x1.5 | " + " | ".join(f"{a[i]['range0']:.0f} / {b[i]['range0']:.0f}" for i in ids) + " |")
    out.append("| Best-range distance, nm, x1.29 / x1.5 | " + " | ".join(f"{a[i]['range_lr']:.0f} / {b[i]['range_lr']:.0f}" for i in ids) + " |")
    return "\n".join(out)


def all_tables():
    parts = []
    for rule, title in (("V", "Sizing rule A: same touchdown speed (61 kt at gross)"),
                        ("S", "Sizing rule B: same wing area (150 ft2)")):
        d = json.load(open(os.path.join(HERE, "results", f"sweep_{rule}.json")))
        parts.append(tables(d, title))
    return "\n\n".join(parts)


if __name__ == "__main__":
    import sys
    if "--doc" in sys.argv:
        t = open(os.path.join(HERE, "planform.template.md")).read()
        t = t.replace("{{TABLES}}", all_tables()).replace("{{CALIB}}", calib_table())
        t = t.replace("{{CLOSED}}", closed_table()).replace("{{BOX}}", box_table())
        t = t.replace("{{CDF}}", cdf_table())
        open(os.path.join(HERE, "..", "planform.md"), "w").write(t)
        open(os.path.join(HERE, "results", "tables.md"), "w").write(all_tables() + "\n")
    else:
        print(all_tables())
