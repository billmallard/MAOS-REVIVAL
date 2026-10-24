# Piper PA-46-310P Malibu

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | certified, out of production |
| Designer / maker | Piper Aircraft |
| Years | 1984-88 |
| Number built | 403 (TCDS serials) |
| Survivors / registered | 212 registered |
| Seats | 6 |
| Configuration | Low wing, 6 seats, retractable gear, pressurized 5.5 psi |
| Construction | All-metal |
| Engine | Continental TSIO-520-BE, 310 hp, twin turbo, intercooled |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 4,100 lb | T | FAA DRS, TCDS A25SO Rev 42, 16 Feb 2026, read 2026-10-24 (archived: docs/longlist/sources/tcds-A25SO-rev42-2026-02-16.pdf); value unchanged from Rev 26 | - |
| Empty weight | 2,645 lb | F | [source](https://www.aopa.org/go-fly/aircraft-and-ownership/aircraft-fact-sheets/piper-malibu-mirage) | - |
| Useful load | 1,455 lb | F | [source](https://www.aopa.org/go-fly/aircraft-and-ownership/aircraft-fact-sheets/piper-malibu-mirage) | - |
| Useful load, fleet or as-weighed | 1,400 lb | B | [source](https://www.flyingmag.com/used-aircraft-guide-piper-malibu-and-mirage-cheap-for-what-they-do/) | 'typical useful loads' |
| Usable fuel | 120 US gal | T | FAA DRS, TCDS A25SO Rev 42, 16 Feb 2026, read 2026-10-24 (archived: docs/longlist/sources/tcds-A25SO-rev42-2026-02-16.pdf); value unchanged from Rev 26 | 122 total, 12 lb unusable |
| Published range | 1,300 nm | P | [source](https://australianaviation.com.au/1985/06/airtest-piper-malibu/) | 120 gal, power and reserve not stated |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 205 | 22000 | 65% | 15 | P | [source](https://australianaviation.com.au/1985/06/airtest-piper-malibu/) | flight test |
| 180 | 20000 | 55% | 12 | P | [source](https://australianaviation.com.au/1985/06/airtest-piper-malibu/) | overweight ferry flight |
| 210 M | 25000 | 75% | - | B | [source](https://www.flyingmag.com/used-aircraft-guide-piper-malibu-and-mirage-cheap-for-what-they-do/) | owner-reported |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: incomplete: no speed**
  - Useful load: 1,455 lb (pass) against 1,000 lb.
  - Range: 1,300 nm (pass; 120 gal, power and reserve not stated) against 1,000 nm.
  - Cruise: not found against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- **Measured or reported: pass**
  - Useful load: 1,400 lb (pass) against 1,000 lb.
  - Range: 1,800 nm (pass; still air, no reserve, from fuel and measured flow at 180 KTAS) against 1,000 nm.
  - Cruise: 210 KTAS at 25,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 1,000 / 946 @ 180 kt, 12.0 gph.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 310 hp (-6% speed, est. 193 KTAS).

Sanity flags:

- published range 1,300 nm vs 1,800 nm from fuel and flow
- fleet useful load 55 lb below factory
- a live type family (M350 in production), so not orphaned

## Why it died

Engine problems led to a 1987 voluntary grounding request; replaced by the PA-46-350P Mirage. The type lives on as the M350 (Flying).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Cabin-class pressurised six-seat single; its engine troubles show how much an airframe's reputation rides on its powerplant.

## Rights and provenance (known so far; research, not legal advice)

TCDS A25SO holder: Piper Aircraft, Inc. (owned by the Government of Brunei). Owned by the stage 2 rights research (AER-3787).

## Safety record

PA-46 family: ~21% of accidents engine-related (Aviation Consumer).

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
