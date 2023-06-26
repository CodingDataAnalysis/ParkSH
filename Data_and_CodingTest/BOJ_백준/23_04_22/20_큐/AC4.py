import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):

    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    deq = deque(sys.stdin.readline().strip()[1:-1].split(','))


    txt = [p[i] for i in range(len(p))]
    flag = 0

    for j in txt:
        try:
            if j == "R":
                flag += 1
            elif j == "D":
                if flag % 2 == 0:
                    print(deq.popleft())
                    flag = 0
                    print('good')
                else:
                    deq.reverse()
                    deq.popleft()
                    flag = 0
        except:
            print("error")
            break

    if deq:
        print("[" + ', '.join(map(str, deq)) + "]")
#%%
