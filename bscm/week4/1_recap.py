firstname = "Collin"
age = 33
isMarried = True 
height = 1.94 
courses = ["Data skills", "Web programming"]
print(courses[0])

# count from 14 till 19 
for x in range(14,20):
    print(x)

# alle even getallen tussen 4301 en 4444
# I: startpunt? 4301
# I: eindpunt? 4444
start = int(input("Startpunt?"))
eind = int(input("eind?"))

for nummertjeXOXO in range(start,eind):
    if nummertjeXOXO % 2 == 0:
        print(nummertjeXOXO)