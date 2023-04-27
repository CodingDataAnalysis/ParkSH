import sys

N = int(sys.stdin.readline())


for i in range(1,N+1):

    if sum(map(int, str(i)) , i) == N:
        print(i)
        break
    if i == N:
        print(0)
        break

#%%
