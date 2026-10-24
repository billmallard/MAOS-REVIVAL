#!/usr/bin/env python3
"""Stage 1 screen for the legacy design survey.

Reads candidates.json (published numbers, each with grade and source) and
computes, for every candidate:

  - the screen against the brief's targets (useful load, range, cruise),
  - payload with fuel for 1,000 nm, with no reserve and with a 45 min reserve,
  - a first-cut fit against the Aeromomentum engine line,
  - sanity flags where the published numbers do not build up.

Usage:
  python3 screen.py            print the screen table and flags
  python3 screen.py --write    also write them into LONGLIST.md between markers

The method and its limits are in LONGLIST.md ("Method"). In short: fuel for a
leg = distance / KTAS x fuel flow at a published cruise setting, no wind, no
taxi/climb/descent allowance (optimistic by roughly 3-5 gal on a 1,000 nm
leg). The reserve is 45 min at the same fuel flow. Where a setting states its
power but no fuel flow, the flow is estimated at BSFC_EST and graded E.
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "candidates.json"
LONGLIST = HERE / "LONGLIST.md"

# Targets from docs/BRIEF.md.
UL_FLOOR = 1000.0      # lb
RANGE_FLOOR = 1000.0   # nm
SPEED_FLOOR = 160.0    # KTAS, at altitude
SPEED_PREF = 180.0     # KTAS
# Near-miss bands: within 10% on load and range, 10 kt on speed.
UL_NEAR = 900.0
RANGE_NEAR = 900.0
SPEED_NEAR = 150.0
# "At altitude": a cruise figure below this altitude, or with none stated,
# is flagged rather than accepted at face value.
ALT_MIN = 6000.0

LEG_NM = 1000.0
RESERVE_H = 0.75
DENSITY = {"avgas": 6.0, "jet-a": 6.7}  # lb/US gal
# Best-power-to-economy piston BSFC, lb/hp/h, used only where a setting's
# power is published but its fuel flow is not (Gudmundsson ch. 7 range of
# 0.42-0.50 for air-cooled GA pistons; 0.45 is the middle).
BSFC_EST = 0.45

# Aeromomentum line, aeromomentum.com, read 2026-10-24 (grade F). Power is the
# published rating; no continuous rating or critical altitude is published
# for the turbo models. Dry weight lb, where published.
AEROMOMENTUM = [
    ("AM13", 100, False, None),
    ("AM15", 120, False, 185),
    ("AM13T", 140, True, 200),
    ("AM15T", 160, True, 215),
    ("AM20T", 260, True, 285),
]


def val(field):
    """A graded number is [value, grade, source, note]; return the value."""
    if field is None:
        return None
    if isinstance(field, list):
        return field[0]
    return field


def useful(c):
    """Screen on the fleet figure where one is published, then an as-flown
    estimate (a one-off prototype known to have flown heavier than its
    published design figure), else the factory."""
    return val(c.get("useful_fleet")) or val(c.get("useful_asflown")) or val(c.get("useful"))


def flow(c, s):
    """Fuel flow for a setting, and whether it is our estimate."""
    if s.get("gph"):
        return s["gph"], False
    if s.get("power_pct") and c.get("hp"):
        hp = c["hp"] * c.get("engines", 1)
        return BSFC_EST * hp * s["power_pct"] / 100.0 / DENSITY[c.get("fuel_type", "avgas")], True
    return None, False


def settings(c):
    return c.get("cruise", [])


def screen_setting(c):
    for s in settings(c):
        if s.get("screen"):
            return s
    return settings(c)[0] if settings(c) else {}


def legs(c, fuel=None):
    """Per-setting still-air range and payload at LEG_NM."""
    ul = useful(c)
    fuel = fuel or val(c.get("fuel_gal"))
    dens = DENSITY[c.get("fuel_type", "avgas")]
    # Our estimated flow is used only when no setting publishes one.
    published = any(s.get("gph") for s in settings(c))
    out = []
    for s in settings(c):
        gph, est = flow(c, s)
        if not s.get("ktas") or not gph or not fuel or (est and published):
            continue
        rng = fuel / gph * s["ktas"]
        pay = []
        for res in (0.0, RESERVE_H):
            gal = (LEG_NM / s["ktas"] + res) * gph
            pay.append(None if (gal > fuel or ul is None) else ul - gal * dens)
        out.append({"s": s, "gph": gph, "est": est, "rng": rng, "p0": pay[0], "p45": pay[1]})
    return out


def best_leg(c):
    L = legs(c)
    if not L:
        return None

    def key(x):
        if x["p45"] is not None:
            return (2, x["p45"])
        if x["p0"] is not None:
            return (1, x["p0"])
        return (0, x["rng"])
    return max(L, key=key)


def band(x, floor, near):
    if x is None:
        return "?"
    if x >= floor:
        return "pass"
    if x >= near:
        return "near"
    return "fail"


def screen(c):
    ul = useful(c)
    ul_s = band(ul, UL_FLOOR, UL_NEAR)

    # Range: still-air, no reserve, best published setting, so every row is on
    # one basis. Published ranges carry mixed reserve bases; fall back to one
    # only when no fuel flow can be had for any setting.
    L = legs(c)
    rng_pub = c.get("range", {}).get("nm")
    rng_calc = max((x["rng"] for x in L), default=None)
    rng = rng_calc or rng_pub
    rng_s = band(rng, RANGE_FLOOR, RANGE_NEAR)
    rng_basis = "calc" if rng_calc else ("pub" if rng_pub else "")
    if rng_calc and any(x["est"] for x in L if x["rng"] == rng_calc):
        rng_basis = "calc, est. flow"

    s = screen_setting(c)
    spd, alt = s.get("ktas"), s.get("alt_ft")
    spd_s = band(spd, SPEED_FLOOR, SPEED_NEAR)
    if spd_s == "pass" and spd >= SPEED_PREF:
        spd_s = "pass+"
    alt_ok = alt is not None and alt >= ALT_MIN

    misses = []
    if ul_s in ("near", "fail"):
        misses.append(f"UL -{UL_FLOOR - ul:.0f} lb")
    if rng_s in ("near", "fail"):
        misses.append(f"range -{RANGE_FLOOR - rng:.0f} nm")
    if spd_s in ("near", "fail"):
        misses.append(f"speed -{SPEED_FLOOR - spd:.0f} kt")
    states = [ul_s, rng_s, spd_s.rstrip("+")]
    if c.get("overall_override"):
        overall, misses = c["overall_override"], []
    elif "?" in states:
        overall = "incomplete"
    elif "fail" in states:
        overall = "fail"
    elif "near" in states:
        overall = "near miss"
    else:
        overall = "pass"
    # A speed with no altitude, or a low one, is not accepted at face value:
    # the verdict says so rather than hiding it in a flag.
    if overall in ("pass", "near miss") and spd is not None and not alt_ok:
        overall += ", speed unconditioned"
    return {
        "ul": ul, "ul_s": ul_s, "rng": rng, "rng_s": rng_s, "rng_basis": rng_basis,
        "rng_pub": rng_pub, "rng_calc": rng_calc,
        "spd": spd, "alt": alt, "alt_ok": alt_ok, "spd_s": spd_s,
        "overall": overall, "misses": ", ".join(misses),
    }


def flags(c):
    """Sanity checks: where the published numbers do not build up."""
    out = []
    s = screen(c)
    if s["rng_calc"] and s["rng_pub"] and abs(s["rng_pub"] - s["rng_calc"]) / s["rng_calc"] > 0.15:
        out.append(f"published range {s['rng_pub']:,.0f} nm vs {s['rng_calc']:,.0f} nm from fuel and flow")
    if s["spd"] is not None and not s["alt_ok"]:
        out.append("screen speed has no altitude, or is below 6,000 ft")
    mtow, emp, ul = val(c.get("mtow")), val(c.get("empty")), val(c.get("useful"))
    if mtow and emp and ul and abs(mtow - emp - ul) > 25:
        out.append(f"weights do not add: {mtow:,.0f} - {emp:,.0f} != {ul:,.0f}")
    if c.get("useful_fleet") and c.get("useful"):
        d = val(c["useful"]) - val(c["useful_fleet"])
        if d > 0:
            out.append(f"fleet useful load {d:,.0f} lb below factory")
    if c.get("useful_asflown") and c.get("useful"):
        d = val(c["useful"]) - val(c["useful_asflown"])
        if d > 0:
            out.append(f"as-flown useful load estimate {d:,.0f} lb below the published design figure")
    opt = val(c.get("fuel_opt_gal"))
    if opt:
        r = max((x["rng"] for x in legs(c, opt)), default=None)
        if r:
            out.append(f"with optional tanks ({opt:g} gal) still-air range is {r:,.0f} nm")
    out += c.get("flags", [])
    return out


def engine_fit(c):
    if c.get("engine_fit"):
        return c["engine_fit"]
    hp = c.get("hp")
    n = c.get("engines", 1)
    if c.get("fuel_type") == "jet-a":
        return "No: turbine; no Aeromomentum equivalent"
    if not hp:
        return "?"
    tw = f"{n}x " if n > 1 else ""
    for name, p, turbo, _ in AEROMOMENTUM:
        if p >= hp and (turbo or not c.get("turbo")):
            return f"Yes: {tw}{name} ({p} hp) for {hp} hp"
    # Above the line: AM20T at 260 hp; cruise speed scaled by the cube root of
    # power (parasite-drag-dominated cruise, same propulsive efficiency).
    f = (260.0 / hp) ** (1.0 / 3.0)
    spd = screen_setting(c).get("ktas")
    est = f", est. {spd * f:.0f} KTAS" if spd else ""
    return f"Short: {tw}AM20T 260 hp vs {hp} hp (-{(1 - f) * 100:.0f}% speed{est})"


def fmt(x, unit=""):
    return "-" if x is None else f"{x:,.0f}{unit}"


def table(cands):
    hdr = ("| # | Candidate | Seats | Origin | Useful load, lb | Range, nm (still air) "
           "| Cruise KTAS @ alt | Screen | Payload @ 1,000 nm, lb (no res / 45 min) "
           "| Aeromomentum fit | Why it died |")
    rows = [hdr, "|" + "---|" * 11]
    for i, c in enumerate(cands):
        s = screen(c)
        ul_txt = f"{fmt(s['ul'])} {s['ul_s']}"
        if c.get("useful_fleet"):
            ul_txt += f" (fleet; {fmt(val(c.get('useful')))} factory)"
        elif c.get("useful_asflown"):
            ul_txt += f" (as-flown est.; {fmt(val(c.get('useful')))} design)"
        rng_txt = f"{fmt(s['rng'])} {s['rng_s']}" + (f" ({s['rng_basis']})" if s["rng_basis"] else "")
        if s["spd"] is None:
            spd_txt = "-"
        else:
            spd_txt = f"{s['spd']:.0f} @ {fmt(s['alt'], ' ft') if s['alt'] else 'alt n/s'} {s['spd_s']}"
            if not s["alt_ok"]:
                spd_txt += " *"
            if screen_setting(c).get("design"):
                spd_txt += " (design)"
        b = best_leg(c)
        if b is None:
            pay = "no fuel flow or fuel published"
        elif b["p0"] is None:
            pay = f"cannot: {b['rng']:,.0f} nm max on usable fuel"
        else:
            pay = f"{fmt(b['p0'])} / {fmt(b['p45']) if b['p45'] is not None else 'cannot'}"
            pay += f" @ {b['s']['ktas']:.0f} kt, {b['gph']:.1f} gph" + (" (est. flow)" if b["est"] else "")
        verdict = s["overall"] + (f" ({s['misses']})" if s["misses"] else "")
        rows.append(
            f"| {i} | [{c['name']}](../candidates/{c['id']}.md) | {c['seats']} | {', '.join(c['origin'])} "
            f"| {ul_txt} | {rng_txt} | {spd_txt} | {verdict} | {pay} "
            f"| {engine_fit(c)} | {c.get('why_died_short', '')} |"
        )
    return "\n".join(rows)


def flag_list(cands):
    lines = []
    for c in cands:
        f = flags(c)
        if f:
            lines.append(f"- **{c['name']}**: " + "; ".join(f) + ".")
    return "\n".join(lines)


def counts(cands):
    out = {}
    for c in cands[1:]:  # row 0 is the reference
        o = screen(c)["overall"].split(",")[0].split(" (")[0]
        out[o] = out.get(o, 0) + 1
    return out


def replace_block(txt, name, body):
    a, b = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    pre, rest = txt.split(a)
    _, post = rest.split(b)
    return f"{pre}{a}\n{body}\n{b}{post}"


def main():
    cands = json.loads(DATA.read_text())
    t, fl = table(cands), flag_list(cands)
    print(t, "\n\n", fl, "\n\nScreen counts (excluding the reference row):", counts(cands))
    if "--write" in sys.argv:
        txt = LONGLIST.read_text()
        txt = replace_block(txt, "screen-table", t)
        txt = replace_block(txt, "flags", fl)
        LONGLIST.write_text(txt)


if __name__ == "__main__":
    main()
