import random
arr, arr1 = [], []
for i in range(15):
    arr.append(random.randrange(-10, 30))
    arr1.append(arr[i])
    if arr[i] < 10:
        arr1[i] = 0
    if arr[i] > 20:
        arr1[i] = 1
print('Исходнный массив: ', arr,'\nИзменённый массив: ', arr1)