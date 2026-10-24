<!-- Desk research by a delegated research agent for AER-3783 (2026-10-24), reviewed by AERO; quotes re-fetched against their sources before commit. Public sources only; nobody was contacted. -->

# Widening the net: commercial failures with an idea worth keeping

Date: 2026-10-24
Task: AER-3783 legacy design survey, AeroCommons (non-profit)
Mission targets: useful load >= 1,000 lb, range >= 1,000 nm, cruise > 160 KTAS (pref > 180) at altitude, 2/4/6 seats, engine baseline Aeromomentum AM20T (260 hp turbo) / AM15T (160 hp), liquid-cooled and auto-derived.

## Method

- Desk research using public web pages only (web search, page fetches, curl). No contact with anyone, no forms or sign-ups.
- FAA type certificate data sheets (TCDS) were pulled from FAA DRS (drs.faa.gov) as a guest session and read as text. The PDF URL pattern is `https://drs.faa.gov/api/content/alf/<document id>`. The document id is given with each citation.
- Every number carries a grade: F factory/brochure/designer, T TCDS, P flight test/POH/magazine pilot report, B builder/owner/registry, R measured record, E estimate (whose is stated). When a number came from Wikipedia, the grade reflects the type of original source Wikipedia cites, and the citation says (via Wikipedia). Those are secondary and should be upgraded before they carry weight.
- This file contains no verbatim quotations. All text is paraphrase. Where a number was not found in a fetched source, it says not found.
- Unit conversions done by us are graded E (AeroCommons conversion).
- Wikipedia pages are live pages fetched 2026-10-24. They may change.

## Summary table

| # | Design | Years | Built | Seats | Engine | Headline cruise | Useful load | Range | Idea worth keeping | Fit |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Mooney M20L PFM | 1988-89 | 41 | 4 | Porsche PFM 3200, 217 hp (T) | 161 kn max (via Wikipedia, grade F) | not found (gross 2,900 lb T) | not found | Auto-derived engine with single-lever electronic power control; the failure was about support and liability, not the airframe | High: closest precedent to AM20T |
| 2 | Toyota FV2400 + TAA-1 | 1991-2002 | engine certified; TAA-1: 1 | 4 (TAA-1) | Lexus V8 twin-turbo, 360 hp (F); TAA-1 used Lycoming | not found | not found | not found | Certified auto-derived V8 with dual-channel FADEC flew in a Cessna 340 testbed; a car maker gave up because of cost and market size | High: the AM20T risk case |
| 3 | Cessna 182 JT-A (and 172 TD) | 2007-2015 | 182 JT-A: not certified | 4 | SMA SR305, 227 hp diesel (F) | 156 kt max cruise (F) | 1,018 lb (F) | 1,025 nm at max cruise (F) | A 4-seat piston with 1,000 lb useful and 1,000 nm already existed on paper; it died on the engine supplier and certification timeline | High: numbers match our targets |
| 4 | Diamond DA50 SuperStar (2007) | 2007-09 | prototype(s), count not found | 5 | TCM TSIOF-550-J, 350 hp, FADEC (F) | 180 kt at 8,000 ft, 68% (F) | not found (MTOW 3,670 lb F) | not found | Airframe designed from the start to take gasoline, diesel or turboprop up to 350 hp; fixed gear at 180 kt | High: engine-agnostic airframe |
| 5 | Scaled Composites Catbird (Model 81) | 1988 | 1 | 5 | Lycoming TIO-360, 210 hp | 192.3 mph average on 8.9 gph over 400-mile CAFE course (R) | 976.63 lb payload carried in 1993 CAFE (R, via Wikipedia) | not found | Three-surface, flapless laminar composite single: speed and efficiency on 210 hp | Very high: aero benchmark for AM20T class |
| 6 | Commander 114TC | 1995-2002 | not found for 114TC; about 200 by Commander Aircraft 1992-2002 | 4 | Lycoming TIO-540-AG1A, 270 hp (T) | 187 kt at 75% (P) | 1,153 lb (P), but max zero fuel 3,000 lb (T) | 670 nm at 75%, 780 nm at 65% (P) | Roomy, strong, comfortable 4-seat with turbo; killed by capital and market, not by the design | Medium: cabin and turbo benchmark, fuel and ZFW lesson |
| 7 | Bellanca Aries T-250 | 1973-80 | 5 (incl. 1 test article) | 4-5 | Lycoming O-540, 250 hp | 170 kt (P) | 1,300 lb (P) | 900-1,000 mi with four (P) | Laminar wing on a simple, flat-panel all-metal airframe built for low cost | High: fits all targets except range on paper |
| 8 | Adam A500 | 2002-08 | 7 | 6 | 2 x TCM TSIO-550-E, 350 hp each (T) | 230 kt at 22,000 ft (F, 2003) | 2,100 lb planned (F); 160 lb with full fuel as built (via Wikipedia) | 892 nm at 75% (via Wikipedia) | Centerline push-pull thrust; and a warning on composite empty-weight growth | Medium: weight discipline lesson |
| 9 | AASI Jetcruzer 450/500 | 1989-2002 | 5 | 5-6 | PT6A-27 at 599 shp (T, 450) | 320 kt projected (F, 500) | 2,300 lb projected (F, 500) | 1,330-1,420 nm projected (F, 500) | Canard pusher certified with spin-resistance criteria | Medium: handling and safety idea, wrong size and engine |
| 10 | Wassmer WA-51/52/54 | 1966-77 | 154 | 4 | Lycoming 150-180 hp | WA-54: 260 km/h at 1,700 m (via Wikipedia, F) = 140 kt (E) | WA-54: 510 kg = 1,124 lb (E, from Wikipedia weights) | WA-54: 1,340 km = 724 nm (E) | First certified all-composite (glass-fibre) 4-seat production aircraft | Medium: composite certification precedent, low speed |
| 11 | Seawind 300C | 1982-2021 | about 80 kits, no certified aircraft | 4 | Lycoming 300 hp / TCM IO-550-N 310 hp | 166 kt max, 147 kt economy (F) | 1,100 lb (F) | 1,460 mi no reserve (F) | Composite amphibian that still carried 1,100 lb; failed on certification and funding | Low-medium: structure benchmark only |
| 12 | LearAvia Lear Fan 2100 | 1981-85 | 3 | 8 | 2 x PT6B-35F, 650 shp each, one pusher prop via combining gearbox | 322 mph at 40,000 ft (via Wikipedia, F) | 3,250 lb (E, from Wikipedia weights) | 1,783 mi (via Wikipedia, F) | Buried engines driving a pusher prop by shafts; composite pressurized fuselage | Low-medium: buried liquid-cooled engine layout precedent, wrong size |

