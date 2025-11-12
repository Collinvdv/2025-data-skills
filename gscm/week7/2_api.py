import requests

# get data from an api 
res = requests.get("https://dummyjson.com/products")

# check the status code, 200 = success, 404 = can not found, 500 = server broken
if res.status_code == 200:
    # sweet I have some data it is json, so I need to use json()
    response = res.json()
    
    # woopsie a lot of information I only need the products array
    products = response["products"]

    # I will now loop over every single product, bcs I want to check if the raing
    # is heigher than 4 to print it out
    for product in products:
        if product['rating'] > 4:
            print(f"{product['title']} has a rating of {product['rating']}")
else:
    print("Can not reach it")