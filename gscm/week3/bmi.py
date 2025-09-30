# Calculcate BMI 
# formula: weight (in kg ) / (height * height)
# 2 variables weight, height
# print out the bmi
# height 1.94, weight 86
# result 22.85

# Underweight (BMI < 18.5)
# Healthy Weigh (BMI between 18.5 and 25)
# Overweight (BMI > 25)
# OBESEEEEE (BMI > 30)
weight = float(input("What is your weight?"))
height = float(input("What is your height?"))
bmi = weight / (height * height)

if bmi < 18.5:
    print ("Underweight")
elif bmi < 25:
    print("healthy")
elif bmi < 30:
    print("overweight")
else:
    print("OBESEEEE")