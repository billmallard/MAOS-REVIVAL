"""Stage 3 revision 2 (AER-3783, after Bill's review of 2026-10-24).

Imported by narrative.py after its first-pass entries: it updates the designs
Bill kept, adds the two he asked for (Bellanca T-250 Aries, Meyers 200D) and
re-ranks. Bill's calls are quoted from his review comment on AER-3783.
"""

EXPRESS_STUDY = """
**What the record shows** (sources and the full accident table: `docs/shortlist/check/express/README.md`):

- **Grand Prairie, the accident Bill knew: NTSB CEN21LA096.** Express CT N772BM, 21 December 2020, two killed. It departed runway 17 at Grand Prairie Municipal, and the pilot asked for and was given a right turn. The tower then told him to keep the turn tight to stay out of Arlington's airspace. The NTSB track shows a continuous climbing right turn. A witness saw the bank steepen into a steep dive, with power coming up after the dive began. Probable cause: "The pilot's loss of airplane control during the departure turn, which resulted in an aerodynamic stall and impact with terrain." No mechanical anomaly. The NTSB does not state the tail type; "CT" is the cruciform-tail designation in the kit makers' and Jane's usage (P; tail type E).
- **CEN15FA321 (Holland MN, 2015, three killed)** ended in a high-pitch, steep right turn with airspeed decaying to 48 kt, then an upright right spin (Chelton EFIS data, NTSB docket). The NTSB named "the airplane's design, which resulted in poor yaw stability at low airspeed" as contributing. It did no testing of its own: the finding rests on the 1997 CAFE Foundation flight test (P).
- **CAFE 1997, N360EZ (cruciform tail, 210 hp), measured:** yaw doublets overshot "4-5 times" before settling (low directional damping); after 1 g clean stalls an "uncommanded right yaw with inadequate elevator control" until 85 kt; at 26 deg the rudder "seemed to set up a partial stall of the vertical fin"; the horizontal tail was blanked by the fin at high sideslip, so the elevator ran out and the nose pitched down. With 20 deg rudder stops the same traits appeared to a lesser degree (P).
- **Express Design Inc., February 1995**, told every owner of the cruciform-tail Express CT that rudder could produce an unexpected pitch-down, confirmed by outside consultants, and recommended the larger Series 90 tail (F).
- **The accident record** (our count from CAROL, ASN and foreign reports): 18 fatal Express-family accidents and 30 deaths, 1990-2025, on about 100 aircraft ever registered (about 55 active); 19 and 32 if a "Terrair Express" of unconfirmed lineage is included. This replaces the first pass's 13 and 21, which missed six. Of 17 stall or loss-of-control events in flight, the turn is recorded as **right in 9**, left in 3, conflicting in 1, and not recorded in 4. Three of the nine right-turn events followed an engine failure and two were turns ATC or the pattern required, so the record alone does not prove a right-hand bias. Both tail families appear among the stall events.

**Why climbing right turns, an inference from the physics and the data, not a finding.** At high power and low speed, P-factor, slipstream swirl and torque all yaw a clockwise-turning (as seen from the cockpit) tractor to the left, so the pilot climbs holding right rudder. In a climbing left turn those tendencies already supply the yaw, and the right rudder the pilot is holding works against a skid. In a climbing right turn, a pilot who tightens the turn with more right rudder, and holds the bank back with left aileron, is cross-controlled in a skid: the inside (right) wing flies at the higher angle of attack, its down-going aileron raises it further, and it stalls first, so the airplane rolls and spins to the right. An airframe with weak directional stability lets that skid grow further for the same rudder and is slow to straighten, and the Express adds three things to it:

1. **A fin too small for the fuselage in front of it.** The fuselage is wide and tapering, which is destabilising in yaw (CAFE names it). On our estimate the fuselage alone gives Cn_beta of about -0.0013 per degree. A fin under about 15 ft2 at a 14 ft arm leaves the total near neutral; a normal light-single margin (about +0.0010 to +0.0015 per degree) needs about 20-24 ft2 (table below). No Express fin dimensions are published, so the current fin is placed by inference from CAFE's measured behaviour, not by measurement.
2. **More power than the tail was proven with.** CAFE flew 210 hp. The Grand Prairie and Holland aircraft had 250 and 260 hp, and later builds ran 300 hp and IO-550s. The left-turning tendencies, and the rudder the pilot needs against them, grow roughly with power at climb speed. An AM20T (260 hp, 300 hp for five minutes) sits in the same band, so a revival must size the tail for it.
3. **Stall speeds higher than the book.** CAFE measured 67 KCAS clean and 58 KCAS full flap at 2,865 lb. The kit makers published Vs1 55-58 kt. At 3,200 lb in a 45 deg bank the clean stall is 84 KCAS on CAFE's basis, against 69-73 kt on the published one (table below). A pilot flying a tight departure turn by the book is closer to the stall than the book says. One previous owner told the NTSB he never saw the published 55 kt and flew his own 85/70 kt.

**What fixes it, and what each fix costs** (cruise cost from the stage 3 model at 195 hp and 8,000 ft; mass E):

| Fix | What it does | Cruise cost | Mass and other cost |
|---|---|---|---|
| Fin to about 20-24 ft2, sized at 260-300 hp | Restores a normal directional-stability margin and rudder power | 2.0-2.9 kt | About +8-12 lb aft (E), which needs about the same again in nose ballast unless the tail surfaces get lighter |
| Dorsal fin, about 3 ft2 | Delays the fin stall CAFE saw at high sideslip | 0.7 kt | A few lb; no tooling for the main surfaces |
| Ventral fin, about 3 ft2 | Adds yaw stiffness below the horizontal tail's wake | 0.8 kt | A few lb; ground clearance in the flare has to be checked |
| Horizontal tail out of the fin's wake, at S-90 size (31 ft2, low) | Ends the fin blanking the elevator; EDI's consultant computed the forward-CG range growing from 11.2 in to 20 in | about 3 kt (40% more tail wetted area); 4.3 kt with dorsal and ventral | New tail tooling; it is what the kit makers themselves offered |
| Stall strips at the inboard leading edge | Makes the untwisted laminar wing stall root-first, with buffet, instead of dropping a wing | negligible (E) | 1-2 kt higher stall speed (E); must be set in flight test |
| Leading-edge cuff outboard | Delays the tip stall | 2-4 kt on a laminar wing (E): the cuff trips laminar flow | Not recommended ahead of the tail fixes |
| Stiff rudder circuit, 20 deg stops | Owners found cable stretch and a small horn cut real rudder travel to a few degrees; CAFE recommended 20 deg | none | Build quality and inspection, no drag |
| Consistent rigging | Stab incidence varied from 0 to -0.8 deg and more across eras; owners re-shim | none | A jig and a check, not a redesign |
| Lighter tail surfaces | Owners weighed 81 lb of rudder and elevators and carry 56-62 lb of nose ballast; one built aluminium surfaces 33 lb lighter | none | Saves weight twice: the surfaces and the ballast |
| Honest V-speeds, a fixed static system, an AOA indicator with aural warning | Lets the pilot see the real margin in a turn | none | A few lb; a flight-test programme to publish real numbers |

A revival on this airframe would re-derive the tail and fly a stall and departure-resistance programme before any kit was sold. Whether a given fix gives acceptable spin or departure behaviour can only be shown in flight test; nothing here claims it.
"""

EXPRESS_MARKET = """
Bill: "I never understood why this didn't do better in the market." On the record, the airplane was liked and the business never delivered it. In order of weight (sources in `docs/shortlist/check/express/README.md`):

1. **It lost its demonstrator before there was a fleet.** AOPA Pilot's August 1990 pilot report says there were "no customer airplanes yet flying". On 25 July 1990 the second factory demonstrator spun in on its way to Oshkosh, killing three (NTSB; CAFE and Kitplanes say four). With no customer aircraft to point to, CAFE says the crash "led to a severe contraction in sales eventually prompting Ken Wheeler to enter bankruptcy" (P).
2. **The kits were not complete, so the fleet never grew.** Kits were incomplete at the Wheeler bankruptcy and the plans were incomplete; one builder "actually created much of the documentation used by subsequent builders" (CAFE). The kit makers claimed 1,000-2,000 build hours; CAFE's builder took 5,000. About 30 of about 300 kits were finished by 1997 (P). A builder put it plainly: "nothing sells kits like kits completed and on the flight line" (B).
3. **Five owners, three bankruptcies, and each one redesigned instead of shipping.** Wheeler (to 1991), Express Design (Chapter 7, 1996), Express Aircraft Co (out of business 2004, after its president was killed in the turbine Auriga), Exosphere (2005-07; five builders won about $250,000 in judgments for undelivered parts and prepaid builder assist), and Composite Aircraft Technology (2007, last seen about 2013). Builders report months of parts delays and poor metal parts (B, F).
4. **The tail problem was public, and its fix was an extra.** A builder's dispute with Wheeler over the tail (1991), then Express Design's 1995 letter recommending the Series 90 tail, told every prospect that the airplane had a handling issue and that the cure cost money.
5. **The competition shipped.** In 1994 a Lancair IV airframe was $46,900 and a IV-P $66,900, for a faster airplane; in 2003-05 an Express 2000 FT was $48,900, against a Velocity XL at $37,500 (2005). Van's RV-10 arrived in 2003 as a complete matched-hole metal four-seat kit from a company that delivers; one long-time Express builder wrote that today he would probably pick an RV-10 (B).

**What a revival fixes.** Points 2-5 are business execution, which is what a modern, fully tooled, complete kit or factory-assist build addresses (stage 4). Point 1 is history. The tail is an engineering fix with a known cost. What a revival cannot buy back is the accident record, which is why the tail and a flight-test programme come first.
"""

