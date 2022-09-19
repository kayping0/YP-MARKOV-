A=int(input("Введите целое число: "))
B=int(input("Введите целое число: "))
if A<B:
    for i in range(A, B + 1):
        print(i, end="; ")
else:
    for i in range(A, B-1, - 1):
        print(i, end="; ")
