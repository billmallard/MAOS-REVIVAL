# Prescott Pusher: evidence for the stage 3 deep dive

Stage 3 revision (AER-3783, 2026-10-24), from Bill's request. The dossier
(`docs/candidates/prescott-pusher.md`) carries the reading; this folder carries
the evidence and the arithmetic.

- `levers.py` / `levers_output.md`: the Prescott on Aeromomentum engines at
  altitude, with the fuel, structure and gross-weight levers, on two drag bases
  (brochure-consistent k 1.35, measured-consistent k 1.55). Run it from the
  analysis workspace, where it finds `perf.py` and the model.
- `balance.py` / `balance_output.md` (AER-3866): the re-derivation with
  MANUFACTURING's structure delta, the weight-and-balance of the AM20T
  installation on stations read off the designer's plan, the four balance
  options, and a rotation moment check. It supersedes `levers.py`'s structure
  placeholders and its guessed balance arms. Runs from the repo:
  `python3 balance.py > balance_output.md`.
  AER-3902 folded in SAFETY's three input corrections (N747P's 49 lb ballast
  datum, the constant-speed propeller, option C's neutral-point loss); the
  output's correction ledger walks from PR #10's first numbers to the
  corrected ones.
- `SAFETY.md` (AER-3899): SAFETY's review of the balance options, the
  approach and landing technique and the accident record, committed verbatim
  by AERO. Its constraints R1-R10 bind any re-derivation.
- `avl/prescott_np.avl` / `avl/prescott_np_st.txt`: the wing + T-tail
  vortex-lattice model behind the neutral point (`maos avl`, OPER `a a 2`, `x`,
  `st`).
- The desk research below was done by a delegated research agent and reviewed
  by AERO; quoted strings were re-fetched and matched against their sources
  before commit. Public sources only; nobody was contacted.

## Balance study (AER-3866): how the stations were read

