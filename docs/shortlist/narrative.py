"""Stage 3 narrative per shortlisted design, and the script that writes the
stage 3 block into each dossier in docs/candidates/.

  python3 docs/shortlist/narrative.py

The numeric tables come from check/results/<id>_stage3.md (report.py); the
prose below is AERO's reading of them and of the sources in check/geometry/.
Re-running replaces everything between the stage 3 markers and nothing else.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERE = os.path.dirname(os.path.abspath(__file__))
CAND = os.path.join(HERE, "..", "candidates")
START = "<!-- stage3:start -->"
END = "<!-- stage3:end -->"

N = {}

N["rutan-defiant"] = dict(
    status="dropped",
    bill='Bill, 2026-10-24: "no chance. Rutan has it and it\'s not what I\'m after." Dropped from the shortlist; the long-list row stays.',
    ideas=['Centreline thrust: two engines with no asymmetric-thrust or Vmc problem, the right answer when both engines are uncertified automotive conversions. The record shows no engine-out accident on about 30 aircraft.', 'A canard that protects the main wing from stalling, on a twin.'],
    rank="1 of 8",
    results=["rutan-defiant"],
    engine="""- **Power.** Two AM15T (160 hp each, 215 lb dry; grade F) replace two O-320s at 160 hp: the only design on the shortlist whose published power the Aeromomentum line matches directly. At the assumed 75% continuous rating that is 240 hp in cruise, the same as the brochure's 75% point.
- **Mass and CG.** Installed mass 2 x 304 lb against about 2 x 308 lb: -8 lb overall (E). Because the two engines sit at opposite ends, a revival can trim CG by choosing which installation carries the radiator. No ballast is expected, but it is not computed.
- **Cooling and installation.** Two liquid-cooled installations replace two updraft air-cooled ones that ran without cowl flaps. The rear engine's belly scoop overheated on at least one build (Twin & Turbine, 2026). A radiator in a ducted, Meredith-type installation is the obvious place to recover some of the 1.72 drag factor. That is not credited.
- **Props.** The plans forbade constant-speed props: the pilot cannot tell which engine has failed, and the aft prop risked fatigue (Rutan, Canard Pusher). A geared Aeromomentum engine changes the prop question, and the answer needs a design study, not an assumption.""",
    rights="""Open question, with a likely holder (Elon, `docs/rights/rutan-defiant.md`, PR #3, updated 2026-10-24). RAF sold its last plans and licensed its last builder in June 1985. **No 1985 rights buyer is on the record.** The one newsletter line that says rights "were sold" (Canard Pusher 54, 1988) is a reworded reprint of a 1985 paragraph that mentions no sale, and every other RAF and Rutan account says RAF stopped selling plans and kept its assets. The likely holder is therefore Rutan Aircraft Factory or Burt Rutan; that is an inference, not a document. What the holder owns is thin: the plans copyright (Fred Keller, who drew the homebuilder plans for a share of sales, may hold an interest), no type certificate, no live patent, no molds (moldless construction), and not the DEFIANT name, which Sikorsky and Lockheed Martin hold for aircraft. RAF called its end of licensing "final, official and irrevocable" (Canard Pusher 71), and Rutan wrote in February 2025 that he objects to unlicensed building from "bogus plans". So there is one identifiable, living party to approach, and his stance is on the record. The prototype N78RA is at the Hiller Aviation Museum. An attorney is needed on who holds the rights and on the Keller interest. Approaching anyone needs Bill's go-ahead.""",
    safety="""Record (ASN and NTSB, lower bound): 6 US NTSB events 1997-2018 and 2 fatal, worldwide, on about 30 completed aircraft (about 20 active). The recurring item is the retractable nose gear: landings with it up or unlocked, and a collapse. RAF issued a mandatory nose-gear change in 1987 after three retract-link failures. One fatal accident was an aborted-takeoff overrun on a 2,160 ft turf strip; the NTSB quoted the owner's manual on the high wing loading needing longer runways. The other was a loss of control after a go-around, cause undetermined, with no engine anomaly. **No engine-out or asymmetric-thrust accident is on record**, which is the configuration's point. Sample too small for a rate.""",
    died="""The 1979 certification programme lost its financing, and RAF stopped selling all plans in 1985 over liability. Neither applies to an experimental revival with a modern builder-support model. What does carry over: about 30 were completed from 176 plans sets, so the build was hard, and a revival has to fix that through manufacturing (stage 4).""",
    verdict="""**Rank 1.** It is the only direct Aeromomentum fit, gives twin redundancy for uncertified engines with no Vmc problem, has a clean record, and died for reasons a revival removes. Its weakness is drag. The published numbers say it is 1.7 times draggier than its geometry, so its payload at 1,000 nm with a 45 min reserve is cannot to 669 lb at 178-190 KTAS, and 807-821 lb at 150-159 KTAS. Its geometry is also the thinnest-sourced of the top four: the canard, chords and fuselage section are all estimates.""",
    next="""- Confirm whether RAF or Burt Rutan holds the rights, and whether Keller has an interest (attorney via Elon; any approach is Bill's call).
- Measure N78RA at the Hiller museum (canard, chords, cowls) if Bill approves contact; it would replace most of the estimated geometry.
- A drag study of the two cooling installations and the prop question (AERO, if it goes forward).
- The modern rebuild's empty weight (MANUFACTURING, stage 4): the plans prototype's 1,600 lb is the only figure.""",
)

