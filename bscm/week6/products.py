import requests
import pandas as pd

req = requests.get("https://dummyjson.com/products?limit=194")

brand = input("Give me the brand")

if req.status_code == 200:
    data = req.json()
    products = data["products"]
    
    array = []
    for product in products:
        if "brand" in product:
            if product["brand"] == brand:
                print(product["id"])
                mappedArray = [
                    product["id"],
                    product["title"],
                    product["brand"],
                    product["description"],
                    product["category"],
                    product["price"],
                    product["stock"]
                ]

                array.append(mappedArray)

    headers = [ "id", "title", "brand", "description", "category", "price", "stock"]

    products = pd.DataFrame(array, columns=headers)

    products.to_excel(f"./{brand}_products_from_api.xlsx", index = False)
else: 
    print("Iets fout gegaan in de API")