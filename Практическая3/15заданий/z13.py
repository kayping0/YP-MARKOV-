a = int(input("Введите a: "))
b = int(input("Введите b: "))
if a<b:
    x= 2*a+2*b
elif a>b:
    x=a-b+1
elif a==b:
    x=b*b
else:
    print("x не найдено")
print("x=", x)