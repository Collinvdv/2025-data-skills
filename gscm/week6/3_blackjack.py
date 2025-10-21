# Rules
# random cards will be given 
# if heigher then 21, you will broke 
# if lower then 16 you need to ask a new card 

# O: HELLO WELCOME TO BLACKJACK 
# O: We start with you, say stop when you don't want new cards 
# O: CARD 9
# I: NEW
# O: CARD 3
# I: NEW
# O: 5
# I: STOP
# O: Your total now is 17
import random

# Say hello
print("HELLO WELCOME TO BLACKJACK ")
print("We start with you, say stop when you don't want new cards ")

# User card logic 
cmd = input("Give me a commando choose between STOP or NEW")
userTotal = 0

# Give cards untill they stop 
while cmd != "stop":
    # give new card logic 
    newCard = random.randint(1,11)
    userTotal += newCard
    print(newCard)

    # Ask a new command to the user
    print(f"Your current total is {userTotal}")
    if userTotal > 21: 
        cmd = "stop"
        print("Game over, more then 21")
    elif userTotal < 16:
        cmd = "new"
        print("It is lower than 16, so I must give you a new card")
    else:
        cmd = input("Give me a commando choose between STOP or NEW")

if userTotal < 21:
    print("Let see what the pc does")

    pcTotal = 0;

    while pcTotal < 16: 
        newCard = random.randint(1,11)
        print(f"The pc draw the card {newCard}")
        pcTotal += newCard

    print(f"The pc total is {pcTotal}")

    if  pcTotal > 21:
        print("user won")
    elif pcTotal > userTotal:
        print("pc won")
    elif pcTotal == userTotal:
        print("draw")
    else:
        print("user won")