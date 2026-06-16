import requests
import json
from bs4 import BeautifulSoup

def get_eu_ai_policy():
    url = "https://artificialintelligenceact.eu/implementation-documents/"
    
    headers = {
        "User-Agent": "ai-policy-tracker/1.0"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching EU AI Act data: {e}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    headings = soup.find_all("h4")
    
    if not headings:
        print("Warning: No documents found — the page structure may have changed")
        return
    
    documents = []
    
    for doc in headings:
        date = doc.find_next_sibling()
        document = {
            "title": doc.text.strip(),
            "date": date.text.strip() if date else "No date",
            "source": "EU AI Act Tracker",
            "url": "https://artificialintelligenceact.eu/implementation-documents/"
        }
        documents.append(document)
    
    with open("data/eu.json", "w") as f:
        json.dump(documents, f, indent=2)
    
    print(f"Saved {len(documents)} documents to data/eu.json")

if __name__ == "__main__":
    get_eu_ai_policy()