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

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 169 M | 6190 | - | 11.1 | P | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | CAFE measured, 25.4 in / 2,780 rpm, density altitude |
| 162 | 7750 | - | 9.5 | P | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | CAFE measured, leaned |
| 153 | 9813 | - | 9.7 | P | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | CAFE measured |
| 110 | - | - | 5.8 | P | [source](https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf) | CAFE best mpg |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: incomplete: no speed**
  - Useful load: 1,045 lb (pass) against 1,000 lb.
  - Range: 1,401 nm (pass; CAFE-computed VFR range at 9.7 gph) against 1,000 nm.
  - Cruise: not found against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- **Measured or reported: near miss** - UL -99 lb
  - Useful load: 901 lb (near) against 1,000 lb.
  - Range: 1,745 nm (pass; still air, no reserve, from fuel and measured flow at 110 KTAS) against 1,000 nm.
  - Cruise: 169 KTAS at 6,190 ft (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 585 / 559 @ 110 kt, 5.8 gph.
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 210 hp.

Sanity flags:

- published range 1,401 nm vs 1,745 nm from fuel and flow
- fleet useful load 144 lb below factory
- CAFE measured cruise on 210 hp is the best-evidenced speed/flow data in this list; a 300 hp build would be faster but heavier

## Why it died

A fatal four-occupant crash before Oshkosh 1990 contracted sales and bankrupted Wheeler; EDI (1996) and Express Aircraft Co. also failed (CAFE report).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Four real seats and a 1,000 lb design useful load on 210 hp, with the best-measured performance in the survey (CAFE 1997).
- An NLF(1)-0215F laminar wing on a kit; a cruciform tail on the FT variant. Stall and yaw behaviour is the open issue (stage 3).

## Rights and provenance (known so far; research, not legal advice)

Wheeler -> Express Design Inc. (1992) -> Express Aircraft Co. (1996/97) -> Composite Aircraft Technology (2007). Current holder not found. Owned by the stage 2 rights research (AER-3787).

## Safety record

1990 crash killed 4 (pilot error); demonstrator engine failure, no injuries (CAFE).

<!-- stage3:start -->

## Stage 3: shortlist rank 2 of 5 (AER-3783)

Our own check, from published geometry and weights, calibrated against published flight data. Method, calibration and the Aeromomentum assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are research, not legal advice. Nobody has been contacted.

### Bill's call

Bill, 2026-10-24: "Very interesting... I never understood why this didn't do better in the market." He knew a pilot killed in an Express at Grand Prairie Municipal: "It has a tendency to bite in with the stall behavior in climbing right turns." Kept and dug into: the stall and yaw problem and the market failure, below.

### Verdict

**Rank 2.** The best-evidenced design on the shortlist (a CAFE flight test and a weighed aircraft), with four real seats on 210-260 hp. On the long list's published column it passes useful load (1,045 lb, the kit maker's) and range (1,401 nm, which is CAFE's computed VFR range, not a maker's figure) but has no maker's speed; as measured it misses useful load by 99 lb (901 lb on the weighed aircraft) and cruises 169 KTAS at 6,190 ft. On an AM20T our check gives 179-191 KTAS and 1,062-1,115 nm on full fuel at continuous power. Its accident record is the problem, and the dig below connects it to the tail, the power the tail was asked to handle, and stall speeds higher than published, each with a stated fix and cost. It died of business execution, which a revival can fix. It ranks below the Aries because the tail must be re-derived and flight-tested before anything else, and because its rights are orphaned.

### Idea ledger (what a new airplane should keep)

- Four real seats and a 1,000 lb design useful load on 210 hp, with the best-measured performance in the survey (CAFE 1997).
- An NLF(1)-0215F laminar wing on a kit, which CAFE's numbers show working: 169 KTAS at 6,190 ft on about 169 hp.
- Lesson, the tail: size the vertical tail for the installed power and keep the horizontal tail out of the fin's wake; the S-90 tail was the kit makers' own fix.
- Lesson, the business: complete kits, real build hours and a flying fleet sell kits; redesign churn and incomplete kits killed it.

