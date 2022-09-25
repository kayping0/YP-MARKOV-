f=int(input("Введите число 'f': "))
k=int(input("Введите число 'k': "))
if f<5 and k>2:
	R=f+k-1
elif k<2:
	R=k**2
elif k==2:
	R=1
else:
	print("Переменная R не найдена")
print("R=",R)
