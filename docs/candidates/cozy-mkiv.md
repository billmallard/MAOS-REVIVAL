# Cozy MKIV (reference)

Stage 1 stub (extended in stage 3 below), generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Nat Puffer, Co-Z Development (Rutan Long-EZ lineage) |
| Years | 1991 on; plans still sold |
| Number built | ~1,450 plans sets sold by 2009; ~225 flying then (Co-Z FAQ); 350 built by 2015 (Wikipedia) |
| Survivors / registered | FAA count not obtained |
| Seats | 4 |
| Configuration | Canard pusher, 4 seats (2+2 side by side), fixed mains, retractable nose gear |
| Construction | Moldless foam/fiberglass composite |
| Engine | Lycoming O-360, 180 hp (160-200 hp suitable) |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,050 lb | F | [source](https://www.aircraftspruce.com/cozy/specs.html) | - |
| Empty weight | 1,050 lb | F | [source](https://www.aircraftspruce.com/cozy/specs.html) | designer's estimated empty weight (AOPA Pilot 1994) |
| Useful load | 1,000 lb | F | [source](https://www.aircraftspruce.com/cozy/specs.html) | derived 2,050 - 1,050 |
| Useful load, fleet or as-weighed | 871 lb | P | [source](http://acversailles.free.fr/documentation/03~Documentation_Generale_M_Suire/Essais_en_vol/COZY_MARK-IV.pdf) | one builder aircraft weighed by the CAFE Foundation (N494CZ, 1,179.3 lb empty) against the 2,050 lb design gross; not a fleet average |
| Usable fuel | 52 US gal | F | [source](https://www.aircraftspruce.com/catalog/pnpages/01-00257.php) | capacity; usable not stated |
| Published range | 1,129 nm | F | [source](https://www.aircraftspruce.com/cozy/specs.html) | 40% power, 12,000 ft, reserve not stated (1,300 mi converted) |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 174 | 8500 | - | - | P | [source](https://www.kitplanes.com/archive-august-1991/) | factory demonstrator measured, 2,700 rpm, fixed-pitch prop |
| 191 P | 8000 | 75% | - | F | [source](https://www.aircraftspruce.com/cozy/specs.html) | 220 mph converted |
| 192 | - | - | 10.5 | F | [source](https://www.aopa.org/news-and-media/all-news/1994/december/pilot/ez-does-it) | claimed max cruise, quoted by AOPA Pilot Dec 1994 |
| 161 | 12000 | 40% | - | F | [source](https://www.aircraftspruce.com/cozy/specs.html) | 185 mph converted, 40% power |
| 176.7 M | 8021 | - | 10.0 | P | [source](http://acversailles.free.fr/documentation/03~Documentation_Generale_M_Suire/Essais_en_vol/COZY_MARK-IV.pdf) | CAFE flight test, N494CZ, IO-360 180 hp, WOT 23.5 in / 2,607 rpm, best-power region, density altitude, 1,864 lb |
| 169.5 | 12032 | - | 8.2 | P | [source](http://acversailles.free.fr/documentation/03~Documentation_Generale_M_Suire/Essais_en_vol/COZY_MARK-IV.pdf) | CAFE flight test, N494CZ, WOT 20.1 in / 2,545 rpm, mid mixture sweep, density altitude, 1,874 lb |
| 163.5 | 8102 | - | 8.3 | P | [source](http://acversailles.free.fr/documentation/03~Documentation_Generale_M_Suire/Essais_en_vol/COZY_MARK-IV.pdf) | CAFE flight test, N494CZ, WOT 23.5 in / 2,500 rpm, lean of peak, density altitude |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: pass**
  - Useful load: 1,000 lb (pass) against 1,000 lb.
  - Range: 1,129 nm (pass; 40% power, 12,000 ft, reserve not stated (1,300 mi converted)) against 1,000 nm.
  - Cruise: 191 KTAS at 8,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot (951 nm max).
- **Measured or reported: fail** - UL -129 lb
  - Useful load: 871 lb (fail) against 1,000 lb.
  - Range: 1,049 nm (pass; still air, no reserve, from fuel and measured flow) against 1,000 nm.
  - Cruise: 177 KTAS at 8,021 ft (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 581 / cannot @ 170 kt, 8.2 gph.
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 180 hp.

Sanity flags:

- fleet useful load 129 lb below factory
- the only published speed/flow pair (192 kt, 10.5 gph) is a claim, and the 40%-power range has no published flow
- as published (1,000 lb, 1,129 nm, 191 KTAS at 8,000 ft) it passes all three floors; the 951 nm in the first version of this list was 52 gal / 10.5 gph x 192 kt, the AOPA-quoted max-cruise claim, set against a range published at 40% power: a basis mismatch, not a units error (1,300 statute mi = 1,129 nm is right)

## Why it died

Not dead. Aircraft Spruce has held exclusive rights since 1 Jan 2004 and sells plans and components (http://www.cozyaircraft.com/czmain.htm).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Side-by-side front seats in a canard pusher: the Long-EZ layout widened to four seats without losing its cruise efficiency on 180 hp.
- Moldless foam-and-glass construction that a plans builder can do without tooling; the cost is build hours and builder-to-builder weight scatter (871 lb useful on the CAFE aircraft against 1,000 lb designed).

## Rights and provenance (known so far; research, not legal advice)

Aircraft Spruce (exclusive marketing rights from Co-Z Development, 2004); also bought Brock metal-parts tooling 2005. Owned by the stage 2 rights research (AER-3787).

## Safety record

Co-Z FAQ cites two fatal accidents (to ~2009); a four-aboard MKIV was lost off California 15 Jan 2024 (NBC LA).

<!-- stage3:start -->

## Stage 3: reference (AER-3783)

Our own check, from published geometry and weights, calibrated against published flight data. Method, calibration and the Aeromomentum assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are research, not legal advice. Nobody has been contacted.

### Verdict

**Reference, on two bases that are kept apart.** As published (cozyaircraft.com specs), the Cozy MKIV passes all three floors: 1,000 lb useful, 191 KTAS at 75% and 8,000 ft, and 1,130 nm (1,300 statute miles) at 40% power. As measured on the CAFE Foundation's test aircraft it gives 871 lb useful (1,179 lb empty against the 2,050 lb design gross), 177 KTAS at 8,000 ft at full throttle, and 1,049 nm still air with no reserve at 12,000 ft lean. The gap is empty weight: the designer's 1,050 lb against one equipped builder aircraft at 1,179 lb. Our drag check matches CAFE's measured speeds with a factor of 1.36. Candidates are compared with the Cozy published-to-published and measured-to-measured. The first version of the long list called it a near miss on 951 nm; that was a basis mismatch (a max-cruise claim against a 40% power range), not a units error.

### Idea ledger (what a new airplane should keep)

- Side-by-side front seats in a canard pusher: the Long-EZ layout widened to four seats without losing its cruise efficiency on 180 hp.
- Moldless construction a plans builder can do without tooling; the cost is build hours and weight scatter between builders.

### Published, measured and our check, side by side

Read across a row only within one column's basis. The three targets are separate floors.

| | As published | Measured or reported | Our check, original engine |
|---|---|---|---|
| Useful load | 1,000 lb (pass) | 871 lb (fail) | 871 lb (the empty weight the model uses: 1,179 lb) |
| Range | 1,129 nm (pass; 40% power, 12,000 ft, reserve not stated (1,300 mi converted)) | 1,049 nm (pass; still air, no reserve, from fuel and measured flow) | 829 nm, still air, no reserve, full fuel from MTOW, at 131 hp and 8,000 ft |
| Cruise | 191 KTAS at 8,000 ft (pass+) | 177 KTAS at 8,021 ft (pass) | 175 KTAS at 131 hp and 8,000 ft |
| Screen | pass | fail | see the verdict |

### Independent performance check

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

### Engine fit with the Aeromomentum line

- **Power.** The AM20T at 195 hp assumed continuous replaces a 180 hp IO-360, so it gains power. Our check gives 202-217 KTAS.
- **Mass and CG.** The installed mass rises about 63 lb (E), in the tail of a canard. Useful load falls from 871 lb (CAFE-weighed) to 808 lb, and the aft CG moves the wrong way for a type whose owner's manual warns it "could become locked in" aft of the limit.
- **Fuel.** At 195 hp the 50.7 gal usable gives only 645-668 nm. The Cozy cannot fly 1,000 nm on this engine at any setting we computed.

### Rights and provenance (stage 2)

Firmly held (Elon, `docs/rights/cozy-mkiv.md`, PR #3). Aircraft Spruce has held exclusive rights since 2004, claims US copyright, sells plans with a one-airplane licence, and the licence bars using the drawings to design another aircraft. Not a revival target; it is the yardstick.

### Safety record

Record (NTSB CAROL, Mark IV): 22 events, 7 fatal, 12 killed, on about 350 built. Powerplant and fuel dominate. Two items are tied to the configuration. The belly landing brake, deployed in flight, blocked engine airflow and caused total power loss twice. And on two aircraft a main-wing stall would not break, both traced by the NTSB to building outside the plans (canard incidence, removed vortilons, aft CG).

### Why it died, and whether a revival fixes it

It did not die. It is the reference.

### Not yet done

- None; it stays the yardstick.
- What a modern rebuild changes in mass, cost and build hours (MANUFACTURING, stage 4, AER-3784).

<!-- stage3:end -->
