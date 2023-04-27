import sys

# 에라토스테네스의 체를 이용하여 n 이하의 소수를 구하는 함수
def is_prime(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if primes[i] == True:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes


# 골드바흐의 파티션을 구하는 함수
def goldbach_partition(n, primes):
    cnt = 0
    k = 0
    for p in primes:
        if p:
            if primes[n-k] and n-k>=k:
                cnt+=1
            if n-k<0:
                return cnt
        k+=1
primes = is_prime(1000001)
T = int(sys.stdin.readline())
res = []
for i in range(T):
    N = int(sys.stdin.readline())
    res.append(goldbach_partition(N, primes))
for p in res:
    print(p)
#%%
