import sys
from collections import deque

N = int(sys.stdin.readline())

a = deque(i for i in range(1,N+1))

for i in range(len(a)-1):
    a.popleft()
    a.append(a.popleft())

print(a[0])
