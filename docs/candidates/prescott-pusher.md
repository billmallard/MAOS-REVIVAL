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

Two screens, never mixed: the maker's figures as published, and measured or reported data. Useful load and range are targets: a miss is reported with its size, and payload against range is the tradeoff to read. Cruise above 160 KTAS is a floor.

- **As published: fail** - UL -150 lb, range -131 nm
  - Useful load: 850 lb (fail) against 1,000 lb.
  - Range: 869 nm (fail; not stated (1,000 mi)) against 1,000 nm.
  - Cruise: 165 KTAS at 7,500 ft (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm, lb, no reserve / 45 min: cannot (866 nm max).
- **Measured or reported: partial: UL fail, speed near, speed unconditioned** - UL -261 lb, speed -9 kt
  - Useful load: 739 lb (fail) against 1,000 lb.
  - Range: - nm (?; none found) against 1,000 nm.
  - Cruise: 151 KTAS at an unstated altitude (near) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm, lb, no reserve / 45 min: cannot (866 nm max).
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

**Rank 2, top tier.** As published it passes speed (165 KTAS at 7,500 ft) and misses useful load by 150 lb (850) and range by about 130 nm (869 nm, reserve not stated). As measured it is weaker: the one weighed builder aircraft had 739 lb useful, and Kitplanes measured 151 KTAS at 73% at an unpublished altitude, which our model can reproduce only with a drag factor of 1.46-1.67 against the brochure's 1.35. On an AM20T it is fast. As built on 56.5 gal it reaches 648-705 nm, 30-35% short of the range target, with 660-878 lb useful. **It meets both targets on both drag bases only as a re-derivation** at about 2,700 lb gross with 90 gal, and the useful-load target only if the rebuild lands at the light end of MANUFACTURING's structure estimate: 1,142 lb useful, 1,044-1,151 nm, 179-201 KTAS (AER-3866, corrected by AER-3902). At the heavy end useful load is 860 lb, 14% short. Over 1,000 nm with a 45 min reserve at continuous power the re-derivation carries up to 606 lb (light end, brochure basis, 16,000 ft) and nothing on the measured basis at 8,000 ft; at 800 nm it carries 380-691 lb across both ends and bases ([payload-range table](#payload-range-on-the-am20t-aer-3900)). The balance is worse than our first plan-station pass said: once N747P's published 49 lb of ballast and the constant-speed propeller are counted, the AM20T needs 113-130 lb of nose ballast at 2,700 lb, or 51-69 lb even with its radiator in the nose. SAFETY reviewed the balance options and the landing technique (AER-3899): it does not recommend against revival, but against reviving the original configuration plus a balance fix. Its two great assets are a short 12 in prop extension instead of a drive shaft, and the best-preserved engineering record in the survey (SDASM SC.10269: drawings, loads report, wind-tunnel evaluation, structural tests). Its weakness is handling, and it is now specific (SAFETY's verdicts are in [the safety review](#safety-review-aer-3899)): main wheels 21-28 in behind the CG range on prototype 1 (a 30-38 deg tipback, against the usual 15), a tail volume of about 0.50, and a stick-free static margin of only about 6% at the aft limit (all our estimates). The AM20T makes rotation harder through its thrust on a high thrust line more than through its weight. It ranks behind the Aries, which comes close to every target on a straight engine swap (useful load met, range 8-9% short at continuous power), and ahead of the Express, because its engineering survives and it has no long shaft or known tail flaw.

### Idea ledger (what a new airplane should keep)

- **A pusher without a drive shaft.** Engine in the tail cone, prop on a 12 in extension: the clean forward fuselage and quiet cabin of a pusher without the VK-30's shaft risk. No drive failure is on record.
- **Build sequence for a home shop.** A welded tube cage with every system installed before non-structural fibreglass shells go on; shells from CAD-cut patterns. The plugs cost about a tenth of the $200,000 factory tooling (Sport Aviation 1986).
- **CAD/CAM from day one** ("the first aircraft in its class totally designed using CAD/CAM", SDASM), with stretch-formed leading edges on CAD-made dies: a 1980s preview of a digital kit.
- **An NLF(1)-0215F laminar wing** with reflexed flaps and ailerons, on a metal structure.
- **The archive.** Drawings, loads, wind-tunnel and structural test reports in a public museum collection: the strongest re-derivation basis in the survey (rights and use terms: attorney, per Elon).
- Lesson: put the CG, the main gear and the propeller clearance together first; an engine in the tail drives all three, and the Prescott's handling complaints trace to that.
- Lesson: a financing model that turned pay-as-you-build into pay-up-front, and parts that lagged marketing, lost the builders' trust before the airplane could earn it.

### Published, measured and our check, side by side

Read across a row only within one column's basis. Useful load and range are targets; cruise above 160 KTAS is a floor.

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

*Stage 3 record (2026-10-24). Its structure placeholders and its balance arms (8 ft and 6 ft, so 1.33 lb of ballast per pound of engine) are superseded by [the re-derivation below](#the-re-derivation-with-the-structure-delta-and-the-balance-aer-3866); the fuel and power levers still stand.*

Bill's question: on an Aeromomentum engine, turbo-normalised at altitude, what moves useful load (850 lb published, 150 short), range (869 nm published, about 130 short) and speed, and how close does it come to the targets? Script and full tables: `docs/shortlist/check/prescott/levers.py`. Assumptions: 195 / 120 hp continuous and 8,000 / 16,000 ft critical altitudes are ours; the structure deltas are placeholders until MANUFACTURING (AER-3784) answers; the 75 and 90 gal tankage is our estimate (the 15% wing has about 280 gal of geometric volume).

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

**What each lever buys.** More power at altitude buys speed and nothing else: the AM20T lifts cruise to 194-207 KTAS and costs useful load through the tail-cone weight. More fuel buys range and nothing else: 90 gal reaches 1,000 nm at continuous power on both bases. A lighter structure buys useful load pound for pound, but at 2,400 lb even 200 lb lighter leaves the AM20T version at 907 lb. **It meets all three on both bases only as a re-derivation**: a structure designed for about 2,700 lb gross, about 100 lb lighter than today's structure would be at that weight, 90 gal, and the AM20T. The AM15T alternative meets the load and range targets at 2,400 lb with a 200 lb lighter structure, but its cruise speed falls to the 160 KTAS floor (159-169 KTAS). With 90 gal aboard at 2,700 lb, the AM20T re-derivation carries about 540 lb of people and baggage: it is a four-seater with full fuel only for light occupants, as the original was.

**The real constraint is balance, not power.** The AM20T makes the Prescott fast, but its weight in the tail cone makes the documented aft-CG problem worse. A re-derivation would move the wing aft or lengthen the forward fuselage to put the CG where the gear and the tail want it, and that, not the engine, is the design work.

### The re-derivation, with the structure delta and the balance (AER-3866)

Bill picked the Prescott on AER-3783. This section folds in MANUFACTURING's structure estimate (AER-3784) and works the balance on the AM20T. Script, inputs and full tables: `docs/shortlist/check/prescott/balance.py` and `balance_output.md`; how each station was read: that folder's README. The AM20T's 195 hp continuous rating and its critical altitudes are still **our assumptions** (Bill will ask Aeromomentum himself, AER-3800; the survey carries the assumptions until then). Every number here is our estimate (E) unless graded otherwise.

*Corrected 2026-10-25 (AER-3902), on SAFETY's review (AER-3899, section 1): N747P's 49 lb of ballast is published, so the empty-CG reference is now the airplane that needed it; the AM20T's constant-speed propeller is now in the weight and balance; option C now pays for its own neutral-point loss. The numbers below are the corrected ones. The output's correction ledger walks from PR #10's first numbers to these, one correction at a time.*

**The geometry now comes from the designer.** Tom Prescott's 1/5-scale plan and article (*RCM*, July 1986) give one full-scale station in the text (main wheels at FS 244, nose tip FS 92, F) and a dimensioned side view. We measured the rest off it:

| Quantity | Value | Basis |
|---|---|---|
| Designer's C.G. range | FS 216.2-222.9, 12.7-27.0% MAC | E, drawn on the model plan; full-scale status not stated |
| Main wheels | FS 244, so 21-28 in behind the CG range; tipback 30-38 deg (usual: about 15) | F (station), E (angle) |
| Tail volume | 0.50 (GA singles typically 0.6-0.8) | E, tail arm 7.5 ft |
| Neutral point | 39% MAC stick fixed (36-43%), about 33% stick free | E, AVL wing + T-tail 48.7% (hand check 49.6%), less the fuselage (Raymer eq. 16.25) |
| Static margin at the aft limit | about 12% stick fixed, about 6% stick free | E |
| Engine and nose-bay arms from the aft limit | 73 in behind, 123 in ahead | E |
| Ballast per pound of engine | 0.6 lb (stage 3 assumed 1.33) | E |
| Ballast per pound at the propeller plane (FS 322) | 0.8 lb | E |
| Empty CG of the original, on N747P's 49 lb of ballast | 1.8-3.6 in aft of the no-ballast reference (ballast at FS 160 or FS 100; its station is not published) | P (49 lb, SA91), E (station) |
| Propeller change for the AM20T | +34 to +41 lb at FS 322: a 3-blade constant-speed set with spinner (54-61 lb) against about 20 lb of wood | F (MT STC flyers), E (wood) |
| Neutral-point loss from a forward stretch | 0.09% MAC per inch (0.085-0.10) | E, Multhopp strip method |

**1. Useful load and range at the re-derived gross.** AM20T, 2,700 lb, 90 gal, wing and tail 12.5% larger to hold the stall speed (MANUFACTURING's weight assumes it), balance by option B below. Still air, no reserve, full fuel from gross, at continuous power. Critical altitude 8,000 / 16,000 ft.

| Structure end (MANUFACTURING) | Empty, lb | Useful load | Payload with full fuel | Brochure basis (k 1.35): KTAS / nm | Measured basis (k 1.55): KTAS / nm | Against the targets (speed is a floor) |
|---|---|---|---|---|---|---|
| Light (rebuild 1,380 lb at 2,400 lb, +30 lb for 2,700) | 1,558 | **1,142** | 602 | 188-201 / 1,100-1,151 | 179-190 / 1,044-1,093 | **all three met** on both bases |
| Heavy (rebuild 1,630 lb, +85 lb) | 1,840 | **860** | 320 | 188-201 / 1,100-1,151 | 179-190 / 1,044-1,093 | useful load 140 lb (14%) short; range and speed met |
| At 2,400 lb, 56.5 gal (no re-derivation), light / heavy | 1,522 / 1,740 | 878 / 660 | 539 / 321 | 194-207 / 683-705 | 184-196 / 648-669 | useful load 12-34% short; range 30-35% short |

The useful-load target is met at 2,700 lb if the rebuilt empty weight with the AM20T is 1,700 lb or less. MANUFACTURING's range, with the corrected balance, puts it at 1,558-1,840 lb, so the target is met over about half of that range, and the heavy end is at most 14% short. The heavy end starts from the one weighed builder aircraft, N747P: 1,661 lb, of which 49 lb was ballast (SA91, P). That ballast is now taken out and re-solved, so the heavy end no longer double-counts it. Range exceeds 1,000 nm on both drag bases at both critical altitudes. At 16,000 ft the speed is 3-4 kt below stage 3's 2,700 lb figures (204 / 194 KTAS): the cost of the larger wing and tail, which stage 3 left out.

**2. The balance options.** Each is sized alone so the most-aft standard loading (one pilot, 100 lb of bags, 45 min of fuel) sits on the designer's aft limit, at 2,700 lb with 90 gal. Without a fix, the AM20T with its radiator in the tail cone puts that loading 7.6-7.7 in aft of the limit (headline datum: N747P's ballast at FS 100).

| Option | What it takes | Added weight, lb | Useful load, light / heavy | Side effects |
|---|---|---|---|---|
| A. Nose ballast | lead in the nose battery bay (FS 100) | 113-130 | 1,087 / 805 | none on drag; pure dead weight |
| **B. Masses forward** | **radiator and coolant (35 lb) in the nose bay, where the prototype's oil cooler went; remote avionics boxes forward; lead for the rest** | **57-75** (6 of coolant lines, 51-69 of ballast) | **1,142 / 860** | a nose inlet and about 30 ft of coolant line, a single point of failure of the only engine (SAFETY R8); the radiator inlet sees clean air |
| C. Fuselage stretch | a 36-43 in plug between the front seats and the spar, sized to hold A's static margin | 29-34 | 1,171 / 901 | the neutral point moves forward 3-4% MAC, so the aft limit moves forward with it; the front seats move forward too, so the most-forward loading lands 2.5-2.6 in ahead of the forward limit; directional stability not computed. Outside what our weight model was built for: **not a sole fix** |
| D. Wing moved aft | 11 in, with its wing-mounted mains and tanks | about 10 (cage rework) | 1,190 / 925 | the mains move aft too, so rotation gets harder; tail arm and tail volume shrink |

The battery, hydraulic pack and oil cooler were already in the nose on the prototype (SA86, AOPA86, P), so "moving masses forward" has only the new items left to move. The radiator is the one big one. The stage 4 section below now carries the 0.6 ratio (about 9-25 lb avoided by the aft savings, against stage 4's 20-55 lb at 1.3); those savings are already placed at their stations in the numbers above, so they are not a further credit.

**Option B still carries the targets with the least added weight, but it no longer does it alone.** PR #10 put the original exactly on its aft limit with no ballast, the kindest reading, and found B needed 6 lb and no lead. SAFETY found what we had missed: N747P's ballast is published ("With paint, interior, avionics and 49 pounds of ballast necessary to get the weight and balance within its prescribed limits, the final weight came out at 1,661 pounds", SA91 p. 49, the sentence broken across columns in the scan). That moves the original's empty CG 1.8-3.6 in aft, depending on where the 49 lb sat. Moving the radiator forward absorbs about 4 in, so B alone would just about cover the datum; but the AM20T also needs a constant-speed propeller that PR #10 left out, 34-41 lb heavier than the wood one at the far end of the airplane. With both, B needs 51-69 lb of residual lead at the FS 100 datum (28-45 lb at FS 160). A, with no radiator move, needs 113-130 lb (90-107 lb at FS 160). D needs the least added weight but SAFETY rules it out. A weighed survivor or SDASM's weight-and-balance schedule would close the datum range; both are contact, so Bill's call. B holds the CG; it does nothing for rotation.

**Rotation is the harder problem, and balance does not solve it.** A quasi-static moment balance about the main wheels (E: CLmax 1.6 with take-off flap, ground-roll CL 0.5, full-up tail CL -1.0, thrust line 55 in above the ground) gives the speed at which full up elevator can just start the rotation, as a multiple of the stall speed:

| Case | Mains, FS | V_rot / Vs, aft to forward limit |
|---|---|---|
| Original, O-360, prototype 1 mains | 244 | 1.40-1.53 |
| Original, O-360, prototype 2 (mains about 8 in forward, P) | 236 | 1.27 at the aft limit |
| AM20T, 2,700 lb, prototype 2 mains | 236 | 1.35-1.50 |
| The same with a 30% larger horizontal tail | 236 | 1.24-1.36 |

A normal airplane rotates at about 1.1-1.2 Vs, and this one lifts off flat at about 1.8 Vs. The original's 1.4-1.5 is consistent with the record ("high takeoff (rotation) speeds", an airplane that "jumped off the ground unexpectedly"), which is the best check this estimate has. The AM20T makes it worse mostly through thrust, not weight: its extra take-off thrust on a thrust line about 19 in above the CG is worth moving the CG about 6 in forward. The mains cannot simply go further forward. At FS 236 the empty airplane's tipback, with option B's residual ballast, is already down to 14 deg, and at FS 232 it is 8 deg, so the airplane would sit on its tail when someone climbs into the back; the propeller-strike pitch angle also falls to 14-15 deg. What is left is tail power (a 30% larger tail costs about 3 kt and about 10 lb) or a lower thrust line, and both change the airplane's character. That is design work and flight test, not a balance fix.

**3. What desk analysis cannot clear about the handling.** This was the input to SAFETY's review (AER-3899, below):

1. **The CG envelope itself.** Our limits are drawn on a model plan, and the fleet's real empty CG is unknown (N747P needed 49 lb of ballast, SA91, at an unpublished station; its "prescribed limits" are not published either). SDASM's weight-and-balance schedule or a weighed survivor would settle it. Reading the SDASM file is museum contact.
2. **Stick-free stability and stick-force gradient at the aft limit.** Our stick-free margin of about 6% is a handbook estimate. The elevator hinge moments, the trim tab and how far the T-tail elevator floats are unknown, and they are the likely root of "pitch is quite sensitive" (AOPA86).
3. **Rotation and lift-off.** V_rot / Vs is a quasi-static estimate on assumed coefficients. Ground effect, elevator power at full deflection and the "jumps off" behaviour need flight test.
4. **The ground-effect pitch-up** AOPA was briefed on. A vortex-lattice model with a ground image could bound it, but not clear it.
5. **Pitch with power changes.** The thrust line sits about 19 in above the CG, so every power change is a trim change. Its sign and size with 260 hp are unproven, and one go-around ended in a pitch-up and stall (MIA92LA186).
6. **Stall.** There was no aerodynamic warning (AOPA86), and full-stall landings end abruptly (KP88). Deep stall of a T-tail at an aft CG is not tested in the record. SDASM's wind-tunnel evaluation may hold post-stall pitching moments.
7. **Spin.** The record shows it was never spin-tested.
8. **Dynamic stability.** AOPA saw three to four pitch oscillations after a bump. AVL gives a modest pitch damping (Cmq about -11). We claim nothing on the short-period or phugoid modes.
9. **Flutter.** A T-tail on a swept fin, now carrying a heavier, geared, liquid-cooled engine and a constant-speed propeller just behind it. There is no flutter clearance from any source.
10. **Torsional vibration** of the AM20T's reduction gearbox, the 12 in extension and the propeller: an untested combination on an installation that has already lost one propeller (LAX05LA270, cause undetermined).
11. **Structure.** The 2,700 lb gross, a stretch or a wing move, the gear relocation and a larger tail are all structural changes. STRUCTURES is not routed here.
12. **Propeller clearance** with a larger constant-speed propeller, and tipback when the airplane is lightly loaded.

### Safety review (AER-3899)

SAFETY reviewed the balance options, the approach and landing technique and the accident record, on Bill's approval (2026-10-25). The full review, verbatim, is [`docs/shortlist/check/prescott/SAFETY.md`](../shortlist/check/prescott/SAFETY.md); its sections 1-6 judged PR #10's numbers, before the corrections above. Those first verdicts, quoted (revision 1; see the addendum below for C):

| Item | SAFETY's verdict |
|---|---|
| A. Nose ballast | **Acceptable with mitigation** |
| B. Masses forward | **Acceptable with mitigation** |
| C. Fuselage stretch | **Acceptable only with a demonstrated margin** |
| D. Wing moved aft | **Not acceptable** |
| The landing technique | **acceptable with mitigation, and the mitigations have to be design changes.** |

In its words: "None of the four balance options makes this airplane safe on its own, because balance only fixes where the CG sits." And: "**I am not recommending against revival.** I am recommending against reviving it as the original configuration plus a balance fix. A re-derivation can be acceptable if it meets the outcome requirements in section 5." Those requirements, R1-R10 (stick-free margin, pitch change with power, an angle-of-attack stall warning, propeller and tail strike, rotation, spin and deep stall, ballast as built, the option B coolant loop, torsional vibration and flutter, transition training), are in the review's section 5 and are carried here as design constraints on any re-derivation.

SAFETY then re-reviewed the corrected numbers. Its ruling is the [addendum (revision 2)](../shortlist/check/prescott/SAFETY.md#addendum-revision-2-2026-10-25-re-review-of-aeros-corrected-numbers-aer-3902) at the end of the review, which governs where it differs from the table above. It changes one verdict, C, to "**Not acceptable as a sole fix**", and adds a ground-tipback condition to R7; read the addendum for the reasons and the rest of its verdicts.

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

**Original engine, our numbers:** 135 hp at 7,500 ft gives 170 KTAS; still-air range on full usable fuel from MTOW 865 nm (climb allowance 21 lb); no payload at 1,000 nm from gross weight, with or without a 45 min reserve (the tanks do not hold the fuel).

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change +61 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 197 (205) | 789 (789) | 694 | cannot | cannot (cannot) | 166: cannot / cannot |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 210 (219) | 789 (789) | 718 | cannot | cannot (cannot) | 176: cannot / cannot |

### Engine fit with the Aeromomentum line

- **AM20T** (260 hp; 195 hp assumed continuous): 194-207 KTAS at its critical altitude at 2,400 lb (179-201 KTAS at 2,700 lb with the larger wing). It is 61 lb heavier installed than the O-360 (E). On the plan's stations, with N747P's ballast datum and the constant-speed propeller, that needs about 106-112 lb of nose ballast at 2,400 lb on the published airplane (stage 3 said 82; our first plan-station pass, 33), and still 51-69 lb at 2,700 lb with the radiator and coolant (35 lb) in the nose bay where the oil cooler went (AER-3902). Its extra take-off thrust on the high thrust line makes rotation harder (see the re-derivation).
- **AM15T** (160 hp; 120 hp assumed continuous): 26 lb lighter, keeps useful load, cruises at the 160 KTAS floor.
- **Cooling:** liquid cooling would end the tail-cone air-cooling struggle, with a radiator inlet where the oil cooler went (the nose) or in the cone; not designed.
- **Propeller:** the geared Aeromomentum output and a constant-speed prop should recover some of the efficiency the short fixed-pitch prop lost; clearance still limits diameter.

### Payload-range on the AM20T (AER-3900)

Bill's ruling (2026-10-25): useful load and range are targets to report against, with no joint pass/fail; this is the tradeoff between them. Payload is occupants and baggage, in lb, with **no reserve / 45 min reserve**, still air, on the AM20T at the stage 3 assumptions (195 hp continuous, critical altitude 8,000 or 16,000 ft and cruise there, BSFC 0.45, economy 65% of continuous; none published by Aeromomentum). "cannot" means not even an empty cabin reaches it on full tanks. Past the full-tank point the airplane leaves below gross. No seat or baggage cap is applied. Each cell spans both critical altitudes and both drag bases (brochure k 1.35, measured k 1.55), with balance option B and its residual nose ballast (AER-3902). Our estimate (E); script `docs/shortlist/check/payload_range.py`, per-case rows in `payload_range_output.md` beside it.

| Design | Power | KTAS | 600 nm | 800 nm | 1,000 nm | 1,200 nm | Range on full tanks from gross, no reserve, nm |
|---|---|---|---|---|---|---|---|
| 2,400 lb, 56.5 gal, light end (1,522 lb empty) | continuous | 184-207 | 569-589 / cannot-153 | cannot / cannot | cannot / cannot | cannot / cannot | 648-705 |
| 2,400 lb, 56.5 gal, light end (1,522 lb empty) | economy 65% | 155-173 (under the 160 floor at the low end) | 633-644 / 590-602 | 560-579 / 154-514 | cannot-163 / cannot | cannot / cannot | 838-907 |
| 2,400 lb, 56.5 gal, heavy end (1,740 lb empty) | continuous | 184-207 | 351-371 / cannot | cannot / cannot | cannot / cannot | cannot / cannot | 648-705 |
| 2,400 lb, 56.5 gal, heavy end (1,740 lb empty) | economy 65% | 155-173 (under the 160 floor at the low end) | 415-426 / 372-384 | 342-361 / cannot-296 | cannot / cannot | cannot / cannot | 838-907 |
| 2,700 lb, 90 gal, light end (1,558 lb empty) | continuous | 179-201 | 823-842 / 758-777 | 726-756 / 662-691 | 630-670 / cannot-606 | cannot-320 / cannot | 1,044-1,151 |
| 2,700 lb, 90 gal, light end (1,558 lb empty) | economy 65% | 150-167 (under the 160 floor at the low end) | 885-899 / 843-857 | 812-830 / 770-788 | 737-763 / 696-721 | 664-697 / 623-656 | 1,350-1,479 |
| 2,700 lb, 90 gal, heavy end (1,840 lb empty) | continuous | 179-201 | 542-561 / 476-495 | 445-474 / 380-410 | 349-389 / cannot-325 | cannot-38 / cannot | 1,044-1,151 |
| 2,700 lb, 90 gal, heavy end (1,840 lb empty) | economy 65% | 150-167 (under the 160 floor at the low end) | 604-618 / 561-575 | 530-548 / 488-506 | 456-481 / 414-440 | 382-415 / 341-374 | 1,350-1,479 |

**Reading.** As built (56.5 gal) it is a 600 nm airplane at speed: 648-705 nm on full tanks at continuous power, 30-35% short of the range target, and with a 45 min reserve it carries at most 153 lb 600 nm. The re-derivation (2,700 lb, 90 gal) meets the range target, and with a 45 min reserve carries 476-777 lb 600 nm and 380-691 lb 800 nm across both structure ends and both drag bases. Over 1,000 nm at continuous power the reserve takes most of the margin: up to 606 lb at the light end on the brochure basis at 16,000 ft, 325 lb at the heavy end, and nothing on the measured basis at 8,000 ft. Economy power carries 414-721 lb 1,000 nm with the reserve, at 150-167 KTAS, partly under the speed floor. Which drag basis is real moves the 1,000 nm payload with reserve by about 300 lb, about as much as the structure end does; only a flight test of a rebuilt airplane settles it.

### Rights and provenance (stage 2)

Open question (Elon, `docs/rights/prescott-pusher.md`, PR #6). No type certificate; a kit. The engineering record survives at the San Diego Air & Space Museum (Prescott Aeronautical Corporation Collection, SC.10269, open for research): the general-assembly drawing and well over a hundred part drawings including the prop extension, the basic loads report, a wind-tunnel evaluation, structural test reports, the pilot's manual and all kit manuals. Who owns the design rights is not known: the company stopped trading in 1989-1991, and no buyer or bankruptcy record has been found; the second prototype's later owner, "Pusher Aircraft Inc" of Wichita (registry to 2018), is a lead. Custody of papers is not ownership of copyright; an attorney is needed before any use. Reading the collection is museum contact, so Bill's call.

### Safety record

Record (NTSB bulk databases and CAROL, plus foreign reports): 4 confirmed US events, 1 fatal (N58PP, 1990, a Ford V-6 conversion whose engine seized on its first flight, LAX90DUM02), and a probable fifth, also fatal and also a Ford V-6 (N75FM, 1990, CHI90DEE10). Two events are tied to the pusher layout: the cabin door came off in flight and struck the propeller (N19PP, 2009, CEN09CA386), and a wooden propeller separated in cruise (N43PP, 2005, LAX05LA270). One go-around ended in a pitch-up and stall (N747P, 1992, MIA92LA186) on an aircraft whose builder had reported pitch sensitivity and roll-off at lift-off. About 20 airframes with unknown hours: no rate is possible.

### Why it died, and whether a revival fixes it

See "Why it died, properly" above: early handling and performance disappointment tied to the aft CG of an engine in the tail, a financing change from pay-as-you-build to pay-up-front, parts that lagged marketing, and a sale abroad in 1988. A revival fixes the business causes directly and the handling causes only by redesigning the balance.

### Not yet done

- MANUFACTURING's structure delta (AER-3784): folded in by AER-3866.
- SAFETY: reviewed the balance options, the landing technique and the accident record (AER-3899, Bill approved); see [the safety review](#safety-review-aer-3899). STRUCTURES: the structural changes in the re-derivation, and R9's flutter and torsional items, are not routed; Bill's call.
- Kitplanes May 1988 in full (the 151 KTAS conditions), Flying (Oct 1985, Apr 1988) and Popular Mechanics (Aug 1986): not reachable online; a library or a purchased scan would settle the measured basis.
- Reading SDASM SC.10269 (the loads report, the wind-tunnel evaluation, the weight-and-balance schedule): museum contact, Bill's call. It would replace most of our estimates.
- A drawn re-derivation layout at about 2,700 lb with the CG, gear and propeller clearance together. The balance, gear and rotation numbers are in AER-3866; the drawing is still to do (AERO, if it goes forward).
- What a modern rebuild changes in mass, cost and build hours (MANUFACTURING, stage 4, AER-3784).

<!-- stage3:end -->

<!-- stage4:start -->

## Stage 4: what modern manufacturing changes (AER-3784)

Full study (rank 2). Method, prices and sources are in [docs/MANUFACTURING.md](../MANUFACTURING.md#prescott-pusher); the weight table is generated by `docs/manufacturing/weights.py`. Desk study: nothing weighed or quoted by us, nobody contacted. Every E is our estimate.

**Original construction:** a TIG-welded 4130 square-tube cage under non-structural fibreglass shells of 3-8 plies, riveted to bulkheads. The wing is riveted aluminium: a press-brake 2024 C-spar, stretch-formed leading edges on CAD/CAM steel dies, and flush-riveted skins. The engine is in the tail cone. The museum collection SC.10269 holds the drawings and test reports; reading it is Bill's call.

**First, what to delete:** the 3-8-ply fibreglass shells (carbon sandwich instead); the stretch-forming dies, if the wing goes to molded carbon; the carburettor, magnetos and air-cooled baffles in a tail cone that overheated (a liquid-cooled engine with a ducted radiator); the 1980s panel.

**Empty weight:** rebuild **1,380-1,630 lb**, useful load **770-1,020 lb** at 2,400 lb gross (published 850; the weighed builder aircraft had 739). Only the light end reaches 1,000 lb. The AM20T installs +54 to +71 lb over the O-360, in the tail cone, where each pound needs about 0.6 lb of nose ballast on the designer's plan stations (AER-3866; stage 4 used 1.3). The aft weight savings avoid about 9-25 lb of ballast; AERO's balance already places them at their stations, and at 2,700 lb with the radiator in the nose (option B) it still needs 51-69 lb of lead (AER-3902). Gross weight (STRUCTURES) and balance are the levers that decide it.

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
| Option, not in the total: Nose ballast avoided by the aft savings (tail and the aft part of the shell), AM20T case only | -25 | -9 | AERO, on the designer's plan stations: each pound behind the cabin needs about 0.6 lb of nose ballast (AER-3866; stage 4 used 1.3, giving 20-55 lb). Aft savings of about 15-43 lb (tail, plus about 40% of the shell) avoid about 9-25 lb. AERO's balance (AER-3902) already places these savings at their stations, so they are inside its 1,558-1,840 lb at 2,700 lb, not a further credit | E |
| Option, not in the total: Re-derived for about 2,700 lb gross with 90 gal (AERO's re-derivation case) | +30 | +85 | Raymer GA weight equations at a gross ratio of 1.125: wing (Nz W)^0.49, tail 0.38-0.41, fuselage 0.18, main gear 0.77 give +19 to +26 lb at fixed area. Wing and tail area grown to hold the stall speed add about +17 to +24 lb; 90 gal of leading-edge tankage +10-20; heavier attach fittings up to +15 | E |

**Cost, hours, home shop:**
- **Original kit:** $29,500 fixed-gear or $36,500 retractable, with a 1,500 h factory estimate (P, AOPA Pilot 1986).
- **Kit-run tooling:** service tooling for a small run is $60-180k (E).
- **Home shop:** home-molded shells take about 217 ft2 of mold surface, 430-870 h and $3-9k (E).
- **Still a service:** the welded cage (or a qualified welder), and the stretch-formed leading edges and press-brake spars if the wing stays metal.

<!-- stage4:end -->
