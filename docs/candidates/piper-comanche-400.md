# Piper PA-24-400 Comanche 400

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | certified, out of production |
| Designer / maker | Piper Aircraft |
| Years | 1964-66 |
| Number built | 148 |
| Survivors / registered | 75 registered; ~25 flying (P&P) |
| Seats | 4 |
| Configuration | Low wing, 4 seats, retractable gear |
| Construction | All-metal |
| Engine | Lycoming IO-720, 400 hp (8 cyl) |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 3,600 lb | T | [source](https://docs.northeastcomanche.org/tcds/1a15-rev_34.pdf) | - |
| Empty weight | 2,110 lb | F | [source](https://planeandpilotmag.com/1964-piper-comanche-400/) | - |
| Useful load | 1,490 lb | F | [source](https://planeandpilotmag.com/1964-piper-comanche-400/) | - |
| Useful load, fleet or as-weighed | 1,331 lb | P | [source](https://planeandpilotmag.com/1964-piper-comanche-400/) | one test aircraft, 2,269 lb empty |
| Usable fuel | 124 US gal | T | [source](https://docs.northeastcomanche.org/tcds/1a15-rev_34.pdf) | - |
| Published range | 860 nm | F | [source](https://planeandpilotmag.com/1964-piper-comanche-400/) | 55%, 'w/reserve' unspecified, estimated |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 185 P | - | 75% | 22 | F | [source](https://planeandpilotmag.com/1964-piper-comanche-400/) | Jane's via P&P |
| 180 | - | 65% | 19 | F | [source](https://planeandpilotmag.com/1964-piper-comanche-400/) | - |
| 171 | - | 55% | 16 | F | [source](https://planeandpilotmag.com/1964-piper-comanche-400/) | - |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: fail** - range -140 nm
  - Useful load: 1,490 lb (pass) against 1,000 lb.
  - Range: 860 nm (fail; 55%, 'w/reserve' unspecified, estimated) against 1,000 nm.
  - Cruise: 185 KTAS at an unstated altitude (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 929 / 857 @ 171 kt, 16.0 gph.
- **Measured or reported: partial: UL pass**
  - Useful load: 1,331 lb (pass) against 1,000 lb.
  - Range: - nm (?; none found) against 1,000 nm.
  - Cruise: not found against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 400 hp (-13% speed, est. 160 KTAS).

Sanity flags:

- published range 860 nm vs 1,325 nm from fuel and flow
- screen speed has no altitude, or is below 6,000 ft
- fleet useful load 159 lb below factory

## Why it died

Less payload than the Comanche B and a 400 hp burn; the whole line ended when the 1972 Agnes flood destroyed Lock Haven tooling (AvWeb).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- A fast, strong four-seater with an eight-cylinder engine; heavy and thirsty, and its tooling was lost in the 1972 flood.

## Rights and provenance (known so far; research, not legal advice)

TCDS 1A15 holder: Piper Aircraft, Inc. Owned by the stage 2 rights research (AER-3787).

## Safety record

Rear-cylinder cooling problems reported.

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
