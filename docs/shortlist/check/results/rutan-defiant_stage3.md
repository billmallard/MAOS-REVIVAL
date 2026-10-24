Model: `docs/shortlist/check/models/rutan-defiant.json`; result: `docs/shortlist/check/results/rutan-defiant.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 228 ft2, Wing 240 ft2, Canard 31 ft2, Winglets 16 ft2; total 515 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 31.4 ft, area 133 ft2 (F, Canard Pusher #38, Model 74); LE sweep 23 deg (E, inferred). Chords not published: root 6.0 ft, tip 2.5 ft (E) close the area. Eppler-type section, 13% t/c assumed (E).
- Canard not published: 20 ft2 (15% of wing, Long-EZ-like ratio), span 13 ft (E). Winglets 2 x 8 ft2, 4.5 ft high (E).
- Fuselage 22.8 ft (Wikipedia, uncited; E), width 4.1 ft (46 in cabin), height 4.3 ft (E). Cowls at both ends.
- Laminar run x_tr: wing and canard 0.30 (moldless glass, Rutan finish), winglets 0.20, fuselage 0.03 (front prop slipstream).
- Fixed mains with pants plus retracted nose: D/q 0.40 ft2 (E). Two updraft cooling installations at factor 1.0 each (Raymer formula is per hp, so it already scales).
- Canard carries 18% of the lift (E, Long-EZ class trim). Two 69 in fixed-pitch props, rear one in the fuselage wake: installation 0.97 (E).
- Published-point weight unstated: 2,800 lb assumed (E).
- Original installed engine mass 616 lb = typical published dry weight x 1.15 for mount, baffles, exhaust and oil cooler (E; per-variant check owed by MANUFACTURING).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 184 | 8,000 | 240 | 17.8 | F | 216 | +17% | 1.55 | 159 | RAF Model 74 brochure, 75% |
| 168 | 9,000 | 176 | 13.9 | F | 193 | +15% | 1.46 | 126 | RAF brochure economy, 55% |
| 175 | 8,000 | 240 | 18 | P | 216 | +23% | 1.78 | 141 | pilot report in N78RA, full throttle (~75%), density alt ~8,000 ft |
| 168 | 6,500 | 208 | 15 | P | 202 | +20% | 1.66 | 131 | same pilot report, 65% |

**Drag factor used: 1.72** (own published points; fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.29.

**Drag build-up at 8,000 ft, 240 hp, 2,800 lb, with the factor applied:** 177 KTAS, CD0 0.0291 on S = 133.0 ft2, propeller efficiency 0.81, L/D 7.9.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.736 | Swet 239.9 ft2, Re 6.9M, Cf 0.00228, FF 1.346, Q 1.00, x_tr 0.30 |
| Canard | 0.121 | Swet 31.1 ft2, Re 2.4M, Cf 0.00284, FF 1.369, Q 1.00, x_tr 0.30 |
| Winglets | 0.064 | Swet 16.0 ft2, Re 2.8M, Cf 0.00305, FF 1.251, Q 1.05, x_tr 0.20 |
| Fuselage | 0.703 | Swet 227.6 ft2, Re 35.7M, Cf 0.00236, FF 1.309, Q 1.00, x_tr 0.03 |
| fixed mains, faired; nose retracted | 0.400 | fixed allowance |
| cooling | 0.120 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.107 | 5% of the rest |
| calibration factor | 1.617 | x1.718 on the build-up (calibration; basis stated above) |
| induced | 0.394 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 200 hp at 9,000 ft gives 167 KTAS; still-air range on full usable fuel from MTOW 1,237 nm (climb allowance 26 lb); payload at 1,000 nm 788 lb with no reserve, 722 lb with 45 min.

**On the Aeromomentum line (2x AM15T), our numbers.** Installed-mass change -8 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | 2x AM15T | 8k | 178 (197) | 1,350 (1,358) | 1,094 | 721 | cannot (709) | 150: 858 / 807 |
| AM-high (critical alt 16,000 ft, assumed) | 2x AM15T | 16k | 190 (212) | 1,350 (1,358) | 1,156 | 747 | 669 (732) | 159: 871 / 821 |
