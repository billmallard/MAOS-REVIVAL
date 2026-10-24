# Wheeler Express: stall and yaw record, tail study, market failure

Stage 3 revision (AER-3783, 2026-10-24), from Bill's review. The dossier
(`docs/candidates/express-2000.md`) carries the reading; this folder carries the
evidence and the arithmetic.

- `tail_study.py`: directional stability built up from fin area, CAFE's stall
  speeds scaled to weight and bank, and the cruise cost of each tail fix through
  the stage 3 Express model. Run it from the analysis workspace, where it finds
  `perf.py`, the model and the wetted areas:
  `python3 tail_study.py > tail_study_output.md`.
- `tail_study_output.md`: its output, reproduced below.
- The desk research that follows was done by a delegated research agent and
  reviewed by AERO; quoted strings were re-fetched and matched against their
  sources before commit. Public sources only; nobody was contacted.

## Tail study output

Fin lift slope 1.98 /rad; fuselage Cn_beta -0.0764 /rad (-0.00133 /deg); fuselage volume 226 ft3 (E)

| Fin area, ft2 | Vertical tail volume Vv | Cn_beta fin, /deg | Cn_beta total (fuselage + fin), /deg | Reading |
|---|---|---|---|---|
| 10 | 0.035 | 0.00120 | -0.00014 | near neutral or unstable |
| 12 | 0.042 | 0.00144 | 0.00010 | near neutral or unstable |
| 14 | 0.049 | 0.00168 | 0.00034 | near neutral or unstable |
| 16 | 0.055 | 0.00192 | 0.00058 | weak |
| 18 | 0.062 | 0.00216 | 0.00082 | weak |
| 20 | 0.069 | 0.00240 | 0.00106 | typical light single |
| 22 | 0.076 | 0.00264 | 0.00130 | typical light single |
| 24 | 0.083 | 0.00288 | 0.00154 | typical light single |
| 26 | 0.090 | 0.00311 | 0.00178 | strong |

CAFE clean 67.1 KCAS, full flap 58.4 KCAS

| Weight, lb | Bank | Clean stall, KCAS (CAFE basis) | Full-flap stall, KCAS (CAFE basis) | Kit-maker Vs1 scaled, kt |
|---|---|---|---|---|
| 2,865 | 0 deg | 67 | 58 | 55-58 |
| 2,865 | 30 deg | 72 | 63 | 59-62 |
| 2,865 | 45 deg | 80 | 69 | 65-69 |
| 2,865 | 60 deg | 95 | 83 | 78-82 |
| 3,200 | 0 deg | 71 | 62 | 58-61 |
| 3,200 | 30 deg | 76 | 66 | 62-66 |
| 3,200 | 45 deg | 84 | 73 | 69-73 |
| 3,200 | 60 deg | 100 | 87 | 82-87 |

| Fix | KTAS at 195 hp, 8,000 ft | Change |
|---|---|---|
| Baseline (stage 3 model; fin 12 ft2 is our estimate) | 178.5 | +0.0 kt |
| Fin enlarged to 20 ft2 (+8 ft2 planform) | 176.6 | -2.0 kt |
| Fin enlarged to 24 ft2 (+12 ft2) | 175.6 | -2.9 kt |
| Dorsal fin, about 3 ft2 | 177.9 | -0.7 kt |
| Ventral fin, about 3 ft2 | 177.8 | -0.8 kt |
| S-90 style tail: 40% more tail wetted area (CAFE; NTSB) | 175.5 | -3.0 kt |
| S-90 tail plus dorsal and ventral | 174.2 | -4.3 kt |

---

## Desk research: Wheeler Express family: stall/yaw record and market failure (desk research, AER-3783)

Scope: Wheeler Express / Express FT / Express CT (cruciform tail), Auriga / Series 90 / Express 2000 FT, ER, RG, RGT (larger conventional low tail). Public sources only. Nobody was contacted. Researched 2026-10-24.

Grades: **F** factory/designer/kit maker. **T** type certificate (none exists; the type was never certificated). **P** flight test, POH, magazine pilot report or NTSB/foreign-authority final report. **B** builder/owner/registry, including builder-forum posts and NTSB records of conversation with owners. **L** low (wiki, aggregator, ASN). **E** our own estimate, with the method stated.

Quotation marks mark verbatim text from the cited URL. Everything else is paraphrase.

Short names for the most-cited sources:

- **CAFE**: CAFE Foundation / EAA Aircraft Performance Report, Express N360EZ, flown Sept 1997. https://www.kitplanes.com/wp-content/uploads/2025/04/Wheeler-Express-APR-CAFE-Foundation.pdf (P). The same report is docket item 6 of CEN15FA321.
- **NTSB-PDF(mkey)**: `https://data.ntsb.gov/carol-repgen/api/Aviation/ReportMain/GenerateNewestReport/<mkey>/pdf` (final or preliminary report). Docket: `https://data.ntsb.gov/Docket?ProjectID=<mkey>`. The mkeys are listed in the accident table.
- **AOPA 1990**: AOPA Pilot, August 1990, pp. 100-104, Wheeler Express pilot report (the first page is missing from the scan). https://aeroresourcesinc.com/uploads/199008-1990%20Wheeler%20Express%20Homebuilt.pdf (P)
- **EDI 1995**: Express Design Inc. letter to all builders (22 Feb 1995), with "Preliminary Findings: Express Flight Characteristics - Pitching" (18 Feb 1995) and "Operational Recommendations". NTSB docket WPR17FA185, item 4: https://data.ntsb.gov/Docket/Document/docBLOB?ID=40477084&FileExtension=.PDF&FileName=EDI%20Letter%20to%20Owners-Master.PDF (F; scanned, and the OCR is poor in places).
- **WTI 1991**: Wheeler Technology Inc. letter of 15 March 1991. NTSB docket WPR17FA185, item 5: https://data.ntsb.gov/Docket/Document/docBLOB?ID=40477085&FileExtension=.PDF&FileName=Wheeler%20Express%20Letter%20to%20Owners-Master.PDF (F)
- **EBF-n**: old Express Builders Forum thread n, https://express-builder.com/old/forum/messages/1/n.html (B; thread 1568 is under /messages/29/).

---

## A. The stall and yaw problem

### A1. Grand Prairie (KGPM): identified