N["lancair-iv-p"] = dict(
    rank="2 of 8",
    results=["lancair-iv-p"],
    engine="""- **Power.** The AM20T (260 hp take-off, 195 hp assumed continuous) replaces a 350 hp TSIO-550 that cruises at 262 hp. Our check gives 200 KTAS at 8,000 ft (low case) and 211 KTAS at 16,000 ft (high case), against 255 KTAS at FL230 on the original engine at our fleet calibration. Without a real critical altitude for the AM20T, no FL200+ credit is taken.
- **Mass and CG.** The installed mass falls by about 242 lb (E). That weight is in the nose of a tractor with a 36 lb/ft2 wing loading, so it has to come back as ballast or as a longer engine mount. The headline useful load (1,350 lb) takes no credit for the saving; the 1,592 lb optimistic figure takes all of it. Neither has been checked against a real weight-and-balance.
- **Climb.** At 3,550 lb, about 195 hp continuous is roughly 55% of the power the airframe was designed around. Climb rate and high-density-altitude take-off will fall by much more than cruise speed. That is not computed here, but a revival has to quantify it.
- **Cooling and installation.** A liquid-cooled engine and radiator replace an intercooled twin-turbo air-cooled installation that already ran hot in climb (Kitplanes 2019). The cowl is built around a flat six; a new nose is a stage 4 item.""",
    rights="""Open question: chain of title (Elon, `docs/rights/lancair-iv-p.md`, PR #3, updated 2026-10-24). In February 2017 Lancair International Inc. sold all out-of-production kit lines, including the IV and IV-P, with "all assets, intellectual designs and ongoing support business" (company announcement, https://lancair.com/lancair-international-inc-announcing-sale-production-assets-lancair-brand-kit-components-support-assets-new-ownership-based-uvalde-texas/) to Lancair International LLC (Uvalde, TX). In October 2023 JetEXE Aviation (Sacramento) bought the Lancair kit business from the Uvalde owners. **No public source lists what that purchase covered** (an earlier version of this dossier repeated a misquotation saying it included molds and IP; it did not, and is withdrawn). The Texas LLC is still active, so whether JetEXE or the LLC holds the IV-P design is open. The molds have no known location since Uvalde in 2017. Owner-forum posts (low grade) report a legal dispute between the parties and call Lancair "effectively defunct" as of April 2026 (https://www.lancairlive.com/viewtopic.php?p=799); no federal case was found, and Texas state courts were not searched. The company trades as Lancair Aerospace, says the IV-P kit is out of production, and offers parts and service bulletins. "LANCAIR" is a live mark held jointly by JetEXE and Akyna Medical Management. Lancair has licensed a design before (the Calima T-90). So it remains a licence-or-purchase candidate, but **chain of title comes before price**, and an attorney is needed for it. Approaching anyone is Bill's call.""",
    safety="""Record (NTSB bulk databases, our own count of IV-family model strings, 1995-2026): 88 accidents, 43 fatal (49%), 79 killed, on about 360 completed aircraft. Fatal accidents fell from 19 in 2008-2016 to 3 in 2017-2026, which is consistent with the owners' group training push. The NTSB causes in the fatal accidents fall into two big groups. About 13 are low-altitude loss of airspeed or stall-spin on take-off, climb-out, go-around or manoeuvring. About 13 more begin with an engine power loss, often followed by a stall. Weather with structural overload accounts for about 7. **Inference, labelled as such:** the stall-spin group is consistent with a high wing loading and a small wing with a 66 KIAS stall (CAFE). Lower power does not change that, and lower power makes a go-around weaker.""",
    died="""Kit production ended in 2012, and the company sold its older lines in 2016-17 to concentrate on newer designs. That was not a market failure; about 360 were built. A revival therefore does not fix a cause of death. What it would have to fix is the accident pattern, through the wing (the 2019 RDD LX7 rework already offers a new airfoil with double-slotted flaps on the same area), training, and the engine-failure chain.""",
    verdict="""**Rank 2.** It is the strongest airframe that physically survives: 200-211 KTAS on 195 hp and 824 lb over 1,000 nm with reserve in the high case, about 235 aircraft on the register to measure, and parts support still offered. Who could license or sell the design is open: the scope of the 2023 sale is not public and the molds are unlocated. That still leaves it ahead of the Mooney 301, where nothing survives at all, and the VK-30, whose holder is large and firmly set. It ranks below the Defiant for three reasons: the worst fatal record in the survey, a power cut of nearly half its design power, and about 240 lb of nose ballast to find. Its published 278 KTAS reads 8% optimistic against the fleet calibration.""",
    next="""- Chain of title: what JetEXE bought in 2023, whether the Texas LLC still holds the IV-P design, and where the molds are (Elon, then an attorney; contact is Bill's call).
- If it goes forward: a SAFETY review of the stall-spin pattern, asked on AER-3785 first.
- A climb and take-off check at 195 hp, and a weight-and-balance with the lighter engine (AERO).
- Builder-fleet empty weight: two weighed aircraft (2,140 and 2,200 lb) are all we have.""",
)