## Per-design sections

### 1. Mooney M20L PFM (Porsche)

- Designer / maker: Mooney Aircraft Corporation with Porsche Flugmotoren (engine).
- Years: TC approved 25 Feb 1988 (T, TCDS 2A3 rev 58, section XI). Built 1988-89 (P, Plane and Pilot 2022).
- Number built: serials 26-0001 to 26-0041, i.e. 41 eligible serials (T); 41 built (P, Plane and Pilot 2022). Porsche itself says 40 Mooney PFMs and about 5 still airworthy (F, Porsche newsroom 2024).
- Seats: 4 (T).
- Engine: Porsche PFM 3200 N03, 2,343 rpm, 217 hp, 100LL (T). Air-cooled flat six with twin ignition, one lever for throttle, prop and mixture (F, Porsche newsroom).
- Weights and fuel: max weight 2,900 lb, 60.5 gal usable (T). Useful load: not found.
- Speeds: VNE 195 KIAS, VNO 174 KIAS (T). Max speed 161 kn (F, via Wikipedia). Cruise at stated altitude and power: not found in a fetched source.
- Fuel burn: 38 litres per hour (F, Porsche newsroom; conditions not stated).
- Why it failed: buyers judged it too heavy and short on power for Mooney expectations (P, Plane and Pilot 2022). Porsche limited its liability by capping engine availability, and the engines were later removed and returned (P, Plane and Pilot 2010). Mainstream buyers feared teething trouble with a new engine (P, Flying 2024). Factory support ended 2005 (via Wikipedia). Porsche says rivals played on fears about its electrically dependent ignition (F, Porsche newsroom). Category: market plus engine-supplier liability.
- Idea worth keeping: an auto-derived engine with integrated single-lever electronic control can be certified and fly well. The program then died because the engine maker would not stand behind it in the field. Long-term engine support and liability are design inputs, not afterthoughts.
- Its 20-inch fuselage stretch went on to become the base for the M20M/M20R (via Wikipedia; P, Plane and Pilot 2022).
- Relevance: the closest direct precedent for an AM20T installation. Plan for engine-maker exit and for the extra weight of a car engine.
- Sources:
  - TCDS 2A3 rev 58: https://drs.faa.gov/api/content/alf/08b1b046-b7f9-4212-9ea7-9a52a36b5c67
  - https://newsroom.porsche.com/it_CH/2024/history/porsche-aircraft-engine-pfm-mooney-35251.html
  - https://planeandpilotmag.com/scroll/muscle-plane-mooneys
  - https://www.planeandpilotmag.com/article/mooney-m20-pfm-mse-tls-eagle-encore-ovation-bravo/
  - https://flyingmag.com/aircraft/this-1988-mooney-m20l-pfm-is-a-formerly-porsche-powered-aircraftforsale-top-pick
  - https://en.wikipedia.org/wiki/Mooney_M20

