import sys
from collections import deque
import copy
queue = deque()

T = int(sys.stdin.readline())
res_fin = []
for _ in range(T):
    B = list(map(int , sys.stdin.readline().split()))
    c = deque(map(int, sys.stdin.readline().split()))
    i = 0
    d = deque([v,i] for i,v in enumerate(c))
    res =[]
    res = []
    maxe = max(d)[0]

    while True:
        if len(d)==0:
            break
        else:
            maxe = max(d)[0]
            if d[0][0] == maxe:
                res.append(d.popleft())
            else:
                d.append(d.popleft())
    idx =0
    for k,p in res:
        idx+=1
        if p==B[1]:
            res_fin.append(idx)
for i in res_fin:
    print(i)

#%%
