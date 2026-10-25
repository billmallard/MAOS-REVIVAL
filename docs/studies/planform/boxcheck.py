"""Test of the closed-wing span-efficiency claim with AVL (inviscid): at the
same span and total area (AR 7 on total projected area, 150 ft2), compare
e_inv for an open biplane, a Prandtl box (two unswept wings joined by
vertical tip panels) and a joined wing (swept back/forward, tips meeting),
over gap/span 0.05-0.25. e is referenced to the span and total area, so
e > 1 means less induced drag than the best monoplane of the same span.
Prandtl (NACA TN-182, 1924) predicts about 1.37 for a box at gap/span 0.15.
  python3 boxcheck.py
"""
import math, os, re, subprocess, json
HERE = os.path.dirname(os.path.abspath(__file__))
CONT = "/workspace/analysis/AER-3807"
S, AR = 150.0, 7.0
b = math.sqrt(S * AR); s = b / 2
c = S / 2 / b  # each wing rectangular, half the area

def deck(kind, gb):
    h = gb * b
    surf = lambda name, xr, zr, xt, zt: f"""SURFACE
{name}
8 1.0 24 -2.0
YDUPLICATE
0.0
SECTION
{xr:.4f} 0.0 {zr:.4f} {c:.4f} 0.0
SECTION
{xt:.4f} {s:.4f} {zt:.4f} {c:.4f} 0.0
"""
    head = f"{kind}\n0.2\n0 0 0.0\n{S} {c} {b}\n{c:.4f} 0 0\n0.0\n"
    if kind == "biplane":
        body = surf("Lower", 0, 0, 0, 0) + surf("Upper", 0, h, 0, h)
    elif kind == "box":
        body = surf("Lower", 0, 0, 0, 0) + surf("Upper", 0, h, 0, h) + f"""SURFACE
Tip
8 1.0 10 -2.0
YDUPLICATE
0.0
SECTION
0.0 {s:.4f} 0.0 {c:.4f} 0.0
SECTION
0.0 {s:.4f} {h:.4f} {c:.4f} 0.0
"""
    else:  # joined: front swept back 25 deg, rear swept forward, tips meet
        st = 2 * s * math.tan(math.radians(25))
        body = surf("Front", 0, 0, st / 2, 0) + surf("Rear", st, h, st / 2, 0)
    return head + body

out = {}
for kind in ("biplane", "box", "joined"):
    for gb in (0.05, 0.10, 0.15, 0.20, 0.25):
        name = f"box_{kind}_{int(gb*100)}"
        open(os.path.join(HERE, "avl", name + ".avl"), "w").write(deck(kind, gb))
        lp = os.path.join(HERE, "avl", name + ".ft")
        if os.path.exists(lp): os.remove(lp)
        subprocess.run(["maos", "avl", f"{CONT}/avl/{name}.avl"],
                       input=f"oper\na c 0.5\nx\nft\n{CONT}/avl/{name}.ft\n\nquit\n",
                       capture_output=True, text=True)
        e = float(re.search(r"\be\s*=\s*([-\d.Ee+]+)", open(lp).read()).group(1))
        out[f"{kind} {gb:.2f}"] = e
        print(f"{kind:8s} gap/b {gb:.2f}  e_inv {e:.3f}")
json.dump(out, open(os.path.join(HERE, "results", "boxcheck.json"), "w"), indent=1)
