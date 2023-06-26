import sys
import heapq

res= []
for i in range(5):
    n = int(sys.stdin.readline())

    heapq.heappush(res , (n,i+1))
avg = 0
median = 0
j = 0
while res:
    a = heapq.heappop(res)
    print(a)
    j+=1
    if  j==3:
        median  = a[0]
    avg+=a[0]

print(avg//5)
print(median)




#%%
