import requests

def getQuote():
    result = requests.get("https://api.kanye.rest/")

    if result.status_code == 200:
        data = result.json()
        print(data["quote"])
    else: 
        print("Ergens een foutje")

for i in range(1,11):
    getQuote()