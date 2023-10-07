def add(a, b):
    return(a+b)
def min(a, b):
    return(a-b)
def mn(a, b):
    return(a*b)
def dil(a, b):
    return(a/b)
def squr(a, b):
    return((a + b) ** 0,5)
def kv(a, b):
    return((a + b) ** 2)




print("Choose what I must to do: +, -, *, / , squr, ^ ")

choose = input("")
a = int(input("First numbber: "))
b = int(input("Second number: "))

if choose == '+':
    print("Result", add(a, b))
elif choose == '-':
    print("Result", min(a, b))
elif choose == '*':
    print("Result", mn(a, b))
elif choose == '/':
    print("Result", dil(a, b))
elif choose == 'squr':
    print("Result", squr(a, b))
elif choose == '^':
    print("Result", kv(a, b))
else:
    print("Errorrrrrrr")
