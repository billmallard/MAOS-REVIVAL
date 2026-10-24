# Meyers 200D / Aero Commander 200D

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

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
  - Range: 1,153 nm (pass; still air, no reserve, from fuel and measured flow) against 1,000 nm.
  - Cruise: 187 KTAS at an unstated altitude (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 515 / 461 @ 187 kt, 12.0 gph.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 285 hp (-3% speed, est. 177 KTAS).

Sanity flags:

- published range 782 nm vs 1,153 nm from fuel and flow
- screen speed has no altitude, or is below 6,000 ft
- fleet useful load 160 lb below factory
- the 187 kt / 12 gph pair comes from a weak source; at the owner's 15.5 gph the still-air range is ~730 nm

## Why it died

Hand-built with minimal tooling; 'it took $4 million to produce $3 million worth' (P&P).

## Rights and provenance (known so far; research, not legal advice)

TCDS 3A18 holder: Interceptor Aviation Inc., Bethany OK (2014; GlobalParts affiliate). Owned by the stage 2 rights research (AER-3787).

## Safety record

20 accidents in 35 years; 5 tank-run-dry, 9 maintenance; no in-flight breakups (AvWeb).

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