UPDATES = {
    "express-2000": dict(
        rank="2 of 5",
        bill='Bill, 2026-10-24: "Very interesting... I never understood why this didn\'t do better in the market." He knew a pilot killed in an Express at Grand Prairie Municipal: "It has a tendency to bite in with the stall behavior in climbing right turns." Kept and dug into: the stall and yaw problem and the market failure, below.',
        verdict="""**Rank 2.** The best-evidenced design on the shortlist (a CAFE flight test and a weighed aircraft), with four real seats on 210-260 hp. On the long list's published column it passes useful load (1,045 lb, the kit maker's) and range (1,401 nm, which is CAFE's computed VFR range, not a maker's figure) but has no maker's speed; as measured it misses useful load by 99 lb (901 lb on the weighed aircraft) and cruises 169 KTAS at 6,190 ft. On an AM20T our check gives 179-191 KTAS and 1,062-1,115 nm on full fuel at continuous power. Its accident record is the problem, and the dig below connects it to the tail, the power the tail was asked to handle, and stall speeds higher than published, each with a stated fix and cost. It died of business execution, which a revival can fix. It ranks below the Aries because the tail must be re-derived and flight-tested before anything else, and because its rights are orphaned.""",
        ideas=["Four real seats and a 1,000 lb design useful load on 210 hp, with the best-measured performance in the survey (CAFE 1997).",
               "An NLF(1)-0215F laminar wing on a kit, which CAFE's numbers show working: 169 KTAS at 6,190 ft on about 169 hp.",
               "Lesson, the tail: size the vertical tail for the installed power and keep the horizontal tail out of the fin's wake; the S-90 tail was the kit makers' own fix.",
               "Lesson, the business: complete kits, real build hours and a flying fleet sell kits; redesign churn and incomplete kits killed it."],
        extra_sections=[("The stall and yaw problem, and what fixes it", EXPRESS_STUDY),
                        ("Why it failed in the market", EXPRESS_MARKET)],
        safety="""Record (our count, NTSB CAROL with dockets, ASN and foreign reports; full table in `docs/shortlist/check/express/README.md`): 18 fatal accidents and 30 deaths, 1990-2025 (19 and 32 with one aircraft of unconfirmed lineage), on about 100 ever registered and 55 active. Of 17 in-flight stall or loss-of-control events, 14 were fatal; 9 record a right turn, 3 a left. The NTSB named the design's poor yaw stability as contributing in CEN15FA321, on the strength of the 1997 CAFE flight test, and quoted the kit makers' 1991 and 1995 tail letters in WPR17FA185. Power-loss accidents are the second pattern (at least six). See the study above for the configuration link and the fixes.""",
        died="""A 1990 demonstrator crash before any customer aircraft flew, incomplete kits, five owners and three bankruptcies, a public tail problem, and competitors that shipped (details above). The business causes are what a revival with complete, tooled kits fixes; the tail is an engineering fix with a known cruise cost of 2-4 kt.""",
        next="""- Fin dimensions and tail arm: none are published. Measuring an aircraft, with Bill's go-ahead on any contact, would turn the stability table from parametric into a number.
- A tail re-derivation sized at 260-300 hp, then a stall and departure-resistance flight-test plan (AERO; SAFETY review asked on AER-3785 first).
- Trace Composite Aircraft Technology's 2007 assets (Elon).""",
    ),
    "lancair-iv-p": dict(
        rank="3 of 5",
        bill='Bill, 2026-10-24: kept. He believes the assets went to a new company in Austin, Texas, within about two years, which is re-tooling to support existing customers (Elon verifies, AER-3805). He knows the Oregon shop that re-wings and remanufactures Lancairs: "quite impressive actually, but it\'s not cheap."',
        verdict="""**Rank 3.** It has the speed: 200-211 KTAS on our check at an assumed 195 hp, and about 235 aircraft on the register. It ranks third for three reasons: the worst fatal record in the survey, with its stall-spin half tied to a 36 lb/ft2 wing loading; a cut to about 55% of its design power on an AM20T, which costs climb far more than cruise; and an open chain of title. The RDD LX7 re-wing (below) is the evidence that the wing problem can be engineered out, at a price.""",
        ideas=["Pressurisation and FL240 cruise in a kit, the fastest piston four-seater of its era (published 287 KTAS at 24,000 ft).",
               "**The re-wing, as an idea and a data point.** RDD Enterprises (Redmond, Oregon) rebuilds flying IV-Ps as the LX7: a new one-piece dual-spar carbon wing with a laminar section and double-slotted flaps, a new tail, 180 gal of fuel, a BRS parachute and de-ice, on a TSIO-550-E or a PT6A. RDD's figures (F): span 34 ft (stock about 30 ft), area unchanged at 98 ft2 (AvWeb), so aspect ratio about 12 instead of 9 (E); Vso 63 KIAS piston and 58 turbine; MTOW 3,750 lb piston (stock 3,550 lb), empty 2,350 lb (stock 2,200 lb factory); 260 KTAS at FL250 on 24 gph (stock published 287 KTAS at FL240). A broker's pilot report gives 252 KTAS on 17.5 gph at FL210 and calls the stall extremely docile (P). Prices: $821,000 piston and $980,000 turbine complete (AvWeb, 2019). **What it says:** about 25 kt and 150 lb of empty weight bought a docile, slower stall and much more fuel on the same airframe. Our check (E): 63 kt at 3,750 lb on 98 ft2 implies a landing CLmax of about 2.85, at the top end for double-slotted flaps, so the claim should be measured before it is relied on. No independent flight test was found. Sources: https://www.avweb.com/aviation-news/lx7-a-thoroughly-reworked-lancair-iv-p/ ; http://www.lx7aircraft.com/lx7-piston.html ; https://txtopaviation.com/flying-the-rdd-lx7/",
               "Lesson: on an airframe this fast, the wing that makes the speed is also what makes the stall unforgiving; the LX7 shows the trade."],
        next="""- Chain of title, and Bill's Austin company (Elon, AER-3805; contact is Bill's call).
- If it goes forward: a SAFETY review of the stall-spin pattern, asked on AER-3785 first.
- A climb and take-off check at 195 hp, and a weight-and-balance with the lighter engine (AERO).
- The LX7 wing as a modernisation path: an independent stall measurement would settle the 63 kt claim.""",
    ),
    "mooney-301": dict(
        rank="5 of 5",
        bill='Bill, 2026-10-24: "Interesting. There are a few active flying examples." Kept. On the flying examples, the record disagrees; see "The registry, against Bill\'s recollection" below.',
        verdict="""**Rank 5.** It has the best payload-range on our numbers (858-867 lb over 1,000 nm with reserve, as information) and is the only six-seat design close to the mission. It ranks last because nothing of it survives to revive: one airframe, scrapped; drawings that went to Socata in 1987; rights unresolved between Mooney International and Daher; a tail its test pilot called "certainly not certifiable"; and a published speed that reads 9% optimistic against the fleet calibration. A revival is a new design that takes its layout as a reference.""",
        ideas=["A laminar wing, pressurisation and six seats on 360 hp, with a deliberately tiny low-drag cowl inlet: the concept that became the TBM 700.",
               "Lesson: the prototype flew about 200 lb heavy and slower than planned; weight control failed, not the layout."],
        extra_sections=[("The registry, against Bill's recollection", """
**The public record shows one Mooney 301 (Mooney M30), and none flying.** In the FAA registry download of 2026-10-24, the M30 model code (5872030) has exactly one aircraft in its history: N301MX, serial 0000, cancelled 26 July 1989. Nothing is registered on it today, and no current or past registration, amateur-built included, is a 301 copy or replica. The query was checked against a positive control (the Mooney M22 code returns 14). Flying magazine's June 1983 first-flight report calls the aircraft "M30 number one", a company proof-of-concept aircraft, and says a pre-production prototype would follow; no later source has one built. The airframe went to Tarbes in 1987, came back to Kerrville, and was scrapped (wings cut off, the rest to an A&P school in Abilene, Texas; Mooney Events, citing Mooney staff).

**What may explain the difference (inference).** The likeliest is the **Mooney M22 Mustang**: Mooney's other pressurised single, about 36 built, 14 still on the US register, fewer actually flying. The second is the 301's descendant, the **TBM 700 family**, often described as the 301 living on (about 1,011 US registrations). Less likely: Mooney's other speed-named models (201, 231, 252), or Piper's six-seat PA-32R-301. A photo or an N-number from Bill would settle it, and would change this dossier if it shows a 301 airframe.

Sources: FAA Aircraft Registry, ReleasableAircraft.zip (MASTER, DEREG, ACFTREF), 2026-10-24; https://www.aeroresourcesinc.com/uploads/198306-1983%20Mooney%20301%20Prototype.pdf ; https://mooneyevents.com/Mooney301.html
""")],
    ),
    "cessna-p210n": dict(
        status="calibration",
        rank="calibration case, not a candidate",
        bill='Bill, 2026-10-24: probably worthwhile, and kit builders are attempting 210 analogs, "but it\'s not solving some of what I\'m after in the innovation side." Kept only as the calibration case.',
        verdict="""**Calibration case.** Seven POH points match the build-up with drag factors of 1.26-1.32, tight enough to anchor the fleet calibration every other design is checked against. As a candidate it is a live, firmly held certified type, and Bill has set it aside on innovation. The 210-class kits he mentioned are in the long list (fixed-gear, high-wing five-to-six-seat kits; none is a retractable 210 copy).""",
        ideas=["Six seats, pressurisation and a large, well-documented fleet: the reference for the method.",
               "The 210-class kits (Bearhawk 5, Murphy Moose and others) show builders want a six-seat utility airplane; none offers the 210's retractable speed."],
    ),
    "cozy-mkiv": dict(
        status="reference",
        rank="reference",
        verdict="""**Reference, on two bases that are kept apart.** As published (cozyaircraft.com specs), the Cozy MKIV passes all three floors: 1,000 lb useful, 191 KTAS at 75% and 8,000 ft, and 1,130 nm (1,300 statute miles) at 40% power. As measured on the CAFE Foundation's test aircraft it gives 871 lb useful (1,179 lb empty against the 2,050 lb design gross), 177 KTAS at 8,000 ft at full throttle, and 1,049 nm still air with no reserve at 12,000 ft lean. The gap is empty weight: the designer's 1,050 lb against one equipped builder aircraft at 1,179 lb. Our drag check matches CAFE's measured speeds with a factor of 1.36. Candidates are compared with the Cozy published-to-published and measured-to-measured. The first version of the long list called it a near miss on 951 nm; that was a basis mismatch (a max-cruise claim against a 40% power range), not a units error.""",
        ideas=["Side-by-side front seats in a canard pusher: the Long-EZ layout widened to four seats without losing its cruise efficiency on 180 hp.",
               "Moldless construction a plans builder can do without tooling; the cost is build hours and weight scatter between builders."],
    ),
}

