import requests 

latitude = "51.026905620906035"
longitude = "4.479330289108647"
result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")

if result.status_code == 200:
    data = result.json()
    print(data["current"]["temperature_2m"])
else:
    print("f")