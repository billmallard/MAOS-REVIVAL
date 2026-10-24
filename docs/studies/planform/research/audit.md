# AER-3807 citation audit: calibration.md and safety.md

Audited 2026-10-24. I re-fetched every cited source myself: python urllib with a browser User-Agent, HTML stripped, whitespace normalised. PDFs were read with pymupdf, and OCR damage in the scanned NACA reports was checked by hand. Aviation-safety.net returns 403 to urllib, so I fetched it with curl. The Fraser Wayback page returned 429 to urllib, so I fetched it with curl using the `id_` URL form. Wikipedia claims were checked against the live page and its raw wikitext. I contacted nobody.

This file lists problems only. Anything not listed was checked and found to match its source.

## NOT FOUND

None. Every quoted string was found in its cited source. Some matches needed OCR tolerance: RM L7K07 ("11f~", "co~ld", "nndels"), TP-1589 (a line-break hyphen in "resis-tance") and TM-85910 ("greater-than- predicted").

## PARTIAL (paraphrase, attribution, or a truncation that shifts meaning)

1. **safety.md 2.8: the Verhees canard quote "takeoff speed is higher than stall speed, compromising runway performance."** The file says "The D2 designer says that..." In the Kitplanes article this sentence is Phelps's paraphrase. It comes right after a short Verhees quote ("every advantage has its disadvantages," he wrote) and is not inside quote marks in the source. It should be attributed to the article, not quoted as the designer's words.
2. **safety.md 1.2: the RM L7K07 quote "unsatisfactory because of unstable rolling oscillations at high lift coefficients" (wing rock).** The source sentence goes on: "...or because of excessive changes in static longitudinal stability over the lift range." The cut leaves wing rock as the only failure mode. The report's conclusions say model 3 (53 deg sweep, AR 1) failed on longitudinal stability, not roll, and models 6-9 had both problems. The file's "(76/83 deg)" parenthetical also leaves out models 3 and 5, which fall in the AR ≤ 1 group. This is minor, but the quote overstates how uniform the wing-rock finding is.

## UNSUPPORTED (the source does not support the claim as written)

3. **safety.md 1.10: NASA TP-2644 is described as "a low-wing 4-place T-tail research airplane".** The TP-2644 PDF says: "The test airplane was a two-place, single-engine, low-wing, fixed-gear design". It flew four interchangeable tails, and the baseline (tail 4) had a "low, aft-mounted horizontal tail". The four-place T-tail airplane is the TP-2691 airplane (item 1.12). The two airframes have been conflated. The quote "tended to roll-off at the stall" is correct (it is in the NTRS abstract).
4. **safety.md 1.12: TP-2691 airplane called "Piper-derived".** The TP-2691 text says only "four-place, low-wing, single-engine, retractable-gear, T-tail ... one-of-a-kind research airplane". The word "Piper" does not appear anywhere in the report.
5. **safety.md 1.15: Wikipedia "Leading-edge cuff" given as the source for the cuff coming from NASA Langley work and the FAA accepting CAPS in place of full spin testing.** The live article (raw wikitext checked) says only that the Cirrus SR20 and Columbia 350 "gained FAA-certification with the device". There is nothing on CAPS, parachutes, or spin testing being waived. The file does flag this as unverified, but the claim is not on the cited page at all and should be dropped.
6. **safety.md 5.4: "Light, low-wing-loading aircraft ride worse", sourced to Stewart, NASA TP-2913.** TP-2913 is a ride-quality-meter study of one light twin with a maximum wing loading of 32.2 lb/ft² (AR 8.1). That is not low wing loading. The report notes only that GA airplanes "have a reputation for poor ride quality" and contains no wing-loading comparison. The "much worse" subjective finding is supported. The wing-loading framing is not.
7. **calibration.md A1 (Dyke stall row): "70-75 mph; approach 100-110 mph [WP-DD citing A&S]".** On the live Wikipedia page, only the 70-75 mph stall and "nose-high" sentence cite Air & Space. "Approach speeds of 100–110 mph are used" cites Sparky Barnes, "A Dyke Delta Reborn", *Sport Aviation*, Dec 2008. My fetch of A&S also does not contain the 70-75 figure, as the file already notes.
8. **calibration.md A1 (Dyke seats): "WP says 3".** The live infobox has crew "One pilot" plus capacity "3: 2 passengers, with a small third passenger in the center bench seat position". That is four occupants, matching A&S, so there is no conflict. The file misreads the capacity field.
9. **calibration.md source key HBA-Rohr: "Poster 'orion' recalls the Rohr from his time at General Dynamics".** What orion actually says is that he worked at General Dynamics, where he met Walt Mooney, and "As I have the story..." His Rohr details (O-360, "well over 100 flight hours", pre-1973) are second-hand, not his own recollection. That makes the HBA-Rohr side of the engine and flight-hours conflicts weaker than grade B suggests.

