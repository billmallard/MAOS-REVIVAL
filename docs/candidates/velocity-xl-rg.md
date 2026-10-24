# Velocity XL-RG

Stage 1 stub (extended in stage 3 below), generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Danny Maher, Velocity Inc. |
| Years | XL from late 1990s; alive |
| Number built | 229 XLs flown by Dec 2011 (150 XL-RG) |
| Survivors / registered | not counted |
| Seats | 4 |
| Configuration | Canard pusher, 4-5 seats, gull-wing doors, retractable gear |
| Construction | Composite |
| Engine | Lycoming IO-540 260 hp, or Continental IO-550 310 hp; TSIO-550 on XL-5 |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,800 lb | F | [source](https://www.velocityaircraft.com/xl) | 2,750-2,800 by engine |
| Empty weight | 1,700 lb | F | [source](https://www.aircraftspruce.com/catalog/kitspages/velocity2.php) | - |
| Useful load | 1,100 lb | F | [source](https://www.aircraftspruce.com/catalog/kitspages/velocity2.php) | derived |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 70 US gal | F | [source](https://www.velocityaircraft.com/xl) | - |
| Optional fuel | 100 US gal | F | [source](https://www.aircraftspruce.com/catalog/kitspages/velocity2.php) | - |
| Published range | 1,150 nm | F | [source](https://www.velocityaircraft.com/xl) | 65% power, reserve not stated (1,100-1,200) |

Cruise settings (the starred row is the one screened for speed):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 190 * | 3000 | 75% | 15 | P | [source](https://generalaviationnews.com/2005/03/25/velocity-xl-5/) | XL-5 RG, IO-550 310 hp, 24 in/2,400 rpm |
| 205 | - | 75% | - | F | [source](https://www.velocityaircraft.com/xl) | upper end of 190-205 kt by engine |
| 170 | - | - | 11 | F | [source](https://www.velocityaircraft.com/xl) | 'over 170 kts at 11 GPH', XL-FG |

## Screen (stage 1, published numbers)

- **Verdict: pass, speed unconditioned**
- Useful load: 1,100 lb (pass) against 1,000 lb.
- Range: 1,082 nm still-air (pass; basis: calc) against 1,000 nm.
- Cruise: 190 KTAS at 3,000 ft (pass+) against >160 KTAS (>180 preferred).
- Payload at 1,000 nm: 712 lb with no reserve; not possible (tanks too small) with a 45 min reserve. Setting: 170 KTAS at 11.0 gph.
- Aeromomentum fit (first cut): Yes for the IO-540 260 hp build (AM20T 260 hp); short for IO-550 310 hp builds (-6% speed est.).

Sanity flags:

- screen speed has no altitude, or is below 6,000 ft
- with optional tanks (100 gal) still-air range is 1,545 nm

## Why it died

Not dead. Kits and a factory transition course are still offered (Kitplanes).

## Rights and provenance (known so far; research, not legal advice)

Maher -> Scott and Duane Swing (1992) -> Rocket Racing (2008) -> Swing family again (2010). Owned by the stage 2 rights research (AER-3787).

## Safety record

Late-1980s deep-stall accidents in the original Velocity, addressed with leading-edge cuffs; residual 'pitch buck' needs training (Kitplanes 2020).

<!-- stage3:start -->

## Stage 3: shortlist rank 5 of 8 (AER-3783)

Our own check, from published geometry and weights, calibrated against published flight data. Method, calibration and the Aeromomentum assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are research, not legal advice. Nobody has been contacted.

### Verdict

**Rank 5.** It is a live kit with a near Aeromomentum fit, but it reaches 1,000 nm only on optional tanks, and then with 440-457 lb of payload. Its published speed needs a 1.63 drag factor, but that rests on one point and on geometry we had to scale from the Cozy; the factory's own wing figures conflict with Jane's. Low confidence in both directions.

### Independent performance check

Model: `docs/shortlist/check/models/velocity-xl-rg.json`; result: `docs/shortlist/check/results/velocity-xl-rg.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 181 ft2, Wing 130 ft2, Strake 102 ft2, Canard 43 ft2, Winglets 25 ft2; total 482 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 34 ft, area 132.5 ft2 incl. strakes (F, factory; Jane's 2013-14 gives 31 ft / 102 ft2, which matches the smaller SE: unresolved). Panels and strakes scaled from the CAFE-measured Cozy by span ratio 1.21 (E).
- Canard 18.67 ft span, 22.8 ft2 (F). Winglets 2 x 12 ft2 (E).
- Fuselage 20 ft (F); width 4.2 ft (47.5 in cabin), height 4.3 ft: E.
- Laminar run as the Cozy. Retractable gear: no gear term. Canard carries 20% of the lift (E).
- Prop 74 in 3-blade constant speed (E; diameter not found). Published-point weight unstated: 2,600 lb assumed (E).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 190 | 3,000 | 232 | 15 | P | 227 | +20% | 1.63 | 142 | GA News 2005 pilot report, factory demonstrator, 75% of 310 hp |

**Drag factor used: 1.63** (own published points; fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.29.

**Drag build-up at 3,000 ft, 232 hp, 2,600 lb, with the factor applied:** 190 KTAS, CD0 0.0211 on S = 132.5 ft2, propeller efficiency 0.83, L/D 7.9.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.384 | Swet 129.6 ft2, Re 6.3M, Cf 0.00218, FF 1.358, Q 1.00, x_tr 0.35 |
| Strake | 0.321 | Swet 102.4 ft2, Re 11.4M, Cf 0.00233, FF 1.279, Q 1.05, x_tr 0.20 |
| Canard | 0.189 | Swet 43.3 ft2, Re 2.3M, Cf 0.00271, FF 1.610, Q 1.00, x_tr 0.35 |
| Winglets | 0.088 | Swet 25.1 ft2, Re 4.4M, Cf 0.00264, FF 1.262, Q 1.05, x_tr 0.25 |
| Fuselage | 0.546 | Swet 181.4 ft2, Re 37.9M, Cf 0.00215, FF 1.402, Q 1.00, x_tr 0.10 |
| cooling | 0.100 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.081 | 5% of the rest |
| calibration factor | 1.083 | x1.633 on the build-up (calibration; basis stated above) |
| induced | 0.160 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 210 hp at 8,000 ft gives 191 KTAS; still-air range on full usable fuel from MTOW 788 nm (climb allowance 24 lb); payload at 1,000 nm cannot lb with no reserve, cannot lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -104 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 186 (203) | 1,000 (1,104) | 825 | cannot | cannot (cannot) | 157: 613 / cannot |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 199 (217) | 1,000 (1,104) | 860 | cannot | cannot (cannot) | 167: 620 / cannot |

### Independent performance check (optional 100 gal tanks)

Model: `docs/shortlist/check/models/velocity-xl-rg-100gal.json`; result: `docs/shortlist/check/results/velocity-xl-rg-100gal.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 181 ft2, Wing 130 ft2, Strake 102 ft2, Canard 43 ft2, Winglets 25 ft2; total 482 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 34 ft, area 132.5 ft2 incl. strakes (F, factory; Jane's 2013-14 gives 31 ft / 102 ft2, which matches the smaller SE: unresolved). Panels and strakes scaled from the CAFE-measured Cozy by span ratio 1.21 (E).
- Canard 18.67 ft span, 22.8 ft2 (F). Winglets 2 x 12 ft2 (E).
- Fuselage 20 ft (F); width 4.2 ft (47.5 in cabin), height 4.3 ft: E.
- Laminar run as the Cozy. Retractable gear: no gear term. Canard carries 20% of the lift (E).
- Prop 74 in 3-blade constant speed (E; diameter not found). Published-point weight unstated: 2,600 lb assumed (E).
- Variant: optional tanks, 100 gal usable (stage 1, factory option); weights unchanged.

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 190 | 3,000 | 232 | 15 | P | 227 | +20% | 1.63 | 142 | GA News 2005 pilot report, factory demonstrator, 75% of 310 hp |

**Drag factor used: 1.63** (own published points; fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.29.

**Drag build-up at 3,000 ft, 232 hp, 2,600 lb, with the factor applied:** 190 KTAS, CD0 0.0211 on S = 132.5 ft2, propeller efficiency 0.83, L/D 7.9.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.384 | Swet 129.6 ft2, Re 6.3M, Cf 0.00218, FF 1.358, Q 1.00, x_tr 0.35 |
| Strake | 0.321 | Swet 102.4 ft2, Re 11.4M, Cf 0.00233, FF 1.279, Q 1.05, x_tr 0.20 |
| Canard | 0.189 | Swet 43.3 ft2, Re 2.3M, Cf 0.00271, FF 1.610, Q 1.00, x_tr 0.35 |
| Winglets | 0.088 | Swet 25.1 ft2, Re 4.4M, Cf 0.00264, FF 1.262, Q 1.05, x_tr 0.25 |
| Fuselage | 0.546 | Swet 181.4 ft2, Re 37.9M, Cf 0.00215, FF 1.402, Q 1.00, x_tr 0.10 |
| cooling | 0.100 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.081 | 5% of the rest |
| calibration factor | 1.083 | x1.633 on the build-up (calibration; basis stated above) |
| induced | 0.160 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 210 hp at 8,000 ft gives 191 KTAS; still-air range on full usable fuel from MTOW 1,157 nm (climb allowance 24 lb); payload at 1,000 nm 483 lb with no reserve, 413 lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -104 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 186 (203) | 1,000 (1,104) | 1,213 | 505 | 440 (583) | 157: 613 / 571 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 199 (217) | 1,000 (1,104) | 1,275 | 522 | 457 (597) | 167: 620 / 578 |

### Engine fit with the Aeromomentum line

- **Power.** The AM20T at 195 hp assumed continuous replaces a 260-310 hp IO-540 or IO-550 (stage 1 matched the 260 hp build). That gives 186-199 KTAS.
- **Mass and CG.** The installed mass falls by about 104 lb against an IO-550 (E). That is a tail-mounted engine on a canard, where CG range is critical; the headline useful load (1,000 lb) takes no credit for the saving.
- **Fuel.** On the standard 70 gal it cannot fly 1,000 nm at continuous power, even with no reserve. With the factory's optional 100 gal it carries 440-457 lb with a reserve. Every pass here assumes the optional tanks.
- **Cooling.** The radiator has to fit a pusher cowl that already has inlets sized for a flat six; not studied.

### Rights and provenance (stage 2)

Firmly held (Elon, `docs/rights/velocity-xl-rg.md`, PR #3): not an orphan. Velocity, Inc. (Sebastian, FL; the Swing family since 1992, apart from 2008-2010) still sells the XL in fixed and retractable forms, holds the molds and supports the fleet. About 700 Velocities fly, and the factory makes 12-15 kits a year (Kitplanes 2020). No live VELOCITY aircraft mark was found. Nothing here is free to take; an Aeromomentum-engined XL would be a partnership with a live company.

### Safety record

Record (NTSB CAROL, XL-family model strings): 26 events, 5 fatal, 9 killed, on about 229 completed aircraft. The causes are mostly landing-phase control and gear-up or collapsed-gear landings, fuel, engine maintenance, weather and one runway collision. Two items are tied to the configuration. An unlatched passenger door separated and struck the rear engine and prop, killing two (WPR10LA381). And the NTSB found inadequate manufacturer design of the winglet-rudder assembly and its metal-to-composite bond, which caused control-surface flutter (ATL01LA029, non-fatal). One XL-RG departed controlled flight during a self-planned stall test, cause undetermined.

### Why it died, and whether a revival fixes it

It did not die. It is in production. So no revival is needed, and none fixes anything.

### Not yet done

- Resolve the XL wing and canard dimensions (factory 34 ft / 132.5 ft2 against Jane's 31 ft / 102 ft2).
- A measured cruise point at altitude would replace the single 3,000 ft pilot-report point.
- What a modern rebuild changes in mass, cost and build hours (MANUFACTURING, stage 4, AER-3784).

<!-- stage3:end -->
