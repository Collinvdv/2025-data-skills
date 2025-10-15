import requests 

latitude = "51.026905620906035"
longitude = "4.479330289108647"
response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")

if response.status_code == 200:
    data = response.json()
    temp = data["current"]["temperature_2m"]
    print(temp)
else:
    print("slecht overgetypt")