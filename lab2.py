import math

x=int(input("Введите переменную x:"))
y=int(input("Введите переменную y:"))
z=((9*math.pi*y+10*math.cos(x))/(math.sqrt(y)-math.fabs(math.sin(y))))*math.pow(math.e,x)
print("z= {0:.2f}".format(z))


