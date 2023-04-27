import sys
from sympy import Integral,  Symbol , pprint

x = Symbol('x')
f = 2 * x**2

a =  list(map(int ,sys.stdin.readline().split()))
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

def O(a,c,n0):
    n = n0
    fn = a[0]*n + a[1]
    c = c
    if c*n-fn >= 0 and c>=a[0]:
        print(1)
    else:
        print(0)
O(a,c,n0)
#O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인
# 양의 상수 c와 n0가 존재한다}

#7 7
#8
#1

#f(n) = 7n + 7
#g(n) = n
#c = 8
#n0 =1

#f(1) = 14 c*g(1) = 8 , n>=1


#7 7
#8
#10

#f(n) = 7n + 7
#g(n) = n
#c = 8
#n0 = 10

#f(10) = 77  , c*g(10) = 80 , n>=10
#%%
