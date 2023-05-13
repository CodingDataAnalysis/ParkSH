import sys
import itertools

N,M = list(map(int,sys.stdin.readline().split()))

# 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열
N = [i for i in range(1,N+1)]

a= list(itertools.permutations(N,M))

for i in a:
    print(*i)

#%%
