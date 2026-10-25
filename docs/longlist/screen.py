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
UL_TARGET = 1000.0      # lb
RANGE_TARGET = 1000.0   # nm
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


def legs(c, fuel=None, b=None):
    """Per-setting still-air range and payload at LEG_NM; b limits it to one
    basis ('pub' or 'meas') and takes that basis's useful load and fuel."""
    ul = useful(c)
    fuel = fuel or val(c.get("fuel_gal"))
    if b == "pub":
        ul = val(c.get("useful"))
    elif b == "meas":
        ul = val(c.get("useful_fleet")) or val(c.get("useful_asflown"))
        fuel = val(c.get("fuel_gal_meas")) or fuel
    dens = DENSITY[c.get("fuel_type", "avgas")]
    # Our estimated flow is used only when no setting publishes one.
    published = any(s.get("gph") for s in settings(c))
    out = []
    for s in settings(c):
        gph, est = flow(c, s)
        if not s.get("ktas") or not gph or not fuel or (est and published):
            continue
        if b and basis(s) != b and not (est and b == "pub"):
            continue
        rng = fuel / gph * s["ktas"]
        pay = []
        for res in (0.0, RESERVE_H):
            gal = (LEG_NM / s["ktas"] + res) * gph
            pay.append(None if (gal > fuel or ul is None) else ul - gal * dens)
        out.append({"s": s, "gph": gph, "est": est, "rng": rng, "p0": pay[0], "p45": pay[1]})
    return out


def best_leg(c, b=None):
    L = legs(c, b=b)
    if not L:
        return None

    def key(x):
        if x["p45"] is not None:
            return (2, x["p45"])
        if x["p0"] is not None:
            return (1, x["p0"])
        return (0, x["rng"])
    return max(L, key=key)


def band(x, threshold, near):
    if x is None:
        return "?"
    if x >= threshold:
        return "pass"
    if x >= near:
        return "near"
    return "fail"


# Like for like (brief, amended 2026-10-24): every row is screened twice, once on
# the maker's own figures as published and once on measured or reported data,
# and the two are never mixed. A cruise setting's basis is explicit ("basis":
# "pub" or "meas") or follows its grade: F and T are published; R and B are
# measured; P is published when it is a handbook, spec-box or factory figure,
# measured otherwise (an independent flight test, a timed magazine run, an
# owner's report).
PUB_WORDS = ("poh", "flight manual", "handbook", "spec box", "factory")


def basis(s):
    if s.get("basis"):
        return s["basis"]
    g = s.get("grade")
    if g in ("F", "T"):
        return "pub"
    if g in ("R", "B"):
        return "meas"
    if g == "P":
        return "pub" if any(w in (s.get("note") or "").lower() for w in PUB_WORDS) else "meas"
    return "est"


def best_speed(c, b):
    """Highest speed on basis b that states an altitude of at least ALT_MIN;
    else the highest one, which is then marked unconditioned."""
    S = [s for s in settings(c) if basis(s) == b and s.get("ktas")]
    ok = [s for s in S if (s.get("alt_ft") or 0) >= ALT_MIN]
    if ok:
        return max(ok, key=lambda s: s["ktas"])
    return max(S, key=lambda s: s["ktas"]) if S else {}


def calc_range(c, b):
    """Still-air, no-reserve range from usable fuel and flow, on basis b only."""
    fuel = val(c.get("fuel_gal_meas")) if b == "meas" and c.get("fuel_gal_meas") else val(c.get("fuel_gal"))
    R = [(fuel / s["gph"] * s["ktas"], s["ktas"]) for s in settings(c)
         if basis(s) == b and s.get("ktas") and s.get("gph") and fuel]
    return max(R, default=(None, None))


def verdict(states):
    if "?" in states:
        missing = [n for n, x in zip(("UL", "range", "speed"), states) if x == "?"]
        known = [x for x in states if x != "?"]
        return "incomplete: no " + " or ".join(missing) + (", fails on the rest" if "fail" in known else "")
    if "fail" in states:
        return "fail"
    if "near" in states:
        return "near miss"
    return "pass"


