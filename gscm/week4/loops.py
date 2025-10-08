# COUNT FROM 1 till 10
for number in range(50, 101, 3):
    print(number)


for number in range(10, 0, -1):
    print(number)


# all the numbers that are divisible by 7 between 66 and 122
# number % 7, if the remainder is 0 
for number in range(66,123): 
    if number % 7 == 0:
        print(number)

goats = ["T-rex", "Connie", "Clyde"]
print(goats[0])
print(goats[1])
print(goats[2])

for goat in goats:
    print(goat)

for goatIndex in range(0, len(goats)):
    print(goats[goatIndex])

grades = [8, 14, 20, 6]
total = 0

# calculate the average of grades 
for grade in grades: 
    total += grade

avg = total / len(grades)

avg = sum(grades) / len(grades)
print(avg)










# Count from 1 to 100

# Count from 50 to 100 

# Count from 100 to 50 

# Only even numbers (you will need %)

# only the numbers that are divisble by 7

# loop over arrays 

# Only the people that passed

# Calculate the average 

