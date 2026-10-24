# Rutan Defiant

Stage 1 stub (extended in stage 3 below), generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Burt Rutan, RAF (Model 40) |
| Years | 1978 first flight; plans 1984-85 |
| Number built | 176 plans sets; ~30 completed |
| Survivors / registered | ~20 (Twin & Turbine 2026) |
| Seats | 4 |
| Configuration | Canard, centerline-thrust twin (push-pull), fixed-pitch props, no flaps |
| Construction | Moldless composite |
| Engine | 2x Lycoming O-320 160 hp (prototype); builders often 2x O-360 180 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,900 lb | F | [source](https://planeandpilotmag.com/rutan-defiant) | Wikipedia gives 2,997 |
| Empty weight | 1,610 lb | F | [source](https://planeandpilotmag.com/rutan-defiant) | Wikipedia gives 1,701 |
| Useful load | 1,290 lb | F | [source](https://planeandpilotmag.com/rutan-defiant) | derived from P&P |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 108 US gal | P | [source](https://www.twinandturbine.com/?p=15364) | N171D, the aircraft whose cruise is quoted; 90-120 gal across sources |
| Published range | 1,128 nm | F | [source](https://planeandpilotmag.com/rutan-defiant) | not stated |

Cruise settings (the starred row is the one screened for speed):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 162 * | 10000 | - | 16 | P | [source](https://www.twinandturbine.com/?p=15364) | N171D, 160-165 KTAS at 15-17 gph 'in the teens'; 10,000 ft used as the lower bound |
| 152 | - | - | 19 | P | [source](https://www.twinandturbine.com/?p=15364) | low altitude, 150-155 KTAS at 18-20 gph |

## Screen (stage 1, published numbers)

- **Verdict: pass**
- Useful load: 1,290 lb (pass) against 1,000 lb.
- Range: 1,094 nm still-air (pass; basis: calc) against 1,000 nm.
- Cruise: 162 KTAS at 10,000 ft (pass) against >160 KTAS (>180 preferred).
- Payload at 1,000 nm: 697 lb with no reserve; not possible (tanks too small) with a 45 min reserve. Setting: 162 KTAS at 16.0 gph.
- Aeromomentum fit (first cut): Yes: 2x AM15T (160 hp) matches the prototype's 2x 160 hp; 180 hp builds need 2x AM20T (heavier).

Sanity flags:

- none raised

## Why it died

The 1979 certification effort lost its financing; plans ended with RAF's 1985 liability stop (Wikipedia; P&P).

## Rights and provenance (known so far; research, not legal advice)

Rutan Aircraft Factory; not marketed. Owned by the stage 2 rights research (AER-3787).

## Safety record

No configuration-specific pattern found. Single-engine climb 150-400 fpm depending on which engine is out (T&T).

<!-- stage3:start -->

## Stage 3: shortlist rank 1 of 8 (AER-3783)

Our own check, from published geometry and weights, calibrated against published flight data. Method, calibration and the Aeromomentum assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are research, not legal advice. Nobody has been contacted.

### Verdict

**Rank 1.** It is the only direct Aeromomentum fit, gives twin redundancy for uncertified engines with no Vmc problem, has a clean record, and died for reasons a revival removes. Its weakness is drag. The published numbers say it is 1.7 times draggier than its geometry, so its payload at 1,000 nm with a 45 min reserve is cannot to 669 lb at 178-190 KTAS, and 807-821 lb at 150-159 KTAS. Its geometry is also the thinnest-sourced of the top four: the canard, chords and fuselage section are all estimates.

### Independent performance check

Model: `docs/shortlist/check/models/rutan-defiant.json`; result: `docs/shortlist/check/results/rutan-defiant.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 228 ft2, Wing 240 ft2, Canard 31 ft2, Winglets 16 ft2; total 515 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 31.4 ft, area 133 ft2 (F, Canard Pusher #38, plans-built version); LE sweep 23 deg (E, inferred). Chords not published: root 6.0 ft, tip 2.5 ft (E) close the area. Eppler-type section, 13% t/c assumed (E).
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
| 184 | 8,000 | 240 | 17.8 | F | 216 | +17% | 1.55 | 159 | RAF plans spec, CP38, 75% |
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

### Engine fit with the Aeromomentum line

- **Power.** Two AM15T (160 hp each, 215 lb dry; grade F) replace two O-320s at 160 hp: the only design on the shortlist whose published power the Aeromomentum line matches directly. At the assumed 75% continuous rating that is 240 hp in cruise, the same as the brochure's 75% point.
- **Mass and CG.** Installed mass 2 x 304 lb against about 2 x 308 lb: -8 lb overall (E). Because the two engines sit at opposite ends, a revival can trim CG by choosing which installation carries the radiator. No ballast is expected, but it is not computed.
- **Cooling and installation.** Two liquid-cooled installations replace two updraft air-cooled ones that ran without cowl flaps. The rear engine's belly scoop overheated on at least one build (Twin & Turbine, 2026). A radiator in a ducted, Meredith-type installation is the obvious place to recover some of the 1.72 drag factor. That is not credited.
- **Props.** The plans forbade constant-speed props: the pilot cannot tell which engine has failed, and the aft prop risked fatigue (Rutan, Canard Pusher). A geared Aeromomentum engine changes the prop question, and the answer needs a design study, not an assumption.

### Rights and provenance (stage 2)

Open question, with a likely holder (Elon, `docs/rights/rutan-defiant.md`, PR #3, updated 2026-10-24). RAF sold its last plans and licensed its last builder in June 1985. **No 1985 rights buyer is on the record.** The one newsletter line that says rights "were sold" (Canard Pusher 54, 1988) is a reworded reprint of a 1985 paragraph that mentions no sale, and every other RAF and Rutan account says RAF stopped selling plans and kept its assets. The likely holder is therefore Rutan Aircraft Factory or Burt Rutan; that is an inference, not a document. What the holder owns is thin: the plans copyright (Fred Keller, who drew the homebuilder plans for a share of sales, may hold an interest), no type certificate, no live patent, no molds (moldless construction), and not the DEFIANT name, which Sikorsky and Lockheed Martin hold for aircraft. RAF called its end of licensing "final, official and irrevocable" (Canard Pusher 71), and Rutan wrote in February 2025 that he objects to unlicensed building from "bogus plans". So there is one identifiable, living party to approach, and his stance is on the record. The prototype N78RA is at the Hiller Aviation Museum. An attorney is needed on who holds the rights and on the Keller interest. Approaching anyone needs Bill's go-ahead.

### Safety record

Record (ASN and NTSB, lower bound): 6 US NTSB events 1997-2018 and 2 fatal, worldwide, on about 30 completed aircraft (about 20 active). The recurring item is the retractable nose gear: landings with it up or unlocked, and a collapse. RAF issued a mandatory nose-gear change in 1987 after three retract-link failures. One fatal accident was an aborted-takeoff overrun on a 2,160 ft turf strip; the NTSB quoted the owner's manual on the high wing loading needing longer runways. The other was a loss of control after a go-around, cause undetermined, with no engine anomaly. **No engine-out or asymmetric-thrust accident is on record**, which is the configuration's point. Sample too small for a rate.

### Why it died, and whether a revival fixes it

The 1979 certification programme lost its financing, and RAF stopped selling all plans in 1985 over liability. Neither applies to an experimental revival with a modern builder-support model. What does carry over: about 30 were completed from 176 plans sets, so the build was hard, and a revival has to fix that through manufacturing (stage 4).

### Not yet done

- Confirm whether RAF or Burt Rutan holds the rights, and whether Keller has an interest (attorney via Elon; any approach is Bill's call).
- Measure N78RA at the Hiller museum (canard, chords, cowls) if Bill approves contact; it would replace most of the estimated geometry.
- A drag study of the two cooling installations and the prop question (AERO, if it goes forward).
- The modern rebuild's empty weight (MANUFACTURING, stage 4): the plans prototype's 1,600 lb is the only figure.
- What a modern rebuild changes in mass, cost and build hours (MANUFACTURING, stage 4, AER-3784).

<!-- stage3:end -->

<!-- stage4:start -->

## Stage 4: what modern manufacturing changes (AER-3784)

Full study (lead design). Method, prices and sources are in [docs/MANUFACTURING.md](../MANUFACTURING.md); the weight table is generated by `docs/manufacturing/weights.py`. Desk study: nothing weighed or quoted by us, nobody contacted. Every E is our estimate.

**Original construction:** Rutan moldless: hand-laid E-glass over hot-wired full-depth foam cores, contour-filled with micro and sanded. No molds ever existed. It can still be reproduced (the materials are all on sale), but that is exactly the route that left about 30 finished from 176 plans sets.

**Modern route:** molded carbon in female molds (infusion or out-of-autoclave prepreg) on CNC-machined or printed plugs; sandwich skins on spars and ribs instead of full-depth foam; bought pultruded carbon spar caps; flat parts CNC-cut from bought sandwich panel; bought nose-gear actuator, wheels, brakes, gear bow and radiators.

**First, what to delete:** hot-wire templates and full-depth cores; micro contour fill; hand-laid bulkheads and consoles; builder-laid glass spar caps; the builder-made retract nose-gear mechanism (the recurring accident item); two sets of carburettors, magnetos, carb heat and mixture controls (EFI); two sets of air-cooled baffles; the vacuum system if fitted.

**Empty weight:** rebuild **1,360-1,620 lb**, useful load **1,330-1,590 lb** against stage 3's 1,350 lb. With our corrected engine credit (-60 to -32 lb; stage 3 had -8): 1,300-1,580 lb.

**Weight build-up:**

| Item | Light, lb | Heavy, lb | Basis | Grade |
|---|---|---|---|---|
| Starting empty weight | 1,600 | 1,700 | 1,600 standard (F, RAF via pilot report, 337skymaster.com/defiant.htm); 1,680 'equipped, as tested' (P, same report) and aeropedia.com.au (2019) also gives 1,680 lb (762 kg) in its general Defiant spec, not as a weighing of VH-DFY (F/secondary); Wikipedia 1,701. No weighed builder Defiant found | F/P/B |
| Wing, canard, winglets: full-depth hot-wired foam cores with wet-laid glass skins -> molded carbon sandwich skins on spar and ribs, pultruded carbon spar caps | -95 | -40 | Laminate and core arithmetic on AERO's wetted areas (287 ft2): removes 90-120 lb of full-depth foam, adds an inner face, light core and ribs. See the method section | E |
| Fuselage shell: wet-laid glass/foam sandwich -> infused carbon sandwich in female molds | -60 | -30 | 228 ft2 shell; 3 plies wet BID at 0.11-0.12 lb/ft2/ply against 2-3 plies infused 200 gsm carbon at 0.066 | E |
| Bulkheads, firewalls, consoles: hand-laid -> CNC-cut from bought carbon sandwich panel | -15 | -5 | about 40 lb of flat glass/foam parts; flat carbon panel about 35-60% lighter | E |
| Finish: micro contour fill and sanding -> in-mold surface, prime and paint | -55 | -25 | Moldless fill 0.06-0.12 lb/ft2 plus paint over 515 ft2, against molded surface paint only. CAFE weighed the moldless Cozy 12% over brochure, the molded IV-P 0.6% (R) | E |
| Panel: 1980s gauges, radios and vacuum system (if fitted) -> EFIS and current radios | -30 | -10 | Typical steam-to-glass saving; builders often spend it on an autopilot | E |
| Two EFI engines: backup battery and bus so each ECU has two power sources | +10 | +20 | Small battery, contactor, wiring per engine | E |
| Nose gear: plans retract -> bought actuator unit | +0 | +5 | Recurring accident item; bought for reliability, not weight | E |
| **Rebuild empty weight, no engine credit** | **1,360** | **1,620** | sum, rounded to 10 lb | E |
| Option, not in the total: Two in-flight adjustable or constant-speed props instead of fixed pitch | +20 | +50 | Plans forbade constant-speed props; a design study, not a manufacturing choice | E |

**Cost, hours, tooling, skill floor (detail and sources in [MANUFACTURING.md](../MANUFACTURING.md#rutan-defiant)):**

| | Original (moldless plans) | Modern one-off (moldless carbon) | Modern molded kit (10-25 unit run) |
|---|---|---|---|
| Builder hours | No RAF figure found; one build "took 15 years ... Some take 20" (P, AOPA Apr 2020); N171D 7,500-8,000 h (P) | 3,500-6,000 (E) | 2,000-3,500 (E) |
| Airframe change | baseline | -100 to -20 lb (E) | -245 to -85 lb (E) |
| Tooling | none | none | $100-300k (E) |
| All-in to fly | | $90-160k (E) | $140-240k (E) |
| Skill floor | High | High | Medium |

Engines 2x AM15T $35.4-37.6k (F, aeromomentum.com, 2026-10-24). The kit's tooling share drops below 10% of its price at about 10-40 airframes, about the size of the Defiant's historical market. A molded kit buys hours and weight, not cash.

**Rebuild questions:** two independent coolant loops, front radiator in the cowl inlet and rear in a ducted belly scoop. Prop choice stays open: the plans' ban on constant-speed props rested on failed-engine identification (now a display question) and aft-prop fatigue (a STRUCTURES question). Adjustable props are an option at +20 to +50 lb, not in the totals.

**Reproducibility:** whether the plans in builders' hands can lawfully seed a molded re-derivation is Elon's and an attorney's question (stage 2). Measuring N78RA at Hiller would replace most of the estimated geometry; contact is Bill's call.

**Home-shop route** ([MANUFACTURING.md](../MANUFACTURING.md#the-home-shop-route), tools about $20-49k, prices read 2026-10-24, all E): Home molds cost about 670 ft2 of mold surface, 1,300-2,700 h and $10-27k of materials. Total home-molded: 3,700-7,000 h and $59-91k, against a service kit at 2,000-3,500 h and $80-140k, at the same weight.

<!-- stage4:end -->