## Minor locator issues (the claims themselves are supported)

- safety.md 2.7: TM-85910's "approximately 19°" is on PDF p.8 and "greater-than-predicted value of low-speed L/D" is on PDF p.11 of the NTRS PDF, not p.6-7.
- safety.md section 4 (SR22): the figure "Maximum Glide Ratio ~ 8.8 : 1" is confirmed on PDF p.9 of the FAASTeam PDF. The "POH Sec. 3 p.3-18" folio does not appear in that reproduction, so it cannot be checked from the cited source.

## UNVERIFIABLE

None. Every cited URL that I needed was reachable, either directly or by the workarounds above. Sources the files themselves mark as "not read" or "not verified" (TN-1468, RM L8L29, the Mooney forum, the Flying article, the ASI primary PDF) were not counted as problems, except item 5.

## Spot-checks requested by the caller: all confirmed

- 1000aircraftphotos 6802: Prescott Pusher span 29 ft 4 in, wing area 110.8 sq ft, AR 7.76, gross 2,400 lb (plus 2,250 original TOGW, Sindberg's 2,600/2,800 lb, 200 mph CAS).
- Dyke JD-2: 22 ft 3 in, 173 sq ft and 1,980 lb (Wikipedia); 1,950 lb (PAV table, Pilotfriend, Kitplanes).
- PAV report: Facetmobile 15 ft, 214 sq ft, 370/740 lb, AR 1.05 in the table and 1.07 in the text.
- de Piolenc (Wayback) "which limited span to 20 feet". The TWITT 1987 OCR reads "dlctated a 20' span".
- TP-2691: 173 of 209 spins (83%, quoted from ref. 12) and 13 of 244 (5%).
- AOPA quote "25 percent ... approximately 5 percent" is verbatim.
- SR22 "~ 8.8 : 1" is in the FAASTeam PDF.
- Wainfan "just sufficient" sentence is verbatim (PAV p.21). The C150 has the higher L/D at all airspeeds.
- Kitplanes 14 May 2020: "a lot of standard T-hangars are 38 feet wide" and "beyond about 37 feet". The Kohlman J. Aircraft 16(4) 1979 citation is confirmed.
- Wikipedia-sourced figures for the Prescott, Dyke, Facetmobile, V-173, Arup S-2 and S-4, Hatfield LB-1, Verhees D-Plane 1, BlackFly, Stemme S10, Grob G 109 and Long-EZ (rain-trim quote) are all still on the live pages, apart from items 5, 7 and 8 above.

## Count

- **Quoted strings checked:** 80 distinct strings, across 37 source documents.
- **Factual and numeric claims spot-checked against their sources:** about 60, including all of the caller's priority items and every derived AR(d) value.
- **Sources fetched:** 50 URLs, plus raw wikitext for 13 Wikipedia pages and 18 NTRS metadata records.
- **Problems found:** 0 NOT FOUND, 2 PARTIAL, 7 UNSUPPORTED, 0 UNVERIFIABLE, plus 2 minor locator notes.

## Resolution (AERO, 2026-10-24)

All nine items were corrected in `calibration.md` and `safety.md` the same day. Each corrected cell says so. The two page references were also corrected. Three of the items had reached the study text, and `planform.md` was corrected to match: the TP-2644 airplane is two-place; the Dyke approach speed cites Sport Aviation; and the AR 1 delta models failed on wing rock or on longitudinal stability.
