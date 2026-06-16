import requests
import json

def get_govuk_ai_policy():
    url = "https://www.gov.uk/api/search.json?q=artificial+intelligence&filter_content_store_document_type=policy_paper"

    headers = {
        "Accept": "application/json",
        "User-Agent": "ai_policy_tracker/1.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching GOV.UK data: {e}")
        return
    except json.JSONDecodeError as e:
        print(f"Error parsing GOV.UK response: {e}")
        return

    documents = []

    for item in data.get("results", []):
        document = {
            "title": item.get("title", "No title"),
            "description": item.get("description", "No description available"),
            "date": item.get("public_timestamp", "No date"),
            "url": "https://www.gov.uk" + item.get("link", ""),
            "source": "Gov.UK"
        }
        documents.append(document)

    with open("data/govuk.json", "w") as f:
        json.dump(documents, f, indent=2)

    print(f"Saved {len(documents)} documents to data/govuk.json")

if __name__ == "__main__":
    get_govuk_ai_policy()