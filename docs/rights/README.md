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

## Abandoned type certificates: 49 USC 44704(a)(5)

The FAA can release a type certificate's engineering data on request if the TC
has been inactive for 3 or more years and the FAA, using due diligence, cannot
find the owner of record or an heir. A third-party FOIA request starts it. The
FAA writes to the holder's last known address, then publishes a Federal Register
"Notice of Intent to Designate as Abandoned" with a comment deadline. If nobody
answers, the TC is designated abandoned and the data is released. DRS then
shows the TC as "Historical", sub-status "Abandoned". Example: Wing D-1
Derringer, TC A9WE, 87 FR 40578 (7 July 2022), docket FAA-2022-0363.

Whole-TC notices are rare. A Federal Register search on 2026-10-24 found three:
A9WE (2022), H2EU (2015), and a restricted-category group (68 FR 47379, 2003).
The same process is used far more often for STCs.

What a recipient may do with released data is not settled by the notice. That
is a question for counsel. Filing such a request is an outward act: it prompts
the FAA to contact the holder, so it needs Bill's go-ahead.

```sh
curl -s -G https://www.federalregister.gov/api/v1/documents.json \
  --data-urlencode 'conditions[term]="Designate as Abandoned" "Type Certificate"' \
  --data-urlencode 'conditions[agencies][]=federal-aviation-administration' \
  --data-urlencode 'per_page=100' --data-urlencode 'fields[]=citation' \
  --data-urlencode 'fields[]=title'
```

## DRS notes

Filter values must match DRS's option lists exactly. Sending a `null` body
returns them in `metaDataConfig.filters[].optionValues`. Before you record that a
TCDS does not exist, run a positive control: a filter that should return a
known record. For example, `"Model":["M22"]` returns exactly one record.
