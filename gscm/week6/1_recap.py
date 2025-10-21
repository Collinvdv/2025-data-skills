firstname = "Collin"
age = 34
height = 1.94
lastname = input("give me your lastname")
isMarried = True
children = ["Boris", "Renske"]
print(children[0])
print(len(children))

for i in range(1,11):
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
    
for child in children:
    print(child)

cmd = input("Say something")

while cmd != "stop":
    cmd = input("Say something else")

print("congrats you typed stop")


def mergeWords(word1, word2):
    return word1 + " " + word2

fullname = mergeWords(firstname, lastname)