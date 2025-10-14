#(gewicht(kg) / height(m)​ ^ 2
# 3 variables met correcte type
# lengte (1 meter 94), gewicht (85kg), resultaat (22.6)
# O: gezond gewicht

# ik wil functie bmiBerekenen(85, 1.94)
def bmiBerekenen(h, w):
    return round(w / (h ** 2))

weight = float(input("Weight:"))
height = float(input("Height:"))
bmi = bmiBerekenen(height, weight)
print(bmi)

print(bmiBerekenen(1.94,85))