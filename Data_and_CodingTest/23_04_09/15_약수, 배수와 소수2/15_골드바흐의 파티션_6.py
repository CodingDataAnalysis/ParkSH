from sys import stdin
import math

arr = [True]*(1000001)
arr[0],arr[1] = False,False

for i in range(2, int(math.sqrt(len(arr)))+1):
    j=2
    if arr[i]:
        while i*j<=len(arr)-1:
            arr[i*j] = False
            j+=1
T = int(stdin.readline())
for i in range(T):
    n = int(stdin.readline())
    count = 0
    for j in range(2, n//2+1):
        if arr[j] and arr[n - j]:
                count += 1
    print(count)

#%%
