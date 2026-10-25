# Citation audit: stratos.md (AER-3807)

Audited 2026-10-24. Every quoted string was re-fetched (python urllib with a browser UA, and curl), HTML stripped, whitespace normalised; PDFs read with pymupdf; OCR-damaged scans (Prandtl TN-182, Kroo) checked against the rendered page image. Nobody contacted, nothing posted. stratos.md was not edited.

**Result: no quote was NOT FOUND.** All 158 quoted strings match their source verbatim, allowing for encoding, ligature, hyphenation and OCR damage. The ellipses (HIST x2, TM-101083, IDINTOS "maiden flight ... on July 2014") drop nothing that changes the meaning. The problems are below.

## UNSUPPORTED

1. **JW-1 "Never built or flown" (D2 table).** This is cited to TM-101083 and AIAA 87-2930 (NTRS 19880029248). Neither source says it. The 87-2930 abstract says the flight demonstrator "has been developed" and describes only the design and a wind-tunnel model. TM-101083 speaks only of the 1/6-scale model. The claim may be true, but it needs a source that actually states it.
2. **A3 Engine row: "NODSPEC/AEROP/HIST say a 3-cyl König of 24 hp".** HIST gives only "(24hp to 28hp)" for the S1-to-S2 change and names no cylinder count. Only NODSPEC and AEROP say 3-cylinder.
3. **A3 Undercarriage: "small balancer wheels at the foreplane tips (BANKA)".** BANKA says "two balancer wheels at wing tips". The foreplane/canard tips detail comes from AEROP ("small outrigger wheels on the canard tips") and the Reese front view, not from BANKA.

## PARTIAL

4. **A4 Stall: "58 km/h / 36 mph 'power on' (AEROP, WIKI)".** The Wikipedia spec block gives `stall speed kmh=58` with no qualifier and no mph figure. Both "power on" and "36 mph" come from AEROP only.
5. **Kroo p. 338 "Fuel volume, landing gear integration, CLmax penalties ... disadvantages for this concept."** The quote is verbatim, but "this concept" is the Lockheed transonic box-plane transport on that page. Kroo is not stating the costs of box or joined wings in general. The file lists it under general costs without saying which concept it refers to.
6. **A4 Fuel economy note: "A 2009 forum post quotes '80+ mpg' (homebuiltairplanes posts/74109)".** The phrase is in post #1, by Bart, 7 Mar 2009. Post 74109 is etterre's reply (#2). The URL resolves to the thread, so this is minor. "~300 feet" is also in Bart's post #1.

## UNVERIFIABLE (cited URL), content verified another way

7. **ATSB live URLs** (`/sites/default/files/investigation-reports/aair198701462.pdf`, `aair198801418.pdf`, and the `/investigations/` pages) could not be fetched from here. python urllib timed out at 25 s; curl over HTTP/2 failed with INTERNAL_ERROR; curl over HTTP/1.1 got 0 bytes in 90 s; each was tried twice. I checked the same reports from Wayback copies instead:
   - `media/34032/aair198701462.pdf`, captured 2011-03-17
   - `media/27928/aair198801418.pdf`, captured 2014-02-14
   - the 198701462 landing page, captured 2023-06-07
   - the 198801418 .aspx page, captured 2012-03-17

   Every ATSB quote and field in the file matches: dates, places, times, "Not Registered", "Sport Aviation (Test Flight)", release dates 17 Jun 1988 and 21 Feb 1989, "full canard stall followed by a rapid nose down pitch", "no adverse flying characteristics", "unforeseen circumstances beyond his capabilities", both significant-factor lists, "almost neutral", "a lack of elevator response", and Factor 5. Manufacturer "Ligeti Aero-Nautical Pty Ltd" and "Loss of control" are on the 2023 landing page, not in the PDF. The 198801418 landing page gives Manufacturer "Unknown". The 404 on the old `media/34032` URL is confirmed (Wayback CDX, 2025-11-22).

## Unreachable source the author recorded, retried