N["mooney-301"] = dict(
    rank="3 of 8",
    results=["mooney-301"],
    engine="""- **Power.** The AM20T at 195 hp assumed continuous replaces a 360 hp TIO-540 cruising at 270 hp. That gives 176-187 KTAS: above the 160 KTAS floor, below the 180 preferred in the low case.
- **Mass and CG.** The installed mass falls by about 207 lb (E), in the nose of a tractor. The headline useful load takes no credit for it.
- **Cooling.** The 301 used a deliberately tiny LoPresti-style low-drag inlet. A radiator needs its own duct, so the cooling-drag allowance here is a placeholder.
- **Altitude.** The 301 was a pressurised design aimed at FL250. Without a critical altitude for the AM20T, pressurisation buys nothing in our check, and its weight is carried for no speed. A revival on this engine might be unpressurised, which changes the structure (stage 4).""",
    rights="""Open question (Elon, `docs/rights/mooney-301.md`, PR #3). There is no type certificate. The one airframe (N301MX, registration cancelled 1989) was scrapped: its wings were cut off and the rest went to an A&P school in Abilene, Texas. All M30 engineering data went to Socata at Tarbes in 1987 under a joint venture. Mooney International (successor to the developer) and Daher (successor to the joint-venture partner) may both claim it. The joint-venture terms and the lawsuit settlement are not public, and no court record of the dispute was found. **Unresolved on the public record, and nothing usable survives on either path** (Elon, updated 2026-10-24): no type certificate, no patent (any from the era expired by about 2012), no airframe, and no known drawing set outside whatever Daher kept in Tarbes or Mooney kept in Kerrville. The realistic route is a new design that takes the 301's layout as a reference, with counsel on how close is too close to TBM-protected data.""",
    safety="""Record: no NTSB or other accident record; one prototype, about 70 h in 1983, plus Socata data flights. First-hand flight-test account (Bob Kromer, Mooney test pilot, Mooney Flyer, October 2012, https://themooneyflyer.com/issues/2012-OctTMF.pdf): with rapid inputs in gusty air on approach, pitch authority became "almost non-existent". He blamed the inverted-section one-piece stabilator and called it "certainly not certifiable"; a conventional tail was recommended and never fitted. Sources disagree on the tail layout (Wikipedia describes a fixed stabilizer with elevators); we kept the test pilot's account. **Inference:** a tail redesign would fix it, but any revival treats the tail as unvalidated. No fleet, no rate.""",
    died="""Republic Steel's takeover by LTV forced the sale of Mooney. The new French-led owners judged the 301 about 200 lb heavy and too slow, and wanted a 300 kt turboprop, which became the TBM 700. The market gap it was aimed at, a fast six-seat piston single, is real and is still open. But nothing survives to revive except published dimensions: a revival would be a new design that takes the 301 as its starting point.""",
    verdict="""**Rank 3.** It has the best payload-range on our numbers (858-867 lb over 1,000 nm with reserve) and is the only six-seater close to the mission. It ranks third because there is nothing to revive but published dimensions, the rights are an attorney question, the tail is known-bad, and its published speed reads 9% optimistic against the fleet calibration.""",
    next="""- The attorney question on Mooney or Daher (Elon, then Bill).
- Primary geometry: Jane's 1983-84 and Air International January 1984 were read only as quoted. A library copy would replace our estimated chords and tail areas.
- If it goes forward: what an unpressurised six-seat derivative weighs (MANUFACTURING).""",
)