### 2. Toyota FV2400-2TC engine and TAA-1 airframe

- Designer / maker: Toyota with Hamilton Standard (FADEC). Airframes by Scaled Composites: a 1991 V8 testbed, and the TAA-1 in 2002.
- Engine: FV2400-2TC, 4-litre twin-turbo V8 from the Lexus car engine, 360 hp, dual-channel FADEC, single lever, electronic injection and ignition, can run on auto fuel (F, FlightGlobal 1996).
  - Flight tested about 35 h on a Cessna 340 in place of the right-hand Continental (F, FlightGlobal 1996).
  - FAA type certificate Feb 1996, production certificate Jan 1997 (F, FlightGlobal 1997).
- TAA-1: 4 seats, carbon wing and fuselage, first flight 31 May 2002 at Mojave, 1 built, 180 hp Lycoming IO-360 (via airdatanews; via Wikipedia). Empty weight came in well over prediction, and performance was reportedly below expectation (via Wikipedia, rumour-grade; via airdatanews). Registration cancelled March 2011 (via airdatanews, B).
- Performance: cruise, useful load and range not found for either airframe.
- Why it failed: the engine was shelved during the 1990s GA downturn (via Wikipedia). A forum claim says certification-driven redundancy pushed cost up; it was seen only in a search snippet, not fetched, so we do not rely on it. TAA-1 was overweight and joint-venture talks faded (via Wikipedia). Category: market and cost; technical (weight) for TAA-1.
- Idea worth keeping: a liquid-cooled, auto-derived, FADEC-controlled V8 was certified and flown. Even a car maker with deep pockets found per-unit certification and the small GA market fatal. For AeroCommons, the lesson is to use an engine whose maker already sells in volume, and to keep certification effort per installation small.
- Relevance: a direct risk case for the AM20T/AM15T plan, covering FADEC redundancy, exhaust and cooling installation, and small volume.
- Sources:
  - https://www.flightglobal.com/toyota/hamilton-standard-examine-engine-potential/9677.article
  - https://www.flightglobal.com/toyota-is-cleared-to-produce-piston-aero-engine/738.article
  - https://en.wikipedia.org/wiki/Toyota_TAA-1
  - https://www.airdatanews.com/taa-1-the-toyotas-mysterious-airplane/

### 3. Cessna Turbo Skylane JT-A (182 diesel), with the Thielert 172 TD and Centurion 4.0

- Designer / maker: Cessna (Textron). Engine SMA (Safran) SR305.
- Years: prototype shown 2012; first production-conforming flight 22 May 2013 (F, Textron 2013). Orders halted, on hold indefinitely, May 2015 (P, AOPA 2015).
- Number built: not found. No SMA/JT-A entry found in TCDS 3A13 rev 76 (T, negative search of the current sheet).
- Seats: 4 (F).
- Engine: SMA SR305 turbo diesel, 227 hp (F, Textron 2013; AOPA 2015).
- Performance (factory estimates): max cruise 156 kt, 11 gph Jet-A at max cruise, ceiling 20,000 ft, range 1,025 nm at max cruise, 87 gal usable, useful load 1,018 lb (all F, Textron 2013).
- Price: 182 JT-A base price $530,000 against $470,000 for the gasoline 182T (P, AOPA 2015).
- Why it failed:
  - Certification ran long. Problems included a turbocharger failure with an off-airport landing, heated-induction requirements and a later turbo issue (P, AOPA 2015).
  - Cessna's earlier Thielert-powered 172 diesel was derailed by Thielert's bankruptcy (P, AOPA 2018). The later CD-155 Skyhawk JT-A was dropped less than a year after its 2017 certification (P, AOPA 2018).
  - Thielert's 350 hp Centurion 4.0 V8, derived from the Mercedes OM629 car engine, was frozen after the April 2008 insolvency (via Wikipedia).
  - Category: engine supplier and certification schedule, then price.
