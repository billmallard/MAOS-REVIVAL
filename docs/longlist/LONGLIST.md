# Stage 1 long list: 37 candidates and the reference, screened against the targets

**Status:** stage 1 of the legacy survey (AER-3786), compiled 2026-10-24 by AERO.
**Unranked.** Row order is by origin, then by when the data arrived. It is not a
preference. Ranking is stage 3 and happens only after this list is posted.

Everything here is a **published** number, graded and sourced, and screened by
arithmetic we can show. None of it is our own performance check yet; that
comes in stage 3, for the shortlist only. A pass here means "the published
record, read on one consistent basis, meets the targets", not "it performs".

## How to read the table

- **Grades.** F factory, brochure or designer claim. T type certificate data
  sheet. P flight test, POH, or magazine pilot report. B builder-fleet,
  registry, or owner data. R measured record (FAI). E estimate, with whose
  stated. The per-candidate stubs in `docs/candidates/` carry the grade and
  source URL of every number; the table only summarises.
- **Origin.** a = experimental kit or plans; b = certified, out of
  production; c = prototype that never reached production; d = foreign.
- **Two screens, never mixed** (brief, amended 2026-10-24). Each row is
  screened once **as published** (the maker's own figures: brochure, type
  certificate data sheet, handbook) and once on **measured or reported** data
  (an independent flight test, a weighed aircraft, an owner's report, a fleet
  figure). Compare rows published-to-published and measured-to-measured. Grade
  P is split by what it is: a handbook or spec-box figure is published, a timed
  flight test is measured. A setting can also say so explicitly.
- **The three targets are separate floors.** Useful load, range and cruise
  speed are each screened on their own. Payload carried 1,000 nm is shown for
  information only; it is not one of the targets.
- **Useful load.** As published: the factory figure. Measured: a fleet or
  weighed-aircraft figure, or, for a one-off prototype known to have flown
  heavier than its design weight, our as-flown estimate (grade E).
- **Range.** As published: the published range, with whatever reserve basis it
  was published on (the stub says which). Where none is published, it is
  derived from published fuel and a published flow, and says so. Measured: the
  still-air, no-reserve range from usable fuel and a measured fuel flow.
- **Cruise** is the highest speed on that basis that states an altitude of at
  least 6,000 ft; failing that, the highest one, marked `*` and "speed
  unconditioned". `(design)` marks a design or marketing target with no flight
  test behind it.
- **Measured data is usually partial** on a long list. "partial" names what was
  measured and how it screened; "no measured data" means none was found.
- **Payload at 1,000 nm** (information only) is useful load minus the fuel to
  fly 1,000 nm at the setting that leaves the most payload, with no reserve and
  with 45 min at the same flow, on each basis separately. "cannot" means the
  usable fuel does not hold it.

## Method

| Step | Rule | Why |
|---|---|---|
| Targets | Useful load >= 1,000 lb; range >= 1,000 nm; cruise > 160 KTAS (> 180 preferred) at altitude | `docs/BRIEF.md` |
| Near miss | Useful load >= 900 lb; range >= 900 nm; cruise >= 150 KTAS. The miss is stated in the verdict | Brief: a near miss stays on the list, with the miss stated |
| Like for like | Published and measured figures are screened in separate columns and never combined in one verdict | Brief, amended 2026-10-24 |
| Leg fuel (information only) | gal = (1,000 nm / KTAS + reserve h) x gph; 6.0 lb/gal avgas, 6.7 lb/gal Jet-A | Breguet in its constant-speed, constant-flow form; adequate for a screen |
| Allowances | None for taxi, climb, descent or wind | Keeps rows comparable. It flatters every row by roughly 3-5 gal on a 1,000 nm leg, about 20-30 lb of payload |
| Estimated flow | Only where a type publishes no fuel flow at any setting: gph = 0.45 lb/hp/h x rated hp x stated power / 6.0, graded E and marked "est. flow" | 0.45 is mid-range for air-cooled GA pistons (Gudmundsson, *General Aviation Aircraft Design*, ch. 7). It never displaces a published flow |
| Cross-check | A published range more than 15% from the one computed from fuel and flow is flagged, not substituted | Brief: "does the fuel support the claimed range at the claimed flow?" |
| Engine fit | Smallest Aeromomentum model whose published power covers the airframe's rated (continuous where published) power. Above 260 hp, the AM20T is assumed and cruise speed is scaled by the cube root of the power ratio | Parasite-drag-dominated cruise at equal propulsive efficiency. A first cut only: it ignores installed mass, cooling drag and altitude rating |

The screen is `screen.py`, the data `candidates.json`, the stubs
`make_stubs.py`. To regenerate everything below:

```sh
cd docs/longlist
python3 screen.py --write   # rewrites the table and flags in this file
python3 make_stubs.py       # writes stubs that do not exist yet (--force to overwrite)
```

