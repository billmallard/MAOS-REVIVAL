# Cirrus VK-30

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Alan and Dale Klapmeier, Jeff Viken, Cirrus Design |
| Years | 1988 first flight; kits 1988-93 |
| Number built | ~40 kits delivered; ~13 completed |
| Survivors / registered | 4 FAA-registered (2018, peak 12) |
| Seats | 5 |
| Configuration | Mid-engine pusher with extension shaft, 4-5 seats, retractable gear, laminar wing |
| Construction | Composite |
| Engine | Continental IO-550 300 hp or Lycoming IO-540 290 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 3,550 lb | F | [source](https://aeroresourcesinc.com/uploads/199004-1990%20Cirrus%20VK30%20Homebuilt.pdf) | AOPA Pilot spec box; EAA museum gives 3,600 |
| Empty weight | 2,200 lb | F | [source](https://aeroresourcesinc.com/uploads/199004-1990%20Cirrus%20VK30%20Homebuilt.pdf) | prototype; EAA museum gives 2,400 |
| Useful load | 1,350 lb | F | [source](https://aeroresourcesinc.com/uploads/199004-1990%20Cirrus%20VK30%20Homebuilt.pdf) | - |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 95 US gal | F | [source](https://aeroresourcesinc.com/uploads/199004-1990%20Cirrus%20VK30%20Homebuilt.pdf) | - |
| Published range | 1,130 nm | F | [source](https://www.eaa.org/eaa-museum/museum-collection/aircraft-collection-folder/1991-cirrus-vk-30---n33vk) | not stated (1,300 mi converted) |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 205 M | 4500 | 70% | 15.5 | P | [source](https://aeroresourcesinc.com/uploads/199004-1990%20Cirrus%20VK30%20Homebuilt.pdf) | prototype measured, AOPA Pilot Apr 1990 |
| 211 P | 5000 | 75% | 16.7 | F | [source](https://aeroresourcesinc.com/uploads/199004-1990%20Cirrus%20VK30%20Homebuilt.pdf) | manufacturer's calculation |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: pass, speed unconditioned**
  - Useful load: 1,350 lb (pass) against 1,000 lb.
  - Range: 1,130 nm (pass; not stated (1,300 mi converted)) against 1,000 nm.
  - Cruise: 211 KTAS at 5,000 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 875 / 800 @ 211 kt, 16.7 gph.
- **Measured or reported: partial: range pass, speed pass, speed unconditioned**
  - Useful load: - lb (?) against 1,000 lb.
  - Range: 1,256 nm (pass; still air, no reserve, from fuel and measured flow) against 1,000 nm.
  - Cruise: 205 KTAS at 4,500 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- Aeromomentum fit (first cut): Short: AM20T 260 hp vs 290 hp (-4% speed, est. 198 KTAS).

Sanity flags:

- screen speed has no altitude, or is below 6,000 ft

## Why it died

Discontinued 1993 as Cirrus moved to certified aircraft; replacement wing announced 1996 for ~28 kits (Wikipedia).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- A laminar-flow composite wing and a clean pusher fuselage that reached about 200 KTAS on 290-300 hp, the design the Cirrus team learned on before the SR20.
- Lesson: its long shaft drive, cruise-flap flutter and aft-CG spin recovery are what a pusher with a buried engine must design out.

## Rights and provenance (known so far; research, not legal advice)

Cirrus Design, now Cirrus Aircraft. No support program found. Owned by the stage 2 rights research (AER-3787).

## Safety record

7 US crashes, 10 fatalities 1990-2020 (NTSB via Wikipedia), incl. a 1996 stall-test crash in a turbine conversion; prop-governor oil line chafe forced landing on the prototype.

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
