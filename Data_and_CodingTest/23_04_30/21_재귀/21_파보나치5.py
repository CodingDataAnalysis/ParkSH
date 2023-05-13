import sys

def Fibo(N):

    if N==0:
        return 0
    elif N==1:
        return 1
    else:
        return Fibo(N-2) + Fibo(N-1)

N = int(sys.stdin.readline())
print(Fibo(N))
# FIBO(0) + FIBO(1) = 1
# FIBO(2) = 1

# Fibo(5) = Fibo(3) + Fibo(4)

# Fibo(3) = Fibo(2) + Fibo(1)

# Fibo(4) = Fibo(3) + Fibo(2)
#%%
