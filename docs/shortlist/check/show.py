import json,sys
d=json.load(open(sys.argv[1]))
def v(x): return x.get('v') if isinstance(x,dict) else x
for k in ['variant','config','wing','canard_or_htail','vtail','fuselage','nacelles_or_booms','gear','cooling','prop','engine','weights','fuel_usable']:
  x=d.get(k)
  if isinstance(x,dict) and 'v' not in x: print(k, {a:(v(b)) for a,b in x.items() if a!='note'})
  else: print(k, v(x) if isinstance(x,dict) else x)
for p in d['perf_points']: print(' P', {a:p.get(a) for a in ['ktas','alt_ft','power_pct_or_hp','gph','weight_lb','grade']}, (p.get('note') or '')[:120])
print('3v', d.get('three_view_urls'))
