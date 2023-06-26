import heapq
import sys


N ,k = list(map(int, sys.stdin.readline().split()))

x = list(map(int,sys.stdin.readline().split()))



heapq.heapify(x)
# print(x)

for i in range(len(x)-k):
    heapq.heappop(x)

print(heapq.heappop(x))

#%%
