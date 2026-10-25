Model: `docs/shortlist/check/models/meyers-200d.json`; result: `docs/shortlist/check/results/meyers-200d.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 199 ft2, Wing 298 ft2, HTail 54 ft2, Fin 25 ft2; total 577 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 30.5 ft, area 161.5 ft2 (F, Jane's 1967-68; Davisson 1975). Chords not published: taper 0.5 assumed, giving root 7.06 ft and tip 3.53 ft (E, ours). NACA 23015 root, 4412 tip (Lednicer): t/c 15% / 12%.
- Fuselage length 24.33 ft (F); max width 3.8 ft and height 4.2 ft (E, ours; no cabin dimensions published). Davisson notes skin waviness over the tube cage, protruding screws and a belly air dump: Q 1.05 on the fuselage (E).
- Horizontal tail 30 ft2 (10.5 ft x 2.85 ft) and fin 14 ft2: E, ours, by volume coefficient (Vh about 0.55, Vv 0.04, tail arm 13 ft). No tail dimensions are published.
- Laminar run x_tr: wing 0.15 (NACA 230/44-series on a riveted metal wing, flush riveted on the 200D), tails 0.10, fuselage 0.05.
- Retractable gear with doors: no fixed gear drag.
- Air-cooled IO-520 with conventional nose inlets: cooling factor 1.0.
- Original installed engine mass 480 lb = IO-520 dry about 415 lb x 1.15 (E, ours).
- Published point: AOPA Pilot Dec 1991, N31CC, 178 KTAS at 8,500 ft, full throttle 21.5 in / 2,400 rpm, about 67% (191 hp), 14 gph, two aboard; weight not stated, 2,650 lb assumed (E: fleet-typical 2,100 lb empty + two aboard + most of the fuel).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 178 | 8,500 | 191 | 14 | P | 202 | +13% | 1.41 | 140 | AOPA Pilot Dec 1991 (N31CC, 200D): 21.5 in full throttle / 2,400 rpm, about 67%, two aboard; weight E |

**Drag factor used: 1.41** (own published points; fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.29.

**Drag build-up at 8,500 ft, 191 hp, 2,650 lb, with the factor applied:** 178 KTAS, CD0 0.0192 on S = 161.5 ft2, propeller efficiency 0.83, L/D 9.1.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 1.075 | Swet 298.4 ft2, Re 8.5M, Cf 0.00260, FF 1.386, Q 1.00, x_tr 0.15 |
| HTail | 0.226 | Swet 54.1 ft2, Re 4.4M, Cf 0.00309, FF 1.287, Q 1.05, x_tr 0.10 |
| Fin | 0.098 | Swet 25.0 ft2, Re 5.3M, Cf 0.00299, FF 1.252, Q 1.05, x_tr 0.10 |
| Fuselage | 0.597 | Swet 199.5 ft2, Re 37.7M, Cf 0.00228, FF 1.249, Q 1.05, x_tr 0.05 |
| cooling | 0.096 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.105 | 5% of the rest |
| calibration factor | 0.898 | x1.409 on the build-up (calibration; basis stated above) |
| induced | 0.398 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 185 hp at 8,000 ft gives 174 KTAS; still-air range on full usable fuel from MTOW 857 nm (climb allowance 25 lb); no payload at 1,000 nm from gross weight, with or without a 45 min reserve (the tanks do not hold the fuel).

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -89 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 178 (184) | 1,060 (1,149) | 831 | cannot | cannot (cannot) | 148: 648 / cannot |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 189 (196) | 1,060 (1,149) | 863 | cannot | cannot (cannot) | 155: 652 / cannot |
