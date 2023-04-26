import sys
from collections import deque

N,M = list(map(int , sys.stdin.readline().split()))

res = deque(map(int , sys.stdin.readline().split()))
A = deque(i for i in range(1,N+1))
cnt= 0
# print(A.index(res[0]))
while True:
    if len(res) == 0:
        break

    if A[0] == res[0]:
        A.popleft()
        res.popleft()

    elif len(A) - A.index(res[0]) >= A.index(res[0]):
        A.append(A.popleft())
        # print(A)
        cnt+=1
    else:
        A.appendleft(A.pop())
        # print(A)
        cnt+=1
print(cnt)

#%%