NEW = {
    "bellanca-t250-aries": dict(
        rank="1 of 5",
        results=["bellanca-t250-aries"],
        bill='Bill, 2026-10-24: not in the first long list; "add it, and shortlist it if the numbers support that." They do.',
        verdict="""**Rank 1.** As published it passes all three floors: 1,300 lb useful, 1,017 nm at economy cruise with a 45-minute reserve, and 181 KTAS at 75% (altitude not stated); AOPA measured 181 KTAS at 6,500 ft on 73% in 1977. Our check agrees with the published speed (drag factor 1.26-1.34 on AOPA's two points, inside the fleet band), so the airframe is as clean as claimed. It reads the published range about 10% optimistic: 1,008 nm still air with no reserve at 65% and 8,000 ft on 76 gal. On an AM20T it is a direct fit (250 hp to 260 hp take-off, similar cruise power): 185-197 KTAS, 1,300 lb useful (factory; no fleet figure exists for four aircraft), 906-919 nm on full fuel at continuous power, and over 1,000 nm at economy power (154-161 KTAS, 859-861 lb with a reserve, as information). Its record is clean (one NTSB event in about 50 years, on four aircraft), it died with its producer rather than for any flaw, it was designed from flat and single-curve skins to be cheap to build, and its type certificate is still current. Its weaknesses: only four exist, so there is no fleet record to judge, and range at continuous power is about 90 nm short on standard fuel.""",
        ideas=["A laminar (NACA 6-series), constant-chord, flush-riveted metal wing on a fuselage built from flat and single-curve skins to cut production cost: speed from a design meant to be cheap to build (Plane & Pilot; AOPA 1977).",
               "Mains that retract inward under the rear seat so the wing can stay thin; the price was a car-width track and sluggish ground steering (AOPA 1977).",
               "A 250 hp, 1,300 lb useful airframe that is a direct AM20T-class fit, with a current type certificate (A11SW).",
               "Lesson: it died with its producer (Bellanca's 1980 receivership), not on a technical or safety failure."],
        engine="""- **Power.** The AM20T (260 hp take-off, 195 hp assumed continuous) replaces a 250 hp O-540 that cruises at 163-188 hp (65-75%). The cruise power is about the same, so the Aries keeps its speed: 185 KTAS at 8,000 ft (low case) and 197 KTAS at 16,000 ft (high case).
- **Mass and CG.** The installed mass falls by about 64 lb (E), in the nose. That needs ballast or a longer mount; the headline useful load takes no credit for the saving.
- **Cooling.** The O-540 used a single inlet below the spinner and no cowl flaps. A radiator needs its own duct, not yet designed; Raymer's cooling drag is carried unchanged.
- **Fuel.** At continuous power the 76 gal usable gives 906-919 nm still air. A modest tank increase, or economy cruise, closes the range floor.""",
        rights="""Open question, with a current type certificate (stage 2 file pending: Elon, AER-3805). TCDS A11SW (Rev 2, 1 July 1980) is Current; its holder is still Anderson, Greenwood and Company, Houston, with Bellanca listed as former holder, and production certificate 1GL (Bellanca, Alexandria MN) covered serials 3 and up (FAA DRS, P). Unverified secondary company histories say the Anderson Greenwood valve business passed through Keystone, Tyco and Pentair to Emerson, so the TC may sit dormant with a valve company. Four aircraft are registered (the prototype and serials 0003-0005). Who holds the TC and drawings today, and whether they would sell, needs research and then an attorney; any approach is Bill's call.""",
        safety="""Record (NTSB CAROL, queried by make, model and every registration): one event in about 50 years, FTW83LA173 (1983, the prototype): a taxi brake failure and gear collapse, no injuries. No fatal accidents. Four aircraft is too few for a rate, so a clean record here is an absence of evidence, not evidence of safety. AOPA's 1977 flight check noted weak yaw damping after a rudder input and a narrow gear track.""",
        died="""Anderson Greenwood, a Houston valve maker, designed and certified it (about $1.2 million in 1975-76) and took control of Bellanca to build it at Alexandria, Minnesota. The Bellanca plant was nearly idle by 1977 and production capital still had to be raised; Bellanca went into receivership in 1980, reportedly drained by the composite Skyrocket II programme. About four were completed. Nothing in the record is a technical or safety failure. A revival with modern manufacturing and its own financing fixes the cause directly.""",
        next="""- Rights: who holds TC A11SW and the drawings now (Elon, AER-3805; contact is Bill's call).
- Tail dimensions and a three-view: none are published; the tail here is sized by volume coefficient. Measuring one of the four aircraft would replace it.
- A fuel flow at a known power, which no source publishes; it would replace our BSFC assumption in the range.""",
    ),
    "meyers-200d": dict(
        rank="4 of 5",
        results=["meyers-200d"],
        bill='Bill, 2026-10-24: "Interesting to me." He can\'t afford the rights and is "not sure it\'s necessary": re-deriving may do. "That\'s a big plane too." Shortlisted, with the idea ledger and a re-derivation path ahead of the rights.',
        verdict="""**Rank 4.** As published it fails range (782 nm on normal fuel with a 45-minute reserve) and passes useful load (1,060 lb) and speed (182 KTAS at 75%, altitude not stated). As measured it is a near miss: about 900 lb useful at the fleet-typical 2,100 lb empty, and 178 KTAS at 8,500 ft on about 67% (AOPA 1991). Our check needs a drag factor of 1.41 to match AOPA's point, just above the fleet band, which fits a 1960s riveted airframe with the skin waviness and protrusions Davisson noted; it gives 857 nm still air on 74 gal at 65% and 8,000 ft. On an AM20T: 178-189 KTAS, 831-863 nm on full fuel. So the speed is there and the range and empty weight are not, and both are what a re-derivation would fix: more fuel in the wing and a lighter structure. It ranks below the Express because a re-derivation is a new airplane, and above the 301 because a holder, a type certificate, drawings and 58 registered aircraft exist.""",
        ideas=["A welded 4130 steel-tube cage from the firewall to the rear cabin and out to the main-gear points, skinned in aluminium: crash protection and one load path for engine, wing centre section and gear. No airframe ADs or in-flight breakups on record.",
               "Speed on modest power: 177-178 KTAS measured on 67-75% of 285 hp, from a 161.5 ft2 wing with a NACA 230-series root, strong washout and Fowler flaps (benign stall with aileron authority; a low landing speed).",
               "High gear and flap speeds, and a gear-flap interconnect, that make slowing down and configuring easy.",
               "Drop: the four-tank, one-gauge fuel system (ten of its 26 accidents are fuel starvation), no rudder trim or thrust offset, and heavy controls.",
               "Lesson: hand-built at a loss ($4 million to make $3 million of airplanes, Plane & Pilot 2024); a re-derivation must design for cheap production from the start."],
        engine="""- **Power.** The AM20T at 195 hp assumed continuous replaces a 285 hp IO-520 cruising at 185-214 hp. That gives 178 KTAS at 8,000 ft and 189 KTAS at 16,000 ft.
- **Mass and CG.** The installed mass falls by about 89 lb (E), in the nose of a short tractor; ballast or a longer mount takes it back. The headline useful load takes no credit for the saving.
- **Cooling.** A radiator in place of conventional nose inlets: not designed.
- **Fuel.** 74 gal usable is the constraint: 831-863 nm at continuous power. A re-derived wing with about 100 gal closes the floor (E).""",
        rights="""Small holder, live type certificate (Elon, `docs/rights/meyers-200d.md`, PR #3). TCDS 3A18 (Models 200-200D and the Interceptor 400) is Current, Rev 19 (2014), held by Interceptor Aviation Inc.; there is no production certificate. The TC, drawings, jigs and tooling were offered for sale through a broker in October 2019, with no sale found; the parent, GlobalParts Group, was bought by VSE Corporation in 2021, and whether Interceptor Aviation went with it is unknown. Bill's question is whether the rights are needed at all for a re-derivation: what the public record supports (published dimensions, the TCDS, the steel-tube-cage concept) and where an attorney is needed is with Elon on AER-3805.""",
        safety="""Record (our count from the NTSB bulk databases, 1982-2024): 26 accidents, 6 fatal (8 killed), on about 130 built and 58 registered. Ten accidents are fuel starvation, mostly from the four-tank, one-gauge fuel system: a systems flaw a re-derivation drops. The fatal accidents are mixed (fuel starvation, low passes with alcohol, low-altitude manoeuvring, a misinstalled intake screen, a gusty-crosswind take-off). No in-flight breakup. No pattern tied to the configuration was found.""",
        died="""Commercial, not technical. Meyers hand-built each aircraft with minimal tooling; Aero Commander bought the design in 1965 and found it took $4 million to make $3 million of airplanes. It was priced near a V-tail Bonanza and carried less, and its 3,000 lb gross was never raised. A re-derivation designed for production, with more gross weight and fuel, addresses all three.""",
        next="""- The re-derivation question: what the public record supports and where an attorney is needed (Elon, AER-3805).
- Chords, tail areas and a three-view: none are published; the model here assumes taper 0.5 and sizes the tail by volume coefficient.
- A re-derivation sketch at about 3,300 lb gross with 100 gal, on an AM20T (AERO, if it goes forward).""",
    ),
}


