import sys
import math
import itertools


a = [True for i in range(10000+1)]
a[0], a[1] = False, False
for i in range(2, int(math.sqrt(n))+1):
    j = 2
    if a[i]:
        while True:
            if i*j > n:
                break
            a[i*j] = False
            j += 1

T = int(sys.stdin.readline())
for p in range(T):
    n = int(sys.stdin.readline())

    t = list(itertools.combinations_with_replacement(primes, 2))
    d = list(filter(lambda x: sum(x) == n , t))
    print(len(d))
#%%
