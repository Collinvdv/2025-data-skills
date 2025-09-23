firstname = input("What is your name?")
product = input("What is your fav product")
units = int(input("How many units did you buy?"))

print(firstname + " bought " + str(units) + product)
print(firstname,"bought",units,product)
print(f"{firstname} bought {units} {product}")