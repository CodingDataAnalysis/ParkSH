import sys
import heapq

N = int(sys.stdin.readline())

res = []
for i in range(N):
    a = int(sys.stdin.readline())
    heapq.heappush(res , a)

while res:
    print(heapq.heappop(res))
#%%
