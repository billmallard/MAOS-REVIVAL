Model: `docs/shortlist/check/models/express-2000.json`; result: `docs/shortlist/check/results/express-2000.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 218 ft2, Wing 239 ft2, HTail 40 ft2, Fin 22 ft2; total 519 ft2.

**Model assumptions** (grade E unless a source is named):

- Geometry for the cruciform-tail Express FT (CAFE N360EZ): wing span 31 ft, area 130.29 ft2, tip chord 37.5 in, NLF(1)-0215F at 15% t/c, length 25.67 ft (P, CAFE). Root chord set to 5.28 ft so the trapezoid closes CAFE's area.
- Fuselage max width 3.9 ft (44 in cabin + walls) and height 4.1 ft: E, ours; the CAFE report gives neither.
- Horizontal tail total 22.4 ft2 (9.33 ft x 2.4 ft, stabilizer 13.14 ft2 per CAFE plus an estimated elevator); fin 12 ft2: E, ours.
- Laminar run x_tr: wing 0.30, tails 0.20, fuselage 0.05 (builder composite finish; NLF(1)-0215F bucket not credited in full).
- Fixed gear, 6.00x6 mains with pants: D/q 0.60 ft2 for three faired wheels and legs (E, Gudmundsson ch. 15 faired-wheel range).
- CAFE powers are not published: hp is estimated from manifold pressure, rpm and density altitude by Gagg-Ferrar (E). Points at full throttle only.
- Original installed engine mass 380 lb = typical published dry weight x 1.15 for mount, baffles, exhaust and oil cooler (E; per-variant check owed by MANUFACTURING).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 169 | 6,190 | 169 | 11.1 | P | 181 | +7% | 1.20 | 144 | CAFE, full throttle 25.4 in/2780 rpm, density alt; hp E (Gagg-Ferrar) |
| 166 | 7,791 | 149 | 10.5 | P | 174 | +5% | 1.13 | 135 | CAFE, 24.1 in/2600 rpm (about full throttle with ram), peak-speed mixture; hp E |
| 153 | 9,813 | 139 | 9.7 | P | 171 | +12% | 1.34 | 110 | CAFE, 21.4 in/2597 rpm (about full throttle); hp E; excluded from calibration: 14 kt slower than the 7,791 ft point for 2,000 ft more altitude, so it was probably not at full throttle and the hp estimate is high |

**Drag factor used: 1.29** (fleet calibration (own points read cleaner than the fleet); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.16.

**Drag build-up at 6,190 ft, 169 hp, 2,885 lb, with the factor applied:** 164 KTAS, CD0 0.0234 on S = 130.3 ft2, propeller efficiency 0.82, L/D 10.5.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.736 | Swet 239.1 ft2, Re 6.5M, Cf 0.00231, FF 1.336, Q 1.00, x_tr 0.30 |
| HTail | 0.145 | Swet 39.8 ft2, Re 3.6M, Cf 0.00290, FF 1.195, Q 1.05, x_tr 0.20 |
| Fin | 0.077 | Swet 22.2 ft2, Re 4.6M, Cf 0.00277, FF 1.193, Q 1.05, x_tr 0.20 |
| Fuselage | 0.606 | Swet 217.7 ft2, Re 39.0M, Cf 0.00227, FF 1.224, Q 1.00, x_tr 0.05 |
| fixed gear, faired | 0.600 | fixed allowance |
| cooling | 0.089 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.113 | 5% of the rest |
| calibration factor | 0.686 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.575 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 150 hp at 8,000 ft gives 160 KTAS; still-air range on full usable fuel from MTOW 1,242 nm (climb allowance 24 lb); payload at 1,000 nm 456 lb with no reserve, 407 lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change +11 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 179 (186) | 890 (890) | 1,062 | 376 | cannot (cannot) | 149: 481 / 439 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 191 (199) | 890 (890) | 1,115 | 393 | cannot (347) | 157: 487 / 445 |
