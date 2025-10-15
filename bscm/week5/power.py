# def powerTo en dat mag een base number hebben en exponent
# return het resultaat 

# powerTo(2,3) # 8
# powerTo(2,4) # 16
# 2 ^ 3 ====> 2 ** 3

# I: give me the base number? 2
# I: give me the exponent? 3
# O: 8

base = int(input("give me the base number?"))
exponent = int(input("give me the exponent number?"))

def powerTo(b, e):
    return b ** e

print(powerTo(base, exponent))