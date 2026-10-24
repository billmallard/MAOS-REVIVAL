Model: `docs/shortlist/check/models/cessna-p210n.json`; result: `docs/shortlist/check/results/cessna-p210n.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 261 ft2, Wing 320 ft2, HTail 65 ft2, Fin 38 ft2; total 685 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 36.75 ft, area 175 ft2 (P, POH three-view); chords 64/44 in (Wikipedia, consistent with the area); NACA 64A215 / 64A412 (Lednicer).
- Fuselage 28.17 ft (P); width 4.0 ft (44 in cabin + skin) and height 4.8 ft: E, ours.
- Horizontal tail 13 ft span (P) x 2.77 ft mean chord = 36 ft2 (E, Vh ~0.65); fin 19.4 ft2 (E, Vv 0.045).
- Riveted aluminium: laminar run x_tr wing 0.10, tails 0.05, fuselage 0.
- Retractable gear without main gear doors (1979 on): open wells and legs D/q 0.30 ft2 (E). Wing strut-free.
- Turbo TSIO-520-P: 285 hp max continuous (T, TCDS 3A21), flat-rated to 20,000 ft (E). Cooling factor 1.3 (E). BSFC 0.50 at the POH recommended lean (derived from the POH: 19.2 gph at 80% of 285 hp).
- POH points at 4,000 lb, ISA.

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 170 | 10,000 | 222 | 18.0 | P | 189 | +11% | 1.31 | 176 | POH Fig 5-7, 78% |
| 152 | 10,000 | 177 | 13.7 | P | 170 | +12% | 1.32 | 143 | POH, 62% |
| 187 | 20,000 | 228 | 19.2 | P | 206 | +10% | 1.27 | 188 | POH, 80% |
| 176 | 20,000 | 202 | 16.3 | P | 194 | +10% | 1.27 | 169 | POH, 71% |
| 157 | 20,000 | 171 | 13.5 | P | 177 | +13% | 1.32 | 143 | POH, 60% |
| 193 | 23,000 | 231 | 19.2 | P | 212 | +10% | 1.26 | 192 | POH, 81% |
| 171 | 23,000 | 188 | 14.8 | P | 191 | +11% | 1.28 | 159 | POH, 66% |

**Drag factor used: 1.29** (fleet calibration (own points read cleaner than the fleet); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.29.

**Drag build-up at 10,000 ft, 222 hp, 4,000 lb, with the factor applied:** 171 KTAS, CD0 0.0223 on S = 175.0 ft2, propeller efficiency 0.82, L/D 11.5.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 1.205 | Swet 320.0 ft2, Re 6.9M, Cf 0.00285, FF 1.320, Q 1.00, x_tr 0.10 |
| HTail | 0.289 | Swet 65.1 ft2, Re 4.0M, Cf 0.00331, FF 1.279, Q 1.05, x_tr 0.05 |
| Fin | 0.156 | Swet 38.3 ft2, Re 5.2M, Cf 0.00317, FF 1.229, Q 1.05, x_tr 0.05 |
| Fuselage | 0.771 | Swet 261.4 ft2, Re 40.4M, Cf 0.00241, FF 1.225, Q 1.00, x_tr 0.00 |
| retractable gear, no main doors (open wells) | 0.300 | fixed allowance |
| cooling | 0.155 | Raymer 12.39 x 1.30 |
| leakage+protuberance | 0.144 | 5% of the rest |
| calibration factor | 0.876 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.862 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 202 hp at 20,000 ft gives 179 KTAS; still-air range on full usable fuel from MTOW 829 nm (climb allowance 64 lb); payload at 1,000 nm cannot lb with no reserve, cannot lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -161 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 161 (162) | 1,658 (1,819) | 916 | cannot | cannot (cannot) | 130: 1,183 / 1,142 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 171 (171) | 1,658 (1,819) | 931 | cannot | cannot (cannot) | 132: 1,173 / 1,132 |
