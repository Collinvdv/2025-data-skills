import requests

for i in range(1, 21):
    quote = requests.get("https://api.kanye.rest/")

    if quote.status_code == 200:
        actualQuote = quote.json()
        print(str(i) + " : " + actualQuote["quote"])