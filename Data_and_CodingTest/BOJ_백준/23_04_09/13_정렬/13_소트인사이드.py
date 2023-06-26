import sys

A = list(sys.stdin.readline().rstrip())

A = sorted(list(map(int , A)) , reverse= True)
print("".join(map(str, A)))

#%%