- Idea worth keeping: a 4-seat piston at 1,018 lb useful and 1,025 nm on 11 gph is essentially our useful-load and range target, set by a major OEM. The weak link was the new engine, not the airframe.
- Relevance: sets a concrete bar (156 kt, 1,018 lb, 1,025 nm). Our design must beat it on speed with similar power, and must not depend on one fragile engine supplier.
- Sources:
  - https://media.txtav.com/194784-cessna-turbo-skylane-jt-a-takes-first-production-flight
  - https://aopa.org/news-and-media/all-news/2015/may/14/cessna-not-accepting-182-jt-a-orders
  - https://aopa.org/news-and-media/all-news/2018/may/09/cessna-discontinues-turbo-skyhawk-jt-a
  - https://en.wikipedia.org/wiki/Thielert_Centurion
  - TCDS 3A13 rev 76: https://drs.faa.gov/api/content/alf/bbc174fa-726d-4385-bc4d-a451c6091132

### 4. Diamond DA50 SuperStar / Magnum (2007-2009 program)

- Designer / maker: Diamond Aircraft Industries, Wiener Neustadt.
- Years: SuperStar first flight 4 Apr 2007, eleven months from concept to flight (F, Diamond; AvWeb 2007). Magnum first flight 14 May 2008 with an Austro AE300 jet-fuel engine (F, Diamond). Shelved 2009 (F, Diamond).
- Number built: not found.
- Seats: 5 (F, AvWeb 2007).
- Engine: TCM TSIOF-550-J twin-turbo with FADEC, 350 hp. Diesels of 170-300 hp were to be optional (F, AvWeb 2007). The design aimed to take gasoline, turboprop or diesel engines up to 350 hp (via Wikipedia).
- Performance: 180 kt at 8,000 ft at 68% power, fixed gear, MTOW 3,670 lb (F, AvWeb 2007). Wikipedia lists the early MTOW as 3,527 lb, so the sources conflict. Useful load and range: not found.
- Why it failed: the economic crisis in 2009. Diamond moved its effort to the D-Jet (via Wikipedia) and then the DA62 (F, Diamond). The design returned as the DA50 RG with a CD-300 diesel: EASA certified 2020, FAA 2023 (F, Diamond). So the 2007 configuration failed but the line was later revived. Category: money and timing.
- Idea worth keeping: plan the airframe from day one for a family of engines in one power band. Also, a clean fixed-gear composite can reach about 180 kt on roughly 240 hp (E, AeroCommons: 68% x 350 hp).
- Relevance: supports designing one airframe for both AM15T and AM20T, and suggests fixed gear may be enough at 180 kt.
- Sources:
  - https://www.diamondaircraft.com/en/about-diamond/newsroom/diamonddiary/article/the-story-of-the-da50-rg/
  - https://avweb.com/news/another-diamond-in-the-sky/
  - https://en.wikipedia.org/wiki/Diamond_DA50

### 5. Scaled Composites Model 81 Catbird

- Designer / maker: Burt Rutan, Scaled Composites, while Scaled was owned by Beech. Intended as a Bonanza replacement concept (via Wikipedia).
- Years: first flight 14 Mar 1988; restored and reflown 7 Jul 2011 (via Wikipedia). Built: 1.
- Seats: 5. The pilot sits centred, with two forward-facing and two aft-facing passengers (P, Kitplanes 2012).
- Engine: Lycoming TIO-360-C1A6D, 210 hp (via Wikipedia). Kitplanes calls it a carbureted turbo TO-360, so the sources conflict.
- Performance:
  - 1988 CAFE 400: average 192.3 mph on an average 8.9 gph, including a mandatory climb to 7,000 ft MSL (R, Kitplanes 2012).
  - 1993 CAFE Challenge: 210.73 mph, 20.15 mpg, with 976.63 lb payload (R, via Wikipedia).
  - Cruise 218 kt; max 238 kt (F, via Wikipedia; conditions not stated).
  - FAI 2014: 334.44 km/h over a 5,000 km closed circuit (R, via Wikipedia; FAI page blocked to us).
  - Useful load, MTOW and range: not found.
- Airframe: three-surface (canard, wing and conventional tail), flapless, laminar Roncz airfoil (P, Kitplanes 2012; via Wikipedia).
- Why it failed: Beech's finances and competing projects prevented any production decision (via Wikipedia). Category: money and corporate priority. It was never offered for sale.
- Idea worth keeping: a 210 hp five-seater flying a timed course at about 192 mph on 8.9 gph shows what laminar flow, small wetted area and a flapless wing buy. It is the best published efficiency benchmark for our power class.
- Relevance: very high. It is an aero reference for a 160-260 hp, 4-5 seat composite at 180+ KTAS.
- Sources:
  - https://en.wikipedia.org/wiki/Scaled_Composites_Catbird
  - https://www.kitplanes.com/viewfinder-9/

