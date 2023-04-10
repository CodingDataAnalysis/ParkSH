import sys

N = list(map(int,sys.stdin.readline().split()))
S = { sys.stdin.readline().rstrip() for i in range(N[0])}

cnt = 0
for j in range(N[1]):
    if sys.stdin.readline().rstrip() in S:
        cnt+=1
print(cnt)

#%%
