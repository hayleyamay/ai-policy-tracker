import requests
from bs4 import BeautifulSoup

def get_eu_ai_policy():
    url = "https://artificialintelligenceact.eu/implementation-documents/"

    headers = {
        "User-Agent": "ai_policy_tracker/1.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    documents = soup.find_all("h4")

    for doc in documents: 
        print(doc.text)
        date = doc.find_next_sibling()
        if date:
            print(date.text.strip())
        print("---")

get_eu_ai_policy()