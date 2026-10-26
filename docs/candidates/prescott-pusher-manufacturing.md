# Prescott Pusher: build plan

**AER-3868, 2026-10-25, MANUFACTURING.** This plan turns the stage 4 notes
(`docs/MANUFACTURING.md`, PR #5) into a build plan, now that Bill has picked the
Prescott (AER-3783). It sits on AERO's re-derivation (AER-3866, corrected by AER-3902; PR #10 at
`2bae926`): 2,700 lb gross, 90 gal, wing and tail 12.5% larger to hold the
stall speed, and the AM20T in the tail cone with its radiator and coolant moved
to the nose bay (AERO's balance option B, which still needs 51-69 lb of nose
lead). Revised 2026-10-26 after AERO's review of PR #14.

Everything here is our estimate (E) unless a source is named. Prices are from
public pages read on 2026-10-25 ([price check](../manufacturing/price-check-2026-10-25.md)).
No shop, holder or museum has been contacted. Script:
`docs/manufacturing/build_plans.py`.

## What the original record gives us

Better than for any other design in the survey, though most of it sits in a
museum we haven't contacted.

- **The kit structure.** SDASM's finding guide for SC.10269 (December 2022,
  re-read 2026-10-25) lists the builder manuals as 31 sub-kits. They run from
  "Kit 101 fuselage framework" to "Kit 131 rigging inspection and flight", with
  wing spars and ribs, wing skins, leading-edge fuel tanks, gear, hydraulics,
  shells and engine access each a kit of its own. The guide's "more than 30
  kits total" means these sub-kits, not airframes sold.
- **The drawing tree.** The guide lists 185 drawing folders (Box 3: 86, Box 4:
  99), numbered by system (10xxx general, 11xxx fuselage, 12xxx wing, 13xxx
  empennage, 14xxx gear, 15xxx engine and fuel, 16xxx controls). There is also
  an "Engineering parts master lists" folder. That list would replace every
  part count below; reading it is museum contact, Bill's call.
- **The tooling cost.** Sport Aviation, March 1986 (re-fetched 2026-10-25):
  "the plugs alone cost 1/10 of their total factory tooling cost of $200,000."
  At about 2.9x CPI from 1986 (E), that is about $580k today, with the plugs
  about $58k of it.
- **The bought share.** The same article: "There were hundreds of parts to be
  ordered from vendors, cataloged and stocked." The nose gear came from Airite.
- **The riveting.** The heavier wing skin "allowed countersinking (instead of the
  commonly used dimpling) and in combination ... with newer type hand pulled
  flush cherry rivets" gave the smooth surface (SA86). Blind rivets mean nobody
  has to buck, and that lowers the skill floor.

## The plan in brief

The plan has two routes. They differ only in the flying surfaces, and the
choice between them is a trade of weight for money.

| | Route A: cage, molded shells, metal wing and tail | Route B: cage, molded shells, carbon wing and tail |
|---|---|---|
| Parts (excluding standard hardware) | 860-1,310, of which 490-750 unique | 590-930, of which 380-590 unique |
| Made from files or molds / bought | 750-1,140 / 110-175 | 480-760 / 110-175 |
| Kit-run tooling | $78-237k (E) | $116-339k (E) |
| Kit-run crossover (tooling under 10% of kit price) | 6-27 airframes, at a $90-140k kit | 8-34 airframes, at a $100-160k kit |
| Builder hours, kit | 1,800-2,800 (E) | 1,500-2,500 (E) |
| Builder hours, one-off (home-molded shells; welded cage bought from a shop) | 3,000-4,500 (E) | 3,500-5,500 (E; adds the home-molded wing and tail) |
| All-in to fly, kit (kit, AM20T $28-30k, firewall-forward $5-10k, prop $5-12k, panel $15-40k) | $143-232k (E) | $153-252k (E) |
| Empty with AM20T at 2,700 lb, option B, including its nose lead | 1,647-1,869 lb (65-74 lb lead) | 1,558-1,840 lb (51-69 lb lead) (AER-3866/3902) |
| Useful load at 2,700 lb, light / heavy end (target 1,000) | 1,053 / 831 lb: 53 lb over / 169 lb short | 1,142 / 860 lb: 142 lb over / 140 lb short |
| Skill floor | Medium: blind flush rivets on countersunk skins; bonding shells; tank sealing | Medium: bonding cured molded parts with structural adhesive |

**The weight difference is the carbon wing and tail.** Stage 4's light end
already took -20 to -60 lb for a carbon wing and -5 to -15 lb for a carbon tail.
Route A gives those back: +75 lb of structure at the light end and +25 lb at the
heavy end. The metal tail sits aft, so option B also needs 14 / 5 lb more nose
lead (0.6 lb per lb). Route A therefore costs 89 lb of useful load at the light
end and 29 lb at the heavy end.

