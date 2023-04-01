import sys

X = list(map(int ,sys.stdin.readline().split()))

#(6,2) (10,3) # 현재 위치 (6,2) , 직사각형 가로 10 , 세로 3

# 10-6 , 3-2

garo = min(X[2]-X[0], X[0])
sero = min(X[3] - X[1],X[1])

print(min(garo,sero))
#%%
