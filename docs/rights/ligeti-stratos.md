# Ligeti Stratos — rights and provenance

**Stage:** 2, rights and provenance. **Researcher:** Elon. **Board issue:**
AER-3805. **Date:** 2026-10-24. **Status:** first pass, desk research from
public sources only. Nobody has been contacted. Added at Bill's request: "Apparently it was open sourced? The creator did die in a crash but it's worth
a review." AERO is studying it as a planform (AER-3807).

This is research, not legal advice. It reports what public records show and
where they run out. It does not say the design may be copied.

Source quality: **P** primary or official record; **S** reputable secondary;
**L** low (wiki, forum, aggregator).

## Summary

- **"Open sourced" is true as a label and close to empty as a release.** A
  Google Code project, `ligeti-stratos`, announced the Stratos as
  the "Worlds first Open Source Aircraft". The project record carries the
  licence code `gpl2` (GNU GPL v2), with the content-licence field blank (Google
  Code Archive, P). The archive gives no creation date; the project was active
  around 2008, when its organiser presented it (TWITT). **But the repository holds no design files.** Its only
  commit is Google Code's empty "Initial directory structure", and the archive
  holds no downloads and no source zip. A 2015 GitHub export of the same project
  shows the same: one empty commit and a single project-home page (P, checked
  against a control project; see below). The GPL v2 label sits on a repository
  with nothing in it.
- **No original drawings existed to release.** At a March 2008 talk by the
  revival's organiser, the account recorded is that "there were no drawings or
  design specifications Ron could work with to produce and similar aircraft"
  [sic]. Ron Ligeti, the designer's son, was reverse-engineering the aircraft
  and "is in the CAD drawing stages" (TWITT Newsletter No. 262, April 2008, S).
  So anything "open sourced" was new work by Ron Ligeti and Christopher Alan,
  not Charles Ligeti's design data.
- **The project website is unreachable.** ligeti-stratos.com refused
  connections on 2026-10-24, and the Internet Archive was temporarily offline,
  so its terms could not be read. Search-engine summaries describe it as setting
  out to create a full set of construction plans and to give them away free.
  That is a plan to publish, not a publication, and the wording was not checked
  against the page (L).
- **Rights after the designer's death** sit, on the record, with Charles
  Ligeti's family: the project credits "the generosity of the family of the late
  Charles Ligeti, and the active contribution of his son Ron" (Google Code
  project text, P). That is an expression of consent, not a licence text. The
  original company, Ligeti Aero-Nautical Pty Ltd (Wikipedia, L), was not traced.
- **Airframes: accounts conflict, but at least one survives in a museum.** Three
  were built (Wikipedia; aeropedia). One crashed and killed the designer on 22
  September 1987 near Penfield, Victoria (ATSB report 198701462, cited by AHSA
  and Wikipedia). The second is reported on static display at the Australian
  Ultralight museum at Holbrook, NSW, and an unfinished third shell at a museum
  in the Ballarat/Bendigo area (aeropedia, L). In 2008 Ron Ligeti was said to
  hold "the original airframe" (TWITT, S).

## What was actually released

| Item | What the record shows | Source and quality |
|---|---|---|
| Google Code project `ligeti-stratos` | Summary "Worlds first Open Source Aircraft". `license: gpl2`, `contentLicense: ""`, `hasSource: false`. Labels include CharlesLigeti, RonLigeti, ChristopherAlan | Google Code Archive project.json, read 2026-10-24. P. |
| Downloads, source and issues in the archive | None: all return 403, and the wiki list is null. **Control:** the same URLs for the `protobuf` project return 200 (downloads, project) and 206 (source zip), so 403 here means absent, not blocked | Google Code Archive. P. |
| GitHub export (AukeHoekstra/ligeti-stratos, 3 October 2015) | `master`: one commit, "Initial directory structure." (2006, author "nobody"), with no files. `wiki`: only ProjectHome.md, the announcement text. No licence file | GitHub API, 2026-10-24. P. |
| Project announcement text | "Through the generosity of the family of the late Charles Ligeti, and the active contribution of his son Ron, an accomplished aeronautical engineer, the Ligeti Stratos has been made available as what is hoped to be the first of a complete line of Open Source aircraft." | Google Code project text. P. |
| ligeti-stratos.com | Unreachable (connection refused); the Internet Archive was temporarily offline (503). Terms not read | — |
| State of the design data in 2008 | No original drawings or specifications; Ron Ligeti in "the CAD drawing stages"; Christopher Alan planning a quarter-scale model, then a mock-up | TWITT No. 262, April 2008, recap of a 15 March 2008 talk. S. |
| "Plans" on model-aircraft sites (AeroFred, the-blueprints) | R/C model plans and three-view drawings by third parties. Not the aircraft's design data | L. |

**Reading.** Bill's caution is borne out. There is a licence label (GPL v2), but
nothing was committed under it. The original design data did not exist in 2008,
and whatever the website offered cannot be read today. On the public record, no
usable design file sits under a licence AeroCommons could rely on.

## What survives and where

