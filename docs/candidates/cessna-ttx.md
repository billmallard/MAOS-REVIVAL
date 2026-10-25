# Cessna TTx / Columbia 400

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | certified, out of production |
| Designer / maker | Lancair -> Columbia -> Cessna |
| Years | 2004-2018 |
| Number built | ~704 (unverified) |
| Survivors / registered | 609 registered |
| Seats | 4 |
| Configuration | Low wing, 4 seats, fixed gear, side-stick |
| Construction | All-composite (honeycomb sandwich) |
| Engine | Continental TSIO-550-C, 310 hp, twin turbo |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 3,600 lb | T | [source](https://www.easa.europa.eu/sites/default/files/dfu/EASA.IM_.A.516_Issue%205_20180621.pdf) | - |
| Empty weight | 2,535 lb | F | [source](http://web.archive.org/web/20171228025049/http://cessna.txtav.com:80/en/piston/cessna-ttx) | - |
| Useful load | 1,065 lb | F | [source](http://web.archive.org/web/20171228025049/http://cessna.txtav.com:80/en/piston/cessna-ttx) | - |
| Useful load, fleet or as-weighed | 1,027 lb | P | [source](https://aopa.org/news-and-media/all-news/2007/october/01/columbia-400) | one test aircraft, not a fleet average |
| Usable fuel | 102 US gal | T | [source](https://www.easa.europa.eu/sites/default/files/dfu/EASA.IM_.A.516_Issue%205_20180621.pdf) | - |
| Published range | 1,270 nm | F | [source](http://web.archive.org/web/20171228025049/http://cessna.txtav.com:80/en/piston/cessna-ttx) | not stated |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 219 P | 22000 | 75% | 16 | P | [source](https://planeandpilotmag.com/cessna-ttx/) | spec box |
| 180 M | 12000 | - | 15.5 | P | [source](https://www.aopa.org/news-and-media/all-news/2013/july/01/cessna-delivers-ttx) | lean of peak |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. Useful load and range are targets: a miss is reported with its size, and payload against range is the tradeoff to read. Cruise above 160 KTAS is a floor.

- **As published: pass**
  - Useful load: 1,065 lb (pass) against 1,000 lb.
  - Range: 1,270 nm (pass; not stated) against 1,000 nm.
  - Cruise: 219 KTAS at 22,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm, lb, no reserve / 45 min: 627 / 555 @ 219 kt, 16.0 gph.
- **Measured or reported: pass**
  - Useful load: 1,027 lb (pass) against 1,000 lb.
  - Range: 1,185 nm (pass; still air, no reserve, from fuel and measured flow at 180 KTAS) against 1,000 nm.
  - Cruise: 180 KTAS at 12,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm, lb, no reserve / 45 min: 510 / 441 @ 180 kt, 15.5 gph.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 310 hp (-6% speed, est. 207 KTAS).

Sanity flags:

- fleet useful load 38 lb below factory

## Why it died

44 sold in 2015, 23 in 2017, against 355 Cirrus singles; production stopped 2018 (AOPA).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Certified all-composite four-seater with side-stick and 219 KTAS at FL220; lost on market share, not on performance.

## Rights and provenance (known so far; research, not legal advice)

TC A00003SE: Textron Aviation. Chain: Pacific Aviation Composites -> Lancair -> Columbia (bankrupt 2007) -> Cessna. Owned by the stage 2 rights research (AER-3787).

## Safety record

Not found.

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
