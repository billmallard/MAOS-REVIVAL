"""Propeller-efficiency band for the two designs Bill picked, and the efficiency
each pusher's brochure range needs (AER-5717).

  python3 eta_band.py > eta_band_output.md

Why. Range is linear in installed propeller efficiency (Breguet: R ~ eta L/D /
BSFC), and the stage 3 check carries one eta per design from a formula: the
McCormick actuator-disk ideal, times 0.85 for profile and swirl, times an
installation factor (perf.prop_eff). At cruise that gives 0.79 for the
Prescott (pusher, installation 0.95) and 0.83 for the Aries (tractor). This
holds eta fixed at 0.75 and at 0.85 instead, everything else unchanged, and
reports what moves.

What the 0.75 is and is not. NASA TP-2382 (Yip, 1985, "Wind-Tunnel
Investigation of a Full-Scale Canard-Configured General Aviation Airplane",
NTRS 19850011615, PDF p. 9, "Power Effects", fig. 23) measured a maximum
propeller efficiency of 0.75 on a full-scale VariEze-type pusher in the
Langley 30 x 60 ft tunnel. The report says the propeller "was of low pitch for
maximum climb performance and was therefore not properly matched for cruise
conditions", and that the low value "may also be associated to some degree
with the pusher arrangement". It tests no tractor. So 0.75 is a measured low
end for a mismatched prop on a pusher, used here as the band's low end; it is
NOT a measured pusher penalty, and nothing here cites it as one. 0.85 is the
high end of what a well-matched constant-speed prop reaches installed (the
check's own formula tops out at 0.84 on the cleanest type).

Two readings, because the drag factor and eta are not independent:
  (a) drag held. The drag factor k stays at the stage 3 value and only eta
      moves. This is the band the issue asks for. It is right where the drag
      is known independently of the prop, and it is the WORST case where k
      was matched to a published speed.
  (b) drag re-matched. A published speed at a stated power pins eta / k, not
      either alone (eta P = D V). If eta is really 0.75, the same published
      speed means less drag, and range moves much less. Here k is re-solved at
      each eta so that the reference speed of each basis is unchanged.
The Aries's k comes from its own two AOPA points, so (b) is its honest
reading and (a) a bound. The Prescott's two bases (brochure k 1.35, measured
k 1.55) are each matched to one published speed at an assumed power, so the
same holds, less firmly: the brochure point states no power, the measured
point no altitude.

Inputs: identical to payload_range.py (results/<id>.json drag factors,
prescott/balance.py rebuild weights and both drag bases), AM20T at 195 hp
continuous, critical altitude 8,000 / 16,000 ft and cruise there, BSFC 0.45,
economy 65% of continuous. All our assumptions (E).

Pusher brochure ranges. For each pusher with a stage 3 model, the eta at which
our model, at the design's stage 3 drag factor and its original engine, flies
the published range from gross on standard usable fuel. Generous to the
brochure on purpose: no taxi, climb or descent allowance, only the reserve the
brochure states, and, where the brochure does not state the speed or
altitude, the most favourable of 4,000-12,000 ft at the slowest cruise speed:
the speed the stage 3 model flies at 55% power. A
brochure range that needs more than 0.85 even so is marked optimistic. The
Aries (a tractor) is run the same way as a control.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "prescott"))
import perf  # noqa: E402
from run_check import AM20T, climb_allowance  # noqa: E402
from payload_range import payload, full_tank_range, span, SPEED_FLOOR  # noqa: E402
import balance as B  # noqa: E402

ETAS = (None, 0.75, 0.85)   # None: the stage 3 formula (ideal x 0.85 x installation)
CASES = (("AM-low", 8000.0), ("AM-high", 16000.0))
POWERS = (("continuous", 1.0), ("economy 65%", 0.65))
KT = 1.68781  # ft/s per kt
ETA_OPTIMISTIC = 0.85


def with_eta(m, eta):
    m = json.loads(json.dumps(m))
    if eta is not None:
        m["prop"]["eta_fixed"] = eta
    return m


def eta_label(eta):
    return "stage 3 formula" if eta is None else f"{eta:.2f} fixed"


def rematch_k(m, wet, eng, refs, eta):
    """k at which the model with eta fixed flies each reference point at the
    speed the stage 3 model (formula eta, stage 3 k) flies it; the mean over
    the points, as run_check.py averages a type's own points."""
    ks = []
    for alt, hp, W in refs:
        target = perf.solve_speed(m, wet, eng, W, alt, hp)["ktas"]
        mm = with_eta(m, eta)
        lo, hi = 0.5, 3.0
        for _ in range(40):
            mm["drag_factor"] = 0.5 * (lo + hi)
            v = perf.solve_speed(mm, wet, eng, W, alt, hp)["ktas"]
            lo, hi = (mm["drag_factor"], hi) if v > target else (lo, mm["drag_factor"])
        ks.append(0.5 * (lo + hi))
    return sum(ks) / len(ks)


