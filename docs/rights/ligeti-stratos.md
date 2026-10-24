# Ligeti Stratos — rights and provenance

**Stage:** 2, rights and provenance. **Researcher:** Elon. **Board issue:**
AER-3805. **Date:** 2026-10-24. **Status:** first pass, revised after AERO's
review. Desk research from public sources only. Nobody has been contacted.
Added at Bill's request: "Apparently it was open sourced? The creator did die in
a crash but it's worth a review." AERO is studying it as a planform (AER-3807).

This is research, not legal advice. It reports what public records show and
where they run out. It does not say the design may be copied.

Source quality: **P** primary or official record (including the project's own
archived pages, for what the project said about itself); **S** reputable
secondary; **L** low (wiki, forum, aggregator).

## Summary

- **Two licence signals, no licence text, and they conflict.**
  - From June 2006 the project's own website said the family had "agreed to
    release the new 'Second Generation' Ligeti Stratos as Open Source" through a
    gratis "Attribution-NonCommercial-ShareAlike" licence "currently under
    development". The same words were still there in July 2012 (Wayback
    captures of ligetistratos.com and ligeti-stratos.com, P). No licence text
    was found on either domain.
  - The Google Code project `ligeti-stratos` carries the licence code `gpl2`
    (GNU GPL v2), with the content-licence field blank (Google Code Archive, P).
    Its repository holds no design files: one empty commit and no downloads.
  - **The NonCommercial term matters most for AeroCommons.** A non-profit that
    distributes plans and enables kits may still fall foul of it, depending on
    the terms. That is the first attorney question below.
- **Design data did exist, but in the family's hands, not in any release.**
  Charles Ligeti "built everything on the fly using notes", and Ron Ligeti,
  his son, "sorted through the design notes like a jigsaw puzzle". Ron built a
  CATIA V4 model and was converting it to CATIA V5 (project status page, July
  2006, P). In 2008 the organiser said "there were no drawings or design
  specifications" to work from (TWITT No. 262, S). The two fit: notes, but no
  drawings. Neither the notes nor the CAD model was published.
- **Residual rights sit with the family.** Charles Ligeti's design notes are
  concrete works of his, held by his family. Ron Ligeti's CAD model is his own
  work. The project credits "the generosity of the family of the late Charles
  Ligeti, and the active contribution of his son Ron". TWITT says the organiser
  "has convinced Ron Ligeti to release his plans". So the consent on record
  covers Ron's plans. Whether it also covers his father's notes is not stated.
- **The project dates from mid-2006.** The earliest Wayback capture of
  ligetistratos.com is 11 June 2006, and the Google Code repository's first
  commit is dated 31 July 2006. The 2008 TWITT talk came two years in. From
  about 2010 the domains were taken over by spam (pharmacy pages on
  ligetistratos.com; directory and electric-car pages on ligeti-stratos.com).
  Today ligeti-stratos.com refuses connections, and ligetistratos.com redirects
  to a domain sales page. The 2006 captures are the primary record.
- **Airframes: accounts conflict, but at least one survives in a museum.** Three
  were built (Wikipedia; aeropedia). One crashed and killed the designer on 22
  September 1987 near Penfield, Victoria (AHSA, citing ATSB report 198701462).
  The others are reported at Holbrook and near Ballarat/Bendigo (aeropedia, L).
  The 2006 project page calls the original prototype "the sole remaining copy",
  held by Ron Ligeti (P).

## What was actually released

