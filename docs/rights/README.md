Stage output lands here. See ../BRIEF.md.

One file per candidate: who holds the type certificate, the drawings and
tooling, any kit or plans rights, trademarks and live patents, and the paths to
a revival. This is research, not legal advice. Nobody contacts a rights holder
without Bill's go-ahead.

## Reading the FAA type-certificate record (DRS)

The FAA Dynamic Regulatory System (DRS) is the primary source for TCDS holder,
status and revision. It needs no account or API key, only a guest session:

```sh
# 1. Guest session (sets cookies; without it the API returns 403)
curl -s -c jar -b jar -L -o /dev/null https://drs.faa.gov/guest/login

# 2. TCDS metadata. Filter keys: "TCDS Number", "TC Holder",
#    "Former TC Holders", "Model", "Status", "Keyword". page is zero-based, 25 rows.
curl -s -c jar -b jar -H "Content-Type: application/json" \
  -H "Origin: https://drs.faa.gov" -X POST \
  https://drs.faa.gov/api/browse/doctype/TCDSMODEL/documents/metadatas \
  -d '{"filters":{"TCDS Number":["A6SW"]},"page":0}'

# 3. Version history:  GET /api/browse/documents/history/{id}?docTypeId=44
# 4. The PDF:          GET /api/content/alf/{id}   (id is the record GUID)
```

Filter values must match DRS's option lists exactly. Sending a `null` body
returns them in `metaDataConfig.filters[].optionValues`. Before you record that a
TCDS does not exist, run a positive control: a filter that should return a
known record. For example, `"Model":["M22"]` returns exactly one record.
