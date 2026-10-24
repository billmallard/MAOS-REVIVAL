# Stage 4: what modern manufacturing changes for each shortlisted design

**Status:** stage 4 of the legacy survey (AER-3784), compiled 2026-10-24 by
MANUFACTURING, and revised the same day for the stage 3 revision 2 shortlist
(`docs/SHORTLIST.md`, PR #4 at `031f641`). It also uses Elon's rights files
(`docs/rights/`, PR #3). Bill decides which designs, if any, go to development.

This is a desk study. Nothing has been weighed, quoted or built by us. Every
price is from a public page or article, dated; every weight and hour figure
names its source and grade, or is marked as our estimate (E). No vendor, kit
seller, rights holder or museum has been contacted.

**Scope after Bill's review.** AERO's revised ranking is the priority order
until Bill picks:

1. Bellanca T-250 Aries (new)
2. Wheeler Express
3. Lancair IV-P
4. Meyers 200D (new, a re-derivation)
5. Mooney 301

AERO's revision 3 (PR #4 at `63a7397`) puts the **Prescott Pusher** second, behind the Aries, as Bill's top interest. Its section below is built on AERO's stage 3 check and the 1986 AOPA Pilot report.

The Aries and the Express get full studies. The IV-P keeps its full study from
the first version. The Meyers and the 301 get notes. Bill dropped the Defiant,
VK-30, Velocity and Berkut, so their stage 4 sections are gone; the first
version is in git history at `b2b3137`. The P210N stays as a calibration case,
and the Cozy MKIV as the reference.

## What this stage finds

1. **Prescott Pusher: rebuild empty weight 1,380-1,630 lb, useful load 770-1,020 lb
   at the published 2,400 lb gross.** Modern structure takes out 35-175 lb:
   carbon sandwich shells in place of 3-8-ply fibreglass ones over the kept
   steel cage, plus a carbon wing and tail in place of riveted aluminium. Only
   the light end reaches 1,000 lb, and the AM20T is 54-71 lb heavier than the
   O-360, in the tail cone, where AERO puts the ballast at 1.3 lb per lb. Saving
   weight aft avoids 20-55 lb of that ballast. Gross weight, a STRUCTURES question,
   and balance are still the levers that decide it.
2. **Aries: rebuild empty weight 1,780-2,000 lb.** Useful load is 1,150-1,370 lb
   against the factory 1,300; with our engine credit, empty is 1,690-1,940 lb.
   Modern manufacturing doesn't make it much lighter. What it changes is cost:
   the Aries was designed around flat and single-curve skins, so a matched-hole
   kit needs no compound molds or stretch-forming. Tooling is the cheapest of any
   design here, about $40-120k (E), and pays back below 10% of kit price at about
   3-12 airframes. Its range shortfall at continuous power is a fuel question:
   about 20 more gallons in integral wing bays costs 10-20 lb empty.
3. **Express: rebuild empty weight 1,770-2,030 lb.** Useful load is 865-1,125 lb
   against the weighed 901, so at the light end it clears the 1,000 lb floor.
   Three things do it: replacing the vinylester E-glass (the heaviest laminate on
   the shortlist) with infused carbon/epoxy, lighter tail surfaces, and losing the
   56-62 lb of nose ballast S-90 owners carry. The heavy end assumes none of that
   ballast is in the weighed baseline. The re-derived tail and "complete kits" are
   manufacturing tasks with a price, set out below.
4. **IV-P: rebuild empty weight 2,140-2,360 lb, useful load 1,190-1,410 lb.**
   Manufacturing barely moves it. The engine (-150 to -242 lb, if CG allows it)
   and deleting pressurisation (-100 to -200 lb) are what move it. RDD's LX7
   re-wing is a data point the other way: +150 lb empty for a one-piece carbon
   wing with 180 gal, at about $821,000 complete (AvWeb 2019).
5. **Meyers 200D: re-derived empty weight 1,840-2,160 lb.** Useful load is 840-1,160
   lb at the original 3,000 lb gross, and the swap saves 105-133 lb with engine
   credit. A production re-derivation keeps the steel-tube cage. The cage tubes
   and gussets are laser-cut by a service and jig-welded; the four-tank fuel
   system becomes two integral tanks of about 100 gal.
6. **AERO's engine dry weights, checked against the engine type data sheets.**
   - The Meyers IO-520-A is 431 lb (TCDS E5CE), not 415, so its swap saves
     105-133 lb, not 89.
   - The Aries O-540-A4D5 is 375 lb without starter and alternator (TCDS E-295).
     That puts its swap at 63-81 lb, close to AERO's 64.
   - The IV-P's TSIO-550 is 470 lb with turbos (TCDS E5SO), not 550.
   - Aeromomentum's own pages say its listed weights "tend to be the fairly
     typical installed weight". If that is right, AERO's dry x 1.25 rule
     double-counts 71 lb per AM20T. We don't credit it; asking Aeromomentum needs
     Bill's go-ahead.
7. **Every design on the list is a re-derivation:** the IV-P's molds are lost,
   the Express's are unaccounted for, the 301 and the Meyers are new designs from
   a layout, and the Aries's drawings sit with a dormant TC holder.
8. **A home shop (about $20-49k of tools) makes molded-weight composite parts and
   matched-hole metal parts.** On the Express it saves about $30-60k against a
   complete kit, at 1,750-4,000 more builder hours, nearly all of them
   mold-making (more cash on the IV-P, whose re-derived kit costs more). On the metal Aries it saves more cash, $40-90k, for 600-1,200
   more hours of cutting, deburring and drilling. Engine mounts, gear legs,
   pressure-hull sealing, welded primary structure and heat-treated parts stay
   with services. See [The home-shop route](#the-home-shop-route).

## Rebuild empty weight, all designs

Generated by `docs/manufacturing/weights.py` from
`docs/manufacturing/rebuild_weights.json`. "Light" is the lightest credible
outcome and "heavy" the heaviest; the range is not a confidence interval, it is
the spread of the stated assumptions. Useful load is MTOW (as stage 3) less the
rebuild empty weight. The engine swap is kept apart, as in stage 3, because no
one has checked CG. Options (deleting pressurisation, more fuel, the LX7 wing)
are in each dossier but not in these totals.

| Design | Stage 3 empty, lb (basis) | Airframe change, lb | Rebuild empty, lb (no engine credit) | Useful load, lb (stage 3 -> stage 4) | Engine change, lb (our check) | Rebuild empty with engine credit, lb | Grade |
|---|---|---|---|---|---|---|---|
| Prescott Pusher | 1,550 (F) | -175 to -35 | 1,380-1,630 | 850 -> 770-1,020 | +54 to +71 | 1,430-1,700 | E |
| Bellanca T-250 Aries | 1,850 (F) | -75 to +50 | 1,780-2,000 | 1,300 -> 1,150-1,370 | -81 to -63 | 1,690-1,940 | E |
| Wheeler Express | 1,994 (R) | -225 to -20 | 1,770-2,030 | 901 -> 865-1,125 | -6 to +23 | 1,760-2,050 | E |
| Lancair IV-P | 2,200 (F) | -55 to +25 | 2,140-2,360 | 1,350 -> 1,190-1,410 | -242 to -150 | 1,900-2,220 | E |
| Meyers 200D (re-derivation) | 1,940 (F) | -95 to +60 | 1,840-2,160 | 1,060 -> 840-1,160 | -133 to -105 | 1,710-2,060 | E |
| Mooney 301 | 2,548 (F) | -65 to +50 | 2,480-2,700 | 1,452 -> 1,300-1,520 | -293 to -205 | 2,190-2,500 | E |
| Cessna P210N | 2,342 (T) | +0 to +0 | 2,340-2,430 | 1,658 -> 1,570-1,660 | -178 to -150 | 2,160-2,280 | E |
| Cozy MKIV (reference) | 1,179 (R) | -150 to -65 | 1,030-1,110 | 871 -> 940-1,020 | +18 to +57 | 1,050-1,170 | E |

Notes on reading it:

- The stage 3 useful load here is MTOW less stage 3 empty weight. AERO's
  headlines may also subtract an engine change; ours keeps the engine apart.
- Heavy ends that start from equipped figures (IV-P listed at 1,058 kg / 2,332 lb,
  Meyers at about 2,100 lb from owner data, Aries +100 lb on a 1977 spec-table
  weight) can come out *worse* than stage 3. That is the fleet-heavier-than-
  brochure pattern the brief warns about, and we did not round it away.
- For AERO's ranking: the Express is the design manufacturing moves most (its
  useful-load range spans the 1,000 lb floor). The Aries, IV-P and 301 move less
  than their engine credits do. The Meyers moves by its engine credit and by
  whatever gross weight a re-derivation is designed to.

## How the composite deltas are built

Areal weights (E, from published fabric weights):

| Laminate | Dry fabric | Resin fraction (by weight) | Cured, lb/ft2 per ply |
|---|---|---|---|
| BID 7725 E-glass, 8.9 oz/yd2, wet hand layup (Rutan moldless) | 0.062 lb/ft2 | 45-50% | 0.112-0.124 |
| 3K carbon twill 200 gsm, vacuum infusion | 0.041 lb/ft2 | 35-40% | 0.063-0.068 |
| Same, prepreg | 0.041 lb/ft2 | 35% | 0.063 |

Worked example: the Rutan Defiant, on AERO's OpenVSP wetted areas (wing 240,
canard 31, winglets 16, fuselage 228 ft2). Bill dropped the Defiant from the
shortlist on 2026-10-24. The example stays because it is the clearest
moldless-against-molded comparison, and the Cozy reference line scales from it.


- **Lifting surfaces, original.** Glass skins on the outer face only, about 2
  plies: 64-71 lb. Full-depth foam core: wing volume about 0.68 x t/c x
  integral of c^2 dy = 40-55 ft3 after the fuel bays, canard about 3 ft3,
  winglets about 1.5 ft3, at 1.8-2.2 lb/ft3: 90-120 lb. Micro bond coat 11 lb;
  glass spar caps and webs 50-65 lb. About 215-265 lb.
- **Lifting surfaces, molded.** Two carbon plies on both faces: 76 lb. A light
  core on 70% of the faces (6 mm PVC or Nomex, 3-4 lb/ft3): 25-30 lb; core
  adhesive 12 lb; pultruded carbon caps 20-28 lb; webs, ribs and bond paste
  30 lb. About 165-175 lb. **Change -40 to -95 lb.**
- **Fuselage.** Original 3 plies of BID over 10 mm foam, both faces bonded with
  micro: about 117 lb. Infused carbon at 2-3 plies on the same core: 56-77 lb.
  **Change -30 to -60 lb.**
- **Finish.** Moldless micro fill at 0.06-0.12 lb/ft2 plus about 0.05 lb/ft2 of
  primer and paint, on 515 ft2: 57-88 lb. A molded surface needs paint and
  pinhole fill only: 26-31 lb. **Change -25 to -55 lb.**

The same arithmetic scaled by wetted area gives the Cozy reference line. For
designs that were already molded (the Express, and the IV-P) only the
skin-laminate step applies, and for the Express it is larger because its
vinylester E-glass is the heaviest laminate on the shortlist.

What this arithmetic cannot see: ply drops and local reinforcement, hardpoints,
the real core layout, and a minimum gauge set by hangar rash and hail rather
than load. Those are why each range runs as wide as it does. A real laminate
schedule needs STRUCTURES, and only if a design goes to development.

## Engine check

AERO asked us to check its original-engine dry weights, which were typical
figures. We read the engine type certificate data sheets ourselves through the
FAA DRS guest API on 2026-10-24. For the same Lycoming, the operator manual
includes starter and alternator and the TCDS does not; 1E4 marks its weights
"Less starter and alternator", and the difference is about 30 lb. AERO's x1.15
installation factor fits the manual basis, so for Lycomings we add 20-35 lb to
the TCDS figure (E). For Continentals we found no document saying what "basic
dry" includes, so we add 0-25 lb (E).

| Design | Engine flown (source) | AERO's assumed dry, lb | Published dry, lb (basis) | Original installed, lb (x1.15) | AERO's swap change | Our swap change |
|---|---|---|---|---|---|---|
| Prescott Pusher | O-360, 180 hp (Prescott specs; AOPA 1986). Dash number not found | 285 (installed 330) | O-360-A1A 258, without starter and alternator (TCDS E-286 Rev 21); manual basis about 278-293 (E: TCDS + 20-35) | 320-337 | +61 | +54 to +71 (AM20T); AM15T -33 to -16 |
| Bellanca T-250 Aries | O-540-A4D5, 250 hp (dossier); 51A: IO-540-C4B5 | 395 | 375, without starter and alternator (TCDS E-295 Rev 19, Note 5) | 454-472 | -64 | -81 to -63 |
| Wheeler Express | IO-360-ES1B 210 hp (CAFE report) | 330 | 320 (E1CE Rev 21) | 368-397 | +11 | -6 to +23 |
| Lancair IV-P | TSIO-550-E or -B, 350 hp (not confirmed by a builder or Lancair document); CAFE's N114L flew a Regan TIO-540, 360 hp | 550 | 470.2 including both turbos, intercoolers not listed (TCDS E5SO Rev 13) | 541-633 | -242 | -242 to -150 |
| Meyers 200D | IO-520-A, 285 hp (dossier) | 415 | 431 (TCDS E5CE Rev 27) | 496-524 | -89 | -133 to -105 |
| Mooney 301 | "360 hp TSIO-540" in every source; TCDS E14EA lists no 360 hp TIO-540, the maximum is 350 | 520 | 350 hp TIO-540 variants 518-595 (-J2BD/-N2BD 518, -R2AD 524, -W2A 554, -J2B 558, -V2AD 565, -AE2A 595; E14EA Rev 22 Note 10) | 596-684 | -207 | -293 to -205 |
| Cessna P210N (calibration) | TSIO-520-P, -AF from s/n 761 (aircraft TCDS 3A21 Rev 50) | 480 | 470 including turbo; intercooler is a Cessna part (E8CE Rev 24) | 541-569 | -161 | -178 to -150 |
| Cozy MKIV (reference) | O-360 180 hp (dash number not found); IO-360 common | 285 | O-360-A1A 290, IO-360-A1A 324 (manual, not re-fetched; TCDS 258 and 293) | 334-373 | +63 | +18 to +57 |

Aeromomentum (aeromomentum.com, read 2026-10-24): AM20T 260 hp, 285 lb,
$27,995 in the spec table, $29,700 for the 300 hp version (F). The same pages say
both "the installation adds about 25% to the base engine weight" and "the weights
listed tend to be the fairly typical installed weight". AERO read the first. If
the second is meant, the AM20T installed mass is about 320 lb with the 35 lb
radiator allowance, and every swap above improves by about 71 lb. Only
Aeromomentum can say which is meant.

## Cost, hours, tooling and skill floor

Prices are public and dated 2026-10-24 unless stated. Our estimates are marked
E and are bands, not quotes. A band published here gets carried into other
documents as if it were a fact; please carry the E with it.

**Composite tooling estimate (E).** No public price exists for a GA mold set.
Large-format printing bureaus (Thermwood, CEAD, AES, Massivit) and tooling-board
makers are quote-only, and asking would be vendor contact. Our build-up per ft2
of mold surface: plug material $15-40, CNC machining $20-60, mold laminate and
backing structure $20-40, and 2-4 h of labour at $60-90/h, so $120-360/ft2. Mold
surface is the wetted area times 1.3 for flanges, returns and split lines.
Printed molds may cut material cost about a third and lead time by half (IACMI
2017; CompositesWorld 2021), which we do not credit. For scale, Kitplanes (Jul
2024) puts the capital to rebuild a whole kit company at $5-15M; this is the
molds alone.

### Prescott Pusher

**Original construction.** AOPA Pilot (March 1986, P, re-read 2026-10-24)
describes "a combination of tubular steel fuselage covered with a composite,
non-structural shell", with flying surfaces of "conventional aluminum-covered,
built-up spar and rib construction" and "flush riveting ... in all aluminum
surfaces". AERO's stage 3 block (from Sport Aviation 1986 and others) adds:

- a TIG-welded 4130 square-tube cage
- fibreglass shells of 3-8 plies, flush-riveted to bulkheads
- a press-brake 2024 C-spar with nested extrusion caps
- leading edges stretch-formed on CAD/CAM steel dies
- the engine in the tail cone, with a 12 in prop extension

Kits were $29,500 fixed-gear and $36,500 retractable, and Prescott projected
1,500 build hours (P, AOPA Pilot 1986). The museum's finding guide for SC.10269
says "about five years" per plane (B). Published empty weight is 1,550 lb (F).
The one weighed builder aircraft is 1,661 lb (739 lb useful, B). The 1986 design
target was 1,220 lb.

**Rebuild empty weight:** 1,380-1,630 lb, useful load 770-1,020 lb at 2,400 lb
gross (table above; all E).

- **Shells:** -25 to -70 lb. Fibreglass at 3-8 plies is 0.35-0.92 lb/ft2 on AERO's
  167 ft2 of fuselage; a non-structural carbon sandwich is 0.20-0.30 lb/ft2.
- **Molded carbon wing:** -20 to -60 lb. It also holds the NLF section better than
  flush rivets on a stretch-formed nose, which AERO might credit in drag (we don't).
- **Carbon tail:** -5 to -15 lb.
- **Panel:** -10 to -30 lb.
- **Additions:** the EFI backup bus and a pusher radiator duct.
- **Options, not in the totals:**
  - a structural carbon monocoque in place of the cage saves a further 30-70 lb,
    gives up crash protection, and needs STRUCTURES
  - in the AM20T case, the aft savings avoid about 20-55 lb of AERO's 82 lb of
    nose ballast (1.3 lb per lb, AERO)

**What moves it over the floor.** Structure alone reaches 1,000 lb only at the
light end. The AM20T installs 54-71 lb heavier than the O-360, in the tail cone.
That's O-360-A1A 258 lb per TCDS E-286 plus starter and alternator, on the x1.15
rule; AERO's figure is +61. The levers are:

- **Gross weight.** Prescott tested at 2,400 lb and 3.8 g, so a higher gross is a
  STRUCTURES re-substantiation. AERO's 2,700 lb case is the one that clears.
- **Balance.** Wing position, gear and the forward fuselage. That is design work
  AERO has named, and manufacturing doesn't decide it.
- **The engine.** The AM15T installs 16-33 lb lighter than the O-360, at less power.

**Modern route and home shop.**

- **Stretch-formed leading edges** need dies and a stretch press, which is a
  service, not a home tool. The home alternatives are a molded carbon leading edge
  or a carbon wing.
- **Press-brake spars:** a 2024 C-spar of this size needs a press brake, so a
  service. 2024-T3 at 0.032-0.040 in is not on SendCutSend.
- **The cage** stays welded 4130, so a qualified welder or a shop.
- **Shells:** home-molded, about 217 ft2 of mold surface, 430-870 h and $3-9k of
  materials (E).
- **Carbon wing:** about 267 ft2 more (530-1,070 h).
- **Service tooling for a small kit run:** $60-180k (E). That covers shell molds,
  a welding jig, and either matched-hole wing tooling or wing molds.

**Re-derivation.** The museum's collection SC.10269 lists the drawings, the wing
static test, the loads report and the weight-and-balance schedule (finding
guide, Dec 2022). Those would replace most of the estimates above. Contacting the
museum is Bill's call; Elon has asked him.

### Bellanca T-250 Aries (metal, matched-hole)

| | Original (certified, 1976-80) | Modern one-off builder (parts cut from files) | Modern matched-hole kit (small run) |
|---|---|---|---|
| Builder hours | factory-built; about four completed | 3,500-5,000 (E): parts from files, holes final-drilled by hand | 2,500-3,500 (E). Anchors: RV-10 2,000 (F, Van's, via forum); builders report 2,600-3,600 standard (anecdotal). The Aries adds retractable gear and flush riveting on a laminar wing |
| Airframe change | baseline | -30 to +40 lb (structure) | same |
| Airframe parts | | aluminium, rivets and hardware $25-40k (E); 2024-T3 at 0.032-0.040 in is not offered by SendCutSend, so cutting goes to a home router or a full-service sheet-metal shop (not contacted) | $100-150k kit (E). Anchors: RV-10 $89,600 standard and $116,300 quick-build (F, vansaircraft.com, read 2026-10-24) |
| Tooling | | none beyond the builder's | $40-120k (E): CAD and CNC programs; 150-250 unique formed parts at $150-400 per form block or press die; $10-30k of assembly jigs; $8-25k of composite molds for the cowl, tips and fairings. No compound or stretch-formed skins, because the design avoided them |
| Crossover | | | tooling under 10% of the kit price at about 3-12 airframes |
| Engine | O-540, 250 hp | AM20T, $27,995-29,700 (F) | same |
| All-in to fly | | $85-160k (E) | $155-240k (E: kit, engine, firewall-forward $5-10k, prop $5-12k, panel $15-40k) |
| Skill floor | | Medium-high: final-drilling and fitting without matched holes | Medium: Van's-level riveting. The critical skill is flush riveting and dimpling to laminar-wing quality, since waviness costs the laminar run AERO credited (x_tr 0.25) |

**First, what to delete.** The carburettor, magnetos, carb heat and mixture
control (EFI). The single air-cooled inlet and its baffles (one radiator in a
duct). The 1977 avionics and vacuum system (EFIS). In a kit, any part whose
only job was certification paperwork; amateur-built eligibility itself is not
our ruling.

**What it adds.** A radiator duct, a backup power source for the ECU, and, as
an option, about 20 gal of integral wing tankage. A constant-chord wing holds
about 11 gal per foot of span between the spars (E), so a little under a foot
of extra bay per side.

### Wheeler Express (composite, complete kit)

| | Original kit (c. 1990-2007) | Modern complete kit (re-tooled, small run) |
|---|---|---|
| Builder hours | 2,000 claimed by the kit maker; 5,000 for the CAFE aircraft (F/P, CAFE APR) | 2,000-3,000 (E), if the kit is complete: every part molded and trimmed, hardware, firewall-forward package and documented assembly |
| Airframe change | baseline (1,994.1 lb weighed, R) | -225 to -20 lb (table above) |
| Kit price | $34,995 (F, CAFE APR, c. 1998) | $90-150k (E). Anchors: Velocity XL $77,000 base, +$16,000 retract (F, velocityaircraft.com, read 2026-10-24) |
| Tooling | molds unaccounted for since about 2009 | $100-300k (E): about 675 ft2 of mold surface at $120-360/ft2, plus jigs. That includes the new tail: an S-90-size low tail, or a 20-24 ft2 fin, with dorsal and ventral fins |
| Crossover | | tooling under 10% of the kit price at about 7-33 airframes |
| Engine | IO-360-ES 210 hp (CAFE) | AM20T, $27,995-29,700 (F) |
| All-in to fly | | $145-240k (E) |
| Skill floor | High: incomplete kits and plans left builders fabricating and documenting their own parts | Medium: bonding cured molded parts with structural adhesive; one composite workshop |

**First, what to delete.** The vinylester E-glass laminate (infused
carbon/epoxy instead). The cruciform tail and its 1995 retrofit letter (a
re-derived tail, flight-tested before any kit ships). Nose ballast. The IO-360's
baffles, carburettor or injection controls and magnetos. And the incomplete
kit: every part the old builders had to make or document themselves.

**What "complete kit" means in manufacturing terms.** A closed bill of
materials; every part from a mold or a file; matched and pre-drilled hardpoints;
a firewall-forward package for the AM20T; a wiring harness; and an assembly
manual that has been built from by someone other than its author. AERO's
dossier names the market lesson: "nothing sells kits like kits completed and on
the flight line" (B).

### Lancair IV-P

The IV-P molds have no known location since the Uvalde sale in 2017. The
earlier claim that the 2023 JetEXE purchase included molds and IP was a
misquotation, withdrawn in stage 2 and stage 3 (AERO, AER-3784 thread,
2026-10-24). So the working route is a re-derivation from a measured airframe
(about 235 are registered) into new molds. A licence of existing molds stays in
the table only as the case where they turn up.

| | Original kit (c. 2000) | Modern: re-derived, new molds (working route) | Modern: only if the molds turn up and can be licensed |
|---|---|---|---|
| Builder hours | 5,000-6,000 estimated (F, CAFE APR, with Fast-Build); about 4,500 for one builder with fastbuild wing (P, AOPA Pilot Apr 2005) | 3,500-5,000 (E): pressurisation deletion and a kit firewall-forward take out 100-300 h; builder assist (Velocity charges $95/h) takes out more | same |
| Airframe change | baseline | -55 to +25 lb (table above) | -55 to +25 lb |
| Kit price | $104,500 incl. wing mating and Fast-Build (F, CAFE APR); about $200k in 2026 dollars (E, CPI x1.9) | $150-220k airframe (E) plus the tooling share: $4-27k per airframe at 10-25 units | $150-220k (E) plus licence terms (unknown; rights) |
| Tooling | holder's | $90-270k (E: about 584 ft2 of mold surface at the rates below, plus jigs), plus measuring an airframe and re-deriving its structure (STRUCTURES; access to an airframe is Bill's call) | mold refurbishment $20-80k (E) plus a new cowl and radiator duct, $8-25k (E: 40-60 ft2 of mold surface) |
| Crossover | | tooling under 10% of the kit price at about 5-20 airframes | |
| Engine | TSIO-550, 350 hp | AM20T, $27,995-29,700 (F) | same |
| All-in to fly | | $205-340k (E: kit with tooling share, engine, firewall-forward $5-10k, prop $5-12k, panel $15-40k) | $200-310k (E) |
| Skill floor | Medium-high: high-performance build, pressurised door and seal, twin-turbo installation | Medium: cured molded parts; the unpressurised option removes the pressure door, seals and plumbing | same |

**First, what to delete.**

- The twin turbos, intercoolers, oil cooler and air-cooled baffles of the
  TSIO-550 (one liquid-cooled AM20T with one radiator).
- If Bill accepts unpressurised flight up to the engine's critical altitude:
  the pressurisation dump valve, bleed-air plumbing from the turbos, the
  inflatable door seal, the heavy door latches and the extra plies in the
  shell. That is a configuration and mission call, not ours; we only say it is
  100-200 lb and a few hundred build hours.
- Mixture, magnetos and the turbo controls (EFI).

What it does not delete: the 36 lb/ft2 wing that AERO ties to the stall-spin
record. Manufacturing cannot help that.

### Meyers 200D (re-derivation, note)

A production re-derivation keeps the welded 4130 cage that is the design's
point. Cut the tubes and gussets with a tube-laser service (quote-only; not
contacted), fit them in a welding jig, and weld. Skin it in matched-hole
aluminium. Replace the four-tank, one-gauge fuel system (ten of its 26 accidents
are fuel starvation) with two integral wing tanks of about 100 gal. Tooling is
low: a welding jig and form blocks, $30-90k (E). The skill floor is set by the
welding. A cage welded by an amateur is primary structure, so either the builder
is a qualified welder or the cage comes welded from a shop. Rebuild empty
weight, at the original 3,000 lb gross: 1,840-2,160 lb (E). A re-derivation at
about 3,300 lb gross, as AERO suggests, would carry its own structure weight;
that needs STRUCTURES if it goes forward.

### Mooney 301 (note)

Unchanged from the first version: a matched-hole aluminium re-derivation. It
should be unpressurised, because pressurisation costs 100-200 lb and the rivet
sealing a pressure hull needs is the step most beyond an amateur. Rebuild empty
weight, pressurised: 2,480-2,700 lb.

## The home-shop route

Added 2026-10-24 at Bill's direction: "aircraft construction with modern in-home
machining and printing tools" is a deep-dive axis in the brief. Everything above
costs services. This section costs the same airframes built with tools the
builder owns. Prices were read on 2026-10-24 from the vendors' public pages.
Rows marked (a) were read by a research agent, and that agent quoted the page
text; rows marked (v) I re-fetched myself. Nobody was contacted.

### The reference home shop

| Tool | Model (price, read 2026-10-24) | Envelope | Published tolerance | What it is for |
|---|---|---|---|---|
| CNC router, 4 x 8 ft | Avid PRO4896, $11,389 base, +$100 for 12 in Z (v) | 49.5 x 98.75 in, Z 8 or 12 in | accuracy +/-0.005 in, repeatability +/-0.002 in (v) | foam plugs in slabs, mold tiles, bulkheads and ribs from sandwich panel, form blocks, aluminium sheet (Avid does not state aluminium; ShopBot and Shapeoko do (a)) |
| CNC router, 4 x 4 ft (budget) | Shapeoko 5 Pro 4x4, $3,800-4,150 (a) | about 4 x 4 ft | ballscrew +/-50 um per 300 mm (a) | the same work, in half-size tiles |
| Large FDM printer | Elegoo OrangeStorm Giga, $2,499 (a, sale price via page summary) | 800 x 800 x 1000 mm | none published; +/-0.2-0.5 mm typical (E) | plug tiles, jigs, drill guides, small molds |
| CF-capable FDM printer | Bambu Lab H2D, $1,749 sale / $1,999 (a) | 350 x 320 x 320 mm | none published | CF-nylon fixtures, duct and fairing parts, non-structural brackets |
| Resin printer (optional) | Formlabs Form 4L, $7,125 (a) | 353 x 196 x 350 mm | +/-0.15% XY (a) | master patterns, small accurate tooling |
| Benchtop CNC mill | Langmuir MR-1, $5,195 (a); Tormach PCNC 440 from $8,995 (v) | MR-1 23 x 21 x 6.1 in; 440 10 x 6.25 x 10 in | not published by either | fittings, bellcranks, hinge brackets, gear attach blocks from 6061/2024/7075 plate |
| Benchtop CNC lathe (optional) | Tormach 8L, from $12,395 (v). Sherline stopped taking orders on 2026-10-19 (a) | 8 in swing | not published | bushings, spacers, rod-end fittings |
| Vacuum infusion kit | Composite Envisions complete kit, $1,126.27, 4 cfm two-stage pump and trap (v) | as big as the bag | 10 micron pump (a) | infusion and bagging |
| CNC hot-wire (moldless route only) | Foamlinx FC5050, $14,500, 100 in wire (v); FC3927 $8,500, 60 in (v) | wire length is the core length | | full-depth foam cores |
| Curing oven | Easy Composites OV301, $2,955.80, 1,070 mm inside (a): too small for wing panels. A tent oven for 15-20 ft panels is a builder's own build, $1-3k (E) | | | post-cure; out-of-autoclave prepreg |

Three tiers, tools only, before tax, shipping and tooling bits (add 15-25%, E):

- **Minimum, about $20k:** 4x8 router, H2D, MR-1 and the infusion kit. Turned parts are ordered.
- **Core, about $34k:** the minimum plus the large printer and the 8L lathe.
- **Core plus hot-wire, about $49k:** for the moldless route.

Resale value is real but not credited.

Service lead times, for the parts that still go out (vendor pages, read
2026-10-24): SendCutSend ships standard orders in 2-4 business days (a);
Xometry CNC takes 3-7 business days (a); Protolabs says "as fast as 1 day" (a).
SendCutSend offers 2024-T3 only at 0.025 in, so a home router or a full-service
shop is the only route to 0.032-0.040 in 2024-T3 parts.

### What the home shop changes, design by design

Home-molded means the builder routes the plugs and pulls one-off female molds.
Tooling labour is 2-4 h per ft2 of mold surface and materials are $15-40/ft2
(E, the same build-up as the service tooling estimate, with the labour unpaid).
Service kit figures are from the sections above. All E unless sourced.

| Design | Make at home | Still a service or bought part | Home route vs service route: hours and cash |
|---|---|---|---|
| **Prescott Pusher** | Shell plugs and molds (about 217 ft2: 430-870 h, $3-9k of materials); wing ribs and skins from 2024-T3 on the router, or a home-molded carbon wing (about 267 ft2 more, 530-1,070 h); jigs and fittings | The welded 4130 cage (a qualified welder or a shop); the stretch-formed leading edges and press-brake spars, if the wing stays metal; gear; engine mount | Shells only at home: about +430-870 h against molded shells from a kit, saving the shell share of the kit price. With a home carbon wing, as the Express, scaled to about 480 ft2 of mold |
| **Bellanca T-250 Aries** (metal) | Ribs, bulkheads, gussets and skins up to 4 x 8 ft, cut from 2024-T3 on the router with pilot holes, then final-drilled. The wing skin wraps about 6 ft of chord, so it needs a chordwise splice on a 4 ft bed, or a shop with a 5 x 10 ft bed. Routed form blocks for hammer-formed flanges; milled fittings; home-molded cowl, tips and fairings | Gear legs and retract actuators; the stabilator's balance weight and hinge fittings if they are heat-treated; engine mount; long press-brake bends | +600-1,200 h of cutting, deburring and drilling over a service-cut kit, so 3,100-4,700 h. Cash $45-74k (tools $20-34k plus materials $25-40k) against a $100-150k kit, so it saves $40-90k. That needs someone to publish the CAD files first; the kit price pays for them |
| **Wheeler Express** | Home molds from a measured airframe: about 675 ft2, 1,350-2,700 h, $10-27k of tooling materials, including the new tail | Engine mount, gear legs, canopy, radiator | Home-molded: 3,750-7,000 h and $59-91k, against a complete kit at 2,000-3,000 h and $90-150k, at the same weight |
| **Lancair IV-P** | The same plug and mold work from a measured airframe: about 584 ft2, 1,200-2,300 h, $9-23k of tooling materials. Infusion with a tent-oven post-cure instead of prepreg | Measuring the airframe (scanner or service; access is Bill's call); pressure-door seals, latches and windows if it stays pressurised; engine mount | Home-molded: 5,100-8,100 h and $58-87k, against a re-derived kit at 3,500-5,000 h and $155-250k with tooling share. Pressurised laminate quality is the home-shop risk; unpressurised removes most of it |
| **Meyers 200D** (re-derivation) | Skins, ribs and gussets cut on the router; welding-jig parts and tube-cluster gussets routed or milled; milled fittings | The welded tube cage (a tube-laser service for cutting, and a qualified welder); gear; tanks sealed by the builder or a shop | Skins as the Aries. The cage is the step a home shop should not own unless the builder is a qualified welder |
| **Mooney 301** (metal) | As the Aries | As the Aries; never a home-sealed pressure hull | +600-1,200 h over a service-cut kit (E) |
| **Cessna P210N** | Not applicable | | |
| **Cozy MKIV** (reference) | Designed as a garage build: hot-wire cores and routed bulkheads replace templates and hand cutting | As now | Saves templating hours; the weight stays moldless |

**What the table says.** On the Express a home shop buys a molded-weight
airframe for about $30-60k less cash than a complete kit, at 1,750-4,000 more
builder hours, nearly all mold-making; the IV-P saves more, because its
re-derived kit carries more tooling. The molds outlive one
airplane: if three to five builders share a set, the mold hours per builder fall
to roughly 300-900. On the metal Aries the home shop saves more cash, $40-90k,
for fewer extra hours, because there are no molds to make. Whether a shared
mold set or published CAD files are lawful for a given design is a rights
question, not ours. The parts a home shop should not make are the same on every
design: welded engine mounts and welded primary structure (unless the builder
is a qualified welder), landing-gear legs, pressure-hull sealing, and anything
heat-treated.

### Planform and home-tool envelopes (input to AER-3807)

From `docs/manufacturing/planform_parts.py`. W = 3,000 lb, n_ult = 5.7. Area is
130 ft2 for AR 4-10 and 180 ft2 for the two deltas. Root bending is by Schrenk's
approximation, with no canard share and no inertia relief, so it is
conservative. Cap separation is 0.85 x root thickness. All E.

| Point | AR | Area, ft2 | Span, ft | Root chord, ft | Root depth, in | Spar depth, in | Root moment (ult), 1,000 in-lb | Cap force (ult), 1,000 lb | Carbon cap area, in2 |
|---|---|---|---|---|---|---|---|---|---|
| High AR 10 | 10 | 130 | 36.1 | 4.81 | 8.7 | 7.4 | 804 | 109.2 | 1.37 |
| High AR 8 | 8 | 130 | 32.2 | 5.37 | 9.7 | 8.2 | 719 | 87.4 | 1.09 |
| Moderate AR 6.5 | 6.5 | 130 | 29.1 | 6.17 | 11.1 | 9.4 | 642 | 68.0 | 0.85 |
| Low AR 4 | 4 | 130 | 22.8 | 8.77 | 12.6 | 10.7 | 488 | 45.5 | 0.57 |
| Cropped delta AR 3 | 3 | 180 | 23.2 | 14.08 | 16.9 | 14.4 | 470 | 32.7 | 0.41 |
| Delta AR 2 | 2 | 180 | 19.0 | 18.97 | 18.2 | 15.5 | 369 | 23.8 | 0.3 |

| Point | Skin mold, one-piece wing, ft | Skin mold, two-piece panel, ft | Mold width, ft | Female mold depth, in | 4x8 router tiles per panel mold | Within 6 in Z? | Within 12 in Z? | 800 mm printer tiles per panel mold |
|---|---|---|---|---|---|---|---|---|
| High AR 10 | 37.1 | 17.0 | 5.8 | 8.2 | 6 | no | yes | 21 |
| High AR 8 | 33.2 | 15.1 | 6.4 | 8.8 | 4 | no | yes | 18 |
| Moderate AR 6.5 | 30.1 | 13.5 | 7.2 | 9.7 | 4 | no | yes | 18 |
| Low AR 4 | 23.8 | 10.4 | 9.8 | 10.6 | 6 | no | yes | 16 |
| Cropped delta AR 3 | 24.2 | 10.6 | 15.1 | 13.1 | 8 | no | no | 30 |
| Delta AR 2 | 20.0 | 8.5 | 20.0 | 13.9 | 10 | no | no | 32 |

- **Mold area follows wing area, not aspect ratio.** At a fixed area every
  planform needs about the same mold material and tooling hours. Low AR costs
  more router tiles (8-10 per panel for a delta against 4-6) only because the
  root chord is wider than the 4 ft bed.
- **Spar depth roughly doubles and the root cap force falls about 4.5x from AR
  10 to a delta** (7.4 in and 109,000 lb ultimate, against 15.5 in and 24,000
  lb). At fixed area and t/c, cap force scales about with AR. The root fittings
  carry that force. At AR 8-10 they are large 4130 or 7075 parts that belong at
  a service. At AR 4 and below, the loads come into the range a benchtop mill can
  make in plate, though they still need inspection.
- **Shape of the parts.** High-AR panels are long and narrow (15-17 ft for a
  two-piece wing; a one-piece wing of 33-37 ft is not a home part). Low-AR panels
  are short and wide (8.5-10.6 ft span, 9-19 ft root chord). The layup table and
  oven must take the long dimension either way.
- **Router depth.** Female skin molds run 8-14 in deep. AR 4 and above fit a 12 in
  Z router; the deltas do not. Plugs stacked from routed slabs avoid the limit on
  any router.
- **Printers do the small parts, not the wing.** An 800 mm printer needs 16-32
  tiles to cover one wing-panel mold. It belongs on jigs, small molds, ducts and
  fairings, where it is fast.

## The rebuild questions AERO listed

**Tractor noses and radiator ducts (Aries, IV-P, Meyers, Mooney 301).** Every
design on the list is now a tractor. A new cowl is a small tooling job: a
CNC-routed or printed plug and a glass mold, 40-60 ft2 of mold surface, $8-25k
(E), or home-molded. The radiator wants a ducted chin or belly installation; the
duct is two or three molded parts. For CG, what manufacturing can do is put mass
ahead of the firewall: radiator and coolant (about 35 lb), battery (about 25 lb),
and a longer mount (+3-8 lb). That recovers part of the nose moment, not all of
a 63-242 lb engine saving. Whether the rest is ballast or a loading limit is
AERO's weight-and-balance, which nobody has run yet.

**Aries fuel.** About 20 gal of integral wing tankage closes the 90 nm shortfall
at continuous power. It costs 10-20 lb empty (ribs, sealant, access panels) and
a little under a foot more of tank bay per side. Integral tanks need sealing,
which is a learnable builder skill. It is not the pressure-hull job.

**Express tail and complete kits.** The re-derived tail is part of the mold set
above, not an extra. Built in infused carbon, the tail surfaces can come in well
under the 81 lb one S-90 owner weighed, and that removes the reason for nose
ballast. The tail still has to be flight-tested for stall and departure before a
kit ships. That is AERO's and a test pilot's job, not a manufacturing claim.

**Mooney 301 pressurisation.** For an amateur metal rebuild, deleting it is the
single largest simplification available. It removes the outflow and safety
valves, controller, bleed plumbing, door seals, pressure bulkheads and, above
all, the sealing of every rivet in the pressure hull. It saves 100-200 lb. Whether
the mission can live without it is Bill's and AERO's call.

**Meyers fuel system and cage.** See the note above. The cage is the
re-derivation's identity and also its welding-skill floor.

**Rohr 2-175 scale-up (only if Bill carries it forward).** AERO lists three
questions for us: the sparless foam-core skin, the fold joint and the duct. We
have not started them, and will once Bill carries the design forward.

## Tooling that is lost or never existed

| Design | Original tooling | What re-deriving it would take |
|---|---|---|
| Prescott Pusher | Drawings, structural test reports, loads and weight-and-balance folders at the San Diego Air & Space Museum, collection SC.10269 (public finding guide) | Read the collection, which needs museum contact (Bill's call; Elon has asked), then re-derive. The rights holder is not yet known |
| Bellanca T-250 Aries | Drawings and jigs with a dormant TC holder (A11SW, Anderson Greenwood); not located | Measure one of the four registered aircraft (contact is Bill's call), or recover the drawings through the rights route (Elon, AER-3805) |
| Wheeler Express | Unknown since about 2009 | Re-derive from about 55 active airframes and the CAFE data, with a new tail |
| Lancair IV-P | No known location since the 2017 Uvalde sale; the 2023 JetEXE molds claim was withdrawn | Re-derive from one of about 235 registered airframes, unless the molds turn up. Chain of title to an attorney first |
| Meyers 200D | TC, drawings, jigs and tooling offered for sale in 2019; no sale found | A re-derivation from published geometry and the concept, as Bill asked; what the public record supports is with Elon (AER-3805) |
| Mooney 301 | Nothing: airframe scrapped, data to Tarbes 1987 | A new design from published geometry; a library copy of Jane's 1983-84 and Air International Jan 1984 first |
| Cessna P210N | Textron | Not a revival |

## Hand-offs

- **To AERO:**
  - the rebuild empty weights above, which the stage 3 useful loads move with
    pound for pound
  - the engine-mass corrections, including the Meyers IO-520-A
  - the Aeromomentum installed-weight question
  - the nose CG on four tractors, which is your weight-and-balance
- **To Elon and the board:** build cost, hours, tooling and skill floor for the
  Aries, Express and IV-P, above. For every design, whether a re-derivation, a
  shared mold set or published CAD files are lawful decides what is usable.
- **To Bill, through Elon, only if a design goes forward:**
  - STRUCTURES, for a real laminate schedule or sheet-metal gauges, and for the
    Meyers at a higher gross weight
  - permission to measure an Aries, an Express or an IV-P
  - a question to Aeromomentum on its installed weights

## Reproduce

```sh
cd docs/manufacturing
python3 weights.py          # prints the weight tables in this file and the dossiers
python3 weights.py --json   # writes results.json
python3 planform_parts.py   # the planform tables in the home-shop section
```
