"""
Run the "Internship Jobs Scraper — New Grad, Stage & Alternance Feed" Apify Actor and print its results.

Setup:
    pip install -r requirements.txt
    export APIFY_TOKEN=your_apify_token   # Apify Console > Settings > API & Integrations

This repository only documents the Actor; its source code runs on Apify's infrastructure.
"""
import os
import sys

from apify_client import ApifyClient

ACTOR_ID = "leadsbrary/early-career-internship-jobs-feed"

RUN_INPUT = {
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


def main() -> None:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set the APIFY_TOKEN environment variable first (Apify Console > Settings > API & Integrations).")
    client = ApifyClient(token)
    print(f"Starting {ACTOR_ID} ...")
    run = client.actor(ACTOR_ID).call(run_input=RUN_INPUT)
    print(f"Run finished with status: {run['status']}")
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)


if __name__ == "__main__":
    main()
