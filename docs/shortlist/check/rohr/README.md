# Rohr 2-175: scale-up study, reconstructability inventory, the book

Stage 3 revision (AER-3783, 2026-10-24), from Bill's review. The dossier
(`docs/candidates/rohr-2-175.md`) carries the reading; this folder carries the
evidence and the arithmetic.

- `scaleup.py`: the 2-175 as built through our method, then the four-seat
  scale-up on an AM20T (planform, fan and balance sweeps). Run it from the
  analysis workspace, where it finds `perf.py`: `python3 scaleup.py > scaleup_output.md`.
- `scaleup_output.md`: its output.
- The inventory below was done by a delegated research agent and reviewed by
  AERO; quoted strings were re-fetched and matched against their sources before
  commit. Public sources only; nobody was contacted; nothing was bought.

## Desk research: Rohr 2-175 (71X / 71-X): what survives for a rebuild, and the Fraser book

AER-3783 desk research, 2026-10-24. Public sources only. Nobody was contacted and nothing was bought. Ownership is covered in `_rohr_rights_pr1.md` and is not repeated here.

Grades: F factory or designer (includes Rohr project staff writing first-hand); T type certificate; P flight test, official record or patent; B builder, owner or registry; L low (forum, wiki, aggregator); E our own estimate. Quotes are verbatim from the URL cited next to them. Where the TWITT PDF's OCR text layer is garbled, I quote the same article from de Piolenc's own clean web copy (massflow, Wayback 2006).

## Bottom line

- **There is much more geometry available than the rights file suggests.** Richard W. Fraser, a Rohr project engineer, put the late-configuration 3-view online on his company site (2008-2022, now only on the Wayback Machine). It is labelled with span, length, engine and areas. He also posted a dimensioned Rohr sketch of the duct, fan and stator, with airfoils, and a ducted-fan efficiency map. Together with ten Rohr factory photos that SDASM posted on Flickr in 2025-26 (including a clean underside planform shot), they would let an engineer rebuild the outer lines and the propulsor layout to about 5-10%.
- **The published span and length conflict is settled.** Fraser says the 20 ft span and 23 ft length are correct and that the 30 ft / 28 ft labels on Mooney's earlier 3-view (copied by aerofiles) are errors. Our scaled measurements of the late 3-view agree with 20 ft and 23 ft (below).
- **What does not survive publicly:** empty weight, fuel capacity, measured speeds, static thrust, structural layup, airfoil coordinates, and the wood 4-blade propeller that actually flew. No airframe survives.
- **The book exists and has an ISBN, 978-0-615-59079-0.** It was self-published by Fraser Aero Technology Company (Orange, CA): a 166-page colour paperback, US$19.98, last sold by Aircraft Spruce as part 13-11711. It is out of print. No library holding, used copy or live listing was found in the catalogues I could reach. WorldCat, eBay, Biblio and Alibris blocked automated access.

## 1. Reconstructability inventory

