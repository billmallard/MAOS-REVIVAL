# Prescott Pusher

Stage 1 stub (extended in stage 3 below), generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Tom Prescott, Prescott Aeronautical |
| Years | 1985 first flight; kits to ~1989 |
| Number built | 68 kits (Wings Over Kansas); 19 airframes ever on the US register (FAA registry 2026-10-24), plus at least 2 abroad |
| Survivors / registered | 4 current US registrations (N41PP museum, N10JS, N200SX, N40LE); 2 likely airworthy |
| Seats | 4 |
| Configuration | Pusher, 4 seats (2+2), engine in the tail cone on a 12 in prop extension (no drive shaft), T-tail, retractable or fixed tricycle gear |
| Construction | TIG-welded 4130 square-tube cage with non-structural fibreglass shells; riveted aluminium wing, NLF(1)-0215F; CAD/CAM-designed to Part 23 |
| Engine | Lycoming O-360, 180 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,400 lb | F | [source](https://1000aircraftphotos.com/Contributions/6802.htm) | - |
| Empty weight | 1,550 lb | F | [source](https://1000aircraftphotos.com/Contributions/6802.htm) | - |
| Useful load | 850 lb | F | [source](https://1000aircraftphotos.com/Contributions/6802.htm) | - |
| Useful load, fleet or as-weighed | 739 lb | P | [source](http://web.archive.org/web/20241217134717/https://p.pdfhall.com/russ-and-marcia-taylors-prescott-pusher_5b6d873e097c4748748b4604.html) | one builder aircraft weighed (N747P: 1,555 lb in the shop, 1,661 lb finished with ballast for CG; Jack Cox, Sport Aviation, September 1991); not a fleet average |
| Usable fuel | 56.5 US gal | F | [source](https://1000aircraftphotos.com/Contributions/6802.htm) | second prototype |
| Published range | 869 nm | F | [source](https://1000aircraftphotos.com/Contributions/6802.htm) | not stated (1,000 mi) |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 151 M | - | 73% | - | P | [source](https://www.kitplanes.com/archive-may-1988/) | measured, Kitplanes May 1988 (LeRoy Cook), second prototype N42PP; altitude, weight and rpm not published |
| 165 P | 7500 | - | - | F | [source](https://1000aircraftphotos.com/Contributions/6802.htm) | brochure, 190 mph converted |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: fail** - UL -150 lb, range -131 nm
  - Useful load: 850 lb (fail) against 1,000 lb.
  - Range: 869 nm (fail; not stated (1,000 mi)) against 1,000 nm.
  - Cruise: 165 KTAS at 7,500 ft (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot (866 nm max).
- **Measured or reported: partial: UL fail, speed near, speed unconditioned** - UL -261 lb, speed -9 kt
  - Useful load: 739 lb (fail) against 1,000 lb.
  - Range: - nm (?; none found) against 1,000 nm.
  - Cruise: 151 KTAS at an unstated altitude (near) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot (866 nm max).
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 180 hp.

Sanity flags:

- fleet useful load 111 lb below factory
- Bill's top-interest design (AER-3783, 2026-10-24): full deep dive in the stage 3 dossier

## Why it died

Early handling and performance disappointment tied to a far-aft CG (pitch sensitivity, hard rotation), a financing change from pay-as-you-build to pay-up-front (Tom Prescott, 2007), slow parts, and a 1988 sale abroad; folded 1989-1991 with builders mid-kit (Kitplanes; SDASM; Sport Aviation).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- A pusher without a drive shaft: engine in the tail cone, prop on a 12 in extension; no drive failure on record.
- A welded tube cage with all systems installed before non-structural shells go on; CAD/CAM-designed from the start; the engineering archive survives at SDASM.
- Lesson: an engine in the tail sets the CG, gear position and prop clearance together; the Prescott's handling complaints trace to that.

## Rights and provenance (known so far; research, not legal advice)

No TC. Engineering record survives at SDASM (SC.10269); rights holder unknown (docs/rights/prescott-pusher.md, PR #6). Owned by the stage 2 rights research (AER-3787).

## Safety record

4 confirmed US NTSB events, 1 fatal (Ford V-6 conversion, LAX90DUM02), plus a probable fifth (fatal, Ford V-6). Pusher-specific: a door into the prop (CEN09CA386) and a prop separation (LAX05LA270). Pitch-up stall in a go-around (MIA92LA186).

<!-- stage3:start -->

## Stage 3: shortlist rank 2 of 6 (AER-3783)

Our own check, from published geometry and weights, calibrated against published flight data. Method, calibration and the Aeromomentum assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are research, not legal advice. Nobody has been contacted.

### Bill's call

Bill, 2026-10-24: "Prescott Pusher should also be of high interest. This is possibly the top of my list as a target of interest." Moved to the top tier and given the full treatment.

### Verdict

**Rank 2, top tier.** As published it passes speed (165 KTAS at 7,500 ft) and misses useful load by 150 lb (850) and range by about 130 nm (869 nm, reserve not stated). As measured it is weaker: the one weighed builder aircraft had 739 lb useful, and Kitplanes measured 151 KTAS at 73% at an unpublished altitude, which our model can reproduce only with a drag factor of 1.46-1.67 against the brochure's 1.35. On an AM20T it is fast (194-207 KTAS) but the engine's weight in the tail costs about 143 lb of useful load with ballast; **it clears all three floors on both drag bases only as a re-derivation**: about 2,700 lb gross, a structure about 100 lb lighter than today's would be at that weight, 90 gal, and the AM20T (1,077 lb, 1,112-1,172 nm, 194-204 KTAS). Its two great assets are a short 12 in prop extension instead of a drive shaft, and the best-preserved engineering record in the survey (SDASM SC.10269: drawings, loads report, wind-tunnel evaluation, structural tests). Its weakness is balance: a far-aft CG that made rotation hard and pitch sensitive, which a heavier engine in the tail makes worse. It ranks behind the Aries, which clears the floors on a straight engine swap, and ahead of the Express, because its engineering survives and it has no long shaft or known tail flaw.

### Idea ledger (what a new airplane should keep)

- **A pusher without a drive shaft.** Engine in the tail cone, prop on a 12 in extension: the clean forward fuselage and quiet cabin of a pusher without the VK-30's shaft risk. No drive failure is on record.
- **Build sequence for a home shop.** A welded tube cage with every system installed before non-structural fibreglass shells go on; shells from CAD-cut patterns. The plugs cost about a tenth of the $200,000 factory tooling (Sport Aviation 1986).
- **CAD/CAM from day one** ("the first aircraft in its class totally designed using CAD/CAM", SDASM), with stretch-formed leading edges on CAD-made dies: a 1980s preview of a digital kit.
- **An NLF(1)-0215F laminar wing** with reflexed flaps and ailerons, on a metal structure.
- **The archive.** Drawings, loads, wind-tunnel and structural test reports in a public museum collection: the strongest re-derivation basis in the survey (rights and use terms: attorney, per Elon).
- Lesson: put the CG, the main gear and the propeller clearance together first; an engine in the tail drives all three, and the Prescott's handling complaints trace to that.
- Lesson: a financing model that turned pay-as-you-build into pay-up-front, and parts that lagged marketing, lost the builders' trust before the airplane could earn it.

### Published, measured and our check, side by side

Read across a row only within one column's basis. The three targets are separate floors.

| | As published | Measured or reported | Our check, original engine |
|---|---|---|---|
| Useful load | 850 lb (fail) | 739 lb (fail) | 850 lb (the empty weight the model uses: 1,550 lb) |
| Range | 869 nm (fail; not stated (1,000 mi)) | not found | 865 nm, still air, no reserve, full fuel from MTOW, at 135 hp and 7,500 ft |
| Cruise | 165 KTAS at 7,500 ft (pass) | 151 KTAS at altitude not stated (near) | 170 KTAS at 135 hp and 7,500 ft |
| Screen | fail | partial: UL fail, speed near, speed unconditioned | see the verdict |

### The deep-dive axes: storage, home-shop construction, safety, ride

**Aspect ratio 7.8**: a conventional wing, on the high-aspect-ratio side of the planform study (AER-3807, `docs/studies/planform/`); the Rohr 2-175 is its opposite.

- **Storage.** 29.3 ft span, 20.3 ft long, 8 ft 9 in high: fits a 40 ft T-hangar door. The wings bolt on with two bolts per side at the root (Sport Aviation 1986), but no folding or quick removal is described.
- **Construction with home-shop tools.** A good fit. The 4130 square-tube cage is router-jig and welder work; the non-structural shells come off plugs, and plugs are what a home CNC router and a large-format printer can make in sections. The riveted aluminium wing used press-brake spars and stretch-formed leading edges on steel dies; the dies are a service job, the rest is home-shop sheet metal. Largest part a 14.7 ft half-wing; root spar about 8.2 in deep. Builders praised the fit of the sub-kits and found the fibreglass shell the worst job.
- **Safety.** Stall: "super gentle, with practically zero roll tendency" (Sport Aviation 1986) but with "no aerodynamic warning" (AOPA 1986, which saw stall strips being tried); full-stall landings end abruptly (Kitplanes 1988). Spin: never tested as far as the record shows. Takeoff pitch sensitivity and aft-CG lift-off are the documented hazard. Best L/D about 15.7 at 110 KTAS (propeller drag excluded). Pusher-specific events: a door that came off into the propeller (CEN09CA386), and a propeller that separated (LAX05LA270). Both fatal accidents were Ford V-6 conversions.
- **Ride comfort.** Gust dn 1.63 at 21.7 lb/ft2: in the rough half of the shortlist. AOPA (1986) found bumps took three to four pitch oscillations to settle. Cabin 42.5 in wide, and "Cabin size is the same as a Bonanza" (Sport Aviation 1986); rear seats sit higher, on the carry-through; quiet enough at taxi for normal conversation (Sport Aviation 1986).

### Configuration in detail, and the fleet

Sources and the full fleet and accident tables: `docs/shortlist/check/prescott/README.md`.

- **The engine sits in the tail cone, right behind the cabin, and drives the propeller through a 12 in extension, not a drive shaft.** Sport Aviation (March 1986): "the shaft is only 12" long." Prescott chose it deliberately: "Early in the design, I decided not to accept the challenges associated with a mid-engine aircraft and the six to eight foot drive shaft that the mid-engine dictates" (RCM, July 1986, F). The museum's drawing list has a "prop extension" (15302) and an adapter bushing, and no coupling, bearing or damper drawings, so it is most likely a bolted flange spacer (our inference). **No drive failure is on record.** The one drive-train event is a wooden propeller that separated in cruise two weeks after being refitted, with elongated bolt holes, cause undetermined (NTSB LAX05LA270).
- **Propeller:** 65 in recommended, 68 in the largest flown (F). Ground clearance is not published and is called marginal in several sources; the short gear that clearance forced meant a small propeller.
- **Tail:** a T-tail on a swept fin, horizontal tail 29.3 ft2 (11 ft span). The 1/5-scale plan drawn by Prescott shows a small ventral fin ahead of the propeller; not confirmed at full scale.
- **Cooling:** air-cooled, in the tail cone. The prototype overheated its oil until the cooler moved to the nose; builders report a hot right rear cylinder (AOPA 1986; Sport Aviation 1991).
- **Structure:** a TIG-welded 4130 square-tube cage with non-structural fibreglass shells flush-riveted to bulkheads (3-8 plies, CAD-cut patterns), so everything can be installed before the shells go on. Aluminium wing: a press-brake-formed 2024 C-spar with nested extrusion caps, stretch-formed leading edges on CAD/CAM steel dies, NLF(1)-0215F section. Spar tested beyond +3.8/-1.5 g; gear drop-tested to 5.5 g; designed to Part 23 but never certificated (Sport Aviation 1986; Prescott 2007).
- **Gear:** fibreglass mains and an Airite nose gear, hydraulic retraction (fixed and retractable kits were offered). The mains sit far aft because the flight CG is far aft; rotation was hard (Wainfan, Kitplanes).
- **Dimensions** (Prescott 2007, F): span 29 ft 4 in, wing 110.8 ft2 (aspect ratio 7.8), length 20 ft 3 in, height 8 ft 9 in, cabin 42.5 in wide. 2,400 lb gross (designed for 2,250, loads report and tests redone at 2,400); 1,550 lb factory empty; 56.5 gal in the wing leading edges (prototype 2). No dimensioned three-view survives online; the RCM 1/5-scale plan (Outerzone oz14320) is drawn by the designer, with a full-scale dimension table.
- **The fleet** (FAA registry, 2026-10-24): 4 current registrations and 15 deregistered, so 19 airframes ever on the US register. Likely airworthy now: N10JS (Allison 250 turbine) and N200SX (O-540). N41PP, the first prototype, is at the Kansas Aviation Museum. Two more are known abroad. Builders re-engined widely (O-540, Ford V-6, Mazda rotary, Allison 250). **The one weighed builder aircraft**, N747P, came out at 1,555 lb in the shop and 1,661 lb finished with ballast for CG (Sport Aviation 1991), so 739 lb useful: two adults and full fuel. Its first customer called it "really only a two-seat airplane" (Syracuse, Kitplanes).

### Published against measured: the 165 against the 151

**The brochure's 165 KTAS at 7,500 ft against Kitplanes' measured 151 KTAS at 73%.** Kitplanes' May 1988 figure ("174 mph true at 73% power", second prototype) has no published altitude, weight or rpm; the full article was not reachable. Our model resolves the two this way:

| Claim | Drag factor our model needs to reproduce it | Reading |
|---|---|---|
| Brochure: 165 KTAS at 7,500 ft, 75% (135 hp), 2,400 lb | 1.35 | Inside the fleet band (1.16-1.36): the brochure is consistent with the airframe's geometry |
| Kitplanes: 151 KTAS at 73% (131 hp), if flown at sea level | 1.46 | Draggier than the band |
| The same, if flown at 7,500 ft | 1.67 | Much draggier: Defiant-like |

So either Kitplanes flew low and the airplane is 10-25% draggier than its geometry predicts, or the 73% was optimistic: on prototype 1 the fixed-pitch wood propeller held the engine to 2,400-2,600 rpm. The builders' verdict sides with the measurement: "The Prescott Pusher with the 180-hp Lycoming really didn't match up to its marketing numbers" (Syracuse, Kitplanes, B), and Wainfan wrote that "once it got into the air, it proved to have disappointing performance." We carry both bases in every result below, labelled, and never mix them. Every pusher in this survey with measured points reads draggy (Defiant 1.72, Velocity 1.63); the planform study (AER-3807) is the place to test whether that is the configuration.

### Where it lands on an Aeromomentum engine, and what moves it

Bill's question: on an Aeromomentum engine, turbo-normalised at altitude, what moves useful load (850 lb published, 150 short), range (869 nm published, about 130 short) and speed, and does it clear all three floors? Script and full tables: `docs/shortlist/check/prescott/levers.py`. Assumptions: 195 / 120 hp continuous and 8,000 / 16,000 ft critical altitudes are ours; the structure deltas are placeholders until MANUFACTURING (AER-3784) answers; the 75 and 90 gal tankage is our estimate (the 15% wing has about 280 gal of geometric volume).

**The engine sits in the tail, so engine weight costs twice.** Every pound added behind the cabin needs about 1.3 lb of nose ballast to keep the CG where it was (our estimate of the arms), and the Prescott's CG was already its weak point. The AM20T is 61 lb heavier installed than the O-360, which costs about 82 lb of ballast; the AM15T is 26 lb lighter and saves about 35 lb.

| Lever | Useful load | KTAS (brochure basis / measured basis) | Range, nm, full fuel, still air, at continuous power |
|---|---|---|---|
| As published (O-360) | 850 | 165 at 7,500 ft (published) | 869, reserve not stated (published) |
| AM20T alone, 16,000 ft critical altitude | 707 (-143) | 207 / 196 | 705 / 669 |
| AM15T alone, 16,000 ft | 911 | 169 / 159 | 934 / 883 |
| AM20T + 90 gal | 707 | 207 / 196 | 1,187 / 1,127 |
| AM20T + 90 gal + 200 lb lighter structure, at 2,400 lb | 907 | 207 / 196 | 1,187 / 1,127 |
| **AM20T + 90 gal + a 2,700 lb gross structure no more than 100 lb heavier per pound of gross than today's (net -100 lb)** | **1,077** | **204 / 194** | **1,172 / 1,112** |
| AM15T + 90 gal + 200 lb lighter, at 2,400 lb | 1,111 | 169 / **159** | 1,587 / 1,503 |

**What each lever buys.** More power at altitude buys speed and nothing else: the AM20T lifts cruise to 194-207 KTAS and costs useful load through the tail-cone weight. More fuel buys range and nothing else: 90 gal clears 1,000 nm at continuous power on both bases. A lighter structure buys useful load pound for pound, but at 2,400 lb even 200 lb lighter leaves the AM20T version at 907 lb. **It clears all three floors on both bases only as a re-derivation**: a structure designed for about 2,700 lb gross, about 100 lb lighter than today's structure would be at that weight, 90 gal, and the AM20T. The AM15T alternative clears load and range at 2,400 lb with a 200 lb lighter structure, but its cruise speed falls to the floor (159-169 KTAS). With 90 gal aboard at 2,700 lb, the AM20T re-derivation carries about 540 lb of people and baggage: it is a four-seater with full fuel only for light occupants, as the original was.

**The real constraint is balance, not power.** The AM20T makes the Prescott fast, but its weight in the tail cone makes the documented aft-CG problem worse. A re-derivation would move the wing aft or lengthen the forward fuselage to put the CG where the gear and the tail want it, and that, not the engine, is the design work.

### Why it died, properly

On the record (sources in `docs/shortlist/check/prescott/README.md`):

1. **Handling and performance disappointed, early and publicly.** AOPA Pilot (1986) was briefed on a ground-effect pitch-up, found pitch "quite sensitive" at low speed, and noted "no aerodynamic warning" at the stall. Builders reported early lift-off and pitch oscillation from an aft CG ("Yes, we narrowed the CG envelope after that flight"), roll-off at lift-off, and hard rotation. Its first customer called it "somewhat of a ground hog". A retrospective puts it bluntly: "What ultimately killed the market for the Prescott Pusher, however, was the negative buzz generated after some early completions" (airplanezone, L).
2. **The layout's own consequence.** Wainfan: "A rear-engine airplane like the Prescott Pusher is very challenging aerodynamically because the flight CG is so far aft on the fuselage." That put the mains aft, which made rotation hard, and kept the gear short for propeller clearance, which forced a small, inefficient propeller.
3. **Financing and control.** Tom Prescott's own account (2007): "The original marketing grass-roots pay-as-you-go approach was elevated to a high-dollar pay-up-front strategy", and his and Stan Blankenship's key contributions "evaporated in the face of requirements demanded by the financial backer." He also says the delivered kits "had the essence but not all the aerodynamic and structural refinements envisioned or planned".
4. **Parts.** The first customer to fly started "as builder number 29 and I finished first–only because I kept dogging Prescott for parts" (Syracuse, 1989); "the Prescott team was much better at marketing than producing parts."
5. **The end.** In October 1988 Kitplanes reported the company "was being sold to an Australian outfit, which offered no plans about further development"; kit sales stopped in early 1989; SDASM says the company folded in 1991 with builders still completing aircraft. The second prototype was later registered to "Pusher Aircraft Inc", Wichita, until 2018: a lead for the rights work (passed to Elon).

**Does a revival fix it?** The business causes (parts, financing model), yes. The handling causes trace to the aft CG of an engine in the tail; a revival fixes them only by redesigning the balance (wing position, gear, forward fuselage) and flight-testing rotation and stall warning. That is engineering, not a kit-logistics fix.

### The Prescott and the Rohr 2-175: is the configuration the thread?

Bill's two highest-interest designs may share a theme: a clean forward fuselage with the propeller at the back. **What the evidence shows:**

| | Prescott Pusher | Rohr 2-175 |
|---|---|---|
| Engine | In the tail cone right behind the cabin | Buried in the fuselage behind the seats |
| Drive | 12 in prop extension; no drive failure on record | Short extension shaft; redesigned for vibration; one coupling failure in flight |
| Propulsor | Open 65-68 in prop, marginal ground clearance | 40 in fan in a duct, enclosed |
| Planform | Conventional, AR 7.8, T-tail | Tailless delta, AR 2.2, elevons |
| Structure | Steel-tube cage, fibreglass shells, riveted aluminium wing | Sparless foam-core fibreglass stressed skin |
| Storage | 29.3 ft span, no folding | 20 ft span, outer wings and fin fold for a single-car garage |
| Seats, weight | 4 (really 2+2), 2,400 lb | 2, 1,450 lb |
| Cooling | Oil overheat fixed by moving the cooler; hot rear cylinder | Dorsal scoop and exhaust ejector; no overheating at 108 deg F |
| Takeoff and pitch | Pitch-sensitive in ground effect, aft CG, hard rotation | Dog-tooth added for pitch-up; few flights, no handling record to speak of |

**What they share is real, and it is mass at the back.** Both put the propeller behind a clean cabin, and both pay for it in balance: the Prescott's documented aft-CG handling and nose ballast, and the 2-175's scale-up limit (Study 1 of its dossier), where two rows of seats ahead of the engine strain a tailless wing's trim range. Both also had to work at cooling an engine with no propeller blowing over it. **Where they differ is everything else**: planform (the opposite ends of the aspect-ratio argument), propulsor (open prop with a clearance problem against a duct that removes it), structure and storage. So the configuration is a thread in its benefits (a clean, quiet cabin and a protected or short drive) and in its one shared problem (CG); the planform is not shared, and AER-3807 weighs that separately.

### Independent performance check

Model: `docs/shortlist/check/models/prescott-pusher.json`; result: `docs/shortlist/check/results/prescott-pusher.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 167 ft2, Wing 205 ft2, HTail 61 ft2, Fin 29 ft2; total 463 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 29.33 ft, area 110.8 ft2 (F, Tom Prescott's 2007 spec, TP07); root 4.67 ft and tip 3.00 ft (F, RCM 1986 prototype table) scaled 2% to close 110.8 ft2: 4.58 / 2.94 ft. NLF(1)-0215F, 15%, root modified (P, Sport Aviation Mar 1986). Sweep about 10 deg (P).
- Fuselage length 20.28 ft, width 3.67 ft (F, RCM table); height 4.3 ft (E, ours: 42.5 in cabin plus structure; overall height 8 ft 9 in includes the gear and T-tail). Engine in the tail cone, prop on a 12 in extension (P).
- T-tail: horizontal tail 29.3 ft2, 11.0 ft span, root 3.33 ft, tip 2.17 ft (F, RCM prototype table). Fin about 16 ft2 (E, scaled from the 1/5-scale RCM plan).
- Laminar run x_tr: wing 0.25 (NLF section on a flush-riveted metal wing with stretch-formed leading edges; less credit than a composite), tails 0.15, fuselage 0.05.
- Retractable gear (prototype 2 and the retractable kit, P); the fixed-gear kit would add drag (not modelled).
- Cooling factor 1.2 (E): an air-cooled engine buried in a tail cone, with a documented oil-overheat fix and a hot rear cylinder in the field (AOPA 1986; Sport Aviation 1991).
- Prop 65 in (F, factory recommended), installation factor 0.95 for a pusher in the fuselage wake (E, as for the other pushers).
- Original installed engine mass 330 lb = O-360 dry about 285 lb x 1.15 (E).
- No published point states both altitude and power (Kitplanes May 1988: 151 KTAS at 73%, altitude not published; brochure: 165 KTAS at 7,500 ft, power not stated), so the fleet calibration is used and the two points are examined separately (see the dossier).

**Drag factor used: 1.29** (fleet calibration (no published point with known power); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.16.

**Drag build-up at 7,500 ft, 135 hp, 2,300 lb, with the factor applied:** 169 KTAS, CD0 0.0203 on S = 110.8 ft2, propeller efficiency 0.79, L/D 11.3.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.691 | Swet 205.4 ft2, Re 5.7M, Cf 0.00251, FF 1.342, Q 1.00, x_tr 0.25 |
| HTail | 0.246 | Swet 60.7 ft2, Re 4.2M, Cf 0.00297, FF 1.265, Q 1.08, x_tr 0.15 |
| Fin | 0.103 | Swet 29.4 ft2, Re 6.6M, Cf 0.00272, FF 1.224, Q 1.05, x_tr 0.15 |
| Fuselage | 0.532 | Swet 167.0 ft2, Re 30.6M, Cf 0.00236, FF 1.351, Q 1.00, x_tr 0.05 |
| cooling | 0.084 | Raymer 12.39 x 1.20 |
| leakage+protuberance | 0.083 | 5% of the rest |
| calibration factor | 0.505 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.402 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 135 hp at 7,500 ft gives 170 KTAS; still-air range on full usable fuel from MTOW 865 nm (climb allowance 21 lb); payload at 1,000 nm cannot lb with no reserve, cannot lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change +61 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 197 (205) | 789 (789) | 694 | cannot | cannot (cannot) | 166: cannot / cannot |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 210 (219) | 789 (789) | 718 | cannot | cannot (cannot) | 176: cannot / cannot |

### Engine fit with the Aeromomentum line

- **AM20T** (260 hp; 195 hp assumed continuous): 194-207 KTAS at its critical altitude, but 61 lb heavier installed than the O-360, in the tail, which needs about 82 lb of nose ballast (E). See the levers table.
- **AM15T** (160 hp; 120 hp assumed continuous): 26 lb lighter, keeps useful load, cruises at the 160 KTAS floor.
- **Cooling:** liquid cooling would end the tail-cone air-cooling struggle, with a radiator inlet where the oil cooler went (the nose) or in the cone; not designed.
- **Propeller:** the geared Aeromomentum output and a constant-speed prop should recover some of the efficiency the short fixed-pitch prop lost; clearance still limits diameter.

### Rights and provenance (stage 2)

Open question (Elon, `docs/rights/prescott-pusher.md`, PR #6). No type certificate; a kit. The engineering record survives at the San Diego Air & Space Museum (Prescott Aeronautical Corporation Collection, SC.10269, open for research): the general-assembly drawing and well over a hundred part drawings including the prop extension, the basic loads report, a wind-tunnel evaluation, structural test reports, the pilot's manual and all kit manuals. Who owns the design rights is not known: the company stopped trading in 1989-1991, and no buyer or bankruptcy record has been found; the second prototype's later owner, "Pusher Aircraft Inc" of Wichita (registry to 2018), is a lead. Custody of papers is not ownership of copyright; an attorney is needed before any use. Reading the collection is museum contact, so Bill's call.

### Safety record

Record (NTSB bulk databases and CAROL, plus foreign reports): 4 confirmed US events, 1 fatal (N58PP, 1990, a Ford V-6 conversion whose engine seized on its first flight, LAX90DUM02), and a probable fifth, also fatal and also a Ford V-6 (N75FM, 1990, CHI90DEE10). Two events are tied to the pusher layout: the cabin door came off in flight and struck the propeller (N19PP, 2009, CEN09CA386), and a wooden propeller separated in cruise (N43PP, 2005, LAX05LA270). One go-around ended in a pitch-up and stall (N747P, 1992, MIA92LA186) on an aircraft whose builder had reported pitch sensitivity and roll-off at lift-off. About 20 airframes with unknown hours: no rate is possible.

### Why it died, and whether a revival fixes it

See "Why it died, properly" above: early handling and performance disappointment tied to the aft CG of an engine in the tail, a financing change from pay-as-you-build to pay-up-front, parts that lagged marketing, and a sale abroad in 1988. A revival fixes the business causes directly and the handling causes only by redesigning the balance.

### Not yet done

- MANUFACTURING (AER-3784): the modern-structure empty-weight delta, which replaces our placeholders in the levers table.
- Kitplanes May 1988 in full (the 151 KTAS conditions), Flying (Oct 1985, Apr 1988) and Popular Mechanics (Aug 1986): not reachable online; a library or a purchased scan would settle the measured basis.
- Reading SDASM SC.10269 (the loads report, the wind-tunnel evaluation, the weight-and-balance schedule): museum contact, Bill's call. It would replace most of our estimates.
- A re-derivation sketch at about 2,700 lb with the CG, gear and propeller clearance laid out together (AERO, if it goes forward).
- What a modern rebuild changes in mass, cost and build hours (MANUFACTURING, stage 4, AER-3784).

<!-- stage3:end -->

<!-- stage4:start -->

## Stage 4: what modern manufacturing changes (AER-3784)

Full study (rank 2). Method, prices and sources are in [docs/MANUFACTURING.md](../MANUFACTURING.md#prescott-pusher); the weight table is generated by `docs/manufacturing/weights.py`. Desk study: nothing weighed or quoted by us, nobody contacted. Every E is our estimate.

**Original construction:** a TIG-welded 4130 square-tube cage under non-structural fibreglass shells of 3-8 plies, riveted to bulkheads. The wing is riveted aluminium: a press-brake 2024 C-spar, stretch-formed leading edges on CAD/CAM steel dies, and flush-riveted skins. The engine is in the tail cone. The museum collection SC.10269 holds the drawings and test reports; reading it is Bill's call.

**First, what to delete:** the 3-8-ply fibreglass shells (carbon sandwich instead); the stretch-forming dies, if the wing goes to molded carbon; the carburettor, magnetos and air-cooled baffles in a tail cone that overheated (a liquid-cooled engine with a ducted radiator); the 1980s panel.

**Empty weight:** rebuild **1,380-1,630 lb**, useful load **770-1,020 lb** at 2,400 lb gross (published 850; the weighed builder aircraft had 739). Only the light end reaches 1,000 lb. The AM20T installs +54 to +71 lb over the O-360, in the tail cone, where each pound needs about 1.3 lb of nose ballast (AERO). The aft weight savings avoid about 20-55 lb of that ballast. Gross weight (STRUCTURES) and balance are the levers that decide it.

**Re-derived at about 2,700 lb gross with 90 gal (AERO's case):** the structure grows +30 to +85 lb (E; Raymer GA weight scaling plus area for the same stall speed, tankage and fittings). AERO's levers use +30. Rebuild empty 1,410-1,720 lb, useful load 980-1,290 lb, before the engine and ballast.

**Weight build-up:**

| Item | Light, lb | Heavy, lb | Basis | Grade |
|---|---|---|---|---|
| Starting empty weight | 1,550 | 1,661 | 1,550 published spec (F, Prescott 2007); 1,661 for the one weighed builder aircraft, from its 739 lb useful at 2,400 lb gross (B, AERO's stage 3 dossier). The 1986 design target was 1,220 lb (P, AOPA Pilot Mar 1986) | F/B |
| Fuselage shells: non-structural fibreglass, 3-8 plies, riveted to bulkheads over the 4130 cage -> infused carbon sandwich shells (cage kept) | -70 | -25 | 167 ft2 fuselage wetted (AERO OpenVSP). Glass at 3-8 plies is 0.35-0.92 lb/ft2 (58-154 lb); a non-structural carbon sandwich is 0.20-0.30 lb/ft2 (33-50 lb) | E |
| Wing: 2024 press-brake C-spar with extrusion caps, ribs, stretch-formed leading edges and flush-riveted skins (110.8 ft2) -> molded carbon wing | -60 | -20 | Metal GA wing about 2.0-2.5 lb/ft2 of exposed planform (Raymer, approximate weight build-up), about 190-240 lb; a molded carbon wing saves 10-25% (E) | E |
| T-tail: aluminium -> carbon | -15 | -5 | Tail areas not published; about 40-60 lb of tail (E) | E |
| Panel: 1980s avionics -> EFIS | -30 | -10 | 1980s panel | E |
| EFI engine: backup battery and bus | +5 | +10 | One ECU | E |
| Pusher radiator duct and cowl for a liquid-cooled engine aft of the cabin | -5 | +15 | Duct may add; the air-cooled baffles come out | E |
| **Rebuild empty weight, no engine credit** | **1,380** | **1,630** | sum, rounded to 10 lb | E |
| Option, not in the total: Replace the 4130 cage too: structural carbon monocoque fuselage | -70 | -30 | Cage about 90-140 lb for a four-seat tube fuselage (E); a load-carrying shell adds most of it back; loses the cage's crash protection; needs STRUCTURES | E |
| Option, not in the total: Nose ballast avoided by the aft savings (tail and the aft part of the shell), AM20T case only | -55 | -20 | AERO: each pound behind the cabin needs about 1.3 lb of nose ballast. Aft savings of about 15-43 lb (tail, plus about 40% of the shell) avoid about 20-55 lb of the 82 lb AERO carries for the AM20T | E |
| Option, not in the total: Re-derived for about 2,700 lb gross with 90 gal (AERO's re-derivation case) | +30 | +85 | Raymer GA weight equations at a gross ratio of 1.125: wing (Nz W)^0.49, tail 0.38-0.41, fuselage 0.18, main gear 0.77 give +19 to +26 lb at fixed area. Wing and tail area grown to hold the stall speed add about +17 to +24 lb; 90 gal of leading-edge tankage +10-20; heavier attach fittings up to +15 | E |

**Cost, hours, home shop:**
- **Original kit:** $29,500 fixed-gear or $36,500 retractable, with a 1,500 h factory estimate (P, AOPA Pilot 1986).
- **Kit-run tooling:** service tooling for a small run is $60-180k (E).
- **Home shop:** home-molded shells take about 217 ft2 of mold surface, 430-870 h and $3-9k (E).
- **Still a service:** the welded cage (or a qualified welder), and the stretch-formed leading edges and press-brake spars if the wing stays metal.

<!-- stage4:end -->
