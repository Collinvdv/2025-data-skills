# Calculcate BMI 
# formula: weight (in kg ) / (height * height)
# 2 variables weight, height
# print out the bmi
# height 1.94, weight 86
# result 22.85
height = float(input("height")) # "1.94"
weight = float(input("weight"))

bmi = weight/ (height * height)
bmi2 = weight / (height**2) # ** -> power of 
bmi3 = weight / pow(height, 2)
print(bmi)
print(bmi2)
print(bmi3)