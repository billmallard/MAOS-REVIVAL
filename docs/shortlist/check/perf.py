"""Independent cruise-performance check: component drag build-up, propeller
efficiency estimate, power lapse, and a stepwise (exact constant-speed)
Breguet range integration.

Methods and their sources (named in every output):
  Skin friction    Raymer, Aircraft Design 6th ed., eq. 12.25/12.27 (turbulent
                   Prandtl-Schlichting with compressibility), Blasius laminar;
                   mixed flow by the equivalent-turbulent-origin shortcut.
  Form factors     Raymer eq. 12.30 (lifting surfaces), 12.31 (fuselage),
                   12.32 (nacelle); cross-checked to Hoerner, Fluid-Dynamic
                   Drag, ch. 6 (streamline bodies) and ch. 8 (interference).
  Cooling drag     Raymer eq. 12.39 (piston engine cooling, well-designed
                   installation), multiplied by an installation factor.
  Induced drag     Oswald efficiency, Raymer eq. 12.48 (straight wings);
                   canard: lift split, each surface its own CL^2/(pi A e).
  Propeller        McCormick actuator-disk ideal efficiency times a profile
                   and swirl factor of 0.85 (McCormick, Aerodynamics of V/STOL
                   Flight, ch. 4; Gudmundsson, General Aviation Aircraft
                   Design, ch. 14), with a further installation factor.
  Power lapse      Gagg-Ferrar for normally aspirated engines; flat-rated to a
                   critical altitude for turbocharged ones, Gagg-Ferrar above.
  Range            Constant-altitude, constant-speed cruise integrated in
                   10 lb fuel steps (the exact form of Breguet for this
                   schedule); BSFC constant.
"""
import math

G0 = 32.174


def atmos(h_ft):
    """ISA: returns (rho slug/ft3, T degR, a ft/s, sigma)."""
    T0, rho0 = 518.67, 0.0023769
    if h_ft <= 36089:
        T = T0 - 0.00356616 * h_ft
        rho = rho0 * (T / T0) ** 4.2559
    else:
        T = 389.97
        rho = 0.00070612 * math.exp(-(h_ft - 36089) / 20806.7)
    a = math.sqrt(1.4 * 1716.49 * T)
    return rho, T, a, rho / rho0


def mu(T):
    """Sutherland viscosity, slug/ft s."""
    return 3.737e-7 * (T / 518.67) ** 1.5 * (518.67 + 198.72) / (T + 198.72)


def cf_turb(Re, M):
    return 0.455 / (math.log10(Re) ** 2.58 * (1 + 0.144 * M * M) ** 0.65)


def cf_lam(Re):
    return 1.328 / math.sqrt(Re)


def cf_mixed(Re, M, xtr):
    """Laminar to x/c = xtr, turbulent behind it (Schlichting-type shortcut)."""
    if xtr <= 0:
        return cf_turb(Re, M)
    Re_tr = max(Re * xtr, 1.0)
    return cf_turb(Re, M) - xtr * (cf_turb(Re_tr, M) - cf_lam(Re_tr))


def ff_surface(tc, xc_max, sweep_deg, M):
    return ((1 + 0.6 / xc_max * tc + 100 * tc ** 4)
            * 1.34 * M ** 0.18 * math.cos(math.radians(sweep_deg)) ** 0.28)


def ff_body(fineness):
    return 0.9 + 5.0 / fineness ** 1.5 + fineness / 400.0


def ff_nacelle(fineness):
    return 1 + 0.35 / fineness


def oswald(A, sweep_deg=0.0):
    if sweep_deg > 30:
        return 4.61 * (1 - 0.045 * A ** 0.68) * math.cos(math.radians(sweep_deg)) ** 0.15 - 3.1
    return 1.78 * (1 - 0.045 * A ** 0.68) - 0.64


