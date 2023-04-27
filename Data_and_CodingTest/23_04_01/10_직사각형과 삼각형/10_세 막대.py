import sys

a = list(map(int,sys.stdin.readline().split()))

# 작은 두 변의 길이의 합이 제일 긴 변의 길이보다 커야 된다.

a = sorted(a)

res = a[0] + a[1] + min(a[2], a[0]+a[1]-1)
print(res)
#%%