### Published, measured and our check, side by side

Read across a row only within one column's basis. The three targets are separate floors.

| | As published | Measured or reported | Our check, original engine |
|---|---|---|---|
| Useful load | 1,045 lb (pass) | 901 lb (near) | 901 lb (the empty weight the model uses: 1,994 lb) |
| Range | 1,401 nm (pass; CAFE-computed VFR range at 9.7 gph) | 1,745 nm (pass; still air, no reserve, from fuel and measured flow at 110 KTAS) | 1,242 nm, still air, no reserve, full fuel from MTOW, at 150 hp and 8,000 ft |
| Cruise | not found | 169 KTAS at 6,190 ft (pass) | 160 KTAS at 150 hp and 8,000 ft |
| Screen | incomplete: no speed | near miss | see the verdict |

### The stall and yaw problem, and what fixes it

**What the record shows** (sources and the full accident table: `docs/shortlist/check/express/README.md`):

- **Grand Prairie, the accident Bill knew: NTSB CEN21LA096.** Express CT N772BM, 21 December 2020, two killed. It departed runway 17 at Grand Prairie Municipal, and the pilot asked for and was given a right turn. The tower then told him to keep the turn tight to stay out of Arlington's airspace. The NTSB track shows a continuous climbing right turn. A witness saw the bank steepen into a steep dive, with power coming up after the dive began. Probable cause: "The pilot's loss of airplane control during the departure turn, which resulted in an aerodynamic stall and impact with terrain." No mechanical anomaly. The NTSB does not state the tail type; "CT" is the cruciform-tail designation in the kit makers' and Jane's usage (P; tail type E).
- **CEN15FA321 (Holland MN, 2015, three killed)** ended in a high-pitch, steep right turn with airspeed decaying to 48 kt, then an upright right spin (Chelton EFIS data, NTSB docket). The NTSB named "the airplane's design, which resulted in poor yaw stability at low airspeed" as contributing. It did no testing of its own: the finding rests on the 1997 CAFE Foundation flight test (P).
- **CAFE 1997, N360EZ (cruciform tail, 210 hp), measured:** yaw doublets overshot "4-5 times" before settling (low directional damping); after 1 g clean stalls an "uncommanded right yaw with inadequate elevator control" until 85 kt; at 26 deg the rudder "seemed to set up a partial stall of the vertical fin"; the horizontal tail was blanked by the fin at high sideslip, so the elevator ran out and the nose pitched down. With 20 deg rudder stops the same traits appeared to a lesser degree (P).
- **Express Design Inc., February 1995**, told every owner of the cruciform-tail Express CT that rudder could produce an unexpected pitch-down, confirmed by outside consultants, and recommended the larger Series 90 tail (F).
- **The accident record** (our count from CAROL, ASN and foreign reports): 18 fatal Express-family accidents and 30 deaths, 1990-2025, on about 100 aircraft ever registered (about 55 active); 19 and 32 if a "Terrair Express" of unconfirmed lineage is included. This replaces the first pass's 13 and 21, which missed six. Of 17 stall or loss-of-control events in flight, the turn is recorded as **right in 9**, left in 3, conflicting in 1, and not recorded in 4. Three of the nine right-turn events followed an engine failure and two were turns ATC or the pattern required, so the record alone does not prove a right-hand bias. Both tail families appear among the stall events.

**Why climbing right turns, an inference from the physics and the data, not a finding.** At high power and low speed, P-factor, slipstream swirl and torque all yaw a clockwise-turning (as seen from the cockpit) tractor to the left, so the pilot climbs holding right rudder. In a climbing left turn those tendencies already supply the yaw, and the right rudder the pilot is holding works against a skid. In a climbing right turn, a pilot who tightens the turn with more right rudder, and holds the bank back with left aileron, is cross-controlled in a skid: the inside (right) wing flies at the higher angle of attack, its down-going aileron raises it further, and it stalls first, so the airplane rolls and spins to the right. An airframe with weak directional stability lets that skid grow further for the same rudder and is slow to straighten, and the Express adds three things to it:

