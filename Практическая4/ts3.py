A=int(input("Введите целое число: "))
B=int(input("Введите целое число: "))
for i in range(A, B-1, - 1):
    if(i % 2 != 0):
        print(i, end="; ")