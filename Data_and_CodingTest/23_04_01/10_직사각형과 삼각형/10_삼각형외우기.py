import sys

A =[]
for i in range(3):
    a = int(sys.stdin.readline())
    A.append(a)
# print(set(A))
# print(len(set(A)))
# if set(A)==60:
#     print('good')
if len(set(A))==1 and 60 in set(A) :
    print('Equilateral')
elif sum(A)==180 and len(set(A))==2:
    print('Isosceles')
elif sum(A)==180 and len(set(A))==3:
    print('Scalene')
elif sum(A)!= 180:
    print('Error')


#%%
