# Mooney 301

Stage 1 stub (extended in stage 3 below), generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | prototype that never reached production |
| Designer / maker | Roy LoPresti, Mooney Aircraft |
| Years | 1983 first flight; ~70 test hours |
| Number built | 1 |
| Survivors / registered | none (wings cut off; fate unknown) |
| Seats | 6 |
| Configuration | Low wing, 6 seats, retractable gear, pressurized 5.0 psi, NLF wing |
| Construction | Metal |
| Engine | Lycoming TSIO-540, 360 hp, turbo |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 4,000 lb | F | [source](https://mooneyevents.com/Mooney301.html) | - |
| Empty weight | 2,548 lb | F | [source](https://en.wikipedia.org/wiki/Mooney_301) | Air International Jan 1984 |
| Useful load | 1,452 lb | F | [source](https://en.wikipedia.org/wiki/Mooney_301) | derived; Mooney newsletter claims 1,600 |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 100 US gal | F | [source](https://mooneyevents.com/Mooney301.html) | capacity |
| Published range | 986 nm | F | [source](https://mooneyevents.com/Mooney301.html) | cruise, 45 min reserve |

Cruise settings (the starred row is the one screened for speed):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 235 * | 25000 | 75% | 19.7 | F | [source](https://mooneyevents.com/Mooney301.html) | at 'max altitude'; prototype reportedly reached only 260 kt top speed |

## Screen (stage 1, published numbers)

- **Verdict: pass**
- Useful load: 1,452 lb (pass) against 1,000 lb.
- Range: 1,193 nm still-air (pass; basis: calc) against 1,000 nm.
- Cruise: 235 KTAS at 25,000 ft (pass+) against >160 KTAS (>180 preferred).
- Payload at 1,000 nm: 949 lb with no reserve; 860 lb with a 45 min reserve. Setting: 235 KTAS at 19.7 gph.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 360 hp (-10% speed, est. 211 KTAS).

Sanity flags:

- published range 986 nm vs 1,193 nm from fuel and flow

## Why it died

Republic Steel's takeover by LTV forced the sale of Mooney; the new French-led owners judged the 301 ~200 lb heavy and too slow (Wikipedia).

## Rights and provenance (known so far; research, not legal advice)

Mooney (now Mooney International) vs Daher (TBM lineage): whether 301 data sits with either is not found. Owned by the stage 2 rights research (AER-3787).

## Safety record

No accidents found.

<!-- stage3:start -->

## Stage 3: shortlist rank 3 of 8 (AER-3783)

Our own check, from published geometry and weights, calibrated against published flight data. Method, calibration and the Aeromomentum assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are research, not legal advice. Nobody has been contacted.

### Verdict

**Rank 3.** It has the best payload-range on our numbers (858-867 lb over 1,000 nm with reserve) and is the only six-seater close to the mission. It ranks third because there is nothing to revive but published dimensions, the rights are an attorney question, the tail is known-bad, and its published speed reads 9% optimistic against the fleet calibration.

### Independent performance check

Model: `docs/shortlist/check/models/mooney-301.json`; result: `docs/shortlist/check/results/mooney-301.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 293 ft2, Wing 276 ft2, HTail 46 ft2, Fin 28 ft2; total 643 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 36.75 ft, area 150 ft2 (F, Jane's 1983-84 via Wikipedia); NLF(1)-0315. Taper 0.5 assumed (E): root 5.44 ft, tip 2.72 ft.
- Fuselage 29.77 ft (F); width 4.4 ft and height 4.8 ft for a six-seat pressurized cabin: E, ours.
- Tails by volume coefficient (E): horizontal Vh 0.65 -> 26 ft2, vertical Vv 0.045 -> 15.5 ft2.
- Laminar run x_tr: wing 0.20 (NLF section on metal; not credited in full), tails 0.05, fuselage 0.
- Retractable gear: no gear term. LoPresti low-drag cowl: cooling factor 1.0 (E).
- Turbo TIO-540 360 hp flat-rated to 25,000 ft (E). Published-point weight unstated: 3,700 lb assumed (E).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 238 | 17,500 | 270 | 18 | P | 239 | +1% | 1.02 | 266 | Bob Kromer, Mooney test pilot (Mooney Flyer Oct 2012): 235-240 KTAS at 75%, 15,000-20,000 ft |

**Drag factor used: 1.29** (fleet calibration (own points read cleaner than the fleet); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.02.

**Drag build-up at 17,500 ft, 270 hp, 3,700 lb, with the factor applied:** 217 KTAS, CD0 0.0210 on S = 150.0 ft2, propeller efficiency 0.83, L/D 11.0.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 1.008 | Swet 276.1 ft2, Re 6.4M, Cf 0.00258, FF 1.415, Q 1.00, x_tr 0.20 |
| HTail | 0.217 | Swet 45.8 ft2, Re 3.6M, Cf 0.00336, FF 1.342, Q 1.05, x_tr 0.05 |
| Fin | 0.123 | Swet 28.2 ft2, Re 4.6M, Cf 0.00321, FF 1.289, Q 1.05, x_tr 0.05 |
| Fuselage | 0.843 | Swet 292.5 ft2, Re 44.5M, Cf 0.00236, FF 1.220, Q 1.00, x_tr 0.00 |
| cooling | 0.130 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.116 | 5% of the rest |
| calibration factor | 0.707 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.482 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 270 hp at 20,000 ft gives 222 KTAS; still-air range on full usable fuel from MTOW 1,056 nm (climb allowance 55 lb); payload at 1,000 nm 885 lb with no reserve, cannot lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -207 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 176 (193) | 1,452 (1,659) | 1,143 | 922 | 858 (1,107) | 142: 1,015 / 973 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 187 (205) | 1,452 (1,659) | 1,169 | 931 | 867 (1,114) | 146: 1,006 / 964 |

### Engine fit with the Aeromomentum line

- **Power.** The AM20T at 195 hp assumed continuous replaces a 360 hp TIO-540 cruising at 270 hp. That gives 176-187 KTAS: above the 160 KTAS floor, below the 180 preferred in the low case.
- **Mass and CG.** The installed mass falls by about 207 lb (E), in the nose of a tractor. The headline useful load takes no credit for it.
- **Cooling.** The 301 used a deliberately tiny LoPresti-style low-drag inlet. A radiator needs its own duct, so the cooling-drag allowance here is a placeholder.
- **Altitude.** The 301 was a pressurised design aimed at FL250. Without a critical altitude for the AM20T, pressurisation buys nothing in our check, and its weight is carried for no speed. A revival on this engine might be unpressurised, which changes the structure (stage 4).

### Rights and provenance (stage 2)

Open question (Elon, `docs/rights/mooney-301.md`, PR #3). There is no type certificate. The one airframe (N301MX, registration cancelled 1989) was scrapped: its wings were cut off and the rest went to an A&P school in Abilene, Texas. All M30 engineering data went to Socata at Tarbes in 1987 under a joint venture. Mooney International (successor to the developer) and Daher (successor to the joint-venture partner) may both claim it. The joint-venture terms and the lawsuit settlement are not public, and no court record of the dispute was found. **Unresolved on the public record, and nothing usable survives on either path** (Elon, updated 2026-10-24): no type certificate, no patent (any from the era expired by about 2012), no airframe, and no known drawing set outside whatever Daher kept in Tarbes or Mooney kept in Kerrville. The realistic route is a new design that takes the 301's layout as a reference, with counsel on how close is too close to TBM-protected data.

### Safety record

Record: no NTSB or other accident record; one prototype, about 70 h in 1983, plus Socata data flights. First-hand flight-test account (Bob Kromer, Mooney test pilot, Mooney Flyer, October 2012): with rapid inputs in gusty air on approach, pitch authority became "almost non-existent". He blamed the inverted-section one-piece stabilator and called it "certainly not certifiable"; a conventional tail was recommended and never fitted. Sources disagree on the tail layout (Wikipedia describes a fixed stabilizer with elevators); we kept the test pilot's account. **Inference:** a tail redesign would fix it, but any revival treats the tail as unvalidated. No fleet, no rate.

### Why it died, and whether a revival fixes it

Republic Steel's takeover by LTV forced the sale of Mooney. The new French-led owners judged the 301 about 200 lb heavy and too slow, and wanted a 300 kt turboprop, which became the TBM 700. The market gap it was aimed at, a fast six-seat piston single, is real and is still open. But nothing survives to revive except published dimensions: a revival would be a new design that takes the 301 as its starting point.

### Not yet done

- The attorney question on Mooney or Daher (Elon, then Bill).
- Primary geometry: Jane's 1983-84 and Air International January 1984 were read only as quoted. A library copy would replace our estimated chords and tail areas.
- If it goes forward: what an unpressurised six-seat derivative weighs (MANUFACTURING).
- What a modern rebuild changes in mass, cost and build hours (MANUFACTURING, stage 4, AER-3784).

<!-- stage3:end -->
