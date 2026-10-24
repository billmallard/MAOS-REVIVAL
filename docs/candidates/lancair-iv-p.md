# Lancair IV-P

Stage 1 stub (extended in stage 3 below), generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Lance Neibauer, Lancair |
| Years | IV 1991; IV-P 1994; kits ended 2012 |
| Number built | 110 IV + 250 IV-P flying by 2011 (Kitplanes) |
| Survivors / registered | ~208 IV-P registered (184 with airworthiness date) |
| Seats | 4 |
| Configuration | Low wing, 4 seats, retractable gear, pressurized |
| Construction | Composite |
| Engine | Continental TSIO-550, 350 hp, twin turbo |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 3,550 lb | F | [source](https://lancair.com/storage/2019/10/LA_LancairIV_web_f.pdf) | - |
| Empty weight | 2,200 lb | F | [source](https://lancair.com/storage/2019/10/LA_LancairIV_web_f.pdf) | - |
| Useful load | 1,350 lb | F | [source](https://lancair.com/storage/2019/10/LA_LancairIV_web_f.pdf) | - |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 106.5 US gal | P | [source](https://www.aopa.org/news-and-media/all-news/2005/april/pilot/get-up-and-go) | usable, extended tanks as tested; 82-90 gal standard across sources |
| Published range | 1,347 nm | P | [source](https://www.aopa.org/news-and-media/all-news/2005/april/pilot/get-up-and-go) | 65%, 24,000 ft, 45 min reserve (1,550 sm) |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 255 | 16500 | 75% | 17.2 | P | [source](https://www.aopa.org/news-and-media/all-news/2005/april/pilot/get-up-and-go) | best power |
| 284 M | 24000 | 65% | 17 | P | [source](https://www.aopa.org/news-and-media/all-news/2005/april/pilot/get-up-and-go) | best economy |
| 278 P | 23000 | 75% | 18 | P | [source](https://www.aopa.org/news-and-media/all-news/1994/june/pilot/lancair-iv-p) | 50 F lean of peak; below the factory claim |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: pass**
  - Useful load: 1,350 lb (pass) against 1,000 lb.
  - Range: 1,347 nm (pass; 65%, 24,000 ft, 45 min reserve (1,550 sm)) against 1,000 nm.
  - Cruise: 278 KTAS at 23,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 962 / 881 @ 278 kt, 18.0 gph.
- **Measured or reported: partial: range pass, speed pass**
  - Useful load: - lb (?) against 1,000 lb.
  - Range: 1,779 nm (pass; still air, no reserve, from fuel and measured flow) against 1,000 nm.
  - Cruise: 284 KTAS at 24,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 350 hp (-9% speed, est. 231 KTAS).

Sanity flags:

- published range 1,347 nm vs 1,779 nm from fuel and flow

## Why it died

Kits ended 2012; in 2016 the company sold older lines to concentrate on the Evolution (Wikipedia).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Pressurisation and FL240 cruise in a kit, the fastest piston four-seater of its era (published 287 KTAS at 24,000 ft).
- Re-wing data point to follow (Oregon remanufacturer, Bill): a new wing on the same airframe as the fix for the stall-spin record.

## Rights and provenance (known so far; research, not legal advice)

Neibauer -> Bartels (2003) -> Huffstutlers, Lancair International (2017) -> JetEXE / Lancair Aerospace (2023). Owned by the stage 2 rights research (AER-3787).

## Safety record

NTSB narrative WPR12FA180: 26% of Lancairs in accidents, 19% fatal (model and period not stated); Wanttaja 1998-2007: 32 IV accidents, ~40% fatal.

<!-- stage3:start -->

## Stage 3: shortlist rank 2 of 8 (AER-3783)

Our own check, from published geometry and weights, calibrated against published flight data. Method, calibration and the Aeromomentum assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are research, not legal advice. Nobody has been contacted.

### Verdict

**Rank 2.** It is the strongest airframe that physically survives: 200-211 KTAS on 195 hp and 824 lb over 1,000 nm with reserve in the high case, about 235 aircraft on the register to measure, and parts support still offered. Who could license or sell the design is open: the scope of the 2023 sale is not public and the molds are unlocated. That still leaves it ahead of the Mooney 301, where nothing survives at all, and the VK-30, whose holder is large and firmly set. It ranks below the Defiant for three reasons: the worst fatal record in the survey, a power cut of nearly half its design power, and about 240 lb of nose ballast to find. Its published 278 KTAS reads 8% optimistic against the fleet calibration.

### Independent performance check

Model: `docs/shortlist/check/models/lancair-iv-p.json`; result: `docs/shortlist/check/results/lancair-iv-p.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 228 ft2, Wing 176 ft2, HTail 27 ft2, Fin 18 ft2; total 449 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 30.2 ft, area 98 ft2 (F, factory); RXM5-217 root / NACA 64-212 tip (Lednicer). Taper ratio 0.5 assumed (E): root 4.33 ft, tip 2.16 ft.
- Fuselage 25 ft long (F); max width 4.1 ft (46 in cabin + walls) and height 4.4 ft: E, ours.
- Tails sized by volume coefficient (E, Raymer table 6.4 GA single): horizontal Vh 0.65 -> 15.9 ft2, vertical Vv 0.045 -> 10.2 ft2, arm 13 ft.
- Laminar run x_tr: wing 0.25, tails 0.20, fuselage 0.05.
- Retractable gear, doors closed: no gear term; leakage covered by the 5% excrescence line.
- Turbo TSIO-550 flat-rated to 25,000 ft (E). Cooling factor 1.3 for a twin-turbo intercooled installation (E).
- Published-point weight unstated: 3,200 lb assumed (E).
- Original installed engine mass 633 lb = typical published dry weight x 1.15 for mount, baffles, exhaust and oil cooler (E; per-variant check owed by MANUFACTURING).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 278 | 23,000 | 262 | 18 | P | 281 | +1% | 1.03 | 255 | AOPA Pilot Jun 1994, 75%, lean of peak |

**Drag factor used: 1.29** (fleet calibration (own points read cleaner than the fleet); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.03.

**Drag build-up at 23,000 ft, 262 hp, 3,200 lb, with the factor applied:** 255 KTAS, CD0 0.0228 on S = 98.0 ft2, propeller efficiency 0.83, L/D 11.5.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.654 | Swet 176.0 ft2, Re 5.1M, Cf 0.00254, FF 1.462, Q 1.00, x_tr 0.25 |
| HTail | 0.115 | Swet 26.9 ft2, Re 2.9M, Cf 0.00301, FF 1.354, Q 1.05, x_tr 0.20 |
| Fin | 0.071 | Swet 17.9 ft2, Re 3.9M, Cf 0.00283, FF 1.332, Q 1.05, x_tr 0.20 |
| Fuselage | 0.653 | Swet 228.0 ft2, Re 37.7M, Cf 0.00226, FF 1.265, Q 1.00, x_tr 0.05 |
| cooling | 0.154 | Raymer 12.39 x 1.30 |
| leakage+protuberance | 0.082 | 5% of the rest |
| calibration factor | 0.501 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.414 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 262 hp at 20,000 ft gives 248 KTAS; still-air range on full usable fuel from MTOW 1,058 nm (climb allowance 50 lb); payload at 1,000 nm 855 lb with no reserve, cannot lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -242 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 200 (218) | 1,350 (1,592) | 1,136 | 881 | cannot (1,094) | 161: 962 / 920 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 211 (231) | 1,350 (1,592) | 1,155 | 888 | 824 (1,100) | 164: 953 / 911 |

### Engine fit with the Aeromomentum line

- **Power.** The AM20T (260 hp take-off, 195 hp assumed continuous) replaces a 350 hp TSIO-550 that cruises at 262 hp. Our check gives 200 KTAS at 8,000 ft (low case) and 211 KTAS at 16,000 ft (high case), against 255 KTAS at FL230 on the original engine at our fleet calibration. Without a real critical altitude for the AM20T, no FL200+ credit is taken.
- **Mass and CG.** The installed mass falls by about 242 lb (E). That weight is in the nose of a tractor with a 36 lb/ft2 wing loading, so it has to come back as ballast or as a longer engine mount. The headline useful load (1,350 lb) takes no credit for the saving; the 1,592 lb optimistic figure takes all of it. Neither has been checked against a real weight-and-balance.
- **Climb.** At 3,550 lb, about 195 hp continuous is roughly 55% of the power the airframe was designed around. Climb rate and high-density-altitude take-off will fall by much more than cruise speed. That is not computed here, but a revival has to quantify it.
- **Cooling and installation.** A liquid-cooled engine and radiator replace an intercooled twin-turbo air-cooled installation that already ran hot in climb (Kitplanes 2019). The cowl is built around a flat six; a new nose is a stage 4 item.

### Rights and provenance (stage 2)

Open question: chain of title (Elon, `docs/rights/lancair-iv-p.md`, PR #3, updated 2026-10-24). In February 2017 Lancair International Inc. sold all out-of-production kit lines, including the IV and IV-P, "with all assets, intellectual designs, and ongoing support business" to Lancair International LLC (Uvalde, TX). In October 2023 JetEXE Aviation (Sacramento) bought the Lancair kit business from the Uvalde owners. **No public source lists what that purchase covered** (an earlier version of this dossier repeated a misquotation saying it included molds and IP; it did not, and is withdrawn). The Texas LLC is still active, so whether JetEXE or the LLC holds the IV-P design is open. The molds have no known location since Uvalde in 2017. Owner-forum posts (low grade) report a legal dispute between the parties and call Lancair "effectively defunct" as of April 2026; no federal case was found, and Texas state courts were not searched. The company trades as Lancair Aerospace, says the IV-P kit is out of production, and offers parts and service bulletins. "LANCAIR" is a live mark held jointly by JetEXE and Akyna Medical Management. Lancair has licensed a design before (the Calima T-90). So it remains a licence-or-purchase candidate, but **chain of title comes before price**, and an attorney is needed for it. Approaching anyone is Bill's call.

### Safety record

Record (NTSB bulk databases, our own count of IV-family model strings, 1995-2026): 88 accidents, 43 fatal (49%), 79 killed, on about 360 completed aircraft. Fatal accidents fell from 19 in 2008-2016 to 3 in 2017-2026, which is consistent with the owners' group training push. The NTSB causes in the fatal accidents fall into two big groups. About 13 are low-altitude loss of airspeed or stall-spin on take-off, climb-out, go-around or manoeuvring. About 13 more begin with an engine power loss, often followed by a stall. Weather with structural overload accounts for about 7. **Inference, labelled as such:** the stall-spin group is consistent with a high wing loading and a small wing with a 66 KIAS stall (CAFE). Lower power does not change that, and lower power makes a go-around weaker.

### Why it died, and whether a revival fixes it

Kit production ended in 2012, and the company sold its older lines in 2016-17 to concentrate on newer designs. That was not a market failure; about 360 were built. A revival therefore does not fix a cause of death. What it would have to fix is the accident pattern, through the wing (the 2019 RDD LX7 rework already offers a new airfoil with double-slotted flaps on the same area), training, and the engine-failure chain.

### Not yet done

- Chain of title: what JetEXE bought in 2023, whether the Texas LLC still holds the IV-P design, and where the molds are (Elon, then an attorney; contact is Bill's call).
- If it goes forward: a SAFETY review of the stall-spin pattern, asked on AER-3785 first.
- A climb and take-off check at 195 hp, and a weight-and-balance with the lighter engine (AERO).
- Builder-fleet empty weight: two weighed aircraft (2,140 and 2,200 lb) are all we have.
- What a modern rebuild changes in mass, cost and build hours (MANUFACTURING, stage 4, AER-3784).

<!-- stage3:end -->
