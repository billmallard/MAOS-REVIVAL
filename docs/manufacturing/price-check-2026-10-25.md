# Public price check: tooling board, print bureaus and cutting services

**AER-3868, 2026-10-25, MANUFACTURING.** These are public catalogue pages,
fetched by curl on 2026-10-25 and read from the page source. No account was
made, no file was uploaded to an instant-quote engine, and no vendor was
contacted. A catalogue price is a list price for one unit, not a quote. Freight
is extra unless stated.

## What it changes

1. **Plug material: the stage 4 band of $15-40 per ft2 holds, but only for
   urethane board.** Facings of 15 lb/ft3 HDU, 1-2 in thick over a cheap core,
   come to about $15-30 per ft2 of plug surface. Epoxy tooling board at its
   retail block price comes to about $220 per ft2 at 2 in. That is 5-7 times
   over the band, so it belongs on small precision tools or prepreg tools only.
   The build plans assume room-temperature or low-temperature infusion into
   glass/epoxy female molds pulled from HDU plugs. A prepreg route on epoxy
   board would break the tooling bands.
2. **Print bureaus publish no price for a part at mold scale.** Every bureau we
   read prices per part through an upload. Printed tooling stays uncredited in
   the bands, as in stage 4.
3. **Stage 4 was wrong about 2024-T3.** It said a home router or a full-service
   shop was the only route to 0.032-0.040 in 2024-T3. OSH Cut's 2024-T3
   material page lists sheet for laser cutting at 0.032, 0.04, 0.05, 0.063,
   0.08, 0.09, 0.1, 0.125 and 0.19 in, with a maximum part of 119 x 47 in. So
   the Prescott's 0.032 ribs, 0.040 leading edges and 0.050 spar web can all be
   cut from files by a service, and so can the Aries skins, spliced to 119 in.
   One limit remains: neither service lists bending for 2024-T3. (Revised
   2026-10-26: the first version read OSH Cut's summary list at `/materials`,
   which showed fewer gauges, and said no service listed 0.032 in. AERO's
   review caught it.)
4. **Tube cutting for a welded 4130 cage is not orderable off the shelf
   today.** SendCutSend's tube service is on a waitlist. OSH Cut cuts 4130 tube,
   but lists only round profiles. The Prescott cage is square 4130.

## Tooling board

| Product | Seller (page) | Size | List price, qty 1 | Per ft3 | Per ft2 of plug surface | Notes |
|---|---|---|---|---|---|---|
| Precision Board PBLT-15 HDU, 15 lb/ft3 | Interstate Advanced Materials ([page](https://interstateam.com/hdu_board_high_density_urethane_pblt15_50986.php)) | 0.5 x 20 x 60 in | $62.63; $60.75 at 10-19, $56.37 at 50+ | $180 | 1 in facing about $15; 2 in about $30 (E: assumes price scales with thickness, which the page does not show) | Shipping estimate on the page: $97.22 to ZIP 86401, for one sheet. "Prices are subject to change every 6 days" |
| Easy Composites EB700 epoxy tooling board, 700 kg/m3, service temperature 130 C | Easy Composites US ([page](https://www.easycomposites.us/eb700-high-temperature-epoxy-tooling-board)) | 250 x 250 x 50 mm (EB700-006-50; 2.19 kg) | $144.70 | about $1,310 | about $220 at 50 mm | Sold in 50 and 100 mm blocks up to 500 x 500 mm. Only the default block's price is in the page source; the larger blocks were not read |
| Last-A-Foam FR-3704.5, 4.5 lb/ft3 polyurethane | Aircraft Spruce ([page](https://www.aircraftspruce.com/catalog/cmpages/lastafoamFR37045.php)) | 3/8, 1/2, 3/4 x 48 x 96 in | $209.75, $278.00, $447.00 | $223 at 3/4 in | not a facing material | A core-density foam, listed as a cross-check: low-density urethane is not cheap bulk for plugs. A search summary gave $322 for the 1/2 in sheet; the page says $278 |

Not price-checked: EPS or XPS block for plug bulk, plug-surfacing compounds,
mold gelcoat and laminate. Those stay in the stage 4 build-up as estimates.

## Print bureaus

| Bureau (page) | What the page publishes | Price published? |
|---|---|---|
| Xometry FDM ([page](https://www.xometry.com/capabilities/3d-printing-service/fused-deposition-modeling/)) | Build volume "up to 24″ x 36″ x 36″" on Stratasys Fortus 400/450 (to 16 in) and F900 platforms; 0.013 in layers above 16 in; minimum wall 0.047 in under 16 in and 0.060 in above | No; instant quote by upload |
| Additive Plus, Los Angeles ([FDM page](https://additiveplus.com/product/fdm-3d-printing-services/)) | FDM "priced per part" with a "$50 minimum"; materials include ABS, ASA, PETG-CF, PA6-CF, PPS-CF and ULTEM 1010 on request; a separate large-format pellet (FGF) service lists "Parts up to 2 m" | No; the page's estimator returns a price only after an upload |

What this means for tooling (E, from published large-format tooling work:
Corum et al., SFF Symposium 2023, on printed CF-ABS expansion; SABIC and
Tru-Design on PEI autoclave tools): a printed mold is chosen by its cure
temperature. ABS or ASA suits a
room-temperature infusion. A heated post-cure wants PPS-CF or ULTEM-class
material, with the long axis laid along the bead. Xometry's 36 in envelope
makes tiles, not a wing-skin mold. A 2 m pellet print covers a cowl half or a
radiator duct in one piece.

## Cutting services (for the build-plan routes)

| Service (page) | Line | What the page says |
|---|---|---|
| SendCutSend ([2024-T3](https://sendcutsend.com/materials/laser-cut-2024-aluminum/)) | 2024-T3 sheet | "SendCutSend offers 2024 T3 Aluminum in one thickness option: .025″". Instant pricing to 30 x 44 in; 30 x 56 in by custom quote; +/-0.005 in; 2-4 days production |
| SendCutSend ([tube](https://sendcutsend.com/services/tube-cutting/)) | Laser tube cutting | "Our tube cutting capacity is currently limited, and we are not accepting new orders at this time." Starting from $39 per order; +/-0.005 in |
| OSH Cut ([2024-T3 material page](https://www.oshcut.com/materialdetails/aluminum-2024-t3), read 2026-10-26) | 2024-T3 sheet | Laser cutting at 0.032, 0.04, 0.05, 0.063, 0.08, 0.09, 0.1, 0.125, 0.19 in; maximum part 119 x 47 in; no bending listed for 2024-T3. The summary list at `/materials` showed fewer gauges on 2026-10-25; cite the detail page |
| OSH Cut ([materials](https://www.oshcut.com/materials)) | 4130 | Annealed 4130 sheet from 0.04 in; cold-drawn 4130 tube, round only in the list read, 0.625-2 in OD (for example 0.75 x 0.035, 1.25 x 0.065) |

## Regenerating

The prices above were read from the HTML of each page. To re-read one:

```sh
curl -sL --compressed -A "Mozilla/5.0" <page> | python3 -c "import sys,re,html; t=html.unescape(re.sub(r'<[^>]+>',' ',sys.stdin.read())); print(re.findall(r'.{0,100}\\$[0-9][0-9,.]*.{0,40}', t))"
```

Catalogue prices move: the HDU page says its prices change every 6 days.
Re-read before relying on any line here.
