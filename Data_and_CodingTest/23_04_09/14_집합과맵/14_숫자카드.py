import sys

N = int(sys.stdin.readline())

card = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())

card2 = list(map(int,sys.stdin.readline().split()))

res = [0]*20000001

for i in card:
    if res[i]==0:
        res[i] +=1
for i in card2:
    print(res[i] , end = ' ')

#%%
