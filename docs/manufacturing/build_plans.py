#!/usr/bin/env python3
"""Build plans for the two picks: Bellanca T-250 Aries and Prescott Pusher (AER-3868).

Part counts, the make/buy split, the tooling bill and the kit-run crossover.
Every number here is our estimate (E) unless a source is named in SOURCES.
Counts exclude standard hardware (rivets, bolts, nuts, washers, clamps): a
bought assembly (a gear leg, a fuel pump, the engine) counts as one part.

Usage:
    python3 build_plans.py          # prints the tables used in the two build-plan files
    python3 build_plans.py --json   # also writes build_plans.json
"""
import json
import math
import sys

# ---------------------------------------------------------------------------
# Routes. "make" says who makes the part:
#   cut     flat part cut from a file (laser/waterjet/router service, or home router)
#   form    cut, then formed on a block, brake or roll (service or builder)
#   mach    machined fitting (CNC service, or benchtop mill)
#   tube    4130 tube cut and notched from a file (tube-laser service), welded in a jig
#   mold    composite part from a mold
#   buy     bought assembly or catalog part
# Each assembly: (name, make-split {make: (lo, hi) parts}, unique (lo, hi), note)
# ---------------------------------------------------------------------------

ARIES = {
    "name": "Bellanca T-250 Aries",
    "route": "matched-hole aluminium kit; flat and single-curve skins kept; AM20T; 90 gal",
    "assemblies": [
        ("Wing structure, both halves (spars, ribs, skins, stringers, tank bay, gear bay)",
         {"cut": (130, 170), "form": (110, 140), "mach": (12, 20), "buy": (6, 10)}, (55, 80),
         "16 rib stations x 3 rib pieces x 2 wings = 96 ribs from 3 standard shapes plus 10-15 "
         "specials (root, tank ends, gear bay, hinge ribs). Skins are left and right handed"),
        ("Flaps and ailerons (4 surfaces)",
         {"cut": (25, 35), "form": (40, 50), "mach": (4, 8), "buy": (1, 2)}, (25, 35),
         "constant chord: ribs repeat along each surface"),
        ("T-tail: stabilator, fin, rudder, anti-servo tab",
         {"cut": (40, 55), "form": (40, 60), "mach": (8, 12), "buy": (2, 3)}, (60, 90),
         "tail surfaces assumed tapered, so most ribs are unique (no tail drawing found)"),
        ("Fuselage (frames, longerons, stringers, skins, floor, carry-through, doors)",
         {"cut": (120, 165), "form": (100, 140), "mach": (15, 25), "buy": (15, 20)}, (150, 220),
         "slab-sided, flat and single-curve skins (Plane & Pilot); nearly every part unique"),
        ("Landing gear and doors (retractable tricycle)",
         {"cut": (12, 18), "form": (10, 15), "mach": (8, 12), "buy": (10, 15)}, (25, 35),
         "legs, actuators, wheels and brakes bought or service-made"),
        ("Flight controls (yoke, pushrods, bellcranks, cables, trim)",
         {"cut": (15, 20), "form": (10, 15), "mach": (20, 30), "buy": (15, 25)}, (40, 60), ""),
        ("Fuel system, 90 gal integral",
         {"cut": (8, 12), "form": (4, 8), "mach": (2, 4), "buy": (11, 16)}, (15, 25),
         "pumps, selector, senders, filters bought; tank sealing is builder work"),
        ("Firewall forward, AM20T (mount, radiator, duct, exhaust, ECU backup)",
         {"cut": (8, 12), "form": (4, 8), "mach": (3, 6), "mold": (3, 5), "buy": (12, 19)}, (25, 40),
         "welded mount bought or from a shop"),
        ("Composite fairings (cowl, tips, fin cap, fillets, gear-door fairings)",
         {"mold": (12, 18)}, (10, 14), ""),
        ("Cabin, windows, panel, seats, interior",
         {"cut": (10, 20), "form": (5, 10), "mold": (0, 4), "buy": (25, 36)}, (30, 50),
         "windows and windshield are bought formed acrylic"),
        ("Electrical and avionics", {"buy": (25, 40)}, (25, 40), "counted as bought boxes"),
    ],
}

