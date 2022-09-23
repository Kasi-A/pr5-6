import math

a = float(input("a ==> "))
b = float(input("b ==> "))
h = float(input("h ==> "))
print("\n")

x = a
y = 0.0
i = 0

while (x < b):
    y = x * math.sin(x) + math.pow(math.e,x)
    print(f"{i}\t{x}\t{y}")
    x = x + h
    i += 1
