# Internship Jobs Scraper — New Grad, Stage & Alternance Feed — Apify Actor usage guide

[![Run on Apify](https://img.shields.io/badge/Apify-Run%20this%20Actor-24C1E0)](https://apify.com/leadsbrary/early-career-internship-jobs-feed?fpr=aupara)
[![Try Apify free](https://img.shields.io/badge/Apify-Try%20it%20free-24C1E0)](https://console.apify.com/sign-up?fpr=aupara)

Internship jobs scraper for Greenhouse, Lever, Ashby & SmartRecruiters boards. Returns internship, new-grad, apprenticeship, stage and Werkstudent postings with company, country, remote flag, dates and URL as JSON/CSV. From $0.48 per 1,000 results.

> **This repository does not contain the Actor's source code.** The Actor is closed-source and
> runs on Apify's infrastructure. This repo is documentation plus ready-to-run client examples
> (curl, Python, JavaScript) that call the hosted Actor with **your own** Apify API token.

**Run it on Apify →** [https://apify.com/leadsbrary/early-career-internship-jobs-feed?fpr=aupara](https://apify.com/leadsbrary/early-career-internship-jobs-feed?fpr=aupara)

## What it does

Most career-page scrapers return every job of a company. This Actor does the opposite: it scans a built-in list of 60 verified US and EU employer boards (plus any boards you add), classifies each posting with a rule-based multilingual classifier (English, French, German, Spanish) and **only pushes — and bills — early-career roles**. Senior postings are never returned or charged.

Recognised types: `internship`, `new_grad`, `graduate_program`, `apprenticeship`, `working_student`, `entry_level`. Examples of terms it understands: intern, new grad, graduate programme, stage, alternance, apprentissage, Werkstudent, Praktikum, Ausbildung, prácticas.

Data source: the endpoints that Greenhouse, Lever, Ashby and SmartRecruiters publish so employers' jobs can be listed elsewhere. No login, no browser, no CAPTCHA.

## Use cases

- Daily 'new internships since yesterday' feed pushed to a Discord/Slack/Telegram bot via Apify schedules and webhooks
- Populating a university or bootcamp job board with fresh internship and graduate-programme postings
- France/EU coverage of stage, alternance, apprentissage and Werkstudent offers that US-centric lists miss
- Filtering early-career roles by country, remote, season (Summer 2027) or degree level for newsletters
- Tracking which companies open internship programmes and when (early-career hiring signals)


## Input

| Field | Type | Required | Description |
|---|---|---|---|
| `roleTypes` | array | no | Early-career types to keep. Leave empty for internship, new grad, graduate program, apprenticeship and working student. |
| `useDefaultCompanies` | boolean | no | Scan 60 verified US and EU employer boards on Greenhouse, Lever, Ashby and SmartRecruiters. |
| `companies` | array | no | Additional boards as 'ats:token' (greenhouse:stripe, lever:spotify, ashby:notion, smartrecruiters:BoschGroup) or a public board URL. Invalid entries are skipped with a warning. |
| `countries` | array | no | ISO 3166-1 alpha-2 codes to keep (e.g. FR, DE, US). Empty = all countries. |
| `keywords` | array | no | A posting must contain at least one of these in its title or department (case-insensitive). Empty = no filter. |
| `remoteOnly` | boolean | no | Keep only postings flagged remote. |
| `postedWithinDays` | integer | no | Keep postings published or updated in the last N days. 0 = no limit. Postings without a date are kept. |
| `onlyNew` | boolean | no | Return only postings not returned by a previous run with the same state key. |
| `stateKey` | string | no | Name of the incremental state, so several schedules can keep separate 'seen' lists. |
| `includeDescription` | boolean | no | Add the plain-text job description (larger dataset, extra requests for Greenhouse and SmartRecruiters). |
| `maxResults` | integer | no | Stop after this many postings (also caps your spending). |
| `proxyConfiguration` | object | no | Public APIs normally work without a proxy; the datacenter proxy is a safe default if a host rate-limits you. |

The full input form (with defaults and validation) is on the [Actor page](https://apify.com/leadsbrary/early-career-internship-jobs-feed?fpr=aupara).


## Output (sample item)

Sample trimmed for readability (long texts and lists are shortened) — a real run returns the complete data.

```json
{
  "jobId": "greenhouse:stripe:8194291",
  "title": "Data Analyst, Intern",
  "company": "Stripe",
  "ats": "greenhouse",
  "boardToken": "stripe",
  "earlyCareerType": "internship",
  "matchedTerm": "Intern",
  "location": "New York, Seattle, South San Francisco HQ",
  "country": "US",
  "remote": false,
  "department": null,
  "employmentType": null,
  "seasonHint": null,
  "degreeLevelHint": null,
  "language": "en",
  "postedAt": "2026-10-01T15:05:29.000Z",
  "updatedAt": "2026-10-01T15:05:29.000Z",
  "jobUrl": "https://stripe.com/jobs/search?gh_jid=8194291",
  "scrapedAt": "2026-10-05T21:03:07.793Z"
}
```

## Pricing

Pay only for results: about **$0.72 per 1,000 results** on the Apify Free plan, down to **$0.48 per 1,000** on paid Apify plans.

Apify platform usage (compute) is billed by Apify on top of the per-result price — about **$0.02 per 1,000 results** in our measured test runs (estimate, varies with input). Tip: keep only the output formats and options you need to reduce it.

Prices can change — the [Actor page](https://apify.com/leadsbrary/early-career-internship-jobs-feed?fpr=aupara) always shows the current pricing.

## Quick start

You need an Apify account and an API token (Apify Console → **Settings → API & Integrations**).
Never commit your token: export it as the `APIFY_TOKEN` environment variable.

### cURL

```bash
curl -X POST "https://api.apify.com/v2/acts/leadsbrary~early-career-internship-jobs-feed/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
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
```

### Python (`apify-client`)

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run_input = {
    "roleTypes": [
        "internship",
        "new_grad"
    ],
    "useDefaultCompanies": True,
    "companies": [],
    "countries": [],
    "keywords": [],
    "remoteOnly": False,
    "postedWithinDays": 30,
    "onlyNew": False,
    "stateKey": "default",
    "includeDescription": False,
    "maxResults": 3,
    "proxyConfiguration": {
        "useApifyProxy": True
    }
}

run = client.actor("leadsbrary/early-career-internship-jobs-feed").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### JavaScript (`apify-client`)

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const runInput = {
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
};

const run = await client.actor('leadsbrary/early-career-internship-jobs-feed').call(runInput);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

Runnable versions live in [`examples/`](./examples).

## Troubleshooting

- **401 / "User was not found or authentication token is not valid"** — check that `APIFY_TOKEN` is set and copied completely.
- **The run finished but the dataset is empty** — widen your search input or check the run log on the Apify Console.
- **Run stops early** — you may have reached the maximum cost per run you set in Apify; raise it in the run options.
- **Need something else?** Open an issue in this repository or use the Issues tab on the Actor page.

## Don't have an Apify account yet?

[Sign up here](https://console.apify.com/sign-up?fpr=aupara) — new accounts get $5 of free platform usage every month, enough to try most Actors without paying upfront.
Browse the full [Apify Store](https://apify.com/store?fpr=aupara) or [all Actors from this developer](https://apify.com/leadsbrary?fpr=aupara).

## Links

- Actor page: [https://apify.com/leadsbrary/early-career-internship-jobs-feed?fpr=aupara](https://apify.com/leadsbrary/early-career-internship-jobs-feed?fpr=aupara)
- All Actors from this developer: [https://apify.com/leadsbrary?fpr=aupara](https://apify.com/leadsbrary?fpr=aupara)
- Apify API reference: [https://docs.apify.com/api/v2](https://docs.apify.com/api/v2)

## Keywords

internship jobs scraper, new grad jobs api, internship api, graduate jobs feed, entry level jobs scraper, alternance offres scraper, stage offres scraper, werkstudent jobs, apprenticeship jobs scraper, greenhouse jobs scraper, lever jobs scraper, ashby jobs scraper, early career jobs, summer internship 2027, student jobs feed

#internships #newgrad #jobs #earlycareer #alternance #werkstudent #greenhouse #lever #ashby #jobfeed #apify

## License

The example code in this repository is released under the MIT License — see [LICENSE](./LICENSE).
It does not cover the Actor itself, which remains closed-source and is operated by its developer on Apify.