N["cirrus-vk-30"] = dict(
    status="dropped",
    bill='Bill, 2026-10-24: "no thanks". Dropped from the shortlist; the long-list row stays.',
    ideas=['A laminar composite wing on a clean pusher fuselage: the fastest result on our check (199-212 KTAS on an assumed 195 hp).', 'Lesson for any buried-engine pusher, the Rohr 2-175 included: three of its five fatal accidents trace to the shaft drive, a flutter-prone cruise flap and spin recovery at aft CG. A shaft and its couplings must be designed and tested as primary structure.'],
    rank="4 of 8",
    results=["cirrus-vk-30"],
    engine="""- **Power.** The AM20T at 195 hp assumed continuous replaces a 290-300 hp IO-540 or IO-550 cruising at about 200 hp. On a low-drag pusher that gives 199-212 KTAS: the fastest result on the shortlist.
- **Mass and CG.** The installed mass falls by about 121 lb (E). The engine sits behind the cabin over the wing, so the CG moves forward; the headline useful load takes no credit for the saving.
- **Installation.** The prop sits at the tail cone on a roughly 6.5 ft shaft. A geared Aeromomentum engine still needs that shaft and its couplings, and the 2018 fatal accident was a coupling failure. The liquid cooling replaces side scoops and a fan. The second prototype, which had a V-8 automotive engine, had radiator cooling problems and burned in flight (Klapmeier history).""",
    rights="""Firmly held (Elon, `docs/rights/cirrus-vk-30.md`, PR #3). There is no type certificate; it was a kit only. The seller was Cirrus Design, now Cirrus Aircraft, listed in Hong Kong in 2024 and about 85% held by CAIGA, itself about 73% AVIC-owned. No public record says who holds the drawings, molds or tooling; the default assumption, not a finding, is the Cirrus group. "CIRRUS" is a live mark. Two remain on the register, one of them in the EAA museum. Elon's verdict on a direct path: unlikely.""",
    safety="""Record (NTSB bulk databases, own count): 7 accidents, 5 fatal, 10 killed, on about 13 completed aircraft. The fatal causes were: fuel starvation after a builder fuel-system change (1994); failure to recover from an aft-CG spin during stall testing of new wings (1996), where the NTSB cited inadequate handling design and no anti-spin provision; right-wing flutter after a cruise-flap bracket failure from an incomplete bond cure and wrong hinge material (1996); a forced landing after a ruptured oil line (2007); and an in-flight driveshaft fracture after coupling nuts backed off, with the flailing shaft knocking off the tail fairing, killing four (2018). In 1996 Cirrus recommended grounding all VK-30s pending new wings. **Inference:** three of the five fatal accidents (shaft, flap flutter, spin) trace to the design or the configuration, not only to builders.""",
    died="""The founders' own verdict was "we failed as kitmakers". The kit was too complex, so they went to Part 23 certification with the SR20 and bought back about three-quarters of the outstanding kits. A revival fixes that only if the shaft drive, the cruise flap and spin recovery are redesigned, which makes it a new airplane on the VK-30's lines.""",
    verdict="""**Rank 4.** It has the fastest result on our numbers (199-212 KTAS, 815-825 lb over 1,000 nm with reserve). It ranks fourth because the holder is a large, state-controlled company to which it is history, and because its accident record is tied to the very features (shaft drive, flap, spin) a revival would inherit.""",
    next="""- Nothing, unless Bill wants to test whether Cirrus would release it (contact is his call).
- If it goes forward: a SAFETY review of the shaft-drive and flutter accidents, asked on AER-3785 first.""",
)

