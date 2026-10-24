Model: `docs/shortlist/check/models/mooney-301.json`; result: `docs/shortlist/check/results/mooney-301.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 293 ft2, Wing 276 ft2, HTail 46 ft2, Fin 28 ft2; total 643 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 36.75 ft, area 150 ft2 (F, Air International 'Airdata File', January 1984, via Wikipedia); NLF(1)-0315. Taper 0.5 assumed (E): root 5.44 ft, tip 2.72 ft.
- Fuselage 29.77 ft (F); width 4.4 ft and height 4.8 ft for a six-seat pressurized cabin: E, ours.
- Tails by volume coefficient (E): horizontal Vh 0.65 -> 26 ft2, vertical Vv 0.045 -> 15.5 ft2.
- Laminar run x_tr: wing 0.20 (NLF section on metal; not credited in full), tails 0.05, fuselage 0.
- Retractable gear: no gear term. LoPresti low-drag cowl: cooling factor 1.0 (E).
- Turbo TIO-540 360 hp flat-rated to 25,000 ft (E). Published-point weight unstated: 3,700 lb assumed (E).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 238 | 17,500 | 270 | 18 | P | 239 | +1% | 1.02 | 266 | Bob Kromer, Mooney test pilot (Mooney Flyer Oct 2012): 235-240 KTAS at 75%, 15,000-20,000 ft |

**Drag factor used: 1.29** (fleet calibration (own points read cleaner than the fleet); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.02.

**Drag build-up at 17,500 ft, 270 hp, 3,700 lb, with the factor applied:** 217 KTAS, CD0 0.0210 on S = 150.0 ft2, propeller efficiency 0.83, L/D 11.0.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 1.008 | Swet 276.1 ft2, Re 6.4M, Cf 0.00258, FF 1.415, Q 1.00, x_tr 0.20 |
| HTail | 0.217 | Swet 45.8 ft2, Re 3.6M, Cf 0.00336, FF 1.342, Q 1.05, x_tr 0.05 |
| Fin | 0.123 | Swet 28.2 ft2, Re 4.6M, Cf 0.00321, FF 1.289, Q 1.05, x_tr 0.05 |
| Fuselage | 0.843 | Swet 292.5 ft2, Re 44.5M, Cf 0.00236, FF 1.220, Q 1.00, x_tr 0.00 |
| cooling | 0.130 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.116 | 5% of the rest |
| calibration factor | 0.707 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.482 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 270 hp at 20,000 ft gives 222 KTAS; still-air range on full usable fuel from MTOW 1,056 nm (climb allowance 55 lb); payload at 1,000 nm 885 lb with no reserve, cannot lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -207 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 176 (193) | 1,452 (1,659) | 1,143 | 922 | 858 (1,107) | 142: 1,015 / 973 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 187 (205) | 1,452 (1,659) | 1,169 | 931 | 867 (1,114) | 146: 1,006 / 964 |
