import requests
import json 
from bs4 import BeautifulSoup

def get_eu_ai_policy():
    url = "https://artificialintelligenceact.eu/implementation-documents/"

    headers = {
        "User-Agent": "ai_policy_tracker/1.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    headings = soup.find_all("h4")

    documents = []

    for doc in headings: 
        date = doc.find_next_sibling()
        document = {
            "title": doc.text.strip(),
            "date": date.text.strip() if date else "No Date",
            "source": "EU AI Act Tracker",
            "url": "https://artificialintelligenceact.eu/implementation-documents/"
        }
        documents.append(document)
    with open("data/eu.json", "w") as f:
        json.dump(documents, f, indent=2)

    print(f"Saved {len(documents)} documents to data/eu.json")

get_eu_ai_policy()