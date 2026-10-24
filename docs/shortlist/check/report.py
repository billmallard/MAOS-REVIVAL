"""Turn results/<id>.json into the markdown tables used in docs/SHORTLIST.md
and in the stage 3 section of each dossier.

  python3 report.py            -> results/tables.md and results/<id>_stage3.md
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ORDER = ["bellanca-t250-aries", "prescott-pusher", "express-2000", "lancair-iv-p", "meyers-200d", "mooney-301",
         "cessna-p210n", "cozy-mkiv",
         # checked in stage 3, then dropped by Bill (2026-10-24); kept as record
         "rutan-defiant", "cirrus-vk-30", "velocity-xl-rg-100gal", "velocity-xl-rg", "berkut-360"]


def f0(x):
    return "cannot" if x is None else f"{x:,.0f}"


def load(i):
    return json.load(open(os.path.join(HERE, "results", i + ".json")))


def calib_rows(r):
    out = []
    for c in r["calibration"]:
        p = c["pub"]
        out.append(
            f"| {p['ktas']:.0f} | {p['alt_ft']:,} | {p['hp']} | {p.get('gph') or '-'} | "
            f"{p.get('grade')} | {c['our_ktas']:.0f} | {c['d_ktas_pct']:+.0f}% | "
            f"{c['k_match']:.2f} | {c['our_hp_at_pub_ktas']:.0f} | {p.get('note', '')} |")
    return out


def am_row(name, r, case):
    a = r["am"][case]
    return (f"| {name} | {r['am_model']} | {a['alt_ft']/1000:.0f}k | {a['ktas']:.0f} "
            f"({a['opt_ktas']:.0f}) | {a['useful']:,.0f} ({a['useful_opt']:,.0f}) | "
            f"{a['range_nm_fullfuel']:,.0f} | {f0(a['payload_1000_0'])} | "
            f"{f0(a['payload_1000_45'])} ({f0(a['opt_payload_1000_45'])}) | "
            f"{a['eco_ktas']:.0f}: {f0(a['eco_payload_1000_0'])} / {f0(a['eco_payload_1000_45'])} |")


AM_HDR = ("| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | "
          "Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | "
          "Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | "
          "Economy (65%) KTAS: payload no res / 45 min |\n|---|---|---|---|---|---|---|---|---|")

CAL_HDR = ("| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | "
           "Difference | Drag factor to match | Our hp for the published speed | Conditions |\n"
           "|---|---|---|---|---|---|---|---|---|---|")


def stage3(i, r):
    L = []
    b = r["breakdown"]
    L.append(f"Model: `docs/shortlist/check/models/{i}.json`; result: "
             f"`docs/shortlist/check/results/{i}.json`. Method in "
             f"[SHORTLIST.md](../SHORTLIST.md#method).\n")
    L.append("**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** "
             + ", ".join(f"{k} {v['wet_ft2']:.0f} ft2" for k, v in r["wet"].items())
             + f"; total {sum(v['wet_ft2'] for v in r['wet'].values()):.0f} ft2.\n")
    L.append("**Model assumptions** (grade E unless a source is named):\n")
    for a in r["assumptions"]:
        L.append(f"- {a}")
    L.append("")
    if r["calibration"]:
        L.append("**Published points against the raw build-up** (drag factor 1.00):\n")
        L.append(CAL_HDR)
        L += calib_rows(r)
        L.append("")
    L.append(f"**Drag factor used: {r['drag_factor']:.2f}** ({r['k_basis']}; fleet "
             f"calibration 1.29, range 1.16-1.36). Optimistic bound: {r['k_alt']:.2f}.\n")
    cond = b["cond"]
    L.append(f"**Drag build-up at {cond['alt_ft']:,} ft, {cond['hp']} hp, "
             f"{cond.get('W', 0):,.0f} lb, with the factor applied:** "
             f"{b['ktas']:.0f} KTAS, CD0 {b['CD0']:.4f} on S = "
             f"{b['Dq_par']/b['CD0']:.1f} ft2, propeller efficiency {b['eta']:.2f}, "
             f"L/D {b['LD']:.1f}.\n")
    L.append("| Item | D/q, ft2 | Basis |\n|---|---|---|")
    for name, dq, note in b["items"]:
        L.append(f"| {name} | {dq:.3f} | {note} |")
    L.append(f"| induced | {b['Dq_ind']:.3f} | Oswald (Raymer 12.48), lift split stated above |")
    L.append("")
    o = r["orig"]
    L.append(f"**Original engine, our numbers:** {o['hp']} hp at {o['alt_ft']:,} ft gives "
             f"{o['ktas']:.0f} KTAS; still-air range on full usable fuel from MTOW "
             f"{o['range_nm_noreserve_fullfuel_mtow']:,.0f} nm (climb allowance "
             f"{o['climb_allowance_lb']:.0f} lb); payload at 1,000 nm "
             f"{f0(o['payload_1000_0'])} lb with no reserve, {f0(o['payload_1000_45'])} lb "
             f"with 45 min.\n")
    L.append(f"**On the Aeromomentum line ({r['am_model']}), our numbers.** Installed-mass change "
             f"{r['am_dmass_lb']:+.0f} lb. The headline useful load takes no credit for a "
             f"lighter engine (CG ballast assumed to eat it); the number in brackets takes "
             f"the full saving and the optimistic drag factor.\n")
    L.append(AM_HDR)
    L.append(am_row("AM-low (critical alt 8,000 ft, assumed)", r, "AM-low"))
    L.append(am_row("AM-high (critical alt 16,000 ft, assumed)", r, "AM-high"))
    L.append("")
    return "\n".join(L)


def main():
    rs = {i: load(i) for i in ORDER if os.path.exists(os.path.join(HERE, "results", i + ".json"))}
    T = ["# Generated tables (report.py)\n", "## Aeromomentum results, all candidates\n", AM_HDR]
    for i, r in rs.items():
        for case in ("AM-low", "AM-high"):
            T.append(am_row(f"{r['name']} [{case}]", r, case))
    T.append("\n## Calibration\n")
    T.append("| Candidate | Matched factor (own points) | Factor used | Basis |\n|---|---|---|---|")
    for i, r in rs.items():
        ko = "-" if r.get("k_own") is None else f"{r['k_own']:.2f}"
        T.append(f"| {r['name']} | {ko} | {r['drag_factor']:.2f} | {r['k_basis']} |")
    open(os.path.join(HERE, "results", "tables.md"), "w").write("\n".join(T) + "\n")
    for i, r in rs.items():
        open(os.path.join(HERE, "results", i + "_stage3.md"), "w").write(stage3(i, r))


if __name__ == "__main__":
    main()
