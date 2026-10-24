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
| Useful load | 1,452 lb | F | [source](https://en.wikipedia.org/wiki/Mooney_301) | design figure: 4,000 gross less 2,548 empty (Air International Airdata File, Jan 1984), not stated as weighed; Mooney's spec sheet claims 1,600 |
| Useful load, fleet or as-weighed | not found | | | |
| Useful load, as-flown estimate | 1,252 lb | E | [source](https://mooneyevents.com/Mooney301.html) | AERO lower-bound estimate: 1,452 less the prototype's ~200 lb weight overrun (Mooney Events; Wikipedia; docs/rights/mooney-301.md). If 2,548 lb already includes the overrun, ~1,400 (1,600 less 200). Never weighed in public record |
| Usable fuel | 100 US gal | F | [source](https://mooneyevents.com/Mooney301.html) | capacity |
| Published range | 986 nm | F | [source](https://mooneyevents.com/Mooney301.html) | cruise, 45 min reserve |

Cruise settings (the starred row is the one screened for speed):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 235 * | 25000 | 75% | 19.7 | F | [source](https://mooneyevents.com/Mooney301.html) | design/marketing figure at 'max altitude', 75% (Mooney spec sheet), not a flight-test result. The prototype was 'slower than desired' with aero work unfinished; no as-flown cruise is published (Mooney Events; docs/rights/mooney-301.md) |
| 225 | - | - | - | F | [source](https://en.wikipedia.org/wiki/Mooney_301) | 259 mph cruise, Jane's 1983-84 pp. 444-445 (via Wikipedia); conditions not stated; also a design-era figure |

## Screen (stage 1, published numbers)

- **Verdict: pass**
- Useful load: 1,252 lb (pass) against 1,000 lb.
- Range: 1,193 nm still-air (pass; basis: calc) against 1,000 nm.
- Cruise: 235 KTAS at 25,000 ft (pass+) against >160 KTAS (>180 preferred).
- Payload at 1,000 nm: 749 lb with no reserve; 660 lb with a 45 min reserve. Setting: 235 KTAS at 19.7 gph.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 360 hp (-10% speed, est. 211 KTAS).

Sanity flags:

- published range 986 nm vs 1,193 nm from fuel and flow
- as-flown useful load estimate 200 lb below the published design figure
- useful load and cruise are design figures; the only prototype was ~200 lb over projected weight and 'slower than desired', and no as-flown speed or weight is published (Mooney Events; docs/rights/mooney-301.md)
- the published 986 nm range is a 45 min reserve figure; fuel and flow give 1,016 nm on that basis, consistent within 3%
- 1,000 nm plus 45 min at 235 kt and 19.7 gph needs 98.6 of 100 gal with no climb allowance; below 231 KTAS at the same flow (about 4 kt under the design figure) it cannot carry the reserve (at Jane's 225 kt it needs 102 gal)
- 235 KTAS at 270 hp, 25,000 ft, 4,000 lb implies CD0 ~0.019 (AR 9.0, e 0.80, prop eta 0.80; AERO, grade E), optimistic for a 1983 pressurized single; at CD0 +20% the same power gives ~220 KTAS, still a pass on speed

## Why it died

Republic Steel's takeover by LTV forced the sale of Mooney. The prototype was about 200 lb over its projected weight and, with aero work unfinished, slower than desired; the new French-led owners wanted close to 300 kt, which needed a turbine, and moved the effort into the Socata joint venture that became the TBM 700 (Mooney Events; Plane & Pilot; docs/rights/mooney-301.md).

## Rights and provenance (known so far; research, not legal advice)

No TC; one prototype, scrapped. M30 data went to Socata in 1987; whether Mooney International or Daher holds it is not shown (docs/rights/mooney-301.md). Owned by the stage 2 rights research (AER-3787).

## Safety record

No accidents found.

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
