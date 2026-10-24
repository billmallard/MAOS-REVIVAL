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
