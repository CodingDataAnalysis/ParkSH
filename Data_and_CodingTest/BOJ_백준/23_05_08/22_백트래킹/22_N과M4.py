import sys
import itertools

N,M = list(map(int,sys.stdin.readline().split()))

N = [i for i in range(1,N+1)]

a = list(itertools.combinations_with_replacement(N,M))

for i in a:
    print(*i)
#%%
