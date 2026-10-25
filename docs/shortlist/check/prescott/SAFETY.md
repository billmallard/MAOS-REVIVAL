<!--
Committed by AERO from SAFETY's issue document `safety-review` on AER-3899:
revision 1 (83b16d6e-6366-4649-95ba-09a5bfa7f0f8), 2026-10-25, via AER-3902;
revision 2 (57224195-5287-40c3-9d53-b43ea99eb809), 2026-10-25, via AER-3903,
which appends the addendum at the end and leaves revision 1's text unchanged.
SAFETY has no write grant on this repository. Everything below the line is
SAFETY's text, unedited: the verdicts, constraints R1-R10 and the addendum are
verbatim. AERO's response to section 1 (the input corrections) is in
balance.py, balance_output.md and the dossier, docs/candidates/prescott-pusher.md.
-->

> **Provenance.** SAFETY's review, committed verbatim by AERO. Sections 1-6 judged the numbers in PR #10 as first opened. Section 1's three corrections were then taken into `balance.py` (AER-3902; see [balance_output.md](balance_output.md), section 2, correction ledger), and SAFETY re-reviewed the corrected numbers in the **addendum at the end (revision 2), which governs where it differs from sections 1-6**.

---

# Prescott Pusher revival: safety review of aft-CG handling and the approach and landing technique (AER-3899)

SAFETY, 2026-10-25. This is a desk review of AERO's balance study (MAOS-REVIVAL PR #10, branch `aero/aer-3866-prescott-balance`: `docs/candidates/prescott-pusher.md`, `docs/shortlist/check/prescott/balance.py`, `balance_output.md` and the folder README). Bill approved it on 2026-10-25. It covers the Prescott only. Nobody outside the board was contacted.

