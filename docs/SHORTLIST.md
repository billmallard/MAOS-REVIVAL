# Stage 3 shortlist: eight designs ranked on our own performance check

**Status:** stage 3 of the legacy survey (AER-3783), compiled 2026-10-24 by AERO.
It builds on the stage 1 long list (`docs/longlist/LONGLIST.md`, PR #2) and on
Elon's stage 2 rights files (`docs/rights/`, PR #3). Bill decides which designs,
if any, go to development.

This is a desk study. Every number below is our estimate from published geometry
and published weights, calibrated against published flight data. Nothing has been
flown, weighed or measured by us. Rights notes are research, not legal advice.
Nobody has been contacted.

## The ranking

| Rank | Design | Seats | On the Aeromomentum line: KTAS / useful load / payload at 1,000 nm with 45 min (our check, two engine cases) | Rights (stage 2) | Safety record | Why it died; does a revival fix it? |
|---|---|---|---|---|---|---|
| 1 | [Rutan Defiant](candidates/rutan-defiant.md) | 4 | 178-190 KTAS / 1,350 lb / cannot-669 lb on 2x AM15T | Open question: no 1985 buyer on the record; likely holder RAF or Burt Rutan, who owns little (plans copyright) and objects to unlicensed building | 6 NTSB events, 2 fatal, about 30 built; nose gear is the recurring item; no engine-out accident | Certification money, then liability. Yes: an experimental revival needs neither |
| 2 | [Lancair IV-P](candidates/lancair-iv-p.md) | 4 | 200-211 / 1,350 / cannot-824 on AM20T | Open question: chain of title. Scope of the 2023 JetEXE purchase is not public, molds unlocated since 2017; parts support continues | 88 NTSB events, 43 fatal, about 360 built; low-altitude stall-spin and engine failure followed by stall | Kits retired for newer models. The safety pattern is the real problem, and a revival does not fix it by itself |
| 3 | [Mooney 301](candidates/mooney-301.md) | 6 | 176-187 / 1,452 / 858-867 on AM20T | Open question: Mooney International or Daher, unresolved; nothing usable survives on either path. Attorney first | One prototype, no accidents; the test pilot called its pitch control "not certifiable" | Corporate sale; new owners wanted a 300 kt turboprop. Partly: the market gap is real, but nothing survives to revive except published geometry |
| 4 | [Cirrus VK-30](candidates/cirrus-vk-30.md) | 5 | 199-212 / 1,350 / 815-825 on AM20T | Firmly held by Cirrus (AVIC-controlled): unlikely | 7 NTSB events, 5 fatal, about 13 built; driveshaft, cruise-flap flutter and an aft-CG spin are tied to the design | Cirrus left kits for certified aircraft. Only if the shaft drive and the flutter are designed out |
| 5 | [Velocity XL-RG](candidates/velocity-xl-rg.md) | 4 | 186-199 / 1,000 / 440-457 on AM20T, **100 gal optional tanks only** (cannot on standard 70 gal) | Firmly held: a live product (Velocity Inc.) | 26 NTSB events, 5 fatal, about 230 built; one door-into-prop fatal; one NTSB design finding on winglet-rudder flutter | Not dead. An AM20T kit option is a partnership question, not a revival |
| 6 | [Wheeler Express](candidates/express-2000.md) | 4 | 179-191 / 890 / cannot (439-445 at economy power) on AM20T | Open question: last holder (2007) has no visible trace | 17+ US NTSB events, 13 fatal worldwide, about 55 active; about 9 of the 13 fatal are stall or loss of control, and the NTSB named the design's poor yaw stability (CEN15FA321) | A fatal crash collapsed sales, then three bankruptcies. Only with a new tail |
| 7 | [Berkut 360](candidates/berkut-360.md) | 2 | not credible (see below) / 949 / cannot at continuous power; 608-616 at economy power | Open question: molds unaccounted for since 2009 | 9 NTSB events, 2 fatal, about 31 aircraft; builder errors and gear | Founder lawsuits and bankruptcy. Yes, if the molds are found |
| 8 | [Cessna P210N](candidates/cessna-p210n.md) | 6 | 161-171 / 1,658 / cannot at continuous power on AM20T (89 gal) | Firmly held by Textron: modify existing airframes, not a revival | 291 NTSB events, 78 fatal, 874 built; weather, oil-system engine failures, fuel | Cessna ended pistons in 1986. Not a revival candidate; here as the calibration case |
| ref | [Cozy MKIV](candidates/cozy-mkiv.md) | 4 | 202-217 / 808 / cannot (645-668 nm max at continuous power) on AM20T | Firmly held by Aircraft Spruce; the plans licence bars using the drawings for another design | 22 NTSB events, 7 fatal, about 350 built | Alive. Not a revival target |

How to read the performance column. "KTAS" is our speed at the AM20T's assumed
continuous power (195 hp, two AM15T at 240 hp for the Defiant) in the two engine
cases set out below: critical altitude 8,000 ft, cruising at 8,000 ft (the first
figure), and critical altitude 16,000 ft, cruising at 16,000 ft (the second).
"Useful load" takes no credit for a lighter engine. "Payload at 1,000 nm with 45
min" is the payload that flies 1,000 nm at that speed and altitude, from MTOW,
with fuel for a climb allowance and a 45 min reserve at cruise power. "cannot"
means the tanks do not hold the fuel. The full table, with the no-reserve case,
economy power and the optimistic bounds, is [below](#results-on-the-aeromomentum-line).

## What the check says

1. **No candidate carries 1,000 lb over 1,000 nm with a 45 min reserve on an
   Aeromomentum engine.** The best are the Mooney 301 (858-867 lb), the Lancair
   IV-P (824 lb, high-critical-altitude case only) and the Cirrus VK-30
   (815-825 lb). They all clear the useful-load floor (1,000 lb) and the range
   floor (1,000 nm) separately, and all three cruise above 160 KTAS (the
   IV-P and VK-30 above 180) at the assumed continuous power. The brief asks for
   the two together; this is the closest any of them gets, and we did not round it up.

2. **The reference fails harder than stage 1 said.** The CAFE Foundation weighed
   the Cozy MKIV test aircraft at 1,179 lb empty, not the designer's 1,050 lb, so
   its useful load is 871 lb, not 1,000. On its IO-360 our check gives 175 KTAS at
   8,000 ft and 829 nm on full usable fuel with no reserve. On an AM20T the
   heavier liquid-cooled installation drops useful load to 808 lb. Every
   shortlisted design except the Berkut beats the Cozy on payload at 1,000 nm.

3. **Our raw drag build-up is optimistic, and we corrected it rather than trust
   it.** The three types with instrumented flight test or handbook data need 1.16
   to 1.36 times the raw build-up to match their measured speeds: Express 1.16
   (CAFE), P210N 1.29 (POH, seven points), Cozy 1.36 (CAFE, four points). We use
   the median, 1.29, as the fleet calibration. The rest of the gap is cooling
   flow, leakage, roughness and propeller losses the build-up does not see; see
   [Method](#method).

4. **Two headline speeds read cleaner than any measured airplane.** The Lancair
   IV-P's 278 KTAS at FL230 on 262 hp (AOPA Pilot 1994) and the Mooney 301's
   237.5 KTAS at 17,500 ft on 270 hp (its test pilot, 2012) match our raw
   build-up at factors of 1.03 and 1.02. At the fleet calibration the same power
   gives about 255 KTAS and 217 KTAS. That is a finding: treat those figures as
   about 8% optimistic until a measured point says otherwise. We headline the
   fleet calibration for both.

5. **Two types read much draggier than their geometry.** The Rutan Defiant's
   published points need a factor of 1.72 (four points, two grades). It burns
   18 gph for 175 KTAS, 9.7 nm per gallon, against the Express's 15. Two
   cooling systems without cowl flaps, two fixed-pitch props and the front
   prop's slipstream over the fuselage are the likely reasons. The Velocity
   needs 1.63, but that rests on one pilot-report point at 3,000 ft and on
   geometry we had to scale from the Cozy, so it is low confidence. We use each
   type's own factor, so neither is flattered. A constant-speed prop on the
   geared Aeromomentum engine should recover some of the Defiant's loss. We
   have not credited it.

6. **The Berkut cannot be checked.** It has no measured performance anywhere, and
   its wing area (110 ft2) is unsourced. With the fleet calibration our model gives
   239 KTAS on 195 hp, faster than the designer's own 191 KTAS cruise claim.
   That means the geometry is wrong, not that the airplane is fast. Its speed is
   not credited, and its rank rests on weight and fuel alone.

7. **The engine is the largest single unknown.** Aeromomentum publishes no
   continuous rating, no critical altitude and no fuel consumption for the AM20T
   (re-read 2026-10-24). Between our two critical-altitude cases the speed moves
   9-15 kt. If the real continuous rating is lower than 195 hp, every speed here
   falls; at the cube-root rule, 10% less power costs about 3.5% of cruise speed.
   See [The Aeromomentum assumption](#the-aeromomentum-assumption).

## Why this order

The ranking weighs, in this order: whether the design can be revived at all
(rights and surviving data), what it does on the Aeromomentum line by our own
numbers, its safety record and whether that record is tied to the
configuration, and whether a revival fixes what killed it. Performance alone
would put the Mooney 301, the IV-P and the VK-30 on top. The other three
factors pull them apart.

- **Rutan Defiant, first.** It is the only design whose published power matches an
  Aeromomentum installation directly (two AM15T at 160 hp for two O-320s at 160 hp),
  at a 8 lb lighter installed mass. Two engines on the centreline give redundancy
  without an asymmetric-thrust problem, which matters when both engines are
  uncertified automotive conversions. It clears all three floors on our numbers.
  Its weakness is payload with a reserve: cannot in the low case at 178 KTAS,
  669 lb in the high case, 807-821 lb at economy power (150-159 KTAS). Its record
  has no engine-out accident. What killed it (certification money, then
  liability) does not apply to an experimental revival. The rights are an open
  question, but no 1985 buyer is on the record, so the likely holder is one
  living, identifiable party: RAF or Burt Rutan. He holds little beyond the plans
  copyright, and he refused new licences in the 1980s and still objects to
  unlicensed building.
- **Lancair IV-P, second.** It has the strongest airframe that physically
  survives: about 235 on the register to measure, and parts support still
  offered. Who could license or sell the design is open. The scope of the 2023
  JetEXE purchase is not public, the molds have no known location since 2017,
  and low-grade reports describe a dispute between the parties. That is a
  chain-of-title problem, not a closed door, and it still leaves the IV-P ahead
  of the 301 (nothing survives) and the VK-30 (a large, settled holder). Our check gives 200-211 KTAS on 195 hp, and 824 lb
  over 1,000 nm with reserve in the high case. Two things hold it below the
  Defiant. Its fatal-accident record is the worst in the survey, and the stall-spin
  half of it comes from a 36 lb/ft2 wing loading that a smaller engine does not
  change. And putting a 195 hp continuous engine in a 350 hp airframe removes
  the climb margin its pilots rely on, and needs ballast to replace about 240 lb
  of nose weight.
- **Mooney 301, third.** It has the best payload-range on our numbers and is the only
  six-seater that comes close to the mission. But one prototype was built, the
  airframe was scrapped, and the data went to France. A revival is a
  re-derivation from published geometry, with an unvalidated tail. The rights
  question has to go to an attorney before anything else.
- **Cirrus VK-30, fourth.** It has the best speed on our numbers. Its holder is a
  large, state-controlled company for which the VK-30 is history, and three of
  its five fatal accidents trace to the pusher shaft drive, a flutter-prone
  cruise flap and spin recovery. An Aeromomentum engine is geared and liquid-cooled,
  but it would still need the long shaft.
- **Velocity XL-RG, Express, Berkut, P210N.** The Velocity is a live kit. It
  passes only on its optional tanks and is a partnership question, not a revival.
  The Express is the most orphaned and best-measured design, but it misses
  useful load on the weighed aircraft and has a tail the NTSB has named. The
  Berkut is the only two-seater, and it cannot be checked. The P210N calibrates
  the method and is held by Textron.

## Not shortlisted, and why

From the 22 stage 1 passes and near misses:

| Design | Reason |
|---|---|
| Piper PA-46-310P, Mooney Acclaim Type S, Cessna TTx, Socata TB-21 | Live type families held firmly by large OEMs (stage 2). The realistic path is modifying existing airframes, not reviving a design |
| Epic LT | Turbine; no Aeromomentum equivalent |
| Bellanca Skyrocket II | 435 hp, no fuel capacity found, so no range check is possible. Kept on the list as a configuration reference (FAI records, NASA CD0 0.016) |
| Piper Comanche 400, Mooney M22 | 400 and 310 hp: far from 195 hp continuous. The M22 is also pressurised and heavy; its rights are an open question (stage 2) |
| Lancair Super ES | The same holder as the IV-P, without a measured point to calibrate against; the IV-P covers the family |
| Wing Derringer, Windecker Eagle, Meyers 200D | Near misses kept on the long list. Their geometry is thinner than the shortlist's. The Derringer (an abandoned TC whose data the FAA offered to release) and the Windecker (a small foreign-owned TC holder) are the best rights stories in the survey, and both deserve a second look if Bill wants a certified basis |
| Extra EA-400 | A near miss on range; the published numbers do not add up (stage 1), and the rights records disagree (stage 2) |
| Evektor SuperCobra, Grob GF 200 | No fuel flow or no empty weight, so they cannot be screened on the same basis |
| Rohr 2-175 | 1,450 lb gross; it cannot approach the useful-load target. Configuration reference only (stage 2: nothing survives to own) |

## The Aeromomentum assumption

Aeromomentum publishes, for the AM20T: 260 hp at 5,800 rpm, 300 hp for 5 min,
285 lb dry, liquid-cooled, $27,995 (grade F,
https://aeromomentum.com/am20t-230hp-300hp/, re-read 2026-10-24). It does not
publish a continuous rating, a critical altitude or a fuel consumption. Every
number in this document that uses the AM20T or AM15T rests on these
assumptions, which are **ours**:

| Item | Assumed | Basis |
|---|---|---|
| Continuous power | 75% of the take-off rating: 195 hp (AM20T), 120 hp (AM15T) | The usual GA cruise rating convention. Not published |
| Critical altitude | Two cases: 8,000 ft (AM-low) and 16,000 ft (AM-high); Gagg-Ferrar lapse above | Brackets a single-turbo automotive installation. Not published |
| BSFC | 0.45 lb/hp/h | The same estimate as stage 1 (Gudmundsson ch. 7). Not published |
| Installed mass | dry x 1.25 (Aeromomentum's own installation note) + 35 lb for radiator, coolant and plumbing | The 35 lb is ours |
| Cooling drag | Raymer's piston formula, the same as air-cooled | A liquid-cooled radiator can do better (Meredith effect) or worse; not credited either way |

This is an **open risk**, and it can only be closed by data from Aeromomentum or by
a test. Asking Aeromomentum is contact with a manufacturer, which needs Bill's
go-ahead. That question is raised on the issue, not assumed.

## Results on the Aeromomentum line

Our numbers, from `docs/shortlist/check/results/`. The bracketed values are the optimistic
bound: the other drag factor (own published points, or the fleet's 1.16 for the
Berkut) and full credit for a lighter engine.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| Rutan Defiant [AM-low] | 2x AM15T | 8k | 178 (197) | 1,350 (1,358) | 1,094 | 721 | cannot (709) | 150: 858 / 807 |
| Rutan Defiant [AM-high] | 2x AM15T | 16k | 190 (212) | 1,350 (1,358) | 1,156 | 747 | 669 (732) | 159: 871 / 821 |
| Lancair IV-P [AM-low] | AM20T | 8k | 200 (218) | 1,350 (1,592) | 1,136 | 881 | cannot (1,094) | 161: 962 / 920 |
| Lancair IV-P [AM-high] | AM20T | 16k | 211 (231) | 1,350 (1,592) | 1,155 | 888 | 824 (1,100) | 164: 953 / 911 |
| Mooney 301 [AM-low] | AM20T | 8k | 176 (193) | 1,452 (1,659) | 1,143 | 922 | 858 (1,107) | 142: 1,015 / 973 |
| Mooney 301 [AM-high] | AM20T | 16k | 187 (205) | 1,452 (1,659) | 1,169 | 931 | 867 (1,114) | 146: 1,006 / 964 |
| Cirrus VK-30 [AM-low] | AM20T | 8k | 199 (208) | 1,350 (1,471) | 1,225 | 880 | 815 (954) | 165: 973 / 931 |
| Cirrus VK-30 [AM-high] | AM20T | 16k | 212 (221) | 1,350 (1,471) | 1,257 | 890 | 825 (963) | 174: 973 / 930 |
| Velocity XL-RG, 100 gal [AM-low] | AM20T | 8k | 186 (203) | 1,000 (1,104) | 1,213 | 505 | 440 (583) | 157: 613 / 571 |
| Velocity XL-RG, 100 gal [AM-high] | AM20T | 16k | 199 (217) | 1,000 (1,104) | 1,275 | 522 | 457 (597) | 167: 620 / 578 |
| Velocity XL-RG, 70 gal [AM-low] | AM20T | 8k | 186 (203) | 1,000 (1,104) | 825 | cannot | cannot | 157: 613 / cannot |
| Velocity XL-RG, 70 gal [AM-high] | AM20T | 16k | 199 (217) | 1,000 (1,104) | 860 | cannot | cannot | 167: 620 / cannot |
| Wheeler Express [AM-low] | AM20T | 8k | 179 (186) | 890 (890) | 1,062 | 376 | cannot | 149: 481 / 439 |
| Wheeler Express [AM-high] | AM20T | 16k | 191 (199) | 890 (890) | 1,115 | 393 | cannot (347) | 157: 487 / 445 |
| Berkut 360 [AM-low] | AM20T | 8k | not credible | 949 (949) | 873 | cannot | cannot | economy speed not credible: 650 / 608 |
| Berkut 360 [AM-high] | AM20T | 16k | not credible | 949 (949) | 906 | cannot | cannot | economy speed not credible: 658 / 616 |
| Cessna P210N [AM-low] | AM20T | 8k | 161 (162) | 1,658 (1,819) | 916 | cannot | cannot | 130: 1,183 / 1,142 |
| Cessna P210N [AM-high] | AM20T | 16k | 171 (171) | 1,658 (1,819) | 931 | cannot | cannot | 132: 1,173 / 1,132 |
| Cozy MKIV (ref) [AM-low] | AM20T | 8k | 202 (206) | 808 (808) | 645 | cannot | cannot | 172: cannot / cannot |
| Cozy MKIV (ref) [AM-high] | AM20T | 16k | 217 (221) | 808 (808) | 668 | cannot | cannot | 184: cannot / cannot |

The useful loads rest on factory empty weights for the Defiant (plans prototype),
IV-P, VK-30, Mooney 301 and Velocity. No builder-fleet average exists for any of
them, and stage 1 found fleets running 38-245 lb heavier than the factory
wherever both were published. Read every useful load here as an upper bound
until MANUFACTURING's stage 4 rebuild estimate replaces it.

## Our numbers against the published ones, on the original engines

| Design | Published claim | Our number at the same power and altitude | Gap | Verdict |
|---|---|---|---|---|
| Rutan Defiant | 175-184 KTAS at 75%, ~8,000 ft (P/F) | matched with a 1.72 factor | draggy | Published speeds trusted; the airframe is draggier than its geometry |
| Lancair IV-P | 278 KTAS at FL230, 262 hp (P) | 255 KTAS at the fleet calibration | -8% | Published figure optimistic, or this airplane is the cleanest measured. Unproven |
| Mooney 301 | 237.5 KTAS at 17,500 ft, 270 hp (P) | 217 KTAS | -9% | Same as the IV-P |
| Cirrus VK-30 | 205 KTAS at 4,500 ft, ~203 hp (P) | 196 KTAS | -4% | Close: within the calibration spread |
| Velocity XL-RG | 190 KTAS at 3,000 ft, 232 hp (P) | matched with a 1.63 factor | draggy | Low confidence: one point, scaled geometry |
| Wheeler Express | 169 KTAS at 6,190 ft DA, ~169 hp (P, CAFE) | 164 KTAS | -3% | Agrees: this is a calibration case |
| Cessna P210N | 152-193 KTAS at 10,000-23,000 ft (POH) | matched with 1.26-1.32 across seven points | - | Calibration case; the spread is tight |
| Cozy MKIV | 169-182 KTAS at 850-12,000 ft DA (R, CAFE) | matched with 1.32-1.39 across four points | - | Calibration case |

Do the published power and fuel flow agree with each other? For every
published point with both, the implied BSFC (gph x 6 / hp) is 0.39-0.51 lb/hp/h:
0.39-0.42 for the leaned or lean-of-peak points (Express, IV-P, Mooney 301,
Velocity) and 0.43-0.51 for best-power and handbook points (Cozy, Defiant,
VK-30, P210N). That is the normal range for these engines, so no published
speed here hides an impossible power. Once a type's drag factor matches its
published speed, our fuel flow at that speed checks only our BSFC (0.45, or the
POH-derived 0.50 for the P210N and 0.42 for the lean-of-peak IV-P and 301), so
it is not counted as independent evidence.

## Method

One pipeline for every type, in `docs/shortlist/check/`:

1. **Geometry.** A parametric OpenVSP model per type (`vspgen.py`): wing,
   canard or tail, fins or winglets, strakes, and a fuselage on a generic
   station profile scaled to the published length, width and height. Every
   dimension is sourced and graded in `geometry/<id>.json`; what we had to
   estimate (tail areas by volume coefficient, fuselage cross-sections, chords
   that close a published area) is listed in each model's `assumptions`. OpenVSP
   CompGeom gives the wetted area of each component, with buried area removed.
   Fidelity: about +/-3% on the lifting surfaces and +/-10% on the fuselage. This
   is not a lofted reproduction.
2. **Parasite drag.** A component build-up (Raymer, *Aircraft Design* ch. 12;
   Hoerner, *Fluid-Dynamic Drag* ch. 6 and 8 for form and interference): mixed
   laminar-turbulent skin friction with a stated laminar run per component, form
   factors by component type, interference factors 1.00-1.05, a fixed-gear
   allowance where the gear is fixed, cooling drag by Raymer's piston formula
   (eq. 12.39) with an installation factor, and 5% for leakage and protuberances.
3. **Calibration.** We match the build-up to every published point that states
   altitude and power by scaling parasite drag by a factor k. The factor absorbs
   power-estimate, propeller and drag errors together; it is not a pure drag
   number. The fleet calibration is the median of the three instrumented or
   handbook cases (1.29; range 1.16-1.36). Each type uses the larger of its own
   factor and the fleet's, so no type is flattered by its own brochure.
4. **Induced drag.** Oswald efficiency (Raymer eq. 12.48). For canards the
   lift is split between the surfaces (18-20% on the canard) and each surface
   takes its own CL^2/(pi A e). Canard-wing interference is not modelled.
   Induced drag is 5-18% of the total at the reference cruise point for
   these types, so a 20% error in it moves speed by about 1% at most.
5. **Propeller.** McCormick's actuator-disk ideal efficiency at the cruise thrust
   and disk area, times 0.85 for profile and swirl losses, times a stated
   installation factor (0.95-0.97 for fixed-pitch or wake-immersed props). The
   cruise efficiencies come out at 0.79-0.84.
6. **Power.** Normally aspirated engines lapse by Gagg-Ferrar. Turbocharged
   engines are flat-rated to a critical altitude, then lapse by Gagg-Ferrar.
   Where a flight test gives manifold pressure and rpm but not power (the CAFE
   reports), we estimate power at full throttle only, grade E.
7. **Range and payload.** A constant-altitude, constant-speed cruise integrated
   in 5-10 lb fuel steps. This is the exact form of the Breguet range relation
   for that schedule, with the power required recomputed as weight falls. Each
   flight also carries a taxi and climb allowance (10 lb plus twice the ideal
   potential-energy fuel), and no descent credit. Payload at 1,000 nm is solved
   from MTOW, with and without a 45 min reserve at the end-of-cruise power.

**What this method cannot see.** It does not resolve laminar-flow loss from
bugs or rain, real cooling-system design, trim drag beyond the canard lift
split, or propeller-airframe interaction for pushers. Dynamic stability, spin
behaviour and flutter are outside it entirely. Where the safety record raises
those, it is reported from the record and labelled as such; nothing here
clears or condemns a design on handling.

## Hand-offs

- **To Bill:** the card on AER-3783 asks which designs, if any, go to development.
- **To MANUFACTURING (AER-3784, stage 4):** this shortlist, with each dossier's
  construction, geometry sources (`docs/shortlist/check/geometry/`), the
  empty-weight basis, and the engine-swap mass deltas. The useful load of every
  design here moves pound for pound with the empty weight a modern rebuild
  achieves, so stage 4's weight estimate is the number that most changes this
  ranking.
- **To Elon (stage 2):** the ranking. Its rights questions are what most decide
  whether a design can go anywhere. Elon's updated files (PR #3, 2026-10-24)
  answered the first round: no 1985 buyer of the Rutan designs, an open chain of
  title for the IV-P, and an unresolved Mooney/Daher question on the 301. All
  three now need an attorney, not more desk research.
- **SAFETY is not part of this stage.** Two patterns would need SAFETY before any
  development decision: the IV-P's low-altitude stall-spin record, and the
  VK-30's shaft-drive and flutter accidents. Per the epic, that is asked on
  AER-3785 first.

## Reproduce

```sh
# from a host where `maos` is available (OpenVSP runs in the maos-aero-tools container)
cp -r docs/shortlist/check /maos-work/aero/analysis/AER-3783
cd /maos-work/aero/analysis/AER-3783
for m in models/*.json; do python3 run_check.py "$m"; done   # writes vsp/ and results/
python3 report.py                                            # writes results/tables.md, results/<id>_stage3.md
```

`vspgen.py` expects the folder at `/maos-work/aero/analysis/AER-3783`, which the
container sees as `/workspace/analysis/AER-3783`; change `CONTAINER` in that file
to run it elsewhere.
