import sys
from collections import Counter

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))
dic  = Counter(A)

for i in B:
    if dic.get(i):
        print(dic[i] , end = ' ')
    else:
        print(0, end= ' ')

#%%
