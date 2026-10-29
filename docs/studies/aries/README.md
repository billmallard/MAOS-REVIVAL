# Bellanca T-250 Aries: independent check of the range result (AER-3867)

This is the deep check that follows Bill's pick on AER-3783. The stage 3
shortlist check had the Aries on an Aeromomentum AM20T at 906-919 nm on full
fuel at continuous power, "about 90 nm short". This study rebuilds that number
from geometry, calibrates it on every measured speed found for the four
airframes, and reports it the way the brief now asks (amended 2026-10-25):
**useful load and range are targets, not floors.** It does not give a pass/fail
on the pair. It says how close the airplane gets, what it trades for it, and
what closing the gap would cost. Cruise speed above 160 KTAS is still a floor.

Grades used throughout: **T** type certificate data sheet; **F** factory or
Jane's; **P** magazine flight test with stated conditions; **B** owner or
builder report; **E** our estimate. Every number below is **E** unless it says
otherwise. The **AM20T ratings are assumed**: 195 hp continuous (75% of 260 hp
take-off), BSFC 0.45 lb/hp/h, and two critical-altitude bases, AM-low (8,000 ft)
and AM-high (16,000 ft), with cruise at that altitude. None is published by
Aeromomentum. Bill is taking the ratings up with the maker; this check carries
both bases and does not wait on him.

The generated tables are the record: [`tables.md`](tables.md) (calibration,
range matrix, closers, sensitivity), [`closers.md`](closers.md) (combined
closers), [`payload_range.md`](payload_range.md) (the tradeoff). Sources and
their grades are in [`sources.md`](sources.md).

## 1. The result

All figures are on the standard airframe: MTOW 3,150 lb (T), empty 1,850 lb (F,
factory; no airframe has a published weighed figure), 76 gal usable (T), so
1,300 lb useful load (F). With full fuel at MTOW the payload is 844 lb.

**How close it gets to 1,000 nm, full fuel at MTOW (844 lb payload)**

| Cruise | KTAS, AM-low / AM-high | nm, no reserve | nm, 45 min reserve | Against 1,000 nm, with reserve |
|---|---|---|---|---|
| Continuous power, 195 hp | 185 / 196 | 905 / 930 | 766 / 782 | 22-23% short |
| 65% of take-off, 169 hp | 174 / 185 | 985 / 1,008 | 854 / 869 | 13-15% short |
| 160 KTAS (the speed floor) | 160 / 160 | 1,098 / 1,172 | 978 / 1,052 | 2% short / 5% over |
| Fastest speed that still makes 1,000 nm + 45 min | **157** / 167 | - | 1,000 | - |

**Read the stage 3 figure carefully.** Its 906-919 nm is still air with **no
reserve** (stage 3 table, `docs/shortlist/check/results/bellanca-t250-aries.txt`).
On that basis it is 7-10% short, and this study agrees with it (905-930 nm).
With the 45-minute reserve this issue asks for, the same flight is 766-782 nm,
22-23% short.

**The stage 3 "passes at economy" needs a qualifier.** Its economy setting
(127 hp, 65% of the continuous rating) flies **153 KTAS on AM-low**, below the
160 KTAS floor. On AM-low, 76 gal will not carry the airplane 1,000 nm with a
45-minute reserve at any speed that clears the floor: the fastest speed that
makes it is 157 KTAS. On AM-high it makes 1,000 nm with the reserve at up to
167 KTAS.

**The payload-range tradeoff** (45 min reserve; full table with no-reserve
figures in [`payload_range.md`](payload_range.md)):

| Payload, lb | Fuel, gal | 160 KTAS, nm (low / high) | 65% take-off, nm | Continuous, nm |
|---|---|---|---|---|
| 544 (useful load 1,000 lb, take-off 2,850 lb) | 76 | 1,028 / 1,132 | 888 / 916 | 793 / 818 |
| 700 | 76 | 1,002 / 1,090 | 871 / 892 | 779 / 799 |
| 844 (full fuel at MTOW) | 76 | 978 / 1,052 | 854 / 869 | 766 / 782 |
| 900 | 67 | 831 / 888 | 723 / 730 | 647 / 654 |
| 1,000 | 50 | 572 / 600 | 492 / 484 | 434 / 428 |

