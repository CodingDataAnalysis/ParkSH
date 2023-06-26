import sys

N,M = list(map(int ,sys.stdin.readline().split()))
dic = {}
for i in range(1,N+1):
    dic[sys.stdin.readline().rstrip()] = i
res = []
for j in range(M):
    a = sys.stdin.readline().rstrip()
    if dic.get(a):
        res.append(a)
print(len(res))
for k in sorted(res):
    print(k)


#%%