PRESCOTT_COMMON = [
    ("Fuselage cage, 4130 square tube (tubes, gussets, tabs, fittings)",
     {"tube": (90, 140), "cut": (60, 100), "mach": (15, 25)}, (90, 150),
     "SA86: 3/4 x .035 to 1-1/4 x .065 square tube, CAD-cut to length and angle, TIG-welded in a jig"),
    ("Shells and doors, non-structural (shell halves, nose cone, belly pan, scoops, closeouts, "
     "access and cabin doors, gear doors)",
     {"mold": (14, 20), "buy": (2, 4)}, (14, 22),
     "SDASM drawings 11005-11106 and 11400-11407 list these parts"),
    ("Shell bulkheads and attach clips",
     {"cut": (50, 85), "form": (18, 27)}, (20, 35), "SDASM drawing 11108: attach clips, frame, shell"),
    ("Landing gear (retractable; fibreglass mains, bought nose gear)",
     {"cut": (10, 15), "form": (5, 10), "mach": (20, 30), "buy": (15, 25)}, (35, 50),
     "about 35 gear drawings in SDASM SC.10269; Airite nose gear was bought (SA86)"),
    ("Flight controls (column, cables, pulleys, bellcranks, bob weight)",
     {"cut": (25, 35), "form": (10, 15), "mach": (20, 30), "buy": (15, 20)}, (50, 70),
     "about 45 control-system drawings in SC.10269"),
    ("Fuel system, 90 gal",
     {"cut": (6, 10), "form": (4, 8), "mach": (2, 4), "buy": (13, 18)}, (15, 25), ""),
    ("Engine bay, AM20T in the tail cone (mount, 12 in prop extension, exhaust; radiator "
     "and coolant in the nose bay, option B)",
     {"cut": (8, 12), "form": (4, 8), "mach": (4, 6), "tube": (0, 0), "mold": (2, 3), "buy": (17, 26)},
     (30, 45), "prop extension and bushing are machined fatigue parts: a service, never home"),
    ("Cabin, windows, panel, seats, interior, baggage",
     {"cut": (15, 25), "form": (5, 10), "mach": (2, 4), "buy": (18, 31)}, (35, 55), ""),
    ("Electrical and avionics", {"buy": (25, 40)}, (25, 40), "counted as bought boxes"),
]

PRESCOTT_METAL_FLYING = [
    ("Wing, metal, re-sized +12.5% (spars, ribs, skins, leading-edge tanks)",
     {"cut": (80, 115), "form": (85, 125), "mach": (10, 14), "mold": (0, 4), "buy": (5, 8)}, (70, 110),
     "tapered: about 12 rib stations per side, 2-3 pieces each, every station unique; C-spar "
     "with nested caps (SA86)"),
    ("Flaps and ailerons, metal",
     {"cut": (30, 40), "form": (35, 45), "mach": (4, 6)}, (35, 50), "tapered: ribs unique"),
    ("T-tail, metal (stabiliser, elevator, tab, fin, rudder)",
     {"cut": (50, 70), "form": (55, 80), "mach": (10, 15), "buy": (2, 3)}, (70, 100), ""),
]

PRESCOTT_CARBON_FLYING = [
    ("Wing, carbon, re-sized +12.5% (molded skins, spar, webs, ribs, tank bulkheads)",
     {"mold": (24, 36), "cut": (16, 28), "mach": (8, 12), "buy": (4, 6)}, (30, 45),
     "upper and lower skin per side, spar with pultruded caps, ribs cut from sandwich panel; "
     "root fittings machined"),
    ("Flaps and ailerons, carbon", {"mold": (8, 12), "mach": (8, 12)}, (12, 18), ""),
    ("T-tail, carbon", {"mold": (14, 20), "mach": (12, 18), "buy": (2, 3)}, (20, 30), ""),
]

PRESCOTT_A = {"name": "Prescott Pusher, route A",
              "route": "welded cage, molded shells, metal wing and tail (as built, re-sized)",
              "assemblies": PRESCOTT_COMMON + PRESCOTT_METAL_FLYING}
PRESCOTT_B = {"name": "Prescott Pusher, route B",
              "route": "welded cage, molded shells, carbon wing and tail",
              "assemblies": PRESCOTT_COMMON + PRESCOTT_CARBON_FLYING}

MAKES = ["cut", "form", "tube", "mach", "mold", "buy"]


def totals(design):
    split = {m: [0, 0] for m in MAKES}
    uniq = [0, 0]
    for _name, mk, u, _note in design["assemblies"]:
        for m, (lo, hi) in mk.items():
            split[m][0] += lo
            split[m][1] += hi
        uniq[0] += u[0]
        uniq[1] += u[1]
    tot = [sum(v[0] for v in split.values()), sum(v[1] for v in split.values())]
    return {"split": split, "total": tot, "unique": uniq}


