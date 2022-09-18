a=input("Введите цело число \n")
b=input("Введите цело число \n")
c=input("Введите цело число \n")
if a<b:
    if a<c:
        y=a
    else:
        y=c

else:
    if b<c:
        y=b
    else:
        y=c
print("Минимальное: ", y)