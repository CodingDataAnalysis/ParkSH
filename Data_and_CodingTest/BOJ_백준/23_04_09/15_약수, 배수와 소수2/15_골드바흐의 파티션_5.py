import sys
import math

def is_prime(n):
    array = []
    for i in range(n+1):
        array.append(True)
    #print("array_1 : {}".format(array))
    array[0] , array[1] = False, False
    for j in range(2 , int(math.sqrt(n))+1):
        if array[j] == True:
            k =2
            while (j*k <= n):
                if array[j*k] == True:
                    array[j *k] = False
                k+=1
    return array

# 에라토스테네스의 체를 이용하여 n 이하의 소수를 구하는 함수
# def is_prime(n):
#     a = [True]*(n+1)
#     a[0], a[1] = False , False
#     for i in range(2,int(math.sqrt(2*n))+1):
#         j=2
#         if a[i]==True:
#             while True:
#                 if i*j> len(a)-1:
#                     break
#                 a[i*j]=False
#                 j+=1
#     return a

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