| Item | Value | Grade | Source |
|---|---|---|---|
| NTSB number | **CEN21LA096** (mkey 102446), Class 3, final report published 07/12/2022 | P | NTSB-PDF(102446) |
| Date / time | 21 Dec 2020, about 1452 CST | P | same |
| Aircraft | **N772BM**. NTSB make Express, model CT. Serial BMX101, built 2007. Lycoming IO-540-C4B5, 250 hp. Fixed tricycle gear. Destroyed by impact and fire. The NTSB record gives a certified max gross weight of 12,499 lb (an evident placeholder). | P | same |
| Tail type | Not stated anywhere in the NTSB report or docket. The CT designation is the cruciform-tail version in EDI's usage: EDI 1995 says it calls the early design the Express CT because of its cruciform tail (paraphrase of a poor OCR). Jane's says the same: "CT and FT have cruciform tail; 2000 has larger, conventional tail unit". So the tail was probably cruciform. This is not confirmed by the NTSB, and owners did convert CTs to the S-90 tail. | E (from F + L) | EDI 1995; https://janes.migavia.com/usa/express/express.html |
| Occupants | 2 fatal. The pilot was private, age 65, about 1,564 h total and 1,491 h in make/model (estimated), on BasicMed. The right-seat passenger, age 71, was also a private pilot. | P | NTSB-PDF(102446) |
| Flight | Departed runway 17 at GPM for Denton (DTO). Day VMC. Wind 160° at 6 kt, 22 °C, clear. | P | same |
| Phase | CAROL sequence: Maneuvering, loss of control in flight (defining event), then aerodynamic stall/spin, uncontrolled descent, collision with object. NTSB text: "during the departure turn". ASN codes it "Initial climb". | P / L | NTSB-PDF(102446); https://aviation-safety.net/wikibase/245904 |
| Turn direction | **Right.** The pilot requested a right turn after takeoff, and the tower approved it. The tower then told him to keep the turn tight to stay out of Arlington (GKY) airspace. | P | NTSB-PDF(102446); docket memo of record https://data.ntsb.gov/Docket/Document/docBLOB?ID=13873488&FileExtension=pdf&FileName=Memorandum%20of%20Record%20-%20History%20of%20Flight-Rel.pdf |
| Track | The NTSB track plot shows the departure off runway 17 followed by a continuous climbing right turn of roughly 180° back toward the north. The track ends near SH-360. | P (our reading of the plot) | https://data.ntsb.gov/Docket/Document/docBLOB?ID=13803854&FileExtension=pdf&FileName=Plot-Rel.pdf |
| Witness 1 (flight-school owner on the ramp) | "After takeoff the aircraft turned right crosswind and started a turn to the north for a right downwind departure." The bank angle increased significantly and the aircraft entered a steep dive. The engine then came up to what sounded like full power. "It appeared to me that the plane may have entered an accelerated stall while trying to avoid entering Arlingtons airspace." | P (docket) | https://data.ntsb.gov/Docket/Document/docBLOB?ID=13802377&FileExtension=pdf&FileName=Witness%20Statement_Redacted-Rel.pdf |
| Witness 2 (acquaintance of the pilot) | Paraphrase; the document is an image with no text layer. The takeoff run used a lot of runway and the airplane struggled into the air in ground effect. It wallowed to the right a couple of times before climbing out. The pilot then throttled back to what sounded like cruise-climb power, and later what sounded like full power was added. | P (docket) | https://data.ntsb.gov/Docket/Document/docBLOB?ID=13872244&FileExtension=pdf&FileName=Another%20Witness%20FW_%20N772BM%20accident.%20_Redacted-Rel.pdf |
| Probable cause | "The pilot’s loss of airplane control during the departure turn, which resulted in an aerodynamic stall and impact with terrain." Findings: aircraft control (pilot); airspeed not attained/maintained; angle of attack capability exceeded. No mechanical anomaly. Diphenhydramine was found in both occupants but judged unlikely to have contributed. | P | NTSB-PDF(102446) |
| Not in the record | Weight, c.g., flap setting, airspeed, and any flight data. | - | - |

The owner described the problem as a tendency to bite in with the stall in climbing right turns. This event fits that description: a stall in a tightened, climbing right departure turn. It is the only KGPM Express event in CAROL.

### A2. CEN15FA321 (Holland MN, 27 Jul 2015, N3FC, 3 fatal), read in full

Sources: NTSB-PDF(91647), docket https://data.ntsb.gov/Docket?ProjectID=91647 (P).