| # | Item | Location | Access | What it yields | Grade |
|---|---|---|---|---|---|
| 1 | **Late 3-view, titled ROHR 71X** (no canard strakes, so it matches the flying aircraft) | Fraser site, `images/71X_3View_A.jpg` (2983x2423 px): https://web.archive.org/web/2011id_/http://www.fraseraerotechnologycompany.com/images/71X_3View_A.jpg | Online free (Wayback) | Plan, front and side views. Labels: 2 place, span 20 ft, length 23 ft, Lycoming O-320X, wing 180 sq ft, vertical tail 16 sq ft, elevons 22.8 sq ft, gross 1,450 lb. With the labelled span as scale it yields the planform, the fold line, the dog-tooth position, the duct diameter and length, the fin sweep, the side profile and the gear track (our measurements in section 2). | F (Fraser posted it; drafter not stated) |
| 2 | **Early Mooney 3-view, titled Rohr 2-175 (71X)** (with canard strakes) | Fraser site `images/2-175_1_.gif`: https://web.archive.org/web/2011id_/http://www.fraseraerotechnologycompany.com/images/2-175_1_.gif ; same drawing at aerofiles http://www.aerofiles.com/rohr-3vu.jpg (credited to TWITT) | Online free | Three views with a data block: basic wing (incl. control surfaces) 180 sq ft, vertical tail 18 sq ft, elevons 22.8 sq ft, delta slat (exposed) 3.4 sq ft, gross 1,450 lb. Dimension labels of 30 ft span and 28 ft length, plus a height label of 25 ft. Fraser calls those dimensions errors (see section 2). Useful for the strake and slat layout of the early configuration. | F (dimension labels discredited) |
| 3 | **Rohr propulsor sketch titled Configuration of RP-17-V Propeller** (Figure 1 of a Rohr memo; image text, so not quoted) | Fraser page 2, `images/Prop_Fig._1.jpg` and the cleaner `images/Prop_Config.jpg` (same Wayback path) | Online free | **Duct:** NACA 23015 section, length 2.75 ft, area ratio 1.2, ID 40.25 in. **Propeller:** OD 40.0 in, 4,000 rpm, variable pitch forward/flat/reverse. **Blades:** five, NACA 65-006 tip / 65-012 root, chord 4.1 in, activity factor 160. **Stator:** six vanes, NACA 65412, chord 6 in. Sketch dimensions 23.117 in, 21.8 in, 24 in, 9 in and a 4 deg angle; their exact references are not labelled. Pitch change manual with hydraulic boost. This is the turbine propulsor. It was tested statically only and never flew (item 5). | F |
| 4 | **Ducted-propeller efficiency map** (memo Figure 7) | Fraser page 2, `images/Prop_Fig._7.jpg` | Online free | Cp against J with efficiency contours (peak island above 85% near J 0.9-1.1) and blade-angle lines at x = 0.7, no stator. Header: duct section 23015, five blades, prop diameter 40 in, TAF 800, blade no. 40160-4, duct length 2.75 ft. The page also lists Figures 2-6 and 8-12 (stator correction, actuator, Cp/J formulas). Of those I downloaded only Figures 1 and 7; the Figure 8 file came back corrupt from the Wayback Machine. | F |
| 5 | **Rohr internal memo by Mike Voytish, 8 May 1974, on the 71X propulsion unit** (propulsor design philosophy), quoted in full by Fraser | Fraser page 2: https://web.archive.org/web/20111010100515id_/http://www.fraseraerotechnologycompany.com/Rohr_2-175_Fan_Jet_page2.html | Online free | Design requirements for the propulsor: about 160 hp single-shaft turbine, sea level to 10,000 ft, 0-153 kt, "Maximum diameter of 40 inches to work in a duct mounted integral with the airplane.", 4,000 rpm, spinner 15 in max, 700 ft/s tip speed, efficiency targets of 60%+ at take-off (65 kt, SL), 70%+ in climb (90 kt, 5,000 ft) and 80%+ in cruise (152 kt, 10,000 ft). Rohr drawing numbers 189-4025 (propeller interface, 2 sheets) and propeller 189-4001 are named. Fraser adds the flight-article facts: "The 71X flew with one of the Lycoming piston engines and a 4- bladed wood propeller.", and the extension shaft had to be redesigned for vibration. | F |
| 6 | **Fraser, "Rohr 2-175 Fan Jet" web page 1** (history, photos, captions) | https://web.archive.org/web/20120526075225id_/http://fraseraerotechnologycompany.com/Rohr_2-175_Fan_Jet.html | Online free | Dates (taxi tests from September 1974; first flight 14 Oct 1974; "The second and final flight was on December 17, 1974 at Holtville, California."). Airframe history. Turbine and test-rig photos. Mooney's 1973 concept sketch (`Rohr_Jet_Mooney_Scetch.jpg`). Static-load (110%) and drop-test photos. Photo of the 1/2-scale 250 lb ski-test model. Drag chute. "The 20' span and 23' lengths are the correct dimensions." | F |
| 7 | **TWITT Newsletter No. 10, April 1987**: minutes (p. 2) and F. Marc de Piolenc, *The Rohr Two-175 (1974)* (pp. 5-7), written up from Walt Mooney's talk to TWITT on 21 March 1987, with test pilot Don Westergren covering the flight tests | https://rcsoaringdigest.com/TWITT/Apr87Ltr.pdf ; clean HTML copy by de Piolenc: https://web.archive.org/web/20060819181533id_/http://massflow.archivale.com:80/2_175.htm | Online free | **Who "Mooney" is:** Walter E. Mooney, the designer and project manager, not Al Mooney. Content: 20 ft span constraint, 150 hp at 4,400 rpm, four-blade propeller and six-blade stator, 1,280 fpm climb with one aboard, sparless wing with FRP piano-hinge fold joint, dog-tooth for pitch-up, symmetrical airfoil, cooling, flight-test notes, 23 h, the reason it died, destruction of the airframes. No 3-view or table of dimensions in this issue (all 12 pages checked). | F |
| 8 | **TWITT No. 144, June 1998**: Bob Fronius talk | https://rcsoaringdigest.com/TWITT/Jun98Ltr.pdf | Online free | Only a short mention: Fronius built the Two-175 with Mooney; folding wings, towable, 1-car garage. No numbers. | F (thin) |
| 9 | **US 3,931,943, "Airplane rudder and controls"**, Westergren and Mooney, assigned to Rohr Industries. Filed 30 Aug 1974, appl. 502,057, granted 13 Jan 1976 | USPTO full text and drawings PDF: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/3931943 ; https://patentimages.storage.googleapis.com/pdfs/US3931943.pdf | Online free | 6 claims, 6 figures, **no dimensions**. Claims cover the rudder-pedal mechanism: a pair of pivoted pedals, a two-plate bell crank with rollers, an adjustable connecting rod, pedals with a cellular core and thin skin, right-triangle section, and cushioning pads. The abstract: "In a small airplane, a combination nose wheel, shroud and rudder is provided." The shroud is self-centred by airloads, with an optional cable to a conventional rear rudder. Fig. 1 shows the nosewheel shroud-rudder profile and a swept fin outline. Fig. 5 is a flat pattern of the bell crank. Useful for the nose-rudder concept and cockpit control layout, not for aircraft geometry. | P |
| 10 | **SDASM Rohr Collection images tagged "Rohr 2-175 Aircraft"** (10 scans; NHPRC-funded digitisation) | https://www.flickr.com/photos/sdasmarchives/ : 54956563012 (26_0046733), 54956563017 (26_0046734), 54957449021 (26_0046123), 54957625108 (26_0046122), 54957635653 (26_0046735), 54957635678 (26_0046731), 54957635698 (26_0046730), 54957698339 (26_0046728), 54957760600 (26_0046732), 54957760635 (26_0046729). Description on each: "Piction ID--Rohr 2-175 Aircraft" | Online free (Flickr, SDASM terms) | All show N62R. **26_0046731:** underside in flight, nearly square-on: the best planform photo (delta, clipped tips, dog-tooth). **26_0046735:** head-on, on the ground, wings spread: the duct ring, fin on the duct, dorsal scoop, canopy, main-gear fairings in the wing, nose-gear fairing. **26_0046733:** rear three-quarter just off the runway: duct exit with hub and stator vanes visible, fin root on the duct. **26_0046734:** front three-quarter just off the runway: nose-wheel rudder fairing, gull-wing canopy, unsprung mains. **26_0046729, 26_0046730, 26_0046728, 26_0046123:** air-to-air left-side profiles (side elevation, dorsal inlet, duct). **26_0046122, 26_0046732:** distant air-to-air. No photo of the folding mechanism or of the cockpit interior in this set. | F (Rohr corporate photos) |
| 11 | SDASM Hall of Fame image "Chana 74_71X Triphibian, Chana was Deputy Program Manager" | https://www.flickr.com/photos/sdasmarchives/50345243348 | Online free | One more air-to-air left-side view of N62R. Confirms the "Triphibian" programme name. | F |
| 12 | **SDASM Rohr/Goodrich finding guide** (Debbie Seracini, 2013, 29 pp.) | https://sandiegoairandspace.org/assets/pdf/2052340741_pdf.pdf | Finding aid online. Material physical only, by appointment | **Box 46, item 3:** "One 3-ring binder titled SLIDE 71X and filled with 35mm slides in sleeves." This is the only 71X-specific entry in the guide. Searches for 2-175, Two-175, Mooney, Westergren, fan jet, Triphibian, Holtville and N62R found nothing else. Probably the source of the Flickr scans; not confirmed. | P (archive record) |
| 13 | SDASM: William F. Chana Personal Papers (3 boxes, donated 2008-09) | OAC finding aid: https://oac.cdlib.org/findaid/ark:/13030/c8f47x50 | Physical only. The box list did not load (OAC bot check) | The summary says Chana worked at Rohr as a deputy program manager. The box list may hold 71X material; not seen. Chana's autobiography *Over the Wing - The Bill Chana Story* (2003, private) covers the 71X, per Fraser, including Mott Taylor's fix for the extension shaft. Not located online. | P (record) / F (book, unseen) |
| 14 | Mooney's colour slides and 3-views (his personal collection in 1987) and Fraser's "Over 400 new 71X FanJet color slides in excellent condition has been discovered." (Fraser page, 2021 capture) | Fraser page: https://web.archive.org/web/20210511163818id_/https://www.fraseraerotechnologycompany.com/Rohr_2-175_Fan_Jet.html | Unknown, private | Unknown. Fraser wrote in 2012 that he and Westergren intended to give their material to SDASM. Whether they did is not visible in any catalogue I reached. | F (lead only) |
| 15 | *San Diego, air capital of the West* (1991), first-flight table | Internet Archive full text, item `sandiegoaircapit0000scot` | Lending library only | One line: date 10-14-74, Rohr 71X Triphibian, Don Westergren. Confirms the first-flight date. | L/P |
| 16 | aerofiles, Rohr entry | http://www.aerofiles.com/_ro.html | Online free | Span 30 ft 0 in, length 28 ft 0 in (taken from the early 3-view; see section 2), gross 1,450 lb, 150 hp at 4,400 rpm, four-blade fan, six-blade stator, registration N62R and one unnumbered "Nx". | L |
| 17 | Vintage Aviation News, "Grounded Dreams: The Rohr 2-175" (Feb 2026) | https://vintageaviationnews.com/warbird-articles/grounded-dreams/rohr-2-175.html | Online free | A retelling of TWITT. Gives first flight 14 Oct 1974. Photos credited to PAVE_naught/X and "Cancelled Aircraft"/Facebook, including one of the outer panels folded. No new numbers. | L |
| 18 | Michael VH (a former Rohr employee), Blender 3-D model | https://www.flickr.com/photos/michaelvh/14804744250 | Online free | An enthusiast's reconstruction. No data. | L |
| 19 | RC Groups thread *36" span Rohr 2-l75 ducted prop plan now with prototype history explained* (said to carry posts by Westergren and a team member on p. 3) | https://www.rcgroups.com/forums/showthread.php?958304 | Not read: behind a JavaScript challenge and a paid bot gateway (tollbit). Not archived on Wayback | Possibly first-hand recollections. Unverified. | L (unread) |
| 20 | Patent search beyond US 3,931,943 | Tried: Google Patents (blocked us, HTTP 503), Justia assignee list (403), FreePatentsOnline (403), web searches on Mooney, Westergren, Voytish, Borst, Ritenour and Rohr with folding wing, ducted propeller, pitch change. Only hit: Des. 248,033 (1978, Rohr), which turned out to be a **bus**. | — | **No other 2-175 patent found.** The variable-pitch "no stored energy" hub (item 5) is the likeliest unfound candidate. Not ruled out. | — |
| 21 | Jane's All the World's Aircraft, magazines, NTRS | NTRS API: 0 hits for `Rohr 71X`, `Rohr 2-175` and similar (positive control `ducted propeller` = 74). Internet Archive full text: 0 relevant hits for `Rohr 2-175`, `Rohr 71-X`; `Rohr 71X` gives only items 15 and the Ed Leiser chronology. IA holds Jane's AWA 1974-75 as a lending-only item (inside-text search refused), and no 1975-76 or 1976-77 edition. Few 1974-76 issues of Flying, Air Progress, Flight, Aviation Week, Popular Mechanics or Popular Science are on IA. The FlightGlobal PDF archive is offline. Google Books API quota was exhausted. | — | **Nothing found.** I found no evidence that Rohr ever announced the aircraft publicly at the time. Fraser's account (locked storage, then scrapping) suggests it may never have reached Jane's. A Jane's 1975-76 check on paper is still open. | — |

