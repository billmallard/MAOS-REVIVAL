# Van's RV-10

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Van's Aircraft |
| Years | 2003 first flight; alive |
| Number built | 1,075 flown (Van's counter, Oct 2026) |
| Survivors / registered | 816 US-registered (734 with airworthiness date) |
| Seats | 4 |
| Configuration | Low wing, 4 seats, fixed gear |
| Construction | Aluminum |
| Engine | Lycoming IO-540, 235-260 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,700 lb | F | [source](https://www.vansaircraft.com/rv-10/) | - |
| Empty weight | 1,575 lb | F | [source](https://www.vansaircraft.com/rv-10/) | midpoint of 1,520-1,630 |
| Useful load | 1,125 lb | F | [source](https://www.vansaircraft.com/rv-10/) | derived from midpoint |
| Useful load, fleet or as-weighed | 1,050 lb | P | [source](https://www.kitplanes.com/flight-review-seven-into-ten/) | 1,600-1,700 lb typical builder empty, midpoint |
| Usable fuel | 60 US gal | F | [source](https://www.vansaircraft.com/rv-10/) | - |
| Published range | 869 nm | F | [source](https://www.vansaircraft.com/rv-10/) | 55%, 8,000 ft, reserve not stated (1,000 sm) |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 171 P | 8000 | 75% | - | F | [source](https://www.vansaircraft.com/rv-10/) | at gross, 197 mph converted |
| 153 | 8000 | 55% | - | F | [source](https://www.vansaircraft.com/rv-10/) | 176 mph converted |
| 167 M | - | - | 12 | P | [source](https://www.kitplanes.com/flight-review-seven-into-ten/) | 'realistic' 165-170 kt, ~12 gph lean of peak |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: fail** - range -131 nm
  - Useful load: 1,125 lb (pass) against 1,000 lb.
  - Range: 869 nm (fail; 55%, 8,000 ft, reserve not stated (1,000 sm)) against 1,000 nm.
  - Cruise: 171 KTAS at 8,000 ft (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- **Measured or reported: fail** - range -165 nm
  - Useful load: 1,050 lb (pass) against 1,000 lb.
  - Range: 835 nm (fail; still air, no reserve, from fuel and measured flow) against 1,000 nm.
  - Cruise: 167 KTAS at an unstated altitude (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot (835 nm max).
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 260 hp.

Sanity flags:

- fleet useful load 75 lb below factory

## Why it died

Not dead. Still produced and supported.

## Rights and provenance (known so far; research, not legal advice)

Van's Aircraft. Owned by the stage 2 rights research (AER-3787).

## Safety record

Not found; BRS kit available since 2019.

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
