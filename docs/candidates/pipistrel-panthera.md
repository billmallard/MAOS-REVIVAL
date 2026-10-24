# Pipistrel Panthera

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | prototype that never reached production, foreign design |
| Designer / maker | Pipistrel (Slovenia) |
| Years | 2013 first flight; not certified (2026 status unverified) |
| Number built | not found |
| Survivors / registered | sold as Experimental in the US |
| Seats | 4 |
| Configuration | Low wing, 4 seats, retractable trailing-link gear, gull-wing doors, airframe parachute |
| Construction | Carbon/glass/Kevlar composite |
| Engine | Lycoming IO-540-V4A5, 260 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,899 lb | F | [source](https://web.archive.org/web/20200726071257/https://www.pipistrel-aircraft.com/aircraft/cruising/panthera/) | - |
| Empty weight | 1,797 lb | F | [source](https://web.archive.org/web/20200726071257/https://www.pipistrel-aircraft.com/aircraft/cruising/panthera/) | - |
| Useful load | 1,023 lb | F | [source](https://www.pipistrel-aircraft.com/products/panthera/) | Flying 2021 gives 1,100 |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 55.5 US gal | F | [source](https://web.archive.org/web/20200726071257/https://www.pipistrel-aircraft.com/aircraft/cruising/panthera/) | 210 L; usable not stated |
| Published range | 1,460 nm | F | [source](https://www.pipistrel-aircraft.com/products/panthera/) | not stated |

Cruise settings (the starred row is the one screened for speed):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 194 * | 8000 | 75% | 14.8 | F | [source](https://web.archive.org/web/20200726071257/https://www.pipistrel-aircraft.com/aircraft/cruising/panthera/) | - |

## Screen (stage 1, published numbers)

- **Verdict: fail** - range -272 nm
- Useful load: 1,023 lb (pass) against 1,000 lb.
- Range: 728 nm still-air (fail; basis: calc) against 1,000 nm.
- Cruise: 194 KTAS at 8,000 ft (pass+) against >160 KTAS (>180 preferred).
- Payload at 1,000 nm: Does not reach 1,000 nm on usable fuel: 728 nm still-air maximum.
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 260 hp.

Sanity flags:

- published range 1,460 nm vs 728 nm from fuel and flow
- weights do not add: 2,899 - 1,797 != 1,023
- the 1,460 nm claim is reproduced exactly by 420 L (2 x 210 L) at the published flow, while the published 770 lb full-fuel payload implies ~42-55 gal; both cannot be true, and the fuel quantity needs a primary source

## Why it died

Repeated certification slips, including an engine change when Lycoming would not certify the IO-390 for mogas (Wikipedia/AvWeb).

## Rights and provenance (known so far; research, not legal advice)

Textron eAviation (Pipistrel acquired 2022). Owned by the stage 2 rights research (AER-3787).

## Safety record

Not checked.

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