| Item | What the record shows | Source and quality |
|---|---|---|
| Project website, concept page (ligetistratos.com, captured 11 June 2006; ligeti-stratos.com, 2 July 2006 and 28 July 2012) | "Ron Ligeti and his family have agreed to release the new "Second Generation" Ligeti Stratos as Open Source. The designs, specifications, supplier lists and supporting documentation will be made available to the worldwide aviation community through a gratis "Attribution-NonCommercial-ShareAlike" licence currently under development. The license will specifically address safety and other concerns unique to aircraft design and construction." | Wayback captures, read 2026-10-24. P. |
| Licence text on either domain | **None found.** No archived URL on either domain names a licence. The 2012 FAQ page contains no licence terms | Wayback CDX for both domains. P for the absence, as far as captures reach. |
| Google Code project `ligeti-stratos` | "Worlds first Open Source Aircraft". `license: gpl2`, `contentLicense: ""`, `hasSource: false`. Labels include CharlesLigeti, RonLigeti, ChristopherAlan | Google Code Archive project.json. P. |
| Downloads, source and issues in that archive | None: all return 403, and the wiki list is null. **Control:** the same URLs for `protobuf` return 200 and 206, so 403 here means absent, not blocked | Google Code Archive. P. |
| GitHub export (AukeHoekstra/ligeti-stratos, 3 October 2015) | `master`: one commit, "Initial directory structure." (31 July 2006, author "nobody"), with no files. `wiki`: ProjectHome.md only. No licence file | GitHub API. P. |
| Announcement text (website and Google Code) | "Through the generosity of the family of the late Charles Ligeti, and the active contribution of his son Ron, an accomplished aeronautical engineer, the Ligeti Stratos has been made available as what is hoped to be the first of a complete line of Open Source aircraft." | Both of the above. P. |
| Consent, as reported | Christopher Alan "has convinced Ron Ligeti to release his plans with the promise that a web site will be developed", giving the site as http://www.ligetistratos.com/ | TWITT No. 262, April 2008. S. |
| "Plans" on model-aircraft sites (AeroFred, the-blueprints) | R/C model plans and three-views by third parties. Not the aircraft's design data | L. |

**Reading.** Bill's caution is borne out, for a sharper reason than first
thought. The family announced an open release in 2006, but under a
NonCommercial-ShareAlike licence that was still "under development" six years
later. No licence text was ever found. The only formal label, GPL v2, sits on an
empty repository and conflicts with the announced terms. On the public record,
no design file is available under terms AeroCommons can rely on. The design
data that does exist (the notes and the CAD model) is with the family.

## What survives and where

