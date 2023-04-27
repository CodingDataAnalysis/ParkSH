import sys

n = int(sys.stdin.readline())
result = 0
for i in range(1,n):
    result += i * (i - 1) // 2

print(result , 3 , sep='\n')
#%%