So, each target on its own:

- **Useful load:** 1,300 lb (F), 30% over the target on its own. It holds only
  if a rebuilt empty weight stays near the factory 1,850 lb; nobody has
  published a weighed figure for any of the four airframes. Weight moves this
  number one for one, but it does not move range on full fuel.
- **Range:** over 1,000 nm with a 45-minute reserve only at or near the speed
  floor. At AM-high that means 160-167 KTAS with up to about 860 lb of payload.
  At AM-low it means about 710 lb of payload at 160 KTAS.
- **Speed:** 185-196 KTAS at continuous power, over the preferred 180, but only
  for about 770-780 nm with a reserve.
- **1,000 lb of payload over 1,000 nm** is out of reach on the standard MTOW at
  any speed: best-range speed (114-128 KTAS) gives 754 / 682 nm with the
  reserve. It needs the MTOW increase in section 3.

## 2. The drag build-up and its calibration

**Geometry.** TCDS A11SW Rev 2 (T, [archived](../../longlist/sources/tcds-A11SW-rev2-1980-07-01.pdf))
carries **no external dimensions**. What it does give is consistent with the
model: the CG range (17-34% of a 65 in chord) fits the constant-chord wing, and
it adds stations, Vno 165 KCAS and the propeller pitch stops. The external
geometry comes from *Jane's* 1979-80 (F): span 31 ft 4 in, constant chord 5 ft
6 in, length 26 ft 2 in, tailplane span 12 ft 6 in, propeller 6 ft 5 in,
section NACA 600412 modified. The stabilator chord (2.55 ft), fin (15 ft²) and
fuselage cross-section (4.0 x 4.4 ft) are ours (E), from the stage 3 OpenVSP
model and tail-volume coefficients. Jane's tailplane span replaces stage 3's
11.0 ft estimate. Jane's chord confirms the 5.43 ft stage 3 derived from span
and area.

**Build-up** (Raymer/Hoerner component method, `perf.py`, unchanged from stage
3), at 185 KTAS and 8,000 ft, before calibration:

| Component | Wetted area, ft² | D/q, ft² | Notes |
|---|---|---|---|
| Wing | 320.9 | 0.950 | Re 8.9M, laminar to 25% chord, FF 1.29 |
| Fuselage | 234.8 | 0.650 | Re 42.7M, FF 1.24 |
| Stabilator | 64.7 | 0.258 | Q 1.08 |
| Fin | 25.4 | 0.093 | Q 1.05 |
| Cooling | - | 0.094 | Raymer eq. 12.39 |
| Leakage and protuberance | - | 0.102 | 5% of the above |
| **Total, raw** | | **2.147** | CD0 0.0126 on 170 ft² |
| **Calibrated (x 1.290)** | | **2.770** | CD0 0.0163 |

**Calibration** (`tables.md` section 1). Six measured points, all on the
prototype N51AG with the carbureted O-540, all grade P: two from *AOPA Pilot*
(March 1977) and four from R. L. Collins in *Flying* (April 1977). We took the
density altitude of AOPA's cruise point from its own OAT and IAS/TAS pair:
7,400 ft, not the 6,500 ft stage 3 used. Part-throttle power comes from the
Lycoming O-540-A chart, anchored on AOPA's own "73%". The six factors run from
1.246 to 1.334, with a mean of **1.290**. That sits on the surveyed fleet's
1.29, so the Aries is as clean as a typical 1970s metal single and no cleaner.
Moving every test weight across 2,600-3,150 lb, every part-throttle power by
±5%, or AOPA's density altitude across 6,500-7,900 ft keeps the mean within
1.23-1.35.

