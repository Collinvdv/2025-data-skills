#(gewicht(kg) / height(m)​ ^ 2
# 3 variables met correcte type
# lengte (1 meter 94), gewicht (85kg), resultaat (22.6)
# O: 22

height = 1.94
weight = 85 

resultaat = weight / (height * height)
print(resultaat)

resultaat = weight / pow(height, 2)
print(resultaat)

resultaat = weight / height**2 # height ^ 2
print(resultaat)