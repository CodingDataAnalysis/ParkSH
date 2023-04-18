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
    # b = []
    # for i in range(2, N+1):
    #     if a[i] == True:
    #         b.append(i)
    return a

# 주어진 정수를 두 소수의 합으로 나타내는 함수
def goldPartition(x):
    result = []
    for i in range(2, x//2+1):
        if is_prime(i) and is_prime(x-i):
            if not result:
                result.append(i)
                result.append(x-i)
            else:
                if result[1]-result[0] > x - 2*i:
                    result[0] = i
                    result[1] = x-i

    return result


T = int(sys.stdin.readline())
primes = is_prime(1000001) # 10,000 이하의 모든 소수를 미리 계산해둠
res = []
for i in range(T):
    N = int(sys.stdin.readline())
    pair = goldPartition(N)
    res.append(len(pair)) # 가능한 두 소수의 합의 개수를 결과 리스트에 추가

for i in res:
    print(i)

    #print(pair)



#%%
