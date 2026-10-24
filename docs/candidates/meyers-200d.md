# Meyers 200D / Aero Commander 200D

Stage 1 stub (extended in stage 3 below), generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | certified, out of production |
| Designer / maker | Al Meyers; Aero Commander (Rockwell-Standard) |
| Years | 1965-67/68 |
| Number built | ~95-127 (sources conflict) |
| Survivors / registered | 58 200D registered (84 all 200 series) |
| Seats | 4 |
| Configuration | Low wing, 4 seats, retractable gear |
| Construction | Steel-tube cabin cage, metal semimonocoque |
| Engine | Continental IO-520-A, 285 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 3,000 lb | T | [source](http://rgl.faa.gov/Regulatory_and_Guidance_Library/rgMakeModel.nsf/0/ab97f6c31ea6d73786257d2a0052b9e6/$FILE/3A18_Rev_19.pdf) | - |
| Empty weight | 1,940 lb | F | [source](https://avweb.com/?p=124801) | - |
| Useful load | 1,060 lb | F | [source](https://avweb.com/?p=124801) | derived |
| Useful load, fleet or as-weighed | 900 lb | B | [source](https://avweb.com/?p=124801) | ~2,100 lb real-world equipped empty |
| Usable fuel | 74 US gal | T | [source](http://rgl.faa.gov/Regulatory_and_Guidance_Library/rgMakeModel.nsf/0/ab97f6c31ea6d73786257d2a0052b9e6/$FILE/3A18_Rev_19.pdf) | incl. auxiliaries |
| Published range | 782 nm | F | [source](https://en.wikipedia.org/wiki/Meyers_200) | normal fuel, 45 min reserve |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 182 P | - | - | - | F | [source](https://en.wikipedia.org/wiki/Meyers_200) | max cruise (Jane's), 210 mph converted |
| 187 M | - | - | 12 | P | [source](https://planeandpilotmag.com/aero-commander-200/) | weak source; misnames the engine |
| 152 | - | - | 15.5 | P | [source](https://avweb.com/?p=124801) | owner, 23 in / 2,300 rpm, rich of peak |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: fail** - range -218 nm
  - Useful load: 1,060 lb (pass) against 1,000 lb.
  - Range: 782 nm (fail; normal fuel, 45 min reserve) against 1,000 nm.
  - Cruise: 182 KTAS at an unstated altitude (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- **Measured or reported: near miss, speed unconditioned** - UL -100 lb
  - Useful load: 900 lb (near) against 1,000 lb.
  - Range: 1,153 nm (pass; still air, no reserve, from fuel and measured flow at 187 KTAS) against 1,000 nm.
  - Cruise: 187 KTAS at an unstated altitude (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 515 / 461 @ 187 kt, 12.0 gph.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 285 hp (-3% speed, est. 177 KTAS).

Sanity flags:

- published range 782 nm vs 1,153 nm from fuel and flow
- screen speed has no altitude, or is below 6,000 ft
- fleet useful load 160 lb below factory
- the 187 kt / 12 gph pair comes from a weak source; at the owner's 15.5 gph the still-air range is ~730 nm

## Why it died

Hand-built with minimal tooling; after 75 Aero Commander 200Ds, 'it took $4 million to produce $3 million worth' (Plane & Pilot, Jan/Feb 2024, https://planeandpilotmag.com/this-incredible-plane-meyers-aero-commander-200/; the first version of this row cited the 2009 directory page, which does not contain it).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Steel-tube cabin cage inside a metal semimonocoque: crash protection and a reputation for strength and fine handling.
- Lesson: hand-built at a loss ($4M to make $3M of airplanes); a re-derivation must design for cheap production from the start.

## Rights and provenance (known so far; research, not legal advice)

TCDS 3A18 holder: Interceptor Aviation Inc., Bethany OK (2014; GlobalParts affiliate). Owned by the stage 2 rights research (AER-3787).

## Safety record

20 accidents in 35 years; 5 tank-run-dry, 9 maintenance; no in-flight breakups (AvWeb).

<!-- stage3:start -->

## Stage 3: shortlist rank 4 of 5 (AER-3783)

Our own check, from published geometry and weights, calibrated against published flight data. Method, calibration and the Aeromomentum assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are research, not legal advice. Nobody has been contacted.

### Bill's call

Bill, 2026-10-24: "Interesting to me." He can't afford the rights and is "not sure it's necessary": re-deriving may do. "That's a big plane too." Shortlisted, with the idea ledger and a re-derivation path ahead of the rights.

### Verdict

**Rank 4.** As published it fails range (782 nm on normal fuel with a 45-minute reserve) and passes useful load (1,060 lb) and speed (182 KTAS at 75%, altitude not stated). As measured it is a near miss: about 900 lb useful at the fleet-typical 2,100 lb empty, and 178 KTAS at 8,500 ft on about 67% (AOPA 1991). Our check needs a drag factor of 1.41 to match AOPA's point, just above the fleet band, which fits a 1960s riveted airframe with the skin waviness and protrusions Davisson noted; it gives 857 nm still air on 74 gal at 65% and 8,000 ft. On an AM20T: 178-189 KTAS, 831-863 nm on full fuel. So the speed is there and the range and empty weight are not, and both are what a re-derivation would fix: more fuel in the wing and a lighter structure. It ranks below the Express because a re-derivation is a new airplane, and above the 301 because a holder, a type certificate, drawings and 58 registered aircraft exist.

### Idea ledger (what a new airplane should keep)

- A welded 4130 steel-tube cage from the firewall to the rear cabin and out to the main-gear points, skinned in aluminium: crash protection and one load path for engine, wing centre section and gear. No airframe ADs or in-flight breakups on record.
- Speed on modest power: 177-178 KTAS measured on 67-75% of 285 hp, from a 161.5 ft2 wing with a NACA 230-series root, strong washout and Fowler flaps (benign stall with aileron authority; a low landing speed).
- High gear and flap speeds, and a gear-flap interconnect, that make slowing down and configuring easy.
- Drop: the four-tank, one-gauge fuel system (ten of its 26 accidents are fuel starvation), no rudder trim or thrust offset, and heavy controls.
- Lesson: hand-built at a loss ($4 million to make $3 million of airplanes, Plane & Pilot 2024); a re-derivation must design for cheap production from the start.

### Published, measured and our check, side by side

Read across a row only within one column's basis. The three targets are separate floors.

| | As published | Measured or reported | Our check, original engine |
|---|---|---|---|
| Useful load | 1,060 lb (pass) | 900 lb (near) | 1,060 lb (the empty weight the model uses: 1,940 lb) |
| Range | 782 nm (fail; normal fuel, 45 min reserve) | 1,153 nm (pass; still air, no reserve, from fuel and measured flow at 187 KTAS) | 857 nm, still air, no reserve, full fuel from MTOW, at 185 hp and 8,000 ft |
| Cruise | 182 KTAS at altitude not stated (pass+) | 187 KTAS at altitude not stated (pass+) | 174 KTAS at 185 hp and 8,000 ft |
| Screen | fail | near miss, speed unconditioned | see the verdict |

### Independent performance check

Model: `docs/shortlist/check/models/meyers-200d.json`; result: `docs/shortlist/check/results/meyers-200d.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 199 ft2, Wing 298 ft2, HTail 54 ft2, Fin 25 ft2; total 577 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 30.5 ft, area 161.5 ft2 (F, Jane's 1967-68; Davisson 1975). Chords not published: taper 0.5 assumed, giving root 7.06 ft and tip 3.53 ft (E, ours). NACA 23015 root, 4412 tip (Lednicer): t/c 15% / 12%.
- Fuselage length 24.33 ft (F); max width 3.8 ft and height 4.2 ft (E, ours; no cabin dimensions published). Davisson notes skin waviness over the tube cage, protruding screws and a belly air dump: Q 1.05 on the fuselage (E).
- Horizontal tail 30 ft2 (10.5 ft x 2.85 ft) and fin 14 ft2: E, ours, by volume coefficient (Vh about 0.55, Vv 0.04, tail arm 13 ft). No tail dimensions are published.
- Laminar run x_tr: wing 0.15 (NACA 230/44-series on a riveted metal wing, flush riveted on the 200D), tails 0.10, fuselage 0.05.
- Retractable gear with doors: no fixed gear drag.
- Air-cooled IO-520 with conventional nose inlets: cooling factor 1.0.
- Original installed engine mass 480 lb = IO-520 dry about 415 lb x 1.15 (E, ours).
- Published point: AOPA Pilot Dec 1991, N31CC, 178 KTAS at 8,500 ft, full throttle 21.5 in / 2,400 rpm, about 67% (191 hp), 14 gph, two aboard; weight not stated, 2,650 lb assumed (E: fleet-typical 2,100 lb empty + two aboard + most of the fuel).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 178 | 8,500 | 191 | 14 | P | 202 | +13% | 1.41 | 140 | AOPA Pilot Dec 1991 (N31CC, 200D): 21.5 in full throttle / 2,400 rpm, about 67%, two aboard; weight E |

**Drag factor used: 1.41** (own published points; fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.29.

**Drag build-up at 8,500 ft, 191 hp, 2,650 lb, with the factor applied:** 178 KTAS, CD0 0.0192 on S = 161.5 ft2, propeller efficiency 0.83, L/D 9.1.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 1.075 | Swet 298.4 ft2, Re 8.5M, Cf 0.00260, FF 1.386, Q 1.00, x_tr 0.15 |
| HTail | 0.226 | Swet 54.1 ft2, Re 4.4M, Cf 0.00309, FF 1.287, Q 1.05, x_tr 0.10 |
| Fin | 0.098 | Swet 25.0 ft2, Re 5.3M, Cf 0.00299, FF 1.252, Q 1.05, x_tr 0.10 |
| Fuselage | 0.597 | Swet 199.5 ft2, Re 37.7M, Cf 0.00228, FF 1.249, Q 1.05, x_tr 0.05 |
| cooling | 0.096 | Raymer 12.39 x 1.00 |
| leakage+protuberance | 0.105 | 5% of the rest |
| calibration factor | 0.898 | x1.409 on the build-up (calibration; basis stated above) |
| induced | 0.398 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 185 hp at 8,000 ft gives 174 KTAS; still-air range on full usable fuel from MTOW 857 nm (climb allowance 25 lb); payload at 1,000 nm cannot lb with no reserve, cannot lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -89 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 178 (184) | 1,060 (1,149) | 831 | cannot | cannot (cannot) | 148: 648 / cannot |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 189 (196) | 1,060 (1,149) | 863 | cannot | cannot (cannot) | 155: 652 / cannot |

### Engine fit with the Aeromomentum line

- **Power.** The AM20T at 195 hp assumed continuous replaces a 285 hp IO-520 cruising at 185-214 hp. That gives 178 KTAS at 8,000 ft and 189 KTAS at 16,000 ft.
- **Mass and CG.** The installed mass falls by about 89 lb (E), in the nose of a short tractor; ballast or a longer mount takes it back. The headline useful load takes no credit for the saving.
- **Cooling.** A radiator in place of conventional nose inlets: not designed.
- **Fuel.** 74 gal usable is the constraint: 831-863 nm at continuous power. A re-derived wing with about 100 gal closes the floor (E).

### Rights and provenance (stage 2)

Small holder, live type certificate (Elon, `docs/rights/meyers-200d.md`, PR #3). TCDS 3A18 (Models 200-200D and the Interceptor 400) is Current, Rev 19 (2014), held by Interceptor Aviation Inc.; there is no production certificate. The TC, drawings, jigs and tooling were offered for sale through a broker in October 2019, with no sale found; the parent, GlobalParts Group, was bought by VSE Corporation in 2021, and whether Interceptor Aviation went with it is unknown. Bill's question is whether the rights are needed at all for a re-derivation: what the public record supports (published dimensions, the TCDS, the steel-tube-cage concept) and where an attorney is needed is with Elon on AER-3805.

### Safety record

Record (our count from the NTSB bulk databases, 1982-2024): 26 accidents, 6 fatal (8 killed), on about 130 built and 58 registered. Ten accidents are fuel starvation, mostly from the four-tank, one-gauge fuel system: a systems flaw a re-derivation drops. The fatal accidents are mixed (fuel starvation, low passes with alcohol, low-altitude manoeuvring, a misinstalled intake screen, a gusty-crosswind take-off). No in-flight breakup. No pattern tied to the configuration was found.

### Why it died, and whether a revival fixes it

Commercial, not technical. Meyers hand-built each aircraft with minimal tooling; Aero Commander bought the design in 1965 and found it took $4 million to make $3 million of airplanes. It was priced near a V-tail Bonanza and carried less, and its 3,000 lb gross was never raised. A re-derivation designed for production, with more gross weight and fuel, addresses all three.

### Not yet done

- The re-derivation question: what the public record supports and where an attorney is needed (Elon, AER-3805).
- Chords, tail areas and a three-view: none are published; the model here assumes taper 0.5 and sizes the tail by volume coefficient.
- A re-derivation sketch at about 3,300 lb gross with 100 gal, on an AM20T (AERO, if it goes forward).
- What a modern rebuild changes in mass, cost and build hours (MANUFACTURING, stage 4, AER-3784).

<!-- stage3:end -->

<!-- stage4:start -->

## Stage 4: what modern manufacturing changes (AER-3784)

Note (rank 4; a re-derivation). Method, prices and sources are in [docs/MANUFACTURING.md](../MANUFACTURING.md); the weight table is generated by `docs/manufacturing/weights.py`. Desk study: nothing weighed or quoted by us, nobody contacted. Every E is our estimate.

**Original construction:** a welded 4130 steel-tube cabin cage inside an aluminium semimonocoque, hand-built with minimal tooling ($4 million to make $3 million of airplanes).

**Modern route:** keep the cage. Tubes and gussets are cut by a tube-laser service (quote-only, not contacted), fitted in a welding jig and welded, then skinned in matched-hole aluminium. The four-tank, one-gauge fuel system becomes two integral wing tanks of about 100 gal. Tooling is low: a welding jig and form blocks, $30-90k (E).

**Empty weight:** re-derived at the original 3,000 lb gross, **1,840-2,160 lb**, useful load **840-1,160 lb** (published: 1,060). With our engine credit (-133 to -105 lb; IO-520-A 431 lb per TCDS E5CE, not 415): 1,710-2,060 lb. A re-derivation at about 3,300 lb gross needs STRUCTURES if it goes forward.

**Skill floor:** set by the welding. The cage is primary structure, so either the builder is a qualified welder or the cage comes welded from a shop. The skins are Van's-level riveting.

**Weight build-up:**

| Item | Light, lb | Heavy, lb | Basis | Grade |
|---|---|---|---|---|
| Starting empty weight | 1,940 | 2,100 | 1,940 (F, AvWeb); about 2,100 equipped real-world empty (B, AvWeb owner data) | F/B |
| Structure re-derived for production: laser-cut tube cage and gussets, jig-welded; matched-hole skins over it | -50 | +30 | Hand-built 1960s structure with skin waviness and protruding screws (Davisson); CAD sizing against production allowances | E |
| Fuel: four tanks and one gauge -> two integral wing tanks of about 100 gal total | +10 | +25 | Larger tanks, ribs and sealant; the old tanks and selector come out | E |
| Panel: 1960s avionics -> EFIS | -50 | -20 | 1960s IFR panel | E |
| EFI engine: backup battery and bus | +5 | +10 | One ECU | E |
| New nose: cowl and radiator duct | -10 | +15 | Conventional nose inlets today | E |
| **Rebuild empty weight, no engine credit** | **1,840** | **2,160** | sum, rounded to 10 lb | E |

<!-- stage4:end -->
