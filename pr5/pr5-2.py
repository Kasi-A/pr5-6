# 2. Написати програму, яка обчислить середнє число з трьох цілих чисел, заданих з клавіатури. 
a = int(input("1 => "))
b = int(input("2 => "))
c = int(input("3 => "))

if b<=a<=c or c<=a<=b:
    print(a)
elif a<=b<=c or c<=b<=a:
    print(b)
else:
    print(c)