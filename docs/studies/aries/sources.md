# Aries (Model 51): sources found for AER-3867, with grades

Public material only. Nobody was contacted. Searched 2026-10-25.

"Re-checked" means AERO re-fetched the text and matched the quote word for
word. The others were transcribed by a research pass from page images or
scans, and no number in this study depends on them.

## Measured or reported speed and fuel flow

| Source | Airframe | Grade | What it says (verbatim) | Re-checked | Used for |
|---|---|---|---|---|---|
| AOPA Pilot, Mar 1977, flight check ([PDF](https://aeroresourcesinc.com/uploads/197703-1977%20Bellanca%20Aries%20T-250.pdf)) | prototype N51AG | P | 185 mph IAS / 208 mph TAS at 6,500 ft, OAT 50 F, 22.5 inHg / 2,300 rpm, "73%"; 215 / 217 mph at 1,000 ft, full throttle, 2,575 rpm; "partially loaded" | stage 3 | calibration, two points |
| Flying, Apr 1977, R. L. Collins, "Bellanca Aries T-250", pp. 44-51 (Google Books volume `wKfgQo2Zw3MC`; snippets from `https://www.google.com/books/feeds/volumes?q=%22<phrase>%22`) | prototype N51AG | P | "We leveled first at 4,500 feet and selected 23 inches of manifold pressure and 2,300 rpm. The indicated airspeed was 163 knots, for a true of 175 knots. I got a true of 173 knots at 6,500 feet, 21.5 inches and 2,300; and 181 knots at 22.8 inches and 2,300, which would be nearly 75-percent power." / "two-way speed run between VOR stations, the average of the two legs, flown at 6,000 feet pressure altitude, came to 177.6 knots. The power on that run was probably a shade below 75 percent, which means we were burning between 13 and 13.5 gallons per hour." / "We were 300 pounds below gross weight for our initial flight, and the temperature was in the mid40s." / "The T-250 should cruise at 165 knots on 12 gph" | yes, 2026-10-25 | calibration, four points. The 13-13.5 gph is Collins's inference from power ("which means"), not a fuel-flow reading, so it does not check fuel burn independently. Only snippets could be read, not the full pages or the spec table |
| TheWebWingman, "Ride Report: Bellanca Aries T-250", 22 Feb 2014 (the post itself is not archived; its full text is in the site feed, [Wayback](https://web.archive.org/web/20140509072721id_/http://www.thewebwingman.com/feed/)) | N77CT (s/n 0004), ferry Dec 2013 | B | "The published cruise performance numbers are a bit optimistic, I was only able to get about 190MPH TAS instead of the 208MPH TAS promised by the manual, but I'm pleased overall." | yes, 2026-10-25 | pessimistic bound only: altitude and power not stated. Per the 2014 sale listing ([Wayback](https://web.archive.org/web/20150715191742id_/http://sky4buy.com:80/Bellanca-Aries-T-250-Own-a-Piece-of-History-131381054278/0873)), the engine had been repaired with parts of unknown time, and compressions were 70-78/80 (listing not re-checked) |
| In Flight USA, Jun 1995 (scans captured on the old owner page, home.att.net/~wcvog, Wayback 2001-2003) | N250DJ (s/n 0003) | B | owner: "a true 200 mph airplane"; spec box "Cruise speed: 200 mph", "Fuel capacity: 80 gallons", "Empty weight: 1,850 lbs." | no (transcribed from images) | not used: no conditions |

No weighed empty weight, POH page or logged fuel flow was found for any of the
four airframes.

## Geometry and published performance

| Source | Grade | What it gives | Re-checked |
|---|---|---|---|
| TCDS A11SW Rev 2 ([archived copy](../../longlist/sources/tcds-A11SW-rev2-1980-07-01.pdf)) | T | no external dimensions; datum, CG range, stations, speeds, prop pitch stops | yes (fetched from FAA DRS; SHA-256 in the sources README) |
| Jane's All the World's Aircraft 1979-80, "Bellanca Aries T-250" (Internet Archive `janesallworldsai7980fran`, lending only; read through its full-text search, `https://be-api.us.archive.org/fts/v1/search?q=identifier:janesallworldsai7980fran AND "<phrase>"`) | F | "Wing section NACA 600412 modified. Dihedral 6°"; "Wing span 9-55 m (31 ft 4 in) / Wing chord (constant) 1-68 m (5 ft 6 in) / Length overall 7-98 m (26 ft 2 in) / Height overall 2-62 m (8 ft 7 in) / Tailplane span 3-81 m (12 ft 6 in) / Wheel track 1-68 m (5 ft 6 in) / Wheelbase 2-36 m (7 ft 9 in) / Propeller diameter 1-96 m (6 ft 5 in)"; fuel "77 US gallons), of which ... (72 US gallons) are usable"; ranges "max fuel, 45 min reserves at 45% power: 75% power 860 nm ... 65% power 946 nm ... 55% power 1,016 nm"; "Range with five occupants, 189 litres (50 US gallons) fuel, reserves as above 586 nm" | yes: the dimension lines chain in order (span, chord, length, height, tailplane span, track, wheelbase), plus the airfoil line, the range lines with their reserve basis, the five-occupant line and the 72 gal line |
| Skrzydlata Polska, 16 Apr 1978, p. 14 (Internet Archive `skrzydlata-polska-1978-04-16-nr-16`, public) | F | a three-view drawing; the same range table in km | no |
| Photographs: a near side view of N250DJ (General Aviation News, 2025), two front views of N77CT (owner site) | - | could be used to scale the tail; not done, because README section 4 shows it would not move the range | - |

## Contradictions recorded, not resolved

- **Usable fuel**: TCDS 80 total / 76 usable (T, governs); Jane's 77 / 72. The
  TCDS figure is used.
- **Airfoil**: Jane's prints "NACA 600412 modified" (cambered leading edge);
  Lednicer lists "60-412". Same family, 12% thick.
- **Range basis**: the AOPA 1977 spec table pairs 1,170 statute miles (1,016
  nm) with the 65% economy speed, but Jane's gives 1,016 nm at **55%** power
  and 946 nm at 65%. The brochure cover says "990 miles, not counting
  reserves", where Jane's gives 990 miles at 75% *with* a 45 min reserve. The
  stage 3 dossier screened on "1,017 nm at economy cruise"; read that as 55%
  power.
- **Engine**: the registry, Jane's and the 2014 listing put the three 1980
  airframes on the carbureted O-540-A4D5; only the prototype (now N251AG,
  experimental) has an IO-540. An owner post says IO-540-B4C5 for N77CT.
