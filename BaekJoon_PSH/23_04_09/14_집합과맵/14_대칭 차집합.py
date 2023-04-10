import sys

A_cnt , B_cnt = list(map(int,sys.stdin.readline().split()))

A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

print(len(list(set(A)-set(B))) +len(list(set(B)-set(A))))
#%%
