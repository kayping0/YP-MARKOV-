f= int(input("Введите f: "))
v= int(input("Введите v: "))
if f<4 and v>6:
    S=f+v
elif v<6:
    S=v**2
else:
    S=2*v
print("S=", S)