| Item | Account | Source and quality |
|---|---|---|
| Charles Ligeti's design notes | Ron Ligeti "sorted through the design notes like a jigsaw puzzle and correlated them to the aircraft" (2006). Charles "built everything on the fly using notes ... most of the information was locked away in his head" | Project status page, Wayback 2 July 2006. P. |
| Ron Ligeti's CAD model | Ron's dataset "started with a CATIA V4 model he drew after work"; "Ron is now converting the CATIA V4 data to CATIA V5" (2006). "Is in the CAD drawing stages" (2008) | Project status page, P; TWITT, S |
| Original drawings | None, per the 2008 talk: "there were no drawings or design specifications Ron could work with to produce and similar aircraft" [sic] | TWITT No. 262. S. |
| The original prototype | "the sole remaining copy of which is in his possession" (Ron's, 2006). In 2008, Ron "does have the original airframe", kept "in flying condition but has not flown" | Project status page, P; TWITT, S |
| The fatal-crash aircraft | Crashed 22 September 1987 near Penfield, Victoria. AHSA calls it the first production Mk II and says "The damaged aircraft was repaired and is on display at the Ballarat Air Museum, Victoria." AHSA puts "some 340 hours" on the Mk I prototype; aeropedia puts 340 hours on the crashed aircraft; TWITT says over 700 hours in all. Wikipedia calls the crashed aircraft the prototype | AHSA, S; aeropedia, L; TWITT, S; Wikipedia, L |
| A second airframe | "crashed at Mangalore injuring the pilot and it was restored to static display standard at Holbrook for the Australian Ultralight Museum", registered 19-7441, c/n S3-001 | aeropedia, L |
| A third, unfinished | "only a fibreglass shell and was not completed but has survived", on display "at a museum in the Ballarat / Bendigo area" | aeropedia, L |
| Public data | Jane's 1987-88 figures, via Wikipedia (span 5.36 m, wing area 7.53 m², MTOW 188 kg, Wortmann airfoil, König SD 570 at 21 kW). Spec pages for the first-generation prototype and second-generation production aircraft are archived on ligeti-stratos.com (2012-2015 captures). TWITT No. 262 reproduces spec sheets and CAD views. ATSB report 198701462 | L; P (archived pages, ATSB report not read); S |

Three accounts of which airframe is where do not agree: the 2006 project page,
AHSA and aeropedia. The museum holdings are the likeliest survivors to measure.
Visiting or asking any museum, or the family, is contact and Bill's call.

## Holder of residual rights

- **Charles Ligeti's design notes** are his own works. On his death in 1987
  they passed to his estate or heirs. On the public record that is his family,
  and they hold the notes physically.
- **Ron Ligeti's CAD model and plans** are his own works. The consent on record
  ("convinced Ron Ligeti to release his plans") covers these. Whether the family
  consent also extends to Charles's notes is not stated anywhere found.
- **Christopher Alan** organised the project and ran the website. Any material
  he authored is his, unless it was licensed.
- **Ligeti Aero-Nautical Pty Ltd**, the manufacturer named by Wikipedia (AHSA
  and aeropedia use "LGT Aero Nautical"): corporate status not checked. ASIC
  records were not searched.
- **Copyright term.** Charles Ligeti died in 1987. If Australian law gives his
  works life plus 70 years, they stay protected until the end of 2057. That is
  an attorney question, not a conclusion.
- **Patents.** TWITT records that "The fact that the patents on this design
  configuration also made it easier to convince Ron of the benefits of this
  approach." The sentence is garbled; a missing word such as "expired" is
  likely, but that is an inference. The record mentions configuration patents,
  and none has been identified or searched. Any patent from the 1980s would have
  expired by now. Listed as an open item.
- **Trademarks:** "STRATOS" is a common mark in other industries; not checked.

## The path for AeroCommons

| Path | What it would take | Assessment |
|---|---|---|
| **Use the announced open release** | Obtain the actual licence text and files. | **Not available.** No licence text was ever published, and the announced terms are NonCommercial-ShareAlike, which may not suit a non-profit that distributes plans and enables kits. Even if the files surfaced, the terms would need counsel. |
| **License from the family** | Written terms from Ron Ligeti and the family, covering both Charles's notes and Ron's CAD model, ideally under terms that suit AeroCommons. | The most promising route. The family wanted the design open in 2006. Requires contact: Bill's call. |
| **Re-derive from public data** | Jane's figures, archived spec pages, TWITT's spec sheets and CAD views, photographs, the ATSB report; measure a museum airframe. | Feasible for a planform study (AERO, AER-3807). Watch the safety history: the fatal Mk II had full-span elevators on the canard, and AHSA, citing the ATSB, describes a "full canard stall followed by a rapid nose down pitch". |
| **Buy** | Nothing commercial to buy. | Not applicable. |

## Where an aviation IP attorney is needed

1. **The announced NonCommercial term.** What would an
   "Attribution-NonCommercial-ShareAlike" licence mean for a non-profit that
   distributes plans free and enables third parties to sell kits? Does an
   announced but unpublished licence bind or grant anything?
2. **The conflict between signals.** GPL v2 on the Google Code project against
   the NonCommercial-ShareAlike licence announced on the website. Which, if
   either, governs any material, given that neither has a published text
   covering files?
3. **Whose consent covers what.** Ron Ligeti's consent covers his plans. Does
   the family's consent, as published, extend to Charles Ligeti's notes? Who in
   the family or estate can license those?
4. **GPL v2 for aircraft designs**, if files ever surface under it: what counts
   as "source", and what copyleft means for derivative designs and kits.
5. **Australian copyright term and ownership** for Charles Ligeti's works, and
   for the company's if it held any.

## Open items

- Patent search on the Stratos configuration (joined wing, ducted fan) for
  Charles Ligeti, 1980s, in Australia and the US.
- ATSB report 198701462: read in full.
- ASIC status of Ligeti Aero-Nautical Pty Ltd.
- Which museum holds which airframe (Holbrook, Ballarat): resolve from public
  museum catalogues.
- The archived spec pages (first-generation prototype, second-generation
  production) for AERO's planform study.

## Sources

- ligetistratos.com, concept page, Wayback capture of 11 June 2006 (P).
  https://web.archive.org/web/20060611225602/http://www.ligetistratos.com:80/concept.htm
- ligeti-stratos.com, concept page, Wayback 2 July 2006 and 28 July 2012; project
  status page, Wayback 2 July 2006 (P).
  https://web.archive.org/web/20060702121649/http://www.ligeti-stratos.com:80/concept.htm
  https://web.archive.org/web/20120728095846/http://ligeti-stratos.com:80/concept.html
  https://web.archive.org/web/20060702121701/http://www.ligeti-stratos.com:80/project_status.htm
- Wayback CDX listings for both domains, read 2026-10-24 (P).
- Google Code Archive, project `ligeti-stratos`, project.json and wikis.json;
  control project `protobuf`. Read 2026-10-24 (P).
  https://storage.googleapis.com/google-code-archive/v2/code.google.com/ligeti-stratos/project.json
- GitHub, AukeHoekstra/ligeti-stratos, branches `master` and `wiki`, read via the
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
