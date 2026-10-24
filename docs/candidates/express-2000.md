# Express (Wheeler / Series 90 / 2000 FT)

Stage 1 stub (extended in stage 3 below), generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Ken Wheeler, Wheeler Technology |
| Years | 1987 first flight; kits through several owners to ~2011 |
| Number built | ~300 kits, ~30 completed by 1997 |
| Survivors / registered | ~61 registered across variants |
| Seats | 4 |
| Configuration | Low wing, 4 seats, fixed or retractable gear |
| Construction | Vinylester/E-glass/foam composite |
| Engine | Continental IO-360-ES 210 hp (CAFE test aircraft); IO-540/550 on later builds |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,895 lb | F | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | kit-maker design gross; 3,200-3,600 for later variants |
| Empty weight | 1,850 lb | F | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | kit-maker 'normal' |
| Useful load | 1,045 lb | F | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | derived |
| Useful load, fleet or as-weighed | 901 lb | P | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | one builder aircraft weighed by CAFE (N360EZ, 1,994 lb empty), not a fleet average |
| Usable fuel | 92 US gal | P | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | - |
| Published range | 1,401 nm | P | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | CAFE-computed VFR range at 9.7 gph |

Cruise settings (the starred row is the one screened for speed):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 169 * | 6190 | - | 11.1 | P | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | CAFE measured, 25.4 in / 2,780 rpm, density altitude |
| 162 | 7750 | - | 9.5 | P | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | CAFE measured, leaned |
| 153 | 9813 | - | 9.7 | P | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | CAFE measured |
| 110 | - | - | 5.8 | P | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | CAFE best mpg |

## Screen (stage 1, published numbers)

- **Verdict: near miss** - UL -99 lb
- Useful load: 901 lb (near) against 1,000 lb.
- Range: 1,745 nm still-air (pass; basis: calc) against 1,000 nm.
- Cruise: 169 KTAS at 6,190 ft (pass) against >160 KTAS (>180 preferred).
- Payload at 1,000 nm: 585 lb with no reserve; 559 lb with a 45 min reserve. Setting: 110 KTAS at 5.8 gph.
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 210 hp.

Sanity flags:

- published range 1,401 nm vs 1,745 nm from fuel and flow
- fleet useful load 144 lb below factory
- CAFE measured cruise on 210 hp is the best-evidenced speed/flow data in this list; a 300 hp build would be faster but heavier

## Why it died

A fatal four-occupant crash before Oshkosh 1990 contracted sales and bankrupted Wheeler; EDI (1996) and Express Aircraft Co. also failed (CAFE report).

## Rights and provenance (known so far; research, not legal advice)

Wheeler -> Express Design Inc. (1992) -> Express Aircraft Co. (1996/97) -> Composite Aircraft Technology (2007). Current holder not found. Owned by the stage 2 rights research (AER-3787).

## Safety record

1990 crash killed 4 (pilot error); demonstrator engine failure, no injuries (CAFE).

<!-- stage3:start -->

## Stage 3: shortlist rank 6 of 8 (AER-3783)

Our own check, from published geometry and weights, calibrated against published flight data. Method, calibration and the Aeromomentum assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are research, not legal advice. Nobody has been contacted.

### Verdict

**Rank 6.** It has the best evidence on the shortlist (CAFE flight test, a weighed aircraft) and is the most orphaned. On our numbers it misses: 890 lb useful, and it cannot carry a 45 min reserve over 1,000 nm at continuous power (439-445 lb at economy power, 149-157 KTAS). And it has a tail the NTSB has named.

### Independent performance check