**One production airframe disagrees.** The owner of N77CT (s/n 0004, B) saw
"about 190MPH TAS instead of the 208MPH TAS promised" on a 2013 ferry flight,
with altitude and power not stated, on an engine overhauled from parts of
unknown time. Taken at 8,000 ft and 70%, that implies a factor of 1.54, which
costs about 50 nm (sensitivity table, last row). It is kept as a pessimistic
bound and is not used in the mean. No speed with logged conditions exists for
any of the three production airframes.

**Factory range against our model**, original O-540, BSFC 0.45, 45 min reserve:
787 / 879 / 986 nm at 75 / 65 / 55% against Jane's 860 / 946 / 1,016. Jane's
reads 3-9% optimistic. Its reserve is at 45% power, a smaller reserve than ours
at cruise power, and that accounts for part of the gap.

**Sanity checks.** Speed against power and drag: the calibrated build-up flies
AOPA's 181 KTAS at 180 hp by construction. Collins's 13-13.5 gph at "a shade
below 75%" is 0.42-0.44 lb/hp/h at 183 hp, in line with the BSFC used. That
fuel flow is his inference from power, not a meter reading, so it does not
check fuel burn independently. Fuel against range: 905 nm still air at
185 KTAS is 4.9 h, at about 14.6 gph (88 lb/h at 195 hp and 0.45), which is 72
of 76 gal after the climb allowance.

**One method change from stage 3.** The shared range integrator burns fuel in
whole 5 lb steps and drops the last partial step. That understated no-reserve
range, and it let the last step eat into the reserve, which overstated
reserve range, each by up to about 10 nm. This study flies the final fraction
(`cruise_range_frac` in `aries_check.py`); the stage 3 module is unchanged.
The effect on the headline: 904 → 905 nm with no reserve, 775 → 766 nm with
45 min.

## 3. What closes the gap, and what it costs

These are the levers to make 1,000 nm with a 45-minute reserve from full fuel
at MTOW (`tables.md` section 4, `closers.md`). Weights are grade E. Cost is
given where a weight is not the real price.

| Lever | What it takes (AM-low / AM-high) | Weight or cost | What it trades |
|---|---|---|---|
| **Fly slower** | 157 / 167 KTAS on the standard 76 gal | none | Speed. On AM-low this is 3 kt under the 160 floor; on AM-high it clears it |
| **More fuel, at 160 KTAS** | 77.4 gal / none needed | about +1 lb tank (AM-low) | nothing measurable |
| **More fuel, at 65% of take-off** (174 / 185 KTAS) | 86.4 / 84.7 gal (+10 / +9 gal) | about +5 lb tank, plus 54-60 lb of fuel | full-fuel payload 844 → about 780 lb at the same MTOW |
| **More fuel, at continuous** (185 / 196 KTAS) | 94.1 / 91.8 gal (+18 / +16 gal) | about +9 lb tank, plus 96-108 lb of fuel | full-fuel payload 844 → about 730-740 lb at the same MTOW |
| **90 gal usable, then fly as fast as it allows** | 179 / 193 KTAS | about +7 lb tank | as above, about 755 lb full-fuel payload |
| **Five drag items together** (below) | +11 / +13 KTAS, +47 / +49 nm; on 76 gal, 1,000 nm + 45 min at 174 / 186 KTAS | about 10-20 lb, and a smooth bonded wing skin | build cost, mostly the wing skin |
| **Drag items and 90 gal** | 1,000 nm + 45 min at full continuous speed, 196 / 209 KTAS | about 20-30 lb, plus 84 lb of fuel | payload, as above |
| **Raise MTOW**, 1,000 lb payload over 1,000 nm + 45 min | +180 / +160 lb at 160 KTAS (79 / 75 gal); +240 / +230 lb at 65%; +280 / +260 lb at continuous | structure, gear and certification basis; stall speed +3-4% | a structural re-substantiation |

Tank weight is from Raymer's statistical fuel-system relation (eq. 15.53,
integral tanks, two tanks): about 0.5 lb per added gallon in the 80-100 gal
range. **Where the extra fuel goes is not shown.** At 12% thickness and a 5 ft
6 in chord, each foot of wing span between the spars holds roughly 8-9 gal, so
18 gal is about one more foot of tank bay in each wing. No drawing of the
Aries's spar and rib layout was found, so this is an envelope check, not a
tank design. It belongs to MANUFACTURING and, for the bay structure, to
STRUCTURES.

