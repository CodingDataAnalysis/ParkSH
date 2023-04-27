import sys
from collections import deque

N,K  = list(map(int , sys.stdin.readline().split()))

a = deque(i for i in range(1,N+1))
res = []
while a:

    for i in range(K-1):
        a.append(a.popleft())
    res.append(a.popleft())

print(f'<{", ".join(map(str , res))}>')


#%%