### 6. Commander 114TC (Commander Aircraft Company)

- Designer / maker: Rockwell lineage (112 TC approved 1972). Commander Aircraft Co. built the 114B/TC family 1992-2002 (P, AvWeb).
- 114TC: TC approved 4 Aug 1995 (T, TCDS A12SO rev 23).
- Number built: about 200 four-seat singles of all models by Commander Aircraft 1992-2002 (P, AvWeb). 114TC-only count not found.
- Seats: 4 (T, P).
- Engine: Lycoming TIO-540-AG1A, 2,575 rpm, 270 hp (T). Plane and Pilot lists 200 hp, which conflicts with the TCDS; the TCDS governs.
- Weights and fuel: MTOW 3,305 lb, max zero fuel weight 3,000 lb, 88 gal usable (T).
- Performance:
  - Useful load 1,153 lb (P, Plane and Pilot spec box).
  - 187 kt at 75%, 169 kt at 65% (P).
  - Range 670 nm at 75%, 780 nm at 65% with reserve (P).
  - Ceiling 25,000 ft (P).
- Why it failed: the post-2001 slump and failure to raise capital. Chapter 11 was filed, then conversion to Chapter 7 was sought in Jan 2005; one investor defaulted on a $2.8 million deal (P, AvWeb). Category: money and market.
- Idea worth keeping: a wide, strong cabin with good crash protection, plus turbo-normalised altitude performance, gave a well-loved 4-seat. But the 3,000 lb MZFW and 88 gal limit range at high speed. Size fuel and MZFW together if 1,000 nm is a hard target.
- Relevance: a cabin-comfort benchmark, and a warning that useful load on paper is not payload with fuel.
- Sources:
  - TCDS A12SO rev 23: https://drs.faa.gov/api/content/alf/52054e8a-9965-4e10-88b5-db8b3a1d88d1
  - https://planeandpilotmag.com/article/commander-1996-114tc
  - https://avweb.com/briefs/commander-aircraft-to-be-liquidated/

### 7. Bellanca Aries T-250

- Designer / maker: Marvin Greenwood (Anderson-Greenwood), sold under the Bellanca name (via Wikipedia).
- Years: first flight 19 Jul 1973; type certificate 28 Jul 1976 (via Wikipedia). Production 1976-1980 (P, Plane and Pilot 2024).
- Number built: 5 (via Wikipedia). Plane and Pilot says 4 customer aircraft plus 1 structural test article (P).
- Seats: 4-5 (P).
- Engine: Lycoming O-540, 250 hp (P; via Wikipedia).
- Performance:
  - Cruise 170 kt (P, Plane and Pilot 2024). Wikipedia gives 200 mph at 65%, which is 174 kt (E, conversion).
  - Useful load 1,300 lb (P). Wikipedia gives MTOW 3,150 lb and empty 1,850 lb.
  - Fuel 80 gal (P); Wikipedia says 76 gal.
  - Range 900-1,000 miles with four aboard (P); Wikipedia says 1,170 mi with four.
  - Climb 1,200 fpm (P).
- TCDS: not located in FAA DRS by model search (gap).
- Why it failed: Bellanca went into receivership under the financial strain of its programs, notably the composite Skyrocket II (P, Plane and Pilot 2024). Category: money (parent company).
- Idea worth keeping: a laminar-flow wing on a deliberately flat-panel, low-curvature all-metal structure, designed for cheap production (via Wikipedia). It reached about 170 kt with 1,300 lb useful on 250 hp without composites.
- Relevance: high. On paper it nearly meets every target on 250 hp, close to the AM20T rating, with simple tooling.
- Sources:
  - https://planeandpilotmag.com/bellanca-aries-t-250/
  - https://en.wikipedia.org/wiki/Bellanca_Aries

### 8. Adam A500

- Designer / maker: derived from the M-309 CarbonAero demonstrator, designed by Burt Rutan and built by Scaled Composites. Developed by Adam Aircraft, Denver (via Wikipedia).
- Years: first flight 11 Jul 2002 (via Wikipedia); TC approved 11 May 2005 (T, TCDS A00009DE rev 10). Adam ceased operations Feb 2008 (via Wikipedia).
- Number built: 7 (via Wikipedia).
- Seats: 6 (T).
- Engines: 2 x TCM TSIO-550-E, 350 hp each, mounted front and rear for centerline thrust (T).
- Weights and fuel: MTOW 7,000 lb, max ZFW 6,500 lb, 230 gal total / 200 usable, and 180 usable on some serials (T).
- Performance:
  - 2003 projection: cruise 230 kt at 22,000 ft, 210 kt at 60%; empty 4,200 lb, gross 6,300 lb, useful 2,100 lb, 720 lb payload with full fuel (F, AOPA 2003 report on company figures).
  - As built: empty about 1,260 lb (30%) over projection, and 160 lb payload with full fuel (via Wikipedia, citing 2007 evaluation flights).
  - Range 892 nm at 75% (via Wikipedia).
