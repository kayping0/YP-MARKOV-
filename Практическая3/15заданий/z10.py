k=int(input("Введите k: "))
c=int(input("Введите c: "))
if k<5 and c>4:
    X = k+c**2
elif k>c and k>3:
    X= c**2+2
else:
    X = c-1
print("X= ", X)