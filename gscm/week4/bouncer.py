# scenario 1: leeftijd vragen enkel tussen 18 en 65 binnen
# scenario 2: enkel vrouwen tussen 18 en 65
# scenario 3: enkel vrouwen tussen 18 en 65, maar als ze bribemoney geven
# dat hoger is als 20euro laat ik hen ook binnen
age = int(input("geef me je leeftijd"))
gender = input("geslacht") # F/M
bribemoney = int(input("geef je geld?"))

if (age >= 18 and age <=65 and gender =="f") or bribemoney > 20:
    print("enter")
else:
    print("don't enter")