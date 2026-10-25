# Legacy design survey — the brief

**Owner:** Bill Mallard. **Set:** 2026-10-24. **Board record:** `ORG-010` in
maos-workspace (`makerplane/decisions/`).

## Why

**Amended 2026-10-24 (Bill, reviewing stages 1-4):** the survey exists to **surface
promising designs that were commercial failures, and the ideas they proved, so we
can build on them.** Passing the targets is one lens, not the only one. A design
that misses them but carries an idea worth keeping (the Rohr 2-175's planform and
layout, for example) belongs in the analysis. Every dossier now carries an **idea
ledger**: what the design got right that a new airplane should keep.

AeroCommons is changing strategy for the airframe. Instead of designing an
all-new aircraft, we look for **old designs that already work** — experimental
or certified, built or only prototyped — that meet the mission below, and ask
whether one deserves to be revived and improved with modern manufacturing.

The engine question is settled for now: the **Aeromomentum** line is the
baseline powerplant. It meets Bill's price and design targets and the board's
own clean-sheet engine work could not beat it. Its gap is that it is not open
source. A candidate airframe has to work with an Aeromomentum engine, or the
dossier must say plainly what power it needs instead.

## The mission targets

| Target | Value | Preferred |
|---|---|---|
| Useful load | 1,000 lb, a target | more |
| Range | 1,000 nm, a target | more |
| Cruise speed, at altitude | above 160 KTAS, a floor | above 180 KTAS |
| Seats | 2, 4 or 6 — survey all three classes | |

- **Turbocharging is expected.** State the cruise altitude and power setting
  behind every speed. A sea-level brochure speed is not a cruise number.
- **Useful load and range are targets, not floors** (amended 2026-10-25).
  Highly efficient designs show both numbers are achievable, but there are
  tradeoffs, and some planforms suit travel and comfort better than others. A
  design that misses one is not disqualified: report how close it gets and what
  it trades away for it. There is no joint pass/fail gate on the two together;
  report the payload-range tradeoff instead, of which payload carried 1,000 nm
  with a reserve is one point. Cruise speed was not part of this amendment and
  is still a floor.
- **Each target is read on its own** (amended 2026-10-24): useful load, range
  and cruise speed are each reported separately, as Bill stated them.
- **Screen like for like.** Every candidate gets two columns: the published
  figures (screened as published), and our own check or measured data. Compare
  candidates published-to-published and measured-to-measured, never one against
  the other. Where they disagree, say why (for example the Cozy: 1,000 lb, 191
  KTAS and 1,130 nm as published, which passes; versus the CAFE-weighed 1,179 lb
  empty weight, which gives 871 lb useful).
- **Every number names its source and its quality:** factory figure, type
  certificate data sheet, flight test or magazine pilot report, builder-fleet
  average, or our own estimate. Kit-builder fleets run heavier than the
  prototype, so useful load is the number most often oversold.

**The reference point is the Cozy MKIV**: plans-built four-seat canard, ~1,000 lb
useful, high cruise on a 180–200 hp engine. Every candidate is compared with it.

## Where to look — not only at kits

1. **Experimental kits and plans**, alive or orphaned (the Cozy class, and its
   peers and predecessors).
2. **Certified types out of production**, especially fast, efficient ones whose
   type certificate is orphaned or held by a small company.
3. **Prototypes that never reached production.** Bill's example is the
   **Rohr 2-175**. What happened to it, who owns the rights, and could it be
   copied and improved with modern manufacturing?
4. **Foreign designs** that never sold in the US.

## What each candidate's dossier holds

- Identity: designer, years, number built, survivors flying.
- Configuration, seats, construction and materials.
- Published performance against the targets, with each source and how good it is.
- Our own independent check of the performance (from geometry and published
  weights), once it makes the shortlist.
- Fit with the Aeromomentum engine line: power, mass, cooling, mounting.
- **Rights and provenance:** who holds the type certificate, the drawings, the
  kit or plans rights, trademarks and any live patents. Can the design be
  bought, licensed, or lawfully re-derived?
- Why it died: market, money, liability, a technical flaw, or the founder.
- Safety record: an NTSB/accident-history summary for the type.
- What modern manufacturing would change: mass, cost and build hours.

## The deep-dive axes (added 2026-10-24, Bill)

Beyond the three targets, every shortlisted design is judged on four concerns
Bill named, and these are part of the deep dive, not footnotes:

1. **Storage.** Hangar footprint against a standard T-hangar door, height, and
   whether the wings or tail fold, or the airplane is trailerable. Span is the
   driver; the Rohr 2-175 folded both its wings and its fin.
2. **Construction with modern in-home tools.** What a builder can make in a home
   shop with a large-format 3D printer, a CNC router and a small CNC mill (molds,
   plugs, jigs, fittings), against what still has to go to a service, as well as
   the services route already costed.
3. **Safety.** Stall character (gentle or abrupt; warning; departure tendency),
   spin resistance, engine-out glide ratio, and any accident pattern tied to the
   configuration.
4. **Ride comfort.** Gust response, from the sharp-edged or Pratt gust formula
   using each design's own lift-curve slope and wing loading, alongside cabin
   room and noise where known.

**Planform is the thread through all four.** There is a live argument between
the traditional high-aspect-ratio view of efficient aircraft and an emerging
low-aspect-ratio school, especially among pusher designs. The Rohr 2-175 is a
low-aspect-ratio delta, and the Prescott Pusher is a conventional wing. The
planform study (its own board issue) weighs that trade for this mission, and
every dossier states its aspect ratio and where it sits in that argument.

## Rules

- **Diverge before converging.** Stage 1 is an unranked long list of at least 25
  candidates across all three seat classes and all four origins. Ranking comes
  after the long list is posted.
- **Rights research is research, not legal advice.** Find the owners and the
  status. Mark where an aviation IP attorney is needed. **Nobody contacts a
  rights holder, a type-certificate holder or a designer's estate without
  Bill's go-ahead.**
- Honest numbers only. A candidate that misses a target by a little still goes
  on the list, with the miss stated. Do not drop it, and do not round it up.

## Stages

1. **Long list** (AERO): 25 or more candidates with published numbers, sources
   and a screen against the targets. No ranking.
2. **Rights and provenance** (Elon, in parallel): ownership and status for each
   candidate that passes or nearly passes the screen, starting with the Rohr
   2-175.
3. **Shortlist** (AERO): 5–8 candidates ranked on our own performance check,
   Aeromomentum fit, rights status and safety record. Then a card to Bill.
4. **Modern manufacturing** (MANUFACTURING): for each shortlisted design, what a
   modern rebuild changes in materials, tooling, mass, cost and builder hours.

Bill picks which designs, if any, go to development.
