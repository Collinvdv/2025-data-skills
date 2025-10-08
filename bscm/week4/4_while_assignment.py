# The computer chooses a secret number between 1 and 100.
# The user has to guess until it’s correct.
# After each wrong guess → print "Lower.Try again!" OR Higher.
# When correct → print "Well done!".

secretnumber = 55

usernumber = int(input("What is the number?"))

while secretnumber != usernumber:
    if usernumber > secretnumber:
        print("Lager")
    else:
        print("Hoger")
    
    usernumber = int(input("What is the number?"))

print("Well done!")