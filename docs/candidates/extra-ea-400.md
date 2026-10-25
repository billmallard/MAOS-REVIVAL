# Extra EA-400

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | foreign design |
| Designer / maker | Walter Extra, Extra Flugzeugbau (Germany) |
| Years | 1996-~2014 |
| Number built | 27-28 |
| Survivors / registered | 26 flying (2017 owner); 9 on the US registry |
| Seats | 6 |
| Configuration | High wing, T-tail, 6 seats, retractable gear, pressurized |
| Construction | Fibre composite |
| Engine | Continental TSIOL-550-C, 350 hp takeoff / 325 hp continuous, turbo, liquid-cooled |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 4,407 lb | T | [source](https://www.easa.europa.eu/en/downloads/7504/en) | - |
| Empty weight | 2,974 lb | P | [source](https://www.planeandpilotmag.com/?p=14773) | - |
| Useful load | 1,347 lb | P | [source](https://planeandpilotmag.com/extra-400/) | - |
| Useful load, fleet or as-weighed | 1,102 lb | B | [source](https://euroga.org/forums/extra-400/7297) | owner: 'typically less than 500 kg' |
| Usable fuel | 106.7 US gal | T | [source](https://www.easa.europa.eu/en/downloads/7504/en) | 404 L usable |
| Published range | 1,300 nm | P | [source](https://planeandpilotmag.com/the-extra-ea-400-an-underappreciated-pressurized-composite-transportation-plane-from-aerobatic-masters/) | 'over 1,300 nm', no reserve stated |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 205 M | 18000 | 75% | 24 | B | [source](https://www.euroga.org/forums/extra-400/7297?page=2) | owner report |
| 203 P | 18000 | 75% | - | F | [source](https://en.wikipedia.org/wiki/Extra_EA-400) | - |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. Useful load and range are targets: a miss is reported with its size, and payload against range is the tradeoff to read. Cruise above 160 KTAS is a floor.

- **As published: pass**
  - Useful load: 1,347 lb (pass) against 1,000 lb.
  - Range: 1,300 nm (pass; 'over 1,300 nm', no reserve stated) against 1,000 nm.
  - Cruise: 203 KTAS at 18,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm, lb, no reserve / 45 min: cannot be computed on this basis.
- **Measured or reported: near miss** - range -89 nm
  - Useful load: 1,102 lb (pass) against 1,000 lb.
  - Range: 911 nm (near; still air, no reserve, from fuel and measured flow at 205 KTAS) against 1,000 nm.
  - Cruise: 205 KTAS at 18,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm, lb, no reserve / 45 min: cannot (911 nm max).
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 325 hp (-7% speed, est. 190 KTAS).

Sanity flags:

- published range 1,300 nm vs 911 nm from fuel and flow
- weights do not add: 4,407 - 2,974 != 1,347
- fleet useful load 245 lb below factory
- the only liquid-cooled certified piston here, so a natural precedent for a liquid-cooled Aeromomentum install

## Why it died

About 16,000 labour hours and a ~$1M price; the company ran into financial trouble (P&P 2022).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- A high-wing, pressurised, six-seat composite single with a T-tail.
- Lesson: about 16,000 labour hours per airplane made it unaffordable; the build method is the failure.

## Rights and provenance (known so far; research, not legal advice)

EASA TC holder: Aerospace Composites GmbH, Laupheim (Oct 2025). Earlier SST Flugtechnik (insolvent 2025); design rights to Jiangsu A-Star, China (2014). Owned by the stage 2 rights research (AER-3787).

## Safety record

Fatal accidents 1998 (first delivery), 2018 Oklahoma (5 killed), 2025 Switzerland (3 killed).

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