ROHR_SCALE = """
**Question (Bill):** "What happens if we scale up the design?" Take the 2-175's configuration (low delta wing, engine buried in the fuselage, shrouded pusher fan, folding wing and fin) to four seats on an Aeromomentum AM20T, and find what it needs to approach the targets and where it stops working. Conceptual fidelity: a component drag build-up on analytic wetted areas, a ducted-fan momentum model, and a weight estimate calibrated on the survey's weighed composite four-seaters. Script and full tables: `docs/shortlist/check/rohr/`.

**First, the 2-175 itself.** Fraser's late three-view settles the geometry (span 20 ft, wing 180 ft2, aspect ratio 2.2, wing loading 8.1 lb/ft2, tailless cropped delta with elevons, 40 in fan in a 40.25 in duct). Through our method, on the 106 hp a 150 hp engine makes at 10,000 ft, it cruises 142-151 KTAS against Rohr's design target of 152 kt at 10,000 ft (May 1974 memo, F). The target needs 107-122 hp. **The design target is credible**; no measured speed survives to confirm it.

**Four seats on an AM20T** (gross 2,900 lb; empty 0.60 of gross plus 100 lb for the duct, fan, shaft and folds, so 1,840 lb and 1,060 lb useful, E; 105 gal; 195 hp assumed continuous; drag factor 1.16-1.36):

| Wing | Span | KTAS at 8,000 ft | KTAS at 16,000 ft | Range on 105 gal, still air | Touchdown at a 14 deg attitude |
|---|---|---|---|---|---|
| 210 ft2, AR 2.2 (the 2-175's planform, scaled) | 21.5 ft | 152-163 | 156-169 | 1,052-1,127 nm | 65 kt |
| 210 ft2, AR 3.0 | 25.1 ft | 159-169 | 167-178 | 1,091-1,162 nm | 61 kt |
| 210 ft2, AR 4.0 | 29.0 ft | 162-172 | 172-183 | 1,109-1,179 nm | 59 kt |
| 358 ft2, AR 2.2 (geometric scale-up at the 2-175's wing loading) | 28.1 ft | 149-159 | 157-168 | 1,025-1,092 nm | 50 kt |

**What it needs to approach the targets.**
- **A higher aspect ratio than the 2-175's.** As a pure low-aspect-ratio delta it sits on the 160 KTAS floor at 8,000 ft. At AR 3-4 (a cranked or less-swept delta) it reaches 159-172 KTAS at 8,000 ft and 167-183 KTAS at 16,000 ft. The preferred 180 KTAS needs AR 4 and the high critical-altitude case. Range and the estimated useful load clear their floors in every row.
- **About double the 2-175's wing loading.** Square-cube growth works against a straight scale-up: to carry 2,900 lb at the 2-175's 8.1 lb/ft2 the wing grows to 358 ft2, and the extra wetted area makes it slower, not faster. At 13-16 lb/ft2 the wing is 180-210 ft2.
- **A fan sized for drag, not thrust.** At 260 hp the fan's diameter hardly matters at cruise: from the 2-175's 40 in to 53 in (its disk loading at 260 hp) the speed changes by 2 kt, because the bigger duct's drag cancels the better fan efficiency (0.78-0.80). The duct costs a few knots against an open propeller at cruise; it buys an enclosed fan, quieter running, more static thrust and a place to put the radiator, as the 2-175 drew its cooling air through it.

**Where it stops working.**
1. **Landing speed.** A low-aspect-ratio wing reaches its maximum lift only at an angle of attack the gear and the pilot's view do not allow. Limited to a 14 deg attitude, with simple trailing-edge flaps (E), the four-seater touches down at 59-70 kt on 180-210 ft2. The 2-175 landed slowly because it was light; at four seats, short-field and garage-friendly stop pulling the same way as speed.
2. **Balance.** With the engine behind two rows of seats and the fan at the tail, our first-cut weight and balance (positions E) puts the in-flight CG range at about 5% of the mean chord, from pilot alone to four aboard. That is within what elevons on a tailless delta can usually trim, but only if the wing is placed so its neutral point sits well behind the aft CG, and only with rear passengers and fuel close to the CG. Aft baggage, a longer cabin or a heavier fan would break it. A tail or canard fixes it and departs from the 2-175.
3. **The shaft.** The 2-175's own extension shaft had to be redesigned for vibration, and its one recorded incident was a drive coupling failure after take-off. The Cirrus VK-30, the survey's other buried-engine pusher, lost three of its five fatal accidents to the shaft drive, flutter and spin recovery. A four-seat version needs a longer shaft behind two rows of seats; it must be treated as primary structure.
4. **Folding.** At 25-29 ft spread, the outer panels must fold to reach a garage or trailer width. The 2-175's fold (two FRP piano hinges and torsion bosses, no spar) is documented only in words.
5. **The weight estimate.** The 1,060 lb useful load rests on an empty fraction of 0.60 plus our 100 lb for the layout. Every 100 lb of real empty weight above that comes straight off it.

**Reading.** Scaled to four seats on an AM20T, the 2-175's layout reaches the floors on paper only with a higher-aspect-ratio wing than the original, and then flies 15-20 kt slower than the Express or the Aries on the same engine. What the configuration offers instead is an enclosed fan, a compact folding airframe and a buried, quiet engine. Whether those are worth 15-20 kt is Bill's call. Nothing here claims stability, spin or flutter behaviour; a tailless delta's handling is a flight-test question.
"""

