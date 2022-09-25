a = int(input("Введите a: "))
b = int(input("Введите b: "))
if a<2 and b>3:
    C= a+b*b
elif a>b and a>3:
    C=b*b+2
else:
    C=b
print("C=", C)