N["velocity-xl-rg"] = dict(
    status="dropped",
    bill='Bill, 2026-10-24: "no chance." Dropped from the shortlist; the long-list row stays.',
    ideas=['A canard pusher with a real cabin (four or five seats, gull-wing doors), sold continuously as a kit since the 1980s.', "**The Raptor (a lesson, not a Velocity product).** Peter Muller's Raptor Aircraft (about 2013-2021) tried to scale the Velocity-type canard pusher into a pressurised five-seater on his own Audi 3.0 TDI diesel conversion. It promised 300 KTAS at FL250 for about $130,000, and took about 1,500 escrowed $2,000 deposits (archived raptor-aircraft.com specs page, F; Aero-News, P). The prototype came out \"well over 800 pounds heavier than its design weight\" (Aero-News, P): its weighing video showed 3,144 lb empty (as cited by Wikipedia, L) against the 2,300 lb estimated empty weight on its archived specs page (F). Wikipedia's own figure for the overage, 1,344 lb, implies an earlier, lower estimate. Its first real flight, on 10 October 2020, lasted about three minutes, with pitch and lateral oscillations and the powerplant near its temperature limits (Aero-News, P). The engine failed in February 2021 (L). A reduction-drive failure put it in a Nebraska cornfield in August 2021 (N352TD, registration cancelled 2022; Aero-News, P; FAA registry, B). No link to Velocity Inc. was found. **What it teaches:** weight control, an engine and reduction drive proven before the airframe, and professional flight test. Those are the risks an Aeromomentum installation carries too. Sources: https://www.aero-news.net/index.cfm?do=main.textpost&id=39a13f1f-1ad0-4979-9371-e4644989ce85 ; https://www.aero-news.net/index.cfm?do=main.textpost&id=86ec99b2-5784-4217-8b71-22dc71e07bb1 ; https://web.archive.org/web/20200201043759/http://www.raptor-aircraft.com/specs.html ; https://en.wikipedia.org/wiki/Raptor_Aircraft_Raptor"],
    rank="5 of 8",
    results=["velocity-xl-rg", "velocity-xl-rg-100gal"],
    engine="""- **Power.** The AM20T at 195 hp assumed continuous replaces a 260-310 hp IO-540 or IO-550 (stage 1 matched the 260 hp build). That gives 186-199 KTAS.
- **Mass and CG.** The installed mass falls by about 104 lb against an IO-550 (E). That is a tail-mounted engine on a canard, where CG range is critical; the headline useful load (1,000 lb) takes no credit for the saving.
- **Fuel.** On the standard 70 gal it cannot fly 1,000 nm at continuous power, even with no reserve. With the factory's optional 100 gal it carries 440-457 lb with a reserve. Every pass here assumes the optional tanks.
- **Cooling.** The radiator has to fit a pusher cowl that already has inlets sized for a flat six; not studied.""",
    rights="""Firmly held (Elon, `docs/rights/velocity-xl-rg.md`, PR #3): not an orphan. Velocity, Inc. (Sebastian, FL; the Swing family since 1992, apart from 2008-2010) still sells the XL in fixed and retractable forms, holds the molds and supports the fleet. About 700 Velocities fly, and the factory makes 12-15 kits a year (Kitplanes 2020). No live VELOCITY aircraft mark was found. Nothing here is free to take; an Aeromomentum-engined XL would be a partnership with a live company.""",
    safety="""Record (NTSB CAROL, XL-family model strings): 26 events, 5 fatal, 9 killed, on about 229 completed aircraft. The causes are mostly landing-phase control and gear-up or collapsed-gear landings, fuel, engine maintenance, weather and one runway collision. Two items are tied to the configuration. An unlatched passenger door separated and struck the rear engine and prop, killing two (WPR10LA381). And the NTSB found inadequate manufacturer design of the winglet-rudder assembly and its metal-to-composite bond, which caused control-surface flutter (ATL01LA029, non-fatal). One XL-RG departed controlled flight during a self-planned stall test, cause undetermined.""",
    died="""It did not die. It is in production. So no revival is needed, and none fixes anything.""",
    verdict="""**Rank 5.** It is a live kit with a near Aeromomentum fit, but it reaches 1,000 nm only on optional tanks, and then with 440-457 lb of payload. Its published speed needs a 1.63 drag factor, but that rests on one point and on geometry we had to scale from the Cozy; the factory's own wing figures conflict with Jane's. Low confidence in both directions.""",
    next="""- Resolve the XL wing and canard dimensions (factory 34 ft / 132.5 ft2 against Jane's 31 ft / 102 ft2).
- A measured cruise point at altitude would replace the single 3,000 ft pilot-report point.""",
)

