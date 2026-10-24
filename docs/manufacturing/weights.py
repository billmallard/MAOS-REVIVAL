"""Stage 4 rebuild empty-weight ranges, from rebuild_weights.json.

  python3 weights.py          -> prints the tables used in docs/MANUFACTURING.md
                                 and in each dossier's stage 4 section
  python3 weights.py --json   -> results.json (the same numbers, machine-readable)

Convention. Every item carries two deltas: "light" (the lightest credible
outcome) and "heavy" (the heaviest credible outcome), in lb, signed (negative
saves weight). The rebuild empty weight is a range:

  light end = base.low  + sum(item.light)
  heavy end = base.high + sum(item.heavy)

The engine swap is NOT among the items. It is reported separately, as AERO's
stage 3 does: the headline useful load takes no credit for a lighter engine,
because nobody has checked CG yet. Items marked "option" are configuration
choices (deleting pressurisation, a constant-speed prop) that are reported
beside the range but not summed into it. "With engine credit" adds the installed-mass
change [most saving, least saving] from our per-variant check of the original
engine (engine_delta_lb), on AERO's Aeromomentum installed-mass rule.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def r10(x):
    return int(round(x / 10.0)) * 10


def core(c):
    """Items that count toward the range; options are reported but not summed."""
    return [t for t in c["items"] if not t.get("option")]


def compute(d):
    out = {}
    for i, c in d["designs"].items():
        light = c["base"]["low"] + sum(t["light"] for t in core(c))
        heavy = c["base"]["high"] + sum(t["heavy"] for t in core(c))
        eng = c.get("engine_delta_lb")
        out[i] = {
            "name": c["name"],
            "mtow": c["mtow"],
            "stage3_empty": c["stage3_empty"],
            "stage3_useful": c["mtow"] - c["stage3_empty"],
            "airframe_delta_light": sum(t["light"] for t in core(c)),
            "airframe_delta_heavy": sum(t["heavy"] for t in core(c)),
            "empty_light": r10(light),
            "empty_heavy": r10(heavy),
            "useful_light": c["mtow"] - r10(heavy),
            "useful_heavy": c["mtow"] - r10(light),
            "engine_delta_lb": eng,
            "empty_light_eng": None if eng is None else r10(light + eng[0]),
            "empty_heavy_eng": None if eng is None else r10(heavy + eng[1]),
        }
    return out


def table(d, res):
    L = ["| Design | Stage 3 empty, lb (basis) | Airframe change, lb | Rebuild empty, lb (no engine credit) | "
         "Useful load, lb (stage 3 -> stage 4) | Engine change, lb (our check) | Rebuild empty with engine credit, lb | Grade |",
         "|---|---|---|---|---|---|---|---|"]
    for i, r in res.items():
        c = d["designs"][i]
        eng = "-" if r["engine_delta_lb"] is None else f"{r['engine_delta_lb'][0]:+.0f} to {r['engine_delta_lb'][1]:+.0f}"
        ewe = "-" if r["empty_light_eng"] is None else f"{r['empty_light_eng']:,}-{r['empty_heavy_eng']:,}"
        L.append(
            f"| {r['name']} | {r['stage3_empty']:,} ({c['base']['stage3_grade']}) | "
            f"{r['airframe_delta_light']:+.0f} to {r['airframe_delta_heavy']:+.0f} | "
            f"{r['empty_light']:,}-{r['empty_heavy']:,} | "
            f"{r['stage3_useful']:,} -> {r['useful_light']:,}-{r['useful_heavy']:,} | {eng} | {ewe} | E |")
    return "\n".join(L)


def items(d, i):
    c = d["designs"][i]
    b = c["base"]
    L = ["| Item | Light, lb | Heavy, lb | Basis | Grade |", "|---|---|---|---|---|",
         f"| Starting empty weight | {b['low']:,} | {b['high']:,} | {b['basis']} | {b['grade']} |"]
    for t in core(c):
        L.append(f"| {t['item']} | {t['light']:+.0f} | {t['heavy']:+.0f} | {t['basis']} | {t['grade']} |")
    sl = b["low"] + sum(t["light"] for t in core(c))
    sh = b["high"] + sum(t["heavy"] for t in core(c))
    L.append(f"| **Rebuild empty weight, no engine credit** | **{r10(sl):,}** | **{r10(sh):,}** | "
             f"sum, rounded to 10 lb | E |")
    for t in c["items"]:
        if t.get("option"):
            L.append(f"| Option, not in the total: {t['item']} | {t['light']:+.0f} | {t['heavy']:+.0f} | "
                     f"{t['basis']} | {t['grade']} |")
    return "\n".join(L)


def main():
    d = json.load(open(os.path.join(HERE, "rebuild_weights.json")))
    res = compute(d)
    if "--json" in sys.argv:
        json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1)
        return
    print(table(d, res))
    for i in d["designs"]:
        print(f"\n### {d['designs'][i]['name']}\n")
        print(items(d, i))


if __name__ == "__main__":
    main()
