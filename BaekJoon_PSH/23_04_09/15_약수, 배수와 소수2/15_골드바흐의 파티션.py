import sys
import math
import itertools

def is_prime(n):
    a = [True for i in range(n+1)]
    a[0], a[1]= False , False
    for i in range(2, int(math.sqrt(n))+1):
        j=2
        if a[i]==True:
            while True:
                if i*j>len(a)-1:
                    break
                a[i*j]=False
                j+=1
    res = []
    idx = 0
    for i in a:
        if i:
            res.append(idx)
        idx+=1
    t = list(itertools.combinations_with_replacement(res, 2))
    d = list(filter(lambda x: sum(x) ==n , t))
    return len(d)

T = int(sys.stdin.readline())
for p in range(T):
    n = int(sys.stdin.readline())
    # print(d)
    print(is_prime(n))
#%%
