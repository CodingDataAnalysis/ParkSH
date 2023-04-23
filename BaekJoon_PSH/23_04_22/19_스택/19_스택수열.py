import sys
from collections import deque

n = int(sys.stdin.readline())

a = deque()
b = deque()
idx_st = deque()
for i in range(n):
    c = int(sys.stdin.readline())
    a.append(c)
e =  0
for p in range(1, n+1):
    idx_st.append(p)
    print('+')
    while True:
        if len(idx_st)>0:
            idx = idx_st.pop()
        else:
            break
        if a[e] == idx:
            print('-')
            break
        e += 1





#%%