**Basis.** The Prescott revival would be Experimental Amateur-Built, so no certification standard applies. Where I mention a Part 23 or ASTM figure, it is a borrowed engineering yardstick. It is not a requirement, and I have not read any of the ASTM standards. Every number marked E is an estimate (mine, or AERO's where I say so), and it moves if its inputs move. I re-fetched each quoted passage below from its source on 2026-10-25. The one exception is CEN09CA386, where the NTSB server returned 403; that quote is AERO's.

## Verdict in one paragraph

None of the four balance options makes this airplane safe on its own, because balance only fixes where the CG sits. The documented hazards come from three other things: very little stability margin at the aft limit, pitch that couples to power through a thrust line well above the CG, and a propeller and tail cone that stop the pilot from flaring to a normal attitude. Options A and B are acceptable with mitigation. Option C is acceptable only if its neutral-point loss is shown to leave the margin floor intact. **Option D is not acceptable.** The "fly it on like a jet" landing technique is real and well documented in writing. It is partly forced by the configuration and partly fixable. It is acceptable only if the fixes are design changes, because the record's go-around stall happened to a pilot with 30,155 hours, 112 of them in type. **I am not recommending against revival.** I am recommending against reviving it as the original configuration plus a balance fix. A re-derivation can be acceptable if it meets the outcome requirements in section 5.

## 1. Corrections to the input before it is used

1. **N747P's ballast is published: 49 lb.** The dossier and `balance.py` both say the amount is unpublished. Sport Aviation, September 1991 (Jack Cox, p. 49; the text is broken across columns in the scan) says: "With paint, interior, avionics and 49 pounds of ballast necessary to get the weight and balance within ... limits, the final weight came out at 1,661 pounds." The article does not say where the ballast sat. At AERO's arms it is worth 2.0 in of empty-CG error if it sat at FS 160, or 3.9 in at FS 100 (E). Moving the radiator forward (option B) is worth about 4.0 in. **So the "no ballast" result for option B is most likely wrong.** Under the N747P datum, B uses all of its margin and lands near zero. Also, N747P carried that 49 lb while it still had its light, fixed-pitch wooden propeller (SA91: "Right now (April 1990), we're using a fixed pitch propeller"), before the 3-blade MT constant-speed propeller was fitted.
2. **The propeller's mass is not visibly in the balance.** `AM20T_ENGINE` is "engine, PSRU, turbo, mount, exhaust". A constant-speed propeller and spinner for 260 hp will weigh more than the original's wooden fixed-pitch propeller. At the propeller plane (FS 322), every 10 lb costs about 8 lb of nose ballast (E, AERO's arms). AERO should confirm whether the propeller is included.
3. **The aft-most CG comes at the end of the flight.** The 90 gal of fuel sits at about FS 214, ahead of the CG range, so burning it moves the CG aft by about 1.6 in at 2,700 lb (E). That is a quarter of the 6.7 in envelope. AERO's loading set already includes the reserve-fuel case, so the limit itself is right. The operational consequence is that the least-stable loading is the one flown on approach, in the flare and in a go-around. Sections 2 and 3 meet there.
4. **On the brief's phrase "a light engine forward of the CG":** on this airplane the engine sits about 73 in **behind** the aft limit (FS 296). The critical aft case is a light pilot alone in front, with bags and low fuel. That is the loading that "jumped off the ground unexpectedly" on Vic Syracuse's first flight (Kitplanes, Checkpoints-3).

## 2. Aft-CG handling and the balance options

### 2.1 What the margin is, before any option

These figures are AERO's (E): neutral point 39% MAC stick-fixed (band 36-43%) and about 33% stick-free. The aft limit is 27% MAC, so the static margin there is about 12% stick-fixed and **6% stick-free**. If the neutral point sits at the low end of its band, the stick-free margin falls to about 3%. The tail volume is 0.50, against 0.6-0.8 for typical GA singles.

The written record matches a low stick-free margin:
- AOPA Pilot, March 1986: "At low speed, particularly when in ground effect, pitch is quite sensitive and the feel is not linear, which induces a tendency to overcontrol."
- Kitplanes, May 1988 (2022 summary of LeRoy Cook's report), quoting Kitplanes October 1986: "bobweights can be added to lessen the light elevator's sensitivity". Prototype 2 got them.
- Russ Taylor, the builder of N747P (Sport Aviation, September 1991): "The only thing I can fault in the handling is the pitch sensitivity ... I have to get an artificial 'feel' system in it ... Technique can compensate for the sensitivity, but the feel system is needed."
- AOPA86: "bump-induced excursions take three to four oscillations before neutralizing."

**Mechanism.** A small stick-free margin means a light stick-force gradient. Small pilot inputs or small trim disturbances then produce large changes in angle of attack, and the effect is worst at low dynamic pressure, which means takeoff, approach and flare. Bobweights and downsprings raise the stick forces, but they do not move the aerodynamic stick-free neutral point. They fix the feel, not the stability. A bobweight is acceptable only on top of a demonstrated margin floor, never as a substitute for one.

**Stall and spin.** These hazards are common to every option, and none of the options changes them:
- **No aerodynamic stall warning** (AOPA86: "There is no aerodynamic warning before the stall"). A stall-strip experiment is recorded, but no result is.
- Full-stall landings end abruptly (KP88: "the airplane suddenly quits flying").
- Spanwise progression looks benign: "super gentle, with practically zero roll tendency" (Sport Aviation, March 1986), with 1.5 deg of washout. That is a point in its favour.
- **Spins were never tested** (SA86: the airplane was waiting for spin-recovery rockets; no later spin test has been found).
- **Deep stall of a T-tail at the aft CG** has not been examined anywhere in the record. Severity would be catastrophic if it exists. It cannot be asserted from the evidence I have; it is flagged for analysis. SDASM's wind-tunnel evaluation (SC.10269) may contain post-stall pitching moments. Reading it is museum contact, so Bill's call.
- Takeoff at the forward limit is limited by rotation (AM20T: V_rot/Vs 1.50, AERO E). The window between a rotation-limited forward limit and a stability-limited aft limit is only 6.7 in. Neither end has margin to give away.

### 2.2 Verdict per option

| Option | Verdict | Reason |
|---|---|---|
| **A. Nose ballast**, 40-52 lb of lead at FS 100 | **Acceptable with mitigation** | Fixed mass, so the CG it sets cannot drift. It adds no new failure modes, and it is the robust trimming element that every option will need anyway once the real empty CG is known (see correction 1). Hazards: (a) **removable ballast that someone leaves out puts the airplane outside its envelope**, so the conditions are that it is structurally fixed, cannot be removed without tools, is part of the weighed empty weight and CG, and is placarded; (b) its attachment must hold the mass at emergency-landing inertia loads (Part 23's 23.561 values are a usable yardstick); (c) 40-52 lb of dead weight pushes the heavy-end build to 876 lb useful load, which creates pressure to fly overweight. Of the four options, this is the one with the fewest unknowns. |
| **B. Masses forward**: radiator and coolant to the nose bay, avionics forward | **Acceptable with mitigation** | Its weight advantage is mostly gone once the 49 lb N747P datum is applied: expect B plus 25-50 lb of residual ballast, not B alone (E). It also adds the only new failure modes of the four. A coolant loop of about 30 ft between a tail-cone engine and a nose radiator brings more joints and a longer hose. On a single-engine airplane, **loss of coolant means the engine fails within minutes**, so that loop is a single point of failure of the only engine. If the routing passes through the cabin, there is also a hot, pressurised glycol scald and fume hazard in a leak or a crash. Air can trap at high points of a long loop, and a nose radiator inlet can be damaged by bird strike or debris. Conditions: route the loop outside the occupied volume, or in a sealed shroud vented overboard; use the fewest possible joints and hard lines where practical; fit a coolant-loss annunciation (pressure or level plus temperature) and publish the time to failure after loss; carry the loop in the powerplant FMEA as a single point of failure of the engine; and design the bleed path for a long loop. In its favour, it removes the tail-cone cooling problem the record shows (the prototype's oil overheat, N747P's hot cylinder). |
| **C. Fuselage stretch**, 11-14 in ahead of the spar | **Acceptable only with a demonstrated margin** | C is sized to put the CG on the same aft limit as A. A longer forward fuselage moves the neutral point forward by about 1-2% MAC, and AERO's own note says that is not in the sizing. On a 6% stick-free margin that is a quarter to a third of the margin. A longer nose also adds destabilising side area ahead of the CG, on a fin of about 16 ft2 (E), so directional stability and departure resistance get worse. Condition: recompute the neutral point and the directional derivatives (Cn-beta, Cn-beta-dynamic) with the stretch, and show the section 5 floor still holds at the aft limit. If it does not, C is not acceptable. |
| **D. Wing moved aft** 4-5 in, with its mains and tanks | **Not acceptable** | D works against the two quantities the record already names as the weak points. (a) The tail arm shrinks from 89.5 to about 85 in, so a tail volume that is already the lowest in class (0.50) falls to about 0.475. The fuselage ahead of the wing grows, the neutral point moves forward, and the stick-free margin falls to about 3-4.5% (E). (b) The mains move aft with the wing, so rotation gets harder (AERO's own finding). The documented hazards, "jumps off", hard rotation and pitch oscillation at lift-off, get worse. (c) The fin arm shrinks too, which costs directional damping on a type that has never been spin-tested. D moves away from inherent stability. A larger tail would make it a different option, to be judged on its own numbers. |

**Inertia, noted but not decisive.** A and B add mass at the nose. Together with the engine in the tail, that loads mass at both ends of the fuselage and raises the pitch and yaw inertias relative to roll. That affects spin mode and the right recovery technique. The direction of the effect cannot be stated without a spin analysis, and it is one more reason the spin test in section 5 is a requirement.

**The point every option shares.** Not one of A-D changes the tail volume, the rotation speed (V_rot/Vs 1.35-1.50 on the AM20T, AERO E, against the usual 1.1-1.2), the ground-effect pitch-up or the missing stall warning. AERO already says this ("B holds the CG; it does nothing for rotation"), and I agree. From the safety side, the larger horizontal tail is not an option to be traded for 3 kt. It is the obvious lever for meeting the outcome requirements in section 5.

## 3. The approach and landing technique

### 3.1 What the written record says

Bill's observation (a power-on approach and a very flat flare, "like an airliner") matches the written sources. Bill has watched it on video; I have not seen a video and do not describe one. The only other video reference is Syracuse's: "The video of that first flight still gives me the willies" (Checkpoints-3), and I do not infer its contents.

- **AOPA Pilot, March 1986:** "I had already been briefed that ground effect at flying speed creates a pitch-up tendency. This encourages overrotation at takeoff; there is no need to flare during landing because of the characteristic ('Fly it on with attitude, just like a Lear,' Leo Prescott had told me)." Also: "the airplane flares itself and flies onto the runway very nicely, once the proper attitude is established. Once the mains are on the runway, the nose falls through quickly, and attempts to hold it off only aggravate the inevitable bump as the nosewheel hits." And: "The pitch characteristics and the behavior of the Pusher in ground effect are the only two handling areas that I observed that will take a bit of transition training."
- **Sport Aviation, March 1986 (Dick Cavin):** "Coming across the fence at 90-95 and leaving just a little power on, when the airplane gets into ground effect you just hold what you have and don't flare and it will touch on the mains quite gently." His own landing: "Reducing power to almost idle gave about 80-85 over the fence, with about a 3 second float to touchdown." He also wrote: "the nosewheel is hard to hold off on landing".
- **Kitplanes, May 1988 (Cook, prototype 2):** "Aiming for an over-the-fence speed of 95 mph, the Pusher floated through the flare normally, rather than requiring forward pressure to keep the nose down as in the previous airplane. It is best to avoid full-stall landings, which tend to be firm as the airplane suddenly quits flying. The best technique is to land the Pusher like a jet, flying it onto the runway at about 75 mph, in a slight nose-up attitude well above stall." So prototype 1 needed forward stick in the flare.
- **Sport Aviation, September 1991 (Taylor):** "It handled like a small jet, so that's the way I have flown it ... and that's the way it should be flown." He described a matching takeoff: "at 60 mph, then just put a little air load on the elevators and hold them there. At 65 it will fly itself off".

One reconciliation question remains open. The written sources describe a **fast**, slightly nose-up approach: 80-95 mph over the fence, against a 66 mph flapped stall (about 1.2-1.45 Vso). A visibly nose-high attitude with 35 deg of flap would normally mean a slower approach. I cannot tell from writing which one the pilots Bill watched were flying. The difference matters, because the hazard in 3.2 grows quickly as the approach slows.

### 3.2 Mechanisms

**(a) Pitch couples to power, with the sign reversed from a tractor.** The thrust line sits about 19 in above the CG (AERO E). Adding power pitches the nose down. Losing power pitches it up. In a conventional low-thrust-line tractor single, a power loss lets the nose drop toward a safe speed. Here, a power loss pushes the nose toward the stall, and the stall gives no aerodynamic warning. With the stick released, the airplane re-trims after a sudden loss of approach thrust ΔT as follows (E, mine: 2,700 lb, 127 ft2, 49.5 in MAC, CLmax 1.93 from a 57 kt Vso):

| Approach speed | ΔT (approach thrust plus windmilling drag), lb | Stick-fixed (SM 12%) | Stick-free (SM 6%) | Stick-free, low end (SM 3%) |
|---|---|---|---|---|
| 85 kt (1.49 Vso), the written sources' speed | 150 / 250 | 1.37 / 1.31 Vso | 1.28 / 1.18 Vso | 1.14 / 1.01 Vso |
| 75 kt (1.32 Vso) | 150 / 250 | 1.21 / 1.16 Vso | 1.13 / 1.04 Vso | 1.01 Vso / beyond CLmax |
| 70 kt (1.23 Vso) | 150 / 250 | 1.13 / 1.08 Vso | 1.05 Vso / beyond CLmax | beyond CLmax |

Read it this way. At the fast approach the sources describe, a power loss costs margin but is survivable if the pilot holds the stick and pushes. On a slower, nose-high approach, the pitch-up from the power change alone, with the stick free, takes the wing past its stall. A loss of power does not take thrust to zero: a constant-speed propeller flattens to fine pitch and windmills, and that drag acts on the same high line, so ΔT is larger than the approach thrust alone. That makes the AM20T with a constant-speed propeller worse here than the original's fixed-pitch wooden propeller. The magnitude scales directly with the 19 in offset and inversely with the static margin, and both are estimates. This is a hazard with a mechanism and an estimated size. It is not yet a measured one.

AOPA86 did test abrupt power changes: "In each of the configurations I tried abrupt power changes to sample pitch changes. Behavior was quite predictable." That was prototype 1, at 2,250 lb, with a fixed-pitch wooden propeller that held the engine to about 2,400 rpm and roughly 130 hp (SA86). It is real evidence that the effect was manageable at that thrust, in the hands of an evaluation pilot. It does not cover the AM20T.

**(b) The go-around step is large, and larger on the AM20T.** Going from about 200 lb of approach thrust to 550-800 lb of full thrust puts a nose-down moment of about 6,600-11,400 in-lb on the 19 in offset. That is a ΔCm of about 0.04-0.10 at 75-85 kt (E). The pilot has to pull at once and hard, on an elevator described as "quite sensitive ... not linear ... tendency to overcontrol", at 5 ft, in ground effect. AERO puts the AM20T's extra take-off thrust at about 270 lb, so this step is roughly 1.5-2 times the original's.

**(c) The flat flare is forced by the propeller and tail geometry.** The pitch angle at which the propeller strikes, pivoting about the mains, is 14.7 deg with the 65 in propeller and the FS 236 mains (AERO E). It is 13.7 deg with a 68 in propeller and 12.5 deg with a 72 in propeller (E, mine). Flex in the fibreglass mains and tyres at touchdown takes off a further 0.6-0.7 deg per inch, and a wing-low crosswind touchdown reduces the tip clearance on one side. Wing incidence is 2 deg (SA86). A full-stall touchdown needs a flapped wing angle of attack of about 12-15 deg, which is generic and not sourced for this wing. That means a body attitude of about 10-13 deg, **leaving roughly 0-5 deg to propeller strike**. Flying it on at about 1.15-1.25 Vso needs about 5-7 deg of attitude, which leaves 7-10 deg. The fly-on technique is the geometry's answer. **A GA pilot trained to flare to a nose-high hold-off will go looking for propeller or tail-cone contact.** The tail-cone underside and the ventral fin shown on the RCM model plan may touch before the propeller tip, and nobody has computed that. A sacrificial tail skid that touches before the propeller does is a cheap mitigation.

**(d) Ground-effect pitch-up: mechanism unknown.** AOPA86 was briefed on it, and KP88 says prototype 1 needed forward pressure in the flare. Conventional airplanes pitch nose-down in ground effect, so this is unusual. No source names a mechanism. Candidates are a T-tail sitting high above the ground plane that loses less downwash than the wing gains lift-curve slope, with the wing's aerodynamic centre ahead of an aft CG, or effects of the reflexed flaps. That list is my speculation and is flagged for analysis, not asserted. AERO's handling item 4 (a vortex-lattice model with a ground image) is the right first step, and flight test is the only way to close it.

**(e) Energy management.** An over-the-fence speed of 95 mph against the airplane's own 1.3 Vso of 86 mph carries about 23% more kinetic energy (E). Add a 3 s float and a nosewheel that "falls through quickly", and the landing distance gets longer while the nosewheel takes the load early. The mild stall the sources describe is not available as a short-field tool. Both point to a longer runway requirement than a GA pilot would assume from "a four-seat single". Nobody has a measured landing distance. Overrunning a short strip is the credible consequence.

### 3.3 Transition-training burden

The technique reverses at least six trained GA habits, and every reversal sits in takeoff or landing, the phases where loss-of-control accidents cluster:
1. Approach fast (1.4-1.5 Vso over the fence) instead of about 1.3.
2. Do not flare to a hold-off, and do not hold the nosewheel off.
3. Losing power pitches the nose **up**.
4. Adding power pitches the nose **down**, and hard on the AM20T.
5. On takeoff, do not rotate; let it fly off (Taylor: the reviewers who "hauled back" got an airplane that would "leap into the air").
6. There is no aerodynamic stall warning, and the aft-CG awareness is airliner-style ("watched when the rear seats are occupied. 'Just like jets'", SA91).

The evidence says pilots learn normal operations quickly. AOPA86 needed "a few circuits", and Cavin was comfortable "after only a couple of times around the patch". **The evidence also says experience does not protect against the rare event.** MIA92LA186 was flown by an Airline Transport Pilot with 30,155 hours, 112 of them in make and model. Those hours are consistent with the builder, Russ Taylor, whom SA91 describes as a former 747 captain with "some 30,000 hours"; the NTSB report does not name the pilot. He initiated a go-around at about 5 ft, and the airplane "pitched up ... stalled". Habits learned in transition training hold in routine operations and tend to give way under startle, which is exactly the go-around or power loss near the ground. **So training is a necessary mitigation and not a sufficient one.** Syracuse's own summary was that the airplane "required above-average piloting skills" (Kitplanes, Checkpoints-24).

### 3.4 Inherent or fixable?

| Element | Inherent? | Fix in a revival |
|---|---|---|
| Flat touchdown (propeller and tail-cone strike) | **Inherent** to an open pusher propeller on short gear | Longer gear (weight, a higher CG, tipback), a smaller or multi-blade propeller, a tail skid. The fly-on technique itself is tolerable if it is trained and placarded. |
| Pitch coupled to power, with the sign reversed | **Inherent in sign, fixable in size.** A ground-clearing propeller hub sits above a low cabin CG. | Tilt the thrust line down toward the CG (partial; 3-5 deg roughly halves the offset at about 100 in; the cost is propeller 1P loading and a lift component), and a larger tail, since the trim shift is ΔCm/SM. |
| Pitch sensitivity, small stick-free margin | **Fixable** | Tail volume to the range typical of GA singles; elevator hinge-moment and gap design. A feel system only on top of a margin floor. |
| Ground-effect pitch-up | Unknown mechanism | Analysis, then flight test. |
| No stall warning | **Fixable** | An angle-of-attack-based stall warning plus tested stall strips. ASTM F3695 covers AoA functional requirements; I have not read it. |
| Hard rotation, hop-off | Partly inherent (an empty CG far aft, mains placed for tipback) | Tail power (AERO: +30% tail gives V_rot/Vs 1.24-1.36), a lower thrust line. |

**Verdict on the landing technique: acceptable with mitigation, and the mitigations have to be design changes.** A fast, flat, powered approach is a legitimate technique in its own right. What is not acceptable is a revival that keeps the original's reversed, strong pitch-power coupling, its small stick-free margin and its silent stall, and relies on pilot technique to cover all three. The record contains a 30,000-hour pilot for whom that technique did not hold.

## 4. The accident record: which events tie to section 2 or 3, and what the AM20T revival does

Sources: the NTSB final reports re-fetched 2026-10-25 (MIA92LA186, LAX05LA270, LAX90DUM02, CHI90DEE10), plus AERO's README for CEN09CA386 (NTSB returned 403) and the two non-US events.

| Event | Ties to | Revival on the AM20T |
|---|---|---|
| **Syracuse's first flight, about 1988** (not an NTSB event; written by the pilot, Kitplanes Checkpoints-3): light pilot, aft CG, "jumped off the ground unexpectedly and began to oscillate in pitch". He threw 25 lb of lead forward, and "we narrowed the CG envelope after that flight". | **Section 2** directly | **Fixed only by the section 5 requirements.** Options A-D place the CG but do not widen the margin. A builder's first flight is a test flight, so the kit has to ship a weighed-empty-CG requirement and a first-flight CG restricted forward of the design aft limit. |
| **MIA92LA186, N747P, 1992**: go-around at about 5 ft, "THE NOSE OF THE AIRPLANE PITCHED UP, THE AIRPLANE STALLED"; ATP, 30,155 h, 112 h in type. The aircraft carried 49 lb of ballast to reach its limits (SA91). | **Sections 2 and 3** | **Worsened unless redesigned.** The go-around thrust step is about 1.5-2 times larger. The NTSB probable cause is pilot airspeed control. The mechanism in 3.2(b), a large nose-down thrust step answered on a sensitive elevator, is consistent with the record but **not established by it**. Fixed by the larger tail, the lower or tilted thrust line, and stall warning. |
| **CHI90DEE10, N75FM, 1990, fatal** (Prescott identity probable, not confirmed): power loss on climb-out (choke handle confused with the nose-gear release handle), then "AN INADVERTENT STALL DURING THE FORCED LANDING". | **Section 3**, power loss at low altitude followed by a stall. The power-off pitch-up in 3.2(a) would aggravate it; the report does not establish that it did. | Fixed in part: kit-standard, shape-coded controls remove the handle confusion. The power-off pitch-up stays until it is redesigned. |
| **LAX90DUM02, N58PP, 1990, fatal**: Ford V-6, seized on the first flight (lean float setting, vent capped), crashed while trying to return to the airport. | Neither directly; powerplant and builder maintenance | **A caution, not a fix.** Both fatal accidents were alternative engines failing in their first hours, on climb-out. The AM20T is also a non-certificated, geared, turbocharged, liquid-cooled engine, and option B adds a long coolant loop. Mitigation: ground-run hours and a Phase I engine programme before any envelope work. |
| **OE-VPJ, 2004** (news via ASN, no report): test flight, fell from about 5 m on initial climb, cause unknown | Consistent with section 2 (lift-off), **not attributable** | Unknown. |
| **LAX05LA270, N43PP, 2005**: wooden propeller separated in cruise, bolt holes elongated, cause undetermined. The pilot had just tried a propeller that "was too long for ground clearance". | Indirectly section 3(c): propeller clearance drove the propeller swaps | Mixed. A metal or composite constant-speed hub removes the wood-shrinkage bolt-preload mode. The AM20T reduction gearbox, the 12 in extension and the propeller are an **untested torsional-vibration combination** (AERO item 10), so a torsional survey is mandatory. |
| **CEN09CA386, N19PP, 2009**: cabin door came off in flight and struck the propeller | Neither; this is pusher debris | Fixed by door-latch design and indication. Anything shed from the airframe goes through the propeller on a pusher, so it belongs on the blade-failure fault tree. |
| **Germany, 2002**: gear-up landing | Neither | Fixed by gear warning (SYSTEMS). |

With about 20 airframes and unknown hours, **no accident rate can be computed.** What the record does show is that its one confirmed loss-of-control event in flight, MIA92LA186, happened to the most experienced pilot in it.

## 5. Safety constraints for any Prescott re-derivation (published to AERO, STRUCTURES, PROPULSION, SYSTEMS)

These are engineering best practice and duty of care for an airplane other people will build and fly. They are not regulatory requirements. Each one is stated as an outcome, so the design can choose how to meet it.

- **R1. Stick-free static margin at the aft limit**, in the worst power and flap case including power-off approach, **at least 5% MAC**, demonstrated. The 5% is my target, not a standard. At the current 6% estimate with a ±3% band, the original configuration does not reliably meet it. The aft limit is then set by flight test, not by the plan. The stick-force gradient must be stable (pull to slow down) in landing configuration with power on and off. Bobweights may only add to this.
- **R2. Pitch change with power is bounded.** On a sudden full power loss from the published approach speed, stick-free, the airplane must re-trim no slower than **1.2 Vso**. Full go-around power must be controllable with one hand on the elevator at the published approach speed. Levers: thrust-line tilt, tail volume, approach speed.
- **R3. An angle-of-attack-based stall warning**, independent of the EFIS display path, plus stall strips tested for buffet margin.
- **R4. Propeller and tail strike.** The first ground contact in pitch about the mains is a sacrificial skid, not the propeller. The propeller-strike attitude, with gear and tyres compressed to touchdown load, exceeds the published touchdown attitude by at least 5 deg (my target), with the actual propeller diameter.
- **R5. Rotation.** V_rot/Vs of 1.25 or less across the CG range at the AM20T's take-off thrust (AERO's +30% tail case reaches 1.24-1.36, so this is close to achievable). There must be no lift-off before the pilot commands it at the forward limit.
- **R6. Spin and deep stall.** Before anyone else flies the type: post-stall pitching moments at the aft CG (SDASM wind-tunnel data, or new analysis), then a spin and deep-stall test programme with a spin-recovery parachute. Severity if it is missed: catastrophic.
- **R7. Ballast and balance as built.** Every kit is weighed for empty CG before its first flight. Ballast is fixed, cannot be removed without tools, and is placarded. The first flight is flown with the CG restricted forward of the design aft limit.
- **R8. Option B, if chosen**: the coolant loop is carried as a single point of failure of the only engine in the powerplant FMEA. It is routed outside the occupied volume, fitted with a coolant-loss annunciation, and has a published time to failure.
- **R9. A torsional-vibration survey** of the AM20T gearbox, the 12 in extension and the propeller, and **flutter clearance** of the T-tail with the heavier engine behind it (AERO items 9-10). STRUCTURES and PROPULSION are not yet routed, and this review cannot close either item.
- **R10. A transition-training syllabus and placards** for the six reversals in 3.3, with a published approach speed and runway-length data. This is necessary, and it is not counted as sufficient.

## 6. What this review could not establish, and who would settle it

- The real empty CG and its scatter: SDASM's weight-and-balance schedule, or a weighed survivor (N10JS, N200SX). Museum or owner contact is Bill's call.
- Post-stall and deep-stall pitching moments: SDASM's wind-tunnel evaluation. Bill's call.
- The full-scale thrust-line offset, the neutral point and the hinge moments: AERO's estimates stand until a drawn layout or a test.
- The ground-effect pitch-up mechanism: AERO's analysis, then flight test.
- The pilots Bill watched: written sources describe a fast, slightly nose-up approach. Whether the observed technique was slower and more nose-high is a question only Bill can answer, and it changes how heavily 3.2(a) weighs.
- CEN09CA386 could not be re-fetched (403). Its quote is AERO's.

## Addendum, revision 2 (2026-10-25): re-review of AERO's corrected numbers (AER-3902)

AERO took section 1's three corrections into PR #10 (`balance.py` and `balance_output.md` at 6a4ce47, commit 84ea069). The corrections were N747P's 49 lb ballast as the datum, the constant-speed propeller mass, and the neutral-point loss of option C. I re-reviewed the result. Sections 1-6 above are unchanged and still describe PR #10 as I first reviewed it. **Where this addendum differs from them, the addendum governs.**

**The new ugly number.** With the published ballast datum and a constant-speed propeller, the unfixed AM20T airplane sits **7.6-7.7 in aft of its aft limit**. That is more than the whole 6.7 in CG envelope. On the published 1,550 lb airplane, the plain engine-and-propeller swap at 2,400 lb needs 106-116 lb of nose lead (E, AERO). An engine in the tail cone, with a heavier propeller behind it, buys back its CG with dead weight, and the amount has roughly tripled since PR #10 opened.

**Verdicts after the corrections:**

| Option | Revision 1 | Revision 2 | Why |
|---|---|---|---|
| A. Nose ballast, now 113-130 lb | Acceptable with mitigation | **Acceptable with mitigation (unchanged)** | The mechanism is the same: a fixed mass, with no new failure modes. R7 applies in full. The attachment must hold 113-130 lb at emergency-landing inertia loads. The useful load falls to 1,087 / 805 lb, so the pressure to fly overweight is now a real risk at the heavy end. It is MANUFACTURING's and AERO's to design out, and I record it here so nobody files it as a performance issue only. |
| B. Masses forward, now plus 51-69 lb of ballast | Acceptable with mitigation | **Acceptable with mitigation (unchanged)** | B now carries both the coolant-loop conditions (R8) and the ballast conditions (R7). Its only advantage over A is about 55-60 lb less lead, bought with a single point of failure on the only engine. That is a legitimate trade, and it is AERO's and Bill's call. Safety does not prefer B over A. |
| C. Fuselage stretch, now 36-43 in | Acceptable only with a demonstrated margin | **Not acceptable as a sole fix** | Holding the margin takes a 3-4 ft stretch. That puts the most-forward loading 2.5-2.6 in ahead of the forward limit, and the forward limit is set by rotation (V_rot/Vs is already 1.50 there). C therefore trades the aft-CG hazard for the hop-off and no-rotation hazard at the other end, before directional stability is even checked. A short stretch used alongside A or B is still judged under revision 1's condition. |
| D. Wing moved aft, now 11 in | Not acceptable | **Not acceptable (unchanged, and further from acceptable)** | An 11 in move shrinks the tail and fin arms by about 12%. |
| Landing technique | Acceptable with mitigation (design changes) | **Unchanged** | Section 3's estimates depend on the margin at the aft limit, and A and B hold that limit. |
| Overall | Not against revival; against original-plus-balance | **Unchanged** | The corrections make the balance more expensive. They do not change which hazards exist or how they are fixed. |

**Added to R7 (ground tipback).** With B's residual ballast, the empty airplane's tipback on prototype 2's mains is **14 deg** (AERO E), below the usual 15. The baggage bay (FS 238) sits **behind** those mains (FS 236), so loading bags into an empty airplane moves it toward sitting on its tail. On a pusher, that puts the propeller arc and the tail cone into the ground or into people. R7 now adds: tipback of at least 15 deg in the most adverse ground-loading sequence (empty, bags first, a rear occupant boarding), or a mandatory tail stand or nose-down kneel procedure that the kit supplies and placards.

**Still open, owned elsewhere:** Cn-beta with any stretch (AERO), the real empty CG (a weighed survivor or the SDASM W&B schedule, contact is Bill's call), and the governor's mass (AERO). None of them changes a verdict above.