ROHR_RECON = """
**Question (Bill):** "Can we build the existing general concept from the information we have?" **Short answer: the outer lines and the propulsor layout, yes, to about 5-10%; the structure, the weights and the performance, no; they would be re-engineered and then measured.** Full inventory, with every source: `docs/shortlist/check/rohr/README.md`.

| What survives | Where | What it yields |
|---|---|---|
| **The late three-view** of the flying aircraft, labelled: span 20 ft, length 23 ft, Lycoming O-320X, wing 180 ft2, fin 16 ft2, elevons 22.8 ft2, gross 1,450 lb | Richard Fraser's site (a Rohr project engineer), on the Wayback Machine | Planform, fold line, dog-tooth, duct size, fin sweep, side profile, gear track. Our scaled check agrees with the labels within 5%. It settles the span: 20 ft, not the 30 ft aerofiles copied from an earlier drawing that Fraser says was mislabelled |
| **The Rohr propulsor sketch and efficiency map** (memo of 8 May 1974) | Fraser's site | Duct NACA 23015, 40.25 in ID, 2.75 ft long, area ratio 1.2; fan 40 in, five blades (NACA 65-series), 4,000 rpm, variable pitch; six NACA 65412 stator vanes; efficiency targets; cruise target 152 kt at 10,000 ft. This is the turbine propulsor, tested only on the ground; the aircraft flew a four-blade wood propeller whose size is not published |
| **Ten Rohr factory photographs of N62R** | SDASM Flickr (posted 2025-26), from the Rohr collection | Underside planform, head-on view (duct, fin, scoop, canopy, gear), duct exit with hub and stator, side profiles. No fold mechanism or cockpit interior |
| **Walter E. Mooney's 1987 talk** (the designer, not Al Mooney), written up in TWITT No. 10 | TWITT newsletter archive | Configuration logic, 150 hp at 4,400 rpm, sparless foam-core FRP wing with a piano-hinge fold, dog-tooth for pitch-up, symmetrical airfoil, cooling through a dorsal scoop and an exhaust ejector, flight-test notes, why it died |
| **US 3,931,943** (Westergren and Mooney, 1976) | USPTO | The nose-wheel shroud-rudder and pedal mechanism only; no aircraft dimensions |
| **SDASM Rohr/Goodrich collection** | Finding guide online; material by appointment | One 71X entry: a binder of 35 mm slides (Box 46). William Chana's papers (deputy programme manager) may hold more; not seen |
| **The tribute book** | See below | 166 pages of photos, drawings, construction methods and the test pilot's commentary, by the sellers' description |

**What would have to be re-engineered.** The wing and fuselage structure (no layup or airfoil coordinates survive; a sparless foam-core skin would be re-analysed or replaced); the airfoil (only a symmetrical section is recorded, and a tailless delta wants a reflexed one); the fan for an AM20T (the RP-17-V was designed for a 160 shp turbine; the flown wood propeller is unrecorded); the fold mechanism (described, not drawn); and every weight and performance number, which would come from building and flying it. No airframe survives: Fraser records the airframes were cut up and dumped, and the engines, propellers and wheels were salvaged.

**Leads that need contact, so Bill's call:** Fraser reported finding over 400 colour slides (2021); Don Westergren kept one wood propeller and the nose wheel (2012); Mooney's own slides and three-views (he died in 1990).

**The book: *The Rohr 2-175 (71X) FanJet: A Tribute*, Richard W. Fraser with Don Westergren.** Self-published by Fraser Aero Technology Company, Orange, California, about 2012; colour paperback, 166 pages; **ISBN 978-0-615-59079-0**. Last sold at $19.98 by Fraser and by Aircraft Spruce (part 13-11711). Out of print since at least 2019, and Fraser's domain has lapsed. No listing was found on Amazon, AbeBooks or Open Library, and no copy in the Library of Congress or San Diego County Library catalogues. **Not checked, because they block automated access: WorldCat, eBay, Biblio and Alibris.** A few minutes in a browser, by ISBN, would close that. Buying a copy is Bill's call.
"""

NEW["rohr-2-175"] = dict(
    status="study",
    rank="studies, not ranked",
    results=[],
    bill='Bill, 2026-10-24: "The planform, the layout meets much of what I\'m after." It stays in the analysis whatever the targets say, with two studies: "What happens if we scale up the design?" and "Can we build the existing general concept from the information we have?"',
    verdict="""**Not ranked; studied.** As built it is a 1,450 lb two-seater and cannot approach a 1,000 lb useful load. Its design target (152 kt at 10,000 ft on 150 hp) is credible on our check. Scaled to four seats on an AM20T it reaches the floors on paper only with a higher-aspect-ratio wing than the original, and then about 15-20 kt below the conventional shortlisted designs on the same engine; balance with the engine behind two rows of seats, landing speed and the shaft are where it stops working. Its outer lines and propulsor layout can be rebuilt from what survives; its structure, weights and performance cannot.""",
    ideas=["A low, sparless delta wing whose outer panels and fin fold so a two-seater fits a single-car garage.",
           "An engine buried in the fuselage driving a shrouded fan in the tail: enclosed blades, low noise, cooling air drawn through the duct.",
           "A nose-wheel shroud that doubles as a rudder (US 3,931,943).",
           "Lesson: the drive shaft between a buried engine and a tail fan is primary structure; the 2-175's needed a redesign for vibration and failed once in flight."],
    extra_sections=[("Study 1: scale-up to four seats on an AM20T", ROHR_SCALE),
                    ("Study 2: reconstructability, and the book", ROHR_RECON)],
    engine="""- **As built:** a special high-rpm Lycoming (O-320X on the three-view), 150 hp at 4,400 rpm per TWITT, through a short extension shaft to a four-blade wood propeller in the duct. The AM15T (160 hp) is a direct fit for the two-seater.
- **At four seats:** an AM20T (260 hp; 195 hp assumed continuous), with the radiator in the duct inflow. See Study 1.""",
    rights="""Rohr Inc. is now part of Collins Aerospace (RTX). Nothing survives to own beyond whatever drawings or slides are in archives or private hands, and US 3,931,943 (the rudder and pedals) expired long ago. Stage 2: `docs/rights/rohr-2-175.md` (Elon, PR #1). Research, not legal advice.""",
    safety="""Record: no accident. One in-flight incident: a drive-shaft coupling failure after take-off, landed undamaged (stage 1). The extension shaft was redesigned for vibration (Fraser). A spin-recovery drag chute was fitted for flight test (Fraser).""",
    died="""Rohr cut the programme in its 1975 retrenchment for reasons Mooney said had "nothing to do with the merits of the airplane" (TWITT, stage 1). A revival would not be held back by that; it would be held back by the scale-up limits in Study 1.""",
    next="""- Browser checks for the book (WorldCat, eBay, Biblio, AbeBooks by ISBN 978-0-615-59079-0); buying is Bill's call.
- If Bill wants to go further: a cranked-delta four-seat sketch with a real weight and balance and an elevon trim check (AERO), and a SAFETY view on the shaft drive (asked on AER-3785 first).""",
)


