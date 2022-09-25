f = int(input("Введите f: "))
k = int(input("Введите k: "))
if f<k:
    R=f+k*k-1
elif k<2 and f==3:
    R=k*k
else: 
    R=f-1
print("R=", R)
