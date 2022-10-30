from random import *
arr = [randint(0,10) for i in range(10)]
print(arr)
for j in range(0, len(arr)):
    for v in range(j+1, len(arr)):
        if(arr[j] == arr[v]):
            print(arr[j])