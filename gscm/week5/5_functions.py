def sayHelloFullname(fn, ln):
    fullname = fn + " " + ln
    print("Hello " + fullname)

def power2(number):
    return number * number

fn1 = "Collin"
ln1 = "Van der Vorst"

fn2 = "Sharon"
ln2 = "Van der Vorst"

sayHelloFullname(fn1, ln1)
sayHelloFullname(fn2, ln2)

print(power2(5))
result = power2(25)
print(result)