firstname = "Collin"
lastname  = "Van der Vorst"
fullname = firstname + " " + lastname
age = 33
height = 1.94
isAwesome = True
children = ["Boris", "Renske"]
print(children[0])
print(children[1])

for kiddo in children:
    print(kiddo)

def printList(list):
    if len(list) > 0:
        for item in list:
            print(item)
    else:
        print("No items in list")

printList(children)

password = input("give me your password")
secretpassword= "ilovecollinxoxo"

while (password != secretpassword):
    print("Het komt niet overeen")
    password = input("give me your password")

print("joepie ik ben in het systeem")