N["express-2000"] = dict(
    rank="6 of 8",
    results=["express-2000"],
    engine="""- **Power.** The AM20T at 195 hp assumed continuous replaces the 210 hp IO-360-ES of the CAFE aircraft (later builds used 260-300 hp). That gives 179-191 KTAS.
- **Mass and CG.** About +11 lb installed (E). The headline useful load is the CAFE-weighed aircraft's 901 lb less that, 890 lb.
- **Cooling.** CAFE found the stock installation overheated at the published climb speed, and had to climb at 95-98 kt indicated. A liquid-cooled installation could fix that, but it is not computed.""",
    rights="""Open question (Elon, `docs/rights/express-2000.md`, PR #3). It was always a kit. The design passed through at least five owners, three of them through bankruptcy: Wheeler Technology, Express Design Inc., Express Aircraft Co. LLC, Exosphere Aircraft Co., and Composite Aircraft Technology LLC, which bought the assets out of bankruptcy court in September 2007. There is no public trace of CAT after about 2010, and its domain now serves an unrelated site. The old EXPRESS mark was cancelled in 2001. This is the most orphaned design on the shortlist.""",
    safety="""Record (ASN with NTSB numbers, lower bound): at least 17 US NTSB events and 13 fatal accidents worldwide (21 killed), on about 55 active aircraft. About 9 of the 13 fatal accidents are stall or loss of control. In 2015 the NTSB named "the airplane's design, which resulted in poor yaw stability at low airspeed" as a contributing factor, citing the CAFE test (CEN15FA321). CAFE itself found low yaw damping, an uncommanded right yaw after clean stalls, and fin blanking. The 1990 demonstrator crash that ended the company was a spin (SEA90FA146). **Inference:** several of the stall fatalities were big-tail Series 90/2000 aircraft, so the larger tail apparently did not fix it.""",
    died="""The 1990 fatal crash of the second demonstrator on its way to Oshkosh collapsed sales and bankrupted Wheeler; two successor companies also failed. A revival would have to fix the directional stability first: a new tail designed and flight-tested, not a bigger copy.""",
    verdict="""**Rank 6.** It has the best evidence on the shortlist (CAFE flight test, a weighed aircraft) and is the most orphaned. On our numbers it misses: 890 lb useful, and it cannot carry a 45 min reserve over 1,000 nm at continuous power (439-445 lb at economy power, 149-157 KTAS). And it has a tail the NTSB has named.""",
    next="""- Trace Composite Aircraft Technology's 2007 assets through public records (Elon).
- Nothing more from AERO unless Bill wants a tail study.""",
)

N["berkut-360"] = dict(
    status="dropped",
    bill='Bill, 2026-10-24: "not likely. These were expensive to build." Dropped from the shortlist; the long-list row stays.',
    ideas=['Molded carbon and glass parts that took the Long-EZ shape to a retractable 200 kt class two-seater.', "Lesson: over 100 molded parts made the kit expensive to build (Bill's reason) and left the design hostage to its molds, which are now lost."],
    rank="7 of 8",
    results=["berkut-360"],
    engine="""- **Power.** The AM20T at 195 hp assumed continuous replaces a 205 hp IO-360 (most builders chose a 260 hp IO-540). Stage 1 called it a direct fit.
- **Mass and CG.** About +16 lb installed (E), in the tail of a canard. Not checked.
- **Speed.** Our model is not credible here (see below), so no Aeromomentum speed is claimed.""",
    rights="""Open question (Elon, `docs/rights/berkut-360.md`, PR #3). The chain runs from the Ronneberg-Murphy partnership, to Experimental Aviation Inc. (bankrupt), to Renaissance Composites (1996), to Vicki Cruse's Berkut Engineering and Design (2001), which withdrew the kit in 2002. Cruse died in 2009, and who holds the molds (over 100 molded parts by 2002) is not on any public record. The designer, Dave Ronneberg, is active and owns two related aircraft. There is no BERKUT mark.""",
    safety="""Record (NTSB CAROL plus registrations filed under builder names): 9 events, 2 fatal, on about 31 aircraft. The fatal accidents were an accelerated stall in a high-g airshow turn (the prototype, 1995) and an in-flight canard separation because the builder never fitted the attach bolts (2002). The rest are builder errors and retractable-gear failures. The NTSB found no deep stall, rain-on-canard or pusher prop strike. The canard is a bolt-on surface whose missing attachment was fatal.""",
    died="""Lawsuits between the founding partners bankrupted both, later owners did not last, and the kit was withdrawn in 2002 for drone work. A revival fixes that if the molds can be found; it is a business failure, not a design one.""",
    verdict="""**Rank 7.** It is the only two-seater on the shortlist, and it cannot be checked. No measured performance exists, and its wing area is unsourced. Our fleet-calibrated model gives 239 KTAS on 195 hp, faster than the designer's own 191 KTAS cruise claim, which says the geometry is wrong. On weight and fuel alone: 949 lb useful, and 1,000 nm only at economy power (608-616 lb with reserve). Its range and payload are grade E.""",
    next="""- Primary geometry and one measured cruise point; nothing else changes this rank.
- Trace the molds (Elon).""",
)

