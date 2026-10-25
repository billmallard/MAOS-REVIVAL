"""AVL decks for a planform: inviscid vortex-lattice span efficiency and
lift-curve slope (Drela & Youngren, AVL 3.x). Wing alone, mirrored, no
fuselage, no tail: what the planform itself does in potential flow.

Fidelity: inviscid, attached flow, full leading-edge suction. The span
efficiency AVL reports is e_inv (planform only); viscous lift-dependent drag
and fuselage effects are added downstream (planform.py, Kroo 2001 form).
Vortex lift on the deltas is NOT in AVL; it is handled separately (Polhamus).
"""
import math, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CONT = "/workspace/analysis/AER-3807"


def deck(name, S, AR, taper, sweep_le_deg, airfoil="2412", mach=0.25,
         nchord=12, nspan=28):
    b = math.sqrt(S * AR)
    cr = 2 * S / (b * (1 + taper))
    ct = taper * cr
    s = b / 2
    xtip = s * math.tan(math.radians(sweep_le_deg))
    mac = 2 / 3 * cr * (1 + taper + taper ** 2) / (1 + taper)
    # MAC leading edge, for the moment reference (quarter MAC)
    ymac = s / 3 * (1 + 2 * taper) / (1 + taper)
    xref = ymac * math.tan(math.radians(sweep_le_deg)) + 0.25 * mac
    txt = f"""{name}
#Mach
{mach}
#IYsym IZsym Zsym
0 0 0.0
#Sref Cref Bref
{S:.4f} {mac:.4f} {b:.4f}
#Xref Yref Zref
{xref:.4f} 0.0 0.0
#CDp
0.0
SURFACE
Wing
{nchord} 1.0 {nspan} -2.0
YDUPLICATE
0.0
SECTION
0.0 0.0 0.0 {cr:.4f} 0.0
NACA
{airfoil}
SECTION
{xtip:.4f} {s:.4f} 0.0 {ct:.4f} 0.0
NACA
{airfoil}
"""
    return txt, {"b": b, "cr": cr, "ct": ct, "mac": mac, "xref": xref}


def run(name, S, AR, taper, sweep_le_deg, airfoil="2412", mach=0.25):
    txt, g = deck(name, S, AR, taper, sweep_le_deg, airfoil, mach)
    path = os.path.join(HERE, "avl", name + ".avl")
    open(path, "w").write(txt)
    res = {}
    for a in (0.0, 4.0):
        out = os.path.join(HERE, "avl", f"{name}_a{a:g}.ft")
        if os.path.exists(out):
            os.remove(out)
        cmd = f"oper\na a {a}\nx\nft\n{CONT}/avl/{name}_a{a:g}.ft\n\nquit\n"
        r = subprocess.run(["maos", "avl", f"{CONT}/avl/{name}.avl"],
                           input=cmd, capture_output=True, text=True)
        t = open(out).read()
        res[a] = {k: float(re.search(rf"{k}\s*=\s*([-\d.Ee+]+)", t).group(1))
                  for k in ("CLtot", "CDind", "e")}
    cla = (res[4.0]["CLtot"] - res[0.0]["CLtot"]) / math.radians(4.0)
    a0 = -res[0.0]["CLtot"] / cla  # rad
    return dict(g, CLa=cla, alpha0_deg=math.degrees(a0), e_inv=res[4.0]["e"],
                CL4=res[4.0]["CLtot"], CDi4=res[4.0]["CDind"])


if __name__ == "__main__":
    print(run("test_ar8", 150, 8, 0.5, 2.0))
