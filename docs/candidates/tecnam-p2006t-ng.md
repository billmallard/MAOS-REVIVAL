# Tecnam P2006T NG

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | foreign design |
| Designer / maker | Costruzioni Aeronautiche Tecnam SpA, Italy |
| Years | NG launched AERO 2024; EASA TC (Section B, P2006T NG) 19 Feb 2025; FAA certification expected Q4 2026 |
| Number built | - |
| Survivors / registered | In delivery in multiple markets (Tecnam, Flying Jan 2026) |
| Seats | 4 |
| Configuration | High wing light twin, 4 seats, retractable gear |
| Construction | Metal (aluminium) airframe |
| Engine | 2x Rotax 912 iSc3 Sport, 100 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,844 lb | T | [source](https://www.easa.europa.eu/en/downloads/7264/en) | 1290 kg, EASA TCDS A.185 Issue 19 (20 Apr 2026), Section B P2006T NG; converted |
| Empty weight | 1,940 lb | F | [source](https://www.tecnam.com/aircraft/p2006t-ng/) | 880 kg standard empty weight, converted. Tecnam site blocks scripted fetch (HTTP 520); read via WebFetch |
| Useful load | 904 lb | F | [source](https://www.tecnam.com/aircraft/p2006t-ng/) | 410 kg, factory figure, converted |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 52.8 US gal | T | [source](https://www.easa.europa.eu/en/downloads/7264/en) | capacity 200 L (194 L usable per TCDS), converted |
| Published range | 930 nm | F | [source](https://www.tecnam.com/aircraft/p2006t-ng/) | Factory range 930 nm (1722 km); reserve, altitude, power not stated; nautical miles |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 148 P | - | - | 7.4 | F | [source](https://www.tecnam.com/aircraft/p2006t-ng/) | Factory max cruise speed 148 kt / 274 km/h; altitude, power and weight not stated; assumed TAS. gph = 2 x 3.7 USG/h factory fuel consumption (power not stated) |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. Useful load and range are targets: a miss is reported with its size, and payload against range is the tradeoff to read. Cruise above 160 KTAS is a floor.

- **As published: fail** - UL -96 lb, range -70 nm, speed -12 kt
  - Useful load: 904 lb (near) against 1,000 lb.
  - Range: 930 nm (near; Factory range 930 nm (1722 km); reserve, altitude, power not stated; nautical miles) against 1,000 nm.
  - Cruise: 148 KTAS at an unstated altitude (fail) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm, lb, no reserve / 45 min: 604 / cannot @ 148 kt, 7.4 gph.
- **Measured or reported: no data found.**
- Aeromomentum fit (first cut): Yes: 2x AM13 (100 hp) for 100 hp.

Sanity flags:

- screen speed has no altitude, or is below 6,000 ft

## Why it died

Shown at AERO 2025 by German dealer GM Aviation (stand A4-319; fliegermagazin 9 Apr 2025) and at AERO 2026 on Tecnam's stand (aerokurier 28 Apr 2026). Orders for 4 P2006T NG were announced at AERO 2026 (afm.aero). US/Canada launch Jan 2026; FAA certification expected Q4 2026. Price not published.

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Proof that a certified light twin on two 100 hp Rotax engines sells, as a trainer; far below the survey's speed floor.

## Rights and provenance (known so far; research, not legal advice)

Current OEM type (Tecnam), EASA TC A.185 Owned by the stage 2 rights research (AER-3787).

## Safety record

Not checked here

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
