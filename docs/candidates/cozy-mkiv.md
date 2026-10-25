# Cozy MKIV (reference)

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Nat Puffer, Co-Z Development (Rutan Long-EZ lineage) |
| Years | 1991 on; plans still sold |
| Number built | ~1,450 plans sets sold by 2009; ~225 flying then (Co-Z FAQ); 350 built by 2015 (Wikipedia) |
| Survivors / registered | FAA count not obtained |
| Seats | 4 |
| Configuration | Canard pusher, 4 seats (2+2 side by side), fixed mains, retractable nose gear |
| Construction | Moldless foam/fiberglass composite |
| Engine | Lycoming O-360, 180 hp (160-200 hp suitable) |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,050 lb | F | [source](https://www.aircraftspruce.com/cozy/specs.html) | - |
| Empty weight | 1,050 lb | F | [source](https://www.aircraftspruce.com/cozy/specs.html) | designer's estimated empty weight (AOPA Pilot 1994) |
| Useful load | 1,000 lb | F | [source](https://www.aircraftspruce.com/cozy/specs.html) | derived 2,050 - 1,050 |
| Useful load, fleet or as-weighed | 871 lb | P | [source](http://acversailles.free.fr/documentation/03~Documentation_Generale_M_Suire/Essais_en_vol/COZY_MARK-IV.pdf) | one builder aircraft weighed by the CAFE Foundation (N494CZ, 1,179.3 lb empty) against the 2,050 lb design gross; not a fleet average |
| Usable fuel | 52 US gal | F | [source](https://www.aircraftspruce.com/catalog/pnpages/01-00257.php) | capacity; usable not stated |
| Published range | 1,129 nm | F | [source](https://www.aircraftspruce.com/cozy/specs.html) | 40% power, 12,000 ft, reserve not stated (1,300 mi converted) |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 174 | 8500 | - | - | P | [source](https://www.kitplanes.com/archive-august-1991/) | factory demonstrator measured, 2,700 rpm, fixed-pitch prop |
| 191 P | 8000 | 75% | - | F | [source](https://www.aircraftspruce.com/cozy/specs.html) | 220 mph converted |
| 192 | - | - | 10.5 | F | [source](https://www.aopa.org/news-and-media/all-news/1994/december/pilot/ez-does-it) | claimed max cruise, quoted by AOPA Pilot Dec 1994 |
| 161 | 12000 | 40% | - | F | [source](https://www.aircraftspruce.com/cozy/specs.html) | 185 mph converted, 40% power |
| 176.7 M | 8021 | - | 10.0 | P | [source](http://acversailles.free.fr/documentation/03~Documentation_Generale_M_Suire/Essais_en_vol/COZY_MARK-IV.pdf) | CAFE flight test, N494CZ, IO-360 180 hp, WOT 23.5 in / 2,607 rpm, best-power region, density altitude, 1,864 lb |
| 169.5 | 12032 | - | 8.2 | P | [source](http://acversailles.free.fr/documentation/03~Documentation_Generale_M_Suire/Essais_en_vol/COZY_MARK-IV.pdf) | CAFE flight test, N494CZ, WOT 20.1 in / 2,545 rpm, mid mixture sweep, density altitude, 1,874 lb |
| 163.5 | 8102 | - | 8.3 | P | [source](http://acversailles.free.fr/documentation/03~Documentation_Generale_M_Suire/Essais_en_vol/COZY_MARK-IV.pdf) | CAFE flight test, N494CZ, WOT 23.5 in / 2,500 rpm, lean of peak, density altitude |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: pass**
  - Useful load: 1,000 lb (pass) against 1,000 lb.
  - Range: 1,129 nm (pass; 40% power, 12,000 ft, reserve not stated (1,300 mi converted)) against 1,000 nm.
  - Cruise: 191 KTAS at 8,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot (951 nm max).
- **Measured or reported: fail** - UL -129 lb
  - Useful load: 871 lb (fail) against 1,000 lb.
  - Range: 1,049 nm (pass; still air, no reserve, from fuel and measured flow at 170 KTAS) against 1,000 nm.
  - Cruise: 177 KTAS at 8,021 ft (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 581 / cannot @ 170 kt, 8.2 gph.
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 180 hp.

Sanity flags:

- fleet useful load 129 lb below factory
- the only published speed/flow pair (192 kt, 10.5 gph) is a claim, and the 40%-power range has no published flow
- as published (1,000 lb, 1,129 nm, 191 KTAS at 8,000 ft) it passes all three floors; the 951 nm in the first version of this list was 52 gal / 10.5 gph x 192 kt, the AOPA-quoted max-cruise claim, set against a range published at 40% power: a basis mismatch, not a units error (1,300 statute mi = 1,129 nm is right)

## Why it died

Not dead. Aircraft Spruce has held exclusive rights since 1 Jan 2004 and sells plans and components (http://www.cozyaircraft.com/czmain.htm).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Side-by-side front seats in a canard pusher: the Long-EZ layout widened to four seats without losing its cruise efficiency on 180 hp.
- Moldless foam-and-glass construction that a plans builder can do without tooling; the cost is build hours and builder-to-builder weight scatter (871 lb useful on the CAFE aircraft against 1,000 lb designed).

## Rights and provenance (known so far; research, not legal advice)

Aircraft Spruce (exclusive marketing rights from Co-Z Development, 2004); also bought Brock metal-parts tooling 2005. Owned by the stage 2 rights research (AER-3787).

## Safety record

Co-Z FAQ cites two fatal accidents (to ~2009); a four-aboard MKIV was lost off California 15 Jan 2024 (NBC LA).

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