1. **A fin too small for the fuselage in front of it.** The fuselage is wide and tapering, which is destabilising in yaw (CAFE names it). On our estimate the fuselage alone gives Cn_beta of about -0.0013 per degree. A fin under about 15 ft2 at a 14 ft arm leaves the total near neutral; a normal light-single margin (about +0.0010 to +0.0015 per degree) needs about 20-24 ft2 (table below). No Express fin dimensions are published, so the current fin is placed by inference from CAFE's measured behaviour, not by measurement.
2. **More power than the tail was proven with.** CAFE flew 210 hp. The Grand Prairie and Holland aircraft had 250 and 260 hp, and later builds ran 300 hp and IO-550s. The left-turning tendencies, and the rudder the pilot needs against them, grow roughly with power at climb speed. An AM20T (260 hp, 300 hp for five minutes) sits in the same band, so a revival must size the tail for it.
3. **Stall speeds higher than the book.** CAFE measured 67 KCAS clean and 58 KCAS full flap at 2,865 lb. The kit makers published Vs1 55-58 kt. At 3,200 lb in a 45 deg bank the clean stall is 84 KCAS on CAFE's basis, against 69-73 kt on the published one (table below). A pilot flying a tight departure turn by the book is closer to the stall than the book says. One previous owner told the NTSB he never saw the published 55 kt and flew his own 85/70 kt.

**What fixes it, and what each fix costs** (cruise cost from the stage 3 model at 195 hp and 8,000 ft; mass E):

| Fix | What it does | Cruise cost | Mass and other cost |
|---|---|---|---|
| Fin to about 20-24 ft2, sized at 260-300 hp | Restores a normal directional-stability margin and rudder power | 2.0-2.9 kt | About +8-12 lb aft (E), which needs about the same again in nose ballast unless the tail surfaces get lighter |
| Dorsal fin, about 3 ft2 | Delays the fin stall CAFE saw at high sideslip | 0.7 kt | A few lb; no tooling for the main surfaces |
| Ventral fin, about 3 ft2 | Adds yaw stiffness below the horizontal tail's wake | 0.8 kt | A few lb; ground clearance in the flare has to be checked |
| Horizontal tail out of the fin's wake, at S-90 size (31 ft2, low) | Ends the fin blanking the elevator; EDI's consultant computed the forward-CG range growing from 11.2 in to 20 in | about 3 kt (40% more tail wetted area); 4.3 kt with dorsal and ventral | New tail tooling; it is what the kit makers themselves offered |
| Stall strips at the inboard leading edge | Makes the untwisted laminar wing stall root-first, with buffet, instead of dropping a wing | negligible (E) | 1-2 kt higher stall speed (E); must be set in flight test |
| Leading-edge cuff outboard | Delays the tip stall | 2-4 kt on a laminar wing (E): the cuff trips laminar flow | Not recommended ahead of the tail fixes |
| Stiff rudder circuit, 20 deg stops | Owners found cable stretch and a small horn cut real rudder travel to a few degrees; CAFE recommended 20 deg | none | Build quality and inspection, no drag |
| Consistent rigging | Stab incidence varied from 0 to -0.8 deg and more across eras; owners re-shim | none | A jig and a check, not a redesign |
| Lighter tail surfaces | Owners weighed 81 lb of rudder and elevators and carry 56-62 lb of nose ballast; one built aluminium surfaces 33 lb lighter | none | Saves weight twice: the surfaces and the ballast |
| Honest V-speeds, a fixed static system, an AOA indicator with aural warning | Lets the pilot see the real margin in a turn | none | A few lb; a flight-test programme to publish real numbers |