**The drag items, one at a time** (continuous power, AM-low, 45 min):

| Item | Gain | Weight (E) | Notes |
|---|---|---|---|
| Laminar run on the wing, 25% → 40% chord | +24 nm, +6 KTAS | ~0 | needs a smooth bonded or composite skin held below the Braslow-Knox roughness limit: a manufacturing choice, not a bolt-on |
| Modern propeller, +3% efficiency | +9 nm | ±0 | composite three-blade; the 3% is an assumption, not a selected propeller |
| Radiator in a designed duct, cooling drag -40% | +5 nm | part of the installation | the AM20T is liquid-cooled, so a radiator duct has to be designed anyway; this sets its target |
| Control-surface gap seals | +3 nm | 2-4 lb | |
| Leakage seals, root fillet, gear-door and wheel-well seals | +3 nm | 3-6 lb | |

The single largest unknown is not on the airframe. The engine's real fuel
burn moves the result more than any drag item: BSFC 0.42 gives +67 to +71 nm,
0.48 gives -59 to -62 nm.

## 4. How thin the sources are, and what would move the answer

**Thin.** The TCDS has no external dimensions. Jane's gives the planform, the
overall length and the tailplane span, but nothing more. The stabilator chord,
fin, fuselage section and laminar run are our estimates. Every measured speed
comes from one airframe, the prototype, in 1977. Neither magazine states the
test weight. No POH cruise table, weighed empty weight or logged fuel flow was
found for any of the four aircraft.

**But geometry is not what moves the range.** Because the drag factor is
re-calibrated on the six measured points, a geometry error is absorbed into
the factor. Moving any geometry input across its credible range changes the
range by 1 nm or less, against up to ±25 nm without re-calibration
(`tables.md` section 5). What does move it:

| Input | Range of the input | Change in nm, 45 min | Grade now | What would settle it |
|---|---|---|---|---|
| AM20T BSFC | 0.42 - 0.50 | +67 to +71 / -94 to -100 | assumed | Aeromomentum's measured fuel flow at cruise power |
| AM20T continuous rating | 180 - 210 hp | +49 / -44 (slower / faster) | assumed | Aeromomentum's published rating |
| Production-airframe drag (N77CT) | factor 1.29 → 1.54 | -50 | B, conditions unknown | one speed run on a production Aries with altitude, power and weight logged |
| Power at the test points | ±5% | ±13 | E, from the Lycoming chart | the AOPA or Flying fuel flows and mixture settings, if a full scan of either article turns up |
| Test weight | 2,600 - 3,150 lb | -6 / +9 | E | the same |
| Any geometry input | credible range | ≤1 | F / E | a three-view or factory drawings |

So the number that would move most if a better source turned up is the
**engine's fuel burn**, then **a production airframe's measured speed**.
Better geometry would make the build-up more honest, but it would not change
the range much.

## 5. What this study does not show

- No spin, stall, stability or flutter claim. None is made from published
  material.
- The AM20T installation (mass and CG, cooling, mount) is the stage 3 estimate,
  unchanged here.
- Empty weight is the factory figure. A rebuilt airframe that comes out heavier
  loses useful load pound for pound. Range on full fuel stays nearly the same.
- The added tank volume and the MTOW increase are envelope estimates. Neither
  has a structural check, and STRUCTURES is not routed to this issue.

## Regenerating

From the repo root (about 3 minutes, then about 1 minute each):

```
python3 docs/studies/aries/aries_check.py         # results.json, tables.md
cd docs/studies/aries
python3 aries_closers.py                           # closers.json, closers.md
python3 aries_payload_range.py                     # payload_range.json, payload_range.md
```

`aries_check.py` imports `perf.py` and `run_check.py` from
`docs/shortlist/check/` (stage 3, unchanged) and the stage 3 OpenVSP wetted
areas.
