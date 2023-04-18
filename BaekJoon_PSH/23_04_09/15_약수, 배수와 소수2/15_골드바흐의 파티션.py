import sys
import math

def is_prime(N):
    a = [True for i in range(N+1)]
    a[0], a[1] = False, False
    for i in range(2, int(math.sqrt(N))+1):
        j = 2
        if a[i] == True:
            while True:
                if i*j > N:
                    break
                a[i*j] = False
                j += 1
    b = []
    for i in range(2, N+1):
        if a[i] == True:
            b.append(i)
    return b

T = int(sys.stdin.readline())
primes = is_prime(1000000)
for i in range(T):
    N = int(sys.stdin.readline())
    cnt = 0
    for p in primes:
        if p > N // 2:
            break
        if (N - p) in primes:
            cnt += 1
    print(cnt)
