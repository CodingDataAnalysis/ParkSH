import sys
import math

n = int(sys.stdin.readline())

a= [True for i in range(n+1)]
# a = [False , False , True , True , False , True]
a[0] ,a[1] =False , False

i = 2
for i in range(2,int(math.sqrt(n))+1):
    j=1
    while True:
        if i*j>n:
            break
        if a[i*j] == True and j!= 1:
            a[i*j] = False
        j+=1

res = []
for i in range(n):
    if a[i]==True:
        res.append(i)
print(res)



#%%
