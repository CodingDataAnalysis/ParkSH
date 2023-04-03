import sys

xx = list(map(int,sys.stdin.readline().split()))

a = xx[0]
b = xx[1]
c = xx[2]
d = xx[3]
e = xx[4]
f = xx[5]

for x in range(-999,1000):
    for y in range(-999,1000):
        if ( (a*x) + (b*y) == c) and ( (d*x) + (e*y) == f):
            print(x , y , end= '')
            break

#%%
