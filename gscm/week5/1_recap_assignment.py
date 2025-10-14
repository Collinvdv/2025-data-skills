# all even numbers between a start an end and end
# I: start? 4301
# I: end? 4444

# number = 7
# isEven = (7 % 2 == 0)
start = int(input("Start?")) # 4301
end = int(input("End?")) # 4444

if start < end:
    for number in range(start, end + 1):
        if (number % 2 == 0):
            print(number)
else: 
    for number in range(start, end - 1, -1):
        if (number % 2 == 0):
            print(number)