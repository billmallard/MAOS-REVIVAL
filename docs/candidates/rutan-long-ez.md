# Rutan Long-EZ

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Burt Rutan, Rutan Aircraft Factory (Model 61) |
| Years | 1979 first flight; plans 1980-85 |
| Number built | ~833 US-registered (2021, second-hand registry figure) |
| Survivors / registered | >700 registered (Kitplanes 2020) |
| Seats | 2 |
| Configuration | Canard pusher, tandem 2 seats, fixed mains, retractable nose |
| Construction | Moldless foam/fiberglass |
| Engine | Lycoming O-235, 108-118 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 1,325 lb | F | [source](https://en.wikipedia.org/wiki/Rutan_Long-EZ) | 1,425 lb allowed under conditions |
| Empty weight | 710 lb | F | [source](https://en.wikipedia.org/wiki/Rutan_Long-EZ) | - |
| Useful load | 615 lb | F | [source](https://en.wikipedia.org/wiki/Rutan_Long-EZ) | derived |
| Useful load, fleet or as-weighed | 475 lb | B | [source](https://www.kitplanes.com/buying-used-long-ez/) | 1,325 - ~850 lb typical O-235 empty weight (anecdotal, not averaged) |
| Usable fuel | 52 US gal | F | [source](https://en.wikipedia.org/wiki/Rutan_Long-EZ) | - |
| Published range | 1,243 nm | F | [source](https://aeropedia.com.au/content/rutan-long-ez/) | 40% power, 40 min reserve |

Cruise settings (the starred row is the one screened for speed):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 159 * | 8000 | - | - | F | [source](https://aeropedia.com.au/content/rutan-long-ez/) | max cruising, 183 mph converted |
| 125 | 12000 | 40% | - | F | [source](https://aeropedia.com.au/content/rutan-long-ez/) | 144 mph converted |

## Screen (stage 1, published numbers)

- **Verdict: fail** - UL -525 lb, speed -1 kt
- Useful load: 475 lb (fail) against 1,000 lb.
- Range: 1,884 nm still-air (pass; basis: calc, est. flow) against 1,000 nm.
- Cruise: 159 KTAS at 8,000 ft (near) against >160 KTAS (>180 preferred).
- Payload at 1,000 nm: 309 lb with no reserve; 294 lb with a 45 min reserve. Setting: 125 KTAS at 3.4 gph (fuel flow is our estimate at 0.45 lb/hp/h, grade E).
- Aeromomentum fit (first cut): Yes: AM15 (120 hp) for 115 hp.

Sanity flags:

- published range 1,243 nm vs 1,884 nm from fuel and flow
- fleet useful load 140 lb below factory

## Why it died

RAF stopped selling all plans in June 1985 over product-liability exposure after a lawsuit (Wikipedia, Rutan VariEze).

## Rights and provenance (known so far; research, not legal advice)

Rutan Aircraft Factory retains rights; plans not sold. Owned by the stage 2 rights research (AER-3787).

## Safety record

Wikipedia (Feb 2023): 114 airframes lost, 44 fatalities.

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
