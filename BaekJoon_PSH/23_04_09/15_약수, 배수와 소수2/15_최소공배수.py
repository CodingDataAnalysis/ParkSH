import sys
import math

T = int(sys.stdin.readline())
res = []
for i in range(T):
    A,B = list(map(int, sys.stdin.readline().split()))
    res.append(A*B//math.gcd(A,B))

for i in res:
    print(i)
#%%