# Deep-dive axes (brief, 2026-10-24). Numbers from docs/shortlist/check/axes/
# (axes.py): Pratt gust dn per 30 ft/s at 150 KEAS and 8,000 ft, MTOW; best L/D
# from the calibrated build-up with propeller drag excluded (real engine-out
# glide is worse); T-hangar door 40 ft (E). The planform trade itself is argued
# once, in the planform study (AER-3807, docs/studies/planform/), not here.
PLANFORM_LINK = "the planform study (AER-3807, `docs/studies/planform/`)"
AXES = {
    "bellanca-t250-aries": f"""**Aspect ratio 5.8**: a moderate, constant-chord wing, on the conventional side of {PLANFORM_LINK}.

- **Storage.** 31.3 ft span, 8 ft 7 in high (AOPA): fits a 40 ft T-hangar door with room to spare. No folding; not trailerable without removing the wings.
- **Construction with home-shop tools.** This is its strongest axis. The wing is constant-chord, so every rib is the same: one set of CNC-routed form blocks makes them all. The skins are flat or single-curve aluminium, designed that way to cut production cost; blanks can be routed, but bending them needs a brake and the riveting is hand work. The largest part is a 15.7 ft half-wing; the root spar is about 7.8 in deep, a machined or built-up metal spar that may need a service. Fittings suit a small CNC mill.
- **Safety.** Published stalls 63 kt clean and 56 kt in landing configuration (72 and 64 mph); AOPA measured 69 and 63 mph IAS. AOPA described no stall break, so stall character is unrecorded; it did note weak yaw damping after a rudder input. Best L/D about 15.7 at 114 KTAS. Spin behaviour: not on record. One NTSB event in about 50 years, on four aircraft, proves little.
- **Ride comfort.** Gust dn 1.66: the roughest of the shortlist with the Meyers, because its 18.5 lb/ft2 wing loading is low. Cabin 45 in wide, 115 in long, 48.5 in high (AOPA): roomy for the class. Noise: not recorded.""",
    "express-2000": f"""**Aspect ratio 7.4**: conventional, on the high-aspect-ratio side of {PLANFORM_LINK}.

- **Storage.** 31 ft span: fits a 40 ft T-hangar door. No folding.
- **Construction with home-shop tools.** A molded vinylester/E-glass/foam airframe. The molds are the problem: a 15.5 ft half-wing and a four-seat fuselage are far beyond a large-format printer's envelope. Plugs could be CNC-routed from foam in sections and faired, and the molds laid up at home, but tooling at this size is a service job or a kit maker's. A fresh tail (see above) is the one new tool a revival must make. Root spar about 9.5 in deep.
- **Safety.** See the stall-and-yaw study above: weak directional stability, a measured clean stall of 67 KCAS against a published 55-58 kt, and stalls in climbing turns in the record. Best L/D about 14.3 at 108 KTAS with its fixed gear.
- **Ride comfort.** Gust dn 1.57 at 22.2 lb/ft2. Cabin 44 in wide (CAFE). Owners compare it to a fast 182 for room (builder opinion).""",
    "lancair-iv-p": f"""**Aspect ratio 9.3**: the high-aspect-ratio, high-wing-loading end of {PLANFORM_LINK}.

- **Storage.** 30.2 ft span (the LX7 re-wing goes to 34 ft): fits a 40 ft T-hangar door. No folding.
- **Construction with home-shop tools.** A pressurised molded composite airframe. The pressure vessel and the 36 lb/ft2 wing are not home-shop parts; molds are unlocated, so any revival re-tools. Small parts and fittings suit a home mill; the airframe does not.
- **Safety.** The stall is the issue: CAFE measured 66 KIAS; owners report 82-90 kt in practice; Kitplanes called the stall bad. The record's stall-spin half follows from that. The LX7's re-wing claims a docile stall at 63 KIAS, unmeasured. Best L/D about 16.6 at 137 KTAS: good glide, at a high speed.
- **Ride comfort.** Gust dn 1.09: the smoothest of the shortlist, because of its high wing loading. That is the same number that makes the stall fast.""",
    "meyers-200d": f"""**Aspect ratio 5.8**: moderate, with a 23015-to-4412 wing and strong washout; conventional in {PLANFORM_LINK}.

- **Storage.** 30.5 ft span, 7 ft 4 in high: fits a 40 ft T-hangar door. No folding.
- **Construction with home-shop tools.** The welded 4130 cage suits a home shop with a CNC router (jig boards and tube-notching fixtures) and a welder; welding certification is the skill, not the tool. The original riveted aluminium skin over the cage needed heavy hand fitting, which is why it was built at a loss; a re-derivation would design the skin for CNC-cut, matched-hole parts. Root spar about 12.7 in deep at the root (the 15% section). Fittings suit a small mill.
- **Safety.** Benign stall with aileron authority into the stall, credited to its washout (AvWeb; AOPA 1991). Published landing-configuration stall 47 kt (Jane's) against 54 kt (Davisson): unresolved. Best L/D about 14.5 at 109 KTAS. The steel cage is a crash-survivability asset; no in-flight breakup on record.
- **Ride comfort.** Gust dn 1.66 at 18.6 lb/ft2: as rough as the Aries. Near-360 deg visibility; cabin dimensions not published.""",
    "mooney-301": f"""**Aspect ratio 9.0**: a high-aspect-ratio laminar wing, on the conventional side of {PLANFORM_LINK}.

- **Storage.** 36.7 ft span: fits a 40 ft T-hangar door with little margin. No folding.
- **Construction with home-shop tools.** A pressurised riveted metal airframe: not a home-shop design. A revival is a new design, so this axis would be set by that design, not by the 301.
- **Safety.** Its test pilot found pitch authority "almost non-existent" with rapid inputs in gusty air on approach and called the stabilator "certainly not certifiable". Best L/D about 16.7 at 119 KTAS.
- **Ride comfort.** Gust dn 1.40 at 26.7 lb/ft2. Pressurisation was meant to give a quiet, high cabin.""",
    "cozy-mkiv": f"""**Aspect ratio 9.1** (main wing; plus a canard): high aspect ratio, in the pusher camp of {PLANFORM_LINK}.

- **Storage.** 28.1 ft span: fits a 40 ft T-hangar door. Canard pushers are long; check hangar depth.
- **Construction with home-shop tools.** The benchmark: moldless foam and glass, built by plans builders without tooling. Cores are hot-wired or CNC-routed; no molds. The cost is hours and weight scatter.
- **Safety.** The canard stalls first and limits the main wing's angle of attack: stall resistance is the type's selling point. Best L/D about 16.3 at 102 KTAS.
- **Ride comfort.** Gust dn 1.51 at 23.6 lb/ft2 (main wing only; the canard adds lift slope, so this is optimistic). Semi-reclined seats; a tight rear cabin.""",
    "rohr-2-175": f"""**Aspect ratio 2.2**: the low-aspect-ratio delta at the far end of {PLANFORM_LINK}, which weighs this trade for the mission. Here, only its own numbers:

- **Storage.** 20 ft span, with the outer wings and fin folding so it fits a single-car garage (TWITT; Fraser): the best storage idea in the survey. At four seats and AR 3-4 (Study 1) the span grows to 25-29 ft and still fits a 40 ft T-hangar door unfolded; folding would bring it to garage or trailer width.
- **Construction with home-shop tools.** A sparless foam-core fibreglass skin: cores are exactly what a home CNC router cuts, in sections. The fold joint (FRP piano hinges and torsion bosses) and the duct are the hard parts. The deep root (about 12% of a 14.7 ft chord, about 21 in) makes the structure efficient without a spar.
- **Safety.** No accident; one drive-coupling failure; a spin chute was carried in test. A low-aspect-ratio delta stalls at high angle of attack with little break and needs a high landing attitude (Study 1: 59-70 kt touchdown at four seats). Best L/D about 9-10 for the AR 2.2 four-seater, against 14-17 for the conventional designs: a much poorer engine-out glide.
- **Ride comfort.** Its lift-curve slope is about half a conventional wing's, so gusts move it less for the same wing loading. Gust dn 1.78 as built (a light 8.1 lb/ft2), 1.17 for the four-seat AR 2.2 version at 13.8 lb/ft2: nearly as smooth as the IV-P at 36 lb/ft2. That is the low-aspect-ratio school's best argument, and AER-3807 weighs it.""",
}
for _k, _v in AXES.items():
    (NEW if _k in NEW else UPDATES).setdefault(_k, {})["axes"] = _v

UPDATES["lancair-iv-p"]["bill"] += " Elon's follow-up (PR #6) found no Austin holder in the public record; it still shows JetEXE, Sacramento."
NEW["rohr-2-175"]["next"] += "\n- A lead from Elon (PR #6): SDASM holds a signed copy of Bill Chana's memoir, *Over the Wing: The Bill Chana Story* (2003), as archival object 5291. Chana was the 2-175's deputy programme manager; whether it covers the 2-175 is not known. Reading it is museum contact, so Bill's call."


PRESCOTT_CONFIG = """
Sources and the full fleet and accident tables: `docs/shortlist/check/prescott/README.md`.

- **The engine sits in the tail cone, right behind the cabin, and drives the propeller through a 12 in extension, not a drive shaft.** Sport Aviation (March 1986): "the shaft is only 12" long." Prescott chose it deliberately: "Early in the design, I decided not to accept the challenges associated with a mid-engine aircraft and the six to eight foot drive shaft that the mid-engine dictates" (RCM, July 1986, F). The museum's drawing list has a "prop extension" (15302) and an adapter bushing, and no coupling, bearing or damper drawings, so it is most likely a bolted flange spacer (our inference). **No drive failure is on record.** The one drive-train event is a wooden propeller that separated in cruise two weeks after being refitted, with elongated bolt holes, cause undetermined (NTSB LAX05LA270).
- **Propeller:** 65 in recommended, 68 in the largest flown (F). Ground clearance is not published and is called marginal in several sources; the short gear that clearance forced meant a small propeller.
- **Tail:** a T-tail on a swept fin, horizontal tail 29.3 ft2 (11 ft span). The 1/5-scale plan drawn by Prescott shows a small ventral fin ahead of the propeller; not confirmed at full scale.
- **Cooling:** air-cooled, in the tail cone. The prototype overheated its oil until the cooler moved to the nose; builders report a hot right rear cylinder (AOPA 1986; Sport Aviation 1991).
- **Structure:** a TIG-welded 4130 square-tube cage with non-structural fibreglass shells flush-riveted to bulkheads (3-8 plies, CAD-cut patterns), so everything can be installed before the shells go on. Aluminium wing: a press-brake-formed 2024 C-spar with nested extrusion caps, stretch-formed leading edges on CAD/CAM steel dies, NLF(1)-0215F section. Spar tested beyond +3.8/-1.5 g; gear drop-tested to 5.5 g; designed to Part 23 but never certificated (Sport Aviation 1986; Prescott 2007).
- **Gear:** fibreglass mains and an Airite nose gear, hydraulic retraction (fixed and retractable kits were offered). The mains sit far aft because the flight CG is far aft; rotation was hard (Wainfan, Kitplanes).
- **Dimensions** (Prescott 2007, F): span 29 ft 4 in, wing 110.8 ft2 (aspect ratio 7.8), length 20 ft 3 in, height 8 ft 9 in, cabin 42.5 in wide. 2,400 lb gross (designed for 2,250, loads report and tests redone at 2,400); 1,550 lb factory empty; 56.5 gal in the wing leading edges (prototype 2). No dimensioned three-view survives online; the RCM 1/5-scale plan (Outerzone oz14320) is drawn by the designer, with a full-scale dimension table.
- **The fleet** (FAA registry, 2026-10-24): 4 current registrations and 15 deregistered, so 19 airframes ever on the US register. Likely airworthy now: N10JS (Allison 250 turbine) and N200SX (O-540). N41PP, the first prototype, is at the Kansas Aviation Museum. Two more are known abroad. Builders re-engined widely (O-540, Ford V-6, Mazda rotary, Allison 250). **The one weighed builder aircraft**, N747P, came out at 1,555 lb in the shop and 1,661 lb finished with ballast for CG (Sport Aviation 1991), so 739 lb useful: two adults and full fuel. Its first customer called it "really only a two-seat airplane" (Syracuse, Kitplanes).
"""