# ---------------------------------------------------------------------------
# Tooling for a small kit run. Composite mold surface = wetted area x 1.3
# (flanges, returns, split lines), priced at $120-360 per ft2 of mold surface
# (stage 4 build-up, E). Form blocks or dies at $150-400 per unique formed part.
# ---------------------------------------------------------------------------
MOLD_RATE = (120, 360)       # $/ft2 of mold surface, service-made, E (stage 4)
HOME_MOLD = (2, 4, 15, 40)    # h/ft2 and $/ft2 materials, builder-made, E (stage 4)
FORM_BLOCK = (150, 400)       # $ per unique formed part, E (stage 4)
FLANGE = 1.3
GROWTH = 1.125                # Prescott re-derivation: wing and tail area +12.5% (AER-3866)


def mold_cost(ft2):
    return (ft2 * MOLD_RATE[0], ft2 * MOLD_RATE[1])


# Prescott wetted areas. Shell mold surface is stage 4's 217 ft2 (AERO's 167 ft2
# fuselage x 1.3). Wing 113 ft2 (RCM86 table), tail 29.3 + about 16 ft2 (RCM86; fin E).
PRESCOTT_GEOM = {
    "shell_mold_ft2": 217,
    "wing_ref_ft2": 113 * GROWTH,
    "htail_ft2": 29.3 * GROWTH,
    "fin_ft2": 16 * GROWTH,
    "wetted_per_ref": 2.05,     # thin lifting surface, both faces plus thickness
    # leading-edge skin, if molded rather than stretch-formed: girth about 0.53 x mean
    # chord (3.95 ft at the original size, x sqrt(1.125)), on two 14 ft panels
    "le_part_ft2": 0.53 * 3.95 * math.sqrt(GROWTH) * 2 * 14.0,
}
pg = PRESCOTT_GEOM
pg["wing_mold_ft2"] = pg["wing_ref_ft2"] * pg["wetted_per_ref"] * FLANGE
pg["tail_mold_ft2"] = (pg["htail_ft2"] + pg["fin_ft2"]) * pg["wetted_per_ref"] * FLANGE
pg["le_mold_ft2"] = pg["le_part_ft2"] * FLANGE

# Aries: one constant-section skin mold pair serves both wings if the wing has no
# twist (not confirmed). Chord 5.43 ft, half-wing 15.7 ft (dossier).
ARIES_GEOM = {"chord_ft": 5.43, "panel_ft": 15.7}
ARIES_GEOM["skin_mold_ft2"] = 2 * 1.04 * ARIES_GEOM["chord_ft"] * ARIES_GEOM["panel_ft"] * FLANGE


def tooling():
    t = {}
    # Aries, metal kit (stage 4 build-up, unique formed parts re-counted here)
    a = totals(ARIES)
    formed_unique = (150, 250)
    t["Aries, matched-hole kit"] = [
        ("CAD and CNC programs (cut files, form-block files)", (10_000, 30_000)),
        (f"Form blocks / dies, {formed_unique[0]}-{formed_unique[1]} unique formed parts at "
         f"${FORM_BLOCK[0]}-{FORM_BLOCK[1]}",
         (formed_unique[0] * FORM_BLOCK[0], formed_unique[1] * FORM_BLOCK[1])),
        ("Assembly jigs (wing, fuselage, tail)", (10_000, 30_000)),
        ("Molds: cowl, radiator duct, tips, fairings, 65-70 ft2", (8_000, 25_000)),
    ]
    sm = ARIES_GEOM["skin_mold_ft2"]
    t["Aries option: carbon wing skins for the laminar lever"] = [
        (f"Upper and lower constant-section skin molds, {sm:.0f} ft2, both wings if untwisted",
         mold_cost(sm)),
    ]
    t["Prescott, route A (metal wing and tail)"] = [
        ("CAD and CNC programs", (10_000, 30_000)),
        (f"Shell plugs and molds, {pg['shell_mold_ft2']} ft2", mold_cost(pg["shell_mold_ft2"])),
        ("Cage welding jig (tube-laser cut, slotted-plate fixture)", (15_000, 40_000)),
        ("Form blocks, 30-50 unique wing and 30-50 unique tail formed parts",
         (60 * FORM_BLOCK[0], 100 * FORM_BLOCK[1])),
        (f"Leading-edge skin molds (in place of the lost stretch dies), {pg['le_mold_ft2']:.0f} ft2",
         mold_cost(pg["le_mold_ft2"])),
        ("Wing and tail assembly jigs", (8_000, 20_000)),
    ]
    t["Prescott, route B (carbon wing and tail)"] = [
        ("CAD and CNC programs", (10_000, 30_000)),
        (f"Shell plugs and molds, {pg['shell_mold_ft2']} ft2", mold_cost(pg["shell_mold_ft2"])),
        ("Cage welding jig", (15_000, 40_000)),
        (f"Wing skin and spar molds, {pg['wing_mold_ft2']:.0f} ft2", mold_cost(pg["wing_mold_ft2"])),
        (f"Tail molds, {pg['tail_mold_ft2']:.0f} ft2", mold_cost(pg["tail_mold_ft2"])),
        ("Bonding and assembly jigs", (8_000, 20_000)),
    ]
    out = {}
    for k, lines in t.items():
        lo = sum(v[0] for _n, v in lines)
        hi = sum(v[1] for _n, v in lines)
        out[k] = {"lines": [(n, v) for n, v in lines], "total": (lo, hi)}
    return out


