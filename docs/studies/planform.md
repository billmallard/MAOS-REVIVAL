# Planform study: high against low aspect ratio, for this mission

**Issue:** AER-3807. **Author:** AERO. **Date:** 2026-10-24. **Status:** first
issue, for the shortlist dossiers to cite.

This study **presents the trade and does not pick a winner.** That is Bill's call.
Every number below names its method and fidelity. Nothing here claims dynamic
stability, spin behaviour or flutter clearance. Where this document talks about
stall and spin, it reports what the flight and accident record says and labels it.

## What it shows, in five lines

1. **At the same touchdown speed, a delta needs two to three times the wing
   area, so its span comes out about the same as a moderate-aspect-ratio wing
   (26-28 ft against 27 ft).** It cruises 12-18 kt slower on the same power, and
   it climbs, glides and ranges worse. Its spar loads are two to five times
   lower.
2. **At the same wing area, a delta is the fastest and shortest point in the
   sweep (187-191 KTAS, 17-21 ft span).** But it touches down at 80-92 kt,
   descends at 1,500-1,900 fpm power-off on approach, and its ceiling drops to
   12,500-16,000 ft.
3. **Induced drag follows span, not aspect ratio.** This is the low-AR school's
   own leading voice speaking (Wainfan, below). Low aspect ratio pays only where
   it buys less wetted area or a lighter structure. At this mission's 180 KTAS,
   induced drag is only 10-20% of cruise drag on the wings that land at 61 kt,
   so that is where the gain or loss sits.
4. **Ride is a wash at equal landing speed.** The delta's low lift-curve slope
   is cancelled by its low wing loading. The real Dyke Delta and Prescott Pusher
   compute the same 0.51 g per 10 ft/s. The delta rides about half as hard only
   at equal wing loading, which is the fast-landing case.
5. **The home-shop trade runs both ways.** High aspect ratio means long, thin,
   highly loaded spars and fittings. Low aspect ratio means low loads but big
   molds: 8-12 router sheets per skin face against 4-5.
6. **A third family, the closed wing (Ligeti Stratos layout), tops the
   efficiency rows:** best L/D 17.8, glide 14.8, a 28,000 ft ceiling and 5.9 ft
   height. But it rides the hardest (0.66 g per 10 ft/s), it has the thinnest
   spars (4 in), and its weight and stall rest on assumptions no flown
   four-seater has tested.

## The fixed mission and what varies

Everything except the wing, and the tail the wing needs, is held fixed. The
differences in the tables are therefore the planform's.

