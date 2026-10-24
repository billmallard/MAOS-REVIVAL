# Stage 3 shortlist: five designs ranked on our own performance check

**Status:** stage 3 of the legacy survey (AER-3783), revision 2, compiled
2026-10-24 by AERO after Bill's review of the first version. It builds on the
stage 1 long list (`docs/longlist/LONGLIST.md`, PR #2) and Elon's stage 2 rights
files (`docs/rights/`, PR #3). Bill decides which designs, if any, go further.

**What changed since the first version.** The brief was amended (merged to
`main`): the survey mines commercial failures for their ideas as well as their
numbers; the three targets are separate floors; payload carried 1,000 nm is
information, not pass or fail; and every candidate is screened like for like,
published figures against published figures and measured against measured.
Bill dropped the Rutan Defiant, Cirrus VK-30, Velocity XL-RG and Berkut 360,
kept the Lancair IV-P, Mooney 301 and Wheeler Express (the Express to be dug
into), kept the Cessna P210N only as the calibration case, and added the
Bellanca T-250 Aries and Meyers 200D. The Rohr 2-175 stays in the analysis
whatever the targets say, with two studies in its own section below.

This is a desk study. Our numbers come from published geometry and weights,
calibrated against published flight data. Nothing has been flown, weighed or
measured by us. Rights notes are research, not legal advice. Nobody has been
contacted.

## The ranking

Every speed below states its basis. "As published" is the maker's figure (or,
where marked, a flight test), screened as published. "Our check on the AM20T"
is our drag build-up at the AM20T's assumed 195 hp continuous, in two
critical-altitude cases (8,000 ft and 16,000 ft cruise); see
[The Aeromomentum assumption](#the-aeromomentum-assumption).

| Rank | Design | Seats | As published: useful load / range / cruise (floors) | Our check on the AM20T: KTAS / useful load / range on full fuel at continuous power (floors) | Rights (stage 2) | Safety record | Why it died; does a revival fix it? |
|---|---|---|---|---|---|---|---|
| 1 | [Bellanca T-250 Aries](candidates/bellanca-t250-aries.md) | 4-5 | 1,300 lb / 1,017 nm with 45 min / 181 KTAS at 75%, altitude not stated (AOPA measured 181 at 6,500 ft): **all three pass** | 185-197 / 1,300 / 906-919 nm: speed and load pass; range misses by about 90 nm at continuous power, passes at economy (154-161 KTAS) | TC A11SW current, held by Anderson Greenwood (a valve maker); stage 2 file pending | 1 NTSB event in about 50 years, no fatal; only 4 aircraft, so no rate | Its producer, Bellanca, went into receivership in 1980. Yes: nothing technical killed it |
| 2 | [Wheeler Express](candidates/express-2000.md) | 4 | 1,045 lb / 1,401 nm (CAFE-computed) / no maker's speed; measured 169 KTAS at 6,190 ft, 901 lb weighed | 179-191 / 890 / 1,062-1,115 nm: speed and range pass; useful load misses by 110 lb on the weighed aircraft | Orphaned: five owners, three bankruptcies; last holder (2007) untraced | 18 fatal, 30 killed, on about 100 registered; the NTSB named its poor yaw stability; stall in climbing right turns, including Grand Prairie (CEN21LA096) | Business execution (incomplete kits, churn) plus a public tail problem. Yes, with a re-derived tail at 2-4 kt cruise cost and complete kits |
| 3 | [Lancair IV-P](candidates/lancair-iv-p.md) | 4 | 1,350 lb / 1,347 nm with 45 min / 287 KTAS at FL240: **all three pass** | 200-211 / 1,350 / 1,136-1,155 nm: **all three pass** on factory empty weight | Open: chain of title (2023 sale scope not public, molds unlocated) | 88 events, 43 fatal, about 360 built; low-altitude stall-spin and engine failure followed by stall | Kits retired for newer models. The safety pattern is the real problem; the RDD LX7 re-wing shows it can be engineered out, at about 25 kt and $800k+ |
| 4 | [Meyers 200D](candidates/meyers-200d.md) | 4 | 1,060 lb / 782 nm with 45 min / 182 KTAS at 75%, altitude not stated: range fails; measured 178 KTAS at 8,500 ft, about 900 lb fleet useful | 178-189 / 1,060 / 831-863 nm: speed and load pass on factory weight; range misses by 140-170 nm | TC 3A18 current, small holder; TC, drawings and tooling offered for sale in 2019 | 26 accidents, 6 fatal; fuel starvation from the four-tank system is the pattern; no breakups | Hand-built at a loss. Yes, as a re-derivation designed for production, with more fuel |
| 5 | [Mooney 301](candidates/mooney-301.md) | 6 | 1,452 lb (design) / 986 nm with 45 min / 235 KTAS at FL250 (design): range near miss | 176-187 / 1,452 / 1,143-1,169 nm: **all three pass** on design weight | Open: Mooney or Daher, unresolved; nothing usable survives | One prototype, no accidents; its pitch control "not certifiable" per its test pilot | A corporate sale; new owners wanted 300 kt. Partly: the market gap is real, but nothing survives to revive |
| cal. | [Cessna P210N](candidates/cessna-p210n.md) | 6 | Calibration case only (Bill: "not solving some of what I'm after in the innovation side") | 161-171 / 1,658 / 916-931 nm | Firmly held by Textron | 291 events, 78 fatal, 874 built | Not a revival candidate |
| ref | [Cozy MKIV](candidates/cozy-mkiv.md) | 4 | 1,000 lb / 1,130 nm at 40% / 191 KTAS at 75%, 8,000 ft: **all three pass**. Measured (CAFE): 871 lb / 1,049 nm still air / 177 KTAS at 8,000 ft | 202-217 / 808 / 645-668 nm | Firmly held by Aircraft Spruce | 22 events, 7 fatal, about 350 built | Alive. The yardstick |

**How the floors read.** Useful load is the factory empty weight's figure unless
marked; kit-built and equipped fleets run heavier (the Cozy by 129 lb, the
Express by 144 lb, the Meyers by about 160 lb), so read every factory useful
load as an upper bound until stage 4 replaces it. Range on the AM20T is still
air with no reserve on standard usable fuel at the assumed continuous power;
every design gains range at economy power. Payload carried 1,000 nm, the old
combined test, is in the [results table](#results-on-the-aeromomentum-line) as
information only.

## What the check says

1. **On separate floors, two of the five clear all three on the AM20T on our
   numbers**: the IV-P and the Mooney 301, both on factory or design empty
   weights. The Aries clears speed and useful load and falls about 90 nm short
   of the range floor at continuous power (it clears it at economy power). The
   Express misses useful load on its weighed aircraft by 110 lb; the Meyers
   misses range on its 74 gal.
2. **The reference passes as published and misses on useful load as measured.**
   The Cozy MKIV's published figures (1,000 lb, 1,130 nm, 191 KTAS) pass all
   three floors. The CAFE Foundation weighed its test aircraft at 1,179 lb empty,
   so 871 lb useful; it measured 177 KTAS at 8,000 ft; and fuel and measured flow
   give 1,049 nm still air with no reserve. Both bases are kept and compared like
   for like. The first long list's 951 nm was a basis mismatch, not a units error.
3. **Our build-up agrees with two of the new designs' published speeds.** The
   Aries's AOPA points need a drag factor of 1.26-1.34, inside the fleet band
   (1.16-1.36), and the Meyers needs 1.41, just above it. Neither speed is
   flattered. The Aries's published range reads about 10% optimistic.
4. **Two headline speeds still read cleaner than any measured airplane:** the
   IV-P's 278 KTAS and the 301's 237.5 KTAS need factors of 1.03 and 1.02. We
   headline the fleet calibration for both, about 8% slower.
5. **The Express's accident record has an engineering explanation and a priced
   fix**, set out in its dossier: weak directional stability from a fin too small
   for its fuselage (on our estimate, near neutral below about 15 ft2 of fin),
   power raised from the 210 hp the tail was tested with to 250-300 hp, and
   stall speeds 9-12 kt above the published figures. A 20-24 ft2 fin or the
   S-90 tail, with dorsal and ventral fins, costs 2-4 kt of cruise.
6. **The engine is still the largest single unknown.** Aeromomentum publishes no
   continuous rating, critical altitude or fuel consumption for the AM20T. Our
   two critical-altitude cases move speed by 9-15 kt.

## Why this order

The ranking weighs, in order: whether there is something to revive (a design,
data, a type certificate, airframes), what it does on the Aeromomentum line by
our own numbers on separate floors, whether its safety record is tied to the
configuration and fixable, whether a revival fixes what killed it, and what it
contributes to the idea ledger.

- **Bellanca T-250 Aries, first.** It is the only design that passes all three
  floors as published, has a published speed our check agrees with, fits the
  AM20T directly at the same cruise power, has a current type certificate, and
  died for a reason (its producer's receivership) that a revival removes. It was
  also designed to be cheap to build: flat and single-curve skins around a
  laminar wing. Its weaknesses are that only four exist, so its clean record
  proves little, and that it is about 90 nm short of the range floor at
  continuous power on standard fuel.
- **Wheeler Express, second.** It is the best-measured design in the survey, and
  Bill's strongest interest. Its accident record is tied to the configuration,
  but the cause is now specific (the tail, the power it was asked to handle, and
  optimistic stall speeds), and so are the fixes and their cost. It died of
  business execution, which a revival with complete kits fixes. It ranks below
  the Aries because the tail must be re-derived and flight-tested first, it
  misses useful load on its weighed aircraft, and its rights are orphaned.
- **Lancair IV-P, third.** It has the speed (200-211 KTAS on 195 hp) and a large
  fleet. Its fatal record is the worst in the survey and its stall-spin half is
  tied to a 36 lb/ft2 wing loading; it would fly on about 55% of its design
  power; and its chain of title is open. The LX7 re-wing is the evidence that the
  wing can be fixed, and the price of doing it.
- **Meyers 200D, fourth.** Bill's interest is the re-derivation, and that fits the
  numbers: the speed is there and the range and empty weight are not, both of
  which a new wing and structure designed for production would address. It ranks
  above the 301 because a type certificate, drawings and 58 airframes exist.
- **Mooney 301, fifth.** The best payload-range on our numbers and the only
  six-seater near the mission, but nothing of it survives, its rights are
  unresolved, and its tail was judged not certifiable. A revival is a new design
  using its layout.

## The Rohr 2-175: the two studies

Kept in the analysis whatever the targets say (Bill: "The planform, the layout
meets much of what I'm after"). Not ranked. Both studies are in its dossier,
[docs/candidates/rohr-2-175.md](candidates/rohr-2-175.md):

1. **Scale-up:** the 2-175's configuration taken to four seats on an AM20T, and
   where it stops working.
2. **Reconstructability:** what survives (photographs, three-views, the TWITT
   talk, the patent, the SDASM collection, the tribute book) and what it yields.

**Scale-up, in short.** The 2-175's own design target (152 kt at 10,000 ft on
150 hp) is credible on our check: its geometry gives 142-151 KTAS on the power
available. Taken to four seats on an AM20T (2,900 lb, an estimated 1,060 lb
useful, 105 gal), the pure low-aspect-ratio delta sits on the 160 KTAS floor at
8,000 ft; with aspect ratio 3-4 it reaches 159-172 KTAS at 8,000 ft and
167-183 KTAS at 16,000 ft, with 1,090-1,180 nm on 105 gal. That clears the
floors on paper, about 15-20 kt below the Express and the Aries on the same
engine. It stops working at:
- **landing speed**, as wing loading must about double from the 2-175's
  8.1 lb/ft2;
- **balance**, with the engine behind two rows of seats on a tailless wing;
- **the drive shaft**, the weak point of every buried-engine pusher in this
  survey;
- **the weight estimate**, which is unproven.

**Reconstructability, in short.** More survives than the stage 1 and 2 files
knew. A Rohr engineer's labelled three-view settles the geometry (span 20 ft,
not 30; wing 180 ft2). A dimensioned Rohr duct, fan and stator sketch and
ten factory photographs (SDASM, 2025-26) also survive. Together they rebuild
the outer lines and propulsor layout to about 5-10%. The structure, airfoil,
flown propeller, weights and performance do not survive and would be
re-engineered and then measured.

**The book.** *The Rohr 2-175 (71X) FanJet: A Tribute* (Fraser with
Westergren, self-published about 2012, 166 pages, ISBN 978-0-615-59079-0). It
has been out of print since at least 2019. No listing or library copy was found
in the catalogues we could reach. WorldCat, eBay, Biblio and Alibris block
automated access and need a few minutes in a browser. Buying a copy is Bill's
call.

## Dropped by Bill, and why

| Design | Bill, 2026-10-24 | What stays |
|---|---|---|
| Rutan Defiant | "no chance. Rutan has it and it's not what I'm after." | Long-list row; stage 3 check in its dossier; centreline thrust in the idea ledger |
| Cirrus VK-30 | "no thanks" | Long-list row; check in its dossier; its shaft-drive lessons for any buried-engine pusher, the Rohr included |
| Velocity XL-RG | "no chance." | Long-list row; check in its dossier; a note on Peter Muller's Raptor (the successor attempt Bill held a reservation for) in its idea ledger |
| Berkut 360 | "not likely. These were expensive to build." | Long-list row; check in its dossier |

## Not shortlisted, and why

| Design | Reason |
|---|---|
| Piper PA-46-310P, Mooney Acclaim Type S, Cessna TTx, Socata TB-21 | Live type families held firmly by large OEMs (stage 2). The realistic path is modifying existing airframes |
| Epic LT | Turbine; no Aeromomentum equivalent |
| Bellanca Skyrocket II | 435 hp, no fuel capacity found. Kept on the long list as a configuration reference |
| Piper Comanche 400, Mooney M22 | 400 and 310 hp: far from 195 hp continuous |
| Lancair Super ES | Same holder as the IV-P; the IV-P covers the family |
| Wing Derringer and its analogs | The Derringer (an abandoned TC) stays on the long list. Its current analogs, led by the Alpi Pioneer 800 Twin shown at AERO 2026, are four-seat Rotax twins; none is a two-seater, and none has a published range and fuel flow to screen fully (long list) |
| Windecker Eagle | A near miss with thin geometry; the first certified all-composite airplane, in the idea ledger |
| Extra EA-400 | The published numbers do not add up (stage 1) |
| Evektor SuperCobra, Grob GF 200 | No fuel flow or no empty weight |
| 210-class kits (Bearhawk 5, Murphy Moose and others) | Noted in the long list at Bill's request; fixed-gear utility kits, none a retractable 210 copy |

## Ideas worth a look: commercial failures outside the long list

Bill asked for further failures whose ideas deserve a look even where the
numbers miss. These are proposals for the long list, not yet screened; the
figures are as published and graded in the research note
(`docs/shortlist/ideas/README.md`).

| Design | Years, built | Idea worth keeping | Why it failed |
|---|---|---|---|
| Mooney M20L PFM | 1988-89, 41 | An automotive-derived (Porsche) engine with single-lever electronic power control in a certified four-seater: the closest precedent to an Aeromomentum installation | Support and liability, not the airframe |
| Toyota FV2400 engine (and the TAA-1) | 1991-2002 | A certified automotive-derived V8 with dual-channel FADEC, flown in a Cessna 340 testbed | A car maker judged the market too small and the cost too high |
| Cessna 182 JT-A diesel | 2007-15, not certified | A four-seat piston at 1,018 lb useful and 1,025 nm on paper (maker's figures), on a 227 hp diesel | The engine supplier and the certification timeline |
| Diamond DA50 (2007 programme) | 2007-09, prototypes | An airframe designed from the start for gasoline, diesel or turboprop up to 350 hp; fixed gear at 180 kt | Programme shelved |
| Scaled Composites Catbird | 1988, 1 | A three-surface, flapless laminar composite five-seater: 192 mph average on 8.9 gph over a CAFE course (R) | A one-off demonstrator |
| Commander 114TC | 1995-2002 | A roomy, strong turbocharged four-seater: 187 KTAS at 75% (P) | Capital and market |
| Adam A500 | 2002-08, 7 | Centreline push-pull twin, and a warning: about 160 lb of payload with full fuel as built against 2,100 lb planned (via Wikipedia) | Empty-weight growth and money |
| AASI Jetcruzer | 1989-2002, 5 | A canard pusher certified against spin-resistance criteria | Money; wrong size and engine for us |
| Wassmer WA-50 series | 1966-77, 154 | The first certified all-composite production four-seater | Small maker, small market |
| Seawind 300C | 1982-2021, about 80 kits | A composite amphibian that still carried 1,100 lb (F) | Certification and funding |
| Lear Fan 2100 | 1981-85, 3 | Buried engines driving one pusher prop through shafts, in a pressurised composite fuselage: the Rohr's propulsion idea at a larger scale | Certification cost and money |

## The Aeromomentum assumption

Aeromomentum publishes, for the AM20T: 260 hp at 5,800 rpm, 300 hp for 5 min,
285 lb dry, liquid-cooled, $27,995 (grade F,
https://aeromomentum.com/am20t-230hp-300hp/, re-read 2026-10-24). It does not
publish a continuous rating, a critical altitude or a fuel consumption. Every
number in this document that uses the AM20T or AM15T rests on these
assumptions, which are **ours**:

| Item | Assumed | Basis |
|---|---|---|
| Continuous power | 75% of the take-off rating: 195 hp (AM20T), 120 hp (AM15T) | The usual GA cruise rating convention. Not published |
| Critical altitude | Two cases: 8,000 ft (AM-low) and 16,000 ft (AM-high); Gagg-Ferrar lapse above | Brackets a single-turbo automotive installation. Not published |
| BSFC | 0.45 lb/hp/h | The same estimate as stage 1 (Gudmundsson ch. 7). Not published |
| Installed mass | dry x 1.25 (Aeromomentum's own installation note) + 35 lb for radiator, coolant and plumbing | The 35 lb is ours |
| Cooling drag | Raymer's piston formula, the same as air-cooled | A liquid-cooled radiator can do better (Meredith effect) or worse; not credited either way |

This is an **open risk**, and it can only be closed by data from Aeromomentum or by
a test. Asking Aeromomentum is contact with a manufacturer, which needs Bill's
go-ahead. That question is raised on the issue, not assumed.

## Results on the Aeromomentum line

Our numbers, from `docs/shortlist/check/results/` (regenerate with
`report.py`). Bracketed values are the optimistic bound: the other drag factor
and full credit for a lighter engine. The payload columns are information only.
The four designs Bill dropped are kept at the bottom as record.

| Candidate | Engine | Cruise alt | KTAS at continuous power (optimistic) | Useful load, lb (optimistic) | Range, nm, full fuel, no reserve | Payload @ 1,000 nm, no reserve, lb | Payload @ 1,000 nm, 45 min, lb (optimistic) | Economy (65%) KTAS: payload no res / 45 min |
|---|---|---|---|---|---|---|---|---|
| Bellanca (Anderson Greenwood) T-250 Aries (Model 51, O-540 250 hp) [AM-low] | AM20T | 8k | 185 (186) | 1,300 (1,364) | 906 | cannot | cannot (cannot) | 154: 901 / 859 |
| Bellanca (Anderson Greenwood) T-250 Aries (Model 51, O-540 250 hp) [AM-high] | AM20T | 16k | 197 (198) | 1,300 (1,364) | 919 | cannot | cannot (cannot) | 161: 903 / 861 |
| Wheeler Express FT (CAFE N360EZ) [AM-low] | AM20T | 8k | 179 (186) | 890 (890) | 1,062 | 376 | cannot (cannot) | 149: 481 / 439 |
| Wheeler Express FT (CAFE N360EZ) [AM-high] | AM20T | 16k | 191 (199) | 890 (890) | 1,115 | 393 | cannot (347) | 157: 487 / 445 |
| Lancair IV-P (TSIO-550, 30.2 ft wing) [AM-low] | AM20T | 8k | 200 (218) | 1,350 (1,592) | 1,136 | 881 | cannot (1,094) | 161: 962 / 920 |
| Lancair IV-P (TSIO-550, 30.2 ft wing) [AM-high] | AM20T | 16k | 211 (231) | 1,350 (1,592) | 1,155 | 888 | 824 (1,100) | 164: 953 / 911 |
| Meyers / Aero Commander 200D (IO-520-A 285 hp) [AM-low] | AM20T | 8k | 178 (184) | 1,060 (1,149) | 831 | cannot | cannot (cannot) | 148: 648 / cannot |
| Meyers / Aero Commander 200D (IO-520-A 285 hp) [AM-high] | AM20T | 16k | 189 (196) | 1,060 (1,149) | 863 | cannot | cannot (cannot) | 155: 652 / cannot |
| Mooney 301 (TIO-540 360 hp prototype) [AM-low] | AM20T | 8k | 176 (193) | 1,452 (1,659) | 1,143 | 922 | 858 (1,107) | 142: 1,015 / 973 |
| Mooney 301 (TIO-540 360 hp prototype) [AM-high] | AM20T | 16k | 187 (205) | 1,452 (1,659) | 1,169 | 931 | 867 (1,114) | 146: 1,006 / 964 |
| Cessna P210N (TSIO-520-P, 1980 POH) [AM-low] | AM20T | 8k | 161 (162) | 1,658 (1,819) | 916 | cannot | cannot (cannot) | 130: 1,183 / 1,142 |
| Cessna P210N (TSIO-520-P, 1980 POH) [AM-high] | AM20T | 16k | 171 (171) | 1,658 (1,819) | 931 | cannot | cannot (cannot) | 132: 1,173 / 1,132 |
| Cozy MKIV (CAFE N494CZ, IO-360 180 hp) [AM-low] | AM20T | 8k | 202 (206) | 808 (808) | 645 | cannot | cannot (cannot) | 172: cannot / cannot |
| Cozy MKIV (CAFE N494CZ, IO-360 180 hp) [AM-high] | AM20T | 16k | 217 (221) | 808 (808) | 668 | cannot | cannot (cannot) | 184: cannot / cannot |
| Rutan Defiant (Model 40, 2x O-320 160 hp) [AM-low] | 2x AM15T | 8k | 178 (197) | 1,350 (1,358) | 1,094 | 721 | cannot (709) | 150: 858 / 807 |
| Rutan Defiant (Model 40, 2x O-320 160 hp) [AM-high] | 2x AM15T | 16k | 190 (212) | 1,350 (1,358) | 1,156 | 747 | 669 (732) | 159: 871 / 821 |
| Cirrus VK-30 (IO-540 290 hp prototype) [AM-low] | AM20T | 8k | 199 (208) | 1,350 (1,471) | 1,225 | 880 | 815 (954) | 165: 973 / 931 |
| Cirrus VK-30 (IO-540 290 hp prototype) [AM-high] | AM20T | 16k | 212 (221) | 1,350 (1,471) | 1,257 | 890 | 825 (963) | 174: 973 / 930 |
| Velocity XL-RG, optional 100 gal tanks [AM-low] | AM20T | 8k | 186 (203) | 1,000 (1,104) | 1,213 | 505 | 440 (583) | 157: 613 / 571 |
| Velocity XL-RG, optional 100 gal tanks [AM-high] | AM20T | 16k | 199 (217) | 1,000 (1,104) | 1,275 | 522 | 457 (597) | 167: 620 / 578 |
| Velocity XL-RG (IO-550 310 hp) [AM-low] | AM20T | 8k | 186 (203) | 1,000 (1,104) | 825 | cannot | cannot (cannot) | 157: 613 / cannot |
| Velocity XL-RG (IO-550 310 hp) [AM-high] | AM20T | 16k | 199 (217) | 1,000 (1,104) | 860 | cannot | cannot (cannot) | 167: 620 / cannot |
| Berkut 360 (IO-360 205 hp) [AM-low] | AM20T | 8k | 239 (249) | 949 (949) | 873 | cannot | cannot (cannot) | 205: 650 / 608 |
| Berkut 360 (IO-360 205 hp) [AM-high] | AM20T | 16k | 256 (266) | 949 (949) | 906 | cannot | cannot (cannot) | 218: 658 / 616 |

## Our numbers against the published ones, on the original engines

| Design | Published claim | Our number at the same power and altitude | Gap | Verdict |
|---|---|---|---|---|
| Bellanca T-250 Aries | 181 KTAS at 6,500 ft, 73%; 189 KTAS at 1,000 ft, full throttle (P, AOPA 1977) | matched with 1.26-1.34 | - | Agrees: inside the fleet band. The published 1,017 nm with a 45 min reserve reads about 10% optimistic against our 1,008 nm still air with no reserve at 65% |
| Meyers 200D | 178 KTAS at 8,500 ft, about 67% (P, AOPA 1991) | matched with 1.41 | draggy | Slightly above the fleet band, consistent with an old riveted airframe; its own factor is used |
| Lancair IV-P | 278 KTAS at FL230, 262 hp (P) | 255 KTAS at the fleet calibration | -8% | Published figure optimistic, or this airplane is the cleanest measured. Unproven |
| Mooney 301 | 237.5 KTAS at 17,500 ft, 270 hp (P) | 217 KTAS | -9% | Same as the IV-P |
| Wheeler Express | 169 KTAS at 6,190 ft DA, ~169 hp (P, CAFE) | 164 KTAS | -3% | Agrees: this is a calibration case |
| Cessna P210N | 152-193 KTAS at 10,000-23,000 ft (POH) | matched with 1.26-1.32 across seven points | - | Calibration case; the spread is tight |
| Cozy MKIV | 169-182 KTAS at 850-12,000 ft DA (R, CAFE) | matched with 1.32-1.39 across four points | - | Calibration case |

Do the published power and fuel flow agree with each other? For every
published point with both, the implied BSFC (gph x 6 / hp) is 0.39-0.51 lb/hp/h:
0.39-0.42 for the leaned or lean-of-peak points (Express, IV-P, Mooney 301,
Velocity) and 0.43-0.51 for best-power and handbook points (Cozy, Defiant,
VK-30, P210N). That is the normal range for these engines, so no published
speed here hides an impossible power. Once a type's drag factor matches its
published speed, our fuel flow at that speed checks only our BSFC (0.45, or the
POH-derived 0.50 for the P210N and 0.42 for the lean-of-peak IV-P and 301), so
it is not counted as independent evidence.

The four designs Bill dropped keep their comparison rows in their dossiers and in the first version of this file (PR #4 history).

## Method

One pipeline for every type, in `docs/shortlist/check/`:

1. **Geometry.** A parametric OpenVSP model per type (`vspgen.py`): wing,
   canard or tail, fins or winglets, strakes, and a fuselage on a generic
   station profile scaled to the published length, width and height. Every
   dimension is sourced and graded in `geometry/<id>.json`; what we had to
   estimate (tail areas by volume coefficient, fuselage cross-sections, chords
   that close a published area) is listed in each model's `assumptions`. OpenVSP
   CompGeom gives the wetted area of each component, with buried area removed.
   Fidelity: about +/-3% on the lifting surfaces and +/-10% on the fuselage. This
   is not a lofted reproduction.
2. **Parasite drag.** A component build-up (Raymer, *Aircraft Design* ch. 12;
   Hoerner, *Fluid-Dynamic Drag* ch. 6 and 8 for form and interference): mixed
   laminar-turbulent skin friction with a stated laminar run per component, form
   factors by component type, interference factors 1.00-1.05, a fixed-gear
   allowance where the gear is fixed, cooling drag by Raymer's piston formula
   (eq. 12.39) with an installation factor, and 5% for leakage and protuberances.
3. **Calibration.** We match the build-up to every published point that states
   altitude and power by scaling parasite drag by a factor k. The factor absorbs
   power-estimate, propeller and drag errors together; it is not a pure drag
   number. The fleet calibration is the median of the three instrumented or
   handbook cases (1.29; range 1.16-1.36). Each type uses the larger of its own
   factor and the fleet's, so no type is flattered by its own brochure.
4. **Induced drag.** Oswald efficiency (Raymer eq. 12.48). For canards the
   lift is split between the surfaces (18-20% on the canard) and each surface
   takes its own CL^2/(pi A e). Canard-wing interference is not modelled.
   Induced drag is 5-18% of the total at the reference cruise point for
   these types, so a 20% error in it moves speed by about 1% at most.
5. **Propeller.** McCormick's actuator-disk ideal efficiency at the cruise thrust
   and disk area, times 0.85 for profile and swirl losses, times a stated
   installation factor (0.95-0.97 for fixed-pitch or wake-immersed props). The
   cruise efficiencies come out at 0.79-0.84.
6. **Power.** Normally aspirated engines lapse by Gagg-Ferrar. Turbocharged
   engines are flat-rated to a critical altitude, then lapse by Gagg-Ferrar.
   Where a flight test gives manifold pressure and rpm but not power (the CAFE
   reports), we estimate power at full throttle only, grade E.
7. **Range and payload.** A constant-altitude, constant-speed cruise integrated
   in 5-10 lb fuel steps. This is the exact form of the Breguet range relation
   for that schedule, with the power required recomputed as weight falls. Each
   flight also carries a taxi and climb allowance (10 lb plus twice the ideal
   potential-energy fuel), and no descent credit. Payload at 1,000 nm is solved
   from MTOW, with and without a 45 min reserve at the end-of-cruise power.

**What this method cannot see.** It does not resolve laminar-flow loss from
bugs or rain, real cooling-system design, trim drag beyond the canard lift
split, or propeller-airframe interaction for pushers. Dynamic stability, spin
behaviour and flutter are outside it entirely. Where the safety record raises
those, it is reported from the record and labelled as such; nothing here
clears or condemns a design on handling.

**Tail study (Express).** `docs/shortlist/check/express/tail_study.py`
builds directional stability from the fuselage (Raymer eq. 16.47) and a
parametric fin (Raymer eq. 12.6 lift slope; DATCOM sidewash), scales CAFE's
measured stalls to weight and bank, and runs each tail fix through the same
calibrated model. Its fin areas are parametric because no Express fin dimension
is published.

## Hand-offs

- **To Bill:** one card on AER-3783 asks which designs to take further.
- **To MANUFACTURING (AER-3784, stage 4):** the revised shortlist. Four of five
  designs are new to stage 4 or changed: the Aries (an all-metal design built
  for low production cost), the Meyers (a re-derivation: steel-tube cage, new
  wing with more fuel), the Express (with a re-derived tail), and the 301 (a new
  design from its layout). The useful load of each moves pound for pound with the
  empty weight a modern rebuild achieves.
- **To Elon (stage 2, AER-3805):** rights files for the Aries (TC A11SW) and the
  Derringer analogs; the Meyers re-derivation question; the Lancair holders and
  Bill's Austin company; the Rohr book and the SDASM catalogue.
- **SAFETY is not part of this stage.** Two patterns would need SAFETY before any
  development decision: the Express's stall in climbing turns and the IV-P's
  low-altitude stall-spin record. Per the epic, that is asked on AER-3785 first.

## Reproduce

```sh
# from a host where `maos` is available (OpenVSP runs in the maos-aero-tools container)
cp -r docs/shortlist/check /maos-work/aero/analysis/AER-3783
cd /maos-work/aero/analysis/AER-3783
for m in models/*.json; do python3 run_check.py "$m" > "results/$(basename "$m" .json).txt"; done   # writes vsp/, results/<id>.json; stdout is results/<id>.txt
python3 report.py                                            # writes results/tables.md, results/<id>_stage3.md
python3 express/tail_study.py > express/tail_study_output.md # the Express tail study
```

`vspgen.py` expects the folder at `/maos-work/aero/analysis/AER-3783`, which the
container sees as `/workspace/analysis/AER-3783`; change `CONTAINER` in that file
to run it elsewhere. Copy results back into the repo by reading and writing the
files, not with plain `cp`: on this host's network share, `cp` has written NUL
holes into fresh files.
