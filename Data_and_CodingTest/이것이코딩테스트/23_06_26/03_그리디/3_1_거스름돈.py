import sys

c_500 , c_100 , c_50 , c_10 = 0,0,0,0


N = int(sys.stdin.readline())



c_500 = N//500
N = N - (500 * c_500)

c_100 = N//100
N-= (100*c_100)
c_50 = N//50
N-= (50*c_50)
print(N)
c_10 = N//10
N-= (10*c_10)

print(c_500 + c_100 + c_50 + c_10)

#%%
