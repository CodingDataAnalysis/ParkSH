import sys
import heapq


N = int(sys.stdin.readline())

res = []
for i in range(N):
    num = int(sys.stdin.readline())

    heapq.heappush(res , (num , num))
while res:
    print(heapq.heappop(res))
while res:
    print(heapq.heappop(res)[1])
#%%
