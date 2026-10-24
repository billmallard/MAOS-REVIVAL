# Berkut 360

Stage 1 stub (extended in stage 3 below), generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Dave Ronneberg, Experimental Aviation Inc. |
| Years | ~1991; kits ~1992-2002 |
| Number built | ~75 kits, ~20 completed |
| Survivors / registered | 31 registered incl. variants (airport-data via Wikipedia) |
| Seats | 2 |
| Configuration | Canard pusher, tandem 2 seats, retractable gear |
| Construction | Molded carbon/glass composite |
| Engine | Lycoming IO-360, 200-205 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,000 lb | F | [source](https://planeandpilotmag.com/experimental-aviation-berkut/) | - |
| Empty weight | 1,035 lb | F | [source](https://planeandpilotmag.com/experimental-aviation-berkut/) | - |
| Useful load | 965 lb | F | [source](https://planeandpilotmag.com/experimental-aviation-berkut/) | derived |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 55 US gal | F | [source](https://planeandpilotmag.com/experimental-aviation-berkut/) | - |
| Published range | 1,315 nm | F | [source](http://www.airbum.com/pireps/PirepBerkut.html) | economy cruise, 30 min reserve |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 180 M | - | - | - | P | [source](http://www.airbum.com/pireps/PirepBerkut.html) | measured, 2,600 rpm, 19.5 in MP (Sport Aviation Feb 1995) |
| 208 P | 8000 | 75% | 10.3 | F | [source](http://www.airbum.com/pireps/PirepBerkut.html) | factory test with an earlier 'hot-rodded' engine |
| 187 | - | - | 7.7 | F | [source](http://www.airbum.com/pireps/PirepBerkut.html) | factory economy cruise |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: near miss** - UL -35 lb
  - Useful load: 965 lb (near) against 1,000 lb.
  - Range: 1,315 nm (pass; economy cruise, 30 min reserve) against 1,000 nm.
  - Cruise: 208 KTAS at 8,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 718 / 683 @ 187 kt, 7.7 gph.
- **Measured or reported: partial: speed pass, speed unconditioned**
  - Useful load: - lb (?) against 1,000 lb.
  - Range: - nm (?; none found) against 1,000 nm.
  - Cruise: 180 KTAS at an unstated altitude (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 205 hp.

Sanity flags:

- none raised

## Why it died

Lawsuits between Ronneberg and Murphy bankrupted both; later owners did not last and a 2003 sale fell through (Wikipedia).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Molded carbon and glass parts that turned the Long-EZ shape into a retractable 200 kt two-seater.
- Lesson: over 100 molded parts meant expensive tooling and kits (Bill: 'expensive to build'); molds are an asset only while someone keeps them.

## Rights and provenance (known so far; research, not legal advice)

Ronneberg -> Renaissance Composites (Riley, 1996) -> Berkut Engineering and Design. Current holder not public. Owned by the stage 2 rights research (AER-3787).

## Safety record

2002 in-flight canard separation (N827CM); 1995 and 1996 crashes (NTSB via Wikipedia).

<!-- stage3:start -->

## Stage 3: checked, then dropped from the shortlist by Bill (2026-10-24)

Our own check, from published geometry and weights, calibrated against published flight data. Method, calibration and the Aeromomentum assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are research, not legal advice. Nobody has been contacted.

### Bill's call

Bill, 2026-10-24: "not likely. These were expensive to build." Dropped from the shortlist; the long-list row stays.

### Verdict (stage 3, before Bill's review)

**Rank 7.** It is the only two-seater on the shortlist, and it cannot be checked. No measured performance exists, and its wing area is unsourced. Our fleet-calibrated model gives 239 KTAS on 195 hp, faster than the designer's own 191 KTAS cruise claim, which says the geometry is wrong. On weight and fuel alone: 949 lb useful, and 1,000 nm only at economy power (608-616 lb with reserve). Its range and payload are grade E.

### Idea ledger (what a new airplane should keep)

- Molded carbon and glass parts that took the Long-EZ shape to a retractable 200 kt class two-seater.
- Lesson: over 100 molded parts made the kit expensive to build (Bill's reason) and left the design hostage to its molds, which are now lost.

### Published, measured and our check, side by side

Read across a row only within one column's basis. The three targets are separate floors.

| | As published | Measured or reported | Our check, original engine |
|---|---|---|---|
| Useful load | 965 lb (near) | not found | 965 lb (the empty weight the model uses: 1,035 lb) |
| Range | 1,315 nm (pass; economy cruise, 30 min reserve) | not found | 1,034 nm, still air, no reserve, full fuel from MTOW, at 150 hp and 8,000 ft |
| Cruise | 208 KTAS at 8,000 ft (pass+) | 180 KTAS at altitude not stated (pass+) | 218 KTAS at 150 hp and 8,000 ft |
| Screen | near miss | partial: speed pass, speed unconditioned | see the verdict |

### Independent performance check

Model: `docs/shortlist/check/models/berkut-360.json`; result: `docs/shortlist/check/results/berkut-360.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 118 ft2, Wing 85 ft2, Strake 62 ft2, Canard 23 ft2, Winglets 17 ft2; total 305 ft2.

**Model assumptions** (grade E unless a source is named):

- Span 26.67 ft and length 18.5 ft (F, Jane's 1993-94 via Wikipedia). Wing area 110 ft2 is unsourced (E, low confidence). Panels and strakes scaled from the CAFE-measured Cozy by span ratio 0.95 (E).
- Tandem two-seat fuselage: width 2.6 ft, height 3.4 ft (E). Canard 12 ft2, 11.5 ft span; winglets 2 x 8 ft2 (E).
- Fully retractable gear: no gear term. Laminar run as the Cozy. Canard carries 20% of the lift (E).
- Prop 66 in constant speed (E). No measured performance exists, so the fleet-median calibration factor applies.

**Drag factor used: 1.29** (fleet calibration (no published point with known power); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.16.

**Drag build-up at 8,000 ft, 150 hp, 1,850 lb, with the factor applied:** 218 KTAS, CD0 0.0126 on S = 110.0 ft2, propeller efficiency 0.84, L/D 9.8.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.271 | Swet 85.1 ft2, Re 5.0M, Cf 0.00228, FF 1.396, Q 1.00, x_tr 0.35 |
| Strake | 0.207 | Swet 62.0 ft2, Re 9.2M, Cf 0.00242, FF 1.315, Q 1.05, x_tr 0.20 |
| Canard | 0.105 | Swet 22.6 ft2, Re 2.0M, Cf 0.00280, FF 1.655, Q 1.00, x_tr 0.35 |
| Winglets | 0.063 | Swet 16.8 ft2, Re 3.5M, Cf 0.00276, FF 1.298, Q 1.05, x_tr 0.25 |
| Fuselage | 0.317 | Swet 118.0 ft2, Re 35.5M, Cf 0.00216, FF 1.242, Q 1.00, x_tr 0.10 |
| cooling | 0.061 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.051 | 5% of the rest |
| calibration factor | 0.312 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.102 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 150 hp at 8,000 ft gives 218 KTAS; still-air range on full usable fuel from MTOW 1,034 nm (climb allowance 20 lb); payload at 1,000 nm 636 lb with no reserve, cannot lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change +16 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 239 (249) | 949 (949) | 873 | cannot | cannot (cannot) | 205: 650 / 608 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 256 (266) | 949 (949) | 906 | cannot | cannot (cannot) | 218: 658 / 616 |

### Engine fit with the Aeromomentum line

- **Power.** The AM20T at 195 hp assumed continuous replaces a 205 hp IO-360 (most builders chose a 260 hp IO-540). Stage 1 called it a direct fit.
- **Mass and CG.** About +16 lb installed (E), in the tail of a canard. Not checked.
- **Speed.** Our model is not credible here (see below), so no Aeromomentum speed is claimed.

### Rights and provenance (stage 2)

Open question (Elon, `docs/rights/berkut-360.md`, PR #3). The chain runs from the Ronneberg-Murphy partnership, to Experimental Aviation Inc. (bankrupt), to Renaissance Composites (1996), to Vicki Cruse's Berkut Engineering and Design (2001), which withdrew the kit in 2002. Cruse died in 2009, and who holds the molds (over 100 molded parts by 2002) is not on any public record. The designer, Dave Ronneberg, is active and owns two related aircraft. There is no BERKUT mark.

### Safety record

Record (NTSB CAROL plus registrations filed under builder names): 9 events, 2 fatal, on about 31 aircraft. The fatal accidents were an accelerated stall in a high-g airshow turn (the prototype, 1995) and an in-flight canard separation because the builder never fitted the attach bolts (2002). The rest are builder errors and retractable-gear failures. The NTSB found no deep stall, rain-on-canard or pusher prop strike. The canard is a bolt-on surface whose missing attachment was fatal.

### Why it died, and whether a revival fixes it

Lawsuits between the founding partners bankrupted both, later owners did not last, and the kit was withdrawn in 2002 for drone work. A revival fixes that if the molds can be found; it is a business failure, not a design one.

### Not yet done

- Primary geometry and one measured cruise point; nothing else changes this rank.
- Trace the molds (Elon).

<!-- stage3:end -->

<!-- stage4:start -->

## Stage 4: what modern manufacturing changes (AER-3784)

Short note. Method, prices and sources are in [docs/MANUFACTURING.md](../MANUFACTURING.md); the weight table is generated by `docs/manufacturing/weights.py`. Desk study: nothing weighed or quoted by us, nobody contacted. Every E is our estimate.

**Original construction:** molded carbon/glass, over 100 molded parts. Molds unaccounted for since 2009.

**Modern route:** find the molds, or re-derive and re-tool. It is already molded carbon, so there is little weight to win.

**Empty weight:** rebuild **1,000-1,190 lb**, useful load **810-1,000 lb** (stage 3: 965). No weighed aircraft found. Engine change +18 to +20 lb.

**Weight build-up:**

| Item | Light, lb | Heavy, lb | Basis | Grade |
|---|---|---|---|---|
| Starting empty weight | 1,035 | 1,160 | 1,035 (F, Brassey's via Wikipedia). No weighed aircraft found; heavy end applies the Cozy's CAFE 12% over brochure (E) | F/E |
| Lost molds re-made; carbon/glass molded parts kept as carbon | -30 | +20 | Already molded carbon/glass; new tooling neither helps nor hurts much | E |
| Panel: EFIS | -10 | +0 | Small panel | E |
| EFI engine: backup battery and bus | +5 | +10 | One ECU | E |
| **Rebuild empty weight, no engine credit** | **1,000** | **1,190** | sum, rounded to 10 lb | E |

Hours: 1,500 factory (F, AOPA Pilot Dec 1994); kit $29,490 then.

**Home-shop route** ([MANUFACTURING.md](../MANUFACTURING.md#the-home-shop-route), tools about $20-49k, prices read 2026-10-24, all E): The best home-mold candidate by size: about 400 ft2 of mold surface, 800-1,600 h.

<!-- stage4:end -->
