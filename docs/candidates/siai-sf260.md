# SIAI-Marchetti SF.260

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | foreign design |
| Designer / maker | Stelio Frati; Aviamilano / SIAI-Marchetti, Italy |
| Years | 1964-2017 |
| Number built | 976 (~180 civil) |
| Survivors / registered | <100 in US (2000) |
| Seats | 3 |
| Configuration | Low wing, 3 seats, retractable gear, aerobatic |
| Construction | All-metal |
| Engine | Lycoming O/IO-540, 260 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,645 lb | T | [source](https://www.easa.europa.eu/et/downloads/7060/en) | F260E/F |
| Empty weight | 1,750 lb | P | [source](https://www.aopa.org/news-and-media/all-news/2000/july/pilot/siai-marchetti-aermacchi-sf-260) | - |
| Useful load | 895 lb | P | [source](https://www.aopa.org/news-and-media/all-news/2000/july/pilot/siai-marchetti-aermacchi-sf-260) | - |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 62 US gal | T | [source](https://www.easa.europa.eu/et/downloads/7060/en) | - |
| Published range | 1,040 nm | P | [source](https://planeandpilotmag.com/siai-marchetti-sf260/) | 55%, reserve not stated |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 175 P | 6000 | 75% | 14 | P | [source](https://www.aopa.org/news-and-media/all-news/2000/july/pilot/siai-marchetti-aermacchi-sf-260) | SF.260D flight manual |
| 165 M | 15000 | 59% | 12.7 | P | [source](https://www.aopa.org/news-and-media/all-news/2000/july/pilot/siai-marchetti-aermacchi-sf-260) | - |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. Useful load and range are targets: a miss is reported with its size, and payload against range is the tradeoff to read. Cruise above 160 KTAS is a floor.

- **As published: fail** - UL -105 lb
  - Useful load: 895 lb (fail) against 1,000 lb.
  - Range: 1,040 nm (pass; 55%, reserve not stated) against 1,000 nm.
  - Cruise: 175 KTAS at 6,000 ft (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm, lb, no reserve / 45 min: cannot (775 nm max).
- **Measured or reported: partial: range fail, speed pass** - range -194 nm
  - Useful load: - lb (?) against 1,000 lb.
  - Range: 806 nm (fail; still air, no reserve, from fuel and measured flow at 165 KTAS) against 1,000 nm.
  - Cruise: 165 KTAS at 15,000 ft (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm, lb, no reserve / 45 min: cannot be computed on this basis.
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 260 hp.

Sanity flags:

- published range 1,040 nm vs 806 nm from fuel and flow

## Why it died

No reason found; production ended in 2017.

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Aerobatic, fast and strong: 175 KTAS at 6,000 ft on 260 hp with three seats (flight manual), from a small, clean wing.

## Rights and provenance (known so far; research, not legal advice)

EASA TC holder: Leonardo S.p.A. FAA TCDS A10EU. Owned by the stage 2 rights research (AER-3787).

## Safety record

Not researched.

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
