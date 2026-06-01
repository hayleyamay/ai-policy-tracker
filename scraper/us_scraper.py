import requests 
import json 
def get_us_ai_policy():
    api_key = "CrAOq4650zQ6b9vhx5ixG6iWBfjuV5lhYPzOQmUk"
    url = f"https://api.congress.gov/v3/bill?query=artificial+intelligence&sort=updateDate+desc&api_key={api_key}"

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    documents = []

    for item in data["bills"]:
        document = {
            "title": item["title"],
            "date": item["latestAction"]["actionDate"],
            "action": item["latestAction"]["text"],
            "chamber": item["originChamber"],
            "url": item["url"],
            "source": "US Congress"
        } 
        documents.append(document)
    with open("data/us.json", "w") as f:
        json.dump(documents, f, indent=2)
    
    print(f"Saved {len(documents)} documents to data/us.json")

get_us_ai_policy()
