# Bellanca T-250 Aries: build plan

**AER-3868, 2026-10-25, MANUFACTURING.** This plan turns the stage 4 notes
(`docs/MANUFACTURING.md`, PR #5) into a build plan, now that Bill has picked the
Aries (AER-3783). It sits on AERO's independent check (AER-3867, PR #13 at
`866543e`, `docs/studies/aries/`). That check keeps the standard airframe
(MTOW 3,150 lb, factory empty 1,850 lb, 76 gal usable) and shows range closing
on 84-94 gal. This plan builds in 90 gal.

Everything here is our estimate (E) unless a source is named. No drawing of
the Aries has been found: the TCDS (A11SW) gives no dimensions, and Jane's
gives the planform and little else. So the part counts below are built up from
the configuration, not counted off drawings. Prices are from public pages read
on 2026-10-25 ([price check](../manufacturing/price-check-2026-10-25.md)). No
shop, holder or museum has been contacted. Script:
`docs/manufacturing/build_plans.py`.

## The plan in brief

| | Modern matched-hole kit (small run) | One-off builder, parts cut from files |
|---|---|---|
| Route | CNC-cut, matched-hole 2024-T3 kit; the design's flat and single-curve skins kept; composite cowl, duct and fairings; AM20T; 90 gal integral | the same files, cut by OSH Cut or a home router, holes final-drilled by hand |
| Parts (excluding standard hardware) | 900-1,280, of which 460-690 unique | same |
| Made from files or molds / bought | 780-1,100 / 120-190 | same |
| Tooling | $50-185k (E) | builder's own tools, $20-34k (stage 4 home shop) |
| Kit-run crossover | tooling under 10% of a $100-150k kit after 4-19 airframes | not applicable |
| Builder hours | 2,500-3,500 (E, stage 4) | 3,500-5,000 (E, stage 4) |
| Empty weight | 1,780-2,000 lb before engine credit; 1,690-1,940 lb with it (stage 4), plus 7-14 lb for 90 gal | same |
| Skill floor | Medium: Van's-level riveting, countersinking or dimpling to laminar-wing quality, tank sealing | Medium-high: fitting and final-drilling without matched holes |

**A correction to stage 4.** Stage 4 put the Aries tooling at $40-120k and its
crossover at 3-12 airframes. Its own lines did not add up: they sum to about
$41-155k, and that left out the CAD and CNC programs. Priced as separate lines
here, the total is $50-185k and the crossover 4-19 airframes. The Aries is still
the cheapest design on the shortlist to tool, and the reason is unchanged: no
compound curves and no stretch-forming.

## 1. Part count and the make/buy split

Built by `build_plans.py`. Columns are how each part gets made: **cut** (a flat
part cut from a file), **formed** (cut, then flanged on a block, braked or
rolled), **machined** (a fitting), **molded** (composite), **bought** (an
assembly or catalogue part, counted once).

| Assembly | Parts | Unique | Cut | Formed | Machined | Molded | Bought |
|---|---|---|---|---|---|---|---|
| Wing structure, both halves (spars, ribs, skins, stringers, tank bay, gear bay) | 258-340 | 55-80 | 130-170 | 110-140 | 12-20 | | 6-10 |
| Flaps and ailerons (4 surfaces) | 70-95 | 25-35 | 25-35 | 40-50 | 4-8 | | 1-2 |
| T-tail: stabilator, fin, rudder, anti-servo tab | 90-130 | 60-90 | 40-55 | 40-60 | 8-12 | | 2-3 |
| Fuselage (frames, longerons, stringers, skins, floor, carry-through, doors) | 250-350 | 150-220 | 120-165 | 100-140 | 15-25 | | 15-20 |
| Landing gear and doors (retractable tricycle) | 40-60 | 25-35 | 12-18 | 10-15 | 8-12 | | 10-15 |
| Flight controls | 60-90 | 40-60 | 15-20 | 10-15 | 20-30 | | 15-25 |
| Fuel system, 90 gal integral | 25-40 | 15-25 | 8-12 | 4-8 | 2-4 | | 11-16 |
| Firewall forward, AM20T | 30-50 | 25-40 | 8-12 | 4-8 | 3-6 | 3-5 | 12-19 |
| Composite fairings (cowl, tips, fin cap, fillets, gear-door fairings) | 12-18 | 10-14 | | | | 12-18 | |
| Cabin, windows, panel, seats, interior | 40-70 | 30-50 | 10-20 | 5-10 | | 0-4 | 25-36 |
| Electrical and avionics | 25-40 | 25-40 | | | | | 25-40 |
| **Total** | **900-1,283** | **460-689** | 368-507 | 323-446 | 72-117 | 15-27 | 122-186 |

