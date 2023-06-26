import sys

S = sys.stdin.readline().rstrip()
n = len(S)
cnt = 0
substrings = set()

for i in range(n):
    for j in range(i+1, n+1):
        print(S[i:j])
        substrings.add(S[i:j])

cnt = len(substrings)
print(cnt)

#%%
