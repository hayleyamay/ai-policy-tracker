import requests 
def get_govuk_ai_policy():
    url = "https://www.gov.uk/api/search.json?q=artificial+intelligence&filter_content_store_document_type=policy_paper"

    headers = {
        "Accept": "application/json",
        "User-Agent": "ai_policy_tracker/1.0"
    }

    response = requests.get(url, headers=headers)
    data = response.json() 

    for item in data["results"]:
        print(item["title"])
        print(item["description"])
        print(item["public_timestamp"])
        print("https://www.gov.uk" + item["link"])
        print("---") 

get_govuk_ai_policy() 