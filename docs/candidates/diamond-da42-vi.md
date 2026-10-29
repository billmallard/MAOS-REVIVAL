# Diamond DA42-VI (similar-engine comparison)

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | foreign design |
| Designer / maker | Diamond Aircraft Industries, Wiener Neustadt, Austria |
| Years | Current production; new DA42-VI demonstrator debuted publicly at AERO 2026 |
| Number built | - |
| Survivors / registered | In production |
| Seats | 4 |
| Configuration | Low wing light twin, 4 seats, retractable gear |
| Construction | Composite |
| Engine | 2x Austro Engine AE 300 turbocharged 2.0 L diesel, 168 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 4,407 lb | F | [source](https://www.diamondaircraft.com/en/private-owners/aircraft/da42/tech-specs/) | 1,999 kg, factory |
| Empty weight | 3,131 lb | F | [source](https://www.diamondaircraft.com/en/private-owners/aircraft/da42/tech-specs/) | 1,420 kg 'without options', factory |
| Useful load | 1,276 lb | F | [source](https://www.diamondaircraft.com/en/private-owners/aircraft/da42/tech-specs/) | 579 kg 'Max. useful load', factory |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 76.4 US gal | F | [source](https://www.diamondaircraft.com/en/private-owners/aircraft/da42/tech-specs/) | capacity 289 L incl. 100 L auxiliary tank (main 189 L = 50.0 gal); factory conversion |
| Published range | 1,100 nm | F | [source](https://www.diamondaircraft.com/en/private-owners/aircraft/da42/tech-specs/) | 60% power, 12,000 ft, incl. auxiliary tank, incl. climb, no reserves; nautical. Max range 1,225 nm at FL180, 50% power, no reserves. Fuel burn at 60% = 10.4 US gal/h total |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 175 | 16000 | 75% | - | F | [source](https://www.diamondaircraft.com/en/private-owners/aircraft/da42/tech-specs/) | Cruise at 75%, 16,000 ft, MTOM, ISA (324 km/h TAS) |
| 190 P | 16000 | - | - | F | [source](https://www.diamondaircraft.com/en/private-owners/aircraft/da42/tech-specs/) | Max cruising speed at MCP, 16,000 ft, MTOM, ISA (352 km/h TAS) |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. Useful load and range are targets: a miss is reported with its size, and payload against range is the tradeoff to read. Cruise above 160 KTAS is a floor.

- **As published: pass**
  - Useful load: 1,276 lb (pass) against 1,000 lb.
  - Range: 1,100 nm (pass; 60% power, 12,000 ft, incl. auxiliary tank, incl. climb, no reserves; nautical. Max range 1,225 nm at FL180, 50% power, no reserves. Fuel burn at 60% = 10.4 US gal/h total) against 1,000 nm.
  - Cruise: 190 KTAS at 16,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm, lb, no reserve / 45 min: cannot (707 nm max).
- **Measured or reported: no data found.**
- Aeromomentum fit (first cut): Yes: 2x AM20T (260 hp) for 168 hp.

Sanity flags:

- published range 1,100 nm vs 707 nm from fuel and flow

## Why it died

Similar-engine comparator, not Rotax. The DA42-VI demonstrator debuted at AERO 2026 (Diamond release 7 May 2026). At AERO 2025 Diamond showed only a DA50 and a DA62; no DA42 was named (Diamond Diary 29 Apr 2025; fliegermagazin 9 Apr 2025). Price not published.

## Idea ledger (what a new airplane should keep; AERO's judgement)

- A light twin on two automotive-derived 2.0 L turbodiesels: the nearest certified precedent for twin automotive-derived engines, and a benchmark for an Aeromomentum twin.

## Rights and provenance (known so far; research, not legal advice)

Current OEM type (Diamond) Owned by the stage 2 rights research (AER-3787).

## Safety record

Not checked here

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
