import sys

N = int(sys.stdin.readline())

A ,B= [],[]
for i in range(N):
    a = list(map(int,sys.stdin.readline().split()))
    A.append(a[0])
    B.append(a[1])

print( (max(A)-min(A)) * (max(B)-min(B)))

#%%
