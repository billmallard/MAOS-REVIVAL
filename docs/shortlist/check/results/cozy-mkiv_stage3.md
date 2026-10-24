Model: `docs/shortlist/check/models/cozy-mkiv.json`; result: `docs/shortlist/check/results/cozy-mkiv.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 127 ft2, Wing 89 ft2, Strake 73 ft2, Canard 27 ft2, Winglets 20 ft2; total 335 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 28.1 ft, chords 41.5/21 in, LE sweep 23 deg (P, CAFE N494CZ). Strakes (fuel tanks) modelled as a separate inboard surface, 9.5 ft overall span, 7.0/3.5 ft chords (E). CAFE wing area 101.4 ft2 is taken as the reference area (designer figure 88.3 ft2).
- Canard 12.6 ft span, 14.7 ft2, Roncz R1145MS 18.8% t/c (F/P). Winglets 57 in tall (P), 9.5 ft2 each (E).
- Fuselage 16.9 ft (F); width 3.5 ft (39 in cabin + walls), height 3.6 ft: E.
- Laminar run x_tr: wing and canard 0.35 (moldless glass, Eppler 1230 mod), winglets 0.25, fuselage 0.10 (no prop slipstream over it).
- Fixed mains with pants and retracted nose: D/q 0.30 ft2 (E). Canard carries 20% of the lift (E).
- Fixed-pitch 64 in 3-blade wood prop: installation 0.95 (E). CAFE hp is not published: estimated from MP, rpm and density altitude by Gagg-Ferrar at full throttle (E). CAFE says the wing-cuff instrumentation cost about 3 kt.

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 182 | 854 | 174 | 12.9 | R | 205 | +13% | 1.39 | 125 | CAFE measured, WOT 29.2 in/2691 rpm, density alt; hp E |
| 177 | 5,880 | 143 | 10.7 | R | 199 | +12% | 1.36 | 106 | CAFE, WOT 25.1 in/2615 rpm; hp E |
| 177 | 8,021 | 131 | 10.0 | R | 196 | +11% | 1.32 | 101 | CAFE, WOT 23.5 in/2607 rpm, best power; hp E |
| 170 | 12,032 | 112 | 8.2 | R | 190 | +12% | 1.36 | 85 | CAFE, WOT 20.1 in/2545 rpm; hp E |

**Drag factor used: 1.36** (own published points; fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.29.

**Drag build-up at 854 ft, 174 hp, 1,669 lb, with the factor applied:** 184 KTAS, CD0 0.0205 on S = 101.4 ft2, propeller efficiency 0.79, L/D 6.9.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.272 | Swet 88.9 ft2, Re 5.2M, Cf 0.00227, FF 1.348, Q 1.00, x_tr 0.35 |
| Strake | 0.233 | Swet 72.6 ft2, Re 9.7M, Cf 0.00240, FF 1.269, Q 1.05, x_tr 0.20 |
| Canard | 0.117 | Swet 27.0 ft2, Re 2.3M, Cf 0.00273, FF 1.598, Q 1.00, x_tr 0.35 |
| Winglets | 0.070 | Swet 19.7 ft2, Re 3.9M, Cf 0.00271, FF 1.253, Q 1.05, x_tr 0.25 |
| Fuselage | 0.389 | Swet 127.2 ft2, Re 32.7M, Cf 0.00220, FF 1.393, Q 1.00, x_tr 0.10 |
| fixed mains, faired; nose retracted | 0.300 | fixed allowance |
| cooling | 0.075 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.073 | 5% of the rest |
| calibration factor | 0.550 | x1.360 on the build-up (calibration; basis stated above) |
| induced | 0.098 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 131 hp at 8,000 ft gives 175 KTAS; still-air range on full usable fuel from MTOW 829 nm (climb allowance 20 lb); payload at 1,000 nm cannot lb with no reserve, cannot lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change +63 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 202 (206) | 808 (808) | 645 | cannot | cannot (cannot) | 172: cannot / cannot |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 217 (221) | 808 (808) | 668 | cannot | cannot (cannot) | 184: cannot / cannot |
