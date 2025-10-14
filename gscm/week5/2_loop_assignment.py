# Multiplication table of 5

# I: 5
# O: 5 x 1 = 5
# O: 5 x 2 = 10
# O: 5 x 3 = 15
# O: 5 x 4 = 20
# O: 5 x 5 = 25
# O: 5 x 6 = 30
# O: 5 x 7 = 35
# O: 5 x 8 = 40
# O: 5 x 9 = 45
# O: 5 x 10 = 50
base = int(input("Give me a number"))

for multiplier in range(1, 11):
    result = base * multiplier
    #print(f"{base} x {multiplier} = {result}")
    print(str(base) + " x " + str(multiplier) + " = " + str(result))
    print(base, "x", multiplier, "=", result )