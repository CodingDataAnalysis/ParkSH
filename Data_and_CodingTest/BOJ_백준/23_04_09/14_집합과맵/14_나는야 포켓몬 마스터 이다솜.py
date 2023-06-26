import sys

N , M = list(map(int,sys.stdin.readline().split()))

dic = {}
dic2 = {}
for i in range(1,N+1):
    a = sys.stdin.readline().rstrip()
    dic[i] = a
    dic2[a] = i
res =[]
for j in range(M):
    a = sys.stdin.readline().rstrip()
    if a.isnumeric():
        res.append(dic.get(int(a)))

    else:
        res.append(dic2.get(a))
for i in res:
    print(i)
# print(dic.get(1))
# print(dic2.get('bul1'))
#%%