| Item | Account | Source and quality |
|---|---|---|
| Airframe 1 (the aircraft in the fatal crash) | Crashed 22 September 1987 near Penfield, Victoria, killing Charles Ligeti. Wikipedia calls it the prototype. AHSA calls it the first production Mk II and says "The damaged aircraft was repaired and is on display at the Ballarat Air Museum, Victoria." AHSA puts "some 340 hours" on the Mk I prototype, not this aircraft; aeropedia puts the 340 hours on the crashed aircraft itself. TWITT (2008) says over 700 hours in all | Wikipedia, L; AHSA, S; aeropedia, L |
| Airframe 2 | "crashed at Mangalore injuring the pilot and it was restored to static display standard at Holbrook for the Australian Ultralight Museum", registered 19-7441, c/n S3-001 | aeropedia, L |
| Airframe 3 | "only a fibreglass shell and was not completed but has survived", on display "at a museum in the Ballarat / Bendigo area" | aeropedia, L |
| "The original airframe" | Held by Ron Ligeti in 2008, kept "in flying condition but has not flown" | TWITT 2008, S |
| Drawings | None original, per the 2008 talk. Ron Ligeti's re-engineered CAD work, if it was finished, is not found | TWITT, S |
| Public data | Jane's 1987-88 specifications (span 5.36 m, wing area 7.53 m², MTOW 188 kg, Wortmann airfoil, König SD 570 at 21 kW), via Wikipedia. The ATSB investigation report 198701462 | L; P (report not read) |

The accounts do not agree on which airframe is where. The two museum holdings
are the likeliest survivors to measure. Visiting or asking either museum is
contact, and Bill's call.

## Holder of residual rights

- **Charles Ligeti's own works** (any drawings, notes or the design as
  expressed in documents) passed on his death to his estate or heirs. On the
  public record that is his family, and Ron Ligeti acted for it in 2008.
- **Ligeti Aero-Nautical Pty Ltd** (the manufacturer named by Wikipedia; AHSA
  and aeropedia use "LGT Aero Nautical"): corporate status not checked. ASIC
  records were not searched.
- **Ron Ligeti's and Christopher Alan's 2008 re-engineering work** belongs to
  them unless it was licensed. The GPL v2 label is the only licence signal, and
  it covers nothing that was committed.
- **Copyright term.** Charles Ligeti died in 1987. If Australian law gives his
  works life plus 70 years, they stay protected until the end of 2057. That is
  an attorney question, not a conclusion.
- **Patents and trademarks:** none identified. Any 1980s patent has expired.
  "STRATOS" is a common mark in other industries; it was not checked.

## The path for AeroCommons

| Path | What it would take | Assessment |
|---|---|---|
| **Use a genuine open release** | Find the actual published files and their licence text. | **No such files found.** If ligeti-stratos.com or Ron Ligeti's CAD work surfaces with a clear licence, this becomes the cleanest path in the survey, and GPL-style terms fit an open-source non-profit. Today it is a lead, not a path. |
| **Re-derive from public data** | Jane's figures, photographs, published three-views and the ATSB report; measure a museum airframe. | Feasible for a planform study (AERO's AER-3807). The ATSB report matters for safety: the fatal crash followed changes to the canard (full-span elevators) affecting stall and pitch behaviour (Wikipedia, citing the ATSB). |
| **License from the family** | Ask Ron Ligeti or the estate for written terms. | Possible. The family has already signalled it wants the design open. Requires contact: Bill's call. |
| **Buy** | Nothing commercial to buy. | Not applicable. |

## Where an aviation IP attorney is needed

1. **Does a GPL v2 label on an empty Google Code project grant anything?** It
   cannot license files that were never published under it. Confirm that it
   creates no rights in later or off-repository material.
2. **The family's public statement** ("made available ... as ... Open Source"):
   is it a licence, a promise, or nothing enforceable? Who in the family or
   estate can grant a licence?
3. **GPL v2 applied to aircraft designs**, if files surface under it: what
   counts as "source", and what the copyleft means for derivative designs and
   for kits.
4. **Australian copyright term and ownership** for Charles Ligeti's works, and
   for the company's, if it held any.

## Open items

- ligeti-stratos.com through the Internet Archive once it is back online: what
  files and what terms it published (2008-2013).
- Ron Ligeti's CAD work: did it reach a releasable state, and where?
- ATSB report 198701462: read in full.
- ASIC status of Ligeti Aero-Nautical Pty Ltd.
- Which museum holds which airframe (Holbrook, Ballarat): resolve the conflict
  from public museum catalogues.

## Sources

- Google Code Archive, project `ligeti-stratos`, project.json and wikis.json;
  control project `protobuf`. Read 2026-10-24 (P).
  https://storage.googleapis.com/google-code-archive/v2/code.google.com/ligeti-stratos/project.json
- GitHub, AukeHoekstra/ligeti-stratos ("Automatically exported from
  code.google.com/p/ligeti-stratos"), branches `master` and `wiki`, read via the
  API 2026-10-24 (P). https://github.com/AukeHoekstra/ligeti-stratos
- T.W.I.T.T. Newsletter No. 262, April 2008: recap of Christopher Alan's
  15 March 2008 talk (S). https://rcsoaringdigest.com/TWITT/Apr08Ltr.pdf
- Aviation Historical Society of Australia, "22-09-1987", citing ATSB report
  198701462 and Ron Ligeti (S).
  https://www.ahsa.org.au/wp/archives/this-day-in-history/22-09-1987
- Aeropedia, "Ligeti Stratos" (L). https://aeropedia.com.au/content/ligeti-stratos/
- 1000aircraftphotos, "Ligeti Stratos" (L).
  https://1000aircraftphotos.com/Contributions/BankaBob/9901.htm
- Wikipedia, "Ligeti Stratos", specifications from Jane's 1987-88 (L).
  https://en.wikipedia.org/wiki/Ligeti_Stratos
- Hacker News discussion, February 2021, of ligeti-stratos.com (L).
  https://news.ycombinator.com/item?id=26042760
