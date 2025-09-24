import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")
API_HOST = "jsearch.p.rapidapi.com"

def search(query, country="us", date_posted="all", employment_types="FULLTIME", page=1, num_pages=1):
    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }

    params = {
        "query": query,
        "country": country,
        "date_posted": date_posted,
        "employment_types": employment_types,
        "page": page,
        "num_pages": num_pages,
        "language": "en"
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status() 
    return response.json().get("data", [])

def details(job_id, country="us"):
    url = "https://jsearch.p.rapidapi.com/job-details"

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }

    params = {
        "job_id": job_id,
        "country": country
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json().get("data", [])
