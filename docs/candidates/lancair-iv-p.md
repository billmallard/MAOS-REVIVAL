# Lancair IV-P

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Lance Neibauer, Lancair |
| Years | IV 1991; IV-P 1994; kits ended 2012 |
| Number built | 110 IV + 250 IV-P flying by 2011 (Kitplanes) |
| Survivors / registered | ~208 IV-P registered (184 with airworthiness date) |
| Seats | 4 |
| Configuration | Low wing, 4 seats, retractable gear, pressurized |
| Construction | Composite |
| Engine | Continental TSIO-550, 350 hp, twin turbo |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 3,550 lb | F | [source](https://lancair.com/storage/2019/10/LA_LancairIV_web_f.pdf) | - |
| Empty weight | 2,200 lb | F | [source](https://lancair.com/storage/2019/10/LA_LancairIV_web_f.pdf) | - |
| Useful load | 1,350 lb | F | [source](https://lancair.com/storage/2019/10/LA_LancairIV_web_f.pdf) | - |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 106.5 US gal | P | [source](https://www.aopa.org/news-and-media/all-news/2005/april/pilot/get-up-and-go) | usable, extended tanks as tested; 82-90 gal standard across sources |
| Published range | 1,347 nm | P | [source](https://www.aopa.org/news-and-media/all-news/2005/april/pilot/get-up-and-go) | 65%, 24,000 ft, 45 min reserve (1,550 sm) |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 255 | 16500 | 75% | 17.2 | P | [source](https://www.aopa.org/news-and-media/all-news/2005/april/pilot/get-up-and-go) | best power |
| 284 M | 24000 | 65% | 17 | P | [source](https://www.aopa.org/news-and-media/all-news/2005/april/pilot/get-up-and-go) | best economy |
| 278 P | 23000 | 75% | 18 | P | [source](https://www.aopa.org/news-and-media/all-news/1994/june/pilot/lancair-iv-p) | 50 F lean of peak; below the factory claim |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: pass**
  - Useful load: 1,350 lb (pass) against 1,000 lb.
  - Range: 1,347 nm (pass; 65%, 24,000 ft, 45 min reserve (1,550 sm)) against 1,000 nm.
  - Cruise: 278 KTAS at 23,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 962 / 881 @ 278 kt, 18.0 gph.
- **Measured or reported: partial: range pass, speed pass**
  - Useful load: - lb (?) against 1,000 lb.
  - Range: 1,779 nm (pass; still air, no reserve, from fuel and measured flow at 284 KTAS) against 1,000 nm.
  - Cruise: 284 KTAS at 24,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 350 hp (-9% speed, est. 231 KTAS).

Sanity flags:

- published range 1,347 nm vs 1,779 nm from fuel and flow

## Why it died

Kits ended 2012; in 2016 the company sold older lines to concentrate on the Evolution (Wikipedia).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- Pressurisation and FL240 cruise in a kit, the fastest piston four-seater of its era (published 287 KTAS at 24,000 ft).
- Re-wing data point to follow (Oregon remanufacturer, Bill): a new wing on the same airframe as the fix for the stall-spin record.

## Rights and provenance (known so far; research, not legal advice)

Neibauer -> Bartels (2003) -> Huffstutlers, Lancair International (2017) -> JetEXE / Lancair Aerospace (2023). Owned by the stage 2 rights research (AER-3787).

## Safety record

NTSB narrative WPR12FA180: 26% of Lancairs in accidents, 19% fatal (model and period not stated); Wanttaja 1998-2007: 32 IV accidents, ~40% fatal.

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