PRESCOTT_GAP = """
**The brochure's 165 KTAS at 7,500 ft against Kitplanes' measured 151 KTAS at 73%.** Kitplanes' May 1988 figure ("174 mph true at 73% power", second prototype) has no published altitude, weight or rpm; the full article was not reachable. Our model resolves the two this way:

| Claim | Drag factor our model needs to reproduce it | Reading |
|---|---|---|
| Brochure: 165 KTAS at 7,500 ft, 75% (135 hp), 2,400 lb | 1.35 | Inside the fleet band (1.16-1.36): the brochure is consistent with the airframe's geometry |
| Kitplanes: 151 KTAS at 73% (131 hp), if flown at sea level | 1.46 | Draggier than the band |
| The same, if flown at 7,500 ft | 1.67 | Much draggier: Defiant-like |

So either Kitplanes flew low and the airplane is 10-25% draggier than its geometry predicts, or the 73% was optimistic: on prototype 1 the fixed-pitch wood propeller held the engine to 2,400-2,600 rpm. The builders' verdict sides with the measurement: "The Prescott Pusher with the 180-hp Lycoming really didn't match up to its marketing numbers" (Syracuse, Kitplanes, B), and Wainfan wrote that "once it got into the air, it proved to have disappointing performance." We carry both bases in every result below, labelled, and never mix them. Every pusher in this survey with measured points reads draggy (Defiant 1.72, Velocity 1.63); the planform study (AER-3807) is the place to test whether that is the configuration.
"""

PRESCOTT_LEVERS = """
Bill's question: on an Aeromomentum engine, turbo-normalised at altitude, what moves useful load (850 lb published, 150 short), range (869 nm published, about 130 short) and speed, and does it clear all three floors? Script and full tables: `docs/shortlist/check/prescott/levers.py`. Assumptions: 195 / 120 hp continuous and 8,000 / 16,000 ft critical altitudes are ours; the structure deltas are placeholders until MANUFACTURING (AER-3784) answers; the 75 and 90 gal tankage is our estimate (the 15% wing has about 280 gal of geometric volume).

**The engine sits in the tail, so engine weight costs twice.** Every pound added behind the cabin needs about 1.3 lb of nose ballast to keep the CG where it was (our estimate of the arms), and the Prescott's CG was already its weak point. The AM20T is 61 lb heavier installed than the O-360, which costs about 82 lb of ballast; the AM15T is 26 lb lighter and saves about 35 lb.

| Lever | Useful load | KTAS (brochure basis / measured basis) | Range, nm, full fuel, still air, at continuous power |
|---|---|---|---|
| As published (O-360) | 850 | 165 at 7,500 ft (published) | 869, reserve not stated (published) |
| AM20T alone, 16,000 ft critical altitude | 707 (-143) | 207 / 196 | 705 / 669 |
| AM15T alone, 16,000 ft | 911 | 169 / 159 | 934 / 883 |
| AM20T + 90 gal | 707 | 207 / 196 | 1,187 / 1,127 |
| AM20T + 90 gal + 200 lb lighter structure, at 2,400 lb | 907 | 207 / 196 | 1,187 / 1,127 |
| **AM20T + 90 gal + a 2,700 lb gross structure no more than 100 lb heavier per pound of gross than today's (net -100 lb)** | **1,077** | **204 / 194** | **1,172 / 1,112** |
| AM15T + 90 gal + 200 lb lighter, at 2,400 lb | 1,111 | 169 / **159** | 1,587 / 1,503 |

**What each lever buys.** More power at altitude buys speed and nothing else: the AM20T lifts cruise to 194-207 KTAS and costs useful load through the tail-cone weight. More fuel buys range and nothing else: 90 gal clears 1,000 nm at continuous power on both bases. A lighter structure buys useful load pound for pound, but at 2,400 lb even 200 lb lighter leaves the AM20T version at 907 lb. **It clears all three floors on both bases only as a re-derivation**: a structure designed for about 2,700 lb gross, about 100 lb lighter than today's structure would be at that weight, 90 gal, and the AM20T. The AM15T alternative clears load and range at 2,400 lb with a 200 lb lighter structure, but its cruise speed falls to the floor (159-169 KTAS). With 90 gal aboard at 2,700 lb, the AM20T re-derivation carries about 540 lb of people and baggage: it is a four-seater with full fuel only for light occupants, as the original was.

**The real constraint is balance, not power.** The AM20T makes the Prescott fast, but its weight in the tail cone makes the documented aft-CG problem worse. A re-derivation would move the wing aft or lengthen the forward fuselage to put the CG where the gear and the tail want it, and that, not the engine, is the design work.
"""

PRESCOTT_DIED = """
On the record (sources in `docs/shortlist/check/prescott/README.md`):

1. **Handling and performance disappointed, early and publicly.** AOPA Pilot (1986) was briefed on a ground-effect pitch-up, found pitch "quite sensitive" at low speed, and noted "no aerodynamic warning" at the stall. Builders reported early lift-off and pitch oscillation from an aft CG ("Yes, we narrowed the CG envelope after that flight"), roll-off at lift-off, and hard rotation. Its first customer called it "somewhat of a ground hog". A retrospective puts it bluntly: "What ultimately killed the market for the Prescott Pusher, however, was the negative buzz generated after some early completions" (airplanezone, L).
2. **The layout's own consequence.** Wainfan: "A rear-engine airplane like the Prescott Pusher is very challenging aerodynamically because the flight CG is so far aft on the fuselage." That put the mains aft, which made rotation hard, and kept the gear short for propeller clearance, which forced a small, inefficient propeller.
3. **Financing and control.** Tom Prescott's own account (2007): "The original marketing grass-roots pay-as-you-go approach was elevated to a high-dollar pay-up-front strategy", and his and Stan Blankenship's key contributions "evaporated in the face of requirements demanded by the financial backer." He also says the delivered kits "had the essence but not all the aerodynamic and structural refinements envisioned or planned".
4. **Parts.** The first customer to fly started "as builder number 29 and I finished first–only because I kept dogging Prescott for parts" (Syracuse, 1989); "the Prescott team was much better at marketing than producing parts."
5. **The end.** In October 1988 Kitplanes reported the company "was being sold to an Australian outfit, which offered no plans about further development"; kit sales stopped in early 1989; SDASM says the company folded in 1991 with builders still completing aircraft. The second prototype was later registered to "Pusher Aircraft Inc", Wichita, until 2018: a lead for the rights work (passed to Elon).

**Does a revival fix it?** The business causes (parts, financing model), yes. The handling causes trace to the aft CG of an engine in the tail; a revival fixes them only by redesigning the balance (wing position, gear, forward fuselage) and flight-testing rotation and stall warning. That is engineering, not a kit-logistics fix.
"""

PRESCOTT_ROHR = """
Bill's two highest-interest designs may share a theme: a clean forward fuselage with the propeller at the back. **What the evidence shows:**

| | Prescott Pusher | Rohr 2-175 |
|---|---|---|
| Engine | In the tail cone right behind the cabin | Buried in the fuselage behind the seats |
| Drive | 12 in prop extension; no drive failure on record | Short extension shaft; redesigned for vibration; one coupling failure in flight |
| Propulsor | Open 65-68 in prop, marginal ground clearance | 40 in fan in a duct, enclosed |
| Planform | Conventional, AR 7.8, T-tail | Tailless delta, AR 2.2, elevons |
| Structure | Steel-tube cage, fibreglass shells, riveted aluminium wing | Sparless foam-core fibreglass stressed skin |
| Storage | 29.3 ft span, no folding | 20 ft span, outer wings and fin fold for a single-car garage |
| Seats, weight | 4 (really 2+2), 2,400 lb | 2, 1,450 lb |
| Cooling | Oil overheat fixed by moving the cooler; hot rear cylinder | Dorsal scoop and exhaust ejector; no overheating at 108 deg F |
| Takeoff and pitch | Pitch-sensitive in ground effect, aft CG, hard rotation | Dog-tooth added for pitch-up; few flights, no handling record to speak of |

**What they share is real, and it is mass at the back.** Both put the propeller behind a clean cabin, and both pay for it in balance: the Prescott's documented aft-CG handling and nose ballast, and the 2-175's scale-up limit (Study 1 of its dossier), where two rows of seats ahead of the engine strain a tailless wing's trim range. Both also had to work at cooling an engine with no propeller blowing over it. **Where they differ is everything else**: planform (the opposite ends of the aspect-ratio argument), propulsor (open prop with a clearance problem against a duct that removes it), structure and storage. So the configuration is a thread in its benefits (a clean, quiet cabin and a protected or short drive) and in its one shared problem (CG); the planform is not shared, and AER-3807 weighs that separately.
"""

