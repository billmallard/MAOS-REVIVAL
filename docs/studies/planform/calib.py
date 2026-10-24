"""Calibration: AR, wing loading, AVL lift-curve slope and the Pratt gust
response of real designs, on the same basis as the sweep (150 KEAS, 50 ft/s,
12,000 ft density, gross weight). Planforms simplified (graded in the table):
chords not published are assumed from area, span and a stated taper.
  python3 calib.py
"""
import json, math, os, re, subprocess, sys
sys.path.insert(0, "/maos-work/aero/analysis/AER-3783")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import perf, avlgen
HERE = os.path.dirname(os.path.abspath(__file__))
CONT = "/workspace/analysis/AER-3807"

def pratt(W, S, mac, CLa, h=12000.0, V=150.0, U=50.0):
    rho = perf.atmos(h)[0]
    WS = W / S
    mu = 2 * WS / (rho * mac * CLa * 32.174)
    Kg = 0.88 * mu / (5.3 + mu)
    return WS, mu, Kg, Kg * U * V * CLa / (498 * WS)

def cozy():
    """Main wing (88.3 ft2, b 28.1, LE sweep 23, taper 0.5 E) + canard
    (14.7 ft2, b 12.6, rectangular), canard 6 ft above-ahead offset ignored in z.
    Reference area 103.0 ft2 (sum)."""
    b, S, lam = 28.1, 88.3, 0.5
    cr = 2 * S / (b * (1 + lam)); ct = lam * cr
    xt = b / 2 * math.tan(math.radians(23))
    cc = 14.7 / 12.6
    txt = f"""cozy
0.25
0 0 0
103.0 3.3 28.1
10.0 0 0
0.0
SURFACE
Canard
8 1.0 16 -2.0
YDUPLICATE
0.0
SECTION
0 0 0.5 {cc:.4f} 0
NACA
2412
SECTION
0 6.3 0.5 {cc:.4f} 0
NACA
2412
SURFACE
Wing
10 1.0 24 -2.0
YDUPLICATE
0.0
SECTION
9.0 0 0 {cr:.4f} 0
NACA
2412
SECTION
{9.0+xt:.4f} {b/2:.4f} 0 {ct:.4f} 0
NACA
2412
"""
    open(os.path.join(HERE, "avl", "cal_cozy.avl"), "w").write(txt)
    CL = {}
    for a in (0.0, 4.0):
        out = f"{CONT}/avl/cal_cozy_a{a:g}.ft"
        lp = os.path.join(HERE, "avl", f"cal_cozy_a{a:g}.ft")
        if os.path.exists(lp): os.remove(lp)
        subprocess.run(["maos", "avl", f"{CONT}/avl/cal_cozy.avl"],
                       input=f"oper\na a {a}\nx\nft\n{out}\n\nquit\n", capture_output=True, text=True)
        CL[a] = float(re.search(r"CLtot\s*=\s*([-\d.Ee+]+)", open(lp).read()).group(1))
    return (CL[4.0] - CL[0.0]) / math.radians(4), 3.3

CASES = [
 # id, label, b, S, taper, LE sweep, W gross, grade note
 ("prescott", "Prescott Pusher", 29.33, 110.8, 0.6, 2.0, 2400, "b, S, W: designer spec (F, 1000aircraftphotos 6802); taper 0.6 E"),
 ("dyke", "Dyke Delta JD-2", 22.25, 173.0, 0.10, None, 1950, "b, S: Wikipedia / Wainfan PAV table; W 1,950 F; modelled as a straight-TE cropped delta, taper 0.10 E (the real wing is a double delta)"),
 ("facet", "Wainfan Facetmobile FMX-4", 15.0, 214.0, 0.30, None, 740, "b, S, W: Wainfan NASA PAV report 2004 (F); modelled as a cropped delta taper 0.30 E (real: faceted lifting body)"),
]

if __name__ == "__main__":
    rows = []
    for cid, lab, b, S, lam, swp, W, note in CASES:
        AR = b * b / S
        if swp is None:
            swp = math.degrees(math.atan(4 * (1 - lam) / (AR * (1 + lam))))
        a = avlgen.run(f"cal_{cid}", S, AR, lam, swp, "2412" if cid == "prescott" else "0012")
        WS, mu, Kg, dn = pratt(W, S, a["mac"], a["CLa"])
        rows.append(dict(id=cid, label=lab, AR=AR, S=S, b=b, W=W, WS=WS, CLa=a["CLa"], mac=a["mac"],
                         e_inv=a["e_inv"], mu=mu, Kg=Kg, dn=dn, note=note))
    cla, mac = cozy()
    WS, mu, Kg, dn = pratt(2050, 103.0, mac, cla)
    rows.append(dict(id="cozy", label="Cozy MKIV (wing + canard)", AR=28.1**2/88.3, S=103.0, b=28.1, W=2050,
                     WS=WS, CLa=cla, mac=mac, e_inv=None, mu=mu, Kg=Kg, dn=dn,
                     note="main wing 88.3 ft2 + canard 14.7 ft2, b 28.1, W 2,050 (F, cozyaircraft.com); taper 0.5 E; AR is the main wing's"))
    json.dump(rows, open(os.path.join(HERE, "results", "calib.json"), "w"), indent=1)
    for r in rows:
        print(f"{r['label']:28s} AR {r['AR']:5.2f} W/S {r['WS']:5.1f} CLa {r['CLa']:.2f} mu {r['mu']:5.1f} Kg {r['Kg']:.2f} dn50 {r['dn']:.2f} per10 {r['dn']/5:.2f}")
