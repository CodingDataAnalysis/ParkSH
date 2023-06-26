import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    gae , chul = list(map(int,sys.stdin.readline().split()))
    idx = list(map(int , sys.stdin.readline().split()))
    gae = [i for i in range(gae)]

    res = deque()
    cnt = 0
    for i,v in enumerate(idx):
        res.append([v , i])
    while True:
        maxe = max(res)[0]
        idx = res.popleft()

        if maxe == idx[0]:
            cnt +=1
            if idx[1] == chul:
                print(cnt)
                break
        else:
            res.append(idx)




#%%