def drag_components(m, wet, h_ft, V_fts):
    """Return list of (name, D/q ft2, note) for parasite drag at (h, V)."""
    rho, T, a, sig = atmos(h_ft)
    M = V_fts / a
    nu = mu(T) / rho
    out = []
    for c in m["components"]:
        name = c["name"]
        Sw = c.get("swet", wet.get(c.get("vsp", name), {}).get("wet_ft2"))
        if Sw is None:
            raise KeyError(f"no wetted area for {name}")
        Re = V_fts * c["lref"] / nu
        cf = cf_mixed(Re, M, c.get("xtr", 0.0))
        kind = c["kind"]
        if kind == "surface":
            FF = ff_surface(c["tc"], c.get("xc", 0.3), c.get("sweep_tc", 0.0), M)
        elif kind == "body":
            FF = ff_body(c["lref"] / c["dmax"])
        elif kind == "nacelle":
            FF = ff_nacelle(c["lref"] / c["dmax"])
        else:
            raise ValueError(kind)
        Q = c.get("Q", 1.0)
        out.append((name, cf * FF * Q * Sw,
                    f"Swet {Sw:.1f} ft2, Re {Re/1e6:.1f}M, Cf {cf:.5f}, "
                    f"FF {FF:.3f}, Q {Q:.2f}, x_tr {c.get('xtr', 0.0):.2f}"))
    return out


def parasite_Dq(m, wet, h_ft, V_fts, P_hp):
    """Total parasite D/q in ft2, with breakdown."""
    rho, T, a, sig = atmos(h_ft)
    comps = drag_components(m, wet, h_ft, V_fts)
    geo = sum(d for _, d, _ in comps)
    items = list(comps)
    for name, dq in m.get("fixed_Dq", []):  # gear, struts, etc, D/q ft2
        items.append((name, dq, "fixed allowance"))
    # cooling: Raymer 12.39, hp is the power actually being produced
    cool = m.get("cooling_factor", 1.0) * 4.9e-7 * P_hp * T ** 2 / (sig * V_fts)
    items.append(("cooling", cool,
                  f"Raymer 12.39 x {m.get('cooling_factor', 1.0):.2f}"))
    sub = sum(d for _, d, _ in items)
    exc = m.get("excrescence_frac", 0.05) * sub
    items.append(("leakage+protuberance", exc,
                  f"{m.get('excrescence_frac', 0.05)*100:.0f}% of the rest"))
    k = m.get("drag_factor", 1.0)
    if k != 1.0:
        items.append(("calibration factor", (k - 1.0) * sum(d for _, d, _ in items),
                      f"x{k:.3f} on the build-up (calibration; basis stated above)"))
    return sum(d for _, d, _ in items), items


def induced_Dq(m, W_lb, h_ft, V_fts):
    rho, T, a, sig = atmos(h_ft)
    q = 0.5 * rho * V_fts ** 2
    L = W_lb
    total = 0.0
    for s in m["lifting"]:  # each: area, AR, share of lift, e (optional)
        Ls = L * s["share"]
        CL = Ls / (q * s["S"])
        e = s.get("e", oswald(s["AR"], s.get("sweep", 0.0)))
        total += CL ** 2 / (math.pi * s["AR"] * e) * s["S"]
    return total


def prop_eff(m, T_lb, h_ft, V_fts):
    rho, _, _, _ = atmos(h_ft)
    D = m["prop"]["diameter_ft"]
    A = math.pi * D * D / 4 * (1 - m["prop"].get("hub_frac", 0.15) ** 2)
    Tc = T_lb / (0.5 * rho * V_fts ** 2 * A)
    eta_i = 2.0 / (1.0 + math.sqrt(1.0 + Tc))
    return eta_i * 0.85 * m["prop"].get("install", 1.0) , eta_i


def power_avail(eng, h_ft, frac):
    """Shaft hp at altitude for a throttle fraction of rated power."""
    _, _, _, sig = atmos(h_ft)
    hc = eng.get("crit_alt_ft", 0.0)
    if h_ft <= hc:
        lapse = 1.0
    else:
        _, _, _, sc = atmos(hc)
        r = sig / sc
        lapse = r - (1 - r) / 7.55
    Pmax = eng["hp"] * lapse
    cont = eng.get("cont_hp", eng["hp"])
    return min(frac * eng["hp"], Pmax, cont)


