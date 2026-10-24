# Prescott Pusher

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | experimental kit or plans |
| Designer / maker | Tom Prescott, Prescott Aeronautical |
| Years | 1985 first flight; kits to ~1989 |
| Number built | 68 kits (Wings Over Kansas); 19 airframes ever on the US register (FAA registry 2026-10-24), plus at least 2 abroad |
| Survivors / registered | 4 current US registrations (N41PP museum, N10JS, N200SX, N40LE); 2 likely airworthy |
| Seats | 4 |
| Configuration | Pusher, 4 seats (2+2), engine in the tail cone on a 12 in prop extension (no drive shaft), T-tail, retractable or fixed tricycle gear |
| Construction | TIG-welded 4130 square-tube cage with non-structural fibreglass shells; riveted aluminium wing, NLF(1)-0215F; CAD/CAM-designed to Part 23 |
| Engine | Lycoming O-360, 180 hp |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 2,400 lb | F | [source](https://1000aircraftphotos.com/Contributions/6802.htm) | - |
| Empty weight | 1,550 lb | F | [source](https://1000aircraftphotos.com/Contributions/6802.htm) | - |
| Useful load | 850 lb | F | [source](https://1000aircraftphotos.com/Contributions/6802.htm) | - |
| Useful load, fleet or as-weighed | 739 lb | P | [source](http://web.archive.org/web/20241217134717/https://p.pdfhall.com/russ-and-marcia-taylors-prescott-pusher_5b6d873e097c4748748b4604.html) | one builder aircraft weighed (N747P: 1,555 lb in the shop, 1,661 lb finished with ballast for CG; Jack Cox, Sport Aviation, September 1991); not a fleet average |
| Usable fuel | 56.5 US gal | F | [source](https://1000aircraftphotos.com/Contributions/6802.htm) | second prototype |
| Published range | 869 nm | F | [source](https://1000aircraftphotos.com/Contributions/6802.htm) | not stated (1,000 mi) |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 151 M | - | 73% | - | P | [source](https://www.kitplanes.com/archive-may-1988/) | measured, Kitplanes May 1988 (LeRoy Cook), second prototype N42PP; altitude, weight and rpm not published |
| 165 P | 7500 | - | - | F | [source](https://1000aircraftphotos.com/Contributions/6802.htm) | brochure, 190 mph converted |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: fail** - UL -150 lb, range -131 nm
  - Useful load: 850 lb (fail) against 1,000 lb.
  - Range: 869 nm (fail; not stated (1,000 mi)) against 1,000 nm.
  - Cruise: 165 KTAS at 7,500 ft (pass) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot (866 nm max).
- **Measured or reported: partial: UL fail, speed near, speed unconditioned** - UL -261 lb, speed -9 kt
  - Useful load: 739 lb (fail) against 1,000 lb.
  - Range: - nm (?; none found) against 1,000 nm.
  - Cruise: 151 KTAS at an unstated altitude (near) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot (866 nm max).
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 180 hp.

Sanity flags:

- fleet useful load 111 lb below factory
- Bill's top-interest design (AER-3783, 2026-10-24): full deep dive in the stage 3 dossier

## Why it died

Early handling and performance disappointment tied to a far-aft CG (pitch sensitivity, hard rotation), a financing change from pay-as-you-build to pay-up-front (Tom Prescott, 2007), slow parts, and a 1988 sale abroad; folded 1989-1991 with builders mid-kit (Kitplanes; SDASM; Sport Aviation).

## Idea ledger (what a new airplane should keep; AERO's judgement)

- A pusher without a drive shaft: engine in the tail cone, prop on a 12 in extension; no drive failure on record.
- A welded tube cage with all systems installed before non-structural shells go on; CAD/CAM-designed from the start; the engineering archive survives at SDASM.
- Lesson: an engine in the tail sets the CG, gear position and prop clearance together; the Prescott's handling complaints trace to that.

## Rights and provenance (known so far; research, not legal advice)

No TC. Engineering record survives at SDASM (SC.10269); rights holder unknown (docs/rights/prescott-pusher.md, PR #6). Owned by the stage 2 rights research (AER-3787).

## Safety record

4 confirmed US NTSB events, 1 fatal (Ford V-6 conversion, LAX90DUM02), plus a probable fifth (fatal, Ford V-6). Pusher-specific: a door into the prop (CEN09CA386) and a prop separation (LAX05LA270). Pitch-up stall in a go-around (MIA92LA186).

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
