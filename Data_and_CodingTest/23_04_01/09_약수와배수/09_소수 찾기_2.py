import sys
import math

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
a= [True for i in range(1001)]
# a = [False , False , True , True , False , True]
a[0] ,a[1] =False , False

i = 2
for i in range(2,int(math.sqrt(len(a)))+1):
    j=1
    while True:
        if i*j>len(a)-1:
            break
        if a[i*j] == True and j!= 1:
            a[i*j] = False
        j+=1

cnt =0
for i in A:
    if a[i]== True:
        cnt+=1
print(cnt)



#%%
