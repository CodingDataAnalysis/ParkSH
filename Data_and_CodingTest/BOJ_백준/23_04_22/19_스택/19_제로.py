import sys
from collections import deque

K = int(sys.stdin.readline())

A = deque()

for i in range(K):
    a = int(sys.stdin.readline())
    if a == 0:
        A.pop()
    else:
        A.append(a)
print(sum(A))
#%%
