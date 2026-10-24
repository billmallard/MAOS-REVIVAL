# Bellanca (Anderson-Greenwood) T-250 Aries

Stage 1 stub, generated from `docs/longlist/candidates.json` by `docs/longlist/make_stubs.py`. Published numbers only; nothing here is our own performance check yet.

## Identity

| | |
|---|---|
| Origin | certified, out of production |
| Designer / maker | Marvin Greenwood, Anderson, Greenwood & Co. (Houston) |
| Years | first flight 1973; TC A11SW 28 Jul 1976 (Model 51), Model 51A Jun 1980; production stopped with Bellanca receivership 1980 |
| Number built | 4 flying airframes (prototype s/n 0001 + s/n 0003-0005) plus 1 static-test airframe |
| Survivors / registered | 4 registered, all valid (FAA registry 2026-10-24); 3 standard + prototype as experimental |
| Seats | 4 |
| Configuration | Low wing single, 4-5 seats, T-tail stabilator, retractable tricycle gear |
| Construction | All-aluminum, flat skins and single curves, flush riveted; laminar constant-chord wing |
| Engine | Lycoming O-540-A4D5, 250 hp, carbureted (51A: IO-540-C4B5) |

## Published numbers

Grades: F factory/brochure/designer claim; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder-fleet, registry or owner data; R measured record; E estimate (whose is stated).

| Quantity | Value | Grade | Source | Note |
|---|---|---|---|---|
| MTOW | 3,150 lb | T | [source](https://drs.faa.gov/api/content/alf/5b718d89-7d42-46a1-b537-9a3fbe563124) | - |
| Empty weight | 1,850 lb | F | [source](https://aeroresourcesinc.com/uploads/197703-1977%20Bellanca%20Aries%20T-250.pdf) | dry; Plane & Pilot 2010 lists 1,888 |
| Useful load | 1,300 lb | F | [source](https://aeroresourcesinc.com/uploads/197703-1977%20Bellanca%20Aries%20T-250.pdf) | AOPA spec table; 1,262 using P&P empty |
| Useful load, fleet or as-weighed | not found | | | |
| Usable fuel | 76 US gal | T | [source](https://drs.faa.gov/api/content/alf/5b718d89-7d42-46a1-b537-9a3fbe563124) | usable (80 total) |
| Published range | 1,017 nm | F | [source](https://aeroresourcesinc.com/uploads/197703-1977%20Bellanca%20Aries%20T-250.pdf) | published 1,170 statute miles at economy cruise with 45-min reserve (AOPA table labels the power 55%, its economy speed line says 65%); 990 sm (860 nm) at 75% with 45-min reserve; altitude not stated |

Cruise settings (P = screened as published, M = screened as measured; the basis follows the grade unless a setting states it):

| KTAS | Altitude, ft | Power | Fuel flow, gph | Grade | Source | Note |
|---|---|---|---|---|---|---|
| 180.7 M | 6500 | 73% | - | P | [source](https://aeroresourcesinc.com/uploads/197703-1977%20Bellanca%20Aries%20T-250.pdf) | AOPA Pilot flight check Mar 1977, prototype N51AG, 208 mph TAS, 22.5 inHg full throttle / 2300 rpm, partially loaded (weight not stated) |
| 180.7 P | - | 75% | - | F | [source](https://aeroresourcesinc.com/uploads/197703-1977%20Bellanca%20Aries%20T-250.pdf) | manufacturer normal cruise 208 mph; altitude not stated |
| 173.8 | - | 65% | - | F | [source](https://aeroresourcesinc.com/uploads/197703-1977%20Bellanca%20Aries%20T-250.pdf) | manufacturer economy cruise 200 mph; altitude not stated |

## Screen (published numbers; like for like)

Two screens, never mixed: the maker's figures as published, and measured or reported data. The three targets are separate floors; payload at 1,000 nm is information only.

- **As published: pass, speed unconditioned**
  - Useful load: 1,300 lb (pass) against 1,000 lb.
  - Range: 1,017 nm (pass; published 1,170 statute miles at economy cruise with 45-min reserve (AOPA table labels the power 55%, its economy speed line says 65%); 990 sm (860 nm) at 75% with 45-min reserve; altitude not stated) against 1,000 nm.
  - Cruise: 181 KTAS at an unstated altitude (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): 879 / cannot @ 174 kt, 12.2 gph (est. flow).
- **Measured or reported: partial: speed pass**
  - Useful load: - lb (?) against 1,000 lb.
  - Range: - nm (?; none found) against 1,000 nm.
  - Cruise: 181 KTAS at 6,500 ft (pass+) against >160 KTAS (>180 preferred).
  - Payload at 1,000 nm (information): cannot be computed on this basis.
- Aeromomentum fit (first cut): Yes: AM20T (260 hp) for 250 hp.

Sanity flags:

- screen speed has no altitude, or is below 6,000 ft

## Why it died

Anderson Greenwood took control of a struggling Bellanca to build the Aries at Alexandria MN. The Viking plant was nearly idle in 1977 and A-G still had to raise production capital (AOPA 1977). Bellanca went into receivership in 1980 (Plane & Pilot), reportedly drained by the Skyrocket II program. Only about 4 flying airframes were completed. No safety or technical failure is recorded.

## Idea ledger (what a new airplane should keep; AERO's judgement)

- A laminar, constant-chord, flush-riveted metal wing on a fuselage built from flat and single-curve skins to cut production cost: speed (181 KTAS at 6,500 ft on 73% of 250 hp, AOPA 1977) from a design meant to be cheap to build.
- A 250 hp, 1,300 lb useful, four-to-five-seat airframe that is a direct AM20T-class fit; its type certificate (A11SW) is still current and apparently dormant.
- Lesson: it died with its producer (Bellanca's 1980 receivership), not on a technical or safety failure; one NTSB record in about 50 years, on four aircraft.

## Rights and provenance (known so far; research, not legal advice)

TCDS A11SW (Current, Rev 2 1980): holder Anderson, Greenwood and Company, Houston, former holder Bellanca. The A-G valve business later passed via Keystone/Tyco/Pentair to Emerson (secondary sources, unverified), so the TC may sit dormant with a valve company. Owned by the stage 2 rights research (AER-3787).

## Safety record

One NTSB record in about 50 years: FTW83LA173 (1983, N51AG prototype), a taxi brake failure with gear collapse and no injuries. AOPA test noted narrow gear track and weak yaw damping.

## Not yet done

- Independent performance check (drag build-up, propeller, Breguet): stage 3, shortlist only.
- Installed-weight and cooling comparison against the Aeromomentum engine.
- What a modern rebuild changes (MANUFACTURING, stage 4).
