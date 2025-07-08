import os
import requests
import pandas as pd
from time import sleep 
from dotenv import load_dotenv
from config.constants import COUNTRIES, QUERIES, PAGES

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
                    print(f"🔎 {country.upper()} | {city.title()} | {query} | Page {page}")
        