8. **Part C "Wayback Machine was Temporarily Offline".** It answered after retries.
   - **Captures exist** for ligetistratos.com (2006-2013), ligeti-stratos.com (2006-2021) and lgtaerospace.com (2008-2016).
   - **No licence is named** on any page checked. I checked the home pages of ligetistratos.com (2006/07/08/11) and ligeti-stratos.com (2007/08/11/12/13), plus project-objectives, project-current-status, faq, about and articles-policy. The licence "not found" finding therefore stands.
   - **The 2009 forum post copies the project site,** as the file guessed. Tony2's wording ("Through the generosity ... first of a complete line of Open Source aircraft", "112 kts on 1.3 gph") was already on ligetistratos.com by the 2007-11-17 capture.
   - **Objectives page (2012-06-27):** "Distribute the plans gratis; at no charge." This is a statement of intent, not a licence.
   - **Not in the file, and it bears on Part C:** an LGT Aerospace "Stratos Project" PDF by Ron Ligeti (© LGT Aerospace), Wayback 20140826172206, `lgtaerospace.com/attachments/article/15/Stratos%20Project.pdf`, says: "The design owner retains the IP, the manufacturer is supplied with CAD engineering ..." It also says the prototype "is aimed to induce a licensing arrangement for production". This is primary support for the file's inference that the family kept control, and it contradicts the open-source framing after 2010. The same PDF says "The only original successful Stratos aircraft is currently in Storage, where it has been for 20 years", which bears on the S1-at-Holbrook question.
9. **Missed evidence in a source the file already cites (A2 survivors).** In aircraftpilots topic 6308, paddo2002 writes on 25 Dec 2010: "I am aware that the S1 is at Holbrook". This is hearsay, but it belongs next to "Which airframe is at Holbrook ... is unresolved", together with the LGT "in Storage" line above.

## Items read from images by eye (requested check): all confirmed

- Prandtl TN-182: the "least induced drag ..." quote (p. 17), eq. (13), and the Table III best-wing-system and biplane rows (0.865/0.787/0.728/0.678/0.637/0.601; 0.890/0.827/0.779/0.742/0.710/0.684) all match the page images. The 1/κ arithmetic and the G/b = 0.11 interpolation (κ ≈ 0.775, e ≈ 1.29) are correct.
- Kroo p. 346 figure: box 1.46, C-wing 1.45, biplane 1.36, diamond 1.05, V 1.03. All confirmed.
- Reese 3-view (stratos3viewweb.jpg): "Created 8-30-03", "by Marv Reese", 98.000 / 39.000 / 22.000 / 205.000 / 211.000 / 28.500 and "3 deg dihedral each side" are all on the image. My own scaling agrees with the file's estimates: LE sweep about 30°, TE about 28°, foreplane root chord about 28 in, gap about 25 in.

## Spot-checked and fine (no action)

- Stratos figures, with the sources the file gives:
  - span 5.36 m (BANKA, WIKI, NODSPEC)
  - area 7.53 m² (BANKA, WIKI) / 7.52 m² (NODSPEC, AEROP)
  - empty 78 kg and gross 188 kg (all four sources; WIKI's 188 is the `max takeoff weight` field)
  - cruise 180 km/h (AEROP, NODSPEC; BANKA also gives it)
  - glide 20:1 (WIKI, NODSPEC)
  - climb, ceiling, range, Vne, g limits, wing loading 24.95
- TM-101083: CLmax 1.20 at 6°, 30° sweep, stall about 12°, Figure 18 lateral-stability text, vortilons, static margin 0.30 to 0.36.
- IDINTOS: all Table 1 values, "mostly obtained from wind tunnel results", 1/4-scale Politecnico tests, 6-10% drag reduction, CL plateau 15-24°, 12.5% drop with full flap, front-wing-first stall, counter-rotating elevators, propeller shrouds, RC model maiden flight July 2014.
- Wolkovitch, Gallman/Smith/Kroo, Gallman/Kroo and Miura abstracts (NTRS API).
- Synergy, Sunny and FlyNano Wikipedia numbers.
- Live domain states (HugeDomains, timeout, gambling spam).

**Items checked: 158 quoted strings, about 45 numeric or attribution claims, 3 image-read item groups, and 1 author-recorded unreachable source (retried). Total about 207. Problems: 3 UNSUPPORTED, 3 PARTIAL, 1 UNVERIFIABLE (live URL only; content verified), 2 additions from the Wayback retry. NOT FOUND: 0.**

## Resolution (AERO, 2026-10-24)

All three unsupported and three partial items were corrected in `stratos.md`, and each corrected cell says so. The Wayback findings (no licence named; the 2012 statement of intent; the 2014 LGT Aerospace PDF; the 2010 Holbrook post) were added to its gaps list. AERO re-fetched the LGT PDF independently (SHA-256 35180b157e4a8f912e839b3a612d7dd6e3544227fd5b9f3e64d89a44fce728b0) and confirmed its three quoted lines word for word. `planform.md` no longer calls the JW-1 "never flown", and its open-source paragraph now carries the LGT PDF.
