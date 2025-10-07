# alle even getallen die deelbaar zijn door 7 tussen 50 en 100 
# je hebt if nodig en %
for nummertje in range(50, 101, 2):
    if nummertje % 7 == 0:
        print(nummertje)

goats = ["T-rex", "Connie", "Clyde"]

for goat in goats:
    print(goat)

grades = [10, 5, 20, 16, 9]
# Ik wil dat jullie alle gebuisde cijfers afprinten op 20
# for grade in grades:
#     if grade < 10:
#         print(grade)

# gemiddelde berekenen, for loop nodig evt ook len(grades)
avg = sum(grades) / len(grades)

print(avg)