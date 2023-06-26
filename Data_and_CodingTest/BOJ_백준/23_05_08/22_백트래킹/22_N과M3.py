import sys
import itertools

N,M = list(map(int,sys.stdin.readline().split()))


N = [i for i in range(1,N+1)]

a = list(itertools.product(N,repeat =M))

for i in a:
    print(*i)
#%%
