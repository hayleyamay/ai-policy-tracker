import requests
import os
import json

def get_us_ai_policy():
    api_key = os.environ["CONGRESS_API_KEY"]
    
    headers = {
        "Accept": "application/json"
    }
    
    ai_keywords = [
        "artificial intelligence",
        " ai ",
        "machine learning",
        "algorithmic",
        "automated decision",
        "large language model"
    ]
    
    documents = []
    offset = 0
    limit = 250
    max_pages = 10
    page = 0

    try:
        while page < max_pages:
            url = f"https://api.congress.gov/v3/bill/119?sort=updateDate+desc&limit={limit}&offset={offset}&api_key={api_key}"
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            bills = data.get("bills", [])
            if not bills:
                break
                
            for item in bills:
                title = item.get("title", "")
                if any(keyword in title.lower() for keyword in ai_keywords):
                    document = {
                        "title": title,
                        "date": item.get("latestAction", {}).get("actionDate", "No date"),
                        "action": item.get("latestAction", {}).get("text", "No action recorded"),
                        "chamber": item.get("originChamber", "Unknown"),
                        "url": item.get("url", ""),
                        "source": "US Congress"
                    }
                    documents.append(document)
            
            offset += limit
            page += 1
            print(f"Searched page {page}, found {len(documents)} AI bills so far...")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching US Congress data: {e}")
        return
    except json.JSONDecodeError as e:
        print(f"Error parsing US Congress response: {e}")
        return
    
    with open("data/us.json", "w") as f:
        json.dump(documents, f, indent=2)
    
    print(f"Saved {len(documents)} documents to data/us.json")

if __name__ == "__main__":
    get_us_ai_policy()