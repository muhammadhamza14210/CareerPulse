import os
import requests
import pandas as pd
from time import sleep 
from dotenv import load_dotenv
from config.dev_constants import COUNTRIES, QUERIES, PAGES

def run_scraper():
    load_dotenv()
    APP_ID = os.getenv('ADZUNA_APP_ID')
    APP_KEY = os.getenv('ADZUNA_APP_KEY')

    BASE_URL = "https://api.adzuna.com/v1/api/jobs"
    results = []
    request_count = 0

    for country, cities in COUNTRIES.items():
        for city in cities: 
            for query in QUERIES:
                for page in PAGES:
                    print(f"{country.upper()} | {city.title()} | {query} | Page {page}")
                    
                    url = f"{BASE_URL}/{country}/search/{page}"
                    params = {
                        'app_id': APP_ID,
                        'app_key': APP_KEY,
                        'what': query,
                        "where": city,
                        "results_per_page": 50,
                        "content-type": "application/json"
                    }
                    
                    try:
                        res = requests.get(url, params=params)
                        request_count += 1
                        
                        if res.status_code != 200:
                            print(f"Error {res.status_code}: {res.text}")
                            break
                        jobs = res.json().get("results", [])
                        for job in jobs:
                            results.append({
                                "country": country,
                                "city": city,
                                "query": query,
                                "title": job.get("title"),
                                "company": job.get("company", {}).get("display_name"),
                                "location": job.get("location", {}).get("display_name"),
                                "created": job.get("created"),
                                "description": job.get("description"),
                                "category": job.get("category", {}).get("label"),
                                "salary_min": job.get("salary_min"),
                                "salary_max": job.get("salary_max"),
                                "contract_type": job.get("contract_type")
                            })

                        sleep(1.5)
                        
                    except Exception as e:
                        print("💥 Exception:", e)
                        continue

    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(results)
    df.to_csv("data/jobs_raw.csv", index=False)

    print(f"\nSaved {len(df)} jobs to data/jobs_raw.csv")
    print(f"Total API requests made: {request_count}")
