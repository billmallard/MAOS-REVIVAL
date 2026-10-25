Model: `docs/shortlist/check/models/lancair-iv-p.json`; result: `docs/shortlist/check/results/lancair-iv-p.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 228 ft2, Wing 176 ft2, HTail 27 ft2, Fin 18 ft2; total 449 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 30.2 ft, area 98 ft2 (F, factory); RXM5-217 root / NACA 64-212 tip (Lednicer). Taper ratio 0.5 assumed (E): root 4.33 ft, tip 2.16 ft.
- Fuselage 25 ft long (F); max width 4.1 ft (46 in cabin + walls) and height 4.4 ft: E, ours.
- Tails sized by volume coefficient (E, Raymer table 6.4 GA single): horizontal Vh 0.65 -> 15.9 ft2, vertical Vv 0.045 -> 10.2 ft2, arm 13 ft.
- Laminar run x_tr: wing 0.25, tails 0.20, fuselage 0.05.
- Retractable gear, doors closed: no gear term; leakage covered by the 5% excrescence line.
- Turbo TSIO-550 flat-rated to 25,000 ft (E). Cooling factor 1.3 for a twin-turbo intercooled installation (E).
- Published-point weight unstated: 3,200 lb assumed (E).
- Original installed engine mass 633 lb = typical published dry weight x 1.15 for mount, baffles, exhaust and oil cooler (E; per-variant check owed by MANUFACTURING).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 278 | 23,000 | 262 | 18 | P | 281 | +1% | 1.03 | 255 | AOPA Pilot Jun 1994, 75%, lean of peak |

**Drag factor used: 1.29** (fleet calibration (own points read cleaner than the fleet); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.03.

**Drag build-up at 23,000 ft, 262 hp, 3,200 lb, with the factor applied:** 255 KTAS, CD0 0.0228 on S = 98.0 ft2, propeller efficiency 0.83, L/D 11.5.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.654 | Swet 176.0 ft2, Re 5.1M, Cf 0.00254, FF 1.462, Q 1.00, x_tr 0.25 |
| HTail | 0.115 | Swet 26.9 ft2, Re 2.9M, Cf 0.00301, FF 1.354, Q 1.05, x_tr 0.20 |
| Fin | 0.071 | Swet 17.9 ft2, Re 3.9M, Cf 0.00283, FF 1.332, Q 1.05, x_tr 0.20 |
| Fuselage | 0.653 | Swet 228.0 ft2, Re 37.7M, Cf 0.00226, FF 1.265, Q 1.00, x_tr 0.05 |
| cooling | 0.154 | Raymer 12.39 x 1.30 |
| leakage+protuberance | 0.082 | 5% of the rest |
| calibration factor | 0.501 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.414 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 262 hp at 20,000 ft gives 248 KTAS; still-air range on full usable fuel from MTOW 1,058 nm (climb allowance 50 lb); payload at 1,000 nm 855 lb with no reserve, cannot lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -242 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 200 (218) | 1,350 (1,592) | 1,136 | 881 | cannot (1,094) | 161: 962 / 920 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 211 (231) | 1,350 (1,592) | 1,155 | 888 | 824 (1,100) | 164: 953 / 911 |
