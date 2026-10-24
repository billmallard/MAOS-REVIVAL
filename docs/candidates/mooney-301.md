# Mooney 301

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | prototype that never reached production |
| Designer / maker | Roy LoPresti, Mooney Aircraft |
| Years | 1983 first flight; ~70 test hours |
| Number built | 1 |
| Survivors / registered | none (wings cut off; fate unknown) |
| Seats | 6 |
| Configuration | Low wing, 6 seats, retractable gear, pressurized 5.0 psi, NLF wing |
| Construction | Metal |
| Engine | Lycoming TSIO-540, 360 hp, turbo |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 4,000 lb | F | [source](https://mooneyevents.com/Mooney301.html) | - |
| Empty weight | 2,548 lb | F | [source](https://en.wikipedia.org/wiki/Mooney_301) | Air International Jan 1984 |
| Useful load | 1,452 lb | F | [source](https://en.wikipedia.org/wiki/Mooney_301) | derived; Mooney newsletter claims 1,600 |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 100 US gal | F | [source](https://mooneyevents.com/Mooney301.html) | capacity |
| Published range | 986 nm | F | [source](https://mooneyevents.com/Mooney301.html) | cruise, 45 min reserve |

Cruise settings (the starred row is the one screened for speed):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 235 * | 25000 | 75% | 19.7 | F | [source](https://mooneyevents.com/Mooney301.html) | at 'max altitude'; prototype reportedly reached only 260 kt top speed |

## Screen (stage 1, published numbers)

- **Verdict: pass**
- Useful load: 1,452 lb (pass) against 1,000 lb.
- Range: 1,193 nm still-air (pass; basis: calc) against 1,000 nm.
- Cruise: 235 KTAS at 25,000 ft (pass+) against >160 KTAS (>180 preferred).
- Payload at 1,000 nm: 949 lb with no reserve; 860 lb with a 45 min reserve. Setting: 235 KTAS at 19.7 gph.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 360 hp (-10% speed, est. 211 KTAS).

Sanity flags:

- published range 986 nm vs 1,193 nm from fuel and flow

## Why it died

Republic Steel's takeover by LTV forced the sale of Mooney; the new French-led owners judged the 301 ~200 lb heavy and too slow (Wikipedia).

## Rights and provenance (known so far; research, not legal advice)

Mooney (now Mooney International) vs Daher (TBM lineage): whether 301 data sits with either is not found. Owned by the stage 2 rights research (AER-3787).

## Safety record

No accidents found.

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