NEW["prescott-pusher"] = dict(
    rank="2 of 6",
    results=["prescott-pusher"],
    bill='Bill, 2026-10-24: "Prescott Pusher should also be of high interest. This is possibly the top of my list as a target of interest." Moved to the top tier and given the full treatment.',
    verdict="""**Rank 2, top tier.** As published it passes speed (165 KTAS at 7,500 ft) and misses useful load by 150 lb (850) and range by about 130 nm (869 nm, reserve not stated). As measured it is weaker: the one weighed builder aircraft had 739 lb useful, and Kitplanes measured 151 KTAS at 73% at an unpublished altitude, which our model can reproduce only with a drag factor of 1.46-1.67 against the brochure's 1.35. On an AM20T it is fast (194-207 KTAS) but the engine's weight in the tail costs about 143 lb of useful load with ballast; **it clears all three floors on both drag bases only as a re-derivation**: about 2,700 lb gross, a structure about 100 lb lighter than today's would be at that weight, 90 gal, and the AM20T (1,077 lb, 1,112-1,172 nm, 194-204 KTAS). Its two great assets are a short 12 in prop extension instead of a drive shaft, and the best-preserved engineering record in the survey (SDASM SC.10269: drawings, loads report, wind-tunnel evaluation, structural tests). Its weakness is balance: a far-aft CG that made rotation hard and pitch sensitive, which a heavier engine in the tail makes worse. It ranks behind the Aries, which clears the floors on a straight engine swap, and ahead of the Express, because its engineering survives and it has no long shaft or known tail flaw.""",
    ideas=["**A pusher without a drive shaft.** Engine in the tail cone, prop on a 12 in extension: the clean forward fuselage and quiet cabin of a pusher without the VK-30's shaft risk. No drive failure is on record.",
           "**Build sequence for a home shop.** A welded tube cage with every system installed before non-structural fibreglass shells go on; shells from CAD-cut patterns. The plugs cost about a tenth of the $200,000 factory tooling (Sport Aviation 1986).",
           "**CAD/CAM from day one** (\"the first aircraft in its class totally designed using CAD/CAM\", SDASM), with stretch-formed leading edges on CAD-made dies: a 1980s preview of a digital kit.",
           "**An NLF(1)-0215F laminar wing** with reflexed flaps and ailerons, on a metal structure.",
           "**The archive.** Drawings, loads, wind-tunnel and structural test reports in a public museum collection: the strongest re-derivation basis in the survey (rights and use terms: attorney, per Elon).",
           "Lesson: put the CG, the main gear and the propeller clearance together first; an engine in the tail drives all three, and the Prescott's handling complaints trace to that.",
           "Lesson: a financing model that turned pay-as-you-build into pay-up-front, and parts that lagged marketing, lost the builders' trust before the airplane could earn it."],
    axes=f"""**Aspect ratio 7.8**: a conventional wing, on the high-aspect-ratio side of {PLANFORM_LINK}; the Rohr 2-175 is its opposite.

- **Storage.** 29.3 ft span, 20.3 ft long, 8 ft 9 in high: fits a 40 ft T-hangar door. The wings bolt on with two bolts per side at the root (Sport Aviation 1986), but no folding or quick removal is described.
- **Construction with home-shop tools.** A good fit. The 4130 square-tube cage is router-jig and welder work; the non-structural shells come off plugs, and plugs are what a home CNC router and a large-format printer can make in sections. The riveted aluminium wing used press-brake spars and stretch-formed leading edges on steel dies; the dies are a service job, the rest is home-shop sheet metal. Largest part a 14.7 ft half-wing; root spar about 8.2 in deep. Builders praised the fit of the sub-kits and found the fibreglass shell the worst job.
- **Safety.** Stall: "super gentle, with practically zero roll tendency" (Sport Aviation 1986) but with "no aerodynamic warning" (AOPA 1986, which saw stall strips being tried); full-stall landings end abruptly (Kitplanes 1988). Spin: never tested as far as the record shows. Takeoff pitch sensitivity and aft-CG lift-off are the documented hazard. Best L/D about 15.7 at 110 KTAS (propeller drag excluded). Pusher-specific events: a door that came off into the propeller (CEN09CA386), and a propeller that separated (LAX05LA270). Both fatal accidents were Ford V-6 conversions.
- **Ride comfort.** Gust dn 1.63 at 21.7 lb/ft2: in the rough half of the shortlist. AOPA (1986) found bumps took three to four pitch oscillations to settle. Cabin 42.5 in wide, "same as a Bonanza"; rear seats sit higher, on the carry-through; quiet enough at taxi for normal conversation (Sport Aviation 1986).""",
    extra_sections=[("Configuration in detail, and the fleet", PRESCOTT_CONFIG),
                    ("Published against measured: the 165 against the 151", PRESCOTT_GAP),
                    ("Where it lands on an Aeromomentum engine, and what moves it", PRESCOTT_LEVERS),
                    ("Why it died, properly", PRESCOTT_DIED),
                    ("The Prescott and the Rohr 2-175: is the configuration the thread?", PRESCOTT_ROHR)],
    engine="""- **AM20T** (260 hp; 195 hp assumed continuous): 194-207 KTAS at its critical altitude, but 61 lb heavier installed than the O-360, in the tail, which needs about 82 lb of nose ballast (E). See the levers table.
- **AM15T** (160 hp; 120 hp assumed continuous): 26 lb lighter, keeps useful load, cruises at the 160 KTAS floor.
- **Cooling:** liquid cooling would end the tail-cone air-cooling struggle, with a radiator inlet where the oil cooler went (the nose) or in the cone; not designed.
- **Propeller:** the geared Aeromomentum output and a constant-speed prop should recover some of the efficiency the short fixed-pitch prop lost; clearance still limits diameter.""",
    rights="""Open question (Elon, `docs/rights/prescott-pusher.md`, PR #6). No type certificate; a kit. The engineering record survives at the San Diego Air & Space Museum (Prescott Aeronautical Corporation Collection, SC.10269, open for research): the general-assembly drawing and well over a hundred part drawings including the prop extension, the basic loads report, a wind-tunnel evaluation, structural test reports, the pilot's manual and all kit manuals. Who owns the design rights is not known: the company stopped trading in 1989-1991, and no buyer or bankruptcy record has been found; the second prototype's later owner, "Pusher Aircraft Inc" of Wichita (registry to 2018), is a lead. Custody of papers is not ownership of copyright; an attorney is needed before any use. Reading the collection is museum contact, so Bill's call.""",
    safety="""Record (NTSB bulk databases and CAROL, plus foreign reports): 4 confirmed US events, 1 fatal (N58PP, 1990, a Ford V-6 conversion whose engine seized on its first flight, LAX90DUM02), and a probable fifth, also fatal and also a Ford V-6 (N75FM, 1990, CHI90DEE10). Two events are tied to the pusher layout: the cabin door came off in flight and struck the propeller (N19PP, 2009, CEN09CA386), and a wooden propeller separated in cruise (N43PP, 2005, LAX05LA270). One go-around ended in a pitch-up and stall (N747P, 1992, MIA92LA186) on an aircraft whose builder had reported pitch sensitivity and roll-off at lift-off. About 20 airframes with unknown hours: no rate is possible.""",
    died="See \"Why it died, properly\" above: early handling and performance disappointment tied to the aft CG of an engine in the tail, a financing change from pay-as-you-build to pay-up-front, parts that lagged marketing, and a sale abroad in 1988. A revival fixes the business causes directly and the handling causes only by redesigning the balance.",
    next="""- MANUFACTURING (AER-3784): the modern-structure empty-weight delta, which replaces our placeholders in the levers table.
- Kitplanes May 1988 in full (the 151 KTAS conditions), Flying (Oct 1985, Apr 1988) and Popular Mechanics (Aug 1986): not reachable online; a library or a purchased scan would settle the measured basis.
- Reading SDASM SC.10269 (the loads report, the wind-tunnel evaluation, the weight-and-balance schedule): museum contact, Bill's call. It would replace most of our estimates.
- A re-derivation sketch at about 2,700 lb with the CG, gear and propeller clearance laid out together (AERO, if it goes forward).""",
)
# re-rank: Aries 1, Prescott 2, Express 3, IV-P 4, Meyers 5, Mooney 301 6
NEW["bellanca-t250-aries"]["rank"] = "1 of 6"
UPDATES["express-2000"]["rank"] = "3 of 6"
UPDATES["lancair-iv-p"]["rank"] = "4 of 6"
NEW["meyers-200d"]["rank"] = "5 of 6"
UPDATES["mooney-301"]["rank"] = "6 of 6"
UPDATES["express-2000"]["verdict"] = UPDATES["express-2000"]["verdict"].replace("**Rank 2.**", "**Rank 3.**").replace("It ranks below the Aries because", "It ranks below the Aries and the Prescott because").replace("and because its rights are orphaned.", "because its rights are orphaned, and because the Prescott's engineering record survives where the Express's does not.")
UPDATES["lancair-iv-p"]["verdict"] = UPDATES["lancair-iv-p"]["verdict"].replace("**Rank 3.**", "**Rank 4.**")
NEW["meyers-200d"]["verdict"] = NEW["meyers-200d"]["verdict"].replace("**Rank 4.**", "**Rank 5.**")
UPDATES["mooney-301"]["verdict"] = UPDATES["mooney-301"]["verdict"].replace("**Rank 5.**", "**Rank 6.**")
