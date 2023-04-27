import sys
import itertools


a = list(map(int, sys.stdin.readline().split()))

N = a[0]
M = a[1]

# 합이 M을 넘지 않는 카드 3장을 찾는다.

card = list(map(int,sys.stdin.readline().split()))

b=  list(itertools.permutations(card ,3))
maxe=0
for i in b:
    idx = sum(i)
    if idx<=M and maxe<idx:
        maxe = idx
print(maxe)


#%%