Both routes' numbers come from AERO's balance script at PR #10 head `2bae926`
(the AER-3902 correction). It takes N747P's 49 lb of ballast out of the
weighed-airplane basis, adds the constant-speed propeller and re-solves option
B, which now needs 51-69 lb of nose lead. Route A is that script with the carbon
wing and tail deltas removed (AERO's review of this PR; reproduced by us on
2026-10-26). Against the 1,000 lb target, a target and not a floor since
Bill's 2026-10-25 brief change: the light end clears it by 53 lb on route A and
142 lb on route B; the heavy end is 169 lb short on route A and 140 lb short on
route B.

**Why the hours fall from A to B.** About 270-380 fewer parts, nearly all of them
ribs, skins and stiffeners in the flying surfaces. Bonding a molded wing is
slower per joint than riveting, so the fall is smaller than the part count
suggests. The 1986 projection was 1,500 h (AOPA Pilot), and the museum's guide
says "about five years" per plane. Our kit bands sit between those two.

## 1. Part count and the make/buy split

Columns: **cut** (flat part from a file), **formed**, **tube** (4130 tube cut and
notched from a file, welded in a jig), **machined**, **molded**, **bought**
(an assembly, counted once). Common assemblies first, then each route's flying
surfaces.

| Assembly | Parts | Unique | Cut | Formed | Tube | Machined | Molded | Bought |
|---|---|---|---|---|---|---|---|---|
| Fuselage cage, 4130 square tube | 165-265 | 90-150 | 60-100 | | 90-140 | 15-25 | | |
| Shells and doors, non-structural | 16-24 | 14-22 | | | | | 14-20 | 2-4 |
| Shell bulkheads and attach clips | 68-112 | 20-35 | 50-85 | 18-27 | | | | |
| Landing gear (retractable; fibreglass mains, bought nose gear) | 50-80 | 35-50 | 10-15 | 5-10 | | 20-30 | | 15-25 |
| Flight controls | 70-100 | 50-70 | 25-35 | 10-15 | | 20-30 | | 15-20 |
| Fuel system, 90 gal | 25-40 | 15-25 | 6-10 | 4-8 | | 2-4 | | 13-18 |
| Engine bay, AM20T, 12 in prop extension; radiator in the nose bay | 35-55 | 30-45 | 8-12 | 4-8 | | 4-6 | 2-3 | 17-26 |
| Cabin, windows, panel, seats, interior, baggage | 40-70 | 35-55 | 15-25 | 5-10 | | 2-4 | | 18-31 |
| Electrical and avionics | 25-40 | 25-40 | | | | | | 25-40 |
| *Route A:* wing, metal, re-sized | 180-266 | 70-110 | 80-115 | 85-125 | | 10-14 | 0-4 | 5-8 |
| *Route A:* flaps and ailerons, metal | 69-91 | 35-50 | 30-40 | 35-45 | | 4-6 | | |
| *Route A:* T-tail, metal | 117-168 | 70-100 | 50-70 | 55-80 | | 10-15 | | 2-3 |
| *Route B:* wing, carbon, re-sized | 52-82 | 30-45 | 16-28 | | | 8-12 | 24-36 | 4-6 |
| *Route B:* flaps and ailerons, carbon | 16-24 | 12-18 | | | | 8-12 | 8-12 | |
| *Route B:* T-tail, carbon | 28-41 | 20-30 | | | | 12-18 | 14-20 | 2-3 |
| **Total, route A** | **860-1,311** | **489-752** | 334-507 | 221-328 | 90-140 | 87-134 | 16-27 | 112-175 |
| **Total, route B** | **590-933** | **376-585** | 190-310 | 46-78 | 90-140 | 91-141 | 62-91 | 111-173 |

The bought count excludes standard hardware. SA86's "hundreds of parts to be
ordered from vendors" probably counted catalogue hardware too, so the two are
not in conflict, but neither one checks the other.

## 2. What is cut, molded, printed or welded, and by whom