N["cessna-p210n"] = dict(
    rank="8 of 8 (calibration case)",
    results=["cessna-p210n"],
    engine="""- **Power.** The AM20T at 195 hp assumed continuous replaces a TSIO-520-P at 285 hp maximum continuous (TCDS 3A21). That gives 161-171 KTAS: just above the floor.
- **Mass and CG.** The installed mass falls by about 161 lb (E), in the nose; no credit is taken.
- **Fuel.** At continuous power it cannot fly 1,000 nm on 89 gal, even with no reserve. At economy power it carries 1,132-1,142 lb with reserve, but at 130-132 KTAS, below the speed floor.
- **Path.** A re-engine would be an STC on a certified type, not a revival. The engine is uncertified, which is a certification question outside this survey.""",
    rights="""Firmly held (Elon, `docs/rights/cessna-p210n.md`, PR #3). TC 3A21 (Rev 50) is current and held by Textron Aviation, which supports the fleet. 418 piston P210Ns are on the US register. Modifying existing airframes under STCs is proven (the Silver Eagle turbine conversion). Building new ones from data that is not ours is an attorney question.""",
    safety="""Record (NTSB CAROL, P210 model strings, 1978-2026): 291 accidents, 78 fatal events, 162 killed; US only 68 fatal and 139 killed; 874 built. Our keyword screen and reading of the fatal accidents, not NTSB-coded findings: about 36 involve weather, IMC, night or icing, about 11 are engine mechanical failures (mostly oil-system and maintenance), 5 are fuel exhaustion or starvation, and 2 are engine-compartment fires. Gear-up or collapse appears in 53 records, mostly non-fatal. The record includes the 1980 detonation crashes that led to rich-mixture ADs and a 1981 turbo retrofit.""",
    died="""Cessna ended piston production in 1986, in the product-liability era, and the P210R sold only about 40 against the Malibu. The market did not reject the design. But it is a live, firmly held type certificate, not something to revive.""",
    verdict="""**Rank 8.** It is here to calibrate the method. Seven POH points match the build-up with factors of 1.26-1.32, tight enough to anchor the fleet calibration. As a candidate it fails on the AM20T: 161-171 KTAS, and it cannot reach 1,000 nm at continuous power.""",
    next="""- None for the survey. It remains the calibration case if the method changes.""",
)

N["cozy-mkiv"] = dict(
    rank="reference",
    results=["cozy-mkiv"],
    engine="""- **Power.** The AM20T at 195 hp assumed continuous replaces a 180 hp IO-360, so it gains power. Our check gives 202-217 KTAS.
- **Mass and CG.** The installed mass rises about 63 lb (E), in the tail of a canard. Useful load falls from 871 lb (CAFE-weighed) to 808 lb, and the aft CG moves the wrong way for a type whose owner's manual warns it "could become locked in" aft of the limit.
- **Fuel.** At 195 hp the 50.7 gal usable gives only 645-668 nm. The Cozy cannot fly 1,000 nm on this engine at any setting we computed.""",
    rights="""Firmly held (Elon, `docs/rights/cozy-mkiv.md`, PR #3). Aircraft Spruce has held exclusive rights since 2004, claims US copyright, sells plans with a one-airplane licence, and the licence bars using the drawings to design another aircraft. Not a revival target; it is the yardstick.""",
    safety="""Record (NTSB CAROL, Mark IV): 22 events, 7 fatal, 12 killed, on about 350 built. Powerplant and fuel dominate. Two items are tied to the configuration. The belly landing brake, deployed in flight, blocked engine airflow and caused total power loss twice. And on two aircraft a main-wing stall would not break, both traced by the NTSB to building outside the plans (canard incidence, removed vortilons, aft CG).""",
    died="""It did not die. It is the reference.""",
    verdict="""**Reference.** On our check it fails harder than the published record. The CAFE-weighed empty weight is 1,179 lb, giving 871 lb useful, not 1,000. On its IO-360 it does 175 KTAS at 8,000 ft and 829 nm on full usable fuel with no reserve, so it cannot carry any payload over 1,000 nm. Every shortlisted design except the Berkut beats it on payload at 1,000 nm.""",
    next="""- None; it stays the yardstick.""",
)


# Revision 2 (after Bill's review, 2026-10-24): updates, additions, new ranks.
from narrative_rev2 import UPDATES, NEW  # noqa: E402
for _k, _v in UPDATES.items():
    N[_k].update(_v)
N.update(NEW)