def am_rows(m, wet, gross, empty, fuel_lb):
    """Per power: KTAS, payload at 1,000 nm (no reserve, 45 min) and full-tank
    range, each spanned over the two engine cases."""
    out = {}
    for power, frac in POWERS:
        recs = []
        for case, h in CASES:
            eng = dict(AM20T, crit_alt_ft=h)
            P = perf.power_avail(eng, h, eng["cont_hp"] / eng["hp"]) * frac
            V = perf.solve_speed(m, wet, eng, 0.92 * gross, h, P)["V_fts"]
            recs.append({"ktas": V / KT,
                         "p0": payload(m, wet, gross, empty, fuel_lb, h, V, 0.45, 1000.0, 0.0),
                         "p45": payload(m, wet, gross, empty, fuel_lb, h, V, 0.45, 1000.0, 45.0),
                         "rng": full_tank_range(m, wet, gross, fuel_lb, h, V, 0.45, 0.0)})
        out[power] = recs
    return out


def orig_range(m, wet, gross, fuel_lb, oc, bsfc):
    """Original engine at its published cruise setting, as run_check.py step 3:
    still air, no reserve, full fuel from gross, taxi and climb allowance."""
    eng = dict(m["engine"])
    sp = perf.solve_speed(m, wet, eng, 0.92 * gross, oc["alt_ft"], oc["hp"])
    clb = climb_allowance(gross, oc["alt_ft"], bsfc=bsfc)
    rng, _ = perf.cruise_range(m, wet, gross - clb, fuel_lb - clb, oc["alt_ft"], sp["V_fts"], bsfc)
    return sp["ktas"], rng


def designs():
    """(key, label, model, wet, gross, empty, fuel_lb, refs, orig) per row.
    refs: the points whose speed reading (b) holds fixed."""
    out = []
    r = json.load(open(os.path.join(HERE, "results", "bellanca-t250-aries.json")))
    m = json.load(open(os.path.join(HERE, "models", "bellanca-t250-aries.json")))
    m["drag_factor"] = r["drag_factor"]
    refs = [(p["alt_ft"], p["hp"], p.get("weight_lb") or 0.9 * m["weights"]["mtow"])
            for p in m["published"] if p.get("alt_ft") is not None and p["grade"] == "P"]
    out.append(("aries", f"Bellanca T-250 Aries (3,150 lb, 1,850 lb empty, 76 gal, k {r['drag_factor']:.2f})",
                m, r["wet"], 3150.0, r["am"]["AM-low"]["empty"], 76 * 6.0, refs, m["orig_cruise"]))
    for gross, gal in ((2400.0, 56.5), (2700.0, 90.0)):
        for end in ("light", "heavy"):
            items = B.rebuilt_empty(end, gross, "nose") + [(-15.0, B.FS["panel"]), (15.0, B.FS["nosebay"])]
            ffs = B.FS["fuel"] if gross == 2400.0 else B.FS["fuel90"]
            ew = sum(w for w, _ in items) + B.ballast_for(items, gross, gal, ffs)
            for bn, k in B.BASES.items():
                mm, wet = B.model_for(gross, k)
                # both bases are matched at the prototype's size and gross; the
                # reference point is flown on the 2,400 lb model, whose k is the same
                refs = [(7500.0, 135.0 if k == 1.35 else 131.0, 2300.0)]
                out.append((f"prescott-{gross:.0f}-{end}-{k}",
                            f"Prescott Pusher, {gross:,.0f} lb, {gal:g} gal, {end} end ({ew:,.0f} lb empty), "
                            f"{bn.split(' (')[0]} (k {k:.2f})",
                            mm, wet, gross, ew, gal * 6.0, refs, None))
    return out


