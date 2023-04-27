import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(1, n):
    cnt += (n-i)
print(cnt , 2 , sep='\n')