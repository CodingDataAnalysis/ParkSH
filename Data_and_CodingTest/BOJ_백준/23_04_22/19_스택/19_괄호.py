import sys
from collections import deque


T = int(sys.stdin.readline())
A = deque()

# deque(str(sys.stdin.readline().rstrip()))
# while True:
#     if a.pop()==')'
for i in range(T):
    a = str(sys.stdin.readline().rstrip())
    while True:
        if '()' in a:
            a = a.split('()')
            a = "".join(map(str , a))

        else:
            break
    if len(a)<1:
        print('YES')
    else:
        print('NO')

#%%