| Fixed | Value | Grade, source |
|---|---|---|
| Seats, useful load | 4 seats, 1,000 lb useful (payload + 75 US gal fuel) | Bill's brief |
| Engine | Aeromomentum AM20T, 260 hp take-off | F, [aeromomentum.com](https://aeromomentum.com/am20t-230hp-300hp/) (read 2026-10-24) |
| Cruise power, altitude | 195 hp (75%) at 12,000 ft; turbo-normalized to 12,000 ft | E, ours. Aeromomentum publishes neither a continuous rating nor a critical altitude, the same assumption as the stage 3 check |
| Fuel burn | BSFC 0.45 lb/hp/h | E |
| Fuselage | 22 ft x 4.0 ft x 4.4 ft four-seat pusher pod, retractable gear | E, ours |
| Propeller | 6.0 ft pusher, the same on every point (no ducted fan) | E |
| Drag calibration | x1.29 on the build-up, the survey's fleet factor | Stage 3 (AER-3783): CAFE Express 1.16, Cessna P210N POH 1.29, CAFE Cozy 1.36 |
| Non-wing empty weight | 1,445 lb, so the AR 6.5 point has an empty fraction of 0.60 at 19 psf | Stage 3 composite four-seat calibration (Cozy 0.575, Express 0.62, CAFE weighed) |
| Structure | normal category, +3.8 g limit, x1.5 ultimate | 14 CFR 23 legacy |

The six planforms:

| Point | AR | Taper | Planform | Tail | t/c root/tip |
|---|---|---|---|---|---|
| AR10 | 10 | 0.45 | straight, glider-like | horizontal + vertical | 0.14 / 0.12 |
| AR8 | 8 | 0.50 | straight, conventional GA | horizontal + vertical | 0.14 / 0.12 |
| AR6.5 | 6.5 | 0.60 | straight, moderate | horizontal + vertical | 0.14 / 0.12 |
| AR4 | 4 | 0.70 | straight, low AR | horizontal + vertical | 0.14 / 0.12 |
| D3 | 3 | 0.15 | cropped delta, straight trailing edge (Rohr-style) | fin only, tailless | 0.10 / 0.10 |
| D2 | 2 | 0.10 | delta, straight trailing edge (Dyke-style) | fin only, tailless | 0.10 / 0.10 |

**How the wing is sized matters more than any other choice in this study.**
So it is run two ways:

- **Rule A, same touchdown speed (the main case).** Each wing is sized to touch
  down at 61 kt at gross weight. That is the old Part 23 single-engine stall
  limit, used here as a proxy for field length and touchdown energy. The usable
  landing lift coefficient is the smaller of CLmax and the lift at a 14 degree
  landing attitude, taken in ground effect. The straight wings have
  single-slotted flaps (CLmax 1.9). The tailless deltas have no flaps, because
  their elevons trim trailing-edge up. A low-aspect-ratio wing reaches its CLmax
  only at an angle the gear and the pusher propeller cannot allow (25-33 degrees
  here), so its area grows instead.
- **Rule B, same wing area (150 sq ft).** This isolates aspect ratio. It is how
  the low-aspect-ratio advantage is usually shown, and it hides the landing cost.

## Methods and their fidelity

| Quantity | Method | Fidelity |
|---|---|---|
| Span efficiency e_inv, lift-curve slope | **AVL 3.x** vortex lattice, wing alone, 12 x 28 panels per side, Mach 0.25 | Inviscid, attached flow, full leading-edge suction. Checked against CDi = CL^2/(pi AR e) |
| Viscous lift-dependent drag | Kroo (2001, *Annu. Rev. Fluid Mech.* 33): e = 1/(1/(e_inv s) + 0.38 CD0 pi AR) | Empirical |
| Delta leading-edge suction | Raymer (6th ed., sec. 12.6): K = S K100 + (1-S)/CLa. Our S schedule: 0.93 up to CL 0.25, 0.70 at CL 0.8, 0.50 at CL 1.2 | **E, ours**, after the shape of Raymer's suction chart. It is the largest single uncertainty on the delta's climb and glide |
| Vortex lift | Polhamus suction analogy (NASA TN D-3767), Kv = pi | Used only for the touchdown bracket (sharp-edge upper bound) |
| Wetted area | **OpenVSP** CompGeom on a parametric model of fuselage, wing and tails | About +/-3% on surfaces, +/-10% on the fuselage. The deltas bury part of the fuselage in the wing root, and CompGeom credits that |
| Parasite drag | Raymer component build-up (stage 3 `perf.py`), Raymer cooling drag x0.8 for a ducted radiator, 5% excrescence, x1.29 fleet factor | Calibrated on three measured types; none is a delta |
| Weights | Raymer eqs. 15.46-15.48 (GA wing and tails), composite factors 0.85/0.83 | Statistical, built on metal airplanes. See the caveat under the verdict |
| Propeller | McCormick actuator disk x 0.85 x installation 0.90 | E |
| Climb, ceiling, range | Excess power; Gagg-Ferrar lapse above 12,000 ft; stepwise constant-power cruise | Exact for the model |
| Ground effect | McCormick: phi = (16h/b)^2 / (1+(16h/b)^2) on AR, wing 3 ft above the ground | Classical |
| Gust | Pratt formula (14 CFR 23.341 as it stood before amendment 23-64, 2017), Ude 50 ft/s, 150 KEAS, 12,000 ft density, mid-cruise weight | Quasi-static discrete gust, rigid airplane. Not a turbulence (PSD) analysis |
| Root bending | Schrenk spanload at 5.7 g ultimate, from the centreline, no inertia relief | Conservative first pass |

XFoil is not used. No inviscid number is presented as viscous: AVL supplies
e_inv and CL_alpha only, and every drag figure adds the viscous terms above.

## Results

Tables are generated by `report.py` from `results/sweep_V.json` (rule A) and
`results/sweep_S.json` (rule B). Every number in them is ours (grade E) from the
methods above.

### Sizing rule A: same touchdown speed (61 kt at gross)

| | AR10 | AR8 | AR6.5 | AR4 | D3 | D2 |
|---|---|---|---|---|---|---|
| Planform | high AR, glider-like | high AR, conventional GA | moderate AR | low AR, straight wing | cropped delta (Rohr-style) | delta (Dyke-style) |
| Aspect ratio | 10.0 | 8.0 | 6.5 | 4.0 | 3.0 | 2.0 |
| Wing area, ft2 | 113 | 112 | 112 | 126 | 255 | 337 |
| Span, ft | 33.7 | 30.0 | 27.0 | 22.4 | 27.6 | 25.9 |
| Root / tip chord, ft | 4.6 / 2.1 | 5.0 / 2.5 | 5.2 / 3.1 | 6.6 / 4.6 | 16.0 / 2.4 | 23.6 / 2.4 |
| LE sweep, deg | 2 | 2 | 2 | 3 | 45 | 59 |
| Tail | H + V tail | H + V tail | H + V tail | H + V tail | fin only (tailless) | fin only (tailless) |
| Gross weight, lb | 2716 | 2684 | 2662 | 2639 | 2738 | 2785 |
| Empty weight, lb | 1716 | 1684 | 1662 | 1639 | 1738 | 1785 |
| Wing + tail weight, lb | 234 + 37 | 202 + 37 | 179 + 38 | 146 + 48 | 265 + 28 | 316 + 24 |
| Wing loading, psf | 23.9 | 23.9 | 23.7 | 21.0 | 10.7 | 8.3 |
| Wetted area total, ft2 | 480 | 476 | 478 | 524 | 701 | 822 |
| of which wing, ft2 | 209 | 205 | 205 | 229 | 478 | 647 |
| AVL e_inv (inviscid) | 0.992 | 0.994 | 0.994 | 0.997 | 1.000 | 1.000 |
| AVL CL_alpha, /rad (inviscid) | 4.98 | 4.71 | 4.41 | 3.65 | 3.08 | 2.34 |

**1. Performance**

| | AR10 | AR8 | AR6.5 | AR4 | D3 | D2 |
|---|---|---|---|---|---|---|
| CD0 (calibrated) | 0.0218 | 0.0217 | 0.0216 | 0.0208 | 0.0113 | 0.0089 |
| Parasite D/q, ft2 | 2.47 | 2.43 | 2.43 | 2.61 | 2.87 | 2.99 |
| Cruise KTAS, 12,000 ft, 195 hp | 194 | 194 | 192 | 182 | 180 | 176 |
| Induced share: climb (SL, Vy) | 60% | 61% | 62% | 65% | 58% | 60% |
| Induced share: cruise | 10% | 12% | 15% | 21% | 16% | 19% |
| Induced share: 45 min reserve (min power) | 70% | 69% | 70% | 70% | 63% | 64% |
| Reserve leg: KEAS / gph | 73 / 4.4 | 77 / 4.9 | 80 / 5.6 | 85 / 7.2 | 85 / 6.4 | 85 / 6.8 |
| Best L/D (KEAS) | 16.7 (96) | 15.3 (101) | 14.0 (105) | 11.5 (112) | 13.2 (106) | 12.5 (104) |
| Rate of climb SL, 260 hp, fpm | 1722 | 1670 | 1603 | 1408 | 1475 | 1397 |
| Rate of climb 12,000 ft, 195 hp, fpm | 1033 | 958 | 870 | 630 | 741 | 669 |
| Service ceiling, ft (100 fpm) | 26,500 | 25,000 | 23,000 | 19,000 | 21,000 | 20,000 |
| Range at 195 hp, no reserve, nm | 996 | 993 | 985 | 934 | 925 | 902 |
| Range at 195 hp, 45 min reserve, nm | 840 | 838 | 830 | 786 | 780 | 760 |
| Range at best-range speed, no reserve, nm (KTAS) | 1544 (111) | 1430 (118) | 1321 (123) | 1090 (130) | 1197 (123) | 1106 (120) |

**2. Storage** (door: small T-hangar 40 ft x 9 ft 5 in, standard 40 ft x 12 ft; 1 ft clearance each side)

| | AR10 | AR8 | AR6.5 | AR4 | D3 | D2 |
|---|---|---|---|---|---|---|
| Span through a 40 ft door | yes (34 ft) | yes (30 ft) | yes (27 ft) | yes (22 ft) | yes (28 ft) | yes (26 ft) |
| Height, ft (E) | 9.4 | 9.1 | 8.9 | 8.8 | 11.0 | 10.6 |
| Under 9 ft 5 in / 12 ft door | yes / yes | yes / yes | yes / yes | yes / yes | no / yes | no / yes |
| Length, ft | 22 | 22 | 22 | 22 | 22 | 25 |
| Plan footprint (span x length), ft2 | 741 | 659 | 594 | 493 | 608 | 659 |
| Trailer (8.5 ft wide): fold | fold aft 12.6 ft panels alongside fuselage | fold aft 10.7 ft panels alongside fuselage | fold aft 9.3 ft panels alongside fuselage | fold aft 7.0 ft panels alongside fuselage | fold up 9.6 ft panels; fin folds too | fold up 8.7 ft panels; fin folds too |

**3. Home-shop build**

| | AR10 | AR8 | AR6.5 | AR4 | D3 | D2 |
|---|---|---|---|---|---|---|
| Half-wing plug bounding box, ft | 16.8 x 4.6 | 15.0 x 5.0 | 13.5 x 5.2 | 11.2 x 6.6 | 16.0 x 13.8 | 23.6 x 13.0 |
| 4x8 router sheets per plug face (Avid PRO4896) | 5 | 4 | 4 | 3 | 8 | 12 |
| 1 m printer tiles per plug face (BigRep ONE) | 12 | 10 | 10 | 8 | 25 | 32 |
| Half-wing mold fits a 24 ft garage | yes | yes | yes | yes | yes | no |
| Root spar depth, in | 7.4 | 8.0 | 8.3 | 10.5 | 18.3 | 26.9 |
| Root bending, ultimate, ft-lb | 56,131 | 49,774 | 45,231 | 37,711 | 43,200 | 40,575 |
| Spar cap force, ultimate, lb | 100,930 | 83,295 | 72,735 | 47,799 | 31,531 | 20,121 |

**4. Safety**

| | AR10 | AR8 | AR6.5 | AR4 | D3 | D2 |
|---|---|---|---|---|---|---|
| Landing CL usable (attitude 14 deg, in ground effect) | 1.90 | 1.90 | 1.88 | 1.67 | 0.85 | 0.66 |
| Limited by | CLmax | CLmax | attitude | attitude | attitude | attitude |
| Touchdown speed at gross, kt | 61 | 61 | 61 | 61 | 61 | 61 |
| same, with full Polhamus vortex lift, kt | 61 | 61 | 61 | 61 | 55 | 54 |
| Alpha for CLmax out of ground effect, deg | 13 | 14 | 15 | 19 | 25 | 33 |
| Power-off approach at 1.3 V_td: L/D | 7.5 | 7.0 | 6.5 | 5.5 | 8.4 | 8.3 |
| Power-off approach sink, fpm | 1071 | 1150 | 1237 | 1454 | 955 | 967 |
| Engine-out glide ratio, prop stopped (KEAS) | 13.5 (92) | 12.4 (96) | 11.4 (100) | 9.6 (106) | 11.1 (101) | 10.7 (98) |

**5. Ride** (Pratt, 150 KEAS at 12,000 ft, mid-cruise weight)

| | AR10 | AR8 | AR6.5 | AR4 | D3 | D2 |
|---|---|---|---|---|---|---|
| Wing loading, psf | 23.9 | 23.9 | 23.7 | 21.0 | 10.7 | 8.3 |
| CL_alpha, /rad | 4.98 | 4.71 | 4.41 | 3.65 | 3.08 | 2.34 |
| Mass ratio mu_g / alleviation K_g | 47.2 / 0.79 | 45.3 / 0.79 | 43.7 / 0.78 | 35.1 / 0.76 | 11.1 / 0.60 | 7.7 / 0.52 |
| Delta n, 50 ft/s design gust | 2.70 | 2.55 | 2.40 | 2.19 | 2.80 | 2.42 |
| Delta n per 10 ft/s (ride) | 0.54 | 0.51 | 0.48 | 0.44 | 0.56 | 0.48 |
| Sharp-edged, no alleviation, 50 ft/s | 3.41 | 3.23 | 3.06 | 2.86 | 4.69 | 4.63 |

### Sizing rule B: same wing area (150 ft2)

| | AR10 | AR8 | AR6.5 | AR4 | D3 | D2 |
|---|---|---|---|---|---|---|
| Planform | high AR, glider-like | high AR, conventional GA | moderate AR | low AR, straight wing | cropped delta (Rohr-style) | delta (Dyke-style) |
| Aspect ratio | 10.0 | 8.0 | 6.5 | 4.0 | 3.0 | 2.0 |
| Wing area, ft2 | 150 | 150 | 150 | 150 | 150 | 150 |
| Span, ft | 38.7 | 34.6 | 31.2 | 24.5 | 21.2 | 17.3 |
| Root / tip chord, ft | 5.3 / 2.4 | 5.8 / 2.9 | 6.0 / 3.6 | 7.2 / 5.0 | 12.3 / 1.8 | 15.7 / 1.6 |
| LE sweep, deg | 2 | 2 | 2 | 3 | 45 | 59 |
| Tail | H + V tail | H + V tail | H + V tail | H + V tail | fin only (tailless) | fin only (tailless) |
| Gross weight, lb | 2792 | 2756 | 2727 | 2674 | 2636 | 2623 |
| Empty weight, lb | 1792 | 1756 | 1727 | 1674 | 1636 | 1623 |
| Wing + tail weight, lb | 293 + 55 | 256 + 56 | 226 + 57 | 168 + 62 | 174 + 17 | 167 + 12 |
| Wing loading, psf | 18.6 | 18.4 | 18.2 | 17.8 | 17.6 | 17.5 |
| Wetted area total, ft2 | 590 | 591 | 594 | 604 | 497 | 462 |
| of which wing, ft2 | 281 | 280 | 279 | 278 | 283 | 271 |
| AVL e_inv (inviscid) | 0.992 | 0.994 | 0.994 | 0.997 | 1.000 | 1.000 |
| AVL CL_alpha, /rad (inviscid) | 4.98 | 4.71 | 4.41 | 3.65 | 3.08 | 2.34 |

**1. Performance**

| | AR10 | AR8 | AR6.5 | AR4 | D3 | D2 |
|---|---|---|---|---|---|---|
| CD0 (calibrated) | 0.0199 | 0.0198 | 0.0197 | 0.0198 | 0.0146 | 0.0130 |
| Parasite D/q, ft2 | 2.98 | 2.96 | 2.96 | 2.96 | 2.19 | 1.95 |
| Cruise KTAS, 12,000 ft, 195 hp | 183 | 183 | 181 | 176 | 191 | 187 |
| Induced share: climb (SL, Vy) | 58% | 60% | 60% | 63% | 60% | 63% |
| Induced share: cruise | 9% | 10% | 12% | 19% | 24% | 37% |
| Induced share: 45 min reserve (min power) | 70% | 69% | 69% | 69% | 63% | 66% |
| Reserve leg: KEAS / gph | 66 / 3.9 | 69 / 4.4 | 72 / 4.9 | 80 / 6.6 | 103 / 8.5 | 112 / 10.5 |
| Best L/D (KEAS) | 17.7 (86) | 16.2 (90) | 14.9 (94) | 11.9 (104) | 11.3 (129) | 10.0 (140) |
| Rate of climb SL, 260 hp, fpm | 1727 | 1692 | 1642 | 1456 | 1262 | 1013 |
| Rate of climb 12,000 ft, 195 hp, fpm | 1072 | 1017 | 947 | 705 | 436 | 131 |
| Service ceiling, ft (100 fpm) | 28,500 | 27,000 | 25,000 | 20,500 | 16,000 | 12,500 |
| Range at 195 hp, no reserve, nm | 940 | 937 | 930 | 905 | 979 | 954 |
| Range at 195 hp, 45 min reserve, nm | 793 | 790 | 785 | 762 | 823 | 800 |
| Range at best-range speed, no reserve, nm (KTAS) | 1575 (101) | 1463 (106) | 1353 (108) | 1105 (120) | 1078 (147) | 961 (161) |

**2. Storage** (door: small T-hangar 40 ft x 9 ft 5 in, standard 40 ft x 12 ft; 1 ft clearance each side)

| | AR10 | AR8 | AR6.5 | AR4 | D3 | D2 |
|---|---|---|---|---|---|---|
| Span through a 40 ft door | no (39 ft) | yes (35 ft) | yes (31 ft) | yes (24 ft) | yes (21 ft) | yes (17 ft) |
| Height, ft (E) | 10.3 | 10.0 | 9.8 | 9.3 | 9.7 | 8.9 |
| Under 9 ft 5 in / 12 ft door | no / yes | no / yes | no / yes | yes / yes | no / yes | yes / yes |
| Length, ft | 22 | 22 | 22 | 22 | 22 | 22 |
| Plan footprint (span x length), ft2 | 852 | 762 | 687 | 539 | 467 | 381 |
| Trailer (8.5 ft wide): fold | fold aft 15.1 ft panels alongside fuselage | fold aft 13.1 ft panels alongside fuselage | fold aft 11.4 ft panels alongside fuselage | fold aft 8.0 ft panels alongside fuselage | fold up 6.4 ft panels; fin folds too | fold up 4.4 ft panels; fin folds too |

**3. Home-shop build**

| | AR10 | AR8 | AR6.5 | AR4 | D3 | D2 |
|---|---|---|---|---|---|---|
| Half-wing plug bounding box, ft | 19.4 x 5.3 | 17.3 x 5.8 | 15.6 x 6.0 | 12.2 x 7.2 | 12.3 x 10.6 | 15.7 x 8.7 |
| 4x8 router sheets per plug face (Avid PRO4896) | 5 | 5 | 4 | 3 | 6 | 6 |
| 1 m printer tiles per plug face (BigRep ONE) | 12 | 12 | 10 | 12 | 16 | 15 |
| Half-wing mold fits a 24 ft garage | yes | yes | yes | yes | yes | yes |
| Root spar depth, in | 8.5 | 9.2 | 9.6 | 11.5 | 14.0 | 18.0 |
| Root bending, ultimate, ft-lb | 66,357 | 59,096 | 53,560 | 41,775 | 31,924 | 25,508 |
| Spar cap force, ultimate, lb | 103,773 | 85,512 | 74,516 | 48,442 | 30,362 | 18,947 |

**4. Safety**

| | AR10 | AR8 | AR6.5 | AR4 | D3 | D2 |
|---|---|---|---|---|---|---|
| Landing CL usable (attitude 14 deg, in ground effect) | 1.90 | 1.90 | 1.90 | 1.68 | 0.82 | 0.61 |
| Limited by | CLmax | CLmax | CLmax | attitude | attitude | attitude |
| Touchdown speed at gross, kt | 54 | 53 | 53 | 56 | 80 | 92 |
| same, with full Polhamus vortex lift, kt | 54 | 53 | 53 | 56 | 72 | 81 |
| Alpha for CLmax out of ground effect, deg | 13 | 14 | 15 | 19 | 25 | 33 |
| Power-off approach at 1.3 V_td: L/D | 8.1 | 7.5 | 7.0 | 5.7 | 7.1 | 6.3 |
| Power-off approach sink, fpm | 876 | 935 | 1006 | 1286 | 1468 | 1908 |
| Engine-out glide ratio, prop stopped (KEAS) | 14.8 (83) | 13.6 (86) | 12.5 (90) | 10.1 (99) | 9.1 (121) | 7.9 (133) |

**5. Ride** (Pratt, 150 KEAS at 12,000 ft, mid-cruise weight)

| | AR10 | AR8 | AR6.5 | AR4 | D3 | D2 |
|---|---|---|---|---|---|---|
| Wing loading, psf | 18.6 | 18.4 | 18.2 | 17.8 | 17.6 | 17.5 |
| CL_alpha, /rad | 4.98 | 4.71 | 4.41 | 3.65 | 3.08 | 2.34 |
| Mass ratio mu_g / alleviation K_g | 32.0 / 0.75 | 30.1 / 0.75 | 29.1 / 0.74 | 27.2 / 0.74 | 23.6 / 0.72 | 24.3 / 0.72 |
| Delta n, 50 ft/s design gust | 3.31 | 3.14 | 2.97 | 2.48 | 2.07 | 1.59 |
| Delta n per 10 ft/s (ride) | 0.66 | 0.63 | 0.59 | 0.50 | 0.41 | 0.32 |
| Sharp-edged, no alleviation, 50 ft/s | 4.38 | 4.20 | 3.98 | 3.37 | 2.88 | 2.20 |

**Reading notes.**

- "Induced share" is induced drag over total drag at each condition. The climb
  is at Vy at sea level on 260 hp. The reserve is flown at minimum-power speed at
  12,000 ft at end-of-cruise weight.
- Range is on 75 US gal at a constant 195 hp, plus the best-range figure
  (maximum speed per horsepower at each weight). A 45 min reserve is flown at
  cruise power, the conservative convention. None of these points reaches
  1,000 nm with a reserve at 195 hp on 75 gal. That is the fixed fuel load, not
  the planform. Every point passes 1,000 nm at best-range speed.
- The engine-out glide includes a stopped fixed-pitch propeller (D/q 1.0 sq ft,
  E). A feathering propeller would add about 1-2 to every glide ratio.
- Height is gear plus fuselage plus 85% of the fin above the top of the
  fuselage (E). The deltas' fins are larger (25-29 sq ft against 11-15 sq ft),
  sized by a volume coefficient of 0.03 on a 0.45-root-chord arm (E, ours).

## A third family: the closed wing (Ligeti Stratos)

Bill asked for the Ligeti Stratos as its own branch. The research is in
[planform/research/stratos.md](planform/research/stratos.md).

**What the Stratos was.** It was a single-seat closed-wing ultralight by
Charles (Karol) Ligeti, a Czechoslovak chemical engineer who came to Australia
in 1977. The S1 prototype first flew on 25 April 1985 and flew about 340 hours,
including Oshkosh in 1986. The low front wing is swept back about 30 degrees and
the high rear wing is straight. Vertical tip fins join them and double as split
rudders and airbrakes. There is no tail, and the ducted fan is a pusher.

Its figures are designer claims or Jane's (F): span 5.36 m, area 7.52-7.53 m2
(AR 3.8 on total area), empty 78 kg, gross 188 kg, cruise about 97 kt, stall
58 km/h, glide 20:1. Its gap/span of about 0.11 is our reading of a 2003
third-party three-view (E). No independent flight test was found.

**Joined wing or box?** The Stratos is a box (Prandtl) system with a swept lower
wing, not a Wolkovitch joined wing. That matters, because the span-efficiency
gain lives in the vertical gap at the tips. AVL on two rectangular wings of equal
span and total area (AR 7, `boxcheck.py`, inviscid) gives:

| Gap / span | 0.05 | 0.10 | 0.15 | 0.20 | 0.25 |
|---|---|---|---|---|---|
| Open biplane | 1.087 | 1.179 | 1.252 | 1.312 | 1.365 |
| Prandtl box (tip panels) | 1.085 | 1.189 | 1.279 | 1.359 | 1.432 |
| Joined wing, no vertical gap at the tips | 0.961 | 0.969 | 0.979 | 0.992 | 1.005 |

A box at gap/span 0.11-0.20 reaches e of 1.2-1.36. The literature agrees:
Prandtl's TN-182 table gives about 1.29 at 0.11 and 1.47 at 0.2 for an optimally
loaded box, and Kroo (1996) gives 1.46 for a box against 1.05 for a diamond
joined wing at gap/span 0.2. A joined wing whose wings meet without a vertical
gap gets almost nothing (0.96-1.0 here). **The "best wing system" claim holds
for a box, not for a joined wing.**

**The mission point.** CW is a Stratos-layout closed wing at AR 7 on total area
and gap/span 0.11, on the same fuselage, engine, calibration and 61 kt sizing as
the sweep (`joined.py`). AVL gives e_inv 1.233. The tip fins replace the fin, and
there is no tail. Assumptions specific to it (E): two-wing landing CLmax 1.45
with plain flaps on the front wing, and Raymer's wing equation on each wing
separately. The tip joint's structural relief and the rear wing's buckling
penalty are not modelled, so the wing weight could move either way. Each wing's
spar load is bounded as a cantilever. Rule B (same area) lands within 1% of rule
A, because rule A's area is already 153 sq ft.

| Rule A, same touchdown speed | CW (closed wing) | AR10 | AR6.5 | D3 |
|---|---|---|---|---|
| AR on total area / span efficiency e_inv (AVL) | 7.0 / 1.233 | 10.0 / 0.992 | 6.5 / 0.994 | 3.0 / 1.000 |
| Wing area, ft2 / span, ft | 153 / 32.7 | 113 / 33.7 | 112 / 27.0 | 255 / 27.6 |
| Gross weight, lb / wing loading, psf | 2796 / 18.3 | 2716 / 23.9 | 2662 / 23.7 | 2738 / 10.7 |
| Wing + tail (or tip-fin) weight, lb | 339 + 13 | 234 + 37 | 179 + 38 | 265 + 28 |
| Wetted area, ft2 | 504 | 480 | 478 | 701 |
| Cruise KTAS, 12,000 ft, 195 hp | 190 | 194 | 192 | 180 |
| Induced share: climb / cruise / reserve | 59% / 9% / 70% | 60% / 10% / 70% | 62% / 15% / 70% | 58% / 16% / 63% |
| Best L/D (KEAS) | 17.8 (91) | 16.7 (96) | 14.0 (105) | 13.2 (106) |
| Climb SL / 12,000 ft, fpm | 1716 / 1058 | 1722 / 1033 | 1603 / 870 | 1475 / 741 |
| Service ceiling, ft | 28,000 | 26,500 | 23,000 | 21,000 |
| Range 195 hp, 0 / 45 min reserve, nm | 973 / 821 | 996 / 840 | 985 / 830 | 925 / 780 |
| Best-range distance, nm | 1593 | 1544 | 1321 | 1197 |
| Height, ft (E) | 5.9 | 9.4 | 8.9 | 11.0 |
| Trailer fold panel length, ft | 12.1 | 12.6 | 9.3 | 9.6 |
| Root spar depth, in | 4.0 | 7.4 | 8.3 | 18.3 |
| Spar-cap force, ultimate, lb | 96,000 per wing, cantilever bound | 100,930 | 72,735 | 31,531 |
| Power-off approach sink, fpm | 901 | 1071 | 1237 | 955 |
| Engine-out glide, prop stopped | 14.8 | 13.5 | 11.4 | 11.1 |
| Delta n per 10 ft/s (Pratt) | 0.66 | 0.54 | 0.48 | 0.56 |

**The closed wing, axis by axis.**
- **Performance:** the best in the study on L/D, climb at altitude, ceiling and
  best range. Cruise speed is 2-4 kt below AR6.5-10, because its wetted area is
  slightly higher.
- **Storage:** the lowest airplane in the study, at 5.9 ft, because no fin is
  needed. Its span (32.7 ft) is close to AR10's. Trailering needs a fold of two
  wings plus the tip fins, a harder mechanism than one wing.
- **Home shop:** four thin panels, about 4 in deep at the root, and an
  over-constrained structure whose loads depend on the joint's stiffness. That
  makes it the hardest of the families to size in a home shop, and the least
  suited to a simple cantilever analysis.
- **Safety:** the best engine-out glide (14.8) and the lowest approach sink. The
  record on its stall is mixed. The prototype was reported to have "no adverse
  flying characteristics". A 1/6-scale wind-tunnel model of NASA's JW-1 joined wing (TM-101083)
  showed an unstable stall and lost lateral stability as the front
  wing stalled.
- **Ride:** the hardest in the study, at 0.66 g per 10 ft/s, because its
  lift-curve slope is high (4.6 per rad) and its wing loading moderate (18 psf).

**The crash, as the record states it.** Charles Ligeti died on 22 September
1987 at Penfield, Victoria, on the first flight of the modified production
Stratos (BASI/ATSB report [198701462](https://www.atsb.gov.au/investigations/198701462)).
**The official record does not blame the closed-wing configuration.** It
contrasts the crashed airframe with the prototype, which "appeared to suffer no
adverse flying characteristics" over about 340 hours. It attributes the
accident, as "likely", to design changes on the production airframe that were
not tested before the flight. Chief among them were full-span elevators on the
front wing, which the report says would sharpen that wing's stall and aggravate
the nose-down pitch. The changes also removed the main wing's dihedral and
lowered the engine and duct. The significant factors listed are that the pilot
"encountered unforeseen circumstances beyond his capabilities" and that the
aircraft was test-flown too low to recover. The report also says it could not
positively determine all the reasons.

**Verdict: the layout itself was not found to be the cause. How the
modifications interacted with it remains undetermined.** A second airframe was
destroyed on its first test flight on 10 July 1988, at Mangalore (ATSB
[198801418](https://www.atsb.gov.au/investigations/198801418)). The cause was
engine power loss, and the record lists "a lack of elevator response" in the
landing attempt as a factor. Read with the pilot's report of near-neutral pitch
stability after the power loss, that suggests a strong coupling between power
and pitch in the lowered-duct layout. That is our reading, not the record's
finding.

**Open source.** The project site (ligetistratos.com) said by November 2007 that the Stratos was
made available as "the first of a complete line of Open Source aircraft". A 2012
page states an intent to "Distribute the plans gratis; at no charge". No licence
or file set was found in the 2006-2013 archived copies. The most recent primary
source cuts the other way. A 2014 LGT Aerospace project paper by Ron Ligeti
([archived](https://web.archive.org/web/20140826172206/http://lgtaerospace.com/attachments/article/15/Stratos%20Project.pdf))
says "The design owner retains the IP" and aims "to induce a licensing
arrangement for production". It also says the original prototype had been in
storage for 20 years. The project domains have lapsed, and the only
public drawings are a 2003 third-party three-view and a French model plan.
Elon's rights work (AER-3805) owns the question. For reconstruction, what is
publicly in hand today is a three-view and published specifications, not
drawings.

## Calibration: real airplanes

### Geometry, wing loading, lift-curve slope and gust response

On the same gust basis as the sweep (150 KEAS, 50 ft/s, 12,000 ft density, gross
weight). Lift-curve slopes are from AVL on simplified planforms (`calib.py`).
Where chords are not published, taper is assumed (E).

| Design | AR | Span, ft | Area, sq ft | Gross, lb | W/S, psf | CL_alpha, /rad (AVL) | mu_g / K_g | Delta n, 50 ft/s | Delta n per 10 ft/s | Basis |
|---|---|---|---|---|---|---|---|---|---|---|
| Prescott Pusher | 7.76 | 29.3 | 111 | 2,400 | 21.7 | 4.65 | 45.6 / 0.79 | 2.55 | 0.51 | b, S, W: designer spec (F, 1000aircraftphotos 6802); taper 0.6 E |
| Dyke Delta JD-2 | 2.86 | 22.2 | 173 | 1,950 | 11.3 | 2.95 | 15.2 / 0.65 | 2.57 | 0.51 | b, S: Wikipedia / Wainfan PAV table; W 1,950 F; modelled as a straight-TE cropped delta, taper 0.10 E (the real wing is a double delta) |
| Wainfan Facetmobile FMX-4 | 1.05 | 15.0 | 214 | 740 | 3.5 | 1.49 | 5.6 / 0.45 | 2.93 | 0.59 | b, S, W: Wainfan NASA PAV report 2004 (F); modelled as a cropped delta taper 0.30 E (real: faceted lifting body) |
| Cozy MKIV (wing + canard) | 8.94 | 28.1 | 103 | 2,050 | 19.9 | 4.40 | 51.7 / 0.80 | 2.66 | 0.53 | main wing 88.3 ft2 + canard 14.7 ft2, b 28.1, W 2,050 (F, cozyaircraft.com); taper 0.5 E; AR is the main wing's |
| Ligeti Stratos (closed wing) | 3.82 | 17.6 | 81 | 414 | 5.1 | 3.81 | 21.6 / 0.71 | 7.92 | 1.58 | b 5.36 m, S 7.52-7.53 m2, gross 188 kg (F, Jane's 1987-88 via Wikipedia); front swept 30 deg, gap/span 0.11 E (Reese 3-view) |
| Rohr 2-175 | not determinable (area not found) | 20 (de Piolenc) or 30 (aerofiles) | not found | 1,450 | - | - | - | - | - | see below |

The Facetmobile and Stratos rows are on the common 150 KEAS basis for comparison
only. At 3.5 and 5.1 psf the formula's numbers are not meaningful for them, and
the airplanes themselves cruised at about 80-97 kt. The Cozy's two official
sources disagree on canard span and total area (12.6 ft and 103.0 sq ft summed,
against 11.5 ft and 101.4 sq ft); the factory figures are used.

**Rohr 2-175.** Its aspect ratio cannot be stated, because no source found gives
its wing area. de Piolenc, relaying the designer's account (TWITT Newsletter,
April 1987; [archived copy](https://web.archive.org/web/20250119003036/https://massflow.archivale.com/2_175.htm)),
gives a 20 ft span forced by a single-car garage, a "deep root chord and sharp
taper", a symmetrical section and no spar, at 1,450 lb gross
([aerofiles](http://www.aerofiles.com/_ro.html), which instead gives a 30 ft
span). If its wing loading were Dyke-like (10-14 psf), a 20 ft span would put its
AR between 2.8 and 3.8 (E, ours), so the D3 point brackets it. The study cannot
check this until a three-view with dimensions is found. The likely sources are
Richard Fraser's book and the TWITT three-view, and both need a purchase.

**Checks the calibration passes.**

- **Straight-wing CLmax.** The Prescott's designer gives a 66 mph full-flap stall
  at 2,400 lb and 110.8 sq ft (F, [1000aircraftphotos 6802](https://1000aircraftphotos.com/Contributions/6802.htm)).
  That implies CLmax 1.95, against the 1.9 assumed for the sweep's straight
  wings.
- **Delta touchdown.** At the Dyke's 11.3 psf, rule A's delta model predicts a
  63 kt touchdown. The Dyke's published stall is 70-75 mph (61-65 kt;
  [Kitplanes, Wanttaja 2025](https://www.kitplanes.com/dyke-delta/), F). Its
  approach is 100-110 mph, about 1.4 Vs ([Wikipedia](https://en.wikipedia.org/wiki/Dyke_Delta),
  which cites *Sport Aviation*, December 2008), where the sweep assumes 1.3. That is
  consistent with the back-side behaviour in the safety record below.
- **Delta wing loading.** Rule A sizes the Rohr-style D3 at 10.7 psf. The Dyke
  flies at 11.3 psf. The sizing rule reproduces what a real four-seat delta
  designer chose.

**What the calibration does not cover.** No delta or low-AR airplane has measured
cruise data with a stated power and altitude in the record found, so the delta
drag polar is not calibrated against flight. The Facetmobile's designer-reported
drag breakdown (total D/q 2.746 sq ft at 4,000 ft, F, NASA grant report below) is
for a 740 lb single-seater and is not scaled here.

### Who the low-aspect-ratio school is today

- **Barnaby Wainfan** is, in practice, the school. He is a Northrop Grumman
  aerodynamicist who wrote Kitplanes' "Wind Tunnel" column until September 2025
  and designed the Facetmobile (AR 1.05, pusher). His case is in the NASA grant
  report he co-wrote (Wainfan and Nieubert, NAG-1-03054 final report, February
  2004, [PDF](https://wainfan.co/media/pavreport.pdf)), his BatRay design (under
  construction, [wainfan.co](https://wainfan.co/)), and his recurring AirVenture
  forum "The Case for Low Aspect Ratio Personal Aircraft" (2025 recording at
  <https://youtu.be/QaGsopdKids>, not reviewed for this study). The claims are
  structural efficiency from a short, deep structure, a low parts count, flat
  panels that suit CNC work, no classical stall, a slow landing from low wing
  loading, and an airframe that "can cost up to 50% less".
- **His own report concedes the trade breaks even:** "the higher structural
  efficiency of the low aspect ratio configuration is just sufficient to
  overcome its aerodynamic disadvantage relative to the conventional airplane"
  (NAG-1-03054, section 5).
- **Bart Verhees** (Belgium) flies tractor deltas (D-Plane 1, more than 1,100
  hours; D2 under development, with folding wings for road transport), per
  [Kitplanes, 19 May 2022](https://www.kitplanes.com/verhees-d2/).
- **The legacy line:** Zimmerman (Vought V-173), Snyder and Hoffman (Arup S-2 and
  S-4), Hatfield (Little Bird), Dyke (JD-1, JD-2), and Mooney at Rohr (2-175).
- **Pushers in the record.** The only low-AR pushers found that actually flew are
  the Rohr 2-175 and the Facetmobile. Every other low-AR design found is a
  tractor. No company is selling a low-AR GA pusher today. The McGinnis Synergy
  is often grouped with this school, but it is not low aspect ratio: 32.4 ft over
  156 sq ft is AR 6.7 (derived from the
  [factory page](https://web.archive.org/web/20191219054836/http://synergyaircraft.com:80/technical-information/)).
  It is a span-efficiency design.
- **The sharpest counter-argument is also Wainfan's.** In "Design Process: Span
  and Aspect Ratio" ([Kitplanes, 14 May 2020](https://www.kitplanes.com/design-process-span-and-aspect-ratio/))
  he writes that "all wings of the same span will generate the same amount of
  induced drag regardless of wing chord, area or aspect ratio", and that "a lot of
  standard T-hangars are 38 feet wide". In other words, the hangar caps span; it
  does not require low aspect ratio. Rule A's numbers bear this out: D3 and AR6.5
  have nearly the same span (27.6 and 27.0 ft) and come within 130 fpm in climb
  and 2,000 ft in ceiling.

### Wainfan's arguments, tested against the sweep

Bill asked for the low-AR case in Wainfan's own words, tested claim by claim.
The quotes below come from his written work and were re-checked against the
fetched sources. His AirVenture talk was not reviewed, and no written claim of
his on ride or on drag at cruise speed was found.

| His claim | Where | What the sweep says | Verdict |
|---|---|---|---|
| Induced drag follows span: "all wings of the same span will generate the same amount of induced drag regardless of wing chord, area or aspect ratio" | Kitplanes, 14 May 2020 | At equal touchdown speed, D3 (27.6 ft) and AR6.5 (27.0 ft) come within 130 fpm in climb and 2,000 ft in ceiling, despite AR 3 against 6.5. D3's remaining deficit is extra wetted area and lost leading-edge suction, not aspect ratio | **Supported** |
| Structural efficiency from a short, deep structure | NAG-1-03054 report; BatRay page ("high structural efficiency") | Spar-cap force is two to five times lower and the root spar two to three times deeper, at either sizing. But Raymer's wing weight is higher for the deltas at equal touchdown speed (265-316 lb against 179-234 lb), because the area grows. It is lower only at equal area (167-174 lb against 226-293 lb) | **Supported on loads; on weight, it depends on the sizing rule** |
| "Outstanding payload fraction" | BatRay page | The sweep's deltas come out at 0.36-0.38, the same as the straight wings. The Dyke's designer figures give 0.46, and his own fit gives 0.47-0.50 at AR 1-3. Raymer's equations are not built to capture this | **Not tested.** This is the study's largest open question |
| No classical stall; vortex lift at high angle of attack | NAG-1-03054 report | The record supports a mushing stall near 30 degrees for AR 1-3 (his Facetmobile, Verhees, NACA free-flight models). It also records roll-control loss on tailless deltas and a high-sink mush on the Dyke. The sweep adds that a delta needs 25-33 degrees for CLmax, which a landing attitude cannot use | **Supported for the stall itself; the landing does not get to use it** |
| A slow landing from low wing loading | NAG-1-03054 report | True only if the area grows two to three times (rule A, 8-11 psf), and that costs 12-18 kt of cruise. At equal area the deltas touch down at 80-92 kt | **Supported, at a cruise-speed price** |
| The structural gain is "just sufficient" to overcome the aerodynamic disadvantage | NAG-1-03054 report, section 5 | At equal touchdown speed the deltas give up 7-9% of cruise speed and 22-28% of best range against AR10. Whether structure buys that back is the open weight question above | **Consistent.** The sweep cannot close it either way |
| Flat panels suit CNC; lower parts count; "can cost up to 50% less" | NAG-1-03054 report | Not modelled here. MANUFACTURING finds that mold area follows wing area, not aspect ratio, and a delta usually carries more area | **Not tested** |
| "a lot of standard T-hangars are 38 feet wide" | Kitplanes, 14 May 2020 | All rule A wings pass a 38 ft door. At equal area only AR10 (38.7 ft) fails | **Supported.** The hangar caps span; it does not require low AR |

Newer designs building on his work: his own BatRay, under construction with a
Jabiru 3300 ([wainfan.co](https://wainfan.co/)). No other was found.

The full research tables, with every source and grade, are in
[planform/research/calibration.md](planform/research/calibration.md) and
[planform/research/safety.md](planform/research/safety.md). Their quotes were
re-checked against the fetched sources by a separate audit
([planform/research/audit.md](planform/research/audit.md)).

## The safety record, beyond the numbers

These are what the flight and accident record says, graded. They are not our
claims about any design's stall or spin behaviour.

| Finding | Source | Grade |
|---|---|---|
| Delta free-flight models at AR 2-3 had "fairly good" stability and control, but very steep power-off glides at high lift coefficient. Models at AR 1 or below were unsatisfactory, through wing rock at high lift or excessive changes in longitudinal stability | McKinney and Drake, NACA RM L7K07 (1948), [NTRS](https://ntrs.nasa.gov/citations/19930085777) | P |
| On the tailless delta model the elevons became "virtually ineffective" at the stall, and the mild roll-off "could not be controlled" | same, model 2 | P |
| The deltas' minimum glide angle sat at a low CL (about 0.3), not near the stall. Above it, elevator response reversed in transient: back-side behaviour that was "very troublesome to the pilot" | same | P |
| Facetmobile (AR 1.05): "No stall: stable mush", about 1,000 fpm sink at full aft stick, no roll-off. Written by the designer under a NASA grant, not an independent test | NAG-1-03054 report | P (designer) |
| Verhees: "The delta wing is not so safe when it comes to stalls"; a plain delta stalls between half span and the tip, giving a wing drop and spin. His D2 counters it with a more elliptical planform | Kitplanes 2022 | F |
| Dyke Delta: the designer told the NTSB the developed stall is a mush "resulting in a high sink rate and temporary loss of control". 4 of about 8 NTSB records found: two loss-of-control (one on a heavily modified airframe, one with wing bonding defects), two landing or gear events. Too few to call a pattern | NTSB LAX96LA003, MIA84FA003, SEA92LA185, 2025 AirVenture event, via [ASN](https://aviation-safety.net/wikibase/41039) | R |
| NASA's light-airplane stall/spin flight program: a low-wing two-place research airplane "tended to roll-off at the stall" (TP-2644). On a low-wing four-place research airplane, an outboard leading-edge droop cut spin entries from 173 of 209 attempts to 13 of 244 (TP-2691) | Stough, Patton and Sliwa, NASA TP-2644 (1987); Stough, DiCarlo and Patton, NASA TP-2691 (1987), [NTRS](https://ntrs.nasa.gov/citations/19870014181) | P |
| Canard pushers: "extremely stall-resistant" at forward CG; at aft CG and high power a deep-stall trim appeared. NTSB records include deep stalls in a Cozy (FTW97LA009) and a Raven (ERA14LA330), both loaded aft of the CG limit | Chambers, Yip and Moul, NASA TM-85760; ASN | P / R |
| Stalls were in 10% of non-commercial GA accidents but nearly 24% of fatalities (2000-2014). Experimental aircraft had 25% of stall accidents on about 5% of flight activity | AOPA Air Safety Institute, via [AOPA 2017](https://www.aopa.org/news-and-media/all-news/2017/september/pilot/number-crunching) and Plane & Pilot 2024 | R (secondary) |
| Published glide ratios: Cirrus SR22 about 8.8 (POH, prop windmilling); Cessna 172 about 9 (FAA rule of thumb); Grob G109B 28; Stemme S10 50. None found for the Cozy, Long-EZ, Dyke or Facetmobile | SR22 POH via [FAASTeam](https://www.faasafety.gov/files/events/SW/SW19/2025/SW19140688/That_Slow_Sinking_Sensation_Resources.pdf); Jane's via Wikipedia | F / E |

**No four-seat delta or low-AR pusher has a stall or spin test record.** The
nearest is the Dyke Delta, a plans-built tractor.

## Verdict, axis by axis

The trade is presented here; the choice is Bill's.

**1. Performance.** **High aspect ratio wins** on climb, ceiling, glide and long
range, at every sizing. At equal touchdown speed AR10 has a best L/D of 16.7
against 12.5-13.2 for the deltas, a ceiling of 26,500 ft against 20,000-21,000,
and a best-range distance of 1,544 nm against 1,106-1,197. **Low aspect ratio
wins cruise speed only at equal wing area.** There, no tail and a fuselage
buried in the wing root cut wetted area by 16-22%, and the deltas reach
187-191 KTAS against 183 for AR10. The price is a ceiling of 12,500-16,000 ft
and induced drag rising to 24-37% of cruise drag. **Moderate aspect ratio (6-7)
is a wash with high AR on cruise speed** (within 2 kt). It gives up 2-3 points of
L/D and about 15% of best range. A low-AR straight wing with a conventional tail
(AR4) is slower than AR6.5 at rule A and slower than the deltas at rule B, and it
trails AR6.5 on climb, glide and range at both. Low AR pays in performance only
when the tail goes too.

**2. Storage.** **The span advantage of low AR is real only if the landing speed
is allowed to rise.** At equal touchdown speed, every point already passes a
40 ft T-hangar door, and the deltas' span (26-28 ft) is no shorter than AR6.5's
(27 ft). Their tall fins (10.6-11.0 ft overall height) then fail a 9 ft 5 in small T-hangar
door unless the fin folds. That is exactly what the Rohr 2-175 did. At equal
wing area the deltas shrink to 17-21 ft and a 380-470 sq ft footprint, which
suits a garage or a shared hangar. AR10 at the same area (38.7 ft) fails a 40 ft
door with a foot each side. Trailering at 8.5 ft wide (23 CFR 658.15) needs a
fold at every point. On the straight wings it means 7-15 ft outer panels folding
back alongside the fuselage. On the deltas it means 4-10 ft panels folding up
over a long centre section, plus the fin. **The low-AR case is better for
folding** (shorter panels, lower loads at the hinge). **High AR is better for
door height.**

**3. Home-shop construction.** **Low AR wins on loads and spar depth. High AR
wins on part size.** At equal touchdown speed the deltas' root spars are 18-27 in
deep against 7-8 in on AR8-10. Their ultimate spar-cap forces are 20,000-32,000 lb
against 83,000-101,000 lb, which allows lighter root fittings and simpler wing
attachment. But a delta half-wing plug is 16-24 ft by 13-14 ft. That is 8-12
sheets on a 4 x 8 ft CNC router per face, and 25-32 tiles on a 1 m-cube printer.
The D2 half-wing mold does not fit a 24 ft garage. A high-AR half-wing is 15-17 ft
by 5 ft: 4-5 router sheets per face, and a single garage holds it. What goes to
a service is similar either way. High AR needs pultruded carbon spar caps sized
for about 100,000 lb, and root fittings at that load want certified bar stock
and heat treatment, even though a Tormach-class mill (18 x 11 in travel) can cut
them. A low-AR wing needs a large infusion table and oven space for one-piece
centre sections. MANUFACTURING's independent desk scaling on AER-3784
(`docs/manufacturing/planform_parts.py`, MAOS-REVIVAL PR #5; E) agrees. From AR10
to the AR2 delta, root spar depth roughly doubles and cap force falls about 4.5
times (109,000 lb to 24,000 lb ultimate, at its own fixed areas). Mold area
follows wing area, not aspect ratio. It adds a limit this study did not test:
female skin molds run 8-14 in deep, so the deltas' molds exceed a 12 in Z-axis
router, while AR 4 and above fit. Plugs stacked from routed slabs avoid the
limit. It also judges that root fittings at AR 8-10 loads belong at a machining
service, while those at AR 4 and below come within a benchtop mill working in
plate, still with inspection. The home-tool envelopes used here are public-spec
assumptions. MANUFACTURING was asked to confirm them.

**4. Safety.** **The record favours low AR on the stall and high AR on the glide
and the approach.**
- **Stall.** The flight record supports a gradual, mushing stall near 30 degrees
  with buffet warning for AR 1-3 (Facetmobile, Verhees D2, NACA free-flight
  models). It also records loss of roll control on tailless deltas at the stall,
  wing drop on plain deltas, and a high-sink mush on the Dyke. The conventional research airplanes in
  NASA's program rolled off at the stall, and an outboard droop cuts spin entry sharply without
  removing it.
- **Engine-out glide.** High AR wins: 13.5 for AR10 against 10.7-11.1 for the
  deltas at equal touchdown speed, and 7.9-9.1 at equal area.
- **Approach.** At equal touchdown speed the deltas' power-off approach sink is
  the lowest in the sweep (about 960 fpm against 1,070-1,450). That is only
  because rule A gave them two to three times the wing area. At equal area it is
  the highest (1,470-1,910 fpm), with 104-119 kt approaches and 80-92 kt
  touchdowns.
- **Landing attitude.** A delta never reaches its CLmax on the runway: it would
  need 25-33 degrees, against the 14 degree attitude limit. A pusher propeller
  at the tail makes that limit hard.

**5. Ride.** **A wash at equal touchdown speed. Low AR rides softer only at
equal wing loading.** At equal touchdown speed the delta's lower lift-curve slope
(2.3-3.1 per rad against 4.4-5.0) is cancelled by its lower wing loading (8-11 psf
against 24). The gust bump is 0.48-0.56 g per 10 ft/s against 0.48-0.54. The two
real airplanes agree: the Dyke Delta and the Prescott Pusher both compute 0.51.
At equal wing area the deltas ride half as hard (0.32-0.41 against 0.59-0.66
g per 10 ft/s), but that is the fast-landing case. Pratt is a quasi-static,
rigid-airplane formula. Dutch roll, pitch damping and the low-frequency ride a
light airplane is known for are outside it.

## What the study does not settle

- **Low-AR structural weight is the largest open question, and it favours low
  AR.** Raymer's equations are fitted to conventional metal wings. Wainfan's fit
  to real low-AR airplanes (NAG-1-03054, eq. 6.4.1.1, small sample, "considerable
  scatter") gives useful-load fractions of 0.47-0.50 at AR 1-3. The Dyke's
  designer figures give 0.46 (890 of 1,950 lb, F). The sweep's deltas come out
  at 0.36-0.38. If a four-seat delta really reached 0.46, it would carry 1,000 lb
  at about 2,200 lb gross, some 550 lb lighter than this study's estimate. That
  would change the performance verdict. **No weighed four-seat delta exists to
  test it.**
- **The delta's leading-edge suction schedule is ours (E).** At climb and
  approach it moves the delta's induced drag by tens of percent. A VSPAERO or
  OpenFOAM run on a rounded-edge delta at CL 0.5-1.0 would replace it.
- **Tailless trim drag and the CG range are not modelled.** Both cost the deltas
  something not shown here.
- **One propulsor throughout.** The Rohr's shrouded fan was a separate choice
  from its planform, and it is not credited or charged here.
- **No stability analysis.** AVL can give the stability derivatives for each
  point, but this study did not run them, and a tailless delta's static margin
  is a design decision this sweep does not make.
- **Rohr 2-175 geometry** is unknown beyond its span (20 ft, or 30 ft per one
  source).

## How the dossiers use this

Each shortlist dossier states its own aspect ratio and wing loading, names the
sweep point nearest to it, and links here. Its own performance check stays in the
dossier. This study supplies the planform trade around it.

## Files

All under [`docs/studies/planform/`](planform/).

| File | What |
|---|---|
| `planform.py` | The sweep: sizing, weights, OpenVSP wetted areas, performance, landing, gust, structure |
| `avlgen.py` | AVL deck generator and runner |
| `calib.py` | Calibration planforms: AVL and Pratt |
| `joined.py`, `boxcheck.py` | The closed-wing point and the Stratos calibration; AVL test of biplane, box and joined-wing span efficiency |
| `report.py` | Tables and storage/shop columns; `--doc` builds this file from `planform.template.md` |
| `perf.py`, `vspgen.py` | Copied unchanged from the stage 3 check (AER-3783) |
| `avl/`, `vsp/` | Every AVL deck and OpenVSP script the tables came from, with CompGeom outputs |
| `results/` | `sweep_V.json`, `sweep_S.json`, `calib.json`, `tables.md` |
| `research/` | Calibration and safety desk research, and the quote audit |

To regenerate, run inside `/maos-work/aero/analysis/AER-3807` with the `maos`
tool containers: `python3 planform.py; python3 planform.py --rule S; python3 calib.py; python3 joined.py; python3 joined.py --rule S; python3 joined.py --calib; python3 boxcheck.py; python3 report.py --doc`.
