import sys

N = int(sys.stdin.readline())


res = [0]*10001

for k in range(N):
    i = int(sys.stdin.readline())
    res[i]+=1

for k in range(10001):
    if res[k] != 0:
        for p in range(res[k]):
            print(k)
#%%
