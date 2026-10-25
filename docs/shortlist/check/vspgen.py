"""Generate an OpenVSP AngelScript from a simplified planform model and run
CompGeom to get wetted areas per component.

Fidelity: a parametric, published-dimension model (spans, chords, t/c,
fuselage length/width/height with a generic station profile). It reproduces
wetted areas to roughly +/-10% on the fuselage and +/-3% on the lifting
surfaces; it is not a lofted reproduction of the real airframe.

Usage: python3 vspgen.py <model.json>   (writes vsp/<id>.vspscript, runs it,
writes vsp/<id>_wet.json)
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONTAINER = "/workspace/analysis/AER-3783"

# Fuselage station profiles: (x/L, width fraction, height fraction, z/Hmax offset)
PROFILES = {
    # tractor single: cowl, cabin, tapering tail cone
    "tractor": [(0.0, 0.25, 0.30), (0.04, 0.70, 0.70), (0.15, 0.95, 0.90),
                (0.30, 1.00, 1.00), (0.45, 0.95, 0.95), (0.62, 0.62, 0.70),
                (0.82, 0.32, 0.45), (1.0, 0.08, 0.20)],
    # canard pusher: pointed nose, cabin aft of mid, engine cowl to a spinner
    "pusher": [(0.0, 0.05, 0.05), (0.08, 0.45, 0.55), (0.25, 0.85, 0.90),
               (0.45, 1.00, 1.00), (0.65, 0.95, 0.90), (0.85, 0.70, 0.65),
               (0.97, 0.35, 0.35), (1.0, 0.20, 0.20)],
    # push-pull centreline twin: cowl at both ends
    "pushpull": [(0.0, 0.30, 0.30), (0.05, 0.75, 0.70), (0.20, 0.95, 0.90),
                 (0.40, 1.00, 1.00), (0.60, 0.95, 0.90), (0.80, 0.75, 0.70),
                 (0.95, 0.40, 0.40), (1.0, 0.22, 0.22)],
    # mid-engine pusher with a tail cone and aft prop (VK-30 class)
    "pusher_tail": [(0.0, 0.10, 0.10), (0.07, 0.60, 0.65), (0.20, 0.95, 0.95),
                    (0.38, 1.00, 1.00), (0.55, 0.85, 0.85), (0.75, 0.50, 0.55),
                    (0.92, 0.25, 0.35), (1.0, 0.12, 0.15)],
}


def wing_block(name, span, croot, ctip, tc_root, tc_tip, sweep=0.0, x=0.0,
               z=0.0, y=0.0, dihedral=0.0, vertical=False, sym=True):
    """span is the full span of the (mirrored) pair, or the height for a fin."""
    semi = span / 2.0 if (sym and not vertical) else span
    s = f'''
    {{
    string g = AddGeom("WING","");
    SetGeomName(g,"{name}");
    SetParmVal(g,"Span","XSec_1",{semi:.4f});
    SetParmVal(g,"Root_Chord","XSec_1",{croot:.4f});
    SetParmVal(g,"Tip_Chord","XSec_1",{ctip:.4f});
    SetParmVal(g,"Sweep","XSec_1",{sweep:.3f});
    SetParmVal(g,"Dihedral","XSec_1",{dihedral:.3f});
    SetParmVal(g,"ThickChord","XSecCurve_0",{tc_root:.4f});
    SetParmVal(g,"ThickChord","XSecCurve_1",{tc_tip:.4f});
    SetParmVal(g,"X_Rel_Location","XForm",{x:.4f});
    SetParmVal(g,"Y_Rel_Location","XForm",{y:.4f});
    SetParmVal(g,"Z_Rel_Location","XForm",{z:.4f});
'''
    if vertical:
        s += '    SetParmVal(g,"X_Rel_Rotation","XForm",90.0);\n'
        if not sym:
            s += '    SetParmVal(g,"Sym_Planar_Flag","Sym",0);\n'
    s += '    Update();\n    }\n'
    return s


def fuse_block(name, length, width, height, profile, x=0.0, z=0.0):
    st = PROFILES[profile]
    s = f'''
    {{
    string g = AddGeom("FUSELAGE","");
    SetGeomName(g,"{name}");
    SetParmVal(g,"Length","Design",{length:.4f});
    SetParmVal(g,"X_Rel_Location","XForm",{x:.4f});
    SetParmVal(g,"Z_Rel_Location","XForm",{z:.4f});
    Update();
    string xs = GetXSecSurf(g,0);
    // grow to {len(st)} stations
    while (GetNumXSec(xs) < {len(st)}) {{ InsertXSec(g, 1, XS_ELLIPSE); Update(); }}
    for (int i=0;i<GetNumXSec(xs);i++) ChangeXSecShape(xs,i,XS_ELLIPSE);
    Update();
'''
    for i, (xf, wf, hf) in enumerate(st):
        s += f'''    {{ string x = GetXSec(xs,{i});
      SetParmVal(GetXSecParm(x,"XLocPercent"),{xf:.4f});
      SetParmVal(GetXSecParm(x,"Ellipse_Width"),{max(wf*width,0.02):.4f});
      SetParmVal(GetXSecParm(x,"Ellipse_Height"),{max(hf*height,0.02):.4f}); }}
'''
    s += '    Update();\n    }\n'
    return s


def build_script(m):
    out = ['void main()\n{']
    f = m["fuselage"]
    out.append(fuse_block("Fuselage", f["length"], f["width"], f["height"],
                          f["profile"]))
    for nac in m.get("nacelles", []):
        out.append(fuse_block(nac["name"], nac["length"], nac["width"],
                              nac["height"], nac.get("profile", "tractor"),
                              x=nac.get("x", 0.0), z=nac.get("z", 0.0)))
    for s in m["surfaces"]:
        out.append(wing_block(s["name"], s["span"], s["croot"], s["ctip"],
                              s["tc_root"], s.get("tc_tip", s["tc_root"]),
                              sweep=s.get("sweep", 0.0), x=s.get("x", 0.0),
                              y=s.get("y", 0.0), z=s.get("z", 0.0),
                              dihedral=s.get("dihedral", 0.0),
                              vertical=s.get("vertical", False),
                              sym=s.get("sym", True)))
    out.append('''
    Update();
    ComputeCompGeom(SET_ALL,false,0);
    string rid = FindLatestResultsID("Comp_Geom");
    array<string> names = GetStringResults(rid,"Comp_Name");
    array<double> wet = GetDoubleResults(rid,"Wet_Area");
    array<double> th = GetDoubleResults(rid,"Theo_Area");
    for (int i=0;i<int(names.size());i++) Print("WET|"+names[i]+"|"+th[i]+"|"+wet[i]);
    WriteVSPFile("''' + CONTAINER + '/vsp/' + m["id"] + '''.vsp3", SET_ALL);
}''')
    return "\n".join(out)


def run(model_path):
    m = json.load(open(model_path))
    os.makedirs(os.path.join(HERE, "vsp"), exist_ok=True)
    sp = os.path.join(HERE, "vsp", m["id"] + ".vspscript")
    open(sp, "w").write(build_script(m))
    r = subprocess.run(["maos", "vspscript", "-script",
                        f"{CONTAINER}/vsp/{m['id']}.vspscript"],
                       capture_output=True, text=True)
    comps = {}
    for line in (r.stdout + r.stderr).splitlines():
        mm = re.search(r"WET\|([^|]+)\|([-\d.eE+]+)\|([-\d.eE+]+)", line)
        if mm:
            name = mm.group(1).strip()
            comps[name] = {"theo_ft2": float(mm.group(2)),
                           "wet_ft2": float(mm.group(3))}
    if not comps:
        sys.exit("CompGeom produced no output:\n" + r.stdout[-2000:] + r.stderr[-2000:])
    json.dump(comps, open(os.path.join(HERE, "vsp", m["id"] + "_wet.json"), "w"),
              indent=1)
    return comps


if __name__ == "__main__":
    print(json.dumps(run(sys.argv[1]), indent=1))