def like_for_like(i):
    """Published, measured and our check side by side (brief, amended
    2026-10-24): compare published-to-published and measured-to-measured."""
    import json
    import sys
    sys.path.insert(0, os.path.join(HERE, "..", "longlist"))
    import screen as S
    cands = {c["id"]: c for c in json.load(open(os.path.join(HERE, "..", "longlist", "candidates.json")))}
    c = cands.get(i)
    rp = os.path.join(HERE, "check", "results", i + ".json")
    if c is None or not os.path.exists(rp):
        return []
    r = json.load(open(rp))
    P, M = S.screen_col(c, "pub"), S.screen_col(c, "meas")
    o = r["orig"]
    m = json.load(open(os.path.join(HERE, "check", "models", i + ".json")))
    ul_chk = m["weights"]["mtow"] - m["weights"]["empty"]

    def spd(col):
        if col["spd"] is None:
            return "not found"
        return (f"{col['spd']:.0f} KTAS at {S.fmt(col['alt'], ' ft') if col['alt'] else 'altitude not stated'}"
                f" ({col['spd_s']})")

    def rng(col):
        return "not found" if col["rng"] is None else f"{col['rng']:,.0f} nm ({col['rng_s']}; {col['rng_note']})"

    def ul(col):
        return "not found" if col["ul"] is None else f"{col['ul']:,.0f} lb ({col['ul_s']})"
    return [
        "### Published, measured and our check, side by side", "",
        "Read across a row only within one column's basis. The three targets are separate floors.", "",
        "| | As published | Measured or reported | Our check, original engine |",
        "|---|---|---|---|",
        f"| Useful load | {ul(P)} | {ul(M)} | {ul_chk:,.0f} lb (the empty weight the model uses: {m['weights']['empty']:,} lb) |",
        f"| Range | {rng(P)} | {rng(M)} | {o['range_nm_noreserve_fullfuel_mtow']:,.0f} nm, still air, no reserve, full fuel from MTOW, at {o['hp']:.0f} hp and {o['alt_ft']:,.0f} ft |",
        f"| Cruise | {spd(P)} | {spd(M)} | {o['ktas']:.0f} KTAS at {o['hp']:.0f} hp and {o['alt_ft']:,.0f} ft |",
        f"| Screen | {P['overall']} | {M['overall'] if S.cell(M) != '-' else 'no measured data'} | see the verdict |",
        "",
    ]


def block(i):
    n = N[i]
    st = n.get("status", "ranked")
    if st == "dropped":
        head = "## Stage 3: checked, then dropped from the shortlist by Bill (2026-10-24)"
    elif st == "study":
        head = "## Stage 3: studies, not ranked (AER-3783)"
    elif st in ("calibration", "reference"):
        head = f"## Stage 3: {n['rank']} (AER-3783)"
    else:
        head = f"## Stage 3: shortlist rank {n['rank']} (AER-3783)"
    parts = [START, "", head, "",
             "Our own check, from published geometry and weights, calibrated against "
             "published flight data. Method, calibration and the Aeromomentum "
             "assumptions are in [docs/SHORTLIST.md](../SHORTLIST.md). Rights are "
             "research, not legal advice. Nobody has been contacted.", ""]
    if n.get("bill"):
        parts += ["### Bill's call", "", n["bill"], ""]
    parts += ["### Verdict" + (" (stage 3, before Bill's review)" if st == "dropped" else ""), "",
              n["verdict"], ""]
    if n.get("ideas"):
        parts += ["### Idea ledger (what a new airplane should keep)", ""]
        parts += [f"- {x}" for x in n["ideas"]] + [""]
    parts += like_for_like(i)
    if n.get("axes"):
        parts += ["### The deep-dive axes: storage, home-shop construction, safety, ride", "", n["axes"].strip(), ""]
    for k in n.get("extra_sections", []):
        parts += [f"### {k[0]}", "", k[1].strip(), ""]
    for r in n["results"]:
        snip = open(os.path.join(HERE, "check", "results", r + "_stage3.md")).read()
        title = "Independent performance check" + (
            " (optional 100 gal tanks)" if r.endswith("100gal") else "")
        parts += [f"### {title}", "", snip.strip(), ""]
    parts += ["### Engine fit with the Aeromomentum line", "", n["engine"], "",
              "### Rights and provenance (stage 2)", "", n["rights"], "",
              "### Safety record", "", n["safety"], "",
              "### Why it died, and whether a revival fixes it", "", n["died"], "",
              "### Not yet done", "", n["next"]]
    if st != "dropped":
        parts += ["- What a modern rebuild changes in mass, cost and build hours "
                  "(MANUFACTURING, stage 4, AER-3784)."]
    parts += ["", END]
    return "\n".join(parts)


def main():
    for i in N:
        p = os.path.join(CAND, i + ".md")
        s = open(p).read()
        b = block(i)
        if START in s:
            s = s[:s.index(START)] + b + s[s.index(END) + len(END):]
        else:
            k = s.find("## Not yet done")
            if k < 0:
                s = s.rstrip() + "\n\n" + b + "\n"
            else:
                s = s[:k] + b + "\n"
        s = s.replace("Stage 1 stub, generated from",
                      "Stage 1 stub (extended in stage 3 below), generated from", 1)
        open(p, "w").write(s)
        print("wrote", p)


if __name__ == "__main__":
    main()
