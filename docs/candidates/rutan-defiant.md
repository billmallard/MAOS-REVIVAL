# Rutan Defiant

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Burt Rutan, RAF (Model 40) |
| Years | 1978 first flight; plans 1984-85 |
| Number built | 176 plans sets; ~30 completed |
| Survivors / registered | ~20 (Twin & Turbine 2026) |
| Seats | 4 |
| Configuration | Canard, centerline-thrust twin (push-pull), fixed-pitch props, no flaps |
| Construction | Moldless composite |
| Engine | 2x Lycoming O-320 160 hp (prototype); builders often 2x O-360 180 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,900 lb | F | [source](https://planeandpilotmag.com/rutan-defiant) | Wikipedia gives 2,997 |
| Empty weight | 1,610 lb | F | [source](https://planeandpilotmag.com/rutan-defiant) | Wikipedia gives 1,701 |
| Useful load | 1,290 lb | F | [source](https://planeandpilotmag.com/rutan-defiant) | derived from P&P |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 108 US gal | P | [source](https://www.twinandturbine.com/?p=15364) | N171D, the aircraft whose cruise is quoted; 90-120 gal across sources |
| Published range | 1,128 nm | F | [source](https://planeandpilotmag.com/rutan-defiant) | not stated |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 184 P | 8000 | 75% | 17.8 | F | [source](http://www.cozybuilders.org/Canard_Pusher/1983-10_cp-38.pdf) | RAF plans spec, Canard Pusher 38 (Oct 1983); its text says 75% power, its spec table 70%; altitude 8,000 ft from the Skymaster spec block (https://337skymaster.com/defiant.htm), not stated in CP38 |
| 162 M | 10000 | - | 16 | P | [source](https://www.twinandturbine.com/?p=15364) | N171D, 160-165 KTAS at 15-17 gph 'in the teens'; 10,000 ft used as the lower bound |
| 152 | - | - | 19 | P | [source](https://www.twinandturbine.com/?p=15364) | low altitude, 150-155 KTAS at 18-20 gph |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: pass**
  - Useful load: 1,290 lb (pass) against 1,000 lb.
  - Range: 1,128 nm (pass; not stated) against 1,000 nm.
  - Cruise: 184 KTAS at 8,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 710 / cannot @ 184 kt, 17.8 gph.
- **Measured or reported: partial: range pass, speed pass**
  - Useful load: - lb (?) against 1,000 lb.
  - Range: 1,094 nm (pass; still air, no reserve, from fuel and measured flow) against 1,000 nm.
  - Cruise: 162 KTAS at 10,000 ft (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- Aeromomentum fit (first cut): Yes: 2x AM15T (160 hp) matches the prototype's 2x 160 hp; 180 hp builds need 2x AM20T (heavier).

Sanity flags:

- none raised

## Why it died

The 1979 certification effort lost its financing; plans ended with RAF's 1985 liability stop (Wikipedia; P&P).

## Rights and provenance (known so far; research, not legal advice)

Rutan Aircraft Factory; not marketed. Owned by the stage 2 rights research (AER-3787).

## Safety record

No configuration-specific pattern found. Single-engine climb 150-400 fpm depending on which engine is out (T&T).

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
