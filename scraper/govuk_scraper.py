import requests 
def get_govuk_ai_policy():
    url = "https://www.gov.uk/api/search.json?keywords=artificial+intelligence&filter_content_store_document_type=policy_paper"
   
    response = requests.get(url)
    data = response.json()

    print(type(data["search_results"]))
    print(len(data["search_results"]))
    print(data["search_results"][0])

get_govuk_ai_policy() 