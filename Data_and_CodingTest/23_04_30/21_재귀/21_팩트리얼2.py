import sys

def fact(N):

    if N == 1 or N==0:
        return 1
    else:
        return N*fact(N-1)

n = int(sys.stdin.readline())
print(fact(n))

#%%