Source: Tom Prescott, "Prescott Pusher", *RCM*, July 1986, plan 971 (three
sheets, "Designed & drawn by Tom Prescott") and its article, on Outerzone
oz14320 (Wayback copies in `balance.py`'s header). The plan is a 1/5-scale
model of prototype 1 (N41PP); the article's table gives the full-scale
"Prototype" dimensions, and the text gives the one full-scale station we have:

> "The real aircraft has the main wheel located at fuselage station 244
> extended, and retracts to fuselage station 257.4. (The fuselage nose tip is
> station 92.)" (*RCM* July 1986, p. 51; read from the scan, F)

Everything else was measured by AERO on sheet 1's fuselage side view, rendered
at 200 dpi with PyMuPDF. Scale: nose tip to spinner tip is set to the table's
20.28 ft (the plan's printed scale reads 0.7% short), which makes one pixel of
a 5.011x-reduced working image 0.126 in full scale. Readings (working-image x,
then full-scale FS):

| Feature | Image x, px | FS | Note |
|---|---|---|---|
| Nose tip | 33.9 | 92.0 | datum, by the article |
| Wing root leading edge | 851 | 195.1 | inner (root-template) outline, not the fillet |
| "C.G. RANGE" marks, forward / aft | 1,019 / 1,071 | 216.2 / 222.9 | symbol centres; 12.7-27.0% MAC |
| Model nose-wheel axle | 433 | 142.4 | the model's gear |
| Model main axle | 1,087 | 224.9 | the model's, not scale (the article puts the scale position at FS 244) |
| Bulkhead F-5 ("firewall" in the article) | about 1,515 | about 279 | the engine's accessory end |
| Fuselage tail, F-6 aft face | 1,844 | 320 | prop plane taken at FS 322 |
| Horizontal tail root leading edge | about 1,623 | 292.5 | the fin-top section |
| Heights above the ground line: CG mark, thrust line | - | about 31 in, 58 in | at the model's gear height; we use 36 and 55 in |

Reading accuracy is about 1 in full scale. The model is "stand-off sport
scale", so every station is graded E. The "C.G. RANGE" is drawn on the model
plan; the article does not say it is the full-scale range, though the model
was scaled from the full-scale design and flown for data. We read it as the
designer's range and say so wherever it is used. The plan images are not
committed (RCM reserves its rights); the Wayback links regenerate them.

What the plan settles, and what it does not:
- The engine sits about 73 in behind the aft CG limit and the nose bay about
  123 in ahead of it, so one pound of engine needs about 0.6 lb of nose
  ballast, not the 1.33 lb that stage 3 assumed.
- The main wheels sat 21-28 in behind the CG range on prototype 1: a tipback
  of 30-38 deg, against the usual 15. That is the hard rotation in the record.
- The empty-weight CG and its scatter are not on the plan. One builder
  aircraft bounds it: N747P needed "49 pounds of ballast necessary to get the
  weight and balance within its prescribed limits" (SA91, p. 49; found by
  SAFETY, AER-3899), at an unpublished station. `balance.py` carries that as
  its headline datum (AER-3902). SDASM's weight-and-balance schedule
  (SC.10269) would settle it; reading it is museum contact, Bill's call.

## Desk research: Prescott Pusher: configuration, performance, fleet, safety, demise

AER-3783 desk research, 2026-10-24. Public material only; no one contacted.
Companion file: `prescott-pusher.json` (geometry + safety per SCHEMA). Ownership is in
`_prescott_rights.md` and is not redone here.

Grades: **F** factory/designer, **T** TC, **P** flight test / POH / magazine pilot report /
NTSB final, **B** builder/owner/registry/listing, **L** low (forum, wiki, aggregator),
**E** my estimate (method stated). Text in quotation marks is verbatim from the cited page.

Key sources (short names used below):
- **SA86**: Dick Cavin, "Tom Prescott's Pusher", *Sport Aviation*, March 1986 (with Jack Cox sidebar "Linden's Legacy"), text via Wayback copy of pdfhall: http://web.archive.org/web/20231210045500/https://p.pdfhall.com/tom-prescotts-pusher_5b7134c2097c4780378b4584.html
- **AOPA86**: *AOPA Pilot*, March 1986, pp. 100-104 (6-page scan, author's byline page not in the scan): https://www.aeroresourcesinc.com/uploads/198603-1986%20Prescott%20Pusher%20Kit.pdf
- **RCM86**: Tom Prescott, "Prescott Pusher", *RCM* July 1986, plan 971, 1/5-scale R/C model, article and plan on Outerzone oz14320: https://outerzone.co.uk/plan_details.asp?ID=14320 ; article PDF https://outerzone.co.uk/download_file.asp?planID=14320&FileType=Supp&Filename=Prescott_Pusher_oz14320_article.pdf
- **SA88**: Dick Cavin, "Prescott Pusher II", *Sport Aviation* April 1988 (first page only): http://web.archive.org/web/20231210014544/https://p.pdfhall.com/prescott-pusher-ii_5bd1fa54097c47e8248b456d.html
- **KP88**: Kitplanes "Archive: May 1988" (2022 retrospective summary of LeRoy Cook's May 1988 report): https://www.kitplanes.com/archive-may-1988/
- **SA91**: Jack Cox, "Russ and Marcia Taylor's Prescott Pusher", *Sport Aviation*, September 1991, pp. 43-49: http://web.archive.org/web/20241217134717/https://p.pdfhall.com/russ-and-marcia-taylors-prescott-pusher_5b6d873e097c4748748b4604.html
- **TP07**: Tom Prescott's remarks and spec, 1000aircraftphotos No. 6802 (N42PP), 2007: https://1000aircraftphotos.com/Contributions/6802.htm
- **AZ**: airplanezone "Oshkosh Scrapbook: The Prescott Pusher": https://airplanezone.com/Oshkosh/Scrapbook2003/Prescott_Pusher.html
- **VS**: Vic Syracuse (first customer-built Pusher) columns in Kitplanes: Checkpoints https://www.kitplanes.com/checkpoints-11/ , https://www.kitplanes.com/checkpoints-3/ , https://www.kitplanes.com/checkpoints-24/ , https://www.kitplanes.com/checkpoints-14/ , https://www.kitplanes.com/checkpoints-34/ ; Archive Feb 1989 https://www.kitplanes.com/archive-february-1989/
- **FG**: SDASM finding guide SC.10269: https://sandiegoairandspace.org/files/Prescott_Aeronautical_Corporation_Collection-FG-SC.10269.pdf
- **FAA**: FAA ReleasableAircraft.zip (MASTER, DEREG, ACFTREF), downloaded 2026-10-24: https://registry.faa.gov/database/ReleasableAircraft.zip
- **NTSB**: NTSB final reports (URLs in the accident table); NTSB avall/Pre2008 databases and CAROL queried 2026-10-24.

---

## 1. Configuration in detail

### Engine and propeller drive: there is no long shaft
- **The engine is in the tail cone, directly behind the cabin. It drives the prop through a ~12 in extension, not a driveshaft.** SA86 (P): "Mounting it further aft is the way Prescott does it and the shaft is only 12" long." Cavin contrasts this with mounting the engine amidships, which needs a 5-6 ft shaft "with vibratory problems". AOPA86 (P) describes an aft-mounted engine driving the pusher prop through a ~12-inch propeller shaft extension. The designer gives the reason in RCM86 (F): "Early in the design, I decided not to accept the challenges associated with a mid-engine aircraft and the six to eight foot drive shaft that the mid-engine dictates." Wikipedia (L) has the same 12 in figure: https://en.wikipedia.org/wiki/Prescott_Pusher
- **Vibration in flight:** Cavin tried to detect resonance from the 12 in shaft: "I also was curious to see if we could detect any resonant vibration from the 12" shaft." He felt only a slight amount, once or twice, when the throttle was pulled back fairly quickly at about 120 mph (SA86, P; the scanned text is broken across columns there, so this is paraphrased).
- **Parts:** the SDASM drawing list has "15302 - prop extension" and "15303 - Bushing- prop. Adapter", plus 15001 engine installation and 15104 engine mount assembly (FG, P). **No coupling, bearing, torsional damper or driveshaft drawing appears in the list.** INFERENCE (E): the extension is a flanged spacer bolted to the crankshaft flange, carrying the prop on its outer flange. It is not a separate shaft with its own bearings. Whether it was solid or hollow, and what material, is not published.
- **Service history:** no shaft or drive failure appears in any record found. The one drive-train event is N43PP (2005). Its wooden prop separated in cruise: the prop and all attach bolts were missing from the prop flange, and "Three of the bolt holes showed evidence of rubbing and partial elongation of the holes" (NTSB LAX05LA270, P). The prop had been removed and refitted two weeks earlier. The NTSB cause was "the in-flight separation of the propeller for undetermined reasons." Which flange is meant (crank or extension) is not stated.
- **Weight-balance consequence:** to offset the aft engine, the battery and oil cooler sit in the nose (SA86, P). AOPA86 says the nose bay holds the oil coolers and the hydraulic power pack.

### Propeller
- Prototype 1 (N41PP): fixed-pitch wood cruise prop. With it the engine reached only 2,400 rpm on takeoff, which Cavin estimated at about 130 hp, and 2,600 rpm at full throttle. A 3-blade Hoffmann constant-speed prop was on order (SA86, P).
- Diameter: "maximum propeller diameter flown was 68 in (1.63 m) and recommended was 65 in (1.65 m) by the factory" (TP07, F; the metric conversions are the page's own, and 68 in is actually 1.73 m). Tom Prescott judged that an O-540 would make prop clearance an issue without a four-bladed prop (TP07).
- Planned: Prescott bought AVIA Products Co. to develop an electrically controlled multi-blade fiberglass prop (SA86; AOPA86, P). TP07's spec block lists "four-bladed variable pitch". Builder N747P went from a wood fixed-pitch prop to a 3-blade MT constant-speed prop with a 14 in spinner (SA91, P). Italian I-EFTP (Allison 250) advertises a 5-blade prop (winglist, B).
- **Ground clearance: not published.** AZ (L): "The short landing gear mandated a short and inefficient prop." AZ also says marginal prop clearance forced the main gear further aft than ideal. NTSB LAX05LA270 records that a replacement prop "was too long for ground clearance".
- RCM86 plan note (F, model; read from the plan image, not text-searchable): a 14 in maximum prop diameter at 1/5 scale. That scales to 70 in (E).

### Tail
- **T-tail** on a swept fin (SA86; AOPA86, P). The stabiliser sits on top of the fin with a single full-span elevator and trim tab (AOPA86).
- The RCM86 1/5-scale plan shows a small **ventral "sub fin"** under the tail cone, ahead of the prop (F, model plan). No full-scale drawing was found to confirm it.
- Horizontal tail (RCM86 'Prototype' table, F): span 11.00 ft, root chord 3.33 ft, tip chord 2.17 ft, area 29.3 sq ft. The model sheet gives NACA 66(1)-012, a T-tail and -1.5 deg incidence. On prototype 1 the elevator incidence went from -1.5 to -3.0 deg (AOPA86, P).
- Fin (E): model sheet height 8.5 in and average width incl. rudder 10.9 in, i.e. about 42.5 in high, about 54.5 in mean chord and about 16 sq ft at full scale. The model is stand-off scale, so these are rough.
- Changes: prototype 2 got elevator bobweights (KP88, P). AOPA86 reports planned changes to elevator hinging and gap and a lighter tail structure.

### Cooling
- Air-cooled engine in the tail cone. Drawings exist for cooling baffles (15901, 15902) and the oil cooler air box (11901) (FG, P).
- The first two flights of N41PP had unacceptably high oil temperatures. "The fix was to relocate the oil cooler from the engine bay to the nose bay." Adding a spinner raised available prop rpm by 500 and "further improved engine cooling" (AOPA86, P). The nose has an oil-cooler air inlet (SA86, P).
- In the field, builder N747P reported: "Our one persisting mechanical problem is the right rear cylinder, which runs hotter than the rest." The Taylors hoped the MT prop's spinner would improve the cooling outflow (SA91, P).
- Fatal N58PP (Ford V-6): No.3 plug burned or melted and the others showed excessive heat; the cause was a builder-set lean carburetor float and a capped vent (NTSB LAX90DUM02, P). Inlet and outlet areas, and any fans, are not published.

### Structure
- **Fuselage:** TIG-welded square 4130 tube. Tubes are "3/4" .035 wall for the predominate structure to one and one quarter by .065" wall for the wing carry through members"; square tube allowed a 20% wall reduction (SA86, P). The non-structural fiberglass shell (3 to 8 plies, CAD-cut patterns) is flush-riveted to metal bulkheads and the halves are epoxied top and bottom. Everything can be installed before the shells go on (SA86, P). The plugs cost about 1/10 of the $200,000 factory tooling (SA86).
- **Wing:** aluminum, flush-riveted. The spar is a press-brake-formed .050 2024-T3 C-section with nested 2024-T351 extrusion caps (3 laminations at the root tapering to 1 at the tip). Ribs are .032 at about 15 in spacing. Leading edges are .040, stretch-formed on CAD/CAM steel dies, held on dry ice in the "O" condition and age-hardened to T-42. The spar bolts to the carry-through with a 5/8 in 4130 fitting and two 5/8 in bolts per side (SA86, P). Builders built their own spars and drilled the root holes, which set the dihedral, from a factory jig. Syracuse found that following the jig instructions would have given negative dihedral (VS Checkpoints-14, B).
- Strength (SA86, P): main spar tested beyond +3.8/-1.5 g; gear drop-tested to 5.5 g "as per FAR 23". Tom Prescott: original TOGW 2,250 lb; "The loads report was modified and structural testing conducted using a maximum TOGW of 2,400 lb (1,089), 3.8G positive and 1.5G negative load factors." (TP07, F). Flutter testing was 95% done by a Burbank firm in Jan 1986, with a 260 mph dive planned to set Vne at about 235 mph (SA86, P). Wing static test 16 Sep 1986 and other structural test reports are listed in FG (P).
- **Gear:** fiberglass mains (7 lb per leg) and Airite nose gear. Hydraulic gear and flaps (one pump, emergency hand pump); hydraulic nose steering via rocker switch, to become mechanical on production (SA86; AOPA86, P). Retractable and fixed versions were offered (AOPA86). Main gear moved about 8 in forward on prototype 2 (KP88, P).
- Not certificated. Development followed Part 23 but certification was not sought (AOPA86, P).

### Published dimensions

| Item | Value | Grade | Source / note |
|---|---|---|---|
| Span | 29 ft 4 in | F | TP07 |
| Span | 28.5 ft | P | SA86 (prototype 1) |
| Span | 30.00 ft | F | RCM86 table |
| Wing area | 110.8 sq ft (AR 7.76) | F | TP07 |
| Wing area | 110 sq ft (AR 7.3), mean chord 3.93 ft | P | SA86 |
| Wing area | 113 sq ft | F | RCM86 |
| Root / tip chord | 4.67 / 3.00 ft (taper 64.3%) | F | RCM86 |
| Airfoil | NLF(1)-0215F, 15%, root modified; reflexed flaps/ailerons -5 deg | P | SA86 |
| Sweep / dihedral / incidence / washout | 10.25 deg / 3 deg / 2 deg / -1.5 deg | P | SA86 |
| Length | 20 ft 3.4 in (20.28 ft) | F | TP07, RCM86 |
| Height | 8 ft 9 in | F | TP07 (RCM86 says 9.67 ft) |
| Fuselage width | 3.67 ft | F | RCM86 |
| Cabin width | 42.5 in inside ("Cabin width is a comfortable 42.5" inside.") | P | SA86 (TP07: 3 ft 6 in) |
| H-tail | 11.0 ft span, 29.3 sq ft | F | RCM86 |
| Fin | about 16 sq ft, about 42.5 in high | E | scaled from RCM86 model sheet |
| Fuel | 56.5 gal in wing leading edges (prototype 2), up from 45 gal fuselage tank | P | KP88; SA86; AOPA86 |
| MTOW | 2,400 lb (original design 2,250 lb) | F | TP07 |
| Empty | 1,550 lb factory; design empty 1,220 lb in 1986 | F | TP07; AOPA86 |
| Baggage | 100 lb | F | TP07 |

### Three-views and photos
- **Outerzone oz14320** (RCM plan 971, July 1986, 1/5-scale R/C model, drawn by Tom Prescott, 3 sheets, 72 in span). Sheet 1 has fuselage top and side views and fin parts. It is a model plan with a bar scale, not a dimensioned full-scale three-view. The companion article has the full-scale "Prototype" dimension table used above. https://outerzone.co.uk/plan_details.asp?ID=14320
- No Jane's, aerofiles or magazine three-view was found online.
- Photos: 1000aircraftphotos No. 6802 (N42PP) https://1000aircraftphotos.com/Contributions/6802.htm and No. 5648 (N41PP) https://1000aircraftphotos.com/Contributions/KleinBernhard/5648.htm . The SA86 scan has close-ups of the tail cone, frame and tooling. The AOPA86 scan has photos of the frame, gear trunnions and reflexed surfaces. No published close-up of the prop extension itself was found.

---

## 2. Performance as published and as measured

| Source | Aircraft | Figure | Conditions given | Grade |
|---|---|---|---|---|
| KP88 (LeRoy Cook, May 1988) | N42PP (prototype 2, 'frozen design') | "174 mph true at 73% power (from a 180-hp Lycoming O-360)" = 151 KTAS | **Altitude, weight, OAT, rpm, prop: not given** in the online summary; the full article was not found | P |
| TP07 brochure spec | (factory) | cruise 190 mph (165 kt) at 7,500 ft; max cruise 200 mph (174 kt) | power not stated; Prescott: "All technical data provided was tested at the 2,400 lb (1,089) TOGW." | F |
| TP07 | N42PP | "the Pusher (N42PP) achieved 200 mph (329 kmh) CAS" | sea-level standard day, "blue printed" engine of 200+ hp (non-standard) | F |
| SA86 (Cavin, Jan 1986) | N41PP | IAS "just over 170 mph" at full throttle (2,600 rpm), flaps -5 | fixed-pitch wood cruise prop, 2,250 lb, OAT mid-40s F at Wichita (~"sea level standard" per author); Cavin: no point quoting speeds until the right prop is fitted | P |
| AOPA86 | objectives | 75% cruise at 7,500 ft 156 kt; max 160 kt; approach-configuration stall 57 kt; SL climb 980 fpm | retractable, constant-speed prop, 180 hp, 2,250 lb gross | F (objective) |
| SA86 | N41PP | climb 800-1,100 fpm at 110 mph after clean-up; takeoffs about 27 s into near-zero wind | 2,250 lb, fixed prop | P |
| SA91 | N747P (IO-360, wood fixed prop) | "about a thousand feet per minute" | solo, about half fuel, climb at 105 mph | P (builder) |
| SA86 | N41PP | stall "58 mph to 66 mph IAS according to flap and gear configuration used" | 2,250 lb | P |
| TP07 | spec | stall 72 mph clean, 66 mph full flap | 2,400 lb | F |
| KP88 | N42PP | stall break at 66 mph indicated; over-the-fence 95 mph; best landing technique to fly it on at about 75 mph | n/a | P |
| SA91 | N747P | gap seals: stall from 72 to 60 mph; without seals "it would not rotate until it reached 75" | builder | B (via P magazine) |
| TP07 / Wikipedia | spec | range 1,000 mi; ceiling 18,000 ft | **reserve basis not stated** | F / L |

Notes:
- AOPA86 reports "no aerodynamic warning" before the stall: "There is no aerodynamic warning" and the company was trying stall strips.
- Fuel flow is not given for any point. 151 vs 165 KTAS: the magazine number is 14 kt below the brochure number, but the altitude for the magazine number is unknown. A 2022 Kitplanes retrospective sums up: "the performance (cruise speed against landing speeds) failed to impress" (KP88).
- Syracuse: "The Prescott Pusher with the 180-hp Lycoming really didn’t match up to its marketing numbers." (VS Checkpoints-11, B).

---

## 3. Fleet

FAA registry, 2026-10-24 (B). Method: matched ACFTREF model codes whose maker or model contains PRESCOTT (18 Prescott Pusher codes, including the misspelt "PRESCOT PUSHER"; an audit recount, 2026-10-24, found five other PRESCOT codes that are not Pushers). Also matched four-seat models named PUSHER, KIT MFR/KIT MODEL containing PRESCOTT, and the known N-numbers, in both MASTER and DEREG. Positive control: the registry query code reproduces the rights file's four MASTER records.

| N-number | s/n | Year | File | Engine (FAA code) | Status / notes |
|---|---|---|---|---|---|
| N41PP | 001 | 1985 | MASTER | O-360 180 hp | Prototype 1; Kansas Aviation Museum; Exp. R&D/market survey; AW 1986-09-24 |
| N10JS | 008 | - | MASTER | **Allison 250** turbine | Los Angeles CA; amateur-built; AW 1991-10-02; re-registered 2024 |
| N200SX | 100 | 1994 | MASTER | O-540 250 hp | Fort Myers FL; AW 1996-07-03; renewed 2023 |
| N40LE | 32 | 1998 | MASTER | (blank; O-540 per TP07) | Ole Sindberg, IL; no AW date or class on file; Prescott (2007) says he had the most hours of any kit builder |
| N128S (ex-N42PP) | 002 | 1987 | DEREG | unknown | Prototype 2, "PUSHER AIRCRAFT INC", Wichita; AW 2000-03-01; cancelled 2018 |
| N11NF | 011 | 1995 | DEREG | O-360 | AW 1995; cancelled 2012 |
| N19PP | 09 | 1990 | DEREG | IO-360 | AW 1990; accident 2009; cancelled 2012 |
| N225CK | 003 | - | DEREG | - | cancelled 2001 |
| N24VT | 29 | 1988 | DEREG | O-360 | AW 1988; cancelled 2013. E: probably Vic Syracuse's aircraft (he was "builder number 29", finished 1988) |
| N27HL | 015 | - | DEREG | - | cancelled 2011 |
| N310PP | 031 | - | DEREG | - | "PRESCOT PUSHER"; cancelled 1995 |
| N35PP | 35 | 1992 | DEREG | IO-360 | AW 1992; cancelled 2018 |
| N41TP / N655TH | 030 | 2017 | DEREG | unknown | same s/n; N655TH AW 2017, kit field "PRESCOTT AERONAUTICAL CORP"; cancelled 2023 |
| N43PP | 050 | 1988 | DEREG | IO-360 200 hp | AW 1988; accident 2005; cancelled 2008 |
| N516PJ | 023 | - | DEREG | - | cancelled 1998 |
| N58PP | 42 | - | DEREG | Ford V-6 | fatal 1990; cancelled 1990 |
| N747P | 13 | - | DEREG | IO-360 | Taylor; accident 1992; cancelled 1992 |
| N90DX | 014 | 1999 | DEREG | IO-540 300 hp ("PRESCOTT PUSHER 540") | AW 1999; cancelled 2002 |
| N925CU | 036 | - | DEREG | unknown | AW 2004; kit field Prescott; cancelled 2023 |
| N75FM | 028 | - | DEREG | Ford V-6 | "MUNTWYLER/PIERSON PUSHER", 4 seats; fatal 1990. **Probable, not confirmed, Prescott** |

- **Count:** 4 current and 15 more deregistered = **19 distinct Prescott airframes** ever on the US register (20 with N75FM). Kitplanes (2020) said "Some 16 Prescott Pushers are currently on the FAA register" (https://www.kitplanes.com/archive-january-1988/); that is not consistent with today's 4.
- **Likely airworthy now:** N10JS and N200SX (valid registration, AW dates, renewed 2023-24). N40LE has valid registration but no AW data. N41PP is a museum exhibit. Recent flight activity could not be checked (FlightAware gives no history without login).
- **Outside the US:** OE-VPJ (msn 025, Austria, crashed 2004; a damaged Austrian Pusher was offered for sale on HBA in 2014: https://homebuiltairplanes.com/threads/for-sale-prescott-pusher-damaged.18085/ , B). I-EFTP (s/n 055, Italy, Allison 250-B15G, 200 h, EUR 140,000 on winglist, B: https://www.winglist.aero/listings/P5p5BZM7/2013-prescott-pusher). A German Pusher had a gear-up landing in 2002 (registration not given).
- **Production:** "Manufactured 68 kits/3 aircraft." (Wings Over Kansas, https://wingsoverkansas.com/legacy/a93/ , L/S). By Sep 1987 "close to 150 builders had made the initial leap", mostly buying the introductory trim-tab kit, "but it is estimated that about half will drop by the wayside" (SA88, P). The Taylors knew of 25-30 still building in 1991 (SA91).
- **Wide engine variety** (O-360/IO-360, O-540/IO-540, Ford V-6, Mazda rotary, Allison 250) shows builders re-engining for power. TP07 warned that bigger engines turn it into a two-seater.

### Builder-fleet empty weights

| Aircraft | Empty weight | Grade | Source |
|---|---|---|---|
| Factory projection | 1,550 lb | F | TP07 |
| 1986 design empty | 1,220 lb | F | AOPA86 ("Design empty weight is 1,220 pounds, and gross, 2,250.") |
| N747P (Taylor) in shop | "1,555 pounds, which was in line with the factory's projected empty weight of 1,550 pounds" | P | SA91 |
| N747P finished | 1,661 lb, with paint, interior, avionics and ballast for c.g. | P | SA91 ("the final weight came out at 1,661") |
| I-EFTP listing | 703 kg (= factory 1,550 lb copied) | B (not a weighing) | winglist |
| Barnstormers "$3000.00 or Make Offer" PDF | 1,550 lb (Wikipedia copy) | L | https://barnstormers.s3.amazonaws.com/media/docs/doc_SPECIFICATION_2012943_1761094112.pdf |

At 1,661 lb empty and 2,400 lb gross, useful load is 739 lb. With 56 gal (336 lb) of fuel that leaves about 400 lb, i.e. two adults (E, arithmetic). This is consistent with Syracuse's "really only a two-seat airplane" (VS Checkpoints-24: "it was really only a two-seat airplane and required above-average piloting skills.").

---

## 4. Safety record

Queries: local NTSB avall.mdb + Pre2008.mdb (1982-present): make or model containing PRESCOTT or PUSHER, plus every N-number above. CAROL API: make contains PRESCOTT, model contains PRESCOTT, model contains PUSHER, make contains PUSHER. Both returned the same Prescott events. ASN type list "PUSH": https://aviation-safety.net/asndb/type/PUSH

| Date | Reg | NTSB no. | Phase | Fatal | Cause (per report) | Config-related? |
|---|---|---|---|---|---|---|
| 1990-05-17 | N58PP (s/n 42, Ford V-6 260 hp, 2 h) | LAX90DUM02 | initial climb, first flight | **Y (1)** | engine seizure; carb float set very lean, vent capped; builder maintenance | Auto-engine conversion; heat damage noted |
| 1990-09-30 | N75FM ("Pierson Pusher", Ford 3.8 V-6, 28 h) | CHI90DEE10 | initial climb | **Y (1)** | choke activated by mistake (handle resembled nose-gear release); stall in forced landing | Prescott identity probable, not confirmed |
| 1992-09-20 | N747P (s/n 013, IO-360, 106 h) | MIA92LA186 | go-around | N (1 minor) | go-around at ~5 ft, "THE NOSE OF THE AIRPLANE PITCHED UP, THE AIRPLANE STALLED"; airspeed not maintained | **Pitch behaviour**: same pilot had reported pitch sensitivity and roll-off at lift-off (SA91) |
| 2002-05-22 | (Germany) | BFU 3X080-0/02 | landing | N | gear-up landing | No |
| 2004-05-12 | OE-VPJ (msn 025) | none (news, via ASN) | initial climb, test flight | N | fell from ~5 m; aircraft destroyed; cause unknown | Unknown (possibly takeoff handling) |
| 2005-08-14 | N43PP (s/n 050, IO-360 200 hp, 154 h) | LAX05LA270 | cruise, 7,500 ft | N (1 serious) | "the in-flight separation of the propeller for undetermined reasons" | **Prop attachment on the extension installation**; prop recently refitted |
| 2009-06-24 | N19PP (s/n 009, IO-360 200 hp, 104 h) | CEN09CA386 | approach | N | "A partial loss of engine power due to propeller damage from being struck by the cabin-entry door, which inadvertently opened and departed the airframe for undetermined reasons during flight." | **Pusher-specific**: departed parts go through the prop |

NTSB report URLs:
- LAX90DUM02: https://app.ntsb.gov/pdfgenerator/ReportGeneratorFile.ashx?EventID=20001212X23153&AKey=1&RType=Final&IType=FA
- CHI90DEE10: https://app.ntsb.gov/pdfgenerator/ReportGeneratorFile.ashx?EventID=20001212X24208&AKey=1&RType=Final&IType=FA
- MIA92LA186: https://app.ntsb.gov/pdfgenerator/ReportGeneratorFile.ashx?EventID=20001211X15757&AKey=1&RType=Final&IType=LA
- LAX05LA270: https://app.ntsb.gov/pdfgenerator/ReportGeneratorFile.ashx?EventID=20050817X01262&AKey=1&RType=Final&IType=LA
- CEN09CA386: https://data.ntsb.gov/carol-repgen/api/Aviation/ReportMain/GenerateNewestReport/74130/pdf
- ASN: https://aviation-safety.net/wikibase/440282 (Germany), https://aviation-safety.net/wikibase/191809 (OE-VPJ)

**Totals:** 4 confirmed US NTSB events (1 fatal), plus a probable fifth (fatal). Two non-US events. Syracuse corroborates N75FM: "There were a couple of fatalities on other Blanton-equipped Prescott Pushers due to engine failures." (VS Checkpoints-11, B). Both fatal aircraft were Ford V-6 conversions.

**Configuration flags:**
- **Shaft/drive failure:** none on record. There is no long shaft. N43PP's prop separation is the only drive-train event, and its cause is undetermined.
- **Prop strike / clearance:** no prop-strike accident found. Clearance is repeatedly called marginal (AZ, TP07, NTSB LAX05LA270).
- **Rotation and pitch at takeoff:**
  - AOPA86 (P): "I had already been briefed that ground effect at flying speed creates a pitch-up tendency." The author over-rotated and over-corrected on his first takeoff. Also: "At low speed, particularly when in ground effect, pitch is quite sensitive and the feel is not linear".
  - SA91 (P, builder): "As it lifted off, it rolled to the right about 20 degrees".
  - VS (B): "When the aircraft jumped off the ground unexpectedly and began to oscillate in pitch I immediately threw the bag of lead underneath the rudder pedals on the right side." and "Yes, we narrowed the CG envelope after that flight." (Checkpoints-3).
  - AZ (L): "Some of the problems reported were high takeoff (rotation) speeds, pilot induced oscillations on takeoff, and uncommanded rolls on takeoff."
  - Barnaby Wainfan (Kitplanes Wind Tunnel, P-analysis): main gear too far aft makes rotation hard, which "was also reportedly a problem for the Prescott Pusher." https://www.kitplanes.com/wind-tunnel-8/
- **Cooling:** prototype oil overheat fixed by moving the cooler to the nose; builders' hot rear cylinder (AOPA86, SA91).
- **Fleet for rates:** about 20 airframes with unknown hours. No meaningful rate can be computed.

---

## 5. Why it died

1. **Handling and performance reputation (record).**
   - The early press reports flagged pitch sensitivity and ground-effect behaviour (AOPA86). Kitplanes Oct 1986 wrote that "refinements should tame some of the takeoff and landing quirks" (quoted in KP88).
   - AZ (L): "What ultimately killed the market for the Prescott Pusher, however, was the negative buzz generated after some early completions."
   - The first customer to fly called it "a good 2+2 airplane, somewhat of a ground hog" (VS Checkpoints-11).
   - Wainfan (Kitplanes Wind Tunnel 47): "Unfortunately, once it got into the air, it proved to have disappointing performance." https://www.kitplanes.com/wind-tunnel-47/
2. **The layout itself.** Wainfan, Wind Tunnel 88 (https://www.kitplanes.com/wind-tunnel-88/): "A rear-engine airplane like the Prescott Pusher is very challenging aerodynamically because the flight CG is so far aft on the fuselage." With the c.g. far aft, the main gear had to go aft and the gear was short for prop clearance. That produced a small prop and hard rotation (AZ).
3. **Financing and control.**
   - Investors: Jack DeBoer was the major investor. Linden Blue (ex-Beech CEO) joined as investor and CEO (SA86). The Jack Cox sidebar says Blue made a "substantial investment" the previous June and became company chairman.
   - Tom Prescott's own account (TP07, F): "The original marketing grass-roots pay-as-you-go approach was elevated to a high-dollar pay-up-front strategy." His technical input and Stan Blankenship's market savvy were the key elements, and "These two key elements evaporated in the face of requirements demanded by the financial backer." He also says the delivered kits "had the essence but not all the aerodynamic and structural refinements envisioned or planned".
   - The RCM86 article describes the original plan: subsequent kits ship only after payment, because a kit maker "cannot become the banker".
4. **Parts and delivery.** Syracuse in 1989: "I started out as builder number 29 and I finished first–only because I kept dogging Prescott for parts" (VS Archive Feb 1989). Also: "the Prescott team was much better at marketing than producing parts" (VS Checkpoints-11).
5. **Kit model, price and build effort.** 33 sub-kits, each with a manual and video (AZ, L). AOPA86 (P): complete kits, which exclude avionics, instruments, interior, engine, engine mount and prop, "are priced at $29,500 and $36,500, respectively" (fixed and retractable). Also "The company projection of time to complete is 1,500 hours". SDASM: "estimating completion for one plane at about five years" (FG). Syracuse took "over two years". **Competitor prices and build hours from the same period (Glasair, Lancair, Velocity, Express) were not found in a fetched source,** so no comparison is made. Syracuse says the choice for a four-seat kit then was "limited at that time to the mostly-metal Prescott Pusher and the fiberglass Wheeler Express" (VS Checkpoints-11).
6. **1988-1991.** Kitplanes reports that in October 1988 Prescott Aeronautical was "quitting its Wichita, Kansas, operation. The company was being sold to an Australian outfit, which offered no plans about further development of the design." (https://www.kitplanes.com/25th-anniversary-engines-of-change/). In early 1989 Prescott "had decided to stop selling kits" (VS Archive Feb 1989). Wings Over Kansas: operations 1983-1989. SDASM: "in 1991 the company folded as builders were still completing their aircraft" (FG). The Taylors had almost all their parts when "the company announced it was closing its doors" (SA91).
7. **Builders' accounts.**
   - PoA thread (L): an acquaintance who built one said "his was a dog with fleas, or words to that effect". Another member's broker had one "until the prop separated from the airframe in cruise" (= N43PP). https://www.pilotsofamerica.com/community/threads/prescott-pusher.131882/
   - The Taylors stayed positive. They believed that with time to try different engine/prop combinations "it might be a popular kit today" (SA91, paraphrase of a broken passage).

---

## 6. Stall/spin, glide, ride, noise, cabin, storage, construction

- **Stall:**
  - SA86 (P): stall "super gentle, with practically zero roll tendency". A 35 deg flap stall from 10-15 deg bank rolled off only about 5 deg; Cavin credits the Super Tips.
  - AOPA86 (P): no aerodynamic warning, stalls mild; accelerated stalls not tried.
  - KP88 (P): "It is best to avoid full-stall landings, which tend to be firm as the airplane suddenly quits flying."
- **Spin:** not spun as of Jan 1986, waiting for spin-recovery rockets from Germany. The R/C models were "very difficult to get them to spin at all" (SA86). No later spin test was found.
- **Stability:**
  - SA86: dynamic directional and pitch damping good; 25 deg bank picked up with rudder alone at 1.3 Vs.
  - AOPA86: adverse yaw present. Spiral stability better to the right. Bump-induced pitch excursions took three to four oscillations to settle.
- **Glide ratio:** not published.
- **Ride / gust response:** nothing specific beyond the AOPA86 pitch-oscillation note. Wing loading is 21.7 lb/sq ft at 2,400 lb on 110.8 sq ft (E, arithmetic).
- **Noise:** "Noise level at taxi rpm allows normal conversation" (SA86, P; split across a column break in the scan). AOPA86 claims a quieter cabin for the pusher layout, as a design reason, not a measurement.
- **Cabin:** 42.5 in wide (SA86); "Cabin size is the same as a Bonanza" (SA86, a separate sentence about size, not width). Prototype seats were 3 in too high. The rear seats sit higher, on the carry-through (AOPA86). Big left canopy door; baggage bay behind the rear seats. The rear-seat load limits the c.g. (SA91 notes ballast was needed).
- **Storage:** 29 ft 4 in span, 20 ft 3 in length, 8 ft 9 in height (TP07). Wings bolt on at the root with two bolts per side (SA86), but no folding or quick removal is described. It needs a standard T-hangar for its size (E).
- **Construction as builders found it:**
  - Fit was praised: "Early builders remarked of the quality and fit of the sub-kits" (AZ).
  - Marcia Taylor, a first-time builder, found the metal work "really fun". The worst job was attaching the fiberglass shell: "It was messy and needed a lot of work" (SA91).
  - Syracuse caught a spar drill-jig error that would have given negative dihedral (VS Checkpoints-14).
  - Kits arrived slowly (VS).

---

## Gaps (searched, not found)

- **Kitplanes May 1988 conditions** (altitude, weight, OAT, rpm, prop) for 151 KTAS / 73%. Searched kitplanes.com (archive page, site search, WP API), archive.org advanced search, aeroresourcesinc (only the AOPA Mar 1986 scan turned up), web search. Kitplanes Oct 1986 not found either. eBay sellers offer 1986/1988 scans; not purchased.
- **Flying Oct 1985 p.106; Flying Apr 1988 (Eric Weiner, "Un-conventional Values"); Popular Mechanics Aug 1986:** Google Books returned 403 and then a CAPTCHA; the Books API daily quota was exhausted. Not read.
- **Sport Aviation Apr 1988 "Prescott Pusher II":** only page 1 visible on the Wayback/pdfhall copy. Not found: AOPA Pilot May 1986 kit article, Air Progress, Private Pilot, Homebuilt Aircraft magazine.
- **Prop extension design** (solid vs hollow, material, any damper or bearings) and any service bulletins. SDASM lists drawings 15302/15303 only; reading them requires contacting SDASM (not done).
- Prop ground clearance; fuel flow at any cruise point; full-scale tail areas from a primary source; fin chords; cooling inlet/outlet areas; glide ratio; spin test results; range reserve basis.
- **Builder empty weights** beyond N747P. Barnstormers, winglist, Controller (0 listings) and HBA were checked; the listings repeat factory figures. No Trade-A-Plane or AOPA classifieds entries were found.
- **Recent activity** of N10JS, N200SX, N40LE: FlightAware shows no history without login. ADS-B archives not searched.
- **Competitor kit prices and build hours** in 1986-88 for Glasair, Lancair, Velocity and Express: not found in a fetched source.
- **N75FM identity** as a Prescott kit: FAA s/n 028 and the 2,400 lb MGW fit, but NTSB lists 2 seats and s/n 1. The docket was not requested.
- No three-view from Jane's, aerofiles or a magazine was found online. airwar.ru (L) lists sources, including Flying Apr 1988: http://www.airwar.ru/enc/la/pusher.html