def fmt_cell(recs, key):
    return span([x[key] for x in recs])


def band_table():
    rows = {}
    for key, label, m, wet, gross, empty, fuel_lb, refs, oc in designs():
        m0 = m
        # reading (b) needs the 2,400 lb Prescott model to re-match k; the
        # grown 2,700 lb model then takes the re-matched k
        m_ref, wet_ref = (m0, wet) if not key.startswith("prescott") else B.model_for(2400.0, m0["drag_factor"])
        rows[key] = {"label": label, "a": {}, "b": {}}
        for eta in ETAS:
            ma = with_eta(m0, eta)
            rows[key]["a"][eta] = {"am": am_rows(ma, wet, gross, empty, fuel_lb), "k": m0["drag_factor"]}
            if oc:
                rows[key]["a"][eta]["orig"] = orig_range(ma, wet, gross, fuel_lb, oc, 0.45)
            if eta is None:
                rows[key]["b"][eta] = rows[key]["a"][eta]
                continue
            eng = dict(m0["engine"])
            kb = rematch_k(m_ref, wet_ref, eng, refs, eta)
            mb = with_eta(m0, eta)
            mb["drag_factor"] = kb
            rows[key]["b"][eta] = {"am": am_rows(mb, wet, gross, empty, fuel_lb), "k": kb}
            if oc:
                rows[key]["b"][eta]["orig"] = orig_range(mb, wet, gross, fuel_lb, oc, 0.45)
    return rows


def print_band(rows):
    P = print
    for reading, title in (("a", "Reading (a): drag held at the stage 3 factor, eta moved"),
                           ("b", "Reading (b): drag re-matched so each basis keeps its published reference speed")):
        P(f"## {title}\n")
        P("Each cell spans the two engine cases (critical altitude 8,000 and 16,000 ft, cruising there). "
          "Payload is lb carried 1,000 nm, **no reserve / 45 min reserve**, still air; \"cannot\" means "
          "not even an empty cabin reaches 1,000 nm on full tanks. Range is on full tanks from gross, no reserve.\n")
        P("| Design | eta | k | Continuous: KTAS | Continuous: payload at 1,000 nm | Continuous: range, nm "
          "| Economy 65%: KTAS | Economy: payload at 1,000 nm | Economy: range, nm |")
        P("|---|---|---|---|---|---|---|---|---|")
        for key, r in rows.items():
            for eta in ETAS:
                d = r[reading][eta]
                c, e = d["am"]["continuous"], d["am"]["economy 65%"]
                kt_e = fmt_cell(e, "ktas") + (" (under the floor)" if min(x["ktas"] for x in e) <= SPEED_FLOOR else "")
                P(f"| {r['label']} | {eta_label(eta)} | {d['k']:.2f} | {fmt_cell(c, 'ktas')} "
                  f"| {fmt_cell(c, 'p0')} / {fmt_cell(c, 'p45')} | {fmt_cell(c, 'rng')} "
                  f"| {kt_e} | {fmt_cell(e, 'p0')} / {fmt_cell(e, 'p45')} | {fmt_cell(e, 'rng')} |")
        P("")
    P("## Original engines, at the published cruise setting\n")
    P("Still air, no reserve, full fuel from gross, taxi and climb allowance (run_check.py step 3).\n")
    P("| Design | Setting | eta | Reading (a): KTAS, range nm | Reading (b): KTAS, range nm |")
    P("|---|---|---|---|---|")
    for key, r in rows.items():
        if "orig" not in r["a"][None]:
            continue
        for eta in ETAS:
            a, b = r["a"][eta]["orig"], r["b"][eta]["orig"]
            P(f"| {r['label']} | 250 hp O-540 at 162.5 hp (65%), 8,000 ft | {eta_label(eta)} "
              f"| {a[0]:.0f}, {a[1]:,.0f} | {b[0]:.0f}, {b[1]:,.0f} |")
    P("")


