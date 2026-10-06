#!/usr/bin/env bash
# Run the "Internship Jobs Scraper — New Grad, Stage & Alternance Feed" Apify Actor synchronously and print the dataset items.
# Usage: export APIFY_TOKEN=your_apify_token && ./run.sh
set -euo pipefail
: "${APIFY_TOKEN:?Set APIFY_TOKEN first (Apify Console > Settings > API & Integrations)}"

curl -sS -X POST "https://api.apify.com/v2/acts/leadsbrary~early-career-internship-jobs-feed/run-sync-get-dataset-items" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d @- <<'JSON'
{
  "roleTypes": [
    "internship",
    "new_grad"
  ],
  "useDefaultCompanies": true,
  "companies": [],
  "countries": [],
  "keywords": [],
  "remoteOnly": false,
  "postedWithinDays": 30,
  "onlyNew": false,
  "stateKey": "default",
  "includeDescription": false,
  "maxResults": 3,
  "proxyConfiguration": {
    "useApifyProxy": true
  }
}
JSON
