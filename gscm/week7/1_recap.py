firstname = "Collin"
lastname = "Van der Vorst"
age = 34
height = float(input("Give me your height"))
goats = ["T-rex", "Connie", "Clyde"]
print(goats[0]) # t-rex
isAwesome = True

if height > 1.5: 
    print("Normal height")
elif height > 1:
    print("midget")
else:
    print("You have a problem")

cmd = input("Wassup?")

while cmd != "stop":
    print("gooooood")
    cmd = input("Wassup?")

for i in range(1, 11):
    print(i)

for goat in goats:
    print(goat)

