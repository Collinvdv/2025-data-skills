firstname = input("Give me your firstname") # string
lastname = "Van der Vorst"
fullname = firstname + " " + lastname # concat
fullname = f"{firstname} {lastname}"

age = int(input("What is your age")) # integer or int 
height = 1.93 # float
isMarried = True # boolean 

age = age + 1
age += 1
++age

age = age % 2 

if isMarried == True: 
    print("Congrats, you are married")
elif age < 30:
    print("You are pretty young, plenty of time")
else:
    if height < 1.4 and firstname == 'Plop':
        print("You are a dwarf go to the forest to find a partner")
    else:
        print("Find a partneeeer")