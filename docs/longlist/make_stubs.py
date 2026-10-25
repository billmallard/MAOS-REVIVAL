#!/usr/bin/env python3
"""Write a stage 1 stub per candidate in docs/candidates/ from candidates.json.

Stubs are a starting point; from stage 3 on the shortlisted dossiers are
edited by hand. An existing file is never overwritten unless --force is given.

Usage:
  python3 make_stubs.py [--force]
"""

import json
import sys
from pathlib import Path

import screen as S

OUT = S.HERE.parent / "candidates"
ORIGIN = {
    "a": "experimental kit or plans",
    "b": "certified, out of production",
    "c": "prototype that never reached production",
    "d": "foreign design",
}
GRADES = ("F factory/brochure/designer claim; T type certificate data sheet; P flight test, "
          "POH or magazine pilot report; B builder-fleet, registry or owner data; "
          "R measured record; E estimate (whose is stated)")


def cell(x):
    return "-" if x in (None, "") else str(x).replace("|", "/")


def link(src):
    return f"[source]({src})" if src.startswith("http") else cell(src)


def num_row(label, f, unit="lb"):
    if not f:
        return f"| {label} | not found | | | |"
    v, grade, src, note = (f + ["", "", ""])[:4]
    return f"| {label} | {v:,g} {unit} | {grade} | {link(src)} | {cell(note)} |"


def stub(c):
    L = [
        f"# {c['name']}",
        "",
        "Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. "
        "Published numbers only; nothing here is our own performance check yet.",
        "",
        "## Identity",
        "",
        "| | |",
        "|---|---|",
        f"| Origin | {', '.join(ORIGIN[o] for o in c['origin'])} |",
        f"| Designer / maker | {cell(c.get('designer'))} |",
        f"| Years | {cell(c.get('years'))} |",
        f"| Number built | {cell(c.get('built'))} |",
        f"| Survivors / registered | {cell(c.get('flying'))} |",
        f"| Seats | {c['seats']} |",
        f"| Configuration | {cell(c.get('config'))} |",
        f"| Construction | {cell(c.get('construction'))} |",
        f"| Engine | {cell(c.get('engine'))} |",
        "",
        "## Published numbers",
        "",
        f"Grades: {GRADES}.",
        "",
        "| Quantity | Value | Grade | Source | Note |",
        "|---|---|---|---|---|",
        num_row("MTOW", c.get("mtow")),
        num_row("Empty weight", c.get("empty")),
        num_row("Useful load", c.get("useful")),
        num_row("Useful load, fleet or as-weighed", c.get("useful_fleet")),
    ]
    if c.get("useful_asflown"):
        L.append(num_row("Useful load, as-flown estimate", c.get("useful_asflown")))
    L += [
        num_row("Usable fuel", c.get("fuel_gal"), "US gal"),
    ]
    if c.get("fuel_opt_gal"):
        L.append(num_row("Optional fuel", c.get("fuel_opt_gal"), "US gal"))
    r = c.get("range")
    if r:
        L.append(f"| Published range | {r['nm']:,} nm | {r['grade']} | {link(r['src'])} | {cell(r.get('basis'))} |")
    L += [
        "",
        "Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade "
        "unless a setting states it):",
        "",
        "| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |",
        "|---|---|---|---|---|---|---|",
    ]
    sp, sm = S.best_speed(c, "pub"), S.best_speed(c, "meas")
    for x in S.settings(c):
        star = (" P" if x is sp else "") + (" M" if x is sm else "")
        pct = f"{x['power_pct']}%" if x.get("power_pct") else "-"
        L.append(f"| {x['ktas']}{star} | {cell(x.get('alt_ft'))} | {pct} | {cell(x.get('gph'))} "
                 f"| {x['grade']} | {link(x['src'])} | {cell(x.get('note'))} |")
    L += [
        "",
        "## Screen (published numbers; like for like)",
        "",
        "Two screens, never mixed: the maker's figures as published, and measured or reported data. "
        "The three targets are separate floors; payload at 1,000 nm is information only.",
        "",
    ]
    for lab, bb in (("As published", "pub"), ("Measured or reported", "meas")):
        col = S.screen_col(c, bb)
        if S.cell(col) == "-":
            L.append(f"- **{lab}: no data found.**")
            continue
        spd = ("not found" if col["spd"] is None else
               f"{S.fmt(col['spd'])} KTAS at {S.fmt(col['alt'], ' ft') if col['alt'] else 'an unstated altitude'} ({col['spd_s']})")
        L += [
            f"- **{lab}: {col['overall']}**" + (f" - {col['misses']}" if col["misses"] else ""),
            f"  - Useful load: {S.fmt(col['ul'])} lb ({col['ul_s']}) against 1,000 lb.",
            f"  - Range: {S.fmt(col['rng'])} nm ({col['rng_s']}; {col['rng_note'] or 'none found'}) against 1,000 nm.",
            f"  - Cruise: {spd} against >160 KTAS (>180 preferred).",
            f"  - Payload at 1,000 nm (information): {S.payload(c, bb) or 'cannot be computed on this basis'}.",
        ]
    L += [
        f"- Aeromomentum fit (first cut): {S.engine_fit(c)}.",
        "",
        "Sanity flags:",
        "",
    ]
    fl = S.flags(c)
    L += [f"- {f}" for f in fl] if fl else ["- none raised"]
    L += [
        "",
        "## Why it died",
        "",
        cell(c.get("why_died")),
        "",
        "## Idea ledger (what a new airplane should keep; AERO's judgement)",
        "",
    ]
    L += [f"- {x}" for x in c.get("ideas", [])] or ["- none recorded yet"]
    L += [
        "",
        "## Rights and provenance (known so far; research, not legal advice)",
        "",
        cell(c.get("rights")) + " Owned by the stage 2 rights research (AER-3787).",
        "",
        "## Safety record",
        "",
        cell(c.get("safety")),
        "",
        "## Not yet done",
        "",
        "- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.",
        "- Installed-weight and cooling comparison against the Aeromomentum engine.",
        "- What a modern rebuild changes (MANUFACTURING, stage 4).",
        "",
    ]
    return "\n".join(L)


def main():
    force = "--force" in sys.argv
    OUT.mkdir(exist_ok=True)
    n = 0
    for c in json.loads(S.DATA.read_text()):
        p = OUT / f"{c['id']}.md"
        if p.exists() and not force:
            continue
        p.write_text(stub(c))
        n += 1
    print(f"wrote {n} stubs to {OUT}")


if __name__ == "__main__":
    main()
