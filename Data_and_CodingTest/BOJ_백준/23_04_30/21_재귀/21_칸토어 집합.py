import sys
import math

def cantor(n):
    if n == 0:
        return ['-']
    prev = cantor(n - 1)
    new = prev + [' '] * len(prev) + prev
    return new

while True:
    try:
        k = int(sys.stdin.readline())
        print(''.join(cantor(k)))
    except:
        break

#%%
