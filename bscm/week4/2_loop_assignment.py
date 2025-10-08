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
# base = int(input("Give me base nbr"))

# for multiply in range(1,11):
#     result = base * multiply
#     print(f"{base} x {multiply} = {result}")





# Use a loop to find 
#the maximum number in a list [3, 7, 2, 9, 4].
def geefMaximumGetal(numbers):
    maximum = numbers[0]

    for number in numbers: 
        if number > maximum:
            maximum = number

    return maximum

list1 = [4, 10, -3, 99]
list2 = [19, 8, 2, 1]

print(geefMaximumGetal(list1))
print(geefMaximumGetal(list2))