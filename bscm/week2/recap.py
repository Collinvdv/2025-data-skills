firstname = "Collin " # string
lastname = "Van der Vorst"
fullname = firstname + " " + lastname
firstname = "Collina"
fullname = firstname + " " + lastname
age = 34 # integer
height = 1.94 # float

height = 1.94 + 0.02
height += 0.02

# Collin is 1.98 m groot

print(firstname + " is " + str(height) + " m groot")
print(firstname, "is", height, "m groot")
print(f"{firstname} is {height} m groot")