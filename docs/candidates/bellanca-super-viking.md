# Bellanca 17-30A Super Viking

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | certified, out of production |
| Designer / maker | Bellanca Aircraft Corp. |
| Years | 1969-~2001 (low rate) |
| Number built | ~1,356 Vikings all models |
| Survivors / registered | 389 17-30A valid registrations; 71 17-31ATC |
| Seats | 4 |
| Configuration | Low wing, 4 seats, retractable gear |
| Construction | Steel-tube fuselage, fabric; wooden wing |
| Engine | Continental IO-520-K, 300 hp takeoff / 285 hp continuous |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 3,325 lb | T | [source](http://rgl.faa.gov/Regulatory_and_Guidance_Library/rgMakeModel.nsf/0/5af52329a2061d4a86256c24005133db/$FILE/A18ce.pdf) | with placards and matching AFM; 3,200 otherwise |
| Empty weight | 2,217 lb | F | [source](https://en.wikipedia.org/wiki/Bellanca_Viking) | 1976 (Jane's) |
| Useful load | 1,108 lb | F | [source](https://en.wikipedia.org/wiki/Bellanca_Viking) | derived |
| Useful load, fleet or as-weighed | 1,000 lb | B | [source](https://avweb.com/features/bellanca-viking/) | 'typically 1000 pounds or so' |
| Usable fuel | 69 US gal | T | [source](http://rgl.faa.gov/Regulatory_and_Guidance_Library/rgMakeModel.nsf/0/5af52329a2061d4a86256c24005133db/$FILE/A18ce.pdf) | late serials; 60-64 earlier |
| Optional fuel | 84 US gal | T | [source](http://rgl.faa.gov/Regulatory_and_Guidance_Library/rgMakeModel.nsf/0/5af52329a2061d4a86256c24005133db/$FILE/A18ce.pdf) | - |
| Published range | 802 nm | F | [source](https://en.wikipedia.org/wiki/Bellanca_Viking) | max fuel, reserve not stated |

Cruise settings (the starred row is the one screened for speed):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 165 * | 7500 | 62% | - | P | [source](https://planeandpilotmag.com/bellanca-viking-wood-fabric-and-genius/) | owner in pilot report: 165+ kt at 60-65%, flown at 7,500-8,500 ft |
| 163 | - | 75% | - | F | [source](https://en.wikipedia.org/wiki/Bellanca_Viking) | Jane's, 188 mph converted |

## Screen (stage 1, published numbers)

- **Verdict: fail** - range -141 nm
- Useful load: 1,000 lb (pass) against 1,000 lb.
- Range: 859 nm still-air (fail; basis: calc, est. flow) against 1,000 nm.
- Cruise: 165 KTAS at 7,500 ft (pass) against >160 KTAS (>180 preferred).
- Payload at 1,000 nm: Does not reach 1,000 nm on usable fuel: 859 nm still-air maximum.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 285 hp (-3% speed, est. 160 KTAS).

Sanity flags:

- fleet useful load 108 lb below factory
- with optional tanks (84 gal) still-air range is 1,046 nm
- turbo 17-31ATC reported at 190 kt at FL200 (AvWeb, fleet-grade)

## Why it died

Bankrupt in 1980; custom-order production from 1984, bankrupt again in 2001 (AvWeb).

## Rights and provenance (known so far; research, not legal advice)

TCDS A18CE holder (2002): Alexandria Aircraft LLC; reported move to Sulphur OK as Bellanca Aircraft Inc. (2022) unverified. Owned by the stage 2 rights research (AER-3787).

## Safety record

Wood deterioration AD 76-08-04; fuel-mismanagement accidents fell after the 1974 tank simplification (AvWeb).

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
