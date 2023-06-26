import itertools
import sys

def fact(N):
    if N==0:
        return 1
    else:
        return N*fact(N-1)
T =int(sys.stdin.readline())
res = []
for i in range(T):
    N=sorted(list(map(int,sys.stdin.readline().split())))
    # print(fact(N[1])//(fact(N[0]) * fact(N[1]-N[0])))
    print(fact(N[1])//(fact(N[0]) * fact(N[1]-N[0])))
#%%