- Why it failed: Adam Aircraft filed for Chapter 7 bankruptcy in February 2008 (via Wikipedia). Empty-weight growth is on the record (via Wikipedia); that it caused the failure is our inference, not the page's. Category: money, with a weight lesson.
- Idea worth keeping: centerline push-pull thrust removes asymmetric engine-out handling. The bigger lesson is weight: a composite airframe drawn by a top team still came in 30% heavy. Weight margins must be earned in detailed design.
- Relevance: a weight-growth warning for any composite 6-seat at 1,000 lb useful.
- Sources:
  - TCDS A00009DE rev 10: https://drs.faa.gov/api/content/alf/67068196-1336-4728-bb23-4e2229486138
  - https://www.aopa.org/news-and-media/all-news/2003/july/pilot/adam-a500
  - https://en.wikipedia.org/wiki/Adam_A500
  - https://www.flyingmag.com/pilot-reports-pistons-adam-a500/ (200-220 kt quoted range only)

### 9. AASI Jetcruzer 450 / 500

- Designer / maker: Advanced Aerodynamics and Structures Inc. (AASI). Design began 1983; first flight 11 Jan 1989 (via Wikipedia).
- Jetcruzer 450 TC: approved 14 Jun 1994 (T, TCDS A49NM rev 1). The TCDS lists Production Basis: None.
- Number built: 5 (via Wikipedia).
- Seats: TCDS 450 allows five occupants, with no baggage and 120 lb movable ballast required (T). The 500 was planned for six (via Wikipedia).
- Engine: 450 has a PT6A-27 limited to 599 shp (T). 500 has a PT6A-66A flat-rated to 850 shp (via Wikipedia; AOPA 1998).
- 450 limits: MTOW 4,300 lb, 60.5 gal usable (T). Wikipedia's 450 figures (310 kt cruise, 5,000 lb MTOW) conflict with the TCDS and are not used.
- 500 projections: 320 kt high-speed cruise, FL300, 1,330 nm at high speed or 1,420 nm at normal cruise, useful load 2,300 lb, about 700 lb payload with full fuel, stall 65-67 kt (F, AOPA 1998, company projections).
- Spin resistance: Wikipedia says the 450 was the first aircraft FAA-certified as spin-resistant, on 14 Jun 1994. The TCDS text we fetched does not mention spin resistance (gap). AOPA 1998 reports that attempted spins of the 500 produced only a gentle descent or shallow spiral (P).
- Why it failed: noise, high stall speed and CG problems were never solved, and work stopped in 2002 (via Wikipedia). Without flaps, the stall speed went above the Part 23 single-engine limit, which triggered 26 g seat requirements (P, AOPA 1998). Category: technical, then money.
- Idea worth keeping: canard pusher designed to the spin-resistance criteria. The trap is stall speed: a flapless canard can exceed the 61 kt single-engine stall limit and add certification cost.
- Relevance: a handling and safety concept to keep. Its stall-speed trap applies directly to any canard option we study.
- Sources:
  - TCDS A49NM rev 1: https://drs.faa.gov/api/content/alf/81b21b4b-1a13-4d2b-ab46-9dd7d1399e33
  - https://en.wikipedia.org/wiki/AASI_Jetcruzer
  - https://www.aopa.org/news-and-media/all-news/1998/april/pilot/turbine-pilot

### 10. Wassmer WA-50 series (WA-51 Pacific, WA-52 Europa, WA-54 Atlantic)

