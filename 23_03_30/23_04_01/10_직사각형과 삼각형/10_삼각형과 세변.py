import sys

res = []
while True:
    a = list(map(int, sys.stdin.readline().split()))

    if a == [0,0,0]:
        break
    else:

        a = sorted(a)
        if a[2] >= a[0]+a[1]:
           res.append('Invalid')
        elif len(set(a))==1:
            res.append('Equilateral')
        elif len(set(a))==2:
            res.append('Isosceles')
        elif len(set(a))==3:
           res.append('Scalene')




for i in res:
    print(i)

#%%
