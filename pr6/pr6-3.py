import math

a = float(input("a ==> "))
b = float(input("b ==> "))
h = float(input("h ==> "))

x = a
y = 0.0
lst = []


for i in range(20):
    if x > b:
        break
    y = x * math.sin(x) + math.pow(math.e, x)
    y= round(y,2)
    lst.append(y)
    x = x + h
    x = round(x, 1)

print("\n")
print(lst)
print("\n=============================\n")
lst.sort()
print(lst,"\n")