# Kit prices for the crossover (E). Aries: stage 4 band. Prescott: the 1986 kit
# ($29,500 fixed / $36,500 retractable, AOPA86) at about x2.9 CPI is $86-106k; a
# modern kit with molded shells and a welded cage is put at $90-140k.
KIT_PRICE = {
    "Aries, matched-hole kit": (100_000, 150_000),
    "Prescott, route A (metal wing and tail)": (90_000, 140_000),
    "Prescott, route B (carbon wing and tail)": (100_000, 160_000),
}


def crossover(tool, kit, share=0.10):
    """Airframes until tooling is under `share` of the kit price."""
    return (math.ceil(tool[0] / (share * kit[1])), math.ceil(tool[1] / (share * kit[0])))


def fmt_k(v):
    return f"${v[0] / 1000:,.0f}-{v[1] / 1000:,.0f}k"


def main():
    designs = [ARIES, PRESCOTT_A, PRESCOTT_B]
    res = {"designs": {}, "tooling": {}, "geometry": {"prescott": PRESCOTT_GEOM, "aries": ARIES_GEOM}}
    for d in designs:
        tt = totals(d)
        res["designs"][d["name"]] = {"route": d["route"], **tt,
                                     "assemblies": [{"name": n, "split": mk, "unique": u, "note": nt}
                                                    for n, mk, u, nt in d["assemblies"]]}
        print(f"\n## {d['name']}: {d['route']}\n")
        print("| Assembly | Parts | Unique | Cut | Formed | Tube | Machined | Molded | Bought |")
        print("|---|---|---|---|---|---|---|---|---|")
        for n, mk, u, _nt in d["assemblies"]:
            lo = sum(v[0] for v in mk.values())
            hi = sum(v[1] for v in mk.values())
            cells = []
            for m in MAKES:
                v = mk.get(m)
                cells.append(f"{v[0]}-{v[1]}" if v and v[1] else "")
            print(f"| {n} | {lo}-{hi} | {u[0]}-{u[1]} | " + " | ".join(cells) + " |")
        cells = [f"{tt['split'][m][0]}-{tt['split'][m][1]}" if tt['split'][m][1] else "" for m in MAKES]
        print(f"| **Total** | **{tt['total'][0]}-{tt['total'][1]}** | **{tt['unique'][0]}-{tt['unique'][1]}** | "
              + " | ".join(cells) + " |")
        made = sum(tt["split"][m][0] for m in MAKES if m != "buy"), sum(tt["split"][m][1] for m in MAKES if m != "buy")
        print(f"\nMade from files or molds: {made[0]}-{made[1]}; bought: "
              f"{tt['split']['buy'][0]}-{tt['split']['buy'][1]}.")

    tl = tooling()
    res["tooling"] = {k: {"lines": v["lines"], "total": v["total"],
                          "kit_price": KIT_PRICE.get(k),
                          "crossover_10pct": crossover(v["total"], KIT_PRICE[k]) if k in KIT_PRICE else None}
                      for k, v in tl.items()}
    for k, v in tl.items():
        print(f"\n### Tooling: {k}\n")
        print("| Line | Cost (E) |\n|---|---|")
        for n, c in v["lines"]:
            print(f"| {n} | {fmt_k(c)} |")
        print(f"| **Total** | **{fmt_k(v['total'])}** |")
        if k in KIT_PRICE:
            c = crossover(v["total"], KIT_PRICE[k])
            print(f"\nKit price {fmt_k(KIT_PRICE[k])} (E): tooling under 10% of it after {c[0]}-{c[1]} airframes.")
    print("\n### Geometry used\n")
    for k, v in PRESCOTT_GEOM.items():
        print(f"- Prescott {k}: {v:.1f}")
    for k, v in ARIES_GEOM.items():
        print(f"- Aries {k}: {v:.1f}")
    if "--json" in sys.argv:
        with open("build_plans.json", "w") as f:
            json.dump(res, f, indent=1)


if __name__ == "__main__":
    main()
