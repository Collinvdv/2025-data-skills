secretPassword = "Collintje"

userPassword = input("Give me password")
attempts = 1
isBlocked = False

while secretPassword != userPassword:
    userPassword = input("Wroooong, give me password")
    attempts += 1

    if attempts == 5:
        isBlocked = True
        break

if isBlocked == True:
    print("Not welcome, user is blocked")
else:
    print("Welcome")