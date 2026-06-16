import requests
import os
import json

def get_us_ai_policy():
    api_key = os.environ["CONGRESS_API_KEY"]
    url = f"https://api.congress.gov/v3/bill?query=artificial+intelligence&sort=updateDate+desc&api_key={api_key}"
    
    headers = {
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching US Congress data: {e}")
        return
    except json.JSONDecodeError as e:
        print(f"Error parsing US Congress response: {e}")
        return
    
    documents = []
    
    for item in data.get("bills", []):
        document = {
            "title": item.get("title", "No title"),
            "date": item.get("latestAction", {}).get("actionDate", "No date"),
            "action": item.get("latestAction", {}).get("text", "No action recorded"),
            "chamber": item.get("originChamber", "Unknown"),
            "url": item.get("url", ""),
            "source": "US Congress"
        }
        documents.append(document)
    
    with open("data/us.json", "w") as f:
        json.dump(documents, f, indent=2)
    
    print(f"Saved {len(documents)} documents to data/us.json")

if __name__ == "__main__":
    get_us_ai_policy()