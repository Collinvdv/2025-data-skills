# scenario 1: ask for the age, when they are between 18 - 65,
# scenario 2: sausage fest, a lot of problems, we need girlpower

# case 1
# I: What is your age? 18
# I: What is your gender? f
# O: enter

# case 1.2
# I: What is your age? 18
# I: What is your gender? m
# O: don't enter

# case 2
# I: What is your age? 70
# I: What is your gender? f
# O: Don't enter

# case 3
# I: What is your age? 14
# I: What is your gender? m
# O: Don't enter
age = int(input("What is your age?"))
gender = input("What is your gender")
bribeMoney = int(input("What is your age?"))

# solution 1
if (age >= 18 and age <= 65 and gender == "f") or bribeMoney >=15:
    print("enter")
else:
    print("Don't enter")

# solution 2
if age >= 18 and age <= 65 and gender == "f":
    print("enter")
elif bribeMoney >= 15:
    print("enter")
else:
    print("Don't enter")

# solution 3
if age >= 18 and age <= 65:
    if gender == "f":
        print("enter")
    else:
        print("Don't enter")
else:
    if bribeMoney >= 15:
        print("enter")
    else:
        print("Don't enter")

# solution 4
if age > 65 or age < 18 or gender == 'm':
    if bribeMoney >= 15:
        print("enter")
    else:
        print("don't enter")
else:
    print("enter")