# Socata TB-21 Trinidad TC

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | foreign design |
| Designer / maker | Socata (Aerospatiale), France |
| Years | 1985-2012 |
| Number built | TB family 2,150; TB-21 count not found |
| Survivors / registered | not counted |
| Seats | 4 |
| Configuration | Low wing, 4-5 seats, retractable gear |
| Construction | All-metal |
| Engine | Lycoming TIO-540-AB1AD, 250 hp, turbo |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 3,086 lb | T | [source](https://easa.europa.eu/cs/downloads/7156/en) | - |
| Empty weight | 1,915 lb | P | [source](https://peter2000.co.uk/aviation/tb20-experience/1991-03%20AOPA%20PILOT%20-%20TB21%20Cause%20Celebre.pdf) | standard |
| Useful load | 1,182 lb | P | [source](https://peter2000.co.uk/aviation/tb20-experience/1991-03%20AOPA%20PILOT%20-%20TB21%20Cause%20Celebre.pdf) | standard |
| Useful load, fleet or as-weighed | 980 lb | P | [source](https://peter2000.co.uk/aviation/tb20-experience/1991-03%20AOPA%20PILOT%20-%20TB21%20Cause%20Celebre.pdf) | heavily equipped test aircraft, 2,117 lb empty |
| Usable fuel | 86.2 US gal | T | [source](https://easa.europa.eu/cs/downloads/7156/en) | - |
| Published range | 1,030 nm | P | [source](https://planeandpilotmag.com/article/socata-1999-trinidad-tc/) | 65%, with reserve |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 187 P | 25000 | 75% | 16.4 | P | [source](https://peter2000.co.uk/aviation/tb20-experience/1991-03%20AOPA%20PILOT%20-%20TB21%20Cause%20Celebre.pdf) | factory-calculated, AOPA matched flow |
| 169 M | 25000 | 65% | 12.4 | P | [source](https://peter2000.co.uk/aviation/tb20-experience/1991-03%20AOPA%20PILOT%20-%20TB21%20Cause%20Celebre.pdf) | - |
| 141 | 17000 | 55% | 11.1 | P | [source](https://peter2000.co.uk/aviation/tb20-experience/1991-03%20AOPA%20PILOT%20-%20TB21%20Cause%20Celebre.pdf) | - |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: pass**
  - Useful load: 1,182 lb (pass) against 1,000 lb.
  - Range: 1,030 nm (pass; 65%, with reserve) against 1,000 nm.
  - Cruise: 187 KTAS at 25,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot (983 nm max).
- **Measured or reported: near miss** - UL -20 lb
  - Useful load: 980 lb (near) against 1,000 lb.
  - Range: 1,175 nm (pass; still air, no reserve, from fuel and measured flow at 169 KTAS) against 1,000 nm.
  - Cruise: 169 KTAS at 25,000 ft (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 540 / 484 @ 169 kt, 12.4 gph.
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 250 hp.

Sanity flags:

- fleet useful load 202 lb below factory

## Why it died

Build-to-order after 9/11; all marketing and production ended by 2012 (Wikipedia citing Flight).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- A turbocharged four-seater with a roomy cabin from a large European maker; ended by the post-2001 market, not the design.

## Rights and provenance (known so far; research, not legal advice)

EASA TC holder: Daher Aircraft SAS. FAA TCDS A51EU. Owned by the stage 2 rights research (AER-3787).

## Safety record

Not researched.

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
