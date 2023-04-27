import sys
import heapq

N = int(sys.stdin.readline())
res = []
for i in range(N):
    a = list(map(str , sys.stdin.readline().rstrip().split()))
    heapq.heappush(res , (int(a[0]) ,i , a[1]))

res.sort(key = lambda x : (x[0] , x[1]))
# print(res)
for i in res:
    print(i[0] , i[2])
#%%
