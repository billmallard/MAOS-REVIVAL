# AER-3807 planform safety: desk research (public web only)

Scope: high AR (8-10) vs moderate AR (6-7) vs low AR (2-4, deltas) light aircraft, for a four-seat pusher.
Compiled 2026-10-24. Public web only; nobody contacted, nothing posted.

Grades: **P** = flight test / NACA-NASA report / magazine pilot report; **R** = accident record or database;
**F** = manufacturer or designer claim; **E** = estimate or theory (including my own arithmetic).
"PDF p." = page index in the NTRS/source PDF, not the printed folio. Every quoted string was copied from the fetched
text and re-checked against it by script (see end). Text marked **Inference** is mine, not the source's.

---

## 1. Stall character: low-AR wings and deltas vs conventional GA

| # | Finding (what the record says) | Source | Grade |
|---|---|---|---|
| 1.1 | Wind-tunnel tests of Clark Y wings at AR 0.5 to 3. Abstract: "marked delay of the stall and a decided increase in values of maximum lift coefficient ... for aspect ratios of the order of 1 as compared with values for aspect ratios of 2 and 3." (Zimmerman's low-AR work.) The PDF text layer is unreadable, so I have the abstract only. | Zimmerman, NACA TR-431 (1933). https://ntrs.nasa.gov/citations/19930091504 | P |
| 1.2 | Langley free-flight tunnel tests of delta models with 53, 63, 76 and 83 deg sweep. Summary: AR 2-3 models (53/63 deg) had "fairly good" stability and control, but "The power-off glide angles, however, were very steep at high lift coefficients." Models at AR 1 or below (76/83 deg) were unsatisfactory, either because of unstable rolling oscillations at high lift coefficients (wing rock) or because of excessive changes in static longitudinal stability (per the audit, the two failure modes belong to different models) (the summary sentence covers both; corrected after the audit). | McKinney & Drake, NACA RM L7K07 (Jan 1948), PDF p.2. https://ntrs.nasa.gov/citations/19930085777 | P |
| 1.3 | Same RM, model 2 (tailless, elevons). CLmax 0.84. As elevon-up deflection rose past max lift, the elevons became "virtually ineffective" at the stall, and "the mild roll off at the stall could not be controlled." Model 4: stable at the stall with recoveries "generally" possible, but "the model could not always be controlled in a stall although the roll-off was very slow." Leading-edge vortices were seen in smoke and with tufts. | NACA RM L7K07, PDF p.10 (vortex flow), p.12 (model 2), p.16 (model 4) | P |
| 1.4 | Low-speed static stability and roll damping of swept and unswept low-AR wings (bibliographic only; not read). | Tosti, NACA TN-1468 (1947). https://ntrs.nasa.gov/citations/19930082106 | P (not read) |
| 1.5 | Low-speed static stability and rolling characteristics of triangular and modified-triangular low-AR wings (bibliographic only; not read). | Jaquet & Brewer, NACA RM L8L29 (1949). https://ntrs.nasa.gov/citations/19930085542 | P (not read) |
| 1.6 | **FMX-4 Facetmobile (AR 1.07, tailless lifting body) flight test.** Table 4.0.2 gives "Stall:   No stall: stable mush." and minimum speed "Less than 33 knots". At full aft stick (about 30 deg AoA per tunnel data) it showed "a moderate high-frequency aerodynamic buffet, and a power-off sink rate of about 1000 feet per minute." Roll damping stayed stable, with "no tendency to roll off or depart". The pitot stalled at high AoA, so true minimum speed was not measured. The ¼-scale RC model, flown more aggressively, also showed spin resistance. 130 h flown 1993-95. **Caveat:** the designer wrote this report under a NASA grant. It is not an independent NASA test. | Wainfan & Nieubert, NASA LaRC grant NAG-1-03054 Task 01 Final Report (Feb 2004), PDF p.15-17; AR 1.07 on PDF p.20. https://wainfan.co/media/pavreport.pdf | P (designer-authored) |
| 1.7 | Same report, design argument: a properly configured low-AR planform sheds leading-edge vortices that "maintain stable roll damping to very high angles of attack (over 30 degrees)". | Same, PDF p.13 | E (designer theory) |
| 1.8 | **Verhees D2 (two-seat delta).** Designer, quoted in the magazine: "The delta wing is not so safe when it comes to stalls. [It] will first occur somewhere between half span and the tip, resulting in a wing dip and spin." The D2 counters this with a more elliptical planform and outboard elevons. Stall behaviour as reported: the aircraft shakes; at forward CG it mushes nose-high; at aft CG "a wing can dip"; stall AoA 30 deg. | Mark Phelps, Kitplanes, 19 May 2022. https://www.kitplanes.com/verhees-d2/ | F (designer statements in a magazine) |
| 1.9 | **Dyke Delta JD-2 (AR about 2.9).** The designer described the fully developed stall in the NTSB file as a mush "resulting in a high sink rate and temporary loss of control." Stall speed about 75 mph per the designer, 70-75 mph across sources. | NTSB LAX96LA003 via ASN https://aviation-safety.net/wikibase/41039 ; Kitplanes (Wanttaja, 25 Mar 2025) https://www.kitplanes.com/dyke-delta/ | R / F |
| 1.10 | **Conventional GA baseline (NASA Langley stall/spin program).** A low-wing, two-place, fixed-gear research airplane "tended to roll-off at the stall" (corrected after the audit: not the four-place airplane of TP-2691, and its baseline tail was low-mounted). Its four tail designs gave spins at 40-60 deg AoA and 145-208 deg/s, and some flat spins could only be recovered with the spin chute. | Stough, Patton, Sliwa, NASA TP-2644 (Feb 1987). https://ntrs.nasa.gov/citations/19870007382 | P |
| 1.11 | **Outboard leading-edge droop (the "cuff"), RC model and full-scale airplane.** The basic RC model rolled off at 1g and in accelerated stalls. A droop or flap on the outer 40% of the span let the model stall at full up elevator "without a tendency to roll off". Full-span droop "greatly reduced the resistance of the model to enter the flat spin mode" (it made spin resistance worse). | Chambers et al., NASA TP-1589 (Dec 1979), PDF p.49 (RC summary). https://ntrs.nasa.gov/citations/19800004771 | P |
| 1.12 | **Cuff full-scale flight test (low-wing four-place research airplane; "Piper-derived" removed after the audit, not in TP-2691).** Baseline: 173 spins from 209 attempts (83%). With the outboard modification: 13 spins from 244 attempts (5%). It would not spin at idle power or with flaps down, but did spin at max power with abused loadings. | Stough, DiCarlo, Patton, NASA TP-2691 (Jul 1987), PDF p.10 and abstract. https://ntrs.nasa.gov/citations/19870014181 | P |
| 1.13 | Tunnel data: outboard droop "eliminated the abrupt stall of the windtip [sic]" and kept the resultant-force coefficient rising up to about alpha = 32 deg, which the abstract links to spin resistance. | White, NASA CR-3636 (Nov 1982). https://ntrs.nasa.gov/citations/19830003779 | P |
| 1.14 | Rotary-balance data on 16 leading-edge modifications (the Yankee/AA-1-class "model A"). Data only, no analysis. | Bihrle & Mulcay, NASA CR-3102 (1979). https://ntrs.nasa.gov/citations/19800003810 | P |
| 1.15 | Cirrus SR20/22: the live Wikipedia "Leading-edge cuff" article says only that the SR20 was certified with the cuff (the earlier claim that the FAA accepted CAPS in place of spin testing is not on the page; withdrawn after the audit). I could not find a primary FAA or Cirrus document to confirm this. | Wikipedia "Leading-edge cuff" (search summary only, not verified) | F / not verified |
| 1.16 | **Canards (relevant to the pusher).** Full-scale and 0.36-scale canard GA tunnel work. At forward CG the configuration was "extremely stall-resistant". At aft CG and high power, extra pitch control plus reduced stability "overpowered the stall resistance provided by the canard, which led to a high-angle-of-attack, deep-stall trim condition." | Chambers, Yip, Moul, NASA TM-85760 (Apr 1984). https://ntrs.nasa.gov/citations/19840013471 | P |
| 1.17 | 0.36-scale canard pusher with winglets (VariEze-class). Removing the outboard leading-edge droop "degraded roll damping and produced lightly damped roll (wing rock) oscillations". Directional stability was weak. | Satran, NASA TP-2623 (Oct 1986). https://ntrs.nasa.gov/citations/19870000606 | P |
| 1.18 | Full-scale canard GA airplane in the 30x60 tunnel, AoA up to 41.5 deg. Variables included outboard droop, CG and water spray (rain). | Yip, NASA TP-2382 (Mar 1985). https://ntrs.nasa.gov/citations/19850011615 | P (abstract only) |
| 1.19 | Questair Venture: an outboard droop plus two chordwise slots gave "gentle, controllable stall characteristics" in full-scale flight test, with almost no wing rock on the free-to-roll rig. | Meyer, Yip et al., AIAA 89-2237. https://ntrs.nasa.gov/citations/19890060320 | P |

**Inference (section 1):**
- The flight and free-flight record supports these points for AR 2-3 deltas: gradual or mushing stall, high stall AoA (about 30 deg), and buffet warning (FMX-4, D2, RM L7K07).
- The same record says this benign behaviour depends on the configuration. Tailless deltas lose roll control at the stall (RM L7K07). Verhees calls a plain delta prone to a tip-first wing drop. The Dyke Delta mush brings "high sink rate and temporary loss of control".
- AR below about 1.5 adds wing-rock risk (RM L7K07).
- For conventional AR 6-7 wings, the NASA record shows roll-off at the stall is the norm. An outboard cuff cuts spin entry from 83% to 5% of attempts but does not remove it.
- I found no flight-test stall/spin data on AR 8-10 *powered* GA aircraft (as distinct from sailplanes).

## 2. Landing: attitude, sink, back side of the drag curve

| # | Finding | Source | Grade |
|---|---|---|---|
| 2.1 | Delta free-flight models: the large rise of drag with lift moved the minimum glide angle to "a fairly low lift coefficient (CL ~ 0.3) for the model instead of near the stall as with conventional models." Above that CL the elevator response reversed in transient (back side of the drag curve): a brief deflection caused one effect and holding it caused the opposite, which was "very troublesome to the pilot". | NACA RM L7K07, PDF p.10 | P |
| 2.2 | Verhees D2, designer's landing description: "Under [65 knots] the drag curve goes up again. When the speed drops to [54 knots] a lot of power is needed to maintain altitude and build up speed". Also "The D2 at 100 km per hour [54 knots] takes the same power as at 220 km per hour [120 knots]." Final approach 65 kt, a bit higher in turbulence. | Kitplanes, Phelps, 19 May 2022. https://www.kitplanes.com/verhees-d2/ | F |
| 2.3 | Dyke Delta: approach speeds of 100-110 mph and a stall of 70-75 mph. The touchdown configuration is "relatively nose-high". | Wikipedia (approach speed cited to Sport Aviation, Dec 2008) https://en.wikipedia.org/wiki/Dyke_Delta ; Kitplanes https://www.kitplanes.com/dyke-delta/ | F (secondary) |
| 2.4 | Dyke Delta ground attitude: the wing's trailing edge "leaves only a foot or so gap beneath it" during landing. No tail-strike accidents found in the records I located (see 3.x). | Kitplanes, Wanttaja, 25 Mar 2025 | P (magazine) |
| 2.5 | FMX-4: power-off sink about 1000 fpm at full aft stick (about 30 deg AoA). The designer argues low wing loading (3.45 psf, from Wikipedia) offsets the low CLmax and permits slow landings. The 1994 engine failure ended in a low-speed fence strike with no pilot injury. | NAG-1-03054 report PDF p.13, p.16; Wikipedia https://en.wikipedia.org/wiki/Wainfan_Facetmobile | P / E |
| 2.6 | Rohr 2-175 (delta, 1974; 2 flying prototypes, one with 23 flight hours). A history article says the delta "preferred a constant-attitude approach". Instead of a pronounced flare, the pilot held attitude and let it settle in ground effect. Test pilot Don Westergren's comments appear only in the author's paraphrase, not as quotes. A driveshaft coupling failed after takeoff and the aircraft landed undamaged. The programme ended for financial reasons. | Kapil Kajal, Vintage Aviation News, 25 Feb 2026. https://vintageaviationnews.com/warbird-articles/grounded-dreams/rohr-2-175.html | P (secondary history; weak) |
| 2.7 | Space Shuttle orbiter (extreme low-AR context): steep glideslope "approximately 19°", flown with speedbrakes, then a preflare to about 1.5 deg. Early orbital flights saw touchdown scatter from a "greater-than-predicted value of low-speed L/D". | Powers, NASA TM-85910 (Oct 1984), PDF p.8 and p.11. https://ntrs.nasa.gov/citations/19850001764 | P |
| 2.8 | Canard landing/takeoff (Long-EZ): "The touchdown comes at 65 mph or so as the main wing quits flying". An owner reports using "about half the length" of 3000-ft runways. The D2 article (Phelps's paraphrase of the designer, not a quote) says that with a pusher canard takeoff speed is higher than stall speed, compromising runway performance. | Kitplanes, LeRoy Cook, 24 Jul 2020 https://www.kitplanes.com/buying-used-long-ez/ ; Kitplanes D2 article | P / F |

**Inference (section 2):** Two sources describe the same back-side-of-drag-curve behaviour of low-AR deltas on approach: NACA free-flight work (1948) and a modern designer (Verhees). It leads to high approach speeds relative to stall (Dyke: about 1.4x Vs) and a nose-high touchdown. I found no record quantifying tail strikes for light deltas. A four-seat pusher would add prop ground clearance to the nose-high touchdown problem. That combination appears in no record I found, so it is a gap.

## 3. Accident record

### 3a. Dyke Delta JD-2: NTSB records located (Kitplanes says about 8 NTSB reports exist; about 38 ever registered, 15 active)

| Date | Reg | NTSB no. | Phase | Summary as recorded | Grade |
|---|---|---|---|---|---|
| 1983-10-04 | N55AK | MIA84FA003 | En route, 1 fatal | Witnesses saw it pitch down and spin into the ground. Wreckage showed wing bonding failures (non-adhesive bonding between first coat and fiberglass skin). Probable cause blank on ASN. 14 h airframe. | R https://aviation-safety.net/wikibase/40707 |
| 1992-08-21 | N78BS | SEA92LA185 | Landing, 0 fatal | Left main axle separated on touchdown; fatigue crack. | R https://aviation-safety.net/wikibase/363070 |
| 1995-10-21 | N515D | LAX96LA003 | Manoeuvring (test flight), 1 fatal | Slow-flight test after tip tabs were fitted; T-tail added against the design. The pilot had recorded stalls at 100 mph vs 75 mph intended. Probable cause: "Improper planning/decision by the owner/builder (pilot), which resulted in his failure or inability to recover from a stall/mush condition." Wreckage: vertical impact loads, low impact angle. 3 h airframe. | R https://aviation-safety.net/wikibase/41039 |
| 2025-07-22 | N71AW | (docket 200612) | Landing at AirVenture, 0 fatal | Tailwind landing about 2,500 ft down the runway, bounce, hard landing, runway excursion, gear collapse. Probable cause: failure to maintain control while landing with a tailwind. | R https://aviation-safety.net/wikibase/529230 |

The other roughly 4 records were **not found**: NTSB CAROL's API rejected my queries and WebFetch is blocked from ASN.
**Pattern (inference, tiny n):** 2 of 4 involve stall, spin or mush loss of control: one on a heavily modified airframe, one with structural bonding defects. 2 are landing or gear events. Too few to call a type pattern.

### 3b. Canard (VariEze / Long-EZ / Cozy class)

| Finding | Source | Grade |
|---|---|---|
| NTSB-based homebuilt analysis over a stated 10-year window, printed as "December 2007 through January 1998" (presumably 1998-2007). Pilot miscontrol causes about 39% of all homebuilt accidents; the canard rate is 10 points lower ("about 25% less often"). Airspeed-control causes about 10% for canards vs 16% for homebuilts overall. Judgment errors (e.g. fuel starvation) run a bit higher, so the overall pilot-error rate is about the same as all homebuilts. The fatal/total ratio for most canards is "about average". Long-EZ: about 42% of accidents in ground-handling phases. n = 25-30 accidents per type. | Ron Wanttaja, "Safety Is No Accident: Canards," Kitplanes, 10 Aug 2010. https://www.kitplanes.com/safety-is-no-accident-canards/ | R (secondary analysis of NTSB data) |
| Cozy Mk IV N96PJ, 1996, FTW97LA009: main wing stalled first, nose pitched up, pilot "unable to break the stall". Canard incidence too low, 3 of 6 vortilons removed, CG 1.1 in aft of the limit as fuel moved aft. Pilot survived. | https://aviation-safety.net/wikibase/356613 | R |
| Raven canard N79ZR, 2014, ERA14LA330: CG about 3 in aft of the limit, "deep, unrecoverable stall", about 6,000 fpm descent, 1 fatal. | https://aviation-safety.net/wikibase/167822 | R |
| Berkut N91DR, 1995, LAX95LA289: accelerated stall in an 8 g airshow turn at about 200 ft, left wing drop, 1 fatal. Designer: "no main wing stall has been induced" in flight test. | NTSB final report https://app.ntsb.gov/pdfgenerator/ReportGeneratorFile.ashx?EventID=20001207X04287&AKey=1&RType=Final&IType=LA | R |
| Cozy N84CZ, 1995, LAX95LA222: at max gross the takeoff felt "mushy" after rotation; aborted, overran a 3,061-ft runway. Probable cause: premature rotation, proper liftoff speed not reached. | https://aviation-safety.net/wikibase/133045 | R |
| Rain: the Long-EZ's original canard airfoil gave a nose-down "rain trim change". The 1985 Roncz R1145MS canard has "negligible rain trim, and rain adds only 2 knots to the stall speed" (Wikipedia, citing Canard Pusher No. 43, Jan 1985; primary not fetched). | https://en.wikipedia.org/wiki/Rutan_Long-EZ ; Kitplanes Cook 2020 confirms the trim change was "largely eliminated" | F (secondary) |
| Velocity late-1980s deep-stall accidents and wing modification: a Flying article is cited in search results but returned HTTP 410. **Not verified.** | - | not verified |

### 3c. Conventional GA stall/spin share

| Finding | Source | Grade |
|---|---|---|
| AOPA ASI "Stall and Spin Accidents: Keep the Wings Flying" (2017) covers 2000-2014, "more than 2,000" stall accidents. Fatal stall accidents fell by more than half from first to last year. "25 percent of all stall accidents occur in Experimental aircraft, although Experimentals only accounted for approximately 5 percent of all GA flight activity". Departure-phase stalls were fatal "about half the time". | AOPA, McSpadden, 1 Sep 2017. https://www.aopa.org/news-and-media/all-news/2017/september/pilot/number-crunching | R (secondary) |
| Same ASI report as relayed: stalls "were implicated in 10 percent of noncommercial accidents, yet resulted in nearly 24 percent of fatalities". (Primary PDF https://safepilots.org/wp-content/uploads/ASI-Stall_Spin.pdf returned 404, and the archive copy was truncated.) | Plane & Pilot, Frank Ayers, 3 Aug 2024. https://planeandpilotmag.com/avoiding-the-stall/ | R (secondary) |
| ASI phase data: about 25% of go-around stalls, 40% of takeoff/climb stalls and 54% of pattern stalls were fatal; base-to-final stalls 80% fatal. | AvWeb, Tom Turner, 22 Jan 2025. https://avweb.com/features/stalls-in-the-pattern/ | R (secondary) |
| Historical NASA framing: stall and spin accounted for "over 28 percent of the total number of fatalities" in GA (late 1970s, citing refs 1-2). | NASA TP-1589, PDF p.7 | R (as cited by NASA) |

Nall report figures: **not found** in fetchable form.

## 4. Engine-out glide ratio (L/D max) by type

| Type | AR (approx) | Max glide | Source | Grade |
|---|---|---|---|---|
| Stemme S10 (motorglider) | 28.3 | 50 | Wikipedia citing Jane's 2003-04. https://en.wikipedia.org/wiki/Stemme_S10 | F |
| Grob G109B (motorglider) | about 15.9 (E: 17.4²/19) | 28 at 62 kt; min sink 1.1 m/s | Wikipedia citing Jane's 1985-86. https://en.wikipedia.org/wiki/Grob_G_109 | F |
| Cirrus SR22 | about 10 | "Maximum Glide Ratio ~ 8.8 : 1", 92 KIAS at 3600 lb, prop windmilling, flaps up | SR22 POH glide chart (Fig 3-1), reproduced in FAASTeam resources PDF p.9 (the POH page number is not shown in the reproduction). https://www.faasafety.gov/files/events/SW/SW19/2025/SW19140688/That_Slow_Sinking_Sensation_Resources.pdf | F |
| Cessna 152/172 | about 7.5 | about 9.1 (E: 1.5 nm per 1,000 ft rule of thumb) | FAA Safety Briefing "Best Glide Speed and Distance," p.2. https://www.faasafety.gov/files/events/SO/SO15/2023/SO15120971/BestGlide.pdf | E (FAA rule of thumb) |
| Cessna 152 | - | 10.3 max L/D | NAG-1-03054 report, PDF p.34 (Wainfan's comparison) | E |
| Cessna 150 | 6.8 | plotted above FMX-4 at all speeds (Fig 5.0.1) | NAG-1-03054 report, PDF p.20 | P (designer) |
| Mooney M20J | - | Owner forum relays the POH as 1.8 nm per 1000 ft (about 10.9). **Not verified:** forum returned 403 and I did not see the POH. | https://mooneyspace.com/topic/28623-mooney-m20j-glide-ratio-and-distance | not verified |
| Long-EZ / Cozy | - | **not found** (no published glide ratio located) | - | - |
| FMX-4 Facetmobile | 1.07 | Below the C150 curve at all speeds; the numeric peak cannot be read from the text layer. The *proposed* AR 1.86 study airframe is estimated at max L/D 10.5 at 75 KEAS. | NAG-1-03054 report, PDF p.20, p.34 | P (FMX-4 curve) / E (study airframe) |
| Dyke Delta JD-2 | about 2.9 (E: 22.25²/173) | **not found**. Wikipedia says only that it "flew quite well in tow and in a glide" in NASA-funded tow tests (unsourced). | https://en.wikipedia.org/wiki/Dyke_Delta | - |
| Space Shuttle orbiter | about 2.3 | Numeric L/D **not confirmed** from a fetched primary source. Operational glideslope about 19 deg with speedbrakes (TM-85910). The ALT final report (JSC-13864) plots L/D but its text layer is illegible. | https://ntrs.nasa.gov/citations/19850001764 ; https://ntrs.nasa.gov/citations/19780011246 | P (glideslope only) |

## 5. Ride quality vs aspect ratio and wing loading

| # | Finding | Source | Grade |
|---|---|---|---|
| 5.1 | NACA gust-load formula. Peak gust acceleration is proportional to wing lift-curve slope (m) x rho0 x S x Ve x Ue x K / 2W, so it scales with the lift-curve slope and inversely with wing loading. The revised gust factor K depends on a mass-ratio parameter that itself includes the lift-curve slope. | Pratt & Walker, NACA TR-1206 (1954), PDF p.1-3. https://ntrs.nasa.gov/citations/19930090988 | P (theory validated on V-G data) |
| 5.2 | Experimental gust-tunnel evidence that a lower effective lift-curve slope cuts gust response. The 45 deg swept-wing model "would undergo a much lower acceleration increment than the same airplane with the equivalent straight wing." The increment tracked the straight-wing slope x cos(sweep). | Pierce, NACA TN-1528 (Feb 1948), PDF p.2. https://ntrs.nasa.gov/citations/19930082210 | P |
| 5.3 | Verhees D2 designer: behaviour in turbulence is "much nicer" than conventional aircraft; "In an updraft, most aircraft tend to raise the nose and the speed [drops]. A delta reacts the other way." | Kitplanes D2 article, 2022 | F |
| 5.4 | In a light twin (wing loading 32.2 psf; the report makes no wing-loading comparison, corrected after the audit), moderate turbulence felt "much worse" subjectively, but the ride-quality meter missed the low-frequency accelerations. | Stewart, NASA TP-2913 (1989). https://ntrs.nasa.gov/citations/19890013197 | P |
| 5.5 | Gust response extended to ultralights (wing loading about 5 kg/m²) vs small powered aircraft (about 50 kg/m²) vs jets. | R.T. Jones, NASA TM-X-73228 (1977). https://ntrs.nasa.gov/citations/19770017108 | E |
| 5.6 | Raymer textbook discussion and a Wainfan Kitplanes column on low-AR ride: **not found** online. | - | - |

**Inference (section 5):** By the NACA formula, a delta of AR 2-3 has a lift-curve slope roughly 40-60% of an AR 8-10 wing's (E, from standard finite-wing theory, not from a fetched source). At *equal wing loading* that should give proportionally smaller gust bumps. The low-AR light aircraft in the record, however, run very low wing loadings (FMX-4 3.45 psf). That works the other way, so the net ride benefit is configuration-specific. No flight-measured comparison of ride vs AR in light aircraft was found.

---

## Biggest gaps
1. No flight-test stall/spin data for **AR 8-10 powered GA**. No **four-seat delta or low-AR pusher** has a test record beyond the Dyke Delta (tractor, plans-built).
2. Dyke Delta NTSB set is incomplete: 4 of about 8 records found. CAROL API queries failed.
3. Glide ratios not found for Long-EZ, Cozy, Dyke Delta, or the FMX-4 as a number. Shuttle L/D not confirmed. Mooney figure not verified.
4. Primary AOPA ASI stall report and Nall report not retrieved; figures are via AOPA, AvWeb and Plane & Pilot.
5. No measured ride-quality comparison across aspect ratio; only formula and gust-tunnel evidence plus one designer claim.
6. Cirrus cuff certification basis, Velocity deep-stall history, and the Canard Pusher rain data not confirmed from primary sources.

## Quote check
Every quoted string above was matched by script against text I fetched in this session (NTRS PDFs via pypdf, NTSB PDF, ASN, Kitplanes, AOPA, AvWeb, Plane & Pilot, Wikipedia, Vintage Aviation News). Result: all quotes matched. Some needed a manual check because the scanned NACA reports have OCR damage in the text layer: RM L7K07 ("lif~", "co~ld"), TN-1528 ("a irp lane"), the FMX-4 report ("high -frequency"), and a line-break hyphen in TM-85910. The Plane & Pilot quote was matched against the page fetched by curl. "windtip" is the spelling in the CR-3636 abstract. I did not cite the Flying (Garrison 2019) Dyke Delta article: the body is paywalled, and the visible summary is a sponsored "Key Takeaways" box.
