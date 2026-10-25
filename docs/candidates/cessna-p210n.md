# Cessna P210N Pressurized Centurion

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | certified, out of production |
| Designer / maker | Cessna Aircraft Co. |
| Years | 1978-83 (P210R 1985-86) |
| Number built | 834 P210N (TCDS serials) |
| Survivors / registered | 418 registered |
| Seats | 6 |
| Configuration | High wing, 6 seats, retractable gear, pressurized 3.35 psi |
| Construction | All-metal |
| Engine | Continental TSIO-520-P/-AF, 310 hp takeoff / 285 hp continuous, turbo |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 4,000 lb | T | FAA DRS, TCDS 3A21 Rev 50, 18 Nov 2021, read 2026-10-24 (archived: docs/longlist/sources/tcds-3A21-rev50-2021-11-18.pdf); value unchanged from Rev 49 | - |
| Empty weight | 2,426 lb | F | [source](https://www.aopa.org/go-fly/aircraft-and-ownership/aircraft-fact-sheets/cessna-p210) | 1982 standard empty |
| Useful load | 1,574 lb | F | [source](https://www.aopa.org/go-fly/aircraft-and-ownership/aircraft-fact-sheets/cessna-p210) | - |
| Useful load, fleet or as-weighed | 1,480 lb | B | [source](https://www.aviationconsumer.com/aircraftreviews/cessna-p210-centurion/) | owners report 900-1,000 lb payload with full fuel; midpoint + 87 gal |
| Usable fuel | 87 US gal | T | FAA DRS, TCDS 3A21 Rev 50, 18 Nov 2021, read 2026-10-24 (archived: docs/longlist/sources/tcds-3A21-rev50-2021-11-18.pdf); value unchanged from Rev 49 | S/N 761 on; 89 earlier |
| Published range | 925 nm | F | [source](https://australianaviation.com.au/1978/06/p210cessnas-high-flying-single/) | standard fuel, power and reserve not stated |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 199 M | 20000 | - | - | P | [source](https://australianaviation.com.au/1978/06/p210cessnas-high-flying-single/) | flight test, 33 in / 2,500 rpm |
| 183 | 20000 | 75% | 15.5 | F | [source](https://australianaviation.com.au/1978/06/p210cessnas-high-flying-single/) | 11.8 nm/gal |
| 196 P | 20000 | 80% | 18.8 | F | [source](https://australianaviation.com.au/1978/06/p210cessnas-high-flying-single/) | 10.4 nm/gal |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: near miss** - range -75 nm
  - Useful load: 1,574 lb (pass) against 1,000 lb.
  - Range: 925 nm (near; standard fuel, power and reserve not stated) against 1,000 nm.
  - Cruise: 196 KTAS at 20,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 1,066 / cannot @ 183 kt, 15.5 gph.
- **Measured or reported: partial: UL pass, speed pass**
  - Useful load: 1,480 lb (pass) against 1,000 lb.
  - Range: - nm (?; none found) against 1,000 nm.
  - Cruise: 199 KTAS at 20,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 285 hp (-3% speed, est. 193 KTAS).

Sanity flags:

- fleet useful load 94 lb below factory
- owners add tip tanks to reach 1,000 nm with reserve; on factory fuel it is marginal
- kit builders are attempting 210-class airplanes (Bill); what exists is fixed-gear 5-6 seat high-wing kits, none a retractable 210 copy: see '210-class kits' in LONGLIST.md

## Why it died

The Pressurized Centurion ended with Cessna's 1986 piston shutdown; the P210R sold only ~40 against the Malibu (P&P 2005).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Six seats, pressurisation and a large, well-documented fleet: the calibration case for the method. Kit builders now attempt 210 analogs (see the long list).

## Rights and provenance (known so far; research, not legal advice)

TCDS 3A21 holder: Textron Aviation Inc. (from Cessna, 2015). Owned by the stage 2 rights research (AER-3787).

## Safety record

Early detonation engine failures led to a turbo retrofit AD; 210 family accidents 20% fuel, 14% gear-up (Aviation Consumer).

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
