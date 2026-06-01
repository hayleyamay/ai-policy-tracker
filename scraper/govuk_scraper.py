import requests 
import json 
def get_govuk_ai_policy():
    url = "https://www.gov.uk/api/search.json?q=artificial+intelligence&filter_content_store_document_type=policy_paper"

    headers = {
        "Accept": "application/json",
        "User-Agent": "ai_policy_tracker/1.0"
    }

    response = requests.get(url, headers=headers)
    data = response.json() 
    
    documents = []

    for item in data["results"]:
        document = {
            "title": item["title"],
            "description": item["description"],
            "date": item["public_timestamp"],
            "url": "https://www.gov.uk" + item["link"],
            "source": "Gov.UK"
        } 
        documents.append(document)
    with open("data/govuk.json", "w") as f:
        json.dump(documents, f, indent=2)
    
    print(f"Saved {len(documents)} documents to data/govuk.json")

get_govuk_ai_policy() 