import sys
import heapq

N = int(sys.stdin.readline())

res = []
for i in range(N):
    a,b = list(map(int,sys.stdin.readline().split()))
    heapq.heappush(res , (a,b))

while res:
    print(*heapq.heappop(res))

#%%