def solve_speed(m, wet, eng, W_lb, h_ft, P_hp, nprops=1):
    """Speed at which eta*P = D*V. Returns dict."""
    rho, _, a, _ = atmos(h_ft)
    lo, hi = 80.0, 700.0
    for _ in range(80):
        V = 0.5 * (lo + hi)
        Dq, _ = parasite_Dq(m, wet, h_ft, V, P_hp)
        Dq += induced_Dq(m, W_lb, h_ft, V)
        D = 0.5 * rho * V * V * Dq
        Tper = D / nprops
        eta, _ = prop_eff(m, Tper, h_ft, V)
        if eta * P_hp * 550 > D * V:
            lo = V
        else:
            hi = V
    V = 0.5 * (lo + hi)
    Dq_p, items = parasite_Dq(m, wet, h_ft, V, P_hp)
    Dq_i = induced_Dq(m, W_lb, h_ft, V)
    D = 0.5 * rho * V * V * (Dq_p + Dq_i)
    eta, eta_i = prop_eff(m, D / nprops, h_ft, V)
    return {"V_fts": V, "ktas": V / 1.68781, "Dq_par": Dq_p, "Dq_ind": Dq_i,
            "eta": eta, "eta_i": eta_i, "items": items, "LD": W_lb / D,
            "D_lb": D}


def power_required(m, wet, W_lb, h_ft, V_fts, nprops=1):
    """Shaft hp needed to fly at V. Iterates cooling drag on power."""
    rho, _, _, _ = atmos(h_ft)
    P = 150.0
    for _ in range(30):
        Dq_p, _ = parasite_Dq(m, wet, h_ft, V_fts, P)
        Dq = Dq_p + induced_Dq(m, W_lb, h_ft, V_fts)
        D = 0.5 * rho * V_fts ** 2 * Dq
        eta, _ = prop_eff(m, D / nprops, h_ft, V_fts)
        P = D * V_fts / (eta * 550)
    return P, D


def cruise_range(m, wet, W0, fuel_lb, h_ft, V_fts, bsfc, nprops=1,
                 reserve_min=0.0, step=10.0):
    """Constant-altitude, constant-speed range (nm) on fuel_lb, keeping
    reserve_min of fuel at the end-of-cruise power. Returns (nm, hours,
    avg gph-equivalent lb/h)."""
    W = W0
    burned = 0.0
    dist = 0.0
    t = 0.0
    while True:
        P, _ = power_required(m, wet, W, h_ft, V_fts, nprops)
        ff = bsfc * P  # lb/h
        if reserve_min > 0 and burned + ff * reserve_min / 60.0 >= fuel_lb:
            break
        if burned + step > fuel_lb:
            break
        dt = step / ff
        dist += V_fts / 1.68781 * dt
        t += dt
        burned += step
        W -= step
    return dist, t


def fuel_for(m, wet, W0, dist_nm, h_ft, V_fts, bsfc, nprops=1,
             reserve_min=0.0, step=5.0):
    """Fuel (lb) to fly dist_nm at constant V and h starting at W0, plus a
    reserve of reserve_min at the final power."""
    W = W0
    burned = 0.0
    dist = 0.0
    while dist < dist_nm:
        P, _ = power_required(m, wet, W, h_ft, V_fts, nprops)
        ff = bsfc * P
        dt = step / ff
        dd = V_fts / 1.68781 * dt
        if dist + dd > dist_nm:
            frac = (dist_nm - dist) / dd
            burned += step * frac
            W -= step * frac
            dist = dist_nm
            break
        dist += dd
        burned += step
        W -= step
    P, _ = power_required(m, wet, W, h_ft, V_fts, nprops)
    return burned + bsfc * P * reserve_min / 60.0


def payload_at(m, wet, mtow, empty, dist_nm, h_ft, V_fts, bsfc, fuel_max_lb,
               nprops=1, reserve_min=0.0):
    """Payload (lb) that flies dist_nm at (h, V) from MTOW with the given
    empty weight. Fuel needed is computed starting at MTOW (conservative by
    a few lb when payload is lighter). Returns (payload, fuel) or (None,
    fuel) if the tanks cannot hold it."""
    f = fuel_for(m, wet, mtow, dist_nm, h_ft, V_fts, bsfc, nprops, reserve_min)
    if f > fuel_max_lb:
        return None, f
    return mtow - empty - f, f
