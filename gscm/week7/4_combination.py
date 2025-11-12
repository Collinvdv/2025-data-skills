import requests
import pandas as pd

# get data from an api 
res = requests.get("https://dummyjson.com/products")

# check the status code, 200 = success, 404 = can not found, 500 = server broken
if res.status_code == 200:
    # sweet I have some data it is json, so I need to use json()
    response = res.json()
    
    # woopsie a lot of information I only need the products array
    products = response["products"]

    # So i got an array of products, now lets make a connection with excel 
    rows = []

    for product in products:
        rows.append([
            product["id"],
            product["title"],
            product["price"],
            product["rating"],
        ])
    
    headers = ["id", "title", "price", "rating"]

    dataframe = pd.DataFrame(rows, columns=headers)

    dataframe.to_excel("./products_from_api.xlsx", index=False)
else:
    print("Can not reach it")