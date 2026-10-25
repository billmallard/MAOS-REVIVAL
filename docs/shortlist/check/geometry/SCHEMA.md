# Geometry + safety record file, one per aircraft: <id>.json

Every numeric field is an object: {"v": number, "unit": "ft|ft2|in|lb|gal|hp|deg|-", "grade": "F|T|P|B|R|E", "src": "URL", "note": "how derived / which variant"}.
Grades: F factory/brochure/designer; T type certificate data sheet; P flight test, POH or magazine pilot report; B builder/owner/registry; R measured record; E estimate (say whose, e.g. "E: scaled from three-view at <URL>").
Use null for a value you could not find; never invent. If you scale from a three-view drawing, say so and grade E.

{
 "id": "...", "variant": "which exact variant the geometry is for",
 "config": "tractor|pusher|canard pusher|push-pull twin|...",
 "wing": {"span":{}, "area":{}, "root_chord":{}, "tip_chord":{}, "sweep_le_deg":{}, "airfoil":"name(s)", "tc_root":{}, "tc_tip":{}, "winglets": "yes/no + height/area if known"},
 "canard_or_htail": {"kind":"canard|htail|none", "span":{}, "area":{}, "chord":{}, "airfoil":"", "tc":{}},
 "vtail": {"count": 1, "area_each":{}, "height":{}, "root_chord":{}, "tip_chord":{}, "note":"e.g. winglet rudders on canards"},
 "fuselage": {"length":{}, "max_width":{}, "max_height":{}, "cabin_width":{}, "note":""},
 "nacelles_or_booms": "description + dimensions if any (twins, boom tails)",
 "gear": "fixed / retractable / retractable nose only; fairings",
 "cooling": "air/liquid, inlet description, cowl flaps",
 "prop": {"diameter":{}, "blades": 2, "type":"fixed|constant speed", "rpm_cruise":{}},
 "engine": {"model":"", "hp":{}, "turbo": true, "dry_weight":{}},
 "weights": {"mtow":{}, "empty":{}, "max_landing":{}, "zero_fuel_max":{}},
 "fuel_usable":{},
 "perf_points": [ {"ktas":..., "alt_ft":..., "power_pct_or_hp":..., "gph":..., "weight_lb":..., "grade":"", "src":"", "note":""} ],
 "three_view_urls": ["..."],
 "safety": {
   "ntsb_total": {"v":N, "grade":"B", "src":"", "note":"date range, query used (make/model strings)"},
   "ntsb_fatal": {},
   "fleet_size_for_rate": {},
   "pattern": "plain-language summary of recurring causes; note explicitly anything tied to the configuration (canard deep stall/rain, pusher prop strike/fuel exhaustion, high wing loading stall-spin on approach, etc.). Distinguish record from your inference.",
   "notable": ["date - place - outcome - cause per NTSB, with NTSB number and URL"]
 },
 "why_died_detail": "anything beyond the stage-1 summary that bears on whether a revival fixes it",
 "rights_hints": "any ownership/provenance facts you came across (who sells plans/kits/TC now), with URL",
 "gaps": ["what you looked for and could not find"]
}
