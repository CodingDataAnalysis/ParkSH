import sys
from sympy import Integral,  Symbol , pprint

a =  list(map(int ,sys.stdin.readline().split()))
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

n = Symbol('n')

def O(a,c,n0):
    n0 = n0
    fn = a[0]*n + a[1]
    gn = c*n0
    c= c
    if fn-gn>=0:
        print(fn-gn)
        print(1)
    else:
        print(0)
O(a,c,n0)
#%%