## The baseline engine: Aeromomentum's published line

Read from aeromomentum.com on 2026-10-24 (grade F). All are liquid-cooled,
geared, fuel-injected automotive-derived four-cylinders with FADEC.

| Model | Power | Dry weight | Notes | Source |
|---|---|---|---|---|
| AM13 | 100 hp | not stated | 1.3 L | https://aeromomentum.com |
| AM15 | 120 hp at 5,800 rpm | 185 lb | 1,497 cc; weight includes gearbox, starter, alternator, ECU; TBO 2,000 h; $13,000-14,100 | https://aeromomentum.com/am15-117hp-to-147hp/ |
| AM13T | 140 hp at 5,800 rpm | 200 lb | 1,397 cc turbo; TBO 1,500 h; $16,100-17,200 | https://aeromomentum.com/am20-170hp/ |
| AM15T | 160 hp at 5,800 rpm | 215 lb | 1,497 cc turbo; gearbox rated to 225 hp; TBO 1,500 h | https://aeromomentum.com/am15t-160hp/ |
| AM20T | 260 hp at 5,800 rpm; 300 hp for 5 min at 6,200 rpm | 285 lb | 1,998 cc turbo; TBO 1,800 h; $27,995 ($29,700 for the 300 hp version) | https://aeromomentum.com/am20t-230hp-300hp/ |

What the published line does **not** say, and every "at altitude" credit for
an Aeromomentum installation depends on: no **maximum continuous rating** for
any turbo model, and no **critical altitude**. A candidate that cruises at
FL200-FL250 on its original turbo engine gets that credit only on its
original engine. Aeromomentum notes that installation typically adds about
25% to the base weight (AM13T page); radiator mass and cooling drag are not
yet in any number here.

## Coverage

38 rows: the Cozy MKIV reference and 37 candidates.

| Seats | Experimental kit / plans (a) | Certified, out of production (b) | Prototype (c) | Foreign (d) |
|---|---|---|---|---|
| 2 | Long-EZ, Berkut 360, Questair Venture, Lancair Legacy, Glasair III, SX-300 | Wing Derringer | Rohr 2-175 | |
| 3 | | | | SF.260 |
| 4 | Cozy MKIV (ref), Velocity XL-RG, Rutan Defiant, Prescott Pusher, Lancair IV-P, Express, RV-10, Lancair Super ES, Alpi Pioneer 400 (also d) | Acclaim Type S, TTx, Meyers 200D, Super Viking, Windecker Eagle, Comanche 400 | Panthera, SuperCobra (both also d) | TB-21, Robin HR100/285, Ruschmeyer R90 |
| 5 | Cirrus VK-30 | Mooney M22 | Grob GF 200 (also d) | |
| 6 | Epic LT (turbine) | Cessna P210N, Piper PA-46-310P | Bellanca Skyrocket II, Mooney 301 | Extra EA-400 |

The six-seat class is thin in pistons that were ever sold as kits; that is a
real gap in the market, not only in this list.

## The screen

