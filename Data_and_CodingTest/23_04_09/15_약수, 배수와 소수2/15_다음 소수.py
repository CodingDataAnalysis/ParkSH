import sys
import math

T = int(sys.stdin.readline())
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

for k in range(T):
    n = int(sys.stdin.readline())
    while True:
        if is_prime(n):
            print(n)
            break
        else:
            n+=1

#%%
