import sys
import itertools

N,K =list(map(int,(sys.stdin.readline().split())))

a = [True for i in range(N)]
print(len(list(itertools.combinations(a,K))))
#%%
