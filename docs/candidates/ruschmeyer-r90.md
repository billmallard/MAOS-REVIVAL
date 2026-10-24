# Ruschmeyer R90-230RG

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | foreign design |
| Designer / maker | Ruschmeyer Luftfahrttechnik, Germany |
| Years | 1988-96 |
| Number built | 26-30 |
| Survivors / registered | not counted |
| Seats | 4 |
| Configuration | Low wing, 4 seats, retractable gear |
| Construction | Composite |
| Engine | Lycoming IO-540-C4D5, 230 hp (derated) |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,977 lb | T | [source](https://www.easa.europa.eu/bg/downloads/17339/en) | - |
| Empty weight | 1,980 lb | F | [source](https://en.wikipedia.org/wiki/Ruschmeyer_R_90) | Jane's 1993-94 |
| Useful load | 997 lb | F | [source](https://en.wikipedia.org/wiki/Ruschmeyer_R_90) | derived |
| Useful load, fleet or as-weighed | 875 lb | P | [source](https://www.aopa.org/news-and-media/all-news/2001/november/pilot/solaris-sigma-230) | as tested |
| Usable fuel | 62.3 US gal | T | [source](https://www.easa.europa.eu/bg/downloads/17339/en) | - |
| Published range | 600 nm | P | [source](https://www.aopa.org/news-and-media/all-news/1994/november/pilot/ruschmeyer-r90-230-rg) | IFR |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 165 M | 7000 | 75% | 14.5 | P | [source](https://www.aopa.org/news-and-media/all-news/1994/november/pilot/ruschmeyer-r90-230-rg) | - |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: incomplete: no speed, fails on the rest** - UL -3 lb, range -400 nm
  - Useful load: 997 lb (near) against 1,000 lb.
  - Range: 600 nm (fail; IFR) against 1,000 nm.
  - Cruise: not found against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- **Measured or reported: fail** - UL -125 lb, range -291 nm
  - Useful load: 875 lb (fail) against 1,000 lb.
  - Range: 709 nm (fail; still air, no reserve, from fuel and measured flow) against 1,000 nm.
  - Cruise: 165 KTAS at 7,000 ft (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot (709 nm max).
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 230 hp.

Sanity flags:

- published range 600 nm vs 709 nm from fuel and flow
- fleet useful load 122 lb below factory

## Why it died

Bankrupt June 1996; Solaris bought the assets in 1999 but no deliveries were found (Flying).

## Rights and provenance (known so far; research, not legal advice)

EASA TC holder: Bernd Hager, Hannover (2022). Owned by the stage 2 rights research (AER-3787).

## Safety record

Abrupt wing drop at the stall (AOPA).

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