| Work | Route | Service named (public page, 2026-10-25) | Limit found |
|---|---|---|---|
| Cage tubes, cut and notched | tube laser from files, then TIG-welded in a jig | **None orderable off the shelf.** SendCutSend's tube service is not taking new orders; OSH Cut cuts 4130 tube but lists round profiles only. The cage is square 4130, 3/4 x .035 to 1-1/4 x .065 (SA86) | a job-shop tube laser by quote (not contacted), or stock bought and cut on a notching fixture. Changing to round tube is a structural change |
| Cage welding | TIG, in a jig cut from files | a qualified welder or a shop | primary structure: never an unqualified builder |
| Shells, doors, scoops, closeouts (non-structural) | room-temperature infusion in glass/epoxy molds from routed HDU plugs | plug board: Precision Board PBLT-15, $62.63 for 0.5 x 20 x 60 in (Interstate) | about 217 ft2 of mold surface; the shell molds were "almost swimming pool sized" (SA86), longer than any print bed |
| Wing and tail skins, ribs, spar webs in 2024-T3 (route A) | laser-cut from files, pilot-holed | OSH Cut lists 2024-T3 at 0.032-0.19 in, so the 0.032 ribs, 0.040 leading edges and 0.050 spar web (SA86) can all be cut from files | maximum part 119 x 47 in. No 2024-T3 bending listed, so the press-brake C-spar is a brake service (not priced) |
| Leading edges (route A) | molded in place of stretch-formed (see below) | as the shells | |
| Wing, tail and control surfaces (route B) | infused carbon in molds from HDU plugs | as the shells; about 340 ft2 of wing mold and 140 ft2 of tail mold | load-bearing: needs STRUCTURES |
| Fittings, bellcranks, gear trunnions, the prop extension and its bushing | CNC-machined | Xometry, Protolabs (instant quote by upload; not run) | the prop extension is a fatigue part on a drive that has already lost one propeller (NTSB LAX05LA270): a certified shop with material certs, never home |
| Jigs, drill guides, ducts, the nose-bay radiator duct | printed | Xometry FDM to 24 x 36 x 36 in; Additive Plus FGF to 2 m (both price by upload) | no public price |

**The stretch-formed leading edges can't be repeated.** The originals were
formed on male dies, on what SA86 calls "the only machine of its type in the
world". The wing is being re-sized anyway, so those dies would not
fit even if they turned up. Route A replaces them with molded leading-edge skins
(about 81 ft2 of mold surface, $10-29k, E). Those skins form the D-nose and hold
the fuel, as the originals did. **That makes them load-bearing and
fuel-wetted.** The laminate needs STRUCTURES, and the resin must be chosen for
the fuel the AM20T burns. The other route is new stretch dies at a service,
which we have not priced.

## 3. Tooling, for a small kit run

| Line | Route A (E) | Route B (E) | Basis |
|---|---|---|---|
| CAD and CNC programs | $10-30k | $10-30k | E |
| Shell plugs and molds, 217 ft2 | $26-78k | $26-78k | $120-360 per ft2 of mold surface (stage 4) |
| Cage welding jig | $15-40k | $15-40k | E: slotted-plate fixture cut from files |
| Form blocks, 60-100 unique formed wing and tail parts | $9-40k | | $150-400 per block |
| Leading-edge skin molds, 81 ft2 | $10-29k | | as shells |
| Wing skin and spar molds, 339 ft2 | | $41-122k | as shells; 127 ft2 wing x 2.05 wetted x 1.3 |
| Tail molds, 136 ft2 | | $16-49k | (33 + 18 ft2) x 2.05 x 1.3 |
| Assembly and bonding jigs | $8-20k | $8-20k | E |
| **Total** | **$78-237k** | **$116-339k** | |

**Checked against 1986.** Prescott's own tooling was $200,000 in 1986, about
$580k today. Our route A band sits at 13-41% of that. Most of the gap is lines
the modern route doesn't need: the stretch press and its dies, and CNC metal
station templates for the plugs. The rest is plug cost. SA86 puts the plugs at
$20,000, about $58k today. Our plug-material and machining build-up for the
same 217 ft2 is $8-22k ((15-40) + (20-60) dollars per ft2). That is 3-8 times
below the 1986 figure. We put the gap down to 1986 CNC costs, but we can't prove
that. If it is wrong, the shell line is under-priced, and that is the largest
risk in these bands.

**One-off builder against a kit run.** A one-off builder makes the shell molds
at home: 430-870 h and $3-9k of materials (stage 4). They buy the cage cut and
welded from a shop, at a price not checked. In route B they also mold the wing
and tail: about 480 ft2 more, 960-1,900 h. In a kit run the tooling adds
$8-24k (A) or $12-34k (B) to each of 10 kits.

## 4. Is the laminate schedule load-bearing?

**For the shells, no.** They are non-structural over the cage (SA86, AOPA
1986), so their laminate is set by handling, hail and the attachment points,
not by flight loads. That is a manufacturing call, not STRUCTURES.

**For the wing and tail, yes, on both routes.** The re-derivation's 2,700 lb
gross and its 12.5% larger wing and tail are a new structure, whatever it is
made of. Route B's carbon skins and spar are primary structure. Route A's molded
leading edges are the torsion box and the fuel tank. Even route A's metal spar
and skins need new gauges at the new gross. **This is the point to take to
Bill:** if the Prescott goes to development, STRUCTURES is needed for the wing
and tail on either route, and for the cage at 2,700 lb (Prescott tested it at
2,400 lb and 3.8 g).

## What would replace these estimates

- The SDASM parts master list and drawing tree (museum contact, Bill's call).
  It would turn every part count above into a count.
- A tube-laser job shop's price for the square-tube cage, or a decision on round
  tube (STRUCTURES).
- A service price for the 1986-scale shell plugs, which would settle the 3-8x
  question above.
