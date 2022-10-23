from random import *
n = int(input("Введите длинну массива: "))
x = [randint(0,10) for i in range(n)]
print(x)
y = list(reversed(x))
print(y)