def screen_col(c, b):
    """One column of the screen: 'pub' (as published) or 'meas' (measured)."""
    if b == "pub":
        ul = val(c.get("useful"))
        rng = c.get("range", {}).get("nm")
        rng_note = c.get("range", {}).get("basis", "")
        if rng is None:
            rng, kt = calc_range(c, "pub")
            rng_note = f"derived from published fuel and flow at {kt:.0f} KTAS" if rng else ""
    else:
        ul = val(c.get("useful_fleet")) or val(c.get("useful_asflown"))
        rng, kt = calc_range(c, "meas")
        rng_note = f"still air, no reserve, from fuel and measured flow at {kt:.0f} KTAS" if rng else ""
    s = best_speed(c, b)
    spd, alt = s.get("ktas"), s.get("alt_ft")
    alt_ok = alt is not None and alt >= ALT_MIN
    st = [band(ul, UL_TARGET, UL_NEAR), band(rng, RANGE_TARGET, RANGE_NEAR), band(spd, SPEED_FLOOR, SPEED_NEAR)]
    spd_s = st[2] + ("+" if st[2] == "pass" and spd >= SPEED_PREF else "")
    misses = []
    if st[0] in ("near", "fail"):
        misses.append(f"UL -{UL_TARGET - ul:.0f} lb")
    if st[1] in ("near", "fail"):
        misses.append(f"range -{RANGE_TARGET - rng:.0f} nm")
    if st[2] in ("near", "fail"):
        misses.append(f"speed -{SPEED_FLOOR - spd:.0f} kt")
    overall = verdict(st)
    if b == "meas" and "?" in st and any(x != "?" for x in st):
        # Measured data is usually partial on a long list: report what was
        # measured rather than calling the row incomplete.
        overall = "partial: " + ", ".join(f"{n} {x}" for n, x in zip(("UL", "range", "speed"), st) if x != "?")
    if b == "pub" and c.get("overall_override"):
        overall, misses = c["overall_override"], []
    if spd is not None and not alt_ok and (overall.split(" (")[0] in ("pass", "near miss")
                                           or overall.startswith("partial")):
        overall += ", speed unconditioned"
    return {"ul": ul, "ul_s": st[0], "rng": rng, "rng_s": st[1], "rng_note": rng_note,
            "spd": spd, "alt": alt, "alt_ok": alt_ok, "spd_s": spd_s, "set": s,
            "overall": overall, "misses": ", ".join(misses)}


def screen(c):
    """Kept for the flags: the published column, plus both range figures."""
    p = screen_col(c, "pub")
    p["rng_pub"] = c.get("range", {}).get("nm")
    p["rng_calc"] = max((x["rng"] for x in legs(c)), default=None)
    return p


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


def payload(c, b):
    """Payload at 1,000 nm on one basis, as text; None when that basis has no leg."""
    x = best_leg(c, b)
    if x is None or x["p0"] is None and (b == "meas" and not (c.get("useful_fleet") or c.get("useful_asflown"))):
        return None
    if x["p0"] is None:
        return f"cannot ({x['rng']:,.0f} nm max)"
    return (f"{fmt(x['p0'])} / {fmt(x['p45']) if x['p45'] is not None else 'cannot'}"
            f" @ {x['s']['ktas']:.0f} kt, {x['gph']:.1f} gph" + (" (est. flow)" if x["est"] else ""))


def cell(col):
    if col["ul"] is None and col["rng"] is None and col["spd"] is None:
        return "-"
    spd = "-" if col["spd"] is None else (
        f"{col['spd']:.0f} @ {fmt(col['alt'], ' ft') if col['alt'] else 'alt n/s'}"
        + (" *" if not col["alt_ok"] else ""))
    if col["set"].get("design"):
        spd += " (design)"
    return (f"{fmt(col['ul'])} {col['ul_s']}; {fmt(col['rng'])} {col['rng_s']}; "
            f"{spd} {col['spd_s'] if col['spd'] is not None else ''}").strip()


def table(cands):
    hdr = ("| # | Candidate | Seats | Origin | As published: UL lb; range nm; KTAS @ alt | Screen, as published "
           "| Measured or reported: UL lb; range nm; KTAS @ alt | Screen, measured "
           "| Payload @ 1,000 nm, lb (no res / 45 min) | Aeromomentum fit | Why it died |")
    rows = [hdr, "|" + "---|" * 11]
    for i, c in enumerate(cands):
        P, M = screen_col(c, "pub"), screen_col(c, "meas")
        vp = P["overall"] + (f" ({P['misses']})" if P["misses"] else "")
        vm = "no measured data" if cell(M) == "-" else M["overall"] + (f" ({M['misses']})" if M["misses"] else "")
        pay = "; ".join(f"{lab}: {payload(c, bb)}" for lab, bb in (("pub", "pub"), ("meas", "meas"))
                        if payload(c, bb) is not None) or "no fuel flow published"
        rows.append(
            f"| {i} | [{c['name']}](../candidates/{c['id']}.md) | {c['seats']} | {', '.join(c['origin'])} "
            f"| {cell(P)} | {vp} | {cell(M)} | {vm} | {pay} "
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


def counts(cands, b="pub"):
    out = {}
    for c in cands[1:]:  # row 0 is the reference
        o = screen_col(c, b)["overall"].split(",")[0].split(" (")[0]
        if b == "meas" and cell(screen_col(c, b)) == "-":
            o = "no measured data"
        elif o.startswith("partial"):
            o = "partial"
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
    print(t, "\n\n", fl, "\n\nScreen counts, excluding the reference row: as published",
          counts(cands, "pub"), "; measured", counts(cands, "meas"))
    if "--write" in sys.argv:
        txt = LONGLIST.read_text()
        txt = replace_block(txt, "screen-table", t)
        txt = replace_block(txt, "flags", fl)
        LONGLIST.write_text(txt)


if __name__ == "__main__":
    main()