Model: `docs/shortlist/check/models/express-2000.json`; result: `docs/shortlist/check/results/express-2000.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 218 ft2, Wing 239 ft2, HTail 40 ft2, Fin 22 ft2; total 519 ft2.

**Model assumptions** (grade E unless a source is named):

- Geometry for the cruciform-tail Express FT (CAFE N360EZ): wing span 31 ft, area 130.29 ft2, tip chord 37.5 in, NLF(1)-0215F at 15% t/c, length 25.67 ft (P, CAFE). Root chord set to 5.28 ft so the trapezoid closes CAFE's area.
- Fuselage max width 3.9 ft (44 in cabin + walls) and height 4.1 ft: E, ours; the CAFE report gives neither.
- Horizontal tail total 22.4 ft2 (9.33 ft x 2.4 ft, stabilizer 13.14 ft2 per CAFE plus an estimated elevator); fin 12 ft2: E, ours.
- Laminar run x_tr: wing 0.30, tails 0.20, fuselage 0.05 (builder composite finish; NLF(1)-0215F bucket not credited in full).
- Fixed gear, 6.00x6 mains with pants: D/q 0.60 ft2 for three faired wheels and legs (E, Gudmundsson ch. 15 faired-wheel range).
- CAFE powers are not published: hp is estimated from manifold pressure, rpm and density altitude by Gagg-Ferrar (E). Points at full throttle only.
- Original installed engine mass 380 lb = typical published dry weight x 1.15 for mount, baffles, exhaust and oil cooler (E; per-variant check owed by MANUFACTURING).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 169 | 6,190 | 169 | 11.1 | P | 181 | +7% | 1.20 | 144 | CAFE, full throttle 25.4 in/2780 rpm, density alt; hp E (Gagg-Ferrar) |
| 166 | 7,791 | 149 | 10.5 | P | 174 | +5% | 1.13 | 135 | CAFE, 24.1 in/2600 rpm (about full throttle with ram), peak-speed mixture; hp E |
| 153 | 9,813 | 139 | 9.7 | P | 171 | +12% | 1.34 | 110 | CAFE, 21.4 in/2597 rpm (about full throttle); hp E; excluded from calibration: 14 kt slower than the 7,791 ft point for 2,000 ft more altitude, so it was probably not at full throttle and the hp estimate is high |

**Drag factor used: 1.29** (fleet calibration (own points read cleaner than the fleet); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.16.

**Drag build-up at 6,190 ft, 169 hp, 2,885 lb, with the factor applied:** 164 KTAS, CD0 0.0234 on S = 130.3 ft2, propeller efficiency 0.82, L/D 10.5.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.736 | Swet 239.1 ft2, Re 6.5M, Cf 0.00231, FF 1.336, Q 1.00, x_tr 0.30 |
| HTail | 0.145 | Swet 39.8 ft2, Re 3.6M, Cf 0.00290, FF 1.195, Q 1.05, x_tr 0.20 |
| Fin | 0.077 | Swet 22.2 ft2, Re 4.6M, Cf 0.00277, FF 1.193, Q 1.05, x_tr 0.20 |
| Fuselage | 0.606 | Swet 217.7 ft2, Re 39.0M, Cf 0.00227, FF 1.224, Q 1.00, x_tr 0.05 |
| fixed gear, faired | 0.600 | fixed allowance |
| cooling | 0.089 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.113 | 5% of the rest |
| calibration factor | 0.686 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.575 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 150 hp at 8,000 ft gives 160 KTAS; still-air range on full usable fuel from MTOW 1,242 nm (climb allowance 24 lb); payload at 1,000 nm 456 lb with no reserve, 407 lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change +11 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 179 (186) | 890 (890) | 1,062 | 376 | cannot (cannot) | 149: 481 / 439 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 191 (199) | 890 (890) | 1,115 | 393 | cannot (347) | 157: 487 / 445 |

### Engine fit with the Aeromomentum line

- **Power.** The AM20T at 195 hp assumed continuous replaces the 210 hp IO-360-ES of the CAFE aircraft (later builds used 260-300 hp). That gives 179-191 KTAS.
- **Mass and CG.** About +11 lb installed (E). The headline useful load is the CAFE-weighed aircraft's 901 lb less that, 890 lb.
- **Cooling.** CAFE found the stock installation overheated at the published climb speed, and had to climb at 95-98 kt indicated. A liquid-cooled installation could fix that, but it is not computed.

### Rights and provenance (stage 2)

Open question (Elon, `docs/rights/express-2000.md`, PR #3). It was always a kit. The design passed through at least five owners, three of them through bankruptcy: Wheeler Technology, Express Design Inc., Express Aircraft Co. LLC, Exosphere Aircraft Co., and Composite Aircraft Technology LLC, which bought the assets out of bankruptcy court in September 2007. There is no public trace of CAT after about 2010, and its domain now serves an unrelated site. The old EXPRESS mark was cancelled in 2001. This is the most orphaned design on the shortlist.

### Safety record

Record (ASN with NTSB numbers, lower bound): at least 17 US NTSB events and 13 fatal accidents worldwide (21 killed), on about 55 active aircraft. About 9 of the 13 fatal accidents are stall or loss of control. In 2015 the NTSB named "the airplane's design, which resulted in poor yaw stability at low airspeed" as a contributing factor, citing the CAFE test (CEN15FA321). CAFE itself found low yaw damping, an uncommanded right yaw after clean stalls, and fin blanking. The 1990 demonstrator crash that ended the company was a spin (SEA90FA146). **Inference:** several of the stall fatalities were big-tail Series 90/2000 aircraft, so the larger tail apparently did not fix it.

### Why it died, and whether a revival fixes it

The 1990 fatal crash of the second demonstrator on its way to Oshkosh collapsed sales and bankrupted Wheeler; two successor companies also failed. A revival would have to fix the directional stability first: a new tail designed and flight-tested, not a bigger copy.

### Not yet done

- Trace Composite Aircraft Technology's 2007 assets through public records (Elon).
- Nothing more from AERO unless Bill wants a tail study.
- What a modern rebuild changes in mass, cost and build hours (MANUFACTURING, stage 4, AER-3784).

<!-- stage3:end -->

<!-- stage4:start -->

## Stage 4: what modern manufacturing changes (AER-3784)

Short note. Method, prices and sources are in [docs/MANUFACTURING.md](../MANUFACTURING.md); the weight table is generated by `docs/manufacturing/weights.py`. Desk study: nothing weighed or quoted by us, nobody contacted. Every E is our estimate.

**Original construction:** molded vinylester/E-glass/foam, the heaviest laminate on the shortlist. Molds unaccounted for since about 2009.

**Modern route:** new molds and an infused carbon/epoxy airframe, with a new tail.

**Empty weight:** rebuild **1,860-2,030 lb**, useful load **865-1,035 lb** (stage 3: 901, from the CAFE-weighed aircraft). Engine change -6 to +23 lb (IO-360-ES 320 lb, TCDS E1CE). The best case reaches the 1,000 lb floor; the worst does not.

**Weight build-up:**

| Item | Light, lb | Heavy, lb | Basis | Grade |
|---|---|---|---|---|
| Starting empty weight | 1,994 | 2,050 | CAFE weighed N360EZ 1,994.1 lb with oil (R, CAFE APR, flights Sep 1997); designer 1,850 (F). Heavy end ours (E) | R/E |
| Vinylester/E-glass/foam molded parts -> infused carbon/epoxy sandwich in new molds | -120 | -50 | 519 ft2 wetted; vinylester glass skins are the heaviest laminate on the list | E |
| New tail (the NTSB-named yaw stability), larger fin and rudder | +5 | +20 | Size not known until a tail study | E |
| Panel: EFIS | -20 | +0 | 1995 panel | E |
| EFI engine: backup battery and bus | +5 | +10 | One ECU | E |
| **Rebuild empty weight, no engine credit** | **1,860** | **2,030** | sum, rounded to 10 lb | E |

Hours: 2,000 factory, 5,000 for the CAFE aircraft (F/P, CAFE APR); kit $34,995 then.

**Home-shop route** ([MANUFACTURING.md](../MANUFACTURING.md#the-home-shop-route), tools about $20-49k, prices read 2026-10-24, all E): Home molds as the Defiant, scaled to 519 ft2 wetted, including the new tail.

<!-- stage4:end -->
