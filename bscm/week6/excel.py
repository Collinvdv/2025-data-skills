import pandas as pd

array = [
    [ 1, "adidas", 10],
    [ 2, "nike", 20],
    [ 3, "puma", 30],
]

headers = [ "id", "name", "price"]

products = pd.DataFrame(array, columns=headers)

products.to_excel("./products2.xlsx", index = False)
print(products)