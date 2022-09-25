a=int(input("Введите число 'a': "))
b=int(input("Введите число 'b': "))
if a<b:
	C=a+b
elif a>b and a>3:
	C=b**2 -b
else:
	C=b**2-1
print("C=",C)
