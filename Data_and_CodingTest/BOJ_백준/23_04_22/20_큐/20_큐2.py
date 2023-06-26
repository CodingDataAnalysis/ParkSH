import sys
from collections import deque

N = int(sys.stdin.readline())
c = deque()
res = []
for i in range(N):
    a= list(map(str, sys.stdin.readline().rstrip().split()))
    if a[0]=='push':
        c.append(int(a[1]))
    elif a[0] == 'pop':
        if len(c)==0:
            res.append(-1)
        else:
            res.append(c.popleft())
    elif a[0] =='front':
        if len(c)==0:
            res.append(-1)
        else:
            res.append(c[0])
    elif a[0] =='back':
        if len(c)==0:
            res.append(-1)
        else:
            res.append(c[-1])
    elif a[0] == 'size':
        res.append(len(c))
    elif a[0] == 'empty':
        if len(c)==0:
            res.append(1)
        else:
            res.append(0)

for i in res:
    print(i)
#%%