# ---------------------------------------------------- brochure ranges (pushers)
# id: (published range nm, reserve min, stated speed KTAS or None, stated alt ft
#      or None, stated power fraction or None, what the brochure says).
# Each from docs/longlist/candidates.json, where its grade and URL are.
BROCHURE = {
    "cozy-mkiv": (1129.0, 0.0, None, 12000.0, 0.40, "1,300 mi at 40% power, 12,000 ft, reserve not stated"),
    "berkut-360": (1315.0, 30.0, 187.0, None, None, "economy cruise (187 kt at 7.7 gph), 30 min reserve"),
    "velocity-xl-rg": (1150.0, 0.0, None, None, 0.65, "65% power, reserve not stated"),
    "cirrus-vk-30": (1130.0, 0.0, None, None, None, "1,300 mi, conditions not stated"),
    "rutan-defiant": (1128.0, 0.0, None, None, None, "conditions not stated (push-pull twin)"),
    "prescott-pusher": (869.0, 0.0, None, None, None, "1,000 mi, conditions not stated"),
    "bellanca-t250-aries": (1017.0, 45.0, None, None, 0.65,
                            "1,170 mi at economy cruise with 45 min reserve (tractor: control)"),
}
ALTS = (4000.0, 8000.0, 12000.0)
SPEEDS = [100.0 + 5.0 * i for i in range(25)]   # KTAS grid for open conditions


def _range(m, wet, mtow, fuel_lb, bsfc, n, resv, h, V, eta):
    return perf.cruise_range(with_eta(m, eta), wet, mtow, fuel_lb, h, V, bsfc, n, resv)[0]


def _bisect(f, target, lo=0.40, hi=1.30):
    """Smallest eta in [lo, hi] with f(eta) >= target; None if hi falls short."""
    if f(hi) < target:
        return None
    for _ in range(20):
        mid = 0.5 * (lo + hi)
        lo, hi = (lo, mid) if f(mid) >= target else (mid, hi)
    return hi


def eta_needed(i, k=None, lo_frac=0.55):
    """At a fixed speed and a fixed eta, fuel flow scales as 1/eta, so range
    with no reserve scales exactly with eta: a speed and altitude grid flown at
    eta = 1 finds the most favourable condition, and the eta is then solved
    there with the brochure's reserve. lo_frac is the lowest power counted
    as cruise for an open condition (0.55 by default; 0 for any speed on the
    100-220 KTAS grid). With a stated power instead, speed
    moves with eta, so eta is solved directly at that power."""
    rpub, resv, kt, alt, frac, _ = BROCHURE[i]
    r = json.load(open(os.path.join(HERE, "results", i + ".json")))
    m = json.load(open(os.path.join(HERE, "models", i + ".json")))
    m["drag_factor"] = k or r["drag_factor"]
    n = m.get("nprops", 1)
    eng = dict(m["engine"])
    mtow = m["weights"]["mtow"]
    fuel_lb = m["fuel_usable_gal"] * m.get("fuel_density", 6.0)
    bsfc = eng["bsfc"]
    alts = [alt] if alt else ALTS
    best = None
    if frac:
        for h in alts:
            P = perf.power_avail(eng, h, frac) * n
            if P < frac * eng["hp"] * n * 0.999:   # that power is not available at h
                continue
            def f(eta, h=h, P=P):
                V = perf.solve_speed(with_eta(m, eta), wet_of(r), eng, 0.95 * mtow, h, P, n)["V_fts"]
                return _range(m, wet_of(r), mtow, fuel_lb, bsfc, n, resv, h, V, eta)
            e = _bisect(f, rpub)
            if e is not None and (best is None or e < best):
                best = e
        return best, m["drag_factor"]
    cands = []
    for h in alts:
        if kt:
            speeds = [kt * KT]   # a stated speed is taken as flown
        elif lo_frac:
            # open condition: the slowest cruise is the speed the stage 3 model
            # (formula eta) flies at lo_frac power; slower is not cruise. Range
            # at a fixed eta is longest at the slowest speed, so that is the
            # generous end. Judged at the formula eta, not the eta being
            # solved, so a low eta cannot spend the power band on flying slowly.
            P = perf.power_avail(eng, h, lo_frac) * n
            if P < lo_frac * eng["hp"] * n * 0.999:
                continue
            speeds = [perf.solve_speed(m, wet_of(r), eng, 0.95 * mtow, h, P, n)["V_fts"]]
        else:
            speeds = [v * KT for v in SPEEDS]
        for V in speeds:
            r1 = _range(m, wet_of(r), mtow, fuel_lb, bsfc, n, 0.0, h, V, 1.0)
            cands.append((rpub / r1, h, V))
    if not cands:
        return None, m["drag_factor"]
    e0, h, V = min(cands)
    if resv:
        e = _bisect(lambda eta: _range(m, wet_of(r), mtow, fuel_lb, bsfc, n, resv, h, V, eta), rpub)
    else:
        e = e0
    return (None if e is None or e > 1.30 else e), m["drag_factor"]