**Why the wing is cheap.** The wing is constant-chord, so 16 rib stations of
three pieces each, on both wings, make 96 ribs. They come from three standard
shapes plus 10-15 specials (root, tank ends, gear bay, hinge ribs). The wing is
over a quarter of the airframe's parts but about an eighth of its unique parts. The
fuselage and the tail carry most of the unique-part count. No tail drawing has
been found, so we assume the tail surfaces are tapered, with unique ribs.

**What gets bought:** gear legs, retract actuators, wheels and brakes; the
engine and its welded mount; the propeller; the radiator and exhaust; fuel
pumps, selector, senders and filters; windows and windshield (formed acrylic);
seats or seat frames; avionics and wiring. We have not found a catalogue main
gear for a 3,150 lb retractable single. The gear legs are probably a service
part made to drawing, at a price not checked. Gear actuation and leg sourcing
is the largest open item on the bought side.

**What never comes from a home shop:** gear legs, the engine mount, heat-treated
fittings (the wing carry-through and the stabilator hinge and torque tube if
they are heat-treated), and anything a service brakes in 2024-T3 at a radius the
builder cannot check.

## 2. What is cut, formed, molded or printed, and by whom

| Work | Route | Service named (public page, 2026-10-25) | Limit found |
|---|---|---|---|
| Skins, ribs, frames, doublers in 2024-T3, 0.032 in and up | laser-cut from files, pilot-holed | OSH Cut lists 2024-T3 at 0.032, 0.04, 0.05, 0.063, 0.08, 0.09, 0.1, 0.125, 0.19 in ([material page](https://www.oshcut.com/materialdetails/aluminum-2024-t3), read 2026-10-26) | maximum part 119 x 47 in; no 2024-T3 bending. The 6 ft chord wrap fits within 119 in, but a 15.7 ft half-span skin needs at least one spanwise splice |
| Thin 2024-T3 (0.025 in) | laser-cut | SendCutSend, 0.025 in only, instant pricing to 30 x 44 in | small parts only |
| Parts over 119 x 47 in | home router (Avid PRO4896, stage 4) or a full-service shop (not contacted) | | 4 x 8 ft bed; or splice to fit |
| Rib, frame and stringer flanges | hand or press forming on routed form blocks; long bends at a brake service | form blocks routed from HDU or MDF; brake service not priced | 2024-T3 needs larger bend radii than the 5052 and mild steel that brake services are set up for |
| Fittings, bellcranks, hinge brackets | CNC-machined | Xometry, Protolabs (instant quote by upload; not run) | heat-treated fittings to a service with certs |
| Cowl, radiator duct, tips, fin cap, fillets, gear-door fairings | room-temperature infusion in glass/epoxy molds from HDU plugs | plug board: Precision Board PBLT-15, $62.63 for 0.5 x 20 x 60 in (Interstate) | 65-70 ft2 of mold surface |
| Small molds, drill guides, jigs | printed | Xometry FDM to 24 x 36 x 36 in; Additive Plus FGF to 2 m (both price by upload) | no public price |

**The optional laminar wing skin.** AERO's check puts the biggest single drag
item at the wing's laminar run: from 25% to 40% chord is worth about +6 KTAS and
+24 nm (AER-3867). That needs a smooth bonded or composite skin, a manufacturing
choice. The Aries makes it unusually cheap to tool. Its section is constant
along the span, so one upper and one lower skin mold of about 230 ft2 of mold
surface ($28-83k, E) could make both wings, if the wing has no twist. Nobody has
yet confirmed whether it does. **That skin is load-bearing.** A composite wing
skin is primary structure, and its laminate schedule is a STRUCTURES job. The
metal kit above does not depend on it.

## 3. Tooling, for a small kit run

| Line | Cost (E) | Basis |
|---|---|---|
| CAD and CNC programs (cut files, form-block files) | $10-30k | E; one engineer re-deriving and checking a drawing set from a measured airframe |
| Form blocks and dies, 150-250 unique formed parts | $22-100k | $150-400 per block or die (stage 4) |
| Assembly jigs (wing, fuselage, tail) | $10-30k | E |
| Molds: cowl, radiator duct, tips, fairings, 65-70 ft2 | $8-25k | $120-360 per ft2 of mold surface (stage 4). The HDU price check supports the $15-40 per ft2 plug-material line inside it |
| **Total** | **$50-185k** | |
| Option: laminar skin molds, about 230 ft2 | $28-83k | same rate; one set serves both wings only if the wing is untwisted |

**One-off builder against a kit run.** A one-off builder pays no kit tooling.
They pay for their own tools (stage 4's home shop, $20-34k) and 600-1,200 more
hours of cutting, deburring and drilling. That works only once someone has
published the CAD files, and whether that is lawful is a rights question for
Elon. A kit run spreads $50-185k across the airframes. At 10 kits it adds
$5-19k to each; tooling falls under 10% of the kit price after 4-19 airframes.

## 4. The 90 gallons

AERO's closers need 84.7-86.4 gal usable for 1,000 nm plus 45 minutes at 65%
of take-off power, and 91.8-94.1 gal at full continuous (AER-3867), against 76 gal standard. We plan 90 gal.

- **Volume per foot of bay.** Stage 4 put it at 11 gal per foot of span
  between the spars. A spar box from 15-20% to 55-60% chord, at an average 11%
  of the 65 in chord and 90% usable, holds 7.6-9.8 gal per foot (E). AERO's
  8-9 sits inside that, so stage 4's 11 was high, and this corrects it.
- **Length.** 14 more gallons is 0.7-0.9 ft more bay per wing, or 0.9-1.2 ft for
  the 18 gal AERO's AM-low case needs at full continuous power. The constant
  chord means it is more of the same ribs, with no new tooling.
- **Weight.** 7-14 lb empty (Raymer's 0.5 lb per gal, as AERO used, up to our
  stage 4 rate). Fuel and payload trade as in AERO's payload-range table.
- **What we can't see.** We don't know where the original tank bay ends or what
  sits outboard of it. Without a drawing, the 0.7-1.2 ft is an envelope, not a
  tank design.

## 5. Is the structure load-bearing work we can't do?

- **The metal kit, as planned:** no laminate. Gauges come from the original
  drawings if the rights route recovers them (Elon, AER-3805). Otherwise they
  come from a measured airframe, and re-deriving gauges for primary structure is
  a STRUCTURES job.
- **The laminar skin option:** yes. It is a load-bearing composite skin, and the
  laminate schedule is a STRUCTURES job.
- **A higher MTOW** for 1,000 lb of payload over 1,000 nm (+160 to +280 lb,
  AER-3867) is a structural re-substantiation. It is not in this plan.

## What would replace these estimates

- The Aries drawings, through the TC-holder route (Elon). They would replace
  every part count above with a count off the drawing tree.
- One measured airframe (contact is Bill's call). It would settle the wing
  twist, the tank-bay boundaries and the tail geometry.
- A gear-leg source and its price.
