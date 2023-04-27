import sys
import math

res = []
def is_prime(n):


    a = [True]*(2*n+1)
    a[0], a[1] = False , False
    for i in range(2,int(math.sqrt(2*n))+1):
        j=2
        if a[i]==True:
            while True:
                if i*j> len(a)-1:
                    break
                a[i*j]=False
                j+=1
    # idx = 0
    # cnt = 0
    # res2=[]
    sum = 0
    for i in range(n+1, len(a)):
        if a[i] == True:
            sum+=1 #sum에 소수인거만 더하기
    return sum
    #print(a[n+1:2*n+1].count(True))

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print(is_prime(n))




#     for j in a:
#         if idx>n and idx<=2*n:
#             if j == True:
#                 cnt+=1
#                 # res2.append(idx)
#         idx+=1
#     res.append(cnt)
#     # print(res2)
# for k in res:
#     print(k)
#%%