def wet_of(r):
    return r["wet"]


def print_brochure():
    P = print
    P("## The eta each brochure range needs\n")
    P("Our model on the original engine and standard usable fuel, from gross, no taxi, climb or descent "
      "allowance, and the brochure's own reserve. Where the brochure states a power or a speed, it is flown "
      "at that (at the most favourable of 4,000, 8,000 and 12,000 ft if no altitude is stated). Where it "
      "states neither, the most favourable altitude at the slowest cruise speed, the speed our stage 3 model "
      "flies at 55% power (a fixed eta goes furthest at the slowest speed); the last column drops that floor "
      "(any speed from 100 to 220 KTAS), which shows only that almost any brochure range is reachable "
      "flown slowly enough. Two drag readings: the design's stage 3 factor, and the cleanest type in the "
      f"fleet calibration (k 1.16, the CAFE-measured Express). Above {ETA_OPTIMISTIC:.2f} at the stage 3 "
      "factor: **optimistic**.\n")
    P("| Design | Published range, as stated | Stage 3 k | eta needed at stage 3 k | eta needed at k 1.16 "
      "| Open conditions, any speed, stage 3 k | Reading |")
    P("|---|---|---|---|---|---|---|")
    f = lambda e: "over 1.30" if e is None else f"{e:.2f}"  # noqa: E731
    for i, b in BROCHURE.items():
        e3, k3 = eta_needed(i)
        e16, _ = eta_needed(i, 1.16)
        open_ = b[2] is None and b[4] is None
        eany = f(eta_needed(i, None, 0.0)[0]) if open_ else "-"
        if e3 is not None and e3 <= ETA_OPTIMISTIC:
            verdict = "within the band"
        elif e16 is not None and e16 <= ETA_OPTIMISTIC:
            verdict = "**optimistic** at its own drag; within the band only on the cleanest fleet drag"
        else:
            verdict = "**optimistic** even on the cleanest fleet drag"
        if i == "bellanca-t250-aries":
            verdict += " (tractor control)"
        P(f"| {i} | {b[0]:,.0f} nm: {b[5]} | {k3:.2f} | {f(e3)} | {f(e16)} | {eany} | {verdict} |")
    P("")


def main():
    P = print
    P("# Propeller-efficiency band, Aries and Prescott, and the eta behind pusher brochure ranges (AER-5717)\n")
    P("Generated by `eta_band.py`; method, sources and the TP-2382 citation in its docstring. Every number is "
      "ours (E). Engine assumptions as in the stage 3 check: AM20T 195 hp continuous, BSFC 0.45, none "
      "published by Aeromomentum.\n")
    print_band(band_table())
    print_brochure()


if __name__ == "__main__":
    main()