<!-- screen-table:start -->
| # | Candidate | Seats | Origin | As published: UL lb; range nm; KTAS @ alt | Screen, as published | Measured or reported: UL lb; range nm; KTAS @ alt | Screen, measured | Payload @ 1,000 nm, lb (no res / 45 min), information only | Aeromomentum fit | Why it died |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | [Cozy MKIV (reference)](../candidates/cozy-mkiv.md) | 4 | a | 1,000 pass; 1,129 pass; 191 @ 8,000 ft pass+ | pass | 871 fail; 1,049 pass; 177 @ 8,021 ft pass | fail (UL -129 lb) | pub: cannot (951 nm max); meas: 581 / cannot @ 170 kt, 8.2 gph | Yes: AM20T (260 hp) for 180 hp | Alive: plans and parts from Aircraft Spruce |
| 1 | [Rutan Long-EZ](../candidates/rutan-long-ez.md) | 2 | a | 615 fail; 1,243 pass; 159 @ 8,000 ft near | fail (UL -385 lb, speed -1 kt) | 475 fail; - ?; - | partial: UL fail (UL -525 lb) | pub: 449 / 434 @ 125 kt, 3.4 gph (est. flow) | Yes: AM15 (120 hp) for 115 hp | Plans withdrawn 1985 over liability exposure |
| 2 | [Berkut 360](../candidates/berkut-360.md) | 2 | a | 965 near; 1,315 pass; 208 @ 8,000 ft pass+ | near miss (UL -35 lb) | - ?; - ?; 180 @ alt n/s * pass+ | partial: speed pass, speed unconditioned | pub: 718 / 683 @ 187 kt, 7.7 gph | Yes: AM20T (260 hp) for 205 hp | Founder-partner lawsuits bankrupted the company; kit withdrawn 2002 |
| 3 | [Velocity XL-RG](../candidates/velocity-xl-rg.md) | 4 | a | 1,100 pass; 1,150 pass; 205 @ alt n/s * pass+ | pass, speed unconditioned | - ?; 887 fail; 190 @ 3,000 ft * pass+ | partial: range fail, speed pass, speed unconditioned (range -113 nm) | pub: 712 / cannot @ 170 kt, 11.0 gph | Yes for the IO-540 260 hp build (AM20T 260 hp); short for IO-550 310 hp builds (-6% speed est.) | Alive: Velocity Inc. still sells kits |
| 4 | [Rutan Defiant](../candidates/rutan-defiant.md) | 4 | a | 1,290 pass; 1,128 pass; 184 @ 8,000 ft pass+ | pass | - ?; 1,094 pass; 162 @ 10,000 ft pass | partial: range pass, speed pass | pub: 710 / cannot @ 184 kt, 17.8 gph | Yes: 2x AM15T (160 hp) matches the prototype's 2x 160 hp; 180 hp builds need 2x AM20T (heavier) | Certification funding lost 1979; plans withdrawn 1985 (liability) |
| 5 | [Cirrus VK-30](../candidates/cirrus-vk-30.md) | 5 | a | 1,350 pass; 1,130 pass; 211 @ 5,000 ft * pass+ | pass, speed unconditioned | - ?; 1,256 pass; 205 @ 4,500 ft * pass+ | partial: range pass, speed pass, speed unconditioned | pub: 875 / 800 @ 211 kt, 16.7 gph | Short: AM20T 260 hp vs 290 hp (-4% speed, est. 198 KTAS) | Cirrus dropped it in 1993 to build the certified SR20 |
| 6 | [Prescott Pusher](../candidates/prescott-pusher.md) | 4 | a | 850 fail; 869 fail; 165 @ 7,500 ft pass | fail (UL -150 lb, range -131 nm) | - ?; - ?; 151 @ alt n/s * near | partial: speed near, speed unconditioned (speed -9 kt) | pub: cannot (866 nm max) | Yes: AM20T (260 hp) for 180 hp | Slow parts supply and weak sales; company folded 1991 |
| 7 | [Questair Venture](../candidates/questair-venture.md) | 2 | a | 760 fail; 1,000 pass; - | incomplete: no speed, fails on the rest (UL -240 lb) | - ?; - ?; 235 @ alt n/s * pass+ | partial: speed pass, speed unconditioned | pub: cannot (836 nm max) | Short: AM20T 260 hp vs 280 hp (-2% speed, est. 229 KTAS) | Bankruptcy around 1991; parts and support only today |
| 8 | [Lancair IV-P](../candidates/lancair-iv-p.md) | 4 | a | 1,350 pass; 1,347 pass; 278 @ 23,000 ft pass+ | pass | - ?; 1,779 pass; 284 @ 24,000 ft pass+ | partial: range pass, speed pass | pub: 962 / 881 @ 278 kt, 18.0 gph | Short: AM20T 260 hp vs 350 hp (-9% speed, est. 231 KTAS) | Kit production ended 2012; maker now parts and support only |
| 9 | [Lancair Legacy](../candidates/lancair-legacy.md) | 2 | a | 700 fail; 999 near; - | incomplete: no speed, fails on the rest (UL -300 lb, range -1 nm) | - ?; 1,278 pass; 228 @ 11,500 ft pass+ | partial: range pass, speed pass | no fuel flow published | Short: AM20T 260 hp vs 310 hp (-6% speed, est. 217 KTAS) | Last kit 2016; more investment needed to continue |
| 10 | [Glasair III](../candidates/glasair-iii.md) | 2 | a | 775 fail; 1,060 pass; 224 @ 8,000 ft pass+ | fail (UL -225 lb) | - | no measured data | pub: 369 / cannot @ 216 kt, 14.6 gph (est. flow) | Short: AM20T 260 hp vs 300 hp (-5% speed, est. 214 KTAS) | Stoddard-Hamilton bankrupt 2001; revived as a carbon kit (AAC) |
| 11 | [Express (Wheeler / Series 90 / 2000 FT)](../candidates/express-2000.md) | 4 | a | 1,045 pass; 1,401 pass; - | incomplete: no speed | 901 near; 1,745 pass; 169 @ 6,190 ft pass | near miss (UL -99 lb) | meas: 585 / 559 @ 110 kt, 5.8 gph | Yes: AM20T (260 hp) for 210 hp | 1990 fatal crash collapsed sales; successive owners failed |
| 12 | [Swearingen SX-300](../candidates/swearingen-sx-300.md) | 2 | a | 800 fail; 650 fail; - | incomplete: no speed, fails on the rest (UL -200 lb, range -350 nm) | - ?; 988 near; 240 @ alt n/s * pass+ | partial: range near, speed pass, speed unconditioned (range -12 nm) | no fuel flow published | Short: AM20T 260 hp vs 300 hp (-5% speed, est. 229 KTAS) | Kits ended 1989; lost military interest after a prototype crash |
| 13 | [Van's RV-10](../candidates/vans-rv-10.md) | 4 | a | 1,125 pass; 869 fail; 171 @ 8,000 ft pass | fail (range -131 nm) | 1,050 pass; 835 fail; 167 @ alt n/s * pass | fail (range -165 nm) | meas: cannot (835 nm max) | Yes: AM20T (260 hp) for 260 hp | Alive: in production at Van's |
| 14 | [Lancair Super ES](../candidates/lancair-super-es.md) | 4 | a | 1,300 pass; 1,217 pass; 200 @ 10,500 ft pass+ | pass | - | no measured data | pub: 777 / cannot @ 200 kt, 17.4 gph (est. flow) | Short: AM20T 260 hp vs 310 hp (-6% speed, est. 185 KTAS) | Kit production ended 2012 |
| 15 | [Epic LT](../candidates/epic-lt.md) | 6 | a | 3,100 pass; 1,874 pass; - | incomplete: no speed | - ?; 1,767 pass; 317 @ 27,000 ft pass+ | partial: range pass, speed pass | no fuel flow published | No: turbine; no Aeromomentum equivalent | Epic bankrupt 2009; LT kits dropped 2013 for the certified E1000 |
| 16 | [Alpi Pioneer 400](../candidates/alpi-pioneer-400.md) | 4 | a, d | 772 fail; 455 fail; - | incomplete: no speed, fails on the rest (UL -228 lb, range -545 nm) | - ?; 411 fail; 135 @ alt n/s * fail | partial: range fail, speed fail, speed unconditioned (range -589 nm, speed -25 kt) | no fuel flow published | Yes: AM13T (140 hp) for 115 hp | Alive: kit/permit only, no type certificate |
| 17 | [Cessna P210N Pressurized Centurion](../candidates/cessna-p210n.md) | 6 | b | 1,574 pass; 925 near; 196 @ 20,000 ft pass+ | near miss (range -75 nm) | 1,480 pass; - ?; 199 @ 20,000 ft pass+ | partial: UL pass, speed pass | pub: 1,066 / cannot @ 183 kt, 15.5 gph | Short: AM20T 260 hp vs 285 hp (-3% speed, est. 193 KTAS) | Cessna ended all piston production in 1986 (liability era) |
| 18 | [Piper PA-46-310P Malibu](../candidates/piper-pa46-310p.md) | 6 | b | 1,455 pass; 1,300 pass; - | incomplete: no speed | 1,400 pass; 1,800 pass; 210 @ 25,000 ft pass+ | pass | meas: 1,000 / 946 @ 180 kt, 12.0 gph | Short: AM20T 260 hp vs 310 hp (-6% speed, est. 193 KTAS) | Continental engine troubles; replaced by the Lycoming Mirage (1989) |
| 19 | [Mooney M20TN Acclaim Type S](../candidates/mooney-m20tn-acclaim.md) | 4 | b | 1,004 pass; 1,445 pass; 237 @ 25,000 ft pass+ | pass | - ?; 1,369 pass; 200 @ 25,000 ft pass+ | partial: range pass, speed pass | pub: cannot (959 nm max) | Short: AM20T 260 hp vs 280 hp (-2% speed, est. 231 KTAS) | Mooney halted production in Nov 2019 |
| 20 | [Cessna TTx / Columbia 400](../candidates/cessna-ttx.md) | 4 | b | 1,065 pass; 1,270 pass; 219 @ 22,000 ft pass+ | pass | 1,027 pass; 1,185 pass; 180 @ 12,000 ft pass+ | pass | pub: 627 / 555 @ 219 kt, 16.0 gph; meas: 510 / 441 @ 180 kt, 15.5 gph | Short: AM20T 260 hp vs 310 hp (-6% speed, est. 207 KTAS) | Textron ended it in 2018 on slow sales against Cirrus |
| 21 | [Meyers 200D / Aero Commander 200D](../candidates/meyers-200d.md) | 4 | b | 1,060 pass; 782 fail; 182 @ alt n/s * pass+ | fail (range -218 nm) | 900 near; 1,153 pass; 187 @ alt n/s * pass+ | near miss, speed unconditioned (UL -100 lb) | meas: 515 / 461 @ 187 kt, 12.0 gph | Short: AM20T 260 hp vs 285 hp (-3% speed, est. 177 KTAS) | Hand-built at a loss: $4M to make $3M of airplanes |
| 22 | [Bellanca 17-30A Super Viking](../candidates/bellanca-super-viking.md) | 4 | b | 1,108 pass; 802 fail; 163 @ alt n/s * pass | fail (range -198 nm) | 1,000 pass; - ?; 165 @ 7,500 ft pass | partial: UL pass, speed pass | pub: cannot (859 nm max); meas: cannot (859 nm max) | Short: AM20T 260 hp vs 285 hp (-3% speed, est. 160 KTAS) | Bellanca bankrupt 1980 and again 2001; wood wing, low-rate production |
| 23 | [Windecker AC-7 Eagle](../candidates/windecker-eagle.md) | 4 | b | 1,250 pass; 1,070 pass; 177 @ alt n/s * pass | pass, speed unconditioned | - | no measured data | pub: cannot (950 nm max) | Short: AM20T 260 hp vs 285 hp (-3% speed, est. 172 KTAS) | Ran out of money after a $20M+ certification; 1979 revival failed on price |
| 24 | [Wing D-1 Derringer](../candidates/wing-derringer.md) | 2 | b | 980 near; 1,007 pass; 184 @ 13,000 ft pass+ | near miss (UL -20 lb) | - | no measured data | pub: 471 / cannot @ 184 kt, 15.6 gph (est. flow) | Yes: 2x AM15T (160 hp) for 160 hp | Hi-Shear internal problems, then Wing Aircraft bankrupt 1982 |
| 25 | [Mooney M22 Mustang](../candidates/mooney-m22.md) | 5 | b | 1,240 pass; 1,297 pass; 186 @ alt n/s * pass+ | pass, speed unconditioned | - | no measured data | pub: 753 / cannot @ 186 kt, 15.1 gph (est. flow) | Short: AM20T 260 hp vs 310 hp (-6% speed, est. 175 KTAS) | Sold at a loss; helped bankrupt Mooney in 1969 |
| 26 | [Piper PA-24-400 Comanche 400](../candidates/piper-comanche-400.md) | 4 | b | 1,490 pass; 860 fail; 185 @ alt n/s * pass+ | fail (range -140 nm) | 1,331 pass; - ?; - | partial: UL pass | pub: 929 / 857 @ 171 kt, 16.0 gph | Short: AM20T 260 hp vs 400 hp (-13% speed, est. 160 KTAS) | Heavy and thirsty; the 1972 flood destroyed the Comanche tooling |
| 27 | [Rohr 2-175 (71X)](../candidates/rohr-2-175.md) | 2 | c | - | fail (1,450 lb gross weight) | - | no measured data | no fuel flow published | Yes: AM15T (160 hp) for 150 hp | Cut in Rohr's 1975 retrenchment; airframes and drawings destroyed |
| 28 | [Bellanca 19-25 Skyrocket II](../candidates/bellanca-skyrocket-ii.md) | 6 | c | 1,800 pass; 1,273 pass; 222 @ 15,000 ft pass+ | pass | - | no measured data | no fuel flow published | Short: AM20T 260 hp vs 435 hp (-16% speed, est. 187 KTAS) | Money ran out amid founder-investor disputes before certification |
| 29 | [Mooney 301](../candidates/mooney-301.md) | 6 | c | 1,452 pass; 986 near; 235 @ 25,000 ft (design) pass+ | near miss (range -14 nm) | 1,252 pass; - ?; - | partial: UL pass | pub: 949 / 860 @ 235 kt, 19.7 gph | Short: AM20T 260 hp vs 360 hp (-10% speed, est. 211 KTAS) | LTV takeover forced Mooney's sale; new owners wanted 300 kt; became the TBM 700 |
| 30 | [Pipistrel Panthera](../candidates/pipistrel-panthera.md) | 4 | c, d | 1,023 pass; 1,460 pass; 194 @ 8,000 ft pass+ | pass | - | no measured data | pub: cannot (728 nm max) | Yes: AM20T (260 hp) for 260 hp | Certification slipped for a decade; Textron bought Pipistrel in 2022 |
| 31 | [Grob GF 200](../candidates/grob-gf-200.md) | 5 | c, d | - ?; 1,431 pass; 240 @ alt n/s * pass+ | incomplete: no UL | - | no measured data | no fuel flow published | Short: AM20T 260 hp vs 270 hp (-1% speed, est. 237 KTAS) | Grob found no partner to fund production |
| 32 | [Evektor VUT100-131i SuperCobra](../candidates/evektor-supercobra.md) | 4 | c, d | 1,213 pass; 1,000 pass; 175 @ alt n/s * pass | pass, speed unconditioned | - | no measured data | no fuel flow published | Short: AM20T 260 hp vs 315 hp (-6% speed, est. 164 KTAS) | Funding ran out in 2007 before certification |
| 33 | [Extra EA-400](../candidates/extra-ea-400.md) | 6 | d | 1,347 pass; 1,300 pass; 203 @ 18,000 ft pass+ | pass | 1,102 pass; 911 near; 205 @ 18,000 ft pass+ | near miss (range -89 nm) | meas: cannot (911 nm max) | Short: AM20T 260 hp vs 325 hp (-7% speed, est. 190 KTAS) | Too costly to build (~16,000 labour hours); holders insolvent |
| 34 | [Socata TB-21 Trinidad TC](../candidates/socata-tb21.md) | 4 | d | 1,182 pass; 1,030 pass; 187 @ 25,000 ft pass+ | pass | 980 near; 1,175 pass; 169 @ 25,000 ft pass | near miss (UL -20 lb) | pub: cannot (983 nm max); meas: 540 / 484 @ 169 kt, 12.4 gph | Yes: AM20T (260 hp) for 250 hp | Sales never recovered after 9/11; ended by 2012 |
| 35 | [Robin HR100/285 Tiara](../candidates/robin-hr100-285.md) | 4 | d | 1,234 pass; 1,266 pass; 158 @ alt n/s * near | near miss, speed unconditioned (speed -2 kt) | - | no measured data | pub: cannot (612 nm max) | Short: AM20T 260 hp vs 285 hp (-3% speed, est. 153 KTAS) | Its geared Continental Tiara engine failed in the market |
| 36 | [Ruschmeyer R90-230RG](../candidates/ruschmeyer-r90.md) | 4 | d | 997 near; 600 fail; - | incomplete: no speed, fails on the rest (UL -3 lb, range -400 nm) | 875 fail; 709 fail; 165 @ 7,000 ft pass | fail (UL -125 lb, range -291 nm) | meas: cannot (709 nm max) | Yes: AM20T (260 hp) for 230 hp | Ruschmeyer bankrupt 1996; Solaris revival never delivered |
| 37 | [SIAI-Marchetti SF.260](../candidates/siai-sf260.md) | 3 | d | 895 fail; 1,040 pass; 175 @ 6,000 ft pass | fail (UL -105 lb) | - ?; 806 fail; 165 @ 15,000 ft pass | partial: range fail, speed pass (range -194 nm) | pub: cannot (775 nm max) | Yes: AM20T (260 hp) for 260 hp | Military trainer; civil sales a sideline; ended 2017 |
<!-- screen-table:end -->

**Counts, excluding the reference row.** As published: 14 pass, 5 near miss,
9 fail, and 9 incomplete (eight have no maker's speed in our data, only flight
reports; one has no useful load). Six of the published passes and near misses
rest on a speed with no altitude, or one below 6,000 ft. Measured: 2 pass
(PA-46-310P, TTx), 4 near miss (Express, Meyers 200D, Extra EA-400, TB-21),
2 fail, 18 partial and 11 with no measured data. The first version of this list
screened one mixed column (15 pass, 7 near miss, 14 fail, 1 incomplete); the
two columns replace it.

## Sanity flags

Where the published numbers do not build up, or a number needs a caveat. These
are findings, not footnotes.

<!-- flags:start -->
- **Cozy MKIV (reference)**: fleet useful load 129 lb below factory; the only published speed/flow pair (192 kt, 10.5 gph) is a claim, and the 40%-power range has no published flow; as published (1,000 lb, 1,129 nm, 191 KTAS at 8,000 ft) it passes all three floors; the 951 nm in the first version of this list was 52 gal / 10.5 gph x 192 kt, the AOPA-quoted max-cruise claim, set against a range published at 40% power: a basis mismatch, not a units error (1,300 statute mi = 1,129 nm is right).
- **Rutan Long-EZ**: published range 1,243 nm vs 1,884 nm from fuel and flow; fleet useful load 140 lb below factory.
- **Velocity XL-RG**: screen speed has no altitude, or is below 6,000 ft; with optional tanks (100 gal) still-air range is 1,545 nm.
- **Cirrus VK-30**: screen speed has no altitude, or is below 6,000 ft.
- **Questair Venture**: published range 1,000 nm vs 836 nm from fuel and flow.
- **Lancair IV-P**: published range 1,347 nm vs 1,779 nm from fuel and flow.
- **Lancair Legacy**: published range 999 nm vs 1,278 nm from fuel and flow.
- **Express (Wheeler / Series 90 / 2000 FT)**: published range 1,401 nm vs 1,745 nm from fuel and flow; fleet useful load 144 lb below factory; CAFE measured cruise on 210 hp is the best-evidenced speed/flow data in this list; a 300 hp build would be faster but heavier.
- **Swearingen SX-300**: published range 650 nm vs 988 nm from fuel and flow.
- **Van's RV-10**: fleet useful load 75 lb below factory.
- **Epic LT**: included only to represent the 6-seat kit class; a turbine airframe is outside the Aeromomentum mission.
- **Alpi Pioneer 400**: a light-sport-scale four-seater; listed as the foreign kit benchmark, far below the targets.
- **Cessna P210N Pressurized Centurion**: fleet useful load 94 lb below factory; owners add tip tanks to reach 1,000 nm with reserve; on factory fuel it is marginal.
- **Piper PA-46-310P Malibu**: published range 1,300 nm vs 1,800 nm from fuel and flow; fleet useful load 55 lb below factory; a live type family (M350 in production), so not orphaned.
- **Mooney M20TN Acclaim Type S**: with optional tanks (128 gal) still-air range is 1,969 nm.
- **Cessna TTx / Columbia 400**: fleet useful load 38 lb below factory.
- **Meyers 200D / Aero Commander 200D**: published range 782 nm vs 1,153 nm from fuel and flow; screen speed has no altitude, or is below 6,000 ft; fleet useful load 160 lb below factory; the 187 kt / 12 gph pair comes from a weak source; at the owner's 15.5 gph the still-air range is ~730 nm.
- **Bellanca 17-30A Super Viking**: screen speed has no altitude, or is below 6,000 ft; fleet useful load 108 lb below factory; with optional tanks (84 gal) still-air range is 1,046 nm; turbo 17-31ATC reported at 190 kt at FL200 (AvWeb, fleet-grade).
- **Windecker AC-7 Eagle**: screen speed has no altitude, or is below 6,000 ft; the first FAA-certified all-composite airplane; its TC is a rare composite certification precedent.
- **Mooney M22 Mustang**: screen speed has no altitude, or is below 6,000 ft.
- **Piper PA-24-400 Comanche 400**: published range 860 nm vs 1,325 nm from fuel and flow; screen speed has no altitude, or is below 6,000 ft; fleet useful load 159 lb below factory.
- **Rohr 2-175 (71X)**: 1,450 lb gross weight: a 1,000 lb useful load is physically out of reach; a revival would be a new design inspired by it.
- **Bellanca 19-25 Skyrocket II**: FAI C-1c/C-1d speed records 1975, 246-284 kt (measured, grade R); NASA/Ohio State flight test measured CD0 = 0.016 (NTRS 19770054238); no fuel capacity found, so the range cannot be built up.
- **Mooney 301**: published range 986 nm vs 1,193 nm from fuel and flow; as-flown useful load estimate 200 lb below the published design figure; useful load and cruise are design figures; the only prototype was ~200 lb over projected weight and 'slower than desired', and no as-flown speed or weight is published (Mooney Events; docs/rights/mooney-301.md); the published 986 nm range is a 45 min reserve figure; fuel and flow give 1,016 nm on that basis, consistent within 3%; 1,000 nm plus 45 min at 235 kt and 19.7 gph needs 98.6 of 100 gal with no climb allowance; below 231 KTAS at the same flow (about 4 kt under the design figure) it cannot carry the reserve (at Jane's 225 kt it needs 102 gal); 235 KTAS at 270 hp, 25,000 ft, 4,000 lb implies CD0 ~0.019 (AR 9.0, e 0.80, prop eta 0.80; AERO, grade E), optimistic for a 1983 pressurized single; at CD0 +20% the same power gives ~220 KTAS, still a pass on speed.
- **Pipistrel Panthera**: published range 1,460 nm vs 728 nm from fuel and flow; weights do not add: 2,899 - 1,797 != 1,023; the 1,460 nm claim is reproduced exactly by 420 L (2 x 210 L) at the published flow, while the published 770 lb full-fuel payload implies ~42-55 gal; both cannot be true, and the fuel quantity needs a primary source.
- **Grob GF 200**: screen speed has no altitude, or is below 6,000 ft; empty weight not found, so useful load cannot be screened.
- **Evektor VUT100-131i SuperCobra**: screen speed has no altitude, or is below 6,000 ft; weights do not add: 3,197 - 1,940 != 1,213.
- **Extra EA-400**: published range 1,300 nm vs 911 nm from fuel and flow; weights do not add: 4,407 - 2,974 != 1,347; fleet useful load 245 lb below factory; the only liquid-cooled certified piston here, so a natural precedent for a liquid-cooled Aeromomentum install.
- **Socata TB-21 Trinidad TC**: fleet useful load 202 lb below factory.
- **Robin HR100/285 Tiara**: published range 1,266 nm vs 612 nm from fuel and flow; screen speed has no altitude, or is below 6,000 ft; with optional tanks (111.5 gal) still-air range is 1,174 nm.
- **Ruschmeyer R90-230RG**: published range 600 nm vs 709 nm from fuel and flow; fleet useful load 122 lb below factory.
- **SIAI-Marchetti SF.260**: published range 1,040 nm vs 806 nm from fuel and flow.
<!-- flags:end -->

## What the screen says so far (no ranking)

1. **The reference passes as published, and misses on useful load as
   measured.** As published, the Cozy MKIV clears all three floors: 1,000 lb
   useful, 1,129 nm (1,300 statute mi at 40% power, reserve not stated) and
   191 KTAS at 75% and 8,000 ft (cozyaircraft.com specs). Measured on the
   CAFE Foundation's test aircraft, it gives 871 lb useful (1,179 lb empty
   against the 2,050 lb design gross), 1,049 nm still air with no reserve at
   12,000 ft lean, and 177 KTAS at 8,000 ft at wide-open throttle. The gap is
   the empty weight: the designer's 1,050 lb against one equipped builder
   aircraft at 1,179 lb. The first version of this list called the Cozy a
   near miss on 951 nm. That figure is 52 gal / 10.5 gph x 192 kt, the
   max-cruise claim AOPA Pilot quoted, set against a range the designer
   published at 40% power. It was a basis mismatch, not a units error: 1,300
   statute mi is 1,129 nm.
2. **The mission lives where pressurized singles live.** The rows that clear
   all three targets with real margin (P210N, PA-46-310P, Mooney 301,
   Skyrocket II, Lancair IV-P) sit at 3,550-4,100 lb gross and 285-435 hp.
   That is above the AM20T's 260 hp, so on the cube-root estimate they lose
   3-16% of cruise speed on an Aeromomentum engine. The Mooney 301's margin
   rests on design figures: its only prototype flew about 200 lb heavy and
   slower than planned, by an amount never published.
3. **Payload at 1,000 nm with a 45-minute reserve (information only).** It
   is not one of the targets, but it shows which tank sizes are tight. Five
   published passes (P210N, Velocity XL-RG, Rutan Defiant, Lancair Super ES,
   Mooney M22) cannot carry fuel for 1,000 nm plus 45 min in their standard
   tanks. The full table is in the screen above.
4. **Direct Aeromomentum fits among the passes and near misses**, at or under
   260 hp: Rutan Defiant (2x AM15T at the prototype's power), Velocity XL-RG
   (260 hp build), Express (210 hp), Berkut 360, TB-21, Wing Derringer
   (2x AM15T). Everything else needs more power than the line publishes.
5. **Claims that do not build up.** The Pipistrel Panthera's 1,460 nm needs
   about twice its published 210 L of fuel. The Extra EA-400's published
   ranges run from 1,100 to 2,100 nm against 911 nm from 106.7 gal at the
   owner's 24 gph, and its useful load falls about 245 lb in owner hands.
   Fleet useful loads run 38-245 lb below factory figures wherever both exist.
6. **Orphans with the best evidence.** The Express has the best-measured
   performance in the list (CAFE Foundation flight test, 1997), is a near miss
   only on one weighed builder aircraft, and its rights holder is unknown
   after five owners. The Windecker Eagle is the first FAA-certified
   all-composite type and a near miss on range by estimate.
7. **The Rohr 2-175 is not a mission candidate as built.** A 1,450 lb gross,
   150 hp two-seater cannot approach a 1,000 lb useful load; a revival would
   be a new design that borrows its ideas (buried engine, ducted pusher fan).

## Where the evidence is thin

- **Speeds without altitude.** Nine of the 22 passes and near misses screen on
  a speed with no altitude, or one below 6,000 ft.
- **Estimated fuel flows.** Nine rows have no published fuel flow at any
  setting and use the 0.45 lb/hp/h estimate (Long-EZ, Prescott, Questair,
  Glasair III, Super ES, Super Viking, Windecker, Derringer, M22); their range
  and payload are grade E.
- **Fleet weights.** Real fleet averages exist for almost none. Most "fleet"
  figures are one weighed or tested aircraft, or an owner's statement, and are
  labelled as such.
- **Missing numbers.** Skyrocket II has no published fuel capacity; the Grob
  GF 200 no empty weight; the SuperCobra and Super ES no fuel flow; the Rohr
  2-175 no empty weight, fuel or range.
- **Primary documents.** Several TCDS were read from archived or mirror
  copies, not the current FAA revision; the FAA DRS site refused automated
  access. Registry counts are assigned registrations, not airworthy aircraft.
  The Wayback Machine was intermittently offline, so some dead factory pages
  could not be recovered, and Aviation Consumer's fleet data is paywalled.
- **Engine.** Aeromomentum publishes no continuous rating or critical
  altitude for its turbo engines (see above).

## What happens next

- Passes and near misses have gone to the stage 2 rights research (AER-3787)
  as they were found.
- Stage 3 (AER-3783) picks a 5-8 design shortlist and replaces these
  published numbers with our own drag build-up, propeller estimate and
  Breguet range check.
