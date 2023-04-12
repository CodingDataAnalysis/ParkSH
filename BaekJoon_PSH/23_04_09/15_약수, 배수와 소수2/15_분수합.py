import sys
import math

mo =[]
za = []
for i in range(2):
    A,B = list(map(int,sys.stdin.readline().split()))
    za.append(A)
    mo.append(B)

gcd2 = math.gcd(mo[0],mo[1])

lcm = mo[0]*mo[1]//gcd2

za = za[0]*(lcm//mo[0]) + za[1]*(lcm//mo[1])

gcd3 = math.gcd(lcm , za)
print(za//gcd3 , lcm//gcd3)

#%%
