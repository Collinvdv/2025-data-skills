import requests

response = requests.get("https://api.kanye.rest/")

if response.status_code == 200:
    data = response.json()
    print(data["quote"])
else:
    print(response.status_code)
    print("noooop")