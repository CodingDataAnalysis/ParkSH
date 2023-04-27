import sys
import itertools


N = int(sys.stdin.readline())

print(len(list(itertools.permutations([1 for i in range(N)],2))))
#%%
