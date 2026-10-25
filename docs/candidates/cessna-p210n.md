# Cessna P210N Pressurized Centurion

Stage 1 stub (extended in stage 3 below), generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | certified, out of production |
| Designer / maker | Cessna Aircraft Co. |
| Years | 1978-83 (P210R 1985-86) |
| Number built | 834 P210N (TCDS serials) |
| Survivors / registered | 418 registered |
| Seats | 6 |
| Configuration | High wing, 6 seats, retractable gear, pressurized 3.35 psi |
| Construction | All-metal |
| Engine | Continental TSIO-520-P/-AF, 310 hp takeoff / 285 hp continuous, turbo |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 4,000 lb | T | FAA DRS, TCDS 3A21 Rev 50, 18 Nov 2021, read 2026-10-24 (archived: docs/longlist/sources/tcds-3A21-rev50-2021-11-18.pdf); value unchanged from Rev 49 | - |
| Empty weight | 2,426 lb | F | [source](https://www.aopa.org/go-fly/aircraft-and-ownership/aircraft-fact-sheets/cessna-p210) | 1982 standard empty |
| Useful load | 1,574 lb | F | [source](https://www.aopa.org/go-fly/aircraft-and-ownership/aircraft-fact-sheets/cessna-p210) | - |
| Useful load, fleet or as-weighed | 1,480 lb | B | [source](https://www.aviationconsumer.com/aircraftreviews/cessna-p210-centurion/) | owners report 900-1,000 lb payload with full fuel; midpoint + 87 gal |
| Usable fuel | 87 US gal | T | FAA DRS, TCDS 3A21 Rev 50, 18 Nov 2021, read 2026-10-24 (archived: docs/longlist/sources/tcds-3A21-rev50-2021-11-18.pdf); value unchanged from Rev 49 | S/N 761 on; 89 earlier |
| Published range | 925 nm | F | [source](https://australianaviation.com.au/1978/06/p210cessnas-high-flying-single/) | standard fuel, power and reserve not stated |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 199 M | 20000 | - | - | P | [source](https://australianaviation.com.au/1978/06/p210cessnas-high-flying-single/) | flight test, 33 in / 2,500 rpm |
| 183 | 20000 | 75% | 15.5 | F | [source](https://australianaviation.com.au/1978/06/p210cessnas-high-flying-single/) | 11.8 nm/gal |
| 196 P | 20000 | 80% | 18.8 | F | [source](https://australianaviation.com.au/1978/06/p210cessnas-high-flying-single/) | 10.4 nm/gal |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: near miss** - range -75 nm
  - Useful load: 1,574 lb (pass) against 1,000 lb.
  - Range: 925 nm (near; standard fuel, power and reserve not stated) against 1,000 nm.
  - Cruise: 196 KTAS at 20,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 1,066 / cannot @ 183 kt, 15.5 gph.
- **Measured or reported: partial: UL pass, speed pass**
  - Useful load: 1,480 lb (pass) against 1,000 lb.
  - Range: - nm (?; none found) against 1,000 nm.
  - Cruise: 199 KTAS at 20,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 285 hp (-3% speed, est. 193 KTAS).

Sanity flags:

- fleet useful load 94 lb below factory
- owners add tip tanks to reach 1,000 nm with reserve; on factory fuel it is marginal
- kit builders are attempting 210-class airplanes (Bill); what exists is fixed-gear 5-6 seat high-wing kits, none a retractable 210 copy: see '210-class kits' in LONGLIST.md

## Why it died

The Pressurized Centurion ended with Cessna's 1986 piston shutdown; the P210R sold only ~40 against the Malibu (P&P 2005).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Six seats, pressurisation and a large, well-documented fleet: the calibration case for the method. Kit builders now attempt 210 analogs (see the long list).

## Rights and provenance (known so far; research, not legal advice)

TCDS 3A21 holder: Textron Aviation Inc. (from Cessna, 2015). Owned by the stage 2 rights research (AER-3787).

## Safety record

Early detonation engine failures led to a turbo retrofit AD; 210 family accidents 20% fuel, 14% gear-up (Aviation Consumer).

<!-- stage3:start -->

## Stage 3: calibration case, not a candidate (AER-3783)

Our own check, from published geometry and weights, calibrated against published flight data. Method, calibration and the Aeromomentum assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are research, not legal advice. Nobody has been contacted.

### Bill's call

Bill, 2026-10-24: probably worthwhile, and kit builders are attempting 210 analogs, "but it's not solving some of what I'm after in the innovation side." Kept only as the calibration case.

### Verdict

**Calibration case.** Seven POH points match the build-up with drag factors of 1.26-1.32, tight enough to anchor the fleet calibration every other design is checked against. As a candidate it is a live, firmly held certified type, and Bill has set it aside on innovation. The 210-class kits he mentioned are in the long list (fixed-gear, high-wing five-to-six-seat kits; none is a retractable 210 copy).

### Idea ledger (what a new airplane should keep)

- Six seats, pressurisation and a large, well-documented fleet: the reference for the method.
- The 210-class kits (Bearhawk 5, Murphy Moose and others) show builders want a six-seat utility airplane; none offers the 210's retractable speed.

### Published, measured and our check, side by side

Read across a row only within one column's basis. The three targets are separate floors.

| | As published | Measured or reported | Our check, original engine |
|---|---|---|---|
| Useful load | 1,574 lb (pass) | 1,480 lb (pass) | 1,658 lb (the empty weight the model uses: 2,342 lb) |
| Range | 925 nm (near; standard fuel, power and reserve not stated) | not found | 829 nm, still air, no reserve, full fuel from MTOW, at 202 hp and 20,000 ft |
| Cruise | 196 KTAS at 20,000 ft (pass+) | 199 KTAS at 20,000 ft (pass+) | 179 KTAS at 202 hp and 20,000 ft |
| Screen | near miss | partial: UL pass, speed pass | see the verdict |

### Independent performance check

Model: `docs/shortlist/check/models/cessna-p210n.json`; result: `docs/shortlist/check/results/cessna-p210n.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 261 ft2, Wing 320 ft2, HTail 65 ft2, Fin 38 ft2; total 685 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 36.75 ft, area 175 ft2 (P, POH three-view); chords 64/44 in (Wikipedia, consistent with the area); NACA 64A215 / 64A412 (Lednicer).
- Fuselage 28.17 ft (P); width 4.0 ft (44 in cabin + skin) and height 4.8 ft: E, ours.
- Horizontal tail 13 ft span (P) x 2.77 ft mean chord = 36 ft2 (E, Vh ~0.65); fin 19.4 ft2 (E, Vv 0.045).
- Riveted aluminium: laminar run x_tr wing 0.10, tails 0.05, fuselage 0.
- Retractable gear without main gear doors (1979 on): open wells and legs D/q 0.30 ft2 (E). Wing strut-free.
- Turbo TSIO-520-P: 285 hp max continuous (T, TCDS 3A21), flat-rated to 20,000 ft (E). Cooling factor 1.3 (E). BSFC 0.50 at the POH recommended lean (derived from the POH: 19.2 gph at 80% of 285 hp).
- POH points at 4,000 lb, ISA.

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 170 | 10,000 | 222 | 18.0 | P | 189 | +11% | 1.31 | 176 | POH Fig 5-7, 78% |
| 152 | 10,000 | 177 | 13.7 | P | 170 | +12% | 1.32 | 143 | POH, 62% |
| 187 | 20,000 | 228 | 19.2 | P | 206 | +10% | 1.27 | 188 | POH, 80% |
| 176 | 20,000 | 202 | 16.3 | P | 194 | +10% | 1.27 | 169 | POH, 71% |
| 157 | 20,000 | 171 | 13.5 | P | 177 | +13% | 1.32 | 143 | POH, 60% |
| 193 | 23,000 | 231 | 19.2 | P | 212 | +10% | 1.26 | 192 | POH, 81% |
| 171 | 23,000 | 188 | 14.8 | P | 191 | +11% | 1.28 | 159 | POH, 66% |

**Drag factor used: 1.29** (fleet calibration (own points read cleaner than the fleet); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.29.

**Drag build-up at 10,000 ft, 222 hp, 4,000 lb, with the factor applied:** 171 KTAS, CD0 0.0223 on S = 175.0 ft2, propeller efficiency 0.82, L/D 11.5.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 1.205 | Swet 320.0 ft2, Re 6.9M, Cf 0.00285, FF 1.320, Q 1.00, x_tr 0.10 |
| HTail | 0.289 | Swet 65.1 ft2, Re 4.0M, Cf 0.00331, FF 1.279, Q 1.05, x_tr 0.05 |
| Fin | 0.156 | Swet 38.3 ft2, Re 5.2M, Cf 0.00317, FF 1.229, Q 1.05, x_tr 0.05 |
| Fuselage | 0.771 | Swet 261.4 ft2, Re 40.4M, Cf 0.00241, FF 1.225, Q 1.00, x_tr 0.00 |
| retractable gear, no main doors (open wells) | 0.300 | fixed allowance |
| cooling | 0.155 | Raymer 12.39 x 1.30 |
| leakage+protuberance | 0.144 | 5% of the rest |
| calibration factor | 0.876 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.862 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 202 hp at 20,000 ft gives 179 KTAS; still-air range on full usable fuel from MTOW 829 nm (climb allowance 64 lb); payload at 1,000 nm cannot lb with no reserve, cannot lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -161 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 161 (162) | 1,658 (1,819) | 916 | cannot | cannot (cannot) | 130: 1,183 / 1,142 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 171 (171) | 1,658 (1,819) | 931 | cannot | cannot (cannot) | 132: 1,173 / 1,132 |

### Engine fit with the Aeromomentum line

- **Power.** The AM20T at 195 hp assumed continuous replaces a TSIO-520-P at 285 hp maximum continuous (TCDS 3A21). That gives 161-171 KTAS: just above the floor.
- **Mass and CG.** The installed mass falls by about 161 lb (E), in the nose; no credit is taken.
- **Fuel.** At continuous power it cannot fly 1,000 nm on 89 gal, even with no reserve. At economy power it carries 1,132-1,142 lb with reserve, but at 130-132 KTAS, below the speed floor.
- **Path.** A re-engine would be an STC on a certified type, not a revival. The engine is uncertified, which is a certification question outside this survey.

### Rights and provenance (stage 2)

Firmly held (Elon, `docs/rights/cessna-p210n.md`, PR #3). TC 3A21 (Rev 50) is current and held by Textron Aviation, which supports the fleet. 418 piston P210Ns are on the US register. Modifying existing airframes under STCs is proven (the Silver Eagle turbine conversion). Building new ones from data that is not ours is an attorney question.

### Safety record

Record (NTSB CAROL, P210 model strings, 1978-2026): 291 accidents, 78 fatal events, 162 killed; US only 68 fatal and 139 killed; 874 built. Our keyword screen and reading of the fatal accidents, not NTSB-coded findings: about 36 involve weather, IMC, night or icing, about 11 are engine mechanical failures (mostly oil-system and maintenance), 5 are fuel exhaustion or starvation, and 2 are engine-compartment fires. Gear-up or collapse appears in 53 records, mostly non-fatal. The record includes the 1980 detonation crashes that led to rich-mixture ADs and a 1981 turbo retrofit.

### Why it died, and whether a revival fixes it

Cessna ended piston production in 1986, in the product-liability era, and the P210R sold only about 40 against the Malibu. The market did not reject the design. But it is a live, firmly held type certificate, not something to revive.

### Not yet done

- None for the survey. It remains the calibration case if the method changes.
- What a modern rebuild changes in mass, cost and build hours (MANUFACTURING, stage 4, AER-3784).

<!-- stage3:end -->