A revival on this airframe would re-derive the tail and fly a stall and departure-resistance programme before any kit was sold. Whether a given fix gives acceptable spin or departure behaviour can only be shown in flight test; nothing here claims it.

### Why it failed in the market

Bill: "I never understood why this didn't do better in the market." On the record, the airplane was liked and the business never delivered it. In order of weight (sources in `docs/shortlist/check/express/README.md`):

1. **It lost its demonstrator before there was a fleet.** AOPA Pilot's August 1990 pilot report says there were "no customer airplanes yet flying". On 25 July 1990 the second factory demonstrator spun in on its way to Oshkosh, killing three (NTSB; CAFE and Kitplanes say four). With no customer aircraft to point to, CAFE says the crash "led to a severe contraction in sales eventually prompting Ken Wheeler to enter bankruptcy" (P).
2. **The kits were not complete, so the fleet never grew.** Kits were incomplete at the Wheeler bankruptcy and the plans were incomplete; one builder "actually created much of the documentation used by subsequent builders" (CAFE). The kit makers claimed 1,000-2,000 build hours; CAFE's builder took 5,000. About 30 of about 300 kits were finished by 1997 (P). A builder put it plainly: "nothing sells kits like kits completed and on the flight line" (B).
3. **Five owners, three bankruptcies, and each one redesigned instead of shipping.** Wheeler (to 1991), Express Design (Chapter 7, 1996), Express Aircraft Co (out of business 2004, after its president was killed in the turbine Auriga), Exosphere (2005-07; five builders won about $250,000 in judgments for undelivered parts and prepaid builder assist), and Composite Aircraft Technology (2007, last seen about 2013). Builders report months of parts delays and poor metal parts (B, F).
4. **The tail problem was public, and its fix was an extra.** A builder's dispute with Wheeler over the tail (1991), then Express Design's 1995 letter recommending the Series 90 tail, told every prospect that the airplane had a handling issue and that the cure cost money.
5. **The competition shipped.** In 1994 a Lancair IV airframe was $46,900 and a IV-P $66,900, for a faster airplane; in 2003-05 an Express 2000 FT was $48,900, against a Velocity XL at $37,500 (2005). Van's RV-10 arrived in 2003 as a complete matched-hole metal four-seat kit from a company that delivers; one long-time Express builder wrote that today he would probably pick an RV-10 (B).

**What a revival fixes.** Points 2-5 are business execution, which is what a modern, fully tooled, complete kit or factory-assist build addresses (stage 4). Point 1 is history. The tail is an engineering fix with a known cost. What a revival cannot buy back is the accident record, which is why the tail and a flight-test programme come first.

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

Record (our count, NTSB CAROL with dockets, ASN and foreign reports; full table in `docs/shortlist/check/express/README.md`): 18 fatal accidents and 30 deaths, 1990-2025 (19 and 32 with one aircraft of unconfirmed lineage), on about 100 ever registered and 55 active. Of 17 in-flight stall or loss-of-control events, 14 were fatal; 9 record a right turn, 3 a left. The NTSB named the design's poor yaw stability as contributing in CEN15FA321, on the strength of the 1997 CAFE flight test, and quoted the kit makers' 1991 and 1995 tail letters in WPR17FA185. Power-loss accidents are the second pattern (at least six). See the study above for the configuration link and the fixes.

### Why it died, and whether a revival fixes it

A 1990 demonstrator crash before any customer aircraft flew, incomplete kits, five owners and three bankruptcies, a public tail problem, and competitors that shipped (details above). The business causes are what a revival with complete, tooled kits fixes; the tail is an engineering fix with a known cruise cost of 2-4 kt.

### Not yet done

- Fin dimensions and tail arm: none are published. Measuring an aircraft, with Bill's go-ahead on any contact, would turn the stability table from parametric into a number.
- A tail re-derivation sized at 260-300 hp, then a stall and departure-resistance flight-test plan (AERO; SAFETY review asked on AER-3785 first).
- Trace Composite Aircraft Technology's 2007 assets (Elon).
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
