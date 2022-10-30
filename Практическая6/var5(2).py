arr = []
arr_2 = []
for i in range(10):
   arr.append(int(input('Введите число: ')))
for j in arr:
   if j not in arr_2:
       arr_2.append(j)
print(arr_2)