- **Aircraft.** Completed by the pilot in Aug 2008 (serial 1001) with a cruciform tail. Lycoming IO-540-C4B5, 260 hp; MGW 3,200 lb. Pilot: 1,204 h total, 475 h in the airplane.
- **Flight.** A local flight. The airplane made maneuvers at 2,100-3,400 ft, climbed, turned right overhead Holland at 6,600 ft, and entered a rapid descent overhead the site at 6,200 ft.
- **Chelton EFIS data (1 Hz, docket item 5).** The data show the airplane pitched to 34° nose-up at low rpm. IAS decayed to 48 kt in a 47° right bank. As the right bank steepened, rpm rose. Pitch went to 84° nose-down, and the airplane entered an upright right-turning spin to impact. Our reading of the docket table (https://data.ntsb.gov/Docket/Document/docBLOB?ID=40440606&FileExtension=.PDF&FileName=Chelton%20EFIS%20Data%20-%20End%20of%20Flight-Master.PDF): rpm about 1,000-1,190 at the stall (20:12:31-35), then 1,920 at 20:12:36 as bank passed 88°. Flaps were up. The flight manual Vs1 was 55 kt IAS (NTSB), and the builder checklist gives Vs1 55 kt / Vso 51 kt (docket item 7). The EFIS has no sideslip or yaw-rate channel in the docket table.
- **Analysis text on the design.** Earlier flight testing of a similar kit airplane "had poor yaw stability at low airspeed due to the aerodynamic design of the tail section", and in post-stall/high-yaw maneuvering the horizontal tail and elevators appeared to have an inadequate effect (P).
- **Probable cause.** The pilot's failure to maintain airspeed in a high-pitch, steep right turn, exceeding critical AOA. "Contributing to the accident was the airplane’s design, which resulted in poor yaw stability at low airspeed." Finding: "Yaw control - Related operating info" (P).
- **Engineering comparison cited.** The only one is the 1997 CAFE/EAA/FAA performance report, which the NTSB put in the docket. The NTSB did no testing, simulation or analysis of its own. It repeats CAFE: "the 'cruciform' tail (mid-mounted horizontal stabilizer), wide tapering fuselage, and highly swept vertical stabilizer combined to produce low yaw stability". It also repeats that the variant developed by about 17 owners had the same wing and fuselage and a tail with 40% more wetted area (P).
- **Tail dimensions given by the NTSB.** None. It gives only the "40% more wetted area" figure.
- **Docket contents.** Accident-site photos, witness statement, ATC tracks, EFIS data, the CAFE article, the in-flight checklist with stall speeds, toxicology, and a recorder specialist's report. There is no FAA, kit-maker or aerodynamic study.
- **Witness.** The aircraft spun 1 to 1.5 turns nose-down, and he heard the engine sputter twice (P, docket item 2).

The NTSB repeated this design language in **WPR17FA185** (Madras OR, 19 Aug 2017, N246TM, Express CT, cruciform, 1 fatal; NTSB-PDF(95839)). That report quotes the 1991 Wheeler and 1995 EDI letters (see A5) and the CAFE blanking finding. Its analysis says the tail "may stall on approach and turbulent conditions or upon crossing another airplane's wake (or its own wake in a turn)" and that "rapid action must be taken to avoid diving straight into the ground". It concludes that the pilot likely exceeded critical AOA turning base to final (a steep left turn) (P).

### A3. Accident table (all Express-family events found)

Method: CAROL search through the public CAROL web app's API at api.ntsb.gov/searchpub (Make/Model contains Express, Wheeler, Auriga, S90, FT-210, 2000RG/ER/FT). Every hit's narrative was checked, and non-Express hits (Kitfox, RV, etc.) were dropped. Added to that: the ASN type list https://aviation-safety.net/asndb/type/EXPR and ASN wikibase pages (L), and the Swiss BFU report for HB-YMN. The NTSB-PDF/docket mkey is in brackets. "Tail": C = cruciform (FT/CT/original); L = larger conventional low tail (Auriga/S-90/2000); ? = not established.

LOC-flag column:
- **HP** = stall/LOC at low speed with high or climb power, in takeoff, climb-out, go-around or a departure turn.
- **LS** = other low-speed stall/LOC.
- **PL** = stall/LOC after a power loss.
- **-** = not a stall/LOC event.

Direction is given only where the source records it.

| Date | Reg (variant, tail) | Report no. [mkey] | Phase | Fatal | Cause category | LOC flag | Turn/roll direction as recorded | Grade |
|---|---|---|---|---|---|---|---|---|
| 1989-10-26 | N200EX (Express 100, factory demo #1, C) | LAX90DUD01 [26527] | Cruise/forced landing | N (2 minor) | Engine failure (piston pin plug, con rod); landed in a residential area | - | n/a | P |
| 1990-07-25 | N210EX (FT-210, factory demo #2, C) | SEA90FA146 [41119] | Unknown/en route to Oshkosh | Y (3; CAFE and Kitplanes say 4) | LOC: "FAILURE OF THE PILOT TO MAINTAIN CONTROL OF THE AIRCRAFT AND/OR CORRECT THE STALL/SPIN." The witness saw a spin. The pilot had reportedly talked of aerobatics. | LS (spin) | Not recorded | P |
| 1995-09-14 | N360EZ (Express, C) | LAX95LA336 [29218] | Takeoff/initial climb, first flight | N | Premature rotation, inadvertent "departure stall", settled from about 12 ft | HP | Not recorded | P |
| 1997-03-21 | VH-PNK (Express 260) | ATSB 199700909 (via ASN) | Landing | N | Nose gear collapse | - | n/a | L |
| 1998-04-11 | N311RS (Auriga, L) | MIA98LA130 [38496] | Approach after power loss | Y (1) | Boost-pump O-ring leak and power loss. Steep banks, then "rolled rapidly to the left to an inverted position" | PL | Left roll | P |
| 1998-04-20 | N12EX (Express; owner calls it a CT on EBF-1184, C) | MIA98LA138 [38502] | Landing flare | N | Added power in the flare, veered left, loss of directional control | - | Veered left (ground) | P |
| 2000-07-01 | N521MC (Express/FT, C) | CHI00LA219 [49814] | Landing roll | N | Brake pedals obstructed | - | n/a | P |
| 2000-07-29 | N540EX (Express 90, L) | LAX00LA282 [49848] | Landing roll | N (3 serious) | Loss of directional control; became airborne again, trees, fire | - | Not recorded | P |
| 2002-11-19 | N297JH (homebuilt "Express", s/n 129; Wheeler lineage not stated by NTSB) | MIA03LA019 [56095] | Cruise/maneuvering after leaving the pattern | Y (3) | Engine surging and power loss (undetermined), then a stall. Witness: the airplane "entered a right bank" and spun clockwise for 2 turns or fewer | PL | Right / clockwise | P |
| 2003-01-09 | N113YE ("Bluegrass Express", based on Wheeler design) | CHI03LA236 [57686] | En route | Y (1) | Undetermined; wreckage found 6 months later | - | n/a | P |
| 2003-07-27 | N512EA (Auriga FT, PT6 turbine, new wings; "started out life as a S90" per EBF-1030; L) | CHI03LA227 [57595] | Initial climb | Y (1; pilot was president of Express Aircraft Co LLC) | Turbine power loss (fuel pressure). "After takeoff, the airplane went into a right bank turn". Recorded airspeed was below stall speed | PL | Right | P |
| 2004-06-18 | N625J (Express 2000, L) | CADORS 2004O0813 (via ASN) | Go-around at full power | N | Drift in the flare. Go-around with full power and nose raised: stalled at about 25 ft with the left wing dropping to near 90° bank | HP | Left wing drop | L |
| 2006-02-16 | N410MP (Express, Wheeler kit per NTSB) | DFW06LA071 [63241] | Approach | N | Power loss, undetermined | - | n/a | P |
| 2006-08-04 | N554SB (NTSB "Express FT"; owner called it "my CT Express" with an IO-540, EBF-694/828; C) | CHI06WA248 [69165] (Canadian jurisdiction) | About 1 min after takeoff, returning for an unknown emergency | Y (1) | Unknown (ASN: crashed attempting to return) | Unknown | Not recorded | L / P (prelim) |
| 2007-04-16 | N456TS ("Terrair Express", s/n CT101, IO-550, 4-blade; Express lineage not confirmed) | MIA07LA077 [65595] | Base-to-final turn, Sun 'n Fun | Y (2) | Stall in the base-to-final turn after overshooting | LS | **Conflicting:** right base for 27R; witnesses describe both a bank "to the left" and a "turn hard to the right" | P |
| 2007-04-21 | N37CA (Exp 2000, L) | MIA07LA085 [65631] | Base leg | N | Fuel-pump contamination, power loss, ditched | - | n/a | P |
| 2007-07-23 | HB-YMN (Express 2000 ER, L; IO-580) | Swiss BFU 2050; NTSB DEN07WA125 [66297] | Takeoff, record attempt | Y (1) | Take-off mass 2,602 kg against the kit-maker MTOM of 1,542 kg; c.g. 35.8% MAC against a limit of 35.4%. Could neither accelerate, climb nor turn; hit a house 3.8 km out | - (performance, not stall) | No turn made | P (https://www.sust.admin.ch/inhalte/AV-berichte/2050_d.pdf) |
| 2009-12-12 | N93HE (Express, s/n 143) | Bahamas AAIPU; NTSB ERA10WA096 [75160] | Short final, Chub Cay | Y (1) | Pilot loss of control (ASN summary of the AAIPU report) | LS | Not recorded | L |
| 2010-08-18 | LV-X410 (Express) | JIAAC (via ASN) | En route | N | Engine failure | - | n/a | L |
| 2014-06-13 | N55GM (Auriga, L) | WPR14FA243 [89433] | Night approach to unlit runway | Y (2) | LOC; methamphetamine | LS | Not recorded | P |
| 2014-07-16 | N234VV (Auriga, L; Subaru) | ERA14LA342 [89670] | Final | N | Fuel exhaustion | - | n/a | P |
| 2015-02-11 | N564ER (Wheeler Express; IO-540-S1A5, 300 hp) | CEN15FA141 [90715] | Forced landing after power loss | Y (2) | Power loss, then LOC; flown with known engine problems | PL | Not recorded | P |
| 2015-05-29 | N44508 (2000 RG turbine, L) | WPR15LA179 [91316] | Landing roll | N | Main gear collapse | - | n/a | P |
| 2015-07-27 | N3FC (Wheeler Express, C) | CEN15FA321 [91647] | Maneuvering, high pitch | Y (3) | Stall/spin. **Design named as contributing** | LS (power rising during the departure) | Right turn, right spin | P |
| 2016-02-27 | N58PP (Express FT) | none (ASN, news) | Landing | N | Nose gear collapse | - | n/a | L |
| 2016-12-26 | N176PA (Express S-90, L) | WPR17FA041 [94530] | Initial climb | Y (2) | Abnormally steep takeoff climb, then "a sharp right turn", then LOC. Reason for the turn/roll undetermined | HP | Right | P |
| 2017-08-19 | N246TM (Express CT, C) | WPR17FA185 [95839] | 3-mile left base to final | Y (1) | Stall in the base-to-final turn. NTSB cites the cruciform-tail letters | LS | Left ("steep left turn") | P |
| 2019-04-22 | N625J (Express Series 2000, L; IO-550-N) | ERA19FA154 [99295] | Maneuvering, shortly after departure | Y (1) | LOC. Witness: "the right wingtip was down", then it "rolled quickly inverted". Throttle found at idle | LS | Right wing down, then rolled inverted | P |
| 2019-08-07 | N43FD (Express Series 2000, L; IO-550-N1B) | WPR19FA212 [100013] | Short final (right traffic) | Y (2) | Stall about 40 ft above ground. Witness: it "pitched up, entered a descending right bank" | LS | Right | P |
| 2019-12-29 | N55EX (Express) | JIAAC (via ASN) | En route | N | Engine failure | - | n/a | L |
| 2020-08-14 | N505JS (Auriga, L) | CEN20LA342 [101806] | Climb, then forced landing | N | Power loss, undetermined | - | n/a | P |
| 2020-09-08 | C-GEWF (Auriga S90, L) | TSB (via ASN) | Takeoff roll | N | Uncommanded pull to the right; late abort, overran | - | Right (ground) | L |
| **2020-12-21** | **N772BM (Express CT, probably C)** | **CEN21LA096 [102446]** | **Departure turn after takeoff** | **Y (2)** | **Stall in a tightened climbing departure turn** | **HP** | **Right** | P |
| 2022-05-30 | N44508 (Express 2000RG, PT6A-20, L) | CEN22FA216 [105145] | Initial climb, then return to field | Y (1) | Power loss and in-flight fire. In the turn to a field the airplane banked about 75° right with pitch rising to 11°, then an accelerated stall | PL | Right (video: near-vertical descent with right roll) | P |
| 2023-04-24 | N92734 ("EDI Express", TIO-540) | WPR23LA165 [107122] | Takeoff roll | N | Directional control; drifted left, right rudder and brake insufficient | - | Left (ground) | P |
| 2024-08-08 | C-FJLJ (Wheeler Express CT, 1994, C) | TSB (via ASN) | A few feet after takeoff | N | Pilot lost control and hit the runway nose-down | HP | Not recorded | L |
| 2025-05-05 | N519EA (Express 2000 FT, L; kit maker per FAA registry: Express Aircraft Inc) | ERA25FA195 [200109] (preliminary) | En route, convective weather | Y (1) | Erratic flight path in heavy precipitation; the pilot reported difficulty controlling the airplane. Impact about 15° nose-low "while in a right turn"; throttle full open | - (weather/LOC, pending) | Right (at impact) | P (prelim) |

Counts (E, from the table):
- **Fatal accidents.** 19 fatal Express-family accidents with 31 deaths, 1990-2025, including N456TS. Without N456TS, whose lineage is unconfirmed: 18 accidents and 29 deaths.
  - This supersedes the repo's earlier figure of 13 fatal accidents and 21 killed, which missed MIA98LA130, MIA03LA019, CHI03LA227, CHI03LA236, MIA07LA077 and WPR14FA243.
  - SEA90FA146 is counted as 3 deaths, the NTSB figure.
- **Stall/LOC events (LS/HP/PL rows).** 18 in total, 15 of them fatal. Regina 2006 (cause unknown) and ERA25FA195 (weather, preliminary) are excluded. Of the 18:
  - Turn or roll direction recorded as **right**: 8. These are CEN15FA321, WPR17FA041, CEN21LA096, WPR19FA212, CEN22FA216, MIA03LA019, CHI03LA227 and ERA19FA154.
  - Recorded as **left**: 3. These are MIA98LA130, WPR17FA185, and the Oshawa 2004 wing drop.
  - **Conflicting**: 1 (MIA07LA077).
  - **Not recorded**: 6. These are SEA90FA146, LAX95LA336, Chub Cay 2009, WPR14FA243, CEN15FA141 and Chicoutimi 2024.
- **Of the 8 right-turn events:**
  - 3 followed a power loss (MIA03LA019, CHI03LA227, CEN22FA216).
  - 2 were right turns that ATC or the pattern required or approved (CEN21LA096 departure, WPR19FA212 right traffic).
  - ERA25FA195 (excluded above) also ended in a right turn.
- **High-power, low-speed takeoff/climb/go-around events (HP).** 6: LAX95LA336, Oshawa 2004, WPR17FA041, CEN21LA096, Chicoutimi 2024, and Regina 2006 (unknown). Direction is recorded as right in 2 (WPR17FA041, CEN21LA096) and left wing drop in 1 (Oshawa); it is not recorded in the rest.
- **By tail type.** Both tail families appear among the stall/LOC events. C: SEA90FA146, CEN15FA321, WPR17FA185, CEN21LA096 (probable). L: WPR17FA041, ERA19FA154, WPR19FA212, CEN22FA216, MIA98LA130, CHI03LA227, Oshawa 2004.
- **Fleet.** About 100 Express-family aircraft have been on the FAA registry and about 55 are active. Kitplanes: "About 100 examples have been added to the FAA registry, of which about 55 are still active." (L; https://www.kitplanes.com/wheeler-express-yesteryears-homebuilts/)

### A4. Handling, tail and wing data

**Flight test and pilot reports (P)**

- **CAFE 1997 (N360EZ, cruciform, IO-360-ES 210 hp, 2,895 lb gross).**
  - *Yaw damping.* Doublets showed low damping, rudder free and fixed: "It would overshoot 4-5 times before returning to steady conditions." Pitch damping was deadbeat. Spiral stability was neutral.
  - *Adverse yaw.* 15° with the right aileron down and only 2° with the left aileron down.
  - *Roll due to yaw at 120 kt.* Near the end of left-rudder input the airplane entered an uncommanded pitch-down "without yaw recovery in spite of neutralizing the rudder".
  - *Stalls.* Buffet 5-7 kt before the stall, then a slow nose drop. After 1 g clean stalls there was an "uncommanded right yaw with inadequate elevator control" until 85 kt panel IAS.
  - *Rudder travel.* Rudder travel of 26° per the manual "seemed to set up a partial stall of the vertical fin". Tuft/video tests by the owner had shown poor flow over significant portions of the vertical tail.
  - *Horizontal-tail blanking.* The horizontal tail and elevators were blanked by the fin at high yaw. In uncoordinated flight at 120 kt the elevator ran out and the nose pitched down. Recovery came at about 130 kt.
  - *Retest at 20° rudder stops* (the manual allows 20°). The same characteristics appeared to a lesser degree, and the elevator could hold the nose even at full rudder.
  - *Pitot-static.* The panel ASI read more than 14 kt below CAS at minimum speed and about 5 kt high at cruise. The static ports were on the pitot-tube wall and were AOA-sensitive. Panel/CAS pairs: 63 kt/75.6 mph, 71/81.8.
  - *Stall speeds (CAS).* Clean 77.2 mph at 2,865 lb; full flap 67.2 mph at 2,863 lb. Supplier figures: Vs1 58 kt, Vso 55 kt.
  - *Climb.* The published Vy (70-78 kt panel) overheated the engine. CAFE used 95-98 kt; Vy measured 98 kt panel = 116 mph CAS.
  - *Fuel.* The test pilot noted that the 92 gal tankage tempts high take-off weights.
- **AOPA Pilot, Aug 1990 (demonstrator #2, N210EX, the airplane later lost in SEA90FA146).**
  - Stalls described as anticlimactic: the airplane bobs and shudders before the break, and relaxing back pressure recovers it at once.
  - Not tenacious in returning to trimmed speed. Steady in 60° turns: "as stable as a Swiss bank account once set into turns". Quick pitch response; the evaluator overcontrolled at first.
  - The company said the cruciform tail placement aids spin recovery.
  - Elevator trim only. Wing 126 sq ft laminar.
  - The tail had just been changed for airplane #2: a horizontal stabilizer and elevator of greater span, and the fin leading edge moved forward of the stabilizer junction. Wheeler claimed improved aerodynamics and greater pitch authority.
  - Kit-maker figures: Vs1 55 KIAS, Vso 50 KIAS, Vy 70 KIAS, Vx 59 KIAS.
- **NTSB, WPR17FA041 (N176PA, S-90).** The previous owner, a CFI, told the NTSB:
  - the airplane stalled like a 172, docile, with no tendency to roll off either wing;
  - the elevator was "huge";
  - he observed about 70 kt full-flap stall and set his own Vs 85 / Vso 70 KIAS;
  - he considered the POH 55 KCAS factory stall figure unsafe and never observed it.
  - A friend's video showed an Express CT, which he described as having "a smaller wing" and as the reason he gave the buyer vortex generators.

  (B, NTSB records of communication: https://data.ntsb.gov/Docket/Document/docBLOB?ID=40462133&FileExtension=.PDF&FileName=Record%20of%20Communication%20(Previous%20Owner)-Master.PDF and https://data.ntsb.gov/Docket/Document/docBLOB?ID=40462134&FileExtension=.PDF&FileName=Record%20of%20Communications%20(Previous%20Owner)-Master.PDF). His "smaller wing" remark conflicts with CAFE/EDI, which say the CT and S-90 share the wing. Unresolved.
- **EDI POH (N49EX copy, IO-360).** Vs 55 KCAS, Vso 50; spins prohibited, with a spin recovery procedure. There is no description of stall behavior or wing drop. (F, https://express-builder.com/old/docs/poh/rm/Wheeler_Express_POH.pdf)

**Builder/owner commentary (B, express-builder.com)**

- **Rudder authority (EBF-1184, 2006).**
  - A new FT 2000 with the "straight" (conventional) tail had a lack of low-speed rudder authority.
  - One owner flies approaches at 80 kt or more because of slow yaw response, which he calls "wallowing".
  - A Series 90 owner measured rudder deflection under load with a fish scale. He found that system flex (small rudder horn, poor pedal/torque-tube ratios, pulleys) cut actual in-flight travel to a few degrees. He re-routed the cables and fitted a wider horn: 17° each way with much more force.
  - A CT owner (N12EX) would change the rudder/yaw stability and says the airplane wanders in turbulence.
  - In Feb 2000 the factory (EAC) said it had found excessive wear at the rudder hinge/cable attachment on its demonstrators. It redesigned to a shielded-cable system and recommended that EDI Series 90 owners inspect (EBF-55).
- **Tail mass (EBF-1236, 2006/2010).**
  - One S-90 owner weighed his surfaces: rudder 35 lb, each elevator 23 lb, 81 lb in total. He compared that with about 21 lb for a C182.
  - He built aluminum surfaces that saved about 33 lb and moved the c.g. about 3.5 in forward. He had also flight-tested vortex generators.
  - Another owner reports a 32-36 lb rudder and 56-62 lb of nose ballast.
  - Other IO-540 owners report no problems.
- **Vortex generators (EBF-86).**
  - A French CT owner fitted VGs on the horizontal stabilizer and fin ahead of the control surfaces, which improved elevator and rudder response.
  - Another CT (IO-360) with the full Stolspeed VG kit (wings, stab, rudder) reported a full-flap power-off stall of 54 mph IAS against 66 before, better low-speed aileron, a less squirrelly feel below 90 mph, and 4-5 kt cruise loss at 60% power.
  - An 11-year CT owner reports no slow-flight problem.
- **Stab incidence and rigging are inconsistent across eras.**
  - WTI factory setting: -0.2 to -0.8° (WTI 1991). CAFE N360EZ: -0.8°.
  - Express 2000 manual: stab 0°, wing +1.5°.
  - Builders were advised -0.7 to -0.8°. The factory set 0° on its 2000s except N512EA at -1° (EBF-1030).
  - Owners report re-shimming stabs 1-2° nose-down to fair the elevator (EBF-1030, EBF-1343).
- **Pitot-static.** A CT owner found Dynon TAS 12-13 kt high from the flush static ports (EBF-1942).
- **Stall strips.** No mention found anywhere.

**Tail and wing dimensions**

| Quantity | Value | Grade | Source |
|---|---|---|---|
| H-stab span / area, cruciform (N360EZ) | 112 in / 13.14 sq ft, NACA 66-009; chord root/tip 25/8.5 in | P | CAFE |
| Elevator, cruciform | 120 in total span / 8.63 sq ft; chord 11.5 in | P | CAFE |
| Total H-tail, cruciform | 21.8 sq ft (stab plus elevator, our sum of CAFE figures). EDI's "effective horizontal tail area" for the CT is 23 sq ft | E / F | CAFE; EDI 1995 |
| H-tail, S-90 | 31 sq ft effective (EDI). 13 ft span, 40% more wetted area than the CT's 10 ft stabilizer (CAFE text). "20% larger tail" (AeroCrafter via Wikipedia) | F / P / L | EDI 1995; CAFE; https://en.wikipedia.org/wiki/Express_Series_90 |
| Minimum flyable H-tail (EDI consultant) | About 13 sq ft. Computed neutral point and forward trim limits: CT 75.5-86.7 in aft of datum (11.2 in range); S-90 70.5-90.5 in (20 in range). A 34% area increase gives a 78% range increase. Doubling the tail costs about 4 mph cruise. The consultant report is cited as ATS 92-01 (our OCR reading) | F | EDI 1995 |
| Vertical fin, cruciform | Not published ("na, symmetric section"). Highly swept; stab and fin molded in one piece | P / F | CAFE; WTI 1991 |
| Rudder, cruciform | 52 in average span / 4.33 sq ft, chord 12/12 in. Travel 26° per manual, 20° allowed; CAFE recommends 20° | P | CAFE |
| Stab/elevator root chord, cruciform | 37 in | F | WTI 1991 |
| Tail incidence | -0.8° (N360EZ); see the rigging notes above | P | CAFE |
| Tail arm | Not found | - | - |
| Wing | 31 ft span, 130.29 sq ft, root/tip 60/37.5 in, AR 7.4, taper 0.63. NLF(1)-0215F, 15%, design CL 0.2. Incidence +1.5°, no twist, dihedral 5° bottom/4° top | P | CAFE |
| Wing (AOPA 1990) | 126 sq ft | P | AOPA 1990 |
| Airfoil detail | The original NLF(1)-0215F had its trailing-edge cusp removed/flattened on the bottom. The "S2000 v2.0" wing (production break mid-2003) is similar to NACA 747A-315, with about 10 sq ft more area and a taller spar | B | EBF-1030 |
| S300RG/2000RG wing | New wing with a rearward trailing-edge extension of 9 in at the root and 1 in at the tip | L | https://janes.migavia.com/usa/express/express.html |
| Ventral/dorsal fin, tail enlargement by owners | No ventral or dorsal fin mod found. Enlargement was via the S-90/2000 tail (EDI conversion kit; EAC planned a CT-to-S-90 conversion in 1997). One builder (Betts, C-GUPZ, 1990-91) replaced his tail with his own design | F / P | EDI 1995; CAFE; WTI 1991 |

### A5. Kit-maker notices on stall, rigging and the tail

1. **WTI letter, 15 Mar 1991 (F).**
   - It responds to builder Michael Betts (C-GUPZ). Betts had told builders that his was "the third EXPRESS with a problem" after a tail problem, and he cut off his tail.
   - WTI attributes the problem to a horizontal-stab incidence error of about +3°, measured from photos, which forced aft ballast and higher landing speeds. WTI says it carries a risk of "deep stall".
   - WTI states there is no evidence of design problems in either factory crash. It notified the FAA, Transport Canada and EAA that his airplane was no longer a Wheeler Express.
   - The NTSB summary of this letter: if the builder installs the tail correctly there would not be abnormal stall characteristics (P, WPR17FA185).
2. **EDI letter and findings, 22/18 Feb 1995 (F).**
   - EDI found that on the "Express CT" it is possible to generate an unexpected pitch-down with rudder application. Outside aerodynamic consultants confirmed this.
   - The findings discuss under-sized horizontal and vertical tails, tail stall in sideslip at forward c.g. with flaps down, and small vertical tails letting sideslip develop at the stall.
   - Actions: revised operating recommendations for all models, and a recommendation that every CT owner "seriously consider" the S-90 tail update (wording as quoted in NTSB-PDF(95839); the scan's OCR is garbled here).
   - **Operational Recommendations.** These are illegible in part in the OCR. Legible items: Vfe 100 KCAS; 3,200 lb gross for standard models; an Express FT "Loadmaster" c.g. chart; load-factor limits; aerobatics and spins not recommended; yawed (slip) maneuvers restricted; crosswinds over about 10 mph not recommended; flight in excess of light turbulence not recommended; a professional test pilot recommended for initial flights; runways of at least about 3,000 ft. The exact speed values need a cleaner scan.
3. **CAFE 1997 (P, not a bulletin).** Recommends a 20° rudder stop, investigation by a professional test pilot, and a static-port fix.
4. **EAC, Feb 2000 (F, posted on EBF-55).** Rudder horn/cable wear found; Series 90 owners told to inspect; new shielded-cable rudder system.
5. **Not found.** No FAA AD (none can apply to amateur-built aircraft), no SAIB, and no numbered service bulletin from EAC, Exosphere or CAT on stall, rigging or the tail.

---

## B. Why it failed in the market

### B1. Documented facts (F/P/L as marked)

| Year | Event | Grade | Source |
|---|---|---|---|
| 1987 | First flight 28 Jul 1987. Oshkosh debut, orders taken. Ken and Gail Wheeler, Gig Harbor WA; Ken had built a Glasair | P / L | CAFE; https://en.wikipedia.org/wiki/Wheeler_Express |
| by 1989 | About 300 kits sold. Sjostrand bought his in 1989 "one of the 300" | P | CAFE |
| 1990 (Aug) | Airframe $25,975 in 5 installment kits ($5,750 / $5,750 / three at $4,825). Firewall-forward Continental package $25,775. Total $52,270 before avionics; AOPA estimates up to $80k finished. Build-time claim 1,000 h. At the time of the test no customer airplanes were yet flying. RG version planned at +$4,010 | P | AOPA 1990 |
| 1989-10 | Demo #1 N200EX engine failure, crash into houses, occupants walked away. Wheeler presented it as proof of crashworthiness | P | LAX90DUD01; AOPA 1990 |
| 1990-07-25 | Demo #2 N210EX spun in on the way to Oshkosh (3 killed per NTSB; 4 per CAFE/Kitplanes). CAFE: it "led to a severe contraction in sales eventually prompting Ken Wheeler to enter bankruptcy" | P | SEA90FA146; CAFE |
| 1990-91 | Kits delivered incomplete at the time of the Wheeler bankruptcy; EDI made the deficiencies good. Early plans incomplete; Sjostrand created much of the documentation later builders used | L / P | Jane's (janes.migavia.com); CAFE |
| 1991 | Public dispute with builder Betts over the tail (WTI 1991). Betts announced his own tail tooling. A group of about 17 owners developed the "Arriga"/Auriga tail; a former Boeing engineer ran tuft/VG studies "with a goal of certification" | F / P | WTI 1991; CAFE |
| 1991-92 | Ralph Kinner acquired the WTI assets and sold them to David Ullrich | L | https://aeropedia.com.au/content/express-aircraft-express/ |
| 1992-95 | Express Design Inc. (Redmond OR) sold Express and Arriga kits as complete kits, renamed the Arriga the Series 90, and offered a tail conversion kit. Also the six-seat Loadmaster 3200 | P / L | CAFE; Wikipedia |
| 1995-02 | EDI tells all CT owners about the uncommanded pitch-down and recommends the S-90 tail retrofit | F | EDI 1995 |
| 1996-01-06 | EDI files Chapter 7 (Express Link newsletter, cited by Wikipedia) | L | Wikipedia |
| 1996-97 | Express Aircraft Co LLC (Larry Olson, Paul Fagerstrom; Olympia WA) buys the rights. Complete kits promised by April 1998 at $34,995 (no engine/prop/avionics/paint). Kit-maker build time 2,000 h; Sjostrand's actual 5,000 h. About 30 of about 300 completed | P | CAFE |
| 1998 | Express sold as the "Express 2000" from 1998. Kit-maker data: empty 1,825 lb, MTOM 3,400 lb, 82 USG integral tanks | P | BFU 2050 (sust.admin.ch) |
| 2000 | First builder-assist / factory-finished 2000 delivered. Builders report months of parts delays during redesigns of the rudder horn, cables and baggage door; the 2000 tail manual not supplied (EBF-55) | L / B | aeropedia; EBF-55 |
| 2003 | EAC announces a $10M, 90-aircraft contract with a Russian firm (company claim) | F (via forum) | EBF-407 |
| 2003-04 | More than 300 kits sold, about 60 completed and 80 under construction (Apr 2003). Quoted build 1,600 h, or 400 h with builder assist. 2004 prices: 2000 airframe $48,900; S300RG $78,800; 2000RGT $67,500 | L | Jane's (janes.migavia.com) |
| 2003-07-27 | Turbine Auriga FT N512EA crashes after takeoff; the pilot, president of EAC, is killed. The new owners (Davis/Moon) then dropped factory support for the turbine RG and concentrated on the FT | P / B | CHI03LA227; EBF-743 |
| 2003-12 | 2000RG kit to $75,800 from 31 Dec 2003; 2000FT stays at $48,900 | F | EBF-597 (factory post) |
| 2004-09-15 | Owners Roy Davis and Nancy Moon announce Express Aircraft is out of business | B | EBF thread 1568 (timeline by builders), https://express-builder.com/old/forum/messages/29/1568.html |
| 2005-07-05 | Assignment of membership interest to Exosphere Aircraft Co (Barry Henthorn), to "fulfill backorders" | F (press release reposted) | https://www.homebuiltairplanes.com/forums/threads/express-aircraft-purchased-finally.1609/ |
| 2005-09-26 | Madison Bay Holdings takes a 20% stake in Exosphere. The press release, as quoted by builders, describes Exosphere as a light-sport aircraft producer whose models include the Express | L | EBF-1204; Wikipedia |
| 2006-07 | Exosphere says Express assets are not merged into the public company (EXSA) and there is "no commitment to offer kits". Cruciform-tail parts would "probably never be available" without re-tooling. Its focus moves to an LSA (Bede BD-22, 2007) | F | EBF-1204; EBF-1440 |
| 2006-12 | Five builders obtain court judgments for undelivered parts and prepaid builder-assist sessions, about $250,000 in total | B | http://www.wolfelt.com/express/post6.htm |
| 2007-04-05 | Chapter 11 filed the day before a sheriff's sale. The petition was dismissed after a 29 May 2007 hearing, and the company was put into Chapter 7 liquidation | B | wolfelt post6; EBF-1568 |
| 2007-09 | Composite Aircraft Technology (Darrell Peterson) buys all EAC assets through bankruptcy court and moves the molds to Toledo WA | B / L | EBF-1568; Wikipedia |
| 2009 | CAT back in production with a builder-assist center. Its first two years went to supplying parts owed to earlier customers | P (trade press) | https://generalaviationnews.com/2009/09/03/express-aircraft-returns/ |
| 2013 | Last forum trace of CAT activity (Peterson brings an RG and an FT to a fly-in) | B | EBF-407 |
| 2025 | About 100 ever registered with the FAA, about 55 active | L | Kitplanes 2025 (URL above) |

**Competitor prices in the same years (incomplete).**
- Lancair IV basic airframe $46,900 and IV-P $66,900 (1994), quoted build 2,500 h, about 200 IV builders (P; https://www.aopa.org/news-and-media/all-news/1994/june/pilot/lancair-iv-p).
- Velocity XL base $37,500 (2005) (P; https://generalaviationnews.com/2005/03/25/velocity-xl-5/).
- Express 2000FT, 2003-05: $48,900 (F).
- No sourced Glasair III, Murphy or Comp Air prices for the same years were found.

**Magazine coverage found:**
- AOPA Pilot, Aug 1990: positive pilot report.
- CAFE APR, published through EAA Sport Aviation, 1997.
- EAA kit page listing Sport Aviation articles, including "The Series 90: Express Design's Latest Addition" (https://www.eaa.org/eaa/aircraft-building/kits-and-plans/d---g/express).
- General Aviation News 2009 (CAT relaunch) and 2017 (NTSB CEN15FA321 summary plus owner comments).
- Flightglobal, short item: EAC acquired bankrupt Express Design and relaunched (https://flightglobal.com/express-deliveries/7932.article).
- Kitplanes, Apr 2025 retrospective.
- A Kitplanes editor solicited builders in 2005 for an article on orphaned kits (EBF-1021); the article was not found.

### B2. Builder opinion (B; opinion, not fact)

- **Build difficulty and parts.**
  - A builder of five aircraft (Express, Velocity XL RG, Fisher, Harmon Rockets) said "the express was the most difficult to build of all of them". The difficulty was mostly getting parts. He lost "several thousand dollars" when the company shut and bought substitute parts from Van's, Glasair, Lancair and Velocity (EBF-1204).
  - Others: the EDI plans were incomplete and "their metal parts quality was SO BAD" (EBF-55). The manual's drawings were very hard to read; buying parts a second time was expensive (wolfelt post5).
- **Redesign churn.**
  - A 1989 deposit-holder still building a CT 15+ years later said every new owner re-designed parts rather than shipping kits. He wrote that "nothing sells kits like kits completed and on the flight line", and that today he would probably pick an RV-10 (EBF-1204).
  - The same builder said the tail issues "started back in the 1991 time frame" with a first customer airplane whose tail was installed wrongly.
  - Another builder called EDI's cargo pod and similar projects diversions, and the turbine "an unnecessary diversion" (EBF-743).
- **Escrow/deposit losses.** A builder places the escrow and loss problems in the last Ken Wheeler tenure (EBF-743). No amount was found for Wheeler-era deposit losses.
- **Marketing.** "still nobody seems to know how to market, produce, and deliver it". The same writer said Lancair IVs sold despite their cost (EBF-1204).
- **The product itself was liked.**
  - Builders chose it for payload (4 adults plus bags over 1,000 mi) (EBF-1204).
  - Owners compare it to a fast C182 (EBF-1204) and praise the speed and load (EBF-407, EBF-1067).
  - Some say it does not "fly like a 172" and is pilot-demanding (EBF-1204).
  - Owners attribute the accidents to pilot proficiency, e.g. a GA News comment by an 1,100 h owner (https://generalaviationnews.com/2017/07/28/airplanes-design-contributes-to-fatal-accident/).
- **Insurance.** A builder hoped the 2007 revival would "inject some confidence amongst our insurance underwriters" (EBF-1568). No insurance data were found.

---

## Gaps (searched for, not found)

- **Docket items.** Weight, c.g., flap position and airspeed for N772BM; the CEN21LA096 docket has none. Sideslip or yaw-rate data for any accident; the N3FC EFIS table has bank, pitch, IAS, rpm and heading only.
- **Tail configuration (cruciform vs converted)** of N772BM, N3FC-era CTs, N564ER, N297JH, N113YE, N410MP, N93HE, VH-PNK, and whether N554SB had a CT or FT tail.
- **Express lineage** of N456TS ("Terrair Express", s/n CT101) and N297JH; the NTSB does not state it.
- **Canadian records.** Transport Canada CADORS was offline on 2026-10-24 (Oshawa 2004O0813, Orillia 2020, Chicoutimi 2024). No TSB report found for Regina 2006 (N554SB).
- **Other foreign reports.** The original Bahamas AAIPU report (Chub Cay 2009), the ATSB VH-PNK report and the Argentine JIAAC reports were not opened; only the ASN summaries were seen.
- **Dimensions.** Vertical fin area, height and chord for any variant. Tail arm. S-90/2000 horizontal-tail span and chord in kit-maker drawings. Any three-view.
- **Stall strips, wing root/tip stall progression, tuft studies.** Not found. The Paul Robertson tuft/VG tapes mentioned by CAFE were not found.
- **EDI "Operational Recommendations".** The V-speeds need a legible scan. The consultant report ATS 92-01 (our OCR reading) was not found in full.
- **Bulletins and early documents.** Numbered service bulletins from EAC/Exosphere/CAT. The Express Link newsletters (Copeland). The EBU (Express Builders' Union) 1991 analysis.
- **Business details.** Wheeler-era deposit or escrow loss amounts. The exact Wheeler bankruptcy date (sources give 1990, 1991 and 1992).
- **Competitor prices.** Glasair III, Murphy and Comp Air prices for the same years; an RV-10 2004 price from a primary source.
- **Magazine coverage.** Any Flying, Air Progress or Kitplanes flight report from 1987-2010. Sport Aviation article texts (behind EAA login; not accessed).
- **CAT status.** Its status after 2013; its domain lapsed (see the repo rights notes).
