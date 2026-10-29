Model: `docs/shortlist/check/models/bede-bd-4c-80gal.json`; result: `docs/shortlist/check/results/bede-bd-4c-80gal.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 207 ft2, Wing 204 ft2, HTail 41 ft2, Fin 17 ft2; total 469 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 26.2 ft (F, jimbede.com/bd-4c, read 2026-10-29); area 103.9 ft2 from Bede's published wing loading, 23.10 lb/ft2 at 2,400 lb (F, Bede spec sheet specs-bd-4c.png); constant chord 3.97 ft closes the area (E; the BD-4 wing is a constant-chord panel on a tubular spar). NACA 64-415 modified (F), so t/c 0.15.
- Fuselage length 22.6 ft (F); width 4.2 ft from the 46 in cabin plus structure, height 4.5 ft (E, ours; the 7.23 ft overall height includes gear and fin). The real fuselage is slab-sided (flat sheet on a bolted angle truss); the elliptic-section model understates its wetted area, a sensitivity is run in bede/bede_check.py.
- All-flying stabilator 7.5 ft span x 3.0 ft chord, NACA 63-009 (F, Bede page). Fin 9 ft2 (E, ours: vertical-tail volume 0.04 at a 13 ft arm; no fin dimension is published).
- Laminar run x_tr: wing 0.25 (bonded, rivet-free metal skin on a 6-series section; same credit as the flush-riveted Aries, behind a tractor prop), tails 0.15, fuselage 0.05.
- Fixed tricycle gear with S-ply spring mains and fibreglass spats: D/q 0.60 ft2, the same allowance as the Wheeler Express (E, Gudmundsson ch. 15 faired-wheel range).
- 72 in two-blade propeller (F, Bede's recommendation); installation factor 1.0 (tractor). Air-cooled Lycoming O-360, 180 hp (F, one of Bede's two published columns); original installed mass 328 lb, the same O-360 figure the Cozy model uses (E).
- Bede publishes no cruise altitude, weight or fuel flow, so no published point is usable for calibration: the fleet drag factor is used. Published speeds are compared in bede/bede_check.py at stated altitudes instead.
- Usable fuel 80 gal: the top of Bede's '51 to 80 gallons' capacity, usable not stated (F, an upper bound on usable). Same airframe and weights as the 51 gal model.

**Drag factor used: 1.29** (fleet calibration (no published point with known power); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.16.

**Drag build-up at 8,000 ft, 135 hp, 2,208 lb, with the factor applied:** 155 KTAS, CD0 0.0292 on S = 103.9 ft2, propeller efficiency 0.82, L/D 9.4.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.684 | Swet 203.8 ft2, Re 5.4M, Cf 0.00254, FF 1.322, Q 1.00, x_tr 0.25 |
| HTail | 0.157 | Swet 41.1 ft2, Re 4.1M, Cf 0.00298, FF 1.183, Q 1.08, x_tr 0.15 |
| Fin | 0.068 | Swet 17.4 ft2, Re 3.4M, Cf 0.00309, FF 1.197, Q 1.05, x_tr 0.15 |
| Fuselage | 0.652 | Swet 207.1 ft2, Re 30.8M, Cf 0.00236, FF 1.335, Q 1.00, x_tr 0.05 |
| fixed tricycle gear, spring mains, spats | 0.600 | fixed allowance |
| cooling | 0.078 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.112 | 5% of the rest |
| calibration factor | 0.681 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.658 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 117 hp at 8,000 ft gives 145 KTAS; still-air range on full usable fuel from MTOW 1,249 nm (climb allowance 22 lb); payload at 1,000 nm 765 lb with no reserve, 727 lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change +63 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 180 (187) | 1,087 (1,087) | 927 | cannot | cannot (cannot) | 150: 686 / 645 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 192 (200) | 1,087 (1,087) | 971 | cannot | cannot (cannot) | 159: 696 / 655 |
