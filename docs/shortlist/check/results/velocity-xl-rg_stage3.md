Model: `docs/shortlist/check/models/velocity-xl-rg.json`; result: `docs/shortlist/check/results/velocity-xl-rg.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 181 ft2, Wing 130 ft2, Strake 102 ft2, Canard 43 ft2, Winglets 25 ft2; total 482 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 34 ft, area 132.5 ft2 incl. strakes (F, factory; Jane's 2013-14 gives 31 ft / 102 ft2, which matches the smaller SE: unresolved). Panels and strakes scaled from the CAFE-measured Cozy by span ratio 1.21 (E).
- Canard 18.67 ft span, 22.8 ft2 (F). Winglets 2 x 12 ft2 (E).
- Fuselage 20 ft (F); width 4.2 ft (47.5 in cabin), height 4.3 ft: E.
- Laminar run as the Cozy. Retractable gear: no gear term. Canard carries 20% of the lift (E).
- Prop 74 in 3-blade constant speed (E; diameter not found). Published-point weight unstated: 2,600 lb assumed (E).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 190 | 3,000 | 232 | 15 | P | 227 | +20% | 1.63 | 142 | GA News 2005 pilot report, factory demonstrator, 75% of 310 hp |

**Drag factor used: 1.63** (own published points; fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.29.

**Drag build-up at 3,000 ft, 232 hp, 2,600 lb, with the factor applied:** 190 KTAS, CD0 0.0211 on S = 132.5 ft2, propeller efficiency 0.83, L/D 7.9.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.384 | Swet 129.6 ft2, Re 6.3M, Cf 0.00218, FF 1.358, Q 1.00, x_tr 0.35 |
| Strake | 0.321 | Swet 102.4 ft2, Re 11.4M, Cf 0.00233, FF 1.279, Q 1.05, x_tr 0.20 |
| Canard | 0.189 | Swet 43.3 ft2, Re 2.3M, Cf 0.00271, FF 1.610, Q 1.00, x_tr 0.35 |
| Winglets | 0.088 | Swet 25.1 ft2, Re 4.4M, Cf 0.00264, FF 1.262, Q 1.05, x_tr 0.25 |
| Fuselage | 0.546 | Swet 181.4 ft2, Re 37.9M, Cf 0.00215, FF 1.402, Q 1.00, x_tr 0.10 |
| cooling | 0.100 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.081 | 5% of the rest |
| calibration factor | 1.083 | x1.633 on the build-up (calibration; basis stated above) |
| induced | 0.160 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 210 hp at 8,000 ft gives 191 KTAS; still-air range on full usable fuel from MTOW 788 nm (climb allowance 24 lb); no payload at 1,000 nm from gross weight, with or without a 45 min reserve (the tanks do not hold the fuel).

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -104 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 186 (203) | 1,000 (1,104) | 825 | cannot | cannot (cannot) | 157: 613 / cannot |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 199 (217) | 1,000 (1,104) | 860 | cannot | cannot (cannot) | 167: 620 / cannot |
