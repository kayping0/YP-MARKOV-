v=int(input("Введите число 'v': "))
k=int(input("Введите число 'k': "))
if v<k:
	Z=v-k+1
elif k>v:
	Z=k**2-v**2
else:
	Z=k**2 -k
print("Z=",Z)
