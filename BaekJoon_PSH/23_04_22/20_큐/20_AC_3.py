import sys
from collections import deque

T = int(sys.stdin.readline())

for t in range(T):
    p = str(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    x = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    if n == 0:
        x= []
    flag = 0
    for i in p:

        if i == 'R':
            flag+=1
        else:
            if len(x)==0:
                print('error')
                break
            if flag%2 == 0:
                x.popleft()
            else:
                x.pop()
    else:
        if flag%2 == 1:
            print("[" + ",".join(map(str , reversed(x))) + "]")
        else:
            print("[" + ",".join(map(str , x)) + "]")


#%%
