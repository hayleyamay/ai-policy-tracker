import requests 
def get_us_ai_policy():
    api_key = "CrAOq4650zQ6b9vhx5ixG6iWBfjuV5lhYPzOQmUk"
    url = f"https://api.congress.gov/v3/bill?query=artificial+intelligence&sort=updateDate+desc&api_key={api_key}"

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    for item in data["bills"]:
        print(item["title"])
        print(item["latestAction"]["actionDate"])
        print(item["latestAction"]["text"])
        print(item["originChamber"])
        print(item["url"])
        print("---")

get_us_ai_policy()
