import math
# 1. Написати програму, яка обчислюватиме значення функції у залежності від значення аргументу: 𝑓(𝑥)
x = float(input("x = "))


if  x >= 3.7:
    print(x+math.sqrt(x)+math.pow(4*x+7, 1/3))
elif x < 3.7 and x > -1.5:
    print(math.tan(x) + math.pow(x,2))
elif x <= -1.5 :
    print(abs(x))
    