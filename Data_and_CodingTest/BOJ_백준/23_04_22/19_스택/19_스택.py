import sys
from collections import deque

A = deque()

N = int(sys.stdin.readline())

for i in range(N):
    a = list(map(str , sys.stdin.readline().rstrip().split()))
    if a[0] == 'push':
        A.append(a[1])
    elif a[0] == 'pop':
        if len(A)<1:
            print(-1)
        else:
            print(A.pop())
    elif a[0] == 'top':
        if len(A)<1:
            print(-1)
        else:
            print(A[-1])
    elif a[0] == 'empty':
        if len(A)<1:
            print(1)
        else:
            print(0)
    elif a[0] == 'size':
        print(len(A))


#%%
