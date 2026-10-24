# Cirrus VK-30

Stage 1 stub (extended in stage 3 below), generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Alan and Dale Klapmeier, Jeff Viken, Cirrus Design |
| Years | 1988 first flight; kits 1988-93 |
| Number built | ~40 kits delivered; ~13 completed |
| Survivors / registered | 4 FAA-registered (2018, peak 12) |
| Seats | 5 |
| Configuration | Mid-engine pusher with extension shaft, 4-5 seats, retractable gear, laminar wing |
| Construction | Composite |
| Engine | Continental IO-550 300 hp or Lycoming IO-540 290 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 3,550 lb | F | [source](https://aeroresourcesinc.com/uploads/199004-1990%20Cirrus%20VK30%20Homebuilt.pdf) | AOPA Pilot spec box; EAA museum gives 3,600 |
| Empty weight | 2,200 lb | F | [source](https://aeroresourcesinc.com/uploads/199004-1990%20Cirrus%20VK30%20Homebuilt.pdf) | prototype; EAA museum gives 2,400 |
| Useful load | 1,350 lb | F | [source](https://aeroresourcesinc.com/uploads/199004-1990%20Cirrus%20VK30%20Homebuilt.pdf) | - |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 95 US gal | F | [source](https://aeroresourcesinc.com/uploads/199004-1990%20Cirrus%20VK30%20Homebuilt.pdf) | - |
| Published range | 1,130 nm | F | [source](https://www.eaa.org/eaa-museum/museum-collection/aircraft-collection-folder/1991-cirrus-vk-30---n33vk) | not stated (1,300 mi converted) |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 205 M | 4500 | 70% | 15.5 | P | [source](https://aeroresourcesinc.com/uploads/199004-1990%20Cirrus%20VK30%20Homebuilt.pdf) | prototype measured, AOPA Pilot Apr 1990 |
| 211 P | 5000 | 75% | 16.7 | F | [source](https://aeroresourcesinc.com/uploads/199004-1990%20Cirrus%20VK30%20Homebuilt.pdf) | manufacturer's calculation |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: pass, speed unconditioned**
  - Useful load: 1,350 lb (pass) against 1,000 lb.
  - Range: 1,130 nm (pass; not stated (1,300 mi converted)) against 1,000 nm.
  - Cruise: 211 KTAS at 5,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 875 / 800 @ 211 kt, 16.7 gph.
- **Measured or reported: partial: range pass, speed pass, speed unconditioned**
  - Useful load: - lb (?) against 1,000 lb.
  - Range: 1,256 nm (pass; still air, no reserve, from fuel and measured flow at 205 KTAS) against 1,000 nm.
  - Cruise: 205 KTAS at 4,500 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 290 hp (-4% speed, est. 198 KTAS).

Sanity flags:

- screen speed has no altitude, or is below 6,000 ft

## Why it died

Discontinued 1993 as Cirrus moved to certified aircraft; replacement wing announced 1996 for ~28 kits (Wikipedia).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- A laminar-flow composite wing and a clean pusher fuselage that reached about 200 KTAS on 290-300 hp, the design the Cirrus team learned on before the SR20.
- Lesson: its long shaft drive, cruise-flap flutter and aft-CG spin recovery are what a pusher with a buried engine must design out.

## Rights and provenance (known so far; research, not legal advice)

Cirrus Design, now Cirrus Aircraft. No support program found. Owned by the stage 2 rights research (AER-3787).

## Safety record

7 US crashes, 10 fatalities 1990-2020 (NTSB via Wikipedia), incl. a 1996 stall-test crash in a turbine conversion; prop-governor oil line chafe forced landing on the prototype.

<!-- stage3:start -->

## Stage 3: checked, then dropped from the shortlist by Bill (2026-10-24)

Our own check, from published geometry and weights, calibrated against published flight data. Method, calibration and the Aeromomentum assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are research, not legal advice. Nobody has been contacted.

### Bill's call

Bill, 2026-10-24: "no thanks". Dropped from the shortlist; the long-list row stays.

### Verdict (stage 3, before Bill's review)

**Rank 4.** It has the fastest result on our numbers (199-212 KTAS, 815-825 lb over 1,000 nm with reserve). It ranks fourth because the holder is a large, state-controlled company to which it is history, and because its accident record is tied to the very features (shaft drive, flap, spin) a revival would inherit.

### Idea ledger (what a new airplane should keep)

- A laminar composite wing on a clean pusher fuselage: the fastest result on our check (199-212 KTAS on an assumed 195 hp).
- Lesson for any buried-engine pusher, the Rohr 2-175 included: three of its five fatal accidents trace to the shaft drive, a flutter-prone cruise flap and spin recovery at aft CG. A shaft and its couplings must be designed and tested as primary structure.

### Published, measured and our check, side by side

Read across a row only within one column's basis. The three targets are separate floors.

| | As published | Measured or reported | Our check, original engine |
|---|---|---|---|
| Useful load | 1,350 lb (pass) | not found | 1,350 lb (the empty weight the model uses: 2,200 lb) |
| Range | 1,130 nm (pass; not stated (1,300 mi converted)) | 1,256 nm (pass; still air, no reserve, from fuel and measured flow) | 1,206 nm, still air, no reserve, full fuel from MTOW, at 200 hp and 8,000 ft |
| Cruise | 211 KTAS at 5,000 ft (pass+) | 205 KTAS at 4,500 ft (pass+) | 201 KTAS at 200 hp and 8,000 ft |
| Screen | pass, speed unconditioned | partial: range pass, speed pass, speed unconditioned | see the verdict |

### Independent performance check

Model: `docs/shortlist/check/models/cirrus-vk-30.json`; result: `docs/shortlist/check/results/cirrus-vk-30.json`. Method in [SHORTLIST.md](../SHORTLIST.md#method).

**Wetted areas (OpenVSP CompGeom, parametric model from published dimensions):** Fuselage 239 ft2, Wing 215 ft2, HTail 33 ft2, Fin 27 ft2; total 514 ft2.

**Model assumptions** (grade E unless a source is named):

- Wing span 38.66 ft, area 120 ft2 (P, AOPA Pilot Apr 1990); NLF(1)-0414F, 14% t/c. Taper 0.5 assumed (E): root 4.14 ft, tip 2.07 ft.
- Fuselage 26 ft (P); max width 4.3 ft (4 ft cabin + walls) and height 4.5 ft: E, ours. Engine buried; prop at tail cone.
- Tails sized by volume coefficient (E): horizontal Vh 0.60 -> 18.6 ft2, vertical (upper + ventral) Vv 0.04 -> 15.5 ft2, arm 12 ft.
- Laminar run x_tr: wing 0.35 (NLF section, builder finish), tails 0.20, fuselage 0.05.
- Retractable gear: no gear term.
- Cooling factor 1.2: buried engine with side scoops and a fan (E). Pusher prop behind the body: no installation penalty or credit (E).
- Published-point weight unstated: 3,300 lb assumed (E).
- Original installed engine mass 512 lb = typical published dry weight x 1.15 for mount, baffles, exhaust and oil cooler (E; per-variant check owed by MANUFACTURING).

**Published points against the raw build-up** (drag factor 1.00):

| Published KTAS | Density alt, ft | hp | gph | Grade | Our KTAS (raw build-up) | Difference | Drag factor to match | Our hp for the published speed | Conditions |
|---|---|---|---|---|---|---|---|---|---|
| 205 | 4,500 | 203 | 15.5 | P | 216 | +5% | 1.15 | 177 | AOPA Pilot Apr 1990, about 70% of 290 hp |
| 211 | 5,000 | 217 | 16.7 | F | 221 | +5% | 1.13 | 192 | spec block, 75%, manufacturer's calculation |

**Drag factor used: 1.29** (fleet calibration (own points read cleaner than the fleet); fleet calibration 1.29, range 1.16-1.36). Optimistic bound: 1.15.

**Drag build-up at 4,500 ft, 203 hp, 3,300 lb, with the factor applied:** 196 KTAS, CD0 0.0183 on S = 120.0 ft2, propeller efficiency 0.83, L/D 11.8.

| Item | D/q, ft2 | Basis |
|---|---|---|
| Wing | 0.637 | Swet 215.1 ft2, Re 6.1M, Cf 0.00220, FF 1.348, Q 1.00, x_tr 0.35 |
| HTail | 0.127 | Swet 33.4 ft2, Re 4.0M, Cf 0.00284, FF 1.276, Q 1.05, x_tr 0.20 |
| Fin | 0.092 | Swet 26.6 ft2, Re 6.1M, Cf 0.00262, FF 1.255, Q 1.05, x_tr 0.20 |
| Fuselage | 0.662 | Swet 239.3 ft2, Re 49.2M, Cf 0.00219, FF 1.263, Q 1.00, x_tr 0.05 |
| cooling | 0.104 | Raymer 12.39 x 1.20 |
| leakage+protuberance | 0.081 | 5% of the rest |
| calibration factor | 0.494 | x1.290 on the build-up (calibration; basis stated above) |
| induced | 0.255 | Oswald (Raymer 12.48), lift split stated above |

**Original engine, our numbers:** 200 hp at 8,000 ft gives 201 KTAS; still-air range on full usable fuel from MTOW 1,206 nm (climb allowance 27 lb); payload at 1,000 nm 874 lb with no reserve, 807 lb with 45 min.

**On the Aeromomentum line (AM20T), our numbers.** Installed-mass change -121 lb. The headline useful load takes no credit for a lighter engine (CG ballast assumed to eat it); the number in brackets takes the full saving and the optimistic drag factor.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| AM-low (critical alt 8,000 ft, assumed) | AM20T | 8k | 199 (208) | 1,350 (1,471) | 1,225 | 880 | 815 (954) | 165: 973 / 931 |
| AM-high (critical alt 16,000 ft, assumed) | AM20T | 16k | 212 (221) | 1,350 (1,471) | 1,257 | 890 | 825 (963) | 174: 973 / 930 |

### Engine fit with the Aeromomentum line

- **Power.** The AM20T at 195 hp assumed continuous replaces a 290-300 hp IO-540 or IO-550 cruising at about 200 hp. On a low-drag pusher that gives 199-212 KTAS: the fastest result on the shortlist.
- **Mass and CG.** The installed mass falls by about 121 lb (E). The engine sits behind the cabin over the wing, so the CG moves forward; the headline useful load takes no credit for the saving.
- **Installation.** The prop sits at the tail cone on a roughly 6.5 ft shaft. A geared Aeromomentum engine still needs that shaft and its couplings, and the 2018 fatal accident was a coupling failure. The liquid cooling replaces side scoops and a fan. The second prototype, which had a V-8 automotive engine, had radiator cooling problems and burned in flight (Klapmeier history).

### Rights and provenance (stage 2)

Firmly held (Elon, `docs/rights/cirrus-vk-30.md`, PR #3). There is no type certificate; it was a kit only. The seller was Cirrus Design, now Cirrus Aircraft, listed in Hong Kong in 2024 and about 85% held by CAIGA, itself about 73% AVIC-owned. No public record says who holds the drawings, molds or tooling; the default assumption, not a finding, is the Cirrus group. "CIRRUS" is a live mark. Two remain on the register, one of them in the EAA museum. Elon's verdict on a direct path: unlikely.

### Safety record

Record (NTSB bulk databases, own count): 7 accidents, 5 fatal, 10 killed, on about 13 completed aircraft. The fatal causes were: fuel starvation after a builder fuel-system change (1994); failure to recover from an aft-CG spin during stall testing of new wings (1996), where the NTSB cited inadequate handling design and no anti-spin provision; right-wing flutter after a cruise-flap bracket failure from an incomplete bond cure and wrong hinge material (1996); a forced landing after a ruptured oil line (2007); and an in-flight driveshaft fracture after coupling nuts backed off, with the flailing shaft knocking off the tail fairing, killing four (2018). In 1996 Cirrus recommended grounding all VK-30s pending new wings. **Inference:** three of the five fatal accidents (shaft, flap flutter, spin) trace to the design or the configuration, not only to builders.

### Why it died, and whether a revival fixes it

The founders' own verdict was "we failed as kitmakers". The kit was too complex, so they went to Part 23 certification with the SR20 and bought back about three-quarters of the outstanding kits. A revival fixes that only if the shaft drive, the cruise flap and spin recovery are redesigned, which makes it a new airplane on the VK-30's lines.

### Not yet done

- Nothing, unless Bill wants to test whether Cirrus would release it (contact is his call).
- If it goes forward: a SAFETY review of the shaft-drive and flutter accidents, asked on AER-3785 first.

<!-- stage3:end -->
