import sys
from collections import deque

N, M = list(map(int,sys.stdin.readline().split()))

queue_1 = deque(i for i in range(1,N+1))

res = deque(map(int,sys.stdin.readline().split()))
cnt = 0
while True:
    if len(res)==0:
        break
    if queue_1[0] == res[0]:
        queue_1.popleft()
        res.popleft()
    elif len(queue_1) - queue_1.index(res[0]) >= queue_1.index(res[0]):
        # 9 - 8 = 1 >= 8
        queue_1.append(queue_1.popleft())
        cnt+=1
    else:
        queue_1.appendleft(queue_1.pop())
        cnt+=1
print(cnt)
# 1 2 3 4 5 6 7 8 9 10

# 2 3 4 5 6 7 8 9 10 1

#==> 2 출력 ==> 1

# 3 4 5 6 7 8 9 10 1

#%%