## 2. Published numbers

| Quantity | Value | Source | Grade | Note |
|---|---|---|---|---|
| Span (spread) | **20 ft** | Late 3-view (item 1). TWITT: "limited span to 20 feet" (massflow copy). Fraser: "The 20' span and 23' lengths are the correct dimensions." | F | |
| Span | 30 ft 0 in | Early Mooney 3-view (item 2); aerofiles | F / L | Fraser calls these labels errors. Our measurement of the late 3-view supports 20 ft. **Superseded.** |
| Length | **23 ft** | Late 3-view; Fraser | F | Scaled, it runs nose to fin tip (about 23.5 ft); nose to duct exit is about 18.7 ft (E). |
| Length | 28 ft 0 in | Early 3-view; aerofiles | F / L | Superseded, as above. |
| Height | not published | The early 3-view's 25 ft height label is clearly wrong | — | |
| Folded size | fits a standard FHA single-car garage; Fraser: "a standard 20' deep garage" | TWITT; Fraser p. 1 | F | Folded width not published. Scaled distance between the fold lines is about 6.8 ft (E). |
| Wing area | **180 sq ft** | Both 3-views (labelled basic wing, including control surfaces, on the early one) | F | Our polygon from the late 3-view gives about 188 sq ft, within 5% (E). |
| Vertical tail area | 16 sq ft (late) / 18 sq ft (early) | 3-views | F | |
| Elevon area | 22.8 sq ft | Both 3-views | F | Scaled check: about 22 sq ft (E). |
| Delta slat (exposed) | 3.4 sq ft | Early 3-view | F | Early configuration only. |
| Gross weight | **1,450 lb** | Both 3-views; aerofiles | F | |
| Empty weight, useful load, fuel | **not published anywhere found** | — | — | |
| Engine (flown) | Lycoming O-320X (3-view label) | Late 3-view | F | One of two experimental high-rpm Lycomings. A forum (orion, homebuiltairplanes 2007) says O-360 (L). |
| Power and rpm | 150 hp at 4,400 rpm | TWITT: "These gave 150 horsepower at 4400 rpm." (massflow copy) | F | Fraser p. 1 says the special cam ran it "at 4,000 rpm". Conflict; the 4,000 figure may come from the turbine propulsor spec. |
| Propeller (flown) | 4-blade, wood, ducted, with six-blade stator; short extension shaft | TWITT: "A short extension shaft drove a four bladed propeller." Fraser p. 2 | F | Diameter not published. Probably about 40 in to fit the same duct (E). |
| Propulsor (designed, static test only) | RP-17-V: 5 blades, 40.0 in, 4,000 rpm, variable pitch +40/-20 deg, NACA 65-006/65-012, chord 4.1 in, AF 160; stator 6 x NACA 65412, 6 in chord | Item 3; memo (item 5) | F | Designed for a Rohr single-shaft turbine (about 160 shp) that never met power or weight targets. |
| Duct | NACA 23015, length 2.75 ft, ID 40.25 in, area ratio 1.2 | Item 3 | F | Scaled from the 3-view: duct OD about 4.2 ft, length about 2.9 ft (E), consistent. |
| Tip speed | 700 ft/s design | Memo | F | 40 in at 4,000 rpm = 698 ft/s; at 4,400 rpm = 768 ft/s (E). |
| Climb | 1,280 fpm, one aboard | TWITT | F | |
| Design speeds (propulsor spec) | take-off 65 kt; climb 90 kt at 5,000 ft; cruise **152 kt at 10,000 ft**; airspeed range 0-153 kt | Memo | F | Design targets, not measurements. |
| Top speed | 175 mph, implied by the name | Fraser: "for two place with a top speed of 175 mph (not Kts)" | F (claim) | Never shown as measured. |
| Static thrust | not published | — | — | Fraser p. 1: "The aircraft ran away from it's Cessna chase plane on take-off." (anecdote) |
| Cooling | dorsal scoop plus exhaust ejector; no overheating at 108 deg F | TWITT | F | |
| Drag chute | cruciform, about 14 ft (Westergren's vague memory); about 1/2 g deceleration at over 50 mph | Fraser p. 2 | F | Spin-recovery chute. |
| Static test | 110% load test, inverted | Fraser p. 1 photo caption | F | |
| Wing structure | sparless foam-core FRP stressed skin; fold joint of two FRP piano hinges plus truncated-cone torsion bosses; symmetrical airfoil; outboard dog-tooth | TWITT | F | No layup schedule or airfoil coordinates survive publicly. |
| Wing loading | 8.1 lb/sq ft | 1,450 / 180 | E | |
| Aspect ratio | 2.2 | 20^2 / 180 | E | |
| Power loading | 9.7 lb/hp | 1,450 / 150 | E | |
| Planform, scaled from the late 3-view (±10%) | TE unswept; tip chord about 4.1 ft; LE sweep about 47 deg; root chord about 12.6 ft at the fuselage side (about 14.7 ft extrapolated to the centreline); fold line about 3.4 ft from the centreline; dog-tooth about 5.9 ft from the centreline (about 59% semispan); elevon chord about 1.7 ft | Item 1, our measurement | E | Scale from the labelled 20 ft span. Area and duct cross-checks agree within 5%. |
| Airframes | 3: Fraser lists a static test article, one completed flight article, and a third about half built (planned for the turbine). TWITT says two flying prototypes and a static article. | Fraser p. 1; TWITT | F | Conflict. Only N62R appears in any photo. |
| Flight time | "one prototype had accumulated 23 hours in the air" (TWITT) **against** two official flights, 14 Oct and 17 Dec 1974, plus many low taxi hops under 35 ft (Fraser, from Westergren) | massflow copy; Fraser p. 1 | F / F | **Unresolved conflict.** A forum claim of "well over 100" hours is L. |
| Fate | "all the airframes were cut up at night and taken to the Otay dump" (Fraser). Engines, props, instruments and wheels were salvaged. Westergren kept one wood propeller and the nose wheel (fairing cut off). | Fraser p. 1 | F | No airframe survives. The prop and nose wheel were Westergren's in 2012; current whereabouts unknown. |

## 3. The book

**Bibliographic details.**

| | |
|---|---|
| Title | *The Rohr 2-175 (71X) FanJet: A Tribute*. Fraser's own pages style it "The Rohr 2-175 (71-X) Fan Jet". |
| Authors | "By Richard W. Fraser with Don Westergren" (Aircraft Spruce, 2012) |
| Publisher | Fraser Aero Technology Company, 4442 E. Justice Circle, Orange, CA 92869 (self-published) |
| ISBN | **978-0-615-59079-0** (ISBN-10 0-615-59079-9; check digits verified). Printed on Fraser's order page (Wayback, 2019 capture). The 978-0-615 block is a self-publisher block. |
| Year | Not printed on any page seen. "Copyright © 2000 - 2014" on the order page; the earliest capture of the order page is Sept 2013; Aircraft Spruce listed it by March 2012. **First printing about 2012** (E). A "2nd Printing, Volume 1" was announced later. |
| Extent | "Color paperback 166 pages printed on 70 lb. deluxe paper" (Aircraft Spruce, 2012). A 2018 forum post says 164 pages. |
| Content (per seller and author) | Photos, drawings, construction methods, Westergren's flight-test commentary, people. A reader quoted on Fraser's page mentions the tail-cone shape needed to avoid a base-drag penalty behind the shrouded prop, dog-tooth pitch-up mitigation, and polycarbonate windshield forming. |
| OCLC | **Not found.** WorldCat could not be checked: HTTP 429, then Cloudflare error 1015, on every attempt. |

**Price history.** US$19.98 from Fraser plus 8% California tax and postage. His mail-order page also says "Please send $25.00 USA and $28.00 Canada." US$19.98 at Aircraft Spruce, part no. 13-11711.

**Current availability (2026-10-24).**

| Where | Result |
|---|---|
| Fraser Aero Technology Company site | Dead. The domain now serves an Indonesian gambling spam page. The last real captures (2019-2022) say "This book is now out of print." and "WE ARE CURRENTLY OUT OF STOCK FOR THIS INFORMATIVE BOOK. ANOTHER PRINTING SOON." The 2021 capture offers a possible expanded edition, after the slide find. |
| Aircraft Spruce (US) | The old product page `/catalog/bvpages/rohrfanjet.php` returns 404. The site search loads by script, so I could not read it. |
| Aircraft Spruce Europe | Part 13-11711 page: "This product is no longer available" (weight 0.307 kg). |
| Amazon.com | No listing. ISBN search: no results; `/dp/0615590799` returns 404; title and author searches show only unrelated books. |
| AbeBooks (.com, .co.uk) | ISBN search and keyword search (`rohr fan jet fraser`, `rohr fan jet`): no matching copies. |
| Open Library | ISBN 404; title searches 0. |
| Library of Congress | SRU catalogue queries (title words rohr+fanjet, rohr+tribute, `rohr 2-175`, `fan jet` with creator fraser): 0 records. Positive control lockheed+horizons: 3. |
| San Diego County Library (BiblioCommons API) | 0 for `rohr fanjet`, `rohr 2-175`, `rohr fan jet tribute`. Positive control: 1. |
| San Diego Public Library, SDSU, UCSD | Not reached. The BiblioCommons tenant did not answer, and the Primo catalogues need JavaScript. |
| SDASM library | No public book catalogue online. SDASM's research page lists only Flickr, OAC, YouTube and Internet Archive. Chana's papers (item 13) and the 71X slide binder (item 12) are archive holdings, not the book. |
| eBay, Biblio, Alibris, BookFinder, isbnsearch.org | Blocked automated access (HTTP 403 or 202, or browser checks). **Not checked.** |
| Lulu | Search page loads by script; nothing readable. |
| Forums | homebuiltairplanes (2017): "This book is out of print". aircraftpilots (Jan 2017): a buyer thought he had "found one in the UK". homebuiltairplanes (Nov 2018): a reader collecting names for a reprint at "US$19.98 + shipping". No outcome posted. |

**Conclusion:** out of print since at least 2019, no live retail listing found, and no library holding found in the catalogues I could query. The checks that remain need a person in a browser: WorldCat (title and ISBN), eBay, Biblio and AbeBooks want-lists. They are lookups only; buying a copy needs Bill's go-ahead under the no-purchase rule.

## 4. Gaps

1. **Measured performance and weights.** No empty weight, fuel capacity, cruise speed at a known power, stall speed or static thrust survives publicly. The book (if obtained) and the SDASM slide binder are the only remaining hopes. Possibly also the RC Groups thread (item 19).
2. **The flown propeller.** The 4-blade wood prop's diameter, pitch and blade section are not published. Westergren kept one in 2012.
3. **Engine identity.** O-320X (3-view label), 150 hp at 4,400 rpm (TWITT) or 4,000 rpm (Fraser), and O-360 (forum) are not reconciled.
4. **Flight hours.** TWITT's 23 h against Fraser's two official flights.
5. **Number of flying airframes.** TWITT says two; Fraser says one flew and one was half built.
6. **Airfoil and structure.** Only a "symmetrical french curve"; no coordinates or layup.
7. **Fold mechanism.** No public close-up photo or drawing. Vintage Aviation News reproduces a photo of the folded outer panels from a Facebook page; its origin is unknown.
8. **Not reached, worth a manual check:** WorldCat, eBay, Biblio, the SDPL/SDSU/UCSD catalogues, the Chana papers box list (OAC), Jane's AWA 1975-76 on paper, de Piolenc's *Contact!* magazine reprint, Google Patents for other Rohr 1974-77 filings, and the full Fraser Figure set (Figs 2, 4-6, 8-12 are on the Wayback Machine but were not downloaded; the Figure 8 copy was corrupt).
9. **Where Mooney's slides and 3-views went (d. 1990), and Fraser's 400-slide find.** Public catalogues show nothing. Any approach to the families or to Fraser is contact and needs Bill's go-ahead.

## Sources fetched

- TWITT No. 10 (Apr 1987) PDF: https://rcsoaringdigest.com/TWITT/Apr87Ltr.pdf ; TWITT No. 144 (Jun 1998): https://rcsoaringdigest.com/TWITT/Jun98Ltr.pdf
- de Piolenc, clean copy: https://web.archive.org/web/20060819181533id_/http://massflow.archivale.com:80/2_175.htm
- Fraser p. 1 (2012): https://web.archive.org/web/20120526075225id_/http://fraseraerotechnologycompany.com/Rohr_2-175_Fan_Jet.html
- Fraser p. 2 (2011): https://web.archive.org/web/20111010100515id_/http://www.fraseraerotechnologycompany.com/Rohr_2-175_Fan_Jet_page2.html
- Fraser p. 1 (2021): https://web.archive.org/web/20210511163818id_/https://www.fraseraerotechnologycompany.com/Rohr_2-175_Fan_Jet.html
- Fraser order page (2019): https://web.archive.org/web/20190409214009id_/http://fraseraerotechnologycompany.com:80/Rohr_2-175_71X_FanJet_Book_Review.html
- Aircraft Spruce (2012): https://web.archive.org/web/20120330030409id_/http://www.aircraftspruce.com:80/catalog/bvpages/rohrfanjet.php ; Aircraft Spruce EU: https://www.aircraftspruce.eu/the-rohr-2-175--71x--fanjet.htm
- US 3,931,943: https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/3931943
- SDASM Rohr/Goodrich finding guide: https://sandiegoairandspace.org/assets/pdf/2052340741_pdf.pdf ; Flickr items listed in row 10; Chana papers: https://oac.cdlib.org/findaid/ark:/13030/c8f47x50
- aerofiles: http://www.aerofiles.com/_ro.html ; Vintage Aviation News (row 17)
- Forums: https://homebuiltairplanes.com/threads/roho-2-175-71-x-fan-jet.26746/ ; https://homebuiltairplanes.com/threads/interest-in-reprints-of-rohr-2-175-fanjet-book-by-richard-fraser.30797/ ; https://www.aircraftpilots.com/forums/topic/28504-rohr-2-175-ducted-prop-aircraft/ ; https://homebuiltairplanes.com/threads/rohr-2-175.3024/
