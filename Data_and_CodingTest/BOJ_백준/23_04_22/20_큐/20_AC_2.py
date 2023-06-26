import sys
from collections import deque
import copy

T = int(sys.stdin.readline())
for pp in range(T):
    N = list(map(str , sys.stdin.readline().rstrip()))

    n = int(sys.stdin.readline())
    a = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    # print(a)
    # print(len(a))
    if n==0:
        a = []
    flag = 0
    for stt in N:
        if stt == 'R':
            flag+=1
            # print(b)
        else:
            if len(a)<1:
                print('error')
                break
            else:
                if flag%2 ==0:
                    a.popleft()
                else:
                    a.pop()
    else:
        if flag%2==0:
            print("[" + ','.join(map(str,a)) + "]")
        else:
            a.reverse()
            print("[" + ','.join(map(str,a)) + "]")

#%%
