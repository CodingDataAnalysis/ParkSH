import sys
import heapq

N = int(sys.stdin.readline())

res = []
for i in range(N):
    a,b = list(map(int, sys.stdin.readline().split()))

    heapq.heappush(res , (b,a))

while res:
    a = heapq.heappop(res)
    print(a[1] , a[0])
#%%
