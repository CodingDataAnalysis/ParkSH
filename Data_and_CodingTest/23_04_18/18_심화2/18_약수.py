import sys

N = int(sys.stdin.readline())

# a = [14 ,26456 ,2 ,28 ,13228 ,3307 ,7 ,23149 ,8 ,6614 ,46298 ,56 ,4 ,92596]
a = list(map(int,sys.stdin.readline().split()))
print(min(a)*max(a))
#%%
