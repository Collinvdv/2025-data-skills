secretPassword = "Collintje"

userPassword = input("Give me password")
attempts = 1
isBlocked = False

while secretPassword != userPassword:
    if attempts == 5:
        isBlocked = True
        break
    
    userPassword = input("Wroooong, give me password")
    attempts += 1


if isBlocked == True:
    print("Not welcome, user is blocked")
else:
    print("Welcome")