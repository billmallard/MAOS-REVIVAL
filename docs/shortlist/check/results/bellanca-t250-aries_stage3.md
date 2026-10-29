Model: `docs/shortlist/check/models/bellanca-t250-aries.json`; result: `docs/shortlist/check/results/bellanca-t250-aries.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 235 ft2, Wing 321 ft2, HTail 57 ft2, Fin 25 ft2; total 638 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 31.33 ft, area 170 ft2 (F, AOPA Pilot Mar 1977 spec table; Jane's 1980-81); constant chord 5.43 ft closes the area (E; Plane & Pilot describes a constant-chord wing). NACA 6-series laminar section, 12% t/c (B/F: '60-412' per Lednicer, '600412 modified' per Jane's).
- Fuselage length 26.17 ft (F); max width 4.0 ft and height 4.4 ft from the 45 in cabin width and 48.5 in cabin height plus structure (E, ours). Slab-sided fuselage of flat and single-curve skins, flush riveted (Plane & Pilot): form factor not adjusted.
- T-tail stabilator 28 ft2 (11 ft x 2.55 ft) and swept fin 15 ft2: E, ours, sized by volume coefficient (Vh about 0.5 for a stabilator, Vv 0.04, tail arm 14 ft). No tail dimensions are published.
- Laminar run x_tr: wing 0.25 (flush-riveted metal laminar wing; less credit than a composite), tails 0.15, fuselage 0.05.
- Retractable gear with sealed nose-gear doors and flush main doors: no fixed gear drag.
- Air-cooled O-540 with a single inlet and no cowl flaps (AOPA 1977): cooling factor 1.0 (Raymer 12.39 as-is).
- Original installed engine mass 455 lb = O-540 dry about 395 lb x 1.15 (E, ours; dry weight not taken from the research file, which did not look it up).
- Published points: AOPA's 73% at 6,500 ft (full throttle 22.5 in / 2,300 rpm) and full throttle at 1,000 ft; weights not stated, so 0.9 x MTOW is used. hp: 73% of 250 by AOPA's calculation; 1,000 ft full throttle at Gagg-Ferrar lapse (E).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 181 | 6,500 | 182.5 | - | P | 197 | +9% | 1.26 | 148 | AOPA Pilot flight check Mar 1977, prototype N51AG: 208 mph TAS, 22.5 in full throttle / 2,300 rpm, 73% by AOPA's calculation; 'partially loaded', weight not stated |
| 189 | 1,000 | 242 | - | P | 210 | +11% | 1.34 | 182 | AOPA: 217 mph TAS full throttle, 2,575 rpm, choppy air; hp E (Gagg-Ferrar at 1,000 ft) |

**Drag factor used: 1.30** (own published points; fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.29.

**Drag build-up at 6,500 ft, 182.5 hp, 2,835 lb, with the factor applied:** 179 KTAS, CD0 0.0161 on S = 170.0 ft2, propeller efficiency 0.83, L/D 10.3.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.943 | Swet 320.9 ft2, Re 8.9M, Cf 0.00230, FF 1.276, Q 1.00, x_tr 0.25 |
| HTail | 0.225 | Swet 56.9 ft2, Re 4.2M, Cf 0.00297, FF 1.233, Q 1.08, x_tr 0.15 |
| Fin | 0.093 | Swet 25.4 ft2, Re 5.6M, Cf 0.00281, FF 1.236, Q 1.05, x_tr 0.15 |
| Fuselage | 0.650 | Swet 234.8 ft2, Re 42.8M, Cf 0.00224, FF 1.237, Q 1.00, x_tr 0.05 |
| cooling | 0.088 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.100 | 5% of the rest |
| calibration factor | 0.631 | x1.300 on the build-up (calibration; basis stated above) |
| induced | 0.376 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 162.5 hp at 8,000 ft gives 172 KTAS; still-air range on full usable fuel from MTOW 1,008 nm (climb allowance 25 lb); payload at 1,000 nm 848 lb with no reserve, none with 45 min from gross weight (the tanks do not hold the fuel).

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -64 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 185 (186) | 1,300 (1,364) | 906 | cannot | cannot (cannot) | 154: 901 / 859 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 197 (198) | 1,300 (1,364) | 919 | cannot | cannot (cannot) | 161: 903 / 861 |
