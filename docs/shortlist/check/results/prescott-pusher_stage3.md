Model: `docs/shortlist/check/models/prescott-pusher.json`; result: `docs/shortlist/check/results/prescott-pusher.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 167 ft2, Wing 205 ft2, HTail 61 ft2, Fin 29 ft2; total 463 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 29.33 ft, area 110.8 ft2 (F, Tom Prescott's 2007 spec, TP07); root 4.67 ft and tip 3.00 ft (F, RCM 1986 prototype table) scaled 2% to close 110.8 ft2: 4.58 / 2.94 ft. NLF(1)-0215F, 15%, root modified (P, Sport Aviation Mar 1986). Sweep about 10 deg (P).
- Fuselage length 20.28 ft, width 3.67 ft (F, RCM table); height 4.3 ft (E, ours: 42.5 in cabin plus structure; overall height 8 ft 9 in includes the gear and T-tail). Engine in the tail cone, prop on a 12 in extension (P).
- T-tail: horizontal tail 29.3 ft2, 11.0 ft span, root 3.33 ft, tip 2.17 ft (F, RCM prototype table). Fin about 16 ft2 (E, scaled from the 1/5-scale RCM plan).
- Laminar run x_tr: wing 0.25 (NLF section on a flush-riveted metal wing with stretch-formed leading edges; less credit than a composite), tails 0.15, fuselage 0.05.
- Retractable gear (prototype 2 and the retractable kit, P); the fixed-gear kit would add drag (not modelled).
- Cooling factor 1.2 (E): an air-cooled engine buried in a tail cone, with a documented oil-overheat fix and a hot rear cylinder in the field (AOPA 1986; Sport Aviation 1991).
- Prop 65 in (F, factory recommended), installation factor 0.95 for a pusher in the fuselage wake (E, as for the other pushers).
- Original installed engine mass 330 lb = O-360 dry about 285 lb x 1.15 (E).
- No published point states both altitude and power (Kitplanes May 1988: 151 KTAS at 73%, altitude not published; brochure: 165 KTAS at 7,500 ft, power not stated), so the fleet calibration is used and the two points are examined separately (see the dossier).

**Drag factor used: 1.29** (fleet calibration (no published point with known power); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.16.

**Drag build-up at 7,500 ft, 135 hp, 2,300 lb, with the factor applied:** 169 KTAS, CD0 0.0203 on S = 110.8 ft2, propeller efficiency 0.79, L/D 11.3.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.691 | Swet 205.4 ft2, Re 5.7M, Cf 0.00251, FF 1.342, Q 1.00, x_tr 0.25 |
| HTail | 0.246 | Swet 60.7 ft2, Re 4.2M, Cf 0.00297, FF 1.265, Q 1.08, x_tr 0.15 |
| Fin | 0.103 | Swet 29.4 ft2, Re 6.6M, Cf 0.00272, FF 1.224, Q 1.05, x_tr 0.15 |
| Fuselage | 0.532 | Swet 167.0 ft2, Re 30.6M, Cf 0.00236, FF 1.351, Q 1.00, x_tr 0.05 |
| cooling | 0.084 | Raymer 12.39 x 1.20 |
| leakage+protuberance | 0.083 | 5% of the rest |
| calibration factor | 0.505 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.402 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 135 hp at 7,500 ft gives 170 KTAS; still-air range on full usable fuel from MTOW 865 nm (climb allowance 21 lb); payload at 1,000 nm cannot lb with no reserve, cannot lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change +61 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 197 (205) | 789 (789) | 694 | cannot | cannot (cannot) | 166: cannot / cannot |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 210 (219) | 789 (789) | 718 | cannot | cannot (cannot) | 176: cannot / cannot |
