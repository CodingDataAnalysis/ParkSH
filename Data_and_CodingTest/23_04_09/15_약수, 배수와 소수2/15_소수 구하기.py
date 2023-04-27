import sys
import math

M,N = list(map(int,sys.stdin.readline().split()))

a = [True for i in range(N+1)]


a[0],a[1] = False , False

for i in range(2, int(math.sqrt(N)+1)):

    j=2
    if a[i]== True:
        while True:
            if i*j> len(a)-1:
                break

            if a[i*j] == True:
                a[i*j]= False

            j+=1

for i in range(M,N+1):
    if a[i] == True:
        print(i)

#%%
