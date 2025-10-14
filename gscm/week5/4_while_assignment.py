# The computer chooses a secret number between 1 and 100.
# The user has to guess until it’s correct.
# After each wrong guess → print "Lower.Try again!" OR Higher.
# When correct → print "Well done!".

secretNbr = 50
# userNbr = int(input("Give me a number")) # 10

# while secretNbr != userNbr:
#     if (userNbr < secretNbr):
#         print("guess higher")
#     else: 
#         print("guess lower")

#     userNbr = int(input("Give me a number")) # 10

# print("Correct!")

while(True): 
    userNbr = int(input("Give me a number")) # 10

    if (userNbr == secretNbr):
        print("Correct!")
        break
    elif (userNbr < secretNbr):
        print("aim higher")
    else:
        print("aim lower")