Model: `docs/shortlist/check/models/cirrus-vk-30.json`; result: `docs/shortlist/check/results/cirrus-vk-30.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 239 ft2, Wing 215 ft2, HTail 33 ft2, Fin 27 ft2; total 514 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 38.66 ft, area 120 ft2 (P, AOPA Pilot Apr 1990); NLF(1)-0414F, 14% t/c. Taper 0.5 assumed (E): root 4.14 ft, tip 2.07 ft.
- Fuselage 26 ft (P); max width 4.3 ft (4 ft cabin + walls) and height 4.5 ft: E, ours. Engine buried; prop at tail cone.
- Tails sized by volume coefficient (E): horizontal Vh 0.60 -> 18.6 ft2, vertical (upper + ventral) Vv 0.04 -> 15.5 ft2, arm 12 ft.
- Laminar run x_tr: wing 0.35 (NLF section, builder finish), tails 0.20, fuselage 0.05.
- Retractable gear: no gear term.
- Cooling factor 1.2: buried engine with side scoops and a fan (E). Pusher prop behind the body: no installation penalty or credit (E).
- Published-point weight unstated: 3,300 lb assumed (E).
- Original installed engine mass 512 lb = typical published dry weight x 1.15 for mount, baffles, exhaust and oil cooler (E; per-variant check owed by MANUFACTURING).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 205 | 4,500 | 203 | 15.5 | P | 216 | +5% | 1.15 | 177 | AOPA Pilot Apr 1990, about 70% of 290 hp |
| 211 | 5,000 | 217 | 16.7 | F | 221 | +5% | 1.13 | 192 | spec block, 75%, manufacturer's calculation |

**Drag factor used: 1.29** (fleet calibration (own points read cleaner than the fleet); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.15.

**Drag build-up at 4,500 ft, 203 hp, 3,300 lb, with the factor applied:** 196 KTAS, CD0 0.0183 on S = 120.0 ft2, propeller efficiency 0.83, L/D 11.8.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.637 | Swet 215.1 ft2, Re 6.1M, Cf 0.00220, FF 1.348, Q 1.00, x_tr 0.35 |
| HTail | 0.127 | Swet 33.4 ft2, Re 4.0M, Cf 0.00284, FF 1.276, Q 1.05, x_tr 0.20 |
| Fin | 0.092 | Swet 26.6 ft2, Re 6.1M, Cf 0.00262, FF 1.255, Q 1.05, x_tr 0.20 |
| Fuselage | 0.662 | Swet 239.3 ft2, Re 49.2M, Cf 0.00219, FF 1.263, Q 1.00, x_tr 0.05 |
| cooling | 0.104 | Raymer 12.39 x 1.20 |
| leakage+protuberance | 0.081 | 5% of the rest |
| calibration factor | 0.494 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.255 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 200 hp at 8,000 ft gives 201 KTAS; still-air range on full usable fuel from MTOW 1,206 nm (climb allowance 27 lb); payload at 1,000 nm 874 lb with no reserve, 807 lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -121 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 199 (208) | 1,350 (1,471) | 1,225 | 880 | 815 (954) | 165: 973 / 931 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 212 (221) | 1,350 (1,471) | 1,257 | 890 | 825 (963) | 174: 973 / 930 |
