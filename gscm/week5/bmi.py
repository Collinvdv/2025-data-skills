# Calculcate BMI 
# formula: weight (in kg ) / (height * height)
# I WANT YOU TO CREATE A FUNCTION CALLED calculateBmi 
# 2 parameters weight and height
# return the calculcated bmi

# 2 variables weight, height
# print out the bmi
# height 1.94, weight 86
# result 22.85

def calculateBMI(h, w):
    return w / (h * h)

weight = float(input("give your weight"))
height = float(input("give your height"))
bmi = calculateBMI(height, weight)
print(bmi)