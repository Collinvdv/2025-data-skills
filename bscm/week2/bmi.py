#(gewicht(kg) / height(m)​ ^ 2
# 3 variables met correcte type
# lengte (1 meter 94), gewicht (85kg), resultaat (22.6)
# O: gezond gewicht

# kleiner dan 18.5= ondergewicht
# tussen 18.5 en kleiner dan 25 = gezond gewicht
# groter dan 25 overgewicht

weight = float(input("Weight:"))
height = float(input("Height:"))
bmi = weight / (height ** 2)
print(f"Jouw bmi is {round(bmi, 2)}")

if bmi < 18.5:
    print("Eat some proteins")
elif bmi < 25:
    print("Healthy")
else: 
    print("Overgewicht")