- Designer / maker: Société Wassmer, Issoire, France.
- Years: WA-50 prototype first flight 22 Mar 1966; production 1969-1977 (via Wikipedia).
- Number built: 154 in total: WA-51 39, WA-52 59, WA-54 55 (via Wikipedia).
- Seats: 4. Fixed tricycle gear on the production WA-51, WA-52 and WA-54; only the WA-50 prototype had retractable gear (via Wikipedia).
- Engines: Lycoming O-320 at 150 hp, IO-320 at 160 hp, or O-360 at 180 hp, depending on variant (via Wikipedia; flugzeuginfo).
- Performance:
  - WA-54: cruise 260 km/h at 1,700 m, range 1,340 km, empty 620 kg, gross 1,130 kg (via Wikipedia, citing Jane's, F).
  - Our conversions for the WA-54: about 140 kt, about 724 nm, useful load about 510 kg = 1,124 lb (E, AeroCommons arithmetic). The empty weight looks light and should be checked against a TCDS or Jane's.
  - WA-52: cruise 235 km/h, range 909 km, empty 630 kg, MTOW 1,060 kg (flugzeuginfo, F).
- Why it failed: working-capital problems while running two production lines. A receiver was appointed in 1977 and assets passed to Issoire Aviation in 1978 (via Wikipedia, Wassmer page). Category: money.
- Idea worth keeping: the earliest series-certified all-composite 4-seat, with 154 built and certified in the 1960s. Composite certification for a 4-seat single is old ground, not a research risk.
- Relevance: medium. It is a precedent for certification and production of a composite 4-seat. It is too slow to be an aero reference.
- Sources:
  - https://en.wikipedia.org/wiki/Wassmer_WA-51_Pacific
  - https://en.wikipedia.org/wiki/Wassmer
  - https://www.flugzeuginfo.net/acdata_php/acdata_wassmer_wa50_en.php

### 11. Seawind 3000 / 300C

- Designer / maker: designed late 1970s in Haliburton, Ontario. Later Seawind International, SNA Inc., then Seawind LLC (via Wikipedia).
- Years: first flight 23 Aug 1982 (via Wikipedia). Seawind LLC bankruptcy 8 Jul 2021 (via Wikipedia).
- Number built: about 80 kits plus 2 prototypes. No certified aircraft (via Wikipedia).
- Seats: 4 (via Wikipedia).
- Engine: Lycoming 300 hp (F, AvWeb 2003). 300C: TCM IO-550-N, 310 hp (via Wikipedia).
- Performance:
  - 300C as marketed in 2003: 166 kt max cruise, 147 kt economy at about 13 gph, useful load 1,100 lb, range 1,460 mi with no reserve, price $290,000 (F, AvWeb 2003).
  - Wikipedia gives 147 kt at 8,000 ft, 905 nm, empty 2,300 lb, gross 3,400 lb.
- Why it failed: certification dragged from 2007 to 2016 without a TC. Prototypes crashed in 2007 and 2014. There were funding shortfalls and Canadian tax-refund disputes, and owner Richard Silva died in 2019 (via Wikipedia). Category: certification cost and money.
- Idea worth keeping: a composite amphibian still offered about 1,100 lb useful at 3,400 lb gross, showing what composite structure allows at this size. The failure is a textbook case of certification scope outrunning funding.
- Relevance: low-medium. Use it as a structural-weight and program-risk reference only.
- Sources:
  - https://en.wikipedia.org/wiki/Seawind_International_Seawind
  - https://avweb.com/briefs/seawind-joins-soon-to-be-certified-set/

### 12. LearAvia Lear Fan 2100

- Designer / maker: Bill Lear (died 1978), LearAvia; production planned in Belfast (via Wikipedia).
- Years: first flight 1 Jan 1981; abandoned 1985 (via Wikipedia). Built: 3; two are in museums and the third is on static display at the FAA Civil Aerospace Medical Institute (via Wikipedia).
- Seats: 2 crew plus 6 passengers, pressurized (via Wikipedia).
- Engines: 2 x PT6B-35F at 650 shp each, driving one pusher propeller through a combining gearbox on separate shafts (via Wikipedia).
- Performance: cruise 322 mph at 40,000 ft, range 1,783 mi, empty 4,100 lb, gross 7,350 lb (via Wikipedia, F). Useful load is about 3,250 lb (E, AeroCommons arithmetic).
- Why it failed: the FAA would not accept the combining gearbox as reliable enough, and structural problems appeared when the composite fuselage was pressurized (via Wikipedia). Category: technical certification plus money.
- Idea worth keeping: buried engines driving a pusher propeller through shafts give a clean nose and a low-drag fuselage. A liquid-cooled engine makes burying easier than an air-cooled one. The shaft and gearbox are the certification risk; a single engine on a simple shaft avoids the combining gearbox.
- Relevance: low-medium. It is a layout precedent for a buried AM20T and shaft-driven pusher. The aircraft itself is far too large.
- Sources: https://en.wikipedia.org/wiki/LearAvia_Lear_Fan

## Considered and rejected

| Design | Reason |
|---|---|
| All 38 entries on the existing list (Cozy MKIV reference through SF.260) | Already on list. The Lancair IV-P's liquid-cooled TSIOL-550 option and NASA NLF tests on the P210/Skyrocket fall under existing entries. |
| Beechcraft Starship | Twin turboprop, 14,900 lb MTOW (via Wikipedia). Its lessons (composite weight growth of several thousand lb, about 53 built, fleet scrapped) are already covered by the Adam A500. Source: https://en.wikipedia.org/wiki/Beechcraft_Starship |
| OMAC Laser 300 | Single PT6A-135A turboprop (750 hp), metal canard pusher, 6-7 passengers, 3 built, first flight 11 Dec 1981. Abandoned because the money needed for certification and production (stated as $20 million) was never raised (via Wikipedia). Wrong size and engine class. Source: https://en.wikipedia.org/wiki/OMAC_Laser_300 |
| Grob Strato 2C | High-altitude research aircraft, 29,432 lb MTOW, 1 built. Its liquid-cooled TSIOL-550 with three-stage turbocharging set a piston altitude record of 18,552 m (R, via Wikipedia) and is a useful engine note. It is not a GA design. Source: https://en.wikipedia.org/wiki/Grob_Strato_2C |
| Gates-Piaggio GP-180 | Became the Piaggio P.180 Avanti, a commercial success and a twin turboprop. |
| Scaled ATTT | Military/technology demonstrator, not GA. |
| Bede BD-5 / BD-10 | Single seat / jet. |
| Beechcraft Model 73 Jet Mentor | Jet trainer. |
| Mooney Mite | Single seat. |
| Piper PA-48 Enforcer | Military close-support aircraft. |
| Cessna 177 Cardinal, Grumman AA-1, Helio Courier | Sold in volume (successes by our definition), or far below our speed target. |
| Taylor Coot, Pereira Osprey, Edgley Optica, Lockspeiser LDA, Trago Mills SAH-1, Freewing, Aerocar, Molt Taylor Imp, Dyke Delta | Below 160 kt, utility or roadable niche, or plans-built with no commercial venture. Little transferable to a 180 kt, 1,000 lb design. |
| Lancair Evolution, Kestrel K-350, Epic | Turboprop. Evolution is still in production; Epic is already on list. |
| Diamond DA42/DA40 Thielert | Commercial successes. The Thielert story is covered under section 3. |
| Rutan Voyager | Record aircraft, not a GA design. Its liquid-cooled rear engine is noted in the gaps below. |
| Vmax Probe | No public source found in the time available, so excluded rather than guessed. |
| Mooney M10, Cessna NGP, Beech 38P Lightning | Considered as diesel or pressurized-single precedents. Not researched to citation standard in this pass. |
| NASA AGATE / GAP (Teledyne GAP diesel, Williams FJX) | Programs, not aircraft designs. See gaps. |

## Gaps and follow-ups

1. Mooney M20L PFM: cruise at a stated altitude and power, and useful load, are not found in a fetched source. Need a POH or 1988 pilot report (AOPA Pilot and Flying archives).
2. Catbird: MTOW, empty weight, range and cruise conditions are not found. The FAI record page is behind a bot wall. Primary CAFE Foundation reports should replace the Wikipedia figures.
3. Toyota FV2400: installed weight, BSFC and the actual reasons for cancellation are missing. Only secondary sources were found.
4. Bellanca Aries T-250: TCDS not located in DRS. Need a TCDS number for gross weight, fuel and engine (to settle 76 vs 80 gal).
5. Jetcruzer 450: spin-resistance certification is claimed by Wikipedia but absent from the TCDS text. Check the FAA spin-resistance criteria history and AFM.
6. Wassmer WA-54: verify the 620 kg empty weight (fixed gear) against a DGAC or EASA TCDS or a Jane's scan.
7. Commander 114TC: production count for the 114TC alone is not found. The 200 hp figure in Plane and Pilot conflicts with the TCDS 270 hp.
8. Liquid-cooled precedents not yet sourced: TCM Voyager liquid-cooled engines (Rutan Voyager rear engine, TSIOL-550 in the Lancair IV-P option); Orenda OE600 V8; Teledyne GAP diesel under NASA GAP. These are engine-side follow-ups.
9. Laminar-flow evidence for the Bellanca Aries is only a Wikipedia mention. A NASA NTRS search for Aries or Anderson-Greenwood wing data would firm it up.
10. Most Wikipedia-sourced numbers (Lear Fan, Seawind 300C, Adam as-built weights, Wassmer) should be upgraded to primary sources (Jane's, TCDS, magazine reports) before anything here is used for sizing.
