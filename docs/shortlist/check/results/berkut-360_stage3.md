Model: `docs/shortlist/check/models/berkut-360.json`; result: `docs/shortlist/check/results/berkut-360.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 118 ft2, Wing 85 ft2, Strake 62 ft2, Canard 23 ft2, Winglets 17 ft2; total 305 ft2.

**Model assumptions** (grade E unless a source is named):

- Span 26.67 ft and length 18.5 ft (F, Jane's 1993-94 via Wikipedia). Wing area 110 ft2 is unsourced (E, low confidence). Panels and strakes scaled from the CAFE-measured Cozy by span ratio 0.95 (E).
- Tandem two-seat fuselage: width 2.6 ft, height 3.4 ft (E). Canard 12 ft2, 11.5 ft span; winglets 2 x 8 ft2 (E).
- Fully retractable gear: no gear term. Laminar run as the Cozy. Canard carries 20% of the lift (E).
- Prop 66 in constant speed (E). No measured performance exists, so the fleet-median calibration factor applies.

**Drag factor used: 1.29** (fleet calibration (no published point with known power); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.16.

**Drag build-up at 8,000 ft, 150 hp, 1,850 lb, with the factor applied:** 218 KTAS, CD0 0.0126 on S = 110.0 ft2, propeller efficiency 0.84, L/D 9.8.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.271 | Swet 85.1 ft2, Re 5.0M, Cf 0.00228, FF 1.396, Q 1.00, x_tr 0.35 |
| Strake | 0.207 | Swet 62.0 ft2, Re 9.2M, Cf 0.00242, FF 1.315, Q 1.05, x_tr 0.20 |
| Canard | 0.105 | Swet 22.6 ft2, Re 2.0M, Cf 0.00280, FF 1.655, Q 1.00, x_tr 0.35 |
| Winglets | 0.063 | Swet 16.8 ft2, Re 3.5M, Cf 0.00276, FF 1.298, Q 1.05, x_tr 0.25 |
| Fuselage | 0.317 | Swet 118.0 ft2, Re 35.5M, Cf 0.00216, FF 1.242, Q 1.00, x_tr 0.10 |
| cooling | 0.061 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.051 | 5% of the rest |
| calibration factor | 0.312 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.102 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 150 hp at 8,000 ft gives 218 KTAS; still-air range on full usable fuel from MTOW 1,034 nm (climb allowance 20 lb); payload at 1,000 nm 636 lb with no reserve, none with 45 min from gross weight (the tanks do not hold the fuel).

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change +16 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 239 (249) | 949 (949) | 873 | cannot | cannot (cannot) | 205: 650 / 608 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 256 (266) | 949 (949) | 906 | cannot | cannot (cannot) | 218: 658 / 616 |
